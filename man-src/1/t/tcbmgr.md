---
title: "tcbmgr(1)"
name: "tcbmgr"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tcbmgr/"
description: "tcbmgr – the command line utility of the B+ tree database API"
---

<h2 class="name">NAME</h2>
<p> tcbmgr &#8211; the command line utility of the B+ tree database API</p>
<h2>DESCRIPTION</h2>
<p> The command `<code>tcbmgr</code>&#8216; is a utility for test and debugging of the B+ tree database API and its applications. `<i>path</i>&#8216; specifies the path of a database file. `<i>lmemb</i>&#8216; specifies the number of members in each leaf page. `<i>nmemb</i>&#8216; specifies the number of members in each non-leaf page. `<i>bnum</i>&#8216; specifies the number of buckets. `<i>apow</i>&#8216; specifies the power of the alignment. `<i>fpow</i>&#8216; specifies the power of the free block pool. `<i>key</i>&#8216; specifies the key of a record. `<i>value</i>&#8216; specifies the value of a record. `<i>file</i>&#8216; specifies the input file. </p>
<dl>
<dt>
<dd>
 <code>tcbmgr create </code>[<code>-cd</code>|<code>-ci</code>|<code>-cj</code>][<code>-tl</code>][<code>-td</code>|<code>-tb</code>|<code>-tt</code>|<code>-tx</code>]<i>path</i>[<i>lmemb</i>[<i>nmemb</i>[<i>bnum</i>[<i>apow</i>[<i>fpow</i>]]]]]</p>
<dl>
<dt>
<dd> Create a database file.</dl>
<p> <code>tcbmgr inform </code>[<code>-nl</code>|<code>-nb</code>]<i>path</i></p>
<dl>
<dt>
<dd> Print miscellaneous information to the standard output.</dl>
<p> <code>tcbmgr put </code>[<code>-cd</code>|<code>-ci</code>|<code>-cj</code>][<code>-nl</code>|<code>-nb</code>][<code>-sx</code>][<code>-dk</code>|<code>-dc</code>|<code>-dd</code>|<code>-db</code>|<code>-dai</code>|<code>-dad</code>]<i>path</i><i>key</i><i>value</i></p>
<dl>
<dt>
<dd> Store a record.</dl>
<p> <code>tcbmgr out </code>[<code>-cd</code>|<code>-ci</code>|<code>-cj</code>][<code>-nl</code>|<code>-nb</code>][<code>-sx</code>]<i>path</i><i>key</i></p>
<dl>
<dt>
<dd> Remove a record.</dl>
<p> <code>tcbmgr get </code>[<code>-cd</code>|<code>-ci</code>|<code>-cj</code>][<code>-nl</code>|<code>-nb</code>][<code>-sx</code>][<code>-px</code>][<code>-pz</code>]<i>path</i><i>key</i></p>
<dl>
<dt>
<dd> Print the value of a record.</dl>
<p> <code>tcbmgr list </code>[<code>-cd</code>|<code>-ci</code>|<code>-cj</code>][<code>-nl</code>|<code>-nb</code>][<code>-m </code><i>num</i>][<code>-bk</code>][<code>-pv</code>][<code>-px</code>][<code>-j </code><i>str</i>][<code>-rb </code><i>bkey</i><i>ekey</i>][<code>-fm </code><i>str</i>]<i>path</i></p>
<dl>
<dt>
<dd> Print keys of all records, separated by line feeds.</dl>
<p> <code>tcbmgr optimize </code>[<code>-cd</code>|<code>-ci</code>|<code>-cj</code>][<code>-tl</code>][<code>-td</code>|<code>-tb</code>|<code>-tt</code>|<code>-tx</code>][<code>-tz</code>][<code>-nl</code>|<code>-nb</code>][<code>-df</code>]<i>path</i>[<i>lmemb</i>[<i>nmemb</i>[<i>bnum</i>[<i>apow</i>[<i>fpow</i>]]]]]</p>
<dl>
<dt>
<dd> Optimize a database file.</dl>
<p> <code>tcbmgr importtsv </code>[<code>-nl</code>|<code>-nb</code>][<code>-sc</code>]<i>path</i>[<i>file</i>]</p>
<dl>
<dt>
<dd> Store records of TSV in each line of a file.</dl>
<p> <code>tcbmgr version</code></p>
<dl>
<dt>
<dd> Print the version information of Tokyo Cabinet.</dl>
</dl>
<p> Options feature the following. </p>
<dl>
<dt>
<dd> <code>-cd</code> : use the comparison function `tccmpdecimal&#8217;.<br />
 <code>-ci</code> : use the comparison function `tccmpint32&#8242;.<br />
 <code>-cj</code> : use the comparison function `tccmpint64&#8242;.<br />
 <code>-tl</code> : enable the option `BDBTLARGE&#8217;.<br />
 <code>-td</code> : enable the option `BDBTDEFLATE&#8217;.<br />
 <code>-tb</code> : enable the option `BDBTBZIP&#8217;.<br />
 <code>-tt</code> : enable the option `BDBTTCBS&#8217;.<br />
 <code>-tx</code> : enable the option `BDBTEXCODEC&#8217;.<br />
 <code>-nl</code> : enable the option `BDBNOLCK&#8217;.<br />
 <code>-nb</code> : enable the option `BDBLCKNB&#8217;.<br />
 <code>-sx</code> : the input data is evaluated as a hexadecimal data string.<br />
 <code>-dk</code> : use the function `tcbdbputkeep&#8217; instead of `tcbdbput&#8217;.<br />
 <code>-dc</code> : use the function `tcbdbputcat&#8217; instead of `tcbdbput&#8217;.<br />
 <code>-dd</code> : use the function `tcbdbputdup&#8217; instead of `tcbdbput&#8217;.<br />
 <code>-db</code> : use the function `tcbdbputdupback&#8217; instead of `tcbdbput&#8217;.<br />
 <code>-dai</code> : use the function `tcbdbaddint&#8217; instead of `tcbdbput&#8217;.<br />
 <code>-dad</code> : use the function `tcbdbadddouble&#8217; instead of `tcbdbput&#8217;.<br />
 <code>-px</code> : the output data is converted into a hexadecimal data string.<br />
 <code>-pz</code> : do not append line feed at the end of the output.<br />
 <code>-m </code><i>num</i> : specify the maximum number of the output.<br />
 <code>-bk</code> : perform backword scanning.<br />
 <code>-pv</code> : print values of records also.<br />
 <code>-j </code><i>str</i> : specify the key where the cursor jump to.<br />
 <code>-rb </code><i>bkey</i> <i>ekey</i> : specify the range of keys.<br />
 <code>-fm </code><i>str</i> : specify the prefix of keys.<br />
 <code>-tz</code> : enable the option `UINT8_MAX&#8217;.<br />
 <code>-df</code> : perform defragmentation only.<br />
 <code>-sc</code> : normalize keys as lower cases.
</dl>
<p> This command returns 0 on success, another on failure. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tcbtest/">tcbtest</a></code>(1), <code><a href="/docs/linux/man/1-tcbmttest/">tcbmttest</a></code>(1), <code><a href="/docs/linux/man/3-tcbdb/">tcbdb</a></code>(3), <code><a href="/docs/linux/man/3-tokyocabinet/">tokyocabinet</a></code>(3) </p>
<h2>Index</h2>
