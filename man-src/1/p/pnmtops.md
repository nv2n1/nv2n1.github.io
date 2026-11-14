---
title: "pnmtops(1)"
name: "pnmtops"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmtops/"
description: "pnmtops – convert portable anymap to PostScript"
---

<h2 class="name">NAME</h2>
<p> pnmtops &#8211; convert portable anymap to PostScript </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmtops</code> [<code>-scale</code> <i>s</i>] [<code>-dpi</code> <i>n</i>] [<code>-imagewidth</code> <i>n</i>] [<code>-imageheight</code> <i>n</i>] [<code>-width=</code><i>N</i>] [<code>-height=</code><i>N</i>] [<code>-equalpixels</code>] [<code>-turn</code>|<code>-noturn</code>] [<code>-rle</code>|<code>-runlength</code>] [<code>-nocenter</code>] [<code>-setpage</code>] [<code>-nosetpage</code>] [<i>pnmfile</i>] </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one. You may separate an option name and its value with white space instead of an equals sign. </p>
<h2>DESCRIPTION</h2>
<p> Reads a Netpbm image as input. Produces Encapsulated PostScript as output. </p>
<p> If the input file is in color (PPM), <code>pnmtops</code> generates a color PostScript file. Some PostScript interpreters can&#8217;t handle color PostScript. If you have one of these you will need to run your image through <code>ppmtopgm</code> first. </p>
<p> If you specify no output dimensioning options, the output image is dimensioned as if you had specified <code>-scale=1.0</code>, which means aproximately 72 pixels of the input image generate one inch of output (if that fits the page). </p>
<p> Use <code>-imagewidth</code>, <code>-imageheight</code>, <code>-equalpixels</code>, <code>-width</code>, <code>-height</code>, and <code>-scale</code> to adjust that. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-imagewidth</code></p>
<dd> <code>-imageheight</code> Tells how wide and high you want the image on the page, in inches. The aspect ratio of the image is preserved, so if you specify both of these, the image on the page will be the largest image that will fit within the box of those dimensions. </p>
<p> If these dimensions are greater than the page size, you get Postscript output that runs off the page. </p>
<p> You cannot use <code>imagewidth</code> or <code>imageheight</code> with <code>-scale</code> or <code>-equalpixels</code>. </p>
<dt><code>-equalpixels</code></p>
<dd> This option causes the output image to have the same number of pixels as the input image. So if the output device is 600 dpi and your image is 3000 pixels wide, the output image would be 5 inches wide. </p>
<p> You cannot use <code>-equalpixels</code> with <code>-imagewidth</code>, <code>-imageheight</code>, or <code>-scale</code>. </p>
<dt><code>-scale</code></p>
<dd> tells how big you want the image on the page. The value is the number of inches of output image that you want 72 pixels of the input to generate. </p>
<p> But <code>pnmtops </code> rounds the number to something that is an integral number of output device pixels. E.g. if the output device is 300 dpi and you specify <code>-scale=1.0</code>, then 75 (not 72) pixels of input becomes one inch of output (4 output pixels for each input pixel). Note that the <code>-dpi</code> option tell <code>pnmtops</code> how many pixels per inch the output device generates. </p>
<p> If the size so specified does not fit on the page (as measured either by the <code>-width</code> and <code>-height</code> options or the default page size of 8.5 inches by 11 inches), <code>pnmtops</code> ignores the <code>-scale</code> option, issues a warning, and scales the image to fit on the page. </p>
<dt><code>-dpi</code></p>
<dd> This option specifies the dots per inch of your output device. The default is 300 dpi. In theory PostScript is device-independent and you don&#8217;t have to worry about this, but in practice its raster rendering can have unsightly bands if the device pixels and the image pixels aren&#8217;t in sync. </p>
<p> Also this option is crucial to the working of the <code>equalpixels</code> option. </p>
<dt><code>-width</code></p>
<dd>
 <code>-height</code> These options specify the dimensions of the page on which the output is to be printed. This can affect the size of the output image. </p>
<p> The page size has no effect, however, when you specify the <code>-imagewidth</code>, <code>-imageheight</code>, or <code>-equalpixels</code> options. </p>
<p> These options may also affect positioning of the image on the page and even the paper selected (or cut) by the printer/plotter when the output is printed. See the <code>-nosetpage</code> option. </p>
<p> The default is 8.5 inches by 11 inches. </p>
<dt><code>-turn</code></p>
<dd> <code>-noturn</code> These options control whether the image gets turned 90 degrees. Normally, if an image fits the page better when turned (e.g. the image is wider than it is tall, but the page is taller than it is wide), it gets turned automatically to better fit the page. If you specify the <code>-turn</code> option, <code>pnmtops </code> turns the image no matter what its shape; If you specify <code>-noturn</code>, <code>pnmtops</code> does <i>not</i> turn it no matter what its shape.</p>
<dt><code>-rle</code></p>
<dd> <code>-runlength</code> These identical options specify run-length compression. This may save time if the host-to-printer link is slow; but normally the printer&#8217;s processing time dominates, so <code>-rle</code> makes things slower.</p>
<dt><code>-nocenter</code></p>
<dd> By default, <code>pnmtops</code> centers the image on the output page. You can cause <code>pnmtops</code> to instead put the image against the upper left corner of the page with the <code>-nocenter </code> option. This is useful for programs which can include PostScript files, but can&#8217;t cope with pictures which are not positioned in the upper left corner. </p>
<p> For backward compatibility, <code>pnmtops</code> accepts the option <code>-center</code>, but it has no effect. </p>
<dt><code>-setpage</code></p>
<dd> <code>pnmtops </code> can generate a &quot;setpagedevice&quot; directive to tell the printer/plotter what size paper to use (or cut). The dimensions it specifies on this directive are those selected or defaulted by the <code>width</code> and <code>height</code> options or defaulted. If you want a &quot;setpagedevice&quot; directive in the output, specify <code>-setpage</code>. This can be useful if your printer chokes on this directive, which has not always been defined in Postscript, or you want to fake out the printer and print on one size paper as if you&#8217;re printing on another. </p>
<p> Before release 10.0 the default was to generate the &quot;setpagedevice&quot; directive, and there is the switch <code>-nosetpage</code> to supress it, but that&#8217;s actually a no-op now. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5), <code><a href="/docs/linux/man/1-gs/">gs</a></code>(1), <code><a href="/docs/linux/man/1-psidtopgm/">psidtopgm</a></code>(1), <code><a href="/docs/linux/man/1-pstopnm/">pstopnm</a></code>(1), <code><a href="/docs/linux/man/1-pbmtolps/">pbmtolps</a></code>(1), <code><a href="/docs/linux/man/1-pbmtoepsi/">pbmtoepsi</a></code>(1), <code><a href="/docs/linux/man/1-pbmtopsg3/">pbmtopsg3</a></code>(1), <code><a href="/docs/linux/man/1-ppmtopgm/">ppmtopgm</a></code>(1), </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989, 1991 by Jef Poskanzer.<br />
 Modified November 1993 by Wolfgang Stuerzlinger, wrzl [at] gup.uni-linz.ac.at </p>
<h2>Index</h2>
