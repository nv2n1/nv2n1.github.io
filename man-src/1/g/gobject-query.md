---
title: "gobject-query(1)"
name: "gobject-query"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gobject-query/"
description: "gobject-query – display a tree of types"
---

<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gobject-query</code> froots [OPTION&#8230;]</dt>
<dt> <code>gobject-query</code> tree [OPTION&#8230;]</dt></dl>
<h2>DESCRIPTION</h2>
<p> <code>gobject-query</code></p>
<dd>is a small utility that draws a tree of types. </dd>
<p> <code>gobject-query</code> takes a mandatory argument that specifies whether it should iterate over the fundamental types or print a type tree.</p>
<h2>COMMANDS</h2>
<p> <code>froots</code></p>
<dl>
<dt>
</dt><dd> iterate over fundamental roots</dd></dl>
<p> <code>tree</code></p>
<dl>
<dt>
</dt><dd> print type tree</dd></dl>
<h2>OPTIONS</h2>
<p> <code>-r</code> <i>TYPE</i></p>
<dl>
<dt>
</dt><dd> specify the root type</dd></dl>
<p> <code>-n</code></p>
<dl>
<dt>
</dt><dd> don&#8217;t descend type tree</dd></dl>
<p> <code>-b</code> <i>STRING</i></p>
<dl>
<dt>
</dt><dd> specify indent string</dd></dl>
<p> <code>-i</code> <i>STRING</i></p>
<dl>
<dt>
</dt><dd> specify incremental indent string</dd></dl>
<p> <code>-s</code> <i>NUMBER</i></p>
<dl>
<dt>
</dt><dd> specify line spacing</dd></dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Print brief help and exit.</dd></dl>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dt>
</dt><dd> Print version and exit.</dd></dl>
