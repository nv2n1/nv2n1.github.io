---

title: "mimedefang-util(1)"
name: "mimedefang-util"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mimedefang-util/"
description: "mimedefang-util — Utility script for message structure debugging"
---

<p> mimedefang-util &#8212; Utility script for message structure debugging </p>
<h2>SYNOPSIS</h2>
<pre>
    # Print a &quot;pretty&quot; version of an input message
    mimedefang-util --prettyprint &lt; input.msg
    # Print the message structure
    mimedefang-util --structure &lt; input.msg
    # Parse and re-MIME the message
    mimedefang-util --dump &lt; input.msg
</pre>
<h2>DESCRIPTION</h2>
<p> This script provides some debug tools formerly provided as part of mimedefang.pl</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;prettyprint</code></dt>
<dd> Parses a mail message from standard input and reformats it in a &#8220;pretty&#8221; format on standard output. All text/* parts are printed directly, and non-text parts are described without printing their content.</dd>
<dt><code>&#8211;structure</code></dt>
<dd> Parses a mail message from standard input, and outputs a description of the MIME tree to standard output.</dd>
<dt><code>&#8211;dump</code></dt>
<dd> Parses a mail message from standard input, and dumps the parsed message back out again to standard output.</dd>
<dt><code>&#8211;data-dump</code></dt>
<dd> Parses a mail message from standard input, and dumps the parsed message back out again to standard output using Data::Dumper</dd>
<dt><code>&#8211;help</code></dt>
<dd> This help</dd>
<dt><code>&#8211;man</code></dt>
<dd> Full manpage</dd></dl>
<h2>LICENSE AND COPYRIGHT</h2>
<p> Copyright (C) 2010 Roaring Penguin Software Inc. </p>
<p> This program may be distributed under the terms of the GNU General Public License, Version 2, or (at your option) any later version. </p>
