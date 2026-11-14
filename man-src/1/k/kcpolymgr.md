---
title: "kcpolymgr(1)"
name: "kcpolymgr"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kcpolymgr/"
description: "kcpolymgr – command line interface to manage the polymorphic database"
---

<h2 class="name">NAME</h2>
<p> kcpolymgr &#8211; command line interface to manage the polymorphic database</p>
<h2>DESCRIPTION</h2>
<p> The command `<code>kcpolymgr</code>&#8216; is a utility for test and debugging of the polymorphic database and its applications. `<i>path</i>&#8216; specifies the path of a database file. `<i>key</i>&#8216; specifies the key of a record. `<i>value</i>&#8216; specifies the value of a record. `<i>file</i>&#8216; specifies the input/output file. `<i>src</i>&#8216; specifies other database files. </p>
<dl>
<dt>
<dd>
 <code>kcpolymgr create </code>[<code>-otr</code>][<code>-onl</code>|<code>-otl</code>|<code>-onr</code>]<i>path</i></p>
<dl>
<dt>
<dd> Creates a database file.</dl>
<p> <code>kcpolymgr inform </code>[<code>-onl</code>|<code>-otl</code>|<code>-onr</code>][<code>-st</code>]<i>path</i></p>
<dl>
<dt>
<dd> Prints status information.</dl>
<p> <code>kcpolymgr set </code>[<code>-onl</code>|<code>-otl</code>|<code>-onr</code>][<code>-add</code>|<code>-app</code>|<code>-rep</code>|<code>-inci</code>|<code>-incd</code>][<code>-sx</code>]<i>path</i><i>key</i><i>value</i></p>
<dl>
<dt>
<dd> Stores a record.</dl>
<p> <code>kcpolymgr remove </code>[<code>-onl</code>|<code>-otl</code>|<code>-onr</code>][<code>-sx</code>]<i>path</i><i>key</i></p>
<dl>
<dt>
<dd> Removes a record.</dl>
<p> <code>kcpolymgr get </code>[<code>-onl</code>|<code>-otl</code>|<code>-onr</code>][<code>-rm</code>][<code>-sx</code>][<code>-px</code>][<code>-pz</code>]<i>path</i><i>key</i></p>
<dl>
<dt>
<dd> Prints the value of a record.</dl>
<p> <code>kcpolymgr list </code>[<code>-onl</code>|<code>-otl</code>|<code>-onr</code>][<code>-mp</code>|<code>-mr</code>|<code>-ms</code>][<code>-des</code>][<code>-max </code><i>num</i>][<code>-rm</code>][<code>-sx</code>][<code>-pv</code>][<code>-px</code>]<i>path</i>[<i>key</i>]</p>
<dl>
<dt>
<dd> Prints keys of all records, separated by line feeds.</dl>
<p> <code>kcpolymgr clear </code>[<code>-onl</code>|<code>-otl</code>|<code>-onr</code>]<i>path</i></p>
<dl>
<dt>
<dd> Removes all records of a database.</dl>
<p> <code>kcpolymgr import </code>[<code>-onl</code>|<code>-otl</code>|<code>-onr</code>][<code>-sx</code>]<i>path</i>[<i>file</i>]</p>
<dl>
<dt>
<dd> Imports records from a TSV file.</dl>
<p> <code>kcpolymgr copy </code>[<code>-onl</code>|<code>-otl</code>|<code>-onr</code>]<i>path</i><i>file</i></p>
<dl>
<dt>
<dd> Copies the whole database.</dl>
<p> <code>kcpolymgr dump </code>[<code>-onl</code>|<code>-otl</code>|<code>-onr</code>]<i>path</i>[<i>file</i>]</p>
<dl>
<dt>
<dd> Dumps records into a snapshot file.</dl>
<p> <code>kcpolymgr load </code>[<code>-otr</code>][<code>-onl</code>|<code>-otl</code>|<code>-onr</code>]<i>path</i>[<i>file</i>]</p>
<dl>
<dt>
<dd> Loads records from a snapshot file.</dl>
<p> <code>kcpolymgr merge </code>[<code>-onl</code>|<code>-otl</code>|<code>-onr</code>][<code>-add</code>|<code>-app</code>|<code>-rep</code>]<i>path</i><i>src</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Merge records from other databases.</dl>
<p> <code>kcpolymgr setbulk </code>[<code>-onl</code>|<code>-otl</code>|<code>-onr</code>]<i>path</i><i>key</i><i>value</i><code> &#8230;</code></p>
<dl>
<dt>
<dd> Store records at once.</dl>
<p> <code>kcpolymgr removebulk </code>[<code>-onl</code>|<code>-otl</code>|<code>-onr</code>][<code>-sx</code>]<i>path</i><i>key</i><code> &#8230;</code></p>
<dl>
<dt>
<dd> Remove records at once.</dl>
<p> <code>kcpolymgr getbulk </code>[<code>-onl</code>|<code>-otl</code>|<code>-onr</code>][<code>-sx</code>][<code>-px</code>]<i>path</i><i>key</i><code> &#8230;</code></p>
<dl>
<dt>
<dd> Retrieve records at once.</dl>
<p> <code>kcpolymgr check </code>[<code>-onl</code>|<code>-otl</code>|<code>-onr</code>]<i>path</i></p>
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
 <code>-st</code> : prints miscellaneous information.<br />
 <code>-add</code> : performs adding operation.<br />
 <code>-app</code> : performs appending operation.<br />
 <code>-rep</code> : performs replacing operation.<br />
 <code>-inci</code> : performs integer increment operation.<br />
 <code>-incd</code> : performs real number increment operation.<br />
 <code>-sx</code> : the input data is evaluated as a hexadecimal data string.<br />
 <code>-rm</code> : removes the record.<br />
 <code>-px</code> : the output data is converted into a hexadecimal data string.<br />
 <code>-pz</code> : performs not append line feed at the end of the output.<br />
 <code>-mp</code> : performs prefix matching instead of usual scan.<br />
 <code>-mr</code> : performs regular expression matching instead of usual scan.<br />
 <code>-ms</code> : performs similar matching instead of usual scan.<br />
 <code>-des</code> : visits records in descending order.<br />
 <code>-max </code><i>num</i> : specifies the maximum number of shown records.<br />
 <code>-pv</code> : prints values of records also.
</dl>
<p> This command returns 0 on success, another on failure. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-kcpolytest/">kcpolytest</a></code>(1), <code><a href="/docs/linux/man/1-kclangctest/">kclangctest</a></code>(1) </p>
<h2>Index</h2>
