---
title: "pnmpaste(1)"
name: "pnmpaste"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmpaste/"
description: "pnmpaste – paste a rectangle into a portable anymap"
---

<h2 class="name">NAME</h2>
<p> pnmpaste &#8211; paste a rectangle into a portable anymap </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmpaste</code> [<code>-replace</code>|<code>-or</code>|<code>-and</code> |<code>-xor</code>] <i>frompnmfile x y</i> [<i>intopnmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads two portable anymaps as input. Inserts the first anymap into the second at the specified location, and produces a portable anymap the same size as the second as output. If the second anymap is not specified, it is read from stdin. The <i>x</i> and <i>y</i> can be negative, in which case they are interpreted relative to the right and bottom of the anymap, respectively. </p>
<p> This tool is most useful in combination with <i>pnmcut</i>. For instance, if you want to edit a small segment of a large image, and your image editor cannot edit the large image, you can cut out the segment you are interested in, edit it, and then paste it back in. </p>
<p> Another useful companion tool is <i>pbmmask</i>. </p>
<p> <code>pnmcomp</code> is, a more general tool, except that it lacks the &quot;or,&quot; &quot;and,&quot; and &quot;xor&quot; functions. <code>pnmcomp</code> allows you to specify an alpha mask in order to have only part of the inserted image get inserted. So the inserted pixels need not be a rectangle. You can also have the inserted image be translucent, so the resulting image is a mixture of the inserted image and the base image. </p>
<p> [ <code>TIONS</code> ] </p>
<p> The optional flag specifies the operation to use when doing the paste. The default is <code>-replace</code>. The other, logical operations are only allowed if both input images are bitmaps. These operations act as if white is TRUE and black is FALSE. </p>
<p> All flags can be abbreviated to their shortest unique prefix. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pnmcomp/">pnmcomp</a></code>(1), <code><a href="/docs/linux/man/1-pnmcut/">pnmcut</a></code>(1), <code><a href="/docs/linux/man/1-pnminvert/">pnminvert</a></code>(1), <code><a href="/docs/linux/man/1-pnmarith/">pnmarith</a></code>(1), <code><a href="/docs/linux/man/1-pbmmask/">pbmmask</a></code>(1), <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989, 1991 by Jef Poskanzer. </p>
<h2>Index</h2>
