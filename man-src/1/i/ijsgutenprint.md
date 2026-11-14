---
title: "ijsgutenprint(1)"
name: "ijsgutenprint"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ijsgutenprint/"
description: "ijsgutenprint – Ghostscript driver for Gutenprint"
---

<h2>NAME</h2>
<p> ijsgutenprint &#8211; Ghostscript driver for Gutenprint</p>
<h2>SYNOPSIS</h2>
<p> <code>gs</code> -sDEVICE=ijs -sIjsServer=/usr/bin/ijsgutenprint -sDeviceManufacturer=<i>vendor</i> -sDeviceModel=<i>name</i> [ <i>-dIjsUseOutputFD</i> ] -sIjsParams=[ <i>key1</i>=<i>value1</i>,<i>keyn</i>=<i>valuen</i>&#8230; ] [ <i>options</i> ] [ <i>files</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>ijsgutenprint</code> provides Ghostscript with a Gutenprint driver, supporting all printers supported by libgutenprint. </p>
<p> <code>NOTE:</code> ijsgutenprint should never be called directly. Ghostscript will run it if the IjsServer parameter is set to IjsServer=ijsgutenprint when invoking the IJS driver. </p>
<p> <code>NOTE:</code> The only <i>supported</i> method of running ijsgutenprint is via Foomatic. Users running ghostscript directly will not be supported. The driver name used by Foomatic is <i>gutenprint-ijs.5.2</i>.</p>
<h2>OPTIONS</h2>
<p> <i>ijsgutenprint</i> accepts the following Ghostscript IJS options. The Gutenprint-specific options are not documented here.</p>
<dl>
<dt><code>-dIjsUseOutputFD</code></p>
<dd> This option should be specified whenever output from Ghostscript will go to stdout or into a pipe. It may be specified in all other cases, with only a slight performance degradation.</p>
<dt><code>-sIjsParams</code>=<i>Option1</i>=<i>Value1</i>,<i>Option2</i>=<i>Value2</i></p>
<dd> This parameter contains a single string containing a comma-separated list of sub-options.</p>
<dt><code>-sDeviceManufacturer</code>=<i>vendor</i> <code>-sDeviceModel</code>=<i>name</i></p>
<dd> This option must be supplied. There is no default. The IJS driver requires the <i>vendor</i> (it&#8217;s part of the protocol), but the ijsgutenprint driver ignores it.</dl>
<h2>HISTORY</h2>
<p> The Ghostscript <code>stp</code> driver was originally written by Henryk Richter (buggs [at] comlab.uni-rostock.de), and was integrated into Gutenprint during the 3.1 development series. Gutenprint (which was named Gimp-Print prior to release 5.0) itself was originally written by Michael Sweet &lt;mike [at] easysw.com&gt;, who released up to version 2.0; Robert Krawitz released version 3.0. The Gutenprint development team (<a rel="nofollow" href="http://gimp-print.sourceforge.net)">http://gimp-print.sourceforge.net)</a> now maintains the entire package. </p>
<p> The IJS driver was originally written by Russell Lang, and incorporated into Gutenprint (known then as Gimp-Print) in early 2002. This driver corresponds with the IJS protocol 0.32. </p>
<p> The <code>stp</code> driver is no longer supported as of Gutenprint 5.0.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2006 Robert Krawitz (rlk [at] alum.mit.edu) </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place &#8211; Suite 330, Boston, MA 02111-1307, USA.</p>
<h2>AUTHORS</h2>
<p> Robert Krawitz. Originally written by Russell Lang. </p>
<p> This manual page was written by Robert Krawitz (rlk [at] alum.mit.edu) and Roger Leigh (rleigh [at] debian.org).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gs/">gs</a></code>(1) </p>
<h2>Index</h2>
