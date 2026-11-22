---

title: "tex2lyx(1)"
name: "tex2lyx"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tex2lyx/"
description: "tex2lyx – translate well-behaved LaTeX into LyX"
---

<p> tex2lyx - translate well-behaved LaTeX into LyX  </p>
<h2>SYNOPSIS</h2>
<p> The simplest way to use <code>tex2lyx</code> is via the File-&gt;Import-&gt;LaTeX (plain) menu item in LyX. That runs <code>tex2lyx</code> on the given file and loads the resulting file into LyX. You should try that first, and call it from the command line only if you need to use more complicated options. </p>
<p> <code>tex2lyx</code> [ <code>-userdir</code> <i>userdir</i> ] [ <code>-systemdir</code> <i>systemdir</i> ] [ <code>-f</code> ] [ <code>-n</code> ] [ <code>-c</code> <i>textclass</i> ] [ <code>-e</code> <i>encoding</i> ] [ <code>-fixedenc</code> <i>encoding</i> ] [&nbsp;<wbr><code>-m</code> <i>module1</i>[,<i>module2</i>...]] [&nbsp;<wbr><code>-s</code>&nbsp;<wbr><i>sfile1</i>[,<i>sfile2</i>...]] [ <code>-skipchildren</code> ] [ <code>-roundtrip</code> ] [ <code>-copyfiles</code> ] <i>inputfile</i> [ <i>outputfile</i> ]  </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></dt>
<dd> <p> Class. By default, when <code>tex2lyx</code> sees a <code>\documentclass{foo}</code> command, it creates a file of textclass ``foo&#8217;&#8216; and reads the LyX layout file for that class (something like /usr/local/share/lyx/layouts/foo.layout OR <code>HOME</code>/.lyx/layouts/foo.layout). Use <code>-c</code> to declare a different textclass (and read a different layout file). </p>
 </dd>
<dd> <p> This option is needed if the input file is a LaTeX fragment, with no preamble matter or <code>\begin{document}</code> command. LyX files created by <code>tex2lyx</code> from partial files can be included in an existing LyX file using the ``Include LyX File&#8217;&#8216; command from LyX&#8217;s Insert menu. </p>
 </dd>
<dt><code>-m</code></dt>
<dd> <p> Module. Load the given modules. This is useful if <code>tex2lyx</code> does not automatically detect a given module, but you know the modules that provide some commands or environments that are used in the imported file. The modules are loaded in the given order. If a module <i>foo</i> depends on a module <i>bar</i>, <i>bar</i> must be given before <i>foo</i>. </p>
 </dd>
<dt><code>-f</code></dt>
<dd> <p> Force. <code>tex2lyx</code> will not run if the .lyx file it would generate already exists. Use the <code>-f</code> option (carefully) to clobber any existing files. </p>
 </dd>
<dt><code>-e</code></dt>
<dd> <p> Specify the default encoding using the LaTeX name as defined in the encodings file. <code>tex2lyx</code> will use this encoding, but switch if it finds any encoding changing commands in the input. </p>
 </dd>
<dt><code>-fixedenc</code></dt>
<dd> <p> Specify the encoding using the LaTeX name as defined in the encodings file. <code>tex2lyx</code> will ignore any encoding changing commands in the input. </p>
 </dd>
<dt><code>-n</code></dt>
<dd> <p> Noweb. Translate a noweb (aka literate programming) file. This should be (almost?) equivalent to running ``noweb2lyx foo.tex foo.lyx&#8217;&#8216;. This option requires the <code>-c</code> option. </p>
 </dd>
<dt><code>-skipchildren</code></dt>
<dd> <p> Do not translate child documents included via <code>\include</code> and <code>\input</code>. This option is useful if the child documents are generated files and/or contain many commands that <code>tex2lyx</code> does not understand yet. </p>
 </dd>
<dt><code>-s</code></dt>
<dd> <p> Syntax files. Input (one or more quoted, comma-separated) syntax files to read in addition to the default. (see the section on <i>Syntax Files</i> for details). </p>
 </dd>
<dt><code>-sysdir</code></dt>
<dd> <p> Specify a system directory. Normally, you shouldn&#8217;t need this. Your LyX system directory is chosen. Cf. the section <code>FILES</code> for details. </p>
 </dd>
