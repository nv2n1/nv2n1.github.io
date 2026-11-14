---
title: "regedit(1)"
name: "regedit"
section: "1"
letter: "r"
url: "/docs/linux/man/1-regedit/"
description: "regedit – Wine registry editor"
---

<h2 class="name">NAME</h2>
<p> regedit &#8211; Wine registry editor </p>
<h2>SYNOPSIS</h2>
<p> <code>regedit</code> [<i>text file</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>regedit</code> is the Wine registry editor, designed to be compatible with its Microsoft Windows counterpart. If called without any options, it will start the full GUI editor. </p>
<p> The switches are case-insensitive and can be prefixed either by &#8216;-&#8216; or &#8216;/&#8217;.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-E</code> <i>file</i> [<i>regpath</i>]</p>
<dd> Exports the content of the specified registry key to the specified <i>file</i>. It exports the whole registry if no key is specified.</p>
<dt><code>-D</code>&nbsp;<i>regpath</p>
<dd> Deletes the specified registry key.</p>
<dt></i><code>-S</code></p>
<dd> Run regedit silently (ignored, CLI mode is always silent). This exists for compatibility with Windows regedit.</p>
<dt><code>-V</code></p>
<dd> Run regedit in advanced mode (ignored). This exists for compatibility with Windows regedit.</p>
<dt><code>-L</code>&nbsp;<i>location</p>
<dd> Specifies the location of the system.dat registry file (ignored). This exists for compatibility with Windows regedit.</p>
<dt></i><code>-R</code>&nbsp;<i>location</p>
<dd> Specifies the location of the user.dat registry file (ignored). This exists for compatibility with Windows regedit.</p>
<dt></i><code>-?</code></p>
<dd> Prints a help message. Any other options are ignored.</p>
<dt><code>-C</code>&nbsp;<i>file.reg</i></p>
<dd> Create registry from <i>file.reg</i> (unimplemented).</dl>
<h2>BUGS</h2>
<p> Bugs can be reported on the <code>Wine bug tracker</code></p>
<h2>AVAILABILITY</h2>
<p> <code>regedit</code> is part of the Wine distribution, which is available through WineHQ, the <code>Wine development headquarters</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wine/">wine</a></code>(1),<br />
 <code>Wine documentation and support</code> </p>
<h2>Index</h2>
