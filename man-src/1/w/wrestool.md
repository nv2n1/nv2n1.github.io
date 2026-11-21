---

title: "wrestool(1)"
name: "wrestool"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wrestool/"
description: "wrestool – extract resources from Microsoft Windows(R) binaries"
---

<p> wrestool &#8211; extract resources from Microsoft Windows(R) binaries </p>
<h2>SYNOPSIS</h2>
<p> <code>wrestool</code> [<i>OPTIONS</i>]&#8230; [<i>FILE</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>wrestool</code> command. This manual page was written for the Debian GNU distribution because the original program does not have a manual page. </p>
<p> Wrestool reads 16- or 32-bit Microsoft Windows(R) binaries and lists or extracts the resources they contain. Some resources require processing before they can be written to files; wrestool is able to do this with icon and cursor resources. </p>
<p> Filters, specified as command line options, control what resources to extract.</p>
<h2>OPTIONS</h2>
<p> These programs follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;).</p>
<dl>
<dt><code>-x, &#8211;extract</code></dt>
<dd> Extract resources. (By default, resources will be extracted to standard out if &#8211;output was not specified.)</dd>
<dt><code>-l, &#8211;list</code></dt>
<dd> Output list of resources (default).</dd>
<dt><code>-t, &#8211;type=[+|-]ID</code></dt>
<dd> Resource type identifier of affected resources. If preceded with a dash (&#8220;-&#8221;), id must be numeric; if preceded with a plus sign (&#8220;+&#8221;), id must be a string. </dd>
<p> The type ID may also be the name of a resource type. (If this is the case, a leading dash or plus sign may not be included.) A list of resource types can be found in the &#8220;Resource Types&#8221; section.</p>
<dt><code>-n, &#8211;name=[+|-]ID</code></dt>
<dd> Resource name identifier of affected resources. Like the &#8211;type option, a leading dash or plus sign controls the datatype of the id.</dd>
<dt><code>-L, &#8211;language=[+|-]ID</code></dt>
<dd> Resource language identifier. Has no effect when processing 16-bit libraries.</dd>
<dt><code>-a, &#8211;all</code></dt>
<dd> Perform operation on all resource (default).</dd>
<dt><code>-o, &#8211;output=PATH</code></dt>
<dd> Where to place extracted resources. If &#8220;PATH&#8221; does not refer to an existing directory, and does not end with a slash (&#8220;/&#8221;), all output will be written to the file &#8220;PATH&#8221;. (This means that if you extract multiple resources, PATH will contain the last resource only.)</dd>
<dt><code>-R, &#8211;raw</code></dt>
<dd> Do not parse resource contents &#8211; extract raw data. (This option will probably be replaced with &#8211;format=raw in future version of icoutils.)</dd>
<dt><code>-v, &#8211;verbose</code></dt>
<dd> Explain what is being done. The verbose option may be specified more than once, like &#8220;-vv&#8221;, to make wrestool even more verbose.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Display a help message and exit.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Output version information and exit.</dd></dl>
<h2>RESOURCE TYPES</h2>
<p> The wrestool program recognizes the resource types listed below. The ids of these resources are always numeric and not strings.</p>
<dl>
<dt><code>cursor (1)</code></dt>
<dd> A single cursor bitmap image. Read as part of group_cursor resources.</dd>
<dt><code>bitmap (2)</code></dt>
<dd> A bitmap image.</dd>
<dt><code>icon (3)</code></dt>
<dd> A single icon bitmap image. Read as part of group_icon resources. This resource is similar to cursor resources; cursors contain four additional bytes of hotspot coordinates.</dd>
<dt><code>menu (4)</code></dt>
<dd> Resources for menus (in popup and menubars). Currently wrestool does not support this resource type.</dd>
<dt><code>dialog (5)</code></dt>
<dd> Definitions (widgets with locations) for dialog boxes. Currently wrestool does not support this resource type.</dd>
<dt><code>string (6)</code></dt>
<dd> The string table resource, containing a number of unicode strings. Currently wrestool does not support this resource type.</dd>
<dt><code>fontdir (7)</code></dt>
<dd> The font directory, containing information on a number of font resources (8). Non-TTF font (.FON) files are actually libraries with resources in them. Currently wrestool does not support this resource type.</dd>
<dt><code>font (8)</code></dt>
<dd> A single font &#8211; the contents of a .FNT file. Read as part of fontdir resources. Currently wrestool does not support this resource type.</dd>
<dt><code>accelerator (9)</code></dt>
<dd> Keyboard accelerator tables. Currently wrestool does not support this resource type.</dd>
<dt><code>rcdata (10)</code></dt>
<dd> Arbitrary resource data, user-defined. There are no restrictions to the format of these resources.</dd>
<dt><code>messagelist (11)</code></dt>
<dd> Not supported.</dd>
<dt><code>group_cursor (12)</code></dt>
<dd> A set of cursors. With a few modifications (and with cursor resources), this resource can be extracted as a .CUR file.</dd>
<dt><code>group_icon (14)</code></dt>
<dd> A set of icons. With a few modifications (and with icons resources), this resource can be extracted as a .ICO file.</dd>
<dt><code>version (16)</code></dt>
<dd> Version information, stored as binary data. Could be extracted without modifications, but the data is of probably little use. Currently wrestool does not support this resource type.</dd>
<dt><code>dlginclude (17)</code></dt>
<dd> Not supported.</dd>
<dt><code>plugplay (19)</code></dt>
<dd> Not supported.</dd>
<dt><code>vxd (20)</code></dt>
<dd> Not supported.</dd>
<dt><code>anicursor (21)</code></dt>
<dd> Animated cursors. Currently wrestool does not support animated cursor or icons, nor does icotool.</dd>
<dt><code>aniicon (22)</code></dt>
<dd> Animated icons. I have only seen these in Windows(R) 3.x. Currently wrestool does not support animated cursor or icons, nor does icotool.</dd></dl>
<h2>EXAMPLES</h2>
<p> List all resources in file `write.exe&#8217;: </p>
<p>&nbsp;<wbr>&nbsp;$&nbsp;<code>wrestool -l write.exe</code><br />
&nbsp;<wbr>&nbsp;&#8211;type=3 &#8211;name=1 &#8211;lang=1033&nbsp;[type=icon offset=0x3120 size=752]<br />
&nbsp;<wbr>&nbsp;&#8211;type=3 &#8211;name=2 &#8211;lang=1033&nbsp;[type=icon offset=0x3410 size=304]<br />
&nbsp;<wbr>&nbsp;&#8211;type=14 &#8211;name=1 &#8211;lang=1033&nbsp;[type=group_icon offset=0x3540 size=34]<br />
&nbsp;<wbr>&nbsp;&#8211;type=16 &#8211;name=1 &#8211;lang=1033&nbsp;[type=version offset=0x3564 size=808] </p>
<p> List all (group-) icon resource in file `write.exe&#8217;: </p>
<p>&nbsp;<wbr>&nbsp;$&nbsp;<code>wrestool -l &#8211;type=group_icon write.exe</code><br />
&nbsp;<wbr>&nbsp;&#8211;type=14 &#8211;name=1 &#8211;lang=1033&nbsp;[type=group_icon offset=0x3540 size=34] </p>
<p> Extract all icons to current directory, naming the destination files `write.exe_T_N.ico&#8217;: </p>
<p>&nbsp;<wbr>&nbsp;$&nbsp;<code>wrestool -x &#8211;output=. -t14 write.exe</code><br />
&nbsp;<wbr>&nbsp;$&nbsp;<code>ls&nbsp;*.ico</code><br />
&nbsp;<wbr>&nbsp;write.exe_14_1.ico</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-extresso/">extresso</a></code>(1), <code><a href="/docs/linux/man/1-genresscript/">genresscript</a></code>(1), <code><a href="/docs/linux/man/1-icotool/">icotool</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Colin Watson &lt;cjwatson [at] debian.org&gt; for the Debian GNU system (but may be used by others). It was later modified by Oskar Liljeblad &lt;oskar [at] osk.mine.nu&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001 Colin Watson </p>
<p> Copyright &#169; 2001 Oskar Liljeblad </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>TRADEMARKS</h2>
<p> Windows is a registered trademark of Microsoft Corporation in the United States and other countries. </p>
