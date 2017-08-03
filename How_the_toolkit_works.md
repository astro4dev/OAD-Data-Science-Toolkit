How the toolkit works
===================

<p align="center"><img src="https://raw.githubusercontent.com/astro4dev/OAD-Data-Science-Toolkit/master/img/DST_logo_250px.png" alt="DST Logo"/></p>

## Step 1 - Adding toolkit content
The toolkit content is stored on the github servers under the <a href="https://github.com/astro4dev/OAD-Data-Science-Toolkit" target="_blank">OAD-Data-Science-Toolkit</a> repository. Content is added by individual contributors by cloning the repository, making the changes, then creating a pull request. A description of the workflow can be found [here](How_to_upload_content.md). The astro4dev data science working group are automatically informed about the new pull request. The request is then verified before it is added to the main astro4dev repository.

## Step 2 - Adding the content to the database

Once the content has been uploaded to GitHub it has to be added to the MySQL database. This is done by a member of the astro4dev data science working group. The database is composed of many tables which can be dividied into two types.

- Content tables
- Relational tables

### The content tables
The content tables have one word names, e.g. _skills_ and contain information such as the title of the contribution and the link to where it is located on GitHub.

### The connector tables
These tabels are required to connect the content tables in the database. Connector tables all contain a double underscore '__' so they can easily be identified. They have been created so that new tables can easily be added later. Also, it drastically cuts down the size of each individual table (look up _relational databases_). If we wish to connect two content tables, such as _skills_ and _examples_ we have to create an entry in the connector table _skills__examples_. Each time a new piece of content is added to GitHub a *minimum of three* tables have to be updated. Say an example has been added. For it to be properly added to the database, each table with _"example"_ in it's name has to be updated. Here is an example of how the tables are connected.

<p align="center"><img src="https://raw.githubusercontent.com/astro4dev/OAD-Data-Science-Toolkit/master/img/database_structure.png" alt="database structure"/></p>