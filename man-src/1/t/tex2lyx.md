---
title: "tex2lyx(1)"
name: "tex2lyx"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tex2lyx/"
description: "tex2lyx – translate well-behaved LaTeX into LyX"
---

<h2>NAME</h2>
<p> tex2lyx &#8211; translate well-behaved LaTeX into LyX</p>
<h2>SYNOPSIS</h2>
<p> The simplest way to use <code>tex2lyx</code> is via the File-&gt;Import-&gt;LaTeX (plain) menu item in LyX. That runs <code>tex2lyx</code> on the given file and loads the resulting file into LyX. You should try that first, and call it from the command line only if you need to use more complicated options. </p>
<p> <code>tex2lyx</code> [ <code>-userdir</code> <i>userdir</i> ] [ <code>-systemdir</code> <i>systemdir</i> ] [ <code>-f</code> ] [ <code>-n</code> ] [ <code>-c</code> <i>textclass</i> ] [ <code>-e</code> <i>encoding</i> ] [ <code>-fixedenc</code> <i>encoding</i> ] [&nbsp;<wbr><code>-m</code> <i>module1</i>[,<i>module2</i>&#8230;]] [&nbsp;<wbr><code>-s</code>&nbsp;<wbr><i>sfile1</i>[,<i>sfile2</i>&#8230;]] [ <code>-skipchildren</code> ] [ <code>-roundtrip</code> ] [ <code>-copyfiles</code> ] <i>inputfile</i> [ <i>outputfile</i> ]</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> Class. By default, when <code>tex2lyx</code> sees a <tt>\documentclass{foo}</tt> command, it creates a file of textclass &#8220;foo&#8221; and reads the LyX layout file for that class (something like /usr/local/share/lyx/layouts/foo.layout <font SIZE="-1">OR</font> <font SIZE="-1"><code>HOME</code></font>/.lyx/layouts/foo.layout). Use <code>-c</code> to declare a different textclass (and read a different layout file).</p>
<dt>
<dd> This option is needed if the input file is a LaTeX fragment, with no preamble matter or <tt>egin{document}</tt> command. LyX files created by <code>tex2lyx</code> from partial files can be included in an existing LyX file using the &#8220;Include LyX File&#8221; command from LyX&#8217;s Insert menu.</p>
<dt><code>-m</code></p>
<dd> Module. Load the given modules. This is useful if <code>tex2lyx</code> does not automatically detect a given module, but you know the modules that provide some commands or environments that are used in the imported file. The modules are loaded in the given order. If a module <i>foo</i> depends on a module <i>bar</i>, <i>bar</i> must be given before <i>foo</i>.</p>
<dt><code>-f</code></p>
<dd> Force. <code>tex2lyx</code> will not run if the .lyx file it would generate already exists. Use the <code>-f</code> option (carefully) to clobber any existing files.</p>
<dt><code>-e</code></p>
<dd> Specify the default encoding using the LaTeX name as defined in the encodings file. <code>tex2lyx</code> will use this encoding, but switch if it finds any encoding changing commands in the input.</p>
<dt><code>-fixedenc</code></p>
<dd> Specify the encoding using the LaTeX name as defined in the encodings file. <code>tex2lyx</code> will ignore any encoding changing commands in the input.</p>
<dt><code>-n</code></p>
<dd> Noweb. Translate a noweb (aka literate programming) file. This should be (almost?) equivalent to running &#8220;noweb2lyx foo.tex foo.lyx&#8221;. This option requires the <code>-c</code> option.</p>
<dt><code>-skipchildren</code></p>
<dd> Do not translate child documents included via <tt>\include</tt> and <tt>\input</tt>. This option is useful if the child documents are generated files and/or contain many commands that <code>tex2lyx</code> does not understand yet.</p>
<dt><code>-s</code></p>
<dd> Syntax files. Input (one or more quoted, comma-separated) syntax files to read in addition to the default. (see the section on <i>Syntax Files</i> for details).</p>
<dt><code>-sysdir</code></p>
<dd> Specify a system directory. Normally, you shouldn&#8217;t need this. Your LyX system directory is chosen. Cf. the section <tt>FILES</tt> for details.</p>
<dt><code>-userdir</code></p>
<dd> Specify a user directory. Normally, you shouldn&#8217;t need this. Your LyX user directory is chosen. Cf. the section <tt>FILES</tt> for details.</p>
<dt><code>-roundtrip</code></p>
<dd> Call LyX to re-export the created output file to LaTeX. If the output file name is not given it is determined automatically to avoid over-writing the input file by accident: If the input file is named <i>foo.tex</i> the output file will be named <i>foo.lyx.lyx</i>, and the re-exported file will be named <i>foo.lyx.tex</i>.</p>
<dt><code>-copyfiles</code></p>
<dd> Copy all included files <code>tex2lyx</code> is aware of to the output directory if the output file is located in a different directory than the input file. This is useful if you want to ensure that no included file is overwritten (either in roundtrip mode or by a later export from LyX). Please note that the resulting document may be uncompilable. This happens if it needs files that <code>tex2lyx</code> does not know about and therefore does not copy to the output directory.</p>
<dt><code>-help</code></p>
<dd> Help. Print out usage information and quit.</p>
<dt><code>-version</code></p>
<dd> Print out the version number and build information and quit.</dl>
<h2>DESCRIPTION</h2>
<h3>Introduction</h3>
<p> <code>tex2lyx</code> will create a LyX file with the specified name (or <i>dir/foo.lyx</i> if no name was given) from the LaTeX file <i>dir/foo.tex</i>. </p>
<p> Suffixes .tex, .ltx and .latex are supported. If <i>inputfile</i> does not exist and does not have one of these suffixes, <code>tex2lyx</code> will try to translate <i>inputfile.tex</i>. (This is similar to the behavior of LaTeX.) </p>
<p> The purpose of <code>tex2lyx</code> is to translate <i>well-behaved</i> LaTeX2e into LyX. If your LaTeX file doesn&#8217;t compile&#8212;or if you do weird things, like redefining standard LaTeX commands&#8212;it may choke. LaTeX209 will often be translated correctly, but it&#8217;s not guaranteed. </p>
<p> <code>tex2lyx</code> lacks a few features. However, its main goals are:</p>
<dl>
<dt>&bull;</p>
<dd> Get through a well-behaved LaTeX2e file without crashing</p>
<dt>&bull;</p>
<dd> Translate a lot of that file.</p>
<dt>&bull;</p>
<dd> Localize the parts that can&#8217;t be translated and copy them in TeX mode</dl>
<p> It achieves these main goals pretty well on most files.</p>
<h3>Usage</h3>
<p> Here&#8217;s a more lengthy description of what you should do to translate a LaTeX document into LyX.</p>
<dl>
<dt>&bull;</p>
<dd> Run <code>tex2lyx</code>.</p>
<dt>
<dd> <code>tex2lyx</code> will inform you of its progress and give any warnings to stderr, so if you don&#8217;t want any output at all, try (in csh) `tex2lyx foo.tex &gt;&amp; /dev/null&#8217;. You should <font SIZE="-1">NOT</font> redirect standard output to <i>foo.lyx</i>.</p>
<dt>&bull;</p>
<dd> Run LyX (version 2.1 or later) on the resulting .lyx file.</p>
<dt>
<dd> In theory, most of the file will have been translated, and anything that&#8217;s untranslatable will be transferred to TeX code (ERT in LyX-speak). In theory, LyX will be able to read in the file, and to create printed documents from it, because all that untranslated ERT stuff will be passed directly back to LaTeX, which LyX uses as a backend. Unfortunately, reality doesn&#8217;t always reflect theory. If <code>tex2lyx</code> crashes, or LyX cannot read the generated LyX file, see the <tt>BUGS</tt> section below.</p>
<dt>&bull;</p>
<dd> Transform things have been inserted as TeX code manually to LyX features, if possible.</p>
<dt>
<dd> As mentioned above, you should be able to print out the LyX file even without doing this. However, changing a command in TeX code to the corresponding LyX object will allow you to take advantage of LyX&#8217;s <font SIZE="-1">WYSIWYM</font> editing.</p>
<dt>
<dd> <code>tex2lyx</code> is not guaranteed to create a LyX file which generates exactly the same output as the LaTeX file, although its goal is to achieve this. <code>tex2lyx</code> will generally err on the side of translating less to ensure that the resulting output files are accurate, even though this leads to more TeX code and less <font SIZE="-1">WYSIWYM</font>.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">PROOFREAD</font> <font SIZE="-1">THE</font> <font SIZE="-1">DOCUMENT</font>!!</p>
<dt>
<dd> I&#8217;m sure you were planning on doing this anyway, but it&#8217;s particularly important after translating a LaTeX document. <code>tex2lyx</code> is better at &#8220;macro-translating&#8221; (translating the whole document) than &#8220;micro-translating&#8221; (translating every little detail). For example, you may see extra spaces or deleted spaces. Space handling has improved, but it&#8217;s not perfect.</dl>
<h3>What tex2lyx Can Handle</h3>
<p> <code>tex2lyx</code> understands many LaTeX commands. It will translate:</p>
<dl>
<dt>&bull;</p>
<dd> regular text, including mini-commands like ~, `&#8217;, <tt>\@</tt>, <tt>\TeX</tt>, as well as accented characters like <tt>\'{a}</tt>, and the special cases ?` and !`</p>
<dt>&bull;</p>
<dd> title commands like <tt>uthor</tt>, <tt>\date</tt>, <tt>	itle</tt>, <tt>	hanks</tt> and the abstract environment</p>
<dt>&bull;</p>
<dd> heading commands like <tt>\section</tt> including starred commands (<tt>\section*</tt>)</p>
<dt>&bull;</p>
<dd> Environments: quote, quotation, and verse; center, flushright, and flushleft</p>
<dt>&bull;</p>
<dd> itemize, enumerate, and description environments, and their <tt>\item</tt> commands. Also, well-behaved nested lists</p>
<dt>&bull;</p>
<dd> cross-referencing commands: <tt>ef</tt>, <tt>\pageref</tt>, <tt>\label</tt>, and <tt>
