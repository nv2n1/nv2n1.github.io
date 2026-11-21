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
<dt><code>-h, &#8211;help</code></dt>
<dd> Print this message.</dd>
<dl>
</dl>
<dt><code>&#8211;features </code>FEATURES</dt>
<dd> Space-separated list of features.</dd>
<dl>
</dl>
<dt><code>&#8211;all-features</code></dt>
<dd> Build all available features.</dd>
<dl>
</dl>
<dt><code>&#8211;no-default-features</code></dt>
<dd> Do not include the default feature.</dd>
<dl>
</dl>
<dt><code>&#8211;no-deps</code></dt>
<dd> Output information only about the root package and don&#8217;t fetch dependencies.</dd>
<dl>
</dl>
<dt><code>&#8211;manifest-path </code>PATH</dt>
<dd> Path to the manifest.</dd>
<dl>
</dl>
<dt><code>&#8211;format-version </code>VERSION</dt>
<dd> Format version [default: 1]. Valid values: 1.</dd>
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
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cargo/">cargo</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> This work is dual-licensed under Apache 2.0 and MIT terms. See COPYRIGHT file in the cargo source distribution. </p>
