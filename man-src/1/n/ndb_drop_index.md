---
title: "ndb_drop_index(1)"
name: "ndb_drop_index"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ndb_drop_index/"
description: "ndb_drop_index – drop index from an NDB table"
---

<h2 class="name">NAME</h2>
<p> ndb_drop_index &#8211; drop index from an NDB table </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ndb_drop_index </code><i>options</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>ndb_drop_index</code></p>
<dd>drops the specified index from an NDB table. <i>It is recommended that you use this utility only as an example for writing NDB API applications</i> &#8212; see the Warning later in this section for details. </p>
<p> <code>Usage</code>: </p>
<dl>
<dt>
<dd>
<pre>
ndb_drop_index -c <i>connect_string</i> <i>table_name</i> <i>index</i> -d <i>db_name</i>
</pre>
</dl>
<p> The statement shown above drops the index named <i>index</i> from the <i>table</i> in the <i>database</i>. </p>
<p> <code>Additional Options</code>: None that are specific to this application. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Warning</code> </font> </p>
<p> <i>Operations performed on Cluster table indexes using the NDB API are not visible to MySQL and make the table unusable by a MySQL server</i>. If you use this program to drop an index, then try to access the table from an SQL node, an error results, as shown here: </p>
</dl>
<dl>
<dt>
<dd>
<pre><code>
shell&gt; ./ndb_drop_index -c localhost dogs ix -d ctest1
Dropping index dogs/idx...OK
NDBT_ProgramExit: 0 - OK
shell&gt; ./mysql -u jon -p ctest1
Enter password: *******
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 7 to server version: 5.1.44-ndb-7.1.4
Type 'help;' or '\h' for help. Type '
