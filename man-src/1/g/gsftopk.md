---
title: "gsftopk(1)"
name: "gsftopk"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gsftopk/"
description: "gsftopk – render a ghostscript font in TeX pk form"
---

<h2 class="name">NAME</h2>
<p> gsftopk &#8211; render a ghostscript font in TeX pk form </p>
<h2>SYNOPSIS</h2>
<p> <code>gsftopk</code> [-i <i>path</i>] [-q] [-t] [&#8211;debug=<i>n</i>] [&#8211;dosnames] [&#8211;interpreter=<i>path</i>] [&#8211;mapline=<i>line</i>] [&#8211;mapfile=<i>file</i>] [&#8211;quiet] [&#8211;test] [&#8211;help] [&#8211;version] <i>font</i> <i>dpi</i></p>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>font</i></p>
<dd> Name of the font to be created.</p>
<dt><i>dpi</i></p>
<dd> Desired resolution of the font to be created, in dots per inch. This may be a real number.</dl>
<h2>DESCRIPTION</h2>
<p> <code>gsftopk</code> is a program which calls up the ghostscript program <code><a href="/docs/linux/man/1-gs/">gs</a></code>(1) to render a given font at a given resolution. It packs the resulting characters into the <code>pk</code> file format and writes them to a file whose name is formed from the font name and the resolution (rounded to the nearest integer). The font may be in any format acceptable to Ghostscript, including .<i>pfa</i>, .<i>pfb</i>, .<i>gsf</i>, and .<i>ttf</i> files. </p>
<p> This program should normally be called by a script, such as <code>mktexpk</code>, to create fonts on demand. </p>
<p> <code>gsftopk</code> obtains the character widths from the .<i>tfm</i> file, which must exist in the standard search path. It also must be able to find the font in a map file (such as <code>psfonts.map</code>), formatted as in <code><a href="/docs/linux/man/1-dvips/">dvips</a></code>(1)), unless the <code>&#8211;mapline</code> option is used. The set of map files is given by the <code>&#8211;mapfile</code> option, or in the files <code>config.ps</code>, <code>$HOME/.dvipsrc</code>, and <code>config.gsftopk</code> (as would be used by <code>dvips -Pgsftopk</code>). </p>
<p> The following <code>pk</code> &quot;specials&quot; are added at the end of the output file, to provide an internal check on the contents of the file: &quot;<code>jobname=</code><i>font</i>&quot;, &quot;<code>mag=1</code>&quot;, &quot;<code>mode=modeless</code>&quot;, and &quot;<code>pixels_per_inch=</code><i>dpi</i>&quot;. This is in accordance with the TeX Directory Standard (TDS).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;debug=</code><i>n</i></p>
<dd> Set the <code>Kpathsea</code> debug flags according to the integer <i>n</i>.</p>
<dt><code>&#8211;dosnames</code></p>
<dd> Use a name of the form <i>font</i><code>.pk</code> instead of <i>font</i><code>.</code><i>dpi</i><code>pk</code>.</p>
<dt><code>-h</code>, &#8211;help</p>
<dd> Print a brief help synopsis and exit.</p>
<dt><code>-i </code><i>path</i>, &#8211;interpreter=<i>path</i></p>
<dd> Use <i>path</i> as the Ghostscript interpreter.</p>
<dt><code>&#8211;mapfile=</code><i>file</i></p>
<dd> Use <i>file</i> to look for the map information for <i>font</i>. This should be the full name of the file (in other words, no path searching algorithms are applied).</p>
<dt><code>&#8211;mapline=</code><i>line</i></p>
<dd> Use <i>line</i> instead of looking for an entry in a map file. The first word of <i>line</i> must match <i>font</i>.</p>
<dt><code>-q</code>, &#8211;quiet</p>
<dd> Operate quietly; i.e., without writing any messages to the standard output.</p>
<dt><code>-t</code>, &#8211;test</p>
<dd> Test run: return zero status if the font can be found in the map file(s), and nonzero status if it cannot. If this option is specified, then the <i>dpi</i> argument is optional (since the font will not be generated).</p>
<dt><code>-v</code>, &#8211;version</p>
<dd> Print the version number and exit.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>DVIPSRC</code></p>
<dd> Name of file to read instead of <code>$HOME/.dvipsrc</code>. This should be the full name of the file (in other words, no path searching algorithms are applied).</p>
<dt><code>GSFTOPKFONTS</code></p>
<dd> See <font SIZE="-1"><code>TFMFONTS. </code></font></p>
<dt><code>GSFTOPKHEADERS</code></p>
<dd> See <font SIZE="-1"><code>TEXPSHEADERS. </code></font></p>
<dt><code>PSHEADERS</code></p>
<dd> See <font SIZE="-1"><code>TEXPSHEADERS. </code></font></p>
<dt><code>TEXCONFIG</code></p>
<dd> Colon-separated list of paths to search for map files. An extra colon in the list will include the compiled-in default paths at that point. A double slash will enable recursive subdirectory searching at that point in the path.</p>
<dt><code>TFMFONTS</code></p>
<dd> Colon-separated list of paths to search for the .<i>tfm</i> file associated with the font. Double slashes and extra colons behave as with <font SIZE="-1"><code>TEXCONFIG. </code></font> This information may also be supplied by using the environment variables <font SIZE="-1"><code>TFMFONTS </code></font> or <font SIZE="-1"><code>GSFTOPKFONTS. </code></font> These environment variables are checked in the order <font SIZE="-1"><code>GSFTOPKFONTS, </code></font> <font SIZE="-1"><code>TFMFONTS, </code></font> <font SIZE="-1"><code>TFMFONTS; </code></font> the first one (if any) having a value is used.</p>
<dt><code>TEXPSHEADERS</code></p>
<dd> Colon-separated list of paths to search for the Ghostscript driver file <code>render.ps</code> and for any PostScript header or font files (.<i>enc</i>, .<i>pfa</i>, .<i>pfb</i>, .<i>gsf</i>, or .<i>ttf</i> files). Double slashes and extra colons behave as with <font SIZE="-1"><code>TEXCONFIG. </code></font> This information may also be supplied by using the environment variables <font SIZE="-1"><code>PSHEADERS </code></font> or <font SIZE="-1"><code>GSFTOPKHEADERS. </code></font> These environment variables are checked in the order <font SIZE="-1"><code>GSFTOPKHEADERS, </code></font> <font SIZE="-1"><code>TEXPSHEADERS, </code></font> <font SIZE="-1"><code>PSHEADERS; </code></font> the first one (if any) having a value is used.</p>
<dt><code>TFMFONTS</code></p>
<dd> See <font SIZE="-1"><code>TFMFONTS. </code></font></dl>
<h2>CONFIGURATION</h2>
<p> In order to determine the set of map files to be used and the path for finding PostScript files, <code>gsftopk</code> reads, in order, the files <code>config.ps</code>, <code>.dvipsrc</code>, and <code>config.gsftopk</code>. The files <code>config.ps</code> and <code>config.gsftopk</code> are searched for using the environment variable <font SIZE="-1"><code>TEXCONFIG, </code></font> the <code>Kpathsea</code> configuration file, or the compiled-in default paths. The file <code>.dvipsrc</code> is searched for in the user&#8217;s home directory. </p>
<p> These files are in the same format as for <code>dvips</code> (as well as being in the same locations). The entries used by <code>gsftopk</code> are as follows.</p>
<dl>
<dt>H <i>path</i></p>
<dd> Indicates that the Ghostscript driver file <code>render.ps</code> and the PostScript header and font files are to be searched for using <i>path</i>.</p>
<dt>p <i>file</i></p>
<dd> Indicates that the list of map files is to be erased and replaced by <i>file</i>.</p>
<dt>p +<i>file</i></p>
<dd> Indicates that <i>file</i> is to be added to the list of map files.</dl>
<p> All other entries are ignored. </p>
<p> This is similar to the handling of these options when running <code>dvips -Pgsftopk</code>. For more details, see the <code>Kpathsea</code> manual.</p>
<h2>BUGS</h2>
<p> <code>gsftopk</code> sometimes has trouble with fonts with very complicated characters (such as the Seal of the University of California). This is because <code>gsftopk</code> uses the <code>charpath</code> operator to determine the bounding box of each character. If the character is too complicated, then old versions of Ghostscript fail, causing <code>gsftopk</code> to terminate with an error message</p>
<dl>
<dt>
<dd> <code>Call to gs stopped by signal 10</code></dl>
<p> (The number may vary from system to system; it corresponds to a bus error or a segmentation fault.) The best way to fix this bug is to install a current version of ghostscript. As an alternative, <code>gsftopk</code> can be instructed to use the bounding box provided with the font (if one exists) instead of finding a bounding box for each character. To do this, include the string</p>
<dl>
<dt>
<dd> <code>/usefontbbox true def</code></dl>
<p> in the font map file; <i>e.g.</i>,</p>
<dl>
<dt>
<dd> <code>ucseal /usefontbbox true def</code></dl>
<p> This will not affect use of the font by <code>dvips</code>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gs/">gs</a></code>(1), <code><a href="/docs/linux/man/1-gftopk/">gftopk</a></code>(1), <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1), <code><a href="/docs/linux/man/1-xdvi/">xdvi</a></code>(1), <code><a href="/docs/linux/man/1-dvips/">dvips</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Written by Paul Vojta. This program was inspired by Karl Berry&#8217;s <code>gsrenderfont</code>.</p>
<h2>MODIFICATIONS</h2>
<p> Modified by Yves Arrouye to use Karl Berry&#8217;s <code>Kpathsea</code> library. </p>
<h2>Index</h2>
