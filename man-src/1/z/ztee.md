---
title: "ztee(1)"
name: "ztee"
section: "1"
letter: "z"
url: "/docs/linux/man/1-ztee/"
description: "ztee – output buffer and splitter"
---

<h2>NAME</h2>
<p> <code>ztee</code> &#8211; output buffer and splitter</p>
<h2>SYNOPSIS</h2>
<p> ztee [ OPTIONS&#8230; ] [ FILE&#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> <i>ZTee</i> is an output buffer and splitter for use with ZMap output data. ZTee should be used whenever ZMap is piped into an application scanner, placed between ZMap and the application scanner. ZTee writes the transformed output to stdout, and writes the original output to FILE. </p>
<p> See <code>&#8211;help</code> for examples.</p>
<h2>OPTIONS</h2>
<h3>BASIC OPTIONS</h3>
<dl>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd> Ignore input formatting and pass through raw input. This causes ztee to behavior identical to tee, except with buffering.</p>
<dt><code>-m</code>, <code>&#8211;monitor</code></p>
<dd> Print monitor output to stderr</p>
<dt><code>-u</code>, <code>&#8211;status-updates-file</code></p>
<dd> Write status updates (monitor data) to a file in CSV format</p>
<dt><code>-l</code>, <code>&#8211;log-file=name</code></p>
<dd> File to log to.</dl>
<h3>ADDITIONAL OPTIONS</h3>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Display help</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Display version </p>
</dl>
<h2>Index</h2>
