Title: Проблемы с Flash'ем в chrome под Debian
Date: 2014-09-24 19:21
Tags: nix, links
Slug: chrome-flush-plugin-and-debian
Lang: ru
Category: Tips
Authors: shamcode
Summary: Сидел несколько дней под Windows и вот решил перезагрузиться под Debian. По-привычке сразу запустил музыку из Вк... Но музыки нет, а есть ошибка, мол "Flash-плагин упал и не встает. Потыкать палкой?" Тыкание палкой (перезапуск) и ребут всего хрома не помогли. Нашел вот здесь решение:

Сидел несколько дней под Windows и вот решил перезагрузиться под Debian. По-привычке сразу запустил музыку из Вк...
Но музыки нет, а есть ошибка, мол "Flash-плагин упал и не встает. Потыкать палкой?" Тыкание палкой (перезапуск) и ребут
всего хрома не помогли. Нашел вот [здесь](https://code.google.com/p/chromium/issues/detail?id=414135) решение:

1. Закрываем хром
2. Скачиваем [вот тут](http://mirror.pcbeta.com/google/chrome/deb/pool/main/g/google-chrome-stable/) последнюю версию хрома
3. Для моей версии Debian было что-то типо этого: `google-chrome-stable_37.0.2062.94-1_amd64.deb`
4. Распаковываем, и берем вот этот файл:
```bash
../Downloads/chrome/opt/google/chrome/PepperFlash/libpepflashplayer.so
```
5. И заменяем им вот этот:
```bash
/opt/google/chrome/PepperFlash/libpepflashplayer.so
```

Запускаем хром и слушаем музыку как в старые добрые.