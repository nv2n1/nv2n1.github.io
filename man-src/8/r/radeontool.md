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
<dt><code>dac [on|off]</code></dt>
<dd>Power down the external video output</dd>
<dt><code>light [on|off]</code></dt>
<dd>Power down the backlight</dd>
<dt><code>stretch [on|off|vert|horiz|auto|manual]</code></dt>
<dd>Adjusts stretching for resolution mismatch</dd>
<dt><code>regs</code></dt>
<dd>Show a listing of some random registers</dd>
<dt><code>regmatch [pattern]</code></dt>
<dd>Show registers matching wildcard pattern</dd>
<dt><code>regset [pattern] [value]</code></dt>
<dd>Set registers matching wildcard pattern</dd></dl>
<h2>Options</h2>
<p>These programs follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>&#8211;debug</code></dt>
<dd>Show a little debug info</dd>
<dt><code>&#8211;skip=n</code></dt>
<dd>Skips the first n cards and acts on the n+1</dd></dl>
<h2>Author</h2>
<p>This manual page was written by Luigi Gangitano luigi [at] debian.org for the <code>Debian</code> system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 any later version published by the Free Software Foundation.<br/>
&nbsp;<wbr> </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.<br/>
&nbsp;<wbr></p>
