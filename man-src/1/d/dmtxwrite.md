---
title: "dmtxwrite(1)"
name: "dmtxwrite"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dmtxwrite/"
description: "dmtxwrite – create Data Matrix barcodes"
---

<h2>NAME</h2>
<p> dmtxwrite &#8211; create Data Matrix barcodes</p>
<h2>SYNOPSIS</h2>
<p> <code>dmtxwrite</code> [<i>OPTION</i>]&#8230; [FILE]</p>
<h2>DESCRIPTION</h2>
<p> <code>dmtxwrite</code> encodes data from a file or standard input, and writes the resulting ECC200 Data Matrix barcode as an image.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;codewords</code></p>
<dd> Print codeword listing instead of creating barcode.</p>
<dt><code>-d</code>, <code>&#8211;module</code>=<i>N</i></p>
<dd> Module size in pixels.</p>
<dt><code>-m</code>, <code>&#8211;margin</code>=<i>N</i></p>
<dd> Margin size in pixels.</p>
<dt><code>-e</code>, <code>&#8211;encoding</code>=[bfactxe8]</p>
<dd> Encodation scheme.<br />
b&nbsp;<wbr>=&nbsp;<wbr>Best optimized&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>best possible optimization&nbsp;<wbr>(beta)<br />
f&nbsp;<wbr>=&nbsp;<wbr>Fast optimized&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>basic optimization&nbsp;<wbr>(not implemented)<br />
a&nbsp;<wbr>=&nbsp;<wbr>ASCII&nbsp;<wbr>&nbsp;<wbr>[default]&nbsp;<wbr>ASCII standard&nbsp;<wbr>&amp;&nbsp;<wbr>extended<br />
c&nbsp;<wbr>=&nbsp;<wbr>C40&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>digits and uppercase<br />
t&nbsp;<wbr>=&nbsp;<wbr>Text&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>digits and lowercase<br />
x&nbsp;<wbr>=&nbsp;<wbr>X12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ANSI X12 EDI<br />
e&nbsp;<wbr>=&nbsp;<wbr>EDIFACT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ASCII values 32-94<br />
8&nbsp;<wbr>=&nbsp;<wbr>Base 256&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>all byte values 0-255</p>
<dt><code>-f</code>, <code>&#8211;format</code>=<i>FORMAT</i></p>
<dd> Output image format (PNG [default], TIF, GIF, PDF, etc&#8230;).</p>
<dt><code>-l</code>, <code>&#8211;list-formats</code></p>
<dd> List available image formats.</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>FILE</i></p>
<dd> Barcode output filename. Default is standard output.</p>
<dt><code>-p</code>, <code>&#8211;preview</code></p>
<dd> Print ASCII art preview to standard output.</p>
<dt><code>-r</code>, <code>&#8211;resolution</code>=<i>N</i></p>
<dd> Set image print resolution (dpi).</p>
<dt><code>-s</code>, <code>&#8211;symbol-size</code>=[sr|RxC] (default &quot;s&quot;)</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>Automatic symbol size options:<br />
&nbsp;<wbr>s&nbsp;<wbr>=&nbsp;<wbr>Auto square&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r&nbsp;<wbr>=&nbsp;<wbr>Auto rectangle<br />
&nbsp;<wbr>&nbsp;<wbr>Manual symbol size options for square symbols:<br />
&nbsp;<wbr>10&#215;10&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>12&#215;12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>14&#215;14&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>16&#215;16&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>18&#215;18&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>20&#215;20<br />
&nbsp;<wbr>22&#215;22&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>24&#215;24&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>26&#215;26&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>32&#215;32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>36&#215;36&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>40&#215;40<br />
&nbsp;<wbr>44&#215;44&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>48&#215;48&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>52&#215;52&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>64&#215;64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>72&#215;72&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>80&#215;80<br />
&nbsp;<wbr>88&#215;88&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>96&#215;96 104&#215;104 120&#215;120 132&#215;132 144&#215;144<br />
&nbsp;<wbr>&nbsp;<wbr>Manually symbol size options for rectangle symbols:<br />
&nbsp;<wbr>&nbsp;<wbr>8&#215;18&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>8&#215;32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>12&#215;26&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>12&#215;36&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>16&#215;36&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>16&#215;48</p>
<dt><code>-C</code>, <code>&#8211;color</code>=<i>COLOR</i></p>
<dd> Barcode color (not implemented).</p>
<dt><code>-B</code>, <code>&#8211;bg-color</code>=<i>COLOR</i></p>
<dd> Background color (not implemented).</p>
<dt><code>-M</code>, <code>&#8211;mosaic</code></p>
<dd> Create non-standard Data Mosaic barcode.</p>
<dt><code>-R</code>, <code>&#8211;rotate</code>=<i>DEGREES</i></p>
<dd> Rotation angle in degrees (not implemented).</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Use verbose messages.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print program version information.</p>
<dt><code>&#8211;help</code></p>
<dd> Display this help message and quit.</dl>
<h2>STANDARDS</h2>
<p> ISO/IEC 16022:2000 </p>
<p> ANSI/AIM BC11 ISS</p>
<h2>BUGS</h2>
<p> Email bug reports to <i>mike [at] dragonflylogic.com</i></p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2008, 2009 Mike Laughton </p>
<h2>Index</h2>
