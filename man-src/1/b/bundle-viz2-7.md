---
title: "bundle-viz2-7(1)"
name: "bundle-viz2-7"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bundle-viz2-7/"
description: "bundle-viz – Generates a visual dependency graph for your Gemfile"
---

<p><code>bundle-viz</code> &#8211; Generates a visual dependency graph for your Gemfile </p>
<h2>Synopsis</h2>
<p><code>bundle viz</code> [&#8211;file=FILE] [&#8211;format=FORMAT] [&#8211;requirements] [&#8211;version] [&#8211;without=GROUP GROUP]</p>
<h2>Description</h2>
<p><code>viz</code> generates a PNG file of the current <code><a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5)</code> as a dependency graph. <code>viz</code> requires the ruby-graphviz gem (and its dependencies). </p>
<p> The associated gems must also be installed via <code>bundle <a href="/docs/linux/man/1-install/">install</a>(1)</code> <i>bundle-install.1.html</i>.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;file</code>, <code>-f</code></p>
<dd>The name to use for the generated file. See <code>&#8211;format</code> option</p>
<dt><code>&#8211;format</code>, <code>-F</code></p>
<dd>This is output format option. Supported format is png, jpg, svg, dot &#8230;</p>
<dt><code>&#8211;requirements</code>, <code>-R</code></p>
<dd>Set to show the version of each required dependency.</p>
<dt><code>&#8211;version</code>, <code>-v</code></p>
<dd>Set to show each gem version.</p>
<dt><code>&#8211;without</code>, <code>-W</code></p>
<dd>Exclude gems that are part of the specified named group. </p>
</dl>
