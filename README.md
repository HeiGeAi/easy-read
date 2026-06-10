# Easy Read | 人话翻译器

把看不懂的东西，变成谁都能看懂的大白话词汇表。

[English](#english) | [中文](#中文)

---

## 中文

### 这是什么

你有没有过这种体验：

- 刷到一篇 AI 新闻，标题写着"基于 RAG 的 Agentic Workflow 实现了 Context Engineering 的范式跃迁"
- 拿到体检报告，上面写着"TSH 偏高，建议排查甲状腺功能亢进"
- 签合同前想看看条款，满眼"不可抗力""连带责任""仲裁管辖"
- 想学理财，基金说明书里全是"PE""ROE""夏普比率"

**每个字你都认识，连起来就是天书。**

Easy Read 就干一件事：**把这些话翻译成人话。**

> 🤖 翻译前：「基于 RAG 的 Agentic Workflow...」
> ✅ 翻译后：「让 AI 回答问题前先查资料（像考试允许翻书），然后自己规划步骤完成任务。」
>
> 🏥 翻译前：「TSH 偏高，建议排查甲状腺功能亢进」
> ✅ 翻译后：「甲状腺激素的指挥官（TSH）数值偏高，可能是甲状腺太亢奋了，在加班加点分泌激素。需要进一步检查确认。」
>
> ⚖️ 翻译前：「因不可抗力导致的违约不承担连带责任」
> ✅ 翻译后：「如果是地震、洪水、战争这种谁都控制不了的事导致没法履行合同，不用赔钱，也不用替别人背锅。」

它会把文章里所有你看不懂的术语，自动整理成一份**带发音、带解释、带来龙去脉的词汇表**，生成好看的 HTML 页面。打开就能看，存下来还能转发给爸妈。

### 支持的领域

| | 领域 | 典型场景 |
|---|------|----------|
| 🤖 | AI / 科技 | 科技新闻、产品发布、技术博客 |
| 🏥 | 医学 / 健康 | 体检报告、药品说明书、医学新闻 |
| ⚖️ | 法律 | 合同条款、判决书、法律新闻 |
| 💰 | 金融 / 财经 | 财报、基金说明书、经济分析 |
| 📚 | 学术论文 | 跨学科论文、研究报告 |
| 📋 | 政策文件 | 政府白皮书、红头文件、政策解读 |
| 🎮 | 游戏 | 更新日志、游戏机制、攻略 |
| 🔗 | 区块链 / Web3 | 白皮书、DeFi 术语 |
| 🔧 | 硬件 / 数码 | 手机评测、电脑配置、参数对比 |
| 📖 | **任何领域** | **只要你看不懂，就能翻译** |

### 主要功能

- **零门槛**：完全不懂这个领域也能用，给家人看专业内容就靠它
- **自动识别领域**：扔进去的内容是什么领域，它自己判断
- **自动抓术语**：专业概念、缩写、行话，一个不漏
- **输出好看**：HTML 词汇表，带难度等级、发音指南、来龙去脉
- **格式随便扔**：文本、文件、网址、PDF、截图都行
- **全 Agent 通用**：Claude Code、Codex、Cursor、Cline 都能跑

### 安装

#### Claude Code（推荐）

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

#### 其他 Agent

Easy Read 的核心是 SKILL.md（指令）+ Python 脚本（生成 HTML），不绑定特定 Agent。只要你的 Agent 能读文件、跑 Python，就能用。

<details>
<summary><b>Codex (OpenAI)</b></summary>

```bash
git clone https://github.com/HeiGeAi/easy-read.git
# 把 SKILL.md 内容贴进项目的 AGENTS.md 或 .codex/instructions.md
```
</details>

<details>
<summary><b>OpenClaw / DeskClaw</b></summary>

```bash
git clone https://github.com/HeiGeAi/easy-read.git ~/.openclaw/skills/easy-read
# SKILL.md 格式兼容，直接可用
```
</details>

<details>
<summary><b>Cursor</b></summary>

```bash
git clone https://github.com/HeiGeAi/easy-read.git
# 把 SKILL.md 内容加到项目根目录的 .cursor/rules/easy-read.mdc
# 或直接放进 .cursorrules 文件
```
</details>

<details>
<summary><b>Windsurf</b></summary>

```bash
git clone https://github.com/HeiGeAi/easy-read.git
# 把 SKILL.md 内容加到项目根目录的 .windsurfrules
```
</details>

<details>
<summary><b>Cline (VS Code)</b></summary>

```bash
git clone https://github.com/HeiGeAi/easy-read.git
# 把 SKILL.md 内容加到项目根目录的 .clinerules
# 或在 Cline 设置里添加为 Custom Instructions
```
</details>

<details>
<summary><b>Aider</b></summary>

```bash
git clone https://github.com/HeiGeAi/easy-read.git
# 把 SKILL.md 内容加到 .aider.conf.yml 的 read 列表
# 或启动时用 --read SKILL.md 参数
aider --read easy-read/SKILL.md
```
</details>

<details>
<summary><b>GitHub Copilot</b></summary>

```bash
git clone https://github.com/HeiGeAi/easy-read.git
# 把 SKILL.md 内容加到 .github/copilot-instructions.md
```
</details>

<details>
<summary><b>Continue (VS Code / JetBrains)</b></summary>

```bash
git clone https://github.com/HeiGeAi/easy-read.git
# 在 .continue/config.yaml 的 customInstructions 中引用 SKILL.md
# 或把内容加到 .continuerules 文件
```
</details>

<details>
<summary><b>Trae (字节)</b></summary>

```bash
git clone https://github.com/HeiGeAi/easy-read.git
# 把 SKILL.md 内容加到 .trae/rules 文件
```
</details>

<details>
<summary><b>Augment</b></summary>

```bash
git clone https://github.com/HeiGeAi/easy-read.git
# 在 Augment 的 Instructions 设置中引用 SKILL.md 内容
```
</details>

<details>
<summary><b>Devin</b></summary>

在 Devin 的 Knowledge 面板上传 SKILL.md，然后对话时说"按照 Knowledge 里的 Easy Read 流程处理这篇文章"。
</details>

<details>
<summary><b>通用方式（任何 Agent）</b></summary>

```bash
git clone https://github.com/HeiGeAi/easy-read.git
```

告诉你的 Agent："读 `easy-read/SKILL.md`，按里面的流程处理这篇文章"。

工作流：Agent 读 SKILL.md → 分析文章 → 生成 JSON → 调 Python 脚本 → 输出 HTML。
</details>

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

只要是**你奶奶看不懂的词**，它都会抓出来解释：

🤖 **AI 黑话**：Agent、LLM、RAG、Embedding... 圈内人天天说但圈外人一脸懵的词

🏥 **医学天书**：转氨酶、甲亢、HbA1c、MRI 增强... 体检报告上让你焦虑的那些指标

⚖️ **法律黑话**：不可抗力、善意取得、连带责任... 合同里你假装看懂但其实没看懂的条款

💰 **金融密码**：PE、ROE、可转债、量化宽松... 理财文章里让你觉得自己不配赚钱的词

📚 **学术八股**：p值、置信区间、meta分析... 论文里那些让你怀疑自己学历的术语

🎮 **游戏/数码/区块链/政策文件**... 任何领域的专业词汇都能翻译

### 输出长什么样

每个词汇表 = **300 字大白话摘要** + **按难度分级的术语卡片**。

术语按五个等级排列，从"你妈也懂"到"连从业者都得想一想"：

| 等级 | 谁能懂 | 举个例子 |
|------|--------|----------|
| 🟢 入门级 | 所有人 | API → 就像餐厅菜单，让软件之间互相"点菜" |
| 🔵 进阶级 | 关注科技的人 | Prompt Engineering → 学会怎么跟 AI 说话 |
| 🟡 专业级 | 从业者 | Context Window → AI 一次能"记住"多少内容 |
| 🔴 专家级 | 深度技术人 | Embedding → 把文字转成数字让 AI 理解 |
| 🟣 大师级 | 前沿研究者 | Harness Engineering → 给 AI 设计工作环境和工具 |

每个术语还带**发音指南**（国际音标 + 中式发音）和**来龙去脉**（这个词怎么火起来的）。

### 为什么做这个

你去医院看病，医生说"你这个是肱骨外上髁炎"，你一脸懵。他再说"就是网球肘"，你秒懂。

科技新闻每天都在干第一件事。

Easy Read 做的就是"网球肘"这一步：**保留原文的信息量，换一套说人话的表达。**

### 架构

三个文件，各管一段：

| 文件 | 干什么的 |
|------|----------|
| `SKILL.md` | 核心流程和规则（Agent 读这个） |
| `scripts/generate_glossary.py` | 把 JSON 数据变成 HTML 页面 |
| `assets/glossary_template.html` | 页面长什么样 |

### 系统要求

- 任意 AI coding agent（Claude Code / Codex / Cursor / Cline 等）
- Python 3.7+
- 处理网页内容需要 agent 具备联网能力

---

## English

### What This Does

Ever been in one of these situations?

- AI article: "RAG-based Agentic Workflows achieve Context Engineering paradigm shift" → ???
- Medical report: "Elevated TSH, recommend thyroid function assessment" → panic
- Legal contract: "Force majeure events shall exempt joint and several liability" → just sign and pray
- Finance: "The fund's Sharpe ratio underperforms its benchmark's risk-adjusted alpha" → maybe I'll just keep my money in a sock

**Every word makes sense alone. Together, they're hieroglyphics.**

Easy Read translates any of those into plain language, then generates a **glossary with pronunciation guides, difficulty levels, and historical context** as a clean HTML page.

### Supported Domains

| | Domain | Typical Scenarios |
|---|--------|-------------------|
| 🤖 | AI / Tech | Tech news, product launches, dev blogs |
| 🏥 | Medical | Lab reports, drug labels, medical news |
| ⚖️ | Legal | Contracts, court rulings, legal news |
| 💰 | Finance | Earnings reports, fund prospectuses, economic analysis |
| 📚 | Academic | Cross-discipline papers, research reports |
| 📋 | Policy | Government white papers, regulatory docs |
| 🎮 | Gaming | Patch notes, game mechanics, guides |
| 🔗 | Crypto / Web3 | Whitepapers, DeFi terms |
| 🔧 | Hardware | Phone reviews, PC specs, benchmarks |
| 📖 | **Anything** | **If you can't understand it, we can translate it** |

### Key Features

- **Zero background needed**: don't know the field? That's the whole point
- **Auto domain detection**: figures out what field the content is from
- **Auto jargon detection**: catches specialist terms, acronyms, jargon from any domain
- **Clean HTML output**: difficulty levels, pronunciation guides, historical context
- **Throw anything at it**: text, files, URLs, PDFs, screenshots
- **Works with any agent**: Claude Code, Codex, Cursor, Cline, and more

### Installation

#### Claude Code (Recommended)

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

#### Other Agents

Easy Read is just SKILL.md (instructions) + a Python script (HTML generation). Works with any agent that can read files and run Python.

<details>
<summary><b>Codex (OpenAI)</b></summary>

```bash
git clone https://github.com/HeiGeAi/easy-read.git
# Add SKILL.md content to AGENTS.md or .codex/instructions.md
```
</details>

<details>
<summary><b>OpenClaw / DeskClaw</b></summary>

```bash
git clone https://github.com/HeiGeAi/easy-read.git ~/.openclaw/skills/easy-read
# SKILL.md format is compatible, works out of the box
```
</details>

<details>
<summary><b>Cursor</b></summary>

```bash
git clone https://github.com/HeiGeAi/easy-read.git
# Add SKILL.md content to .cursor/rules/easy-read.mdc
# Or put it in .cursorrules
```
</details>

<details>
<summary><b>Windsurf</b></summary>

```bash
git clone https://github.com/HeiGeAi/easy-read.git
# Add SKILL.md content to .windsurfrules
```
</details>

<details>
<summary><b>Cline (VS Code)</b></summary>

```bash
git clone https://github.com/HeiGeAi/easy-read.git
# Add SKILL.md content to .clinerules
# Or set as Custom Instructions in Cline settings
```
</details>

<details>
<summary><b>Aider</b></summary>

```bash
git clone https://github.com/HeiGeAi/easy-read.git
# Add SKILL.md to the read list in .aider.conf.yml
# Or use the --read flag at launch
aider --read easy-read/SKILL.md
```
</details>

<details>
<summary><b>GitHub Copilot</b></summary>

```bash
git clone https://github.com/HeiGeAi/easy-read.git
# Add SKILL.md content to .github/copilot-instructions.md
```
</details>

<details>
<summary><b>Continue (VS Code / JetBrains)</b></summary>

```bash
git clone https://github.com/HeiGeAi/easy-read.git
# Reference SKILL.md in customInstructions in .continue/config.yaml
# Or add content to .continuerules
```
</details>

<details>
<summary><b>Trae</b></summary>

```bash
git clone https://github.com/HeiGeAi/easy-read.git
# Add SKILL.md content to .trae/rules
```
</details>

<details>
<summary><b>Augment</b></summary>

```bash
git clone https://github.com/HeiGeAi/easy-read.git
# Reference SKILL.md in Augment's Instructions settings
```
</details>

<details>
<summary><b>Devin</b></summary>

Upload SKILL.md to Devin's Knowledge panel. Then say: "Follow the Easy Read workflow from Knowledge to process this article."
</details>

<details>
<summary><b>Generic (any agent)</b></summary>

```bash
git clone https://github.com/HeiGeAi/easy-read.git
```

Tell your agent: "Read `easy-read/SKILL.md` and follow the workflow to process this article."

Flow: Agent reads SKILL.md → analyzes article → generates JSON → runs Python script → outputs HTML.
</details>

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

If **your grandma wouldn't know the word**, it gets caught and explained:

🤖 **AI jargon**: Agent, LLM, RAG, Embedding... insider language that outsiders can't parse

🏥 **Medical gibberish**: ALT, TSH, HbA1c, MRI contrast... the numbers on your lab report that make you anxious

⚖️ **Legal speak**: force majeure, indemnification, arbitration... contract clauses you pretend to understand

💰 **Finance codes**: PE, ROE, convertible bonds, QE... terms that make you feel unworthy of managing money

📚 **Academic jargon**: p-value, confidence interval, meta-analysis... words that make you question your degree

🎮 **Gaming / hardware / crypto / policy docs**... any domain's specialist vocabulary

### Output Format

Each glossary = **300-word plain summary** + **term cards sorted by difficulty**.

| Level | Who gets it | Example |
|-------|------------|---------|
| 🟢 Entry | Everyone | API → A menu that lets software "order" from each other |
| 🔵 Intermediate | Tech-curious | Prompt Engineering → Learning how to talk to AI |
| 🟡 Professional | Practitioners | Context Window → How much AI can "remember" at once |
| 🔴 Expert | Deep tech | Embedding → Turning text into numbers for AI |
| 🟣 Master | Researchers | Harness Engineering → Designing AI's work environment |

Every term also includes **pronunciation guide** (IPA + Chinese phonetics) and **historical context** (how the term came to be).

### Why This Exists

You go to the doctor. They say "you have lateral epicondylitis." You panic. Then they say "it's tennis elbow." Instant relief.

Tech news, legal contracts, financial reports, medical results, academic papers... they all do the first thing to people every single day.

Easy Read is the "tennis elbow" step: **keep all the information, swap in words real people actually use.**

### Architecture

Three files, one job each:

| File | What it does |
|------|-------------|
| `SKILL.md` | Core workflow and rules (agent reads this) |
| `scripts/generate_glossary.py` | Turns JSON data into an HTML page |
| `assets/glossary_template.html` | How the page looks |

### Requirements

- Any AI coding agent (Claude Code / Codex / Cursor / Cline, etc.)
- Python 3.7+
- Web fetching capability for URL inputs

---

## 致谢 | Credits

[@blakexu](https://github.com/blakexu) 做的。灵感来源：给我妈解释什么是 AI 的那个下午。

## 许可证 | License

MIT. 随便用，随便改，随便分享。
