# 🧠🕸️ SkillWeaver

⚡ Design, implement, and test new plug-and-play AGI Architectures. ⚡

[High Level Design Document](https://docs.google.com/document/d/1gNaR7g-2pTZiIcUosY0gcW8uCaU6SUwx3xf0UNvalLc/edit?usp=sharing)

## Quick Install

`pip install SkillWeaver`
or
`conda install SkillWeaver -c conda-forge`

## 🤔 What is this?

SkillWeaver treats LLM Chains as singular, out-of-the-box components called 'skills' and makes it simple to implement nuanced, high-level AGI flows. The package simply allows developers to "weave" together skills, which are great at helping AGI solve highly specific, complex tasks.

It is obvious that the future of AI lies in the creation of artificial generalized intelligence (AGI). Presently, LLM models have pushed the boundaries of this by showcasing the power to solve a variety of tasks. However, current LLM flows and pipelines are limited due to context and clarity, making it essential to break down tasks into smaller problems for AGI to solve.

E.g. BabyAGI Schema

![image](https://github.com/cybertheory/skillweaver/assets/27149047/91821f60-e78a-4830-9676-0d1313393cc3)


The project aims to provide an ecosystem of skills out of the box and provide simple tooling to modify existing skills or create brand-new ones with plug-and-play patterns.

Skillweaver provides all the tooling necessary to plan, implement, and fine-tune AGI flows to solve a higher variety of tasks. And even aims to host an ecosystem of Skill Webs for more ambitious developers to weave together to create even more nuanced intelligence.

## 🚀 What can this help with?

🧠 Schemas

Borrowed from Cognitive Psychology and other aspects of Computer Science, A schema defines categories of information and relationships among them. SkillWeaver allows developers to design and implement schemas that define the operations of their AGI.

🕸️ Skill Webs

Just as LangChain allows developers to chain together different ready-to-go tools to create LLM Chains and Agents, SkillWeaver allows developers to chain together out-of-the-box Agents (which we call Skills). Agents are really good at doing complex tasks with a smaller number of tools, by allowing developers to chain together simpler agents we can quicken development times and decrease problem complexity which increases reliability.

🛠️ Skills

SkillWeaver's fundamental building blocks are skills. A skill is essentially an LLM Chain or Agent that is really good at performing a certain task. Skills abstract away all of LangChain's data loaders, transformers, vector stores, prompt templates, and tools so that developers can focus on solving real-world tasks. SkillWeaver provides an ecosystem of skills out of the box.


🧬 Skill Blends

It is useful to have an agent deal with multiple skills at once, this can increase interoperability and understanding to execute tasks. Skill Blends provide different ways to blend skills together to achieve desired results.


🧩 Skill Patterns

These are templates that developers can use to create custom skills easily. Patterns abstract away common boilerplate when making chains.


📊 Skill Charts

In creating AGI using LLM models, it is very important to understand what a model is good at doing so we can provide appropriate abstractions for the model to execute. Skill Charts keep a running record of which skills a model may be excellent at.

## 💁 Contributing

As an open-source project in a rapidly developing field, we are extremely open to contributions, whether it be in the form of a new feature, improved infrastructure, or better documentation.

For detailed information on how to contribute, see [here](.github/CONTRIBUTING.md).

# Attribution
Much of this project is based on [LangChain](https://github.com/hwchase17/langchain).
