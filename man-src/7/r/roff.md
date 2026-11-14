---
title: "roff(7)"
name: "roff"
section: "7"
letter: "r"
url: "/docs/linux/man/7-roff/"
description: "roff – concepts and history of roff typesetting"
---

<p>roff &#8211; concepts and history of roff typesetting</p>
<h2>Description</h2>
<p><i>roff</i> is the general name for a set of text formatting programs, known under names like <code>troff</code>, <code>nroff</code>, <code>ditroff</code>, <code>groff</code>, etc. A <i>roff</i> system consists of an extensible text formatting language and a set of programs for printing and converting to other text formats. Unix-like operating systems distribute a <i>roff</i> system as a core package. </p>
<p> The most common <i>roff</i> system today is the free software implementation GNU <i>roff</i>, <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1). <i>groff</i> implements the look-and-feel and functionality of its ancestors, with many extensions. </p>
<p> The ancestry of <i>roff</i> is described in section &#8220;History&#8221; below. In this document, the term <i>roff</i> always refers to the general class of roff programs, not to the <code>roff</code> command provided in early Unix systems. </p>
<p> In spite of its age, <i>roff</i> is in wide use today, for example, the manual pages on Unix systems (<i>man~pages</i>), many software books, system documentation, standards, and corporate documents are written in roff. The <i>roff</i> output for text devices is still unmatched, and its graphical output has the same quality as other free type-setting programs and is better than some of the commercial systems. </p>
<p> <i>roff</i> is used to format Unix <i>manual pages</i>, (or <i>man pages</i>), the standard documentation system on many Unix-derived operating systems. </p>
<p> This document describes the history of the development of the <i>roff system</i>; some usage aspects common to all <i>roff</i> versions, details on the <i>roff</i> pipeline, which is usually hidden behind front-ends like <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1); a general overview of the formatting language; some tips for editing <i>roff</i> files; and many pointers to further readings.</p>
<h2>History</h2>
<p>Document formatting by computer dates back to the 1960s. The <i>roff</i> system itself is intimately connected to the Unix operating system, but its roots go back to the earlier operating systems CTSS and Multics.</p>
<h3>The Predecessor RUNOFF</h3>
<p><code>roff</code>&#8216;s ancestor <code>RUNOFF</code> was written in the MAD language by <i>Jerry Saltzer</i> for the <i>Compatible Time Sharing System (CTSS)</i>, a project of the Massachusetts Institute of Technology (MIT), in 1963 and 1964&#8212;note that CTSS commands were all uppercase. </p>
<p> In 1965, MIT&#8217;s Project MAC teamed with Bell Telephone Laboratories (BTL) and General Electric to begin the <i>Multics</i> system A command called <code>runoff</code> was written for Multics in the late 60s in the BCPL language, by <i>Bob Morris</i>, <i>Doug McIlroy</i>, and other members of the Multics team. </p>
<p> Like its CTSS ancestor, Multics <code>runoff</code> formatted an input file consisting of text and command lines; commands began with a period and were two letters. Output from these commands was to terminal devices such as IBM Selectric terminals. Multics <code>runoff</code> had additional features added, such as the ability to do two-pass formatting; it became the main format for Multics documentation and text processing. </p>
<p> BCPL and <code>runoff</code> were ported to the GCOS system at Bell Labs when BTL left the development of Multics. </p>
<p> There is a free archive about <i>historical RUNOFF</i> documents. You can get it anonymously by the shell command</p>
<dl>
<dd>$git clone <a rel="nofollow" href="https://github.com/bwarken/RUNOFF_historical.git">https://github.com/bwarken/RUNOFF_historical.git</a></dl>
<p> As well, there is a new project for writing a program that can read <i>RUNOFF files ,</i> but it does not yet work so far. You can get an early version anonymously by the shell command</p>
<dl>
<dd>$git clone <a rel="nofollow" href="https://github.com/bwarken/runoff.git">https://github.com/bwarken/runoff.git</a></dl>
<h3>The Classical nroff/troff System</h3>
<p>At BTL, there was a need to drive the <i>Graphic Systems CAT</i> typesetter, a graphical output device from a PDP-11 computer running Unix. As <code>runoff</code> was too limited for this task it was further developed into a more powerful text formatting system by <i>Joseph F. Ossanna</i>, who already programmed several runoff ports. </p>
<p> The name <i>runoff</i> was shortened to <i>roff</i>. The greatly enlarged language of Ossanna&#8217;s version already included all elements of a full <i>roff system</i>. All modern <i>roff</i> systems try to implement compatibility to this system. So Joe Ossanna can be called the father of all <i>roff</i> systems. </p>
<p> This first <i>roff system</i> had three formatter programs.</p>
<dl>
<dt><code>troff</code></p>
<dd>(<i>typesetter roff/</i>) generated a graphical output for the <i>CAT</i> typesetter as its only device.</p>
<dt><code>nroff</code></p>
<dd>produced text output suitable for terminals and line printers.</p>
<dt><code>roff</code></p>
<dd>was the reimplementation of the former <code>runoff</code> program with its limited features; this program was abandoned in later versions. Today, the name <i>roff</i> is used to refer to a <i>troff/:nroff</i> system as a whole.</dl>
<p> Ossanna&#8217;s first version was written in the PDP-11 assembly language and released in 1973. <i>Brian Kernighan</i> joined the <i>roff</i> development by rewriting it in the C~programming language. The C~version was released in 1975. </p>
<p> The syntax of the formatting language of the <code>nroff</code>/:<code>troff</code> programs was documented in the famous <i>Troff User&#8217;s Manual</i> [CSTR~#54], first published in 1976, with further revisions up to 1992 by Brian Kernighan. This document is the specification of the <i>classical troff</i>. All later <i>roff</i> systems tried to establish compatibility with this specification. </p>
<p> After Ossanna&#8217;s death in 1977, Kernighan went on with developing <i>troff</i>. In the late 1970s, Kernighan equipped <i>troff</i> with a general interface to support more devices, the intermediate output format, and the postprocessor system. This completed the structure of a <i>roff system</i> as it is still in use today; see section &#8220;Using Roff&#8221; below. In 1979, these novelties were described in the paper [CSTR~#97]. This new <i>troff</i> version is the basis for all existing newer troff systems, including <i>groff</i>. On some systems, this <i>device independent troff</i> got a binary of its own, called <code><a href="/docs/linux/man/7-ditroff/">ditroff</a></code>(7). All modern <code>troff</code> programs already provide the full <code>ditroff</code> capabilities automatically.</p>
<h3>Availability</h3>
<p>The source code of both the ancient Unix and classical <i>troff</i> weren&#8217;t available for two decades. Nowadays, it is accessible again (on-line) for non-commercial use; see <code>SEE ALSO</code>, below.</p>
<h3>groff &#8212; free GNU roff</h3>
<p>The most important free <i>roff</i> project was the GNU implementation of <i>troff</i>, written from scratch by <i>James Clark</i> and put under the GNU Public License It was called <i>groff</i> (GNU <i>roff</i>). See <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1) for an overview. </p>
<p> The <i>groff</i> system is still actively developed. It is compatible to the classical <i>troff</i>, but many extensions were added. It is the first <i>roff</i> system that is available on almost all operating systems &#8212; and it is free. This makes <i>groff</i> the de facto <i>roff</i> standard today.</p>
<h3>Free Heirloom roff</h3>
<p>An alternative is <i>Gunnar Ritter&#8217;s Heirloom roff project</i> project, started in 2005, which provides enhanced versions of the various roff tools found in the OpenSolaris and Plan~9 operating systems, now available under free licenses. You can get this package with the shell command:</p>
<dl>
<dd>$ git clone <a rel="nofollow" href="https://github.com/n-t-roff/heirloom-doctools">https://github.com/n-t-roff/heirloom-doctools</a></dl>
<p> Moreover, one finds there the <i>Original Documenter&#8217;s Workbench Release 3.3</i></p>
<h2>Using Roff</h2>
<p>Most people won&#8217;t even notice that they are actually using <i>roff</i>. When you read a system manual page (man page) <i>roff</i> is working in the background. But using <i>roff</i> explicitly isn&#8217;t difficult either. </p>
<p> Some <i>roff</i> implementations provide wrapper programs that make it easy to use the <i>roff</i> system on the shell command line. For example, the GNU <i>roff</i> implementation <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1) provides command-line options to avoid the long command pipes of classical <i>troff</i>; a program <code><a href="/docs/linux/man/1-grog/">grog</a></code>(1) tries to guess from the document which arguments should be used for a run of <code>groff</code>; people who do not like specifying command-line options should try the <code><a href="/docs/linux/man/1-groffer/">groffer</a></code>(1) program for graphically displaying <i>groff</i> files and man pages.</p>
<h3>The roff Pipe</h3>
<p>Each <i>roff</i> system consists of preprocessors, <i>roff</i> formatter programs, and a set of device postprocessors. This concept makes heavy use of the <i>piping</i> mechanism, that is, a series of programs is called one after the other, where the output of each program in the queue is taken as the input for the next program.</p>
<dl>
<dd>cat file | &#8230; | preproc | &#8230; | troff options | postproc</dl>
<p> The preprocessors generate <i>roff</i> code that is fed into a <i>roff</i> formatter (e.g. <code>troff</code>), which in turn generates <i>intermediate output</i> that is fed into a device postprocessor program for printing or final output. </p>
<p> All of these parts use programming languages of their own; each language is totally unrelated to the other parts. Moreover, <i>roff</i> macro packages that were tailored for special purposes can be included. </p>
<p> Most <i>roff</i> documents use the macros of some package, intermixed with code for one or more preprocessors, spiced with some elements from the plain <i>roff</i> language. The full power of the <i>roff</i> formatting language is seldom needed by users; only programmers of macro packages need to know about the gory details.</p>
<h3>Preprocessors</h3>
<p>A <i>roff</i> preprocessor is any program that generates output that syntactically obeys the rules of the <i>roff</i> formatting language. Each preprocessor defines a language of its own that is translated into <i>roff</i> code when run through the preprocessor program. Parts written in these languages may be included within a <i>roff</i> document; they are identified by special <i>roff</i> requests or macros. Each document that is enhanced by preprocessor code must be run through all corresponding preprocessors before it is fed into the actual <i>roff</i> formatter program, for the formatter just ignores all alien code. The preprocessor programs extract and transform only the document parts that are determined for them. </p>
<p> There are a lot of free and commercial <i>roff</i> preprocessors. Some of them aren&#8217;t available on each system, but there is a small set of preprocessors that are considered as an integral part of each <i>roff</i> system. The classical preprocessors are</p>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>tbl</code></td>
<td>for tables.
</td>
</tr>
<tr VALIGN=top>
<td><code>eqn</code></td>
<td>for mathematical formulae.
</td>
</tr>
<tr VALIGN=top>
<td><code>pic</code></td>
<td>for drawing diagrams.
</td>
</tr>
<tr VALIGN=top>
<td><code>refer</code></td>
<td>for bibliographic references.
</td>
</tr>
<tr VALIGN=top>
<td><code>soelim</code></td>
<td>for including macro files from standard locations.
</td>
</tr>
<tr VALIGN=top>
<td><code>chem</code></td>
<td>for drawing chemical formul&aelig;.
</td>
</tr>
</table>
</dl>
<p> Other known preprocessors that are not available on all systems include</p>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>grap</code></td>
<td>for constructing graphical elements.
</td>
</tr>
<tr VALIGN=top>
<td><code>grn</code></td>
<td>for including <code><a href="/docs/linux/man/1-gremlin/">gremlin</a></code>(1) pictures.
</td>
</tr>
</table>
</dl>
<h3>Formatter Programs</h3>
<p>A <i>roff formatter</i> is a program that parses documents written in the <i>roff</i> formatting language or uses some of the <i>roff</i> macro packages. It generates <i>intermediate output</i>, which is intended to be fed into a single device postprocessor that must be specified by a command-line option to the formatter program. The documents must have been run through all necessary preprocessors before. </p>
<p> The output produced by a <i>roff</i> formatter is represented in yet another language, the <i>intermediate output format</i> or <i>troff output</i>. This language was first specified in [CSTR~#97]; its GNU extension is documented in <code><a href="/docs/linux/man/5-groff_out/">groff_out</a></code>(5). The intermediate output language is a kind of assembly language compared to the high-level <i>roff</i> language. The generated intermediate output is optimized for a special device, but the language is the same for every device. </p>
<p> The <i>roff</i> formatter is the heart of the <i>roff</i> system. The traditional <i>roff</i> had two formatters, <code>nroff</code> for text devices and <code>troff</code> for graphical devices. </p>
<p> Often, the name <i>troff</i> is used as a general term to refer to both formatters.</p>
<h3>Devices and Postprocessors</h3>
<p>Devices are hardware interfaces like printers, text or graphical terminals, etc., or software interfaces such as a conversion into a different text or graphical format. </p>
<p> A <i>roff</i> postprocessor is a program that transforms <i>troff</i> output into a form suitable for a special device. The <i>roff</i> postprocessors are like device drivers for the output target. </p>
<p> For each device there is a postprocessor program that fits the device optimally. The postprocessor parses the generated intermediate output and generates device-specific code that is sent directly to the device. </p>
<p> The names of the devices and the postprocessor programs are not fixed because they greatly depend on the software and hardware abilities of the actual computer. For example, the classical devices mentioned in [CSTR~#54] have greatly changed since the classical times. The old hardware doesn&#8217;t exist any longer and the old graphical conversions were quite imprecise when compared to their modern counterparts. </p>
<p> For example, the PostScript device <i>post</i> in classical <i>troff</i> had a resolution of 720 units per inch, while <i>groff</i>&#8216;s <i>ps</i> device has 72000, a refinement of factor 100. </p>
<p> Today the operating systems provide device drivers for most printer-like hardware, so it isn&#8217;t necessary to write a special hardware postprocessor for each printer.</p>
<h2>Roff Programming</h2>
<p>Documents using <i>roff</i> are normal text files decorated by <i>roff</i> formatting elements. The <i>roff</i> formatting language is quite powerful; it is almost a full programming language and provides elements to enlarge the language. With these, it became possible to develop macro packages that are tailored for special applications. Such macro packages are much handier than plain <i>roff</i>. So most people will choose a macro package without worrying about the internals of the <i>roff</i> language.</p>
<h3>Macro Packages</h3>
<p>Macro packages are collections of macros that are suitable to format a special kind of documents in a convenient way. This greatly eases the usage of <i>roff</i>. The macro definitions of a package are kept in a file called <i>name</i><code>.tmac</code> (classically <code>tmac.</code><i>name/</i>). All tmac files are stored in one or more directories at standardized positions. Details on the naming of macro packages and their placement is found in <code><a href="/docs/linux/man/5-groff_tmac/">groff_tmac</a></code>(5). </p>
<p> A macro package that is to be used in a document can be announced to the formatter by the command-line option <code>-m</code>, see <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1), or it can be specified within a document using the file inclusion requests of the <i>roff</i> language, see <code><a href="/docs/linux/man/7-groff/">groff</a></code>(7). </p>
<p> Famous classical macro packages are <i>man</i> for traditional man pages, <i>mdoc</i> for BSD-style manual pages; the macro sets for books, articles, and letters are <i>me</i> (probably from the first name of its creator <i>Eric</i> Allman), <i>ms</i> (from <i>Manuscript Macros/</i>), and <i>mm</i> (from <i>Memorandum Macros/</i>).</p>
<h3>The roff Formatting Language</h3>
<p>The classical <i>roff</i> formatting language is documented in the <i>Troff User&#8217;s Manual</i> [CSTR~#54]. The <i>roff</i> language is a full programming language providing requests, definition of macros, escape sequences, string variables, number or size registers, and flow controls. </p>
<p> <i>Requests</i> are the predefined basic formatting commands similar to the commands at the shell prompt. The user can define request-like elements using predefined <i>roff</i> elements. These are then called <i>macros</i>. A document writer will not note any difference in usage for requests or macros; both are written on a line on their own starting with a dot. </p>
<p> <i>Escape sequences</i> are <i>roff</i> elements starting with a backslash They can be inserted anywhere, also in the midst of text in a line. They are used to implement various features, including the insertion of non-ASCII characters with font changes with in-line comments with the escaping of special control characters like and many other features. </p>
<p> <i>Strings</i> are variables that can store a string. A string is stored by the <code>.ds</code> request. The stored string can be retrieved later by the <code>\*</code> escape sequence. </p>
<p> <i>Registers</i> store numbers and sizes. A register can be set with the request <code>.nr</code> and its value can be retrieved by the escape sequence <code>
</code>.</p>
<h2>File Name Extensions</h2>
<p>Manual pages (man pages) take the section number as a file name extension, e.g., the filename for this document is <i>roff.7</i>, i.e., it is kept in section~7 of the man pages. </p>
<p> The classical macro packages take the package name as an extension, e.g. <i>file.</i><code>me</code> for a document using the <i>me</i> macro package, <i>file.</i><code>mm</code> for <i>mm</i>, <i>file.</i><code>ms</code> for <i>ms</i>, <i>file.</i><code>pic</code> for <i>pic</i> files, etc. </p>
<p> But there is no general naming scheme for <i>roff</i> documents, though <i>file.</i><code>tr</code> for <i>troff file</i> is seen now and then. Maybe there should be a standardization for the filename extensions of <i>roff</i> files. </p>
<p> File name extensions can be very handy in conjunction with the <code><a href="/docs/linux/man/1-less/">less</a></code>(1) pager. It provides the possibility to feed all input into a command-line pipe that is specified in the shell environment variable <code>LESSOPEN</code>. This process is not well documented, so here an example:</p>
<dl>
<dd>LESSOPEN=&#8217;|lesspipe %s&#8217;</dl>
<p> where <code>lesspipe</code> is either a system supplied command or a shell script of your own. </p>
<p> More details for <i>file name extensions</i> can be found at <code><a href="/docs/linux/man/5-groff_filenames/">groff_filenames</a></code>(5).</p>
<h2>Editing Roff</h2>
<p>All <i>roff</i> formatters provide automated line breaks and horizontal and vertical spacing. In order to not disturb this, the following tips can be helpful.</p>
<dl>
<dt>&bull;</p>
<dd>Never include empty or blank lines in a <i>roff</i> document. Instead, use the empty request (a line consisting of a dot only) or a line comment <code>.\if a structuring element is needed.</code></p>
<dt>&bull;</p>
<dd>Never start a line with whitespace because this can lead to unexpected behavior. Indented paragraphs can be constructed in a controlled way by <i>roff</i> requests.</p>
<dt>&bull;</p>
<dd>Start each sentence on a line of its own, for the spacing after a dot is handled differently depending on whether it terminates an abbreviation or a sentence. To distinguish both cases, do a line break after each sentence.</p>
<dt>&bull;</p>
<dd>To additionally use the auto-fill mode in Emacs, it is best to insert an empty <i>roff</i> request (a line consisting of a dot only) after each sentence.</dl>
<p> The following example shows judicious line breaking in a <i>roff</i> input file.</p>
<dl>
<dd>This is an example of a .I roff document that you can type into your text editor. . This is the next sentence in the same paragraph. . This is a longer sentence stretching over several input lines; abbreviations like cf. are easily identified because the dot is not followed by a line break. . In the output, this sentence continues the same paragraph.</dl>
<h3>Editing with Emacs</h3>
<p>The best program for editing a <i>roff</i> document is Emacs (or XEmacs); see <code><a href="/docs/linux/man/1-emacs/">emacs</a></code>(1). It provides an <i>nroff</i> mode that is suitable for all kinds of <i>roff</i> dialects. This mode can be activated by the following methods. </p>
<p> When editing a file within Emacs the mode can be changed by typing &#8216;<i>M-x nroff-mode</i>&#8216;, where <code>M-x</code> means to hold down the <code>Meta</code> key (or <code>Alt</code>) and press the <code>x~</code>key at the same time. </p>
<p> But it is also possible to have the mode automatically selected when the file is loaded into the editor.</p>
<dl>
<dt>&bull;</p>
<dd>The most general method is to include the following 3 comment lines at the end of the file.</p>
<dl>
<dd>
<dl>
<dd>.\&quot; Local Variables: .\&quot; mode: nroff .\&quot; End:</dl>
</dl>
<dt>&bull;</p>
<dd>There is a set of file name extensions, e.g. the man pages that trigger the automatic activation of the <i>nroff</i> mode.</p>
<dt>&bull;</p>
<dd>Theoretically, it is possible to write the sequence</p>
<dl>
<dd>
<dl>
<dd>.\&quot; -*- nroff -*-</dl>
</dl>
<dd>as the first line of a file to have it started in <i>nroff</i> mode when loaded. Unfortunately, some applications such as the <code>man</code> program are confused by this; so this is deprecated.</dl>
<h3>Editing with Vim</h3>
<p>Besides Emacs, some other editors provide <i>nroff</i> style files too, e.g. <code><a href="/docs/linux/man/1-vim/">vim</a></code>(1), an extension of the <code><a href="/docs/linux/man/1-vi/">vi</a></code>(1) program. Vim&#8217;s highlighting can be made to recognize <i>roff</i> files by setting the <i>filetype</i> option in a Vim <i>modeline</i>. For this feature to work, your copy of <code>vim</code> must be built with support for, and configured to enable, several features; consult the editor&#8217;s online help topics &#8220;auto-setting&#8221;, &#8220;filetype&#8221;, and &#8220;syntax&#8221;. Then put the following at the end of your <i>roff</i> files, after any Emacs configuration: </p>
<dl>
<dd>
<dl>
<dd>.\&quot; vim: set filetype=groff:</dl>
</dl>
<p> Replace &#8220;groff&#8221; in the above with &#8220;nroff&#8221; if you want highlighing that does <i>not</i> recognize many of the GNU extensions to <i>roff</i>, such as request, register, and string names longer than two characters.</p>
<h2>Authors</h2>
<p>This document was written by Bernd Warken</p>
<h2>See Also</h2>
<p>There is a lot of documentation on <i>roff</i>. The original papers on classical <i>troff</i> are still available, and all aspects of <i>groff</i> are documented in great detail.</p>
<h3>Internet sites</h3>
<dl>
<dt>History of Unix Manpages</p>
<dd>The history page of the mdocml project provides an overview of <i>roff</i> development up to date, with links to original documentation and comments of the original authors.</p>
<dt>troff.org</p>
<dd>The historical troff site provides an overview and pointers to the historical aspects of <i>roff</i>.</p>
<dt>Multics</p>
<dd>The Multics site contains a lot of information on the MIT projects, CTSS, Multics, early Unix, including <i>runoff</i>; especially useful are a glossary and the many links to ancient documents.</p>
<dt>Unix Archive</p>
<dd>The Ancient Unixes Archive provides the source code and some binaries of the ancient Unixes (including the source code of <i>troff</i> and its documentation) that were made public by Caldera since 2001, e.g. of the famous Unix version~7 for PDP-11 at the Unix V7 site</p>
<dt>Developers at AT&amp;T Bell Labs</p>
<dd>Bell Labs Computing and Mathematical Sciences Research provides a search facility for tracking information on the early developers.</p>
<dt>Plan 9</p>
<dd>The Plan~9 operating system by AT&amp;T Bell Labs.</p>
<dt>runoff</p>
<dd>Jerry Saltzer&#8217;s home page stores some documents using the ancient RUNOFF formatting language.</p>
<dt>CSTR Papers</p>
<dd>The Bell Labs (now Alcatel) CSTR site stores the original <i>troff</i> manuals (CSTR #54, #97, #114, #116, #122) and famous historical documents on programming.</p>
<dt>GNU roff</p>
<dd>The groff web site provides the free <i>roff</i> implementation <i>groff</i>, the actual standard <i>roff</i>.</dl>
<h3>Historical roff Documentation</h3>
<p>Many classical <code>troff</code> documents are still available on-line. The two main manuals of the <i>troff</i> language are</p>
<dl>
<dt>[CSTR~#54]</p>
<dd>J. F. Ossanna, <i>Nroff/:Troff User&#8217;s Manual</i> Bell Labs, 1976; revised by Brian Kernighan, 1992.</p>
<dt>[CSTR~#97]</p>
<dd>Brian Kernighan, <i>A Typesetter-independent TROFF</i> Bell Labs, 1981, revised March 1982.</dl>
<p> The &#8220;little language&#8221; <i>roff</i> papers are</p>
<dl>
<dt>[CSTR~#114]</p>
<dd>Jon L. Bentley and Brian W. Kernighan, <i>GRAP &#8211; A Language for Typesetting Graphs</i> Bell Labs, August 1984.</p>
<dt>[CSTR~#116]</p>
<dd>Brian W. Kernighan, <i>PIC &#8211; A Graphics Language for Typesetting</i> Bell Labs, December 1984.</p>
<dt>[CSTR~#122]</p>
<dd>J. L. Bentley, L. W. Jelinski, and B. W. Kernighan, <i>CHEM &#8211; A Program for Typesetting Chemical Structure Diagrams,</i> <i>Computers and Chemistry</i> Bell Labs, April 1986.</dl>
<p> You can get an archive with most <i>classical roff documentation</i> as reasonable <i>PDF files</i> at <i>github</i> using the <i>shell command</i></p>
<dl>
<dd>$ git clone <a rel="nofollow" href="https://github.com/bwarken/roff_classical.git">https://github.com/bwarken/roff_classical.git</a></dl>
<h3>Manual Pages</h3>
<p>Due to its complex structure, a full <i>roff</i> system has many man pages, each describing a single aspect of <i>roff</i>. Unfortunately, there is no general naming scheme for the documentation among the different <i>roff</i> implementations. In <i>groff</i>, the man page <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1) contains a survey of all documentation available in <i>groff</i>. On other systems, you are on your own, but <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1) might be a good starting point. </p>
