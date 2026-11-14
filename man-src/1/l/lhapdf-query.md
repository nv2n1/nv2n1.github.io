---
title: "lhapdf-query(1)"
name: "lhapdf-query"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lhapdf-query/"
description: "lhapdf-query – Query PDF values from LHAPDF"
---

<h2>NAME</h2>
<p> lhapdf-query &#8211; Query PDF values from LHAPDF</p>
<h2>SYNOPSIS</h2>
<p> <code>lhapdf-query</code> [cmd] [setname|num] [memnum] x Q [flavourID]</p>
<h2>DESCRIPTION</h2>
<p> Retrieve PDF values from LHAPDF, given a set name, member number and values for x and Q. This will return a list of xf(x,Q2) values for each parton; specifying a parton name on the command line will return the single appropriate xf(x,Q2) value for that flavour.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show this help message and exit</p>
<dt><code>-Q</code>, <code>&#8211;quiet</code></p>
<dd> Suppress normal messages</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd> Add extra debug messages</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Lifeng Sun &lt;lifongsun [at] gmail.com&gt; for the Debian system (but may be used by others). </p>
<h2>Index</h2>
