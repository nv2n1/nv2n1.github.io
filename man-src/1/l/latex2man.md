---

title: "latex2man(1)"
name: "latex2man"
section: "1"
letter: "l"
url: "/docs/linux/man/1-latex2man/"
description: "Latex2man is a tool to translate UNIX manual pages written with LaTeXinto a format understood by the UNIX"
---

<p> Latex2man is a tool to translate UNIX manual pages written with LaTeXinto a format understood by the UNIX <i> </p>
<p> <a href="/docs/linux/man/1-man/">man</a></i>(1)-command. Alternatively HTML, TexInfo, or LaTeX code can be produced too. Output of parts of the text may be suppressed using the conditional text feature (for this, LaTeX generation may be used). </p>
<p> latex2man [<code>-t</code><i>transfile</i>] [<code>-c</code><i>CSSfile</i>] [<code>-HMTL</code>] [<code>-h</code>] [<code>-V</code>] [<code>-C</code><i>name</i>] [<code>-a</code><i>char</i>] <i>infile</i> <i>outfile</i> </p>
<p> Latex2man reads the file <i>infile</i> and writes <i>outfile</i>. The input must be a LaTeX document using the latex2man LaTeXpackage. Latex2man translates that document into the <i><a href="/docs/linux/man/1-troff/">troff</a></i>(1) format using the <code>-man</code> macro package. </p>
<p> Using the <code>-H</code> option, HTML code can be produced, instead of <i><a href="/docs/linux/man/1-troff/">troff</a></i>(1). With this option you can, optionally, specify a <i>CSSfile</i> as an argument. CSS (Cascading Style Sheets) allows you to control the appearance of the resulting HTML page. See below for the names of CSS classes that are included in the HTML tags as attributes. </p>
<p> Using the <code>-T</code> option, TexInfo code can be produced, instead of <i><a href="/docs/linux/man/1-troff/">troff</a></i>(1). </p>
<p> Using the <code>-M</code> option, <i><a href="/docs/linux/man/1-troff/">troff</a></i>(1) input is produced. </p>
<p> Using the <code>-L</code> option, LaTeX ouput can be produced, instead of <i><a href="/docs/linux/man/1-troff/">troff</a></i>(1). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-t</code><i>transfile</i></dt>
<dd> <p> <br />
&nbsp;Translation for user defined LaTeX macros.&nbsp; </p>
 </dd>
<dt><code>-c</code><i>CSSfile</i></dt>
<dd> <p> <br />
&nbsp;If you use the&nbsp;<code>-H</code> you can also specify a file that contains CSS style sheets. The link to the CSS file is inserted into the generatedHTML output using the specified <i>CSSfile</i> filename. </p>
 </dd>
<dt><code>-M</code></dt>
<dd> <p> <br />
&nbsp;Produce output suitable for the&nbsp;<i><a href="/docs/linux/man/1-man/">man</a></i>(1) command (default). </p>
 </dd>
<dt><code>-H</code></dt>
<dd> <p> <br />
&nbsp;Instead of producing output suitable for the&nbsp;<i><a href="/docs/linux/man/1-man/">man</a></i>(1) command, HTML code is produced (despite the name of the command). </p>
 </dd>
<dt><code>-T</code></dt>
<dd> <p> <br />
&nbsp;Instead of producing output suitable for the&nbsp;<i><a href="/docs/linux/man/1-man/">man</a></i>(1) command, TexInfo code is produced (despite the name of the command). The generated .texi-file may be processed with <i><a href="/docs/linux/man/1-makeinfo/">makeinfo</a></i>(1) (to produce an .info-file) which in turn may be installed using <i><a href="/docs/linux/man/1-install-info/">install-info</a></i>(1). The Info tags @dircategory and @direntry are provided. </p>
 </dd>
<dt><code>-L</code></dt>
<dd> <p> <br />
&nbsp;The LaTeX source is written to the&nbsp;<i>outfile</i>. This is useful in conjunction with the <code>-C</code><i>name</i> option. </p>
 </dd>
