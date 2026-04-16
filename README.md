# Easy Read | 人话翻译器

一个 Claude Code skill，将技术文章转换为易懂内容 — 把充满术语的 AI/科技新闻变成任何人都能理解的大白话。

[English](#english) | [中文](#中文)

---

## 中文

### 这是什么

**Easy Read（人话翻译器）** 帮助非技术人员理解复杂的技术内容。它自动识别难懂的术语，创建美观的词汇表，用大白话解释，并提供文章摘要，让完全没有技术背景的人也能看懂。

核心特点：

https://github.com/user-attachments/assets/[demo-video-placeholder]

### 主要功能

- **零技术背景要求** — 专为爷爷奶奶、学生和任何对科技新闻好奇的人设计
- **智能术语识别** — 自动识别需要解释的术语（AI 概念、缩写、流行词）
- **美观的输出** — 简洁现代的 HTML 词汇表，带难度等级、发音指南和历史背景
- **多种输入格式** — 接受文本、文件、网址、PDF、截图 — 任何你扔给它的东西
- **信息平权** — 每个人都应该理解正在塑造我们世界的技术，无论背景如何

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
4. 创建美观的 HTML 词汇表，包含：
   - 难度等级（入门级 → 大师级）
   - 发音指南（国际音标 + 中式发音）
   - 历史背景（术语如何演变）
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

Skill 识别那些会让**零计算机基础**的人困惑的术语：

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
一个 300 字的大白话摘要，捕捉关键点，不假设任何技术知识。

#### 按难度等级分类的词汇表

**入门级** — 日常生活中可能遇到的基础概念
- 例如："API" → "应用程序接口 — 就像餐厅的菜单，让不同软件之间能互相'点菜'交流"

**进阶级** — 需要一些背景知识
- 例如："Prompt Engineering" → "提示词工程 — 学会怎么跟 AI 说话，让它更懂你的意思"

**专业级** — 行业从业者常用
- 例如："Context Window" → "上下文窗口 — AI 一次能'记住'多少内容的限制"

**专家级** — 深度技术概念
- 例如："Embedding" → "嵌入向量 — 把文字转成数字，让 AI 能理解和比较"

**大师级** — 前沿研究
- 例如："Harness Engineering" → "驾驭工程 — 设计 AI 的工作环境和工具，而不是写更长的提示词"

#### 每个术语包含

- **中文名称** — 中文翻译
- **英文名称** — 原始术语
- **发音** — 国际音标 + 中式发音提示
- **大白话解释** — 用日常语言解释含义
- **历史背景** — 术语如何演变（追溯 1-2 个版本）
- **时间线** — 何时流行起来

### 架构

这个 skill 使用**渐进式工作流**：

| 文件 | 用途 | 何时使用 |
|------|------|----------|
| `SKILL.md` | 核心工作流程和规则 | 始终（skill 调用时） |
| `scripts/generate_glossary.py` | HTML 生成逻辑 | 阶段 3（输出创建） |
| `assets/glossary_template.html` | 视觉模板 | 阶段 3（输出创建） |

设计遵循原则："让复杂的东西变得易懂，而不是简化。"

### 设计哲学

这个 skill 诞生于以下信念：

1. **信息应该对每个人都可及。** 你的奶奶应该能够阅读 AI 新闻而不感到迷失。

2. **术语是障碍，不是特色。** 技术术语存在是为了精确，但它们不应该把人们排除在理解重要发展之外。

3. **背景很重要。** 知道一个术语从哪里来，有助于你理解它要去哪里。

4. **美观的设计有助于理解。** 设计良好的词汇表不仅仅是好看 — 它帮助你学习。

### 系统要求

- [Claude Code](https://claude.ai/claude-code) CLI
- Python 3.7+（用于词汇表生成）
- 处理网页内容需要：`web-access` skill 或类似工具

### 输出示例

当你处理一篇关于"Harness Engineering"的文章时，你会得到一个词汇表，解释：

- **Harness Engineering**（大师级）— "驾驭工程：不是教 AI 怎么做，而是给它设计好工作环境和工具"
- **Prompt Engineering**（进阶级）— "提示词工程：学会跟 AI 说话的艺术"
- **Agent**（专业级）— "智能体：能自己做决策、调用工具的 AI 程序"
- **Context Window**（专家级）— "上下文窗口：AI 一次能'看'多少内容"

加上一个 300 字的摘要，用大白话解释文章的要点。

---

## English

### What This Does

**Easy Read** helps non-technical people understand complex technical content. It automatically identifies difficult terms, creates beautiful glossaries with plain-language explanations, and provides article summaries that make sense to complete beginners.

Here's what makes it special:

https://github.com/user-attachments/assets/[demo-video-placeholder]

### Key Features

- **Zero Technical Background Required** — Designed for grandparents, students, and anyone curious about tech news
- **Smart Jargon Detection** — Automatically identifies terms that need explanation (AI concepts, acronyms, buzzwords)
- **Beautiful Output** — Clean, modern HTML glossaries with difficulty levels, pronunciation guides, and historical context
- **Multiple Input Formats** — Accepts text, files, URLs, PDFs, screenshots — anything you throw at it
- **Information Equity** — Everyone deserves to understand what's happening in tech, regardless of background

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
4. Create a beautiful HTML glossary with:
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

The skill identifies terms that would confuse someone with **zero computer science background**:

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
A 300-word plain-language summary that captures the key points without assuming any technical knowledge.

#### Glossary by Difficulty Level

**Entry Level** — Basic concepts you might encounter in daily life
- Example: "API" → "Application Programming Interface — like a restaurant menu that lets different software 'order' from each other"

**Intermediate** — Requires some context
- Example: "Prompt Engineering" → "The art of learning how to talk to AI so it understands you better"

**Professional** — Industry practitioners use these
- Example: "Context Window" → "The limit on how much content AI can 'remember' at once"

**Expert** — Deep technical concepts
- Example: "Embedding" → "Converting text into numbers so AI can understand and compare"

**Master** — Cutting-edge research
- Example: "Harness Engineering" → "Designing AI's work environment and tools, rather than writing longer prompts"

#### For Each Term

- **Chinese Name** — 中文名称
- **English Name** — Original term
- **Pronunciation** — IPA phonetic + Chinese pronunciation guide
- **Plain Explanation** — What it means in everyday language
- **Historical Context** — How the term evolved (1-2 versions back)
- **Timeline** — When it became popular

### Architecture

This skill uses a **progressive workflow**:

| File | Purpose | When Used |
|------|---------|-----------|
| `SKILL.md` | Core workflow and rules | Always (skill invocation) |
| `scripts/generate_glossary.py` | HTML generation logic | Phase 3 (output creation) |
| `assets/glossary_template.html` | Visual template | Phase 3 (output creation) |

The design follows the principle: "Make complex things accessible, not simplified."

### Philosophy

This skill was born from the belief that:

1. **Information should be accessible to everyone.** Your grandmother should be able to read AI news without feeling lost.

2. **Jargon is a barrier, not a feature.** Technical terms exist for precision, but they shouldn't exclude people from understanding important developments.

3. **Context matters.** Knowing where a term came from helps you understand where it's going.

4. **Beautiful design aids comprehension.** A well-designed glossary isn't just pretty — it helps you learn.

### Requirements

- [Claude Code](https://claude.ai/claude-code) CLI
- Python 3.7+ (for glossary generation)
- For web content: `web-access` skill or similar

### Example Output

When you process an article about "Harness Engineering", you'll get a glossary that explains:

- **Harness Engineering** (Master) — "Designing AI's work environment and tools, not teaching it what to do"
- **Prompt Engineering** (Intermediate) — "The art of learning how to talk to AI"
- **Agent** (Professional) — "An AI program that can make decisions and use tools on its own"
- **Context Window** (Expert) — "How much content AI can 'see' at once"

Plus a 300-word summary explaining the article's main points in plain language.

---

## 致谢 | Credits

Created by [@blakexu](https://github.com/blakexu) with Claude Code.

Inspired by the belief that everyone deserves to understand the technology shaping our world.

受信念启发：每个人都应该理解正在塑造我们世界的技术。

## 许可证 | License

MIT — Use it, modify it, share it. | 使用它，修改它，分享它。
