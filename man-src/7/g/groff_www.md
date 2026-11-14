---
title: "groff_www(7)"
name: "groff_www"
section: "7"
letter: "g"
url: "/docs/linux/man/7-groff_www/"
description: "groff_www – groff macros for authoring web pages"
---

<p>groff_www &#8211; groff macros for authoring web pages</p>
<h2>Synopsis</h2>
<p>[<i>option</i> &#8230;] [<i>input-file</i> &#8230;]</p>
<h2>Description</h2>
<p>This manual page describes the GNU -mwww macro package, which is part of the groff document formatting system. The manual page is very a basic guide, and the HTML device driver (<code>grohtml</code>) has been completely rewritten but still remains as in an alpha state. It has been included into the distribution so that a lot of people have a chance to test it. Note that this macro file is automatically called (via the <i>troffrc</i> file) if you use <code>-Thtml</code> or <code>-Txhtml</code>. </p>
<p> To see the hyperlinks in action, please format this man page with the <code>grohtml</code> device. </p>
<p> Here is a summary of the functions found in this macro set. </p>
<table>
<tr VALIGN=top>
<td>.JOBNAME</td>
<td>split output into multiple files
</td>
</tr>
<tr VALIGN=top>
<td>.HX</td>
<td>automatic heading level cut off
</td>
</tr>
<tr VALIGN=top>
<td>.BCL</td>
<td>specify colours on a web page
</td>
</tr>
<tr VALIGN=top>
<td>.BGIMG</td>
<td>specify background image
</td>
</tr>
<tr VALIGN=top>
<td>.URL</td>
<td>create a URL using two parameters
</td>
</tr>
<tr VALIGN=top>
<td>.FTP</td>
<td>create an FTP reference
</td>
</tr>
<tr VALIGN=top>
<td>.MTO</td>
<td>create an HTML email address
</td>
</tr>
<tr VALIGN=top>
<td>.TAG</td>
<td>generate an HTML name
</td>
</tr>
<tr VALIGN=top>
<td>.IMG</td>
<td>include an image file
</td>
</tr>
<tr VALIGN=top>
<td>.PIMG</td>
<td>include PNG image
</td>
</tr>
<tr VALIGN=top>
<td>.MPIMG</td>
<td>place PNG on the margin and wrap text around it
</td>
</tr>
<tr VALIGN=top>
<td>.HnS</td>
<td>begin heading
</td>
</tr>
<tr VALIGN=top>
<td>.HnE</td>
<td>end heading
</td>
</tr>
<tr VALIGN=top>
<td>.LK</td>
<td>emit automatically collected links.
</td>
</tr>
<tr VALIGN=top>
<td>.HR</td>
<td>produce a horizontal rule
</td>
</tr>
<tr VALIGN=top>
<td>.NHR</td>
<td>suppress automatic generation of rules.
</td>
</tr>
<tr VALIGN=top>
<td>.HTL</td>
<td>only generate HTML title
</td>
</tr>
<tr VALIGN=top>
<td>.HEAD</td>
<td>add data to &lt;head&gt; block
</td>
</tr>
<tr VALIGN=top>
<td>.ULS</td>
<td>unorder list begin
</td>
</tr>
<tr VALIGN=top>
<td>.ULE</td>
<td>unorder list end
</td>
</tr>
<tr VALIGN=top>
<td>.OLS</td>
<td>ordered list begin
</td>
</tr>
<tr VALIGN=top>
<td>.OLE</td>
<td>ordered list end
</td>
</tr>
<tr VALIGN=top>
<td>.DLS</td>
<td>definition list begin
</td>
</tr>
<tr VALIGN=top>
<td>.DLE</td>
<td>definition list end
</td>
</tr>
<tr VALIGN=top>
<td>.LI</td>
<td>insert a list item
</td>
</tr>
<tr VALIGN=top>
<td>.DC</td>
<td>generate a drop capital
</td>
</tr>
<tr VALIGN=top>
<td>.HTML</td>
<td>pass an HTML raw request to the device driver
</td>
</tr>
<tr VALIGN=top>
<td>.CDS</td>
<td>code example begin
</td>
</tr>
<tr VALIGN=top>
<td>.CDE</td>
<td>code example end
</td>
</tr>
<tr VALIGN=top>
<td>.ALN</td>
<td>place links on left of main text.
</td>
</tr>
<tr VALIGN=top>
<td>.LNS</td>
<td>start a new two-column table with links in the left.
</td>
</tr>
<tr VALIGN=top>
<td>.LNE</td>
<td>end the two-column table.
</td>
</tr>
<tr VALIGN=top>
<td>.LINKSTYLE</td>
<td>initialize default URL attributes.
</td>
</tr>
</table>
<p> Output of the <code>pic</code>, <code>eqn</code>, <code>refer</code>, and <code>tbl</code> preprocessors is acceptable as input.</p>
<h2>Requests</h2>
<dl>
<dt><code>.JOBNAME filename</code></p>
<dd>Split output into multiple HTML files. A file is split whenever a .SH or .NH 1 is encountered. Its argument is the file stem name for future output files. This option is equivalent to <code>grohtml</code>&#8216;s <code>-j</code> option.</p>
<dt><code>.HX n</code></p>
<dd>Specify the cut off depth when generating links from section headings. For example, a parameter of~2 would cause <code>grohtml</code> to generate a list of links for <code>.NH 1</code> and <code>.NH 2</code> but not for <code>.NH 3</code>. Whereas</p>
<dl>
<dd>
<dl>
<dd>
<pre><code>.HX 0</code></pre>
</dl>
</dl>
<dd>tells <code>grohtml</code> that no heading links should be created at all. Another method for turning automatic headings off is by issuing the command-line switch <code>-P-l</code> to <code>groff</code>.</p>
<dt><code>.BCL foreground background active not-visited visited</code></p>
<dd>This macro takes five parameters: foreground, background, active hypertext link, hypertext link not yet visited, and visited hypertext link colour.</p>
<dt><code>.BGIMG imagefile</code></p>
<dd>the only parameter to this macro is the background image file.</p>
<dt><code>.URL url [description] [after]</code></p>
<dd>generates a URL using either one, two or three arguments. The first parameter is the actual URL, the second is the name of the link, and the third is optional stuff to be printed immediately afterwards. If <code>description</code> and <code>after</code> are absent then the <code>URL</code> becomes the anchor text. Hyphenation is disabled while printing the actual URL; explicit breakpoints should be inserted with the <code>\:</code> escape. Here is how to encode foo</p>
<dl>
<dd>
<dl>
<dd><code>.URL <a rel="nofollow" href="http://\:foo.\:org/">http://\:foo.\:org/</a> foo :</code></dl>
</dl>
<dd>If this is processed by a device other than <code>-Thtml</code> or <code>-Txhtml</code> it appears as:</p>
<dl>
<dd>
<dl>
<dd>foo &lt;<a rel="nofollow" href="http://foo.org">http://foo.org</a>&gt;:</dl>
</dl>
<dd>The URL macro can be of any type; for example we can reference Eric Raymond&#8217;s pic guide by:</p>
<dl>
<dd>
<dl>
<dd><code>.URL pic.html &quot;Eric Raymond&#8217;s pic guide&quot;</code></dl>
</dl>
<dt><code>.MTO address [description] [after]</code></p>
<dd>Generate an email HTML reference. The first argument is mandatory as the email address. The optional second argument is the text you see in your browser. If an empty argument is given, <code>address</code> is used instead. An optional third argument is stuff printed immediately afterwards. Hyphenation is disabled while printing the actual email address. For example, Joe User can be achieved by the following macro:</p>
<dl>
<dd>
<dl>
<dd><code>.MTO joe [at] user.org &quot;Joe User&quot;</code></dl>
</dl>
<dd>Note that all the URLs actually are treated as consuming no textual space in groff. This could be considered as a bug since it causes some problems. To circumvent this, <code><a rel="nofollow" href="http://www.tmac">www.tmac</a></code> inserts a zero-width character which expands to a harmless space (only if run with <code>-Thtml</code> or <code>-Txhtml</code>).</p>
<dt><code>.FTP url [description] [after]</code></p>
<dd>indicates that data can be obtained via FTP. The first argument is the URL and the second is the browser text. A third argument, similar to the macros above, is intended for stuff printed immediately afterwards. The second and the third parameter are optional. Hyphenation is disabled while printing the actual URL. As an example, here is the location of the GNU FTP server The macro example above can be specified as:</p>
<dl>
<dd>
<dl>
<dd><code>.FTP <a href="ftp://\:ftp.gnu.org/">ftp://\:ftp.gnu.org/</a> &quot;GNU FTP server&quot; .</code></dl>
</dl>
<dt><code>.TAG name</code></p>
<dd>Generates an HTML name tag from its argument. This can then be referenced using the URL macro. As you can see, you must precede the tag name with <code>#</code> since it is a local reference. This link was achieved via placing a TAG in the URL description above; the source looks like this:</p>
<dl>
<dd>
<dl>
<dd>
<pre><code>.TP
.B URL
generates
.TAG URL
a URL using either two or three arguments.
...
</code></pre>
</dl>
</dl>
<dt><code>.IMG [-R|-L|-C] filename [width] [height]</code></p>
<dd>Include a picture into the document. The first argument is the horizontal location: right, left, or center (<code>-R</code>, <code>-L</code>, or <code>-C</code>). Alignment is centered by default (<code>-C</code>). The second argument is the filename. The optional third and fourth arguments are the width and height. If the width is absent it defaults to 1~inch. If the height is absent it defaults to the width. This maps onto an HTML img tag. If you are including a PNG image then it is advisable to use the <code>PIMG</code> macro.</p>
<dt><code>.PIMG [-R|-L|-C] filename [width [height]]</code></p>
<dd>Include an image in PNG format. This macro takes exactly the same parameters as the <code>IMG</code> macro; it has the advantage of working with PostScript and HTML devices also since it can automatically convert the image into the EPS format, using the following programs of the <code>netpbm</code> package: <code>pngtopnm</code>, <code>pnmcrop</code>, and <code>pnmtops</code>. If the document isn&#8217;t processed with <code>-Thtml</code> or <code>-Txhtml</code> it is necessary to use the <code>-U</code> option of groff.</p>
<dt><code>.MPIMG [-R|-L] [-G gap] filename [width [height]]</code></p>
<dd>Place a PNG image on the margin and wrap text around it. The first parameters are optional. The alignment: left or right (<code>-L</code> or <code>-R</code>) specifies the margin where the picture is placed at. The default alignment is left (<code>-L</code>). Optionally, <code>-G</code><i>~gap</i> can be used to arrange a gap between the picture and the text that wraps around it. The default gap width is zero.<br />
 The first non-optional argument is the filename. The optional following arguments are the width and height. If the width is absent it defaults to 1~inch. If the height is absent it defaults to the width. Example:</p>
<dl>
<dd>
<dl>
<dd>
<pre><code>.MPIMG -L -G 2c foo.png 3c 1.5c
</code></pre>
</dl>
</dl>
<dd>The height and width may also be given as percentages. The PostScript device calculates the width from the <code>.l</code> register and the height from the <code>.p</code> register. For example:</p>
<dl>
<dd>
<dl>
<dd>
<pre><code>.MPIMG -L -G 2c foo.png 15%
</code></pre>
</dl>
</dl>
<dt><code>.HnS n</code></p>
<dd>Begin heading. The numeric heading level <i>n</i> is specified by the first parameter. Use this macro if your headings contain URL, FTP or MTO macros. Example:</p>
<dl>
<dd>
<dl>
<dd>
<pre><code>.HnS 1
.HR
GNU Troff
.URL <a rel="nofollow" href="http://groff.ffii.org">http://groff.ffii.org</a> (Groff)
--- a
.URL <a rel="nofollow" href="http://www.gnu.org/">http://www.gnu.org/</a> GNU
project.
Hosted by
.URL <a rel="nofollow" href="http://ffii.org/">http://ffii.org/</a> FFII .
.HR
.HnE
</code></pre>
</dl>
</dl>
<dd>In this case you might wish to disable automatic links to headings. This can be done via <code>-P-l</code> from the command line.</p>
<dt><code>.HnE</code></p>
<dd>End heading.</p>
<dt><code>.LK</code></p>
<dd>Force grohtml to place the automatically generated links at this position. If this manual page has been processed with <code>-Thtml</code> or <code>-Txhtml</code> those links can be seen right here.</p>
<dt><code>.HR</code></p>
<dd>Generate a full-width horizontal rule for <code>-Thtml</code> and <code>-Txhtml</code>. No effect for all other devices.</p>
<dt><code>.NHR</code></p>
<dd>Suppress generation of the top and bottom rules which grohtml emits by default.</p>
<dt><code>.HTL</code></p>
<dd>Generate an HTML title only. This differs from the <code>TL</code> macro of the <code>ms</code> macro package which generates both an HTML title and an &lt;H1&gt; heading. Use it to provide an HTML title as search engine fodder but a graphic title in the document. The macro terminates when a space or break is seen (.sp, .br).</p>
<dt><code>.HEAD</code></p>
<dd>Add arbitrary HTML data to the &lt;head&gt; block. Ignored if not processed with <code>-Thtml</code> or <code>-Txhtml</code>. Example:</p>
<dl>
<dd>
<dl>
<dd>
<pre><code>.HEAD &quot;&lt;link \</code>
<code> rel=&quot;&quot;icon&quot;&quot; \</code>
<code> type=&quot;&quot;image/png&quot;&quot; \</code>
<code> href=&quot;&quot;<a rel="nofollow" href="http://foo.org//bar.png">http://foo.org//bar.png</a>&quot;&quot;/&gt;&quot;</code></pre>
</dl>
</dl>
<dt><code>.HTML</code></p>
<dd>All text after this macro is treated as raw HTML. If the document is processed without <code>-Thtml</code> or <code>-Txhtml</code> then the macro is ignored. Internally, this macro is used as a building block for other higher-level macros.</p>
<dd>For example, the <code>BGIMG</code> macro is defined as</p>
<dl>
<dd>
<dl>
<dd>
<pre><code>.de BGIMG
. HTML &lt;body background=\$1&gt;
..
</code></pre>
</dl>
</dl>
<dt><code>.DC l text [color]</code></p>
<dd>Produce a drop capital. The first parameter is the letter to be dropped and enlarged, the second parameter <code>text</code> is the adjoining text whose height the first letter should not exceed. The optional third parameter is the color of the dropped letter. It defaults to black.</p>
<dt><code>.CDS</code></p>
<dd>Start displaying a code section in constant width font.</p>
<dt><code>.CDE</code></p>
<dd>End code display</p>
<dt><code>.ALN [color] [percentage]</code></p>
<dd>Place section heading links automatically to the left of the main text. The color argument is optional and if present indicates which HTML background color is to be used under the links. The optional percentage indicates the amount of width to devote to displaying the links. The default values are #eeeeee and 30 for color and percentage width, respectively. This macro should only be called once at the beginning of the document. After calling this macro each section heading emits an HTML table consisting of the links in the left and the section text on the right.</p>
<dt><code>.LNS</code></p>
<dd>Start a new two-column table with links in the left column. This can be called if the document has text before the first .SH and if .ALN is used. Typically this is called just before the first paragraph and after the main title as it indicates that text after this point should be positioned to the right of the left-hand navigational links.</p>
<dt><code>.LNE</code></p>
<dd>End a two-column table. This should be called at the end of the document if .ALN was used.</p>
<dt><code>.LINKSTYLE color [ fontstyle [ openglyph closeglyph ] ]</code></p>
<dd>Initialize default URL attributes to be used if this macro set is not used with the HTML device. The macro set initializes itself with the following call</p>
<dl>
<dd>
<dl>
<dd>
<pre><code>.LINKSTYLE blue CR \[la] \[ra]
</code></pre>
</dl>
</dl>
<dd>but these values will be superseded by a user call to LINKSTYLE.</dl>
<h2>Section Heading Links</h2>
<p>By default <code>grohtml</code> generates links to all section headings and places these at the top of the HTML document. (See LINKS for details of how to switch this off or alter the position).</p>
<h2>Limitations Of Grohtml</h2>
<p><code>tbl</code> information is currently rendered as a PNG image.</p>
<h2>Files</h2>
<p><i>/usr/:share/:groff/:1.22.4/:tmac/<a rel="nofollow" href="http://www.tmac">www.tmac</a></i></p>
<h2>Authors</h2>
<p>The <i>www</i> macro package was written by Gaius Mulley with additions by Werner Lemberg and Bernd Warken</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1), <code><a href="/docs/linux/man/1-grohtml/">grohtml</a></code>(1), <code><a href="/docs/linux/man/1-netpbm/">netpbm</a></code>(1) </p>