<dt><code>-C</code><i>name</i></dt>
<dd> <p> <br />
&nbsp;Output the conditional text for&nbsp;<i>name</i>. If more than one name should be given use quotes: <code>-C</code><i>&#8216;name1 name2 ...&#8216;</i> <br />
 The following names are defined automatically: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>*</code></dt>
<dd> <p> <code>-H</code> defines HTML </p>
 </dd>
<dt><code>*</code></dt>
<dd> <p> <code>-T</code> defines TEXI </p>
 </dd>
<dt><code>*</code></dt>
<dd> <p> <code>-M</code> defines MAN </p>
 </dd>
<dt><code>*</code></dt>
<dd> <p> <code>-L</code> defines LATEX </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt><code>-a</code><i>char</i></dt>
<dd> <p> <br />
&nbsp;Is used only in conjunction with -T. <br />
 Background: <br />
 TexInfo ignores all blanks before the first word on a new line. In order to produce some additional space before that word (using \SP) some character has to be printed before the additional space. By default this is a . (dot). The <i>char</i> specifies an alternative for that first character. Giving a blank to <code>-a</code> supresses the indentation of a line. <br />
 Note: only for the first \SP of a series that <i>char</i> is printed. </p>
 </dd>
<dt><code>-h</code></dt>
<dd> <p> <br />
&nbsp;Show a help text.&nbsp; </p>
 </dd>
<dt><code>-V</code></dt>
<dd> <p> <br />
&nbsp;Show version information.&nbsp; </p>
 </dd></dl>
<h2>FILES</h2>
<dl>
<dt>latex2man.tex</dt>
<dd> <p> <br />
&nbsp;The LaTeX file containing this Man-page.&nbsp; </p>
 </dd>
<dt>latex2man.inc</dt>
<dd> <p> <br />
&nbsp;A file read with&nbsp;\input{..}&nbsp;.&nbsp; </p>
 </dd>
<dt>latex2man.sty</dt>
<dd> <p> <br />
&nbsp;The LaTeX package defining the environments and&nbsp; commands. </p>
 </dd>
<dt>latex2man.cfg</dt>
<dd> <p> <br />
&nbsp;The configuration file for Latex2man LaTeX-package. </p>
 </dd>
<dt>latex2man.css</dt>
<dd> <p> <br />
&nbsp;File containing example CSS definitions.&nbsp; </p>
 </dd>
<dt>latex2man.trans</dt>
<dd> <p> <br />
&nbsp;File containing example translations of user&nbsp; defined LaTeX macros. </p>
 </dd>
<dt>fancyheadings.sty</dt>
<dd> <p> <br />
&nbsp;A LaTeX package used to typeset head- and&nbsp; foot lines. </p>
 </dd>
<dt>fancyhdr.sty</dt>
<dd> <p> <br />
&nbsp;A LaTeX package used to typeset head- and foot&nbsp; lines. </p>
 </dd>
<dt>rcsinfo.sty</dt>
<dd> <p> <br />
&nbsp;A LaTeX package used to extract and use RCS version&nbsp; control information in LaTeX documents. </p>
 </dd></dl>
<dl>
<dt><code>latex2man.pdf</code></dt>
<dd> <p> <br />
&nbsp;The PDF version of this document.&nbsp; </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<p> LaTeX,TexInfo, <i><a href="/docs/linux/man/1-troff/">troff</a></i>(1), <i><a href="/docs/linux/man/1-groff/">groff</a></i>(1), <i><a href="/docs/linux/man/1-makeinfo/">makeinfo</a></i>(1). </p>
<h2>LaTeX COMMANDS</h2>
<p> The LaTeX package latex2man is used to write the Man-pages with LaTeX.Since we translate into other text formats, not all LaTeX stuff can be translated. </p>
<h3>PACKAGE OPTIONS</h3>
<p> The latex2man package accepts the following options: </p>
<dl>
<dt>fancy </dt>
<dd> <p> use the LaTeX package fancyheadings. </p>
 </dd>
<dt>fancyhdr </dt>
<dd> <p> use the LaTeX package fancyhdr. </p>
 </dd>
<dt>nofancy </dt>
<dd> <p> neither the LaTeX package fancyheadings nor fancyhdr are used. </p>
 </dd></dl>
