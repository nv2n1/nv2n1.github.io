---
title: "gpt-postinstall(8)"
name: "gpt-postinstall"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gpt-postinstall/"
description: "gpt-postinstall – Searches for post install scripts and executes them"
---

<p><code>gpt-postinstall</code> &#8211; Searches for post install scripts and executes them</p>
<h2>Synopsis</h2>
<pre> gpt-postinstall [-help -force -version -man -location ]</pre>
<h2>Description</h2>
<p><code>gpt-postinstall</code> Searches an installation for post-install scripts that have not been run yet and executes them. These scripts are installed by Setup packages and are designed to localize an installation. The <i>-force</i> flag can be used to re-run all of the setup scripts.</p>
<h2>Options</h2>
<dl>
<dt><code>-force</code></p>
<dd>forces all action to be taken, regardless of state.</p>
<dt><code>-help</code></p>
<dd>Print a brief help message and exits.</p>
<dt><code>-man</code></p>
<dd>Prints the manual page and exits.</p>
<dt><code>-version</code></p>
<dd>Prints the version of <font SIZE="-1">GPT</font> and exits.</p>
<dt><code>-location</code></p>
<dd>Location indicates the path to the Globus installation that will be used.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-gpt-install/">gpt-install</a></i>(1) <i><a href="/docs/linux/man/1-gpt-uninstall/">gpt-uninstall</a></i>(1) <i><a href="/docs/linux/man/1-gpt-verify/">gpt-verify</a></i>(1)</p>
<h2>Author</h2>
<p>Michael Bletzinger &lt;mbletzin.ncsa.uiuc.edu&gt; and Eric Blau &lt;eblau.ncsa.uiuc.edu&gt;</p>
