---
title: "texdoctk(1)"
name: "texdoctk"
section: "1"
letter: "t"
url: "/docs/linux/man/1-texdoctk/"
description: "texdoctk – GUI for easier access of TeX package and program documentations"
---

<h2 class="name">NAME</h2>
<p> texdoctk &#8211; GUI for easier access of TeX package and program documentations </p>
<h2>SYNOPSIS</h2>
<p> <code>texdoctk</code> -[aq]</p>
<h2>DESCRIPTION</h2>
<p> <code>texdoctk</code> is a GUI for easier access to a large part of the vast amount of package and program documentations and tutorials for TeX and its different derivatives (mainly LaTeX). It is optimized and included in the teTeX and fpTeX distributions and also available with TeXLive. </p>
<p> The documentation is grouped into 17 categories; the 18th button of the main panel is inactive by default and intended for use with local additions (see section <code>CONFIGURATION</code> below). </p>
<p> In the settings window you see a checkbox in the html-&gt;ps and text-&gt;ps converter menus for switching on/off output redirect. This is due to the fact that some converters do not write their output into a file but to stdout by default, so a redirect is needed, e.g. </p>
<p> a2ps myfile.txt &gt;myfile.ps</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-v</i></p>
<dd> verbose: enable some viewer messages which are otherwise sent to stderr, as well as some warning popup windows. This can also be set in a configuration file.</p>
<dt><i>-a</i></p>
<dd> autoview: autostart viewer if a listbox contains only one item (this will frequently happen in search results). This can also be set in a configuration file.</dl>
<h2>CONFIGURATION</h2>
<p> The configuration is controlled by the system default configuration file ($TEXMFMAIN)/texdoctk/texdocrc.defaults, most of whose entries can though be overridden by the users&#8217; own optional ~/.texdocrc files and/or command line options.</p>
<h3>The Settings menu and configuration files</h3>
<p> The Settings menu is used to change the user-definable settings of <code>texdoctk</code> for the duration of the program call or as new defaults. The latter case is the purpose of the Save button, which generates or rewrites the user&#8217;s own ~/.texdocrc file. The system defaults cannot be edited with the Settings menu.</p>
<dl>
<dt>Paths</p>
<dd> The TEXMF-type paths on the system are reported, and the user can specify the name of the subdirectory of $HOMETEXMF, where the personal documentation is stored.</p>
<dt>General viewer behaviour</p>
<dd>
<p> <i>Suppress error messages</i> toggle verbose mode (see option -v); default is off. </p>
<p> <i>Autostart viewer for one-item listboxes</i> if a listbox contains only one item (see option -a) </p>
<p> <i>Use text viewer for unknown file format</i> i.e. treat the file as plain text. <code>texdoctk</code> should recognize the usual file formats and also relate names like README to plain text, but some docs may have freely invented names. Default is on; if switched off, trying to view such files will raise an error. The switch does not influence printing: unrecognized formats cannot be printed. </p>
<p> <i>Change viewer colours</i> using either RGB triplets in the format #rrggbb or the standardized names.</p>
<dt>DVI/PostScript/PDF/HTML/Plain text</p>
<dd> For text files, <code>texdoctk</code> provides an own viewer. If this viewer is disabled, but no alternative viewer is specified, <code>texdoctk</code> tries to read the content of the environment variable $PAGER. </p>
<p> If you want to print the documentations, you will need converters to turn non-PS files into PostScript. Here are some suggestions: </p>
<p> dvi-&gt;ps: dvips (is part of teTeX) (<a rel="nofollow" href="http://www.radicaleye.com/dvips.html)">http://www.radicaleye.com/dvips.html)</a> </p>
<p> pdf-&gt;ps: pdf2ps (<a rel="nofollow" href="http://www.cs.wisc.edu/~ghost)">http://www.cs.wisc.edu/~ghost)</a> or Acrobat Reader (<a rel="nofollow" href="http://www.adobe.com)">http://www.adobe.com)</a> </p>
<p> html-&gt;ps: html2ps (<a rel="nofollow" href="http://user.it.uu.se/~jan/html2ps.html)">http://user.it.uu.se/~jan/html2ps.html)</a> </p>
<p> plain text-&gt;ps: a2ps (<a rel="nofollow" href="http://www-inf.enst.fr/~demaille/a2ps/)">http://www-inf.enst.fr/~demaille/a2ps/)</a> </p>
<p> The html-&gt;ps and text-&gt;ps converter menus for switching on/off output redirect. This is due to the fact that some converters do not write their output into a file but to stdout by default, so a redirect is needed, e.g. <code>a2ps myfile.txt &gt;myfile.ps</code></dl>
<p> The system-wide configuration file is ($TEXMFMAIN)/texdoctk/texdocrc.defaults and should only be writable by the administrator of the installation using any text editor. The optional user configuration file is ~/.texdocrc and can override all but those system settings which affect the installation as a whole. The preferred way of changing it is through the Settings menu.</p>
<h3>The databases</h3>
<p> <code>texdoctk</code> comes with a default database file ($TEXMFMAIN)/texdoctk/texdoctk.dat with a special format. It is divided into 17 sections corresponding to the 17 buttons that are active by default. Each section begins with a line </p>
<p> @<i>section_name</i> </p>
<p> where <i>section_name</i> is the text as it appears in the button. This title is followed by the descriptive entries for each documentation, which have this format: </p>
<p> <i>package-label</i>;Short description for listbox (opt. <i>package-name</i>);path in doc directory;optional keywords </p>
<p> (without breaking the line!). Comments (initiated with a #) and empty lines are ignored by the program. The second field is the text displayed in the selection listboxes of <code>texdoctk</code>, and you will usually want to mention the name of the package in parens along with it; the first field is a <code>unique</code> label for the package for internal use of the program which will usually be chosen identical to the package name, but can be different if there is more than one documentation file coming with a package. </p>
<p> The administrator will probably install additional packages in the local texmf tree. The corresponding documentation can be made accessible by an additional database $TEXMFLOCAL/texdoctk/texdoctk-local.dat. Furthermore, individual users possibly install additional packages in an texmf subdirectory of their $HOME, for which they can make an individual database themselves as $TEXMFHOME/texdoctk/texdoctk-pers.dat. After creating such files, texhash must be executed. </p>
<p> Both types of databases must have the same structure as the system database, although they need (and should) not include all its sections if there are no additional entries. For example, if the the package <i>foo</i> is added to the local tree such that its documentation file is ($TEXMFLOCAL)/doc/latex/foo/foo.dvi and it is decided that it fits best into the existing category Graphics, texdoctk-local.dat would look like this: </p>
<p> @Graphics<br />
 foo;Create bells and whistles (foo);latex/foo/foo.dvi;decoration </p>
<p> The entry for <i>foo</i> will then be appended to the list of entries in the Graphics category. The 18th button can be activated in the same way, but using a new category name; possible entries at the beginning of the database which have not been assigned to a category will be assigned to the default Miscellaneous, making the 18th button active with that label. Note that you cannot have more than 18 categories; if there are more, only the one defined last will appear and be used. </p>
<p> If the documentation is included in the .sty file instead of a proper documentation file, the optional keywords should start with -?- directly after the semicolon, where ? is 0, 1, 2 or 3; these are flags which indicate in which part of the .sty the instructions are placed and should help <code>texdoctk</code> to extract the documentation from the style and present it without the code, which would normally be of little use.</p>
<dl>
<dt>0</p>
<dd> no specific place, scattered between the code</p>
<dt>1</p>
<dd> at end, behind ndinput; some .sty files have well-organized documentation behind the end of the actual code, where TeX doesn&#8217;t see it upon compilation</p>
<dt>2</p>
<dd> at beginning, terminated by %%%%%%; in some other cases, some usage information is at the beginning of the .sty as a comment terminated by a line full of %</p>
<dt>3</p>
<dd> as 2, but with a blank line as termination</dl>
<p> See the system database for plenty of examples. </p>
<h2>FILES</h2>
<p> $TEXMFMAIN/texdoctk/texdocrc.defaults system-wide configuration file </p>
<p> ~/.texdocrc (optional) personal configuration file; can also be created with the Settings menu </p>
<p> $TEXMFMAIN/texdoctk/texdoctk.dat default database file for documentation files of the distribution </p>
<p> $TEXMFLOCAL/texdoctk/texdoctk-local.dat (optional) local database file for documentation files </p>
<p> $TEXMFHOME/texdoctk/texdoctk-pers.dat (optional) personal database file of individual users for documentation files</p>
<h2>BUGS</h2>
<p> Widget placement in topic toplevels becomes ugly when the toplevel is stretched or shrunk. </p>
<p> The font in the frame labels of the Settings menu are not forced to the default font; this will become visible e.g. at hi-res screens, where the label font is not scaled up. </p>
<p> Netscape and Mozilla error output will be written to stderr even if the quiet mode was set.</p>
<h2>AUTHOR</h2>
<p> <code>texdoctk</code> was written by Thomas Ruedas &lt;tr [at] geol.ku.dk&gt;. </p>
<p> This manual page was originally written by Adrian Bunk &lt;bunk [at] fs.tum.de&gt; for the Debian GNU/Linux system (but may be used by others). It is now maintained by Thomas Ruedas. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2000-2004 Thomas Ruedas<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
