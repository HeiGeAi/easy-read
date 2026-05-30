# Easy Read | 人话翻译器

Claude Code skill。扔一篇科技文章进去，出来一份带词汇表的大白话版本。

[English](#english) | [中文](#中文)

---

## 中文

### 这是什么

**你奶奶也能看懂的科技新闻翻译器。**

满屏 Agent、RAG、Embedding 看不懂？Easy Read 把术语全部翻译成人话，生成一份 HTML 词汇表 + 300 字摘要。打开就能看，存下来还能转发给家人。

https://github.com/user-attachments/assets/[demo-video-placeholder]

### 主要功能

- **零门槛**：完全不懂技术也能用，给爸妈看科技新闻就靠它
- **自动抓术语**：AI 概念、缩写、流行梗，一个不漏
- **输出好看**：HTML 词汇表，带难度等级、发音指南、来龙去脉
- **格式随便扔**：文本、文件、网址、PDF、截图都行
- **信息平权**：技术改变每个人的生活，每个人都该看得懂

### 安装

#### 通过插件市场安装（推荐）

直接从 Claude Code 安装：

```bash
/plugin marketplace add HeiGeAi/easy-read
/plugin install easy-read@easy-read
```

然后在 Claude Code 中输入 `/easy-read` 使用。

#### 手动安装

将 skill 文件复制到你的 Claude Code skills 目录：

```bash
# 克隆仓库
git clone https://github.com/HeiGeAi/easy-read.git ~/.claude/skills/easy-read
```

或手动复制：

```bash
# 创建 skill 目录
mkdir -p ~/.claude/skills/easy-read/{scripts,assets}

# 复制所有文件
cp SKILL.md ~/.claude/skills/easy-read/
cp scripts/generate_glossary.py ~/.claude/skills/easy-read/scripts/
cp assets/glossary_template.html ~/.claude/skills/easy-read/assets/
```

然后在 Claude Code 中输入 `/easy-read` 使用。

### 使用方法

#### 基础用法

```
/easy-read

> "这篇文章看不懂" [粘贴文章内容]
```

Skill 会：

1. 提取并分析内容
2. 识别所有技术术语和行话
3. 为每个术语生成大白话解释
4. 创建 HTML 词汇表，包含：
   - 难度等级（入门级 → 大师级）
   - 发音指南（国际音标 + 中式发音）
   - 历史背景（术语怎么演变来的）
   - 300 字文章摘要
5. 保存到桌面的 `claudecode/easy-read-output/` 文件夹
6. 在浏览器中打开

#### 支持的输入格式

**纯文本：**
```
/easy-read

> "帮我理解这个：[粘贴文章]"
```

**文件：**
```
/easy-read

> "解释这个文件：~/Documents/ai-article.pdf"
```

**网址：**
```
/easy-read

> "这篇文章看不懂：https://example.com/article"
```

**截图：**
```
/easy-read

> "看不明白这个" [附加截图]
```

### 会解释什么

识别那些会让**完全没有技术背景的人**懵圈的术语：

#### AI/ML 概念
- Prompt Engineering（提示词工程）、Context Engineering（上下文工程）、Harness Engineering（驾驭工程）
- Agent（智能体）、LLM（大语言模型）、RAG（检索增强生成）、Fine-tuning（微调）
- Embedding（嵌入）、Token（令牌）、Context Window（上下文窗口）

#### 技术术语
- API（应用程序接口）、SDK（软件开发工具包）、CLI（命令行界面）、Framework（框架）
- Backend（后端）、Frontend（前端）、Full-stack（全栈）
- Open Source（开源）、Repository（仓库）、Deployment（部署）

#### 缩写和流行词
- GPT、AI、ML、NLP
- SaaS、PaaS、IaaS
- 大模型、提示词、上下文

#### 文化引用
- 游戏引用（Dota、英雄联盟）
- 梗和网络文化
- 历史科技事件

### 输出格式

每个词汇表包含：

#### 文章摘要
300 字大白话摘要，抓住核心观点，不假设你有任何背景知识。

#### 按难度分级的词汇表

**入门级**：日常生活可能碰到的基础概念
- "API" → "应用程序接口，就像餐厅菜单，让不同软件之间能互相'点菜'"

**进阶级**：需要一点背景知识
- "Prompt Engineering" → "提示词工程，学会怎么跟 AI 说话，让它更懂你的意思"

**专业级**：从业者常用
- "Context Window" → "上下文窗口，AI 一次能'记住'多少内容的上限"

**专家级**：深度技术概念
- "Embedding" → "嵌入向量，把文字转成数字，让 AI 能理解和比较"

**大师级**：前沿研究方向
- "Harness Engineering" → "驾驭工程，给 AI 设计工作环境和工具，比写更长的提示词管用"

#### 每个术语包含

- **中文名称**
- **英文原词**
- **发音**：国际音标 + 中式发音
- **大白话解释**
- **来龙去脉**：术语怎么演变来的
- **时间线**：什么时候火起来的

### 架构

渐进式工作流：

| 文件 | 干什么的 | 什么时候用 |
|------|----------|-----------|
| `SKILL.md` | 核心流程和规则 | 每次调用 |
| `scripts/generate_glossary.py` | HTML 生成 | 第三阶段（生成输出） |
| `assets/glossary_template.html` | 视觉模板 | 第三阶段（生成输出） |

原则：**让复杂的东西变得易懂，信息量一点不丢。**

### 为什么做这个

出发点很简单：**你奶奶应该也能看懂 AI 新闻。**

术语本身是为了精确，但大多数时候它变成了门槛。你去医院看病，医生一堆专业名词说你的病情，你听不懂就焦虑。科技新闻是同一个问题。

Easy Read 做的事情：保留原文的信息量，换一套说人话的表达。把术语还原成它本来要说的意思，加上来龙去脉，看完就懂。

好看的排版也是功能的一部分。读起来舒服，才能真的读进去。

### 系统要求

- [Claude Code](https://claude.ai/claude-code) CLI
- Python 3.7+
- 处理网页内容需要 `web-access` skill

### 输出示例

处理一篇关于 Harness Engineering 的文章，词汇表长这样：

- **Harness Engineering**（大师级）："驾驭工程，给 AI 设计好工作环境和工具箱"
- **Prompt Engineering**（进阶级）："提示词工程，学会跟 AI 说话的技巧"
- **Agent**（专业级）："智能体，能自己做决定、调用工具的 AI 程序"
- **Context Window**（专家级）："上下文窗口，AI 一次能'看到'多少内容"

加上 300 字摘要，用大白话讲清楚文章核心。

---

## English

### What This Does

**Tech articles your grandma can actually read.**

Run into an article full of Agent, RAG, Embedding and have no idea what any of it means? Easy Read translates every piece of jargon into plain language, generates an HTML glossary with a 300-word summary. Open it, read it, send it to anyone.

https://github.com/user-attachments/assets/[demo-video-placeholder]

### Key Features

- **Zero tech background needed**: built for parents, students, and anyone curious about tech
- **Auto jargon detection**: catches AI concepts, acronyms, buzzwords
- **Clean HTML output**: difficulty levels, pronunciation guides, historical context
- **Throw anything at it**: text, files, URLs, PDFs, screenshots
- **Information equity**: tech shapes everyone's life, everyone should be able to follow along

### Installation

#### Via Plugin Marketplace (Recommended)

Install directly from Claude Code:

```bash
/plugin marketplace add HeiGeAi/easy-read
/plugin install easy-read@easy-read
```

Then use it by typing `/easy-read` in Claude Code.

#### Manual Installation

Copy the skill files to your Claude Code skills directory:

```bash
# Clone the repository
git clone https://github.com/HeiGeAi/easy-read.git ~/.claude/skills/easy-read
```

Or manually copy:

```bash
# Create the skill directory
mkdir -p ~/.claude/skills/easy-read/{scripts,assets}

# Copy all files
cp SKILL.md ~/.claude/skills/easy-read/
cp scripts/generate_glossary.py ~/.claude/skills/easy-read/scripts/
cp assets/glossary_template.html ~/.claude/skills/easy-read/assets/
```

Then use it by typing `/easy-read` in Claude Code.

### Usage

#### Basic Usage

```
/easy-read

> "I can't understand this article" [paste article text]
```

The skill will:

1. Extract and analyze the content
2. Identify all technical terms and jargon
3. Generate plain-language explanations for each term
4. Create an HTML glossary with:
   - Difficulty levels (Entry → Master)
   - Pronunciation guides (IPA + Chinese phonetics)
   - Historical context (how the term evolved)
   - A 300-word article summary
5. Save to your Desktop in `claudecode/easy-read-output/`
6. Open it in your browser

#### Supported Input Formats

**Text:**
```
/easy-read

> "Help me understand this: [paste article]"
```

**Files:**
```
/easy-read

> "Explain this file: ~/Documents/ai-article.pdf"
```

**URLs:**
```
/easy-read

> "I can't understand this article: https://example.com/article"
```

**Screenshots:**
```
/easy-read

> "Can't understand this" [attach screenshot]
```

### What Gets Explained

Identifies terms that would confuse someone with **zero computer science background**:

#### AI/ML Concepts
- Prompt Engineering, Context Engineering, Harness Engineering
- Agent, LLM, RAG, Fine-tuning
- Embedding, Token, Context Window

#### Technical Terms
- API, SDK, CLI, Framework
- Backend, Frontend, Full-stack
- Open Source, Repository, Deployment

#### Acronyms & Buzzwords
- GPT, AI, ML, NLP
- SaaS, PaaS, IaaS
- 大模型, 提示词, 上下文

#### Cultural References
- Game references (Dota, League of Legends)
- Memes and internet culture
- Historical tech events

### Output Format

Each glossary includes:

#### Article Summary
300-word plain-language summary. No assumed knowledge.

#### Glossary by Difficulty Level

**Entry Level**: basics you might encounter in daily life
- "API" → "Like a restaurant menu that lets different software 'order' from each other"

**Intermediate**: needs a bit of context
- "Prompt Engineering" → "Learning how to talk to AI so it gets what you mean"

**Professional**: industry practitioners use these daily
- "Context Window" → "How much content AI can 'remember' at once"

**Expert**: deep technical concepts
- "Embedding" → "Turning text into numbers so AI can understand and compare"

**Master**: cutting-edge research
- "Harness Engineering" → "Designing AI's work environment and tools, way more effective than longer prompts"

#### For Each Term

- **Chinese Name**
- **English Name**
- **Pronunciation**: IPA + Chinese phonetic guide
- **Plain Explanation**
- **Historical Context**: how the term evolved
- **Timeline**: when it became popular

### Architecture

Progressive workflow:

| File | Purpose | When Used |
|------|---------|-----------|
| `SKILL.md` | Core workflow and rules | Every invocation |
| `scripts/generate_glossary.py` | HTML generation | Phase 3 (output) |
| `assets/glossary_template.html` | Visual template | Phase 3 (output) |

Principle: **Make complex things accessible. Keep every bit of information.**

### Why This Exists

Simple idea: **your grandma should be able to read AI news too.**

Jargon exists for precision, but most of the time it becomes a wall. Going to the doctor and getting hit with medical terms you can't follow is stressful. Tech news has the same problem.

Easy Read keeps all the original information, just swaps in language real people actually use. Every term gets traced back to what it really means, with enough context to make it stick.

Good design is part of the function. If it's easy on the eyes, it's easier on the brain.

### Requirements

- [Claude Code](https://claude.ai/claude-code) CLI
- Python 3.7+
- For web content: `web-access` skill

### Example Output

Process an article about Harness Engineering and get a glossary like this:

- **Harness Engineering** (Master): "Designing AI's work environment and toolbox"
- **Prompt Engineering** (Intermediate): "The skill of talking to AI effectively"
- **Agent** (Professional): "An AI program that makes its own decisions and uses tools"
- **Context Window** (Expert): "How much content AI can 'see' at once"

Plus a 300-word summary explaining the core in plain language.

---

## 致谢 | Credits

[@blakexu](https://github.com/blakexu) 用 Claude Code 做的。

## 许可证 | License

MIT. 随便用，随便改，随便分享。
