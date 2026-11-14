---
title: "simpos(1)"
name: "simpos"
section: "1"
letter: "s"
url: "/docs/linux/man/1-simpos/"
description: "simpos – Find position of a named object in the sky"
---

<h2>Name</h2>
<p> simpos &#8211; Find position of a named object in the sky</p>
<h2>Synopsis</h2>
<p> simpos [options] [object name]</p>
<h2>Description</h2>
<p> <i>simpos</i> is a utility for finding the coordinates of any named object in the sky using the SIMBAD name resolver at either the CDS in Strasbourg or the ADS in Cambridge, MA. It can search SIMBAD, Vizier, and/or NED (NASA Extragalactic Database) in any order.</p>
<h2>Options</h2>
<dl>
<dt><code>object name</code></p>
<dd> Name of object for which to find coordinates.</p>
<dt><code>@listfile</code></p>
<dd> File with one object name per line.</p>
<dt><code>-a</code></p>
<dd> Print all information that is returned</p>
<dt><code>-b &lt;RA&gt; &lt;Dec&gt;</code></p>
<dd> Output B1950 (FK4) coordinates instead of default J2000 (FK5)</p>
<dt><code>-c</code></p>
<dd> Use the CDS server in Strasbourg, France rather than the default server at the Astrophysical Data System in Cambridge, Massachusetts, USA.</p>
<dt><code>-d</code></p>
<dd>
&nbsp;<wbr>Output RA and Dec in degrees instead of hh:mm:ss dd:mm:ss</p>
<dt><code>-e</code></p>
<dd> Output ecliptic coordinates</p>
<dt><code>-g</code></p>
<dd> Output galactic coordinates</p>
<dt><code>-i</code></p>
<dd> Print object ID(s) returned</p>
<dt><code>-n</code></p>
<dd> Find coordinates using NED</p>
<dt><code>-s </code></p>
<dd> Find coordinates using SIMBAD</p>
<dt><code>-t</code></p>
<dd> Print output as tab-separated table</p>
<dt><code>-v</code></p>
<dd> Verbose listing of results of search</p>
<dt><code>-z</code></p>
<dd> Find coordinates in the Vizier catalogs </p>
</dl>
<h2>See Also</h2>
<p> scat() </p>
<h2>Web Page</h2>
<p> <a rel="nofollow" href="http://tdc-www.harvard.edu/software/wcstools/scat/">http://tdc-www.harvard.edu/software/wcstools/scat/</a> </p>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
<h2>Index</h2>
