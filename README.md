# 🦜️🧠 LangBrain

⚡ Bidirectional connection of your SDKs, APIs, and LLMs to create autonomous services ⚡
[High Level Design Document](https://docs.google.com/document/d/1gNaR7g-2pTZiIcUosY0gcW8uCaU6SUwx3xf0UNvalLc/edit?usp=sharing)

[![Release Notes](https://img.shields.io/github/v/release/cybertheory/langbrain)](https://github.com/cybertheory/langbrain/releases)
[![lint](https://github.com/hwchase17/langchain/actions/workflows/lint.yml/badge.svg)](https://github.com/hwchase17/langchain/actions/workflows/lint.yml)
[![test](https://github.com/hwchase17/langchain/actions/workflows/test.yml/badge.svg)](https://github.com/hwchase17/langchain/actions/workflows/test.yml)
[![linkcheck](https://github.com/hwchase17/langchain/actions/workflows/linkcheck.yml/badge.svg)](https://github.com/hwchase17/langchain/actions/workflows/linkcheck.yml)
[![Downloads](https://static.pepy.tech/badge/langchain/month)](https://pepy.tech/project/langchain)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/langchainai.svg?style=social&label=Follow%20%40LangChainAI)](https://twitter.com/langchainai)
[![](https://dcbadge.vercel.app/api/server/6adMQxSpJS?compact=true&style=flat)](https://discord.gg/6adMQxSpJS)
[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/hwchase17/langchain)
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/hwchase17/langchain)
[![GitHub star chart](https://img.shields.io/github/stars/hwchase17/langchain?style=social)](https://star-history.com/#hwchase17/langchain)
[![Dependency Status](https://img.shields.io/librariesio/github/hwchase17/langchain)](https://libraries.io/github/hwchase17/langchain)
[![Open Issues](https://img.shields.io/github/issues-raw/hwchase17/langchain)](https://github.com/hwchase17/langchain/issues)


## Quick Install

`pip install langbrain`
or
`conda install langbrain -c conda-forge`

## 🤔 What is this?

Built upon LangChain, LangBrain takes a plug-and-play, composable approach allowing interoperability between systems as desired by the developer with no need to work through boilerplate mappings. Simply ensure your desired SDKs or APIs are supported and use our prebuilt 'connections' enabling users to utilize a chosen LLM as an autonomous interface.

Upon the success of libraries such as LangChain, it is evident that the power in Large Language Models comes from augmenting external computation and knowledge. Up till now, Plugins and Embeddings have been the way most LLM platforms provide value. Taking this one step further, LangBrain standardizes the use of LLMs as a sort of computational nexus, allowing the creation of autonomous agents by establishing an ecosystem of bi-directional connections between models and existing SDKs or APIs.

Note: For certain larger connections, LangBrain can automate the process of assimilating knowledge bases in configurable vector stores.

## 🚀 What can this help with?

There are six main areas that LangChain is designed to help with.
These are, in increasing order of complexity:

**📃 LLMs and Prompts:**

This includes prompt management, prompt optimization, a generic interface for all LLMs, and common utilities for working with LLMs.

**🔗 Chains:**

Chains go beyond a single LLM call and involve sequences of calls (whether to an LLM or a different utility). LangChain provides a standard interface for chains, lots of integrations with other tools, and end-to-end chains for common applications.

**📚 Data Augmented Generation:**

Data Augmented Generation involves specific types of chains that first interact with an external data source to fetch data for use in the generation step. Examples include summarization of long pieces of text and question/answering over specific data sources.

**🤖 Agents:**

Agents involve an LLM making decisions about which Actions to take, taking that Action, seeing an Observation, and repeating that until done. LangChain provides a standard interface for agents, a selection of agents to choose from, and examples of end-to-end agents.

**🧠 Memory:**

Memory refers to persisting state between calls of a chain/agent. LangChain provides a standard interface for memory, a collection of memory implementations, and examples of chains/agents that use memory.

**🧐 Evaluation:**

[BETA] Generative models are notoriously hard to evaluate with traditional metrics. One new way of evaluating them is using language models themselves to do the evaluation. LangChain provides some prompts/chains for assisting in this.

For more information on these concepts, please see our [full documentation](https://langchain.readthedocs.io/en/latest/).

## 💁 Contributing

As an open-source project in a rapidly developing field, we are extremely open to contributions, whether it be in the form of a new feature, improved infrastructure, or better documentation.

For detailed information on how to contribute, see [here](.github/CONTRIBUTING.md).

# Attribution
Much of this project is based on [LangChain](https://github.com/hwchase17/langchain).

