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
<dt><code>object name</code></dt>
<dd> Name of object for which to find coordinates.</dd>
<dt><code>@listfile</code></dt>
<dd> File with one object name per line.</dd>
<dt><code>-a</code></dt>
<dd> Print all information that is returned</dd>
<dt><code>-b &lt;RA&gt; &lt;Dec&gt;</code></dt>
<dd> Output B1950 (FK4) coordinates instead of default J2000 (FK5)</dd>
<dt><code>-c</code></dt>
<dd> Use the CDS server in Strasbourg, France rather than the default server at the Astrophysical Data System in Cambridge, Massachusetts, USA.</dd>
<dt><code>-d</code></dt>
<dd>
&nbsp;<wbr>Output RA and Dec in degrees instead of hh:mm:ss dd:mm:ss</dd>
<dt><code>-e</code></dt>
<dd> Output ecliptic coordinates</dd>
<dt><code>-g</code></dt>
<dd> Output galactic coordinates</dd>
<dt><code>-i</code></dt>
<dd> Print object ID(s) returned</dd>
<dt><code>-n</code></dt>
<dd> Find coordinates using NED</dd>
<dt><code>-s </code></dt>
<dd> Find coordinates using SIMBAD</dd>
<dt><code>-t</code></dt>
<dd> Print output as tab-separated table</dd>
<dt><code>-v</code></dt>
<dd> Verbose listing of results of search</dd>
<dt><code>-z</code></dt>
<dd> Find coordinates in the Vizier catalogs </dd>
</dl>
<h2>See Also</h2>
<p> scat() </p>
<h2>Web Page</h2>
<p> <a rel="nofollow" href="http://tdc-www.harvard.edu/software/wcstools/scat/">http://tdc-www.harvard.edu/software/wcstools/scat/</a> </p>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
<h2>Index</h2>
