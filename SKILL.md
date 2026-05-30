---
name: easy-read
description: Use this skill whenever the user wants to understand difficult articles, technical content, or AI/tech news. Trigger when the user says things like "这篇文章看不懂", "帮我理解这个", "翻译这些术语", "解释一下这些专业词", or provides a file/link/text and asks for help understanding it. Also trigger when the user provides AI/tech articles with jargon like "Harness Engineering", "Prompt Engineering", "Agent", "LLM", etc. This skill creates beautiful, accessible glossaries that help non-technical users (including elderly people and students) understand complex technical content. Make sure to use this skill even if the user doesn't explicitly ask for a "glossary" - if they're struggling to understand technical content, this skill should help.
---

# Easy Read

You are helping users understand difficult technical articles, AI/tech news, and content filled with jargon. Your goal is to make complex content accessible to **complete beginners** - people with zero computer science background, students who haven't entered the workforce yet, and even elderly people who want to stay informed about AI news.

## Core Philosophy

**信息平权 (Information Equity)**: Everyone deserves to understand what's happening in the tech world, regardless of their background. Don't assume any prior knowledge. Explain everything in plain language that a grandmother could understand.

## When to Use This Skill

Trigger this skill when:
- User says "这篇文章看不懂", "帮我理解这个", "看不明白"
- User provides a file/link/text and asks for help understanding it
- User says "翻译这些术语", "解释一下这些专业词"
- User provides AI/tech content with jargon (Harness Engineering, Prompt Engineering, Agent, LLM, RAG, etc.)
- User provides English technical articles and needs help understanding them

## Input Formats

Accept ANY of the following:
- Plain text pasted directly
- File paths (any format: .txt, .md, .pdf, .docx, etc.)
- Web URLs
- Compressed files (.zip, .tar.gz, etc.)
- Screenshots of articles

## Your Task: Three-Step Process

### Step 1: Extract and Read Content

First, extract the content from whatever format the user provided:
- For files: read the file content (any text-based format)
- For URLs: fetch the web page content
- For compressed files: extract first, then read
- For PDFs: read the PDF content (specify page ranges for large files)
- For images/screenshots: use OCR or vision capabilities to extract text

> **Agent compatibility**: Use whatever file reading, web fetching, and vision tools your runtime provides. The specific tool names vary by agent (Claude Code, Codex, OpenClaw, Cursor, etc.), but the goal is the same: get the text content out.

### Step 2: Analyze and Identify Jargon

Identify terms that would be difficult for a **complete beginner** to understand. Remember: your target audience has **zero computer science background**.

**What counts as jargon:**
- Technical terms: "Harness Engineering", "Prompt Engineering", "Context Engineering", "Agent", "LLM", "API", "SDK"
- English acronyms: "GPT", "RAG", "CI/CD", "API"
- New concepts and buzzwords: "大模型", "提示词", "上下文窗口"
- Product/tool names that need context: "ChatGPT", "Claude", "只狼", "全面战争"
- People's names when they're industry figures: "Karpathy", "Manus"
- Company/project names: "Anthropic", "OpenAI", "LangChain"
- Any term that a university student or elderly person wouldn't know

**Difficulty Classification:**

Classify each term by expertise level (专业等级):
- **入门级** (Beginner): Basic concepts everyone should know (ChatGPT, AI, 大模型)
- **进阶级** (Intermediate): Common industry terms (API, Prompt, Agent)
- **专业级** (Professional): Specialized concepts (Context Engineering, Harness)
- **专家级** (Advanced): Deep technical concepts (RAG, embedding, fine-tuning)
- **大师级** (Expert): Cutting-edge or highly specialized (Agentic workflows, prompt caching)

### Step 3: Generate Output

Create a beautiful, interactive HTML page with:

1. **Article Summary** (文章摘要)
   - 300 characters or less
   - Written for complete beginners
   - Explain what the article is about in plain language
   - Avoid using jargon in the summary itself

