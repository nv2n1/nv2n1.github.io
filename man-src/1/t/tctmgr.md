---
title: "tctmgr(1)"
name: "tctmgr"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tctmgr/"
description: "tctmgr – the command line utility of the table database API"
---

<h2 class="name">NAME</h2>
<p> tctmgr &#8211; the command line utility of the table database API</p>
<h2>DESCRIPTION</h2>
<p> The command `<code>tctmgr</code>&#8216; is a utility for test and debugging of the table database API and its applications. `<i>path</i>&#8216; specifies the path of a database file. `<i>bnum</i>&#8216; specifies the number of buckets. `<i>apow</i>&#8216; specifies the power of the alignment. `<i>fpow</i>&#8216; specifies the power of the free block pool. `<i>pkey</i>&#8216; specifies the primary key of a record. `<i>cols</i>&#8216; specifies the names and the values of a record alternately. `<i>name</i>&#8216; specifies the name of a column. `<i>op</i>&#8216; specifies an operator. `<i>expr</i>&#8216; specifies the condition expression. `<i>file</i>&#8216; specifies the input file. </p>
<dl>
<dt>
<dd>
 <code>tctmgr create </code>[<code>-tl</code>][<code>-td</code>|<code>-tb</code>|<code>-tt</code>|<code>-tx</code>]<i>path</i>[<i>bnum</i>[<i>apow</i>[<i>fpow</i>]]]</p>
