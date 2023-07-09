---
layout: post
title: Intelligent Agents
subtitle: The fifth module of the course
categories: Modules
tags: [agent, AI, multi-agent system, hybrid agent, NLP, ACLs, parse trees]
---
## Summary of the Intelligent Agents module

On this page I collected notes on my humble progress during the module...

## Unit 1. Dark sides of Agent-based systems

**Summary Post for the Discussion** <br> 

We had a remarkable discussion with fellow students on the topic of Intelligent Agents in social media. During our conversation about agent-based systems like chatbots, sentiment analysis, and recommender systems, we also delved into the darker side of their development. These tools, while assisting companies in staying competitive by enhancing user engagement and satisfaction through the analysis of user behavior, can also manipulate users. 

Intelligent Agents on social media, striving to keep users constantly scrolling, have caused problems such as information overload, doom-scrolling, shortened attention spans, sexualization of kids, polarization, and the spread of fake news.

Alberto Castro (Castro, 2023) highlighted that recommender systems still have room for improvement, particularly in sensitive areas like data privacy. He provided an example of "bad" targeting, where a customer discovered about his young daughter's pregnancy through targeted ads.<br> 
Our discussion also touched on bias within recommender systems, which can lead to discrimination against certain user groups and the creation of prejudicial filter bubbles.

At the conclusion of our conversation, Anastasia Rizzo (Rizzo, 2023) posed thought-provoking questions. For instance, how can we strike a balance between the benefits of these agents and user safety and autonomy? What measures can companies and developers implement to mitigate the negative impacts and foster responsible AI deployment?

And in the end, I have got a nice list of useful and actual [references](https://github.com/Vasilisalook/vasilisalook.github.io/blob/main/IA_Unit1_References.txt) on the topic above. 

## Unit 2. FOL for Linguists

As a linguist, I have devised a primitive visual scheme for transforming sentences from English natural language to First-order language in order to grasp the main idea on my own. **First-order logic** offers greater expressive power than **Propositional logic**, which is also utilized in the field of computing. I find it fascinating and intellectually stimulating to interpret information from "English human" format to "English computer" format. I believe this is of great importance because individuals can be represented as agents in systems too.

 ![FOL](/assets/images/banners/FOL_linguistics.jpg) <br> 

Understanding the fundamental terms and rules of this logic is crucial. For example, a **predicate** is a component of a sentence that contains a verb or makes a statement about the subject (where the **subject** is an **attribute** represented as a piece of information enclosed in brackets in computing).

I consider this point to be where programming becomes a highly creative process. To write a sentence like *"It is rained"* as *weather(X, rain)*, one needs to exercise creativity. Another intriguing observation is that pronouns such as *I, it, you, he*, and *she* can be regarded as **variables** in natural language. My insight is that a human language itself is a program, albeit a highly layered and sophisticated one.

## Units 3-4. Hybrid Agents

The agent architectures turned out to be one of the most challenging topics for me throughout the entire educational process because the level of abstraction here seemed too high. It felt like I needed visualisations for every concept.

I realised that hybrid agents are something between symbolic (or deliberative) reasoning agents and reactive agents. They attempt to balance proactiveness with reactivity (Beckley, 2023).

However, I have heard the term "hybrid intelligent agent" used in a slightly different context, as I illustrated below. 

 ![Intelligent agents](/assets/images/banners/hybrid.jpg) <br>

I believe it is a beautiful branch of science because it bridges the tangible, carbon-based physical world with the unique universe that each individual constructs in their mind. It seems that computers may even construct this virtual space better than humans.

I understand that the concept of an intelligent agent is used metaphorically to bring together currently disconnected strands of computer science, such as machine learning, robotics, multi-agent systems, and so on.

## Unit 5. Development Team Project

To be honest, it has been quite challenging for me while working on the development team project...

## Unit 6. Creating Agent Dialogues

I have created an [Agent Dialogue using KQML](https://github.com/Vasilisalook/vasilisalook.github.io/blob/main/KQML.docx) to design a basic example of communication between agents. I realised that KQML was popular in the 1990s, whereas nowadays the Foundation for Intelligent Physical Agents (FIPA-ACL) is more commonly used. Unlike Python or Java, ACLs are more complex and offer greater interoperability, although they lack language integration.

**Summary for the ACL and agent system discussion**

In this module, we have had the best and the most engaging discussion with my fellow students throughout my entire time studying at the University of Essex. The discussion came at a crucial moment when my team and I were trying to differentiate between a multi-agent system and a single-agent system. I warmly invite you [to read the Collaborative Discussion Summary, which includes a list of useful references.](https://github.com/Vasilisalook/vasilisalook.github.io/blob/main/Agents%20Discussion%20Summary.docx)

## Unit 7. Natural Language Processing (NLP)

?

## Unit 8. Creating Parse Trees

![Parse Trees](/assets/images/banners/parse.jpg)  <br>

Parse tree shows the relationships between a specific sentence and the grammar concepts. As a linguist, I find this topic very familiar. It's great to see that programmers utilise the same concepts, such as "part of speech" (POS) or "grammatical relations." Decades of philological research by humans have been incredibly helpful for computer science.

When I first started studying methods like lemmatisation (reducing a word to its root form), I had concerns about cutting off the end of words because it may remove important contextual information (such as distinguishing between one dog or many dogs). However, I soon realised that the major disadvantage of lemmatisation algorithms is their slower speed compared to stemming algorithms.
