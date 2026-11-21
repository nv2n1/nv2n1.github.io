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
<dt><code>-h, &#8211;help</code></dt>
<dd> Print this message.</dd>
<dl>
</dl>
<dt><code>-a, &#8211;add </code>LOGIN</dt>
<dd> Name of a user or team to add as an owner.</dd>
<dl>
</dl>
<dt><code>-r, &#8211;remove </code>LOGIN</dt>
<dd> Name of a user or team to remove as an owner.</dd>
<dl>
</dl>
<dt><code>-l, &#8211;list</code></dt>
<dd> List owners of a crate.</dd>
<dl>
</dl>
<dt><code>&#8211;index </code>INDEX</dt>
<dd> Registry index to modify owners for.</dd>
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
<p> Add user as an owner of the current package</p>
<dl>
<dt>
</dt><dd>
<pre>
$&nbsp;<wbr>cargo owner --add user
</pre>
</dd></dl>
<p> Remove user as an owner of the current package</p>
<dl>
<dt>
</dt><dd>
<pre>
$&nbsp;<wbr>cargo owner --remove user
</pre>
</dd></dl>
<p> Use a certain API token to authenticate with</p>
<dl>
<dt>
</dt><dd>
<pre>
$&nbsp;<wbr>cargo owner --token U6WHXacP3Qqwd5kze1fohr4JEOmGCuRK2
</pre>
</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cargo/">cargo</a>(1), <a href="/docs/linux/man/1-cargo-publish/">cargo-publish</a>(1), <a href="/docs/linux/man/1-cargo-login/">cargo-login</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> This work is dual-licensed under Apache 2.0 and MIT terms. See COPYRIGHT file in the cargo source distribution. </p>
