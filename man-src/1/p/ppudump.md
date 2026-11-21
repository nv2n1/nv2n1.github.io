---

title: "ppudump(1)"
name: "ppudump"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppudump/"
description: "ppudump – The FPC Pascal unit dump program."
---

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
<dt><code>-h</code></dt>
<dd> shows a short help screen.</dd>
<dt><code>-v</code><i>xxx</i></dt>
<dd> Controls the level of verbosity. <i>xxx </i> is any combination of the following letters:</dd>
<dl>
<dl>
<dt><i>a</i></dt>
<dd> Shows all information stored in the PPU file.</dd>
<dt><i>b</i></dt>
<dd> Shows the browser information in the PPU file (if present).</dd>
<dt><i>d</i></dt>
<dd> Shows the definitions in the PPU file.</dd>
<dt><i>h </i></dt>
<dd> Shows the header information in the PPU file.</dd>
<dt><i>i</i></dt>
<dd> Shows only interface information, implementation information is not shown.</dd>
<dt><i>m</i></dt>
<dd> Shows only implementation information, interface interface is not shown.</dd>
<dt><i>s</i></dt>
<dd> Shows the symbols stored in the PPU file.</dd></dl>
</dl>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>
</dt><dd> <code><a href="/docs/linux/man/1-ppc386/">ppc386</a></code>(1) <code><a href="/docs/linux/man/1-ppumove/">ppumove</a></code>(1) </dd>
</dl>
