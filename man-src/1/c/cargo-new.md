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
<dt><code>-h, &#8211;help</code></dt>
<dd> Print this message.</dd>
<dl>
</dl>
<dt><code>&#8211;vcs </code>VCS</dt>
<dd> Initialize a new repository for the given version control system (git or hg) or do not initialize any version control at all (none) overriding a global configuration.</dd>
<dl>
</dl>
<dt><code>&#8211;bin</code></dt>
<dd> Use a binary instead of a library template.</dd>
<dl>
</dl>
<dt><code>&#8211;name </code>NAME</dt>
<dd> Set the resulting package name.</dd>
<dl>
</dl>
<dt><code>-v, &#8211;verbose</code></dt>
<dd> Use verbose output.</dd>
<dl>
</dl>
<dt><code>-q, &#8211;quiet</code></dt>
<dd> No output printed to stdout.</dd>
<dl>
</dl>
<dt><code>&#8211;color </code>WHEN</dt>
<dd> Coloring: auto, always, never.</dd>
<dl>
</dl>
</dl>
<h2>EXAMPLES</h2>
<p> Create a binary cargo package in the current directory</p>
<dl>
<dt>
</dt><dd>
<pre>
$&nbsp;<wbr>cargo new --bin ./
</pre>
</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cargo/">cargo</a>(1), <a href="/docs/linux/man/1-cargo-init/">cargo-init</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> This work is dual-licensed under Apache 2.0 and MIT terms. See COPYRIGHT file in the cargo source distribution. </p>
