---
title: "ttembed(1)"
name: "ttembed"
section: "1"
letter: "t"
url: "/docs/linux/man/1-ttembed/"
description: "ttembed – remove embedding restrictions from TrueType files"
---

<h2>NAME</h2>
<p> ttembed &#8211; remove embedding restrictions from TrueType files</p>
<h2>SYNOPSIS</h2>
<p> <code>ttembed</code> [<i>-n</i>] <i>fontfile</i></p>
<h2>DESCRIPTION</h2>
<p> <code>ttembed</code> sets the <code>fsType</code> field of the OS/2 table to zero and recalculates the OS/2 table&#8217;s checksum.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-n</p>
<dd> Dry-run mode, which just displays the fsType field and filename of the given fonts if it is non-zero (i.e. if <code>ttembed</code> would change it. </p>
</dl>
<h2>Index</h2>
