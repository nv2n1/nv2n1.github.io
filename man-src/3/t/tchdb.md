---
title: "tchdb(3)"
name: "tchdb"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tchdb/"
description: "tchdb – the hash database API"
---

<p>tchdb &#8211; the hash database API</p>
<h2>Description</h2>
<p>Hash database is a file containing a hash table and is handled with the hash database API. To use the hash database API, include `<code>tcutil.h</code>&#8216;, `<code>tchdb.h</code>&#8216;, and related standard header files. Usually, write the following description near the front of a source file. </p>
<pre><code>#include &lt;tcutil.h&gt;

#include &lt;tchdb.h&gt;

#include &lt;stdlib.h&gt;

#include &lt;time.h&gt;

#include &lt;stdbool.h&gt;

#include &lt;stdint.h&gt;</code></pre>
<p> Objects whose type is pointer to `<code>TCHDB</code>&#8216; are used to handle hash databases. A hash database object is created with the function `<code>tchdbnew</code>&#8216; and is deleted with the function `<code>tchdbdel</code>&#8216;. To avoid memory leak, it is important to delete every object when it is no longer in use. Before operations to store or retrieve records, it is necessary to open a database file and connect the hash database object to it. The function `<code>tchdbopen</code>&#8216; is used to open a database file and the function `<code>tchdbclose</code>&#8216; is used to close the database file. To avoid data missing or corruption, it is important to close every database file when it is no longer in use. It is forbidden for multible database objects in a process to open the same database at the same time. </p>
<h2>Api</h2>
<p>The function `tchdberrmsg&#8217; is used in order to get the message string corresponding to an error code. </p>
<dl>
<dd><code>const char *tchdberrmsg(int </code><i>ecode</i><code>);</code></p>
<dl>
<dd>`<i>ecode</i>&#8216; specifies the error code.</dl>
<dl>
<dd>The return value is the message string of the error code.</dl>
</dl>
<p> The function `tchdbnew&#8217; is used in order to create a hash database object. </p>
<dl>
<dd><code>TCHDB *tchdbnew(void);</code></p>
<dl>
<dd>The return value is the new hash database object.</dl>
</dl>
<p> The function `tchdbdel&#8217; is used in order to delete a hash database object. </p>
<dl>
<dd><code>void tchdbdel(TCHDB *</code><i>hdb</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object.</dl>
<dl>
<dd>If the database is not closed, it is closed implicitly. Note that the deleted object and its derivatives can not be used anymore.</dl>
</dl>
<p> The function `tchdbecode&#8217; is used in order to get the last happened error code of a hash database object. </p>
<dl>
<dd><code>int tchdbecode(TCHDB *</code><i>hdb</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object.</dl>
<dl>
<dd>The return value is the last happened error code.</dl>
<dl>
<dd>The following error codes are defined: `TCESUCCESS&#8217; for success, `TCETHREAD&#8217; for threading error, `TCEINVALID&#8217; for invalid operation, `TCENOFILE&#8217; for file not found, `TCENOPERM&#8217; for no permission, `TCEMETA&#8217; for invalid meta data, `TCERHEAD&#8217; for invalid record header, `TCEOPEN&#8217; for open error, `TCECLOSE&#8217; for close error, `TCETRUNC&#8217; for trunc error, `TCESYNC&#8217; for sync error, `TCESTAT&#8217; for stat error, `TCESEEK&#8217; for seek error, `TCEREAD&#8217; for read error, `TCEWRITE&#8217; for write error, `TCEMMAP&#8217; for mmap error, `TCELOCK&#8217; for lock error, `TCEUNLINK&#8217; for unlink error, `TCERENAME&#8217; for rename error, `TCEMKDIR&#8217; for mkdir error, `TCERMDIR&#8217; for rmdir error, `TCEKEEP&#8217; for existing record, `TCENOREC&#8217; for no record found, and `TCEMISC&#8217; for miscellaneous error.</dl>
</dl>
<p> The function `tchdbsetmutex&#8217; is used in order to set mutual exclusion control of a hash database object for threading. </p>
<dl>
<dd><code>bool tchdbsetmutex(TCHDB *</code><i>hdb</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object which is not opened.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Note that the mutual exclusion control of the database should be set before the database is opened.</dl>
</dl>
<p> The function `tchdbtune&#8217; is used in order to set the tuning parameters of a hash database object. </p>
<dl>
<dd><code>bool tchdbtune(TCHDB *</code><i>hdb</i><code>, int64_t </code><i>bnum</i><code>, int8_t </code><i>apow</i><code>, int8_t </code><i>fpow</i><code>, uint8_t </code><i>opts</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object which is not opened.</dl>
<dl>
<dd>`<i>bnum</i>&#8216; specifies the number of elements of the bucket array. If it is not more than 0, the default value is specified. The default value is 16381. Suggested size of the bucket array is about from 0.5 to 4 times of the number of all records to be stored.</dl>
<dl>
<dd>`<i>apow</i>&#8216; specifies the size of record alignment by power of 2. If it is negative, the default value is specified. The default value is 4 standing for 2^4=16.</dl>
<dl>
<dd>`<i>fpow</i>&#8216; specifies the maximum number of elements of the free block pool by power of 2. If it is negative, the default value is specified. The default value is 10 standing for 2^10=1024.</dl>
<dl>
<dd>`<i>opts</i>&#8216; specifies options by bitwise-or: `HDBTLARGE&#8217; specifies that the size of the database can be larger than 2GB by using 64-bit bucket array, `HDBTDEFLATE&#8217; specifies that each record is compressed with Deflate encoding, `HDBTBZIP&#8217; specifies that each record is compressed with BZIP2 encoding, `HDBTTCBS&#8217; specifies that each record is compressed with TCBS encoding.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Note that the tuning parameters should be set before the database is opened.</dl>
</dl>
<p> The function `tchdbsetcache&#8217; is used in order to set the caching parameters of a hash database object. </p>
<dl>
<dd><code>bool tchdbsetcache(TCHDB *</code><i>hdb</i><code>, int32_t </code><i>rcnum</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object which is not opened.</dl>
<dl>
<dd>`<i>rcnum</i>&#8216; specifies the maximum number of records to be cached. If it is not more than 0, the record cache is disabled. It is disabled by default.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Note that the caching parameters should be set before the database is opened.</dl>
</dl>
<p> The function `tchdbsetxmsiz&#8217; is used in order to set the size of the extra mapped memory of a hash database object. </p>
<dl>
<dd><code>bool tchdbsetxmsiz(TCHDB *</code><i>hdb</i><code>, int64_t </code><i>xmsiz</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object which is not opened.</dl>
<dl>
<dd>`<i>xmsiz</i>&#8216; specifies the size of the extra mapped memory. If it is not more than 0, the extra mapped memory is disabled. The default size is 67108864.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Note that the mapping parameters should be set before the database is opened.</dl>
</dl>
<p> The function `tchdbsetdfunit&#8217; is used in order to set the unit step number of auto defragmentation of a hash database object. </p>
<dl>
<dd><code>bool tchdbsetdfunit(TCHDB *</code><i>hdb</i><code>, int32_t </code><i>dfunit</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object which is not opened.</dl>
<dl>
<dd>`<i>dfunit</i>&#8216; specifie the unit step number. If it is not more than 0, the auto defragmentation is disabled. It is disabled by default.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Note that the defragmentation parameters should be set before the database is opened.</dl>
</dl>
<p> The function `tchdbopen&#8217; is used in order to open a database file and connect a hash database object. </p>
<dl>
<dd><code>bool tchdbopen(TCHDB *</code><i>hdb</i><code>, const char *</code><i>path</i><code>, int </code><i>omode</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object which is not opened.</dl>
<dl>
<dd>`<i>path</i>&#8216; specifies the path of the database file.</dl>
<dl>
<dd>`<i>omode</i>&#8216; specifies the connection mode: `HDBOWRITER&#8217; as a writer, `HDBOREADER&#8217; as a reader. If the mode is `HDBOWRITER&#8217;, the following may be added by bitwise-or: `HDBOCREAT&#8217;, which means it creates a new database if not exist, `HDBOTRUNC&#8217;, which means it creates a new database regardless if one exists, `HDBOTSYNC&#8217;, which means every transaction synchronizes updated contents with the device. Both of `HDBOREADER&#8217; and `HDBOWRITER&#8217; can be added to by bitwise-or: `HDBONOLCK&#8217;, which means it opens the database file without file locking, or `HDBOLCKNB&#8217;, which means locking is performed without blocking.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
</dl>
<p> The function `tchdbclose&#8217; is used in order to close a hash database object. </p>
<dl>
<dd><code>bool tchdbclose(TCHDB *</code><i>hdb</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Update of a database is assured to be written when the database is closed. If a writer opens a database but does not close it appropriately, the database will be broken.</dl>
</dl>
<p> The function `tchdbput&#8217; is used in order to store a record into a hash database object. </p>
<dl>
<dd><code>bool tchdbput(TCHDB *</code><i>hdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object connected as a writer.</dl>
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
<p> The function `tchdbput2&#8242; is used in order to store a string record into a hash database object. </p>
<dl>
<dd><code>bool tchdbput2(TCHDB *</code><i>hdb</i><code>, const char *</code><i>kstr</i><code>, const char *</code><i>vstr</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object connected as a writer.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>`<i>vstr</i>&#8216; specifies the string of the value.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the database, it is overwritten.</dl>
</dl>
<p> The function `tchdbputkeep&#8217; is used in order to store a new record into a hash database object. </p>
<dl>
<dd><code>bool tchdbputkeep(TCHDB *</code><i>hdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object connected as a writer.</dl>
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
<p> The function `tchdbputkeep2&#8242; is used in order to store a new string record into a hash database object. </p>
<dl>
<dd><code>bool tchdbputkeep2(TCHDB *</code><i>hdb</i><code>, const char *</code><i>kstr</i><code>, const char *</code><i>vstr</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object connected as a writer.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>`<i>vstr</i>&#8216; specifies the string of the value.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the database, this function has no effect.</dl>
</dl>
<p> The function `tchdbputcat&#8217; is used in order to concatenate a value at the end of the existing record in a hash database object. </p>
<dl>
<dd><code>bool tchdbputcat(TCHDB *</code><i>hdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object connected as a writer.</dl>
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
<p> The function `tchdbputcat2&#8242; is used in order to concatenate a string value at the end of the existing record in a hash database object. </p>
<dl>
<dd><code>bool tchdbputcat2(TCHDB *</code><i>hdb</i><code>, const char *</code><i>kstr</i><code>, const char *</code><i>vstr</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object connected as a writer.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>`<i>vstr</i>&#8216; specifies the string of the value.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If there is no corresponding record, a new record is created.</dl>
</dl>
<p> The function `tchdbputasync&#8217; is used in order to store a record into a hash database object in asynchronous fashion. </p>
<dl>
<dd><code>bool tchdbputasync(TCHDB *</code><i>hdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object connected as a writer.</dl>
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
<dd>If a record with the same key exists in the database, it is overwritten. Records passed to this function are accumulated into the inner buffer and wrote into the file at a blast.</dl>
</dl>
<p> The function `tchdbputasync2&#8242; is used in order to store a string record into a hash database object in asynchronous fashion. </p>
<dl>
<dd><code>bool tchdbputasync2(TCHDB *</code><i>hdb</i><code>, const char *</code><i>kstr</i><code>, const char *</code><i>vstr</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object connected as a writer.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>`<i>vstr</i>&#8216; specifies the string of the value.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the database, it is overwritten. Records passed to this function are accumulated into the inner buffer and wrote into the file at a blast.</dl>
</dl>
<p> The function `tchdbout&#8217; is used in order to remove a record of a hash database object. </p>
<dl>
<dd><code>bool tchdbout(TCHDB *</code><i>hdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object connected as a writer.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
</dl>
<p> The function `tchdbout2&#8242; is used in order to remove a string record of a hash database object. </p>
<dl>
<dd><code>bool tchdbout2(TCHDB *</code><i>hdb</i><code>, const char *</code><i>kstr</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object connected as a writer.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
</dl>
<p> The function `tchdbget&#8217; is used in order to retrieve a record in a hash database object. </p>
<dl>
<dd><code>void *tchdbget(TCHDB *</code><i>hdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the region of the value of the corresponding record. `NULL&#8217; is returned if no record corresponds.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tchdbget2&#8242; is used in order to retrieve a string record in a hash database object. </p>
<dl>
<dd><code>char *tchdbget2(TCHDB *</code><i>hdb</i><code>, const char *</code><i>kstr</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>If successful, the return value is the string of the value of the corresponding record. `NULL&#8217; is returned if no record corresponds.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tchdbget3&#8242; is used in order to retrieve a record in a hash database object and write the value into a buffer. </p>
<dl>
<dd><code>int tchdbget3(TCHDB *</code><i>hdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, void *</code><i>vbuf</i><code>, int </code><i>max</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>vbuf</i>&#8216; specifies the pointer to the buffer into which the value of the corresponding record is written.</dl>
<dl>
<dd>`<i>max</i>&#8216; specifies the size of the buffer.</dl>
<dl>
<dd>If successful, the return value is the size of the written data, else, it is -1. -1 is returned if no record corresponds to the specified key.</dl>
<dl>
<dd>Note that an additional zero code is not appended at the end of the region of the writing buffer.</dl>
</dl>
<p> The function `tchdbvsiz&#8217; is used in order to get the size of the value of a record in a hash database object. </p>
<dl>
<dd><code>int tchdbvsiz(TCHDB *</code><i>hdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>If successful, the return value is the size of the value of the corresponding record, else, it is -1.</dl>
</dl>
<p> The function `tchdbvsiz2&#8242; is used in order to get the size of the value of a string record in a hash database object. </p>
<dl>
<dd><code>int tchdbvsiz2(TCHDB *</code><i>hdb</i><code>, const char *</code><i>kstr</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>If successful, the return value is the size of the value of the corresponding record, else, it is -1.</dl>
</dl>
<p> The function `tchdbiterinit&#8217; is used in order to initialize the iterator of a hash database object. </p>
<dl>
<dd><code>bool tchdbiterinit(TCHDB *</code><i>hdb</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>The iterator is used in order to access the key of every record stored in a database.</dl>
</dl>
<p> The function `tchdbiternext&#8217; is used in order to get the next key of the iterator of a hash database object. </p>
<dl>
<dd><code>void *tchdbiternext(TCHDB *</code><i>hdb</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the region of the next key, else, it is `NULL&#8217;. `NULL&#8217; is returned when no record is to be get out of the iterator.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use. It is possible to access every record by iteration of calling this function. It is allowed to update or remove records whose keys are fetched while the iteration. However, it is not assured if updating the database is occurred while the iteration. Besides, the order of this traversal access method is arbitrary, so it is not assured that the order of storing matches the one of the traversal access.</dl>
</dl>
<p> The function `tchdbiternext2&#8242; is used in order to get the next key string of the iterator of a hash database object. </p>
<dl>
<dd><code>char *tchdbiternext2(TCHDB *</code><i>hdb</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object.</dl>
<dl>
<dd>If successful, the return value is the string of the next key, else, it is `NULL&#8217;. `NULL&#8217; is returned when no record is to be get out of the iterator.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use. It is possible to access every record by iteration of calling this function. However, it is not assured if updating the database is occurred while the iteration. Besides, the order of this traversal access method is arbitrary, so it is not assured that the order of storing matches the one of the traversal access.</dl>
</dl>
<p> The function `tchdbiternext3&#8242; is used in order to get the next extensible objects of the iterator of a hash database object. </p>
<dl>
<dd><code>bool tchdbiternext3(TCHDB *</code><i>hdb</i><code>, TCXSTR *</code><i>kxstr</i><code>, TCXSTR *</code><i>vxstr</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object.</dl>
<dl>
<dd>`<i>kxstr</i>&#8216; specifies the object into which the next key is wrote down.</dl>
<dl>
<dd>`<i>vxstr</i>&#8216; specifies the object into which the next value is wrote down.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false. False is returned when no record is to be get out of the iterator.</dl>
</dl>
<p> The function `tchdbfwmkeys&#8217; is used in order to get forward matching keys in a hash database object. </p>
<dl>
<dd><code>TCLIST *tchdbfwmkeys(TCHDB *</code><i>hdb</i><code>, const void *</code><i>pbuf</i><code>, int </code><i>psiz</i><code>, int </code><i>max</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object.</dl>
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
<p> The function `tchdbfwmkeys2&#8242; is used in order to get forward matching string keys in a hash database object. </p>
<dl>
<dd><code>TCLIST *tchdbfwmkeys2(TCHDB *</code><i>hdb</i><code>, const char *</code><i>pstr</i><code>, int </code><i>max</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object.</dl>
<dl>
<dd>`<i>pstr</i>&#8216; specifies the string of the prefix.</dl>
<dl>
<dd>`<i>max</i>&#8216; specifies the maximum number of keys to be fetched. If it is negative, no limit is specified.</dl>
<dl>
<dd>The return value is a list object of the corresponding keys. This function does never fail. It returns an empty list even if no key corresponds.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use. Note that this function may be very slow because every key in the database is scanned.</dl>
</dl>
<p> The function `tchdbaddint&#8217; is used in order to add an integer to a record in a hash database object. </p>
<dl>
<dd><code>int tchdbaddint(TCHDB *</code><i>hdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, int </code><i>num</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object connected as a writer.</dl>
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
<p> The function `tchdbdbadddouble&#8217; is used in order to add a real number to a record in a hash database object. </p>
<dl>
<dd><code>double tchdbadddouble(TCHDB *</code><i>hdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, double </code><i>num</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object connected as a writer.</dl>
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
<p> The function `tchdbsync&#8217; is used in order to synchronize updated contents of a hash database object with the file and the device. </p>
<dl>
<dd><code>bool tchdbsync(TCHDB *</code><i>hdb</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object connected as a writer.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>This function is useful when another process connects to the same database file.</dl>
</dl>
<p> The function `tchdboptimize&#8217; is used in order to optimize the file of a hash database object. </p>
<dl>
<dd><code>bool tchdboptimize(TCHDB *</code><i>hdb</i><code>, int64_t </code><i>bnum</i><code>, int8_t </code><i>apow</i><code>, int8_t </code><i>fpow</i><code>, uint8_t </code><i>opts</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object connected as a writer.</dl>
<dl>
<dd>`<i>bnum</i>&#8216; specifies the number of elements of the bucket array. If it is not more than 0, the default value is specified. The default value is two times of the number of records.</dl>
<dl>
<dd>`<i>apow</i>&#8216; specifies the size of record alignment by power of 2. If it is negative, the current setting is not changed.</dl>
<dl>
<dd>`<i>fpow</i>&#8216; specifies the maximum number of elements of the free block pool by power of 2. If it is negative, the current setting is not changed.</dl>
<dl>
<dd>`<i>opts</i>&#8216; specifies options by bitwise-or: `HDBTLARGE&#8217; specifies that the size of the database can be larger than 2GB by using 64-bit bucket array, `HDBTDEFLATE&#8217; specifies that each record is compressed with Deflate encoding, `HDBTBZIP&#8217; specifies that each record is compressed with BZIP2 encoding, `HDBTTCBS&#8217; specifies that each record is compressed with TCBS encoding. If it is `UINT8_MAX&#8217;, the current setting is not changed.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>This function is useful to reduce the size of the database file with data fragmentation by successive updating.</dl>
</dl>
<p> The function `tchdbvanish&#8217; is used in order to remove all records of a hash database object. </p>
<dl>
<dd><code>bool tchdbvanish(TCHDB *</code><i>hdb</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object connected as a writer.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
</dl>
<p> The function `tchdbcopy&#8217; is used in order to copy the database file of a hash database object. </p>
<dl>
<dd><code>bool tchdbcopy(TCHDB *</code><i>hdb</i><code>, const char *</code><i>path</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object.</dl>
<dl>
<dd>`<i>path</i>&#8216; specifies the path of the destination file. If it begins with `@&#8217;, the trailing substring is executed as a command line.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false. False is returned if the executed command returns non-zero code.</dl>
<dl>
<dd>The database file is assured to be kept synchronized and not modified while the copying or executing operation is in progress. So, this function is useful to create a backup file of the database file.</dl>
</dl>
<p> The function `tchdbtranbegin&#8217; is used in order to begin the transaction of a hash database object. </p>
<dl>
<dd><code>bool tchdbtranbegin(TCHDB *</code><i>hdb</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object connected as a writer.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>The database is locked by the thread while the transaction so that only one transaction can be activated with a database object at the same time. Thus, the serializable isolation level is assumed if every database operation is performed in the transaction. All updated regions are kept track of by write ahead logging while the transaction. If the database is closed during transaction, the transaction is aborted implicitly.</dl>
</dl>
<p> The function `tchdbtrancommit&#8217; is used in order to commit the transaction of a hash database object. </p>
<dl>
<dd><code>bool tchdbtrancommit(TCHDB *</code><i>hdb</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object connected as a writer.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Update in the transaction is fixed when it is committed successfully.</dl>
</dl>
<p> The function `tchdbtranabort&#8217; is used in order to abort the transaction of a hash database object. </p>
<dl>
<dd><code>bool tchdbtranabort(TCHDB *</code><i>hdb</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object connected as a writer.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Update in the transaction is discarded when it is aborted. The state of the database is rollbacked to before transaction.</dl>
</dl>
<p> The function `tchdbpath&#8217; is used in order to get the file path of a hash database object. </p>
<dl>
<dd><code>const char *tchdbpath(TCHDB *</code><i>hdb</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object.</dl>
<dl>
<dd>The return value is the path of the database file or `NULL&#8217; if the object does not connect to any database file.</dl>
</dl>
<p> The function `tchdbrnum&#8217; is used in order to get the number of records of a hash database object. </p>
<dl>
<dd><code>uint64_t tchdbrnum(TCHDB *</code><i>hdb</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object.</dl>
<dl>
<dd>The return value is the number of records or 0 if the object does not connect to any database file.</dl>
</dl>
<p> The function `tchdbfsiz&#8217; is used in order to get the size of the database file of a hash database object. </p>
<dl>
<dd><code>uint64_t tchdbfsiz(TCHDB *</code><i>hdb</i><code>);</code></p>
<dl>
<dd>`<i>hdb</i>&#8216; specifies the hash database object.</dl>
<dl>
<dd>The return value is the size of the database file or 0 if the object does not connect to any database file.</dl>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-tchtest/">tchtest</a></code>(1), <code><a href="/docs/linux/man/1-tchmttest/">tchmttest</a></code>(1), <code><a href="/docs/linux/man/1-tchmgr/">tchmgr</a></code>(1), <code><a href="/docs/linux/man/3-tokyocabinet/">tokyocabinet</a></code>(3) </p>
