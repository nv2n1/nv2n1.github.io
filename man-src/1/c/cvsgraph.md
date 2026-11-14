---
title: "cvsgraph(1)"
name: "cvsgraph"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cvsgraph/"
description: "cvsgraph – A CVS/RCS repository grapher"
---

<h2>NAME</h2>
<p> cvsgraph &#8211; A CVS/RCS repository grapher</p>
<h2>SYNOPSIS</h2>
<p> <code>cvsgraph</code> [<i>options</i>] [<i>file</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>CvsGraph</code> generates images and image maps from CVS/RCS repository files.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code></p>
<dd> Deprecated, use -O&#8217;branch_dupbox=-1&#8242; for same functionality.</p>
<dt><code>-c</code> <i>file</i></p>
<dd> Read alternate config from <i>file</i>.</p>
<dt><code>-d</code> <i>level</i></p>
<dd> Enable debug mode at <i>level</i>. The amount of information is determined by a bitwise or of the following: 1=config lexer, 2=config parser, 4=rcsfile lexer, 8=rcsfile parser, 16=rcsfile structure. The <i>level</i> argument may be in decimal, octal or hexadecimal format.</p>
<dt><code>-h</code></p>
<dd> A brief description of possible options.</p>
<dt><code>-i</code></p>
<dd> Generate an image map instead of an image.</p>
<dt><code>-I</code> <i>file</i></p>
<dd> Also write an image map to <i>file</i>. This can be useful if you want to generate both image and image map simultaneously. This halves the total time spent on accessing the repository file because it is parsed only once.<br />
 However, keeping track of auto-generated files can be a bit of a hack if used in HTTP requests (unless you pass both image and HTML file in one HTTP stream).<br />
 Note 1: most time is used for the image-drawing routines (actually libgd), so you might want to think twice in CGI apps.<br />
 Note 2: you can still use &#8216;<code>-o</code>&#8216; to specify an output file for the image. And, if you also specify &#8216;<code>-i</code>&#8216;, then you&#8217;ll get two image maps, for whatever purpose that might be.</p>
<dt><code>-k</code></p>
<dd> Deprecated, use -O&#8217;auto_stretch=-1&#8242; for same functionality.<br />
 This function is <code>not</code> stable.</p>
<dt><code>-M</code> <i>name</i></p>
<dd> Deprecated, use -O&#8217;map_name=&quot;AMapName&quot;&#8217; for same functionality.</p>
<dt><code>-m</code> <i>mod</i></p>
<dd> Use <i>mod</i> as the CVS module. This option overrides <code>cvsmodule</code> in the configuration file.</p>
<dt><code>-O</code> <i>cfg_option=value[;opt=val[&#8230;]]</i></p>
<dd> Set <i>cfg_option</i> to <i>value</i>. Multiple <code>-O</code> are allowed as well as multiple options can be set simultaneously by separating them with &#8216;;&#8217;. See <code><a href="/docs/linux/man/5-cvsgraph-conf/">cvsgraph.conf</a>(5)</code> for a detailed list of options. See also <code>CONFIGURATION</code> below.</p>
<dt><code>-o</code> <i>file</i></p>
<dd> Output to <i>file</i>. Otherwise, output is written to standard output.</p>
<dt><code>-q</code></p>
<dd> Be quiet (i.e. no warnings)</p>
<dt><code>-r</code> <i>path</i></p>
<dd> Use <i>path</i> as the CVS root. This option overrides <code>cvsroot</code> in the configuration file.</p>
<dt><code>-s</code></p>
<dd> Deprecated, use -O&#8217;strip_untagged=-1&#8242; for same functionality.</p>
<dt><code>-S</code></p>
<dd> Deprecated, use -O&#8217;strip_first_rev=-1&#8242; for same functionality.</p>
<dt><code>-u</code></p>
<dd> Deprecated, use -O&#8217;upside_down=-1&#8242; for same functionality.</p>
<dt><code>-V</code></p>
<dd> Print version and exit.</p>
<dt><code>-x</code> <i>{3,4,x}</i></p>
<dd> Set the HTML level of compliance for image maps. Use <i>3</i> for HTML 3.x, <i>4</i> for HTML 4.x and <i>x</i> for XHTML. Default is HTML 3.x compatibility.</p>
<dt><code>-[0-9]</code> <i>txt</i></p>
<dd> Use <i>txt</i> for expansion</dl>
<h2>CONFIGURATION</h2>
<p> <code>CvsGraph</code> starts with reading a configuration file. If the &#8216;<code>-c</code>&#8216; option is given on the command line, then it is read. Otherwise, <code>cvsgraph</code> first looks for a configuration file in the current directory using <i>./cvsgraph.conf</i> and, if not found, tries to open <i>/etc/cvsgraph.conf</i>. Defaults and command line overrides will be used if no configuration file can be opened. The format of the configuration file is described in <code><a href="/docs/linux/man/5-cvsgraph-conf/">cvsgraph.conf</a>(5)</code>. Configuration parameters entered on the command line have always precedence over the configuration file. Configuration options are processed in the following order:<br />
 &#8211; configuration file<br />
 &#8211; &#8216;<code>-O</code>&#8216; command line options<br />
 &#8211; other command line overrides (<code>-bkMmrSsu</code>)<br />
 If you do not want to process any configuration file, then you can set option &#8216;<code>-c /dev/null</code>&#8216;, which will read an empty configuration file. </p>
<p> The location of a repository file is determined by the configuration parameters <code>cvsroot</code> and <code>cvsmodule</code> and the respective command line options &#8216;<code>-r</code>&#8216; and &#8216;<code>-m</code>&#8216;. The <code>cvsroot</code>, <code>cvsmodule</code> and <i>file</i> are concatenated with separating &#8216;/&#8217; path-separators forming the final location:<br />
 &lt;cvsroot&gt;/&lt;cvsmodule&gt;/<i>file</i><br />
 No path-separator is appended if <code>cvsroot</code> and <code>cvsmodule</code> are empty strings. An error message is issued if the resulting path cannot be opened. Note that <code>cvsgraph</code> does not attempt to check any validity of the path components. This enables a user to open any file on the file-system by setting <code>cvsroot</code> and <code>cvsmodule</code> to empty strings.<br />
 For example, <i>cvsgraph -r &#8221; -m &#8221; ../myfile,v</i> would try to open the file <i>../myfile,v</i>. Note that a variety of possibilities yield the same file and all have their advantages and drawbacks, which are mostly related to the possible use of the parameters in text expansions. </p>
<p> If no <i>file</i> is given on the command line, then input is read from standard input. This can make expansion strings somewhat strange looking, but they are composed with the information available. If no input file was given, then the input filename for expansion is set to <code>&lt;stdin&gt;</code>. </p>
<h2>OUTPUT</h2>
<p> The output generated by <code>cvsgraph</code> can be either an image (default) or and HTML image map (&#8216;<code>-i</code>&#8216; and &#8216;<code>-I</code>&#8216; options).<br />
 Images can have several formats, depending on the capabilities of the gd library on which the drawing is built. The configuration allows for GIF, PNG or JPEG type images. Some recent versions of gd do no longer support GIF and PNG will be used instead. GIF support in gd was added again after the lzw patent expired.<br />
 Generation of image maps conforms to the HTML standard and maps rectangular regions of the image where revisions and branches are drawn. Additionally, an extra rectangular region is generated between revisions to support diff generation.</p>
<h2>FILES</h2>
<dl>
<dt><i>/etc/cvsgraph.conf</i></p>
<dd> Configuration file read for default layout parameters.</dl>
<h2>AUTHOR</h2>
<p> <code>CvsGraph</code> is written and maintained by B. Stultiens.<br />
 Send comments and bug reports to <i>cvsgraph [at] akhphd.au.dk</i> (read the mailnote in the README file first) and visit the homepage at:<br />
 <i><a rel="nofollow" href="http://www.akhphd.au.dk/~bertho/cvsgraph/">http://www.akhphd.au.dk/~bertho/cvsgraph/</a></i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-cvsgraph-conf/">cvsgraph.conf</a>(5)</code> </p>
<h2>Index</h2>
