---
title: "cargo-new(1)"
name: "cargo-new"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cargo-new/"
description: "cargo-new – Create a new cargo package"
---

<h2 class="name">NAME</h2>
<p> cargo-new &#8211; Create a new cargo package </p>
<h2>SYNOPSIS</h2>
<p> cargo new [OPTIONS] &lt;PATH&gt;</p>
<h2>DESCRIPTION</h2>
<p> Create a new cargo package at &lt;PATH&gt;. </p>
<p> Use the &#8211;vcs option to control the version control system to use.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Print this message.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;vcs </code>VCS</p>
<dd> Initialize a new repository for the given version control system (git or hg) or do not initialize any version control at all (none) overriding a global configuration.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;bin</code></p>
<dd> Use a binary instead of a library template.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;name </code>NAME</p>
<dd> Set the resulting package name.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Use verbose output.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-q, &#8211;quiet</code></p>
<dd> No output printed to stdout.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;color </code>WHEN</p>
<dd> Coloring: auto, always, never.</p>
<dl>
<dt>
<dd></dl>
</dl>
<h2>EXAMPLES</h2>
<p> Create a binary cargo package in the current directory</p>
<dl>
<dt>
<dd>
<pre>
$&nbsp;<wbr>cargo new --bin ./
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cargo/">cargo</a>(1), <a href="/docs/linux/man/1-cargo-init/">cargo-init</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> This work is dual-licensed under Apache 2.0 and MIT terms. See COPYRIGHT file in the cargo source distribution. </p>
<h2>Index</h2>
