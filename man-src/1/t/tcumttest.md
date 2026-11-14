---
title: "tcumttest(1)"
name: "tcumttest"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tcumttest/"
description: "tcutest – test cases of the on-memory database API"
---

<h2 class="name">NAME</h2>
<p> tcutest &#8211; test cases of the on-memory database API</p>
<h2>DESCRIPTION</h2>
<p> The command `<code>tcumttest</code>&#8216; is a utility for facility test under multi-thread situation. This command is used in the following format. `<i>rnum</i>&#8216; specifies the number of iterations. `<i>bnum</i>&#8216; specifies the number of buckets. </p>
<dl>
<dt>
<dd>
 <code>tcumttest combo </code>[<code>-rnd</code>]<i>tnum</i><i>rnum</i>[<i>bnum</i>] [<code>-tr</code>]<code></p>
<dl>
<dt>
<dd> Peform storing, retrieving, and removing in turn.</dl>
<p> tcumttest typical </code>[<code>-nc</code>][<code>-rr </code><i>num</i>]<i>tnum</i><i>rnum</i>[<i>bnum</i>] [<code>-tr</code>]<code></p>
<dl>
<dt>
<dd> Perform typical operations selected at random.</dl>
</dl>
<p> Options feature the following. </p>
<dl>
<dt>
<dd> -rnd</code> : select keys at random.<br />
 <code>-nc</code> : omit the comparison test.<br />
 -rr <i>num</i> : specifiy the ratio of reading operation by percentage.<br />
 <code>-tr</code> : use on-memory tree database object.
</dl>
<p> This command returns 0 on success, another on failure. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tcutest/">tcutest</a></code>(1), <code><a href="/docs/linux/man/1-tcucodec/">tcucodec</a></code>(1), <code><a href="/docs/linux/man/3-tcutil/">tcutil</a></code>(3), <code><a href="/docs/linux/man/3-tokyocabinet/">tokyocabinet</a></code>(3) </p>
<h2>Index</h2>
