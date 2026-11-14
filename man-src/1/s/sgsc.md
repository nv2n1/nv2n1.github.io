---
title: "sgsc(1)"
name: "sgsc"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sgsc/"
description: "sgsc – Find HST GSC stars in a square on the sky"
---

<h2>Name</h2>
<p> sgsc &#8211; Find HST GSC stars in a square on the sky</p>
<h2>Synopsis</h2>
<p> sgsc [options] [-b or -j] ra dec [equinox]</p>
<h2>Description</h2>
<p> <i>sgsc</i> is a utility for finding all of the Hubble Space Telescope Guide Star Catalog objects in a specified region of the sky and listing them with their sky positions and magnitudes in order of brightness, with the brighter ones first. Output is to standard out, unless the -w flag is set, in which case it goes to objectname.gsc or search.gsc. It is somewhat similar to RGSC, which can search from lists of coordinates but cannot sort the output. It is a link to scat.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd> List single closest catalog source</p>
<dt><code>-b &lt;RA&gt; &lt;Dec&gt;</code></p>
<dd> Output B1950 (FK4) coordinates</p>
<dt><code>-d</code></p>
<dd> Sort by distance from center instead of flux</p>
<dt><code>-g &lt;class&gt;</code></p>
<dd> Object class (0=stars 3=galaxies -1=all)</p>
<dt><code>-h</code></p>
<dd> Print heading, else do not</p>
<dt><code>-j &lt;RA&gt; &lt;Dec&gt;</code></p>
<dd> Output J2000 (FK5) coordinates around this center</p>
<dt><code>-m [&lt;bright magnitude&gt;] &lt;faint magnitude&gt;</code></p>
<dd> Limiting catalog magnitude(s) (default none, bright -2 if only faint is given)</p>
<dt><code>-n &lt;num&gt;</code></p>
<dd> Number of brightest stars to print</p>
<dt><code>-o &lt;name&gt;</code></p>
<dd> Object name used for output file naming</p>
<dt><code>-r &lt;radius&gt;</code></p>
<dd> Radius of search circle 1in arcsec (default 10)</p>
<dt><code>-s</code></p>
<dd> Sort by RA instead of flux</p>
<dt><code>-t</code></p>
<dd> Tab table to standard output as well as file</p>
<dt><code>-v</code></p>
<dd> Verbose listing of processing intermediate results</p>
<dt><code>-w</code></p>
<dd> Write tab table output file imagename.gsc</dl>
<h2>See Also</h2>
<p> <a href="/docs/linux/man/1-scat/">scat</a>(1), <a href="/docs/linux/man/1-rgsc/">rgsc</a>(1), <a href="/docs/linux/man/1-suac/">suac</a>(1), <a href="/docs/linux/man/1-susac/">susac</a>(1), <a href="/docs/linux/man/1-imgsc/">imgsc</a>(1)</p>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
<h2>Index</h2>
