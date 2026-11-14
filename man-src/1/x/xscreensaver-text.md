---
title: "xscreensaver-text(1)"
name: "xscreensaver-text"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xscreensaver-text/"
description: "xscreensaver-text – prints some text to stdout, for use by screen savers."
---

<h2 class="name">NAME</h2>
<p> xscreensaver-text &#8211; prints some text to stdout, for use by screen savers. </p>
<h2>SYNOPSIS</h2>
<p> <code>xscreensaver-text</code> [&#8211;verbose] [&#8211;columns <i>N</i>] [&#8211;text <i>STRING</i>] [&#8211;file <i>PATH</i>] [&#8211;program <i>CMD</i>] [&#8211;url <i>URL</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <i>xscreensaver-text</i> script prints out some text for use by various screensavers, according to the options set in the ~/.xscreensaver file. This may dump the contents of a file, run a program, or load a URL.</p>
<h2>OPTIONS</h2>
<p> <i>xscreensaver-text</i> accepts the following options:</p>
<dl>
<dt><code>&#8211;columns </code><i>N</i> or &#8211;cols <i>N</i></p>
<dd> Where to wrap lines; default 72 columns.</p>
<dt><code>&#8211;verbose </code>or -v</p>
<dd> Print diagnostics to stderr. Multiple <i>-v</i> switches increase the amount of output.</dl>
<p> Command line options may be used to override the settings in the ~/.xscreensaver file:</p>
<dl>
<dt><code>&#8211;string </code><i>STRING</i></p>
<dd> Print the given string. It may contain % escape sequences as per <code><a href="/docs/linux/man/2-strftime/">strftime</a></code>(2).</p>
<dt><code>&#8211;file </code><i>PATH</i></p>
<dd> Print the contents of the given file. If &#8211;cols is specified, re-wrap the lines; otherwise, print them as-is.</p>
<dt><code>&#8211;program </code><i>CMD</i></p>
<dd> Run the given program and print its output. If &#8211;cols is specified, re-wrap the output.</p>
<dt><code>&#8211;url </code><i>HTTP-URL</i></p>
<dd> Download and print the contents of the HTTP document. If it contains HTML, RSS, or Atom, it will be converted to plain-text. </p>
<p> Note: this re-downloads the document every time it is run! It might be considered abusive for you to point this at a web server that you do not control!</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>HTTP_PROXY</code> or http_proxy</p>
<dd> to get the default HTTP proxy host and port.</dl>
<h2>BUGS</h2>
<p> The RSS and Atom output is always ISO-8859-1, regardless of locale. </p>
<p> URLs should be cached, use &quot;If-Modified-Since&quot;, and obey &quot;Expires&quot;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xscreensaver-demo/">xscreensaver-demo</a></code>(1), <code><a href="/docs/linux/man/1-xscreensaver/">xscreensaver</a></code>(1), <code><a href="/docs/linux/man/1-fortune/">fortune</a></code>(1), <code><a href="/docs/linux/man/1-phosphor/">phosphor</a></code>(1), <code><a href="/docs/linux/man/1-apple2/">apple2</a></code>(1), <code><a href="/docs/linux/man/1-starwars/">starwars</a></code>(1), <code><a href="/docs/linux/man/1-fontglide/">fontglide</a></code>(1), <code><a href="/docs/linux/man/1-dadadodo/">dadadodo</a></code>(1), <code><a href="/docs/linux/man/1-webcollage/">webcollage</a></code>(1),</p>
<dl>
<dt>
<dd> <i><a rel="nofollow" href="http://www.livejournal.com/stats/latest-rss.bml,">http://www.livejournal.com/stats/latest-rss.bml,</a></i></p>
<dl>
<dt>
<dd> <i><a rel="nofollow" href="https://en.wikipedia.org/w/index.php?title=Special:NewPages">https://en.wikipedia.org/w/index.php?title=Special:NewPages</a>&amp;feed=rss,</i></p>
<dl>
<dt>
<dd> <code><a href="/docs/linux/man/1-driftnet/">driftnet</a></code>(1), <code>EtherPEG</code>, <code>EtherPeek</code></dl>
</dl>
</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005 by Jamie Zawinski. Permission to use, copy, modify, distribute, and sell this software and its documentation for any purpose is hereby granted without fee, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation. No representations are made about the suitability of this software for any purpose. It is provided &quot;as is&quot; without express or implied warranty.</p>
<h2>AUTHOR</h2>
<p> Jamie Zawinski &lt;jwz [at] jwz.org&gt;, 20-Mar-2005. </p>
<h2>Index</h2>
