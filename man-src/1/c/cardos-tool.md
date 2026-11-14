---
title: "cardos-tool(1)"
name: "cardos-tool"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cardos-tool/"
description: "cardos-tool – displays information about Card OS-based security tokens or format them"
---

<h2 class="name">NAME</h2>
<p> cardos-tool &#8211; displays information about Card OS-based security tokens or format them </p>
<h2>SYNOPSIS</h2>
<p> <code>cardos-tool</code> [OPTIONS]</p>
<h2>DESCRIPTION</h2>
<p> The <code>cardos-tool</code> utility is used to display information about smart cards and similar security tokens based on Siemens Card/OS M4.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;info</code>, <code>-i</code></p>
<dl>
<dt>
<dd> Display information about the card or token.</dl>
<p> <code>&#8211;format</code>, <code>-f</code></p>
<dl>
<dt>
<dd> Format the card or token.</dl>
<p> <code>&#8211;reader</code> number, <code>-r</code> number</p>
<dl>
<dt>
<dd> Specify the reader number <i>number</i> to use. The default is reader 0.</dl>
<p> <code>&#8211;card-driver</code> name, <code>-c</code> driver</p>
<dl>
<dt>
<dd> Use the card driver specified by <i>name</i>. The default is to auto-detect the correct card driver.</dl>
<p> <code>&#8211;wait, -w</code></p>
<dl>
<dt>
<dd> Causes <code>cardos-info</code> to wait for the token to be inserted into reader.</dl>
<p> <code>&#8211;verbose, -v</code></p>
<dl>
<dt>
<dd> Causes <code>cardos-info</code> to be more verbose. Specify this flag several times to enable debug output in the opensc library.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-opensc/">opensc</a>(7) </p>
<h2>Index</h2>
