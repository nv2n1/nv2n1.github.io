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
<dt><code>&#8211;snapshot filename</code></dt>
<dd> Create a snapshot image from the specified layers and save it to filename. The snapshot is saved in PNG format.</dd>
<dt><code>&#8211;lang language</code></dt>
<dd> Set the language used by QGIS. Language is specified using the locale string that matches one of the translations supported by QGIS. For example, to use the German translation, specify <code>&#8211;lang de</code></dd>
<dt><code>&#8211;project filename</code></dt>
<dd> Load the specified <font SIZE="-1">QGIS</font> project file. The layers specified in the project file are loaded, the layers are symbolized, and the view extent is restored.</dd>
<dt><code>&#8211;extent xmin,ymin,xmax,ymax</code></dt>
<dd> Set initial map extent by passing coordinates of that rectangle.</dd>
<dt><code>&#8211;width width</code></dt>
<dd> Width of snapshot to emit</dd>
<dt><code>&#8211;height height</code></dt>
<dd> Height of snapshot to emit</dd>
<dt><code>&#8211;nologo</code></dt>
<dd> Hide splash screen</dd>
<dt><code>&#8211;noplugins</code></dt>
<dd>
 Don&#8217;t restore plugins on startup. Useful if some third-party plugins make QGIS crash during startup.</dd>
<dt><code>&#8211;optionspath path</code></dt>
<dd> Use the given QSettings path</dd>
<dt><code>&#8211;configpath path</code></dt>
<dd> Use the given path for all user configuration</dd>
<dt><code>&#8211;help</code></dt>
<dd>
 Display brief usage help.</dd>
<dt><code>file&#8230;</code></dt>
<dd> A list of one or more files to be loaded into QGIS at startup. Files must consist of a data format supported by QGIS and only disk-based formats can be loaded using this method. This includes shapefiles, MapInfo files, and most raster formats. Data stores that cannot be loaded in this way include PostGIS layers in a PostgreSQL database and GRASS vector/raster data. </dd>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.config/QGIS/qgis.conf</code></dt>
<dd> QGIS preferences file. This file stores windows size/location, loaded plugins, user options, and other application settings.</dd></dl>
<h2>BUGS</h2>
<p> See the QGIS home page (<a rel="nofollow" href="http://qgis.org)">http://qgis.org)</a> for a list of known issues with the latest release.</p>
<h2>AUTHOR</h2>
<p> Gary Sherman &lt;sherman at mrcc.com&gt; </p>
