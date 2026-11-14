---
title: "tchmttest(1)"
name: "tchmttest"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tchmttest/"
description: "tchmttest – test cases of the hash database API"
---

<h2 class="name">NAME</h2>
<p> tchmttest &#8211; test cases of the hash database API</p>
<h2>DESCRIPTION</h2>
<p> The command `<code>tchmttest</code>&#8216; is a utility for facility test under multi-thread situation. This command is used in the following format. `<i>path</i>&#8216; specifies the path of a database file. `<i>tnum</i>&#8216; specifies the number of running threads. `<i>rnum</i>&#8216; specifies the number of iterations. `<i>bnum</i>&#8216; specifies the number of buckets. `<i>apow</i>&#8216; specifies the power of the alignment. `<i>fpow</i>&#8216; specifies the power of the free block pool. </p>
<dl>
<dt>
<dd>
 <code>tchmttest write </code>[<code>-tl</code>][<code>-td</code>|<code>-tb</code>|<code>-tt</code>|<code>-tx</code>][<code>-rc </code><i>num</i>][<code>-xm </code><i>num</i>][<code>-df </code><i>num</i>][<code>-nl</code>|<code>-nb</code>][<code>-as</code>][<code>-rnd</code>]<i>path</i><i>tnum</i><i>rnum</i>[<i>bnum</i>[<i>apow</i>[<i>fpow</i>]]]</p>
<dl>
<dt>
<dd> Store records with keys of 8 bytes. They change as `00000001&#8242;, `00000002&#8217;&#8230;</dl>
<p> <code>tchmttest read </code>[<code>-rc </code><i>num</i>][<code>-xm </code><i>num</i>][<code>-df </code><i>num</i>][<code>-nl</code>|<code>-nb</code>][<code>-wb</code>][<code>-rnd</code>]<i>path</i><i>tnum</i></p>
<dl>
<dt>
<dd> Retrieve all records of the database above.</dl>
<p> <code>tchmttest remove </code>[<code>-rc </code><i>num</i>][<code>-xm </code><i>num</i>][<code>-df </code><i>num</i>][<code>-nl</code>|<code>-nb</code>][<code>-rnd</code>]<i>path</i><i>tnum</i></p>
<dl>
<dt>
<dd> Remove all records of the database above.</dl>
<p> <code>tchmttest wicked </code>[<code>-tl</code>][<code>-td</code>|<code>-tb</code>|<code>-tt</code>|<code>-tx</code>][<code>-nl</code>|<code>-nb</code>][<code>-nc</code>]<i>path</i><i>tnum</i><i>rnum</i></p>
<dl>
<dt>
<dd> Perform updating operations selected at random.</dl>
<p> <code>tchmttest typical </code>[<code>-tl</code>][<code>-td</code>|<code>-tb</code>|<code>-tt</code>|<code>-tx</code>][<code>-rc </code><i>num</i>][<code>-xm </code><i>num</i>][<code>-df </code><i>num</i>][<code>-nl</code>|<code>-nb</code>][<code>-nc</code>][<code>-rr </code><i>num</i>]<i>path</i><i>tnum</i><i>rnum</i>[<i>bnum</i>[<i>apow</i>[<i>fpow</i>]]</p>
<dl>
<dt>
<dd> Perform typical operations selected at random.</dl>
<p> <code>tchmttest race </code>[<code>-tl</code>][<code>-td</code>|<code>-tb</code>|<code>-tt</code>|<code>-tx</code>][<code>-xm </code><i>num</i>][<code>-df </code><i>num</i>][<code>-nl</code>|<code>-nb</code>]<i>path</i><i>tnum</i><i>rnum</i>[<i>bnum</i>[<i>apow</i>[<i>fpow</i>]]</p>
<dl>
<dt>
<dd> Perform race condition test.</dl>
</dl>
<p> Options feature the following. </p>
<dl>
<dt>
<dd> <code>-tl</code> : enable the option `HDBTLARGE&#8217;.<br />
 <code>-td</code> : enable the option `HDBTDEFLATE&#8217;.<br />
 <code>-tb</code> : enable the option `HDBTBZIP&#8217;.<br />
 <code>-tt</code> : enable the option `HDBTTCBS&#8217;.<br />
 <code>-tx</code> : enable the option `HDBTEXCODEC&#8217;.<br />
 <code>-rc </code><i>num</i> : specify the number of cached records.<br />
 <code>-xm </code><i>num</i> : specify the size of the extra mapped memory.<br />
 <code>-df </code><i>num</i> : specify the unit step number of auto defragmentation.<br />
 <code>-nl</code> : enable the option `HDBNOLCK&#8217;.<br />
 <code>-nb</code> : enable the option `HDBLCKNB&#8217;.<br />
 <code>-as</code> : use the function `tchdbputasync&#8217; instead of `tchdbput&#8217;.<br />
 <code>-rnd</code> : select keys at random.<br />
 <code>-wb</code> : use the function `tchdbget3&#8242; instead of `tchdbget&#8217;.<br />
 <code>-nc</code> : omit the comparison test.<br />
 <code>-rr </code><i>num</i> : specify the ratio of reading operation by percentage.
</dl>
<p> This command returns 0 on success, another on failure. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tchtest/">tchtest</a></code>(1), <code><a href="/docs/linux/man/1-tchmgr/">tchmgr</a></code>(1), <code><a href="/docs/linux/man/3-tchdb/">tchdb</a></code>(3), <code><a href="/docs/linux/man/3-tokyocabinet/">tokyocabinet</a></code>(3) </p>
<h2>Index</h2>
