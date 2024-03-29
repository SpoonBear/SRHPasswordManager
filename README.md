# SRHPasswordManager
SRH - Software Development classes 

# Welcome to SRH Password Manager

## Project Overview

This project aims to develop a Password Manager using Python for the Software Development class. This manager should be able to store user credentials in an encrypted simple database, as well as being able to create folders to better organize them, and provide a passphrase generator to create more secure credentials.

 This is a project developed for the Software Development course at SRH Berlin University of Applied Sciences.
 
## FINAL PROJECT SUBMISSION

## Table of Contents

  * [1. Git](#1-git)
  * [2. UML](#2-uml)
  * [3. Requirements Engineering](#3-requirements-engineering)
  * [4. Analysis](#4-analysis)
  * [5. DDD](#5-ddd)
  * [6. Metrices](#6-metrices)
  * [7. Clean Code Dev](#7-clean-code-dev)
  * [8. Build](#8-build)
  * [9. UnitTests](#9-unittests)
  * [10. IDE](#10-ide)
  * [11. Functional Programming](#11-functional-programming)

## 1. Git

>Use and understand Git! Play with Branches and undo/revert things = go back in time!

The GitHub Desktop app, GitHub plugin for VSCode and the GitHub dashboard were used to commit and merge the progress for this project, documenting changes and reverting the occasional bad implementation.

&rarr; [See commit history for main](https://github.com/SpoonBear/SRHPasswordManager/commits/main)

&rarr; [See commit history for dev](https://github.com/SpoonBear/SRHPasswordManager/commits/dev)

[Back to Table of Contents](#table-of-contents)

## 2. UML 

>UML at least 3 good different big diagrams. "good" means you can pump it up artificially as written in DDD. You have 10 million $ from me! Please export the pics. I can not install all the tools to view them! Perfect would be 1) one dynamic diagram like an activity diagranm 2) one or two static diagrams as component, class or deployment and if needed a use-case diagram.

Activity Diagram for an user adding a new category to the Notebook

![Activity Diagram 1](https://github.com/SpoonBear/SRHPasswordManager/assets/148366878/29200315-103a-4f29-9c54-b6502908a761)

Activity Diagram for an user requesting to check if their credentials have been leaked

![Activity Diagram 2](https://github.com/SpoonBear/SRHPasswordManager/assets/148366878/8793f615-ccb4-4acf-8f90-6dc52ef4d662)

Class Diagram for Notebook

![Class Diagram](https://github.com/SpoonBear/SRHPasswordManager/blob/dev/Resources/UML/Class%20Diagram.png)

Use-Case Diagram

![Use Case Diagram](https://github.com/SpoonBear/SRHPasswordManager/blob/dev/Resources/UML/Use%20Case%20Diagram.png)

[Back to Table of Contents](#table-of-contents)

## 3. Requirements Engineering

>Describe your project or any project (e.g. one related to your work or a private project) neatly using the methods of Requirements Engineering by mapping some requirements in 2 tools (!).To do this, use the most important description attributes from the script! Approximately 5-10 requirements per tool should be sufficient. Two variants should be provided = tools. A 'self-made' version and a professional = possibly commercial version, i.e. with 2 tools! Examples of 'self-made' variants: Airtable, notion.so, Trello, etc. Examples of commercial tools: Monday, Jira, Doors, ObjectIF, Xebrio, etc. (see Miro). Instead of the professional version, you can also build a tool yourself.

For the Self-Made tool I used Notion.so, in which I created a kanban board to hold the cards. Inside these cards I added all the attributes related to the Requirements.

For the professional tool I used Jira, in its built in board I also added the attributes related to the Requirements.

Notion Overview

![Notion Overview](https://github.com/SpoonBear/SRHPasswordManager/blob/dev/Resources/Requirement%20Engineering/Notion%20Overview.png)

Jira Overview

![Notion Overview](https://github.com/SpoonBear/SRHPasswordManager/blob/dev/Resources/Requirement%20Engineering/Jira%20Overview.png)

&rarr; [See full requirements and details](https://github.com/SpoonBear/SRHPasswordManager/tree/dev/Resources/Requirement%20Engineering)

[Back to Table of Contents](#table-of-contents)

## 4. Analysis

>From all the points in the Analysis learning unit, A) come up with your own checklist (on an extra DIN A4 page) with the points that you consider relevant to your project. B. Carry out an analysis of your semester project/your favourite / start-up idea and would like to submit this analysis as part of a large documentary! Write enough about each point to create at least 2 pages. Assume that you will soon have an angel for the start-up chapter. If successful, you would get a lot of “money” to be able to do the design and implement it later. So get your start-up successfully into the race!

&rarr; [Checklist](https://github.com/SpoonBear/SRHPasswordManager/blob/dev/Resources/Analysis%20A.pdf)

&rarr; [Analysis](https://github.com/SpoonBear/SRHPasswordManager/blob/dev/Resources/Analysis%20B.pdf)

[Back to Table of Contents](#table-of-contents)

## 5. DDD

>DDD Do a DDD session to find your domains! If your domain is too small, invent other domains around and document these domains (as if you have 100 Mio € from Edlich-Investment!) Develop a clear strategic design with mappings/relationships with >=8 Domains coming from an A) Event Storming. Drop your Domains into a B) Core Domain Chart and draw the C) Relations between the Domains!  

Event Storming

![Event Storming](https://github.com/SpoonBear/SRHPasswordManager/blob/dev/Resources/DDD/Event%20Storming.png)

Core Domains Chart

![Core Domains Chart](https://github.com/SpoonBear/SRHPasswordManager/blob/dev/Resources/DDD/Core%20Domains%20Chart.png)

Domain Relations

![Domain Relations](https://github.com/SpoonBear/SRHPasswordManager/blob/dev/Resources/DDD/Domain%20Relations.png)

[Back to Table of Contents](#table-of-contents)

## 6. Metrices

>Metrics at least two. Sonarcube would be great. Other non-trivial metrics are also fine.

SonarCloud

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=SpoonBear_SRHPasswordManager&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=SpoonBear_SRHPasswordManager)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=SpoonBear_SRHPasswordManager&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=SpoonBear_SRHPasswordManager)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=SpoonBear_SRHPasswordManager&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=SpoonBear_SRHPasswordManager)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=SpoonBear_SRHPasswordManager&metric=bugs)](https://sonarcloud.io/summary/new_code?id=SpoonBear_SRHPasswordManager)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=SpoonBear_SRHPasswordManager&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=SpoonBear_SRHPasswordManager)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=SpoonBear_SRHPasswordManager&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=SpoonBear_SRHPasswordManager)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=SpoonBear_SRHPasswordManager&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=SpoonBear_SRHPasswordManager)

Codacy

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/5dc8f8ff2999490aae985cbd444ea91d)](https://app.codacy.com/gh/SpoonBear/SRHPasswordManager/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

[Back to Table of Contents](#table-of-contents)

## 7. Clean Code Dev

>Clean Code Development: A) At least 5 points you can show me with an explanation of why this is clean code in your code and/or what has improved & B) >>10 points on your personal CCD cheat sheet. E.g. a PDF.

A)

Refactoring: At the start of my project I tried writing everything in a single main function, later on I changed into objects.

&rarr; [Before](https://github.com/SpoonBear/SRHPasswordManager/commit/8f7367d3e7c5fc5c1b122d1a72c3ae271dd374a5)
&rarr; [After](https://github.com/SpoonBear/SRHPasswordManager/commit/803a157fca506dead51e8300376dcabe53dab9bd)

Always try to explain yourself in code: In general, most of my code is explained with comments, trying to do a step-by-step guide of the methods.

&rarr;[Comments 1](https://github.com/SpoonBear/SRHPasswordManager/blob/d404919af1126c1147c9dc01d821ed93ca727700/src/main/python/SRHPasswordManager.py#L151-L162)
&rarr;[Comments 2](https://github.com/SpoonBear/SRHPasswordManager/blob/d404919af1126c1147c9dc01d821ed93ca727700/src/main/python/SRHPasswordManager.py#L71-L87)

Error handling: For certain expected situations, I have added error handling to have more information available for the user and for debugging, and also to have graceful errors.

&rarr;[Error Handling 1](https://github.com/SpoonBear/SRHPasswordManager/blob/d404919af1126c1147c9dc01d821ed93ca727700/src/main/python/SRHPasswordManager.py#L86-L87)
&rarr;[Error handling 2](https://github.com/SpoonBear/SRHPasswordManager/blob/d404919af1126c1147c9dc01d821ed93ca727700/src/main/python/SRHPasswordManager.py#L131-L133)

Choose descriptive and unambiguous names: I try to write my methods and variables as descriptive and unambiguous as posible, avoiding names like 'a1' or 'methd'

&rarr;[Method example](https://github.com/SpoonBear/SRHPasswordManager/blob/d404919af1126c1147c9dc01d821ed93ca727700/src/main/python/SRHPasswordManager.py#L61)
&rarr;[Variable example](https://github.com/SpoonBear/SRHPasswordManager/blob/d404919af1126c1147c9dc01d821ed93ca727700/src/main/python/SRHPasswordManager.py#L73)

Related code should appear vertically dense: To increase readability, my code is dense when the methods or functions are related; and sparse when there's logic or where classes end.

&rarr;[Script overview](https://github.com/SpoonBear/SRHPasswordManager/blob/dev/src/main/python/SRHPasswordManager.py#L73)

B)

&rarr;[Cheat Sheet](https://github.com/SpoonBear/SRHPasswordManager/blob/dev/Resources/CCD/Clean%20Code%20Cheat%20Sheet.pdf)

[Back to Table of Contents](#table-of-contents)

## 8. Build

>Build Management with any Build System as Ant, Maven, Gradle, etc. (only Travis is perhaps not enough) Do e.g. generate Docs, call tests, etc. (it could be also disconnected from the project just to learn a build tool!) and CICD

For build management, I used PyBuilder, as it has similar functionalities to Maven

![PyBuilder](https://github.com/SpoonBear/SRHPasswordManager/blob/dev/Resources/Build/PyBuilder.png)

This tool supports different tasks such as coverage analysis, unittests and documentation generation.

By installing PyBuilder and creating a build.py file, I described the tasks that would be run and what plugins would be used. 

&rarr; [Build Config](https://github.com/SpoonBear/SRHPasswordManager/blob/dev/build.py)

The required coverage is 50% and the methods that are tested are check_for_file(), load_and_decrypt(), encrypt_and_write() and add_entry().

![Build](https://github.com/SpoonBear/SRHPasswordManager/blob/dev/Resources/Build/Build.png)

Also, it generated documentation in html from an .rst file, so that it is ready for pubishing.

&rarr; [Generated Docs](https://github.com/SpoonBear/SRHPasswordManager/tree/dev/docs/build/html)

[Back to Table of Contents](#table-of-contents)

## 9. UnitTests

>Integrate some nice unit tests in your Code to be integrated into the Build

Using PyBuilder I wrote the tests for the check_for_file(), load_and_decrypt(), encrypt_and_write() and add_entry() methods.

For this, I had to create a _tests.py file in src/unittest/python.

In here I specified which methods would be tested, by using the same logic and imports used in my main script.

&rarr; [Unittest File](https://github.com/SpoonBear/SRHPasswordManager/blob/dev/src/unittest/python/SRHPasswordManager_tests.py)

[Back to Table of Contents](#table-of-contents)

## 10. IDE

>Use a good IDE and get fluent with it: e.g. IntelliJ. What are your favourite key shortcuts?!

CHOSEN IDE: [VISUAL STUDIO CODE](https://code.visualstudio.com/)

Most used shortcuts:

- ```Ctrl+X,Y,Z``` for cutting, copying and pasting
- ```Ctrl+F``` to find methods and variables
- ```Ctrl+H``` to replace
- ```F2``` for renaming
- ```F8``` and Shift+F8 to toggle between problems

Extensions used:

- ```Pylance``` for more efficient coding
- ```GitHub``` Pull Requests and Issued, for integration with GitHub

[Back to Table of Contents](#table-of-contents)

## 11. Functional Programming
>prove that you have covered all functional aspects in your code as:
>- only final data structures
>- (mostly) side-effect-free functions
>- the use of higher-order functions
>- functions as parameters and return values
>- use closures / anonymous functions
>- You can also do it outside of your project. Even in other languages such as F#, Clojure, Julia, etc.

[TODO]

[Back to Table of Contents](#table-of-contents)
