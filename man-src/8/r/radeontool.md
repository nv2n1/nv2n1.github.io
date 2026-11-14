---
title: "radeontool(8)"
name: "radeontool"
section: "8"
letter: "r"
url: "/docs/linux/man/8-radeontool/"
description: "radeontool — utility to get/set registers and to control backlight on radeon based laptops"
---

<p>radeontool &#8212; utility to get/set registers and to control backlight on radeon based laptops</p>
<h2>Synopsis</h2>
<p><code>radeontool</code> [<i>option</i>] [<i>command</i>]</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>radeontool</code> command. </p>
<p> This manual page was written for the <code>Debian</code> distribution because the original program does not have a manual page. </p>
<p> <code>radeontool</code> is a program that switches on/off backlight and external output on ATI Radeon based laptops, and is able to list or set register values.</p>
<h2>Commands</h2>
<p>You can specify one of the following commands:</p>
<dl>
<dt><code>dac [on|off]</code></p>
<dd>Power down the external video output</p>
<dt><code>light [on|off]</code></p>
<dd>Power down the backlight</p>
<dt><code>stretch [on|off|vert|horiz|auto|manual]</code></p>
<dd>Adjusts stretching for resolution mismatch</p>
<dt><code>regs</code></p>
<dd>Show a listing of some random registers</p>
<dt><code>regmatch [pattern]</code></p>
<dd>Show registers matching wildcard pattern</p>
<dt><code>regset [pattern] [value]</code></p>
<dd>Set registers matching wildcard pattern</dl>
<h2>Options</h2>
<p>These programs follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>&#8211;debug</code></p>
<dd>Show a little debug info</p>
<dt><code>&#8211;skip=n</code></p>
<dd>Skips the first n cards and acts on the n+1</dl>
<h2>Author</h2>
<p>This manual page was written by Luigi Gangitano luigi [at] debian.org for the <code>Debian</code> system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 any later version published by the Free Software Foundation.<br />
&nbsp;<wbr> </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.<br />
&nbsp;<wbr></p>
