# The Twelve-Factor App

## Introduction

- In the modern era, software is commonly delivered as a service: called web apps, or software-as-a-service. 

The twelve-factor app is a methodology for building software-as-a-service apps that:

1. Use declarative formats for setup automation, to minimize time and cost for new developers joining the project;

2. Have a clean contract with the underlying operating system, offering maximum portability between execution environments;

3. Are suitable for deployment on modern cloud platforms, obviating the need for servers and systems administration;

4. Minimize divergence between development and production, enabling continuous deployment for maximum agility;

5. And can scale up without significant changes to tooling, architecture, or development practices.

The twelve-factor methodology can be applied to apps written in any programming language, and which use any combination of backing services (database, queue, memory cache, etc).



## The Twelve Factors

I. Codebase : One codebase tracked in revision control, many deploys

II. Dependencies : Explicitly declare and isolate dependencies

III. Config: Store config in the environment

IV. Backing services: Treat backing services as attached resources

V. Build, release, run :Strictly separate build and run stages

VI. Processes : Execute the app as one or more stateless processes

VII. Port binding : Export services via port binding

VIII. Concurrency : Scale out via the process model

IX. Disposability: Maximize robustness with fast startup and graceful shutdown

X. Dev/prod parity : Keep development, staging, and production as similar as possible

XI. Logs : Treat logs as event streams

XII. Admin processes : Run admin/management tasks as one-off processes