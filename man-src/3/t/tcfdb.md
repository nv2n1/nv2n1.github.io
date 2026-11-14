---
title: "tcfdb(3)"
name: "tcfdb"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcfdb/"
description: "tcfdb – the fixed-length database API"
---

<p>tcfdb &#8211; the fixed-length database API</p>
<h2>Description</h2>
<p>Fixed-length database is a file containing an array of fixed-length elements and is handled with the fixed-length database API. To use the fixed-length database API, include `<code>tcutil.h</code>&#8216;, `<code>tcfdb.h</code>&#8216;, and related standard header files. Usually, write the following description near the front of a source file. </p>
<pre><code>#include &lt;tcutil.h&gt;

#include &lt;tcfdb.h&gt;

#include &lt;stdlib.h&gt;

#include &lt;stdbool.h&gt;

#include &lt;stdint.h&gt;</code></pre>
<p> Objects whose type is pointer to `<code>TCFDB</code>&#8216; are used to handle fixed-length databases. A fixed-length database object is created with the function `<code>tcfdbnew</code>&#8216; and is deleted with the function `<code>tcfdbdel</code>&#8216;. To avoid memory leak, it is important to delete every object when it is no longer in use. Before operations to store or retrieve records, it is necessary to open a database file and connect the fixed-length database object to it. The function `<code>tcfdbopen</code>&#8216; is used to open a database file and the function `<code>tcfdbclose</code>&#8216; is used to close the database file. To avoid data missing or corruption, it is important to close every database file when it is no longer in use. It is forbidden for multible database objects in a process to open the same database at the same time. </p>
<h2>Api</h2>
<p>The function `tcfdberrmsg&#8217; is used in order to get the message string corresponding to an error code. </p>
<dl>
<dd><code>const char *tcfdberrmsg(int </code><i>ecode</i><code>);</code></p>
<dl>
<dd>`<i>ecode</i>&#8216; specifies the error code.</dl>
<dl>
<dd>The return value is the message string of the error code.</dl>
</dl>
<p> The function `tcfdbnew&#8217; is used in order to create a fixed-length database object. </p>
<dl>
<dd><code>TCFDB *tcfdbnew(void);</code></p>
<dl>
<dd>The return value is the new fixed-length database object.</dl>
</dl>
<p> The function `tcfdbdel&#8217; is used in order to delete a fixed-length database object. </p>
<dl>
<dd><code>void tcfdbdel(TCFDB *</code><i>fdb</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object.</dl>
<dl>
<dd>If the database is not closed, it is closed implicitly. Note that the deleted object and its derivatives can not be used anymore.</dl>
</dl>
<p> The function `tcfdbecode&#8217; is used in order to get the last happened error code of a fixed-length database object. </p>
<dl>
<dd><code>int tcfdbecode(TCFDB *</code><i>fdb</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object.</dl>
<dl>
<dd>The return value is the last happened error code.</dl>
<dl>
<dd>The following error codes are defined: `TCESUCCESS&#8217; for success, `TCETHREAD&#8217; for threading error, `TCEINVALID&#8217; for invalid operation, `TCENOFILE&#8217; for file not found, `TCENOPERM&#8217; for no permission, `TCEMETA&#8217; for invalid meta data, `TCERHEAD&#8217; for invalid record header, `TCEOPEN&#8217; for open error, `TCECLOSE&#8217; for close error, `TCETRUNC&#8217; for trunc error, `TCESYNC&#8217; for sync error, `TCESTAT&#8217; for stat error, `TCESEEK&#8217; for seek error, `TCEREAD&#8217; for read error, `TCEWRITE&#8217; for write error, `TCEMMAP&#8217; for mmap error, `TCELOCK&#8217; for lock error, `TCEUNLINK&#8217; for unlink error, `TCERENAME&#8217; for rename error, `TCEMKDIR&#8217; for mkdir error, `TCERMDIR&#8217; for rmdir error, `TCEKEEP&#8217; for existing record, `TCENOREC&#8217; for no record found, and `TCEMISC&#8217; for miscellaneous error.</dl>
</dl>
<p> The function `tcfdbsetmutex&#8217; is used in order to set mutual exclusion control of a fixed-length database object for threading. </p>
<dl>
<dd><code>bool tcfdbsetmutex(TCFDB *</code><i>fdb</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object which is not opened.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Note that the mutual exclusion control is needed if the object is shared by plural threads and this function should be called before the database is opened.</dl>
</dl>
<p> The function `tcfdbtune&#8217; is used in order to set the tuning parameters of a fixed-length database object. </p>
<dl>
<dd><code>bool tcfdbtune(TCFDB *</code><i>fdb</i><code>, int32_t </code><i>width</i><code>, int64_t </code><i>limsiz</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object which is not opened.</dl>
<dl>
<dd>`<i>width</i>&#8216; specifies the width of the value of each record. If it is not more than 0, the default value is specified. The default value is 255.</dl>
<dl>
<dd>`<i>limsiz</i>&#8216; specifies the limit size of the database file. If it is not more than 0, the default value is specified. The default value is 268435456.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Note that the tuning parameters should be set before the database is opened.</dl>
</dl>
<p> The function `tcfdbopen&#8217; is used in order to open a database file and connect a fixed-length database object. </p>
<dl>
<dd><code>bool tcfdbopen(TCFDB *</code><i>fdb</i><code>, const char *</code><i>path</i><code>, int </code><i>omode</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object which is not opened.</dl>
<dl>
<dd>`<i>path</i>&#8216; specifies the path of the database file.</dl>
<dl>
<dd>`<i>omode</i>&#8216; specifies the connection mode: `FDBOWRITER&#8217; as a writer, `FDBOREADER&#8217; as a reader. If the mode is `FDBOWRITER&#8217;, the following may be added by bitwise-or: `FDBOCREAT&#8217;, which means it creates a new database if not exist, `FDBOTRUNC&#8217;, which means it creates a new database regardless if one exists, `FDBOTSYNC&#8217;, which means every transaction synchronizes updated contents with the device. Both of `FDBOREADER&#8217; and `FDBOWRITER&#8217; can be added to by bitwise-or: `FDBONOLCK&#8217;, which means it opens the database file without file locking, or `FDBOLCKNB&#8217;, which means locking is performed without blocking.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
</dl>
<p> The function `tcfdbclose&#8217; is used in order to close a fixed-length database object. </p>
<dl>
<dd><code>bool tcfdbclose(TCFDB *</code><i>fdb</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Update of a database is assured to be written when the database is closed. If a writer opens a database but does not close it appropriately, the database will be broken.</dl>
</dl>
<p> The function `tcfdbput&#8217; is used in order to store a record into a fixed-length database object. </p>
<dl>
<dd><code>bool tcfdbput(TCFDB *</code><i>fdb</i><code>, int64_t </code><i>id</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object connected as a writer.</dl>
<dl>
<dd>`<i>id</i>&#8216; specifies the ID number. It should be more than 0. If it is `FDBIDMIN&#8217;, the minimum ID number of existing records is specified. If it is `FDBIDPREV&#8217;, the number less by one than the minimum ID number of existing records is specified. If it is `FDBIDMAX&#8217;, the maximum ID number of existing records is specified. If it is `FDBIDNEXT&#8217;, the number greater by one than the maximum ID number of existing records is specified.</dl>
<dl>
<dd>`<i>vbuf</i>&#8216; specifies the pointer to the region of the value.</dl>
<dl>
<dd>`<i>vsiz</i>&#8216; specifies the size of the region of the value. If the size of the value is greater than the width tuning parameter of the database, the size is cut down to the width.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the database, it is overwritten.</dl>
</dl>
<p> The function `tcfdbput2&#8242; is used in order to store a record with a decimal key into a fixed-length database object. </p>
<dl>
<dd><code>bool tcfdbput2(TCFDB *</code><i>fdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object connected as a writer.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the decimal key. It should be more than 0. If it is &quot;min&quot;, the minimum ID number of existing records is specified. If it is &quot;prev&quot;, the number less by one than the minimum ID number of existing records is specified. If it is &quot;max&quot;, the maximum ID number of existing records is specified. If it is &quot;next&quot;, the number greater by one than the maximum ID number of existing records is specified.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>vbuf</i>&#8216; specifies the pointer to the region of the value.</dl>
<dl>
<dd>`<i>vsiz</i>&#8216; specifies the size of the region of the value. If the size of the value is greater than the width tuning parameter of the database, the size is cut down to the width.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the database, it is overwritten.</dl>
</dl>
<p> The function `tcfdbput3&#8242; is used in order to store a string record with a decimal key into a fixed-length database object. </p>
<dl>
<dd><code>bool tcfdbput3(TCFDB *</code><i>fdb</i><code>, const char *</code><i>kstr</i><code>, const void *</code><i>vstr</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object connected as a writer.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the decimal key. It should be more than 0. If it is &quot;min&quot;, the minimum ID number of existing records is specified. If it is &quot;prev&quot;, the number less by one than the minimum ID number of existing records is specified. If it is &quot;max&quot;, the maximum ID number of existing records is specified. If it is &quot;next&quot;, the number greater by one than the maximum ID number of existing records is specified.</dl>
<dl>
<dd>`<i>vstr</i>&#8216; specifies the string of the value.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the database, it is overwritten.</dl>
</dl>
<p> The function `tcfdbputkeep&#8217; is used in order to store a new record into a fixed-length database object. </p>
<dl>
<dd><code>bool tcfdbputkeep(TCFDB *</code><i>fdb</i><code>, int64_t </code><i>id</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object connected as a writer.</dl>
<dl>
<dd>`<i>id</i>&#8216; specifies the ID number. It should be more than 0. If it is `FDBIDMIN&#8217;, the minimum ID number of existing records is specified. If it is `FDBIDPREV&#8217;, the number less by one than the minimum ID number of existing records is specified. If it is `FDBIDMAX&#8217;, the maximum ID number of existing records is specified. If it is `FDBIDNEXT&#8217;, the number greater by one than the maximum ID number of existing records is specified.</dl>
<dl>
<dd>`<i>vbuf</i>&#8216; specifies the pointer to the region of the value.</dl>
<dl>
<dd>`<i>vsiz</i>&#8216; specifies the size of the region of the value. If the size of the value is greater than the width tuning parameter of the database, the size is cut down to the width.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the database, this function has no effect.</dl>
</dl>
<p> The function `tcfdbputkeep2&#8242; is used in order to store a new record with a decimal key into a fixed-length database object. </p>
<dl>
<dd><code>bool tcfdbputkeep2(TCFDB *</code><i>fdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object connected as a writer.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the decimal key. It should be more than 0. If it is &quot;min&quot;, the minimum ID number of existing records is specified. If it is &quot;prev&quot;, the number less by one than the minimum ID number of existing records is specified. If it is &quot;max&quot;, the maximum ID number of existing records is specified. If it is &quot;next&quot;, the number greater by one than the maximum ID number of existing records is specified.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>vbuf</i>&#8216; specifies the pointer to the region of the value.</dl>
<dl>
<dd>`<i>vsiz</i>&#8216; specifies the size of the region of the value. If the size of the value is greater than the width tuning parameter of the database, the size is cut down to the width.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the database, this function has no effect.</dl>
</dl>
<p> The function `tcfdbputkeep3&#8242; is used in order to store a new string record with a decimal key into a fixed-length database object. </p>
<dl>
<dd><code>bool tcfdbputkeep3(TCFDB *</code><i>fdb</i><code>, const char *</code><i>kstr</i><code>, const void *</code><i>vstr</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object connected as a writer.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the decimal key. It should be more than 0. If it is &quot;min&quot;, the minimum ID number of existing records is specified. If it is &quot;prev&quot;, the number less by one than the minimum ID number of existing records is specified. If it is &quot;max&quot;, the maximum ID number of existing records is specified. If it is &quot;next&quot;, the number greater by one than the maximum ID number of existing records is specified.</dl>
<dl>
<dd>`<i>vstr</i>&#8216; specifies the string of the value.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the database, this function has no effect.</dl>
</dl>
<p> The function `tcfdbputcat&#8217; is used in order to concatenate a value at the end of the existing record in a fixed-length database object. </p>
<dl>
<dd><code>bool tcfdbputcat(TCFDB *</code><i>fdb</i><code>, int64_t </code><i>id</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object connected as a writer.</dl>
<dl>
<dd>`<i>id</i>&#8216; specifies the ID number. It should be more than 0. If it is `FDBIDMIN&#8217;, the minimum ID number of existing records is specified. If it is `FDBIDPREV&#8217;, the number less by one than the minimum ID number of existing records is specified. If it is `FDBIDMAX&#8217;, the maximum ID number of existing records is specified. If it is `FDBIDNEXT&#8217;, the number greater by one than the maximum ID number of existing records is specified.</dl>
<dl>
<dd>`<i>vbuf</i>&#8216; specifies the pointer to the region of the value.</dl>
<dl>
<dd>`<i>vsiz</i>&#8216; specifies the size of the region of the value. If the size of the value is greater than the width tuning parameter of the database, the size is cut down to the width.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If there is no corresponding record, a new record is created.</dl>
</dl>
<p> The function `tcfdbputcat2&#8242; is used in order to concatenate a value with a decimal key in a fixed-length database object. </p>
<dl>
<dd><code>bool tcfdbputcat2(TCFDB *</code><i>fdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object connected as a writer.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the decimal key. It should be more than 0. If it is &quot;min&quot;, the minimum ID number of existing records is specified. If it is &quot;prev&quot;, the number less by one than the minimum ID number of existing records is specified. If it is &quot;max&quot;, the maximum ID number of existing records is specified. If it is &quot;next&quot;, the number greater by one than the maximum ID number of existing records is specified.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>vbuf</i>&#8216; specifies the pointer to the region of the value.</dl>
<dl>
<dd>`<i>vsiz</i>&#8216; specifies the size of the region of the value. If the size of the value is greater than the width tuning parameter of the database, the size is cut down to the width.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If there is no corresponding record, a new record is created.</dl>
</dl>
<p> The function `tcfdbputcat3&#8242; is used in order to concatenate a string value with a decimal key in a fixed-length database object. </p>
<dl>
<dd><code>bool tcfdbputcat3(TCFDB *</code><i>fdb</i><code>, const char *</code><i>kstr</i><code>, const void *</code><i>vstr</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object connected as a writer.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the decimal key. It should be more than 0. If it is &quot;min&quot;, the minimum ID number of existing records is specified. If it is &quot;prev&quot;, the number less by one than the minimum ID number of existing records is specified. If it is &quot;max&quot;, the maximum ID number of existing records is specified. If it is &quot;next&quot;, the number greater by one than the maximum ID number of existing records is specified.</dl>
<dl>
<dd>`<i>vstr</i>&#8216; specifies the string of the value.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If there is no corresponding record, a new record is created.</dl>
</dl>
<p> The function `tcfdbout&#8217; is used in order to remove a record of a fixed-length database object. </p>
<dl>
<dd><code>bool tcfdbout(TCFDB *</code><i>fdb</i><code>, int64_t </code><i>id</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object connected as a writer.</dl>
<dl>
<dd>`<i>id</i>&#8216; specifies the ID number. It should be more than 0. If it is `FDBIDMIN&#8217;, the minimum ID number of existing records is specified. If it is `FDBIDMAX&#8217;, the maximum ID number of existing records is specified.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
</dl>
<p> The function `tcfdbout2&#8242; is used in order to remove a record with a decimal key of a fixed-length database object. </p>
<dl>
<dd><code>bool tcfdbout2(TCFDB *</code><i>fdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object connected as a writer.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the decimal key. It should be more than 0. If it is &quot;min&quot;, the minimum ID number of existing records is specified. If it is &quot;max&quot;, the maximum ID number of existing records is specified.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
</dl>
<p> The function `tcfdbout3&#8242; is used in order to remove a string record with a decimal key of a fixed-length database object. </p>
<dl>
<dd><code>bool tcfdbout3(TCFDB *</code><i>fdb</i><code>, const char *</code><i>kstr</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object connected as a writer.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the decimal key. It should be more than 0. If it is &quot;min&quot;, the minimum ID number of existing records is specified. If it is &quot;max&quot;, the maximum ID number of existing records is specified.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
</dl>
<p> The function `tcfdbget&#8217; is used in order to retrieve a record in a fixed-length database object. </p>
<dl>
<dd><code>void *tcfdbget(TCFDB *</code><i>fdb</i><code>, int64_t </code><i>id</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object.</dl>
<dl>
<dd>`<i>id</i>&#8216; specifies the ID number. It should be more than 0. If it is `FDBIDMIN&#8217;, the minimum ID number of existing records is specified. If it is `FDBIDMAX&#8217;, the maximum ID number of existing records is specified.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the region of the value of the corresponding record. `NULL&#8217; is returned if no record corresponds.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcfdbget2&#8242; is used in order to retrieve a record with a decimal key in a fixed-length database object. </p>
<dl>
<dd><code>void *tcfdbget2(TCFDB *</code><i>fdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the decimal key. It should be more than 0. If it is &quot;min&quot;, the minimum ID number of existing records is specified. If it is &quot;max&quot;, the maximum ID number of existing records is specified.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the region of the value of the corresponding record. `NULL&#8217; is returned if no record corresponds.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcfdbget3&#8242; is used in order to retrieve a string record with a decimal key in a fixed-length database object. </p>
<dl>
<dd><code>char *tcfdbget3(TCFDB *</code><i>fdb</i><code>, const char *</code><i>kstr</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the decimal key. It should be more than 0. If it is &quot;min&quot;, the minimum ID number of existing records is specified. If it is &quot;max&quot;, the maximum ID number of existing records is specified.</dl>
<dl>
<dd>If successful, the return value is the string of the value of the corresponding record. `NULL&#8217; is returned if no record corresponds.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcfdbget4&#8242; is used in order to retrieve a record in a fixed-length database object and write the value into a buffer. </p>
<dl>
<dd><code>int tcfdbget4(TCFDB *</code><i>fdb</i><code>, int64_t </code><i>id</i><code>, void *</code><i>vbuf</i><code>, int </code><i>max</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object.</dl>
<dl>
<dd>`<i>id</i>&#8216; specifies the ID number. It should be more than 0. If it is `FDBIDMIN&#8217;, the minimum ID number of existing records is specified. If it is `FDBIDMAX&#8217;, the maximum ID number of existing records is specified.</dl>
<dl>
<dd>`<i>vbuf</i>&#8216; specifies the pointer to the buffer into which the value of the corresponding record is written.</dl>
<dl>
<dd>`<i>max</i>&#8216; specifies the size of the buffer.</dl>
<dl>
<dd>If successful, the return value is the size of the written data, else, it is -1. -1 is returned if no record corresponds to the specified key.</dl>
<dl>
<dd>Note that an additional zero code is not appended at the end of the region of the writing buffer.</dl>
</dl>
<p> The function `tcfdbvsiz&#8217; is used in order to get the size of the value of a record in a fixed-length database object. </p>
<dl>
<dd><code>int tcfdbvsiz(TCFDB *</code><i>fdb</i><code>, int64_t </code><i>id</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object.</dl>
<dl>
<dd>`<i>id</i>&#8216; specifies the ID number. It should be more than 0. If it is `FDBIDMIN&#8217;, the minimum ID number of existing records is specified. If it is `FDBIDMAX&#8217;, the maximum ID number of existing records is specified.</dl>
<dl>
<dd>If successful, the return value is the size of the value of the corresponding record, else, it is -1.</dl>
</dl>
<p> The function `tcfdbvsiz2&#8242; is used in order to get the size of the value with a decimal key in a fixed-length database object. </p>
<dl>
<dd><code>int tcfdbvsiz2(TCFDB *</code><i>fdb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the decimal key. It should be more than 0. If it is &quot;min&quot;, the minimum ID number of existing records is specified. If it is &quot;max&quot;, the maximum ID number of existing records is specified.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>If successful, the return value is the size of the value of the corresponding record, else, it is -1.</dl>
</dl>
<p> The function `tcfdbvsiz3&#8242; is used in order to get the size of the string value with a decimal key in a fixed-length database object. </p>
<dl>
<dd><code>int tcfdbvsiz3(TCFDB *</code><i>fdb</i><code>, const char *</code><i>kstr</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the decimal key. It should be more than 0. If it is &quot;min&quot;, the minimum ID number of existing records is specified. If it is &quot;max&quot;, the maximum ID number of existing records is specified.</dl>
<dl>
<dd>If successful, the return value is the size of the value of the corresponding record, else, it is -1.</dl>
</dl>
<p> The function `tcfdbiterinit&#8217; is used in order to initialize the iterator of a fixed-length database object. </p>
<dl>
<dd><code>bool tcfdbiterinit(TCFDB *</code><i>fdb</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>The iterator is used in order to access the key of every record stored in a database.</dl>
</dl>
<p> The function `tcfdbiternext&#8217; is used in order to get the next ID number of the iterator of a fixed-length database object. </p>
<dl>
<dd><code>uint64_t tcfdbiternext(TCFDB *</code><i>fdb</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object.</dl>
<dl>
<dd>If successful, the return value is the next ID number of the iterator, else, it is 0. 0 is returned when no record is to be get out of the iterator.</dl>
<dl>
<dd>It is possible to access every record by iteration of calling this function. It is allowed to update or remove records whose keys are fetched while the iteration. The order of this traversal access method is ascending of the ID number.</dl>
</dl>
<p> The function `tcfdbiternext2&#8242; is used in order to get the next decimay key of the iterator of a fixed-length database object. </p>
<dl>
<dd><code>void *tcfdbiternext2(TCFDB *</code><i>fdb</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the region of the next decimal key, else, it is `NULL&#8217;. `NULL&#8217; is returned when no record is to be get out of the iterator.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use. It is possible to access every record by iteration of calling this function. It is allowed to update or remove records whose keys are fetched while the iteration. The order of this traversal access method is ascending of the ID number.</dl>
</dl>
<p> The function `tcfdbiternext3&#8242; is used in order to get the next decimay key string of the iterator of a fixed-length database object. </p>
<dl>
<dd><code>char *tcfdbiternext3(TCFDB *</code><i>fdb</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object.</dl>
<dl>
<dd>If successful, the return value is the string of the next decimal key, else, it is `NULL&#8217;. `NULL&#8217; is returned when no record is to be get out of the iterator.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use. It is possible to access every record by iteration of calling this function. It is allowed to update or remove records whose keys are fetched while the iteration. The order of this traversal access method is ascending of the ID number.</dl>
</dl>
<p> The function `tcfdbrange&#8217; is used in order to get range matching ID numbers in a fixed-length database object. </p>
<dl>
<dd><code>uint64_t *tcfdbrange(TCFDB *</code><i>fdb</i><code>, int64_t </code><i>lower</i><code>, int64_t </code><i>upper</i><code>, int </code><i>max</i><code>, int *</code><i>np</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object.</dl>
<dl>
<dd>`<i>lower</i>&#8216; specifies the lower limit of the range. If it is `FDBIDMIN&#8217;, the minimum ID is specified.</dl>
<dl>
<dd>`<i>upper</i>&#8216; specifies the upper limit of the range. If it is `FDBIDMAX&#8217;, the maximum ID is specified.</dl>
<dl>
<dd>`<i>max</i>&#8216; specifies the maximum number of keys to be fetched. If it is negative, no limit is specified.</dl>
<dl>
<dd>`<i>np</i>&#8216; specifies the pointer to the variable into which the number of elements of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to an array of ID numbers of the corresponding records. `NULL&#8217; is returned on failure. This function does never fail. It returns an empty array even if no key corresponds.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcfdbrange2&#8242; is used in order to get range matching decimal keys in a fixed-length database object. </p>
<dl>
<dd><code>TCLIST *tcfdbrange2(TCFDB *</code><i>fdb</i><code>, const void *</code><i>lbuf</i><code>, int </code><i>lsiz</i><code>, const void *</code><i>ubuf</i><code>, int </code><i>usiz</i><code>, int </code><i>max</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object.</dl>
<dl>
<dd>`<i>lbuf</i>&#8216; specifies the pointer to the region of the lower key. If it is &quot;min&quot;, the minimum ID number of existing records is specified.</dl>
<dl>
<dd>`<i>lsiz</i>&#8216; specifies the size of the region of the lower key.</dl>
<dl>
<dd>`<i>ubuf</i>&#8216; specifies the pointer to the region of the upper key. If it is &quot;max&quot;, the maximum ID number of existing records is specified.</dl>
<dl>
<dd>`<i>usiz</i>&#8216; specifies the size of the region of the upper key.</dl>
<dl>
<dd>`<i>max</i>&#8216; specifies the maximum number of keys to be fetched. If it is negative, no limit is specified.</dl>
<dl>
<dd>The return value is a list object of the corresponding decimal keys. This function does never fail. It returns an empty list even if no key corresponds.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use. Note that this function may be very slow because every key in the database is scanned.</dl>
</dl>
<p> The function `tcfdbrange3&#8242; is used in order to get range matching decimal keys with strings in a fixed-length database object. </p>
<dl>
<dd><code>TCLIST *tcfdbrange3(TCFDB *</code><i>fdb</i><code>, const char *</code><i>lstr</i><code>, const char *</code><i>ustr</i><code>, int </code><i>max</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object.</dl>
<dl>
<dd>`<i>lstr</i>&#8216; specifies the string of the lower key. If it is &quot;min&quot;, the minimum ID number of existing records is specified.</dl>
<dl>
<dd>`<i>ustr</i>&#8216; specifies the string of the upper key. If it is &quot;max&quot;, the maximum ID number of existing records is specified.</dl>
<dl>
<dd>`<i>max</i>&#8216; specifies the maximum number of keys to be fetched. If it is negative, no limit is specified.</dl>
<dl>
<dd>The return value is a list object of the corresponding decimal keys. This function does never fail. It returns an empty list even if no key corresponds.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use. Note that this function may be very slow because every key in the database is scanned.</dl>
</dl>
<p> The function `tcfdbrange4&#8242; is used in order to get keys with an interval notation in a fixed-length database object. </p>
<dl>
<dd><code>TCLIST *tcfdbrange4(TCFDB *</code><i>fdb</i><code>, const void *</code><i>ibuf</i><code>, int </code><i>isiz</i><code>, int </code><i>max</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object.</dl>
<dl>
<dd>`<i>ibuf</i>&#8216; specifies the pointer to the region of the interval notation.</dl>
<dl>
<dd>`<i>isiz</i>&#8216; specifies the size of the region of the interval notation.</dl>
<dl>
<dd>`<i>max</i>&#8216; specifies the maximum number of keys to be fetched. If it is negative, no limit is specified.</dl>
<dl>
<dd>The return value is a list object of the corresponding decimal keys. This function does never fail. It returns an empty list even if no key corresponds.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use. Note that this function may be very slow because every key in the database is scanned.</dl>
</dl>
<p> The function `tcfdbrange5&#8242; is used in order to get keys with an interval notation string in a fixed-length database object. </p>
<dl>
<dd><code>TCLIST *tcfdbrange5(TCFDB *</code><i>fdb</i><code>, const void *</code><i>istr</i><code>, int </code><i>max</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object.</dl>
<dl>
<dd>`<i>istr</i>&#8216; specifies the pointer to the region of the interval notation string.</dl>
<dl>
<dd>`<i>max</i>&#8216; specifies the maximum number of keys to be fetched. If it is negative, no limit is specified.</dl>
<dl>
<dd>The return value is a list object of the corresponding decimal keys. This function does never fail. It returns an empty list even if no key corresponds.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use. Note that this function may be very slow because every key in the database is scanned.</dl>
</dl>
<p> The function `tcfdbaddint&#8217; is used in order to add an integer to a record in a fixed-length database object. </p>
<dl>
<dd><code>int tcfdbaddint(TCFDB *</code><i>fdb</i><code>, int64_t </code><i>id</i><code>, int </code><i>num</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object connected as a writer.</dl>
<dl>
<dd>`<i>id</i>&#8216; specifies the ID number. It should be more than 0. If it is `FDBIDMIN&#8217;, the minimum ID number of existing records is specified. If it is `FDBIDPREV&#8217;, the number less by one than the minimum ID number of existing records is specified. If it is `FDBIDMAX&#8217;, the maximum ID number of existing records is specified. If it is `FDBIDNEXT&#8217;, the number greater by one than the maximum ID number of existing records is specified.</dl>
<dl>
<dd>`<i>num</i>&#8216; specifies the additional value.</dl>
<dl>
<dd>If successful, the return value is the summation value, else, it is `INT_MIN&#8217;.</dl>
<dl>
<dd>If the corresponding record exists, the value is treated as an integer and is added to. If no record corresponds, a new record of the additional value is stored.</dl>
</dl>
<p> The function `tcfdbadddouble&#8217; is used in order to add a real number to a record in a fixed-length database object. </p>
<dl>
<dd><code>double tcfdbadddouble(TCFDB *</code><i>fdb</i><code>, int64_t </code><i>id</i><code>, double </code><i>num</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object connected as a writer.</dl>
<dl>
<dd>`<i>id</i>&#8216; specifies the ID number. It should be more than 0. If it is `FDBIDMIN&#8217;, the minimum ID number of existing records is specified. If it is `FDBIDPREV&#8217;, the number less by one than the minimum ID number of existing records is specified. If it is `FDBIDMAX&#8217;, the maximum ID number of existing records is specified. If it is `FDBIDNEXT&#8217;, the number greater by one than the maximum ID number of existing records is specified.</dl>
<dl>
<dd>`<i>num</i>&#8216; specifies the additional value.</dl>
<dl>
<dd>If successful, the return value is the summation value, else, it is Not-a-Number.</dl>
<dl>
<dd>If the corresponding record exists, the value is treated as a real number and is added to. If no record corresponds, a new record of the additional value is stored.</dl>
</dl>
<p> The function `tcfdbsync&#8217; is used in order to synchronize updated contents of a fixed-length database object with the file and the device. </p>
<dl>
<dd><code>bool tcfdbsync(TCFDB *</code><i>fdb</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object connected as a writer.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>This function is useful when another process connects to the same database file.</dl>
</dl>
<p> The function `tcfdboptimize&#8217; is used in order to optimize the file of a fixed-length database object. </p>
<dl>
<dd><code>bool tcfdboptimize(TCFDB *</code><i>fdb</i><code>, int32_t </code><i>width</i><code>, int64_t </code><i>limsiz</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object connected as a writer.</dl>
<dl>
<dd>`<i>width</i>&#8216; specifies the width of the value of each record. If it is not more than 0, the current setting is not changed.</dl>
<dl>
<dd>`<i>limsiz</i>&#8216; specifies the limit size of the database file. If it is not more than 0, the current setting is not changed.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
</dl>
<p> The function `tcfdbvanish&#8217; is used in order to remove all records of a fixed-length database object. </p>
<dl>
<dd><code>bool tcfdbvanish(TCFDB *</code><i>fdb</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object connected as a writer.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
</dl>
<p> The function `tcfdbcopy&#8217; is used in order to copy the database file of a fixed-length database object. </p>
<dl>
<dd><code>bool tcfdbcopy(TCFDB *</code><i>fdb</i><code>, const char *</code><i>path</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object.</dl>
<dl>
<dd>`<i>path</i>&#8216; specifies the path of the destination file. If it begins with `@&#8217;, the trailing substring is executed as a command line.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false. False is returned if the executed command returns non-zero code.</dl>
<dl>
<dd>The database file is assured to be kept synchronized and not modified while the copying or executing operation is in progress. So, this function is useful to create a backup file of the database file.</dl>
</dl>
<p> The function `tcfdbtranbegin&#8217; is used in order to begin the transaction of a fixed-length database object. </p>
<dl>
<dd><code>bool tcfdbtranbegin(TCFDB *</code><i>fdb</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object connected as a writer.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>The database is locked by the thread while the transaction so that only one transaction can be activated with a database object at the same time. Thus, the serializable isolation level is assumed if every database operation is performed in the transaction. All updated regions are kept track of by write ahead logging while the transaction. If the database is closed during transaction, the transaction is aborted implicitly.</dl>
</dl>
<p> The function `tcfdbtrancommit&#8217; is used in order to commit the transaction of a fixed-length database object. </p>
<dl>
<dd><code>bool tcfdbtrancommit(TCFDB *</code><i>fdb</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object connected as a writer.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Update in the transaction is fixed when it is committed successfully.</dl>
</dl>
<p> The function `tcfdbtranabort&#8217; is used in order to abort the transaction of a fixed-length database object. </p>
<dl>
<dd><code>bool tcfdbtranabort(TCFDB *</code><i>fdb</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object connected as a writer.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Update in the transaction is discarded when it is aborted. The state of the database is rollbacked to before transaction.</dl>
</dl>
<p> The function `tcfdbpath&#8217; is used in order to get the file path of a fixed-length database object. </p>
<dl>
<dd><code>const char *tcfdbpath(TCFDB *</code><i>fdb</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object.</dl>
<dl>
<dd>The return value is the path of the database file or `NULL&#8217; if the object does not connect to any database file.</dl>
</dl>
<p> The function `tcfdbrnum&#8217; is used in order to get the number of records of a fixed-length database object. </p>
<dl>
<dd><code>uint64_t tcfdbrnum(TCFDB *</code><i>fdb</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object.</dl>
<dl>
<dd>The return value is the number of records or 0 if the object does not connect to any database file.</dl>
</dl>
<p> The function `tcfdbfsiz&#8217; is used in order to get the size of the database file of a fixed-length database object. </p>
<dl>
<dd><code>uint64_t tcfdbfsiz(TCFDB *</code><i>fdb</i><code>);</code></p>
<dl>
<dd>`<i>fdb</i>&#8216; specifies the fixed-length database object.</dl>
<dl>
<dd>The return value is the size of the database file or 0 if the object does not connect to any database file.</dl>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-tcftest/">tcftest</a></code>(1), <code><a href="/docs/linux/man/1-tcfmttest/">tcfmttest</a></code>(1), <code><a href="/docs/linux/man/1-tcfmgr/">tcfmgr</a></code>(1), <code><a href="/docs/linux/man/3-tokyocabinet/">tokyocabinet</a></code>(3) </p>
