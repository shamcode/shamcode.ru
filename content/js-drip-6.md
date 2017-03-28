Title: Js Drip #6 Конструкторы в JavaScript
Date: 2015-01-27 23:08
Tags: links, js, jsdrip
Slug: js-drip6
Lang: ru
Category: Translations
Authors: shamcode
Summary: Вольный перевод JsDrip #6 Constructors in JavaScript

Вольный перевод [JsDrip #6 Constructors in JavaScript](http://adripofjavascript.com/blog/drips/constructors-in-javascript.html)

Не смотря на то, что конструкторы в JavaScript это мощный инструмент, мало кто ими пользуется.
(возможно из-за их [дурной славы](http://crockford.com/)). Но если ты реально хочешь научиться JavaScript, ты просто
обязан знать как они работают.

Что такое конструктор? Это обычная функция, используемая с оператором `new`, который показывает что будет создан объект
специального типа.

```js
// `Color` это конструктор
var red = new Color(255, 0, 0);
```

В примере `red` это новый объект `Color`. Но как это работает?

```js
function Color(r, g, b) {
    this.r = r;
    this.g = g;
    this.b = b;
}

var red = new Color(255, 0, 0);
```

Как видишь, конструктор `Color` берет свои аргумента и прикрепляет их к объекту `this`. Это из--за того, что вызов
конструктора с `new`, устанавливает `this` конструктора на объект, который будет возвращен new.

Код выше грубо говоря эквивалентен этом:

```
var red = {
    r: 255,
    g: 0,
    b: 0
};
```
Тогда зачем вообще использовать конструктор? На это есть несколько важных причин.

Первое, использование конструктора означает, что создаваемые объекты будут иметь похожую базовую структуру и ты
с меньшей вероятностью сделаешь ошибку, если бы вручную создавал целую кучу объектов.

Второе, использование конструктора помечает созданные объекты, как образец (*instance*) `Color`.

```js
var red = new Color(255, 0, 0);

var blue = { r: 255, g: 0, b: 0 };

// Выведет: true
console.log(red instanceof Color);

// Выведет: false
console.log(blue instanceof Color);
```

Это дает нам возможность проверять, объект нужного ли типа мы обрабатываем.

Третье, использование конструктора позволяет проще связывать специальные методы с прототипом конструктора и они
будут доступны для всех создаваемых с помощью это конструктора объектов.

```js
function Color(r, g, b) {
    this.r = r;
    this.g = g;
    this.b = b;
}

Color.prototype.getAverage = function () {
    var total = this.r + this.g + this.b;
    var avg = total / 3;
    return parseInt(avg, 10);
};

var red = new Color(255, 0, 0);
var white = new Color(255, 255, 255);

// Выведет: 85
console.log(red.getAverage());

// Выведет: 255
console.log(white.getAverage());
```

И самое главное **всегда** используй `new` когда вызываешь конструктор.  Иначе, конструктор может полностью
испоганить `this`, который случайно оказывался при вызове. В большинстве случаев `this` будет указывать на глобальный
объект (`window` в браузере или global в `Node`)

Поэтому принято отличать регистром имя конструктора, что бы было понятно, что его нужно использовать только вместе с `new`.

В следующей статье мы расскажем как снизить эту опасность при работе с конструктором.