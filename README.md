# build_scripts

build_scripts 是一个使用 python 实现 Shell DSL，用于实现微服务/软件的构建过程。

软件构建是一个复杂过程。不同的技术栈常常会使用不同的构建工具。比如 rust 会使用 cargo，c/c++ 会 makefile、cmake，javascript 大部分场景都会使用 npm。一些简单的脚本可能只是 copy/move/zip 三步走。但是对于实际的生产项目，则会通过构建脚本实现打包出不同的安装包，比如直接安装使用的 zip 包；用于容器化环境的 docker 镜像包。难免会引入复杂的构建过程。再者，ci/cd 的需要也需要构建脚本提供支撑。

常见的构建脚本多基于 shell 实现，主要就是 bash。shell 的优点是 linux 系统环境下，基本上开箱即用。如果使用容器化的构建环境，可以实现不同的环境的工具一致性。但是 shell 也是有明显问题。

首先 shell 脚本是为简单的脚本需求实现的，shell 内置的功能非常有限，常常依赖其他工具。其次，shell 语言一致性很差，语法可以用奇怪来形容。再就是开发工具（ide/编辑器）对于 shell 支持非常有限。最后，shell 脚本测试基本上依赖一次又一次完全执行来保证正确性。因此使用 shell 实现大型、复杂的构建脚本并非正确的选择。

与 shell 相比，python 则显得功能强大。语言本身的一致性、工具支持、测试都比 shell 有很大的提升，另外 python 的上手难易程度并不比 shell 高多少。python 内置的强大功能也足够应对常见的构建任务需求。

## 特性

- Shell DSL
  - 基于 python 实现的 shell 命令 DSL
    - 以 python 函数的封装常用的命令，可以更好地与 python 脚本进行集成
  - DSL 也方便迁移原来的构建脚本
- 动态配置任务
  - 通过串行运行，实现多级的构建目标
  - 通过 start.builder_list 控制构建任务，runner 会从 builders 包中查找相应的模块（稍改可以实现从环境变量获取任务）
- 简单的构建目标实现
  - 每个构建目标实际上是一个 python 的模块
    - 模块里需要导出 Builder 类，并提供 build 方法
  - 构建目标的代码由 runner 执行

## LICENSE

[MIT](LICENSE)
