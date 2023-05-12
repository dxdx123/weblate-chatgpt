.. image:: https://s.weblate.org/cdn/Logo-Darktext-borders.png
   :alt: Weblate
   :target: https://weblate.org/
   :height: 80px

**Weblate is libre software web-based continuous localization system,
used by over 2500 libre projects and companies in more than 165 countries.**

Example how to customize Weblate look see `Weblate documentation`_ for more
information.

.. _Weblate documentation: https://docs.weblate.org/en/latest/admin/customize.html


安装自定义组件(AddOns)




weblate参考文档：https://docs.weblate.org/zh_CN/weblate-4.16.4/admin/customize.html#customizing-weblate
以安装官方自定义质量检查组件https://github.com/WeblateOrg/customize-example 为例：
进入weblate容器挂载出来的项目目录 /data/weblate_data/weblate-docker_weblate-data/python
使用 git clone git@github.com:WeblateOrg/customize-example.git 克隆到该目录下，并修改这个目录的文件夹权限 chmod 777 -R customize-example ，防止下面安装时候会出现的权限报错。
进入weblate容器中 docker exec -it weblate-docker-weblate-1 bash，并进入/app/data/python目录下，执行python module安装命令 pip install -e . ，改安装命令会自动下载对应的依赖。
模块一旦安装，就可以用在 Webalte 配置中（例如 weblate_customization.checks.FooCheck 对应的脚本为：customize-example/weblate_customization/checks.py中的FooCheck类）。
这个组件功能应用于翻译标记中，具体见文档：https://docs.weblate.org/zh_CN/weblate-4.16.4/admin/projects.html#translation-flags
编写自定义质量检查的更多参考：https://docs.weblate.org/zh_CN/weblate-4.16.4/admin/checks.html#writing-own-checks