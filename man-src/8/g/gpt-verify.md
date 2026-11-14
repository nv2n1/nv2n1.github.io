---
title: "gpt-verify(8)"
name: "gpt-verify"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gpt-verify/"
description: "gpt-verify – Verify dependencies needed for Globus are avaliable."
---

<p><code>gpt-verify</code> &#8211; Verify dependencies needed for Globus are avaliable.</p>
<h2>Synopsis</h2>
<p>gpt-verify [ -sdk -bundle -help -version -man ]</p>
<h2>Description</h2>
<p><code>gpt-verify</code> is used to verify both runtime and setup dependencies along with setup packages for the current Globus installation. <code>gpt-verify</code> will serach through the list of dependencies and make sure that each is met. If a problem is found, <code>gpt-verify</code> will exit with an error and list missing files.</p>
<h2>Options</h2>
<dl>
<dt><code>-sdk</code>: Verify build dependencies.</p>
<dd>
<dt><code>-bundle</code></p>
<dd>Verify installed bundles only.</p>
<dt><code>-help</code></p>
<dd>Print a brief help message and exits.</p>
<dt><code>-man</code></p>
<dd>Prints the manual page and exits.</p>
<dt><code>-version</code></p>
<dd>Prints the version of <font SIZE="-1">GPT</font> and exits.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-gpt-install/">gpt-install</a></i>(8) <i><a href="/docs/linux/man/8-gpt-uninstall/">gpt-uninstall</a></i>(8) <i><a href="/docs/linux/man/8-gpt-query/">gpt-query</a></i>(8) <i><a href="/docs/linux/man/8-gpt-postinstall/">gpt-postinstall</a></i>(8)</p>
<h2>Author</h2>
<p>Michael Bletzinger &lt;mbletzin.ncsa.uiuc.edu&gt; and Eric Blau &lt;eblau.ncsa.uiuc.edu&gt;</p>
