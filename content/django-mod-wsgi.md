Title: Несколько django приложений на одном apache с mod_wsgi
Date: 2014-03-11 04:43
Tags: apache, django, modwsgi
Slug: django-mod_wsgi
Lang: ru
Category: Tips
Authors: shamcode
Summary: Захотелось мне развернуть на VPS два django приложения, причем одно бы крутилось на основном домене, а второе на поддомене ([shamcode.ru](shamcode.ru) и [todo.shamcode.ru](todo.shamcode.ru))...

Захотелось мне развернуть на VPS два django приложения, причем одно бы крутилось на основном домене, а второе на поддомене
([shamcode.ru](shamcode.ru) и [todo.shamcode.ru](todo.shamcode.ru)). Вроде бы ничего сложного, но почему-то они начали пытаться
брать настройки друг-друга. [Полное решение](http://stackoverflow.com/questions/11505576/deploying-multiple-django-apps-on-apache-with-mod-wsgi).

Т.е. проблема устраняется запуском каждого приложения в своей группе процессов.
