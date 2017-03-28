Title: JS Drip #3 Сортировка массива с Array#sort
Date: 2015-01-20 22:32
Tags: links, js, jsdrip
Slug: js-drip3
Lang: ru
Category: Translations
Authors: shamcode
Summary: Вольный перевод Js Drip #3 Reordering Arrays with Array#sort

Вольный перевод [Js Drip #3 Reordering Arrays with Array#sort](http://adripofjavascript.com/blog/drips/reordering-arrays-with-array-sort.html)

В прошлый раз мы упоминули `sort` - стандартный метод сортировки, доступный для всех массивов.
Он работает именно так, как и ожидается:

```js
// Получим [1, 2, 3]
[3, 2, 1].sort();

// Получим ["a", "b", "c"]
["c", "b", "a"].sort();

// Получим [1, 2, "a", "b"]
["b", 2, "a", 1].sort();
```

Ты можешь заметить, что сортировка производится с словарном порядке (сначала числа, потом буквы). Но что делать,
 если тебе нужно отсортировать массив по какому-то другому признаку? Например, сначала должна идти "лучшая" машина?
 Как раз для этого `sort` принимает в качестве аргумента твою функцию сравнения.

```js
var cars = [
    "Honda Civic",
    "Ford Taurus",
    "Chevy Malibu"
]

cars.sort(function(a, b) {
    // По умолчанию 0, т.е.
    // сортировать не нужно
    var returnVal = 0;

    // Если `a` это Chevy, отнимем 1
    // что бы поднять `a` "выше" в сортировке
    // потому что Chevys это круто.
    if (a.match(/Chevy/)) {
        returnVal = returnVal - 1;
    }

    // Если `b` это Chevy, добавим 1
    // что бы поднять `b` "выше" в сортировке
    if (b.match(/Chevy/)) {
        returnVal = returnVal + 1;
    }

    return returnVal;
});

// Выведет:
// ["Chevy Malibu", "Honda Civic", "Ford Taurus"]
console.log(cars);
```

Функция сравнения принимает два значения (`a` и `b` в примере) и возвращает число.

* Если она вернула отрицательно число, `a` будет ближе к началу массива
* Если она вернула положительно число, `a` будет ближе к концу массива
* И если `0`, то сортивки `a` и `b` не будет

Когда передается функция в `sort`, эта функция будет вызываться с разными аргументами до тех пор, пока массив не
будет отсортирован.

Важно, что если возвращается `0`, то это не гарантирует, что `a` и `b` будут оставлены с теми же индексами.
Это просто означает, что сортировка не нужна и объекты "равны" (точнее эквиваленты по тому признаку, по которому
происходит сортировка).

Движок JavaScript может оставить эти элементы на прежних местах, но это не является спецификацией языка.