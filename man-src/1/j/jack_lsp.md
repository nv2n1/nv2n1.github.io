---
title: "jack_lsp(1)"
name: "jack_lsp"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jack_lsp/"
description: "jack_lsp – JACK toolkit client to list informtion on ports"
---

<h2>NAME</h2>
<p> jack_lsp &#8211; JACK toolkit client to list informtion on ports</p>
<h2>SYNOPSIS</h2>
<p> <code>jack_lsp</code> [ <i>-s</i> | <i>&#8211;server</i> servername ] [ <i>-AclLptvh</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>jack_lsp</code> lists all known ports associated with a JACK server. It can also optionally list various kinds of information about each port.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-s</code>, <code>&#8211;server</code> <i>servername</i></p>
<dd>
 Connect to the jack server named <i>servername</i></p>
<dt><code>-A</code>, <code>&#8211;aliases</code></p>
<dd>
 List aliases for each port</p>
<dt><code>-c</code>, <code>&#8211;connections</code></p>
<dd>
 List connections to/from each port</p>
<dt><code>-l</code>, <code>&#8211;latency</code></p>
<dd>
 Display per-port latency in frames at each port</p>
<dt><code>-L</code>, <i>&#8211;latency</i></p>
<dd>
 Display total latency in frames at each port</p>
<dt><code>-p</code>, <code>&#8211;properties</code></p>
<dd>
 Display port properties. Output may include input|output, can-monitor, physical, terminal</p>
<dt><code>-t</code>, <code>&#8211;type</code></p>
<dd>
 Display port type</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>
 Display help/usage message</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd>
 Output version information and exit </p>
</dl>
<h2>Index</h2>
