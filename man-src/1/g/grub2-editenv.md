---
title: "grub2-editenv(1)"
name: "grub2-editenv"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grub2-editenv/"
description: "grub-editenv — Manage the GRUB environment block."
---

<h2>NAME</h2>
<p> <code>grub-editenv</code> &#8212; Manage the GRUB environment block. </p>
<h2>SYNOPSIS</h2>
<p> <code>grub-editenv</code> [-v | &#8211;verbose] [<i>FILE</i>]</p>
<dl>
<dt>
<dd> &lt;create | list | set <i>NAME</i>=<i>VALUE</i> | unset <i>NAME</i>&gt; </p>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>grub-editenv</code> is a command line tool to manage GRUB&#8217;s stored environment. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;verbose</code></p>
<dd> Print verbose messages. </p>
<dt><code>FILE</code></p>
<dd>
<dl>
<dt>
<dd> File name to use for grub environment. Default is /boot/grub/grubenv .</dl>
</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>create</code></p>
<dd>
<dl>
<dt>
<dd> Create a blank environment block file.</dl>
<dt><code>list</code></p>
<dd>
<dl>
<dt>
<dd> List the current variables.</dl>
<dt><code>set</code> [<i>NAME</i>=<i>VALUE</i> &#8230;]</p>
<dd> Set variables. </p>
<dt><code>unset [</code><i>NAME</i> &#8230;]</p>
<dd> Delete variables. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code>info grub</code> </p>
<h2>Index</h2>
