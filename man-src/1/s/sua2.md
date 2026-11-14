---
title: "sua2(1)"
name: "sua2"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sua2/"
description: "Find USNO-A2.0 Catalog stars in a square on the sky"
---

<h2>Name</h2>
<p> Find USNO-A2.0 Catalog stars in a square on the sky</p>
<h2>Synopsis</h2>
<p> sua2 [options] ra dec system</p>
<h2>Description</h2>
<p> <i>suac</i> finds all of the U.S. Naval Observatory A2.0 Catalog objects in a specified region of the sky and lists their sky positions and magnitudes in order of brightness. Output is to standard out, unless the -w flag is set, in which case it goes to objectname.uac or search.uac. It is a link to scat.</p>
<h2>Options</h2>
<p> <code>-a</code> list single closest catalog source <code>-b</code> Output B1950 (FK4) coordinates <code>-d</code> Sort by distance from center instead of flux <code>-e</code> Output ecliptic coordinates <code>-f</code> Output search center for other programs <code>-g</code> Output galactic coordinates <code>-h</code> Print heading, else do not <code>-i</code> Print catalog object name, not catalog number (=ua2_region_number) <code>-j</code> Output J2000 (FK5) coordinates <code>-l</code> Print center and closest star on one line <code>-m [&lt;bright magnitude&gt;] &lt;faint magnitude&gt;</code> Limiting catalog magnitude(s) (default none, bright -2 if only faint is given) <code>-n &lt;num&gt;</code> Number of brightest stars to print <code>-o &lt;name&gt;</code> Object name used to name output file <code>-p</code> Sort by distance from search center instead of brightness <code>-q &lt;years&gt;</code> Equinox of output positions in years <code>-r &lt;radius&gt;</code> Search box half-width in arcsec or dd:mm:ss If negative, this is a radius; if two numbers, first is in right ascension, second is in declination. (default is 10, that is a 20&#215;20 arcsec box) <code>-s</code> Sort by right ascension instead of flux <code>-t</code> Tab table output <code>-u &lt;num&gt;</code> Print X Y instead of number in front of non-tab entry <code>-v</code> Verbose listing of processing intermediate results <code>-w</code> Write tab table output file imagename.uac <code>-y</code> Epoch of output positions in years</p>
<h2>See Also</h2>
<p> <a href="/docs/linux/man/1-scat/">scat</a>(1), <a href="/docs/linux/man/1-susac/">susac</a>(1), <a href="/docs/linux/man/1-imuac/">imuac</a>(1), <a href="/docs/linux/man/1-sgsc/">sgsc</a>(1)</p>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
<h2>Index</h2>