<dt><code>-userdir</code></dt>
<dd> <p> Specify a user directory. Normally, you shouldn&#8217;t need this. Your LyX user directory is chosen. Cf. the section <code>FILES</code> for details. </p>
 </dd>
<dt><code>-roundtrip</code></dt>
<dd> <p> Call LyX to re-export the created output file to LaTeX. If the output file name is not given it is determined automatically to avoid over-writing the input file by accident: If the input file is named <i>foo.tex</i> the output file will be named <i>foo.lyx.lyx</i>, and the re-exported file will be named <i>foo.lyx.tex</i>. </p>
 </dd>
<dt><code>-copyfiles</code></dt>
<dd> <p> Copy all included files <code>tex2lyx</code> is aware of to the output directory if the output file is located in a different directory than the input file. This is useful if you want to ensure that no included file is overwritten (either in roundtrip mode or by a later export from LyX). Please note that the resulting document may be uncompilable. This happens if it needs files that <code>tex2lyx</code> does not know about and therefore does not copy to the output directory. </p>
 </dd>
<dt><code>-help</code></dt>
<dd> <p> Help. Print out usage information and quit. </p>
 </dd>
<dt><code>-version</code></dt>
<dd> <p> Print out the version number and build information and quit. </p>
 </dd></dl>
<h2>DESCRIPTION</h2>
<h3>Introduction</h3>
<p> <code>tex2lyx</code> will create a LyX file with the specified name (or <i>dir/foo.lyx</i> if no name was given) from the LaTeX file <i>dir/foo.tex</i>. </p>
<p> Suffixes .tex, .ltx and .latex are supported. If <i>inputfile</i> does not exist and does not have one of these suffixes, <code>tex2lyx</code> will try to translate <i>inputfile.tex</i>. (This is similar to the behavior of LaTeX.) </p>
<p> The purpose of <code>tex2lyx</code> is to translate <i>well-behaved</i> LaTeX2e into LyX. If your LaTeX file doesn&#8217;t compile---or if you do weird things, like redefining standard LaTeX commands---it may choke. LaTeX209 will often be translated correctly, but it&#8217;s not guaranteed. </p>
<p> <code>tex2lyx</code> lacks a few features. However, its main goals are: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Get through a well-behaved LaTeX2e file without crashing </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Translate a lot of that file. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Localize the parts that can&#8217;t be translated and copy them in TeX mode </p>
 </dd></dl>
<p> It achieves these main goals pretty well on most files.  </p>
<h3>Usage</h3>
<p> Here&#8217;s a more lengthy description of what you should do to translate a LaTeX document into LyX. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Run <code>tex2lyx</code>. </p>
 </dd>
<dd> <p> <code>tex2lyx</code> will inform you of its progress and give any warnings to stderr, so if you don&#8217;t want any output at all, try (in csh) `tex2lyx foo.tex &gt;&amp; /dev/null&#8217;. You should NOT redirect standard output to <i>foo.lyx</i>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Run LyX (version 2.1 or later) on the resulting .lyx file. </p>
 </dd>
<dd> <p> In theory, most of the file will have been translated, and anything that&#8217;s untranslatable will be transferred to TeX code (ERT in LyX-speak). In theory, LyX will be able to read in the file, and to create printed documents from it, because all that untranslated ERT stuff will be passed directly back to LaTeX, which LyX uses as a backend. Unfortunately, reality doesn&#8217;t always reflect theory. If <code>tex2lyx</code> crashes, or LyX cannot read the generated LyX file, see the <code>BUGS</code> section below. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Transform things have been inserted as TeX code manually to LyX features, if possible. </p>
 </dd>
<dd> <p> As mentioned above, you should be able to print out the LyX file even without doing this. However, changing a command in TeX code to the corresponding LyX object will allow you to take advantage of LyX&#8217;s WYSIWYM editing. </p>
 </dd>
<dd> <p> <code>tex2lyx</code> is not guaranteed to create a LyX file which generates exactly the same output as the LaTeX file, although its goal is to achieve this. <code>tex2lyx</code> will generally err on the side of translating less to ensure that the resulting output files are accurate, even though this leads to more TeX code and less WYSIWYM. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PROOFREAD THE DOCUMENT!! </p>
 </dd>
