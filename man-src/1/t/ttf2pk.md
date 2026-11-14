---
title: "ttf2pk(1)"
name: "ttf2pk"
section: "1"
letter: "t"
url: "/docs/linux/man/1-ttf2pk/"
description: "ttf2pk – convert a TrueType font into TeX’s PK format"
---

<h2 class="name">NAME</h2>
<p> ttf2pk &#8211; convert a TrueType font into TeX&#8217;s PK format </p>
<h2>SYNOPSIS</h2>
<p> <code>ttf2pk</code> [<code>-q</code>] [<code>-n</code>] <i>font-name resolution</i><br />
 <code>ttf2pk</code> <code>-t</code> [<code>-q</code>] <i>font-name</i><br />
 <code>ttf2pk &#8211;version</code> | <code>&#8211;help</code></p>
<h2>DESCRIPTION</h2>
<p> This program converts a TrueType font into a file; the created font can then be used with TeX or LaTeX. </p>
<p> CJKV (Chinese/Japanese/Korean/old Vietnamese) subfonts as created by <code>ttf2tfm</code> are also supported. </p>
<p> <code>ttf2pk</code> always assumes 10pt as the design size for the written TeX font.</p>
<h2>PARAMETERS</h2>
<dl>
<dt><code>-q</code></p>
<dd> This optional switch makes <code>ttf2pk</code> quiet. It suppresses any informational output except warning and error messages.</p>
<dt><code>-n</code></p>
<dd> Use only ` as the extension instead of ` &lt;<i>resolution</i>&gt;</p>
<dt><code>-t</code></p>
<dd> Test for the existence of <i>font-name</i>. Returns 0 on success and prints out the corresponding line of a map file (default: provided the <code>-q</code> switch isn&#8217;t set.</p>
<dt><i>font-name</i></p>
<dd> The TeX name of the font. <code>ttf2pk</code> looks this name up in a map file (see below) for further information how to process the font.</p>
<dt><i>resolution</i></p>
<dd> The resolution, given in dots per inch. Currently the horizontal resolution is equal to the vertical resolution. The design size is always assumed to be 10pt.</p>
<dt><code>&#8211;version</code></p>
<dd> Shows the current version of <code>ttf2pk</code> and the used file search library (e.g.&nbsp;<code>kpathsea</code>).</p>
<dt><code>&#8211;help</code></p>
<dd> Shows usage information.</dl>
<p> Environment variables for file searching are described in the manual page of <code>ttf2tfm</code>.</p>
<h2>THE CONFIGURATION FILE</h2>
<p> <code>ttf2pk</code> uses a small configuration file called in each line it contains a keyword with its value, separated by whitespace. Comment lines can start with any of the following characters: `*&#8217;, `#&#8217;, `;&#8217;, and `%&#8217;. Leading whitespace is ignored. </p>
<p> Currently, only one keyword, `map&#8217;, is recognized in this file; it takes a map file name as a parameter. If no extension is given to the map file name, is appended. No whitespace is allowed in the map file name. The `map&#8217; keyword can be given more than once to specify multiple map files; if the map file name is prepended by a plus sign, it is added to the list of map files to be used. Example: </p>
<p> This makes <code>ttf2pk</code> to first read then </p>
<p> If the configuration file is not found, <code>ttf2pk</code> tries to use instead.</p>
<h2>MAP FILES</h2>
<p> Parameters specified to <code>ttf2tfm</code> are preserved for <code>ttf2pk</code> in map files&#8212;<code>ttf2tfm</code> writes out to standard output, as the last line, a proper entry for a map file. </p>
<p> As an example, a call to </p>
<p> will produce the following line: </p>
<p> See <code><a href="/docs/linux/man/1-ttf2tfm/">ttf2tfm</a></code>(1) and <code><a href="/docs/linux/man/1-afm2tfm/">afm2tfm</a></code>(1) of the <code>dvips</code> package for a detailed description of encoding files. </p>
<p> Here a table listing the various <code>ttf2tfm</code> parameters and the corresponding entries in a map file: </p>
<p> -s<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Slant</p>
<p> -e<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Extend</p>
<p> -p<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Encoding</p>
<p> -f<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Fontindex</p>
<p> -P<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Pid</p>
<p> -E<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Eid</p>
<p> -n<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>PS=Yes</p>
<p> -N<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>PS=Only</p>
<p> -R<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Replacement</p>
<p> -x<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Rotate=Yes</p>
<p> -y<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Y-Offset</p>
<p> Single replacement glyph names given to <code>ttf2tfm</code> with `<code>-r</code><i>&nbsp;old-glyphname new-glyphname</i>&#8216; are directly specified with `<i>old-glyphname</i>=<i>new-glyphname</i>&#8216;. They will be ignored if in subfont mode or if no encoding file is given. </p>
<p> One additional parameter in a map file is unique to <code>ttf2pk</code>: `Hinting&#8217;, which can take the values `On&#8217; or `Off&#8217;. Some fonts (e.g. the CJK part of are rendered incorrectly if hinting is activated. Default is `On&#8217; (you can also use `Yes&#8217;, `No&#8217;, `1&#8242;, and `0&#8242;). </p>
<p> For a description of subfonts (i.e., entries of the form `<i>&lt;namestem&gt;</i> <i>&lt;sfd-filename&gt;</i> please refer to <code><a href="/docs/linux/man/1-ttf2tfm/">ttf2tfm</a></code>(1). </p>
<p> The format of a map file is simple. Each line defines a font; first comes the TeX font name, then its TrueType font file name, followed by the parameters in any order. Case is significant (even for parameter names); the parameters are separated from its values by an equal sign, with whitespace possibly surrounding it. <code>ttf2pk</code> reads in all map files line by line in the order given in the configuration file, continuing until the TeX font specified on the command line is found, otherwise the programs exits with error code 2. Thus you can use any character invalid in a TeX font name to start a comment line. </p>
<p> You can use `\&#8217; as the final character of a line to indicate that the input is continued on the next line. The backslash and the following newline character will be removed. </p>
<p> <code>ttf2pk</code> will abort if it can&#8217;t find or read the TeX font metrics file of the given TeX font name.</p>
<h2>RETURN VALUE</h2>
<p> If the call was successful, 0 will be returned. In case of error, the return value is 1. Finally, if the font can&#8217;t be found in the map files, 2 is returned. This simplifies the inclusion of <code>ttf2pk</code> into scripts like <code>mktexpk</code> for automatic font generation.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ttf2tfm/">ttf2tfm</a></code>(1), <code><a href="/docs/linux/man/1-afm2tfm/">afm2tfm</a></code>(1)</p>
<h2>AVAILABILITY</h2>
<p> <code>ttf2pk</code> is part of the FreeType 1 package, a high quality TrueType rendering library.</p>
<h2>AUTHORS</h2>
<p> Werner LEMBERG<br />
 Fr&eacute;d&eacute;ric LOYER </p>
<h2>Index</h2>
