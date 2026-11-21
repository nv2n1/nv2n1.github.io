---
title: "dmtxread(1)"
name: "dmtxread"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dmtxread/"
description: "dmtxread – scan Data Matrix barcodes"
---

<h2>NAME</h2>
<p> dmtxread &#8211; scan Data Matrix barcodes</p>
<h2>SYNOPSIS</h2>
<p> <code>dmtxread</code> [<i>options</i>] [<i>FILE</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>dmtxread</code> searches the named input FILEs (or standard input if no files are named or the filename &quot;-&quot; is given) for ECC200 Data Matrix barcodes, reads their contents, and writes the decoded messages to standard output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;codewords</code></dt>
<dd> Only print the codewords extracted from a Data Matrix, and not the actual decoded message.</dd>
<dt><code>-e</code>, <code>&#8211;minimum-edge=</code><i>N</i></dt>
<dd> Pixel length of smallest expected edge in image.</dd>
<dt><code>-E</code>, <code>&#8211;maximum-edge=</code><i>N</i></dt>
<dd> Pixel length of largest expected edge in image.</dd>
<dt><code>-g</code>, <code>&#8211;gap</code>=<i>N</i></dt>
<dd> Use scan grid with gap of <i>N</i> pixels (or less) between lines.</dd>
<dt><code>-l</code>, <code>&#8211;list-formats</code></dt>
<dd> List the supported input image formats.</dd>
<dt><code>-m</code>, <code>&#8211;milliseconds</code>=<i>N</i></dt>
<dd> Stop scan after N milliseconds (per image).</dd>
<dt><code>-n</code>, <code>&#8211;newline</code></dt>
<dd> Print a newline character at the end of decoded data.</dd>
<dt><code>-p</code>, <code>&#8211;page</code>=<i>N</i></dt>
<dd> Only scan Nth page of images.</dd>
<dt><code>-q</code>, <code>&#8211;square-deviation</code>=<i>N</i></dt>
<dd> Maximum deviation (degrees) from squareness between adjacent barcode sides. Default value is N=40, but N=10 is recommended for flat applications like faxes and other scanned documents. Barcode regions found with corners &lt;(90-N) or &gt;(90+N) will be ignored by the decoder.</dd>
<dt><code>-r</code>, <code>&#8211;resolution</code>=<i>N</i></dt>
<dd> Decoding resolution in dots per inch (DPI). Only used for vectorial input images such as SVG, PDF, etc&#8230; This option accepts a single argument (eg: 300) as well as horizontal and vertical resolutions (eg: 300&#215;150). The default resolution is 72dpi.</dd>
<dt><code>-s</code>, <code>&#8211;symbol-size</code>=<i>[asr|RxC]</i></dt>
<dd> Only consider barcodes of specific size or shape.<br />
a&nbsp;<wbr>=&nbsp;<wbr>All sizes&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[default]<br />
s&nbsp;<wbr>=&nbsp;<wbr>Only squares<br />
r&nbsp;<wbr>=&nbsp;<wbr>Only rectangles<br />
&nbsp;<wbr>RxC&nbsp;<wbr>=&nbsp;<wbr>Exactly this many rows and columns&nbsp;<wbr>(10&#215;10, 8&#215;18, etc&#8230;)</dd>
<dt><code>-t</code>, <code>&#8211;threshold</code>=<i>N</i></dt>
<dd> Set the minimum edge threshold as a percentage of maximum. For example, an edge between a pure white and pure black pixel would have an intensity of 100. Edges with intensities below the indicated threshold will be ignored by the decoding process. Lowering the threshold will increase the amount of work to be done, but may be necessary for low contrast or blurry images.</dd>
<dt><code>-x</code>, <code>&#8211;x-range-min</code>=<i>N[%]</i></dt>
<dd> Do not scan pixels to the left of pixel column N (or N%).</dd>
<dt><code>-X</code>, <code>&#8211;x-range-max</code>=<i>N[%]</i></dt>
<dd> Do not scan pixels to the right of pixel column N (or N%).</dd>
<dt><code>-y</code>, <code>&#8211;y-range-min</code>=<i>N[%]</i></dt>
<dd> Do not scan pixels above pixel row N (or N%).</dd>
<dt><code>-Y</code>, <code>&#8211;y-range-max</code>=<i>N[%]</i></dt>
<dd> Do not scan pixels below pixel row N (or N%).</dd>
<dt><code>-C</code>, <code>&#8211;corrections-max</code>=<i>N</i></dt>
<dd> Correct at most N errors per image (0 = correction disabled).</dd>
<dt><code>-D</code>, <code>&#8211;diagnose</code></dt>
<dd> Make copy of image with additional diagnostic data.</dd>
<dt><code>-M</code>, <code>&#8211;mosaic</code> (experimental)</dt>
<dd> Interpret detected regions as Data Mosaic barcodes.</dd>
<dt><code>-N</code>, <code>&#8211;stop-after</code>=<i>N</i></dt>
<dd> Stop scanning after Nth barcode is returned.</dd>
<dt><code>-P</code>, <code>&#8211;page-numbers</code></dt>
<dd> Print each decoded message with its fax/tiff page number.</dd>
<dt><code>-R</code>, <code>&#8211;corners</code></dt>
<dd> Prefix the decoded message with the barcode&#8217;s corner locations.</dd>
<dt><code>-S</code>, <code>&#8211;shrink</code>=<i>N</i></dt>
<dd> Internally shrink image by factor of N. Shrinking is accomplished by skipping N-1 pixels at a time, often producing significantly faster scan times. It also improves scan success rate for images taken with poor camera focus provided the image is sufficiently large.</dd>
<dt><code>-U</code>, <code>&#8211;unicode</code></dt>
<dd> Print Extended ASCII characters in UTF-8 Unicode.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Use verbose messages.</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Print program version information.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Display this help message and quit.</dd></dl>
<h2>STANDARDS</h2>
<p> ISO/IEC 16022:2000 </p>
<p> ANSI/AIM BC11 ISS</p>
<h2>DIAGNOSTICS</h2>
<p> Exit status has following possible meanings:<br />
0&nbsp;<wbr>&nbsp;<wbr>At least one barcode was found and decoded<br />
1&nbsp;<wbr>&nbsp;<wbr>No barcodes were found<br />
&nbsp;<wbr>&nbsp;<wbr>&gt;1&nbsp;<wbr>&nbsp;<wbr>Error occurred that prevented command from executing normally</p>
<h2>BUGS</h2>
<p> Email bug reports to <i>mike [at] dragonflylogic.com</i></p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2008, 2009 Mike Laughton </p>
