---

title: "pdfjadetex(1)"
name: "pdfjadetex"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdfjadetex/"
description: "pdfjadetex – PDF output from JadeTeX"
---

<p> pdfjadetex - PDF output from JadeTeX </p>
<h2>SYNOPSIS</h2>
<p> <code>pdfjadetex</code> [<i>options</i>] [<i>commands</i>]  </p>
<h2>DESCRIPTION</h2>
<p> This manual page was derived from the manual page for pdfTeX and is not meant to be exhaustive. The complete documentation for this version of TeX can be found in the info file or manual <i>Web2C: A TeX implementation</i>. </p>
<p> pdfjadeTeX is a version of TeX that can create <i>PDF</i> files as well as <i>DVI</i> files. </p>
<p> The typical use of pdfjadeTeX is with a pregenerated formats for which PDF output has been enabled. The <code>pdfjadetex</code> command uses the equivalent of the plain JadeTeX format. </p>
<p> pdfjadeTeX&#8217;s handling of its command-line arguments is similar to that of LaTeX.  </p>
<h2>OPTIONS</h2>
<p> This version of pdfjadeTeX understands the following command line options. </p>
<dl>
<dt><code>--fmt</code><i>&nbsp;format</i></dt>
<dd> <p> Use <i>format</i> as the name of the format to be used, instead of the name by which pdfjadeTeX was called or a <i>%&amp;</i> line. </p>
 </dd>
<dt><code>--help</code></dt>
<dd> <p> Print help message and exit. </p>
 </dd>
<dt><code>--ini</code></dt>
<dd> <p> Be <code>pdfinitex</code>, for dumping formats; this is implicitly true if the program is called as <code>pdfinitex</code>. </p>
 </dd>
<dt><code>--interaction</code><i>&nbsp;mode</i></dt>
<dd> <p> Sets the interaction mode. The mode can be one of <i>batchmode</i>, <i>nonstopmode</i>, <i>scrollmode</i>, and <i>errorstopmode</i>. The meaning of these modes is the same as that of the corresponding \commands. </p>
 </dd>
<dt><code>--ipc</code></dt>
<dd> <p> Send DVI or PDF output to a socket as well as the usual output file. Whether this option is available is the choice of the installer. </p>
 </dd>
<dt><code>--ipc-start</code></dt>
<dd> <p> As <code>--ipc</code>, and starts the server at the other end as well. Whether this option is available is the choice of the installer. </p>
 </dd>
<dt><code>--kpathsea-debug</code><i>&nbsp;bitmask</i></dt>
<dd> <p> Sets path searching debugging flags according to the bitmask. See the <i>Kpathsea</i> manual for details. </p>
 </dd>
<dt><code>--maketex</code><i>&nbsp;fmt</i></dt>
<dd> <p> Enable mktex <i>fmt</i>, where <i>fmt</i> must be one of <i>tex</i> or <i>tfm</i>. </p>
 </dd>
<dt><code>--no-maketex</code><i>&nbsp;fmt</i></dt>
<dd> <p> Disable mktex <i>fmt</i>, where <i>fmt</i> must be one of <i>tex</i> or <i>tfm</i>. </p>
 </dd>
<dt><code>--output-comment</code><i>&nbsp;string</i></dt>
<dd> <p> Use <i>string</i> for the DVI file comment instead of the date. </p>
 </dd>
<dt><code>--progname</code><i>&nbsp;name</i></dt>
<dd> <p> Pretend to be program <i>name</i>. This affects both the format used and the search paths. </p>
 </dd>
<dt><code>--shell-escape</code></dt>
<dd> <p> Enable the <code>\write18{</code><i>command</i><code>}</code> construct. The <i>command</i> can be any Bourne shell command. This construct is normally disallowed for security reasons. </p>
 </dd>
<dt><code>--version</code></dt>
<dd> <p> Print version information and exit. </p>
 </dd></dl>
<h2>ENVIRONMENT</h2>
<p> See the Kpathsearch library documentation (the `Path specifications&#8217; node) for precise details of how the environment variables are used. The <code>kpsewhich</code> utility can be used to query the values of the variables. </p>
<p> One caveat: In most pdfjadeTeX formats, you cannot use ~ in a filename you give directly to pdfjadeTeX, because ~ is an active character, and hence is expanded, not taken as part of the filename. Other programs, such as Metafont, do not have this problem. </p>
<dl>
<dt>TEXMFOUTPUT</dt>
<dd> <p> Normally, pdfjadeTeX puts its output files in the current directory. If any output file cannot be opened there, it tries to open it in the directory specified in the environment variable TEXMFOUTPUT. There is no default value for that variable. For example, if you say <i>tex paper</i> and the current directory is not writable, if TEXMFOUTPUT has the value <i>/tmp</i>, pdfjadeTeX attempts to create <i>/tmp/paper.log</i> (and <i>/tmp/paper.pdf</i>, if any output is produced.) </p>
 </dd>
<dt>TEXINPUTS</dt>
<dd> <p> Search path for <i>\input</i> and <i>\openin</i> files. This should probably start with ``.&#8216;&#8216;, so that user files are found before system files. </p>
 </dd>
<dt>TEXFONTS</dt>
<dd> <p> Search path for font metric (<i>.tfm</i>) files. </p>
 </dd>
<dt>TEXFORMATS</dt>
<dd> <p> Search path for format files. </p>
 </dd>
<dt>TEXPOOL</dt>
<dd> <p> search path for <code>pdfinitex</code> internal strings. </p>
 </dd>
<dt>TEXEDIT</dt>
<dd> <p> Command template for switching to editor. The default, usually <code>vi</code>, is set when pdfjadeTeX is compiled. </p>
 </dd></dl>
<h2>FILES</h2>
<p> The location of the files mentioned below varies from system to system. Use the <code>kpsewhich</code> utility to find their locations. </p>
<dl>
<dt><i>pdfjadetex.pool</i></dt>
<dd> <p> Encoded text of pdfjadeTeX&#8217;s messages. </p>
 </dd>
<dt><i>texfonts.map</i></dt>
<dd> <p> Filename mapping definitions. </p>
 </dd>
<dt><i>*.tfm</i></dt>
<dd> <p> Metric files for pdfjadeTeX&#8217;s fonts. </p>
 </dd>
<dt><i>*.fmt</i></dt>
<dd> <p> Predigested pdfjadeTeX format (.fmt) files. <br/>
 </p>
 </dd></dl>
<h2>BUGS</h2>
<p> This version of pdfjadeTeX fails to trap arithmetic overflow when dimensions are added or subtracted. Cases where this occurs are rare, but when it does the generated <i>DVI</i> file will be invalid.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-jadetex/">jadetex</a></code>(1), <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1), <code><a href="/docs/linux/man/1-mf/">mf</a></code>(1), <code>undump</code>(1).  </p>
<h2>AUTHORS</h2>
<p> The author of pdfjadeTeX is Sebastian Rahtz. </p>
<p> This manual page was derived by Marcus Brinkmann for the Debian distribution from the pdfTeX manual page from the teTeX distribution by Thomas Esser. </p>
