---
title: "ras_palette(5)"
name: "ras_palette"
section: "5"
letter: "r"
url: "/docs/linux/man/5-ras_palette/"
---

<h2><code>NAME</code></h2>
<p>ras_palette &#8211; format descriptions for palette files for NCAR View</p>
<h2><code>SYNOPSIS</code></h2>
<pre>palette_file.pal
palette_file.txt</pre>
<h2><code>DESCRIPTION</code></h2>
<p>NCAR View supports a binary as well as a textual format for color palettes. </p>
<p> The binary format is compatible with NCSA HDF and must have a file extension of &quot;.pal&quot;. The palette has a red, a green, and a blue table, each with 256 single unsigned byte entries. A 0 represents no intensity for a given color, and a 255 full intensity. In the file, the palette is stored as: </p>
<pre><i>R0 R1 ... R255 G0 G1 ... G255 B0 B1 ... B255</i></pre>
<p>for a total of 768 bytes. </p>
<p> The textual format can be created by a program or manually with a text editor. It provides for 256 RGB entries but also allows for a sparse color table. In the latter case, missing values are calculated from those provided using linear interpolation. If unspecified, the 0 entry defaults to black and the 255 entry to white. Each color palette entry has the following format: </p>
<pre><i>index_number red green blue</i></pre>
<p>where <i>index_number</i>, <i>red</i>, <i>green</i>, and <i>blue</i> are all integers in the range 0 to 255.</p>
<h2><code>EXAMPLES</code></h2>
<p>All of the examples below deal with textual color palettes.</p>
<dl>
<dt>Setting Entries</p>
<dd>
<dd>Set color index 0 to black. </p>
<pre>0 0 0 0</pre>
<dd>Set color index 255 to white </p>
<pre>255 255 255 255</pre>
<dt>Grayscale Ramp</p>
<dd>
<dd>Let&#8217;s suppose you have a file named &quot;my.txt&quot; and it has just two lines in it: the black entry and the white entry from above. This will produce a grayscale color palette, where the table starts at black and ramps up to white; since only entries 0 and 255 are specified, the remaining indicies are interpolated. </p>
<pre>0 0 0 0
255 255 255 255</pre>
<dd>(<i>Note</i>: An empty palette file (e.g. &quot;empty.txt&quot;) is legal and, since the 0 index defaults to black and the 255 index to white, produces a grayscale ramp just as in the above example.)</p>
<dt>Temperature Color Scale</p>
<dd>
<dd>Let&#8217;s suppose you want entry 0 to be black, and the remaining indices to start at 1 with a fully-saturated blue and shift linearly to 255 with a fully-saturated red. Only three entries are required in your file, &quot;temp.txt&quot;. </p>
<pre>0 0 0 0
1 0 0 255
255 255 0 0</pre>
</dl>
<h2><code>SEE ALSO</code></h2>
<p><code>rasview</code>(1NCARG),<code>rascat</code>(1NCARG),<code>rasgetpal</code>(1NCARG), <code>rassplit</code>(1NCARG),<code>rasls</code>(1NCARG),<code>ras_formats</code>(5NCARG)</p>
<h2><code>BUGS/CAVEATS</code></h2>
<p>Color palettes are only useful with indexed-color imagery.</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research </p>
<p> The use of this Software is governed by a License Agreement.</p>
