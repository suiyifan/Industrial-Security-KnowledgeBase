# Git 与 GitHub 基础

## 1. Git 是什么

Git 是版本控制工具。你可以把它理解成“学习和代码的时间机器”。

它能记录：

- 你什么时候改了文件。
- 哪些内容被新增、删除、修改。
- 每一次修改的原因。
- 当前项目能不能回到某个历史版本。

GitHub 是代码托管平台。你可以把本地 Git 仓库上传到 GitHub，让项目成为可展示的作品集。

## 2. 为什么工控安全岗位需要 Git

这个岗位强调研究、工具开发、报告输出。Git 能帮你证明：

- 你持续学习，不是一夜包装出来。
- 你能写结构化项目。
- 你能沉淀脚本、实验和报告。
- 你具备基本工程习惯。

面试时，一个干净的 GitHub 仓库比“我学过很多东西”更有说服力。

## 3. Git 的核心概念

### 3.1 Repository 仓库

仓库就是一个被 Git 管理的项目文件夹。

常用命令：

```powershell
git init
```

含义：把当前文件夹初始化为 Git 仓库。

### 3.2 Working Tree 工作区

工作区就是你正在编辑的文件。

例如你修改了 `README.md`，这个修改还没有进入 Git 记录，它就在工作区。

查看工作区状态：

```powershell
git status
```

### 3.3 Staging Area 暂存区

暂存区是提交前的准备区。你可以选择哪些文件进入下一次提交。

```powershell
git add README.md
git add .
```

`git add .` 表示把当前目录下的所有改动加入暂存区。

### 3.4 Commit 提交

提交是一次正式记录。

```powershell
git commit -m "Add networking notes"
```

提交信息要说明“这次改了什么”，不要写成 `update`、`fix` 这种含糊词。

### 3.5 Branch 分支

分支可以让你在不影响主线的情况下尝试新内容。

```powershell
git branch
git switch -c sprint-01-fundamentals
```

初学阶段可以先只用 `main` 或 `master`，等项目内容多了再使用分支。

## 4. 最小日常工作流

每天学习结束后执行：

```powershell
git status
git add .
git commit -m "Add Linux permission notes"
```

如果已经连接 GitHub：

```powershell
git push
```

## 5. 推荐提交信息格式

可以使用简单格式：

```text
Add Python socket notes
Add Modbus TCP lab report
Update interview Q&A
Fix typo in Linux notes
```

关键词建议：

- `Add`: 新增内容
- `Update`: 更新已有内容
- `Fix`: 修正错误
- `Refactor`: 调整结构
- `Docs`: 文档相关

## 6. 初学者常见问题

### 6.1 git status 看到红色文件是什么意思

通常表示文件还没有进入暂存区，或者文件被修改但还没 `git add`。

### 6.2 git status 看到绿色文件是什么意思

表示文件已经进入暂存区，下一次 `git commit` 会记录它们。

### 6.3 commit 之后还能改吗

能。你继续修改文件，再做新的 commit。不要害怕提交，Git 的价值就在于保留过程。

### 6.4 要不要每天 push 到 GitHub

建议每天 push。这样你的学习路径会形成可见轨迹。

## 7. 本章实践

### 练习 1：创建学习笔记并提交

1. 新建 `memory/Today.md`。
2. 写下今天学到的 3 个概念。
3. 执行 `git status`。
4. 执行 `git add .`。
5. 执行 `git commit -m "Add daily learning note"`。

### 练习 2：查看历史

```powershell
git log --oneline
```

你应该能看到每一次提交的短哈希和提交信息。

## 8. 面试表达

可以这样说：

> 我用 Git 管理自己的工控安全知识库，把每个阶段的学习笔记、实验报告和工具脚本都做版本记录。这样既方便复盘，也能让面试官看到我的学习路径和工程习惯。

<!-- NAVIGATION_INDEX -->

---

## 导航索引

- 上一篇：[01 章学习地图：计算机与安全基础]()
- 本章目录：[01_Fundamentals]()
- 下一篇：[Linux 基础]()

