# The Crystal Project
💎 The Crystal Project is open source distribute api that works as a micro-service for platforms that allow users to link creative works. Crystal parses through creative works and stores them in a distributed database along with varying criteria to deem the source credible.

## About
At Gemify, we needed a solution to ensure that information that ended up on our platform was reviewed by our community in a way that is dictated by our community in order to provide a democratic process that aims to avoid abuse. Unfortunately, we do not have the capital to moderate what goes through our platforms at our current state and we want to make the barrier as low as possible for others who wish to provide solutions to issues that currently plague in tech. Let it be clear that tech is inherently political, if you would like to learn more about where we stand politically check it out here: https://gemify.tech/politics

## Issues
While our intent is to democratize tech it might have significant reprecussions and negative impacts always supersede good intent. Here are some flaws and issues that we are aware of and how we aim to avoid something from going astray:

- Issue: Tech giants already have the ability to police and monitor their content and it is not the communty's job to work for them for free.
- Reponse: We agree and expect that these platforms help provide resources for contributors if they truly care about progressive technology.

- Issue: Platforms that spread hate and allow fascism to fester should not have access to this project.
- Response: We do not believe that platforms that rely on the spread of misinformation will benefit from Crystal as it only threatens the spread of misinformation that some platforms rely on.

- Issue: Cross-polinating feedback from other platforms may reflect poorly on information as a result of groupthink.
- Response: Where feedback is provided is tracked and platforms and users that abuse it can be added to a deny list or filtered out by platforms.

## Walkthrough
Before any platform or outlet publishes a creative work, they have the abiltiy to request a Crystal Identifier from any node in the Crystal network or a UUID-4 that stores the URL for indexing purposes. The platform or outlet can store this identifier in its meta data with other key value pairs that help give context to users when retrieving information.

Registering a creative work with Crystal allows nodes in the Crystal network to provide feedback on the credibility of that particular work through each platform that it is linked on or on the location of the work itself.

There are different standards upon which users can provide feedback to each source in order to provide users with the ability to store retrieve and interpret data in formats that make sense to them based on the creative work and the context provided.  

Platforms can then embed a modal with information provided with Crystal that contains information provided by other users onto their application upon any mention of a link that has been registered with Crystal.

## Example
Headnovel, a social media site that allows users to post text and media to share with a users family and friends, has a misinformation problem and it has failed to corectly police content in a way that is both accurate and hastey over the past decade. Despite external pressures and empty promises it continues to fail in ways that convince its users that is accurate or democratic.
 
In order to solve this, Headnovel sets up a Crystal node that is accessible from crystal.example.com. They then are able to automate a process that retreives information from this url when a user accesses a link shared by another user the feedback and credibility information. This information is synced with other nodes in order to gather feedback from other platforms as well.

If a user would like to provide feedback on a creative work, they can do so from whichever platform they are accessing.
