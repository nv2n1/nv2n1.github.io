---
title: "tcbtest(1)"
name: "tcbtest"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tcbtest/"
description: "tcbtest – test cases of the B+ tree database API"
---

<h2 class="name">NAME</h2>
<p> tcbtest &#8211; test cases of the B+ tree database API</p>
<h2>DESCRIPTION</h2>
<p> The command `<code>tcbtest</code>&#8216; is a utility for facility test and performance test. This command is used in the following format. `<i>path</i>&#8216; specifies the path of a database file. `<i>rnum</i>&#8216; specifies the number of iterations. `<i>lmemb</i>&#8216; specifies the number of members in each leaf page. `<i>nmemb</i>&#8216; specifies the number of members in each non-leaf page. `<i>bnum</i>&#8216; specifies the number of buckets. `<i>apow</i>&#8216; specifies the power of the alignment. `<i>fpow</i>&#8216; specifies the power of the free block pool. </p>
<dl>
<dt>
<dd>
 <code>tcbtest write </code>[<code>-mt</code>][<code>-cd</code>|<code>-ci</code>|<code>-cj</code>][<code>-tl</code>][<code>-td</code>|<code>-tb</code>|<code>-tt</code>|<code>-tx</code>][<code>-lc </code><i>num</i>][<code>-nc </code><i>num</i>][<code>-xm </code><i>num</i>][<code>-df </code><i>num</i>][<code>-ls </code><i>num</i>][<code>-ca </code><i>num</i>][<code>-nl</code>|<code>-nb</code>][<code>-rnd</code>]<i>path</i><i>rnum</i>[<i>lmemb</i>[<i>nmemb</i>[<i>bnum</i>[<i>apow</i>[<i>fpow</i>]]]]]</p>
