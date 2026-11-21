---
title: "tcamttest(1)"
name: "tcamttest"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tcamttest/"
description: "tcamttest – test cases of the abstract database API"
---

<h2>DESCRIPTION</h2>
<p> The command `<code>tcamttest</code>&#8216; is a utility for facility test under multi-thread situation. This command is used in the following format. `<i>name</i>&#8216; specifies the database name. `<i>tnum</i>&#8216; specifies the number of running threads. `<i>rnum</i>&#8216; specifies the number of iterations. </p>
<dl>
<dt>
</dt><dd>
 <code>tcamttest write </code><i>name</i><i>tnum</i><i>rnum</i></dd>
<dl>
<dt>
</dt><dd> Store records with keys of 8 bytes. They change as `00000001&#8242;, `00000002&#8217;&#8230;</dd></dl>
<p> <code>tcamttest read </code><i>name</i><i>tnum</i></p>
<dl>
<dt>
</dt><dd> Retrieve all records of the database above.</dd></dl>
<p> <code>tcamttest remove </code><i>name</i><i>tnum</i></p>
<dl>
<dt>
</dt><dd> Remove all records of the database above.</dd></dl>
</dl>
<p> This command returns 0 on success, another on failure. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tcatest/">tcatest</a></code>(1), <code><a href="/docs/linux/man/1-tcamgr/">tcamgr</a></code>(1), <code><a href="/docs/linux/man/3-tcadb/">tcadb</a></code>(3), <code><a href="/docs/linux/man/3-tokyocabinet/">tokyocabinet</a></code>(3) </p>
