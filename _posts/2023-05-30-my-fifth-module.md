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

We had a remarkable discussion with fellow students on the topic of Intelligent Agents in social media. During our conversation about agent-based systems like chatbots, sentiment analysis, and recommender systems, we also delved into the darker side of their development. These tools, while assisting companies in staying competitive by enhancing user engagement and satisfaction through the analysis of user behaviour, can also manipulate users. 

Intelligent Agents on social media, striving to keep users constantly scrolling, have caused problems such as information overload, doom-scrolling, shortened attention spans, sexualisation of kids, polarisation, and the spread of fake news.

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

 ![Team Project Main Picture](/assets/images/banners/background%20pic.jpg) <br>
To be honest, I found it quite challenging to work on the development team project, particularly when it came to distinguishing between a multi-agent system, a single-agent system, and a distributed system with autonomous objects.

According to Odell (2002), agents exhibit autonomy because they can react to their environment and follow instructions. For instance, agents have the ability to both "say 'No' and ‘Go’. Agents engage in a negotiation-like process, exchanging information and incorporating it into their existing knowledge acquired from the environment. Based on this knowledge, agents make decisions on how to proceed.

Another challenge we encountered was the usage of Knowledge Query and Manipulation Language (KQML). This widely used agent communication language (ACL) allows agents with different goals and ontologies to share information while pursuing their individual objectives (Finin at al., 1994).

However, at the beginning, our team had a vague understanding of how to appropriately implement KQML in Python. As a result, we decided to start with creating a single-agent system with two modules to address the needs of the Digital Forensics domain for a hypothetical detective agency. The system's purpose was to locate specific file types within a file system, archive them, and transmit the results for further analysis.

We proposed implementing this task using a single-agent system, considering that intelligent agents possess key characteristics such as autonomy, reactivity, proactivity, adaptability, and the ability to communicate and coordinate with other agents (Kendrick et al., 2016).
During the evaluation, the tutor provided positive feedback, stating that the report was well-presented and covered the topic in sufficient detail. However, they advised us to provide explanations for the choices we made and to enhance our focus on critical analysis.

[References]( https://github.com/Vasilisalook/vasilisalook.github.io/blob/main/References%20for%20Team%20Project%201.txt)<br> 
[Team Project 1](https://github.com/Vasilisalook/vasilisalook.github.io/blob/main/Team%20Project%201.docx)

## Unit 6. Creating Agent Dialogues

I have created an [Agent Dialogue using KQML](https://github.com/Vasilisalook/vasilisalook.github.io/blob/main/KQML.docx) to design a basic example of communication between agents. I realised that KQML was popular in the 1990s, whereas nowadays the Foundation for Intelligent Physical Agents (FIPA-ACL) is more commonly used. Unlike Python or Java, ACLs are more complex and offer greater interoperability, although they lack language integration.

**Summary for the ACL and agent system discussion**

In this module, we have had the best and the most engaging discussion with my fellow students throughout my entire time studying at the University of Essex. The discussion came at a crucial moment when my team and I were trying to differentiate between a multi-agent system and a single-agent system. I warmly invite you [to read the Collaborative Discussion Summary, which includes a list of useful references.](https://github.com/Vasilisalook/vasilisalook.github.io/blob/main/Agents%20Discussion%20Summary.docx)

## Unit 7. Natural Language Processing (NLP)

![spaCy](/assets/images/banners/spacy.png)  <br>

As a linguist, I find natural language processing (NLP) branch of computer science to be incredibly fascinating. I enjoy working with the spaCy library, which offers a wide range of linguistic annotations for sentences and enables faster analysis than searching through dictionaries.

Another practical application of NLP is utilising machine learning (ML) to analyse whether comments in the Russian language contain toxic content (I did it last year during ML module).

I will encounter numerous tasks in the context of NLP while working on my Capstone project (the project is around news texts and bias detection methods).

However, one of the major challenges in NLP is the scarcity of sufficient training data (Ain et al., 2017). This has led to the emergence of pre-trained BERT models, which are based on NLP tasks such as Masked Language Modelling and Next Sentence Prediction anyway.

## Unit 8. Creating Parse Trees

![Parse Trees](/assets/images/banners/parse.jpg)  <br>

Parse tree shows the relationships between a specific sentence and the grammar concepts. Again, as a linguist, I find this topic very familiar. It's great to see that programmers utilise the same concepts, such as "part of speech" (POS) or "grammatical relations." Decades of philological research by humans have been incredibly helpful for computer science.

When I first started studying methods like lemmatisation (reducing a word to its root form), I had concerns about cutting off the end of words because it may remove important contextual information (such as distinguishing between one dog or many dogs). However, I soon realised that the major disadvantage of lemmatisation algorithms is their slower speed compared to stemming algorithms.

## Unit 9. Deep Learning

**Collaborative Discussion 3**

## Unit 10. Deep Learning in action

Activity Guidance
You are required to research an application of Deep Learning that you think is going to have an impact on society (whether that is positive or negative). When you have found your application you should make a post on the discussion forum that covers:
An overview of the technology (e.g., what it does).
A brief synopsis of how it works.
The potential impacts this will have in terms of ethics, privacy, social good, or any other socio-technical aspects that you feel are relevant.

## Unit 11. Team Project 2 (Presentation)
## Unit 12. Skill Matrix and Action Plan

