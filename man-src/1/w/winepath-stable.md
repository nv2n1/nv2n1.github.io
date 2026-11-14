---
title: "winepath-stable(1)"
name: "winepath-stable"
section: "1"
letter: "w"
url: "/docs/linux/man/1-winepath-stable/"
description: "winepath – Tool to convert Unix paths to/from Win32 paths"
---

<h2 class="name">NAME</h2>
<p> winepath &#8211; Tool to convert Unix paths to/from Win32 paths </p>
<h2>SYNOPSIS</h2>
<p> <code>winepath</code> <i>option </i>{<i>path</i>}</p>
<h2>DESCRIPTION</h2>
<p> <code>winepath</code> is a tool to convert a Unix path to/from a Win32 (short/long) path compatible with its Microsoft Windows counterpart. </p>
<p> If more than one option is given then the input paths are output in all formats specified, in the order long, short, Unix, Windows. If no option is given the default output is Unix format.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-u</code>,<code>&nbsp;&#8211;unix</p>
<dd> converts a Windows path to a Unix path.</p>
<dt>-w</code>,<code>&nbsp;&#8211;windows</p>
<dd> converts a Unix path to a long Windows path.</p>
<dt>-l</code>,<code>&nbsp;&#8211;long</p>
<dd> converts the short Windows path of an existing file or directory to the long format.</p>
<dt>-s</code>,<code>&nbsp;&#8211;short</p>
<dd> converts the long Windows path of an existing file or directory to the short format.</p>
<dt>-0</p>
<dd> separate output with 
