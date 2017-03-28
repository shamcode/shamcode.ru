Title: Js Drip #4 Что такое Array?
Date: 2015-01-21 23:42
Tags: links, js, jsdrip
Slug: js-drip4
Lang: ru
Category: Translations
Authors: shamcode
Summary: Вольный перевод Js Drip#4 What is an Array?

Вольный перевод [Js Drip#4 What is an Array?](http://adripofjavascript.com/blog/drips/what-is-an-array.html)

Для опытного разработчика этот вопрос покажется простейшим, но в контексте JavaSript все гораздо интересней.

В общем, массив это список значений, которые могут быть получены с помощью целого числа как "ключа".
Список начинается с 0 и до конца. Если мы опишем массив в нотации объектов JavaScript, то он будет выглядеть так:

```js
fakeArray = {
    0: "value 1",
    1: "value 2"
}
```

Тебе не кажется, что мы кое-что пропустили? Ох, мы знаем. Это надоедливое свойство `length`.

```js
fakeArray = {
    0: "value 1",
    1: "value 2",
    length: 2
}
```

Это подозрительно похоже на массив. И как мы говорили раньше, работает точно так же, как и объект `arguments`.
Мы также упоминали, что он работает именно так "под капотом" движка JavaScript.

По-правде, в JavaScript массивы - это объекты специального типа, встроенные в язык. Это можно легко увидеть,
сравнивая поведения массивов и объектов.

```js
fakeArray = {
    0: "value 1",
    1: "value 2",
    length: 2
};

// Выведет "value 1"
console.log(fakeArray[0]);

realArray = ["value 1", "value 2"];
realArray.text = "some text";

// Выведет "some text"
console.log(realArray.text);
```

Как видишь, доступ к свойствам объекта осуществляется точно так же как и к массиву. И ты можешь добавлять свои
свойства в массив так же, как и для любого другого объекта.

Но что насчет специальных методов массива? Всяких там `indexOf`, `slice` и `sort`? Оказывается, что это просто функции,
добавленные к объекту массива. (Точнее они добавлены в прототип массива, но не будем забегать вперед)

```js
realArray = ["value 1", "value 2"];

// Выведет "0"
console.log(realArray.indexOf("value 1"));

realArray.indexOf = function() {
    return "I'll never tell.";
};

// Выведет "I'll never tell."
console.log(realArray.indexOf("value 1"));
```

Фактически, имея достаточно времени, мы можем переделать весь нативный функционал массивов на свой, основанный на
манипуляции с объектом.
Вот пример переделанного метода `push`:

```js
fakeArray = {
    length: 0,
    push: function (val) {
        // Добавим новое значение в объект
        // со следующим доступным ключом
        this[this.length] = val;

        // Изменим свойство length
        this.length = this.length + 1;

        // Возвращаем измененную длину
        return this.length;
    }
};

fakeArray.push("first value");
fakeArray.push("second value");

// Выведет "first value"
console.log(fakeArray[0]);

// Выведет "second value"
console.log(fakeArray[1]);
```

Но одну вещь мы не сможем переписать - удобный синтаксис для создания массива (квадратные скобки). Но мы всегда можем
использовать конструктор. По-сути, эти два варианта полностью эквиваленты.

```js
literalWay = ["value 1"];

constructorWay = new Array("value 1");
```

Если ты готов отказаться от использования нативного синтаксиса, то можешь полностью восстановить концепцию массивов
JavaScript, чтобы в итоге получить примерно такое:

```js
myCustomArray = new CustomArray("value 1");
```

Теперь ты знаешь (если не знал) как работают массивы в JavaScript.