<p> The default option may be specified in the file latex2man.cfg. </p>
<h3>PACKAGE SPECIFIC ENVIRONMENTS</h3>
<p> The following environments are provided by the package: </p>
<dl>
<dt>\begin{Name}{chapter}{name}{author}{info}{title} </dt>
<dd> <p> The Name environment takes five arguments: 1. the Man-page chapter, 2. the name of the Man-page, 3. the author, 4. some short information about the tool printed in the footline of the Man-page, and 5. a text which is used as title, for HTML and LaTeX (it&#8217;s ignored for output of the Man-page or TeXinfo. The Name environment must be the first environment in the document. Processing starts with this environment. Any text before this is ignored (exception: the setVersion and setDate commands). (Note: all arguments of \begin{Name} must be written on one line). </p>
 </dd>
<dt>\begin{Table}[width]{columns} </dt>
<dd> <p> The Table environment takes two arguments: the first optional one specifies a width of the last column, the second one gives the number of columns. For example: </p>
 </dd></dl>
<p> \begin{Table}[2cm]{3} <br />
 Here &amp; am &amp; I \\\hline <br />
 A 1 &amp; A 2 &amp; A 3 1 2 3 4 5 A 3 1 2 3 4 5 \\ <br />
 B 1 &amp; B 2 &amp; B 3 \\ <br />
 \end{Table} </p>
<p> will be typeset as: </p>
<table>
<tr VALIGN=top>
<td> Here </td>
<td> am </td>
<td> I 
</td>
</tr>
<tr VALIGN=top>
<td><hr />
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
<p> If the Man-page is formatted with <i><a href="/docs/linux/man/1-troff/">troff</a></i>(1) and tables are used, the <i><a href="/docs/linux/man/1-tbl/">tbl</a></i>(1) preprocessor should be called, usually by giving a <code>-t</code> to the call of <i><a href="/docs/linux/man/1-troff/">troff</a></i>(1). When viewing the generated manula page using <i><a href="/docs/linux/man/1-man/">man</a></i>(1), <i><a href="/docs/linux/man/1-tbl/">tbl</a></i>(1) is called automatically. </p>
<dl>
<dt>\begin{Description} </dt>
<dd> <p> is the same as \begin{description} </p>
 </dd>
<dt>\begin{Description}[label] </dt>
<dd> <p> is similar to \begin{description}, but the item labels have at minimum the size of the (optional) word <i>label</i>. The difference is visible only in the DVI and PDF-output, not in the troff, TexInfo or HTML output. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>a </dt>
<dd> <p> |a \begin{description} </p>
 </dd>
<dt>ab </dt>
<dd> <p> |ab </p>
 </dd>
<dt>abc </dt>
<dd> <p> |abc </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd>
<dl>
<dd>  </dd></dl>
<dl>
<dt>a </dt>
<dd> <p> |a \begin{Description} </p>
 </dd>
<dt>ab </dt>
<dd> <p> |ab </p>
 </dd>
<dt>abc </dt>
<dd> <p> |abc </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd>
<dl>
<dd>  </dd></dl>
<dl>
<dt>a </dt>
<dd> <p> |a \begin{Description}[aa] </p>
 </dd>
<dt>ab </dt>
<dd> <p> |ab </p>
 </dd>
<dt>abc </dt>
<dd> <p> |abc </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
</dl>
<h3>ACCEPTED LaTeX ENVIRONMENTS</h3>
<p> The following environments are accepted: </p>
<dl>
<dt><code>*</code></dt>
<dd> <p> description </p>
 </dd>
<dt><code>*</code></dt>
<dd> <p> enumerate </p>
 </dd>
<dt><code>*</code></dt>
<dd> <p> itemize </p>
 </dd>
<dt><code>*</code></dt>
<dd> <p> verbatim </p>
 </dd>
<dt><code>*</code></dt>
<dd> <p> center </p>
 </dd></dl>
<p> They may be nested: </p>
<dl>
<dt><code>*</code></dt>
<dd> <p> Itemize and nested center: <center> A centered line.<br />
 Another centered line. <br />
 <br />
 <br />
 </p>
 </dd>
<dt><code>*</code></dt>
<dd> <p> <br />
 Another item an nested enumerate <br />
 </p>
 </dd>
<dl>
<dd> <p> <br />
 </p>
 </dd>
<dl>
<dt>1.</dt>
<dd> <p> <br />
 a <br />
 </p>
 </dd>
<dt>2.</dt>
<dd> <p> <br />
 b <br />
 </p>
 </dd></dl>
</dl>
<p> <br />
 </p>
<dl>
<dd> <p> <br />
 </p>
<p> <br />
 </p>
 </dd></dl>
<p> <br />
 </dl>
 </p>
<p> <br />
  </p>
<h3>PACKAGE SPECIFIC MACROS</h3>
<p> <br />
 </p>
<p> <br />
 The following commands are provided: <br />
 </p>
<dl>
<dt>\Opt{option} </dt>
<dd> <p> <br />
 Option: \Opt{-o} will be typeset as <code>-o</code>.<br />
 </p>
 </dd>
<dt>\Arg{argument} </dt>
<dd> <p> <br />
 Argument: \Arg{filename} will be typeset as <br />
 <i>filename</i>.<br />
 </p>
 </dd>
<dt>\OptArg{option}{argument} </dt>
<dd> <p> <br />
 Option with Argument:<br />
 \OptArg{-o}{filename} will be typeset as <code>-o</code><i>filename</i>.<br />
 </p>
 </dd>
<dt>\OptoArg{option}{argument} </dt>
<dd> <p> <br />
 Option with optional Argument:<br />
 \OptoArg{-o}{filename} will be <br />
 typeset as <code>-o</code>[<i>filename</i>].<br />
 </p>
 </dd>
<dt>\oOpt{option} </dt>
<dd> <p> <br />
 Optional option, e.g. \oOpt{-o} will be <br />
 typeset as [<code>-o</code>].<br />
 </p>
 </dd>
<dt>\oArg{argument} </dt>
<dd> <p> <br />
 Optional argument, e.g. \oArg{filename} <br />
 will be typeset as [<i>filename</i>].<br />
 </p>
 </dd>
<dt>\oOptArg{option}{argument} </dt>
<dd> <p> <br />
 Optional option with argument, e.g.<br />
 \oOptArg{-o}{filename} will be typeset as [<code>-o</code><i>filename</i>].<br />
 </p>
 </dd>
<dt>\oOptoArg{option}{argument} </dt>
<dd> <p> <br />
 Optional option with optional <br />
 argument, e.g.<br />
 \oOptoArg{-o}{filename} will be typeset as [<code>-o</code>[<i>filename</i>]].<br />
 </p>
 </dd>
<dt>\File{filename} </dt>
<dd> <p> <br />
 used to typeset filenames, e.g. <br />
 \File{filename} will be typeset as filename.<br />
 </p>
 </dd>
<dt>\Prog{prog} </dt>
<dd> <p> <br />
 used to typeset program names, e.g. <br />
 \Prog{latex2man} will be typeset as latex2man.<br />
 </p>
 </dd>
<dt>\Cmd{command}{chapter} </dt>
<dd> <p> <br />
 used to typeset references to other <br />
 commands, e.g.<br />
 \Cmd{latex2man}{1} will be typeset as <i><a href="/docs/linux/man/1-latex2man/">latex2man</a></i>(1).<br />
 </p>
 </dd>
<dt>\Bar </dt>
<dd> <p> <br />
 is typeset as |.<br />
 </p>
 </dd>
<dt>\Bs </dt>
<dd> <p> <br />
 (BackSlash) is typeset as \.<br />
 </p>
 </dd>
<dt>\Tilde </dt>
<dd> <p> <br />
 is typeset as a ~.<br />
 </p>
 </dd>
<dt>\Dots </dt>
<dd> <p> <br />
 is typeset as ...<br />
 <br />
 </p>
 </dd>
<dt>\Bullet </dt>
<dd> <p> <br />
 us typeset as *.<br />
 </p>
 </dd>
<dt>\setVersion{..} </dt>
<dd> <p> <br />
 set .. as version information. <br />
 </p>
 </dd>
<dt>\setVersionWord{..} </dt>
<dd> <p> <br />
 set .. for the word <i>Version:</i><br />
 in <br />
 the footline.<br />
 The default is \setVersionWord{Version:}. <br />
 </p>
 </dd>
<dt>\Version </dt>
<dd> <p> <br />
 returns the version information. <br />
 </p>
 </dd>
<dt>\setDate{..} </dt>
<dd> <p> <br />
 sets .. as date information. <br />
 </p>
 </dd>
<dt>\Date </dt>
<dd> <p> <br />
 returns the date information. <br />
 </p>
 </dd>
<dt>\Email{..} </dt>
<dd> <p> <br />
 use to mark an Email address:<br />
 \Email{Juergen.Vollmer [at] informatik-vollmer.de} is typeset as:<br />
 <code>Juergen.Vollmer [at] informatik-vollmer.de</code>.<br />
 </p>
 </dd>
<dt>\URL{..} </dt>
<dd> <p> <br />
 use to mark an URL: <br />
 \URL{<a rel="nofollow" href="http://www.foo.de/\Tilde">http://www.foo.de/\Tilde</a> vollmer} is typeset as<br />
 <code><a rel="nofollow" href="http://www.foo.de/~vollmer">http://www.foo.de/~vollmer</a></code>.<br />
 </p>
 </dd>
<dt>\LatexManEnd </dt>
<dd> <p> <br />
 the input file is read and processed until reading <br />
 end-of-file or<br />
 \LatexManEnd (at the beginning of a line). <br />
 LaTeXignores this command. <br />
 </p>
 </dd>
<dt>\Lbr, \Rbr </dt>
<dd> <p> <br />
 is typeset as [ and ] (these variants are <br />
 needed only somtimes like in<br />
 \item[FooBar\LBr xx \Lbr]. Usually [ ] will work. <br />
 </p>
 </dd>
<dt>\LBr, \RBr </dt>
<dd> <p> <br />
 is typeset as { and } (these variants are <br />
 needed when using { or } as arguments to macros. <br />
 </p>
 </dd>
<dt>\Circum </dt>
<dd> <p> <br />
 is typeset as ^.<br />
 </center> </p>
 </dd>
<dt>\Percent </dt>
<dd> <p> is typeset as %. </p>
 </dd>
<dt>\TEXbr </dt>
<dd> <p> If processed with LaTeX causes a linebreak (i.e. is equivalent to \\).In the output of latex2man this macro is ignored. </p>
 </dd>
<dt>\TEXIbr </dt>
<dd> <p> If TexInfo output is generated, causes a linebreak (i.e. is equivalent to \\),otherwise ignored. </p>
 </dd>
<dt>\MANbr </dt>
<dd> <p> If Man-Page output is generated, causes a linebreak (i.e. is equivalent to \\),otherwise ignored. </p>
 </dd>
<dt>\HTMLbr </dt>
<dd> <p> If HTML output is generated, causes a linebreak (i.e. is equivalent to \\),otherwise ignored. </p>
 </dd>
<dt>\medskip </dt>
<dd> <p> An empty line. </p>
 </dd>
<dt>\SP </dt>
<dd> <p> Produces some extra space, works also at the beginning of lines. The code of the second line looks like: \SP abc \SP\SP xx\\: <br />
 abc xx <br />
 abc xx <br />
 abc xx </p>
 </dd></dl>
<p> Note: Due to some ``problems&#8217;&#8216; with TexInfo, the lines starting with \SP have a leading . (dot) in the TexInfo output, see <code>-a</code><i>char</i>. </p>
<h3>ACCEPTED MACROS FROM THE RCSINFO PACKAGE</h3>
<dl>
<dt>\rcsInfo $Id ...$ </dt>
<dd> <p> if the LaTeX package rcsinfo is used, this command is used to extract the date of the Man-page. </p>
 </dd>
<dt>\rcsInfoLongDate </dt>
<dd> <p> if the LaTeX package rcsinfo is used, this command is used to typeset the date coded in the $Id ..$ string. </p>
 </dd></dl>
<h3>ACCEPTED LaTeX MACROS</h3>
<p> The following standard LaTeX commands are accepted: 