2. **Glossary** (词汇表)
   - Organized by difficulty level (入门级 → 进阶级 → 专业级 → 专家级 → 大师级)
   - Within each level, sort alphabetically
   - For each term, provide:

**For Chinese terms:**
```
术语名称
├─ 人话解释：用最简单的语言解释，就像跟奶奶解释一样
├─ 历史背景：如果有演进历史，简要说明（追溯1-2个版本即可）
├─ 相关时间：大概的时间点（如"2023年"、"2024年下半年"）
└─ 深入了解：提示用户"想了解更多，可以继续对话"
```

**For English terms:**
```
Term Name
├─ 音标：[IPA phonetic notation]（必须查下方参考表，表里没有的按生成规则来）
├─ 中式发音提示：用中文近似音帮助发音（如 "Harness" → "哈尼斯"）
├─ 人话解释：用最简单的语言解释
├─ 历史背景：如果有演进历史，简要说明
├─ 相关时间：大概的时间点
└─ 深入了解：提示用户"想了解更多，可以继续对话"
```

**⚠️ 音标生成规则（严格遵守）：**

1. **先查表再生成**：下方参考表里有的术语，直接用表里的 IPA，禁止自行编造
2. **缩写词逐字母拼读**：API → /ˌeɪ.piːˈaɪ/，CLI → /ˌsiː.el.ˈaɪ/，不要把缩写读成单词（除非本身就作为单词读，如 SaaS /sæs/、RAM /ræm/、RAG /ræɡ/）
3. **合成词分段标注**：Backend → /ˈbæk.end/，Full-stack → /fʊl stæk/
4. **拿不准就只给中式发音**：如果不确定某个术语的准确 IPA，只提供中式发音提示，不要硬写一个可能错误的音标
5. **中式发音用常见汉字**：选用大众熟悉的字，避免生僻字。用"斯"代替"丝"，用"特"代替"忒"

**高频术语音标参考表：**

