# 🧠🕸️ SkillWeaver

⚡ A Better Approach to Designing and Creating Next Level AGI ⚡

[High Level Design Document](https://docs.google.com/document/d/1gNaR7g-2pTZiIcUosY0gcW8uCaU6SUwx3xf0UNvalLc/edit?usp=sharing)

## Quick Install

`pip install SkillWeaver`
or
`conda install SkillWeaver -c conda-forge`

## 🤔 What is this?
Upon the success of frameworks such as LangChain, it is evident that the power in Large Language Models comes from automating external computation and knowledge. Up till now, Plugins and Embeddings have been the way most LLM platforms provide value. 

Taking this one step further, SkillWeaver uses the LangChain standard and treats LLMs as a sort of hostable computational nexus, allowing the creation of 24/7 live autonomous agents and establishing an ecosystem of bi-directional connections between models and existing SDKs or APIs.

Built upon LangChain, SkillWeaver takes a plug-and-play, composable approach allowing interoperability between systems as desired by the developer with no need to work through boilerplate.

## 🚀 What can this help with?

🧠 Schemas

Borrowed from Cognitive Psychology and other aspects of Computer Science, A schema defines categories of information and relationships among them. SkillWeaver allows developers to design and implement schemas that define the operations of their AGI.

🧠 Skills

SkillWeaver's fundamental building blocks are skills. A skill is essentially an LLM Chain or Agent that is really good at performing a certain task. Skills abstract away all of LangChain's data loaders, transformers, vector stores, prompt templates, and tools so that developers can focus on solving real-world tasks. SkillWeaver provides an ecosystem of skills out of the box.

🧠 Skill Patterns

These are templates that developers can use to create custom skills easily. Patterns abstract away common boilerplate when making chains.

🧠 Skill Blends

It is useful to have an agent deal with multiple skills at once, this can increase interoperability and understanding to solve problems. Skill Blends provide different ways to blend skills together to achieve desired results.

🧠 Skill Webs

Just as LangChain allows developers to chain together different ready-to-go tools to create LLM Chains and Agents, SkillWeaver allows developers to chain together out-of-the-box Agents (which we call Skills). Agents are really good at doing complex tasks with a smaller number of tools, by allowing developers to chain together simpler agents we can quicken development times and decrease problem complexity which increases reliability.

🧠 Skill Charts

In creating AGI using LLM models, it is very important to understand what a model is good at doing so we can provide appropriate abstractions for the model to execute. Skill Charts keep a running record of which skills a model may be excellent at.

## 💁 Contributing

As an open-source project in a rapidly developing field, we are extremely open to contributions, whether it be in the form of a new feature, improved infrastructure, or better documentation.

For detailed information on how to contribute, see [here](.github/CONTRIBUTING.md).

# Attribution
Much of this project is based on [LangChain](https://github.com/hwchase17/langchain).
