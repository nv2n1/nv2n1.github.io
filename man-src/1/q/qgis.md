---
title: "qgis(1)"
name: "qgis"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qgis/"
description: "qgis – QGIS Geographic Information System"
---

<h2>NAME</h2>
<p> qgis &#8211; QGIS Geographic Information System</p>
<h2>SYNOPSIS</h2>
<p> <code>qgis [&#8211;snapshot</code> <i>filename]</i><br />
 <code> [&#8211;lang</code> <i>language]</i><br />
 <code> [&#8211;project</code> <i>projectfile]</i><br />
 <code> [&#8211;extent</code> <i>xmin,ymin,xmax,ymax]</i><br />
 <code> [&#8211;width</code> <i>width]</i><br />
 <code> [&#8211;height</code> <i>height]</i><br />
 <code> [&#8211;nologo]</code><br />
 <code> [&#8211;noplugins]</code><br />
 <code> [&#8211;optionspath</code> <i>path]</i><br />
 <code> [&#8211;configpath</code> <i>path]</i><br />
 <code> [&#8211;help]</code><br />
 <code> [file]&#8230;</code><br />
 See OPTIONS for a full description.</p>
<h2>DESCRIPTION</h2>
<p> QGIS is a cross platform, Free and Open Source Geographic Information System (GIS). Supported platforms include Linux/Unix, Mac OS X and Microsoft Windows. QGIS supports vector, raster, and database formats. QGIS is licensed under the GNU General Public License. </p>
<p> Some of the major features include: </p>
<p> *Support for spatially enabled PostGIS tables<br />
 *Support for shapefiles, ArcInfo coverages, Mapinfo, and other formats<br />
&nbsp;<wbr>&nbsp;<wbr>supported by OGR&nbsp;<wbr><br />
 *Raster support for a large number of formats<br />
 *Identify features<br />
 *Display attribute tables<br />
 *Select features<br />
 *GRASS Digitizing<br />
 *Feature labeling </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;snapshot filename</code></p>
<dd> Create a snapshot image from the specified layers and save it to filename. The snapshot is saved in PNG format.</p>
<dt><code>&#8211;lang language</code></p>
<dd> Set the language used by QGIS. Language is specified using the locale string that matches one of the translations supported by QGIS. For example, to use the German translation, specify <code>&#8211;lang de</code></p>
<dt><code>&#8211;project filename</code></p>
<dd> Load the specified <font SIZE="-1">QGIS</font> project file. The layers specified in the project file are loaded, the layers are symbolized, and the view extent is restored.</p>
<dt><code>&#8211;extent xmin,ymin,xmax,ymax</code></p>
<dd> Set initial map extent by passing coordinates of that rectangle.</p>
<dt><code>&#8211;width width</code></p>
<dd> Width of snapshot to emit</p>
<dt><code>&#8211;height height</code></p>
<dd> Height of snapshot to emit</p>
<dt><code>&#8211;nologo</code></p>
<dd> Hide splash screen</p>
<dt><code>&#8211;noplugins</code></p>
<dd>
 Don&#8217;t restore plugins on startup. Useful if some third-party plugins make QGIS crash during startup.</p>
<dt><code>&#8211;optionspath path</code></p>
<dd> Use the given QSettings path</p>
<dt><code>&#8211;configpath path</code></p>
<dd> Use the given path for all user configuration</p>
<dt><code>&#8211;help</code></p>
<dd>
 Display brief usage help.</p>
<dt><code>file&#8230;</code></p>
<dd> A list of one or more files to be loaded into QGIS at startup. Files must consist of a data format supported by QGIS and only disk-based formats can be loaded using this method. This includes shapefiles, MapInfo files, and most raster formats. Data stores that cannot be loaded in this way include PostGIS layers in a PostgreSQL database and GRASS vector/raster data. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.config/QGIS/qgis.conf</code></p>
<dd> QGIS preferences file. This file stores windows size/location, loaded plugins, user options, and other application settings.</dl>
<h2>BUGS</h2>
<p> See the QGIS home page (<a rel="nofollow" href="http://qgis.org)">http://qgis.org)</a> for a list of known issues with the latest release.</p>
<h2>AUTHOR</h2>
<p> Gary Sherman &lt;sherman at mrcc.com&gt; </p>
<h2>Index</h2>