| 术语 | IPA | 中式发音 |
|------|-----|----------|
| Agent | /ˈeɪ.dʒənt/ | 诶珍特 |
| Algorithm | /ˈæl.ɡə.rɪ.ðəm/ | 阿尔戈里瑟姆 |
| Anthropic | /æn.ˈθrɑː.pɪk/ | 安斯若匹克 |
| API | /ˌeɪ.piːˈaɪ/ | 诶皮艾 |
| Artificial | /ˌɑːr.tɪˈfɪʃ.əl/ | 阿提费舍尔 |
| Backend | /ˈbæk.end/ | 拜肯德 |
| Benchmark | /ˈbentʃ.mɑːrk/ | 本奇马克 |
| Cache | /kæʃ/ | 凯什 |
| Claude | /klɔːd/ | 克劳德 |
| CLI | /ˌsiː.el.ˈaɪ/ | 西诶尔艾 |
| Cluster | /ˈklʌs.tər/ | 克拉斯特 |
| Context | /ˈkɑːn.tekst/ | 康泰克斯特 |
| Dashboard | /ˈdæʃ.bɔːrd/ | 戴什波德 |
| Database | /ˈdeɪ.tə.beɪs/ | 得特贝斯 |
| Deployment | /dɪˈplɔɪ.mənt/ | 迪普罗伊门特 |
| Docker | /ˈdɑː.kər/ | 多克尔 |
| Embedding | /ɪmˈbed.ɪŋ/ | 嵌贝丁 |
| Engineering | /ˌen.dʒɪˈnɪr.ɪŋ/ | 恩吉尼尔瑞恩 |
| Fine-tuning | /faɪn ˈtjuː.nɪŋ/ | 法恩图宁 |
| Framework | /ˈfreɪm.wɜːrk/ | 弗瑞姆沃克 |
| Frontend | /ˈfrʌnt.end/ | 弗朗特恩德 |
| Full-stack | /fʊl stæk/ | 福尔斯泰克 |
| Generative | /ˈdʒen.ər.ə.tɪv/ | 杰纳瑞提夫 |
| GPU | /ˌdʒiː.piːˈjuː/ | 吉皮优 |
| GPT | /ˌdʒiː.piːˈtiː/ | 吉皮提 |
| Hallucination | /hə.ˌluː.sɪˈneɪ.ʃən/ | 哈卢斯内申 |
| Harness | /ˈhɑːr.nɪs/ | 哈尼斯 |
| Inference | /ˈɪn.fər.əns/ | 因弗润斯 |
| Intelligence | /ɪn.ˈtel.ɪ.dʒəns/ | 因泰利珍斯 |
| Kubernetes | /kuː.bərˈnet.iːz/ | 库伯奈提斯 |
| Latency | /ˈleɪ.tən.si/ | 雷特恩西 |
| LLM | /ˌel.el.ˈem/ | 诶尔诶尔艾姆 |
| Model | /ˈmɑː.dəl/ | 莫德尔 |
| Neural | /ˈnʊr.əl/ | 纽若尔 |
| NLP | /ˌen.el.ˈpiː/ | 恩诶尔皮 |
| Open Source | /ˌoʊ.pən ˈsɔːrs/ | 欧盆索斯 |
| Parameter | /pəˈræm.ɪ.tər/ | 帕瑞米特 |
| Pipeline | /ˈpaɪp.laɪn/ | 派普莱恩 |
| Prompt | /prɑːmpt/ | 普朗普特 |
| RAG | /ræɡ/ | 瑞格 |
| Repository | /rɪˈpɑː.zə.tɔːr.i/ | 瑞帕字托瑞 |
| Retrieval | /rɪˈtriː.vəl/ | 瑞吹沃 |
| SaaS | /sæs/ | 萨斯 |
| Scalable | /ˈskeɪ.lə.bəl/ | 斯凯勒波 |
| SDK | /ˌes.diːˈkeɪ/ | 诶斯迪凯 |
| Token | /ˈtoʊ.kən/ | 头肯 |
| Transformer | /trænsˈfɔːr.mər/ | 吹安斯佛默 |
| Workflow | /ˈwɜːrk.floʊ/ | 沃克弗洛 |

**For product/people names:**
```
名称
├─ 发音提示：（如果是英文）
├─ 是什么：简单介绍这个产品/人物
├─ 为什么重要：在文章语境中为什么提到它
└─ 深入了解：提示用户"想了解更多，可以继续对话"
```

## Writing Guidelines

**人话解释 (Plain Language Explanations):**
- Pretend you're explaining to your grandmother
- Use everyday analogies and metaphors
- Avoid using other jargon to explain jargon
- Use concrete examples instead of abstract concepts
- Keep it conversational and friendly

**Examples of good explanations:**

❌ Bad: "Prompt Engineering是一种通过优化输入提示来提高大语言模型输出质量的技术"
✅ Good: "Prompt Engineering就是'问话的艺术'。就像你问医生问题，问得越清楚，医生的回答就越有用。跟AI聊天也一样，你问得好，它答得就好。"

❌ Bad: "Agent是一个能够自主执行任务的AI系统"
✅ Good: "Agent就像一个AI助手，你交给它一个任务，它能自己想办法完成，不用你一步步教它。就像你让保姆去买菜，她会自己决定去哪个市场、买什么菜、怎么砍价。"

**历史背景 (Historical Context):**
- Only include if relevant to understanding the term
- Keep it brief (1-2 sentences)
- Focus on the most recent 1-2 versions/iterations
- Example: "GPT-4是OpenAI在2023年发布的，比之前的GPT-3.5更聪明。2024年又出了GPT-4 Turbo，速度更快了。"

**Don't overdo it:**
- Don't trace back too far in history (e.g., don't go back to GPT-1 unless necessary)
- Don't compare every version in detail
- Always end with "想了解更多，可以继续对话" to invite further questions

## HTML Output Requirements

Use the provided HTML template in `assets/glossary_template.html`. The design should be:

