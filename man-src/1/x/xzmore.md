---
title: "xzmore(1)"
name: "xzmore"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xzmore/"
description: "xzmore, lzmore – view xz or lzma compressed (text) files"
---

<h2 class="name">NAME</h2>
<p> xzmore, lzmore &#8211; view xz or lzma compressed (text) files </p>
<h2>SYNOPSIS</h2>
<p> <code>xzmore</code> [<i>file&#8230;</i>]<br />
 <code>lzmore</code> [<i>file&#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>xzmore</code> is a filter which allows examination of <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1) or <code><a href="/docs/linux/man/1-lzma/">lzma</a></code>(1) compressed text files one screenful at a time on a soft-copy terminal. </p>
<p> To use a pager other than the default <code>more,</code> set environment variable <code>PAGER</code> to the name of the desired program. The name <code>lzmore</code> is provided for backward compatibility with LZMA Utils.</p>
<dl>
<dt><code>e</code> or <code>q</code></p>
<dd> When the prompt &#8211;More&#8211;(Next file: <i>file</i>) is printed, this command causes <code>xzmore</code> to exit.</p>
<dt><code>s</code></p>
<dd> When the prompt &#8211;More&#8211;(Next file: <i>file</i>) is printed, this command causes <code>xzmore</code> to skip the next file and continue.</dl>
<p> For list of keyboard commands supported while actually viewing the content of a file, refer to manual of the pager you use, usually <code><a href="/docs/linux/man/1-more/">more</a></code>(1).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-more/">more</a></code>(1), <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1), <code><a href="/docs/linux/man/1-xzless/">xzless</a></code>(1), <code><a href="/docs/linux/man/1-zmore/">zmore</a></code>(1) </p>
<h2>Index</h2>
