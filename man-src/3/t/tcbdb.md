---
title: "tcbdb(3)"
name: "tcbdb"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcbdb/"
description: "tcbdb – the B+ tree database API"
---

<p>tcbdb &#8211; the B+ tree database API</p>
<h2>Description</h2>
<p>B+ tree database is a file containing a B+ tree and is handled with the B+ tree database API. To use the B+ tree database API, include `<code>tcutil.h</code>&#8216;, `<code>tcbdb.h</code>&#8216;, and related standard header files. Usually, write the following description near the front of a source file. </p>
<pre><code>#include &lt;tcutil.h&gt;

#include &lt;tcbdb.h&gt;

#include &lt;stdlib.h&gt;

#include &lt;time.h&gt;

#include &lt;stdbool.h&gt;

#include &lt;stdint.h&gt;</code></pre>
<p> Objects whose type is pointer to `<code>TCBDB</code>&#8216; are used to handle B+ tree databases. A B+ tree database object is created with the function `<code>tcbdbnew</code>&#8216; and is deleted with the function `<code>tcbdbdel</code>&#8216;. To avoid memory leak, it is important to delete every object when it is no longer in use. Before operations to store or retrieve records, it is necessary to open a database file and connect the B+ tree database object to it. The function `<code>tcbdbopen</code>&#8216; is used to open a database file and the function `<code>tcbdbclose</code>&#8216; is used to close the database file. To avoid data missing or corruption, it is important to close every database file when it is no longer in use. It is forbidden for multible database objects in a process to open the same database at the same time. </p>
<h2>Api</h2>
<p>The function `tcbdberrmsg&#8217; is used in order to get the message string corresponding to an error code. </p>
<dl>
<dd><code>const char *tcbdberrmsg(int </code><i>ecode</i><code>);</code></p>
<dl>
<dd>`<i>ecode</i>&#8216; specifies the error code.</dl>
<dl>
<dd>The return value is the message string of the error code.</dl>
</dl>
<p> The function `tcbdbnew&#8217; is used in order to create a B+ tree database object. </p>
<dl>
<dd><code>TCBDB *tcbdbnew(void);</code></p>
<dl>
<dd>The return value is the new B+ tree database object.</dl>
</dl>
<p> The function `tcbdbdel&#8217; is used in order to delete a B+ tree database object. </p>
<dl>
<dd><code>void tcbdbdel(TCBDB *</code><i>bdb</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object.</dl>
<dl>
<dd>If the database is not closed, it is closed implicitly. Note that the deleted object and its derivatives can not be used anymore.</dl>
</dl>
<p> The function `tcbdbecode&#8217; is used in order to get the last happened error code of a B+ tree database object. </p>
<dl>
<dd><code>int tcbdbecode(TCBDB *</code><i>bdb</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object.</dl>
<dl>
<dd>The return value is the last happened error code.</dl>
<dl>
<dd>The following error codes are defined: `TCESUCCESS&#8217; for success, `TCETHREAD&#8217; for threading error, `TCEINVALID&#8217; for invalid operation, `TCENOFILE&#8217; for file not found, `TCENOPERM&#8217; for no permission, `TCEMETA&#8217; for invalid meta data, `TCERHEAD&#8217; for invalid record header, `TCEOPEN&#8217; for open error, `TCECLOSE&#8217; for close error, `TCETRUNC&#8217; for trunc error, `TCESYNC&#8217; for sync error, `TCESTAT&#8217; for stat error, `TCESEEK&#8217; for seek error, `TCEREAD&#8217; for read error, `TCEWRITE&#8217; for write error, `TCEMMAP&#8217; for mmap error, `TCELOCK&#8217; for lock error, `TCEUNLINK&#8217; for unlink error, `TCERENAME&#8217; for rename error, `TCEMKDIR&#8217; for mkdir error, `TCERMDIR&#8217; for rmdir error, `TCEKEEP&#8217; for existing record, `TCENOREC&#8217; for no record found, and `TCEMISC&#8217; for miscellaneous error.</dl>
</dl>
<p> The function `tcbdbsetmutex&#8217; is used in order to set mutual exclusion control of a B+ tree database object for threading. </p>
<dl>
<dd><code>bool tcbdbsetmutex(TCBDB *</code><i>bdb</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object which is not opened.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Note that the mutual exclusion control of the database should be set before the database is opened.</dl>
</dl>
<p> The function `tcbdbsetcmpfunc&#8217; is used in order to set the custom comparison function of a B+ tree database object. </p>
<dl>
<dd><code>bool tcbdbsetcmpfunc(TCBDB *</code><i>bdb</i><code>, TCCMP </code><i>cmp</i><code>, void *</code><i>cmpop</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object which is not opened.</dl>
<dl>
<dd>`<i>cmp</i>&#8216; specifies the pointer to the custom comparison function. It receives five parameters. The first parameter is the pointer to the region of one key. The second parameter is the size of the region of one key. The third parameter is the pointer to the region of the other key. The fourth parameter is the size of the region of the other key. The fifth parameter is the pointer to the optional opaque object. It returns positive if the former is big, negative if the latter is big, 0 if both are equivalent.</dl>
<dl>
<dd>`<i>cmpop</i>&#8216; specifies an arbitrary pointer to be given as a parameter of the comparison function. If it is not needed, `NULL&#8217; can be specified.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>The default comparison function compares keys of two records by lexical order. The functions `tccmplexical&#8217; (dafault), `tccmpdecimal&#8217;, `tccmpint32&#8242;, and `tccmpint64&#8242; are built-in. Note that the comparison function should be set before the database is opened. Moreover, user-defined comparison functions should be set every time the database is being opened.</dl>
</dl>
<p> The function `tcbdbtune&#8217; is used in order to set the tuning parameters of a B+ tree database object. </p>
<dl>
<dd><code>bool tcbdbtune(TCBDB *</code><i>bdb</i><code>, int32_t </code><i>lmemb</i><code>, int32_t </code><i>nmemb</i><code>, int64_t </code><i>bnum</i><code>, int8_t </code><i>apow</i><code>, int8_t </code><i>fpow</i><code>, uint8_t </code><i>opts</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object which is not opened.</dl>
<dl>
<dd>`<i>lmemb</i>&#8216; specifies the number of members in each leaf page. If it is not more than 0, the default value is specified. The default value is 128.</dl>
<dl>
<dd>`<i>nmemb</i>&#8216; specifies the number of members in each non-leaf page. If it is not more than 0, the default value is specified. The default value is 256.</dl>
<dl>
<dd>`<i>bnum</i>&#8216; specifies the number of elements of the bucket array. If it is not more than 0, the default value is specified. The default value is 16381. Suggested size of the bucket array is about from 1 to 4 times of the number of all pages to be stored.</dl>
<dl>
<dd>`<i>apow</i>&#8216; specifies the size of record alignment by power of 2. If it is negative, the default value is specified. The default value is 8 standing for 2^8=256.</dl>
<dl>
<dd>`<i>fpow</i>&#8216; specifies the maximum number of elements of the free block pool by power of 2. If it is negative, the default value is specified. The default value is 10 standing for 2^10=1024.</dl>
<dl>
<dd>`<i>opts</i>&#8216; specifies options by bitwise-or: `BDBTLARGE&#8217; specifies that the size of the database can be larger than 2GB by using 64-bit bucket array, `BDBTDEFLATE&#8217; specifies that each page is compressed with Deflate encoding, `BDBTBZIP&#8217; specifies that each page is compressed with BZIP2 encoding, `BDBTTCBS&#8217; specifies that each page is compressed with TCBS encoding.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Note that the tuning parameters should be set before the database is opened.</dl>
</dl>
<p> The function `tcbdbsetcache&#8217; is used in order to set the caching parameters of a B+ tree database object. </p>
<dl>
<dd><code>bool tcbdbsetcache(TCBDB *</code><i>bdb</i><code>, int32_t </code><i>lcnum</i><code>, int32_t </code><i>ncnum</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object which is not opened.</dl>
<dl>
<dd>`<i>lcnum</i>&#8216; specifies the maximum number of leaf nodes to be cached. If it is not more than 0, the default value is specified. The default value is 1024.</dl>
<dl>
<dd>`<i>ncnum</i>&#8216; specifies the maximum number of non-leaf nodes to be cached. If it is not more than 0, the default value is specified. The default value is 512.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Note that the caching parameters should be set before the database is opened.</dl>
</dl>
<p> The function `tcbdbsetxmsiz&#8217; is used in order to set the size of the extra mapped memory of a B+ tree database object. </p>
<dl>
<dd><code>bool tcbdbsetxmsiz(TCBDB *</code><i>bdb</i><code>, int64_t </code><i>xmsiz</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object which is not opened.</dl>
<dl>
<dd>`<i>xmsiz</i>&#8216; specifies the size of the extra mapped memory. If it is not more than 0, the extra mapped memory is disabled. It is disabled by default.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Note that the mapping parameters should be set before the database is opened.</dl>
</dl>
<p> The function `tcbdbsetdfunit&#8217; is used in order to set the unit step number of auto defragmentation of a B+ tree database object. </p>
<dl>
<dd><code>bool tcbdbsetdfunit(TCBDB *</code><i>bdb</i><code>, int32_t </code><i>dfunit</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object which is not opened.</dl>
<dl>
<dd>`<i>dfunit</i>&#8216; specifie the unit step number. If it is not more than 0, the auto defragmentation is disabled. It is disabled by default.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Note that the defragmentation parameter should be set before the database is opened.</dl>
</dl>
<p> The function `tcbdbopen&#8217; is used in order to open a database file and connect a B+ tree database object. </p>
<dl>
<dd><code>bool tcbdbopen(TCBDB *</code><i>bdb</i><code>, const char *</code><i>path</i><code>, int </code><i>omode</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object which is not opened.</dl>
<dl>
<dd>`<i>path</i>&#8216; specifies the path of the database file.</dl>
<dl>
<dd>`<i>omode</i>&#8216; specifies the connection mode: `BDBOWRITER&#8217; as a writer, `BDBOREADER&#8217; as a reader. If the mode is `BDBOWRITER&#8217;, the following may be added by bitwise-or: `BDBOCREAT&#8217;, which means it creates a new database if not exist, `BDBOTRUNC&#8217;, which means it creates a new database regardless if one exists, `BDBOTSYNC&#8217;, which means every transaction synchronizes updated contents with the device. Both of `BDBOREADER&#8217; and `BDBOWRITER&#8217; can be added to by bitwise-or: `BDBONOLCK&#8217;, which means it opens the database file without file locking, or `BDBOLCKNB&#8217;, which means locking is performed without blocking.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
</dl>
<p> The function `tcbdbclose&#8217; is used in order to close a B+ tree database object. </p>
<dl>
<dd><code>bool tcbdbclose(TCBDB *</code><i>bdb</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Update of a database is assured to be written when the database is closed. If a writer opens a database but does not close it appropriately, the database will be broken.</dl>
</dl>
<p> The function `tcbdbput&#8217; is used in order to store a record into a B+ tree database object. </p>
<dl>
<dd><code>bool tcbdbput(TCBDB *</code><i>bdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object connected as a writer.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>vbuf</i>&#8216; specifies the pointer to the region of the value.</dl>
<dl>
<dd>`<i>vsiz</i>&#8216; specifies the size of the region of the value.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the database, it is overwritten.</dl>
</dl>
<p> The function `tcbdbput2&#8242; is used in order to store a string record into a B+ tree database object. </p>
<dl>
<dd><code>bool tcbdbput2(TCBDB *</code><i>bdb</i><code>, const char *</code><i>kstr</i><code>, const char *</code><i>vstr</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object connected as a writer.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>`<i>vstr</i>&#8216; specifies the string of the value.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the database, it is overwritten.</dl>
</dl>
<p> The function `tcbdbputkeep&#8217; is used in order to store a new record into a B+ tree database object. </p>
<dl>
<dd><code>bool tcbdbputkeep(TCBDB *</code><i>bdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object connected as a writer.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>vbuf</i>&#8216; specifies the pointer to the region of the value.</dl>
<dl>
<dd>`<i>vsiz</i>&#8216; specifies the size of the region of the value.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the database, this function has no effect.</dl>
</dl>
<p> The function `tcbdbputkeep2&#8242; is used in order to store a new string record into a B+ tree database object. </p>
<dl>
<dd><code>bool tcbdbputkeep2(TCBDB *</code><i>bdb</i><code>, const char *</code><i>kstr</i><code>, const char *</code><i>vstr</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object connected as a writer.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>`<i>vstr</i>&#8216; specifies the string of the value.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the database, this function has no effect.</dl>
</dl>
<p> The function `tcbdbputcat&#8217; is used in order to concatenate a value at the end of the existing record in a B+ tree database object. </p>
<dl>
<dd><code>bool tcbdbputcat(TCBDB *</code><i>bdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object connected as a writer.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>vbuf</i>&#8216; specifies the pointer to the region of the value.</dl>
<dl>
<dd>`<i>vsiz</i>&#8216; specifies the size of the region of the value.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If there is no corresponding record, a new record is created.</dl>
</dl>
<p> The function `tcbdbputcat2&#8242; is used in order to concatenate a string value at the end of the existing record in a B+ tree database object. </p>
<dl>
<dd><code>bool tcbdbputcat2(TCBDB *</code><i>bdb</i><code>, const char *</code><i>kstr</i><code>, const char *</code><i>vstr</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object connected as a writer.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>`<i>vstr</i>&#8216; specifies the string of the value.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If there is no corresponding record, a new record is created.</dl>
</dl>
<p> The function `tcbdbputdup&#8217; is used in order to store a record into a B+ tree database object with allowing duplication of keys. </p>
<dl>
<dd><code>bool tcbdbputdup(TCBDB *</code><i>bdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object connected as a writer.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>vbuf</i>&#8216; specifies the pointer to the region of the value.</dl>
<dl>
<dd>`<i>vsiz</i>&#8216; specifies the size of the region of the value.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the database, the new record is placed after the existing one.</dl>
</dl>
<p> The function `tcbdbputdup2&#8242; is used in order to store a string record into a B+ tree database object with allowing duplication of keys. </p>
<dl>
<dd><code>bool tcbdbputdup2(TCBDB *</code><i>bdb</i><code>, const char *</code><i>kstr</i><code>, const char *</code><i>vstr</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object connected as a writer.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>`<i>vstr</i>&#8216; specifies the string of the value.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the database, the new record is placed after the existing one.</dl>
</dl>
<p> The function `tcbdbputdup3&#8242; is used in order to store records into a B+ tree database object with allowing duplication of keys. </p>
<dl>
<dd><code>bool tcbdbputdup3(TCBDB *</code><i>bdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, const TCLIST *</code><i>vals</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object connected as a writer.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the common key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the common key.</dl>
<dl>
<dd>`<i>vals</i>&#8216; specifies a list object containing values.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the database, the new records are placed after the existing one.</dl>
</dl>
<p> The function `tcbdbout&#8217; is used in order to remove a record of a B+ tree database object. </p>
<dl>
<dd><code>bool tcbdbout(TCBDB *</code><i>bdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object connected as a writer.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If the key of duplicated records is specified, the first one is selected.</dl>
</dl>
<p> The function `tcbdbout2&#8242; is used in order to remove a string record of a B+ tree database object. </p>
<dl>
<dd><code>bool tcbdbout2(TCBDB *</code><i>bdb</i><code>, const char *</code><i>kstr</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object connected as a writer.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If the key of duplicated records is specified, the first one is selected.</dl>
</dl>
<p> The function `tcbdbout3&#8242; is used in order to remove records of a B+ tree database object. </p>
<dl>
<dd><code>bool tcbdbout3(TCBDB *</code><i>bdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object connected as a writer.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If the key of duplicated records is specified, all of them are removed.</dl>
</dl>
<p> The function `tcbdbget&#8217; is used in order to retrieve a record in a B+ tree database object. </p>
<dl>
<dd><code>void *tcbdbget(TCBDB *</code><i>bdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the region of the value of the corresponding record. `NULL&#8217; is returned if no record corresponds.</dl>
<dl>
<dd>If the key of duplicated records is specified, the first one is selected. Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcbdbget2&#8242; is used in order to retrieve a string record in a B+ tree database object. </p>
<dl>
<dd><code>char *tcbdbget2(TCBDB *</code><i>bdb</i><code>, const char *</code><i>kstr</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>If successful, the return value is the string of the value of the corresponding record. `NULL&#8217; is returned if no record corresponds.</dl>
<dl>
<dd>If the key of duplicated records is specified, the first one is selected. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcbdbget3&#8242; is used in order to retrieve a record in a B+ tree database object as a volatile buffer. </p>
<dl>
<dd><code>const void *tcbdbget3(TCBDB *</code><i>bdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the region of the value of the corresponding record. `NULL&#8217; is returned if no record corresponds.</dl>
<dl>
<dd>If the key of duplicated records is specified, the first one is selected. Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is volatile and it may be spoiled by another operation of the database, the data should be copied into another involatile buffer immediately.</dl>
</dl>
<p> The function `tcbdbget4&#8242; is used in order to retrieve records in a B+ tree database object. </p>
<dl>
<dd><code>TCLIST *tcbdbget4(TCBDB *</code><i>bdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>If successful, the return value is a list object of the values of the corresponding records. `NULL&#8217; is returned if no record corresponds.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use.</dl>
</dl>
<p> The function `tcbdbvnum&#8217; is used in order to get the number of records corresponding a key in a B+ tree database object. </p>
<dl>
<dd><code>int tcbdbvnum(TCBDB *</code><i>bdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>If successful, the return value is the number of the corresponding records, else, it is 0.</dl>
</dl>
<p> The function `tcbdbvnum2&#8242; is used in order to get the number of records corresponding a string key in a B+ tree database object. </p>
<dl>
<dd><code>int tcbdbvnum2(TCBDB *</code><i>bdb</i><code>, const char *</code><i>kstr</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>If successful, the return value is the number of the corresponding records, else, it is 0.</dl>
</dl>
<p> The function `tcbdbvsiz&#8217; is used in order to get the size of the value of a record in a B+ tree database object. </p>
<dl>
<dd><code>int tcbdbvsiz(TCBDB *</code><i>bdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>If successful, the return value is the size of the value of the corresponding record, else, it is -1.</dl>
<dl>
<dd>If the key of duplicated records is specified, the first one is selected.</dl>
</dl>
<p> The function `tcbdbvsiz2&#8242; is used in order to get the size of the value of a string record in a B+ tree database object. </p>
<dl>
<dd><code>int tcbdbvsiz2(TCBDB *</code><i>bdb</i><code>, const char *</code><i>kstr</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>If successful, the return value is the size of the value of the corresponding record, else, it is -1.</dl>
<dl>
<dd>If the key of duplicated records is specified, the first one is selected.</dl>
</dl>
<p> The function `tcbdbrange&#8217; is used in order to get keys of ranged records in a B+ tree database object. </p>
<dl>
<dd><code>TCLIST *tcbdbrange(TCBDB *</code><i>bdb</i><code>, const void *</code><i>bkbuf</i><code>, int </code><i>bksiz</i><code>, bool </code><i>binc</i><code>, const void *</code><i>ekbuf</i><code>, int </code><i>eksiz</i><code>, bool </code><i>einc</i><code>, int </code><i>max</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object.</dl>
<dl>
<dd>`<i>bkbuf</i>&#8216; specifies the pointer to the region of the key of the beginning border. If it is `NULL&#8217;, the first record is specified.</dl>
<dl>
<dd>`<i>bksiz</i>&#8216; specifies the size of the region of the beginning key.</dl>
<dl>
<dd>`<i>binc</i>&#8216; specifies whether the beginning border is inclusive or not.</dl>
<dl>
<dd>`<i>ekbuf</i>&#8216; specifies the pointer to the region of the key of the ending border. If it is `NULL&#8217;, the last record is specified.</dl>
<dl>
<dd>`<i>eksiz</i>&#8216; specifies the size of the region of the ending key.</dl>
<dl>
<dd>`<i>einc</i>&#8216; specifies whether the ending border is inclusive or not.</dl>
<dl>
<dd>`<i>max</i>&#8216; specifies the maximum number of keys to be fetched. If it is negative, no limit is specified.</dl>
<dl>
<dd>The return value is a list object of the keys of the corresponding records. This function does never fail. It returns an empty list even if no record corresponds.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use.</dl>
</dl>
<p> The function `tcbdbrange2&#8242; is used in order to get string keys of ranged records in a B+ tree database object. </p>
<dl>
<dd><code>TCLIST *tcbdbrange2(TCBDB *</code><i>bdb</i><code>, const char *</code><i>bkstr</i><code>, bool </code><i>binc</i><code>, const char *</code><i>ekstr</i><code>, bool </code><i>einc</i><code>, int </code><i>max</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object.</dl>
<dl>
<dd>`<i>bkstr</i>&#8216; specifies the string of the key of the beginning border. If it is `NULL&#8217;, the first record is specified.</dl>
<dl>
<dd>`<i>binc</i>&#8216; specifies whether the beginning border is inclusive or not.</dl>
<dl>
<dd>`<i>ekstr</i>&#8216; specifies the string of the key of the ending border. If it is `NULL&#8217;, the last record is specified.</dl>
<dl>
<dd>`<i>einc</i>&#8216; specifies whether the ending border is inclusive or not.</dl>
<dl>
<dd>`<i>max</i>&#8216; specifies the maximum number of keys to be fetched. If it is negative, no limit is specified.</dl>
<dl>
<dd>The return value is a list object of the keys of the corresponding records. This function does never fail. It returns an empty list even if no record corresponds.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use.</dl>
</dl>
<p> The function `tcbdbfwmkeys&#8217; is used in order to get forward matching keys in a B+ tree database object. </p>
<dl>
<dd><code>TCLIST *tcbdbfwmkeys(TCBDB *</code><i>bdb</i><code>, const void *</code><i>pbuf</i><code>, int </code><i>psiz</i><code>, int </code><i>max</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object.</dl>
<dl>
<dd>`<i>pbuf</i>&#8216; specifies the pointer to the region of the prefix.</dl>
<dl>
<dd>`<i>psiz</i>&#8216; specifies the size of the region of the prefix.</dl>
<dl>
<dd>`<i>max</i>&#8216; specifies the maximum number of keys to be fetched. If it is negative, no limit is specified.</dl>
<dl>
<dd>The return value is a list object of the corresponding keys. This function does never fail. It returns an empty list even if no key corresponds.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use.</dl>
</dl>
<p> The function `tcbdbfwmkeys2&#8242; is used in order to get forward matching string keys in a B+ tree database object. </p>
<dl>
<dd><code>TCLIST *tcbdbfwmkeys2(TCBDB *</code><i>bdb</i><code>, const char *</code><i>pstr</i><code>, int </code><i>max</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object.</dl>
<dl>
<dd>`<i>pstr</i>&#8216; specifies the string of the prefix.</dl>
<dl>
<dd>`<i>max</i>&#8216; specifies the maximum number of keys to be fetched. If it is negative, no limit is specified.</dl>
<dl>
<dd>The return value is a list object of the corresponding keys. This function does never fail. It returns an empty list even if no key corresponds.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use.</dl>
</dl>
<p> The function `tcbdbaddint&#8217; is used in order to add an integer to a record in a B+ tree database object. </p>
<dl>
<dd><code>int tcbdbaddint(TCBDB *</code><i>bdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, int </code><i>num</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object connected as a writer.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>num</i>&#8216; specifies the additional value.</dl>
<dl>
<dd>If successful, the return value is the summation value, else, it is `INT_MIN&#8217;.</dl>
<dl>
<dd>If the corresponding record exists, the value is treated as an integer and is added to. If no record corresponds, a new record of the additional value is stored.</dl>
</dl>
<p> The function `tcbdbadddouble&#8217; is used in order to add a real number to a record in a B+ tree database object. </p>
<dl>
<dd><code>double tcbdbadddouble(TCBDB *</code><i>bdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, double </code><i>num</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object connected as a writer.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>num</i>&#8216; specifies the additional value.</dl>
<dl>
<dd>If successful, the return value is the summation value, else, it is Not-a-Number.</dl>
<dl>
<dd>If the corresponding record exists, the value is treated as a real number and is added to. If no record corresponds, a new record of the additional value is stored.</dl>
</dl>
<p> The function `tcbdbsync&#8217; is used in order to synchronize updated contents of a B+ tree database object with the file and the device. </p>
<dl>
<dd><code>bool tcbdbsync(TCBDB *</code><i>bdb</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object connected as a writer.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>This function is useful when another process connects to the same database file.</dl>
</dl>
<p> The function `tcbdboptimize&#8217; is used in order to optimize the file of a B+ tree database object. </p>
<dl>
<dd><code>bool tcbdboptimize(TCBDB *</code><i>bdb</i><code>, int32_t </code><i>lmemb</i><code>, int32_t </code><i>nmemb</i><code>, int64_t </code><i>bnum</i><code>, int8_t </code><i>apow</i><code>, int8_t </code><i>fpow</i><code>, uint8_t </code><i>opts</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object connected as a writer.</dl>
<dl>
<dd>`<i>lmemb</i>&#8216; specifies the number of members in each leaf page. If it is not more than 0, the current setting is not changed.</dl>
<dl>
<dd>`<i>nmemb</i>&#8216; specifies the number of members in each non-leaf page. If it is not more than 0, the current setting is not changed.</dl>
<dl>
<dd>`<i>bnum</i>&#8216; specifies the number of elements of the bucket array. If it is not more than 0, the default value is specified. The default value is two times of the number of pages.</dl>
<dl>
<dd>`<i>apow</i>&#8216; specifies the size of record alignment by power of 2. If it is negative, the current setting is not changed.</dl>
<dl>
<dd>`<i>fpow</i>&#8216; specifies the maximum number of elements of the free block pool by power of 2. If it is negative, the current setting is not changed.</dl>
<dl>
<dd>`<i>opts</i>&#8216; specifies options by bitwise-or: `BDBTLARGE&#8217; specifies that the size of the database can be larger than 2GB by using 64-bit bucket array, `BDBTDEFLATE&#8217; specifies that each record is compressed with Deflate encoding, `BDBTBZIP&#8217; specifies that each page is compressed with BZIP2 encoding, `BDBTTCBS&#8217; specifies that each page is compressed with TCBS encoding. If it is `UINT8_MAX&#8217;, the current setting is not changed.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>This function is useful to reduce the size of the database file with data fragmentation by successive updating.</dl>
</dl>
<p> The function `tcbdbvanish&#8217; is used in order to remove all records of a B+ tree database object. </p>
<dl>
<dd><code>bool tcbdbvanish(TCBDB *</code><i>bdb</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object connected as a writer.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
</dl>
<p> The function `tcbdbcopy&#8217; is used in order to copy the database file of a B+ tree database object. </p>
<dl>
<dd><code>bool tcbdbcopy(TCBDB *</code><i>bdb</i><code>, const char *</code><i>path</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object.</dl>
<dl>
<dd>`<i>path</i>&#8216; specifies the path of the destination file. If it begins with `@&#8217;, the trailing substring is executed as a command line.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false. False is returned if the executed command returns non-zero code.</dl>
<dl>
<dd>The database file is assured to be kept synchronized and not modified while the copying or executing operation is in progress. So, this function is useful to create a backup file of the database file.</dl>
</dl>
<p> The function `tcbdbtranbegin&#8217; is used in order to begin the transaction of a B+ tree database object. </p>
<dl>
<dd><code>bool tcbdbtranbegin(TCBDB *</code><i>bdb</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object connected as a writer.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>The database is locked by the thread while the transaction so that only one transaction can be activated with a database object at the same time. Thus, the serializable isolation level is assumed if every database operation is performed in the transaction. Because all pages are cached on memory while the transaction, the amount of referred records is limited by the memory capacity. If the database is closed during transaction, the transaction is aborted implicitly.</dl>
</dl>
<p> The function `tcbdbtrancommit&#8217; is used in order to commit the transaction of a B+ tree database object. </p>
<dl>
<dd><code>bool tcbdbtrancommit(TCBDB *</code><i>bdb</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object connected as a writer.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Update in the transaction is fixed when it is committed successfully.</dl>
</dl>
<p> The function `tcbdbtranabort&#8217; is used in order to abort the transaction of a B+ tree database object. </p>
<dl>
<dd><code>bool tcbdbtranabort(TCBDB *</code><i>bdb</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object connected as a writer.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Update in the transaction is discarded when it is aborted. The state of the database is rollbacked to before transaction.</dl>
</dl>
<p> The function `tcbdbpath&#8217; is used in order to get the file path of a B+ tree database object. </p>
<dl>
<dd><code>const char *tcbdbpath(TCBDB *</code><i>bdb</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object.</dl>
<dl>
<dd>The return value is the path of the database file or `NULL&#8217; if the object does not connect to any database file.</dl>
</dl>
<p> The function `tcbdbrnum&#8217; is used in order to get the number of records of a B+ tree database object. </p>
<dl>
<dd><code>uint64_t tcbdbrnum(TCBDB *</code><i>bdb</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object.</dl>
<dl>
<dd>The return value is the number of records or 0 if the object does not connect to any database file.</dl>
</dl>
<p> The function `tcbdbfsiz&#8217; is used in order to get the size of the database file of a B+ tree database object. </p>
<dl>
<dd><code>uint64_t tcbdbfsiz(TCBDB *</code><i>bdb</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object.</dl>
<dl>
<dd>The return value is the size of the database file or 0 if the object does not connect to any database file.</dl>
</dl>
<p> The function `tcbdbcurnew&#8217; is used in order to create a cursor object. </p>
<dl>
<dd><code>BDBCUR *tcbdbcurnew(TCBDB *</code><i>bdb</i><code>);</code></p>
<dl>
<dd>`<i>bdb</i>&#8216; specifies the B+ tree database object.</dl>
<dl>
<dd>The return value is the new cursor object.</dl>
<dl>
<dd>Note that the cursor is available only after initialization with the `tcbdbcurfirst&#8217; or the `tcbdbcurjump&#8217; functions and so on. Moreover, the position of the cursor will be indefinite when the database is updated after the initialization of the cursor.</dl>
</dl>
<p> The function `tcbdbcurdel&#8217; is used in order to delete a cursor object. </p>
<dl>
<dd><code>void tcbdbcurdel(BDBCUR *</code><i>cur</i><code>);</code></p>
<dl>
<dd>`<i>cur</i>&#8216; specifies the cursor object.</dl>
</dl>
<p> The function `tcbdbcurfirst&#8217; is used in order to move a cursor object to the first record. </p>
<dl>
<dd><code>bool tcbdbcurfirst(BDBCUR *</code><i>cur</i><code>);</code></p>
<dl>
<dd>`<i>cur</i>&#8216; specifies the cursor object.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false. False is returned if there is no record in the database.</dl>
</dl>
<p> The function `tcbdbcurlast&#8217; is used in order to move a cursor object to the last record. </p>
<dl>
<dd><code>bool tcbdbcurlast(BDBCUR *</code><i>cur</i><code>);</code></p>
<dl>
<dd>`<i>cur</i>&#8216; specifies the cursor object.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false. False is returned if there is no record in the database.</dl>
</dl>
<p> The function `tcbdbcurjump&#8217; is used in order to move a cursor object to the front of records corresponding a key. </p>
<dl>
<dd><code>bool tcbdbcurjump(BDBCUR *</code><i>cur</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>);</code></p>
<dl>
<dd>`<i>cur</i>&#8216; specifies the cursor object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false. False is returned if there is no record corresponding the condition.</dl>
<dl>
<dd>The cursor is set to the first record corresponding the key or the next substitute if completely matching record does not exist.</dl>
</dl>
<p> The function `tcbdbcurjump2&#8242; is used in order to move a cursor object to the front of records corresponding a key string. </p>
<dl>
<dd><code>bool tcbdbcurjump2(BDBCUR *</code><i>cur</i><code>, const char *</code><i>kstr</i><code>);</code></p>
<dl>
<dd>`<i>cur</i>&#8216; specifies the cursor object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false. False is returned if there is no record corresponding the condition.</dl>
<dl>
<dd>The cursor is set to the first record corresponding the key or the next substitute if completely matching record does not exist.</dl>
</dl>
<p> The function `tcbdbcurprev&#8217; is used in order to move a cursor object to the previous record. </p>
<dl>
<dd><code>bool tcbdbcurprev(BDBCUR *</code><i>cur</i><code>);</code></p>
<dl>
<dd>`<i>cur</i>&#8216; specifies the cursor object.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false. False is returned if there is no previous record.</dl>
</dl>
<p> The function `tcbdbcurnext&#8217; is used in order to move a cursor object to the next record. </p>
<dl>
<dd><code>bool tcbdbcurnext(BDBCUR *</code><i>cur</i><code>);</code></p>
<dl>
<dd>`<i>cur</i>&#8216; specifies the cursor object.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false. False is returned if there is no next record.</dl>
</dl>
<p> The function `tcbdbcurput&#8217; is used in order to insert a record around a cursor object. </p>
<dl>
<dd><code>bool tcbdbcurput(BDBCUR *</code><i>cur</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>, int </code><i>cpmode</i><code>);</code></p>
<dl>
<dd>`<i>cur</i>&#8216; specifies the cursor object of writer connection.</dl>
<dl>
<dd>`<i>vbuf</i>&#8216; specifies the pointer to the region of the value.</dl>
<dl>
<dd>`<i>vsiz</i>&#8216; specifies the size of the region of the value.</dl>
<dl>
<dd>`<i>cpmode</i>&#8216; specifies detail adjustment: `BDBCPCURRENT&#8217;, which means that the value of the current record is overwritten, `BDBCPBEFORE&#8217;, which means that the new record is inserted before the current record, `BDBCPAFTER&#8217;, which means that the new record is inserted after the current record.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false. False is returned when the cursor is at invalid position.</dl>
<dl>
<dd>After insertion, the cursor is moved to the inserted record.</dl>
</dl>
<p> The function `tcbdbcurput2&#8242; is used in order to insert a string record around a cursor object. </p>
<dl>
<dd><code>bool tcbdbcurput2(BDBCUR *</code><i>cur</i><code>, const char *</code><i>vstr</i><code>, int </code><i>cpmode</i><code>);</code></p>
<dl>
<dd>`<i>cur</i>&#8216; specifies the cursor object of writer connection.</dl>
<dl>
<dd>`<i>vstr</i>&#8216; specifies the string of the value.</dl>
<dl>
<dd>`<i>cpmode</i>&#8216; specifies detail adjustment: `BDBCPCURRENT&#8217;, which means that the value of the current record is overwritten, `BDBCPBEFORE&#8217;, which means that the new record is inserted before the current record, `BDBCPAFTER&#8217;, which means that the new record is inserted after the current record.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false. False is returned when the cursor is at invalid position.</dl>
<dl>
<dd>After insertion, the cursor is moved to the inserted record.</dl>
</dl>
<p> The function `tcbdbcurout&#8217; is used in order to remove the record where a cursor object is. </p>
<dl>
<dd><code>bool tcbdbcurout(BDBCUR *</code><i>cur</i><code>);</code></p>
<dl>
<dd>`<i>cur</i>&#8216; specifies the cursor object of writer connection.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false. False is returned when the cursor is at invalid position.</dl>
<dl>
<dd>After deletion, the cursor is moved to the next record if possible.</dl>
</dl>
<p> The function `tcbdbcurkey&#8217; is used in order to get the key of the record where the cursor object is. </p>
<dl>
<dd><code>char *tcbdbcurkey(BDBCUR *</code><i>cur</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>cur</i>&#8216; specifies the cursor object.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the region of the key, else, it is `NULL&#8217;. `NULL&#8217; is returned when the cursor is at invalid position.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcbdbcurkey2&#8242; is used in order to get the key string of the record where the cursor object is. </p>
<dl>
<dd><code>char *tcbdbcurkey2(BDBCUR *</code><i>cur</i><code>);</code></p>
<dl>
<dd>`<i>cur</i>&#8216; specifies the cursor object.</dl>
<dl>
<dd>If successful, the return value is the string of the key, else, it is `NULL&#8217;. `NULL&#8217; is returned when the cursor is at invalid position.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcbdbcurkey3&#8242; is used in order to get the key of the record where the cursor object is, as a volatile buffer. </p>
<dl>
<dd><code>const char *tcbdbcurkey3(BDBCUR *</code><i>cur</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>cur</i>&#8216; specifies the cursor object.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the region of the key, else, it is `NULL&#8217;. `NULL&#8217; is returned when the cursor is at invalid position.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is volatile and it may be spoiled by another operation of the database, the data should be copied into another involatile buffer immediately.</dl>
</dl>
<p> The function `tcbdbcurval&#8217; is used in order to get the value of the record where the cursor object is. </p>
<dl>
<dd><code>char *tcbdbcurval(BDBCUR *</code><i>cur</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>cur</i>&#8216; specifies the cursor object.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the region of the value, else, it is `NULL&#8217;. `NULL&#8217; is returned when the cursor is at invalid position.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcbdbcurval2&#8242; is used in order to get the value string of the record where the cursor object is. </p>
<dl>
<dd><code>char *tcbdbcurval2(BDBCUR *</code><i>cur</i><code>);</code></p>
<dl>
<dd>`<i>cur</i>&#8216; specifies the cursor object.</dl>
<dl>
<dd>If successful, the return value is the string of the value, else, it is `NULL&#8217;. `NULL&#8217; is returned when the cursor is at invalid position.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcbdbcurval3&#8242; is used in order to get the value of the record where the cursor object is, as a volatile buffer. </p>
<dl>
<dd><code>const char *tcbdbcurval3(BDBCUR *</code><i>cur</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>cur</i>&#8216; specifies the cursor object.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the region of the value, else, it is `NULL&#8217;. `NULL&#8217; is returned when the cursor is at invalid position.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is volatile and it may be spoiled by another operation of the database, the data should be copied into another involatile buffer immediately.</dl>
</dl>
<p> The function `tcbdbcurrec&#8217; is used in order to get the key and the value of the record where the cursor object is. </p>
<dl>
<dd><code>bool tcbdbcurrec(BDBCUR *</code><i>cur</i><code>, TCXSTR *</code><i>kxstr</i><code>, TCXSTR *</code><i>vxstr</i><code>);</code></p>
<dl>
<dd>`<i>cur</i>&#8216; specifies the cursor object.</dl>
<dl>
<dd>`<i>kxstr</i>&#8216; specifies the object into which the key is wrote down.</dl>
<dl>
<dd>`<i>vxstr</i>&#8216; specifies the object into which the value is wrote down.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false. False is returned when the cursor is at invalid position.</dl>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-tcbtest/">tcbtest</a></code>(1), <code><a href="/docs/linux/man/1-tcbmttest/">tcbmttest</a></code>(1), <code><a href="/docs/linux/man/1-tcbmgr/">tcbmgr</a></code>(1), <code><a href="/docs/linux/man/3-tokyocabinet/">tokyocabinet</a></code>(3) </p>
