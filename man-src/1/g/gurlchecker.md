---
title: "gurlchecker(1)"
name: "gurlchecker"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gurlchecker/"
description: "gurlchecker – A graphical web link checker that works on a whole site, a single local page or a browser bookmarks file."
---

<h2>NAME</h2>
<p> gurlchecker &#8211; A graphical web link checker that works on a whole site, a single local page or a browser bookmarks file.</p>
<h2>SYNOPSIS</h2>
<p> <code>gurlchecker</code> [ <code>-h|&#8211;help</code> ] [ <code>-v|&#8211;version</code> ] [ <code>-u|&#8211;http-user </code><i>user</i> ] [ <code>-p|&#8211;http-passwd </code><i>password</i> ] [ <code>-A|&#8211;no-urls-args</code> ] [ <code>Done. </code> ]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents the <code>gurlchecker</code> command. </p>
<p> <code>gurlchecker</code> is a graphical web link checker. It searches URLs in a whole site, a single local page or a browser bookmarks page, checking them, one by one, in order to know their validity. Furthermore, it can manage entire projects.</p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Show version of program.</p>
<dt><code>-u, &#8211;http-user</code></p>
<dd> User name for HTTP Basic Authentication.</p>
<dt><code>-p, &#8211;http-passwd</code></p>
<dd> Password for HTTP Basic Authentication.</p>
<dt><code>-A, &#8211;no-urls-args</code></p>
<dd> Ignore URLs arguments. </p>
<p> With this option gurlchecker will systematically remove arguments on URLs. It is usefull to avoid nasty infinite loops when arguments are randomly generated, for example.</dl>
<h2>AUTHORS</h2>
<p> This manual page was written by Daniel Pecos Martinez &lt;&lt;dani [at] netpecos.org&gt;&gt; and Emmanuel Saracco &lt;&lt;esaracco [at] users.labs.libre-entreprise.org&gt;&gt; for the Debian system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.1 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts. </p>
<h2>Index</h2>
