---
title: "pdfmex(1)"
name: "pdfmex"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdfmex/"
description: "pdftex – PDF output from TeX"
---
<h2>SYNOPSIS</h2>
<p> <code>pdftex</code> [<i>options</i>] [<i></i><code>&amp;</code>format] [<i>file</i>|<i></i><code>\</code>commands]  </p>
<h2>DESCRIPTION</h2>
<p> Run the pdfTeX typesetter on <i>file</i>, usually creating <i>file.pdf</i>. If the file argument has no extension, &quot;.tex&quot; will be appended to it. Instead of a filename, a set of pdfTeX commands can be given, the first of which must start with a backslash. With a <code>&amp;</code><i>format</i> argument pdfTeX uses a different set of precompiled commands, contained in <i>format</i><code>.fmt</code>; it is usually better to use the <code>-fmt</code> <i>format</i> option instead. </p>
<p> pdfTeX is a version of TeX, with the e-TeX extensions, that can create PDF files as well as DVI files. </p>
<p> In DVI mode, pdfTeX can be used as a complete replacement for the TeX engine. </p>
<p> The typical use of pdfTeX is with a pregenerated formats for which PDF output has been enabled. The <code>pdftex</code> command uses the equivalent of the plain TeX format, and the <code>pdflatex</code> command uses the equivalent of the LaTeX format. To generate formats, use the <code>-ini</code> switch. </p>
<p> The <code>pdfinitex</code> and <code>pdfvirtex</code> commands are pdfTeX&#8217;s analogues to the <code>initex</code> and <code>virtex</code> commands. In this installation, if the links exist, they are symbolic links to the <code>pdftex</code> executable. </p>
<p> In PDF mode, pdfTeX can natively handle the <i>PDF</i>, <i>JPG</i>, <i>JBIG2</i>, and <i>PNG</i> graphics formats. pdfTeX cannot include PostScript or Encapsulated PostScript (EPS) graphics files; first convert them to PDF using <code><a href="/docs/linux/man/1-epstopdf/">epstopdf</a></code>(1). pdfTeX&#8217;s handling of its command-line arguments is similar to that of of the other TeX programs in the <i>web2c</i> implementation. </p>
<p> Starting with version 1.40, pdfTeX incorporates the e-TeX extensions, and pdfeTeX is just a copy of pdfTeX. See <code><a href="/docs/linux/man/1-etex/">etex</a></code>(1).  </p>
<h2>OPTIONS</h2>
<p> This version of pdfTeX understands the following command line options. </p>
<dl>
<dt><code>-cnf-line</code><i>&nbsp;string</i></dt>
<dd> <p> Parse <i>string</i> as a <i>texmf.cnf</i> configuration line. See the Kpathsea manual. </p>
 </dd>
<dt><code>-draftmode</code></dt>
<dd> <p> Sets \pdfdraftmode so pdfTeX doesn&#8217;t write a PDF and doesn&#8217;t read any included images, thus speeding up execution. </p>
 </dd>
<dt><code>-enc</code></dt>
<dd> <p> Enable the encTeX extensions. This option is only effective in combination with <code>-ini</code>. For documentation of the encTeX extensions see <a rel="nofollow" href="http://www.olsak.net/enctex.html.">http://www.olsak.net/enctex.html.</a> </p>
 </dd>
<dt><code>-etex</code></dt>
<dd> <p> Enable the e-TeX extensions. This option is only effective in combination with <code>-ini</code>. See <code><a href="/docs/linux/man/1-etex/">etex</a></code>(1). </p>
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
<dd> <p> Use <i>format</i> as the name of the format to be used, instead of the name by which pdfTeX was called or a <i>%&amp;</i> line. </p>
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
<dd> <p> Send DVI or PDF output to a socket as well as the usual output file. Whether this option is available is the choice of the installer. </p>
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
<dd> <p> In DVI mode, use <i>string</i> for the DVI file comment instead of the date. This option is ignored in PDF mode. </p>
 </dd>
<dt><code>-output-directory</code><i>&nbsp;directory</i></dt>
<dd> <p> Write output files in <i>directory</i> instead of the current directory. Look up input files in <i>directory</i> first, the along the normal search path. </p>
 </dd>