<dl>
<dt>
<dd> Store records with keys of 8 bytes. They change as `00000001&#8242;, `00000002&#8217;&#8230;</dl>
<p> <code>tcbtest read </code>[<code>-mt</code>][<code>-cd</code>|<code>-ci</code>|<code>-cj</code>][<code>-lc </code><i>num</i>][<code>-nc </code><i>num</i>][<code>-xm </code><i>num</i>][<code>-df </code><i>num</i>][<code>-nl</code>|<code>-nb</code>][<code>-wb</code>][<code>-rnd</code>]<i>path</i></p>
<dl>
<dt>
<dd> Retrieve all records of the database above.</dl>
<p> <code>tcbtest remove </code>[<code>-mt</code>][<code>-cd</code>|<code>-ci</code>|<code>-cj</code>][<code>-lc </code><i>num</i>][<code>-nc </code><i>num</i>][<code>-xm </code><i>num</i>][<code>-df </code><i>num</i>][<code>-nl</code>|<code>-nb</code>][<code>-rnd</code>]<i>path</i></p>
<dl>
<dt>
<dd> Remove all records of the database above.</dl>
<p> <code>tcbtest rcat </code>[<code>-mt</code>][<code>-cd</code>|<code>-ci</code>|<code>-cj</code>][<code>-tl</code>][<code>-td</code>|<code>-tb</code>|<code>-tt</code>|<code>-tx</code>][<code>-lc </code><i>num</i>][<code>-nc </code><i>num</i>][<code>-xm </code><i>num</i>][<code>-df </code><i>num</i>][<code>-ls </code><i>num</i>][<code>-ca </code><i>num</i>][<code>-nl</code>|<code>-nb</code>][<code>-pn </code><i>num</i>][<code>-dai</code>|<code>-dad</code>|<code>-rl</code>|<code>-ru</code>]<i>path</i><i>rnum</i>[<i>lmemb</i>[<i>nmemb</i>[<i>bnum</i>[<i>apow</i>[<i>fpow</i>]]]]]</p>
<dl>
<dt>
<dd> Store records with partway duplicated keys using concatenate mode.</dl>
<p> <code>tcbtest queue </code>[<code>-mt</code>][<code>-cd</code>|<code>-ci</code>|<code>-cj</code>][<code>-tl</code>][<code>-td</code>|<code>-tb</code>|<code>-tt</code>|<code>-tx</code>][<code>-lc </code><i>num</i>][<code>-nc </code><i>num</i>][<code>-xm </code><i>num</i>][<code>-df </code><i>num</i>][<code>-ls </code><i>num</i>][<code>-ca </code><i>num</i>][<code>-nl</code>|<code>-nb</code>]<i>path</i><i>rnum</i>[<i>lmemb</i>[<i>nmemb</i>[<i>bnum</i>[<i>apow</i>[<i>fpow</i>]]]]]</p>
<dl>
<dt>
<dd> Perform queueing and dequeueing.</dl>
<p> <code>tcbtest misc </code>[<code>-mt</code>][<code>-tl</code>][<code>-td</code>|<code>-tb</code>|<code>-tt</code>|<code>-tx</code>][<code>-nl</code>|<code>-nb</code>]<i>path</i><i>rnum</i></p>
<dl>
<dt>
<dd> Perform miscellaneous test of various operations.</dl>
<p> <code>tcbtest wicked </code>[<code>-mt</code>][<code>-tl</code>][<code>-td</code>|<code>-tb</code>|<code>-tt</code>|<code>-tx</code>][<code>-nl</code>|<code>-nb</code>]<i>path</i><i>rnum</i></p>
<dl>
<dt>
<dd> Perform updating operations selected at random.</dl>
</dl>
<p> Options feature the following. </p>
<dl>
<dt>
<dd> <code>-mt</code> : call the function `tchdbsetmutex&#8217;.<br />
 <code>-cd</code> : use the comparison function `tccmpdecimal&#8217;.<br />
 <code>-ci</code> : use the comparison function `tccmpint32&#8242;.<br />
 <code>-cj</code> : use the comparison function `tccmpint64&#8242;.<br />
 <code>-tl</code> : enable the option `BDBTLARGE&#8217;.<br />
 <code>-td</code> : enable the option `BDBTDEFLATE&#8217;.<br />
 <code>-tb</code> : enable the option `BDBTBZIP&#8217;.<br />
 <code>-tt</code> : enable the option `BDBTTCBS&#8217;.<br />
 <code>-tx</code> : enable the option `BDBTEXCODEC&#8217;.<br />
 <code>-lc </code><i>num</i> : specify the number of cached leaf pages.<br />
 <code>-nc </code><i>num</i> : specify the number of cached non-leaf pages.<br />
 <code>-xm </code><i>num</i> : specify the size of the extra mapped memory.<br />
 <code>-df </code><i>num</i> : specify the unit step number of auto defragmentation.<br />
 <code>-ls </code><i>num</i> : specify the maximum size of each leaf page.<br />
 <code>-ca </code><i>num</i> : specify the capacity number of records.<br />
 <code>-nl</code> : enable the option `BDBNOLCK&#8217;.<br />
 <code>-nb</code> : enable the option `BDBLCKNB&#8217;.<br />
 <code>-rnd</code> : select keys at random.<br />
 <code>-wb</code> : use the function `tcbdbget3&#8242; instead of `tcbdbget&#8217;.<br />
 <code>-pn </code><i>num</i> : specify the number of patterns.<br />
 <code>-dai</code> : use the function `tcbdbaddint&#8217; instead of `tcbdbputcat&#8217;.<br />
 <code>-dad</code> : use the function `tcbdbadddouble&#8217; instead of `tcbdbputcat&#8217;.<br />
 <code>-rl</code> : set the length of values at random.<br />
 <code>-ru</code> : select update operations at random.
</dl>
<p> This command returns 0 on success, another on failure. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tcbmttest/">tcbmttest</a></code>(1), <code><a href="/docs/linux/man/1-tcbmgr/">tcbmgr</a></code>(1), <code><a href="/docs/linux/man/3-tcbdb/">tcbdb</a></code>(3), <code><a href="/docs/linux/man/3-tokyocabinet/">tokyocabinet</a></code>(3) </p>
<h2>Index</h2>
