# 插件说明
### 这是一个示例插件，演示如何在把自定义weblate组件添加[附加组件]页面，以便安装使用。
### 详情请参照官方文档：https://docs.weblate.org/zh_CN/weblate-4.16.4/admin/customize.html

## 运行环境
* 运行方式：docker-compose方式运行
* 挂载目录：weblate的/app/data目录，映射到宿主机上的/data/weblate_data/weblate-docker_weblate-data/
* 自定义插件存放目录：`挂载目录`/python
* appsettings-override.py文件目录：`挂载目录`

## 安装运行插件
- 把插件拷贝到 `自定义插件存放目录`
- 在appsettings-override.py文件中添加插件，根据插件类型可能需要注册到不同的列表中。
  - appsettings-override.py文件如果没有，自行创建即可
  - 插件命名规则：[插件包名].[插件代码所在的文件名].[插件类名]。
  - 常见的插件有以下几种，注册到对应的数组里即可：
      ```
      # Checks
      CHECK_LIST += ("weblate_customization.checks.FooCheck",)
    
      # Autofixes
      AUTOFIX_LIST += ("weblate_customization.autofix.FooFixer",)
    
      # Add-ons
      WEBLATE_ADDONS += ("weblate_customization.addons.ExamplePreAddon",)
      ```
  - 示例 appsettings-override.py文件
- 进入weblate容器，执行命令 
    ```
    # 假设当前安装的插件是weblate_holdon插件
    docker exec -it weblate-docker-weblate-1 /bin/bash
    cd /app/data/python/
    mkdir weblate-holdon && cd weblate-holdon
  
    # 克隆插件到本地
    git clone -b holdon https://github.com/dxdx123/weblate-chatgpt.git .
  
    # 重启容器
    docker restart weblate-docker-weblate-1
    ```
- 重启docker容器后，进入weblate对应的页面查看插件。
  - 其中 附加组件 可以在 [项目]/[部件]/[附加组件]列表中看到
## Q&A
- 如果报错可以查看docker日志
  ```
  docker logs -f weblate-docker-weblate-1
  ```