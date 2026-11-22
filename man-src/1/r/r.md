---

title: "r(1)"
name: "r"
section: "1"
letter: "r"
url: "/docs/linux/man/1-r/"
description: "r.what.color – Queries colors for a raster map layer."
---

<p> <i></i><code>r.what.color</code> &#8211; Queries colors for a raster map layer.</p>
<h2>KEYWORDS</h2>
<p> raster</p>
<h2>SYNOPSIS</h2>
<p> <code>r.what.color</code><br/>
 <code>r.what.color help</code><br/>
 <code>r.what.color</code> [-<code>i</code>] <code>input</code>=<i>string</i> [<code>value</code>=<i>float</i>[,<i>float</i>,&#8230;]] [<code>format</code>=<i>string</i>] [&#8211;<code>verbose</code>] [&#8211;<code>quiet</code>]</p>
<h3>Flags:</h3>
<dl>
<dt><code>-i</code></dt>
<dd>
 Read values from stdin</dd>
<dt><code>&#8211;verbose</code></dt>
<dd>
 Verbose module output</dd>
<dt><code>&#8211;quiet</code></dt>
<dd>
 Quiet module output</dd></dl>
<h3>Parameters:</h3>
<dl>
<dt><code>input</code>=<i>string</i></dt>
<dd>
 Name of existing raster map to query colors</dd>
<dt><code>value</code>=<i>float[,float</i>,&#8230;]</dt>
<dd>
 Values to query colors for</dd>
<dt><code>format</code>=<i>string</i></dt>
<dd>
 Output format (printf-style)<br/>
 Default: <i>%d:%d:%d</i></dd></dl>
<h2>DESCRIPTION</h2>
<p> <i>r.what.color</i> outputs the color associated with user-specified category values in a raster input map. </p>
<p> Values may be specified either using the <code>values=</code> option, or by specifying the <code>-i</code> flag and passing the values on stdin, one per line. </p>
<p> For each value which is specified, a line of output will be generated consisting of the category value followed by the color, e.g.:<br/>
 r.what.color input=elevation.dem value=1500<br/>
 1500: 223:127:31 </p>
<p> If the input map is an integer (CELL) map, the category will be written as an integer (no decimal point), otherwise it will be written in floating point format (<i>printf(&quot;%f&quot;)</i> format). </p>
<p> If the lookup fails for a value, the color will be output as an asterisk, e.g.:<br/>
 r.what.color input=elevation.dem value=9999<br/>
 9999: * </p>
<p> If a value cannot be parsed, both the value and the color will be output as an asterisk, e.g.:<br/>
 r.what.color input=elevation.dem value=bogus<br/>
 *: * </p>
<p> The format can be changed using the <code>format=</code> option. The value should be a <i>printf()</i>-style format string containing three conversion specifiers for the red, green and blue values respectively, e.g.:<br/>
 r.what.color input=elevation.dem value=1500 format=&#8217;%02x:%02x:%02x&#8217;<br/>
 1500: df:7f:1f </p>
<p> If your system supports the <i>%m$</i> syntax, you can change the ordering of the components, e.g.:<br/>
 r.what.color input=elevation.dem value=1500 format=&#8217;%3$02x:%2$02x:%1$02x&#8217;<br/>
 1500: 1f:7f:df </p>
<p> Common formats: </p>
<dl>
<dl>
<dt>
</dt><dd> Tcl/Tk: format=&quot;#%02x%02x%02x&quot;</dd>
<dt>
</dt><dd> WxPython: format=&#8217;&quot;#%02x%02x%02x&quot;&#8217; or format=&#8217;&quot;(%d,%d,%d)&quot;&#8217;</dd></dl>
</dl>
<h2>SEE ALSO</h2>
<p> <i> r.what </i></p>
<h2>AUTHOR</h2>
<p> Glynn Clements </p>
<p> Full index </p>
<p> � 2003-2008 GRASS Development Team </p>
