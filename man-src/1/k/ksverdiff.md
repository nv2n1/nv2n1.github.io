---
title: "ksverdiff(1)"
name: "ksverdiff"
section: "1"
letter: "k"
url: "/docs/linux/man/1-ksverdiff/"
description: "ksverdiff — display the differences in kickstart syntax"
---

<h2>NAME</h2>
<p> ksverdiff &#8212; display the differences in kickstart syntax</p>
<h2>SYNOPSIS</h2>
<p> <code>ksverdiff</code> [<code>-f</code> | <code>&#8211;from FROMVER</code>] [<code>-t</code> | <code>&#8211;to TOVER</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>ksverdiff</code> is a program that takes two versions of kickstart syntax and lists the differences between them. It will generate a list of options added to every command since FROMVER, a list of commands added since FROMVER, a list of commands deprecated since FROMVER, and a list of commands removed since FROMVER.</p>
<h2>EXIT STATUS</h2>
<p> <code>ksverdiff</code> returns 0 on success, and 1 if either FROMVER or TOVER are invalid.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code> | <code>&#8211;from FROMVER</code></p>
<dd> The version of kickstart syntax to start with. In other words, this is the lower bound version.</p>
<dt><code>-t</code> | <code>&#8211;TO TOVER</code></p>
<dd> The version of kickstart syntax to end with. In other words, this is the upper bound version.</dl>
<h2>SEE ALSO</h2>
<p> ksflatten (1), ksvalidator (1) </p>
<h2>Index</h2>
