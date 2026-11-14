---
title: "accton(8)"
name: "accton"
section: "8"
letter: "a"
url: "/docs/linux/man/8-accton/"
description: "accton – turns process accounting on or off"
---

<p>accton &#8211; turns process accounting on or off</p>
<h2>Synopsis</h2>
<dl>
<dt><code>accton</code></p>
<dd>[<i>OPTION</i>] on<code>|</code>off<code>|</code>filename</p>
<dt><code>accton</code></p>
<dd>[ <code>-V</code> | <code>&#8211;version </code> ] [ <code>-h</code> | <code>&#8211;help</code> ]</dl>
<h2>Description</h2>
<p><code>accton</code> <i>filename</i> turns on process accounting.</p>
<h2>Options</h2>
<dl>
<dt>
<dt><code>-V, &#8211;version</code></p>
<dd>
<dd>Print the version number of <code>ac</code> to standard output and quit.</p>
<dt><code>-h, &#8211;help</code></p>
<dd>Prints the usage string and default locations of system files to standard output and exits.</p>
<dt><code>on</code></p>
<dd>Turns on process accounting using the default accounting file name.</p>
<dt><code>off</code></p>
<dd>Turns off process accounting.</dl>
<h2>Files</h2>
<dl>
<dt><i>acct</i></p>
<dd>The system wide process accounting file. See <code><a href="/docs/linux/man/5-acct/">acct</a></code>(5) (or <code><a href="/docs/linux/man/5-pacct/">pacct</a></code>(5)) for further details.</dl>
<h2>Author</h2>
<p>The GNU accounting utilities were written by Noel Cragg &lt;noel [at] gnu.ai.mit.edu&gt;. The man page was adapted from the accounting texinfo page by Susan Kleinmann &lt;sgk [at] sgk.tiac.net&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-acct/">acct</a></code>(5), <code><a href="/docs/linux/man/1-ac/">ac</a></code>(1) </p>
