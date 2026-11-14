---
title: "tex4ht(1)"
name: "tex4ht"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tex4ht/"
description: "TeX4ht – a system for authoring hypertext with TeX and friends"
---

<h2 class="name">NAME</h2>
<p> TeX4ht &#8211; a system for authoring hypertext with TeX and friends </p>
<h2>SYNOPSIS</h2>
<p> <code>mk4ht</code> <i>command</i> <i>file</i> [ <i>options1</i> ] [ <i>options2</i> ] [ <i>options3</i> ] </p>
<p> <code>httex</code>|<code>htlatex</code>|<code>httexi</code> <i>file</i> [ <i>options1</i> ] [ <i>options2</i> ] [ <i>options3</i> ] </p>
<p> <code>ht</code> tex|latex <i>file</i> [ <i>t4ht options</i> ] </p>
<p> <code>tex4ht</code> [ <code>-f</code><i>dir-char</i> ] <i>file[.dvi]</i> [ <code>-c</code><i>tag-name</i> ] [ <code>-e</code><i>env-file</i> ] [ <code>-g</code><i>bitmap-file-ext</i> ] [ <code>-h</code>(<code>e|f|F|g|s|v|V</code>) ] [ <code>-i</code><i>htf-font-dir</i> ] [ <code>-l</code><i>bookkeeping-file</i> ] [ <code>-P</code>(<code>*</code>|<i>filter</i>) ] [ <code>-t</code><i>tfm-font-dir</i> ] [ <code>-u10</code> ] [ <code>-utf8</code> ] [ <code>-xs</code> ] </p>
<p> <code>t4ht</code> [ <code>-f</code><i>dir-char</i> ] <i>file[.lg]</i> [ <code>-c</code><i>tag-name</i> ] [ <code>-d</code><i>out-dir</i> ] [ <code>-e</code><i>env-file</i> ] [ <code>-i</code> ] [ <code>-m</code><i>mode</i> ] [ <code>-M</code><i>mode</i> ] [ <code>-p</code> ] [ <code>-r</code> ] [ <code>-S</code>(<code>*</code>|<i>filter</i>) ] [ <code>-X</code><i>field-content</i> ] [ <code>-.</code><i>field-content</i> ] </p>
<h2>DESCRIPTION</h2>
<p> (This manual page was written for the Debian GNU/Linux distribution because the original program does not have a manual page. Instead, it is documented in detail at the author&#8217;s website; see below. Please refer to that documentation for more details or up to date information.) </p>
<p> This page documents briefly the portmanteau perl script <code>mk4ht</code>, the more specific shell scripts <code>httex</code>, htlatex<code>, httexi</code>, and others like them, the lower level shell script interface <code>ht</code>, and the commands <code>tex4ht</code> and t4ht that all these scripts invoke. Together these programs constitute TeX4ht; a highly configurable TeX-based authoring system for producing hypertext. </p>
<p> TeX4ht interacts with TeX-based applications through a style file <i>tex4ht.sty</i> and other files which are loaded by this style file, leaving the processing of the source files to the native TeX compiler. The output of the TeX compiler is then post-processed by <code>tex4ht</code> and t4ht<code>.</code> Consequently, TeX4ht can handle most features of TeX-based systems in general, and of LaTeX in particular. </p>
<p> The shell scripts <code> httex ,</code> htlatex <code>and</code> httexi convert TeX (respectively LaTeX and texinfo) into HTML. Typical user requirements should be satisfied by these scripts which can generally convert typical TeX source <i>without</i> requiring any modifications. </p>
<p> To convert from a one of the other dialects of TeX (like ConTeXt), <i>or</i> to convert into one of the other variants of hypertext (MathML, XML, OO and so on), it is <i>recommended</i> that you use the perl script <code>mk4ht.</code> Most common usage of the system can be covered by the appropriate use of this command with its options. </p>
<p> The shell script <code> ht</code> is a much more elementary script which is provided for more complicated needs. Its correct use depends on a better understanding of the system. </p>
<p> All these scripts begin with suitable invocations of <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1) or <code><a href="/docs/linux/man/1-latex/">latex</a></code>(1) or other dialects of TeX as required. The post-processing of the <i>.dvi</i> output is handled by <code>tex4ht.</code> Anything that cannot be rendered using HTML (or its chosen hypertext variant), such as the creation of bitmap images or CSS (Cascade Style Sheet) files is handled by the auxiliary program <code>t4ht.</code> The method used for generating the images can be configured. </p>
<h2>OPTIONS</h2>
<p> The following is only a very brief summary of the main program options. For more details of the command-line and configuration options, see the HTML documentation (see below).</p>
<h3>Options for httex, htlatex and httexi</h3>
<p> <code>httex</code>, <code>htlatex</code> and <code>httexi</code> are shell scripts that can be used to convert a file in the TeX/LaTeX/texinfo format into HTML. This TeX source file should be like any other TeX source file normally used to produce a <i>.dvi</i> file by processing with TeX and friends. The name of such a file is the mandatory file argument for each script. This is followed by up to three optional arguments (delimited with quotation marks). These arguments, which are <code>not</code> required for typical usage, are as follows:</p>
<dl>
<dt>1.</p>
<dd> The first argument is a list of options for the <i>tex4ht.sty</i> style file (used with tex or latex), separated with commas. See the HTML documentation for the list of options available. The <i>.log</i> file generated by tex/latex also includes summaries of some of the options available. If not empty, this argument must start with <code>html</code> or <code>xhtml</code>. Additional options could be <code>mathml</code> or <code>docbook</code> to indicate appropriate style of output.</p>
<dt>2.</p>
<dd> This argument is used to select tagged sections of <i>tex4ht.env</i> that specifies the font files (*.htf) to use. This corresponds to the <code>-c</code> option for the command <i>tex4ht</i> as explained below. Examples include <code>unicode</code> or <code>mozilla</code>.</p>
<dt>3.</p>
<dd> This argument lists options for the <i>t4ht</i> program as explained below.</dl>
<p> See the HTML documentation for more details and examples. </p>
<p> Similar scripts are available within the directory <i>/usr/share/tex4ht</i> for generating other kinds of hypertext output. It is also possible to use the perl script <code>mk4ht</code> as explained below.</p>
<h3>Options for mk4ht</h3>
<p> <code>mk4ht</code> is a perl script that can be used to convert TeX source files from numerous dialects of TeX into different hypertext variants. This script takes two mandatory arguments: the name of the command to run and the file to run it on. Each possible command is of the form &quot;&lt;variant&gt;&lt;dialect&gt;&quot;: so for example <i>xhmlatex</i> denotes a LaTeX source that needs to be converted to XHTML with MathML extensions. The possible names for commands can be found by listing the directory <i>/usr/share/tex4ht.</i> The three optional arguments to <code>mk4ht</code> are identical to those outlined above for <code>httex</code>, htlatex<code> and </code>httexi<code>.</code> In fact, the command <code>htlatex</code> foo is identical to <code>mk4ht</code> htlatex<code> foo</code> except that the former is shorter to type! However, <code>mk4ht</code> can be configured to shorten the command line as follows. </p>
<p> Each user can create the configuration file <i>mk4ht.cfg</i> or <i>.mk4ht</i> in the home or working directory to configure commonly used options for mk4ht; in addition options to clean up temporary files can also be added to this configuration file. Running the command <code>mk4ht</code> without any arguments will summarise the use of this user configuration file.</p>
<h3>Options for ht</h3>
<p> <code>ht</code> is a small shell script that is used to run the tex4ht programs. It has two compulsory arguments, as follows:</p>
<dl>
<dt>1.</p>
<dd> The TeX command name to run, usually either <code>tex</code> or <code>latex</code>.</p>
<dt>2.</p>
<dd> The input file name (with or without extension).</dl>
<p> It may take any additional options, which will be passed on to the call to <code>t4ht</code>.</p>
<h3>General directory/file search options</h3>
<p> Several of the options detailed below relate to setting directory paths to find particular kinds of files. Note the following when specifying directories for the programs:</p>
<dl>
<dt>1.</p>
<dd> There must be no space between the option letter (eg, <code>-t</code>) and the directory/file name.</p>
<dt>2.</p>
<dd> The directory name must end with a trailing slash (<code>/</code>, or <code>/!</code> &#8211; see below).</p>
<dt>3.</p>
<dd> You can add an exclamation mark (<code>!</code>) to the end of the directory name, to enable sub-directory searching.</p>
<dt>4.</p>
<dd> Only one directory can be specified at a time. To search multiple directories, either use the sub-directory searching facility or repeat the option. (The directory search options can be repeated as often as required.)</p>
<dt>5.</p>
<dd> When compiled with <code>kpathsea</code> (as in the Debian package), the path-searching is in part taken over by kpathsea. On a Debian system see <i>/usr/share/doc/tex4ht/README.kpathsea</i> for more information on path-searching in a kpathsea-enabled tex4ht.</dl>
<p> As well as command-line options, most of these options can (and normally should) be set in the configuration file <i>tex4ht.env</i>. The format within this file is similar, but without using a hyphen before the option letter. See the HTML documentation for more details on the configuration options available. The file <i>tex4ht.env</i> can be superseded on a per-directory and/or a per-user basis as explained in the HTML documentation. On a Debian system see <i>/usr/share/doc/tex4ht/README.Debian</i> as well.</p>
<h3>Options for tex4ht</h3>
<dl>
<dt><code>-c</code><i>tag-name</i></p>
<dd> Certain lines within the <i>tex4ht.env</i> configuration file can be marked with tags. These lines (typically <i>htf-font-dir</i> search lines) will be omitted unless specifically requested by specifying the tag name on the tex4ht command line. If not used, a command-line option of <code>-c</code><i>default</i> is assumed. (See the supplied tex4ht.env file for examples of tagged sections.)</p>
<dt><code>-e</code><i>env-file</i></p>
<dd> Specify address of the tex4ht configuration file <i>tex4ht.env</i>.</p>
<dt><code>-g</code><i>bitmap-file-ext</i></p>
<dd> Set the extension of bitmap images to <i>bitmap-file-ext</i> instead of the default <i>.png</i>. Note that the extension should begin with a dot (<code>.</code>). Note also that this option only affects images generated automatically for symbol fonts, and not images generated with the <code>\Picture</code> macro of tex4ht.</p>
<dt><code>-he</code></p>
<dd> Trace errors and warnings (produces verbose output).</p>
<dt><code>-hg</code></p>
<dd> Trace groups</p>
<dt><code>-hs</code></p>
<dd> Trace <code>\special</code>s.</p>
<dt><code>-hV</code></p>
<dd> Trace search path for tex4ht.env configuration file</p>
<dt><code>-hF</code></p>
<dd> Trace search path for <i>.htf</i> font files</p>
<dt><code>-hv</code></p>
<dd> Dump contents of found tex4ht.env configuration file to stderr (for debugging)</p>
<dt><code>-hf</code></p>
<dd> Dump contents of each <i>.htf</i> font file found to stderr (for debugging)</p>
<dt><code>-i</code><i>htf-font-dir</i></p>
<dd> Set directory for HTF font files (used by tex4ht) to <i>htf-font-dir</i>.</p>
<dt><code>-l</code><i>bookkeeping-file</i></p>
<dd> Specify name of the file listing cache used to speed up filename lookups (ignored if compiled with kpathsea support)</p>
<dt><code>-P</code><i>filter</i></p>
<dd> Restrict system calls requested in the source (La)TeX files to utilities whose names have <i>filter</i> as a prefix. Use a single asterisk as <i>filter</i> to allow any system calls.</p>
<dt><code>-t</code><i>tfm-font-dir</i></p>
<dd> Set directory for TFM font files to <i>tfm-font-dir</i> (ignored if compiled with kpathsea support).</p>
<dt><code>-u10</code></p>
<dd> Use base 10 encoding for unicode characters.</p>
<dt><code>-utf8</code></p>
<dd> Use utf-8 encoding for unicode characters.</p>
<dt><code>-xs</code></p>
<dd> Use 8.3 (MSDOS style) file names for the generated PNG files.</dl>
<h3>Options for t4ht</h3>
<dl>
<dt><code>-c</code><i>tag-name</i></p>
<dd> Certain lines within the <i>tex4ht.env</i> configuration file can be marked with tags. These lines (typically scripts for post-processing files) will be omitted unless specifically requested by specifying the tag name on the tex4ht command line. If not used, a command-line option of <code>-c</code><i>default</i> is assumed. (See the supplied tex4ht.env file for examples of tagged sections.)</p>
<dt><code>-d</code><i>out-dir</i></p>
<dd> Output files to directory <i>out-dir</i>, instead of to the current directory.</p>
<dt><code>-e</code><i>env-file</i></p>
<dd> Specify address of the tex4ht configuration file <i>tex4ht.env</i>.</p>
<dt><code>-i</code></p>
<dd> Generate verbose debugging output.</p>
<dt><code>-m</code><i>mode</i></p>
<dd> Create any new output files with access mode as indicated by <i>mode</i>. The <i>mode</i> should be a numeric mode, as used by the <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1) command.</p>
<dt><code>-M</code><i>mode</i></p>
<dd> As <i>-m</i> but change all mode of all output files (including reused bitmaps).</p>
<dt><code>-p</code></p>
<dd> Do not convert pictures (ie, images generated with macros like <code>\Picture</code>, not characters in symbol fonts that will be automatically converted into a graphic file).</p>
<dt><code>-r</code></p>
<dd> Do not resuse existing bitmaps of glyphs (for characters in symbol fonts etc), but instead generate all bitmaps anew.</p>
<dt><code>-S</code><i>filter</i></p>
<dd> Restrict system calls requested in the source (La)TeX files to utilities whose names have <i>filter</i> as a prefix. Use a single asterisk as <i>filter</i> to allow any system calls.</p>
<dt><code>-X</code><i>field-content</i></p>
<dd> Scripts for post-processing of files can be specified in tex4ht.env. If these scripts refer to a field %%3, content for that field can be set with this command-line option.</p>
<dt><code>-.</code><i>field-content</i></p>
<dd> Scripts for post-processing of groups of files with a particular extension can be specified in tex4ht.env. If these scripts refer to a field %%2, content for that field can be set with this command-line option.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/tex4ht/tex4ht.env</i></p>
<dd> Configuration file for tex4ht. This file is commented within the file, and some additional notes are in <i>/usr/share/doc/tex4ht/README.kpathsea</i> on a Debian system. Further explanation is available in the HTML documentation.</p>
<dt><i>/etc/texmf/texmf.cnf</i></p>
<dd> Global configuration file for all TeX-related programs using the kpathsea path searching library. The variables <i>TEX4HTINPUTS</i>, <i>T4HTINPUTS</i> and <i>TEX4HTFONTSET</i> within this file relate to file searching within <code>tex4ht</code> and <code>t4ht.</code> These variables may also be set in the environment, outwith /etc/texmf/texmf.cnf.</p>
<dt><i>/usr/share/texmf/tex4ht/ht-fonts/*.htf</i></p>
<dd> Hypertext font files used by tex4ht.</p>
<dt><i>/usr/share/texmf/tex/generic/tex4ht/tex4ht.sty</i> and <i>/usr/share/texmf/tex/generic/tex4ht/*.4ht</i></p>
<dd> Macro files used by tex or latex when using tex4ht to generate HTML output.</p>
<dt><i>/usr/share/tex4ht/*</i></p>
<dd> Shell scripts for generating different kinds of hypertext output from tex or latex sources.</dl>
<h2>SEE ALSO</h2>
<p> The use of the tex4ht macros is documented in the HTML documentation at the web site given below. </p>
<p> <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1), <code><a href="/docs/linux/man/1-latex/">latex</a></code>(1), <code><a href="/docs/linux/man/1-amstex/">amstex</a></code>(1), <code><a href="/docs/linux/man/1-kpsewhich/">kpsewhich</a></code>(1), <i><a rel="nofollow" href="http://www.cse.ohio-state.edu/~gurari/TeX4ht/mn.html">http://www.cse.ohio-state.edu/~gurari/TeX4ht/mn.html</a></i></p>
<h2>BUGS</h2>
<p> This manual page is not complete. Users should refer to the HTML documentation for fuller details of the configuration options and for details of the use of the tex4ht style files. <code>tex4ht</code> is still a work in progress, so bug reports and requests are very welcome: contact Eitan Gurari &lt;gurari [at] cis.ohio-state.edu&gt;.</p>
<h2>AUTHOR</h2>
<p> This manual page was originally written by Andrew Gray &lt;ajpg [at] debian.org&gt; (and then modified by Kapil Paranjape), for the Debian GNU/Linux system (but it may be used by others). </p>
<p> The <code>tex4ht</code> programs and macro files were written by Eitan Gurari &lt;gurari [at] cis.ohio-state.edu&gt;. The author maintains a home page at <i><a rel="nofollow" href="http://www.cse.ohio-state.edu/~gurari/TeX4ht/">http://www.cse.ohio-state.edu/~gurari/TeX4ht/</a></i> </p>
<h2>Index</h2>
