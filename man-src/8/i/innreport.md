---
title: "innreport(8)"
name: "innreport"
section: "8"
letter: "i"
url: "/docs/linux/man/8-innreport/"
---

innreport - summarize INN log files.

<h2>Synopsis</h2>

innreport -f innreport.conf [ -[no]options ] [ logfiles ]

<h2>Description</h2>

<i>Innreport</i> is a <i><a HREF="/docs/linux/man/1-perl/">perl</a></i>(1) script that summarizes INN log files. It is normally invoked by <i><a HREF="/docs/linux/man/8-scanlogs/">scanlogs</a></i>(8). Supported programs are <i><a HREF="/docs/linux/man/8-innd/">innd</a></i>(8), <i><a HREF="/docs/linux/man/1-innfeed/">innfeed</a></i>(1), <i><a HREF="/docs/linux/man/8-innxmit/">innxmit</a></i>(8), <i>nntplink, </i> <i><a HREF="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8), <i><a HREF="/docs/linux/man/8-batcher/">batcher</a></i>(8), <i><a HREF="/docs/linux/man/1-rnews/">rnews</a></i>(1) and a few others.

<h2>Options</h2>

There are lots of 'em. Run innreport with ``-h'' or ``-help'' to get full details.

<h2>History</h2>

Written by Fabien Tassin &lt;fta [at] sofaraway.org&gt; for InterNetNews. This is revision 8242, dated 2008-12-21.

<h2>See Also</h2>

<a HREF="/docs/linux/man/8-innd/">innd</a>(8), <a HREF="/docs/linux/man/8-innfeed/">innfeed</a>(8), <a HREF="/docs/linux/man/8-innxmit/">innxmit</a>(8), <a HREF="/docs/linux/man/8-news-daily/">news.daily</a>(8), <a HREF="/docs/linux/man/5-newslog/">newslog</a>(5), <a HREF="/docs/linux/man/8-nnrpd/">nnrpd</a>(8), <a HREF="/docs/linux/man/8-scanlogs/">scanlogs</a>(8), <a HREF="/docs/linux/man/8-writelog/">writelog</a>(8). 
