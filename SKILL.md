---
name: easy-read
description: Use this skill whenever the user wants to understand difficult articles or content filled with jargon from ANY field. Covers AI/tech, medical, legal, financial, academic, policy, gaming, crypto, hardware, and more. Trigger when the user says things like "这篇文章看不懂", "帮我理解这个", "翻译这些术语", "这个报告看不明白", "体检报告什么意思", "合同条款看不懂", or provides a file/link/text and asks for help understanding it. This skill creates beautiful, accessible glossaries that help non-expert users understand complex content from any domain. If someone is struggling to understand something, this skill should help.
---

# Easy Read

You are helping users understand difficult content filled with jargon from **any field**. Your goal is to make complex content accessible to **complete beginners** in that field, regardless of their background.

## Core Philosophy

**信息平权 (Information Equity)**: Every piece of knowledge locked behind jargon is a door slammed in someone's face. Your job is to open it. Don't assume any prior knowledge. Explain everything in plain language that a grandmother could understand.

## When to Use This Skill

Trigger this skill when the user is struggling to understand content from **any domain**:

- **AI / 科技**："这篇 AI 文章看不懂"、文章里全是 Agent、LLM、RAG
- **医学 / 健康**："体检报告什么意思"、"这个药的说明书看不懂"、医学论文
- **法律**："合同条款看不懂"、"判决书什么意思"、法律新闻
- **金融 / 财经**："财报看不明白"、"基金说明书太专业了"、经济分析
- **学术论文**："这篇论文太难了"、跨学科论文、学术黑话
- **政策 / 政府文件**："这个政策文件说的是什么"、白皮书、红头文件
- **硬件 / 数码**："手机评测看不懂参数"、电脑配置推荐
- **游戏**："更新日志看不懂"、游戏机制术语、攻略
- **区块链 / Web3**："白皮书看不懂"、DeFi 术语
- **通用**：任何用户说"看不懂"、"帮我理解"、"翻译这些术语"的场景

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

First, **detect the domain** of the content (AI/tech, medical, legal, financial, academic, policy, gaming, crypto, hardware, etc.). This determines what counts as "jargon" and what explanatory style to use.

Identify terms that would be difficult for a **complete beginner in that domain** to understand.

**What counts as jargon (by domain):**

🤖 **AI / 科技**
- Technical terms: Harness Engineering, Prompt Engineering, Agent, LLM, API, SDK
- Acronyms: GPT, RAG, CI/CD, NLP
- Buzzwords: 大模型, 提示词, 上下文窗口
- Products/people: ChatGPT, Claude, Karpathy, Anthropic, OpenAI

🏥 **医学 / 健康**
- 疾病名称: 肱骨外上髁炎（网球肘）、甲状腺功能亢进
- 检查指标: ALT、AST、TSH、HbA1c、CT、MRI
- 药物术语: 缓释片、肠溶胶囊、生物等效性
- 手术/治疗: 微创手术、介入治疗、放疗、靶向药

⚖️ **法律**
- 法律概念: 不可抗力、善意取得、连带责任、诉讼时效
- 合同术语: 违约金、免责条款、仲裁、管辖权
- 诉讼用语: 上诉、再审、执行、保全

💰 **金融 / 财经**
- 指标术语: PE、PB、ROE、毛利率、净利润率
- 产品名词: ETF、LOF、可转债、期权、对冲
- 宏观概念: 量化宽松、降准降息、CPI、PPI

📚 **学术论文**
- 研究方法: 对照实验、双盲、p值、置信区间、meta分析
- 论文结构: Abstract、Methodology、Discussion、Peer Review
- 统计术语: 回归分析、标准差、显著性、相关系数

📋 **政策 / 政府文件**
- 政策用语: 供给侧改革、双循环、新质生产力、专精特新
- 机构缩写: 发改委、工信部、证监会、央行

🎮 **游戏**
- 游戏机制: DPS、坦克、奶妈、Buff/Debuff、CD、刷副本
- 竞技术语: ELO、MMR、段位、赛季
- 特定游戏: 只狼、艾尔登法环、全面战争

