---
title: "tctmttest(1)"
name: "tctmttest"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tctmttest/"
description: "tctmttest – test cases of the table database API"
---

<h2 class="name">NAME</h2>
<p> tctmttest &#8211; test cases of the table database API</p>
<h2>DESCRIPTION</h2>
<p> The command `<code>tctmttest</code>&#8216; is a utility for facility test under multi-thread situation. This command is used in the following format. `<i>path</i>&#8216; specifies the path of a database file. `<i>tnum</i>&#8216; specifies the number of running threads. `<i>rnum</i>&#8216; specifies the number of iterations. `<i>bnum</i>&#8216; specifies the number of buckets. `<i>apow</i>&#8216; specifies the power of the alignment. `<i>fpow</i>&#8216; specifies the power of the free block pool. </p>
<dl>
<dt>
<dd>
 <code>tctmttest write </code>[<code>-tl</code>][<code>-td</code>|<code>-tb</code>|<code>-tt</code>|<code>-tx</code>][<code>-rc </code><i>num</i>][<code>-lc </code><i>num</i>][<code>-nc </code><i>num</i>][<code>-xm </code><i>num</i>][<code>-df </code><i>num</i>][<code>-ip</code>][<code>-is</code>][<code>-in</code>][<code>-it</code>][<code>-if</code>][<code>-ix</code>][<code>-nl</code>|<code>-nb</code>][<code>-rnd</code>]<i>path</i><i>tnum</i><i>rnum</i>[<i>bnum</i>[<i>apow</i>[<i>fpow</i>]]]</p>
<dl>
<dt>
<dd> Store records with columns &quot;str&quot;, &quot;num&quot;, &quot;type&quot;, and &quot;flag&quot;.</dl>
<p> <code>tctmttest read </code>[<code>-rc </code><i>num</i>][<code>-lc </code><i>num</i>][<code>-nc </code><i>num</i>][<code>-xm </code><i>num</i>][<code>-df </code><i>num</i>][<code>-nl</code>|<code>-nb</code>][<code>-rnd</code>]<i>path</i><i>tnum</i></p>
<dl>
<dt>
<dd> Retrieve all records of the database above.</dl>
<p> <code>tctmttest remove </code>[<code>-rc </code><i>num</i>][<code>-lc </code><i>num</i>][<code>-nc </code><i>num</i>][<code>-xm </code><i>num</i>][<code>-df </code><i>num</i>][<code>-nl</code>|<code>-nb</code>][<code>-rnd</code>]<i>path</i><i>tnum</i></p>
<dl>
<dt>
<dd> Remove all records of the database above.</dl>
<p> <code>tctmttest wicked </code>[<code>-tl</code>][<code>-td</code>|<code>-tb</code>|<code>-tt</code>|<code>-tx</code>][<code>-nl</code>|<code>-nb</code>]<i>path</i><i>tnum</i><i>rnum</i></p>
<dl>
<dt>
<dd> Perform updating operations selected at random.</dl>
<p> <code>tctmttest typical </code>[<code>-tl</code>][<code>-td</code>|<code>-tb</code>|<code>-tt</code>|<code>-tx</code>][<code>-rc </code><i>num</i>][<code>-lc </code><i>num</i>][<code>-nc </code><i>num</i>][<code>-xm </code><i>num</i>][<code>-df </code><i>num</i>][<code>-nl</code>|<code>-nb</code>][<code>-rr </code><i>num</i>]<i>path</i><i>tnum</i><i>rnum</i>[<i>bnum</i>[<i>apow</i>[<i>fpow</i>]]</p>
<dl>
<dt>
<dd> Perform typical operations selected at random.</dl>
</dl>
<p> Options feature the following. </p>
<dl>
<dt>
<dd> <code>-tl</code> : enable the option `TDBTLARGE&#8217;.<br />
 <code>-td</code> : enable the option `TDBTDEFLATE&#8217;.<br />
 <code>-tb</code> : enable the option `TDBTBZIP&#8217;.<br />
 <code>-tt</code> : enable the option `TDBTTCBS&#8217;.<br />
 <code>-tx</code> : enable the option `TDBTEXCODEC&#8217;.<br />
 <code>-rc </code><i>num</i> : specify the number of cached records.<br />
 <code>-lc </code><i>num</i> : specify the number of cached leaf pages.<br />
 <code>-nc </code><i>num</i> : specify the number of cached non-leaf pages.<br />
 <code>-xm </code><i>num</i> : specify the size of the extra mapped memory.<br />
 <code>-df </code><i>num</i> : specify the unit step number of auto defragmentation.<br />
 <code>-ip</code> : create the number index for the primary key.<br />
 <code>-is</code> : create the string index for the column &quot;str&quot;.<br />
 <code>-in</code> : create the number index for the column &quot;num&quot;.<br />
 <code>-it</code> : create the string index for the column &quot;type&quot;.<br />
 <code>-if</code> : create the token inverted index for the column &quot;flag&quot;.<br />
 <code>-ix</code> : create the q-gram inverted index for the column &quot;text&quot;.<br />
 <code>-nl</code> : enable the option `TDBNOLCK&#8217;.<br />
 <code>-nb</code> : enable the option `TDBLCKNB&#8217;.<br />
 <code>-rnd</code> : select keys at random.<br />
 <code>-nc</code> : omit the comparison test.<br />
 <code>-rr </code><i>num</i> : specify the ratio of reading operation by percentage.
</dl>
<p> This command returns 0 on success, another on failure. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tcttest/">tcttest</a></code>(1), <code><a href="/docs/linux/man/1-tctmgr/">tctmgr</a></code>(1), <code><a href="/docs/linux/man/3-tctdb/">tctdb</a></code>(3), <code><a href="/docs/linux/man/3-tokyocabinet/">tokyocabinet</a></code>(3) </p>
<h2>Index</h2>
