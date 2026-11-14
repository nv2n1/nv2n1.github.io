---
title: "tcfmttest(1)"
name: "tcfmttest"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tcfmttest/"
description: "tcfmttest – test cases of the fixed-length database API"
---

<h2 class="name">NAME</h2>
<p> tcfmttest &#8211; test cases of the fixed-length database API</p>
<h2>DESCRIPTION</h2>
<p> The command `<code>tcfmttest</code>&#8216; is a utility for facility test under multi-thread situation. This command is used in the following format. `<i>path</i>&#8216; specifies the path of a database file. `<i>tnum</i>&#8216; specifies the number of running threads. `<i>rnum</i>&#8216; specifies the number of iterations. `<i>width</i>&#8216; specifies the width of the value of each record. `<i>limsiz</i>&#8216; specifies the limit size of the database file. </p>
<dl>
<dt>
<dd>
 <code>tcfmttest write </code>[<code>-nl</code>|<code>-nb</code>][<code>-rnd</code>]<i>path</i><i>tnum</i><i>rnum</i>[<i>width</i>[<i>limsiz</i>]]</p>
<dl>
<dt>
<dd> Store records with keys of 8 bytes. They change as `00000001&#8242;, `00000002&#8217;&#8230;</dl>
<p> <code>tcfmttest read </code>[<code>-nl</code>|<code>-nb</code>][<code>-wb</code>][<code>-rnd</code>]<i>path</i><i>tnum</i></p>
<dl>
<dt>
<dd> Retrieve all records of the database above.</dl>
<p> <code>tcfmttest remove </code>[<code>-nl</code>|<code>-nb</code>][<code>-rnd</code>]<i>path</i><i>tnum</i></p>
<dl>
<dt>
<dd> Remove all records of the database above.</dl>
<p> <code>tcfmttest wicked </code>[<code>-nl</code>|<code>-nb</code>][<code>-nc</code>]<i>path</i><i>tnum</i><i>rnum</i></p>
<dl>
<dt>
<dd> Perform updating operations selected at random.</dl>
<p> <code>tcfmttest typical </code>[<code>-nl</code>|<code>-nb</code>][<code>-nc</code>][<code>-rr </code><i>num</i>]<i>path</i><i>tnum</i><i>rnum</i>[<i>width</i>[<i>limsiz</i>]]</p>
<dl>
<dt>
<dd> Perform typical operations selected at random.</dl>
</dl>
<p> Options feature the following. </p>
<dl>
<dt>
<dd> <code>-nl</code> : enable the option `FDBNOLCK&#8217;.<br />
 <code>-nb</code> : enable the option `FDBLCKNB&#8217;.<br />
 <code>-rnd</code> : select keys at random.<br />
 <code>-wb</code> : use the function `tcfdbget4&#8242; instead of `tcfdbget2&#8242;.<br />
 <code>-nc</code> : omit the comparison test.<br />
 <code>-rr</code> <i>num</i> : specifiy the ratio of reading operation by percentage.
</dl>
<p> This command returns 0 on success, another on failure. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tcftest/">tcftest</a></code>(1), <code><a href="/docs/linux/man/1-tcfmgr/">tcfmgr</a></code>(1), <code><a href="/docs/linux/man/3-tcfdb/">tcfdb</a></code>(3), <code><a href="/docs/linux/man/3-tokyocabinet/">tokyocabinet</a></code>(3) </p>
<h2>Index</h2>
