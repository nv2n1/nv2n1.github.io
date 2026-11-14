---
title: "tctdb(3)"
name: "tctdb"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tctdb/"
description: "tctdb – the table database API"
---

<p>tctdb &#8211; the table database API</p>
<h2>Description</h2>
<p>Table database is a file containing records composed of the primary keys and arbitrary columns and is handled with the table database API. To use the table database API, include `<code>tcutil.h</code>&#8216;, `<code>tctdb.h</code>&#8216;, and related standard header files. Usually, write the following description near the front of a source file. </p>
<pre><code>#include &lt;tcutil.h&gt;

#include &lt;tctdb.h&gt;

#include &lt;stdlib.h&gt;

#include &lt;stdbool.h&gt;

#include &lt;stdint.h&gt;</code></pre>
<p> Objects whose type is pointer to `<code>TCTDB</code>&#8216; are used to handle table databases. A table database object is created with the function `<code>tctdbnew</code>&#8216; and is deleted with the function `<code>tctdbdel</code>&#8216;. To avoid memory leak, it is important to delete every object when it is no longer in use. Before operations to store or retrieve records, it is necessary to open a database file and connect the table database object to it. The function `<code>tctdbopen</code>&#8216; is used to open a database file and the function `<code>tctdbclose</code>&#8216; is used to close the database file. To avoid data missing or corruption, it is important to close every database file when it is no longer in use. It is forbidden for multible database objects in a process to open the same database at the same time. </p>
<h2>Api</h2>
<p>The function `tctdberrmsg&#8217; is used in order to get the message string corresponding to an error code. </p>
<dl>
<dd><code>const char *tctdberrmsg(int </code><i>ecode</i><code>);</code></p>
<dl>
<dd>`<i>ecode</i>&#8216; specifies the error code.</dl>
<dl>
<dd>The return value is the message string of the error code.</dl>
</dl>
<p> The function `tctdbnew&#8217; is used in order to create a table database object. </p>
<dl>
<dd><code>TCTDB *tctdbnew(void);</code></p>
<dl>
<dd>The return value is the new table database object.</dl>
</dl>
<p> The function `tctdbdel&#8217; is used in order to delete a table database object. </p>
<dl>
<dd><code>void tctdbdel(TCTDB *</code><i>tdb</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object.</dl>
<dl>
<dd>If the database is not closed, it is closed implicitly. Note that the deleted object and its derivatives can not be used anymore.</dl>
</dl>
<p> The function `tctdbecode&#8217; is used in order to get the last happened error code of a table database object. </p>
<dl>
<dd><code>int tctdbecode(TCTDB *</code><i>tdb</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object.</dl>
<dl>
<dd>The return value is the last happened error code.</dl>
<dl>
<dd>The following error codes are defined: `TCESUCCESS&#8217; for success, `TCETHREAD&#8217; for threading error, `TCEINVALID&#8217; for invalid operation, `TCENOFILE&#8217; for file not found, `TCENOPERM&#8217; for no permission, `TCEMETA&#8217; for invalid meta data, `TCERHEAD&#8217; for invalid record header, `TCEOPEN&#8217; for open error, `TCECLOSE&#8217; for close error, `TCETRUNC&#8217; for trunc error, `TCESYNC&#8217; for sync error, `TCESTAT&#8217; for stat error, `TCESEEK&#8217; for seek error, `TCEREAD&#8217; for read error, `TCEWRITE&#8217; for write error, `TCEMMAP&#8217; for mmap error, `TCELOCK&#8217; for lock error, `TCEUNLINK&#8217; for unlink error, `TCERENAME&#8217; for rename error, `TCEMKDIR&#8217; for mkdir error, `TCERMDIR&#8217; for rmdir error, `TCEKEEP&#8217; for existing record, `TCENOREC&#8217; for no record found, and `TCEMISC&#8217; for miscellaneous error.</dl>
</dl>
<p> The function `tctdbsetmutex&#8217; is used in order to set mutual exclusion control of a table database object for threading. </p>
<dl>
<dd><code>bool tctdbsetmutex(TCTDB *</code><i>tdb</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object which is not opened.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Note that the mutual exclusion control is needed if the object is shared by plural threads and this function should be called before the database is opened.</dl>
</dl>
<p> The function `tctdbtune&#8217; is used in order to set the tuning parameters of a table database object. </p>
<dl>
<dd><code>bool tctdbtune(TCTDB *</code><i>tdb</i><code>, int64_t </code><i>bnum</i><code>, int8_t </code><i>apow</i><code>, int8_t </code><i>fpow</i><code>, uint8_t </code><i>opts</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object which is not opened.</dl>
<dl>
<dd>`<i>bnum</i>&#8216; specifies the number of elements of the bucket array. If it is not more than 0, the default value is specified. The default value is 131071. Suggested size of the bucket array is about from 0.5 to 4 times of the number of all records to be stored.</dl>
<dl>
<dd>`<i>apow</i>&#8216; specifies the size of record alignment by power of 2. If it is negative, the default value is specified. The default value is 4 standing for 2^4=16.</dl>
<dl>
<dd>`<i>fpow</i>&#8216; specifies the maximum number of elements of the free block pool by power of 2. If it is negative, the default value is specified. The default value is 10 standing for 2^10=1024.</dl>
<dl>
<dd>`<i>opts</i>&#8216; specifies options by bitwise-or: `TDBTLARGE&#8217; specifies that the size of the database can be larger than 2GB by using 64-bit bucket array, `TDBTDEFLATE&#8217; specifies that each record is compressed with Deflate encoding, `TDBTBZIP&#8217; specifies that each record is compressed with BZIP2 encoding, `TDBTTCBS&#8217; specifies that each record is compressed with TCBS encoding.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Note that the tuning parameters should be set before the database is opened.</dl>
</dl>
<p> The function `tctdbsetcache&#8217; is set the caching parameters of a table database object. </p>
<dl>
<dd><code>bool tctdbsetcache(TCTDB *</code><i>tdb</i><code>, int32_t </code><i>rcnum</i><code>, int32_t </code><i>lcnum</i><code>, int32_t </code><i>ncnum</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object which is not opened.</dl>
<dl>
<dd>`<i>rcnum</i>&#8216; specifies the maximum number of records to be cached. If it is not more than 0, the record cache is disabled. It is disabled by default.</dl>
<dl>
<dd>`<i>lcnum</i>&#8216; specifies the maximum number of leaf nodes to be cached. If it is not more than 0, the default value is specified. The default value is 4096.</dl>
<dl>
<dd>`<i>ncnum</i>&#8216; specifies the maximum number of non-leaf nodes to be cached. If it is not more than 0, the default value is specified. The default value is 512.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Note that the caching parameters should be set before the database is opened. Leaf nodes and non-leaf nodes are used in column indices.</dl>
</dl>
<p> The function `tctdbsetxmsiz&#8217; is used in order to set the size of the extra mapped memory of a table database object. </p>
<dl>
<dd><code>bool tctdbsetxmsiz(TCTDB *</code><i>tdb</i><code>, int64_t </code><i>xmsiz</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object which is not opened.</dl>
<dl>
<dd>`<i>xmsiz</i>&#8216; specifies the size of the extra mapped memory. If it is not more than 0, the extra mapped memory is disabled. The default size is 67108864.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Note that the mapping parameters should be set before the database is opened.</dl>
</dl>
<p> The function `tctdbsetdfunit&#8217; is used in order to set the unit step number of auto defragmentation of a table database object. </p>
<dl>
<dd><code>bool tctdbsetdfunit(TCTDB *</code><i>tdb</i><code>, int32_t </code><i>dfunit</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object which is not opened.</dl>
<dl>
<dd>`<i>dfunit</i>&#8216; specifie the unit step number. If it is not more than 0, the auto defragmentation is disabled. It is disabled by default.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Note that the defragmentation parameters should be set before the database is opened.</dl>
</dl>
<p> The function `tctdbopen&#8217; is used in order to open a database file and connect a table database object. </p>
<dl>
<dd><code>bool tctdbopen(TCTDB *</code><i>tdb</i><code>, const char *</code><i>path</i><code>, int </code><i>omode</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object which is not opened.</dl>
<dl>
<dd>`<i>path</i>&#8216; specifies the path of the database file.</dl>
<dl>
<dd>`<i>omode</i>&#8216; specifies the connection mode: `TDBOWRITER&#8217; as a writer, `TDBOREADER&#8217; as a reader. If the mode is `TDBOWRITER&#8217;, the following may be added by bitwise-or: `TDBOCREAT&#8217;, which means it creates a new database if not exist, `TDBOTRUNC&#8217;, which means it creates a new database regardless if one exists, `TDBOTSYNC&#8217;, which means every transaction synchronizes updated contents with the device. Both of `TDBOREADER&#8217; and `TDBOWRITER&#8217; can be added to by bitwise-or: `TDBONOLCK&#8217;, which means it opens the database file without file locking, or `TDBOLCKNB&#8217;, which means locking is performed without blocking.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
</dl>
<p> The function `tctdbclose&#8217; is used in order to close a table database object. </p>
<dl>
<dd><code>bool tctdbclose(TCTDB *</code><i>tdb</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Update of a database is assured to be written when the database is closed. If a writer opens a database but does not close it appropriately, the database will be broken.</dl>
</dl>
<p> The function `tctdbput&#8217; is used in order to store a record into a table database object. </p>
<dl>
<dd><code>bool tctdbput(TCTDB *</code><i>tdb</i><code>, const void *</code><i>pkbuf</i><code>, int </code><i>pksiz</i><code>, TCMAP *</code><i>cols</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object connected as a writer.</dl>
<dl>
<dd>`<i>pkbuf</i>&#8216; specifies the pointer to the region of the primary key.</dl>
<dl>
<dd>`<i>pksiz</i>&#8216; specifies the size of the region of the primary key.</dl>
<dl>
<dd>`<i>cols</i>&#8216; specifies a map object containing columns.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the database, it is overwritten.</dl>
</dl>
<p> The function `tctdbput2&#8242; is used in order to store a string record into a table database object with a zero separated column string. </p>
<dl>
<dd><code>bool tctdbput2(TCTDB *</code><i>tdb</i><code>, const void *</code><i>pkbuf</i><code>, int </code><i>pksiz</i><code>, const void *</code><i>cbuf</i><code>, int </code><i>csiz</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object connected as a writer.</dl>
<dl>
<dd>`<i>pkbuf</i>&#8216; specifies the pointer to the region of the primary key.</dl>
<dl>
<dd>`<i>pksiz</i>&#8216; specifies the size of the region of the primary key.</dl>
<dl>
<dd>`<i>cbuf</i>&#8216; specifies the pointer to the region of the zero separated column string where the name and the value of each column are situated one after the other.</dl>
<dl>
<dd>`<i>csiz</i>&#8216; specifies the size of the region of the column string.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the database, it is overwritten.</dl>
</dl>
<p> The function `tctdbput3&#8242; is used in order to store a string record into a table database object with a tab separated column string. </p>
<dl>
<dd><code>bool tctdbput3(TCTDB *</code><i>tdb</i><code>, const char *</code><i>pkstr</i><code>, const char *</code><i>cstr</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object connected as a writer.</dl>
<dl>
<dd>`<i>pkstr</i>&#8216; specifies the string of the primary key.</dl>
<dl>
<dd>`<i>cstr</i>&#8216; specifies the string of the the tab separated column string where the name and the value of each column are situated one after the other.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the database, it is overwritten.</dl>
</dl>
<p> The function `tctdbputkeep&#8217; is used in order to store a new record into a table database object. </p>
<dl>
<dd><code>bool tctdbputkeep(TCTDB *</code><i>tdb</i><code>, const void *</code><i>pkbuf</i><code>, int </code><i>pksiz</i><code>, TCMAP *</code><i>cols</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object connected as a writer.</dl>
<dl>
<dd>`<i>pkbuf</i>&#8216; specifies the pointer to the region of the primary key.</dl>
<dl>
<dd>`<i>pksiz</i>&#8216; specifies the size of the region of the primary key.</dl>
<dl>
<dd>`<i>cols</i>&#8216; specifies a map object containing columns.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the database, this function has no effect.</dl>
</dl>
<p> The function `tctdbputkeep2&#8242; is used in order to store a new string record into a table database object with a zero separated column string. </p>
<dl>
<dd><code>bool tctdbputkeep2(TCTDB *</code><i>tdb</i><code>, const void *</code><i>pkbuf</i><code>, int </code><i>pksiz</i><code>, const void *</code><i>cbuf</i><code>, int </code><i>csiz</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object connected as a writer.</dl>
<dl>
<dd>`<i>pkbuf</i>&#8216; specifies the pointer to the region of the primary key.</dl>
<dl>
<dd>`<i>pksiz</i>&#8216; specifies the size of the region of the primary key.</dl>
<dl>
<dd>`<i>cbuf</i>&#8216; specifies the pointer to the region of the zero separated column string where the name and the value of each column are situated one after the other.</dl>
<dl>
<dd>`<i>csiz</i>&#8216; specifies the size of the region of the column string.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the database, this function has no effect.</dl>
</dl>
<p> The function `tctdbputkeep3&#8242; is used in order to store a new string record into a table database object with a tab separated column string. </p>
<dl>
<dd><code>bool tctdbputkeep3(TCTDB *</code><i>tdb</i><code>, const char *</code><i>pkstr</i><code>, const char *</code><i>cstr</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object connected as a writer.</dl>
<dl>
<dd>`<i>pkstr</i>&#8216; specifies the string of the primary key.</dl>
<dl>
<dd>`<i>cstr</i>&#8216; specifies the string of the the tab separated column string where the name and the value of each column are situated one after the other.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the database, this function has no effect.</dl>
</dl>
<p> The function `tctdbputcat&#8217; is used in order to concatenate columns of the existing record in a table database object. </p>
<dl>
<dd><code>bool tctdbputcat(TCTDB *</code><i>tdb</i><code>, const void *</code><i>pkbuf</i><code>, int </code><i>pksiz</i><code>, TCMAP *</code><i>cols</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object connected as a writer.</dl>
<dl>
<dd>`<i>pkbuf</i>&#8216; specifies the pointer to the region of the primary key.</dl>
<dl>
<dd>`<i>pksiz</i>&#8216; specifies the size of the region of the primary key.</dl>
<dl>
<dd>`<i>cols</i>&#8216; specifies a map object containing columns.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If there is no corresponding record, a new record is created.</dl>
</dl>
<p> The function `tctdbputcat2&#8242; is used in order to concatenate columns in a table database object with a zero separated column string. </p>
<dl>
<dd><code>bool tctdbputcat2(TCTDB *</code><i>tdb</i><code>, const void *</code><i>pkbuf</i><code>, int </code><i>pksiz</i><code>, const void *</code><i>cbuf</i><code>, int </code><i>csiz</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object connected as a writer.</dl>
<dl>
<dd>`<i>pkbuf</i>&#8216; specifies the pointer to the region of the primary key.</dl>
<dl>
<dd>`<i>pksiz</i>&#8216; specifies the size of the region of the primary key.</dl>
<dl>
<dd>`<i>cbuf</i>&#8216; specifies the pointer to the region of the zero separated column string where the name and the value of each column are situated one after the other.</dl>
<dl>
<dd>`<i>csiz</i>&#8216; specifies the size of the region of the column string.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If there is no corresponding record, a new record is created.</dl>
</dl>
<p> The function `tctdbputcat3&#8242; is used in order to concatenate columns in a table database object with with a tab separated column string. </p>
<dl>
<dd><code>bool tctdbputcat3(TCTDB *</code><i>tdb</i><code>, const char *</code><i>pkstr</i><code>, const char *</code><i>cstr</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object connected as a writer.</dl>
<dl>
<dd>`<i>pkstr</i>&#8216; specifies the string of the primary key.</dl>
<dl>
<dd>`<i>cstr</i>&#8216; specifies the string of the the tab separated column string where the name and the value of each column are situated one after the other.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If there is no corresponding record, a new record is created.</dl>
</dl>
<p> The function `tctdbout&#8217; is used in order to remove a record of a table database object. </p>
<dl>
<dd><code>bool tctdbout(TCTDB *</code><i>tdb</i><code>, const void *</code><i>pkbuf</i><code>, int </code><i>pksiz</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object connected as a writer.</dl>
<dl>
<dd>`<i>pkbuf</i>&#8216; specifies the pointer to the region of the primary key.</dl>
<dl>
<dd>`<i>pksiz</i>&#8216; specifies the size of the region of the primary key.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
</dl>
<p> The function `tctdbout2&#8242; is used in order to remove a string record of a table database object. </p>
<dl>
<dd><code>bool tctdbout2(TCTDB *</code><i>tdb</i><code>, const char *</code><i>pkstr</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object connected as a writer.</dl>
<dl>
<dd>`<i>pkstr</i>&#8216; specifies the string of the primary key.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
</dl>
<p> The function `tctdbget&#8217; is used in order to retrieve a record in a table database object. </p>
<dl>
<dd><code>TCMAP *tctdbget(TCTDB *</code><i>tdb</i><code>, const void *</code><i>pkbuf</i><code>, int </code><i>pksiz</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object.</dl>
<dl>
<dd>`<i>pkbuf</i>&#8216; specifies the pointer to the region of the primary key.</dl>
<dl>
<dd>`<i>pksiz</i>&#8216; specifies the size of the region of the primary key.</dl>
<dl>
<dd>If successful, the return value is a map object of the columns of the corresponding record. `NULL&#8217; is returned if no record corresponds.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tcmapnew&#8217;, it should be deleted with the function `tcmapdel&#8217; when it is no longer in use.</dl>
</dl>
<p> The function `tctdbget2&#8242; is used in order to retrieve a record in a table database object as a zero separated column string. </p>
<dl>
<dd><code>char *tctdbget2(TCTDB *</code><i>tdb</i><code>, const void *</code><i>pkbuf</i><code>, int </code><i>pksiz</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object.</dl>
<dl>
<dd>`<i>pkbuf</i>&#8216; specifies the pointer to the region of the primary key.</dl>
<dl>
<dd>`<i>pksiz</i>&#8216; specifies the size of the region of the primary key.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the region of the column string of the corresponding record. `NULL&#8217; is returned if no record corresponds.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tctdbget3&#8242; is used in order to retrieve a string record in a table database object as a tab separated column string. </p>
<dl>
<dd><code>char *tctdbget3(TCTDB *</code><i>tdb</i><code>, const char *</code><i>pkstr</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object.</dl>
<dl>
<dd>`<i>pkstr</i>&#8216; specifies the string of the primary key.</dl>
<dl>
<dd>If successful, the return value is the tab separated column string of the corresponding record. `NULL&#8217; is returned if no record corresponds.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tctdbvsiz&#8217; is used in order to get the size of the value of a record in a table database object. </p>
<dl>
<dd><code>int tctdbvsiz(TCTDB *</code><i>tdb</i><code>, const void *</code><i>pkbuf</i><code>, int </code><i>pksiz</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the primary key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the primary key.</dl>
<dl>
<dd>If successful, the return value is the size of the value of the corresponding record, else, it is -1.</dl>
</dl>
<p> The function `tctdbvsiz2&#8242; is used in order to get the size of the value of a string record in a table database object. </p>
<dl>
<dd><code>int tctdbvsiz2(TCTDB *</code><i>tdb</i><code>, const char *</code><i>pkstr</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the primary key.</dl>
<dl>
<dd>If successful, the return value is the size of the value of the corresponding record, else, it is -1.</dl>
</dl>
<p> The function `tctdbiterinit&#8217; is used in order to initialize the iterator of a table database object. </p>
<dl>
<dd><code>bool tctdbiterinit(TCTDB *</code><i>tdb</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>The iterator is used in order to access the primary key of every record stored in a database.</dl>
</dl>
<p> The function `tctdbiternext&#8217; is used in order to get the next primary key of the iterator of a table database object. </p>
<dl>
<dd><code>void *tctdbiternext(TCTDB *</code><i>tdb</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the region of the next primary key, else, it is `NULL&#8217;. `NULL&#8217; is returned when no record is to be get out of the iterator.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use. It is possible to access every record by iteration of calling this function. It is allowed to update or remove records whose keys are fetched while the iteration. However, it is not assured if updating the database is occurred while the iteration. Besides, the order of this traversal access method is arbitrary, so it is not assured that the order of storing matches the one of the traversal access.</dl>
</dl>
<p> The function `tctdbiternext2&#8242; is used in order to get the next primary key string of the iterator of a table database object. </p>
<dl>
<dd><code>char *tctdbiternext2(TCTDB *</code><i>tdb</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object.</dl>
<dl>
<dd>If successful, the return value is the string of the next primary key, else, it is `NULL&#8217;. `NULL&#8217; is returned when no record is to be get out of the iterator.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use. It is possible to access every record by iteration of calling this function. However, it is not assured if updating the database is occurred while the iteration. Besides, the order of this traversal access method is arbitrary, so it is not assured that the order of storing matches the one of the traversal access.</dl>
</dl>
<p> The function `tctdbiternext3&#8242; is used in order to get the columns of the next record of the iterator of a table database object. </p>
<dl>
<dd><code>TCMAP *tctdbiternext3(TCTDB *</code><i>tdb</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object.</dl>
<dl>
<dd>If successful, the return value is a map object of the columns of the next record, else, it is `NULL&#8217;. `NULL&#8217; is returned when no record is to be get out of the iterator. The primary key is added into the map as a column of an empty string key.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tcmapnew&#8217;, it should be deleted with the function `tcmapdel&#8217; when it is no longer in use. It is possible to access every record by iteration of calling this function. However, it is not assured if updating the database is occurred while the iteration. Besides, the order of this traversal access method is arbitrary, so it is not assured that the order of storing matches the one of the traversal access.</dl>
</dl>
<p> The function `tctdbfwmkeys&#8217; is used in order to get forward matching primary keys in a table database object. </p>
<dl>
<dd><code>TCLIST *tctdbfwmkeys(TCTDB *</code><i>tdb</i><code>, const void *</code><i>pbuf</i><code>, int </code><i>psiz</i><code>, int </code><i>max</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object.</dl>
<dl>
<dd>`<i>pbuf</i>&#8216; specifies the pointer to the region of the prefix.</dl>
<dl>
<dd>`<i>psiz</i>&#8216; specifies the size of the region of the prefix.</dl>
<dl>
<dd>`<i>max</i>&#8216; specifies the maximum number of keys to be fetched. If it is negative, no limit is specified.</dl>
<dl>
<dd>The return value is a list object of the corresponding keys. This function does never fail. It returns an empty list even if no key corresponds.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use. Note that this function may be very slow because every key in the database is scanned.</dl>
</dl>
<p> The function `tctdbfwmkeys2&#8242; is used in order to get forward matching string primary keys in a table database object. </p>
<dl>
<dd><code>TCLIST *tctdbfwmkeys2(TCTDB *</code><i>tdb</i><code>, const char *</code><i>pstr</i><code>, int </code><i>max</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object.</dl>
<dl>
<dd>`<i>pstr</i>&#8216; specifies the string of the prefix.</dl>
<dl>
<dd>`<i>max</i>&#8216; specifies the maximum number of keys to be fetched. If it is negative, no limit is specified.</dl>
<dl>
<dd>The return value is a list object of the corresponding keys. This function does never fail. It returns an empty list even if no key corresponds.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use. Note that this function may be very slow because every key in the database is scanned.</dl>
</dl>
<p> The function `tctdbaddint&#8217; is used in order to add an integer to a column of a record in a table database object. </p>
<dl>
<dd><code>int tctdbaddint(TCTDB *</code><i>tdb</i><code>, const void *</code><i>pkbuf</i><code>, int </code><i>pksiz</i><code>, int </code><i>num</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object connected as a writer.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the primary key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the primary key.</dl>
<dl>
<dd>`<i>num</i>&#8216; specifies the additional value.</dl>
<dl>
<dd>If successful, the return value is the summation value, else, it is `INT_MIN&#8217;.</dl>
<dl>
<dd>The additional value is stored as a decimal string value of a column whose name is &quot;_num&quot;. If no record corresponds, a new record with the additional value is stored.</dl>
</dl>
<p> The function `tctdbadddouble&#8217; is used in order to add a real number to a column of a record in a table database object. </p>
<dl>
<dd><code>double tctdbadddouble(TCTDB *</code><i>tdb</i><code>, const void *</code><i>pkbuf</i><code>, int </code><i>pksiz</i><code>, double </code><i>num</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object connected as a writer.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the primary key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the primary key.</dl>
<dl>
<dd>`<i>num</i>&#8216; specifies the additional value.</dl>
<dl>
<dd>If successful, the return value is the summation value, else, it is Not-a-Number.</dl>
<dl>
<dd>The additional value is stored as a decimal string value of a column whose name is &quot;_num&quot;. If no record corresponds, a new record with the additional value is stored.</dl>
</dl>
<p> The function `tctdbsync&#8217; is used in order to synchronize updated contents of a table database object with the file and the device. </p>
<dl>
<dd><code>bool tctdbsync(TCTDB *</code><i>tdb</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object connected as a writer.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>This function is useful when another process connects to the same database file.</dl>
</dl>
<p> The function `tctdboptimize&#8217; is used in order to optimize the file of a table database object. </p>
<dl>
<dd><code>bool tctdboptimize(TCTDB *</code><i>tdb</i><code>, int64_t </code><i>bnum</i><code>, int8_t </code><i>apow</i><code>, int8_t </code><i>fpow</i><code>, uint8_t </code><i>opts</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object connected as a writer.</dl>
<dl>
<dd>`<i>bnum</i>&#8216; specifies the number of elements of the bucket array. If it is not more than 0, the default value is specified. The default value is two times of the number of records.</dl>
<dl>
<dd>`<i>apow</i>&#8216; specifies the size of record alignment by power of 2. If it is negative, the current setting is not changed.</dl>
<dl>
<dd>`<i>fpow</i>&#8216; specifies the maximum number of elements of the free block pool by power of 2. If it is negative, the current setting is not changed.</dl>
<dl>
<dd>`<i>opts</i>&#8216; specifies options by bitwise-or: `TDBTLARGE&#8217; specifies that the size of the database can be larger than 2GB by using 64-bit bucket array, `TDBTDEFLATE&#8217; specifies that each record is compressed with Deflate encoding, `TDBTBZIP&#8217; specifies that each record is compressed with BZIP2 encoding, `TDBTTCBS&#8217; specifies that each record is compressed with TCBS encoding. If it is `UINT8_MAX&#8217;, the current setting is not changed.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>This function is useful to reduce the size of the database file with data fragmentation by successive updating.</dl>
</dl>
<p> The function `tctdbvanish&#8217; is used in order to remove all records of a table database object. </p>
<dl>
<dd><code>bool tctdbvanish(TCTDB *</code><i>tdb</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object connected as a writer.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
</dl>
<p> The function `tctdbcopy&#8217; is used in order to copy the database file of a table database object. </p>
<dl>
<dd><code>bool tctdbcopy(TCTDB *</code><i>tdb</i><code>, const char *</code><i>path</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object.</dl>
<dl>
<dd>`<i>path</i>&#8216; specifies the path of the destination file. If it begins with `@&#8217;, the trailing substring is executed as a command line.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false. False is returned if the executed command returns non-zero code.</dl>
<dl>
<dd>The database file is assured to be kept synchronized and not modified while the copying or executing operation is in progress. So, this function is useful to create a backup file of the database file.</dl>
</dl>
<p> The function `tctdbtranbegin&#8217; is used in order to begin the transaction of a table database object. </p>
<dl>
<dd><code>bool tctdbtranbegin(TCTDB *</code><i>tdb</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object connected as a writer.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>The database is locked by the thread while the transaction so that only one transaction can be activated with a database object at the same time. Thus, the serializable isolation level is assumed if every database operation is performed in the transaction. Because all pages are cached on memory while the transaction, the amount of referred records is limited by the memory capacity. If the database is closed during transaction, the transaction is aborted implicitly.</dl>
</dl>
<p> The function `tctdbtrancommit&#8217; is used in order to commit the transaction of a table database object. </p>
<dl>
<dd><code>bool tctdbtrancommit(TCTDB *</code><i>tdb</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object connected as a writer.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Update in the transaction is fixed when it is committed successfully.</dl>
</dl>
<p> The function `tctdbtranabort&#8217; is used in order to abort the transaction of a table database object. </p>
<dl>
<dd><code>bool tctdbtranabort(TCTDB *</code><i>tdb</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object connected as a writer.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Update in the transaction is discarded when it is aborted. The state of the database is rollbacked to before transaction.</dl>
</dl>
<p> The function `tctdbpath&#8217; is used in order to get the file path of a table database object. </p>
<dl>
<dd><code>const char *tctdbpath(TCTDB *</code><i>tdb</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object.</dl>
<dl>
<dd>The return value is the path of the database file or `NULL&#8217; if the object does not connect to any database file.</dl>
</dl>
<p> The function `tctdbrnum&#8217; is used in order to get the number of records ccccof a table database object. </p>
<dl>
<dd><code>uint64_t tctdbrnum(TCTDB *</code><i>tdb</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object.</dl>
<dl>
<dd>The return value is the number of records or 0 if the object does not connect to any database file.</dl>
</dl>
<p> The function `tctdbfsiz&#8217; is used in order to get the size of the database file of a table database object. </p>
<dl>
<dd><code>uint64_t tctdbfsiz(TCTDB *</code><i>tdb</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object.</dl>
<dl>
<dd>The return value is the size of the database file or 0 if the object does not connect to any database file.</dl>
</dl>
<p> The function `tctdbsetindex&#8217; is used in order to set a column index to a table database object. </p>
<dl>
<dd><code>bool tctdbsetindex(TCTDB *</code><i>tdb</i><code>, const char *</code><i>name</i><code>, int </code><i>type</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object connected as a writer.</dl>
<dl>
<dd>`<i>name</i>&#8216; specifies the name of a column. If the name of an existing index is specified, the index is rebuilt. An empty string means the primary key.</dl>
<dl>
<dd>`<i>type</i>&#8216; specifies the index type: `TDBITLEXICAL&#8217; for lexical string, `TDBITDECIMAL&#8217; for decimal string, `TDBITTOKEN&#8217; for token inverted index, `TDBITQGRAM&#8217; for q-gram inverted index. If it is `TDBITOPT&#8217;, the index is optimized. If it is `TDBITVOID&#8217;, the index is removed. If `TDBITKEEP&#8217; is added by bitwise-or and the index exists, this function merely returns failure.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Note that the setting indices should be set after the database is opened.</dl>
</dl>
<p> The function `tctdbgenuid&#8217; is used in order to generate a unique ID number of a table database object. </p>
<dl>
<dd><code>int64_t tctdbgenuid(TCTDB *</code><i>tdb</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object connected as a writer.</dl>
<dl>
<dd>The return value is the new unique ID number or -1 on failure.</dl>
</dl>
<p> The function `tctdbqrynew&#8217; is used in order to create a query object. </p>
<dl>
<dd><code>TDBQRY *tctdbqrynew(TCTDB *</code><i>tdb</i><code>);</code></p>
<dl>
<dd>`<i>tdb</i>&#8216; specifies the table database object.</dl>
<dl>
<dd>The return value is the new query object.</dl>
</dl>
<p> The function `tctdbqrydel&#8217; is used in order to delete a query object. </p>
<dl>
<dd><code>void tctdbqrydel(TDBQRY *</code><i>qry</i><code>);</code></p>
<dl>
<dd>`<i>qry</i>&#8216; specifies the query object.</dl>
</dl>
<p> The function `tctdbqryaddcond&#8217; is used in order to add a narrowing condition to a query object. </p>
<dl>
<dd><code>void tctdbqryaddcond(TDBQRY *</code><i>qry</i><code>, const char *</code><i>name</i><code>, int </code><i>op</i><code>, const char *</code><i>expr</i><code>);</code></p>
<dl>
<dd>`<i>qry</i>&#8216; specifies the query object.</dl>
<dl>
<dd>`<i>name</i>&#8216; specifies the name of a column. An empty string means the primary key.</dl>
<dl>
<dd>`<i>op</i>&#8216; specifies an operation type: `TDBQCSTREQ&#8217; for string which is equal to the expression, `TDBQCSTRINC&#8217; for string which is included in the expression, `TDBQCSTRBW&#8217; for string which begins with the expression, `TDBQCSTREW&#8217; for string which ends with the expression, `TDBQCSTRAND&#8217; for string which includes all tokens in the expression, `TDBQCSTROR&#8217; for string which includes at least one token in the expression, `TDBQCSTROREQ&#8217; for string which is equal to at least one token in the expression, `TDBQCSTRRX&#8217; for string which matches regular expressions of the expression, `TDBQCNUMEQ&#8217; for number which is equal to the expression, `TDBQCNUMGT&#8217; for number which is greater than the expression, `TDBQCNUMGE&#8217; for number which is greater than or equal to the expression, `TDBQCNUMLT&#8217; for number which is less than the expression, `TDBQCNUMLE&#8217; for number which is less than or equal to the expression, `TDBQCNUMBT&#8217; for number which is between two tokens of the expression, `TDBQCNUMOREQ&#8217; for number which is equal to at least one token in the expression, `TDBQCFTSPH&#8217; for full-text search with the phrase of the expression, `TDBQCFTSAND&#8217; for full-text search with all tokens in the expression, `TDBQCFTSOR&#8217; for full-text search with at least one token in the expression, `TDBQCFTSEX&#8217; for full-text search with the compound expression. All operations can be flagged by bitwise-or: `TDBQCNEGATE&#8217; for negation, `TDBQCNOIDX&#8217; for using no index.</dl>
<dl>
<dd>`<i>expr</i>&#8216; specifies an operand exression.</dl>
</dl>
<p> The function `tctdbqrysetorder&#8217; is used in order to set the order of a query object. </p>
<dl>
<dd><code>void tctdbqrysetorder(TDBQRY *</code><i>qry</i><code>, const char *</code><i>name</i><code>, int </code><i>type</i><code>);</code></p>
<dl>
<dd>`<i>qry</i>&#8216; specifies the query object.</dl>
<dl>
<dd>`<i>name</i>&#8216; specifies the name of a column. An empty string means the primary key.</dl>
<dl>
<dd>`<i>type</i>&#8216; specifies the order type: `TDBQOSTRASC&#8217; for string ascending, `TDBQOSTRDESC&#8217; for string descending, `TDBQONUMASC&#8217; for number ascending, `TDBQONUMDESC&#8217; for number descending.</dl>
</dl>
<p> The function `tctdbqrysetlimit&#8217; is used in order to set the limit number of records of the result of a query object. </p>
<dl>
<dd><code>void tctdbqrysetlimit(TDBQRY *</code><i>qry</i><code>, int </code><i>max</i><code>, int </code><i>skip</i><code>);</code></p>
<dl>
<dd>`<i>qry</i>&#8216; specifies the query object.</dl>
<dl>
<dd>`<i>max</i>&#8216; specifies the maximum number of records of the result. If it is negative, no limit is specified.</dl>
<dl>
<dd>`<i>skip</i>&#8216; specifies the number of skipped records of the result. If it is not more than 0, no record is skipped.</dl>
</dl>
<p> The function `tctdbqrysearch&#8217; is used in order to execute the search of a query object. </p>
<dl>
<dd><code>TCLIST *tctdbqrysearch(TDBQRY *</code><i>qry</i><code>);</code></p>
<dl>
<dd>`<i>qry</i>&#8216; specifies the query object.</dl>
<dl>
<dd>The return value is a list object of the primary keys of the corresponding records. This function does never fail. It returns an empty list even if no record corresponds.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use.</dl>
</dl>
<p> The function `tctdbqrysearchout&#8217; is used in order to remove each record corresponding to a query object. </p>
<dl>
<dd><code>bool tctdbqrysearchout(TDBQRY *</code><i>qry</i><code>);</code></p>
<dl>
<dd>`<i>qry</i>&#8216; specifies the query object of the database connected as a writer.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
</dl>
<p> The function `tctdbqryproc&#8217; is used in order to process each record corresponding to a query object. </p>
<dl>
<dd><code>bool tctdbqryproc(TDBQRY *</code><i>qry</i><code>, TDBQRYPROC </code><i>proc</i><code>, void *</code><i>op</i><code>);</code></p>
<dl>
<dd>`<i>qry</i>&#8216; specifies the query object of the database connected as a writer.</dl>
<dl>
<dd>`<i>proc</i>&#8216; specifies the pointer to the iterator function called for each record. It receives four parameters. The first parameter is the pointer to the region of the primary key. The second parameter is the size of the region of the primary key. The third parameter is a map object containing columns. The fourth parameter is the pointer to the optional opaque object. It returns flags of the post treatment by bitwise-or: `TDBQPPUT&#8217; to modify the record, `TDBQPOUT&#8217; to remove the record, `TDBQPSTOP&#8217; to stop the iteration.</dl>
<dl>
<dd>`<i>op</i>&#8216; specifies an arbitrary pointer to be given as a parameter of the iterator function. If it is not needed, `NULL&#8217; can be specified.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
</dl>
<p> The function `tctdbqryhint&#8217; is used in order to get the hint string of a query object. </p>
<dl>
<dd><code>const char *tctdbqryhint(TDBQRY *</code><i>qry</i><code>);</code></p>
<dl>
<dd>`<i>qry</i>&#8216; specifies the query object.</dl>
<dl>
<dd>The return value is the hint string.</dl>
</dl>
<p> The function `tctdbmetasearch&#8217; is used in order to retrieve records with multiple query objects and get the set of the result. </p>
<dl>
<dd><code>TCLIST *tctdbmetasearch(TDBQRY **</code><i>qrys</i><code>, int </code><i>num</i><code>, int </code><i>type</i><code>);</code></p>
<dl>
<dd>`<i>qrys</i>&#8216; specifies an array of the query objects.</dl>
<dl>
<dd>`<i>num</i>&#8216; specifies the number of elements of the array.</dl>
<dl>
<dd>`<i>type</i>&#8216; specifies a set operation type: `TDBMSUNION&#8217; for the union set, `TDBMSISECT&#8217; for the intersection set, `TDBMSDIFF&#8217; for the difference set.</dl>
<dl>
<dd>The return value is a list object of the primary keys of the corresponding records. This function does never fail. It returns an empty list even if no record corresponds.</dl>
<dl>
<dd>If the first query object has the order setting, the result array is sorted by the order. Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use.</dl>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-tcttest/">tcttest</a></code>(1), <code><a href="/docs/linux/man/1-tctmttest/">tctmttest</a></code>(1), <code><a href="/docs/linux/man/1-tctmgr/">tctmgr</a></code>(1), <code><a href="/docs/linux/man/3-tokyocabinet/">tokyocabinet</a></code>(3) </p>
