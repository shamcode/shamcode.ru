Title: Публикация пакетов в npm
Date: 2017-03-12 21:24
Tags: js, npm
Slug: npm-publishing
Lang: ru
Category: Tips
Authors: shamcode
Summary: Последовтельность действий для публикации пакета в NPM

1. Редактируем `version` в `package.json`

2. `git commit`

3. `git tag #sem version, as 1.0.5`

4. `git push origin master`

5. `npm publish`