---
title: "lzless(1)"
name: "lzless"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lzless/"
description: "xzless, lzless – view xz or lzma compressed (text) files"
---

<h2 class="name">NAME</h2>
<p> xzless, lzless &#8211; view xz or lzma compressed (text) files </p>
<h2>SYNOPSIS</h2>
<p> <code>xzless</code> [<i>file</i>&#8230;]<br />
 <code>lzless</code> [<i>file</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>xzless</code> is a filter that displays text from compressed files to a terminal. It works on files compressed with <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1) or <code><a href="/docs/linux/man/1-lzma/">lzma</a></code>(1). If no <i>files</i> are given, <code>xzless</code> reads from standard input. </p>
<p> <code>xzless</code> uses <code><a href="/docs/linux/man/1-less/">less</a></code>(1) to present its output. Unlike <code>xzmore</code>, its choice of pager cannot be altered by setting an environment variable. Commands are based on both <code><a href="/docs/linux/man/1-more/">more</a></code>(1) and <code><a href="/docs/linux/man/1-vi/">vi</a></code>(1) and allow back and forth movement and searching. See the <code><a href="/docs/linux/man/1-less/">less</a></code>(1) manual for more information. </p>
<p> The command named <code>lzless</code> is provided for backward compatibility with LZMA Utils.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>LESSMETACHARS</code></p>
<dd> A list of characters special to the shell. Set by <code>xzless</code> unless it is already set in the environment.</p>
<dt><code>LESSOPEN</code></p>
<dd> Set to a command line to invoke the <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1) decompressor for preprocessing the input files to <code><a href="/docs/linux/man/1-less/">less</a></code>(1).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-less/">less</a></code>(1), <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1), <code><a href="/docs/linux/man/1-xzmore/">xzmore</a></code>(1), <code><a href="/docs/linux/man/1-zless/">zless</a></code>(1) </p>
<h2>Index</h2>
