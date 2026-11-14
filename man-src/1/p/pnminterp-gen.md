---
title: "pnminterp-gen(1)"
name: "pnminterp-gen"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnminterp-gen/"
description: "pamstretch-gen – use pamstretch and pnmscale to scale by non-integer values"
---

<h2 class="name">NAME</h2>
<p> pamstretch-gen &#8211; use pamstretch and pnmscale to scale by non-integer values</p>
<h2>SYNOPSIS</h2>
<p> <code>pamstretch-gen</code> <i>N</i> [<i>pnmfile</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>pamstretch-gen </code> is a program which uses <code><a href="/docs/linux/man/1-pamstretch/">pamstretch</a></code>(1), <code><a href="/docs/linux/man/1-pnmfile/">pnmfile</a></code>(1), and <code><a href="/docs/linux/man/1-pnmscale/">pnmscale</a></code>(1) to smoothly scale up a PNM file by any ratio; it&#8217;s like a more general version of pamstretch (hence the name). But other than the `any ratio&#8217; bit, it&#8217;s much the same as pamstretch. :-) </p>
<h2>BUGS</h2>
<p> Uses awk just to make some simple floating-point calculations, which is probably overkill. But using dc makes my head hurt. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pamstretch/">pamstretch</a></code>(1), <code><a href="/docs/linux/man/1-pnmscale/">pnmscale</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Russell Marks (russell.marks [at] ntlworld.com). </p>
<h2>Index</h2>
