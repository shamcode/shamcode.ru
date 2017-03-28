Title: JS Drip #1 Параметры по умолчанию в Javascript
Date: 2014-12-22 22:56
Tags: links, js
Slug: js-drip1
Lang: ru
Category: Translations
Authors: shamcode
Summary: Вольный перевод Js Drip #1 Default Parameters in JavaScript

Вольный перевод [Js Drip #1 Default Parameters in JavaScript](http://us6.campaign-archive1.com/?u=2cc20705b76fa66ab84a6634f&id=ce9ce7921e)

Такие языки как Ruby, CoffeeScript и будущие версии Javascript [\[1\]][1] позволяют задавать параметры по умолчанию при
определении функции. Это выглядит примерно так:

```js
function myFunc(param1, param2 = "second string") {
    console.log(param1, param2);
}

// Выведет: "first string" и "second string"
myFunc("first string");

// Выведет: "first string" и "second string version 2"
myFunc("first string", "second string version 2");
```

Увы, эта конструкция не доступна в текущей версии Javscript.  Что мы можем сделать, чтобы достичь такого поведения
с нынешними возможностями?

Простейшее решение выглядит так:

```js
function myFunc(param1, param2) {
    if (param2 === undefined) {
        param2 = "second string";
    }

    console.log(param1, param2);
}

// Выведет: "first string" и "second string version 2"
myFunc("first string", "second string version 2");
```

Этот прием зависит от того факта, что параметр пропущеный во время вызова всегда равен undefined. И это хорошее решение,
 если у вас есть только один параметр. Но что делать, если у вас их несколько?

В этом случае вам, вероятно, следует передавать в параметре объект, так как это дает преимущество, т.к. необходимо
явно называть все, что вы хотите передать. И если вы передаете в качестве параметра объект, то имеет смысл объявить
параметры по умолчанию таким же образом.

```js
function myFunc(paramObject) {
    var defaultParams = {
        param1: "first string",
        param2: "second string",
        param3: "third string"
    };

    var finalParams = defaultParams;

    // Мы перебираем все свойства paramObject
    for (var key in paramObject) {
        // Если текущее свойство не было унаследовано, то обрабатываем
        if (paramObject.hasOwnProperty(key)) {
            // Если текущее свойство определено,
            // добавляем его в finalParams
            if (paramObject[key] !== undefined) {
                finalParams[key] = defaultParams[key];
            }
        }
    }

    console.log(finalParams.param1,
                finalParams.param2,
                finalParams.param3);
}
```

Это немного громоздко, так что если вы часто используете эту схему, то имеет смысл извлечь перебор и логику фильтрации
в отдельную функцию. К счастью, умные люди, которые пишут JQuery и underscore, сделали это в соответствующих extend
методах. [\[2\]][2] [\[3\]][3]

Вот обновленная версия, которая использует метод extend библиотеки underscore для достижения того же результата.

```js
function myFunc(paramObject) {
    var defaultParams = {
        param1: "first string",
        param2: "second string",
        param3: "third string"
    };

    var finalParams = _.extend(defaultParams, paramObject);

    console.log(finalParams.param1,
                finalParams.param2,
                finalParams.param3);
}

// Вывод:
// "My own string" и "second string" и "third string"
myFunc({param1: "My own string"});
```
Вот так вы можете использовать параметры по умолчанию в текущих версиях JavaScript.

###Ссылки:
1. [Harmony of Dreams Come True, by Brendan Eich][1]
2. [Underscore's extend method][2]
3. [jQuery's extend method][3]

[1]: https://brendaneich.com/2012/10/harmony-of-dreams-come-true/ (Harmony of Dreams Come True, by Brendan Eich)
[2]: http://underscorejs.org/#extend (Underscore's extend method)
[3]: http://api.jquery.com/jQuery.extend/ (jQuery's extend method)