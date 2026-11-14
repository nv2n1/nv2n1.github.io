---
title: "intel_reg_dumper(1)"
name: "intel_reg_dumper"
section: "1"
letter: "i"
url: "/docs/linux/man/1-intel_reg_dumper/"
description: "intel_reg_dumper – Decode a bunch of Intel GPU registers for debugging"
---

<h2>NAME</h2>
<p> intel_reg_dumper &#8211; Decode a bunch of Intel GPU registers for debugging</p>
<h2>SYNOPSIS</h2>
<p> <code>intel_reg_dumper [ options ] [ file ]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>intel_reg_dumper</code> is a tool to read and decode the values of many Intel GPU registers. It is commonly used in debugging video mode setting issues. If the <code>file</code> argument is present, the registers will be decoded from the given file instead of the current registers. Use the <code>intel_reg_snapshot</code> tool to generate such files. </p>
<p> When the <code>file</code> argument is present and the <code>-d</code> argument is not present, <code>intel_reg_dumper</code> will assume the file was generated on an Ironlake machine.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d id</code></p>
<dd> when a dump file is used, use &#8216;id&#8217; as device id (in hex)</p>
<dt><code>-h</code></p>
<dd> prints a help message</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-intel_reg_snapshot/">intel_reg_snapshot</a>(1)</code> </p>
<h2>Index</h2>
