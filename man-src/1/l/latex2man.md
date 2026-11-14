---
title: "latex2man(1)"
name: "latex2man"
section: "1"
letter: "l"
url: "/docs/linux/man/1-latex2man/"
description: "Latex2man is a tool to translate UNIX manual pages written with LaTeXinto a format understood by the UNIX"
---

<h2 class="name">NAME</h2>
<p> Latex2man is a tool to translate UNIX manual pages written with LaTeXinto a format understood by the UNIX <i></p>
<p> <a href="/docs/linux/man/1-man/">man</a></i>(1)-command. Alternatively HTML, TexInfo, or LaTeX code can be produced too. Output of parts of the text may be suppressed using the conditional text feature (for this, LaTeX generation may be used). </p>
<h2>SYNOPSIS</h2>
<p> latex2man [<code>-t</code><i>transfile</i>] [<code>-c</code><i>CSSfile</i>] [<code>-HMTL</code>] [<code>-h</code>] [<code>-V</code>] [<code>-C</code><i>name</i>] [<code>-a</code><i>char</i>] <i>infile</i> <i>outfile</i> </p>
<h2>DESCRIPTION</h2>
<p> Latex2man reads the file <i>infile</i> and writes <i>outfile</i>. The input must be a LaTeX document using the latex2man LaTeXpackage. Latex2man translates that document into the <i><a href="/docs/linux/man/1-troff/">troff</a></i>(1) format using the <code>-man</code> macro package. </p>
<p> Using the <code>-H</code> option, HTML code can be produced, instead of <i><a href="/docs/linux/man/1-troff/">troff</a></i>(1). With this option you can, optionally, specify a <i>CSSfile</i> as an argument. CSS (Cascading Style Sheets) allows you to control the appearance of the resulting HTML page. See below for the names of CSS classes that are included in the HTML tags as attributes. </p>
<p> Using the <code>-T</code> option, TexInfo code can be produced, instead of <i><a href="/docs/linux/man/1-troff/">troff</a></i>(1). </p>
<p> Using the <code>-M</code> option, <i><a href="/docs/linux/man/1-troff/">troff</a></i>(1) input is produced. </p>
<p> Using the <code>-L</code> option, LaTeX ouput can be produced, instead of <i><a href="/docs/linux/man/1-troff/">troff</a></i>(1). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-t</code><i>transfile</i></p>
<dd>
&nbsp;Translation for user defined LaTeX macros.&nbsp;</p>
<dt><code>-c</code><i>CSSfile</i></p>
<dd>
&nbsp;If you use the&nbsp;<code>-H</code> you can also specify a file that contains CSS style sheets. The link to the CSS file is inserted into the generatedHTML output using the specified <i>CSSfile</i> filename.</p>
<dt><code>-M</code></p>
<dd>
&nbsp;Produce output suitable for the&nbsp;<i><a href="/docs/linux/man/1-man/">man</a></i>(1) command (default).</p>
<dt><code>-H</code></p>
<dd>
&nbsp;Instead of producing output suitable for the&nbsp;<i><a href="/docs/linux/man/1-man/">man</a></i>(1) command, HTML code is produced (despite the name of the command).</p>
<dt><code>-T</code></p>
<dd>
&nbsp;Instead of producing output suitable for the&nbsp;<i><a href="/docs/linux/man/1-man/">man</a></i>(1) command, TexInfo code is produced (despite the name of the command). The generated .texi-file may be processed with <i><a href="/docs/linux/man/1-makeinfo/">makeinfo</a></i>(1) (to produce an .info-file) which in turn may be installed using <i><a href="/docs/linux/man/1-install-info/">install-info</a></i>(1). The Info tags @dircategory and @direntry are provided.</p>
<dt><code>-L</code></p>
<dd>
&nbsp;The LaTeX source is written to the&nbsp;<i>outfile</i>. This is useful in conjunction with the <code>-C</code><i>name</i> option.</p>
<dt><code>-C</code><i>name</i></p>
<dd>
&nbsp;Output the conditional text for&nbsp;<i>name</i>. If more than one name should be given use quotes: <code>-C</code><i>&#8216;name1 name2 &#8230;&#8217;</i><br />
 The following names are defined automatically:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>*</code></p>
