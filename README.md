# Easy Read

A Claude Code skill that transforms technical articles into accessible content — turning jargon-filled AI/tech news into plain language anyone can understand.

## What This Does

**Easy Read** helps non-technical people understand complex technical content. It automatically identifies difficult terms, creates beautiful glossaries with plain-language explanations, and provides article summaries that make sense to complete beginners.

Here's what makes it special:

https://github.com/user-attachments/assets/[demo-video-placeholder]

### Key Features

- **Zero Technical Background Required** — Designed for grandparents, students, and anyone curious about tech news
- **Smart Jargon Detection** — Automatically identifies terms that need explanation (AI concepts, acronyms, buzzwords)
- **Beautiful Output** — Clean, modern HTML glossaries with difficulty levels, pronunciation guides, and historical context
- **Multiple Input Formats** — Accepts text, files, URLs, PDFs, screenshots — anything you throw at it
- **信息平权 (Information Equity)** — Everyone deserves to understand what's happening in tech, regardless of background

## Installation

### Via Plugin Marketplace (Recommended)

Install directly from Claude Code:

```bash
/plugin marketplace add [your-username]/easy-read
/plugin install easy-read@easy-read
```

Then use it by typing `/easy-read` in Claude Code.

### Manual Installation

Copy the skill files to your Claude Code skills directory:

```bash
# Clone the repository
git clone https://github.com/[your-username]/easy-read.git ~/.claude/skills/easy-read
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

## Usage

### Basic Usage

```
/easy-read

> "这篇文章看不懂" [paste article text]
```

The skill will:

1. Extract and analyze the content
2. Identify all technical terms and jargon
3. Generate plain-language explanations for each term
4. Create a beautiful HTML glossary with:
   - Difficulty levels (入门级 → 大师级)
   - Pronunciation guides (IPA + Chinese phonetics)
   - Historical context (how the term evolved)
   - A 300-word article summary
5. Save to your Desktop in `claudecode/easy-read-output/`
6. Open it in your browser

### Supported Input Formats

**Text:**
```
/easy-read

> "帮我理解这个：[paste article]"
```

**Files:**
```
/easy-read

> "解释这个文件：~/Documents/ai-article.pdf"
```

**URLs:**
```
/easy-read

> "这篇文章看不懂：https://example.com/article"
```

**Screenshots:**
```
/easy-read

> "看不明白这个" [attach screenshot]
```

## What Gets Explained

The skill identifies terms that would confuse someone with **zero computer science background**:

### AI/ML Concepts
- Prompt Engineering, Context Engineering, Harness Engineering
- Agent, LLM, RAG, Fine-tuning
- Embedding, Token, Context Window

### Technical Terms
- API, SDK, CLI, Framework
- Backend, Frontend, Full-stack
- Open Source, Repository, Deployment

### Acronyms & Buzzwords
- GPT, AI, ML, NLP
- SaaS, PaaS, IaaS
- 大模型, 提示词, 上下文

### Cultural References
- Game references (Dota, League of Legends)
- Memes and internet culture
- Historical tech events

## Output Format

Each glossary includes:

### Article Summary
A 300-word plain-language summary that captures the key points without assuming any technical knowledge.

### Glossary by Difficulty Level

**入门级 (Entry Level)** — Basic concepts you might encounter in daily life
- Example: "API" → "应用程序接口 — 就像餐厅的菜单，让不同软件之间能互相'点菜'交流"

**进阶级 (Intermediate)** — Requires some context
- Example: "Prompt Engineering" → "提示词工程 — 学会怎么跟AI说话，让它更懂你的意思"

**专业级 (Professional)** — Industry practitioners use these
- Example: "Context Window" → "上下文窗口 — AI一次能'记住'多少内容的限制"

**专家级 (Expert)** — Deep technical concepts
- Example: "Embedding" → "嵌入向量 — 把文字转成数字，让AI能理解和比较"

**大师级 (Master)** — Cutting-edge research
- Example: "Harness Engineering" → "驾驭工程 — 设计AI的工作环境和工具，而不是写更长的提示词"

### For Each Term

- **Chinese Name** — 中文名称
- **English Name** — Original term
- **Pronunciation** — IPA phonetic + 中式发音提示
- **Plain Explanation** — What it means in everyday language
- **Historical Context** — How the term evolved (1-2 versions back)
- **Timeline** — When it became popular

## Architecture

This skill uses a **progressive workflow**:

| File | Purpose | When Used |
|------|---------|-----------|
| `SKILL.md` | Core workflow and rules | Always (skill invocation) |
| `scripts/generate_glossary.py` | HTML generation logic | Phase 3 (output creation) |
| `assets/glossary_template.html` | Visual template | Phase 3 (output creation) |

The design follows the principle: "Make complex things accessible, not simplified."

## Philosophy

This skill was born from the belief that:

1. **Information should be accessible to everyone.** Your grandmother should be able to read AI news without feeling lost.

2. **Jargon is a barrier, not a feature.** Technical terms exist for precision, but they shouldn't exclude people from understanding important developments.

3. **Context matters.** Knowing where a term came from helps you understand where it's going.

4. **Beautiful design aids comprehension.** A well-designed glossary isn't just pretty — it helps you learn.

## Requirements

- [Claude Code](https://claude.ai/claude-code) CLI
- Python 3.7+ (for glossary generation)
- For web content: `web-access` skill or similar

## Example Output

When you process an article about "Harness Engineering", you'll get a glossary that explains:

- **Harness Engineering** (大师级) — "驾驭工程：不是教AI怎么做，而是给它设计好工作环境和工具"
- **Prompt Engineering** (进阶级) — "提示词工程：学会跟AI说话的艺术"
- **Agent** (专业级) — "智能体：能自己做决策、调用工具的AI程序"
- **Context Window** (专家级) — "上下文窗口：AI一次能'看'多少内容"

Plus a 300-word summary explaining the article's main points in plain language.

## Credits

Created by [@blakexu](https://github.com/blakexu) with Claude Code.

Inspired by the belief that everyone deserves to understand the technology shaping our world.

## License

MIT — Use it, modify it, share it.
