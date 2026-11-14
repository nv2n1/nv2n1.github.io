---
title: "tcatest(1)"
name: "tcatest"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tcatest/"
description: "tcatest – test cases of the abstract database API"
---

<h2 class="name">NAME</h2>
<p> tcatest &#8211; test cases of the abstract database API</p>
<h2>DESCRIPTION</h2>
<p> The command `<code>tcatest</code>&#8216; is a utility for facility test and performance test. This command is used in the following format. `<i>name</i>&#8216; specifies the database name. `<i>rnum</i>&#8216; specifies the number of iterations. `<i>tnum</i>&#8216; specifies the number of transactions. </p>
<dl>
<dt>
<dd>
 <code>tcatest write </code><i>name</i><i>rnum</i></p>
<dl>
<dt>
<dd> Store records with keys of 8 bytes. They change as `00000001&#8242;, `00000002&#8217;&#8230;</dl>
<p> <code>tcatest read </code><i>name</i></p>
<dl>
<dt>
<dd> Retrieve all records of the database above.</dl>
<p> <code>tcatest remove </code><i>name</i></p>
<dl>
<dt>
<dd> Remove all records of the database above.</dl>
<p> <code>tcatest rcat </code><i>name</i><i>rnum</i></p>
<dl>
<dt>
<dd> Store records with partway duplicated keys using concatenate mode.</dl>
<p> <code>tcatest misc </code><i>name</i><i>rnum</i></p>
<dl>
<dt>
<dd> Perform miscellaneous test of various operations.</dl>
<p> <code>tcatest wicked </code><i>name</i><i>rnum</i></p>
<dl>
<dt>
<dd> Perform updating operations of list and map selected at random.</dl>
<p> <code>tcatest compare </code><i>name</i><i>tnum</i><i>rnum</i></p>
<dl>
<dt>
<dd> Perform comparison test of database schema.</dl>
</dl>
<p> This command returns 0 on success, another on failure. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tcamttest/">tcamttest</a></code>(1), <code><a href="/docs/linux/man/1-tcamgr/">tcamgr</a></code>(1), <code><a href="/docs/linux/man/3-tcadb/">tcadb</a></code>(3), <code><a href="/docs/linux/man/3-tokyocabinet/">tokyocabinet</a></code>(3) </p>
<h2>Index</h2>
