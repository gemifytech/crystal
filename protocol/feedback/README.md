# Feedback Specs
The Feedback component offers users from distributed platforms to offer critical feedback of creative works. This feedback is critical for allowing users to determine whether a creative work that is provided on any platform is legitimate.

As a warning, this is still being changed to accomodate the initial use case and still consists of issues that do not necessarily address the problems which we are trying to solve.

## Types
Crystal includes different metrics to rate and review creative works that makes sense for the type of work. We intend to adapt these types and add new ones as we consider new versions of creative works and as we consider new use cases.

### Albedo
This feedback method is our default feedback method which can be changed at any time with the help of other developers/designers working on this.

The Albedo method relies on three tri-bools that are used to score a creative work in order to determine whether it should be trusted.

#### Accuracy
Accuracy determines if any new or existing information presented is accurate to the best knowledge of the reader.

#### Coverage
Coverage determines if the information presented discusses the information that is implied by the claims that the work notes.

#### Clarity
Clarity determines if the information that has been presented is clear to readers.

#### Note
An optional text note that adds some information about the piece that the user may want to keep in mind.

#### Examples
Keep in mind that the following are very rough examples based on a single persons opinion. The examples that follow will be changed in order to


News Article - A news article presents some information about a politician commiting a crime. The header, description, and tone of the article implies that they were wrongfully accused of said crime. The article presents information that implies that no crime was commited, while avoiding certain information that the reader may need to form am informed decision.

Accuracy - The reader will need to make a decision of whether they consider the facts presented accurate. 

Coverage - 

Clarity - 

---

Opinion Piece - An anchor in their spare time wants to defend billionaires for the contributions that they make to certain non-profit organizations. They go on to point out various contributions from people like Jeff Bezos, Elon Musk, and Bill Gates in order to build sypathy for the rich and show how efficient they are to the reader.

Accuracy - The reader notices that this is an opinion piece and immediately marks this metric down.

Coverage - The reader notices that this opinion piece covers a good amount of information of how billionaires make contributions, but doesn't go into any kind of discussion on how their individual contributions do not solve systemic issues that would be better handled if that power was in someone elses hands. The reader can choose whether or not they will upvote or downvote.

Clarity - The reader understand the opinion that the reader is trying to make and the information presented makes sense.