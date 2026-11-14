---
title: "man(5)"
name: "man"
section: "5"
letter: "m"
url: "/docs/linux/man/5-man/"
description: "man.config – configuration data for man"
---

<p>man.config &#8211; configuration data for man</p>
<h2>Description</h2>
<p>This file is read by <code><a href="/docs/linux/man/1-man/">man</a></code>(1) and contains (a) information on how to construct the search path for man, (b) full path names for various programs like nroff, eqn, tbl etc. used by man, and (c) a list with uncompressors for files with a given extension. An alternative version of this file can be specified with </p>
<dl>
<dd>man -C private_man.config &#8230;</dl>
<p> The command names may be provided with options. Useful options to nroff can be found in <a href="/docs/linux/man/1-grotty/">grotty</a>(1). For example, instead of the default line </p>
<dl>
<dd>
<pre>NROFF /usr/bin/groff -mandoc -Tlatin1</pre>
</dl>
<p> one may write </p>
<dl>
<dd>
<pre>NROFF /usr/bin/groff -mandoc -Tlatin1 -P-u -P-b</pre>
</dl>
<p> in order to suppress underlining and overstriking.</p>
<h2>Files</h2>
<p><i>@man_config_file@</i></p>
<h2>Author</h2>
<p>John W. Eaton was the original author of <code>man</code>. Zeyd M. Ben-Halim released man 1.2, and Andries Brouwer followed up with versions 1.3 thru 1.5p. Federico Lucifredi &lt;flucifredi [at] acm.org&gt; is the current maintainer.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-col/">col</a>(1), (g)<a href="/docs/linux/man/1-eqn/">eqn</a>(1), (g)<a href="/docs/linux/man/1-pic/">pic</a>(1), <a href="/docs/linux/man/1-groff/">groff</a>(1), <a href="/docs/linux/man/1-grotty/">grotty</a>(1), (g)<a href="/docs/linux/man/1-refer/">refer</a>(1), (g)<a href="/docs/linux/man/1-tbl/">tbl</a>(1), <a href="/docs/linux/man/1-less/">less</a>(1), man (1) and <a href="/docs/linux/man/1-compress/">compress</a>(1), <a href="/docs/linux/man/1-gzip/">gzip</a>(1). </p>
