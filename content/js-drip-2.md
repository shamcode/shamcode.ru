Title: Js Drip #2 Произвольное количество параметров с объектом arguments
Date: 2014-12-25 23:44
Tags: links, js, jsdrip
Slug: js-drip2
Lang: ru
Category: Translations
Authors: shamcode
Summary: Вольный перевод JS Drip#2 Arbitrary Parameters with the arguments Object

Вольный перевод [JS Drip#2 Arbitrary Parameters with the arguments Object](http://us6.campaign-archive2.com/?u=2cc20705b76fa66ab84a6634f&id=c8f1074cb2)

В прошлый раз мы тебе рассказали про работу с аргументами по умолчанию. Это дает определенную гибкость при работе с
аргументами, но что делать, если тебе нужно в функции обрабатывать столько аргументов, сколько в неё было передано?
Например, нужна функция, которая складывает все переданные ей аргументы. Как это сделать?

```js
function addAll () {
    // Какой тут код?
}

// Должна вернуть 6
addAll(1, 2, 3);

// Должна вернуть 10
addAll(1, 2, 3, 4);
```

К счастью, JavaScript позволяет сделать это очень легко. Вся соль в объекте `arguments`.

Хоть объект `arguments` и не является массивом, но ведет себя как массив (читай: поддерживает индексацию и имеет
ссылку на связанную функцию), содержащий все аргументы, переданные функции.

```
function myFunc () {
    console.log(arguments[0], arguments[1]);
}

// Выведет "param1" и "param2"
myFunc("param1", "param2");
```

Узнав о `arguments`, ты можешь легко написать функцию сложения, обрабатывающую все переданне аргументы.

```js
function addAll () {
    var sum = 0;

    for (var i = 0; i < arguments.length; i++) {
        sum = sum + arguments[i];
    }

    return sum;
}

// Вернет 6
addAll(1, 2, 3);

// Вернет 10
addAll(1, 2, 3, 4);
```

Но есть одна проблема. Надеюсь, ты не забыл, что arguments это на самом деле не массив? Проверить можно так:

```js
function myFunc () {
    console.log(Array.isArray(arguments));
}

//Выведет 'false'
myFunc('param');
```

Так что это не массив. Ты спросишь: "%usernames%, а есть ли разница?" А мы тебе ответим: да. Он не поддерживает
привычные методы массива, т.е. всякие `push`,` pop`, `slice`, `indexOf` и тому подобный `sort`.

```js
function sortArgs () {
    // Это не сработает!
    sorted = arguments.sort()

    return sorted;
}
```

На это можно напороться, особенно если передавать содержимое `arguments` в другую функцию, которая ожидает реальный массив.
Решение дьявольски простое в реализации, но чуть сложнее в понимании:

```js
function sortArgs () {
    // Конвертируем объект arguments в реальный массив
    var args = [].slice.call(arguments);

    // Теперь работает!
    sorted = args.sort()

    return sorted;
}
```

Рассмотрим решение по шагам:

1. Мы создали пустой массив.
2. Мы использовали метод `slice` у этого массива.
3. Мы использовали метод `call`, что бы сказать `slice`, что он должен обработать объект arguments, а не пустой массив.

Вызов `slice` без указания начального индекса вернет исходный, не срезанный массив. В итоге получаем именно то, что и
хотели: реальный массив, содержащий все аргументы, переданные в функцию.