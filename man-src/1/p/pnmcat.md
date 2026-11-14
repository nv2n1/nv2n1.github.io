---
title: "pnmcat(1)"
name: "pnmcat"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmcat/"
description: "pnmcat – concatenate portable anymaps"
---

<h2 class="name">NAME</h2>
<p> pnmcat &#8211; concatenate portable anymaps </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmcat</code> [<code>-white</code>|<code>-black</code>] <code>-leftright</code>|<code>-lr</code> [<code>-jtop</code>|<code>-jbottom</code>] <i>pnmfile pnmfile</i> &#8230;<br />
 <code>pnmcat</code> [<code>-white</code>|<code>-black</code>] <code>-topbottom</code>|<code>-tb</code> [<code>-jleft</code>|<code>-jright</code>] <i>pnmfile pnmfile</i> &#8230; </p>
<h2>DESCRIPTION</h2>
<p> Reads portable anymaps as input. Concatenates them either left to right or top to bottom, and produces a portable anymap as output. </p>
<p> <code>pamdice</code> splits an image up into smaller ones. </p>
<p> <code>pnmtile</code> concatenates a single input image to itself repeatedly. </p>
<h2>OPTIONS</h2>
<p> If the anymaps are not all the same height (left-right) or width (top-bottom), the smaller ones have to be justified with the largest. By default, they get centered, but you can specify one side or the other with one of the -j* flags. So, <code>-topbottom -jleft</code> would stack the anymaps on top of each other, flush with the left edge. </p>
<p> The <code>-white</code> and <code>-black</code> flags specify what color to use to fill in the extra space when doing this justification. If neither is specified, the program makes a guess. </p>
<p> All flags can be abbreviated to their shortest unique prefix. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pamdice/">pamdice</a></code>(1), <code><a href="/docs/linux/man/1-pnmtile/">pnmtile</a></code>(1), <code><a href="/docs/linux/man/1-pamcut/">pamcut</a></code>(1), <code><a href="/docs/linux/man/5-pnm/">pnm</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989 by Jef Poskanzer. </p>
<h2>Index</h2>
