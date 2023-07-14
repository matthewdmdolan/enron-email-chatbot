# Enron Email Chatbot

# Introduction

LLMs are the hot topic at the moment, with LinkedIn dominated by posts about the applications of ChatGPT in the work environment, alongside a lot of scaremongering surrounding the unethical applications of 
the technologies and unintended consequences of their applications. Namely, taking over some jobs. However, LLMs are trained on datasets that are typically petabytes in size, and require computational resources well beyond my means.

Nevertheless, I wanted to see if I could build a chat bot that utilises some of the new NLP analysis methods, which would able to reply to emails in a professional way, that would be able to automate some of the repetiive administrator roles I worked in during my youth, to identify just how successful AI would be at 'taking our jobs'. 

There are some amazing open source technologies that allow you to quickly build chatbots e.g. flowise, which I did use to develop a PoC to see if I'm on the right lines with utilising the dataset, but 
this was more a task to develop my understanding of the workings behind this new technology that's supposedly going to turn our lives into a utopia, or mad max dystopia. Depending on what Linkedin posts you believe. 

# Dataset 

Initially, I found a lot of the popular public datasets for training chatbots aren't optimised for this task. For example, The Google Blogger Corpus (Goohttps://u.cs.biu.ac.il/~koppel/BlogCorpus.htm) is another popular dataset but I felt (rightly or wrongly) blogs were typically framed to be more educational than your average email sent in a corporate environment. 

However, I stumbled upon the enron dataset (source: https://www.cs.cmu.edu/~enron/). The dataset contains over 500k anonymised emails sent by 150 users, mostly senior management of Enron, organized into folders. However some further context is needed behind this dataset: 

Enron, a Texas-based energy company, committed one of the largest accounting frauds in history. It used deceptive accounting to inflate revenues, temporarily becoming the seventh-largest US corporation. The fraud's exposure led to a rapid collapse and bankruptcy filing in December 2001. The emails were made public following an investigation by US authorities, but later purchased by MIT to help with developing datasets for the emerging field of NLP analysis. 

There are undoubtedbly limitations to utilising a dataset that was derived from toxic circumstances. Nathan Heller identified some interesting points:
- Racial slurs and Pornography are common
- Around half of the emails are only one sentence long.

Source: https://www.newyorker.com/magazine/2017/07/24/what-the-enron-e-mails-say-about-us

The email length is less of an issue for our analysis, and pornography is less of a concern due to the fact we are only analysing the text data and not any attachments. However, the racial slurs are a big issue if this chat bot was to be operationalised. Racial biases in the training of AI models is a hotly contested issue and something we should combat so I will be researching how we can reduce these biases in the development of the model. For further reading on biases in the application of AI Models I highy recommend are Weapons of Math Destruction by Cathy O'Neil. 

Nevertheless, as one of the only publicly available datasets on email data, I still decided to develop the chatbot despite these observed limitations. 
