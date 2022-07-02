# build_scripts

一个简单的 python 构建脚本，用于实现微服务/应用的构建过程。

包含：

- python 包装的 shell 命令 DSL
    - DSL 更方便与 python 代码集成
- 动态配置任务
    - 通过串行运行，实现多级的构建任务
    - 通过 start.builder_list 控制构建任务，runner 会从 builders 包中查找相应的模块
        - 稍改一个可以实现从环境变量获取任务

## LICENSE

MIT
