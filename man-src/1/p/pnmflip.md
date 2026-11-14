---
title: "pnmflip(1)"
name: "pnmflip"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmflip/"
description: "pnmflip – perform one or more flip operations on a portable anymap"
---

<h2 class="name">NAME</h2>
<p> pnmflip &#8211; perform one or more flip operations on a portable anymap </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmflip</code> [<code>-leftright</code>|<code>-lr</code>] [<code>-topbottom</code>|<code>-tb</code>] [<code>-transpose</code>|<code>-xy</code>] [<code>-rotate90</code>|<code>-r90</code>|<code>-ccw</code> ] [<code>-rotate270</code>|<code>-r270</code>|<code>-cw</code> ] [<code>-rotate180</code>|<code>-r180</code>] [<i>pnmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable anymap as input. Performs one or more flip operations, in the order specified, and writes out a portable anymap.</p>
<h2>OPTIONS</h2>
<p> The flip operations available are: left for right (<code>-leftright</code> or <code>-lr</code>); top for bottom (<code>-topbottom</code> or <code>-tb</code>); and transposition (<code>-transpose</code> or <code>-xy</code>). In addition, some canned concatenations are available: <code>-rotate90</code> or <code>-ccw</code> is equivalent to <code>-transpose</code> <code>-topbottom</code>; <code>-rotate270</code> or <code>-cw</code> is equivalent to <code>-transpose</code> <code>-leftright</code>; and <code>-rotate180</code> is equivalent to <code>-leftright</code> <code>-topbottom</code>. </p>
<p> All flags can be abbreviated to their shortest unique prefix.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pnmrotate/">pnmrotate</a>(1), <a href="/docs/linux/man/5-pnm/">pnm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989 by Jef Poskanzer. </p>
<h2>Index</h2>
