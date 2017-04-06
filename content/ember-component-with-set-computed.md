Title: Использование computed'ов c сеттерами внутри Ember.Component
Date: 2017-03-31 01:36
Tags: js, ember
Slug: ember-component-with-set-computed
Lang: ru
Category: Development
Authors: shamcode
Summary: Недавно натолкнулся на не совсем очевидно поведение компонентов в Ember

При использовании сеттеров в `Ember.Component` я сталкнулся с нетрививальным поведеним ember,
при передаче параметеров в компонент.

Смотри, например у тебя есть компонент:

```js
import Ember from 'ember';

const {
          computed
      } = Ember;

export default Ember.Component.extend( {
    required: computed( function() {
		alert( 'No overridden!' );
    } ),
    overridden: computed( 'required', {
  	    get( key ) {
  	        this.get( '_inner' );
  	    },
        set( key, value ) {
    	    this.set( '_inner', `${value}_${this.get( 'required' )}` );
        }
    } ),
    displayValue: computed.alias( 'overridden' )
} );
```

И вот так ты  его используешь:
```hbs
{{side-effect
  overridden='foo'
  required='bar'}}
```

Как думаешь, вылетит alert или нет? Можешь проверить себя на [ember-twiddle](https://ember-twiddle.com/470882bbad6757c7c700f183230b1a93).

А вот для меня было неожиданно, что вылетит.

Причём, если поменять порядок параметров при передаче в компонет, то не вылетит:

```hbs
{{side-effect
  required='bar'
  overridden='foo'}}
```

Помнить о порядке для именнованых параметров это так себе идея, поэтому будет радикально рефакторить, а точне полностью избавляться от `this.set`.
Для этого вынесем второй аргумент `this.set( ... )` в отдельный `Ember.computed`:

```js
import Ember from 'ember';

const {
          computed
      } = Ember;

export default Ember.Component.extend( {
    required: computed( function() {
		alert( 'No overridden!' );
    } ),
    displayValue: computed( 'required', 'overridden', function() {
        return `${this.get( 'overridden' )}_${this.get( 'required' )}`;
    } )
} );
```

И теперь все [работает как-надо](https://ember-twiddle.com/c8728eee37674763a4a50a8f5061bf50)!

Проверить, если ли у тебя похожий код можно с помощью линтера [ember-best-practices](https://github.com/chadhietala/ember-best-practices), для этого
даже отдельное правило есть: [no-side-effect-cp](https://github.com/chadhietala/ember-best-practices/blob/master/guides/rules/no-side-effect-cp.md)

Ну и на будущее - не используй `Ember.set` в внутри computed, это легко может привести к [эксепшену](https://github.com/emberjs/ember.js/blob/ee8ab348484421f254fe995c6f04f0d4a0859cfa/packages/ember-metal/lib/transaction.js#L74)