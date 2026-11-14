---
title: "writelog(8)"
name: "writelog"
section: "8"
letter: "w"
url: "/docs/linux/man/8-writelog/"
description: "writelog – add a entry to an INN log file."
---

<p>writelog &#8211; add a entry to an INN log file.</p>
<h2>Synopsis</h2>
<p><code>writelog</code> <i>name</i> <i>text&#8230;</i></p>
<h2>Description</h2>
<p>The <i>writelog</i> script is used to write a log entry or send it as mail. The <i>name</i> parameter specifies the name of the log file where the entry should be written. If it is the word &#8220;mail&#8221; then the entry is mailed to the news administrator, <i>&lt;USER specified with &#8211;with-news-master at configure&gt;</i>. The data that is written or sent consists of the <i>text</i> given on the command line, followed by standard input indented by four spaces. <i><a href="/docs/linux/man/1-shlock/">Shlock</a></i>(1) is used to avoid simultaneous updates to a single log file.</p>
<h2>History</h2>
<p>Written by Landon Curt Noll &lt;chongo [at] toad.com&gt; and Rich $alz &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. This is revision 5909, dated 2002-12-03.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-innd/">innd</a>(8), <a href="/docs/linux/man/8-innstat/">innstat</a>(8), <a href="/docs/linux/man/8-news-daily/">news.daily</a>(8), <a href="/docs/linux/man/5-newslog/">newslog</a>(5), <a href="/docs/linux/man/8-nnrpd/">nnrpd</a>(8), <a href="/docs/linux/man/8-scanlogs/">scanlogs</a>(8). </p>
