---
title: "tchtest(1)"
name: "tchtest"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tchtest/"
description: "tchtest – test cases of the hash database API"
---

<h2 class="name">NAME</h2>
<p> tchtest &#8211; test cases of the hash database API</p>
<h2>DESCRIPTION</h2>
<p> To use the hash database API easily, the commands `<code>tchtest</code>&#8216;, `<code>tchmttest</code>&#8216;, and `<code>tchmgr</code>&#8216; are provided. </p>
<p> The command `<code>tchtest</code>&#8216; is a utility for facility test and performance test. This command is used in the following format. `<i>path</i>&#8216; specifies the path of a database file. `<i>rnum</i>&#8216; specifies the number of iterations. `<i>bnum</i>&#8216; specifies the number of buckets. `<i>apow</i>&#8216; specifies the power of the alignment. `<i>fpow</i>&#8216; specifies the power of the free block pool. </p>
<dl>
<dt>
<dd>
 <code>tchtest write </code>[<code>-mt</code>][<code>-tl</code>][<code>-td</code>|<code>-tb</code>|<code>-tt</code>|<code>-tx</code>][<code>-rc </code><i>num</i>][<code>-xm </code><i>num</i>][<code>-df </code><i>num</i>][<code>-nl</code>|<code>-nb</code>][<code>-as</code>][<code>-rnd</code>]<i>path</i><i>rnum</i>[<i>bnum</i>[<i>apow</i>[<i>fpow</i>]]]</p>
<dl>
<dt>
<dd> Store records with keys of 8 bytes. They change as `00000001&#8242;, `00000002&#8217;&#8230;</dl>
<p> <code>tchtest read </code>[<code>-mt</code>][<code>-rc </code><i>num</i>][<code>-xm </code><i>num</i>][<code>-df </code><i>num</i>][<code>-nl</code>|<code>-nb</code>][<code>-wb</code>][<code>-rnd</code>]<i>path</i></p>
<dl>
<dt>
<dd> Retrieve all records of the database above.</dl>
<p> <code>tchtest remove </code>[<code>-mt</code>][<code>-rc </code><i>num</i>][<code>-xm </code><i>num</i>][<code>-df </code><i>num</i>][<code>-nl</code>|<code>-nb</code>][<code>-rnd</code>]<i>path</i></p>
<dl>
<dt>
<dd> Remove all records of the database above.</dl>
<p> <code>tchtest rcat </code>[<code>-mt</code>][<code>-tl</code>][<code>-td</code>|<code>-tb</code>|<code>-tt</code>|<code>-tx</code>][<code>-rc </code><i>num</i>][<code>-xm </code><i>num</i>][<code>-df </code><i>num</i>][<code>-nl</code>|<code>-nb</code>][<code>-pn </code><i>num</i>][<code>-dai</code>|<code>-dad</code>|<code>-rl</code>|<code>-ru</code>]<i>path</i><i>rnum</i>[<i>bnum</i>[<i>apow</i>[<i>fpow</i>]]]</p>
<dl>
<dt>
<dd> Store records with partway duplicated keys using concatenate mode.</dl>
<p> <code>tchtest misc </code>[<code>-mt</code>][<code>-tl</code>][<code>-td</code>|<code>-tb</code>|<code>-tt</code>|<code>-tx</code>][<code>-nl</code>|<code>-nb</code>]<i>path</i><i>rnum</i></p>
<dl>
<dt>
<dd> Perform miscellaneous test of various operations.</dl>
<p> <code>tchtest wicked </code>[<code>-mt</code>][<code>-tl</code>][<code>-td</code>|<code>-tb</code>|<code>-tt</code>|<code>-tx</code>][<code>-nl</code>|<code>-nb</code>]<i>path</i><i>rnum</i></p>
<dl>
<dt>
<dd> Perform updating operations selected at random.</dl>
</dl>
<p> Options feature the following. </p>
<dl>
<dt>
<dd> <code>-mt</code> : call the function `tchdbsetmutex&#8217;.<br />
 <code>-tl</code> : enable the option `HDBTLARGE&#8217;.<br />
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
 <code>-pn </code><i>num</i> : specify the number of patterns.<br />
 <code>-dai</code> : use the function `tchdbaddint&#8217; instead of `tchdbputcat&#8217;.<br />
 <code>-dad</code> : use the function `tchdbadddouble&#8217; instead of `tchdbputcat&#8217;.<br />
 <code>-rl</code> : set the length of values at random.<br />
 <code>-ru</code> : select update operations at random.
</dl>
<p> This command returns 0 on success, another on failure. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tchmttest/">tchmttest</a></code>(1), <code><a href="/docs/linux/man/1-tchmgr/">tchmgr</a></code>(1), <code><a href="/docs/linux/man/3-tchdb/">tchdb</a></code>(3), <code><a href="/docs/linux/man/3-tokyocabinet/">tokyocabinet</a></code>(3) </p>
<h2>Index</h2>
