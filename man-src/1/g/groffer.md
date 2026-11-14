---
title: "groffer(1)"
name: "groffer"
section: "1"
letter: "g"
url: "/docs/linux/man/1-groffer/"
description: "groffer – display groff files and man pages on X and tty"
---

<h2 class="name">NAME</h2>
<p> groffer &#8211; display groff files and man pages on X and tty </p>
<h2>SYNOPSIS</h2>
<p> [<i>mode-option</i> &#8230; ] [<i>groff-option</i> &#8230; ] [<i>man-option</i> &#8230; ] [<i>X-option</i> &#8230; ] [ <code>&#8212;</code> ] [<i>filespec</i> &#8230; ] <code>-h</code> <code>&#8211;help</code> <code>-v</code> <code>&#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>groffer</code> program is the easiest way to use <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1). It can display arbitrary documents written in the <i>groff</i> language, see <code><a href="/docs/linux/man/7-groff/">groff</a></code>(7), or other <i>roff</i> languages, see <code><a href="/docs/linux/man/7-roff/">roff</a></code>(7), that are compatible to the original <i>troff</i> language. It finds and runs all necessary <i>groff</i> preprocessors, such as <code>chem</code>. </p>
<p> The <code>groffer</code> program also includes many of the features for finding and displaying the Unix manual pages (<i>man~pages</i>), such that it can be used as a replacement for a <code><a href="/docs/linux/man/1-man/">man</a></code>(1) program. Moreover, compressed files that can be handled by <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1) or <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1) are decompressed on-the-fly. </p>
<p> The normal usage is quite simple by supplying a file name or name of a <i>man~page</i> without further options. But the option handling has many possibilities for creating special behaviors. This can be done either in configuration files, with the shell environment variable <i>GROFFER_OPT</i>, or on the command line. </p>
<p> The output can be generated and viewed in several different ways available for <i>groff</i>. This includes the X Window System-based <i>groff</i> program <code><a href="/docs/linux/man/1-gxditview/">gxditview</a></code>(1), each <i>PostScript</i>, <i>PDF</i>, or <i>DVI</i> display program, a web browser by generating <i>HTML</i> or <i>XHTML</i> in <i>www~mode</i>, or several <i>text~modes</i> in text terminals. </p>
<p> Most of the options that must be named when running <code>groff</code> directly are determined automatically for <code>groffer</code>, due to the internal usage of the <code><a href="/docs/linux/man/1-grog/">grog</a></code>(1) program. But all parts can also be controlled manually by arguments. </p>
<p> Several file names can be specified on the command-line arguments. They are transformed into a single document in the normal way of <code>groff</code>. </p>
<p> Option handling is done in GNU style. Options and file names can be mixed freely. The option &#8220;<code>&#8212;</code>&#8221; closes the option handling, all following arguments are treated as file names. Long options can be abbreviated in several ways.</p>
<h2>OPTION OVERVIEW</h2>
<dl>
<dt><i>breaking options</i></p>
<dd>
<dl>
<dt>
<dd>
<p> [ <code>-h~</code>|<code>~&#8211;help</code> ] [ <code>-v~</code>|<code>~&#8211;version</code> ]</dl>
<dt><i>groffer mode options</i></p>
<dd>
<dl>
<dt>
<dd>
<p> [ <code>&#8211;auto</code> ] [ <code>&#8211;default</code> ] [ <code>&#8211;default-modes </code><i>mode1,mode2,&#8230; </i> ] [ <code>&#8211;dvi</code> ] [ <code>&#8211;groff</code> ] [ <code>&#8211;html</code> ] [ <code>&#8211;latin1</code> ] [ <code>&#8211;mode </code><i>display_mode</i> ] [ <code>&#8211;pdf</code> ] [ <code>&#8211;pdf2</code> ] [ <code>&#8211;ps</code> ] [ <code>&#8211;source</code> ] [ <code>&#8211;text</code> ] [ <code>&#8211;to-stdout</code> ] [ <code>&#8211;tty</code> ] [ <code>&#8211;utf8</code> ] [ <code>&#8211;viewer </code><i>prog</i> ] [ <code>&#8211;www</code> ] [ <code>&#8211;xhtml</code> ] [ <code>&#8211;x~</code>|<code>~&#8211;X</code> ]</dl>
<dt><i>options related to groff</i></p>
<dd>
<dl>
<dt>
<dd>
<p> [ <code>-T~</code>|<code>~&#8211;device </code><i>device</i> ] [ <code>-Z~</code>|<code>~&#8211;intermediate-output~</code>|<code>~&#8211;ditroff</code> ] </p>
<p> All further <code>groff</code> short options are accepted.</dl>
<dt><i>options for man~pages</i></p>
<dd>
<dl>
<dt>
<dd>
<p> [ <code>&#8211;apropos</code> ] [ <code>&#8211;apropos-data</code> ] [ <code>&#8211;apropos-devel</code> ] [ <code>&#8211;apropos-progs</code> ] [ <code>&#8211;man</code> ] [ <code>&#8211;no-man</code> ] [ <code>&#8211;no-special</code> ] [ <code>&#8211;whatis</code> ]</dl>
<dt><i>long options taken over from GNU man</i></p>
<dd>
<dl>
<dt>
<dd>
<p> [ <code>&#8211;all</code> ] [ <code>&#8211;ascii</code> ] [ <code>&#8211;ditroff</code> ] [ <code>&#8211;extension </code><i>suffix</i> ] [ <code>&#8211;locale </code><i>language</i> ] [ <code>&#8211;local-file</code> ] [ <code>&#8211;location~</code>|<code>~&#8211;where</code> ] [ <code>&#8211;manpath </code><i>dir1:dir2:&#8230; </i> ] [ <code>&#8211;no-location</code> ] [ <code>&#8211;pager </code><i>program</i> ] [ <code>&#8211;sections </code><i>sec1:sec2:&#8230; </i> ] [ <code>&#8211;systems </code><i>sys1,sys2,&#8230; </i> ] [ <code>&#8211;troff-device </code><i>device</i> ] </p>
<p> Further long options of GNU <code>man</code> are accepted as well.</dl>
<dt><i>options mapped to X Window System Toolkit Intrinsics options</i></p>
<dd>
<dl>
<dt>
<dd>
<p> [ <code>&#8211;bd~</code>|<code>~&#8211;bordercolor </code><i>pixels</i> ] [ <code>&#8211;bg~</code>|<code>~&#8211;background </code><i>color</i> ] [ <code>&#8211;bw~</code>|<code>~&#8211;borderwidth </code><i>pixels</i> ] [ <code>&#8211;display </code><i>X-display</i> ] [ <code>&#8211;fg~</code>|<code>~&#8211;foreground </code><i>color</i> ] [ <code>&#8211;fn~</code>|<code>~&#8211;ft~</code>|<code>~&#8211;font </code><i>font_name</i> ] [ <code>&#8211;geometry </code><i>size_pos</i> ] [ <code>&#8211;resolution </code><i>value</i> ] [ <code>&#8211;rv</code> ] [ <code>&#8211;title </code><i>string</i> ] [ <code>&#8211;xrm </code><i>X-resource</i> ]</dl>
<dt><i>options for development</i></p>
<dd>
<dl>
<dt>
<dd>
<p> [ <code>&#8211;debug</code> ] [ <code>&#8211;debug-filenames</code> ] [ <code>&#8211;debug-grog</code> ] [ <code>&#8211;debug-keep</code> ] [ <code>&#8211;debug-params</code> ] [ <code>&#8211;debug-tmpdir</code> ] [ <code>&#8211;do-nothing</code> ] [ <code>&#8211;print </code><i>text</i> ] [ <code>-V</code> ]</dl>
<dt><i>filespec arguments</i></p>
<dd>
<dl>
<dt>
<dd>
<p> The <i>filespec</i> parameters are all arguments that are neither an option nor an option argument. They usually mean a file name or a <i>man page</i> searching scheme. </p>
<p> In the following, the term <i>section_extension</i> is used. It means a word that consists of a <i>man section</i> that is optionally followed by an <i>extension</i>. The name of a <i>man section</i> is a single character from <code>[1-9on]</code>, the <i>extension</i> is some word. The <i>extension</i> is mostly lacking. </p>
<p> No <i>filespec</i> parameters means standard input.</p>
<dl>
<dt><code>&#8211;</code></p>
<dd> stands for standard input (can occur several times).</p>
<dt><i>filename</i></p>
<dd> the path name of an existing file.</p>
<dt><code>man:</code><i>name</i><code>(</code><i>section_extension</i><code>)</code></p>
<dd> <code>man:</code><i>name</i><code>.</code><i>section_extension</i> <i>name</i><code>(</code><i>section_extension</i><code>)</code> <i>name</i><code>.</code><i>section_extension</i> <i>section_extension name</i> search the man~page <i>name</i> in the section with optional extension <i>section_extension</i>.</p>
<dt><code>man:</code><i>name</i></p>
<dd> man~page in the lowest <i>man~section</i> that has <i>name</i>.</p>
<dt><i>name</i></p>
<dd> if <i>name</i> is not an existing file search for the man~page <i>name</i> in the lowest man~section.</dl>
</dl>
</dl>
<h2>OPTION DETAILS</h2>
<p> The <code>groffer</code> program can usually be run with very few options. But for special purposes, it supports many options. These can be classified in 5 option classes. </p>
<p> All short options of <code>groffer</code> are compatible with the short options of <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1). All long options of <code>groffer</code> are compatible with the long options of <code><a href="/docs/linux/man/1-man/">man</a></code>(1). </p>
<p> Arguments for long option names can be abbreviated in several ways. First, the argument is checked whether it can be prolonged as is. Furthermore, each minus sign <code>&#8211;</code> is considered as a starting point for a new abbreviation. This leads to a set of multiple abbreviations for a single argument. For example, <code>&#8211;de-n-f</code> can be used as an abbreviation for <code>&#8211;debug-not-func</code>, but <code>&#8211;de-n</code> works as well. If the abbreviation of the argument leads to several resulting options an error is raised. </p>
<p> These abbreviations are only allowed in the environment variable <i>GROFFER_OPT</i>, but not in the configuration files. In configuration, all long options must be exact.</p>
<h3>groffer breaking Options</h3>
<p> As soon as one of these options is found on the command line it is executed, printed to standard output, and the running <code>groffer</code> is terminated thereafter. All other arguments are ignored.</p>
<dl>
<dt><code>-h~</code>|<code>~&#8211;help</code></p>
<dd> Print help information with a short explanation of options to standard output.</p>
<dt><code>-v~</code>|<code>~&#8211;version</code></p>
<dd> Print version information to standard output.</dl>
<h3>groffer Mode Options</h3>
<p> The display mode and the viewer programs are determined by these options. If none of these mode and viewer options is specified <code>groffer</code> tries to find a suitable display mode automatically. The default modes are <i>mode pdf</i>, <i>mode ps</i>, <i>mode html</i>, <i>mode xhtml</i>, <i>mode x</i>, and <i>mode dvi</i> in the X Window System with different viewers and <i>mode tty</i> with device <i>utf8</i> under <code>less</code> on a terminal; other modes are tested if the programs for the main default mode do not exist. </p>
<p> In the X Window System, many programs create their own window when called. <code>groffer</code> can run these viewers as an independent program in the background. As this does not work in text mode on a terminal (tty) there must be a way to know which viewers are X Window System-based graphical programs. The <code>groffer</code> script has a small amount of information on some viewer names. If a viewer argument of the command-line chooses an element that is recognized as an X Window System-based program in this list, it is treated as a viewer that can run in the background. Unrecognized viewers are not run in the background. </p>
<p> For each mode, you are free to choose whatever viewer you want. That need not be some graphical viewer suitable for this mode. There is a chance to view the output source; for example, the combination of the options <code>&#8211;mode=ps</code> and <code>&#8211;viewer=less</code> shows the content of the <i>PostScript</i> output, the source code, with the pager <code>less</code>.</p>
<dl>
<dt><code>&#8211;auto</code></p>
<dd> Equivalent to <code>&#8211;mode=auto</code>.</p>
<dt><code>&#8211;default</code></p>
<dd> Reset all configuration from previously processed command-line options to the default values. This is useful to wipe out all former options of the configuration, in <i>GROFFER_OPT</i>, and restart option processing using only the rest of the command line.</p>
<dt><code>&#8211;default-modes</code><i>&nbsp;mode1,mode2,&#8230; </i></p>
<dd> Set the sequence of modes for <i>auto~mode</i> to the comma separated list given in the argument. See <code>&#8211;mode</code> for details on modes. Display in the default manner; actually, this means to try the modes <i>x</i>, <i>ps</i>, and <i>tty</i> in this sequence.</p>
<dt><code>&#8211;dvi</code></p>
<dd> Equivalent to <code>&#8211;mode=dvi</code>. Known <i>DVI</i> viewers for the X Window System include <code><a href="/docs/linux/man/1-xdvi/">xdvi</a></code>(1) and <code><a href="/docs/linux/man/1-dvilx/">dvilx</a></code>(1).</p>
<dt><code>&#8211;groff</code></p>
<dd> Equivalent to <code>&#8211;mode=groff</code>.</p>
<dt><code>&#8211;html</code></p>
<dd> Equivalent to <code>&#8211;mode=html</code>.</p>
<dt><code>&#8211;mode</code><i>&nbsp;value</i></p>
<dd> Set the display mode. The following mode values are recognized:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>auto</code></p>
<dd> Select the automatic determination of the display mode. The sequence of modes that are tried can be set with the <code>&#8211;default-modes</code> option. Useful for restoring the <i>default~mode</i> when a different mode was specified before.</p>
<dt><code>dvi</code></p>
<dd> Display formatted input in a <i>DVI</i> viewer program. By default, the formatted input is displayed with the <code><a href="/docs/linux/man/1-xdvi/">xdvi</a></code>(1) program.</p>
<dt><code>groff</code></p>
<dd> After the file determination, switch <code>groffer</code> to process the input like <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1) would do. This disables the <i>groffer</i> viewing features.</p>
<dt><code>html</code></p>
<dd> Translate the input into HTML format and display the result in a web browser program. By default, the existence of a sequence of standard web browsers is tested, starting with <code><a href="/docs/linux/man/1-konqueror/">konqueror</a></code>(1) and <code><a href="/docs/linux/man/1-mozilla/">mozilla</a></code>(1). The text HTML viewer is <code><a href="/docs/linux/man/1-lynx/">lynx</a></code>(1). By default, the existence of a sequence of standard web browsers is tested, starting with <code><a href="/docs/linux/man/1-konqueror/">konqueror</a></code>(1) and <code><a href="/docs/linux/man/1-mozilla/">mozilla</a></code>(1). The text HTML viewer is <code><a href="/docs/linux/man/1-lynx/">lynx</a></code>(1).</p>
<dt><code>pdf</code></p>
<dd> Transform <i>roff input files</i> into a <i>PDF file</i> by using the <code>groff (1)</code> device <code>-Tpdf</code>. This is the default <code>PDF</code> generator. The generated <i>PDF file</i> is displayed with suitable viewer programs, such as <code><a href="/docs/linux/man/1-okular/">okular</a></code>(1).</p>
<dt><code>pdf2</code></p>
<dd> This is the traditional <i>pdf mode</i>. Sometimes this mode produces more correct output than the default <code>PDF mode</code>. By default, the input is formatted by <code>groff</code> using the PostScript device, then it is transformed into the PDF file format using <code><a href="/docs/linux/man/1-gs/">gs</a></code>(1), or <code><a href="/docs/linux/man/1-ps2pdf/">ps2pdf</a></code>(1). If that&#8217;s not possible, the <i>PostScript mode (ps)</i> is used instead. Finally it is displayed using different viewer programs.</p>
<dt><code>ps</code></p>
<dd> Display formatted input in a PostScript viewer program. By default, the formatted input is displayed in one of many viewer programs.</p>
<dt><code>text</code></p>
<dd> Format in a <i>groff~text~mode</i> and write the result to standard output without a pager or viewer program. The text device, <i>latin1</i> by default, can be chosen with option <code>-T</code>.</p>
<dt><code>tty</code></p>
<dd> Format in a <i>groff~text~mode</i> and write the result to standard output using a text pager program, even when in the X Window System.</p>
<dt><code>www</code></p>
<dd> Equivalent to <code>&#8211;mode=html</code>.</p>
<dt><code>x</code></p>
<dd> Display the formatted input in a native <i>roff</i> viewer. By default, the formatted input is displayed with the <code><a href="/docs/linux/man/1-gxditview/">gxditview</a></code>(1) program being distributed together with <code>groff</code>. But the legacy X Window System application <code><a href="/docs/linux/man/1-xditview/">xditview</a></code>(1) can also be chosen with the option <code>&#8211;viewer</code>. The default resolution is <code>75dpi</code>, but <code>100dpi</code> are also possible. The default <i>groff</i> device for the resolution of <code>75dpi</code> is <code>X75-12</code>, for <code>100dpi</code> it is <code>X100</code>. The corresponding <i>groff intermediate output</i> for the actual device is generated and the result is displayed. For a resolution of <code>100dpi</code>, the default width of the geometry of the display program is chosen to <code>850dpi</code>.</p>
<dt><code>X</code></p>
<dd> Equivalent to <code>&#8211;mode=x</code>.</p>
<dt><code>xhtml</code></p>
<dd> Translate the input into <i>XHTML</i> format, which is an <i>XML</i> version of <i>HTML</i>. Then display the result in a web browser program, mostly the known <i>HTML viewers</i>.</dl>
<p> The following modes do not use the <i>groffer</i> viewing features. They are only interesting for advanced applications.</p>
<dl>
<dt><code>groff</code></p>
<dd> Generate device output with plain <i>groff</i> without using the special viewing features of <i>groffer</i>. If no device was specified by option <code>-T</code> the <i>groff</i> default <code>ps</code> is assumed.</p>
<dt><code>source</code></p>
<dd> Output the roff source code of the input files without further processing.</dl>
</dl>
<dt><code>&#8211;pdf</code></p>
<dd> Equivalent to <code>&#8211;mode=pdf</code>. <code>&#8211;pdf2</code> Equivalent to <code>&#8211;mode=pdf2</code>.</p>
<dt><code>&#8211;ps</code></p>
<dd> Equivalent to <code>&#8211;mode=ps</code>. Common PostScript viewers include <code><a href="/docs/linux/man/1-okular/">okular</a></code>(1), <code><a href="/docs/linux/man/1-evince/">evince</a></code>(1), <code><a href="/docs/linux/man/1-gv/">gv</a></code>(1), <code><a href="/docs/linux/man/1-ghostview/">ghostview</a></code>(1), and <code><a href="/docs/linux/man/1-gs/">gs</a></code>(1), In each case, arguments can be provided additionally.</p>
<dt><code>&#8211;source</code></p>
<dd> Equivalent to <code>&#8211;mode=source</code>.</p>
<dt><code>&#8211;text</code></p>
<dd> Equivalent to <code>&#8211;mode=text</code>.</p>
<dt><code>&#8211;to-stdout</code></p>
<dd> The file for the chosen mode is generated and its content is printed to standard output. It will not be displayed in graphical mode.</p>
<dt><code>&#8211;tty</code></p>
<dd> Equivalent to <code>&#8211;mode=tty</code>. The standard pager is <code><a href="/docs/linux/man/1-less/">less</a></code>(1). This option is equivalent to <i>man</i> option <code>&#8211;pager=,</code><i>prog</i>. The option argument can be a file name or a program to be searched in <i>$PATH</i>; arguments can be provided additionally.</p>
<dt><code>&#8211;viewer</code><i>&nbsp;prog</i></p>
<dd> Choose a viewer program for actual device or mode. This can be a file name or a program to be searched in <i>$PATH</i>; arguments can be provided additionally.</p>
<dt><code>&#8211;www</code></p>
<dd> Equivalent to <code>&#8211;mode=html</code>.</p>
<dt><code>&#8211;X~</code>|<code>~&#8211;x</code></p>
<dd> Equivalent to <code>&#8211;mode=x</code>. Suitable viewer programs are <code><a href="/docs/linux/man/1-gxditview/">gxditview</a></code>(1) which is the default and <code><a href="/docs/linux/man/1-xditview/">xditview</a></code>(1).</p>
<dt><code>&#8212;</code></p>
<dd> Signals the end of option processing; all remaining arguments are interpreted as <i>filespec</i> parameters.</dl>
<p> Besides these, <code>groffer</code> accepts all short options that are valid for the <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1) program. All non-<code>groffer</code> options are sent unmodified via <code>grog</code> to <code>groff</code>. So postprocessors, macro packages, compatibility with <i>classical</i> <i>troff</i>, and much more can be manually specified.</p>
<h3>Options related to groff</h3>
<p> All short options of <code>groffer</code> are compatible with the short options of <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1). The following of <code>groff</code> options have either an additional special meaning within <code>groffer</code> or make sense for normal usage. </p>
<p> Because of the special outputting behavior of the <code>groff</code> option <code>-Z</code> <code>groffer</code> was designed to be switched into <i>groff~mode</i>; the <i>groffer</i> viewing features are disabled there. The other <code>groff</code> options do not switch the mode, but allow to customize the formatting process.</p>
<dl>
<dt><code>&#8211;a</code></p>
<dd> This generates an ASCII approximation of output in the <i>text~modes</i>. That could be important when the text pager has problems with control sequences in <i>tty mode</i>.</p>
<dt><code>&#8211;m</code><i>&nbsp;file</i></p>
<dd> Add <i>file</i> as a <i>groff</i> macro file. This is useful in case it cannot be recognized automatically.</p>
<dt><code>&#8211;P</code><i>&nbsp;opt_or_arg</i></p>
<dd> Send the argument <i>opt_or_arg</i> as an option or option argument to the actual <code>groff</code> postprocessor.</p>
<dt><code>&#8211;T </code><i>devname</i>~|<code>~&#8211;device </code><i>devname</i></p>
<dd> This option determines <code>groff</code>&#8216;s output device. The most important devices are the text output devices for referring to the different character sets, such as <code>ascii</code>, <code>utf8</code>, <code>latin1</code>, <code>utf8</code>, and others. Each of these arguments switches <code>groffer</code> into a <i>text~mode</i> using this device, to <i>mode~tty</i> if the actual mode is not a <i>text~mode</i>. The following <i>devname</i> arguments are mapped to the corresponding <code>groffer</code> <code>&#8211;mode=,</code><i>devname</i> option: <code>dvi</code>, <code>html</code>, <code>xhtml</code>, and <code>ps</code>. All <code>X*</code> arguments are mapped to <i>mode~x</i>. Each other <i>devname</i> argument switches to <i>mode~groff</i> using this device.</p>
<dt><code>&#8211;X</code></p>
<dd> is equivalent to <code>groff -X</code>. It displays the <i>groff intermediate output</i> with <code>gxditview</code>. As the quality is relatively bad this option is deprecated; use <code>&#8211;X</code> instead because the <i>x~mode</i> uses an <i>X</i>* device for a better display.</p>
<dt><code>-Z~</code>|<code>~&#8211;intermediate-output~</code>|<code>~&#8211;ditroff</code></p>
<dd> Switch into <i>groff~mode</i> and format the input with the <i>groff intermediate output</i> without postprocessing; see <code><a href="/docs/linux/man/5-groff_out/">groff_out</a></code>(5). This is equivalent to option <code>&#8211;ditroff</code> of <i>man</i>, which can be used as well.</dl>
<p> All other <code>groff</code> options are supported by <code>groffer</code>, but they are just transparently transferred to <code>groff</code> without any intervention. The options that are not explicitly handled by <code>groffer</code> are transparently passed to <code>groff</code>. Therefore these transparent options are not documented here, but in <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1). Due to the automatism in <code>groffer</code>, none of these <code>groff</code> options should be needed, except for advanced usage.</p>
<h3>Options for man~pages</h3>
<dl>
<dt><code>&#8211;apropos</code></p>
<dd> Start the <code><a href="/docs/linux/man/1-apropos/">apropos</a></code>(1) command or facility of <code><a href="/docs/linux/man/1-man/">man</a></code>(1) for searching the <i>filespec</i> arguments within all <i>man~page</i> descriptions. Each <i>filespec</i> argument is taken for search as it is; <i>section</i> specific parts are not handled, such that <code>7 groff</code> searches for the two arguments <code>7</code> and <code>groff</code>, with a large result; for the <i>filespec</i> <code>groff.7</code> nothing will be found. The <i>language</i> locale is handled only when the called programs do support this; the GNU <code>apropos</code> and <code>man -k</code> do not. The display differs from the <code>apropos</code> program by the following concepts:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> Construct a <i>groff</i> frame similar to a <i>man~page</i> to the output of <code>apropos</code>,</p>
<dt>*</p>
<dd> each <i>filespec</i> argument is searched on its own.</p>
<dt>*</p>
<dd> The restriction by <code>&#8211;sections</code> is handled as well,</p>
<dt>*</p>
<dd> wildcard characters are allowed and handled without a further option.</dl>
</dl>
<dt><code>&#8211;apropos-data</code></p>
<dd> Show only the <code>apropos</code> descriptions for data documents, these are the <code><a href="/docs/linux/man/7-man/">man</a></code>(7) <i>sections~4</i>, <i>5</i>, and <i>7</i>. Direct <i>section</i> declarations are ignored, wildcards are accepted.</p>
<dt><code>&#8211;apropos-devel</code></p>
<dd> Show only the <code>apropos</code> descriptions for development documents, these are the <code><a href="/docs/linux/man/7-man/">man</a></code>(7) <i>sections~2</i>, <i>3</i>, and <i>9</i>. Direct <i>section</i> declarations are ignored, wildcards are accepted.</p>
<dt><code>&#8211;apropos-progs</code></p>
<dd> Show only the <code>apropos</code> descriptions for documents on programs, these are the <code><a href="/docs/linux/man/7-man/">man</a></code>(7) <i>sections~1</i>, <i>6</i>, and <i>8</i>. Direct <i>section</i> declarations are ignored, wildcards are accepted.</p>
<dt><code>&#8211;whatis</code></p>
<dd> For each <i>filespec</i> argument search all <i>man~pages</i> and display their description &#8212; or say that it is not a <i>man~page</i>. This is written from anew, so it differs from <i>man</i>&#8216;s <code>whatis</code> output by the following concepts</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> each retrieved file name is added,</p>
<dt>*</p>
<dd> local files are handled as well,</p>
<dt>*</p>
<dd> the <i>language</i> and <i>system</i> locale is supported,</p>
<dt>*</p>
<dd> the display is framed by a <i>groff</i> output format similar to a <i>man~page</i>,</p>
<dt>*</p>
<dd> wildcard characters are allowed without a further option.</dl>
</dl>
</dl>
<p> The following options were added to <code>groffer</code> for choosing whether the file name arguments are interpreted as names for local files or as a search pattern for <i>man~pages</i>. The default is looking up for local files.</p>
<dl>
<dt><code>&#8211;man</code></p>
<dd> Check the non-option command-line arguments (<i>filespecs</i>) first on being <i>man~pages</i>, then whether they represent an existing file. By default, a <i>filespec</i> is first tested whether it is an existing file.</p>
<dt><code>&#8211;no-man~</code>|<code>~&#8211;local-file</code></p>
<dd> Do not check for <i>man~pages</i>. <code>&#8211;local-file</code> is the corresponding <code>man</code> option.</p>
<dt><code>&#8211;no-special</code></p>
<dd> Disable former calls of <code>&#8211;all</code>, <code>&#8211;apropos*</code>, and <code>&#8211;whatis</code>.</dl>
<h3>Long options taken over from GNU man</h3>
<p> The long options of <code>groffer</code> were synchronized with the long options of GNU <code>man</code>. All long options of GNU <code>man</code> are recognized, but not all of these options are important to <code>groffer</code>, so most of them are just ignored. These ignored <code>man</code> options are <code>&#8211;catman</code>, <code>&#8211;troff</code>, and <code>&#8211;update</code>. </p>
<p> In the following, the <code>man</code> options that have a special meaning for <code>groffer</code> are documented. </p>
<p> If your system has GNU <code>man</code> installed the full set of long and short options of the GNU <code>man</code> program can be passed via the environment variable <i>MANOPT</i>; see <code><a href="/docs/linux/man/1-man/">man</a></code>(1).</p>
<dl>
<dt><code>&#8211;all</code></p>
<dd> In searching <i>man~pages</i>, retrieve all suitable documents instead of only one.</p>
<dt><code>-7~</code>|<code>~&#8211;ascii</code></p>
<dd> In <i>text~modes</i>, display ASCII translation of special characters for critical environment. This is equivalent to <code>groff -mtty_char</code>; see <code><a href="/docs/linux/man/5-groff_tmac/">groff_tmac</a></code>(5).</p>
<dt><code>&#8211;ditroff</code></p>
<dd> Produce <i>groff intermediate output</i>. This is equivalent to <code>groffer</code> <code>-Z</code>.</p>
<dt><code>&#8211;extension</code><i>&nbsp;suffix</i></p>
<dd> Restrict <i>man~page</i> search to file names that have <i>suffix</i> appended to their section element. For example, in the file name <i>/usr/share/man/man3/terminfo.3ncurses.gz</i> the <i>man~page</i> extension is <i>ncurses</i>.</p>
<dt><code>&#8211;locale</code><i>&nbsp;language</i></p>
<dd> Set the language for <i>man~pages</i>. This has the same effect, but overwrites <i>$LANG</i>.</p>
<dt><code>&#8211;location</code></p>
<dd> Print the location of the retrieved files to standard error.</p>
<dt><code>&#8211;no-location</code></p>
<dd> Do not display the location of retrieved files; this resets a former call to <code>&#8211;location</code>. This was added by <code>groffer</code>.</p>
<dt><code>&#8211;manpath</code><i>&nbsp;&#8216;dir1:dir2:&#8230; &#8216;</i></p>
<dd> Use the specified search path for retrieving <i>man~pages</i> instead of the program defaults. If the argument is set to the empty string &quot;&quot; the search for <i>man~page</i> is disabled.</p>
<dt><code>&#8211;pager</code></p>
<dd> Set the pager program in <i>tty~mode</i>; default is <code>less</code>. This can be set with <code>&#8211;viewer</code>.</p>
<dt><code>&#8211;sections</code><i>&nbsp;sec1:sec2:&#8230; </i></p>
<dd> Restrict searching for <i>man~pages</i> to the given <i>sections</i>, a colon-separated list.</p>
<dt><code>&#8211;systems</code><i>&nbsp;sys1,sys2,&#8230; </i></p>
<dd> Search for <i>man~pages</i> for the given operating systems; the argument <i>systems</i> is a comma-separated list.</p>
<dt><code>&#8211;where</code></p>
<dd> Equivalent to <code>&#8211;location</code>.</dl>
<h3>X Window System Toolkit Intrinsics Options</h3>
<p> The following long options were adapted from the corresponding X Window System Toolkit Intrinsics options. <code>groffer</code> will pass them to the actual viewer program if it is an X Window System program. Otherwise these options are ignored. </p>
<p> Unfortunately these options use the old style of a single minus for long options. For <code>groffer</code> that was changed to the standard with using a double minus for long options, for example, <code>groffer</code> uses the option <code>&#8211;font</code> for the X Window System Toolkit Intrinsics option <code>-font</code>. </p>
<p> See <code><a href="/docs/linux/man/7-x/">X</a></code>(7) and the manual <i>X Toolkit Intrinsics &#8211; C Language Interface</i> for more details on these options and their arguments.</p>
<dl>
<dt><code>&#8211;background</code><i>&nbsp;color</i></p>
<dd> Set the background color of the viewer window.</p>
<dt><code>&#8211;bd</code><i>&nbsp;pixels</i></p>
<dd> This is equivalent to <code>&#8211;bordercolor</code>.</p>
<dt><code>&#8211;bg</code><i>&nbsp;color</i></p>
<dd> This is equivalent to <code>&#8211;background</code>.</p>
<dt><code>&#8211;bw</code><i>&nbsp;pixels</i></p>
<dd> This is equivalent to <code>&#8211;borderwidth</code>.</p>
<dt><code>&#8211;bordercolor</code><i>&nbsp;pixels</i></p>
<dd> Specifies the color of the border surrounding the viewer window.</p>
<dt><code>&#8211;borderwidth</code><i>&nbsp;pixels</i></p>
<dd> Specifies the width in pixels of the border surrounding the viewer window.</p>
<dt><code>&#8211;display</code><i>&nbsp;X-display</i></p>
<dd> Set the X Window System display on which the viewer program shall be started. See section &#8220;Display Names&#8221; in <code><a href="/docs/linux/man/7-x/">X</a></code>(7) for the syntax of the argument.</p>
<dt><code>&#8211;foreground</code><i>&nbsp;color</i></p>
<dd> Set the foreground color of the viewer window.</p>
<dt><code>&#8211;fg</code><i>&nbsp;color</i></p>
<dd> This is equivalent to <code>&#8211;foreground</code>.</p>
<dt><code>&#8211;fn</code><i>&nbsp;font_name</i></p>
<dd> This is equivalent to <code>&#8211;font</code>.</p>
<dt><code>&#8211;font</code><i>&nbsp;font_name</i></p>
<dd> Set the font used by the viewer window. The argument is an X Window System font name.</p>
<dt><code>&#8211;ft</code><i>&nbsp;font_name</i></p>
<dd> This is equivalent to <code>&#8211;font</code>.</p>
<dt><code>&#8211;geometry</code><i>&nbsp;size_pos</i></p>
<dd> Set the geometry of the display window, that means its size and its starting position. See section &#8220;Geometry Specifications&#8221; in <code><a href="/docs/linux/man/7-x/">X</a></code>(7) for the syntax of the argument.</p>
<dt><code>&#8211;resolution</code><i>&nbsp;value</i></p>
<dd> Set X Window System resolution in dpi (dots per inch) in some viewer programs. The only supported dpi values are <code>75</code> and <code>100</code>. Actually, the default resolution for <code>groffer</code> is set to <code>75dpi</code>. The resolution also sets the default device in <i>mode x</i>.</p>
<dt><code>&#8211;rv</code></p>
<dd> Reverse foreground and background color of the viewer window.</p>
<dt><code>&#8211;title</code><i>&nbsp;&#8216;some text&#8217;</i></p>
<dd> Set the title for the viewer window.</p>
<dt><code>&#8211;xrm</code><i>&nbsp;&#8216;resource&#8217;</i></p>
<dd> Set the X Window System server resource to the given value.</dl>
<h3>Options for Development</h3>
<dl>
<dt><code>&#8211;debug</code></p>
<dd> Enable all debugging options <code>&#8211;debug-,</code><i>type</i>. The temporary files are kept and not deleted, the <code>grog</code> output is printed, the name of the temporary directory is printed, the displayed file names are printed, and the parameters are printed.</p>
<dt><code>&#8211;debug-filenames</code></p>
<dd> Print the names of the files and <i>man~pages</i> that are displayed by <code>groffer</code>.</p>
<dt><code>&#8211;debug-grog</code></p>
<dd> Print the output of all <code>grog</code> commands.</p>
<dt><code>&#8211;debug-keep</code></p>
<dd> Enable two debugging informations. Print the name of the temporary directory and keep the temporary files, do not delete them during the run of <code>groffer</code>.</p>
<dt><code>&#8211;debug-params</code></p>
<dd> Print the parameters, as obtained from the configuration files, from <i>GROFFER_OPT</i>, and the command-line arguments.</p>
<dt><code>&#8211;debug-tmpdir</code></p>
<dd> Print the name of the temporary directory.</p>
<dt><code>&#8211;do-nothing</code></p>
<dd> This is like <code>&#8211;version</code>, but without the output; no viewer is started. This makes only sense in development.</p>
<dt><code>&#8211;print=,</code><i>text</i></p>
<dd> Just print the argument to standard error. This is good for parameter check.</p>
<dt><code>-V</code></p>
<dd> This is an advanced option for debugging only. Instead of displaying the formatted input, a lot of <i>groffer</i> specific information is printed to standard output:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> the output file name in the temporary directory,</p>
<dt>*</p>
<dd> the display mode of the actual <code>groffer</code> run,</p>
<dt>*</p>
<dd> the display program for viewing the output with its arguments,</p>
<dt>*</p>
<dd> the active parameters from the config files, the arguments in <i>GROFFER_OPT</i>, and the arguments of the command line,</p>
<dt>*</p>
<dd> the pipeline that would be run by the <code>groff</code> program, but without executing it.</dl>
</dl>
</dl>
<p> Other useful debugging options are the <code>groff</code> option <code>-Z</code> and <code>&#8211;mode=groff</code>.</p>
<h3>Filespec Arguments</h3>
<p> A <i>filespec</i> parameter is an argument that is not an option or option argument. In <code>groffer</code>, <i>filespec</i> parameters are a file name or a template for searching <i>man~pages</i>. These input sources are collected and composed into a single output file such as <code>groff</code> does. </p>
<p> The strange POSIX behavior to regard all arguments behind the first non-option argument as <i>filespec</i> arguments is ignored. The GNU behavior to recognize options even when mixed with <i>filespec</i> arguments is used throughout. But, as usual, the double minus argument <code>&#8212;</code> ends the option handling and interprets all following arguments as <i>filespec</i> arguments; so the POSIX behavior can be easily adopted. </p>
<p> The options <code>&#8211;apropos*</code> have a special handling of <i>filespec</i> arguments. Each argument is taken as a search scheme of its own. Also a regexp (regular expression) can be used in the filespec. For example, <code>groffer &#8211;apropos &#8216;^gro.f$&#8217;</code> searches <code>groff</code> in the <i>man~page</i> name, while <code>groffer &#8211;apropos groff</code> searches <code>groff</code> somewhere in the name or description of the <i>man~pages</i>. </p>
<p> All other parts of <i>groffer</i>, such as the normal display or the output with <code>&#8211;whatis</code> have a different scheme for <i>filespecs</i>. No regular expressions are used for the arguments. The <i>filespec</i> arguments are handled by the following scheme. </p>
<p> It is necessary to know that on each system the <i>man~pages</i> are sorted according to their content into several sections. The <i>classical man sections</i> have a single-character name, either a digit from <code>1</code> to <code>9</code> or one of the characters <code>n</code> or <code>o</code>. </p>
<p> This can optionally be followed by a string, the so-called <i>extension</i>. The <i>extension</i> allows the storage of several <i>man~pages</i> with the same name in the same <i>section</i>. But the <i>extension</i> is only rarely used; usually it is omitted. Then the <i>extensions</i> are searched automatically by alphabet. </p>
<p> In the following, we use the name <i>section_extension</i> for a word that consists of a single character <i>section</i> name or a <i>section</i> character that is followed by an <i>extension</i>. Each <i>filespec</i> parameter can have one of the following forms in decreasing sequence.</p>
<dl>
<dt>*</p>
<dd> No <i>filespec</i> parameters means that <code>groffer</code> waits for standard input. The minus option <code>&#8211;</code> always stands for standard input; it can occur several times. If you want to look up a <i>man~page</i> called <code>&#8211;</code> use the argument <code>man:-</code>.</p>
<dt>*</p>
<dd> Next a <i>filespec</i> is tested whether it is the path name of an existing file. Otherwise it is assumed to be a searching pattern for a <i>man~page</i>.</p>
<dt>*</p>
<dd> <code>man:</code><i>name</i><code>(</code><i>section_extension</i><code>)</code><i>,</i> <code>man:</code><i>name</i><code>.</code><i>section_extension,</i> <i>name</i><code>(</code><i>section_extension</i><code>)</code><i>,</i> or <i>name</i><code>.</code><i>section_extension</i> search the man~page <i>name</i> in man~section and possibly extension of <i>section_extension</i>.</p>
<dt>*</p>
<dd> Now <code>man:</code><i>name</i> searches for a <i>man~page</i> in the lowest <i>man~section</i> that has a document called <i>name</i>.</p>
<dt>*</p>
<dd> <i>section_extension~name</i> is a pattern of 2 arguments that originates from a strange argument parsing of the <code>man</code> program. Again, this searches the man page <i>name</i> with <i>section_extension</i>, a combination of a <i>section</i> character optionally followed by an <i>extension</i>.</p>
<dt>*</p>
<dd> We are left with the argument <i>name</i> which is not an existing file. So this searches for the <i>man~page</i> called <i>name</i> in the lowest <i>man~section</i> that has a document for this name.</dl>
<p> Several file name arguments can be supplied. They are mixed by <code>groff</code> into a single document. Note that the set of option arguments must fit to all of these file arguments. So they should have at least the same style of the <i>groff</i> language.</p>
<h2>OUTPUT MODES</h2>
<p> By default, the <code>groffer</code> program collects all input into a single file, formats it with the <code>groff</code> program for a certain device, and then chooses a suitable viewer program. The device and viewer process in <code>groffer</code> is called a <i>mode</i>. The mode and viewer of a running <code>groffer</code> program is selected automatically, but the user can also choose it with options. The modes are selected by option the arguments of <code>&#8211;mode=,</code><i>anymode</i>. Additionally, each of this argument can be specified as an option of its own, such as <code>anymode</code>. Most of these modes have a viewer program, which can be chosen by the option <code>&#8211;viewer</code>. </p>
<p> Several different modes are offered: graphical modes for the X Window System, <i>text~modes</i>, and some direct <i>groff~modes</i> for debugging and development. </p>
<p> By default, <code>groffer</code> first tries whether <i>x~mode</i> is possible, then <i>ps~mode</i>, and finally <i>tty~mode</i>. This mode testing sequence for <i>auto~mode</i> can be changed by specifying a comma separated list of modes with the option <code>&#8211;default-modes.</code> </p>
<p> The searching for <i>man~pages</i> and the decompression of the input are active in every mode.</p>
<h3>Graphical Display Modes</h3>
<p> The graphical display modes work mostly in the X Window System environment (or similar implementations within other windowing environments). The environment variable <i>DISPLAY</i> and the option <code>&#8211;display</code> are used for specifying the X Window System display to be used. If this environment variable is empty, <code>groffer</code> assumes that the X Window System is not running and changes to a <i>text~mode</i>. You can change this automatic behavior by the option <code>&#8211;default-modes</code>. </p>
<p> Known viewers for the graphical display modes and their standard X Window System viewer programs are</p>
<dl>
<dt>*</p>
<dd> in a PDF viewer (<i>pdf~mode</i>)</p>
<dt>*</p>
<dd> in a web browser (<i>html</i>, (<i>xhtml</i>, or <i>www~mode</i>)</p>
<dt>*</p>
<dd> in a PostScript viewer (<i>ps~mode</i>)</p>
<dt>*</p>
<dd> X Window System <i>roff</i> viewers such as <code><a href="/docs/linux/man/1-gxditview/">gxditview</a></code>(1) or <code><a href="/docs/linux/man/1-xditview/">xditview</a></code>(1) (in <i>x~mode</i>)</p>
<dt>*</p>
<dd> in a DVI viewer program (<i>dvi~mode</i>)</dl>
<p> The <i>pdf~mode</i> has a major advantage &#8212; it is the only graphical display mode that allows searching for text within the viewer; this can be a really important feature. Unfortunately, it takes some time to transform the input into the PDF format, so it was not chosen as the major mode. </p>
<p> These graphical viewers can be customized by options of the X Window System Toolkit Intrinsics. But the <code>groffer</code> options use a leading double minus instead of the single minus used by the X Window System Toolkit Intrinsics.</p>
<h3>Text modes</h3>
<p> There are two modes for text output, <i>mode~text</i> for plain output without a pager and <i>mode~tty</i> for a text output on a text terminal using some pager program. </p>
<p> If the variable <i>DISPLAY</i> is not set or empty, <code>groffer</code> assumes that it should use <i>tty~mode</i>. </p>
<p> In the actual implementation, the <i>groff</i> output device <i>latin1</i> is chosen for <i>text~modes</i>. This can be changed by specifying option <code>-T</code> or <code>&#8211;device</code>. </p>
<p> The pager to be used can be specified by one of the options <code>&#8211;pager</code> and <code>&#8211;viewer</code>, or by the environment variable <i>PAGER</i>. If all of this is not used the <code><a href="/docs/linux/man/1-less/">less</a></code>(1) program with the option <code>-r</code> for correctly displaying control sequences is used as the default pager.</p>
<h3>Special Modes for Debugging and Development</h3>
<p> These modes use the <i>groffer</i> file determination and decompression. This is combined into a single input file that is fed directly into <code>groff</code> with different strategy without the <i>groffer</i> viewing facilities. These modes are regarded as advanced, they are useful for debugging and development purposes. </p>
<p> The <i>source~mode</i> with option <code>&#8211;source</code> just displays the decompressed input. </p>
<p> Option <code>&#8211;to-stdout</code> does not display in a graphical mode. It just generates the file for the chosen mode and then prints its content to standard output. </p>
<p> The <i>groff~mode</i> passes the input to <code>groff</code> using only some suitable options provided to <code>groffer</code>. This enables the user to save the generated output into a file or pipe it into another program. </p>
<p> In <i>groff~mode</i>, the option <code>-Z</code> disables post-processing, thus producing the <i>groff intermediate</i> <i>output</i>. In this mode, the input is formatted, but not postprocessed; see <code><a href="/docs/linux/man/5-groff_out/">groff_out</a></code>(5) for details. </p>
<p> All <code>groff</code> short options are supported by <code>groffer</code>.</p>
<h2>MAN PAGE SEARCHING</h2>
<p> The default behavior of <code>groffer</code> is to first test whether a file parameter represents a local file; if it is not an existing file name, it is assumed to represent the name of a <i>man~page</i>. The following options can be used to determine whether the arguments should be handled as file name or <i>man~page</i> arguments.</p>
<dl>
<dt><code>&#8211;man</code></p>
<dd> forces to interpret all file parameters as <i>filespecs</i> for searching <i>man~pages</i>.</p>
<dt><code>&#8211;no-man</code></p>
<dd> <code>&#8211;local-file</code> disable the <i>man</i> searching; so only local files are displayed.</dl>
<p> If neither a local file nor a <i>man~page</i> was retrieved for some file parameter a warning is issued on standard error, but processing is continued.</p>
<h3>Search Algorithm</h3>
<p> Let us now assume that a <i>man~page</i> should be searched. The <code>groffer</code> program provides a search facility for <i>man~pages</i>. All long options, all environment variables, and most of the functionality of the GNU <code><a href="/docs/linux/man/1-man/">man</a></code>(1) program were implemented. The search algorithm shall determine which file is displayed for a given <i>man~page</i>. The process can be modified by options and environment variables. </p>
<p> The only <i>man</i> action that is omitted in <code>groffer</code> are the preformatted <i>man~pages</i>, also called <i>cat~pages</i>. With the excellent performance of the actual computers, the preformatted <i>man~pages</i> aren&#8217;t necessary any longer. Additionally, <code>groffer</code> is a <i>roff</i> program; it wants to read <i>roff</i> source files and format them itself. </p>
<p> The algorithm for retrieving the file for a <i>man~page</i> needs first a set of directories. This set starts with the so-called <i>man~path</i> that is modified later on by adding names of <i>operating system</i> and <i>language</i>. This arising set is used for adding the section directories which contain the <i>man~page</i> files. </p>
<p> The <i>man~path</i> is a list of directories that are separated by colon. It is generated by the following methods.</p>
<dl>
<dt>*</p>
<dd> The environment variable <i>MANPATH</i> can be set.</p>
<dt>*</p>
<dd> It can be read from the arguments of the environment variable <i>MANOPT</i>.</p>
<dt>*</p>
<dd> The <i>man~path</i> can be manually specified by using the option <code>&#8211;manpath</code>. An empty argument disables the <i>man~page</i> searching.</p>
<dt>*</p>
<dd> When no <i>man~path</i> was set the <code><a href="/docs/linux/man/1-manpath/">manpath</a></code>(1) program is tried to determine one.</p>
<dt>*</p>
<dd> If this does not work a reasonable default path from <i>$PATH</i> is determined.</dl>
<p> We now have a starting set of directories. The first way to change this set is by adding names of <i>operating</i> <i>systems</i>. This assumes that <i>man~pages</i> for several <i>operating systems</i> are installed. This is not always true. The names of such <i>operating systems</i> can be provided by 3 methods.</p>
<dl>
<dt>*</p>
<dd> The environment variable <i>SYSTEM</i> has the lowest precedence.</p>
<dt>*</p>
<dd> This can be overridden by an option in <i>MANOPT</i>.</p>
<dt>*</p>
<dd> This again is overridden by the command-line option <code>&#8211;systems</code>.</dl>
<p> Several names of <i>operating systems</i> can be given by appending their names, separated by a comma. </p>
<p> The <i>man~path</i> is changed by appending each <i>system</i> name as subdirectory at the end of each directory of the set. No directory of the <i>man~path</i> set is kept. But if no <i>system</i> name is specified the <i>man~path</i> is left unchanged. </p>
<p> After this, the actual set of directories can be changed by <i>language</i> information. This assumes that there exist <i>man~pages</i> in different languages. The wanted <i>language</i> can be chosen by several methods.</p>
<dl>
<dt>*</p>
<dd> Environment variable <i>LANG</i>.</p>
<dt>*</p>
<dd> This is overridden by <i>LC_MESSAGES</i>.</p>
<dt>*</p>
<dd> This is overridden by <i>LC_ALL</i>.</p>
<dt>*</p>
<dd> This can be overridden by providing an option in <i>MANOPT</i>.</p>
<dt>*</p>
<dd> All these environment variables are overridden by the command-line option <code>&#8211;locale</code>.</dl>
<p> The <i>default language</i> can be specified by specifying one of the pseudo-language parameters C or POSIX. This is like deleting a formerly given <i>language</i> information. The <i>man~pages</i> in the <i>default language</i> are usually in English. </p>
<p> Of course, the <i>language</i> name is determined by <code>man</code>. In GNU <code>man</code>, it is specified in the POSIX~1003.1 based format: </p>
<p> <i>&lt;language&gt;/</i>[_,<i>&lt;territory&gt;/</i>[.<i>&lt;character-set&gt;/</i>[,,<i>&lt;version&gt;/</i>]]], </p>
<p> but the two-letter code in <i>&lt;language&gt;</i> is sufficient for most purposes. If for a complicated <i>language</i> formulation no <i>man~pages</i> are found <code>groffer</code> searches the country part consisting of these first two characters as well. </p>
<p> The actual directory set is copied thrice. The <i>language</i> name is appended as subdirectory to each directory in the first copy of the actual directory set (this is only done when a language information is given). Then the 2-letter abbreviation of the <i>language</i> name is appended as subdirectories to the second copy of the directory set (this is only done when the given language name has more than 2 letters). The third copy of the directory set is kept unchanged (if no <i>language</i> information is given this is the kept directory set). These maximally 3 copies are appended to get the new directory set. </p>
<p> We now have a complete set of directories to work with. In each of these directories, the <i>man</i> files are separated in <i>sections</i>. The name of a <i>section</i> is represented by a single character, a digit between <i>1</i> and <i>9</i>, or the character <i>o</i> or <i>n</i>, in this order. </p>
<p> For each available <i>section</i>, a subdirectory <code>man</code><i>&lt;section&gt;</i> exists containing all <i>man</i> files for this <i>section</i>, where <i>&lt;section&gt;</i> is a single character as described before. Each <i>man</i> file in a <i>section</i> directory has the form <i></i>man&lt;section&gt;/&lt;name&gt;.&lt;section&gt;[&lt;extension&gt;][.&lt;compression&gt;], where <i>&lt;extension&gt;</i> and <i>&lt;compression&gt;</i> are optional. <i>&lt;name&gt;</i> is the name of the <i>man~page</i> that is also specified as filespec argument on the command line. </p>
<p> The <i>extension</i> is an addition to the section. This postfix acts like a subsection. An <i>extension</i> occurs only in the file name, not in name of the <i>section</i> subdirectory. It can be specified on the command line. </p>
<p> On the other hand, the <i>compression</i> is just an information on how the file is compressed. This is not important for the user, such that it cannot be specified on the command line. </p>
<p> There are 4 methods to specify a <i>section</i> on the command line:</p>
<dl>
<dt>*</p>
<dd> Environment variable <i>MANSECT</i></p>
<dt>*</p>
<dd> Command line option <code>&#8211;sections</code></p>
<dt>*</p>
<dd> Appendix to the <i>name</i> argument in the form <i>&lt;name&gt;.&lt;section&gt;</i></p>
<dt>*</p>
<dd> Preargument before the <i>name</i> argument in the form <i>&lt;section&gt; &lt;name&gt;</i></dl>
<p> It is also possible to specify several <i>sections</i> by appending the single characters separated by colons. One can imagine that this means to restrict the <i>man~page</i> search to only some <i>sections</i>. The multiple <i>sections</i> are only possible for <i>MANSECT</i> and <code>&#8211;sections</code>. </p>
<p> If no <i>section</i> is specified all <i>sections</i> are searched one after the other in the given order, starting with <i>section~1</i>, until a suitable file is found. </p>
<p> There are 4 methods to specify an <i>extension</i> on the command line. But it is not necessary to provide the whole extension name, some abbreviation is good enough in most cases.</p>
<dl>
<dt>*</p>
<dd> Environment variable <i>EXTENSION</i></p>
<dt>*</p>
<dd> Command line option <code>&#8211;extension</code></p>
<dt>*</p>
<dd> Appendix to the <i>&lt;name&gt;.&lt;section&gt;</i> argument in the form <i>&lt;name&gt;.&lt;section&gt;&lt;extension&gt;</i></p>
<dt>*</p>
<dd> Preargument before the <i>name</i> argument in the form <i>&lt;section&gt;&lt;extension&gt; &lt;name&gt;</i></dl>
<p> For further details on <i>man~page</i> searching, see <code><a href="/docs/linux/man/1-man/">man</a></code>(1).</p>
<h3>Examples of man files</h3>
<dl>
<dt><code>/usr/share/man/man1/groff.1</code></p>
<dd> This is an uncompressed file for the <i>man~page</i> groff in <i>section~1</i>. It can be called by <i>sh#</i> groffer~groff No <i>section</i> is specified here, so all <i>sections</i> should be searched, but as <i>section~1</i> is searched first this file will be found first. The file name is composed of the following components. <code>/usr/share/man/</code> must be part of the <i>man~path</i>; the subdirectory <code>man1/</code> and the part <code>.1</code> stand for the <i>section</i>; <code>groff</code> is the name of the <i>man~page</i>.</p>
<dt><code>/usr/local/share/man/man7/groff.7.gz</code></p>
<dd> The file name is composed of the following components. <code>/usr/local/share/man</code> must be part of the <i>man~path</i>; the subdirectory <code>man7/</code> and the part <code>.7</code> stand for the <i>section</i>; <code>groff</code> is the name of the <i>man~page</i>; the final part <code>.gz</code> stands for a compression with <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1). As the <i>section</i> is not the first one it must be specified as well. This can be done by one of the following commands. <i>sh#</i>~groffer~groff.7 <i>sh#</i>~groffer~7~groff <i>sh#</i>~groffer~&#8211;sections=7~groff</p>
<dt><code>/usr/local/man/man1/ctags.1emacs21.bz2</code></p>
<dd> Here <code>/usr/local/man</code> must be in <i>man~path</i>; the subdirectory <code>man1/</code> and the file name part <code>.1</code> stand for <i>section~1</i>; the name of the <i>man~page</i> is <code>ctags</code>; the section has an extension <code>emacs21</code>; and the file is compressed as <code>.bz2</code> with <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1). The file can be viewed with one of the following commands <i>sh#</i>~groffer~ctags.1e <i>sh#</i>~groffer~1e~ctags <i>sh#</i>~groffer~&#8211;extension=e~&#8211;sections=1~ctags where e works as an abbreviation for the extension emacs21.</p>
<dt><code>/usr/man/linux/de/man7/man.7.Z</code></p>
<dd> The directory <code>/usr/man</code> is now part of the <i>man~path</i>; then there is a subdirectory for an <i>operating system</i> name <code>linux/</code>; next comes a subdirectory <code>de/</code> for the German <i>language</i>; the <i>section</i> names <code>man7</code> and <code>.7</code> are known so far; <code>man</code> is the name of the <i>man~page</i>; and <code>.Z</code> signifies the compression that can be handled by <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1). We want now show how to provide several values for some options. That is possible for <i>sections</i> and <i>operating system</i> names. So we use as <i>sections~5</i> and <i>7</i> and as <i>system</i> names <i>linux</i> and <i>aix</i>. The command is then </p>
<p> <i>sh#</i> groffer~&#8211;locale=de~&#8211;sections=5:7~&#8211;systems=linux,aix~man <i>sh#</i> LANG=de~MANSECT=5:7~SYSTEM=linux,aix~groffer~man</dl>
<h2>DECOMPRESSION</h2>
<p> The program has a decompression facility. If standard input or a file that was retrieved from the command line parameters is compressed with a format that is supported by either <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1) or <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1) it is decompressed on-the-fly. This includes the GNU <code>.gz</code>, <code>.bz2</code>, and the traditional <code>.Z</code> compression. The program displays the concatenation of all decompressed input in the sequence that was specified on the command line.</p>
<h2>ENVIRONMENT</h2>
<p> The <code>groffer</code> program supports many system variables, most of them by courtesy of other programs. All environment variables of <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1) and GNU <code><a href="/docs/linux/man/1-man/">man</a></code>(1) and some standard system variables are honored.</p>
<h3>Native groffer Variables</h3>
<dl>
<dt><i>GROFFER_OPT</i></p>
<dd> Store options for a run of <code>groffer</code>. The options specified in this variable are overridden by the options given on the command line. The content of this variable is run through the shell builtin &#8220;eval&#8221;, so arguments containing whitespace or special shell characters should be quoted. Do not forget to export this variable, otherwise it does not exist during the run of <code>groffer</code>.</dl>
<h3>System Variables</h3>
<p> The following variables have a special meaning for <code>groffer</code>.</p>
<dl>
<dt><i>DISPLAY</i></p>
<dd> If set, this variable indicates that the X Window System is running. Testing this variable decides on whether graphical or text output is generated. This variable should not be changed by the user carelessly, but it can be used to start the graphical <code>groffer</code> on a remote X Window System terminal. For example, depending on your system, <code>groffer</code> can be started on the second monitor by the command </p>
<p> <i>sh#</i> DISPLAY=:0.1~groffer~what.ever &amp;</p>
<dt><i>LC_ALL</i></p>
<dd> <i>LC_MESSAGES</i> <i>LANG</i> If one of these variables is set (in the above sequence), its content is interpreted as the locale, the language to be used, especially when retrieving <i>man~pages</i>. A locale name is typically of the form <i>language</i>[<code>_</code><i>territory</i>[<code>.</code><i>codeset</i>[<code>@</code><i>modifier</i>]]], where <i>language</i> is an ISO 639 language code, <i>territory</i> is an ISO 3166 country code, and <i>codeset</i> is a character set or encoding identifier like ISO-8859-1 or UTF-8; see <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3). The locale values C and POSIX stand for the default, i.e. the <i>man~page</i> directories without a language prefix. This is the same behavior as when all 3~variables are unset.</p>
<dt><i>PAGER</i></p>
<dd> This variable can be used to set the pager for the tty output. For example, to disable the use of a pager completely set this variable to the <code><a href="/docs/linux/man/1-cat/">cat</a></code>(1) program </p>
<p> <i>sh#</i> PAGER=cat~groffer~anything </p>
<dt><i>PATH</i></p>
<dd> All programs within the <code>groffer</code> script are called without a fixed path. Thus this environment variable determines the set of programs used within the run of <code>groffer</code>.</dl>
<h3>Groff Variables</h3>
<p> The <code>groffer</code> program internally calls <code>groff</code>, so all environment variables documented in <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1) are internally used within <code>groffer</code> as well. The following variable has a direct meaning for the <code>groffer</code> program.</p>
<dl>
<dt><i>GROFF_TMPDIR</i></p>
<dd> If the value of this variable is an existing, writable directory, <code>groffer</code> uses it for storing its temporary files, just as <code>groff</code> does. See the <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1) man page for more details on the location of temporary files.</dl>
<h3>Man Variables</h3>
<p> Parts of the functionality of the <code>man</code> program were implemented in <code>groffer</code>; support for all environment variables documented in <code><a href="/docs/linux/man/1-man/">man</a></code>(1) was added to <code>groffer</code>, but the meaning was slightly modified due to the different approach in <code>groffer</code>; but the user interface is the same. The <code>man</code> environment variables can be overwritten by options provided with <i>MANOPT</i>, which in turn is overwritten by the command line.</p>
<dl>
<dt><i>EXTENSION</i></p>
<dd> Restrict the search for <i>man~pages</i> to files having this extension. This is overridden by option <code>&#8211;extension</code>; see there for details.</p>
<dt><i>MANOPT</i></p>
<dd> This variable contains options as a preset for <code><a href="/docs/linux/man/1-man/">man</a></code>(1). As not all of these are relevant for <code>groffer</code> only the essential parts of its value are extracted. The options specified in this variable overwrite the values of the other environment variables that are specific to <i>man</i>. All options specified in this variable are overridden by the options given on the command line.</p>
<dt><i>MANPATH</i></p>
<dd> If set, this variable contains the directories in which the <i>man~page</i> trees are stored. This is overridden by option <code>&#8211;manpath</code>.</p>
<dt><i>MANSECT</i></p>
<dd> If this is a colon separated list of section names, the search for <i>man~pages</i> is restricted to those manual sections in that order. This is overridden by option <code>&#8211;sections</code>.</p>
<dt><i>SYSTEM</i></p>
<dd> If this is set to a comma separated list of names these are interpreted as <i>man~page</i> trees for different operating systems. This variable can be overwritten by option <code>&#8211;systems</code>; see there for details.</dl>
<p> The environment variable <i>MANROFFSEQ</i> is ignored by <code>groffer</code> because the necessary preprocessors are determined automatically.</p>
<h2>CONFIGURATION FILES</h2>
<p> The <code>groffer</code> program can be preconfigured by two configuration files.</p>
<dl>
<dt><code>/etc/groff/groffer.conf</code></p>
<dd> System-wide configuration file for <code>groffer</code>.</p>
<dt><code>$HOME/.groff/groffer.conf</code></p>
<dd> User-specific configuration file for <code>groffer</code>, where <i>$HOME</i> denotes the user&#8217;s home directory. This file is called after the system-wide configuration file to enable overriding by the user.</dl>
<p> Both files are handled for the configuration, but the configuration file in <code>/etc</code> comes first; it is overwritten by the configuration file in the home directory; both configuration files are overwritten by the environment variable <i>GROFFER_OPT</i>; everything is overwritten by the command line arguments. </p>
<p> The configuration files contain options that should be called as default for every <code>groffer</code> run. These options are written in lines such that each contains either a long option, a short option, or a short option cluster; each with or without an argument. So each line with configuration information starts with a minus character &#8220;<code>&#8211;</code>&#8220;; a line with a long option starts with two minus characters &#8220;<code>&#8212;</code>&#8220;, a line with a short option or short option cluster starts with a single minus &#8220;<code>&#8211;</code>&#8220;. </p>
<p> The option names in the configuration files may not be abbreviated, they must be exact. </p>
<p> The argument for a long option can be separated from the option name either by an equal sign &#8220;<code>=</code>&#8221; or by whitespace, i.e. one or several space or tab characters. An argument for a short option or short option cluster can be directly appended to the option name or separated by whitespace. The end of an argument is the end of the line. It is not allowed to use a shell environment variable in an option name or argument. </p>
<p> It is not necessary to use quotes in an option or argument, except for empty arguments. An empty argument can be provided by appending a pair of quotes to the separating equal sign or whitespace; with a short option, the separator can be omitted as well. For a long option with a separating equal sign &#8220;<code>=</code>&#8220;, the pair of quotes can be omitted, thus ending the line with the separating equal sign. All other quote characters are cancelled internally. </p>
<p> In the configuration files, arbitrary whitespace is allowed at the beginning of each line, it is just ignored. Each whitespace within a line is replaced by a single space character &#8221; &#8221; internally. </p>
<p> All lines of the configuration lines that do not start with a minus character are ignored, such that comments starting with &#8220;<code>#</code>&#8221; are possible. So there are no shell commands in the configuration files. </p>
<p> As an example, consider the following configuration file that can be used either in <code>/etc/groff/groffer.conf</code> or <font SIZE="+2"><code>~</code></font><code>/.groff/groffer.conf .</code> </p>
<pre>
# groffer configuration file
#
# groffer options that are used in each call of groffer
--foreground=DarkBlue
--resolution=100
--viewer=gxditview -geometry 900x1200
</pre>
<p> The lines starting with <code>#</code> are just ignored, so they act as command lines. This configuration sets four <code>groffer</code> options (the lines starting with &#8220;<code>&#8211;</code>&#8220;). This has the following effects:</p>
<dl>
<dt>*</p>
<dd> Use a text color of <code>DarkBlue</code> in all viewers that support this, such as <code>gxditview</code>.</p>
<dt>*</p>
<dd> Use a resolution of <code>100dpi</code> in all viewers that support this, such as <code>gxditview</code>. By this, the default device in <i>x mode</i> is set to <code>X100</code>.</p>
<dt>*</p>
<dd> Force <code><a href="/docs/linux/man/1-gxditview/">gxditview</a></code>(1) as the <i>x-mode</i> viewer using the geometry option for setting the width to <code>900px</code> and the height to <code>1200px</code>. This geometry is suitable for a resolution of <code>100dpi</code>.</p>
<dt>*</p>
<dd> Use <code><a href="/docs/linux/man/1-xpdf/">xpdf</a></code>(1) as the <i>pdf-mode</i> viewer with the argument <code>-Z</code> <code>150</code>.</dl>
<h2>EXAMPLES</h2>
<p> The usage of <code>groffer</code> is very easy. Usually, it is just called with a file name or <i>man~page</i>. The following examples, however, show that <code>groffer</code> has much more fancy capabilities. </p>
<p> <i>sh#</i>~groffer~/usr/local/share/doc/groff/meintro.ms.gz </p>
<p> Decompress, format and display the compressed file <code>meintro.ms.gz</code> in the directory <code>/usr/local/share/doc/groff</code>, using the standard viewer <code>gxditview</code> as graphical viewer when in the X Window System, or the <code><a href="/docs/linux/man/1-less/">less</a></code>(1) pager program otherwise. </p>
<p> <i>sh#</i>~groffer~groff </p>
<p> If the file <code>./groff</code> exists use it as input. Otherwise interpret the argument as a search for the <i>man~page</i> named <code>groff</code> in the smallest possible <i>man~section</i>, being section 1 in this case. </p>
<p> <i>sh#</i>~groffer~man:groff </p>
<p> search for the <i>man~page</i> of <code>groff</code> even when the file <code>./groff</code> exists. </p>
<p> <i>sh#</i>~groffer~groff.7 <i>sh#</i>~groffer~7~groff </p>
<p> search the <i>man~page</i> of <code>groff</code> in <i>man~section</i> <code>7</code>. This section search works only for a digit or a single character from a small set. </p>
<p> <i>sh#</i>~groffer~fb.modes </p>
<p> If the file <code>./fb.modes</code> does not exist interpret this as a search for the <i>man~page</i> of <code>fb.modes</code>. As the extension <i>modes</i> is not a single character in classical section style the argument is not split to a search for <code>fb</code>. </p>
<p> <i>sh#</i>~groffer~groff~&#8217;<a href="/docs/linux/man/1-troff/">troff</a>(1)&#8217;~man:roff </p>
<p> The arguments that are not existing files are looked-up as the following <i>man~pages</i>: <code>groff</code> (automatic search, should be found in <i>man</i>~section~1), <code>troff</code> (in section~1), and <code>roff</code> (in the section with the lowest number, being~7 in this case). The quotes around <i>&#8216;<a href="/docs/linux/man/1-troff/">troff</a>(1)&#8217;</i> are necessary because the parentheses are special shell characters; escaping them with a backslash character <i>\(</i> and <i>\)</i> would be possible, too. The formatted files are concatenated and displayed in one piece. </p>
<p> <i>sh#</i>~LANG=de~groffer~&#8211;man~&#8211;viewer=galeon~ls </p>
<p> Retrieve the German <i>man~page</i> (language <i>de</i>) for the <code>ls</code> program, decompress it, format it to <i>html</i> or <i>xhtml</i> format (<i>www~mode</i>) and view the result in the web browser <code>galeon</code>. The option <code>&#8211;man</code> guarantees that the <i>man~page</i> is retrieved, even when a local file <code>ls</code> exists in the actual directory. </p>
<p> <i>sh#</i>~groffer~&#8211;source~&#8217;<a href="/docs/linux/man/7-man-roff/">man:roff</a>(7)&#8217; </p>
<p> Get the <i>man~page</i> called <i>roff</i> in <i>man</i>~section 7, decompress it, and print its unformatted content, its source code. </p>
<p> <i>sh#</i>~groffer~&#8211;de-p~&#8211;in~&#8211;ap </p>
<p> This is a set of abbreviated arguments, it is determined as </p>
<p> <i>sh#</i>~groffer~&#8211;debug-params~&#8211;intermediate-output~&#8211;apropos </p>
<p> <i>sh#</i>~cat~file.gz~|~groffer~-Z~-mfoo </p>
<p> The file <code>file.gz</code> is sent to standard input, this is decompressed, and then this is transported to the <i>groff intermediate output mode</i> without post-processing (<code>groff</code> option <code>-Z</code>), using macro package <i>foo</i> (<code>groff</code> option <code>-m</code>). </p>
<p> <i>sh#</i>~echo~&#8217;(CBWOW!&#8217;~| &gt; groffer &#8211;x &#8211;bg red &#8211;fg yellow &#8211;geometry 200&#215;100 &#8211; </p>
<p> Display the word WOW! in a small window in constant-width bold font, using color yellow on red background.</p>
<h2>COMPATIBILITY</h2>
<p> The <code>groffer</code> program is written in Perl, the Perl version during writing was v5.8.8. </p>
<p> <code>groffer</code> provides its own parser for command-line arguments that is compatible to both POSIX <code><a href="/docs/linux/man/1-getopts/">getopts</a></code>(1) and GNU <code><a href="/docs/linux/man/1-getopt/">getopt</a></code>(1). It can handle option arguments and file names containing white space and a large set of special characters. The following standard types of options are supported.</p>
<dl>
<dt>*</p>
<dd> The option consisting of a single minus <code>&#8211;</code> refers to standard input.</p>
<dt>*</p>
<dd> A single minus followed by characters refers to a single character option or a combination thereof; for example, the <code>groffer</code> short option combination <code>-Qmfoo</code> is equivalent to <code>-Q~-m~foo</code>.</p>
<dt>*</p>
<dd> Long options are options with names longer than one character; they are always preceded by a double minus. An option argument can either go to the next command-line argument or be appended with an equal sign to the argument; for example, <code>&#8211;long=arg</code> is equivalent to <code>&#8211;long~arg</code>.</p>
<dt>*</p>
<dd> An argument of <code>&#8212;</code> ends option parsing; all further command-line arguments are interpreted as <i>filespec</i> parameters, i.e. file names or constructs for searching <i>man~pages</i>).</p>
<dt>*</p>
<dd> All command-line arguments that are neither options nor option arguments are interpreted as <i>filespec</i> parameters and stored until option parsing has finished. For example, the command line </p>
<p> <i>sh#</i>~groffer file1 -a -o arg file2 </p>
<p> is equivalent to </p>
<p> <i>sh#</i>~groffer -a -o arg &#8212; file1 file2 </p>
</dl>
<p> The free mixing of options and <i>filespec</i> parameters follows the GNU principle. That does not fulfill the strange option behavior of POSIX that ends option processing as soon as the first non-option argument has been reached. The end of option processing can be forced by the option &#8220;<code>&#8212;</code>&#8221; anyway.</p>
<h2>AUTHORS</h2>
<p> <code>groffer</code> was written by Bernd Warken</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1)</p>
<dl>
<dt>
<dd> Details on the options and environment variables available in <code>groff</code>; all of them can be used with <code>groffer</code>.</dl>
<dl>
<dt><code><a href="/docs/linux/man/1-grog/">grog</a></code>(1)</p>
<dd> This program tries to guess the necessary <code>groff</code> command-line options from the input and the <code>groffer</code> options.</p>
<dt><code><a href="/docs/linux/man/7-groff/">groff</a></code>(7)</p>
<dd> Documentation of the <i>groff</i> language.</p>
<dt><code><a href="/docs/linux/man/7-groff_char/">groff_char</a></code>(7)</p>
<dd> Documentation on the <i>groff</i> characters, special characters, and glyphs..</p>
<dt><code><a href="/docs/linux/man/5-groff_tmac/">groff_tmac</a></code>(5)</p>
<dd> Documentation on the <i>groff</i> macro files.</p>
<dt><code><a href="/docs/linux/man/5-groff_out/">groff_out</a></code>(5)</p>
<dd> Documentation on the <i>groff intermediate output</i> before the run of a <i>postprocessor</i>. (<i>ditroff</i> output). This can be run by the <code>groff</code> or <code>groffer</code> option <code>-Z</code>.</p>
<dt><code><a href="/docs/linux/man/1-man/">man</a></code>(1)</p>
<dd> The standard program to display <i>man~pages</i>. The information there is only useful if it is the <i>man~page</i> for GNU <code>man</code>. Then it documents the options and environment variables that are supported by <code>groffer</code>.</p>
<dt><code><a href="/docs/linux/man/1-gxditview/">gxditview</a></code>(1)</p>
<dd> <code><a href="//www.systutorials.com/docs/linux/man/1x-xditview/">xditview</a></code>(1x)</p>
<dl>
<dt>
<dd> Viewers for <code>groffer</code>&#8216;s <i>x~mode</i>.</dl>
<dt><code><a href="/docs/linux/man/1-kpdf/">kpdf</a></code>(1)</p>
<dd> <code><a href="/docs/linux/man/1-kghostview/">kghostview</a></code>(1) <code><a href="/docs/linux/man/1-evince/">evince</a></code>(1) <code><a href="/docs/linux/man/1-ggv/">ggv</a></code>(1) <code><a href="/docs/linux/man/1-gv/">gv</a></code>(1) <code><a href="/docs/linux/man/1-ghostview/">ghostview</a></code>(1) <code><a href="/docs/linux/man/1-gs/">gs</a></code>(1) Viewers for <code>groffer</code>&#8216;s <i>ps~mode</i>.</p>
<dt><code><a href="/docs/linux/man/1-kpdf/">kpdf</a></code>(1)</p>
<dd> <code><a href="/docs/linux/man/1-acroread/">acroread</a></code>(1) <code><a href="/docs/linux/man/1-evince/">evince</a></code>(1) <code><a href="/docs/linux/man/1-xpdf/">xpdf</a></code>(1) <code><a href="/docs/linux/man/1-gpdf/">gpdf</a></code>(1) <code><a href="/docs/linux/man/1-kghostview/">kghostview</a></code>(1) <code><a href="/docs/linux/man/1-ggv/">ggv</a></code>(1) Viewers for <code>groffer</code>&#8216;s <i>pdf~mode</i>.</dl>
<p> <code><a href="/docs/linux/man/1-kdvi/">kdvi</a></code>(1), <code><a href="/docs/linux/man/1-xdvi/">xdvi</a></code>(1), <code><a href="/docs/linux/man/1-dvilx/">dvilx</a></code>(1)</p>
<dl>
<dt>
<dd> Viewers for <code>groffer</code>&#8216;s <i>dvi~mode</i>.</dl>
<dl>
<dt><code><a href="/docs/linux/man/1-konqueror/">konqueror</a></code>(1)</p>
<dd> <code><a href="/docs/linux/man/1-epiphany/">epiphany</a></code>(1) <code><a href="/docs/linux/man/1-firefox/">firefox</a></code>(1) <code><a href="/docs/linux/man/1-mozilla/">mozilla</a></code>(1) <code><a href="/docs/linux/man/1-netscape/">netscape</a></code>(1) <code><a href="/docs/linux/man/1-lynx/">lynx</a></code>(1) Web-browsers for <code>groffer</code>&#8216;s <i>html</i>, <i>xhtml</i>, or <i>www~mode</i>.</p>
<dt><code><a href="/docs/linux/man/1-less/">less</a></code>(1)</p>
<dd> <code><a href="/docs/linux/man/1-more/">more</a></code>(1) Standard pager program for the <i>tty~mode</i>.</p>
<dt><code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1)</p>
<dd> <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1) <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1) The decompression programs supported by <code>groffer</code>. </p>
</dl>
<h2>Index</h2>