🔗 **区块链 / Web3**
- 核心概念: 智能合约、Gas Fee、Layer2、跨链、质押
- DeFi 术语: 流动性池、AMM、TVL、Yield Farming
- 缩写: DAO、NFT、DEX、CEX

🔧 **硬件 / 数码**
- 处理器: 制程、核心数、主频、功耗、TDP
- 显示: 分辨率、刷新率、OLED、Mini-LED
- 存储: SSD、NVMe、DRAM、UFS

**通用规则**: 以上只是常见示例。对于**任何领域**，识别标准都是同一个：**你奶奶看不懂的词，就该解释。**

**Difficulty Classification:**

Classify each term by expertise level (专业等级). The examples below are cross-domain:
- **入门级** (Beginner): 日常能碰到的基础概念（AI、体检、合同、基金）
- **进阶级** (Intermediate): 关注这个领域就会遇到的词（API、转氨酶、违约金、PE）
- **专业级** (Professional): 从业者常用（Context Engineering、MRI 增强扫描、仲裁条款、对冲）
- **专家级** (Advanced): 深度专业概念（RAG、HbA1c 达标率、善意取得、可转债定价）
- **大师级** (Expert): 前沿/极度专业（Agentic workflows、基因编辑 CRISPR、反垄断经济学分析）

### Step 3: Generate Output

Create a beautiful, static HTML page with:

1. **Article Summary** (文章摘要)
   - 控制在一小段：中文约 300 字以内，英文约 60 词以内
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

1. **先查表再生成**：下方参考表按领域分组（科技 / 医学 / 法律 / 金融 / 学术），先在对应领域表里找，有就直接用表里的 IPA，禁止自行编造。复数或变形词先还原成词典原形再查（Agents 查 Agent、Embeddings 查 Embedding）
2. **缩写词逐字母拼读**：API → /ˌeɪ.piːˈaɪ/，CLI → /ˌsiː.el.ˈaɪ/，不要把缩写读成单词（除非本身就作为单词读，如 SaaS /sæs/、RAM /ræm/、RAG /ræɡ/）
3. **合成词分段标注**：Backend → /ˈbæk.end/，Full-stack → /fʊl stæk/
4. **统一用美式音**：全表按美式发音（rhotic /r/、tune 用 /tuː/ 不用 /tjuː/），别混英式
5. **拿不准就只给中式发音**：如果不确定某个术语的准确 IPA，只提供中式发音提示，不要硬写一个可能错误的音标
6. **中式发音按音节对应，别套万能字**：
   - 选用大众熟悉的字，避免生僻字。用"斯"代替"丝"，用"特"代替"忒"
   - **/r/ 开头别一律用"瑞"**（"瑞"读 rui 带 ui 音）：/ræ/ 用"拉"（RAG → 拉格）、/rɪ/ 用"瑞"、/reɪ/ 才用"瑞"
   - **/tr/ 别用"吹"**（"吹"是 ch 音）：trans 用"特兰斯"（Transformer → 特兰斯佛默）、tri 用"特里"（Retrieval → 瑞特里沃）
   - **/ɪŋ/ 结尾要收鼻音**：用"英""宁""玲"，别用"恩"（Engineering → 恩吉尼尔英）
   - 每标一个中式发音，在心里读一遍，跟英文原词对不上就换字

**高频术语音标参考表 · AI / 科技：**