<dd> <p> I&#8217;m sure you were planning on doing this anyway, but it&#8217;s particularly important after translating a LaTeX document. <code>tex2lyx</code> is better at ``macro-translating&#8217;&#8216; (translating the whole document) than ``micro-translating&#8217;&#8216; (translating every little detail). For example, you may see extra spaces or deleted spaces. Space handling has improved, but it&#8217;s not perfect. </p>
 </dd></dl>
<h3>What tex2lyx Can Handle</h3>
<p> <code>tex2lyx</code> understands many LaTeX commands. It will translate: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> regular text, including mini-commands like ~, `&#8216;, <code>\@</code>, <code>\TeX</code>, as well as accented characters like <code>\&#8216;{a}</code>, and the special cases ?` and !` </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> title commands like <code>\author</code>, <code>\date</code>, <code>\title</code>, <code>\thanks</code> and the abstract environment </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> heading commands like <code>\section</code> including starred commands (<code>\section*</code>) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Environments: quote, quotation, and verse; center, flushright, and flushleft </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> itemize, enumerate, and description environments, and their <code>\item</code> commands. Also, well-behaved nested lists </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> cross-referencing commands: <code>\ref</code>, <code>\pageref</code>, <code>\label</code>, and <code>\cite</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>\footnote</code> and <code>\margin</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> font-changing commands including <code>\em</code>, <code>\emph</code>, <code>\textit</code>, and corresponding commands to change family, size, series, and shape </p>
 </dd>
<dt>&bull; </dt>
<dd> <p> <code>\input{foo}</code> (or <code>\input{foo.blah}</code>) and <code>\include{foo}</code>. Plain TeX <code>\input</code> command ``<code>\input foo.tex</code>&#8216;&#8216; is also supported. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> tabular environment, and commands that go inside it like <code>\hline</code>, <code>\cline</code>, and <code>\multicolumn</code> (but see below) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> float environments table and table*, as well as <code>\caption</code> commands within them </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> float environments figure and figure*, as well as graphics inclusion commands \epsf, \epsffile, \epsfbox, \epsfxsize, \epsfig, \psfig, and \includegraphics. Both the graphics and graphicx forms of \includegraphics are supported. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> thebibliography environment and <code>\bibitem</code> command, as well as BibTeX&#8217;s <code>\bibliography</code> and <code>\bibliographystyle</code> commands </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> miscellaneous commands: <code>\hfill</code>, <code>\</code><code>\</code>, <code>\noindent</code>, <code>\ldots</code>... </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> documentclass-specific environments (and some commands) which can be translated to LyX layouts </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> arguments to certain untranslatable commands (e.g. <code>\mbox</code>) </p>
 </dd></dl>
<p> Some of this support may not be 100% yet. See below for details </p>
<p> <code>tex2lyx</code> copies math (almost) verbatim from your LaTeX file. Luckily, LyX reads in LaTeX math, so (almost) any math which is supported by LyX should work just fine. </p>
<p> <code>tex2lyx</code> will copy any preamble commands (i.e., anything before <code>\begin{document}</code>) verbatim. Fancy stuff you&#8217;ve got in your preamble should thus be conserved in printed documents, although it will not of course show up in the LyX window. Check Document-&gt;Settings-&gt;LaTeX Preamble to see the result.  </p>
<h3>What tex2lyx Can't Handle --- But it's OK</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> some spacing commands (<code>\hspace</code>, <code>\pagebreak</code> and <code>\linebreak</code>) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>\centering</code>, <code>\raggedleft</code>, <code>\raggedright</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>\verb</code> and verbatim environment. <code>tex2lyx</code> is careful to copy <i>exactly</i> in this case, including comments and whitespace. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> unknown (e.g., user-defined) environments and commands </p>
 </dd></dl>
<p> <code>tex2lyx</code> copies unknown commands, along with their arguments, verbatim into the LyX file. Also, if it sees a <code>\begin{foo}</code> where it doesn&#8217;t recognize the ``foo&#8217;&#8216; environment, it will copy verbatim until it sees <code>\end{foo}</code> (unless you use the <code>-r</code> option). Most of these unknown commands won&#8217;t cause <code>tex2lyx</code> to break; they&#8217;ll merely require you to do some editing once you&#8217;ve loaded the file up in LyX. That should be less painful than editing either the .tex or the .lyx file using a text editor.  </p>
<h3>What tex2lyx Handles Badly --- aka BUGS</h3>
<p> Since <code>tex2lyx</code> is relatively new, it&#8217;s got a number of problems. As it matures, these bugs will be squished. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> ``Exact&#8217;&#8216; copying of unknown environments and commands isn&#8217;t quite exact. This will yield ugly LyX, but in almost all cases the output will be the same. However, most parts of the file will be copied perfectly, including whitespace and comments. This includes: the LaTeX preamble, verbatim environments as well as <code>\verb</code> commands, and skip blocks. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>tex2lyx</code> translates only a subset of the document class options to native features. Other options are placed in the ``options&#8217;&#8216; field in the Document-&gt;Settings popup. </p>
 </dd>
<dd> <p> More importantly, <code>tex2lyx</code> doesn&#8217;t translate <code>\newcommands</code>, unknown <code>\usepackage</code> commands and other unknown code in the preamble. It simply copies that into the LaTeX preamble. If you use special commands, e.g. to specify the text layout in a way that that is not understood by LyX, tex2lyx won&#8217;t recognize it. Note that these settings will be overwritten if you modify the text layout in LyX&#8217;s document settings. Better remove these special options from the LaTeX preamble (Document-&gt;Settings-&gt;LaTeX Preamble) and use the corresponding LyX document settings, if possible. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The foil document class has a couple of bugs. <code>tex2lyx</code> may do weird things with optional arguments to <code>\foilhead</code> commands. Also, it may handle <code>\begin{dinglist}</code> incorrectly (although the stuff in the environment should translate normally). </p>
 </dd></dl>
<p> All known bugs of <code>tex2lyx</code> can be found on <i></i><i><a rel="nofollow" href="http://www.lyx.org/trac/wiki/BugTrackerHome">http://www.lyx.org/trac/wiki/BugTrackerHome</a></i><i></i>. </p>
<p> <code>tex2lyx</code> is rather robust. As mentioned above, it may not translate your file perfectly, but the result should be usable and it shouldn&#8217;t crash. If you encounter problems---and the problem is not one of those mentioned above or on <i></i><i><a rel="nofollow" href="http://www.lyx.org/trac/wiki/BugTrackerHome">http://www.lyx.org/trac/wiki/BugTrackerHome</a></i><i></i>---please report the issue as described in the section on <i>Bug Reports</i>.  </p>
<h3>What LyX Can't Handle</h3>
<p> LyX itself is missing a couple of features, such that even if <code>tex2lyx</code> translates things perfectly, LyX may still have trouble reading it. If you really need these features, you can export your final document as LaTeX, and put them back in. See <i></i><i>BUGS</i><i></i> for more details on these bugs. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> For a number of commands (such as <code>\\</code>), LyX does not support the optional argument. <code>tex2lyx</code> will automatically discard the optional arguments with a warning to stdout. LyX also ignores the width argument for the thebibliography environment. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> LyX support for tables isn&#8217;t perfect. For complicated tables, use a ``skip&#8217;&#8216; block, so that they will be copied in TeX mode. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> LyX allows figures to have sizes in the units known to TeX, such as in, cm, etc. It also translates percentages of \textwidth, \textheight, \columnwidth, but no other lengths (e.g. if you wanted to scale a figure to size \topmargin for some reason). <code>tex2lyx</code> will copy figures with untranslatable sizes in TeX mode. Again, you might be able to fix that within LyX. </p>
 </dd></dl>
<h2>EXAMPLES</h2>
<p> tex2lyx <code>-f</code> <code>-r</code> ``myenv&#8217;&#8216; foo.tex </p>
<p> The above will create a file foo.lyx from foo.tex, overwriting if necessary. When it finds a <code>\begin{myenv} ... \end{myenv}</code> block, it will translate the stuff within the block, but copy the <code>\begin</code> and <code>\end</code> commands in TeX mode. </p>
<p> tex2lyx <code>-n</code> <code>-c</code> ``literate-article&#8217;&#8216; foo.tex </p>
<p> The above will change a noweb document into a LyX literate-article document. A user would do this if the noweb document had documentclass article.  </p>
<h2>NOTES</h2>
<h3>Bug Reports</h3>
<p> Bugs should be reported to the LyX bug tracker at <a rel="nofollow" href="http://www.lyx.org/trac/wiki/BugTrackerHome.">http://www.lyx.org/trac/wiki/BugTrackerHome.</a> Additionally, you can post a message to the LyX developers&#8217; mailing list. Its address is currently lyx-devel [at] lists.lyx.org. If your message bounces, you can check the LyX home page, <a rel="nofollow" href="http://www.lyx.org/.">http://www.lyx.org/.</a> If you are running <code>tex2lyx</code> on a huge file, please do not send all of the output in your bug report. Just include the last ten or twenty lines of output, along with the piece of the LaTeX file it crashed on. Or, even better, attach a small but complete file which causes the same problem as your original file.  </p>
<h3>Layout Files</h3>
<p> <code>tex2lyx</code> reads a LyX layout file to know how to handle LaTeX environments and commands which get translated to LyX layouts. This file will include all ``normal&#8217;&#8216; non-math environments (i.e., including quote and itemize, but not tabular, minipage, and some other fancy environments), and commands like <code>\section</code> and <code>\title</code>. If you want to tex2lyx a class that doesn&#8217;t have an existing layout file, then you&#8217;ll have to create a layout file. But you have to do this anyway, in order to LyX the file, since LyX depends on layout files to know how to display and process its files. Check the LyX documentation for help with this task (which can be hard or easy, depending on the class you want to create a layout file for.) If your class is quite similar to a class that has a layout file, then consider using the <code>-c</code> option.  </p>
<h3>Syntax Files</h3>
<p> <code>tex2lyx</code> always reads at least one syntax file, called the default syntax file. <code>tex2lyx</code> will read your personal syntax file if it exists; otherwise it will read the system-wide file. <code>tex2lyx</code> will read additional syntax files if you specify them with the <code>-s</code> option. (These extra files should have the same format as the default file, but will tend to be shorter, since they only have to specify extra commands not found in the default file.) A syntax file tells <code>tex2lyx</code> a few things. </p>
<p> First, it describes the syntax of each command, that is, how many required arguments and how many optional arguments the command takes. Knowing this makes it easier for <code>tex2lyx</code> to copy (in TeX mode) commands that it doesn&#8217;t know how to translate. The syntax file simply has a command, followed by braces or brackets describing its arguments in the correct order. For example, a syntax file entry <code>\bibitem[]{}</code> means that the <code>\bibitem</code> command takes an optional argument followed by a required one, while the entry <code>\bf</code> means that the <code>\bf</code> command takes no arguments at all. When <code>tex2lyx</code> encounters a token that it doesn&#8217;t know how to translate into LyX, it will copy the token---along with the correct number of arguments---exactly. If the token is not in the syntax file, then <code>tex2lyx</code> just copies as many arguments as it finds. This means that it may copy too much. But since the user can specify additional syntax files, that shouldn&#8217;t happen often. </p>
<p> Some commands that cannot be translated to LyX, like <code>\mbox</code>, have as one of their arguments regular LaTeX text. If the string ``translate&#8217;&#8216; is put into an argument of an (untranslatable) command in the syntax file, then <code>tex2lyx</code> will translate that argument instead of copying it verbatim. So, for example, the default syntax file has <code>\raisebox{}[][]{translate}</code>. This means that the <code>\raisebox</code> command and the first argument (and optional arguments if they exist) are copied in TeX mode, but the last argument (which may contain math, complicated LaTeX, other untranslatable commands, etc.) will be translated into LyX. You can&#8217;t use ``translate&#8217;&#8216; on optional arguments. </p>
<p> User-defined syntax files are allowed to define new commands and their syntax, or override the number of arguments for a command given in the default syntax file. (E.g., if you&#8217;re using a style that gives an extra argument to some command...) However, this will only be useful for commands copied in TeX mode. Commands which are actually translated by <code>tex2lyx</code> (like <code>\item</code>) have their argument syntax hard-coded. The hard-coded commands are identified in the default syntax file. </p>
<p> Second, the syntax file describes any ``regular environments&#8217;&#8216;. Usually, an entire unknown environment will be copied in TeX mode. If you define a regular environment ``foo&#8217;&#8216;, though, then only the <code>\begin{foo}</code> and <code>\end{foo}</code> commands will be copied in TeX mode; the text within the environment will be treated (i.e., translated) by <code>tex2lyx</code> as regular LaTeX, rather than being copied into TeX mode. Don&#8217;t try to declare ``tabbing&#8217;&#8216; and ``picture&#8217;&#8216; as regular environments, as the text within those environments will confuse <code>tex2lyx</code>; use this capability for new environments you create that have plain text or math or simple commands in them. You also can&#8217;t declare unknown math environments (like equation*) as regular environments, either, since the LyX math editor won&#8217;t understand them. The names of regular environments appear, whitespace-separated, between <code>\begin{tex2lyxre}</code> and <code>\end{tex2lyxre}</code> statements in the syntax file. (If you have a regular environment which you won&#8217;t use very often, you can use the <code>-r</code> option rather than writing a syntax file.)  </p>
<h2>WARNINGS</h2>
<p> Always keep a copy of your original LaTeX files either under a different name or in a different directory. There are a couple ways in which using LyX could lead to overwriting the original LaTeX file. </p>
<p> If you import foo.tex to create foo.lyx, then edit foo.lyx and want to re-export it, note that it will overwrite the original foo.tex. (LyX will ask you if you want to overwrite it.)  </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>LYX_DIR_21x</code></dt>
<dd> <p> can be used to specify which system directory to use. </p>
 </dd></dl>
<p> The system directory is determined by searching for the file &quot;chkconfig.ltx&quot;. Directories are searched in this order: <br/>
 1) -sysdir command line parameter <br/>
 2) LYX_DIR_21x environment variable <br/>
 3) Maybe &lt;path of binary&gt;/TOP_SRCDIR/lib <br/>
 4) &lt;path of binary&gt;/../share/&lt;name of binary&gt;/ <br/>
 5) hardcoded lyx_dir (at build time: /usr/share/lyx) </p>
<dl>
<dt><code>LYX_USERDIR_21x</code></dt>
<dd> <p> can be used to specify which user directory to use. </p>
 </dd></dl>
<p> The user directory is, in order of precedence: <br/>
 1) -userdir command line parameter <br/>
 2) LYX_USERDIR_21x environment variable <br/>
 3) $HOME/.&lt;name of binary&gt; if no explicit setting is made  </p>
<h2>FILES</h2>
<p> If <i></i><i>LIBDIR</i><i></i> is the system-wide LyX directory and <i></i><i>MY_LYXDIR</i><i></i> is your personal LyX directory, then the following files are read by tex2lyx: </p>
<dl>
<dt><i></i><i>MY_LYXDIR</i><i></i>/layouts/*.layout</dt>
<dd> <p> User&#8217;s personal layout files for document classes </p>
 </dd>
<dt><i></i><i>MY_LYXDIR</i><i></i>/syntax.default</dt>
<dd> <p> User&#8217;s personal syntax file </p>
 </dd>
<dt><i></i><i>MY_LYXDIR</i><i></i>/encodings</dt>
<dd> <p> User&#8217;s personal encoding definition file </p>
 </dd>
<dt><i></i><i>LIBDIR</i><i></i>/layouts/*.layout</dt>
<dd> <p> System-wide layout files for document classes </p>
 </dd>
<dt><i></i><i>LIBDIR</i><i></i>/lib/syntax.default</dt>
<dd> <p> System-wide LaTeX syntax file </p>
 </dd>
<dt><i></i><i>LIBDIR</i><i></i>/lib/encodings</dt>
<dd> <p> System-wide encoding definition file </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-lyx/">lyx</a></i>(1), <i><a href="/docs/linux/man/1-latex/">latex</a></i>(1)  </p>
<h2>AUTHORS</h2>
<p> tex2lyx is Copyright (c) 2003ff. by the LyX Team (lyx-devel [at] lists.lyx.org) </p>
