---
title: "mag(1)"
name: "mag"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mag/"
description: "mag – computes TeX fontsizes and magsteps"
---

<h2 class="name">NAME</h2>
<p> mag &#8211; computes TeX fontsizes and magsteps </p>
<h2>SYNOPSIS</h2>
<p> <code>mag</code> [-<code>R</code><i>dpi</i>] magstep . . . </p>
<p> <code>mag</code> [-<code>r</code>] [-<code>R</code><i>dpi</i>] fontsize . . . </p>
<h2>DESCRIPTION</h2>
<p> delim $$ This tool calculates fontsizes given magsteps. TeXfonts are provided as true sized fonts or as magnifications. The fontsize of a true sized font equals the resolution of the printer (ex. 300). The fontsize of a font magnified $n$ <i>magsteps</i> equals: 1.2 sup{n} times 300 delim off rounded to its nearest integer value. Fontnames for TeX fonts normally consists of the name (<i>cmr</i>), pointsize (<i>10</i>), type (<i>pk</i>) and fontsize (<i>360</i>), for example: <i>cmr10.360pk</i>. </p>
<h2>EXAMPLES</h2>
<p> The result of <i>mag -R240 -2 0 0.5 1</i> will be: </p>
<pre>
167 240 263 288 
</pre>
<p> The inverse function is computed with the <i>-r</i> option. The result of <i>mag -r -R240 167 240 263 288</i> will be the fontsteps: </p>
<pre>
-2 0 0.5 1
</pre>
<p> The UNIX shells allow command substitution. One can write: </p>
<pre>
mag -r -R240 `mag -R240 -2 0 0.5 1`
</pre>
<h2>DATE</h2>
<p> 18 December, 1989 </p>
<h2>AUTHOR</h2>
<pre>
Piet Tutelaers
University of Technology Eindhoven
Maintained in TeX Live; please send bug reports or other correspondence
to tex-k [at] tug.org (<a rel="nofollow" href="http://lists.tug.org/tex-k">http://lists.tug.org/tex-k</a>).
</pre>
<h2>Index</h2>