<dd> <code>-H</code> defines HTML</p>
<dt><code>*</code></p>
<dd> <code>-T</code> defines TEXI</p>
<dt><code>*</code></p>
<dd> <code>-M</code> defines MAN</p>
<dt><code>*</code></p>
<dd> <code>-L</code> defines LATEX</dl>
</dl>
<dl>
<dt>
<dd>
</dl>
<dt><code>-a</code><i>char</i></p>
<dd>
&nbsp;Is used only in conjunction with -T.<br />
 Background:<br />
 TexInfo ignores all blanks before the first word on a new line. In order to produce some additional space before that word (using \SP) some character has to be printed before the additional space. By default this is a . (dot). The <i>char</i> specifies an alternative for that first character. Giving a blank to <code>-a</code> supresses the indentation of a line.<br />
 Note: only for the first \SP of a series that <i>char</i> is printed.</p>
<dt><code>-h</code></p>
<dd>
&nbsp;Show a help text.&nbsp;</p>
<dt><code>-V</code></p>
<dd>
&nbsp;Show version information.&nbsp;</dl>
<h2>FILES</h2>
<dl>
<dt>latex2man.tex</p>
<dd>
&nbsp;The LaTeX file containing this Man-page.&nbsp;</p>
<dt>latex2man.inc</p>
<dd>
&nbsp;A file read with&nbsp;\input{..}&nbsp;.&nbsp;</p>
<dt>latex2man.sty</p>
<dd>
&nbsp;The LaTeX package defining the environments and&nbsp; commands.</p>
<dt>latex2man.cfg</p>
<dd>
&nbsp;The configuration file for Latex2man LaTeX-package.</p>
<dt>latex2man.css</p>
<dd>
&nbsp;File containing example CSS definitions.&nbsp;</p>
<dt>latex2man.trans</p>
<dd>
&nbsp;File containing example translations of user&nbsp; defined LaTeX macros.</p>
<dt>fancyheadings.sty</p>
<dd>
&nbsp;A LaTeX package used to typeset head- and&nbsp; foot lines.</p>
<dt>fancyhdr.sty</p>
<dd>
&nbsp;A LaTeX package used to typeset head- and foot&nbsp; lines.</p>
<dt>rcsinfo.sty</p>
<dd>
&nbsp;A LaTeX package used to extract and use RCS version&nbsp; control information in LaTeX documents.</dl>
<dl>
<dt><code>latex2man.pdf</code></p>
<dd>
&nbsp;The PDF version of this document.&nbsp;</dl>
<h2>SEE ALSO</h2>
<p> LaTeX,TexInfo, <i><a href="/docs/linux/man/1-troff/">troff</a></i>(1), <i><a href="/docs/linux/man/1-groff/">groff</a></i>(1), <i><a href="/docs/linux/man/1-makeinfo/">makeinfo</a></i>(1). </p>
<h2>LaTeX COMMANDS</h2>
<p> The LaTeX package latex2man is used to write the Man-pages with LaTeX.Since we translate into other text formats, not all LaTeX stuff can be translated. </p>
<h3>PACKAGE OPTIONS</h3>
<p> The latex2man package accepts the following options: </p>
<dl>
<dt>fancy</p>
<dd> use the LaTeX package fancyheadings.</p>
<dt>fancyhdr</p>
<dd> use the LaTeX package fancyhdr.</p>
<dt>nofancy</p>
<dd> neither the LaTeX package fancyheadings nor fancyhdr are used.</dl>
<p> The default option may be specified in the file latex2man.cfg. </p>
<h3>PACKAGE SPECIFIC ENVIRONMENTS</h3>
<p> The following environments are provided by the package:</p>
<dl>
<dt>egin{Name}{chapter}{name}{author}{info}{title}</p>
<dd> The Name environment takes five arguments: 1. the Man-page chapter, 2. the name of the Man-page, 3. the author, 4. some short information about the tool printed in the footline of the Man-page, and 5. a text which is used as title, for HTML and LaTeX (it&#8217;s ignored for output of the Man-page or TeXinfo. The Name environment must be the first environment in the document. Processing starts with this environment. Any text before this is ignored (exception: the setVersion and setDate commands). (Note: all arguments of egin{Name} must be written on one line).</p>
<dt>egin{Table}[width]{columns}</p>
<dd> The Table environment takes two arguments: the first optional one specifies a width of the last column, the second one gives the number of columns. For example:</dl>
<p> egin{Table}[2cm]{3}<br />
 Here &amp; am &amp; I \\hline<br />
 A 1 &amp; A 2 &amp; A 3 1 2 3 4 5 A 3 1 2 3 4 5 \<br />
 B 1 &amp; B 2 &amp; B 3 \<br />
 nd{Table} </p>
<p> will be typeset as: </p>
<table>
<tr VALIGN=top>
<td> Here </td>
<td> am </td>
<td> I
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> A 1 </td>
<td> A 2 </td>
<td> A 3 1 2 3 4 5 A 3 1 2 3 4 5
</td>
</tr>
<tr VALIGN=top>
<td> B 1 </td>
<td> B 2 </td>
<td> B 3
</td>
</tr>
</table>
<p> If no optional <i>width</i> argument is given, all entries are typeset left justified. The <i>width</i> is a length measured absolutly in <i>cm</i>. Processing with LaTeX a p{width} column is typeset as last column. The translation to <i><a href="/docs/linux/man/1-troff/">troff</a></i>(1) commands results in a lw(width) column specification. Translating to HTML and TexInfo ignores the <i>width</i> parameter. </p>
<p> \hline may be used. </p>
<p> If the Man-page is formatted with <i><a href="/docs/linux/man/1-troff/">troff</a></i>(1) and tables are used, the <i><a href="/docs/linux/man/1-tbl/">tbl</a></i>(1) preprocessor should be called, usually by giving a <code>-t</code> to the call of <i><a href="/docs/linux/man/1-troff/">troff</a></i>(1). When viewing the generated manula page using <i><a href="/docs/linux/man/1-man/">man</a></i>(1), <i><a href="/docs/linux/man/1-tbl/">tbl</a></i>(1) is called automatically.</p>
<dl>
<dt>egin{Description}</p>
<dd> is the same as egin{description}</p>
<dt>egin{Description}[label]</p>
<dd> is similar to egin{description}, but the item labels have at minimum the size of the (optional) word <i>label</i>. The difference is visible only in the DVI and PDF-output, not in the troff, TexInfo or HTML output.</p>
<dl>
<dt>
<dd>
<dl>
<dt>a</p>
<dd> |a egin{description}</p>
<dt>ab</p>
<dd> |ab</p>
<dt>abc</p>
<dd> |abc</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd></dl>
<dl>
<dt>a</p>
<dd> |a egin{Description}</p>
<dt>ab</p>
<dd> |ab</p>
<dt>abc</p>
<dd> |abc</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd></dl>
<dl>
<dt>a</p>
<dd> |a egin{Description}[aa]</p>
<dt>ab</p>
<dd> |ab</p>
<dt>abc</p>
<dd> |abc</dl>
</dl>
<dl>
<dt>
<dd>
</dl>
</dl>
<h3>ACCEPTED LaTeX ENVIRONMENTS</h3>
<p> The following environments are accepted:</p>
<dl>
<dt><code>*</code></p>
<dd> description</p>
<dt><code>*</code></p>
<dd> enumerate</p>
<dt><code>*</code></p>
<dd> itemize</p>
<dt><code>*</code></p>
<dd> verbatim</p>
<dt><code>*</code></p>
<dd> center</dl>
<p> They may be nested:</p>
<dl>
<dt><code>*</code></p>
<dd> Itemize and nested center: <center> A centered line.<br />
 Another centered line. </p>
<dt><code>*</code></p>
<dd>
 Another item an nested enumerate </p>
<dl>
<dt>
<dd>
<dl>
<dt>1.</p>
<dd>
 a </p>
<dt>2.</p>
<dd>
 b
</dl>
</dl>
<dl>
<dt>
<dd>
</dl>
</dl>
<h3>PACKAGE SPECIFIC MACROS</h3>
<p> The following commands are provided: </p>
<dl>
<dt>\Opt{option}</p>
<dd>
 Option: \Opt{-o} will be typeset as <code>-o</code>.</p>
<dt>\Arg{argument}</p>
<dd>
 Argument: \Arg{filename} will be typeset as<br />
 <i>filename</i>.</p>
<dt>\OptArg{option}{argument}</p>
<dd>
 Option with Argument:<br />
 \OptArg{-o}{filename} will be typeset as <code>-o</code><i>filename</i>.</p>
<dt>\OptoArg{option}{argument}</p>
<dd>
 Option with optional Argument:<br />
 \OptoArg{-o}{filename} will be<br />
 typeset as <code>-o</code>[<i>filename</i>].</p>
<dt>\oOpt{option}</p>
<dd>
 Optional option, e.g. \oOpt{-o} will be<br />
 typeset as [<code>-o</code>].</p>
<dt>\oArg{argument}</p>
<dd>
 Optional argument, e.g. \oArg{filename}<br />
 will be typeset as [<i>filename</i>].</p>
<dt>\oOptArg{option}{argument}</p>
<dd>
 Optional option with argument, e.g.<br />
 \oOptArg{-o}{filename} will be typeset as [<code>-o</code><i>filename</i>].</p>
<dt>\oOptoArg{option}{argument}</p>
<dd>
 Optional option with optional<br />
 argument, e.g.<br />
 \oOptoArg{-o}{filename} will be typeset as [<code>-o</code>[<i>filename</i>]].</p>
<dt>\File{filename}</p>
<dd>
 used to typeset filenames, e.g.<br />
 \File{filename} will be typeset as filename.</p>
<dt>\Prog{prog}</p>
<dd>
 used to typeset program names, e.g.<br />
 \Prog{latex2man} will be typeset as latex2man.</p>
<dt>\Cmd{command}{chapter}</p>
<dd>
 used to typeset references to other<br />
 commands, e.g.<br />
 \Cmd{latex2man}{1} will be typeset as <i><a href="/docs/linux/man/1-latex2man/">latex2man</a></i>(1).</p>
<dt>\Bar</p>
<dd>
 is typeset as |.</p>
<dt>\Bs</p>
<dd>
 (BackSlash) is typeset as \.</p>
<dt>\Tilde</p>
<dd>
 is typeset as a ~.</p>
<dt>\Dots</p>
<dd>
 is typeset as &#8230;</p>
<dt>\Bullet</p>
<dd>
 us typeset as *.</p>
<dt>\setVersion{..}</p>
<dd>
 set .. as version information. </p>
<dt>\setVersionWord{..}</p>
<dd>
 set .. for the word <i>Version:</i><br />
 in<br />
 the footline.<br />
 The default is \setVersionWord{Version:}. </p>
<dt>\Version</p>
<dd>
 returns the version information. </p>
<dt>\setDate{..}</p>
<dd>
 sets .. as date information. </p>
<dt>\Date</p>
<dd>
 returns the date information. </p>
<dt>\Email{..}</p>
<dd>
 use to mark an Email address:<br />
 \Email{Juergen.Vollmer [at] informatik-vollmer.de} is typeset as:<br />
 <code>Juergen.Vollmer [at] informatik-vollmer.de</code>.</p>
<dt>
