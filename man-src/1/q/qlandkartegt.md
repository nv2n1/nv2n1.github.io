---
title: "qlandkartegt(1)"
name: "qlandkartegt"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qlandkartegt/"
description: "QLandkarteGT – GPS mapping (GeoTiff and vector) and GPSr management"
---

<h2>NAME</h2>
<p> QLandkarteGT &#8211; GPS mapping (GeoTiff and vector) and GPSr management</p>
<h2>SYNOPSIS</h2>
<p> <code>qlandkartegt</code> [ <code>-d</code> | <code>&#8211;debug</code> ] [ <code>-h</code> | <code>&#8211;help</code> ] <code>-m</code><i>&nbsp;<wbr>FD</i> | <code>&#8211;monitor=</code><i>FD</i> ] [ <code>-n</code> | <code>&#8211;no-splash</code> ] [ <i>files</i>&#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> <i>QLandkarteGT</i> is a versatile tool for GPS maps in GeoTiff format as well as Garmin&#8217;s img vector map format. <i>QLandkarteGT</i> is the successor of <i>QLandkarte</i>. Among various improvements (e.g. 2D/3D map rendering and reduced resource demands) the major difference is its device-independent architecture, which is not limited to Garmin devices anymore. </p>
<p> Additionally, <i>QLandkarteGT</i> serves as a frontend to the GDAL tools, to make georeferencing of scanned maps feasible for users. In contrast to similar tools (e.g. QGis) its straightforward interface is especially suited for non-scientific users.</p>
<h2>OPTIONS</h2>
<p> <i>QLandkarteGT</i> currently understands the following options. Note that long options must be specified in full (by now).</p>
<dl>
<dt><code>-d</code></p>
<dd>
<dt><code>&#8211;debug</code></p>
<dd> Enable additional debugging messages to standard output.</p>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd> Print a short option summary, and exit.</p>
<dt><code>-m</code><i>&nbsp;<wbr>FD</i></p>
<dd>
<dt><code>&#8211;monitor=</code><i>FD</i></p>
<dd> Monitor the file descriptor <i>FD</i> for activity. If any new data arrives on the descriptor, a single byte is read from it, all currently active data are discarded, and the geo data files that have been specified at the end of the command-line when starting <i>QLandkarteGT</i> are read and evaluated again.</p>
<dt><code>-n</code></p>
<dd>
<dt><code>&#8211;no-splash</code></p>
<dd> Do not display the splash screen on startup.</dl>
<p> All remaining positional arguments are considered names of geo data files to be read and evaluated upon startup.</p>
<h2>SEE ALSO</h2>
<p> <i>QLandkarteGT</i> Homepage: <code><a rel="nofollow" href="http://www.qlandkarte.org">http://www.qlandkarte.org</a></code></p>
<h2>AUTHOR</h2>
<p> <i>QLandkarteGT</i> was written and is currently maintained by Oliver Eichler <code>&lt;oliver.eichler [at] gmx.de&gt;</code>. </p>
<h2>Index</h2>
