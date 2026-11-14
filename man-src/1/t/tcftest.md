---
title: "tcftest(1)"
name: "tcftest"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tcftest/"
description: "tcftest – test cases of the fixed-length database API"
---

<h2 class="name">NAME</h2>
<p> tcftest &#8211; test cases of the fixed-length database API</p>
<h2>DESCRIPTION</h2>
<p> The command `<code>tcftest</code>&#8216; is a utility for facility test and performance test. This command is used in the following format. `<i>path</i>&#8216; specifies the path of a database file. `<i>rnum</i>&#8216; specifies the number of iterations. `<i>width</i>&#8216; specifies the width of the value of each record. `<i>limsiz</i>&#8216; specifies the limit size of the database file. </p>
<dl>
<dt>
<dd>
 <code>tcftest write </code>[<code>-mt</code>][<code>-nl</code>|<code>-nb</code>][<code>-rnd</code>]<i>path</i><i>rnum</i>[<i>width</i>[<i>limsiz</i>]]</p>
<dl>
<dt>
<dd> Store records with keys of 8 bytes. They change as `00000001&#8242;, `00000002&#8217;&#8230;</dl>
<p> <code>tcftest read </code>[<code>-mt</code>][<code>-nl</code>|<code>-nb</code>][<code>-wb</code>][<code>-rnd</code>]<i>path</i></p>
<dl>
<dt>
<dd> Retrieve all records of the database above.</dl>
<p> <code>tcftest remove </code>[<code>-mt</code>][<code>-nl</code>|<code>-nb</code>][<code>-rnd</code>]<i>path</i></p>
<dl>
<dt>
<dd> Remove all records of the database above.</dl>
<p> <code>tcftest rcat </code>[<code>-mt</code>][<code>-nl</code>|<code>-nb</code>][<code>-pn </code><i>num</i>][<code>-dai</code>|<code>-dad</code>|<code>-rl</code>]<i>path</i><i>rnum</i>[<i>limsiz</i>]]</p>
<dl>
<dt>
<dd> Store records with partway duplicated keys using concatenate mode.</dl>
<p> <code>tcftest misc </code>[<code>-mt</code>][<code>-nl</code>|<code>-nb</code>]<i>path</i><i>rnum</i></p>
<dl>
<dt>
<dd> Perform miscellaneous test of various operations.</dl>
<p> <code>tcftest wicked </code>[<code>-mt</code>][<code>-nl</code>|<code>-nb</code>]<i>path</i><i>rnum</i></p>
<dl>
<dt>
<dd> Perform updating operations selected at random.</dl>
</dl>
<p> Options feature the following. </p>
<dl>
<dt>
<dd> <code>-mt</code> : call the function `tcfdbsetmutex&#8217;.<br />
 <code>-nl</code> : enable the option `FDBNOLCK&#8217;.<br />
 <code>-nb</code> : enable the option `FDBLCKNB&#8217;.<br />
 <code>-rnd</code> : select keys at random.<br />
 <code>-wb</code> : use the function `tcfdbget4&#8242; instead of `tcfdbget2&#8242;.<br />
 <code>-pn </code><i>num</i> : specify the number of patterns.<br />
 <code>-dai</code> : use the function `tcfdbaddint&#8217; instead of `tcfdbputcat&#8217;.<br />
 <code>-dad</code> : use the function `tcfdbadddouble&#8217; instead of `tcfdbputcat&#8217;.<br />
 <code>-rl</code> : set the length of values at random.<br />
 <code>-ru</code> : perform random operation on random key.
</dl>
<p> This command returns 0 on success, another on failure. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tcfmttest/">tcfmttest</a></code>(1), <code><a href="/docs/linux/man/1-tcfmgr/">tcfmgr</a></code>(1), <code><a href="/docs/linux/man/3-tcfdb/">tcfdb</a></code>(3), <code><a href="/docs/linux/man/3-tokyocabinet/">tokyocabinet</a></code>(3) </p>
<h2>Index</h2>