<dt><code>-output-format</code><i>&nbsp;format</i></dt>
<dd> <p> Set the output format mode, where <i>format</i> must be either <i>pdf</i> or <i>dvi</i>. This also influences the set of graphics formats understood by pdfTeX. </p>
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
<dd> <p> Enable the \write18{<i>command</i>} construct. The <i>command</i> can be any shell command. This construct is normally disallowed for security reasons. </p>
 </dd>
<dt><code>-no-shell-escape</code></dt>
<dd> <p> Disable the \write18{<i>command</i>} construct, even if it is enabled in the <i>texmf.cnf</i> file. </p>
 </dd>
<dt><code>-shell-restricted</code></dt>
<dd> <p> Enable restricted \write18{}, as explained in the ``Shell escapes&#8217;&#8216; section of the Web2c Texinfo manual. </p>
 </dd>
<dt><code>-src-specials</code></dt>
<dd> <p> In DVI mode, insert source specials into the DVI file. This option is ignored in PDF mode. </p>
 </dd>
<dt><code>-src-specials</code><i>&nbsp;where</i></dt>
<dd> <p> In DVI mode, insert source specials in certain places of the DVI file. The <i>where</i> argument is a comma-separated value list: <i>cr</i>, <i>display</i>, <i>hbox</i>, <i>math</i>, <i>par</i>, <i>parent</i>, or <i>vbox</i>. This option is ignored in PDF mode. </p>
 </dd>
<dt><code>-synctex</code><i>&nbsp;NUMBER</i></dt>
<dd> <p> generate SyncTeX data for previewers according to bits of NUMBER. See the <i>synctex</i> manual page for details. </p>
 </dd>
<dt><code>-translate-file</code><i>&nbsp;tcxname</i></dt>
<dd> <p> Use the <i>tcxname</i> translation table to set the mapping of input characters and re-mapping of output characters. </p>
 </dd>
<dt><code>-default-translate-file</code><i>&nbsp;tcxname</i></dt>
<dd> <p> Like <code>-translate-file</code> except that a <i>%&amp;</i> line can overrule this setting. </p>
 </dd>
<dt><code>-version</code></dt>
<dd> <p> Print version information and exit. </p>
 </dd>
<dt><code>-8bit</code></dt>
<dd> <p> make all characters printable by default. </p>
 </dd></dl>
