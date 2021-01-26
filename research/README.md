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