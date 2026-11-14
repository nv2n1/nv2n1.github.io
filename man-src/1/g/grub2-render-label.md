---
title: "grub2-render-label(1)"
name: "grub2-render-label"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grub2-render-label/"
description: "grub-render-label — Render an Apple disk label."
---

<h2>NAME</h2>
<p> <code>grub-render-label</code> &#8212; Render an Apple disk label. </p>
<h2>SYNOPSIS</h2>
<p> <code>grub-render-label</code> [-b | &#8211;bgcolor=<i>COLOR</i>] [-c | &#8211;color=<i>COLOR</i>]</p>
<dl>
<dt>
<dd> [-f | &#8211;font=<i>FILE</i>] [-i | &#8211;input=<i>FILE</i>]</dl>
<dl>
<dt>
<dd> [-o | &#8211;output=<i>FILE</i>] [-t | &#8211;text=<i>STRING</i>]</dl>
<dl>
<dt>
<dd> [-v | &#8211;verbose] </p>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>grub-render-label</code> renders an Apple disk label (.disk_label) file. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;color</code>=<i>COLOR</i></p>
<dd> Use <i>COLOR as the color for generated labels. </p>
<dt></i><code>&#8211;bgcolor</code>=<i>COLOR</i></p>
<dd> Use <i>COLOR</i> as the background color for generated labels. </p>
<dt><code>&#8211;font</code>=<i>FILE</i></p>
<dd> Use <i>FILE</i> as the font file for generated labels. </p>
<dt>&#8211;input=<i>FILE</i></p>
<dd> Read input text from <i>FILE</i>. </p>
<dt>&#8211;output=<i>FILE</i></p>
<dd> Render output to <i>FILE</i>. </p>
<dt>&#8211;text=<i>STRING</i></p>
<dd> Use <i>STRING</i> as input text. </p>
<dt>&#8211;verbose</p>
<dd> Print verbose output. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code>info grub</code> </p>
<h2>Index</h2>