<h2>ENVIRONMENT</h2>
<p> See the Kpathsea library documentation (e.g., the `Path specifications&#8217; node) for precise details of how the environment variables are used. The <code>kpsewhich</code> utility can be used to query the values of the variables. </p>
<p> One caveat: In most pdfTeX formats, you cannot use ~ in a filename you give directly to pdfTeX, because ~ is an active character in TeX, and hence is expanded, not taken as part of the filename. Other programs, such as Metafont, do not have this problem. </p>
<dl>
<dt><code>TEXMFOUTPUT</code></dt>
<dd> <p> Normally, pdfTeX puts its output files in the current directory. If any output file cannot be opened there, it tries to open it in the directory specified in the environment variable TEXMFOUTPUT. There is no default value for that variable. For example, if you say <i>pdftex paper</i> and the current directory is not writable and TEXMFOUTPUT has the value <i>/tmp</i>, pdfTeX attempts to create <i>/tmp/paper.log</i> (and <i>/tmp/paper.pdf</i>, if any output is produced.) TEXMFOUTPUT is also checked for input files, as TeX often generates files that need to be subsequently read; for input, no suffixes (such as ``.tex&#8217;&#8216;) are added by default, the input name is simply checked as given. </p>
 </dd>
<dt><code>TEXINPUTS</code></dt>
<dd> <p> Search path for <i>\input</i> and <i>\openin</i> files. This normally starts with ``.&#8216;&#8216;, so that user files are found before system files. An empty path component will be replaced with the paths defined in the <i>texmf.cnf</i> file. For example, set TEXINPUTS to &quot;.:/home/user/tex:&quot; to prepend the current directory and ``/home/user/tex&#8217;&#8216; to the standard search path. </p>
 </dd>
<dt><code>TEXFORMATS</code></dt>
<dd> <p> Search path for format files. </p>
 </dd>
<dt><code>TEXEDIT</code></dt>
<dd> <p> Command template for switching to editor. The default, usually <code>vi</code>, is set when pdfTeX is compiled. </p>
 </dd>
<dt><code>TFMFONTS</code></dt>
<dd> <p> Search path for font metric (<i>.tfm</i>) files. </p>
 </dd>
<dt><code>SOURCE_DATE_EPOCH</code></dt>
<dd> <p> If set, its value, taken to be in epoch-seconds, will be used for the timestamps in the PDF output, such as the CreationDate and ModDate keys. This is useful for making reproducible builds. </p>
 </dd>
<dt><code>FORCE_SOURCE_DATE</code></dt>
<dd> <p> If set to the value &quot;1&quot;, the time-related TeX primitives (<i>\year</i>, <i>\month</i>, <i>\day</i>, <i>\time</i>) are also initialized from the value of SOURCE_DATE_EPOCH. This is not recommended if there is any viable alternative. <br />
 pdfTeX also has several primitives to support reproducible builds, which are preferable to setting these environment variables; see the main manual. </p>
 </dd></dl>
<p> Many, many more environment variables may be consulted related to path searching. See the Kpathsea manual.  </p>
<h2>FILES</h2>
<p> The location of the files mentioned below varies from system to system. Use the <code>kpsewhich</code> utility to find their locations. </p>
<dl>
<dt><i>pdftex.map</i></dt>
<dd> <p> Font name mapping definitions. </p>
 </dd>
<dt><i>*.tfm</i></dt>
<dd> <p> Metric files for pdfTeX&#8217;s fonts. </p>
 </dd>
<dt><i>*.fmt</i></dt>
<dd> <p> Predigested pdfTeX format (.fmt) files. </p>
 </dd></dl>
<h2>NOTES</h2>
<h2>BUGS</h2>
<p> This version of pdfTeX fails to trap arithmetic overflow when dimensions are added or subtracted. Cases where this occurs are rare, but when it does the generated DVI or PDF file will be invalid.  </p>
<h2>AVAILABILITY</h2>
<p> pdfTeX is available for a large variety of machine architectures and operating systems. pdfTeX is part of all major TeX distributions. <br />
 The pdfTeX home page: <a rel="nofollow" href="http://www.pdftex.org.">http://www.pdftex.org.</a> <br />
 pdfTeX on CTAN: <a rel="nofollow" href="https://ctan.org/pkg/pdftex.">https://ctan.org/pkg/pdftex.</a> <br />
 pdfTeX mailing list for all discussion: <a rel="nofollow" href="https://lists.tug.org/pdftex.">https://lists.tug.org/pdftex.</a>  </p>
<h2>SEE ALSO</h2>
<p> This manual page is not meant to be exhaustive. The complete documentation for this version of pdfTeX can be found in the <i>pdfTeX user manual</i> and the Texinfo manuals <i>Kpathsea library</i>, <i>Web2C: A TeX implementation</i>. These manuals, and more, can be accessed from the pdfTeX or CTAN web pages given above. </p>
<p> Some related programs: <code><a href="/docs/linux/man/1-epstopdf/">epstopdf</a></code>(1), <code><a href="/docs/linux/man/1-etex/">etex</a></code>(1), <code><a href="/docs/linux/man/1-latex/">latex</a></code>(1), <code><a href="/docs/linux/man/1-luatex/">luatex</a></code>(1), <code><a href="/docs/linux/man/1-mptopdf/">mptopdf</a></code>(1), <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1), <code><a href="/docs/linux/man/1-mf/">mf</a></code>(1).  </p>
<h2>AUTHORS</h2>
<p> The primary authors of pdfTeX are Han The Thanh, Petr Sojka, Jiri Zlatuska, and Peter Breitenlohner (eTeX). </p>
<p> TeX was designed by Donald E. Knuth, who implemented it using his Web system for Pascal programs. It was ported to Unix at Stanford by Howard Trickey, and at Cornell by Pavel Curtis. The version now offered with the Unix TeX distribution is that generated by the Web to C system (<code>web2c</code>), originally written by Tomas Rokicki and Tim Morgan. The encTeX extensions were written by Petr Olsak. </p>
