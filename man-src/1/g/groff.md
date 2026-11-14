---
title: "groff(1)"
name: "groff"
section: "1"
letter: "g"
url: "/docs/linux/man/1-groff/"
description: "groff – front-end for the groff document formatting system"
---

<h2 class="name">NAME</h2>
<p> groff &#8211; front-end for the groff document formatting system </p>
<h2>SYNOPSIS</h2>
<p> [ <code>-abcegijklpstzCEGNRSUVXZ</code> ] [ <code>-d </code><i>cs</i> ] [ <code>-D </code><i>arg</i> ] [ <code>-f </code><i>fam</i> ] [ <code>-F </code><i>dir</i> ] [ <code>-I </code><i>dir</i> ] [ <code>-K </code><i>arg</i> ] [ <code>-L </code><i>arg</i> ] [ <code>-m </code><i>name</i> ] [ <code>-M </code><i>dir</i> ] [ <code>-n </code><i>num</i> ] [ <code>-o </code><i>list</i> ] [ <code>-P </code><i>arg</i> ] [ <code>-r </code><i>cn</i> ] [ <code>-T </code><i>dev</i> ] [ <code>-w </code><i>name</i> ] [ <code>-W </code><i>name</i> ] [<i>file</i> &#8230;] <code>-h</code> <code>&#8211;help</code> <code>-v</code> [<i>option</i> &#8230;] <code>&#8211;version</code> [<i>option</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> This document describes the <code>groff</code> program, the main front-end for the <i>groff</i> document formatting system. The <i>groff</i> program and macro suite is the implementation of a <code><a href="/docs/linux/man/7-roff/">roff</a></code>(7) system within the free software collection GNU The <i>groff</i> system has all features of the classical <i>roff</i>, but adds many extensions. </p>
<p> The <code>groff</code> program allows control of the whole <i>groff</i> system by command-line options. This is a great simplification in comparison to the classical case (which uses pipes only).</p>
<h2>OPTIONS</h2>
<p> The command line is parsed according to the usual GNU convention. Whitespace is permitted between a command-line option and its argument. Options can be grouped behind a single &#8216;-&#8216; (minus character). A filename of <code>&#8211;</code> (minus character) denotes the standard input. </p>
<p> As <code>groff</code> is a wrapper program for <code>troff</code> both programs share a set of options. But the <code>groff</code> program has some additional, native options and gives a new meaning to some <code>troff</code> options. On the other hand, not all <code>troff</code> options can be fed into <code>groff</code>.</p>
<h3>Native groff Options</h3>
<p> The following options either do not exist for <code>troff</code> or are differently interpreted by <code>groff</code>.</p>
<dl>
<dt><code>-D&nbsp;</code><i>arg</i></p>
<dd> Set default input encoding used by <code>preconv</code> to <i>arg</i>. Implies <code>-k</code>.</p>
<dt><code>-e</code></p>
<dd> Preprocess with <code>eqn</code>.</p>
<dt><code>-g</code></p>
<dd> Preprocess with <code>grn</code>.</p>
<dt><code>-G</code></p>
<dd> Preprocess with <code>grap</code>. Implies <code>-p</code>.</p>
<dt><code>-h</code></p>
<dd> <code>&#8211;help</code> Print a help message.</p>
<dt><code>-I&nbsp;</code><i>dir</i></p>
<dd> This option may be used to specify a directory to search for files (both those on the command line and those named in <code>.psbb</code> and <code>.so</code> requests, and <code>\X&#8217;ps: import&#8217;</code> , <code>\X&#8217;ps: file&#8217;</code> and <code>\X&#8217;pdf: pdfpic&#8217;</code> escapes). The current directory is always searched first. This option may be specified more than once; the directories are searched in the order specified. No directory search is performed for files specified using an absolute path. This option implies the <code>-s</code> option.</p>
<dt><code>-j</code></p>
<dd> Preprocess with <code>chem</code>. Implies <code>-p</code>.</p>
<dt><code>-k</code></p>
<dd> Preprocess with <code>preconv</code>. This is run before any other preprocessor. Please refer to <code>preconv</code>&#8216;s manual page for its behaviour if no <code>-K</code> (or <code>-D</code>) option is specified.</p>
<dt><code>-K&nbsp;</code><i>arg</i></p>
<dd> Set input encoding used by <code>preconv</code> to <i>arg</i>. Implies <code>-k</code>.</p>
<dt><code>-l</code></p>
<dd> Send the output to a spooler program for printing. The command that should be used for this is specified by the <code>print</code> command in the device description file, see <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5). If this command is not present, the output is piped into the <code><a href="/docs/linux/man/1-lpr/">lpr</a></code>(1) program by default. See options <code>-L</code> and <code>-X</code>.</p>
<dt><code>-L&nbsp;</code><i>arg</i></p>
<dd> Pass <i>arg</i> to the spooler program. Several arguments should be passed with a separate -L option each. Note that <code>groff</code> does not prepend &#8216;-&#8216; (a minus sign) to <i>arg</i> before passing it to the spooler program.</p>
<dt><code>-N</code></p>
<dd> Don&#8217;t allow newlines within <i>eqn</i> delimiters. This is the same as the <code>-N</code> option in <code>eqn</code>.</p>
<dt><code>-p</code></p>
<dd> Preprocess with <code>pic</code>.</p>
<dt><code>-P&nbsp;</code><i>-option</i></p>
<dd> <code>-P&nbsp;</code><i>-option</i><code>&nbsp;-P&nbsp;</code><i>arg</i> Pass <i>-option</i> or <i>-option~arg</i> to the postprocessor. The option must be specified with the necessary preceding minus sign(s) &#8216;-&#8216; or &#8216;&#8211;&#8216; because <code>groff</code> does not prepend any dashes before passing it to the postprocessor. For example, to pass a title to the <code>gxditview</code> postprocessor, the shell command</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> groff -X -P -title -P &#8216;groff it&#8217; foo</dl>
</dl>
<dt>
<dd> is equivalent to</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> groff -X -Z foo | gxditview -title &#8216;groff it&#8217; &#8211;</dl>
</dl>
<dt><code>-R</code></p>
<dd> Preprocess with <code>refer</code>. No mechanism is provided for passing arguments to <code>refer</code> because most <code>refer</code> options have equivalent language elements that can be specified within the document. See <code><a href="/docs/linux/man/1-refer/">refer</a></code>(1) for more details.</p>
<dt><code>-s</code></p>
<dd> Preprocess with <code>soelim</code>.</p>
<dt><code>-S</code></p>
<dd> Safer mode. Pass the <code>-S</code> option to <code>pic</code> and disable the following <code>troff</code> requests: <code>.open</code>, <code>.opena</code>, <code>.pso</code>, <code>.sy</code>, and <code>.pi</code>. For security reasons, safer mode is enabled by default.</p>
<dt><code>-t</code></p>
<dd> Preprocess with <code>tbl</code>.</p>
<dt><code>-T&nbsp;</code><i>dev</i></p>
<dd> Set output device to <i>dev</i>. For this device, <code>troff</code> generates the <i>intermediate</i> <i>output</i>; see <code><a href="/docs/linux/man/5-groff_out/">groff_out</a></code>(5). Then <code>groff</code> calls a postprocessor to convert <code>troff</code>&#8216;s <i>intermediate output</i> to its final format. Real devices in <code>groff</code> are</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>dvi</p>
<dd> TeX DVI format (postprocessor is <code>grodvi</code>).</p>
<dt>html</p>
<dd> xhtml HTML and XHTML output (preprocessors are <code>soelim</code> and <code>pre-grohtml</code>, postprocessor is <code>post-grohtml</code>).</p>
<dt>lbp</p>
<dd> Canon CAPSL printers (LBP-4 and LBP-8 series laser printers; postprocessor is <code>grolbp</code>).</p>
<dt>lj4</p>
<dd> HP LaserJet4 compatible (or other PCL5 compatible) printers (postprocessor is <code>grolj4</code>).</p>
<dt>ps</p>
<dd> PostScript output (postprocessor is <code>grops</code>).</p>
<dt>pdf</p>
<dd> Portable Document Format (PDF) output (postprocessor is <code>gropdf</code>).</dl>
</dl>
</dl>
<dt>
<dd> For the following TTY output devices (postprocessor is always <code>grotty</code>), <code>-T</code> selects the output encoding:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>ascii</p>
<dd> 7bit ASCII.</p>
<dt>cp1047</p>
<dd> Latin-1 character set for EBCDIC hosts.</p>
<dt>latin1</p>
<dd> ISO 8859-1.</p>
<dt>utf8</p>
<dd> Unicode character set in UTF-8 encoding. This mode has the most useful fonts for TTY mode, so it is the best mode for TTY output.</dl>
</dl>
</dl>
<dt>
<dd> The following arguments select <code>gxditview</code> as the &#8216;postprocessor&#8217; (it is rather a viewing program):</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>X75</p>
<dd> 75dpi resolution, 10pt document base font.</p>
<dt>X75-12</p>
<dd> 75dpi resolution, 12pt document base font.</p>
<dt>X100</p>
<dd> 100dpi resolution, 10pt document base font.</p>
<dt>X100-12</p>
<dd> 100dpi resolution, 12pt document base font.</dl>
</dl>
</dl>
<dt>
<dd> The default device is <code>ps</code>.</p>
<dt><code>-U</code></p>
<dd> Unsafe mode. Reverts to the (old) unsafe behaviour; see option <code>-S</code>.</p>
<dt><code>-v</code></p>
<dd> <code>&#8211;version</code> Output version information of <code>groff</code> and of all programs that are run by it; that is, the given command line is parsed in the usual way, passing <code>-v</code> to all subprograms.</p>
<dt><code>-V</code></p>
<dd> Output the pipeline that would be run by <code>groff</code> (as a wrapper program) on the standard output, but do not execute it. If given more than once, the commands are both printed on the standard error and run.</p>
<dt><code>-X</code></p>
<dd> Use <code>gxditview</code> instead of using the usual postprocessor to (pre)view a document. The printing spooler behavior as outlined with options <code>-l</code> and <code>-L</code> is carried over to <code><a href="/docs/linux/man/1-gxditview/">gxditview</a></code>(1) by determining an argument for the <code>-printCommand</code> option of <code><a href="/docs/linux/man/1-gxditview/">gxditview</a></code>(1). This sets the default <code>Print</code> action and the corresponding menu entry to that value. <code>-X</code> only produces good results with <code>-Tps</code>, <code>-TX75</code>, <code>-TX75-12</code>, <code>-TX100</code>, and <code>-TX100-12</code>. The default resolution for previewing <code>-Tps</code> output is 75dpi; this can be changed by passing the <code>-resolution</code> option to <code>gxditview</code>, for example</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> groff -X -P-resolution -P100 -man foo.1</dl>
</dl>
<dt><code>-z</code></p>
<dd> Suppress output generated by <code>troff</code>. Only error messages are printed.</p>
<dt><code>-Z</code></p>
<dd> Do not automatically postprocess <i>groff intermediate output</i> in the usual manner. This will cause the <code>troff</code> <i>output</i> to appear on standard output, replacing the usual postprocessor output; see <code><a href="/docs/linux/man/5-groff_out/">groff_out</a></code>(5).</dl>
<h3>Transparent Options</h3>
<p> The following options are transparently handed over to the formatter program <code>troff</code> that is called by <code>groff</code> subsequently. These options are described in more detail in <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1).</p>
<dl>
<dt><code>-a</code></p>
<dd> ASCII approximation of output.</p>
<dt><code>-b</code></p>
<dd> Backtrace on error or warning.</p>
<dt><code>-c</code></p>
<dd> Disable color output. Please consult the <code><a href="/docs/linux/man/1-grotty/">grotty</a></code>(1) man page for more details.</p>
<dt><code>-C</code></p>
<dd> Enable compatibility mode.</p>
<dt><code>-d&nbsp;</code><i>cs</i></p>
<dd> <code>-d&nbsp;</code><i>name</i><code>=</code><i>s</i> Define string.</p>
<dt><code>-E</code></p>
<dd> Disable <code>troff</code> error messages.</p>
<dt><code>-f&nbsp;</code><i>fam</i></p>
<dd> Set default font family.</p>
<dt><code>-F&nbsp;</code><i>dir</i></p>
<dd> Set path for device <i>DESC</i> files.</p>
<dt><code>-i</code></p>
<dd> Process standard input after the specified input files.</p>
<dt><code>-m&nbsp;</code><i>name</i></p>
<dd> Include macro file name<i>.tmac</i> (or <i>tmac.</i>name); see also <code><a href="/docs/linux/man/5-groff_tmac/">groff_tmac</a></code>(5).</p>
<dt><code>-M&nbsp;</code><i>dir</i></p>
<dd> Path for macro files.</p>
<dt><code>-n&nbsp;</code><i>num</i></p>
<dd> Number the first page <i>num</i>.</p>
<dt><code>-o&nbsp;</code><i>list</i></p>
<dd> Output only pages in <i>list</i>.</p>
<dt><code>-r&nbsp;</code><i>cn</i></p>
<dd> <code>-r&nbsp;</code><i>name</i><code>=</code><i>n</i> Set number register.</p>
<dt><code>-w&nbsp;</code><i>name</i></p>
<dd> Enable warning <i>name</i>. See <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1) for names.</p>
<dt><code>-W&nbsp;</code><i>name</i></p>
<dd> disable warning <i>name</i>. See <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1) for names.</dl>
<h2>USING GROFF</h2>
<p> The <i>groff system</i> implements the infrastructure of classical roff; see <code><a href="/docs/linux/man/7-roff/">roff</a></code>(7) for a survey on how a <i>roff</i> system works in general. Due to the front-end programs available within the <i>groff</i> system, using <i>groff</i> is much easier than <i>classical roff</i>. This section gives an overview of the parts that constitute the <i>groff</i> system. It complements <code><a href="/docs/linux/man/7-roff/">roff</a></code>(7) with <i>groff</i>-specific features. This section can be regarded as a guide to the documentation around the <i>groff</i> system.</p>
<h3>Paper Size</h3>
<p> The <i>virtual</i> paper size used by <code>troff</code> to format the input is controlled globally with the requests <code>.po</code>, <code>.pl</code>, and <code>.ll</code>. See <code><a href="/docs/linux/man/5-groff_tmac/">groff_tmac</a></code>(5) for the &#8216;papersize&#8217; macro package which provides a convenient interface. </p>
<p> The <i>physical</i> paper size, giving the actual dimensions of the paper sheets, is controlled by output devices like <code>grops</code> with the command-line options <code>-p</code> and <code>-l</code>. See <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5) and the man pages of the output devices for more details. <code>groff</code> uses the command-line option <code>-P</code> to pass options to output devices; for example, the following selects A4 paper in landscape orientation for the PS device:</p>
<dl>
<dt>
<dd> groff -Tps -P-pa4 -P-l &#8230;</dl>
<h3>Front-ends</h3>
<p> The <code>groff</code> program is a wrapper around the <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1) program. It allows one to specify the preprocessors by command-line options and automatically runs the postprocessor that is appropriate for the selected device. Doing so, the sometimes tedious piping mechanism of classical <code><a href="/docs/linux/man/7-roff/">roff</a></code>(7) can be avoided. </p>
<p> The <code><a href="/docs/linux/man/1-grog/">grog</a></code>(1) program can be used for guessing the correct <i>groff</i> command line to format a file. </p>
<p> The <code><a href="/docs/linux/man/1-groffer/">groffer</a></code>(1) program is an all-around viewer for <i>groff</i> files and man pages.</p>
<h3>Preprocessors</h3>
<p> The <i>groff</i> preprocessors are reimplementations of the classical preprocessors with moderate extensions. The standard preprocessors distributed with the <i>groff</i> package are</p>
<dl>
<dt><code><a href="/docs/linux/man/1-eqn/">eqn</a></code>(1)</p>
<dd> for mathematical formulae,</p>
<dt><code><a href="/docs/linux/man/1-grn/">grn</a></code>(1)</p>
<dd> for including <code><a href="/docs/linux/man/1-gremlin/">gremlin</a></code>(1) pictures,</p>
<dt><code><a href="/docs/linux/man/1-pic/">pic</a></code>(1)</p>
<dd> for drawing diagrams,</p>
<dt><code><a href="/docs/linux/man/1-chem/">chem</a></code>(1)</p>
<dd> for chemical structure diagrams,</p>
<dt><code><a href="/docs/linux/man/1-refer/">refer</a></code>(1)</p>
<dd> for bibliographic references,</p>
<dt><code><a href="/docs/linux/man/1-soelim/">soelim</a></code>(1)</p>
<dd> for including macro files from standard locations,</dl>
<p> and</p>
<dl>
<dt><code><a href="/docs/linux/man/1-tbl/">tbl</a></code>(1)</p>
<dd> for tables.</dl>
<p> A new preprocessor not available in classical <i>troff</i> is <code><a href="/docs/linux/man/1-preconv/">preconv</a></code>(1) which converts various input encodings to something <code>groff</code> can understand. It is always run first before any other preprocessor. </p>
<p> Besides these, there are some internal preprocessors that are automatically run with some devices. These aren&#8217;t visible to the user.</p>
<h3>Macro Packages</h3>
<p> Macro packages can be included by option <code>-m</code>. The <i>groff</i> system implements and extends all classical macro packages in a compatible way and adds some packages of its own. Actually, the following macro packages come with <i>groff</i>:</p>
<dl>
<dt><code>man</code></p>
<dd> The traditional man page format; see <code><a href="/docs/linux/man/7-groff_man/">groff_man</a></code>(7). It can be specified on the command line as <code>-man</code> or <code>-m~man</code>.</p>
<dt><code>mandoc</code></p>
<dd> The general package for man pages; it automatically recognizes whether the documents uses the <i>man</i> or the <i>mdoc</i> format and branches to the corresponding macro package. It can be specified on the command line as <code>-mandoc</code> or <code>-m~mandoc</code>.</p>
<dt><code>mdoc</code></p>
<dd> The BSD-style man page format; see <code><a href="/docs/linux/man/7-groff_mdoc/">groff_mdoc</a></code>(7). It can be specified on the command line as <code>-mdoc</code> or <code>-m~mdoc</code>.</p>
<dt><code>me</code></p>
<dd> The classical <i>me</i> document format; see <code><a href="/docs/linux/man/7-groff_me/">groff_me</a></code>(7). It can be specified on the command line as <code>-me</code> or <code>-m~me</code>.</p>
<dt><code>mm</code></p>
<dd> The classical <i>mm</i> document format; see <code><a href="/docs/linux/man/7-groff_mm/">groff_mm</a></code>(7). It can be specified on the command line as <code>-mm</code> or <code>-m~mm</code>.</p>
<dt><code>ms</code></p>
<dd> The classical <i>ms</i> document format; see <code><a href="/docs/linux/man/7-groff_ms/">groff_ms</a></code>(7). It can be specified on the command line as <code>-ms</code> or <code>-m~ms</code>.</p>
<dt><code>www</code></p>
<dd> HTML-like macros for inclusion in arbitrary <i>groff</i> documents; see <code><a href="/docs/linux/man/7-groff_www/">groff_www</a></code>(7).</dl>
<p> Details on the naming of macro files and their placement can be found in <code><a href="/docs/linux/man/5-groff_tmac/">groff_tmac</a></code>(5); this man page also documents some other, minor auxiliary macro packages not mentioned here.</p>
<h3>Programming Language</h3>
<p> General concepts common to all <i>roff</i> programming languages are described in <code><a href="/docs/linux/man/7-roff/">roff</a></code>(7). </p>
<p> The <i>groff</i> extensions to the classical <i>troff</i> language are documented in <code><a href="/docs/linux/man/7-groff_diff/">groff_diff</a></code>(7). </p>
<p> An overview of language features, including all supported escapes and requests, can be found in <code><a href="/docs/linux/man/7-groff/">groff</a></code>(7).</p>
<h3>Formatters</h3>
<p> The central <i>roff</i> formatter within the <i>groff</i> system is <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1). It provides the features of both the classical <i>troff</i> and <i>nroff</i>, as well as the <i>groff</i> extensions. The command-line option <code>-C</code> switches <code>troff</code> into <i>compatibility mode</i> which tries to emulate classical <i>roff</i> as much as possible. </p>
<p> There is a shell script <code><a href="/docs/linux/man/1-nroff/">nroff</a></code>(1) that emulates the behavior of classical <code>nroff</code>. It tries to automatically select the proper output encoding, according to the current locale. </p>
<p> The formatter program generates <i>intermediate output</i>; see <code><a href="/docs/linux/man/7-groff_out/">groff_out</a></code>(7).</p>
<h3>Devices</h3>
<p> In <i>roff</i>, the output targets are called <i>devices</i>. A device can be a piece of hardware, e.g., a printer, or a software file format. A device is specified by the option <code>-T</code>. The <i>groff</i> devices are as follows.</p>
<dl>
<dt><code>ascii</code></p>
<dd> Text output using the <code><a href="/docs/linux/man/7-ascii/">ascii</a></code>(7) character set.</p>
<dt><code>cp1047</code></p>
<dd> Text output using the EBCDIC code page IBM cp1047 (e.g., OS/390 Unix).</p>
<dt><code>dvi</code></p>
<dd> TeX DVI format.</p>
<dt><code>html</code></p>
<dd> HTML output.</p>
<dt><code>latin1</code></p>
<dd> Text output using the ISO Latin-1 (ISO 8859-1) character set; see <code><a href="/docs/linux/man/7-iso_8859_1/">iso_8859_1</a></code>(7).</p>
<dt><code>lbp</code></p>
<dd> Output for Canon CAPSL printers (LBP-4 and LBP-8 series laser printers).</p>
<dt><code>lj4</code></p>
<dd> HP LaserJet4-compatible (or other PCL5-compatible) printers.</p>
<dt><code>ps</code></p>
<dd> PostScript output; suitable for printers and previewers like <code><a href="/docs/linux/man/1-gv/">gv</a></code>(1).</p>
<dt><code>pdf</code></p>
<dd> PDF files; suitable for viewing with tools such as <code><a href="/docs/linux/man/1-evince/">evince</a></code>(1) and <code><a href="/docs/linux/man/1-okular/">okular</a></code>(1).</p>
<dt><code>utf8</code></p>
<dd> Text output using the Unicode (ISO 10646) character set with UTF-8 encoding; see <code><a href="/docs/linux/man/7-unicode/">unicode</a></code>(7).</p>
<dt><code>xhtml</code></p>
<dd> XHTML output.</p>
<dt><code>X75</code></p>
<dd> 75dpi X Window System output suitable for the previewers <code><a href="//www.systutorials.com/docs/linux/man/1x-xditview/">xditview</a></code>(1x) and <code><a href="/docs/linux/man/1-gxditview/">gxditview</a></code>(1). A variant for a 12pt document base font is <code>X75-12</code>.</p>
<dt><code>X100</code></p>
<dd> 100dpi X Window System output suitable for the previewers <code><a href="//www.systutorials.com/docs/linux/man/1x-xditview/">xditview</a></code>(1x) and <code><a href="/docs/linux/man/1-gxditview/">gxditview</a></code>(1). A variant for a 12pt document base font is <code>X100-12</code>.</dl>
<p> The postprocessor to be used for a device is specified by the <code>postpro</code> command in the device description file; see <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5). This can be overridden with the <code>-X</code> option. </p>
<p> The default device is <code>ps</code>.</p>
<h3>Postprocessors</h3>
<p> <i>groff</i> provides 3~hardware postprocessors:</p>
<dl>
<dt><code><a href="/docs/linux/man/1-grolbp/">grolbp</a></code>(1)</p>
<dd> for some Canon printers,</p>
<dt><code><a href="/docs/linux/man/1-grolj4/">grolj4</a></code>(1)</p>
<dd> for printers compatible to the HP LaserJet~4 and PCL5,</p>
<dt><code><a href="/docs/linux/man/1-grotty/">grotty</a></code>(1)</p>
<dd> for text output using various encodings, e.g., on text-oriented terminals or line printers.</dl>
<p> Today, most printing or drawing hardware is handled by the operating system, by device drivers, or by software interfaces, usually accepting PostScript. Consequently, there isn&#8217;t an urgent need for more hardware device postprocessors. </p>
<p> The <i>groff</i> software devices for conversion into other document file formats are</p>
<dl>
<dt><code><a href="/docs/linux/man/1-grodvi/">grodvi</a></code>(1)</p>
<dd> for the DVI format,</p>
<dt><code><a href="/docs/linux/man/1-grohtml/">grohtml</a></code>(1)</p>
<dd> for HTML and XHTML formats,</p>
<dt><code><a href="/docs/linux/man/1-grops/">grops</a></code>(1)</p>
<dd> for PostScript.</p>
<dt><code><a href="/docs/linux/man/1-gropdf/">gropdf</a></code>(1)</p>
<dd> for PDF.</dl>
<p> Combined with the many existing free conversion tools this should be sufficient to convert a <i>troff</i> document into virtually any existing data format.</p>
<h3>Utilities</h3>
<p> The following utility programs around <i>groff</i> are available.</p>
<dl>
<dt><code><a href="/docs/linux/man/1-addftinfo/">addftinfo</a></code>(1)</p>
<dd> Add information to <i>troff</i> font description files for use with <i>groff</i>.</p>
<dt><code><a href="/docs/linux/man/1-afmtodit/">afmtodit</a></code>(1)</p>
<dd> Create font description files for PostScript device.</p>
<dt><code><a href="/docs/linux/man/1-eqn2graph/">eqn2graph</a></code>(1)</p>
<dd> Convert an <code>eqn</code> image into a cropped image.</p>
<dt><code><a href="/docs/linux/man/1-gdiffmk/">gdiffmk</a></code>(1)</p>
<dd> Mark differences between <i>groff</i>, <i>nroff</i>, or <i>troff</i> files.</p>
<dt><code><a href="/docs/linux/man/1-grap2graph/">grap2graph</a></code>(1)</p>
<dd> Convert a <code>grap</code> diagram into a cropped bitmap image.</p>
<dt><code><a href="/docs/linux/man/1-groffer/">groffer</a></code>(1)</p>
<dd> General viewer program for <i>groff</i> files and man pages.</p>
<dt><code><a href="/docs/linux/man/1-gxditview/">gxditview</a></code>(1)</p>
<dd> The <i>groff</i> X viewer, the GNU version of <code>xditview</code>.</p>
<dt><code><a href="/docs/linux/man/1-hpftodit/">hpftodit</a></code>(1)</p>
<dd> Create font description files for lj4 device.</p>
<dt><code><a href="/docs/linux/man/1-indxbib/">indxbib</a></code>(1)</p>
<dd> Make inverted index for bibliographic databases.</p>
<dt><code><a href="/docs/linux/man/1-lkbib/">lkbib</a></code>(1)</p>
<dd> Search bibliographic databases.</p>
<dt><code><a href="/docs/linux/man/1-lookbib/">lookbib</a></code>(1)</p>
<dd> Interactively search bibliographic databases.</p>
<dt><code><a href="/docs/linux/man/1-pdfroff/">pdfroff</a></code>(1)</p>
<dd> Create PDF documents using <code>groff</code>.</p>
<dt><code><a href="/docs/linux/man/1-pfbtops/">pfbtops</a></code>(1)</p>
<dd> Translate a PostScript font in .pfb format to ASCII.</p>
<dt><code><a href="/docs/linux/man/1-pic2graph/">pic2graph</a></code>(1)</p>
<dd> Convert a <code>pic</code> diagram into a cropped image.</p>
<dt><code><a href="/docs/linux/man/1-tfmtodit/">tfmtodit</a></code>(1)</p>
<dd> Create font description files for TeX DVI device.</p>
<dt><code><a href="//www.systutorials.com/docs/linux/man/1x-xditview/">xditview</a></code>(1x)</p>
<dd> <i>roff</i> viewer historically distributed with the X Window System.</p>
<dt><code><a href="/docs/linux/man/1-xtotroff/">xtotroff</a></code>(1)</p>
<dd> Convert X font metrics into GNU <i>troff</i> font metrics.</dl>
<h2>ENVIRONMENT</h2>
<p> Normally, the path separator in the following environment variables is the colon; this may vary depending on the operating system. For example, DOS and Windows use a semicolon instead.</p>
<dl>
<dt><i>GROFF_BIN_PATH</i></p>
<dd> This search path, followed by <i>PATH</i>, is used for commands that are executed by <code>groff</code>. If it is not set then the directory where the <i>groff</i> binaries were installed is prepended to <i>PATH</i>.</p>
<dt><i>GROFF_COMMAND_PREFIX</i></p>
<dd> When there is a need to run different <i>roff</i> implementations at the same time <i>groff</i> provides the facility to prepend a prefix to most of its programs that could provoke name clashings at run time (default is to have none). Historically, this prefix was the character <code>g</code>, but it can be anything. For example, <code>gtroff</code> stood for <i>groff</i>&#8216;s <code>troff</code>, <code>gtbl</code> for the <i>groff</i> version of <code>tbl</code>. By setting <i>GROFF_COMMAND_PREFIX</i> to different values, the different <i>roff</i> installations can be addressed. More exactly, if it is set to prefix <i>xxx</i> then <code>groff</code> as a wrapper program internally calls <i>xxx</i><code>troff</code> instead of <code>troff</code>. This also applies to the preprocessors <code>eqn</code>, <code>grn</code>, <code>pic</code>, <code>refer</code>, <code>tbl</code>, <code>soelim</code>, and to the utilities <code>indxbib</code> and <code>lookbib</code>. This feature does not apply to any programs different from the ones above (most notably <code>groff</code> itself) since they are unique to the <i>groff</i> package.</p>
<dt><i>GROFF_ENCODING</i></p>
<dd> The value of this environment value is passed to the <code>preconv</code> preprocessor to select the encoding of input files. Setting this option implies <code>groff</code>&#8216;s command-line option <code>-k</code> (this is, <code>groff</code> actually always calls <code>preconv</code>). If set without a value, <code>groff</code> calls <code>preconv</code> without arguments. An explicit <code>-K</code> command-line option overrides the value of <i>GROFF_ENCODING</i>. See <code><a href="/docs/linux/man/1-preconv/">preconv</a></code>(1) for details.</p>
<dt><i>GROFF_FONT_PATH</i></p>
<dd> A list of directories in which to search for the <i>dev</i>name directory in addition to the default ones. See <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1) and <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5) for more details.</p>
<dt><i>GROFF_TMAC_PATH</i></p>
<dd> A list of directories in which to search for macro files in addition to the default directories. See <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1) and <code><a href="/docs/linux/man/5-groff_tmac/">groff_tmac</a></code>(5) for more details.</p>
<dt><i>GROFF_TMPDIR</i></p>
<dd> The directory in which temporary files are created. If this is not set but the environment variable <i>TMPDIR</i> instead, temporary files are created in the directory <i>TMPDIR</i>. On MS-DOS and Windows platforms, the environment variables <i>TMP</i> and <i>TEMP</i> (in that order) are searched also, after <i>GROFF_TMPDIR</i> and <i>TMPDIR</i>. Otherwise, temporary files are created in <i>/tmp</i>. The <code><a href="/docs/linux/man/1-refer/">refer</a></code>(1), <code><a href="/docs/linux/man/1-groffer/">groffer</a></code>(1), <code><a href="/docs/linux/man/1-grohtml/">grohtml</a></code>(1), and <code><a href="/docs/linux/man/1-grops/">grops</a></code>(1) commands use temporary files.</p>
<dt><i>GROFF_TYPESETTER</i></p>
<dd> Preset the default device. If this is not set the <code>ps</code> device is used as default. This device name is overwritten by the option <code>-T</code>.</dl>
<h2>EXAMPLES</h2>
<p> The following example illustrates the power of the <code>groff</code> program as a wrapper around <code>troff</code>. </p>
<p> To process a <i>roff</i> file using the preprocessors <code>tbl</code> and <code>pic</code> and the <code>me</code> macro set, classical <i>troff</i> had to be called by</p>
<dl>
<dt>
<dd> pic foo.me | tbl | troff -me -Tlatin1 | grotty</dl>
<p> Using <code>groff</code>, this pipe can be shortened to the equivalent command</p>
<dl>
<dt>
<dd> groff -p -t -me -T latin1 foo.me</dl>
<p> An even easier way to call this is to use <code><a href="/docs/linux/man/1-grog/">grog</a></code>(1) to guess the preprocessor and macro options and execute the generated command (by using backquotes to specify shell command substitution)</p>
<dl>
<dt>
<dd> `grog -Tlatin1 foo.me`</dl>
<p> The simplest way is to view the contents in an automated way by calling</p>
<dl>
<dt>
<dd> groffer foo.me</dl>
<h2>BUGS</h2>
<p> On EBCDIC hosts (e.g., OS/390 Unix), output devices <code>ascii</code> and <code>latin1</code> aren&#8217;t available. Similarly, output for EBCDIC code page <code>cp1047</code> is not available on ASCII based operating systems.</p>
<h2>INSTALLATION DIRECTORIES</h2>
<p> <i>groff</i> installs files in varying locations depending on its compile-time configuration. On this installation, the following locations are used.</p>
<dl>
<dt><i>/etc/X11/app-defaults</i></p>
<dd> Application defaults directory for <i><a href="/docs/linux/man/1-gxditview/">gxditview</a></i>(1).</p>
<dt><i>/usr/bin</i></p>
<dd> Directory containing <i>groff</i>&#8216;s executable commands.</p>
<dt><i>/usr/share/groff/1.22.4/eign</i></p>
<dd> List of common words for <i><a href="/docs/linux/man/1-indxbib/">indxbib</a></i>(1).</p>
<dt><i>/usr/share/groff/1.22.4</i></p>
<dd> Directory for data files.</p>
<dt><i>/usr/dict/papers/Ind</i></p>
<dd> Default index for <i><a href="/docs/linux/man/1-lkbib/">lkbib</a></i>(1) and <i><a href="/docs/linux/man/1-refer/">refer</a></i>(1).</p>
<dt><i>/usr/share/doc/groff-base</i></p>
<dd> Documentation directory.</p>
<dt><i>/usr/share/doc/groff-base/examples</i></p>
<dd> Example directory.</p>
<dt><i>/usr/share/groff/1.22.4/font</i></p>
<dd> Font directory.</p>
<dt><i>/usr/share/doc/groff-base/html</i></p>
<dd> HTML documentation directory.</p>
<dt><i>/usr/lib/font</i></p>
<dd> Legacy font directory.</p>
<dt><i>/usr/share/groff/site-font</i></p>
<dd> Local font directory.</p>
<dt><i>/usr/share/groff/site-tmac</i></p>
<dd> Local macro package (<i>tmac</i> file) directory.</p>
<dt><i>/usr/share/groff/1.22.4/tmac</i></p>
<dd> Macro package (<i>tmac</i> file) directory.</p>
<dt><i>/usr/share/groff/1.22.4/oldfont</i></p>
<dd> Font directory for compatibility with old versions of <i>groff</i>; see <i><a href="/docs/linux/man/1-grops/">grops</a></i>(1).</p>
<dt><i>/usr/share/doc/groff-base/pdf</i></p>
<dd> PDF documentation directory.</p>
<dt><i>/usr/lib/groff/site-tmac</i></p>
<dd> System macro package (<i>tmac</i> file) directory.</dl>
<h3>groff Macro Directory</h3>
<p> This contains all information related to macro packages. Note that more than a single directory is searched for those files as documented in <code><a href="/docs/linux/man/5-groff_tmac/">groff_tmac</a></code>(5). For the <i>groff</i> installation corresponding to this document, it is located at <i>/usr/share/groff/1.22.4/tmac</i>. The following files contained in the <i>groff macro directory</i> have a special meaning:</p>
<dl>
<dt><i>troffrc</i></p>
<dd> Initialization file for <i>troff</i>. This is interpreted by <code>troff</code> before reading the macro sets and any input.</p>
<dt><i>troffrc-end</i></p>
<dd> Final startup file for <i>troff</i>. It is parsed after all macro sets have been read.</p>
<dt>name<i>.tmac</i></p>
<dd> <i>tmac.</i>name Macro file for macro package <i>name</i>.</dl>
<h3>groff Font Directory</h3>
<p> This contains all information related to output devices. Note that more than a single directory is searched for those files; see <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1). For the <i>groff</i> installation corresponding to this document, it is located at <i>/usr/share/groff/1.22.4/font</i>. The following files contained in the <i>groff font directory</i> have a special meaning:</p>
<dl>
<dt><i>dev</i>name<i>/DESC</i></p>
<dd> Device description file for device <i>name</i>, see <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5).</p>
<dt><i>dev</i>name<i>/</i>F</p>
<dd> Font file for font <i>F</i> of device <i>name</i>.</dl>
<h2>AVAILABILITY</h2>
<p> Information on how to get <i>groff</i> and related information is available at the groff page of the GNU website </p>
<p> Three <i>groff</i> mailing lists are available:</p>
<dl>
<dt>
<dd> bug tracker activity (read-only)</p>
<dt>
<dd> general discussion and</p>
<dt>
<dd> commit activity (read-only) which reports changes to <i>groff</i>&#8216;s source code repository by its developers.</dl>
<p> Details on repository access and much more can be found in the file <i>README</i> at the top directory of the <i>groff</i> source package. </p>
<p> A free implementation of the <code>grap</code> preprocessor, written by Ted Faber can be found at the grap website This is the only <i>grap</i> supported by <i>groff</i>.</p>
<h2>AUTHORS</h2>
<p> <code>groff</code> was written by James Clark This document was rewritten, enhanced, and put under the FDL license in 2002 by Bernd Warken</p>
<h2>SEE ALSO</h2>
<p> <i>Groff: The GNU Implementation of troff</i>, by Trent A. Fisher and Werner Lemberg, is the primary <i>groff</i> manual. You can browse it interactively with &#8220;info groff&#8221;. </p>
<p> Due to its complex structure, the <i>groff</i> system has many man pages. They can be read with <code><a href="/docs/linux/man/1-man/">man</a></code>(1) or <code><a href="/docs/linux/man/1-groffer/">groffer</a></code>(1). </p>
<p> But there are special sections of <i>man pages</i>. <i>groff</i> has man pages in sections <code>1</code>,<code> 5</code>,<code>and</code> 7<code>.</code> When there are several <i>man pages</i> with the same name in the same <i>man</i> section, the one with the lowest section is should as first. The other man pages can be shown anyway by adding the section number as argument before the man page name. Reading the man page about the <i>groff</i> language is done by one of</p>
<dl>
<dt>
<dd>
<pre>
<code>man 7 groff</code>
<code>groffer 7 groff</code>
</pre>
</dl>
<dl>
<dt>Introduction, history and further readings:</p>
<dd> <code><a href="/docs/linux/man/7-roff/">roff</a></code>(7).</p>
<dt>Viewer for groff files:</p>
<dd> <code><a href="/docs/linux/man/1-groffer/">groffer</a></code>(1), <code><a href="/docs/linux/man/1-gxditview/">gxditview</a></code>(1), <code><a href="//www.systutorials.com/docs/linux/man/1x-xditview/">xditview</a></code>(1x).</p>
<dt>Wrapper programs for formatters:</p>
<dd> <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), <code><a href="/docs/linux/man/1-grog/">grog</a></code>(1).</p>
<dt>Roff preprocessors:</p>
<dd> <code><a href="/docs/linux/man/1-eqn/">eqn</a></code>(1), <code><a href="/docs/linux/man/1-grn/">grn</a></code>(1), <code><a href="/docs/linux/man/1-pic/">pic</a></code>(1), <code><a href="/docs/linux/man/1-chem/">chem</a></code>(1), <code><a href="/docs/linux/man/1-preconv/">preconv</a></code>(1), <code><a href="/docs/linux/man/1-refer/">refer</a></code>(1), <code><a href="/docs/linux/man/1-soelim/">soelim</a></code>(1), <code><a href="/docs/linux/man/1-tbl/">tbl</a></code>(1), <code><a href="/docs/linux/man/1-grap/">grap</a></code>(1).</p>
<dt>Roff language with the groff extensions:</p>
<dd> <code><a href="/docs/linux/man/7-groff/">groff</a></code>(7), <code><a href="/docs/linux/man/7-groff_char/">groff_char</a></code>(7), <code><a href="/docs/linux/man/7-groff_diff/">groff_diff</a></code>(7), <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5).</p>
<dt>Roff formatter programs:</p>
<dd> <code><a href="/docs/linux/man/1-nroff/">nroff</a></code>(1), <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1), <code><a href="/docs/linux/man/7-ditroff/">ditroff</a></code>(7).</p>
<dt>The intermediate output language:</p>
<dd> <code><a href="/docs/linux/man/7-groff_out/">groff_out</a></code>(7).</p>
<dt>Postprocessors for the output devices:</p>
<dd> <code><a href="/docs/linux/man/1-grodvi/">grodvi</a></code>(1), <code><a href="/docs/linux/man/1-grohtml/">grohtml</a></code>(1), <code><a href="/docs/linux/man/1-grolbp/">grolbp</a></code>(1), <code><a href="/docs/linux/man/1-grolj4/">grolj4</a></code>(1), <code><a href="/docs/linux/man/5-lj4_font/">lj4_font</a></code>(5), <code><a href="/docs/linux/man/1-grops/">grops</a></code>(1), <code><a href="/docs/linux/man/1-gropdf/">gropdf</a></code>(1), <code><a href="/docs/linux/man/1-grotty/">grotty</a></code>(1).</p>
<dt>Groff macro packages and macro-specific utilities:</p>
<dd> <code><a href="/docs/linux/man/5-groff_tmac/">groff_tmac</a></code>(5), <code><a href="/docs/linux/man/7-groff_man/">groff_man</a></code>(7), <code><a href="/docs/linux/man/7-groff_mdoc/">groff_mdoc</a></code>(7), <code><a href="/docs/linux/man/7-groff_me/">groff_me</a></code>(7), <code><a href="/docs/linux/man/7-groff_mm/">groff_mm</a></code>(7), <code><a href="/docs/linux/man/7-groff_mmse/">groff_mmse</a></code>(7) (only in Swedish locales), <code><a href="/docs/linux/man/7-groff_mom/">groff_mom</a></code>(7), <code><a href="/docs/linux/man/7-groff_ms/">groff_ms</a></code>(7), <code><a href="/docs/linux/man/7-groff_www/">groff_www</a></code>(7), <code><a href="/docs/linux/man/7-groff_trace/">groff_trace</a></code>(7), <code><a href="/docs/linux/man/7-mmroff/">mmroff</a></code>(7).</p>
<dt>The following utilities are available:</p>
<dd> <code><a href="/docs/linux/man/1-addftinfo/">addftinfo</a></code>(1), <code><a href="/docs/linux/man/1-afmtodit/">afmtodit</a></code>(1), <code><a href="/docs/linux/man/1-eqn2graph/">eqn2graph</a></code>(1), <code><a href="/docs/linux/man/1-gdiffmk/">gdiffmk</a></code>(1), <code><a href="/docs/linux/man/1-grap2graph/">grap2graph</a></code>(1), <code><a href="/docs/linux/man/1-groffer/">groffer</a></code>(1), <code><a href="/docs/linux/man/1-gxditview/">gxditview</a></code>(1), <code><a href="/docs/linux/man/1-hpftodit/">hpftodit</a></code>(1), <code><a href="/docs/linux/man/1-indxbib/">indxbib</a></code>(1), <code><a href="/docs/linux/man/1-lkbib/">lkbib</a></code>(1), <code><a href="/docs/linux/man/1-lookbib/">lookbib</a></code>(1), <code><a href="/docs/linux/man/1-pdfroff/">pdfroff</a></code>(1), <code><a href="/docs/linux/man/1-pfbtops/">pfbtops</a></code>(1), <code><a href="/docs/linux/man/1-pic2graph/">pic2graph</a></code>(1), <code><a href="/docs/linux/man/1-tfmtodit/">tfmtodit</a></code>(1), <code><a href="/docs/linux/man/1-xtotroff/">xtotroff</a></code>(1). </p>
</dl>
<h2>Index</h2>
