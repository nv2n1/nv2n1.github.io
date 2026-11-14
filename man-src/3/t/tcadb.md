---
title: "tcadb(3)"
name: "tcadb"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcadb/"
description: "tcadb – the abstract database API"
---

<p>tcadb &#8211; the abstract database API</p>
<h2>Description</h2>
<p>Abstract database is a set of interfaces to use on-memory hash database, on-memory tree database, hash database, B+ tree database, fixed-length database, and table database with the same API. To use the abstract database API, include `<code>tcutil.h</code>&#8216;, `<code>tcadb.h</code>&#8216;, and related standard header files. Usually, write the following description near the front of a source file. </p>
<pre><code>#include &lt;tcutil.h&gt;

#include &lt;tcadb.h&gt;

#include &lt;stdlib.h&gt;

#include &lt;stdbool.h&gt;

#include &lt;stdint.h&gt;</code></pre>
<p> Objects whose type is pointer to `<code>TCADB</code>&#8216; are used to handle abstract databases. An abstract database object is created with the function `<code>tcadbnew</code>&#8216; and is deleted with the function `<code>tcadbdel</code>&#8216;. To avoid memory leak, it is important to delete every object when it is no longer in use. Before operations to store or retrieve records, it is necessary to connect the abstract database object to the concrete one. The function `<code>tcadbopen</code>&#8216; is used to open a concrete database and the function `<code>tcadbclose</code>&#8216; is used to close the database. To avoid data missing or corruption, it is important to close every database instance when it is no longer in use. It is forbidden for multible database objects in a process to open the same database at the same time. </p>
<h2>Api</h2>
<p>The function `tcadbnew&#8217; is used in order to create an abstract database object. </p>
<dl>
<dd><code>TCADB *tcadbnew(void);</code></p>
<dl>
<dd>The return value is the new abstract database object.</dl>
</dl>
<p> The function `tcadbdel&#8217; is used in order to delete an abstract database object. </p>
<dl>
<dd><code>void tcadbdel(TCADB *</code><i>adb</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
</dl>
<p> The function `tcadbopen&#8217; is used in order to open an abstract database. </p>
<dl>
<dd><code>bool tcadbopen(TCADB *</code><i>adb</i><code>, const char *</code><i>name</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
<dl>
<dd>`<i>name</i>&#8216; specifies the name of the database. If it is &quot;*&quot;, the database will be an on-memory hash database. If it is &quot;+&quot;, the database will be an on-memory tree database. If its suffix is &quot;.tch&quot;, the database will be a hash database. If its suffix is &quot;.tcb&quot;, the database will be a B+ tree database. If its suffix is &quot;.tcf&quot;, the database will be a fixed-length database. If its suffix is &quot;.tct&quot;, the database will be a table database. Otherwise, this function fails. Tuning parameters can trail the name, separated by &quot;#&quot;. Each parameter is composed of the name and the value, separated by &quot;=&quot;. On-memory hash database supports &quot;bnum&quot;, &quot;capnum&quot;, and &quot;capsiz&quot;. On-memory tree database supports &quot;capnum&quot; and &quot;capsiz&quot;. Hash database supports &quot;mode&quot;, &quot;bnum&quot;, &quot;apow&quot;, &quot;fpow&quot;, &quot;opts&quot;, &quot;rcnum&quot;, &quot;xmsiz&quot;, and &quot;dfunit&quot;. B+ tree database supports &quot;mode&quot;, &quot;lmemb&quot;, &quot;nmemb&quot;, &quot;bnum&quot;, &quot;apow&quot;, &quot;fpow&quot;, &quot;opts&quot;, &quot;lcnum&quot;, &quot;ncnum&quot;, &quot;xmsiz&quot;, and &quot;dfunit&quot;. Fixed-length database supports &quot;mode&quot;, &quot;width&quot;, and &quot;limsiz&quot;. Table database supports &quot;mode&quot;, &quot;bnum&quot;, &quot;apow&quot;, &quot;fpow&quot;, &quot;opts&quot;, &quot;rcnum&quot;, &quot;lcnum&quot;, &quot;ncnum&quot;, &quot;xmsiz&quot;, &quot;dfunit&quot;, and &quot;idx&quot;.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>The tuning parameter &quot;capnum&quot; specifies the capacity number of records. &quot;capsiz&quot; specifies the capacity size of using memory. Records spilled the capacity are removed by the storing order. &quot;mode&quot; can contain &quot;w&quot; of writer, &quot;r&quot; of reader, &quot;c&quot; of creating, &quot;t&quot; of truncating, &quot;e&quot; of no locking, and &quot;f&quot; of non-blocking lock. The default mode is relevant to &quot;wc&quot;. &quot;opts&quot; can contains &quot;l&quot; of large option, &quot;d&quot; of Deflate option, &quot;b&quot; of BZIP2 option, and &quot;t&quot; of TCBS option. &quot;idx&quot; specifies the column name of an index and its type separated by &quot;:&quot;. For example, &quot;casket.tch#bnum=1000000#opts=ld&quot; means that the name of the database file is &quot;casket.tch&quot;, and the bucket number is 1000000, and the options are large and Deflate.</dl>
</dl>
<p> The function `tcadbclose&#8217; is used in order to close an abstract database object. </p>
<dl>
<dd><code>bool tcadbclose(TCADB *</code><i>adb</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Update of a database is assured to be written when the database is closed. If a writer opens a database but does not close it appropriately, the database will be broken.</dl>
</dl>
<p> The function `tcadbput&#8217; is used in order to store a record into an abstract database object. </p>
<dl>
<dd><code>bool tcadbput(TCADB *</code><i>adb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
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
<p> The function `tcadbput2&#8242; is used in order to store a string record into an abstract object. </p>
<dl>
<dd><code>bool tcadbput2(TCADB *</code><i>adb</i><code>, const char *</code><i>kstr</i><code>, const char *</code><i>vstr</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>`<i>vstr</i>&#8216; specifies the string of the value.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the database, it is overwritten.</dl>
</dl>
<p> The function `tcadbputkeep&#8217; is used in order to store a new record into an abstract database object. </p>
<dl>
<dd><code>bool tcadbputkeep(TCADB *</code><i>adb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
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
<p> The function `tcadbputkeep2&#8242; is used in order to store a new string record into an abstract database object. </p>
<dl>
<dd><code>bool tcadbputkeep2(TCADB *</code><i>adb</i><code>, const char *</code><i>kstr</i><code>, const char *</code><i>vstr</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>`<i>vstr</i>&#8216; specifies the string of the value.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If a record with the same key exists in the database, this function has no effect.</dl>
</dl>
<p> The function `tcadbputcat&#8217; is used in order to concatenate a value at the end of the existing record in an abstract database object. </p>
<dl>
<dd><code>bool tcadbputcat(TCADB *</code><i>adb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, const void *</code><i>vbuf</i><code>, int </code><i>vsiz</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
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
<p> The function `tcadbputcat2&#8242; is used in order to concatenate a string value at the end of the existing record in an abstract database object. </p>
<dl>
<dd><code>bool tcadbputcat2(TCADB *</code><i>adb</i><code>, const char *</code><i>kstr</i><code>, const char *</code><i>vstr</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>`<i>vstr</i>&#8216; specifies the string of the value.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>If there is no corresponding record, a new record is created.</dl>
</dl>
<p> The function `tcadbout&#8217; is used in order to remove a record of an abstract database object. </p>
<dl>
<dd><code>bool tcadbout(TCADB *</code><i>adb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
</dl>
<p> The function `tcadbout2&#8242; is used in order to remove a string record of an abstract database object. </p>
<dl>
<dd><code>bool tcadbout2(TCADB *</code><i>adb</i><code>, const char *</code><i>kstr</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
</dl>
<p> The function `tcadbget&#8217; is used in order to retrieve a record in an abstract database object. </p>
<dl>
<dd><code>void *tcadbget(TCADB *</code><i>adb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
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
<p> The function `tcadbget2&#8242; is used in order to retrieve a string record in an abstract database object. </p>
<dl>
<dd><code>char *tcadbget2(TCADB *</code><i>adb</i><code>, const char *</code><i>kstr</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>If successful, the return value is the string of the value of the corresponding record. `NULL&#8217; is returned if no record corresponds.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use.</dl>
</dl>
<p> The function `tcadbvsiz&#8217; is used in order to get the size of the value of a record in an abstract database object. </p>
<dl>
<dd><code>int tcadbvsiz(TCADB *</code><i>adb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
<dl>
<dd>`<i>kbuf</i>&#8216; specifies the pointer to the region of the key.</dl>
<dl>
<dd>`<i>ksiz</i>&#8216; specifies the size of the region of the key.</dl>
<dl>
<dd>If successful, the return value is the size of the value of the corresponding record, else, it is -1.</dl>
</dl>
<p> The function `tcadbvsiz2&#8242; is used in order to get the size of the value of a string record in an abstract database object. </p>
<dl>
<dd><code>int tcadbvsiz2(TCADB *</code><i>adb</i><code>, const char *</code><i>kstr</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
<dl>
<dd>`<i>kstr</i>&#8216; specifies the string of the key.</dl>
<dl>
<dd>If successful, the return value is the size of the value of the corresponding record, else, it is -1.</dl>
</dl>
<p> The function `tcadbiterinit&#8217; is used in order to initialize the iterator of an abstract database object. </p>
<dl>
<dd><code>bool tcadbiterinit(TCADB *</code><i>adb</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>The iterator is used in order to access the key of every record stored in a database.</dl>
</dl>
<p> The function `tcadbiternext&#8217; is used in order to get the next key of the iterator of an abstract database object. </p>
<dl>
<dd><code>void *tcadbiternext(TCADB *</code><i>adb</i><code>, int *</code><i>sp</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
<dl>
<dd>`<i>sp</i>&#8216; specifies the pointer to the variable into which the size of the region of the return value is assigned.</dl>
<dl>
<dd>If successful, the return value is the pointer to the region of the next key, else, it is `NULL&#8217;. `NULL&#8217; is returned when no record is to be get out of the iterator.</dl>
<dl>
<dd>Because an additional zero code is appended at the end of the region of the return value, the return value can be treated as a character string. Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use. It is possible to access every record by iteration of calling this function. It is allowed to update or remove records whose keys are fetched while the iteration. However, it is not assured if updating the database is occurred while the iteration. Besides, the order of this traversal access method is arbitrary, so it is not assured that the order of storing matches the one of the traversal access.</dl>
</dl>
<p> The function `tcadbiternext2&#8242; is used in order to get the next key string of the iterator of an abstract database object. </p>
<dl>
<dd><code>char *tcadbiternext2(TCADB *</code><i>adb</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
<dl>
<dd>If successful, the return value is the string of the next key, else, it is `NULL&#8217;. `NULL&#8217; is returned when no record is to be get out of the iterator.</dl>
<dl>
<dd>Because the region of the return value is allocated with the `malloc&#8217; call, it should be released with the `free&#8217; call when it is no longer in use. It is possible to access every record by iteration of calling this function. However, it is not assured if updating the database is occurred while the iteration. Besides, the order of this traversal access method is arbitrary, so it is not assured that the order of storing matches the one of the traversal access.</dl>
</dl>
<p> The function `tcadbfwmkeys&#8217; is used in order to get forward matching keys in an abstract database object. </p>
<dl>
<dd><code>TCLIST *tcadbfwmkeys(TCADB *</code><i>adb</i><code>, const void *</code><i>pbuf</i><code>, int </code><i>psiz</i><code>, int </code><i>max</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
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
<p> The function `tcadbfwmkeys2&#8242; is used in order to get forward matching string keys in an abstract database object. </p>
<dl>
<dd><code>TCLIST *tcadbfwmkeys2(TCADB *</code><i>adb</i><code>, const char *</code><i>pstr</i><code>, int </code><i>max</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
<dl>
<dd>`<i>pstr</i>&#8216; specifies the string of the prefix.</dl>
<dl>
<dd>`<i>max</i>&#8216; specifies the maximum number of keys to be fetched. If it is negative, no limit is specified.</dl>
<dl>
<dd>The return value is a list object of the corresponding keys. This function does never fail. It returns an empty list even if no key corresponds.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use. Note that this function may be very slow because every key in the database is scanned.</dl>
</dl>
<p> The function `tcadbaddint&#8217; is used in order to add an integer to a record in an abstract database object. </p>
<dl>
<dd><code>int tcadbaddint(TCADB *</code><i>adb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, int </code><i>num</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
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
<p> The function `tcadbadddouble&#8217; is used in order to add a real number to a record in an abstract database object. </p>
<dl>
<dd><code>double tcadbadddouble(TCADB *</code><i>adb</i><code>, const void *</code><i>kbuf</i><code>, int </code><i>ksiz</i><code>, double </code><i>num</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
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
<p> The function `tcadbsync&#8217; is used in order to synchronize updated contents of an abstract database object with the file and the device. </p>
<dl>
<dd><code>bool tcadbsync(TCADB *</code><i>adb</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
</dl>
<p> The function `tcadboptimize&#8217; is used in order to optimize the storage of an abstract database object. </p>
<dl>
<dd><code>bool tcadboptimize(TCADB *</code><i>adb</i><code>, const char *</code><i>params</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
<dl>
<dd>`<i>params</i>&#8216; specifies the string of the tuning parameters, which works as with the tuning of parameters the function `tcadbopen&#8217;. If it is `NULL&#8217;, it is not used.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>This function is useful to reduce the size of the database storage with data fragmentation by successive updating.</dl>
</dl>
<p> The function `tcadbvanish&#8217; is used in order to remove all records of an abstract database object. </p>
<dl>
<dd><code>bool tcadbvanish(TCADB *</code><i>adb</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
</dl>
<p> The function `tcadbcopy&#8217; is used in order to copy the database file of an abstract database object. </p>
<dl>
<dd><code>bool tcadbcopy(TCADB *</code><i>adb</i><code>, const char *</code><i>path</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
<dl>
<dd>`<i>path</i>&#8216; specifies the path of the destination file. If it begins with `@&#8217;, the trailing substring is executed as a command line.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false. False is returned if the executed command returns non-zero code.</dl>
<dl>
<dd>The database file is assured to be kept synchronized and not modified while the copying or executing operation is in progress. So, this function is useful to create a backup file of the database file.</dl>
</dl>
<p> The function `tcadbtranbegin&#8217; is used in order to begin the transaction of an abstract database object. </p>
<dl>
<dd><code>bool tcadbtranbegin(TCADB *</code><i>adb</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>The database is locked by the thread while the transaction so that only one transaction can be activated with a database object at the same time. Thus, the serializable isolation level is assumed if every database operation is performed in the transaction. All updated regions are kept track of by write ahead logging while the transaction. If the database is closed during transaction, the transaction is aborted implicitly.</dl>
</dl>
<p> The function `tcadbtrancommit&#8217; is used in order to commit the transaction of an abstract database object. </p>
<dl>
<dd><code>bool tcadbtrancommit(TCADB *</code><i>adb</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Update in the transaction is fixed when it is committed successfully.</dl>
</dl>
<p> The function `tcadbtranabort&#8217; is used in order to abort the transaction of an abstract database object. </p>
<dl>
<dd><code>bool tcadbtranabort(TCADB *</code><i>adb</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
<dl>
<dd>If successful, the return value is true, else, it is false.</dl>
<dl>
<dd>Update in the transaction is discarded when it is aborted. The state of the database is rollbacked to before transaction.</dl>
</dl>
<p> The function `tcadbpath&#8217; is used in order to get the file path of an abstract database object. </p>
<dl>
<dd><code>const char *tcadbpath(TCADB *</code><i>adb</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
<dl>
<dd>The return value is the path of the database file or `NULL&#8217; if the object does not connect to any database. &quot;*&quot; stands for on-memory hash database. &quot;+&quot; stands for on-memory tree database.</dl>
</dl>
<p> The function `tcadbrnum&#8217; is used in order to get the number of records of an abstract database object. </p>
<dl>
<dd><code>uint64_t tcadbrnum(TCADB *</code><i>adb</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
<dl>
<dd>The return value is the number of records or 0 if the object does not connect to any database instance.</dl>
</dl>
<p> The function `tcadbsize&#8217; is used in order to get the size of the database of an abstract database object. </p>
<dl>
<dd><code>uint64_t tcadbsize(TCADB *</code><i>adb</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
<dl>
<dd>The return value is the size of the database or 0 if the object does not connect to any database instance.</dl>
</dl>
<p> The function `tcadbmisc&#8217; is used in order to call a versatile function for miscellaneous operations of an abstract database object. </p>
<dl>
<dd><code>TCLIST *tcadbmisc(TCADB *</code><i>adb</i><code>, const char *</code><i>name</i><code>, const TCLIST *</code><i>args</i><code>);</code></p>
<dl>
<dd>`<i>adb</i>&#8216; specifies the abstract database object.</dl>
<dl>
<dd>`<i>name</i>&#8216; specifies the name of the function. All databases support &quot;put&quot;, &quot;out&quot;, &quot;get&quot;, &quot;putlist&quot;, &quot;outlist&quot;, &quot;getlist&quot;, and &quot;getpart&quot;. &quot;put&quot; is to store a record. It receives a key and a value, and returns an empty list. &quot;out&quot; is to remove a record. It receives a key, and returns an empty list. &quot;get&quot; is to retrieve a record. It receives a key, and returns a list of the values. &quot;putlist&quot; is to store records. It receives keys and values one after the other, and returns an empty list. &quot;outlist&quot; is to remove records. It receives keys, and returns an empty list. &quot;getlist&quot; is to retrieve records. It receives keys, and returns keys and values of corresponding records one after the other. &quot;getpart&quot; is to retrieve the partial value of a record. It receives a key, the offset of the region, and the length of the region.</dl>
<dl>
<dd>`<i>args</i>&#8216; specifies a list object containing arguments.</dl>
<dl>
<dd>If successful, the return value is a list object of the result. `NULL&#8217; is returned on failure.</dl>
<dl>
<dd>Because the object of the return value is created with the function `tclistnew&#8217;, it should be deleted with the function `tclistdel&#8217; when it is no longer in use.</dl>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-tcatest/">tcatest</a></code>(1), <code><a href="/docs/linux/man/1-tcamttest/">tcamttest</a></code>(1), <code><a href="/docs/linux/man/1-tcamgr/">tcamgr</a></code>(1), <code><a href="/docs/linux/man/3-tokyocabinet/">tokyocabinet</a></code>(3) </p>
