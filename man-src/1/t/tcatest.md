---

title: "tcatest(1)"
name: "tcatest"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tcatest/"
description: "tcatest – test cases of the abstract database API"
---

<p> The command `<code>tcatest</code>&#8216; is a utility for facility test and performance test. This command is used in the following format. `<i>name</i>&#8216; specifies the database name. `<i>rnum</i>&#8216; specifies the number of iterations. `<i>tnum</i>&#8216; specifies the number of transactions. </p>
<dl>
<dt>
</dt><dd>
 <code>tcatest write </code><i>name</i><i>rnum</i></dd>
<dl>
<dt>
</dt><dd> Store records with keys of 8 bytes. They change as `00000001&#8242;, `00000002&#8217;&#8230;</dd></dl>
<p> <code>tcatest read </code><i>name</i></p>
<dl>
<dt>
</dt><dd> Retrieve all records of the database above.</dd></dl>
<p> <code>tcatest remove </code><i>name</i></p>
<dl>
<dt>
</dt><dd> Remove all records of the database above.</dd></dl>
<p> <code>tcatest rcat </code><i>name</i><i>rnum</i></p>
<dl>
<dt>
</dt><dd> Store records with partway duplicated keys using concatenate mode.</dd></dl>
<p> <code>tcatest misc </code><i>name</i><i>rnum</i></p>
<dl>
<dt>
</dt><dd> Perform miscellaneous test of various operations.</dd></dl>
<p> <code>tcatest wicked </code><i>name</i><i>rnum</i></p>
<dl>
<dt>
</dt><dd> Perform updating operations of list and map selected at random.</dd></dl>
<p> <code>tcatest compare </code><i>name</i><i>tnum</i><i>rnum</i></p>
<dl>
<dt>
</dt><dd> Perform comparison test of database schema.</dd></dl>
</dl>
<p> This command returns 0 on success, another on failure. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tcamttest/">tcamttest</a></code>(1), <code><a href="/docs/linux/man/1-tcamgr/">tcamgr</a></code>(1), <code><a href="/docs/linux/man/3-tcadb/">tcadb</a></code>(3), <code><a href="/docs/linux/man/3-tokyocabinet/">tokyocabinet</a></code>(3) </p>
