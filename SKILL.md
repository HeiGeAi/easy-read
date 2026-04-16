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
- For files: use Read tool
- For URLs: use WebFetch or web_access skill
- For compressed files: extract first, then read
- For PDFs: use Read with appropriate page ranges
- For images/screenshots: use vision tools to extract text

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
- **资深级** (Advanced): Deep technical concepts (RAG, embedding, fine-tuning)
- **专家级** (Expert): Cutting-edge or highly specialized (Agentic workflows, prompt caching)

### Step 3: Generate Output

Create a beautiful, interactive HTML page with:

1. **Article Summary** (文章摘要)
   - 300 characters or less
   - Written for complete beginners
   - Explain what the article is about in plain language
   - Avoid using jargon in the summary itself

2. **Glossary** (词汇表)
   - Organized by difficulty level (入门级 → 进阶级 → 专业级 → 资深级 → 专家级)
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
├─ 音标：[IPA phonetic notation]
├─ 中式发音提示：用中文拼音或常见字帮助发音（如 "Harness" → "哈内斯，类似'哈尼斯'"）
├─ 人话解释：用最简单的语言解释
├─ 历史背景：如果有演进历史，简要说明
├─ 相关时间：大概的时间点
└─ 深入了解：提示用户"想了解更多，可以继续对话"
```

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

1. **Read the content**
   ```python
   # Use appropriate tool based on input type
   # For files: Read tool
   # For URLs: WebFetch or web_access
   # For images: vision tools
   ```

2. **Analyze and extract jargon**
   ```python
   # Identify all terms that need explanation
   # Classify by difficulty level
   # Gather context for each term
   ```

3. **Generate explanations**
   ```python
   # For each term:
   # - Write plain language explanation
   # - Add pronunciation help (for English terms)
   # - Add historical context (if relevant)
   # - Add time reference (if relevant)
   ```

4. **Create summary**
   ```python
   # Write 300-character summary
   # Use plain language
   # Avoid jargon
   ```

5. **Generate HTML**
   ```python
   # Use the template from assets/glossary_template.html
   # Populate with data
   # Save to user's desktop/claudecode output folder
   ```

6. **Save output**
   ```python
   # Save to: ~/Desktop/claudecode/jargon-translator-output/
   # Filename: glossary_YYYYMMDD_HHMMSS.html
   # Tell user where the file is saved
   ```

## Output Location

Always save output to: `~/Desktop/claudecode/jargon-translator-output/`

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
7. Save to ~/Desktop/claudecode/jargon-translator-output/glossary_20260416_143022.html
8. Tell user: "我已经为你生成了一个词汇表，保存在桌面的 claudecode/jargon-translator-output 文件夹里。打开 HTML 文件就能看到所有术语的解释，都是用最简单的语言写的。如果想深入了解某个词，随时问我！"

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
