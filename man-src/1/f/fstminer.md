---
title: "fstminer(1)"
name: "fstminer"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fstminer/"
description: "fst2miner – Data mining of FST files"
---

<h2>NAME</h2>
<p> fst2miner &#8211; Data mining of FST files</p>
<h2>SYNTAX</h2>
<p> fstminer [<i>option</i>]&#8230; [<i>FSTFILE</i>]</p>
<h2>DESCRIPTION</h2>
<p> Mines FST files for specific data values and generates gtkwave save files to stdout for future reload.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d,&#8211;dumpfile</code> &lt;<i>filename</i>&gt;</p>
<dd> Specify FST input dumpfile.</p>
<dt><code>-m,&#8211;match</code> &lt;<i>value</i>&gt;</p>
<dd> Specifies &quot;bitwise&quot; match data (binary, real, string)</p>
<dt><code>-x,&#8211;hex</code> &lt;<i>value</i>&gt;</p>
<dd> Specifies hexadecimal match data that will automatically be converted to binary for searches</p>
<dt><code>-n,&#8211;namesonly</code></p>
<dd> Indicates that only facnames should be printed in a gtkwave savefile compatible format. By doing this, the file can be used to specify which traces are to be imported into gtkwave.</p>
<dt><code>-c,&#8211;comprehensive</code></p>
<dd> Indicates that results are not to stop after the first match. This can be used to extract all the matching values in the trace.</p>
<dt><code>-h,&#8211;help</code></p>
<dd> Show help screen.</dl>
<h2>EXAMPLES</h2>
<p> fstminer dumpfile.fst &#8211;hex 20470000 -n</p>
<dl>
<dt>This attempts to match the hex value 20470000 across all facilities and when the value is encountered, the facname only is printed to stdout in order to generate a gtkwave compatible save file.</p>
<dd></dl>
<h2>LIMITATIONS</h2>
<p> <i>fstminer</i> only prints the first time a value is encountered for a specific net. This is done in order to cut down on the size of output files and to aid in following data such as addresses through a simulation model. </p>
<h2>AUTHORS</h2>
<p> Anthony Bybell &lt;bybell [at] rocketmail.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-vztminer/">vztminer</a></i>(1) <i><a href="/docs/linux/man/1-lxt2miner/">lxt2miner</a></i>(1) <i><a href="/docs/linux/man/1-fst2vcd/">fst2vcd</a></i>(1) <i><a href="/docs/linux/man/1-vcd2fst2/">vcd2fst2</a></i>(1) <i><a href="/docs/linux/man/1-gtkwave/">gtkwave</a></i>(1) </p>
<h2>Index</h2>
