---
title: "scat(1)"
name: "scat"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scat/"
description: "scat – Find catalog stars in a square or circle on the sky"
---

<h2>Name</h2>
<p> scat &#8211; Find catalog stars in a square or circle on the sky</p>
<h2>Synopsis</h2>
<p> scat [options] [-b or -j] ra dec [equinox]</p>
<h2>Description</h2>
<p> <i>scat</i> is a utility for finding all of the Hubble Space Telescope Guide Star Catalog (GSC), U.S. Naval Observatory A2.0 (UA2), B1.0 (UB1), SA2.0 (USA2), or UJ (UJC) Catalogs, or locally catalogued objects in a specified region of the sky and listing their sky coordinates to standard output. If the -w flag is set, they are written to a file objectname.catalogname, where objectname is given by the argument to -o on the command line, defaulting to &quot;search&quot;, and catalogname is given by the argument to -c on the command line. The catalog defaults to the GSC, if no -c argument is present. scat resembles <a href="/docs/linux/man/1-rgsc/">rgsc</a>(1) and <a href="/docs/linux/man/1-star/">star</a>(1), which can search from lists of coordinates but cannot sort the output. sgsc, suac, and susac are links to this program.1</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd> List the single closest catalog source</p>
<dt><code>-b &lt;RA&gt; &lt;Dec&gt;</code></p>
<dd> Output B1950 (FK4) coordinates around this center</p>
<dt><code>-c &lt;name&gt;</code></p>
<dd> Reference catalog (gsc(=HST GSC), ua2(=USNO-A2.0), TMC(=2MASS Point Source Catalog), gsc2(=GSC II), ub1(=USNO-B1.0), local file, etc.)</p>
<dt><code>-d</code></p>
<dd>
&nbsp;<wbr>Output RA and Dec in degrees instead of hh:mm:ss dd:mm:ss</p>
<dt><code>-e</code></p>
<dd> Output ecliptic coordinates</p>
<dt><code>-f</code></p>
<dd> Output search center for other programs</p>
<dt><code>-g &lt;class&gt;</code></p>
<dd> HST Guide Star Catalog object class (0=stars 3=galaxies -1=all)</p>
<dt><code>-h</code></p>
<dd> Print search and column heading, else do not</p>
<dt><code>-i</code></p>
<dd> Print catalog object name, not catalog number</p>
<dt><code>-j &lt;RA&gt; &lt;Dec&gt;</code></p>
<dd> Output J2000 (FK5) coordinates around this center</p>
<dt><code>-k &lt;keyword&gt;</code></p>
<dd> Add value of this keyword to end of output lines from a tab table search</p>
<dt><code>-l</code></p>
<dd> Print search center and closest star on one line</p>
<dt><code>-m [&lt;bright magnitude&gt;] &lt;faint magnitude&gt;</code></p>
<dd> Limiting catalog magnitude(s) (default none, bright -2 if only faint is given)</p>
<dt><code>-n &lt;num&gt;</code></p>
<dd> Number of brightest stars to print</p>
<dt><code>-o &lt;name&gt;</code></p>
<dd> Object name used for output file naming</p>
<dt><code>-q &lt;year&gt;</code></p>
<dd> Equinox of output position in fractional years</p>
<dt><code>-r &lt;radius&gt;</code></p>
<dd> Halfwidth (-radius if negative) of search area in arcseconds (default 10)</p>
<dt><code>-s d|m|n|p|r</code></p>
<dd> Sort by (d)eclination, (m)agnitude, (n)o sort, (p)distance from center, or (r)ight ascension.</p>
<dt><code>-t</code></p>
<dd> Tab table to standard output or file</p>
<dt><code>-u &lt;x&gt; &lt;y&gt;</code></p>
<dd> Print x y instead of number in front of non-tab output, before RA and Dec or add x and y columns to end of tab output line</p>
<dt><code>-v</code></p>
<dd> Verbose listing of processing intermediate results</p>
<dt><code>-w</code></p>
<dd> Write output file objectname.catalog or search.catalog if -o is not used.</p>
<dt><code>-x &lt;type&gt;</code></p>
<dd> GSC object type (0=stars 3=galaxies -1=all -2=bands)</p>
<dt><code>-y &lt;year&gt;</code></p>
<dd> Epoch of output positions in fractional years (for proper motion only)</p>
<dt><code>-z</code></p>
<dd> Append to existing output file search.catalog or objectname.catalog. Start file if it does not already exist. </p>
</dl>
<h2>See Also</h2>
<p> imcat() </p>
<h2>Web Page</h2>
<p> <a rel="nofollow" href="http://tdc-www.harvard.edu/software/wcstools/scat/">http://tdc-www.harvard.edu/software/wcstools/scat/</a> </p>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
<h2>Index</h2>
