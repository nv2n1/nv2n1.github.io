---
title: "ppudump(1)"
name: "ppudump"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppudump/"
description: "ppudump – The FPC Pascal unit dump program."
---

<h2>NAME</h2>
<p> ppudump &#8211; The FPC Pascal unit dump program. </p>
<h2>SYNOPSIS</h2>
<p> <i>ppudump</i> [-h] [-v[h|i|m|d|s|b|a]] ppu-file1 ppufile2 &#8230; </p>
<h2>Description</h2>
<p> <code>ppudump</code> writes the contents of a Free Pascal unit file to standard output. It gives a listing of all definitions in the unit file. The format of the listing can be controlled by the options. </p>
<h2>Usage</h2>
<p> You can invoke ppudump with as arguments the names of the units that you want to dump. You need not specify a extension, by default <i>.ppu</i> is assumed. The output goes to standard output. </p>
<h2>Options</h2>
<p> <code>ppudump</code> has only two options: </p>
<dl>
<dt><code>-h</code></p>
<dd> shows a short help screen.</p>
<dt><code>-v</code><i>xxx</i></p>
<dd> Controls the level of verbosity. <i>xxx </i> is any combination of the following letters:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>a</i></p>
<dd> Shows all information stored in the PPU file.</p>
<dt><i>b</i></p>
<dd> Shows the browser information in the PPU file (if present).</p>
<dt><i>d</i></p>
<dd> Shows the definitions in the PPU file.</p>
<dt><i>h </i></p>
<dd> Shows the header information in the PPU file.</p>
<dt><i>i</i></p>
<dd> Shows only interface information, implementation information is not shown.</p>
<dt><i>m</i></p>
<dd> Shows only implementation information, interface interface is not shown.</p>
<dt><i>s</i></p>
<dd> Shows the symbols stored in the PPU file.</dl>
</dl>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>
<dd> <code><a href="/docs/linux/man/1-ppc386/">ppc386</a></code>(1) <code><a href="/docs/linux/man/1-ppumove/">ppumove</a></code>(1) </p>
</dl>
<h2>Index</h2>
