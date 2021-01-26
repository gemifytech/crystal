# Resarch
Research has been done to get us to where we are now and that reseach will continue to allow us to build something that continues to serve additional use cases. We are building Crystal to combat the spread of misinformation.

# GEM Protocol
Similar to other protocols like the OGP, we have designed a protocol to help satisfy the needs of...

# Meta Tags
- gem:id - The UUID associated with the creative work published.
- gem:url - The canonical URL of your creative work that will be used to identify where the creative work was first published, e.g., "https://emerald.gemify.com/report/1/".
- gem:title - The title of your creative work as it should appear within the graph, e.g., "Megacorp did X".
- gem:type - The type of your creative work, e.g., "article.web". Depending on the type you specify, other properties may also be required.
- gem:site_name - The name of the platform that the creative work was originally published to.
- gem:author - The name of the author who created the work.
- gem:published_date - The date the the creative work was published.
- gem:modified_date - The dates that the creative work was modified.
- gem:topic - The topic used to easily categorize.

## Entry Types

---

`webarticle`

An article from a web article.

Required fields: author, title, journal, year, volume

Optional fields: 

`journalarticle`

An article from a journal.

Required fields: author, title, journal, year, volume

Optional fields: number, pages, month, doi, note, key

`magazinearticle`

An article from a magazine.

Required fields: author, title, journal, year, volume

Optional fields: number, pages, month, doi, note, key

`manualarticle`

A manual article.

`newspaperarticle`

A newspaper article.

`ancienttext`

Ancient text.

`artwork`

Ancient text.

`audiovisualmaterial`

Audio visual material.

`bill`

A bill.

`book`

A book with an explicit publisher.

Required fields: author/editor, title, publisher, year

Optional fields: volume/number, series, address, edition, month, note, key, url

`booklet`

A work that is printed and bound, but without a named publisher or sponsoring institution.

Required fields: title

Optional fields: author, howpublished, address, month, year, note, key

`case`

A case.

`catalog`

A catalog.

`chart`

A chart.

`classicalwork`

A classical work.

`computerprogram`

A computer program.

`conference`

