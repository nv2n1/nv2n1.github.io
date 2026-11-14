---
title: "tchmgr(1)"
name: "tchmgr"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tchmgr/"
description: "tchmgr – the command line utility of the hash database API"
---

<h2 class="name">NAME</h2>
<p> tchmgr &#8211; the command line utility of the hash database API</p>
<h2>DESCRIPTION</h2>
<p> The command `<code>tchmgr</code>&#8216; is a utility for test and debugging of the hash database API and its applications. `<i>path</i>&#8216; specifies the path of a database file. `<i>bnum</i>&#8216; specifies the number of buckets. `<i>apow</i>&#8216; specifies the power of the alignment. `<i>fpow</i>&#8216; specifies the power of the free block pool. `<i>key</i>&#8216; specifies the key of a record. `<i>value</i>&#8216; specifies the value of a record. `<i>file</i>&#8216; specifies the input file. </p>
<dl>
<dt>
<dd>
 <code>tchmgr create </code>[<code>-tl</code>][<code>-td</code>|<code>-tb</code>|<code>-tt</code>|<code>-tx</code>]<i>path</i>[<i>bnum</i>[<i>apow</i>[<i>fpow</i>]]]</p>
<dl>
<dt>
<dd> Create a database file.</dl>
<p> <code>tchmgr inform </code>[<code>-nl</code>|<code>-nb</code>]<i>path</i></p>
<dl>
<dt>
<dd> Print miscellaneous information to the standard output.</dl>
<p> <code>tchmgr put </code>[<code>-nl</code>|<code>-nb</code>][<code>-sx</code>][<code>-dk</code>|<code>-dc</code>|<code>-dai</code>|<code>-dad</code>]<i>path</i><i>key</i><i>value</i></p>
<dl>
<dt>
<dd> Store a record.</dl>
<p> <code>tchmgr out </code>[<code>-nl</code>|<code>-nb</code>][<code>-sx</code>]<i>path</i><i>key</i></p>
<dl>
<dt>
<dd> Remove a record.</dl>
<p> <code>tchmgr get </code>[<code>-nl</code>|<code>-nb</code>][<code>-sx</code>][<code>-px</code>][<code>-pz</code>]<i>path</i><i>key</i></p>
<dl>
<dt>
<dd> Print the value of a record.</dl>
<p> <code>tchmgr list </code>[<code>-nl</code>|<code>-nb</code>][<code>-m </code><i>num</i>][<code>-pv</code>][<code>-px</code>][<code>-fm </code><i>str</i>]<i>path</i></p>
<dl>
<dt>
<dd> Print keys of all records, separated by line feeds.</dl>
<p> <code>tchmgr optimize </code>[<code>-tl</code>][<code>-td</code>|<code>-tb</code>|<code>-tt</code>|<code>-tx</code>][<code>-tz</code>][<code>-nl</code>|<code>-nb</code>][<code>-df</code>]<i>path</i>[<i>bnum</i>[<i>apow</i>[<i>fpow</i>]]]</p>
<dl>
<dt>
<dd> Optimize a database file.</dl>
<p> <code>tchmgr importtsv </code>[<code>-nl</code>|<code>-nb</code>][<code>-sc</code>]<i>path</i>[<i>file</i>]</p>
<dl>
<dt>
<dd> Store records of TSV in each line of a file.</dl>
<p> <code>tchmgr version</code></p>
<dl>
<dt>
<dd> Print the version information of Tokyo Cabinet.</dl>
</dl>
<p> Options feature the following. </p>
<dl>
<dt>
<dd> <code>-tl</code> : enable the option `HDBTLARGE&#8217;.<br />
 <code>-td</code> : enable the option `HDBTDEFLATE&#8217;.<br />
 <code>-tb</code> : enable the option `HDBTBZIP&#8217;.<br />
 <code>-tt</code> : enable the option `HDBTTCBS&#8217;.<br />
 <code>-tx</code> : enable the option `HDBTEXCODEC&#8217;.<br />
 <code>-nl</code> : enable the option `HDBNOLCK&#8217;.<br />
 <code>-nb</code> : enable the option `HDBLCKNB&#8217;.<br />
 <code>-sx</code> : the input data is evaluated as a hexadecimal data string.<br />
 <code>-dk</code> : use the function `tchdbputkeep&#8217; instead of `tchdbput&#8217;.<br />
 <code>-dc</code> : use the function `tchdbputcat&#8217; instead of `tchdbput&#8217;.<br />
 <code>-dai</code> : use the function `tchdbaddint&#8217; instead of `tchdbput&#8217;.<br />
 <code>-dad</code> : use the function `tchdbadddouble&#8217; instead of `tchdbput&#8217;.<br />
 <code>-px</code> : the output data is converted into a hexadecimal data string.<br />
 <code>-pz</code> : do not append line feed at the end of the output.<br />
 <code>-m </code><i>num</i> : specify the maximum number of the output.<br />
 <code>-pv</code> : print values of records also.<br />
 <code>-fm </code><i>str</i> : specify the prefix of keys.<br />
 <code>-tz</code> : enable the option `UINT8_MAX&#8217;.<br />
 <code>-df</code> : perform defragmentation only.<br />
 <code>-sc</code> : normalize keys as lower cases.
</dl>
<p> This command returns 0 on success, another on failure. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tchtest/">tchtest</a></code>(1), <code><a href="/docs/linux/man/1-tchmttest/">tchmttest</a></code>(1), <code><a href="/docs/linux/man/3-tchdb/">tchdb</a></code>(3), <code><a href="/docs/linux/man/3-tokyocabinet/">tokyocabinet</a></code>(3) </p>
<h2>Index</h2>
