---
title: "qtdoc(1)"
name: "qtdoc"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qtdoc/"
description: "qtdoc – Open a Qt(TM) help page in Konqueror"
---

<h2 class="name">NAME</h2>
<p> qtdoc &#8211; Open a Qt(TM) help page in Konqueror </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>qtdoc</code> [<i>classname</i>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>qtdoc</code></p>
<dd>opens a Qt(TM) help page in Konqueror. If <i>classname</i> is given, it opens the help page for that class. Otherwise the main Qt(TM) help page is opened. <i>classname</i> is case insensitive. </p>
<p> This utility is part of the KDE Software Development Kit</p>
<h2>ENVIRONMENT</h2>
<p> <code>QTDIR</code></p>
<dl>
<dt>
<dd> The directory beneath which Qt(TM) is installed. The main Qt(TM) help page is expected to be in $<code>QTDIR</code>/doc/html/.</dl>
<h2>EXAMPLES</h2>
<p> To display the help on the class QString: </p>
<dl>
<dt>
<dd>
<pre>
<code>qtdoc</code><code>QString</code>
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-kdedoc/">kdedoc</a>(1), <a href="/docs/linux/man/1-assistant/">assistant</a>(1)</p>
<h2>AUTHORS</h2>
<p> This manual page was prepared by Ben Burton&lt;bab [at] debian.org&gt;</p>
<h2>AUTHOR</h2>
<p> <code>Ben Burton</code> &lt;bab [at] debian.org&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>Index</h2>
