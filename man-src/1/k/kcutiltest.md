---
title: "kcutiltest(1)"
name: "kcutiltest"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kcutiltest/"
description: "kcutiltest – command line interface to test the utility functions"
---

<h2 class="name">NAME</h2>
<p> kcutiltest &#8211; command line interface to test the utility functions</p>
<h2>DESCRIPTION</h2>
<p> The command `<code>kcutiltest</code>&#8216; is a utility for facility test and performance test of the utility functions. This command is used in the following format. `<i>rnum</i>&#8216; specifies the number of iterations. `<i>path</i>&#8216; specifies the path of a file. </p>
<dl>
<dt>
<dd>
 <code>kcutiltest mutex </code>[<code>-th </code><i>num</i>][<code>-iv </code><i>num</i>]<i>rnum</i></p>
<dl>
<dt>
<dd> Performs test of lock primitives.</dl>
<p> <code>kcutiltest cond </code>[<code>-th </code><i>num</i>][<code>-iv </code><i>num</i>]<i>rnum</i></p>
<dl>
<dt>
<dd> Performs test of condition variable primitives.</dl>
<p> <code>kcutiltest para </code>[<code>-th </code><i>num</i>][<code>-iv </code><i>num</i>]<i>rnum</i></p>
<dl>
<dt>
<dd> Performs test of parallel processing.</dl>
<p> <code>kcutiltest file </code>[<code>-th </code><i>num</i>][<code>-rnd</code>][<code>-msiz </code><i>num</i>]<i>path</i><i>rnum</i></p>
<dl>
<dt>
<dd> Performs test of the file system abstraction.</dl>
<p> <code>kcutiltest lhmap </code>[<code>-rnd</code>][<code>-bnum </code><i>num</i>]<i>rnum</i></p>
<dl>
<dt>
<dd> Performs test of doubly-linked hash map.</dl>
<p> <code>kcutiltest thmap </code>[<code>-rnd</code>][<code>-bnum </code><i>num</i>]<i>rnum</i></p>
<dl>
<dt>
<dd> Performs test of memory-saving hash map.</dl>
<p> <code>kcutiltest talist </code>[<code>-rnd</code>]<i>rnum</i></p>
<dl>
<dt>
<dd> Performs test of memory-saving array list.</dl>
<p> <code>kcutiltest misc </code><i>rnum</i></p>
<dl>
<dt>
<dd> Performs test of miscellaneous mechanisms.</dl>
</dl>
<p> Options feature the following. </p>
<dl>
<dt>
<dd> <code>-th </code><i>num</i> : specifies the number of worker threads.<br />
 <code>-iv </code><i>num</i> : specifies the interval between iterations.<br />
 <code>-rnd</code> : performs random test.<br />
 <code>-msiz </code><i>num</i> : specifies the size of the memory-mapped region.<br />
 <code>-bnum </code><i>num</i> : specifies the number of buckets of the hash table.
</dl>
<p> This command returns 0 on success, another on failure. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-kcutilmgr/">kcutilmgr</a></code>(1) </p>
<h2>Index</h2>
