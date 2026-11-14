---
title: "kcforestmgr(1)"
name: "kcforestmgr"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kcforestmgr/"
description: "kcforestmgr – command line interface to manage the directory tree database"
---

<h2 class="name">NAME</h2>
<p> kcforestmgr &#8211; command line interface to manage the directory tree database</p>
<h2>DESCRIPTION</h2>
<p> The command `<code>kcforestmgr</code>&#8216; is a utility for test and debugging of the file tree database and its applications. `<i>path</i>&#8216; specifies the path of a database file. `<i>key</i>&#8216; specifies the key of a record. `<i>value</i>&#8216; specifies the value of a record. `<i>file</i>&#8216; specifies the input/output file. </p>
<dl>
<dt>
<dd>
 <code>kcforestmgr create </code>[<code>-otr</code>][<code>-onl</code>|<code>-otl</code>|<code>-onr</code>][<code>-tc</code>][<code>-bnum </code><i>num</i>][<code>-psiz </code><i>num</i>][<code>-rcd</code>|<code>-rcld</code>|<code>-rcdd</code>]<i>path</i></p>
<dl>
<dt>
<dd> Creates a database file.</dl>
<p> <code>kcforestmgr inform </code>[<code>-onl</code>|<code>-otl</code>|<code>-onr</code>][<code>-st</code>]<i>path</i></p>
<dl>
<dt>
<dd> Prints status information.</dl>
<p> <code>kcforestmgr set </code>[<code>-onl</code>|<code>-otl</code>|<code>-onr</code>][<code>-add</code>|<code>-app</code>|<code>-rep</code>|<code>-inci</code>|<code>-incd</code>][<code>-sx</code>]<i>path</i><i>key</i><i>value</i></p>
<dl>
<dt>
<dd> Stores a record.</dl>
<p> <code>kcforestmgr remove </code>[<code>-onl</code>|<code>-otl</code>|<code>-onr</code>][<code>-sx</code>]<i>path</i><i>key</i></p>
<dl>
<dt>
<dd> Removes a record.</dl>
<p> <code>kcforestmgr get </code>[<code>-onl</code>|<code>-otl</code>|<code>-onr</code>][<code>-rm</code>][<code>-sx</code>][<code>-px</code>][<code>-pz</code>]<i>path</i><i>key</i></p>
<dl>
<dt>
<dd> Prints the value of a record.</dl>
<p> <code>kcforestmgr list </code>[<code>-onl</code>|<code>-otl</code>|<code>-onr</code>][<code>-des</code>][<code>-max </code><i>num</i>][<code>-rm</code>][<code>-sx</code>][<code>-pv</code>][<code>-px</code>]<i>path</i>[<i>key</i>]</p>
<dl>
<dt>
<dd> Prints keys of all records, separated by line feeds.</dl>
<p> <code>kcforestmgr clear </code>[<code>-onl</code>|<code>-otl</code>|<code>-onr</code>]<i>path</i></p>
<dl>
<dt>
<dd> Removes all records of a database.</dl>
<p> <code>kcforestmgr import </code>[<code>-onl</code>|<code>-otl</code>|<code>-onr</code>][<code>-sx</code>]<i>path</i>[<i>file</i>]</p>
<dl>
<dt>
<dd> Imports records from a TSV file.</dl>
<p> <code>kcforestmgr copy </code>[<code>-onl</code>|<code>-otl</code>|<code>-onr</code>]<i>path</i><i>file</i></p>
<dl>
<dt>
<dd> Copies the whole database.</dl>
<p> <code>kcforestmgr dump </code>[<code>-onl</code>|<code>-otl</code>|<code>-onr</code>]<i>path</i>[<i>file</i>]</p>
<dl>
<dt>
<dd> Dumps records into a snapshot file.</dl>
<p> <code>kcforestmgr load </code>[<code>-otr</code>][<code>-onl</code>|<code>-otl</code>|<code>-onr</code>]<i>path</i>[<i>file</i>]</p>
<dl>
<dt>
<dd> Loads records from a snapshot file.</dl>
<p> <code>kcforestmgr setbulk </code>[<code>-onl</code>|<code>-otl</code>|<code>-onr</code>]<i>path</i><i>key</i><i>value</i><code> &#8230;</code></p>
<dl>
<dt>
<dd> Store records at once.</dl>
<p> <code>kcforestmgr removebulk </code>[<code>-onl</code>|<code>-otl</code>|<code>-onr</code>][<code>-sx</code>]<i>path</i><i>key</i><code> &#8230;</code></p>
<dl>
<dt>
<dd> Remove records at once.</dl>
<p> <code>kcforestmgr getbulk </code>[<code>-onl</code>|<code>-otl</code>|<code>-onr</code>][<code>-sx</code>][<code>-px</code>]<i>path</i><i>key</i><code> &#8230;</code></p>
<dl>
<dt>
<dd> Retrieve records at once.</dl>
<p> <code>kcforestmgr check </code>[<code>-onl</code>|<code>-otl</code>|<code>-onr</code>]<i>path</i></p>
<dl>
<dt>
<dd> Checks consistency.</dl>
</dl>
<p> Options feature the following. </p>
<dl>
<dt>
<dd> <code>-otr</code> : opens the database with the truncation option.<br />
 <code>-onl</code> : opens the database with the no locking option.<br />
 <code>-otl</code> : opens the database with the try locking option.<br />
 <code>-onr</code> : opens the database with the no auto repair option.<br />
 <code>-tc</code> : tunes the database with the compression option.<br />
 <code>-bnum </code><i>num</i> : specifies the number of buckets of the hash table.<br />
 <code>-psiz </code><i>num</i> : specifies the size of each page.<br />
 <code>-rcd</code> : use the decimal comparator instead of the lexical one.<br />
 <code>-rcld</code> : use the lexical descending comparator instead of the ascending one.<br />
 <code>-rcdd</code> : use the decimal descending comparator instead of the lexical one.<br />
 <code>-st</code> : prints miscellaneous information.<br />
 <code>-add</code> : performs adding operation.<br />
 <code>-app</code> : performs appending operation.<br />
 <code>-rep</code> : performs replacing operation.<br />
 <code>-inci</code> : performs integer increment operation.<br />
 <code>-incd</code> : performs real number increment operation.<br />
 <code>-sx</code> : the input data is evaluated as a hexadecimal data string.<br />
 <code>-rm</code> : removes the record.<br />
 <code>-px</code> : the output data is converted into a hexadecimal data string.<br />
 <code>-pz</code> : does not append line feed at the end of the output.<br />
 <code>-des</code> : visits records in descending order.<br />
 <code>-max </code><i>num</i> : specifies the maximum number of shown records.<br />
 <code>-pv</code> : prints values of records also.
</dl>
<p> This command returns 0 on success, another on failure. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-kcforesttest/">kcforesttest</a></code>(1) </p>
<h2>Index</h2>
