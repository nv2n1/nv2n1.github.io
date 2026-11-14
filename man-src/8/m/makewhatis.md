---
title: "makewhatis(8)"
name: "makewhatis"
section: "8"
letter: "m"
url: "/docs/linux/man/8-makewhatis/"
description: "makewhatis – Create the whatis database"
---

<p>makewhatis &#8211; Create the whatis database</p>
<h2>Synopsis</h2>
<p><code>makewhatis [-u] [-v] [-w] [-s </code><i>sections</i><code> ] [-c [</code><i>catpath</i><code>]] [</code><i>manpath</i><code>]</code></p>
<h2>Description</h2>
<p><code>makewhatis</code> reads all the manual pages contained in the given <i>sections</i> of <i>manpath</i> or the preformatted pages contained in the given <i>sections</i> of <i>catpath</i>. For each page, it writes a line in the whatis database; each line consists of the name of the page and a short description, separated by a dash. The description is extracted using the content of the NAME section of the manual page. </p>
<p> Since other languages use a different term for the NAME section, <code>makewhatis</code> recognizes the equivalent terms in Czech, Italian, Finnish, French, German and Spanish. </p>
<p> If no <i>manpath</i> argument is given, <i>/usr/man</i> is assumed by default.</p>
<h2>Options</h2>
<dl>
<dt><code>-u</code></p>
<dd>Update database with new pages (file&#8217;s status was last changed 24 hours ago)</p>
<dt><code>-v</code></p>
<dd>Verbose output</p>
<dt><code>-w</code></p>
<dd>Use manpath obtained from `man &#8211;path`</p>
<dt><code>-s</code><i> sections</i></p>
<dd>Looks in the <i>sections</i> of <i>manpath</i> or <i>catpath</i>. If the option is absent, the MANSECT env var will be used. If it too is absent, the MANSECT setting in man.conf will be used.</p>
<dt><code>-c</code><i> catpath</i></p>
<dd>The preformatted manual pages located in <i>catpath</i> are scanned. If the argument is not provided, it is assumed to be the first existing directory between <i>/usr/man/preformat</i> and <i>/usr/man</i>.</dl>
<h2>Examples</h2>
<p>To rebuild only <i>/usr/X11R6/man/whatis</i> and <i>/usr/local/man/whatis</i></p>
<dl>
<dd>makewhatis /usr/X11R6/man /usr/local/man</dl>
<p> To rebuild all the databases, including those of the Finnish, French and Italian translations</p>
<dl>
<dd>LANGUAGE=fi:fr:it makewhatis -w</dl>
<h2>Bugs</h2>
<p><code>makewhatis</code> may not handle too well manual pages written with non-standard troff macros, such as the Tcl/Tk pages. </p>
<p> <code>makewhatis</code> does not work on preformatted translations.</p>
<h2>Author</h2>
<p>John W. Eaton was the original author of <code>man</code>. Zeyd M. Ben-Halim released man 1.2, and Andries Brouwer followed up with versions 1.3 thru 1.5p. Federico Lucifredi &lt;flucifredi [at] acm.org&gt; is the current maintainer.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-apropos/">apropos</a></code>(1), <code><a href="/docs/linux/man/1-man/">man</a></code>(1), <code><a href="/docs/linux/man/1-whatis/">whatis</a></code>(1) </p>
