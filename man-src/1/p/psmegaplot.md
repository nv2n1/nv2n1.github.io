---
title: "psmegaplot(1)"
name: "psmegaplot"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psmegaplot/"
description: "psmegaplot – To create poster-size PostScript plots from page-size plot"
---

<h2>NAME</h2>
<p> psmegaplot &#8211; To create poster-size <i>PostScript</i> plots from page-size plot</p>
<h2>SYNOPSIS</h2>
<p> <code>psmegaplot</code> <i>plotfile</i> <code>-S</code><i>scale</i> [ <code>-C</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>psmegaplot</code> reads a <code>GMT</code>-produced <i>PostScript</i> file and &#8216;blows it up&#8217; by an arbitrary scale. The result is several plots that make up the pieces in a jigsaw puzzle. Cut and paste these pieces to make a &#8216;megaplot&#8217;. </p>
<dl>
<dt><i>plotfile</i></p>
<dd> <i>PostScript</i> file as created by the <code>GMT</code> programs.</p>
<dt><code>-S</code></p>
<dd> Multiply the x- and y-dimension by <i>scale</i>. <i>scale</i> must be larger than 1.0.</dl>
<h2>OPTIONS</h2>
<p> No space between the option flag and the associated arguments.</p>
<dl>
<dt><code>-C</code></p>
<dd> Plot crop marks in each corner of every output page. [Default is no marks]</dl>
<h2>EXAMPLES</h2>
<p> To magnify a contour-map PostScript file 3 times, giving a total of 9 output pages to be pasted together, use </p>
<p> <code>psmegaplot</code> hawaii_contour.ps <code>-S</code>3 <code>-C</code> &gt; hawaii_contour_megaplot.ps</p>
<h2>BUGS</h2>
<p> This program is unlikely to work on non-<code>GMT</code>-produced <i>PostScript</i> files since it anticipates the structure of the file. It also assumes that the output media is Letter size.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gmt/">GMT</a></i>(1) </p>
<h2>Index</h2>
