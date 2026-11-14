---
title: "tcutest(1)"
name: "tcutest"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tcutest/"
description: "tcutest – test cases of the utility API"
---

<h2 class="name">NAME</h2>
<p> tcutest &#8211; test cases of the utility API</p>
<h2>DESCRIPTION</h2>
<p> The command `<code>tcutest</code>&#8216; is a utility for facility test and performance test. This command is used in the following format. `<i>rnum</i>&#8216; specifies the number of iterations. `<i>anum</i>&#8216; specifies the initial number of elements of array. `<i>bnum</i>&#8216; specifies the number of buckets. </p>
<dl>
<dt>
<dd>
 <code>tcutest xstr </code><i>rnum</i></p>
<dl>
<dt>
<dd> Perform test of extensible string.</dl>
<p> <code>tcutest list </code>[<code>-rd</code>]<i>rnum</i>[<i>anum</i>]</p>
<dl>
<dt>
<dd> Perform test of array list.</dl>
<p> <code>tcutest map </code>[<code>-rd</code>][<code>-tr</code>][<code>-rnd</code>][<code>-dk</code>|<code>-dc</code>|<code>-dai</code>|<code>-dad</code>|<code>-dpr</code>]<i>rnum</i>[<i>bnum</i>]</p>
<dl>
<dt>
<dd> Perform test of hash map.</dl>
<p> <code>tcutest tree </code>[<code>-rd</code>][<code>-tr</code>][<code>-rnd</code>][<code>-dk</code>|<code>-dc</code>|<code>-dai</code>|<code>-dad</code>|<code>-dpr</code>]<i>rnum</i></p>
<dl>
<dt>
<dd> Perform test of ordered tree.</dl>
<p> <code>tcutest mdb </code>[<code>-rd</code>][<code>-tr</code>][<code>-rnd</code>][<code>-dk</code>|<code>-dc</code>|<code>-dai</code>|<code>-dad</code>|<code>-dpr</code>]<i>rnum</i>[<i>bnum</i>]</p>
<dl>
<dt>
<dd> Perform test of on-memory hash database.</dl>
<p> <code>tcutest ndb </code>[<code>-rd</code>][<code>-tr</code>][<code>-rnd</code>][<code>-dk</code>|<code>-dc</code>|<code>-dai</code>|<code>-dad</code>|<code>-dpr</code>]<i>rnum</i></p>
<dl>
<dt>
<dd> Perform test of on-memory tree database.</dl>
<p> <code>tcutest misc </code><i>rnum</i></p>
<dl>
<dt>
<dd> Perform test of miscellaneous routines.</dl>
<p> <code>tcutest wicked </code><i>rnum</i></p>
<dl>
<dt>
<dd> Perform updating operations of list and map selected at random.</dl>
</dl>
<p> Options feature the following. </p>
<dl>
<dt>
<dd> <code>-rd</code> : perform the reading test also.<br />
 <code>-tr</code> : perform the iterator test also.<br />
 <code>-rnd</code> : select keys at random.<br />
 <code>-dk</code> : use the function `tcxxxputkeep&#8217; instead of `tcxxxput&#8217;.<br />
 <code>-dc</code> : use the function `tcxxxputcat&#8217; instead of `tcxxxput&#8217;.<br />
 <code>-dai</code> : use the function `tcxxxaddint&#8217; instead of `tcxxxput&#8217;.<br />
 <code>-dad</code> : use the function `tcxxxadddouble&#8217; instead of `tcxxxput&#8217;.<br />
 <code>-dpr</code> : use the function `tcxxxputproc&#8217; instead of `tcxxxput&#8217;.
</dl>
<p> This command returns 0 on success, another on failure. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tcumttest/">tcumttest</a></code>(1), <code><a href="/docs/linux/man/1-tcucodec/">tcucodec</a></code>(1), <code><a href="/docs/linux/man/3-tcutil/">tcutil</a></code>(3), <code><a href="/docs/linux/man/3-tokyocabinet/">tokyocabinet</a></code>(3) </p>
<h2>Index</h2>