| 术语 | IPA | 中式发音 |
|------|-----|----------|
| Agent | /ˈeɪ.dʒənt/ | 诶珍特 |
| Algorithm | /ˈæl.ɡə.rɪ.ðəm/ | 阿尔戈里瑟姆 |
| Anthropic | /ænˈθrɑ.pɪk/ | 安斯若匹克 |
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
| Embedding | /ɪmˈbed.ɪŋ/ | 因贝丁 |
| Engineering | /ˌen.dʒɪˈnɪr.ɪŋ/ | 恩吉尼尔英 |
| Fine-tuning | /faɪn ˈtuː.nɪŋ/ | 法恩图宁 |
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
| Kubernetes | /kuː.bərˈneɪ.tiːz/ | 库伯奈提斯 |
| Latency | /ˈleɪ.tən.si/ | 雷特恩西 |
| LLM | /ˌel.el.ˈem/ | 诶尔诶尔艾姆 |
| Model | /ˈmɑː.dəl/ | 莫德尔 |
| Neural | /ˈnʊr.əl/ | 纽若尔 |
| NLP | /ˌen.el.ˈpiː/ | 恩诶尔皮 |
| Open Source | /ˌoʊ.pən ˈsɔːrs/ | 欧盆索斯 |
| Parameter | /pəˈræm.ɪ.tər/ | 帕拉米特 |
| Pipeline | /ˈpaɪp.laɪn/ | 派普莱恩 |
| Prompt | /prɑːmpt/ | 普朗普特 |
| RAG | /ræɡ/ | 拉格 |
| Repository | /rɪˈpɑː.zə.tɔːr.i/ | 瑞帕泽托瑞 |
| Retrieval | /rɪˈtriː.vəl/ | 瑞特里沃 |
| SaaS | /sæs/ | 萨斯 |
| Scalable | /ˈskeɪ.lə.bəl/ | 斯凯勒波 |
| SDK | /ˌes.diːˈkeɪ/ | 诶斯迪凯 |
| Token | /ˈtoʊ.kən/ | 头肯 |
| Transformer | /trænsˈfɔːr.mər/ | 特兰斯佛默 |
| Workflow | /ˈwɜːrk.floʊ/ | 沃克弗洛 |

**高频术语音标参考表 · 医学 / 健康：**

| 术语 | IPA | 中式发音 |
|------|-----|----------|
| Aneurysm | /ˈæn.jə.rɪ.zəm/ | 安尼瑞森 |
| Antibiotic | /ˌæn.ti.baɪˈɑː.tɪk/ | 安提拜阿提克 |
| Arrhythmia | /əˈrɪð.mi.ə/ | 阿里德米亚 |
| Biopsy | /ˈbaɪ.ɑːp.si/ | 拜阿普西 |
| Catheter | /ˈkæθ.ɪ.tər/ | 卡西特 |
| CRISPR | /ˈkrɪs.pər/ | 克里斯珀 |
| Fibrillation | /ˌfɪb.rɪˈleɪ.ʃən/ | 菲布里雷申 |
| Metastasis | /məˈtæs.tə.sɪs/ | 梅塔斯塔西斯 |
| MRI | /ˌem.ɑːrˈaɪ/ | 诶姆阿艾 |
| Placebo | /pləˈsiː.boʊ/ | 普拉西波 |

**高频术语音标参考表 · 法律：**

| 术语 | IPA | 中式发音 |
|------|-----|----------|
| Arbitration | /ˌɑːr.bɪˈtreɪ.ʃən/ | 阿比特雷申 |
| Fiduciary | /fɪˈduː.ʃi.er.i/ | 菲杜舍瑞 |
| Indemnification | /ɪnˌdem.nɪ.fɪˈkeɪ.ʃən/ | 因德姆尼菲凯申 |
| Jurisdiction | /ˌdʒʊr.ɪsˈdɪk.ʃən/ | 朱瑞斯迪克申 |
| Liability | /ˌlaɪ.əˈbɪl.ə.ti/ | 莱阿比勒提 |
| Plaintiff | /ˈpleɪn.tɪf/ | 普雷恩提夫 |
| Subpoena | /səˈpiː.nə/ | 萨皮那 |

**高频术语音标参考表 · 金融 / 财经：**

| 术语 | IPA | 中式发音 |
|------|-----|----------|
| Amortization | /ˌæm.ər.tɪˈzeɪ.ʃən/ | 阿摩提泽申 |
| Derivative | /dɪˈrɪv.ə.tɪv/ | 迪瑞沃提夫 |
| Dividend | /ˈdɪv.ɪ.dend/ | 迪维登德 |
| EBITDA | /ɪˈbɪt.dɑː/ | 伊比特达 |
| Equity | /ˈek.wɪ.ti/ | 埃奎提 |
| Leverage | /ˈlev.ər.ɪdʒ/ | 列沃瑞吉 |
| Portfolio | /pɔːrtˈfoʊ.li.oʊ/ | 波特佛里欧 |

**高频术语音标参考表 · 学术 / 研究：**

