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
Upon the success of frameworks such as LangChain, it is evident that the power in Large Language Models comes from augmenting external computation and knowledge. Up till now, Plugins and Embeddings have been the way most LLM platforms provide value. Taking this one step further, LangBrain uses the LangChain standard and treats LLMs as a sort of computational nexus, allowing the creation of autonomous agents by establishing an ecosystem of bi-directional connections between models and existing SDKs or APIs.

Built upon LangChain, LangBrain takes a plug-and-play, composable approach allowing interoperability between systems as desired by the developer with no need to work through boilerplate mappings. Simply ensure your desired SDKs or APIs are supported and use our prebuilt 'connections' enabling users to utilize a chosen LLM as an autonomous interface.

Note: For certain larger connections, LangBrain can automate the process of assimilating knowledge bases in configurable vector stores.

## 🚀 What can this help with?

There are 5 main areas that LangBrain is designed to help with.
These are in increasing order of complexity:

**💡 Full Autonomous:**

Full Autonomous involves having knowledge of the system and its own existence and abilities. By turning LangBrain on its self, we achieve a sense of meta-cognition, and an LLM can fully control the framework, create its own connections on demand, and make desicions to solve problems.

**🤖 Agents:**

Agents involve an LLM making decisions about which Actions to take, taking that Action, seeing an Observation, and repeating that until done. LangChain provides a standard interface for agents. LangBrain aims to build upon this standard and create a more nuanced ecosytem of unidirectional and bidirectional connections to various community added software packages.

**🔗 Integrations and Automations:**

Being able to host a LangBrain instance is important to building long term solutions. LangBrain aims to create a series of APIs and a Web Application to host and monitor autonomous solutions. This can also then be incorporated in existing IPASS, Automation, and Data Integration solutions.

**🧐 Dashboard and Analytics:**

LangBrain admits the risks involved in creating highly autonomous agents. In order to mitigate such risks LangBrain aims to allow human observation of all communication through dashboards.

**🧠 Knowledge:**

LangBrain provides an autonomous proccess of identifying relevant information and documentation of software packages and uploading to preconfigured vector store instances. This ensures LLMs have the skillset and knowledge nessecary to make desicions and carry out tasks.

For more information on these concepts, please see our [full documentation](https://langchain.readthedocs.io/en/latest/).

## 💁 Contributing

As an open-source project in a rapidly developing field, we are extremely open to contributions, whether it be in the form of a new feature, improved infrastructure, or better documentation.

For detailed information on how to contribute, see [here](.github/CONTRIBUTING.md).

# Attribution
Much of this project is based on [LangChain](https://github.com/hwchase17/langchain).

