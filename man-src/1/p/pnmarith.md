---
title: "pnmarith(1)"
name: "pnmarith"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pnmarith/"
description: "pnmarith – perform arithmetic on two portable anymaps"
---

<h2 class="name">NAME</h2>
<p> pnmarith &#8211; perform arithmetic on two portable anymaps </p>
<h2>SYNOPSIS</h2>
<p> <code>pnmarith</code> <code>-add</code>|<code>-subtract</code>|<code>-multiply</code>|<code>-difference</code>|<code>-minimum</code>|<code>-maximum.</code> <i>pnmfile1 pnmfile2</i></p>
<h2>DESCRIPTION</h2>
<p> Reads two portable anymaps as input. Performs the specified arithmetic operation, and produces a portable anymap as output. The two input anymaps must be the same width and height. </p>
<p> The arithmetic is performed between corresponding pixels in the two anymaps, as if maxval was 1.0, black was 0.0, and a linear scale in between. Results that fall outside of [0..1) are truncated. </p>
<p> The operator <i>-difference</i> calculates the absolute value of <i>pnmarith -subtract pnmfile1 pnmfile2,</i> i.e. no truncation is done. </p>
<p> All flags can be abbreviated to their shortest unique prefix.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pbmmask/">pbmmask</a>(1), <a href="/docs/linux/man/1-pnmpaste/">pnmpaste</a>(1), <a href="/docs/linux/man/1-pnminvert/">pnminvert</a>(1), <a href="/docs/linux/man/5-pnm/">pnm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1989, 1991 by Jef Poskanzer. Lightly modified by Marcel Wijkstra &lt;wijkstra [at] fwi.uva.nl&gt; </p>
<h2>Index</h2>