<dl>
<dt>
<dd> Create a database file.</dl>
<p> <code>tctmgr inform </code>[<code>-nl</code>|<code>-nb</code>]<i>path</i></p>
<dl>
<dt>
<dd> Print miscellaneous information to the standard output.</dl>
<p> <code>tctmgr put </code>[<code>-nl</code>|<code>-nb</code>][<code>-sx</code>][<code>-dk</code>|<code>-dc</code>|<code>-dai</code>|<code>-dad</code>]<i>path</i><i>pkey</i>[<i>cols</i><code> &#8230;</code>]</p>
<dl>
<dt>
<dd> Store a record.</dl>
<p> <code>tctmgr out </code>[<code>-nl</code>|<code>-nb</code>][<code>-sx</code>]<i>path</i><i>pkey</i></p>
<dl>
<dt>
<dd> Remove a record.</dl>
<p> <code>tctmgr get </code>[<code>-nl</code>|<code>-nb</code>][<code>-sx</code>][<code>-px</code>][<code>-pz</code>]<i>path</i><i>pkey</i></p>
<dl>
<dt>
<dd> Print the value of a record.</dl>
<p> <code>tctmgr list </code>[<code>-nl</code>|<code>-nb</code>][<code>-m </code><i>num</i>][<code>-pv</code>][<code>-px</code>][<code>-fm </code><i>str</i>]<i>path</i></p>
<dl>
<dt>
<dd> Print the primary keys of all records, separated by line feeds.</dl>
<p> <code>tctmgr search </code>[<code>-nl</code>|<code>-nb</code>][<code>-ord </code><i>name</i><i>type</i>][<code>-m </code><i>num</i>][<code>-sk </code><i>num</i>][<code>-kw</code>][<code>-pv</code>][<code>-px</code>][<code>-ph</code>][<code>-bt </code><i>num</i>][<code>-rm</code>][<code>-ms </code><i>type</i>]<i>path</i>[<i>name</i><i>op</i><i>expr</i><code> &#8230;</code>]</p>
<dl>
<dt>
<dd> Print records matching conditions, separated by line feeds.</dl>
<p> <code>tctmgr optimize </code>[<code>-tl</code>][<code>-td</code>|<code>-tb</code>|<code>-tt</code>|<code>-tx</code>][<code>-tz</code>][<code>-nl</code>|<code>-nb</code>][<code>-df</code>]<i>path</i>[<i>bnum</i>[<i>apow</i>[<i>fpow</i>]]]</p>
<dl>
<dt>
<dd> Optimize a database file.</dl>
<p> <code>tctmgr setindex </code>[<code>-nl</code>|<code>-nb</code>][<code>-it </code><i>type</i>]<i>path</i><i>name</i></p>
<dl>
<dt>
<dd> Set the index of a column.</dl>
<p> <code>tctmgr importtsv </code>[<code>-nl</code>|<code>-nb</code>][<code>-sc</code>]<i>path</i>[<i>file</i>]</p>
<dl>
<dt>
<dd> Store records of TSV in each line of a file.</dl>
<p> <code>tctmgr version</code></p>
<dl>
<dt>
<dd> Print the version information of Tokyo Cabinet.</dl>
</dl>
<p> Options feature the following. </p>
<dl>
<dt>
<dd> <code>-tl</code> : enable the option `TDBTLARGE&#8217;.<br />
 <code>-td</code> : enable the option `TDBTDEFLATE&#8217;.<br />
 <code>-tb</code> : enable the option `TDBTBZIP&#8217;.<br />
 <code>-tt</code> : enable the option `TDBTTCBS&#8217;.<br />
 <code>-tx</code> : enable the option `TDBTEXCODEC&#8217;.<br />
 <code>-nl</code> : enable the option `TDBNOLCK&#8217;.<br />
 <code>-nb</code> : enable the option `TDBLCKNB&#8217;.<br />
 <code>-sx</code> : the input data is evaluated as a hexadecimal data string.<br />
 <code>-dk</code> : use the function `tctdbputkeep&#8217; instead of `tctdbput&#8217;.<br />
 <code>-dc</code> : use the function `tctdbputcat&#8217; instead of `tctdbput&#8217;.<br />
 <code>-dai</code> : use the function `tctdbaddint&#8217; instead of `tctdbput&#8217;.<br />
 <code>-dad</code> : use the function `tctdbadddouble&#8217; instead of `tctdbput&#8217;.<br />
 <code>-px</code> : the output data is converted into a hexadecimal data string.<br />
 <code>-pz</code> : do not append line feed at the end of the output.<br />
 <code>-m </code><i>num</i> : specify the maximum number of the output.<br />
 <code>-pv</code> : print values of records also.<br />
 <code>-fm </code><i>str</i> : specify the prefix of keys.<br />
 <code>-ord </code><i>name</i> <i>type</i> : specify the order of the result.<br />
 <code>-sk </code><i>num</i> : specify the number of skipped records.<br />
 <code>-kw</code> : print KWIC string.<br />
 <code>-ph</code> : print hint information also.<br />
 <code>-bt</code> : specify the number of benchmark tests.<br />
 <code>-rm</code> : remove every record in the result.<br />
 <code>-ms </code><i>type</i> : specify the set operation of meta search.<br />
 <code>-tz</code> : enable the option `UINT8_MAX&#8217;.<br />
 <code>-df</code> : perform defragmentation only.<br />
 <code>-it </code><i>type</i> : specify the index type among &quot;lexical&quot;, &quot;decimal&quot;, &quot;token&quot;, &quot;qgram&quot;, and &quot;void&quot;.<br />
 <code>-sc</code> : normalize keys as lower cases.
</dl>
<p> The operator of the `search&#8217; subcommand is one of &quot;STREQ&quot;, &quot;STRINC&quot;, &quot;STRBW&quot;, &quot;STREW&quot;, &quot;STRAND&quot;, &quot;STROR&quot;, &quot;STROREQ&quot;, &quot;STRRX&quot;, &quot;NUMEQ&quot;, &quot;NUMGT&quot;, &quot;NUMGE&quot;, &quot;NUMLT&quot;, &quot;NUMLE&quot;, &quot;NUMBT&quot;, &quot;NUMOREQ&quot;, &quot;FTSPH&quot;, &quot;FTSAND&quot;, &quot;FTSOR&quot;, and &quot;FTSEX&quot;. If &quot;~&quot; preposes each operator, the logical meaning is reversed. If &quot;+&quot; preposes each operator, no index is used for the operator. The type of the `-ord&#8217; option is one of &quot;STRASC&quot;, &quot;STRDESC&quot;, &quot;NUMASC&quot;, and &quot;NUMDESC&quot;. The type of the `-ms&#8217; option is one of &quot;UNION&quot;, &quot;ISECT&quot;, and &quot;DIFF&quot;. This command returns 0 on success, another on failure. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tcttest/">tcttest</a></code>(1), <code><a href="/docs/linux/man/1-tctmttest/">tctmttest</a></code>(1), <code><a href="/docs/linux/man/3-tctdb/">tctdb</a></code>(3), <code><a href="/docs/linux/man/3-tokyocabinet/">tokyocabinet</a></code>(3) </p>
<h2>Index</h2>
