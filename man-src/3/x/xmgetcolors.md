---
title: "xmgetcolors(3)"
name: "xmgetcolors"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmgetcolors/"
---

<b>XmGetColors</b> --- A function that generates foreground, select, and shadow colors
<h2>Synopsis</h2><pre>#include &lt;Xm/Xm.h&gt;
<b>void XmGetColors</b>(
<b>Screen * screen</b>,
<b>Colormap colormap</b>,
<b>Pixel background</b>,
<b>Pixel * foreground</b>,
<b>Pixel * top_shadow</b>,
<b>Pixel * bottom_shadow</b>,
<b>Pixel * select</b>);</pre><h2>Description</h2><b>XmGetColors</b> takes a screen, a colormap, and a background pixel, and returns pixel values for foreground, select, and shadow colors.
<dl COMPACT><dt><i>screen</i>
<dd>Specifies the screen for which these colors should be allocated.
<dt><i>colormap</i>
<dd>Specifies the colormap from which these colors should be allocated.
<dt><i>background</i>
<dd>Specifies the background on which the colors should be based.
<dt><i>foreground</i>
<dd>Specifies a pointer to the returned foreground pixel value. If this argument is NULL, no value is allocated or returned for this color.
<dt><i>top_shadow</i>
<dd>Specifies a pointer to the returned top shadow pixel value. If this argument is NULL, no value is allocated or returned for this color.
<dt><i>bottom_shadow</i>
<dd>Specifies a pointer to the returned bottom shadow pixel value. If this argument is NULL, no value is allocated or returned for this color.
<dt><i>select</i>
<dd>Specifies a pointer to the returned select pixel value. If this argument is NULL, no value is allocated or returned for this color.</dl><h2>Related</h2><b><a HREF="/docs/linux/man/3-xmchangecolor/">XmChangeColor</a></b>(3), <b><a HREF="/docs/linux/man/3-xmgetcolorcalculation/">XmGetColorCalculation</a></b>(3), and <b><a HREF="/docs/linux/man/3-xmsetcolorcalculation/">XmSetColorCalculation</a></b>(3).
