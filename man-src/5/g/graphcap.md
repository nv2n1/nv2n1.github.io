---
title: "graphcap(5)"
name: "graphcap"
section: "5"
letter: "g"
url: "/docs/linux/man/5-graphcap/"
description: "graphcap – A list of supported NCAR Graphics device definition files for use with the CGM interpreters ctrans and ictrans."
---

<p>graphcap &#8211; A list of supported NCAR Graphics device definition files for use with the CGM interpreters ctrans and ictrans.</p>
<h2>Description</h2>
<dl>
<dt><code>a60</code></p>
<dd>Abekas a60 raster image format.</p>
<dt><code>adm5</code></p>
<dd>ADM5 with the DEC RG1500 graphics board.</p>
<dt><code>aed.a</code></p>
<dd>AED512 in ASCII mode.</p>
<dt><code>aed.b</code></p>
<dd>AED512 in binary mode.</p>
<dt><code>avs</code></p>
<dd>Application Visualization System raster image format.</p>
<dt><code>balsml</code></p>
<dd>HI DMP-29 in small chart mode.</p>
<dt><code>ditroff</code></p>
<dd>Device-independent troff.</p>
<dt><code>form</code></p>
<dd>A blank form for user-defined graphcap definitions.</p>
<dt><code>CTXT</code></p>
<dd>Produces a human-readable ASCII dump of the input.</p>
<dt><code>hdf</code></p>
<dd>NCSA&#8217;s HDF (Hierarchical Data Format) formatted raster file.</p>
<dt><code>hp2648a</code></p>
<dd>HP2648A graphics terminal.</p>
<dt><code>hp150</code></p>
<dd>HP150 personal computer.</p>
<dt><code>hp7475a</code></p>
<dd>HP7475a six pen plotter.</p>
<dt><code>hp7510a</code></p>
<dd>HP7510a color film recorder.</p>
<dt><code>hpgl</code></p>
<dd>Basic support for the HP-GL language in its most elementary form. This graphcap is provided for older printers/plotters that do not support the full HP-GL/2 language as standardized by HP.</p>
<dt><code>hpgl2</code></p>
<dd>Support for the HP-GL/2 language as standardized by HP. Use this graphcap for devices that support HP-GL/2 but do not support either the dual context extensions (device accepts languages in addition to HP-GL/2) or the palette extensions (allows for user-defined colors).</p>
<dt><code>hpgl2.dual</code></p>
<dd>Support for the HP-GL/2 language as standardized by HP running with the dual context extensions (device accepts languages in addition to HP-GL/2). If the device also supports the palette extensions, use the hpgl2pe.dual graphcap.</p>
<dt><code>hpgl2pe</code></p>
<dd>Support for the HP-GL/2 language as standardized by HP running with the palette extensions (allows for user-defined colors). If the device also supports the dual context extensions (device accepts languages in addition to HP-GL/2), use the hpgl2pe.dual graphcap.</p>
<dt><code>hpgl2pe.dual</code></p>
<dd>Support for the HP-GL/2 language as standardized by HP running with the palette extensions (allows for user-defined colors) and the dual context extensions (device accepts languages in addition to HP-GL/2).</p>
<dt><code>hppcl</code></p>
<dd>Produces files for the HP LaserJet family of printers (LaserJet, LaserJet Plus, LaserJet Series II, LaserJet 500 Plus, etc.); hppcl is meant to replace the now obsolete hpljxxx graphcaps. The ctrans &quot;-dpi&quot; and &quot;-landscape&quot; options can be used for various resolutions and picture positioning.</p>
<dt><code>imagen</code></p>
<dd>Graphcap for the IMAGEN 8/300 laser printer in graphics landscape mode.</p>
<dt><code>imagen.port</code></p>
<dd>Graphcap for the IMAGEN 8/300 laser printer in graphics portrait mode.</p>
<dt><code>nrif</code></p>
<dd>NCAR Raster Interchange Format formatted raster file.</p>
<dt><code>pc.mono</code></p>
<dd>This graphcap is used to drive PCPLOT on IBM and compatible PC&#8217;s.</p>
<dt><code>ps.color</code></p>
<dd>Color PostScript graphcap (portrait mode).</p>
<dt><code>ps.land.color</code></p>
<dd>Color PostScript graphcap (landscape mode).</p>
<dt><code>ps.land.mono</code></p>
<dd>Black and white PostScript (landscape mode).</p>
<dt><code>ps.mono</code></p>
<dd>Black and white PostScript (portrait mode).</p>
<dt><code>qms800</code></p>
<dd>QMS800 laser printer.</p>
<dt><code>r6211</code></p>
<dd>RAMTEK 6211 in TEKTRONIX compatible mode.</p>
<dt><code>s100</code></p>
<dd>SELINAR HiREZ100 graphics terminal.</p>
<dt><code>sgi</code></p>
<dd>Silicon Graphics raster image format.</p>
<dt><code>sun</code></p>
<dd>Sun formatted raster file.</p>
<dt><code>t4010</code></p>
<dd>Tektronix 4010 and 4012.</p>
<dt><code>t4025</code></p>
<dd>TEKTRONIX 4025 graphics terminal.</p>
<dt><code>t4105</code></p>
<dd>TEKTRONIX 4105 color graphics terminal.</p>
<dt><code>t4107</code></p>
<dd>TEKTRONIX 4107 color graphics terminal.</p>
<dt><code>t4107.seg</code></p>
<dd>TEKTRONIX 4107 color graphics terminal.</p>
<dt><code>t4115</code></p>
<dd>TEKTRONIX 4115 color graphics terminal.</p>
<dt><code>t4115.seg</code></p>
<dd>TEKTRONIX 4115 color graphics terminal.</p>
<dt><code>tal1590</code></p>
<dd>Talaris 1590 plotter.</p>
<dt><code>tekalike</code></p>
<dd>TEKALIKE program on the APPLE MACINTOSH.</p>
<dt><code>versaterm</code></p>
<dd>VERSATERM program on the APPLE MACINTOSH.</p>
<dt><code>vt100</code></p>
<dd>VT100 with Digital Engeering VT640 retrofit.</p>
<dt><code>vt125</code></p>
<dd>VT125 graphics terminal.</p>
<dt><code>vt220</code></p>
<dd>VT220 with Selinar SG220 graphics retrofit board.</p>
<dt><code>vt330</code></p>
<dd>VT330 graphics terminal.</p>
<dt><code>vt340</code></p>
<dd>VT340 graphics terminal (returns with white foreground and black background).</p>
<dt><code>vt340w</code></p>
<dd>VT340 graphics terminal (returns with black foreground and white background).</p>
<dt><code>X11</code></p>
<dd>X Window System interface.</p>
<dt><code>xwd</code></p>
<dd>X11 xwd formatted raster file.</dl>
<h2>See Also</h2>
<p>Online: ctrans(1NCARG), ras_formats(1NCARG), graphc(5NCARG), ncarg_env(5NCARG) </p>
<p> Hardcopy: NCAR Graphics Fundamentals, UNIX Version; CGM, Graphcap, and Fontcap Supplement</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
