---
title: "pamtowinicon(1)"
name: "pamtowinicon"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamtowinicon/"
description: "pamtowinicon – convert Netpbm PAM images to a Microsoft Windows icon file"
---

<h2 class="name">NAME</h2>
<p> pamtowinicon &#8211; convert Netpbm PAM images to a Microsoft Windows icon file</p>
<h2>SYNOPSIS</h2>
<p> <code>pamtowinicon</code> [<code>-pngthreshold=</code><i>threshold</i>] [<code>-truetransparent</code>] [<code>-verbose</code>] [<i>pam_file</i>] </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one to designate an option. You may use either white space or equals signs between an option name and its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamtowinicon</code> reads an RGB_ALPHA Netpbm PAM file and converts it to a Microsoft Windows icon file. </p>
<p> The output goes to Standard Output. </p>
<p> The input is a multi-image PAM file; each image becomes an icon in the output file. If you have input images in multiple files, you can simply combine them with <code>cat</code> and pass the result to <code>pamtowinicon</code>. </p>
<h2>OPTIONS</h2>
<p> In addition to the options common to all programs based on libnetpbm (most notably <code>-quiet</code>, see Common Options ), <code>pamtowinicon</code> recognizes the following command line options: </p>
<dl>
<dt><code>-pngthreshold=</code><i>threshold</i></p>
<dd> <code>pamtowinicon</code> encodes images with resolutions above or equal <i>threshold</i> by <i>threshold</i> as PNG by running <code><a href="/docs/linux/man/1-pnmtopng/">pnmtopng</a></code>(1) using the more traditional BMP format. </p>
<p> When the program uses PNG encoding for a 5-channel PAM with separate AND mask (see below), it discards the AND mask. </p>
<p> The default value for <i>threshold</i> is 128. </p>
<dt><code>-truetransparent</code></p>
<dd> Make all pixels outside the opaque area black, avoiding inversion and other effects on the background of the image (see <code>Windows</code><a href="/docs/linux/man/1-icons/">Icons</a><code>(1)</code> ). </p>
<dt><code>-verbose</code></p>
<dd> Print more messages </p>
</dl>
<h2>IMAGES</h2>
<p> <code>pamtowinicon</code> reads a (multi-image) Netpbm PAM file as input and outputs an single Windows icon file containing those images. </p>
<p> The images in the icon file are in the same order as in the PAM input. </p>
<h3>PAM Input</h3>
<p> <code>pamtowinicon</code> interprets the PAM images as follows, based on the number of channels. </p>
<p> &lt;TABLE summary=&quot;Image type based on number of channels&quot; border=1 align=&quot;center&quot;&gt; &lt;TR&gt;&lt;TH&gt;channels&lt;/TH&gt;&lt;TH&gt;image&lt;/TH&gt;&lt;/TR&gt; &lt;TR&gt;&lt;TD&gt;1&lt;/TD&gt;&lt;TD&gt;fully opaque grayscale image&lt;/TD&gt;&lt;/TR&gt; &lt;TR&gt;&lt;TD&gt;2&lt;/TD&gt;&lt;TD&gt;grayscale image with alpha channel&lt;/TD&gt;&lt;/TR&gt; &lt;TR&gt;&lt;TD&gt;3&lt;/TD&gt;&lt;TD&gt;fully opaque color image&lt;/TD&gt;&lt;/TR&gt; &lt;TR&gt;&lt;TD&gt;4&lt;/TD&gt;&lt;TD&gt;color image with alpha channel&lt;/TD&gt;&lt;/TR&gt; &lt;TR&gt;&lt;TD&gt;5&lt;/TD&gt;&lt;TD&gt;color image with alpha channel and additional AND mask&lt;/TD&gt;&lt;/TR&gt; &lt;/TABLE&gt; </p>
<p> The tuple types of the PAMs are irrelevant. </p>
<h3>AND Mask</h3>
<p> The so-called &amp;lsquo;AND mask&amp;rsquo; is a special feature of Microsoft Windows icons. It is required for all BMP encoded images. At the first sight, the AND mask is a 1-bit alpha channel, but it is also used for e.g. shading the icon while dragging. See <code>Windows</code><a href="/docs/linux/man/1-icons/">Icons</a><code>(1)</code><br />
&nbsp;<wbr>for details. </p>
<p> If there is no explicit AND mask, but transparency data in the input image, <code>pamtowinicon</code> sets the AND mask to opaque where the sample in the alpha channel is below maxval, and to transparent elsewhere. </p>
<p> If no transparency data is present in the input image, <code>pamtowinicon</code> assumes the whole image to be fully opaque. </p>
<h3>BMP Output</h3>
<p> When BMP encoding an image, <code>pamtowinicon</code> tries to use the most compact <code>BI_RGB</code> format allowed for icon images with a color depth of eight bits per channel. </p>
<p> <code>pamtowinicon</code> generates neither 16-bit <code>BI_RGB</code> nor <code>BI_BITFIELDS</code> BMP encoded images, even if the maxval of the input PAM is not 255. </p>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-winicontopam/">winicontopam</a></code>(1) </p>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-ppmtowinicon/">ppmtowinicon</a></code>(1) </p>
<dt>&bull;</p>
<dd>
<p> <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) </p>
<dt>&bull;</p>
<dd>
<p> <code>Windows</code><a href="/docs/linux/man/1-icons/">Icons</a><code>(1)</code> </p>
</dl>
<p> For information on the PNG format, see <a rel="nofollow" href="http://schaik.com/png">http://schaik.com/png</a> . </p>
<h2>HISTORY</h2>
<p> <code>pamtowinicon</code> was new in Netpbm 10.63 (June 2013). It obsoleted <code>ppmtowinicon</code> by providing more function and conforming better to Netpbm conventions. </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2013 by Ludolf Holzheid. </p>
<p> Translated to Netpbm coding style by Bryan Henderson. </p>
<h2>Index</h2>
