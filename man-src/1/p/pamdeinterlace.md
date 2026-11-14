---
title: "pamdeinterlace(1)"
name: "pamdeinterlace"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamdeinterlace/"
description: "pamdeinterlace – remove ever other row from a PAM/PNM image"
---

<h2 class="name">NAME</h2>
<p> pamdeinterlace &#8211; remove ever other row from a PAM/PNM image</p>
<h2>SYNOPSIS</h2>
<p> <code>pamdeinterlace</code> [<code>-takeodd</code>] [<code>-takeeven</code>] <i>N</i> [<i>infile</i>] </p>
<p> You can use the minimum unique abbreviation of the options. You can use two hyphens instead of one. You can separate an option name from its value with white space instead of an equals sign. </p>
<h2>DESCRIPTION</h2>
<p> <code>pamdeinterlace</code> Removes all the even-numbered or odd-numbered rows from the input PNM or PAM image. Specify which with the <code>-takeeven</code> and <code>-takeodd</code> options. </p>
<p> This can be useful if the image is a video capture from an interlaced video source. In that case, each row shows the subject 1/60 second before or after the two rows that surround it. If the subject is moving, this can detract from the quality of the image. </p>
<p> Because the resulting image is half the height of the input image, you will then want to use <code>pamstretch</code> or <code>pnmscale </code> to restore it to its normal height: </p>
<p> <code>pamdeinterlace myimage.ppm | pamstretch -yscale=2 &gt;newimage.ppm</code> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-takeodd</code></p>
<dd> Take the odd-numbered rows from the input and put them in the output. The rows are numbered starting at zero, so the first row in the output is the second row from the input. You cannot specify both <code>-takeeven</code> and <code>-takeodd</code>. </p>
<dt><code>-takeeven</code></p>
<dd> Take the even-numbered rows from the input and put them in the output. The rows are numbered starting at zero, so the first row in the output is the first row from the input. This is the default. You cannot specify both <code>-takeeven</code> and <code>-takeodd</code>. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pamstretch/">pamstretch</a></code>(1), <code><a href="/docs/linux/man/1-pnmscale/">pnmscale</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> put by Bryan Henderson in the public domain in 2001 </p>
<h2>Index</h2>
