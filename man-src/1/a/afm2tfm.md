---
title: "afm2tfm(1)"
name: "afm2tfm"
section: "1"
letter: "a"
url: "/docs/linux/man/1-afm2tfm/"
description: "afm2tfm – convert Adobe font metrics to TeX font metrics"
---

<h2 class="name">NAME</h2>
<p> afm2tfm &#8211; convert Adobe font metrics to TeX font metrics </p>
<h2>DESCRIPTION</h2>
<p> PostScript fonts are (or should be) accompanied by font metric files such as <code>Times-Roman.afm,</code> which describes the characteristics of the font called Times-Roman. To use such fonts with TeX, we need TFM files that contain similar information. This program does that conversion. </p>
<p> For all the details, see the dvips manual (<a rel="nofollow" href="http://tug.org/dvips">http://tug.org/dvips</a>).</p>
<h2>FILES</h2>
<p> <i>psfonts.map</i> in the config directory used by dvips.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-dvips/">dvips</a>(1), <a href="/docs/linux/man/1-tex/">tex</a>(1), <a href="/docs/linux/man/1-vptovf/">vptovf</a>(1), <a href="/docs/linux/man/1-fontinst/">fontinst</a>(1), <a href="/docs/linux/man/1-afm2pl/">afm2pl</a>(1), <a href="/docs/linux/man/1-otftotfm/">otftotfm</a>(1)</p>
<h2>BUGS</h2>
<p> An option to add letterspacing to the virtual font was rejected by Knuth because it would make the fi and fl ligatures break the normal rhythmic pattern.</p>
<h2>AUTHORS</h2>
<p> Tomas Rokicki and Donald E. Knuth. </p>
<p> Maintained in TeX Live; please send bug reports or other correspondence to tex-k [at] tug.org (<a rel="nofollow" href="http://lists.tug.org/tex-k">http://lists.tug.org/tex-k</a>). </p>
<h2>Index</h2>
