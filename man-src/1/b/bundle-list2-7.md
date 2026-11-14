---
title: "bundle-list2-7(1)"
name: "bundle-list2-7"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bundle-list2-7/"
description: "bundle-list – List all the gems in the bundle"
---

<p><code>bundle-list</code> &#8211; List all the gems in the bundle </p>
<h2>Synopsis</h2>
<p><code>bundle list</code> [&#8211;name-only] [&#8211;paths] [&#8211;without-group=GROUP] [&#8211;only-group=GROUP]</p>
<h2>Description</h2>
<p>Prints a list of all the gems in the bundle including their version. </p>
<p> Example: </p>
<p> bundle list &#8211;name-only </p>
<p> bundle list &#8211;paths </p>
<p> bundle list &#8211;without-group test </p>
<p> bundle list &#8211;only-group dev </p>
<p> bundle list &#8211;only-group dev &#8211;paths</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;name-only</code></p>
<dd>Print only the name of each gem.</p>
<dt><code>&#8211;paths</code></p>
<dd>Print the path to each gem in the bundle.</p>
<dt><code>&#8211;without-group</code></p>
<dd>Print all gems expect from a group.</p>
<dt><code>&#8211;only-group</code></p>
<dd>Print gems from a particular group. </p>
</dl>
