---
title: "ntsysv(8)"
name: "ntsysv"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntsysv/"
description: "ntsysv – simple interface for configuring runlevels"
---

<p>ntsysv &#8211; simple interface for configuring runlevels</p>
<h2>Synopsis</h2>
<p><code>ntsysv</code> [&#8211;back] [&#8211;level &lt;levels&gt;]</p>
<h2>Description</h2>
<p><code>ntsysv</code> is a simple interface for configuring runlevel services which are also configurable through <code>chkconfig</code>. By default, it configures runlevels 2, 3, 4, and 5. If the user would like to configure other runlevels, those levels can be specified on the command line by listing the levels after <code>&#8211;level</code>, without any spaces. For example, the option <i>&#8211;level 016</i> edits runlevels 0, 1, and 6. A service is considered to be started in the runlevel set if it is started in any of the runlevels which are being edited. The <code>ntsysv</code> window normally contains a <code>Cancel</code> button. If <code>&#8211;back</code> is specified, a <code>Back</code> button appears instead. </p>
<h2>Return Codes</h2>
<p><code>ntsysv</code> returns 0 on success, 2 on error, and 1 if the user cancelled (or backed out of) the program.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-chkconfig/">chkconfig</a></code>(8), </p>
<h2>Author</h2>
<pre>Erik Troan &lt;ewt [at] redhat.com&gt;</pre>
