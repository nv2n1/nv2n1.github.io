---

title: "tla2vcd(1)"
name: "tla2vcd"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tla2vcd/"
description: "tla2vcd – Converts TLA to VCD or LST files"
---

<p> tla2vcd &#8211; Converts TLA to VCD or LST files</p>
<h2>SYNTAX</h2>
<p> tla2vcd [<i>option</i>]&#8230; <i>TLAFILE</i> [[<i>TLAFILE</i>]&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> Converts TLA files from Tektronix logic analyzers to VCD or LST files. Conversion to VCD allows viewing in tools such as <i><a href="/docs/linux/man/1-gtkwave/">gtkwave</a></i>(1).</p>
<h2>OPTIONS</h2>
<dl>
<dt>
</dt><dd> <code>-t</code> Generate text LST file instead of VCD file</dd>
<dt><code>-l</code></dt>
<dd> List the available channels/groups and exit</dd>
<dt><code>-s</code> &lt;<i>signal_list</i>&gt;</dt>
<dd> Select signals from regular expression list</dd>
<dt><code>-a</code></dt>
<dd> All channels</dd>
<dt><code>-m</code></dt>
<dd> Append MagniVu info (only in listing mode)</dd>
<dt><code>-z</code></dt>
<dd> Compress output</dd>
<dt><code>-v</code></dt>
<dd> Verbose </dd>
</dl>
<h2>AUTHORS</h2>
<p> Emil</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-lxt2vcd/">lxt2vcd</a></i>(1) <i><a href="/docs/linux/man/1-vzt2vcd/">vzt2vcd</a></i>(1) <i><a href="/docs/linux/man/1-gtkwave/">gtkwave</a></i>(1) </p>
