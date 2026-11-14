---
title: "cargo-owner(1)"
name: "cargo-owner"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cargo-owner/"
description: "cargo-owner – Manage the owners of a crate of the registry"
---

<h2 class="name">NAME</h2>
<p> cargo-owner &#8211; Manage the owners of a crate of the registry </p>
<h2>SYNOPSIS</h2>
<p> cargo owner [OPTIONS] [&lt;CRATE&gt;]</p>
<h2>DESCRIPTION</h2>
<p> This command will modify the owners for a package on the specified registry (or default). Note that owners of a package can upload new versions, and yank old versions. Explicitly named owners can also modify the set of owners, so take caution! </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Print this message.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-a, &#8211;add </code>LOGIN</p>
<dd> Name of a user or team to add as an owner.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-r, &#8211;remove </code>LOGIN</p>
<dd> Name of a user or team to remove as an owner.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-l, &#8211;list</code></p>
<dd> List owners of a crate.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;index </code>INDEX</p>
<dd> Registry index to modify owners for.</p>
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
<p> Add user as an owner of the current package</p>
<dl>
<dt>
<dd>
<pre>
$&nbsp;<wbr>cargo owner --add user
</pre>
</dl>
<p> Remove user as an owner of the current package</p>
<dl>
<dt>
<dd>
<pre>
$&nbsp;<wbr>cargo owner --remove user
</pre>
</dl>
<p> Use a certain API token to authenticate with</p>
<dl>
<dt>
<dd>
<pre>
$&nbsp;<wbr>cargo owner --token U6WHXacP3Qqwd5kze1fohr4JEOmGCuRK2
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cargo/">cargo</a>(1), <a href="/docs/linux/man/1-cargo-publish/">cargo-publish</a>(1), <a href="/docs/linux/man/1-cargo-login/">cargo-login</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> This work is dual-licensed under Apache 2.0 and MIT terms. See COPYRIGHT file in the cargo source distribution. </p>
<h2>Index</h2>
