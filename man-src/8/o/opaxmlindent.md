---
title: "opaxmlindent(8)"
name: "opaxmlindent"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opaxmlindent/"
description: "opaxmlindent"
---

<p>opaxmlindent </p>
<p> <code>(Linux)</code> Takes well-formed XML as input, filters out comments, and generates a uniformly-indented equivalent XML file. Use opaxmlindent to reformat files for easier reading and review, also to reformat a file for easy comparison with diff.</p>
<h2>Syntax</h2>
<p>opaxmlindent [-t|-k] [-i <i>indent</i>] [ <i>input_file</i>]</p>
<h2>Options</h2>
<dl>
<dt>-t</p>
<dd>Trims leading and trailing whitespace in tag contents. </p>
<dt>-k</p>
<dd>In tags with purely whitespace that contain newlines, keep newlines as-is. Default is to format as an empty list. </p>
<dt>-i <i>indent</i></p>
<dd>Sets indentation to use per level. Default is 4. </p>
<dt>
&nbsp;<wbr><i>input_file</i>&nbsp;<wbr></p>
<dd>XML file to read. Default is stdin. </p>
</dl>
