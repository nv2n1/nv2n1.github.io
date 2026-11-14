---
title: "groff_tmac(5)"
name: "groff_tmac"
section: "5"
letter: "g"
url: "/docs/linux/man/5-groff_tmac/"
description: "groff_tmac – macro files in the roff typesetting system"
---

<p>groff_tmac &#8211; macro files in the roff typesetting system</p>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/7-roff/">roff</a></code>(7) type-setting system provides a set of macro packages suitable for special kinds of documents. Each macro package stores its macros and definitions in a file called the package&#8217;s <code>tmac file</code>. The name is deduced from &#8216;<code>T</code><i>roff</i><code>MAC</code><i>ros</i>&#8216;. </p>
<p> The tmac files are normal roff source documents, except that they usually contain only definitions and setup commands, but no text. All tmac files are kept in a single or a small number of directories, the <code>tmac</code> directories.</p>
<h2>Groff Macro Packages</h2>
<p><i>groff</i> provides all classical macro packages, some more full packages, and some secondary packages for special purposes. Note that it is not possible to use multiple primary macro packages at the same time; saying e.g.</p>
<dl>
<dd><i>sh#</i> groff -m man -m ms foo</dl>
<p> or</p>
<dl>
<dd><i>sh#</i> groff -m man foo -m ms bar</dl>
<p> fails. Exception to this is the use of man pages written with either the <code>mdoc</code> or the <code>man</code> macro package. See below the description of the <i>andoc.tmac</i> file.</p>
<h3>Man~Pages</h3>
<dl>
<dt><i>man</i></p>
<dd>This is the classical macro package for Unix manual pages (man~pages); it is quite handy and easy to use; see <code><a href="/docs/linux/man/7-groff_man/">groff_man</a></code>(7).</p>
<dt><i>doc</i></p>
<dd><i>mdoc</i> An alternative macro package for man~pages mainly used in BSD systems; it provides many new features, but it is not the standard for man~pages; see <code><a href="/docs/linux/man/7-groff_mdoc/">groff_mdoc</a></code>(7).</p>
<dt><i>andoc</i></p>
<dd><i>mandoc</i> Use this file in case you don&#8217;t know whether the <code>man</code> macros or the <code>mdoc</code> package should be used. Multiple man pages (in either format) can be handled.</dl>
<h3>Full Packages</h3>
<p>The packages in this section provide a complete set of macros for writing documents of any kind, up to whole books. They are similar in functionality; it is a matter of taste which one to use.</p>
<dl>
<dt><i>me</i></p>
<dd>The classical <i>me</i> macro package; see <code><a href="/docs/linux/man/7-groff_me/">groff_me</a></code>(7).</p>
<dt><i>mm</i></p>
<dd>The semi-classical <i>mm</i> macro package; see <code><a href="/docs/linux/man/7-groff_mm/">groff_mm</a></code>(7).</p>
<dt><i>mom</i></p>
<dd>The new <i>mom</i> macro package, only available in groff. As this is not based on other packages, it can be freely designed. So it is expected to become quite a nice, modern macro package. See <code><a href="/docs/linux/man/7-groff_mom/">groff_mom</a></code>(7).</p>
<dt><i>ms</i></p>
<dd>The classical <i>ms</i> macro package; see <code><a href="/docs/linux/man/7-groff_ms/">groff_ms</a></code>(7).</dl>
<h3>Language-specific Packages</h3>
<dl>
<dt><i>cs</i></p>
<dd>This file adds support for Czech localization, including the main macro packages (me, mom, mm, and ms).</p>
<dd>Note that <i>cs.tmac</i> sets the input encoding to latin-2.</p>
<dt><i>de</i></p>
<dd><i>den</i> German localization support, including the main macro packages (me, mom, mm, and ms).</p>
<dd><i>de.tmac</i> selects hyphenation patterns for traditional orthography, and <i>den.tmac</i> does the same for the new orthography (&#8216;Rechtschreibreform&#8217;). It should be used as the last macro package on the command line.</p>
<dt><i>fr</i></p>
<dd>This file adds support for French localization, including the main macro packages (me, mom, mm, and ms). Example:</p>
<dl>
<dd>
<dl>
<dd><i>sh#</i> groff -ms -mfr foo.ms &gt; foo.ps</dl>
</dl>
<dd>Note that <i>fr.tmac</i> sets the input encoding to latin-9 to get proper support of the &#8216;oe&#8217; ligature.</p>
<dt><i>sv</i></p>
<dd>Swedish localization support, including the me, mom, and ms macro packages. Note that Swedish for the mm macros is handled separately; see <code><a href="/docs/linux/man/7-groff_mmse/">groff_mmse</a></code>(7) (only in Swedish locales). It should be used as the last macro package on the command line.</dl>
<h3>Input Encodings</h3>
<dl>
<dt><i>latin1</i></p>
<dd><i>latin2</i> <i>latin5</i> <i>latin9</i> Various input encodings supported directly by groff. Normally, this macro is loaded at the very beginning of a document or specified as the first macro argument on the command line. <code>roff</code> loads latin1 by default at start-up. Note that these macro packages don&#8217;t work on EBCDIC hosts.</p>
<dt><i>cp1047</i></p>
<dd>Encoding support for EBCDIC. On those platforms it is loaded automatically at start-up. Due to different character ranges used in <code>roff</code> it doesn&#8217;t work on architectures which are based on ASCII.</dl>
<p> Note that it can happen that some input encoding characters are not available for a particular output device. For example, saying </p>
<p> groff -Tlatin1 -mlatin9 &#8230; </p>
<p> fails if you use the Euro character in the input. Usually, this limitation is present only for devices which have a limited set of output glyphs (<code>-Tascii</code>, <code>-Tlatin1</code>); for other devices it is usually sufficient to install proper fonts which contain the necessary glyphs.</p>
<h3>Special Packages</h3>
<p>The macro packages in this section are not intended for stand-alone usage, but can be used to add special functionality to any other macro package or to plain groff.</p>
<dl>
<dt><i>62bit</i></p>
<dd>Provides macros for addition, multiplication, and division of 62-bit integers (allowing safe multiplication of 31-bit integers, for example).</p>
<dt><i>ec</i></p>
<dd>Switch to the EC and TC font families. To be used with <code><a href="/docs/linux/man/1-grodvi/">grodvi</a></code>(1) &#8211; this man page also gives more details of how to use it.</p>
<dt><i>hdtbl</i></p>
<dd>The Heidelberger table macros, contributed by Joachim Walsdorff, allow the generation of tables through a syntax similar to the HTML table model. Note that <i>hdtbl</i> is a macro package, not a preprocessor like <code><a href="/docs/linux/man/1-tbl/">tbl</a></code>(1). <i>hdtbl</i> works only with the <code>-Tps</code> and <code>-Tpdf</code> output devices. See <code><a href="/docs/linux/man/7-groff_hdtbl/">groff_hdtbl</a></code>(7)<code>.</code></p>
<dt><i>papersize</i></p>
<dd>This macro file is already loaded at start-up by <code>troff</code> so it isn&#8217;t necessary to call it explicitly. It provides an interface to set the paper size on the command line with the option -dpaper=,size. Possible values for <i>size</i> are the same as the predefined <code>papersize</code> values in the DESC file (only lowercase; see <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5) for more) except <code>a7</code>&#8211;<code>d7</code>. An appended <code>l</code> (ell) character denotes landscape orientation. Examples: <code>a4</code>, <code>c3l</code>, <code>letterl</code>.</p>
<dd>Most output drivers need additional command-line switches <code>-p</code> and <code>-l</code> to override the default paper length and orientation as set in the driver-specific DESC file. For example, use the following for PS output on A4 paper in landscape orientation:</p>
<dd><i>sh#</i> groff -Tps -dpaper=a4l -P-pa4 -P-l -ms foo.ms &gt; foo.ps</p>
<dt><i>pdfpic</i></p>
<dd>A single macro is provided in this file, <code>PSPIC</code>, to include a PDF graphic in a document, i.e., under the output device <code>-Tpdf</code>. For all other devices, <i>pspic</i> is used. So <i>pdfpic</i> is an extension of <i>pspic</i>. By that you can now even replace all <code>PSPIC</code> by <code>PDFPIC</code>, nothing gets lost by that. The options of <code>PDFPIC</code> are identical to the <code>PSDIF</code> options.</p>
<dt><i>pic</i></p>
<dd>This file provides proper definitions for the macros <code>PS</code> and <code>PE</code>, needed for the <code><a href="/docs/linux/man/1-pic/">pic</a></code>(1) preprocessor. They center each picture. Use it only if your macro package doesn&#8217;t provide proper definitions for those two macros (actually, most of them already do).</p>
<dt><i>pspic</i></p>
<dd>A single macro is provided in this file, <code>PSPIC</code>, to include a PostScript graphic in a document. The following output devices support inclusion of PS images: <code>-Tps</code>, <code>-Tdvi</code>, <code>-Thtml</code>, and <code>-Txhtml</code>; for all other devices the image is replaced with a hollow rectangle of the same size. This macro file is already loaded at start-up by <code>troff</code> so it isn&#8217;t necessary to call it explicitly.</p>
<dd>Syntax:</p>
<dl>
<dd>
<dl>
<dd><code>.PSPIC</code> [<code>-L</code>|<code>-R</code>|<code>-C</code>|<code>-I</code>&nbsp;<i>n</i>] <i>file</i> [<i>width</i> [,<i>height/</i>]]</dl>
</dl>
<dd><i>file</i> is the name of the PostScript file; <i>width</i> and <i>height</i> give the desired width and height of the image. If neither a <i>width</i> nor a <i>height</i> argument is specified, the image&#8217;s natural width (as given in the file&#8217;s bounding box) or the current line length is used as the width, whatever is smaller. The <i>width</i> and <i>height</i> arguments may have scaling indicators attached; the default scaling indicator is~<code>i</code>. This macro scales the graphic uniformly in the x and y~directions so that it is no more than <i>width</i> wide and <i>height</i> high. Option <code>-C</code> centers the graphic horizontally, which is the default. The <code>-L</code> and <code>-R</code> options cause the graphic to be left-aligned and right-aligned, respectively. The <code>-I</code> option causes the graphic to be indented by~<i>n</i> (default scaling indicator is~<code>m</code>).</p>
<dd>For use of <code>.PSPIC</code> within a diversion it is recommended to extend it with the following code, assuring that the diversion&#8217;s width completely covers the image&#8217;s width.</p>
<dl>
<dd>
<dl>
<dd>.am PSPIC .&nbsp;<wbr>&nbsp;vpt 0 \h'(\n[ps-offset]u + \n[ps-deswid]u)&#8217; .&nbsp;<wbr>&nbsp;sp -1 .&nbsp;<wbr>&nbsp;vpt 1 ..</dl>
</dl>
<dt><i>ptx</i></p>
<dd>A single macro is provided in this file, <code>xx</code>, for formatting permuted index entries as produced by the GNU <code><a href="/docs/linux/man/1-ptx/">ptx</a></code>(1) program. In case you need a different formatting, copy the macro into your document and adapt it to your needs.</p>
<dt><i>trace</i></p>
<dd>Use this for tracing macro calls. It is only useful for debugging. See <code><a href="/docs/linux/man/7-groff_trace/">groff_trace</a></code>(7)<code>.</code></p>
<dt><i>tty-char</i></p>
<dd>Overrides the definition of standard troff characters and some groff characters for TTY devices. The optical appearance is intentionally inferior compared to that of normal TTY formatting to allow processing with critical equipment.</p>
<dt><i>www</i></p>
<dd>Additions of elements known from the HTML format, as used in the internet (World Wide Web) pages; this includes URL links and mail addresses; see <code><a href="/docs/linux/man/7-groff_www/">groff_www</a></code>(7).</dl>
<h2>Naming</h2>
<p>Classical roff systems were designed before the conventions of the modern C <code><a href="/docs/linux/man/3-getopt/">getopt</a></code>(3) call evolved, and used a naming scheme for macro packages that looks odd to modern eyes. Macro packages were always included with the option <code>-m</code>; when this option was directly followed by its argument without an intervening space, this looked like a long option preceded by a single minus &#8212; a sensation in the computer stone age. To make this invocation form work, classical troff macro packages used names that started with the letter &#8216;m&#8217;, which was omitted in the naming of the macro file. </p>
<p> For example, the macro package for the man pages was called <i>man</i>, while its macro file <i>tmac.an</i>. So it could be activated by the argument <i>an</i> to option <code>-m</code>, or <code>-man</code> for short. </p>
<p> For similar reasons, macro packages that did not start with an &#8216;m&#8217; had a leading &#8216;m&#8217; added in the documentation and in speech; for example, the package corresponding to <i>tmac.doc</i> was called <i>mdoc</i> in the documentation, although a more suitable name would be <i>doc</i>. For, when omitting the space between the option and its argument, the command-line option for activating this package reads <code>-mdoc</code>. </p>
<p> To cope with all situations, actual versions of <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1) are smart about both naming schemes by providing two macro files for the inflicted macro packages; one with a leading &#8216;m&#8217; the other one without it. So in <i>groff</i>, the <i>man</i> macro package may be specified as one of the following four methods:</p>
<dl>
<dd><i>sh#</i> groff -m man <i>sh#</i> groff -man <i>sh#</i> groff -mman <i>sh#</i> groff -m an</dl>
<p> Recent packages that do not start with &#8216;m&#8217; do not use an additional &#8216;m&#8217; in the documentation. For example, the <i>www</i> macro package may be specified only as one of the two methods:</p>
<dl>
<dd><i>sh#</i> groff -m www <i>sh#</i> groff -mwww</dl>
<p> Obviously, variants like <i>-mmwww</i> would not make much sense. </p>
<p> A second strange feature of classical troff was to name macro files in the form <i>tmac.</i>name. In modern operating systems, the type of a file is specified as a postfix, the file name extension. Again, groff copes with this situation by searching both <i>anything</i><code>.tmac</code> and <code>tmac.</code><i>anything</i> if only <i>anything</i> is specified. </p>
<p> The easiest way to find out which macro packages are available on a system is to check the man~page <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), or the contents of the <i>tmac</i> directories. </p>
<p> In <i>groff</i>, most macro packages are described in~man pages called <code>groff_</code><a href="/docs/linux/man/7-name/">name</a>(7), with a leading &#8216;m&#8217; for the classical packages.</p>
<h2>Inclusion</h2>
<p>There are several ways to use a macro package in a document. The classical way is to specify the troff/groff option <code>-m</code> <i>name</i> at run-time; this makes the contents of the macro package <i>name</i> available. In groff, the file name<i>.tmac</i> is searched within the tmac path; if not found, <i>tmac.</i>name is searched for instead. </p>
<p> Alternatively, it is also possible to include a macro file by adding the request <code>.so</code> <i>filename</i> into the document; the argument must be the full file name of an existing file, possibly with the directory where it is kept. In groff, this was improved by the similar request <code>.mso</code> <i>package</i>, which added searching in the tmac path, just like option <code>-m</code> does. </p>
<p> Note that in order to resolve the <code>.so</code> and <code>.mso</code> requests, the roff preprocessor <code><a href="/docs/linux/man/1-soelim/">soelim</a></code>(1) must be called if the files to be included need preprocessing. This can be done either directly by a pipeline on the command line or by using the troff/groff option <code>-s</code>. <i>man</i> calls soelim automatically. </p>
<p> For example, suppose a macro file is stored as</p>
<dl>
<dd><i>/usr/:share/:groff/:1.22.4/:tmac/macros.tmac</i></dl>
<p> and is used in some document called <i>docu.roff</i>. </p>
<p> At run-time, the formatter call for this is</p>
<dl>
<dd><i>sh#</i> groff -m macros docu.roff</dl>
<p> To include the macro file directly in the document either</p>
<dl>
<dd>.mso macros.tmac</dl>
<p> is used or</p>
<dl>
<dd>.so /usr/:share/:groff/:1.22.4/:tmac/macros.tmac</dl>
<p> In both cases, the formatter should be called with option <code>-s</code> to invoke <code>soelim</code>.</p>
<dl>
<dd><i>sh#</i> groff -s docu.roff</dl>
<p> If you want to write your own groff macro file, call it whatever<i>.tmac</i> and put it in a directory in the tmac path; see section &#8220;Files&#8221; below. Then documents can include it with the <code>.mso</code> request or the option <code>-m</code>.</p>
<h2>Writing Macros</h2>
<p>A <code><a href="/docs/linux/man/7-roff/">roff</a></code>(7) document is a text file that is enriched by predefined formatting constructs, such as requests, escape sequences, strings, numeric registers, and macros from a macro package. These elements are described in <code><a href="/docs/linux/man/7-roff/">roff</a></code>(7). </p>
<p> To give a document a personal style, it is most useful to extend the existing elements by defining some macros for repeating tasks; the best place for this is near the beginning of the document or in a separate file. </p>
<p> Macros without arguments are just like strings. But the full power of macros reveals when arguments are passed with a macro call. Within the macro definition, the arguments are available as the escape sequences <code>\$1</code>, , <code>\$9</code>, <code>\$[</code><code>]</code>, <code>\$*</code>, and <code>\$@</code>, the name under which the macro was called is in <code>\$0</code>, and the number of arguments is in register <code>
[.$]</code>; see <code><a href="/docs/linux/man/7-groff/">groff</a></code>(7).</p>
<h3>Copy-in Mode</h3>
<p>The phase when groff reads a macro is called <i>copy-in mode</i> or <i>copy mode</i> in roff-talk. This is comparable to the C~preprocessing phase during the development of a program written in the C~language. </p>
<p> In this phase, groff interprets all backslashes; that means that all escape sequences in the macro body are interpreted and replaced by their value. For constant expressions, this is wanted, but strings and registers that might change between calls of the macro must be protected from being evaluated. This is most easily done by doubling the backslash that introduces the escape sequence. This doubling is most important for the positional parameters. For example, to print information on the arguments that were passed to the macro to the terminal, define a macro named &#8216;.print_args&#8217;, say.</p>
<dl>
<dd>.ds midpart was called with .de print_args .&nbsp;<wbr>&nbsp;tm&nbsp;[I]\$0[] &nbsp;\*[midpart]&nbsp;\n[.$]&nbsp;arguments: .&nbsp;<wbr>&nbsp;tm&nbsp;\$* ..</dl>
<p> When calling this macro by</p>
<dl>
<dd>.print_args arg1 arg2</dl>
<p> the following text is printed to the terminal:</p>
<dl>
<dd>print_args was called with the following 2 arguments: arg1 arg2</dl>
<p> Let&#8217;s analyze each backslash in the macro definition. As the positional parameters and the number of arguments change with each call of the macro their leading backslash must be doubled, which results in \<i>$*</i> and \<i>[.$]</i>. The same applies to the macro name because it could be called with an alias name, so \<i>$0</i>. </p>
<p> On the other hand, <i>midpart</i> is a constant string, it does not change, so no doubling for \<i>*[midpart]</i>. The \<i>f</i> escape sequences are predefined groff elements for setting the font within the text. Of course, this behavior does not change, so no doubling with \<i>f[I]</i> and \<i>f[]</i>.</p>
<h3>Draft Mode</h3>
<p>Writing groff macros is easy when the escaping mechanism is temporarily disabled. In groff, this is done by enclosing the macro definition(s) into a pair of <code>.eo</code> and <code>.ec</code> requests. Then the body in the macro definition is just like a normal part of the document &#8212; text enhanced by calls of requests, macros, strings, registers, etc. For example, the code above can be written in a simpler way by</p>
<dl>
<dd>.eo .ds midpart was called with .de print_args .&nbsp;<wbr>&nbsp;tm&nbsp;[I]\$0[] &nbsp;\*[midpart]&nbsp;
[.$]&nbsp;arguments: .&nbsp;<wbr>&nbsp;tm&nbsp;\$* .. .ec</dl>
<p> Unfortunately, draft mode cannot be used universally. Although it is good enough for defining normal macros, draft mode fails with advanced applications, such as indirectly defined strings, registers, etc. An optimal way is to define and test all macros in draft mode and then do the backslash doubling as a final step; do not forget to remove the <i>.eo</i> request.</p>
<h3>Tips for Macro Definitions</h3>
<dl>
<dt>&bull;</p>
<dd>Start every line with a dot, for example, by using the groff request <code>.nop</code> for text lines, or write your own macro that handles also text lines with a leading dot.</p>
<dl>
<dd>
<dl>
<dd>.de Text .&nbsp;<wbr>&nbsp;if (\n[.$] == 0)&nbsp;\ .&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return .&nbsp;<wbr>&nbsp;nop&nbsp;\)\$*\) ..</dl>
</dl>
<dt>&bull;</p>
<dd>Write a comment macro that works both for copy-in and draft mode; for as escaping is off in draft mode, trouble might occur when normal comments are used. For example, the following macro just ignores its arguments, so it acts like a comment line:</p>
<dl>
<dd>
<dl>
<dd>.de c .. .c This is like a comment line.</dl>
</dl>
<dt>&bull;</p>
<dd>In long macro definitions, make ample use of comment lines or almost-empty lines (this is, lines which have a leading dot and nothing else) for a better structuring.</p>
<dt>&bull;</p>
<dd>To increase readability, use groff&#8217;s indentation facility for requests and macro calls (arbitrary whitespace after the leading dot).</dl>
<h3>Diversions</h3>
<p>Diversions can be used to implement quite advanced programming constructs. They are comparable to pointers to large data structures in the C~programming language, but their usage is quite different. </p>
<p> In their simplest form, diversions are multi-line strings, but they get their power when diversions are used dynamically within macros. The (formatted) information stored in a diversion can be retrieved by calling the diversion just like a macro. </p>
<p> Most of the problems arising with diversions can be avoided if you remain aware of the fact that diversions always store complete lines. If diversions are used when the line buffer has not been flushed, strange results are produced; not knowing this, many people get desperate about diversions. To ensure that a diversion works, line breaks should be added at the right places. To be on the secure side, enclose everything that has to do with diversions into a pair of line breaks; for example, by explicitly using <code>.br</code> requests. This rule should be applied to diversion definition, both inside and outside, and to all calls of diversions. This is a bit of overkill, but it works nicely. </p>
<p> [If you really need diversions which should ignore the current partial line, use environments to save the current partial line and/:or use the <code>.box</code> request.] </p>
<p> The most powerful feature using diversions is to start a diversion within a macro definition and end it within another macro. Then everything between each call of this macro pair is stored within the diversion and can be manipulated from within the macros.</p>
<h2>Files</h2>
<p>All macro package files must be named name<i>.tmac</i> to fully use the tmac mechanism. <i>tmac.</i>name as with classical packages is possible as well, but deprecated. </p>
<p> The macro files are kept in the <i>tmac directories</i>; a colon separated list of these constitutes the <i>tmac path</i>. </p>
<p> The search sequence for macro files is (in that order):</p>
<dl>
<dt>&bull;</p>
<dd>the directories specified with troff/groff&#8217;s <code>-M</code> command-line option</p>
<dt>&bull;</p>
<dd>the directories given in the <i>GROFF_TMAC_PATH</i> environment variable</p>
<dt>&bull;</p>
<dd>the current directory (only if in unsafe mode, which is enabled by the <code>-U</code> command-line switch)</p>
<dt>&bull;</p>
<dd>the home directory</p>
<dt>&bull;</p>
<dd>a platform-specific directory, being</p>
<dl>
<dd>
<dl>
<dd><i>/usr/:lib/:groff/:site-tmac</i></dl>
</dl>
<dd>in this installation</p>
<dt>&bull;</p>
<dd>a site-specific (platform-independent) directory, being</p>
<dl>
<dd>
<dl>
<dd><i>/usr/:share/:groff/:site-tmac</i></dl>
</dl>
<dd>in this installation</p>
<dt>&bull;</p>
<dd>the main tmac directory, being</p>
<dl>
<dd>
<dl>
<dd><i>/usr/:share/:groff/:1.22.4/:tmac</i></dl>
</dl>
<dd>in this installation</dl>
<h2>Environment</h2>
<dl>
<dt><i>GROFF_TMAC_PATH</i></p>
<dd>A colon separated list of additional tmac directories in which to search for macro files. See the previous section for a detailed description.</dl>
<h2>Authors</h2>
<p>This document was written by Bernd Warken and Werner Lemberg</p>
<h2>See Also</h2>
<p><i>Groff: The GNU Implementation of troff</i>, by Trent A. Fisher and Werner Lemberg, is the primary <i>groff</i> manual. You can browse it interactively with &#8220;info groff&#8221;.</p>
<dl>
<dt><code><a href="/docs/linux/man/1-groff/">groff</a></code>(1)</p>
<dd>an overview of the groff system.</p>
<dt><code><a href="/docs/linux/man/7-groff_man/">groff_man</a></code>(7),</p>
<dd><code><a href="/docs/linux/man/7-groff_mdoc/">groff_mdoc</a></code>(7), <code><a href="/docs/linux/man/7-groff_me/">groff_me</a></code>(7), <code><a href="/docs/linux/man/7-groff_mm/">groff_mm</a></code>(7), <code><a href="/docs/linux/man/7-groff_mom/">groff_mom</a></code>(7), <code><a href="/docs/linux/man/7-groff_ms/">groff_ms</a></code>(7), <code><a href="/docs/linux/man/7-groff_trace/">groff_trace</a></code>(7), <code><a href="/docs/linux/man/7-groff_www/">groff_www</a></code>(7). the groff tmac macro packages.</p>
<dt><code><a href="/docs/linux/man/7-groff/">groff</a></code>(7)</p>
<dd>the groff language.</dl>
<p> The Filesystem Hierarchy Standard is available at the FHS web site </p>
