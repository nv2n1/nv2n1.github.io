---

title: "sgsc(1)"
name: "sgsc"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sgsc/"
description: "sgsc – Find HST GSC stars in a square on the sky"
---

<p> sgsc &#8211; Find HST GSC stars in a square on the sky</p>
<h2>Synopsis</h2>
<p> sgsc [options] [-b or -j] ra dec [equinox]</p>
<h2>Description</h2>
<p> <i>sgsc</i> is a utility for finding all of the Hubble Space Telescope Guide Star Catalog objects in a specified region of the sky and listing them with their sky positions and magnitudes in order of brightness, with the brighter ones first. Output is to standard out, unless the -w flag is set, in which case it goes to objectname.gsc or search.gsc. It is somewhat similar to RGSC, which can search from lists of coordinates but cannot sort the output. It is a link to scat.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></dt>
<dd> List single closest catalog source</dd>
<dt><code>-b &lt;RA&gt; &lt;Dec&gt;</code></dt>
<dd> Output B1950 (FK4) coordinates</dd>
<dt><code>-d</code></dt>
<dd> Sort by distance from center instead of flux</dd>
<dt><code>-g &lt;class&gt;</code></dt>
<dd> Object class (0=stars 3=galaxies -1=all)</dd>
<dt><code>-h</code></dt>
<dd> Print heading, else do not</dd>
<dt><code>-j &lt;RA&gt; &lt;Dec&gt;</code></dt>
<dd> Output J2000 (FK5) coordinates around this center</dd>
<dt><code>-m [&lt;bright magnitude&gt;] &lt;faint magnitude&gt;</code></dt>
<dd> Limiting catalog magnitude(s) (default none, bright -2 if only faint is given)</dd>
<dt><code>-n &lt;num&gt;</code></dt>
<dd> Number of brightest stars to print</dd>
<dt><code>-o &lt;name&gt;</code></dt>
<dd> Object name used for output file naming</dd>
<dt><code>-r &lt;radius&gt;</code></dt>
<dd> Radius of search circle 1in arcsec (default 10)</dd>
<dt><code>-s</code></dt>
<dd> Sort by RA instead of flux</dd>
<dt><code>-t</code></dt>
<dd> Tab table to standard output as well as file</dd>
<dt><code>-v</code></dt>
<dd> Verbose listing of processing intermediate results</dd>
<dt><code>-w</code></dt>
<dd> Write tab table output file imagename.gsc</dd></dl>
<h2>See Also</h2>
<p> <a href="/docs/linux/man/1-scat/">scat</a>(1), rgsc(1), suac(1), susac(1), <a href="/docs/linux/man/1-imgsc/">imgsc</a>(1)</p>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
