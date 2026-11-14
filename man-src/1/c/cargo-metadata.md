---
title: "cargo-metadata(1)"
name: "cargo-metadata"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cargo-metadata/"
description: "cargo-metadata – Machine-readable metadata about the current project"
---

<h2 class="name">NAME</h2>
<p> cargo-metadata &#8211; Machine-readable metadata about the current project </p>
<h2>SYNOPSIS</h2>
<p> cargo metadata [OPTIONS]</p>
<h2>DESCRIPTION</h2>
<p> Output the resolved dependencies of a project, the concrete used versions including overrides, in machine-readable format.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Print this message.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;features </code>FEATURES</p>
<dd> Space-separated list of features.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;all-features</code></p>
<dd> Build all available features.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;no-default-features</code></p>
<dd> Do not include the default feature.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;no-deps</code></p>
<dd> Output information only about the root package and don&#8217;t fetch dependencies.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;manifest-path </code>PATH</p>
<dd> Path to the manifest.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;format-version </code>VERSION</p>
<dd> Format version [default: 1]. Valid values: 1.</p>
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
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cargo/">cargo</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> This work is dual-licensed under Apache 2.0 and MIT terms. See COPYRIGHT file in the cargo source distribution. </p>
<h2>Index</h2>
