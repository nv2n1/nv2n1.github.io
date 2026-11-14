---
title: "pamflip(1)"
name: "pamflip"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamflip/"
description: "pamflip – flip or rotate a PAM or PNM image"
---

<h2 class="name">NAME</h2>
<p> pamflip &#8211; flip or rotate a PAM or PNM image</p>
<h2>SYNOPSIS</h2>
<p> <code>pamflip</code> { <code>-leftright</code> | <code>-lr</code> | <code>-topbottom</code> | <code>-tb</code> | <code>-transpose</code> | <code>-xy</code> | <code>-rotate90</code> | <code>-r90</code> | <code>-cw</code> | <code>-rotate270</code> | <code>-r270</code> | <code>-ccw</code> | <code>-rotate180</code> | <code>-r180</code> <code>-null</code> | <code>-xform=</code><i>xform1</i><code>,</code><i>xform2</i>&#8230; } [<code>-memsize=</code><i>mebibytes</i>] [<code>-pagesize=</code><i>bytes</i>] [<i>pamfile</i>] </p>
<p> All options can be abbreviated to their shortest unique prefix. You may use two hyphens instead of one to designate an option. You may use either white space or an equals sign between an option name and its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pamflip</code> flips a PAM or PNM image top for bottom or left for right, or transposes it horizontal for vertical, or rotates it 1, 2, or 3 quarter turns. </p>
<p> To rotate at other angles, use <code>pnmrotate</code>. It is much slower, though. </p>
<p> The input image is <i>pamfile</i>, or Standard Input if <i>pamfile</i> is not specified. </p>
<p> To flip/rotate a JFIF (JPEG) image losslessly, use <code>jpegtran</code>. <code>jpegtran</code> is part of the Independent Jpeg Group&#8217;s compression library package, not part of Netpbm. The normal Netpbm way to flip a JFIF file would be to convert it to PNM, use <code>pamflip</code>, and convert back to JFIF. But since JPEG compression is lossy, the resulting image would have less quality than the original. <code>jpegtran</code>, on the other hand, can do this particular transformation directly on the compressed data without loss. </p>
<h2>OPTIONS</h2>
<p> You must supply exactly one of the following options: </p>
<p> <code>pamflip</code>&#8216;s predecessor (before Netpbm 10.7 &#8211; August 2002) <code>pnmflip</code> did not have the <code>-xform</code> option and instead allowed you to specify any number of the other options, including zero. It applied all the indicated transformations, in the order given, just like with <code>pamflip</code>&#8216;s <code>-xform</code> option. (Reason for the change: this kind of interpretation of options is inconsistent with the rest of Netpbm and most of the Unix world, and thus hard to understand and to implement). </p>
<dl>
<dt><code>-leftright</code></p>
<dd>
<dt><code>-lr</code></p>
<dd> Flip left for right. </p>
<dt><code>-topbottom</code></p>
<dd>
<dt><code>-tb</code></p>
<dd> Flip top for bottom. </p>
<dt><code>-transpose</code></p>
<dd>
<dt><code>-xy</code></p>
<dd> Transpose horizontal for vertical. I.e. make the pixel at (x,y) be at (y,x). </p>
<dt><code>-rotate90</code></p>
<dd>
<dt><code>-r90</code></p>
<dd>
<dt><code>-ccw</code></p>
<dd> Rotate counterclockwise 90 degrees. </p>
<dt><code>-rotate180</code></p>
<dd>
<dt><code>-r180</code></p>
<dd> Rotate 180 degrees. </p>
<dt><code>-rotate270</code></p>
<dd>
<dt><code>-r270</code></p>
<dd>
<dt><code>-cw</code></p>
<dd> Rotate counterclockwise 270 degrees (clockwise 90 degrees) </p>
<dt><code>-null</code></p>
<dd> No change. (The purpose of this option is the convenience of programs that invoke <code>pamflip</code> after computing the kind of transformation desired, including none at all). </p>
<p> This option was new in Netpbm 10.13 (December 2002).<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<dt><code>-xform=</code><i>xform1</i><code>,</code><i>xform2</i>&#8230;</p>
<dd> Apply all the transforms listed, in order. The valid values for the transforms are as follows and have the same meanings as the identically named options above. </p>
<dt>&bull;</p>
<dd> leftright</p>
<dt>&bull;</p>
<dd> topbottom</p>
<dt>&bull;</p>
<dd> transpose </p>
<p> This option was new in Netpbm 10.13 (December 2002). </p>
</dl>
<p> The following options help <code>pamflip</code> use memory efficiently. Some flipping operations on very large images can cause <code>pamflip</code> to have a very large working set, which means if you don&#8217;t have enough real memory, the program can page thrash, which means it takes a ridiculous amount time to run. If your entire image fits in real memory, you don&#8217;t have a problem. If you&#8217;re just flipping top for bottom or left for right, you don&#8217;t have a problem. Otherwise, pay attention. If you&#8217;re interested in the details of the thrashing problem and how <code>pamflip</code> approaches it, you&#8217;re invited to read a complete explanation in comments in the source code. </p>
<dl>
<dt><code>-memsize=</code><i>mebibytes</i></p>
<dd> <i>mebibytes</i> is the size in mebibytes (aka megabytes) of memory available for <code>pamflip</code>. It is the lesser of the amount of real or virtual memory available. </p>
<p> <code>pamflip</code> does nothing special to allocate real memory or control it&#8217;s allocation &#8212; it gets whatever it gets just by referencing virtual memory normally. The real memory figure in question is the maximum amount that <code>pamflip</code> can be expected to end up with by doing that. This is just about impossible for you to know, of course, but you can estimate. The total real memory in your system should be a major factor in your estimate. </p>
<p> If <code>pamflip</code> cannot fit the entire image in the amount of memory you specify, it does the transformation in chunks, using temporary files for intermediate results. </p>
<p> Strict horizontal transformations (either left for right or null), <code>pamflip</code> never keeps more than one row in memory, so the memory size is irrelevant and <code>pamflip</code> doesn&#8217;t use temporary files. </p>
<p> The real memory is important when you do a column for row type of transformation (e.g. <code>-rotate90</code>). In that case, even if <code>pamflip</code> can fit the entire image in virtual memory at once, if it does not also fit in real memory, the program will thrash like crazy because of the order in which <code>pamflip</code> accesses the pixels, and that means it will take a ridiculously long time to run. A proper <code>-memsize</code> drastically reduces the paging. </p>
<p> If you specify <code>-memsize</code> too large, <code>pamflip</code> may attempt to get more virtual memory than the system allows it and fail. If it can get the virtual memory, but <code>-memsize</code> is larger than the amount of real memory the system allows it and the transformation is row for column, it will page thrash and run very slowly. A value even slightly too high is the same as infinity. </p>
<p> If you specify <code>-memsize</code> too small, the program will run slightly more slowly due to extra overhead in manipulating temporary files. Also, if your environment isn&#8217;t set up to make temporary files possible, <code>pamflip</code> will fail. </p>
<p> Doing the entire transformation &#8216;in memory&#8217; doesn&#8217;t speed things up as much as you might think, because even with the temporary files, the data is just as likely to be in memory. Virtual memory gets paged to disk and disk files get cached in memory. In fact, the pixels fit much more compactly into memory when stored in a temporary file than when stored &#8216;in memory&#8217; because <code>pamflip</code> uses a more efficient format. So you&#8217;re likely to have <i>less</i> disk I/O when you allow <code>pamflip</code> less memory. </p>
<p> If you do not specify <code>-memsize</code>, <code>pamflip</code> assumes infinity. </p>
<p> This option did not exist before Netpbm 10.7 (August 2002). </p>
<p> Before Netpbm 10.42 (March 2008), this option applied only to real memory. <code>pamflip</code> would always keep the entire image in virtual memory and if it could not get enough virtual memory, it failed. <code>pamflip</code> accessed the pixels in an order designed to keep real memory use within the specified amount.<br />
&nbsp;<wbr>&nbsp;<wbr></p>
<dt><code>-pagesize=</code><i>bytes</i></p>
<dd> <i>bytes</i> is the size in bytes of a paging unit &#8212; the amount of memory that gets paged in or out as an indivisible unit &#8212; in your system. The default is 4KiB. </p>
<p> This option has no effect. </p>
<p> Before Netpbm 10.42 (March 2008), <code>pamflip</code> used it to control its use of real memory. </p>
<p> This option did not exist before Netpbm 10.7 (August 2002). </p>
<p> Miscellaneous options: </p>
<dt><code>-verbose</code></p>
<dd> This option causes <code>pamflip</code> to issue messages to Standard Error about its progress. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmrotate/">pnmrotate</a></code>(1) , <code><a href="/docs/linux/man/1-pnm/">pnm</a></code>(1) , <code><a href="/docs/linux/man/1-pam/">pam</a></code>(1) , <code>jpegtran</code> manual </p>
<h2>HISTORY</h2>
<p> <code>pamflip</code> replaced <code>pnmflip</code> in Netpbm 10.13 (December 2002). <code>pamflip</code> is backward compatible, but also works on PAM images. </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989 by Jef Poskanzer. </p>
<h2>Index</h2>