The same as `inproceedings`, included for [Scribe](https://en.wikipedia.org/wiki/Scribe_(markup_language)) compatibility.

`dictionary`

A dictionary.

`encyclopedia`

An encyclopedia.

`equation`

An equation.

`figure`

A figure.

`grant`

A grant.

`governmentdocument`

A government document.

`hearing`

A hearing.

`inbook`

A part of a book, usually untitled. May be a chapter (or section, etc.) and/or a range of pages.

Required fields: author/editor, title, chapter/pages, publisher, year

Optional fields: volume/number, series, type, address, edition, month, note, key

`incollection`

A part of a book having its own title.

Required fields: author, title, booktitle, publisher, year

Optional fields: editor, volume/number, series, type, chapter, pages, address, edition, month, note, key

`inproceedings`

An article in a conference proceedings.

Required fields: author, title, booktitle, year

Optional fields: editor, volume/number, series, pages, address, month, organization, publisher, note, key

`legalrule`

A legal rule.

`manual`

Technical documentation.Required fields: title

Optional fields: author, organization, address, edition, month, year, note, key

`manuscript`

A manuscript

`map`

A map.

`mastersthesis`

A [Master's](https://en.wikipedia.org/wiki/Master%27s_degree) [thesis](https://en.wikipedia.org/wiki/Thesis).

Required fields: author, title, school, year

Optional fields: type, address, month, note, key

`misc`

For use when nothing else fits.

Required fields: none

Optional fields: author, title, howpublished, month, year, note, key

`music`

A piece of music.

`pamphlet`

A pamphlet.

`patent`

A patent.

`personalcommunication`

Personal communication.

`phdthesis`

A [Ph.D.](https://en.wikipedia.org/wiki/Doctor_of_Philosophy) thesis.

Required fields: author, title, school, year

Optional fields: type, address, month, note, key

`proceedings`

The proceedings of a conference.

Required fields: title, year

Optional fields: editor, volume/number, series, address, month, publisher, organization, note, key

`report`

A report published by a school or other institution, usually numbered within a series.

Required fields: author, title, institution, year

Optional fields: type, number, address, month, note, key

`serialpublication`

A serial publication.

`standard`

A standard.

`statute`

A statute.

`unpublished`

A document having an author and title, but not formally published.

Required fields: author, title, note

Optional fields: month, year, key

`webpage`

A webpage

`aggregatedatabase`

An aggregate database.

`onlinedatabase`

An online database.

## Field Types

`type` - 1

The field overriding the default type of publication (e.g. "Research Note" for techreport, "{PhD} dissertation" for phdthesis, "Section" for inbook/incollection)

### Author Info

`author` - 101

The name(s) of the author(s) (in the case of more than one author, separated by `and`)

`secondaryauthor` - 102

The name(s) of the secondary author(s) (typically an editor, separated by `and`)

`subsidiaryauthor` - 103

The name(s) of the secondary author(s) (typically an editor, separated by `and`)

`email` - 151

The email of the author(s)

`address` - 10

Publisher's address (usually just the city, but can be the full address for lesser-known publishers)

### Source Info

`title` - 201

The title of the work

`shorttitle` - 202

A shortened title of the work

`secondarytitle` - 203

The title of the book, if only part of it is being cited or a conference name

`alternatetitle` - 204

The title of the book, if only part of it is being cited or a conference name

`translatedtitle` - 205

The title of the book, if only part of it is being cited or a conference name

`tertiarytitle` - 206

The title of the book, if only part of it is being cited or a conference name

`pages` - 31

Page numbers, separated either by commas or double-hyphens.

`abstract` -14

An abstract of the work.

`edition` - 18

The edition of a book, long form (such as "First" or "Second")

`volume` - 37

The volume of a journal or multi-volume book

`series` - 35

The series of books the book was published in (e.g. "[The Hardy Boys](https://en.wikipedia.org/wiki/The_Hardy_Boys)" or "[Lecture Notes in Computer Science](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science)")

`section` - 30

The section.

`chapter` - 15

The chapter number

`number` - 27

The "(issue) number" of a journal, magazine, or tech-report, if applicable. Note that this is not the "article number" assigned by some journals.

`label` - 28

A label.

`url` - 13

The url of the work.

`annote` - 11

An annotation for annotated bibliography styles (not typical)

### Publisher Info

`publisher` - 32

The publisher's name

`originalpublication` - 33

The original publication name.

### Time Info

`month` - 502

The month of publication (or, if unpublished, the month of creation)

`year` - 501

The year of publication (or, if unpublished, the year of creation)

`publishdate` - 551

The date the work was published.

`accessdate` - 552

The date the work was accessed.

`modifydate` - 553

The date the work was modified.

`crossref` - 16

The key of the cross-referenced entry

`doi` - 17

digital object identifier

`reprintedition` - 19

The edition of a book, long form (such as "First" or "Second")

`editor` - 20

The name(s) of the editor(s)

`howpublished` - 21

How it was published, if the publishing method is nonstandard

`institution` - 22

The institution that was involved in the publishing, but not necessarily the publisher

`journal` - 23

The journal or magazine the work was published in

`key` - 24

A hidden field used for specifying or overriding the alphabetical
order of entries (when the "author" and "editor" fields are missing).
Note that this is very different from the key (mentioned just after this list) that is used to cite or cross-reference the entry.

`organization` - 29

The conference sponsor

`school` - 34

The school where the thesis was written

`callnumber` - 39

A call number

`accessionnumber` - 40

unique identifier assigned to, and achieving initial control of, each acquisition

`databaseprovider` - 41

The database provider.

`databasename` - 42

The database name.

`ISBN`

The ISBN is an International Standard Book Number. Since 2007, this number is a 13 digit number that helps to identify a specific book variant that has been published. Every different type of the same book which gets published needs to have its own ISBN. This means a hardcover book and a paperback book, although the manuscript is exactly the same, are going to have a different assigned ISBN because they are each a publication variant.

`ISSN` - 43

The database name.

`note` - 26

Miscellaneous extra information

`tags` - 26

Miscellaneous extra information

`material` - 26

Miscellaneous extra information