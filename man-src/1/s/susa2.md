---
title: "susa2(1)"
name: "susa2"
section: "1"
letter: "s"
url: "/docs/linux/man/1-susa2/"
description: "Find USNO-SA2.0 Catalog stars in a square on the sky"
---

<h2>Name</h2>
<p> Find USNO-SA2.0 Catalog stars in a square on the sky</p>
<h2>Synopsis</h2>
<p> susac [options] [-b or -j] ra dec</p>
<h2>Description</h2>
<p> <i>suac</i> finds all of the U.S. Naval Observatory SA2.0 Catalog objects in a specified region of the sky and lists their sky positions and magnitudes in order of brightness. Output is to standard out, unless the -w flag is set, in which case it goes to objectname.uac or search.uac. It is a link to scat.</p>
<h2>Options</h2>
<p> <code>-a</code> list single closest catalog source <code>-b &lt;RA&gt; &lt;Dec&gt;</code> Output B1950 (FK4) coordinates around this center <code>-d</code> Sort by distance from center instead of flux <code>-h</code> Print heading, else do not <code>-j &lt;RA&gt; &lt;Dec&gt;</code> Output J2000 (FK5) coordinates around this center <code>-m [&lt;bright magnitude&gt;] &lt;faint magnitude&gt;</code> Limiting catalog magnitude(s) (default none, bright -2 if only faint is given) <code>-n &lt;num&gt;</code> Number of brightest stars to print <code>-o &lt;name&gt;</code> Object name used to name output file <code>-r &lt;radius&gt;</code> Search radius in arcsec (default 10) <code>-s</code> Sort by right ascension instead of flux <code>-t</code> Tab table to standard output as well as file <code>-u &lt;num&gt;</code> Plate number for catalog sources (0=all) <code>-v</code> Verbose listing of processing intermediate results <code>-w</code> Write tab table output file imagename.uac</p>
<h2>See Also</h2>
<p> <a href="/docs/linux/man/1-scat/">scat</a>(1), <a href="/docs/linux/man/1-sua2/">sua2</a>(1), <a href="/docs/linux/man/1-imusa2/">imusa2</a>(1), <a href="/docs/linux/man/1-sgsc/">sgsc</a>(1)</p>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
<h2>Index</h2>
