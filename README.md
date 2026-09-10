# 大数据与人工智能课程

> 个人课程学习仓库 —— Mingxing-bigdata

## 课程目标
- 掌握 Python 数据分析基础
- 理解常见机器学习算法原理
- 熟悉大数据处理流程与工具（Hadoop / Spark / Flink 生态）

## 目录结构

| 目录 | 用途 |
|---|---|
| `.workbuddy/skills/concept-learner/` | **项目级 Skill**（概念学习资料生成技能） |
| `learning-materials/` | 概念学习资料（HTML 交互卡：Agent / 上下文 / Skill / Agent 记忆 / 向量检索·RAG / 反思机制 / 关系图） |
| `concept-relationship.md` | 三概念关系说明（Markdown 源，含 Mermaid） |
| `notes/` | 课堂笔记与自学总结 |
| `assignments/` | 课程作业 |
| `src/` | 课程代码与示例 |
| `requirements.txt` | Python 第三方依赖清单 |

## 环境
- Python 3.12（Windows 命令为 `python`，macOS/Linux 为 `python3`）
- Git 2.43
- VSCode 1.136（推荐编辑器）

### 安装 Python 依赖
```bash
pip install -r requirements.txt    # Windows
pip3 install -r requirements.txt   # macOS / Linux
```

## 概念学习作业（Agent Skills）

本次作业设计了一个**可复用**的概念学习 Skill，并用它生成三份概念资料与一份关系说明。设计原则：Skill 接收"任意一个新概念"作为输入，而不是为本次三个概念写一次性提示词。

### Skill 存放路径（项目级）
| 位置 | 说明 |
|---|---|
| `.workbuddy/skills/concept-learner/SKILL.md` | **项目级 Skill 源文件**（随仓库版本管理，教师可直接查看） |
| `~/.workbuddy/skills/concept-learner/SKILL.md` | 本机用户级副本（便于在任意项目调用，可选） |

SKILL.md 顶部包含 YAML 元数据（`name` / `description`），并明确说明：适用场景、输入信息、生成步骤（8 步）、输出结构（模板）、资料来源要求、交付前自检清单。

### 如何在 WorkBuddy 中调用
1. 将本仓库根目录作为工作区在 WorkBuddy 中打开，项目级 Skill（`.workbuddy/skills/`）即自动可被发现；
2. 在对话中直接提出概念学习需求即可自动触发（Agent 读取各技能 `description` 进行匹配），例如：
   - "帮我系统学一下 XX 概念"
   - "用 concept-learner 给『布隆过滤器』做一张学习卡"
   - "帮我把『数据倾斜』整理成概念学习资料"
3. 匹配成功后，Agent 加载 SKILL.md，按"澄清 → 一句话理解 → 拆机制 → 找案例 → 辨析 → 自测 → 来源核查"流程执行，产出结构化学习卡。
4. 若在其它工作区使用：把 `.workbuddy/skills/concept-learner/` 复制到 `~/.workbuddy/skills/`（用户级）即可全局调用。

### 已生成的学习资料
- `learning-materials/agent.html` —— 概念：Agent（智能体）
- `learning-materials/llm-context.html` —— 概念：大模型的上下文（Context）
- `learning-materials/skill.html` —— 概念：Agent Skill
- `learning-materials/concept-relationship.html` —— 三概念关系（交互版）
- `learning-materials/agent-memory.html` —— 概念：Agent 的记忆系统
- `learning-materials/rag.html` —— 概念：向量检索 / RAG（检索增强生成）
- `learning-materials/reflection.html` —— 概念：反思机制（Reflexion）
- `concept-relationship.md` —— 三概念关系（Markdown 源，含 Mermaid 图）

每份概念资料均包含：学习目标、一句话通俗理解（AI 生成）、核心机制/组成、一个具体应用场景、易混淆与使用边界、自测问题、可视化选择题测验、可核查的学术资料来源链接。

### AI 使用与人工核查说明
本次作业按课程要求使用了 AI 协助（设计 Skill 流程、起草资料初稿、整理 Git 命令），并做了以下人工核查：

**AI 已完成并如实记录：**
- [x] 资料来源链接于 2026-09-06 逐条实际打开核验，正文论断与来源一致（除 `learning-materials/llm-context.html` 中 OpenAI 链接因本机区域网络拦截未能打开，已在该文件内明确标注）；
- [x] 概念机制性表述与至少一个一手来源比对一致；
- [x] 三份资料均按同一 Skill 模板输出（验证 Skill 可复用性）。

**本人（学生）提交前需完成：**
- [ ] 通读三份概念资料与关系文档，确认理解无误
- [ ] （可选）如需个人化，可将各资料“一句话理解（AI 生成）”改写为自己的表达；否则保留 AI 通俗版
- [ ] 抽查并确认文末每条来源链接可打开
- [ ] 回答各资料"自测问题"检验是否真正掌握
- [ ] 确认本仓库在 GitHub 上为**公开**状态

## 常用 Git 命令

```bash
git pull                    # 拉取最新
git add .                   # 暂存所有改动
git commit -m "说明修改"     # 提交
git push                    # 推送到 GitHub
```

## 更新日志
- v0.3.0：按作业要求将 Skill 调整为**项目级**（`.workbuddy/skills/concept-learner/`）；学习资料改为 HTML 交互卡并移至 `learning-materials/`
- v0.4.0：新增概念资料 Agent 的记忆系统（`learning-materials/agent-memory.html`），含记忆系统架构图、可视化选择题测验与 arXiv 学术来源；资料来源统一为权威学术文献
- v0.5.0：新增概念资料 向量检索/RAG（`rag.html`，检索流水线图 + arXiv:2005.11401/2004.04906/2002.08909）与 反思机制（`reflection.html`，反思循环图 + arXiv:2303.11366/2303.17651/2308.11432）；均含可视化选择题测验与学术来源；全部 7 张卡互相导航
- v0.2.0：新增概念学习作业——可复用 concept-learner Skill、三份概念资料与关系文档；README 补充调用方式与 AI 核查说明
- v0.1.1：新增 requirements.txt 与依赖安装说明；运行命令改为跨平台写法；修复学习卡抽题逻辑
- v0.1.0：初始化仓库，搭建课程骨架
