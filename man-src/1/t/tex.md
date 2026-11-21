---
title: "tex(1)"
name: "tex"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tex/"
description: "tex, initex – text formatting and typesetting"
---

<h2 class="name">NAME</h2>
<p> tex, initex &#8211; text formatting and typesetting </p>
<h2>SYNOPSIS</h2>
<p> <code>tex</code> [<i>options</i>] [<i></i><code>&amp;</code>format] [<i>file</i>|<i></i><code>\</code>commands]</p>
<h2>DESCRIPTION</h2>
<p> Run the TeX typesetter on <i>file</i>, usually creating <i>file.dvi</i>. If the file argument has no extension, &quot;.tex&quot; will be appended to it. Instead of a filename, a set of TeX commands can be given, the first of which must start with a backslash. With a <code>&amp;</code><i>format</i> argument TeX uses a different set of precompiled commands, contained in <i>format</i><code>.fmt</code>; it is usually better to use the <code>-fmt</code> <i>format</i> option instead. </p>
<p> TeX formats the interspersed text and commands contained in the named files and outputs a typesetter independent file (called <i>DVI</i>, which is short for <i>DeVice Independent</i>). TeX&#8217;s capabilities and language are described in <i>The TeXbook</i>. TeX is normally used with a large body of precompiled macros, and there are several specific formatting systems, such as LaTeX, which require the support of several macro files. </p>
<p> This version of TeX looks at its command line to see what name it was called under. If they exist, then both <code>initex</code> and <code>virtex</code> are symbolic links to the <code>tex</code> executable. When called as <code>initex</code> (or when the <code>-ini</code> option is given) it can be used to precompile macros into a <i>.fmt</i> file. When called as <code>virtex</code> it will use the <i>plain</i> format. When called under any other name, TeX will use that name as the name of the format to use. For example, when called as <code>tex</code> the <i>tex</i> format is used, which is identical to the <i>plain</i> format. The commands defined by the <i>plain</i> format are documented in <i>The TeXbook</i>. Other formats that are often available include <i>latex</i> and <i>amstex</i>. </p>
<p> The non-option command line arguments to the TeX program are passed to it as the first input line. (But it is often easier to type extended arguments as the first input line, since UNIX shells tend to gobble up or misinterpret TeX&#8217;s favorite symbols, like backslashes, unless you quote them.) As described in <i>The TeXbook</i>, that first line should begin with a filename, a <i></i> <i>\controlsequence</i>, or a <i>&amp;formatname</i>. </p>
<p> The normal usage is to say </p>
<pre><code>tex paper
</code></pre>
<p> to start processing <i>paper.tex</i>. The name <i>paper</i> will be the ``jobname&#8217;&#8216;, and is used in forming output filenames. If TeX doesn&#8217;t get a filename in the first line, the jobname is <i>texput</i>. When looking for a file, TeX looks for the name with and without the default extension (<i>.tex</i>) appended, unless the name already contains that extension. If <i>paper</i> is the ``jobname&#8217;&#8216;, a log of error messages, with rather more detail than normally appears on the screen, will appear in <i>paper.log</i>, and the output file will be in <i>paper.dvi</i>. </p>
<p> This version of TeX can look in the first line of the file <i>paper.tex</i> to see if it begins with the magic sequence <i>%&amp;</i>. If the first line begins with <code>%&amp;</code><i>format</i> <code>-translate-file</code><i>&nbsp;tcxname</i> then TeX will use the named format and translation table <i>tcxname</i> to process the source file. Either the format name or the <code>-translate-file</code> specification may be omitted, but not both. This overrides the format selection based on the name by which the program is invoked. The <code>-parse-first-line</code> option or the <code>parse_first_line</code> configuration variable controls whether this behaviour is enabled. </p>
<p> The <i>e</i> response to TeX&#8217;s error prompt causes the system default editor to start up at the current line of the current file. The environment variable TEXEDIT can be used to change the editor used. It may contain a string with &quot;%s&quot; indicating where the filename goes and &quot;%d&quot; indicating where the decimal line number (if any) goes. For example, a TEXEDIT string for <code>emacs</code> can be set with the <code>sh</code> command </p>
<pre><code>
 TEXEDIT=&quot;emacs +%d %s&quot;; export TEXEDIT 
</code></pre>
<p> A convenient file in the library is <i>null.tex</i>, containing nothing. When TeX can&#8217;t find a file it thinks you want to input, it keeps asking you for another filename; responding `null&#8217; gets you out of the loop if you don&#8217;t want to input anything. You can also type your EOF character (usually control-D). </p>
<h2>OPTIONS</h2>
<p> This version of TeX understands the following command line options. </p>
<dl>
<dt><code>-cnf-line</code><i>&nbsp;string</i></dt>
<dd> <p> Parse <i>string</i> as a <i>texmf.cnf</i> configuration line. See the Kpathsea manual. </p>
 </dd>
<dt><code>-enc</code></dt>
<dd> <p> Enable the encTeX extensions. This option is only effective in combination with <code>-ini</code>. For documentation of the encTeX extensions see <code><a rel="nofollow" href="http://www.olsak.net/enctex.html">http://www.olsak.net/enctex.html</a></code>. </p>
 </dd>
<dt><code>-file-line-error</code></dt>
<dd> <p> Print error messages in the form <i>file:line:error</i> which is similar to the way many compilers format them. </p>
 </dd>
<dt><code>-no-file-line-error</code></dt>
<dd> <p> Disable printing error messages in the <i>file:line:error</i> style. </p>
 </dd>
<dt><code>-file-line-error-style</code></dt>
<dd> <p> This is the old name of the <code>-file-line-error</code> option. </p>
 </dd>
<dt><code>-fmt</code><i>&nbsp;format</i></dt>
<dd> <p> Use <i>format</i> as the name of the format to be used, instead of the name by which TeX was called or a <i>%&amp;</i> line. </p>
 </dd>
<dt><code>-halt-on-error</code></dt>
<dd> <p> Exit with an error code when an error is encountered during processing. </p>
 </dd>
<dt><code>-help</code></dt>
<dd> <p> Print help message and exit. </p>
 </dd>
<dt><code>-ini</code></dt>
<dd> <p> Start in <i>INI</i> mode, which is used to dump formats. The <i>INI</i> mode can be used for typesetting, but no format is preloaded, and basic initializations like setting catcodes may be required. </p>
 </dd>
<dt><code>-interaction</code><i>&nbsp;mode</i></dt>
<dd> <p> Sets the interaction mode. The mode can be either <i>batchmode</i>, <i>nonstopmode</i>, <i>scrollmode</i>, and <i>errorstopmode</i>. The meaning of these modes is the same as that of the corresponding \commands. </p>
 </dd>
<dt><code>-ipc</code></dt>
<dd> <p> Send DVI output to a socket as well as the usual output file. Whether this option is available is the choice of the installer. </p>
 </dd>
<dt><code>-ipc-start</code></dt>
<dd> <p> As <code>-ipc</code>, and starts the server at the other end as well. Whether this option is available is the choice of the installer. </p>
 </dd>
<dt><code>-jobname</code><i>&nbsp;name</i></dt>
<dd> <p> Use <i>name</i> for the job name, instead of deriving it from the name of the input file. </p>
 </dd>
<dt><code>-kpathsea-debug</code><i>&nbsp;bitmask</i></dt>
<dd> <p> Sets path searching debugging flags according to the bitmask. See the <i>Kpathsea</i> manual for details. </p>
 </dd>
<dt><code>-mktex</code><i>&nbsp;fmt</i></dt>
<dd> <p> Enable mktex <i>fmt</i>, where <i>fmt</i> must be either <i>tex</i> or <i>tfm</i>. </p>
 </dd>
<dt><code>-mltex</code></dt>
<dd> <p> Enable MLTeX extensions. Only effective in combination with <code>-ini</code>. </p>
 </dd>
<dt><code>-no-mktex</code><i>&nbsp;fmt</i></dt>
<dd> <p> Disable mktex <i>fmt</i>, where <i>fmt</i> must be either <i>tex</i> or <i>tfm</i>. </p>
 </dd>
<dt><code>-output-comment</code><i>&nbsp;string</i></dt>
<dd> <p> Use <i>string</i> for the <i>DVI</i> file comment instead of the date. </p>
 </dd>
<dt><code>-output-directory</code><i>&nbsp;directory</i></dt>
<dd> <p> Write output files in <i>directory</i> instead of the current directory. Look up input files in <i>directory</i> first, then along the normal search path. See also description of the TEXMFOUTPUT environment variable. </p>
 </dd>
<dt><code>-parse-first-line</code></dt>
<dd> <p> If the first line of the main input file begins with <i>%&amp;</i> parse it to look for a dump name or a <code>-translate-file</code> option. </p>
 </dd>
<dt><code>-no-parse-first-line</code></dt>
<dd> <p> Disable parsing of the first line of the main input file. </p>
 </dd>
<dt><code>-progname</code><i>&nbsp;name</i></dt>
<dd> <p> Pretend to be program <i>name</i>. This affects both the format used and the search paths. </p>
 </dd>
<dt><code>-recorder</code></dt>
<dd> <p> Enable the filename recorder. This leaves a trace of the files opened for input and output in a file with extension <i>.fls</i>. </p>
 </dd>
<dt><code>-shell-escape</code></dt>
<dd> <p> Enable the <code>\write18{</code><i>command</i><code>}</code> construct. The <i>command</i> can be any shell command. This construct is normally disallowed for security reasons. </p>
 </dd>
<dt><code>-no-shell-escape</code></dt>
<dd> <p> Disable the <code>\write18{</code><i>command</i><code>}</code> construct, even if it is enabled in the <i>texmf.cnf</i> file. </p>
 </dd>
<dt><code>-src-specials</code></dt>
<dd> <p> Insert source specials into the <i>DVI</i> file. </p>
 </dd>
<dt><code>-src-specials</code><i>&nbsp;where</i></dt>
<dd> <p> Insert source specials in certain places of the <i>DVI</i> file. <i>where</i> is a comma-separated value list: <i>cr</i>, <i>display</i>, <i>hbox</i>, <i>math</i>, <i>par</i>, <i>parent</i>, or <i>vbox</i>. </p>
 </dd>
<dt><code>-translate-file</code><i>&nbsp;tcxname</i></dt>
<dd> <p> Use the <i>tcxname</i> translation table to set the mapping of input characters and re-mapping of output characters. </p>
 </dd>
<dt><code>-default-translate-file</code><i>&nbsp;tcxname</i></dt>
<dd> <p> Like <code>-translate-file</code> except that a <i>%&amp;</i> line can overrule this setting. </p>
 </dd>
<dt><code>-version</code></dt>
<dd> <p> Print version information and exit. </p>
 </dd></dl>
<h2>ENVIRONMENT</h2>
<p> See the Kpathsearch library documentation (the `Path specifications&#8217; node) for precise details of how the environment variables are used. The <code>kpsewhich</code> utility can be used to query the values of the variables. </p>
<p> One caveat: In most TeX formats, you cannot use ~ in a filename you give directly to TeX, because ~ is an active character, and hence is expanded, not taken as part of the filename. Other programs, such as Metafont, do not have this problem. </p>
<dl>
<dt><code>TEXMFOUTPUT</code></dt>
<dd> <p> Normally, TeX puts its output files in the current directory. If any output file cannot be opened there, it tries to open it in the directory specified in the environment variable TEXMFOUTPUT. There is no default value for that variable. For example, if you say <i>tex paper</i> and the current directory is not writable, if TEXMFOUTPUT has the value <i>/tmp</i>, TeX attempts to create <i>/tmp/paper.log</i> (and <i>/tmp/paper.dvi</i>, if any output is produced.) TEXMFOUTPUT is also checked for input files, as TeX often generates files that need to be subsequently read; for input, no suffixes (such as ``.tex&#8217;&#8216;) are added by default, the input name is simply checked as given. </p>
 </dd>
<dt><code>TEXINPUTS</code></dt>
<dd> <p> Search path for <i>\input</i> and <i>\openin</i> files. This should probably start with ``.&#8216;&#8216;, so that user files are found before system files. An empty path component will be replaced with the paths defined in the <i>texmf.cnf</i> file. For example, set TEXINPUTS to &quot;.:/home/user/tex:&quot; to prepend the current directory and ``/home/user/tex&#8217;&#8216; to the standard search path. </p>
 </dd>
<dt><code>TEXFORMATS</code></dt>
<dd> <p> Search path for format files. </p>
 </dd>
<dt><code>TEXPOOL</code></dt>
<dd> <p> search path for <code>tex</code> internal strings. </p>
 </dd>
<dt><code>TEXEDIT</code></dt>
<dd> <p> Command template for switching to editor. The default, usually <code>vi</code>, is set when TeX is compiled. </p>
 </dd>
<dt><code>TFMFONTS</code></dt>
<dd> <p> Search path for font metric (<i>.tfm</i>) files. </p>
 </dd></dl>
<p> Notes for Debian developers: please keep in mind, that this version of the TeX interpreter ignores the <code>SOURCE_DATE_EPOCH</code> variable. Instead the current timestamp is written into the <i>DVI</i> file. If you need a reproducible time stamp, please use any engine based on pdfTeX, e.g., etex, pdftex, latex, pdflatex.  </p>
<h2>FILES</h2>
<p> The location of the files mentioned below varies from system to system. Use the <code>kpsewhich</code> utility to find their locations. </p>
<dl>
<dt><i>texmf.cnf</i></dt>
<dd> <p> Configuration file. This contains definitions of search paths as well as other configuration parameters like <code>parse_first_line</code>. </p>
 </dd>
<dt><i>tex.pool</i></dt>
<dd> <p> Text file containing TeX&#8217;s internal strings. </p>
 </dd>
<dt><i>texfonts.map</i></dt>
<dd> <p> Filename mapping definitions. </p>
 </dd>
<dt><i>*.tfm</i></dt>
<dd> <p> Metric files for TeX&#8217;s fonts. </p>
 </dd>
<dt><i>*.fmt</i></dt>
<dd> <p> Predigested TeX format (.fmt) files. </p>
 </dd>
<dt><i>$TEXMFMAIN/tex/plain/base/plain.tex</i></dt>
<dd> <p> The basic macro package described in the TeXbook. <br />
 </p>
 </dd></dl>
<h2>NOTES</h2>
<p> This manual page is not meant to be exhaustive. The complete documentation for this version of TeX can be found in the info manual <i>Web2C: A TeX implementation</i>.  </p>
<h2>BUGS</h2>
<p> This version of TeX implements a number of optional extensions. In fact, many of these extensions conflict to a greater or lesser extent with the definition of TeX. When such extensions are enabled, the banner printed when TeX starts is changed to print <code>TeXk</code> instead of <code>TeX</code>. </p>
<p> This version of TeX fails to trap arithmetic overflow when dimensions are added or subtracted. Cases where this occurs are rare, but when it does the generated <i>DVI</i> file will be invalid.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mf/">mf</a></code>(1), <br />
 Donald E. Knuth, <i>The TeXbook</i>, Addison-Wesley, 1986, ISBN 0-201-13447-0. <br />
 Leslie Lamport, <i>LaTeX &#8211; A Document Preparation System</i>, Addison-Wesley, 1985, ISBN 0-201-15790-X. <br />
 K. Berry, <i>Eplain: Expanded plain TeX</i>, <a rel="nofollow" href="https://tug.org/eplain">https://tug.org/eplain</a> <br />
 Michael Spivak, <i>The Joy of TeX</i>, 2nd edition, Addison-Wesley, 1990, ISBN 0-8218-2997-1. <br />
 <i>TUGboat</i> (the journal of the TeX Users Group). <a rel="nofollow" href="https://tug.org/TUGboat">https://tug.org/TUGboat</a>  </p>
<h2>TRIVIA</h2>
<p> TeX, pronounced properly, rhymes with ``blecchhh.&#8216;&#8216; The proper spelling in typewriter-like fonts is ``TeX&#8217;&#8216; and not ``TEX&#8217;&#8216; or ``tex.&#8216;&#8216;  </p>
<h2>AUTHORS</h2>
<p> TeX was created by Donald E. Knuth, who implemented it using his Web system for Pascal programs. It was ported to Unix at Stanford by Howard Trickey, and at Cornell by Pavel Curtis. The version now offered with the Unix TeX distribution is that generated by the Web to C system (<code>web2c</code>), originally written by Tomas Rokicki and Tim Morgan. </p>
<p> The encTeX extensions were written by Petr Olsak. </p>