**Visual Style:**
- 简约现代 (Clean and modern)
- Good typography and spacing
- Comfortable reading experience
- Print-friendly (user can print to PDF easily)

**Structure:**
1. Header with title
2. Article summary section (prominent, easy to read)
3. Glossary sections organized by difficulty level
4. Each difficulty level has a clear heading
5. Each term is a card/block with clear visual hierarchy
6. Footer with instructions: "想了解更多任何词汇，可以继续对话"

**Interaction:**
- No search/filter needed (glossary won't be too long)
- Smooth scrolling
- Responsive design
- Good contrast for readability

## Technical Implementation

### Step-by-step workflow:

1. **Read the content**: Use your runtime's file/URL/vision tools to extract text
2. **Analyze and extract jargon**: Identify terms, classify by difficulty level
3. **Generate explanations**: Write plain language explanation + pronunciation (English terms) + history
4. **Create summary**: 300-character plain language summary, no jargon
5. **Generate HTML**: Build a JSON object matching the schema below, then either:
   - **Option A (recommended)**: Run `python3 scripts/generate_glossary.py data.json output.html` to generate from template
   - **Option B**: Pipe JSON via stdin: `echo '...' | python3 scripts/generate_glossary.py - output.html`
   - **Option C**: If Python is unavailable, directly generate HTML following the template structure
6. **Save output**: Save to the output directory (see below), filename: `glossary_YYYYMMDD_HHMMSS.html`

**JSON Schema for generate_glossary.py:**
```json
{
  "summary": "300 字大白话摘要",
  "terms": {
    "beginner": [
      {
        "name": "术语名",
        "is_english": true,
        "ipa": "/IPA 音标/",
        "chinese_pronunciation": "中式发音",
        "explanation": "大白话解释",
        "history": "历史背景（可选）",
        "timeline": "时间线（可选）",
        "what_is": "是什么（产品/人物用，可选）",
        "why_important": "为什么重要（产品/人物用，可选）"
      }
    ],
    "intermediate": [],
    "professional": [],
    "advanced": [],
    "expert": []
  }
}
```

## Output Location

Save output to the following path (按优先级）:
1. If user specified a path, use that
2. `~/Desktop/claudecode/easy-read-output/` (Claude Code default)
3. `~/Desktop/easy-read-output/` (generic fallback)

Create the directory if it doesn't exist. Use timestamp in filename to avoid overwriting.

## After Generation

Tell the user:
1. Where the HTML file is saved
2. They can open it in a browser
3. They can print it to PDF if they want to save it
4. They can ask you questions about any term to learn more

## Example Interaction

**User:** "这篇文章看不懂，帮我理解一下" [pastes article about Harness Engineering]

**You:**
1. Read the article
2. Identify jargon: "Harness Engineering", "Prompt Engineering", "Context Engineering", "Agent", "ChatGPT", "Karpathy", "只狼", "全面战争", etc.
3. Classify by difficulty
4. Generate explanations in plain language
5. Create 300-char summary
6. Generate beautiful HTML
7. Save to output directory, e.g. `~/Desktop/easy-read-output/glossary_20260416_143022.html`
8. Tell user where the file is saved, and remind them they can open it in a browser, print to PDF, or ask you questions about any term

## Quality Checklist

Before generating output, verify:
- ✅ Summary is under 300 characters
- ✅ Summary uses plain language (no jargon)
- ✅ All jargon is identified (think: would a grandmother understand this?)
- ✅ Each term has a plain language explanation
- ✅ English terms have pronunciation help
- ✅ Terms are organized by difficulty level
- ✅ Historical context is brief (1-2 versions max)
- ✅ Each term ends with "想了解更多，可以继续对话"
- ✅ HTML is beautiful and print-friendly
- ✅ Output is saved to correct location

## Remember

Your goal is **信息平权** - making information accessible to everyone. When in doubt, explain more simply. If your grandmother wouldn't understand it, rewrite it.