| 术语 | IPA | 中式发音 |
|------|-----|----------|
| Correlation | /ˌkɔːr.əˈleɪ.ʃən/ | 科瑞雷申 |
| Empirical | /ɪmˈpɪr.ɪ.kəl/ | 因皮瑞口 |
| Hypothesis | /haɪˈpɑː.θə.sɪs/ | 海帕思西斯 |
| Methodology | /ˌmeθ.əˈdɑː.lə.dʒi/ | 迈瑟多罗吉 |
| Paradigm | /ˈpær.ə.daɪm/ | 帕拉戴姆 |
| Qualitative | /ˈkwɑː.lə.teɪ.tɪv/ | 库阿勒泰提夫 |

> 以上非科技领域同样适用音标规则：先查表，表里没有的按规则生成，拿不准只给中式发音。

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
2. **Domain overview bar** (涉及领域概览): emoji tag 横排展示本文涉及的领域和术语数量，让用户一眼扫到全貌
3. Article summary section (prominent, easy to read)
4. Glossary sections organized by difficulty level
5. Each difficulty level has a clear heading
6. Each term is a card/block with clear visual hierarchy
7. Footer with instructions: "想了解更多任何词汇，可以继续对话"

**Static delivery:**
- No search/filter or runtime JavaScript needed (glossary won't be too long)
- No animations or scrolling effects; the full page is readable immediately
- Responsive design
- Good contrast for readability

**术语数量控制：** 一般控制在 15-30 个术语。如果文章术语特别多，优先保留对理解主旨最关键的，其余可在结尾一句话带过（提示用户「还有其他词想问随时说」），别硬塞几十张卡片把页面撑得又臭又长。

## Technical Implementation

### Step-by-step workflow:

1. **Read the content**: Use your runtime's file/URL/vision tools to extract text
2. **Analyze and extract jargon**: Identify terms, classify by difficulty level
3. **Generate explanations**: Write plain language explanation + pronunciation (English terms) + history
4. **Create summary**: plain language summary (中文约 300 字 / 英文约 60 词以内), no jargon
5. **Generate HTML**: Build a JSON object matching the schema below, then either:
   - **Option A (recommended)**: Run `python3 scripts/generate_glossary.py data.json output.html` to generate from template
   - **Option B**: Pipe JSON via stdin: `echo '...' | python3 scripts/generate_glossary.py - output.html`
   - **Option C**: If Python is unavailable, generate the HTML directly. Read `assets/glossary_template.html`, replace the three placeholders `{{DOMAIN_OVERVIEW}}`、`{{SUMMARY}}`、`{{GLOSSARY_SECTIONS}}` with your rendered HTML fragments, and reuse the same CSS classes the script emits: 每个术语用 `<article class="entry">`，难度分组用 `<section class="chapter level-beginner">`（等级类名 `level-beginner`、`level-intermediate`、`level-professional`、`level-advanced`、`level-expert`），音标用 `<span class="ipa" lang="en">`，中式发音用 `<span class="cn-phon">`。务必对所有文本做 HTML 转义。
6. **Save output**: Save to the output directory (see below), filename: `glossary_YYYYMMDD_HHMMSS.html`

**JSON Schema for generate_glossary.py:**
```json
{
  "summary": "300 字大白话摘要",
  "domains": [
    {"emoji": "🤖", "name": "AI / 科技", "count": 5},
    {"emoji": "🏥", "name": "医学", "count": 2}
  ],
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

`domains` 字段说明：列出本文涉及的所有领域，每个领域带 emoji、名称和术语数量。会在词汇表顶部渲染成一排标签，用户一眼就能看出这篇文章涉及哪些领域。常用 emoji 对照：🤖 AI/科技、🏥 医学、⚖️ 法律、💰 金融、📚 学术、📋 政策、🎮 游戏、🔗 区块链、🔧 硬件。

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
7. Save to output directory, e.g. `~/Desktop/claudecode/easy-read-output/glossary_20260416_143022.html`
8. Tell user where the file is saved, and remind them they can open it in a browser, print to PDF, or ask you questions about any term

## Quality Checklist

Before generating output, verify:
- ✅ Summary stays within one short paragraph (中文约 300 字 / 英文约 60 词)
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
