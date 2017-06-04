Title: Эксперименты с transform-class-properties
Date: 2017-06-02 01:36
Tags: js
Slug: transform-class-properties
Lang: ru
Category: Development
Authors: shamcode
Summary: Недавно наткнулся на баг, который был вызван моим не знанием как на самом деле работает плагин для babel `transform-class-properties`. Ну и решил поэксперементировать

Есть такая фича [ES Class Fields & Static Properties](https://github.com/tc39/proposal-class-public-fields) и сейчас она находится в Stage-2.
Но руки чешутся и решил я её поисопльзовать. Получилось не очень. Точнее выглядит прикольно, удобно, но вот такой баг поймал:

```js
class Foo {
    constructor() {
        console.log( this.baz );
    }

    baz = 'default';
}

class Bar extends Foo {
    baz = 'Wow';
}

new Bar();
// Выведет в консоле 'default'
```

А ожидал я `Wow`... Но если немного поменять код:

```js
class Foo {
    constructor() {
        console.log( this.baz() );
    }

    baz() {
        return 'default';
    }
}

class Bar extends Foo {
    baz() {
        return 'Wow';
    }
}

new Bar();
// Выведет в консоле 'Wow'
```

А причина в том, что код с `instance property` транспилировался примерно в такой:

```js

class Foo {
    constructor() {
        this.baz = 'default';

        console.log(this.baz);
    }

}

class Bar extends Foo {
    constructor(...args) {
        var _temp;

        return _temp = super(...args), this.baz = 'Wow', _temp;
    }

}
```

Т.е. запись в поле `baz` шла после вызова родительского конструктора. 
Единственная опция `spec` плагина `transform-class-properties` не меняет ситуацию: вместо простого присваивание будет использовать `Object.defineProperty`;  
Использование статических переменных тоже не решает проблемы. 

Поэтому придётся использовать геттеры:

```js
class Foo {
    constructor() {
        console.log( this.baz );
    }

    get baz() {
        return 'default';
    }
}

class Bar extends Foo {
    get baz() {
        return 'Wow';
    }
}

new Bar();
// Выведет в консоль 'Wow'
```

Ссылка на [demo-репозиторий](https://github.com/shamcode/transform-class-properties-demo)



