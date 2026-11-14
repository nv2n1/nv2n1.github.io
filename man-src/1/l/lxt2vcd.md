---
title: "lxt2vcd(1)"
name: "lxt2vcd"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lxt2vcd/"
description: "lxt2vcd – Converts LXT2 files to VCD"
---

<h2>NAME</h2>
<p> lxt2vcd &#8211; Converts LXT2 files to VCD</p>
<h2>SYNTAX</h2>
<p> lxt2vcd [<i>option</i>]&#8230; [<i>LXT2FILE</i>]</p>
<h2>DESCRIPTION</h2>
<p> Converts LXT2 files to VCD files on stdout. If an output filename is not specified, the VCD is emitted to stdout. Note that &quot;regular&quot; LXT2 files will convert to VCD files with monotonically increasing time values. LXT2 files which are dumped with the &quot;partial&quot; option (to speed up access in wave viewers) will dump with monotonically increasing time values per 2k block of nets. This may be fixed in later versions of <i>lxt2vcd</i>. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l,&#8211;lxtname</code> &lt;<i>filename</i>&gt;</p>
<dd> Specify LXT2 input filename.</p>
<dt><code>-o,&#8211;output</code> &lt;<i>filename</i>&gt;</p>
<dd> Specify optional VCD output filename.</p>
<dt><code>-f,&#8211;flatearth</code></p>
<dd> Emit flattened hierarchies.</p>
<dt>
<dt><code>-n,&#8211;notruncate</code></p>
<dd>
<dd> Do not shorten bitvectors. This disables binary value compression as described in the IEEE-1364 specification. (i.e., all values except for &#8216;1&#8217; left propagate as a sign bit on vectors which do not fill up their entire declared width)</p>
<dt><code>-h,&#8211;help</code></p>
<dd> Display help then exit. </p>
</dl>
<h2>EXAMPLES</h2>
<p> To run this program the standard way type:</p>
<dl>
<dt>lxt2vcd filename.lxt</p>
<dd> The VCD conversion is emitted to stdout.</dl>
<h2>LIMITATIONS</h2>
<p> <i>lxt2vcd</i> does not re-create glitches as these are coalesced together into one value change during the writing of the LXT2 file. </p>
<h2>AUTHORS</h2>
<p> Anthony Bybell &lt;bybell [at] rocketmail.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-vcd2lxt2/">vcd2lxt2</a></i>(1) <i><a href="/docs/linux/man/1-vcd2lxt/">vcd2lxt</a></i>(1) <i><a href="/docs/linux/man/1-gtkwave/">gtkwave</a></i>(1) </p>
<h2>Index</h2>
