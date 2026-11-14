---
title: "antiword(1)"
name: "antiword"
section: "1"
letter: "a"
url: "/docs/linux/man/1-antiword/"
description: "antiword – show the text and images of MS Word documents"
---

<h2>NAME</h2>
<p> antiword &#8211; show the text and images of MS Word documents</p>
<h2>SYNOPSIS</h2>
<p> <code>antiword</code> [ <i>options</i> ] <i>wordfiles</i></p>
<h2>DESCRIPTION</h2>
<p> <i>Antiword</i> is an application that displays the text and the images of Microsoft Word documents.<br />
 A wordfile named &#8211; stands for a Word document read from the standard input.<br />
 Only documents made by MS Word version 2 and version 6 or later are supported.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a </code><i>papersize</i></p>
<dd> Output in Adobe PDF form. Printable on paper of the specified size: 10&#215;14, a3, a4, a5, b4, b5, executive, folio, legal, letter, note, quarto, statement or tabloid.</p>
<dt><code>-f</code></p>
<dd> Output in formatted text form. That means that bold text is printed like *bold*, italics like /italics/ and underlined text as _underlined_.</p>
<dt><code>-h</code></p>
<dd> Give a help message.</p>
<dt><code>-i </code><i>image level</i></p>
<dd> The image level determines how images will be shown.</p>
<dl>
<dt>
<dd>
<dl>
<dt>0:</p>
<dd> Use non-standard extensions from Ghostscript. This output may not print on any PostScript printer, but is useful in case no hard copy is needed. It is also useful when Ghostscript is used as a filter to print a PostScript file to a non-PostScript printer.</p>
<dt>1:</p>
<dd> Show no images.</p>
<dt>2:</p>
<dd> PostScript level 2 compatible. (default)</p>
<dt>3:</p>
<dd> PostScript level 3 compatible. (EXPERIMENTAL, Portable Network Graphics (PNG) images are not printed correctly)</dl>
</dl>
<dt><code>-m </code><i>mapping file</i></p>
<dd> This file is used to map Unicode characters to your local character set. The default mapping file depends on the locale.</p>
<dt><code>-p </code><i>papersize</i></p>
<dd> Output in PostScript form. Printable on paper of the specified size: 10&#215;14, a3, a4, a5, b4, b5, executive, folio, legal, letter, note, quarto, statement or tabloid.</p>
<dt><code>-r</code></p>
<dd> Include text removed by the revisioning system.</p>
<dt><code>-s</code></p>
<dd> Include text with the so-called &quot;hidden text&quot; attribute.</p>
<dt><code>-t</code></p>
<dd> Output in text form. (default)</p>
<dt><code>-w </code><i>width</i></p>
<dd> In text mode this is the line width in characters. A value of zero puts an entire paragraph on a line, useful when the text is to used as input for another wordprocessor. This value is ignored in PostScript mode.</p>
<dt><code>-x </code><i>document type definition</i></p>
<dd> Output in XML form. Currently the only document type definition is db (for DocBook).</p>
<dt><code>-L</code></p>
<dd> In PostScript mode: use landscape mode.</dl>
<h2>FILES</h2>
<dl>
<dt>Mapping files like 8859-1.txt</p>
<dd>
 Antiword looks for its mapping files in three directories, in the order given:<br />
 (1) The directory specified by $ANTIWORDHOME<br />
 (2) The directory specified by $HOME/.antiword<br />
 (3) Directory /usr/share/antiword</p>
<dt>The fontnames file</p>
<dd>
 Antiword will look for its fontname file in the same directories as used for the mapping files.<br />
 The fontnames file contains the translation table from font names used by MS Word to font names used by PostScript.</p>
<dt>NOTE:</p>
<dd>
 Antiword cannot tell the difference between a file that does not exist and a file that cannot be opened for reading.</dl>
<h2>ENVIRONMENT</h2>
<p> Antiword uses the environment variable &#8220;ANTIWORDHOME&#8221; as the first directory to look for its files. Antiword uses the environment variable &#8220;HOME&#8221; to find the user&#8217;s home directory. When in text mode it uses the variable &#8220;COLUMNS&#8221; to set the width of the output (unless overridden by the -w option). </p>
<p> Antiword uses the environment variables &#8220;LC_ALL&#8221;, &#8220;LC_CTYPE&#8221; and &#8220;LANG&#8221; (in that order) to get the current locale and uses this information to select the default mapping file.</p>
<h2>BUGS</h2>
<p> Antiword is far from complete. Many features are still missing. Many images are not shown yet. Some of the images that are shown, are shown in the wrong place. PostScript output is only available in ISO 8859-1 and ISO 8859-2.</p>
<h2>WEB SITES</h2>
<p> The most recent released version of Antiword is always available from:<br />
 <a rel="nofollow" href="http://www.winfield.demon.nl/index.html">http://www.winfield.demon.nl/index.html</a><br />
 or try<br />
 <a rel="nofollow" href="http://antiword.cjb.net/">http://antiword.cjb.net/</a></p>
<h2>AUTHOR</h2>
<p> Adri van Os &lt;antiword [at] winfield.demon.nl&gt;<br />
 or try &lt;comments [at] antiword.cjb.net&gt; </p>
<p> R.F. Smith &lt;rsmith [at] xs4all.nl&gt; and<br />
 Sindi Keesan &lt;keesan [at] cyberspace.org&gt;<br />
 contributed to this manual page.</p>
<h2>LICENSE</h2>
<p> Antiword is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> Linux is a registered trademark of Linus Torvalds.<br />
 Adobe, PDF and PostScript are trademarks of Adobe Systems Incorporated.<br />
 Microsoft is a registered trademark and Windows is a trademark of Microsoft Corporation. </p>
<h2>Index</h2>
