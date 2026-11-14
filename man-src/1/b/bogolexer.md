---
title: "bogolexer(1)"
name: "bogolexer"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bogolexer/"
description: "bogolexer – Utility program for separating email messages into tokens"
---

<h2 class="name">NAME</h2>
<p> bogolexer &#8211; Utility program for separating email messages into tokens </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>bogolexer</code> [-p] [-q] [-h] [-n] [-v] [-x&nbsp;<wbr><i>flags</i>] [-c&nbsp;<wbr><i>file</i>] [-C] [-D] [-I&nbsp;<wbr><i>file</i>] [-O&nbsp;<wbr><i>file</i>] [-V]</dl>
<h2>DESCRIPTION</h2>
<dd>Bogolexer is part of the bogofilter Bayesian spam filter package. </p>
<p> It is used to separate messages into tokens and to test new versions of the lexer.l code.</p>
<h2>OPTIONS</h2>
<p> The <code>-p</code> option tells bogolexer to print just the tokens read from stdin, without any extra messages. </p>
<p> The <code>-q</code> option tells bogolexer to print a token count, without printing the actual tokens. </p>
<p> The <code>-h</code> option prints the help message and exits. </p>
<p> The <code>-n</code> option tells bogolexer to map non-ascii characters to the question point &#8216;?&#8217;. </p>
<p> The <code>-v</code> option increases the verbosity level. </p>
<p> The <code>-x </code><i>flags</i> option allows setting of debug flags for printing debug messages. </p>
<p> The <code>-c</code><i>filename</i> option tells bogolexer to read the config file named. </p>
<p> The <code>-C</code> option prevents bogolexer from reading configuration files. </p>
<p> The <code>-D</code> option redirects the debugging output to stdout (it defaults to stderr). </p>
<p> The <code>-I </code><i>filename</i> option tells bogolexer to read its input from the specified file, rather than from <i>stdin</i>. </p>
<p> The <code>-O </code><i>filename</i> option tells bogolexer to write its output to the specified file, rather than to <i>stdout</i>. </p>
<p> The <code>-V</code> option prints the version number and exits.</p>
<h2>AUTHOR</h2>
<p> The bogofilter developer team. </p>
<p> For updates, see m[blue]<code>the bogofilter project page</code>m[]<font SIZE="-2">[1]</font>.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-bogofilter/">bogofilter</a>(1), <a href="/docs/linux/man/1-bogotune/">bogotune</a>(1), <a href="/docs/linux/man/1-bogoupgrade/">bogoupgrade</a>(1), <a href="/docs/linux/man/1-bogoutil/">bogoutil</a>(1)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> the bogofilter project page</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://bogofilter.sourceforge.net/">http://bogofilter.sourceforge.net/</a></dl>
</dl>
<h2>Index</h2>
