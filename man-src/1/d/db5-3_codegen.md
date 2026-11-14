---
title: "db5-3_codegen(1)"
name: "db5-3_codegen"
section: "1"
letter: "d"
url: "/docs/linux/man/1-db5-3_codegen/"
description: "db5.3_codegen – generate application code for Berkeley DB"
---

<p>Berkeley DB</p>
<h2>Name</h2>
<p><code>db5.3_codegen</code> &#8211; generate application code for Berkeley DB </p>
<h2>Synopsis</h2>
<p>[-<code>Vv </code>[-<code>a </code><i>api</i> ] ] [-<code>i </code><i>file</i> ] [-<code>o </code><i>prefix</i> ]</p>
<h2>Description</h2>
<p>The utility generates application code to create and configure Berkeley DB database environments and databases based on a simple description language and writes it to one or more output files. The generated code may need modification, in the case of complicated applications, but will usually significantly reduce the time required to create Berkeley DB applications. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-a </code><i>api</i></p>
<dd>Generate code for the specified API (currently, only Do c Dc is accepted )</p>
<dt><code>-i </code><i>file</i></p>
<dd>Specify an input <i>file</i> by default, standard input is used.</p>
<dt><code>-o </code><i>prefix</i></p>
<dd>Specify an output file <i>prefix</i> by default, &#8220;application&#8221; is used.</p>
<dt><code>-V</code></p>
<dd>Write the library version number to standard output and exit.</p>
<dt><code>-v</code></p>
<dd>Run in verbose mode.</dl>
<p> The utility exits 0 on success, and &gt;0 if an error occurs.</p>
<h2>C Language Specific Information</h2>
<p>By default, when the utility generates C-language code, the output file is named &#8220;application.c &#8221; The output filename can be specified with the &#8211;<code>o</code> option. </p>
<p> At the beginning of the output file is a list of public database environment (Vt DB_ENV ) handles and database (Vt DB ) handles, as specified by the description language. The database environment handle variables are named &#8220;<i>XXX </i><code>_dbenv</code> &#8221; where &#8220;<i>XXX</i> &#8221; is the name of the environment in the input specification. For databases associated with a database environment, the database handle variables are named &#8220;<i>XXX </i><code>_ </code><i>YYY</i> &#8221; where &#8220;<i>XXX</i> &#8221; is the name of the environment, and &#8220;<i>YYY</i> &#8221; is the name of the database. For standalone databases, the database handle variables are named &#8220;<i>XXX</i> &#8221; where &#8220;<i>XXX</i> &#8221; is the name of the database. </p>
<p> There are two public functions in the output file: Fn bdb_startup and Fn bdb_shutdown . The Fn bdb_startup function should be called to create and configure the database environments and databases, and the Fn bdb_shutdown function should be called to gracefully shut down the environments and databases.</p>
<h2>Specification Language</h2>
<p>The uses a simple description language: </p>
<ul>
<li> Lines in the input consist of white-space separated tokens.
<li> Tokens are case-insensitive.
<li> Empty lines and lines where the first non-space character is a hash mark (&#8220;#&#8221; ) are ignored. In addition, hash marks may appear in lines, in which case the content of the line from the hash mark to the end of the line is ignored. </ul>
<p> There are two top-level objects: &#8220;environment&#8221; and &#8220;database&#8221; which correspond to database environments and databases, respectively. These top-level objects can be associated with keywords to describe their configuration and relationships. </p>
<p> For example, the following input would create two standalone databases: </p>
<blockquote>
<pre>database data_one {
 type btree
}
database data_two {
 type btree
}</pre>
</blockquote>
<p> In this case, there would be no Vt DB_ENV handle, and the public Vt DB handles would be: </p>
<blockquote>
<pre>DB *data_one;
DB *data_two;</pre>
</blockquote>
<p> For example, the following input would create a database environment which contains three databases: </p>
<blockquote>
<pre>environment myenv {
 database data_one {
 type btree
 }
 database data_two {
 type btree
 }
 database data_three {
 type btree
 }
}</pre>
</blockquote>
<p> In this case, the public Vt DB_ENV and Vt DB handles would be: </p>
<blockquote>
<pre>DB_ENV *myenv_dbenv;
DB *myenv_data_one;
DB *myenv_data_two;
DB *myenv_data_three;</pre>
</blockquote>
<p> A variety of keywords can be specified for the databases and the environments. For example, the cache size can be specified for the database environment, and the page size can be specified for the database, as well as for secondary relationships: </p>
<blockquote>
<pre>environment myenv {
 cachesize 2 0 10
 database data_one {
 type btree
 pagesize 1024
 }
 database data_two {
 primary data_one
 secondary_offset 10 15
 type btree
 pagesize 32768
 }
 database data_three {
 type btree
 pagesize 512
 }
}</pre>
</blockquote>
<h3>Environment Keywords</h3>
<dl>
<dt><code>environment</code></p>
<dd>Start a database environment block. </p>
<p> There must be three tokens on the line: the keyword, the name of the environment and an opening brace (&#8220;{&#8221; )</p>
<dt><code>home</code></p>
<dd>Specify the database environment home directory. </p>
<p> There must be two tokens on the line: the keyword and the home directory.</p>
<dt><code>cachesize</code></p>
<dd>Specify the database environment cache size. </p>
<p> There must be two tokens on the line: the keyword, the gigabytes of cache, the bytes of cache, and the number of caches (the number of underlying physical areas into which the cache is logically divided).</p>
<dt><code>private</code></p>
<dd>Specify the database environment is private. </p>
<p> There must be one token on the line: the keyword by itself.</p>
<dt><code>}</code></p>
<dd>End the database environment block. </p>
<p> There must be one token on the line: the keyword by itself.</dl>
<h3>Database Keywords</h3>
<dl>
<dt><code>database</code></p>
<dd>Start a database block. </p>
<p> There must be three tokens on the line: the keyword, the name of the database and an opening brace (&#8220;{&#8221; )</p>
<dt><code>custom</code></p>
<dd>Specify a custom key-comparison routine. This is used when the Btree database requires a specific sort that cannot generate. A stub key comparison routine will be created and configured for the database which should be modified as necessary. See the &#8220;<code>key_type</code> &#8221; keyword for more information. </p>
<p> There must be one token on the line: the keyword by itself.</p>
<dt><code>dupsort</code></p>
<dd>Configure the database to support sorted duplicates. </p>
<p> There must be one token on the line: the keyword by itself.</p>
<dt><code>extentsize</code></p>
<dd>Configure the size of the Queue database extent files. </p>
<p> There must be two tokens on the line: the keyword and the extent file size, as a number of pages.</p>
<dt><code>key_type</code></p>
<dd>Configure a integral type key-comparison routine. This is used when the Btree database key is an integral type (such as &#8220;Vt unsigned int &#8221; or &#8220;Vt u_int32_t ) &#8221; Any C-language integral type may be specified. See the &#8220;<code>custom</code> &#8221; keyword for more information. A Btree comparison routine based on the type of the key will be created and configured. </p>
<p> There must be two tokens on the line: the keyword and the type.</p>
<dt><code>pagesize</code></p>
<dd>Configure the database page size. </p>
<p> There must be two tokens on the line: the keyword and the page size in bytes.</p>
<dt><code>primary</code></p>
<dd>Configure the database as a secondary index. A stub secondary callback routine will be created and configured for the database, which should be modified as necessary. See the &#8220;<code>secondary_offset</code> &#8221; keyword for more information. </p>
<p> There must be two tokens on the line: the keyword and the name of the primary database for which this database is a secondary.</p>
<dt><code>recnum</code></p>
<dd>Configure the Btree database to support record number access. </p>
<p> There must be one token on the line: the keyword by itself.</p>
<dt><code>re_len</code></p>
<dd>Configure the record length for a Queue database or a fixed-length Recno database. </p>
<p> There must be two tokens on the line: the keyword and the length of a record, in bytes. </p>
<dt><code>secondary_offset</code></p>
<dd>Configure a secondary callback routine based on a byte string found in the primary database&#8217;s data item. </p>
<p> There must be three tokens on the line: the keyword, the byte offset from the beginning of the primary data item where the secondary key occurs, and the length of the secondary key in bytes.</p>
<dt><code>transaction</code></p>
<dd>Configure the database (and, by extension, the database environment), to be transactional. </p>
<p> There must be one token on the line: the keyword by itself.</p>
<dt><code>type</code></p>
<dd>Configure the database type. </p>
<p> There must be two tokens on the line: the keyword and the type, where the type is one of &#8220;btree&#8221; &#8220;hash&#8221; &#8220;queue&#8221; or &#8220;recno&#8221;</p>
<dt><code>}</code></p>
<dd>End the database environment block. </p>
<p> There must be one token on the line: the keyword by itself.</dl>
<h2>Authors</h2>
<p>An Thorsten Glaser Aq tg [at] debian.org wrote this manual page for the Debian project (but may be used by others) after the original HTML format documentation Copyright &#169; 1996,2008 Oracle. All rights reserved.</p>
