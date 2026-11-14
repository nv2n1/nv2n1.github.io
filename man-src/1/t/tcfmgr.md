---
title: "tcfmgr(1)"
name: "tcfmgr"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tcfmgr/"
description: "tcfmgr – the command line utility of the fixed-length database API"
---

<h2 class="name">NAME</h2>
<p> tcfmgr &#8211; the command line utility of the fixed-length database API</p>
<h2>DESCRIPTION</h2>
<p> The command `<code>tcfmgr</code>&#8216; is a utility for test and debugging of the fixed-length database API and its applications. `<i>path</i>&#8216; specifies the path of a database file. `<i>width</i>&#8216; specifies the width of the value of each record. `<i>limsiz</i>&#8216; specifies the limit size of the database file. `<i>key</i>&#8216; specifies the key of a record. `<i>value</i>&#8216; specifies the value of a record. `<i>file</i>&#8216; specifies the input file. </p>
<dl>
<dt>
<dd>
 <code>tcfmgr create </code><i>path</i>[<i>width</i>[<i>limsiz</i>]]</p>
<dl>
<dt>
<dd> Create a database file.</dl>
<p> <code>tcfmgr inform </code>[<code>-nl</code>|<code>-nb</code>]<i>path</i></p>
<dl>
<dt>
<dd> Print miscellaneous information to the standard output.</dl>
<p> <code>tcfmgr put </code>[<code>-nl</code>|<code>-nb</code>][<code>-sx</code>][<code>-dk</code>|<code>-dc</code>|<code>-dai</code>|<code>-dad</code>]<i>path</i><i>key</i><i>value</i></p>
<dl>
<dt>
<dd> Store a record.</dl>
<p> <code>tcfmgr out </code>[<code>-nl</code>|<code>-nb</code>][<code>-sx</code>]<i>path</i><i>key</i></p>
<dl>
<dt>
<dd> Remove a record.</dl>
<p> <code>tcfmgr get </code>[<code>-nl</code>|<code>-nb</code>][<code>-sx</code>][<code>-px</code>][<code>-pz</code>]<i>path</i><i>key</i></p>
<dl>
<dt>
<dd> Print the value of a record.</dl>
<p> <code>tcfmgr list </code>[<code>-nl</code>|<code>-nb</code>][<code>-m </code><i>num</i>][<code>-pv</code>][<code>-px</code>][<code>-rb </code><i>lkey</i><i>ukey</i>][<code>-ri </code><i>str</i>]<i>path</i></p>
<dl>
<dt>
<dd> Print keys of all records, separated by line feeds.</dl>
<p> <code>tcfmgr optimize </code>[<code>-nl</code>|<code>-nb</code>]<i>path</i>[<i>width</i>[<i>limsiz</i>]]</p>
<dl>
<dt>
<dd> Optimize a database file.</dl>
<p> <code>tcfmgr importtsv </code>[<code>-nl</code>|<code>-nb</code>][<code>-sc</code>]<i>path</i>[<i>file</i>]</p>
<dl>
<dt>
<dd> Store records of TSV in each line of a file.</dl>
<p> <code>tcfmgr version</code></p>
<dl>
<dt>
<dd> Print the version information of Tokyo Cabinet.</dl>
</dl>
<p> Options feature the following. </p>
<dl>
<dt>
<dd> <code>-nl</code> : enable the option `FDBNOLCK&#8217;.<br />
 <code>-nb</code> : enable the option `FDBLCKNB&#8217;.<br />
 <code>-sx</code> : the input data is evaluated as a hexadecimal data string.<br />
 <code>-dk</code> : use the function `tcfdbputkeep&#8217; instead of `tcfdbput&#8217;.<br />
 <code>-dc</code> : use the function `tcfdbputcat&#8217; instead of `tcfdbput&#8217;.<br />
 <code>-dai</code> : use the function `tcfdbaddint&#8217; instead of `tcfdbput&#8217;.<br />
 <code>-dad</code> : use the function `tcfdbadddouble&#8217; instead of `tcfdbput&#8217;.<br />
 <code>-px</code> : the output data is converted into a hexadecimal data string.<br />
 <code>-pz</code> : do not append line feed at the end of the output.<br />
 <code>-m </code><i>num</i> : specify the maximum number of the output.<br />
 <code>-pv</code> : print values of records also.<br />
 <code>-rb </code><i>lkey</i> <i>ukey</i> : specify the range of keys.<br />
 <code>-ri </code><i>str</i> : specify the interval notation of keys.<br />
 <code>-sc</code> : normalize keys as lower cases.
</dl>
<p> This command returns 0 on success, another on failure. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tcftest/">tcftest</a></code>(1), <code><a href="/docs/linux/man/1-tcfmttest/">tcfmttest</a></code>(1), <code><a href="/docs/linux/man/3-tcfdb/">tcfdb</a></code>(3), <code><a href="/docs/linux/man/3-tokyocabinet/">tokyocabinet</a></code>(3) </p>
<h2>Index</h2>
