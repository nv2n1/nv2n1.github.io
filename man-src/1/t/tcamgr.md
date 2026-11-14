---
title: "tcamgr(1)"
name: "tcamgr"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tcamgr/"
description: "tcamgr – the command line utility of the abstract database API"
---

<h2 class="name">NAME</h2>
<p> tcamgr &#8211; the command line utility of the abstract database API</p>
<h2>DESCRIPTION</h2>
<p> The command `<code>tcamgr</code>&#8216; is a utility for test and debugging of the abstract database API and its applications. `<i>name</i>&#8216; specifies the name of a database. `<i>key</i>&#8216; specifies the key of a record. `<i>value</i>&#8216; specifies the value of a record. `<i>params</i>&#8216; specifies the tuning parameters. `<i>func</i>&#8216; specifies the name of a function. `<i>arg</i>&#8216; specifies the arguments of the function. `<i>dest</i>&#8216; specifies the path of the destination file. </p>
<dl>
<dt>
<dd>
 <code>tcamgr create </code><i>name</i></p>
<dl>
<dt>
<dd> Create a database file.</dl>
<p> <code>tcamgr inform </code><i>name</i></p>
<dl>
<dt>
<dd> Print miscellaneous information to the standard output.</dl>
<p> <code>tcamgr put </code>[<code>-sx</code>][<code>-sep </code><i>chr</i>][<code>-dk</code>|<code>-dc</code>|<code>-dai</code>|<code>-dad</code>]<i>name</i><i>key</i><i>value</i></p>
<dl>
<dt>
<dd> Store a record.</dl>
<p> <code>tcamgr out </code>[<code>-sx</code>][<code>-sep </code><i>chr</i>]<i>name</i><i>key</i></p>
<dl>
<dt>
<dd> Remove a record.</dl>
<p> <code>tcamgr get </code>[<code>-sx</code>][<code>-sep </code><i>chr</i>][<code>-px</code>][<code>-pz</code>]<i>name</i><i>key</i></p>
<dl>
<dt>
<dd> Print the value of a record.</dl>
<p> <code>tcamgr list </code>[<code>-sep </code><i>chr</i>][<code>-m </code><i>num</i>][<code>-pv</code>][<code>-px</code>][<code>-fm </code><i>str</i>]<i>name</i></p>
<dl>
<dt>
<dd> Print keys of all records, separated by line feeds.</dl>
<p> <code>tcamgr optimize </code><i>name</i><i>params</i></p>
<dl>
<dt>
<dd> Optimize a database file.</dl>
<p> <code>tcamgr misc </code>[<code>-sx</code>][<code>-sep </code><i>chr</i>][<code>-px</code>]<i>name</i><i>func</i>[<i>arg</i><code>&#8230;</code>]</p>
<dl>
<dt>
<dd> Call a versatile function for miscellaneous operations.</dl>
<p> <code>tcamgr map </code>[<code>-fm </code><i>str</i>]<i>name</i><i>dest</i></p>
<dl>
<dt>
<dd> Map records into another B+ tree database.</dl>
<p> <code>tcamgr version</code></p>
<dl>
<dt>
<dd> Print the version information of Tokyo Cabinet.</dl>
</dl>
<p> Options feature the following. </p>
<dl>
<dt>
<dd> <code>-sx</code> : the input data is evaluated as a hexadecimal data string.<br />
 <code>-sep </code><i>chr</i> : specify the separator of the input data.<br />
 <code>-dk</code> : use the function `tcadbputkeep&#8217; instead of `tcadbput&#8217;.<br />
 <code>-dc</code> : use the function `tcadbputcat&#8217; instead of `tcadbput&#8217;.<br />
 <code>-dai</code> : use the function `tcadbaddint&#8217; instead of `tcadbput&#8217;.<br />
 <code>-dad</code> : use the function `tcadbadddouble&#8217; instead of `tcadbput&#8217;.<br />
 <code>-px</code> : the output data is converted into a hexadecimal data string.<br />
 <code>-pz</code> : do not append line feed at the end of the output.<br />
 <code>-m </code><i>num</i> : specify the maximum number of the output.<br />
 <code>-pv</code> : print values of records also.<br />
 <code>-fm </code><i>str</i> : specify the prefix of keys.
</dl>
<p> This command returns 0 on success, another on failure. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tcatest/">tcatest</a></code>(1), <code><a href="/docs/linux/man/1-tcamttest/">tcamttest</a></code>(1), <code><a href="/docs/linux/man/3-tcadb/">tcadb</a></code>(3), <code><a href="/docs/linux/man/3-tokyocabinet/">tokyocabinet</a></code>(3) </p>
<h2>Index</h2>
