---

title: "lambda(1)"
name: "lambda"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lambda/"
description: "omega, iniomega, viromega – extended unicode TeX"
---

<p> omega, iniomega, viromega - extended unicode TeX </p>
<h2>SYNOPSIS</h2>
<p> <code>omega</code> [<i>options</i>] [<code>&amp;</code> <i>format</i> ] [ <i>file</i> | <code>\</code> <i>commands</i> ]  </p>
<h2>DESCRIPTION</h2>
<p> Run the Omega typesetter on <i>file</i>, usually creating <i>file.dvi</i>. If the file argument has no extension, &quot;.tex&quot; will be appended to it. Instead of a filename, a set of Omega commands can be given, the first of which must start with a backslash. With a <code>&amp;</code><i>format</i> argument Omega uses a different set of precompiled commands, contained in <i>format.fmt</i>; it is usually better to use the <code>-fmt</code> <i>format</i> option instead. </p>
<p> Omega is a version of the TeX program modified for multilingual typesetting. It uses unicode, and has additional primitives for (among other things) bidirectional typesetting. </p>
<p> The <code>iniomega</code> and <code>viromega</code> commands are Omega&#8217;s analogues to the <code>initex</code> and <code>virtex</code> commands. In this installation, they are symlinks to the <code>omega</code> executable. </p>
<p> Omega&#8217;s command line options are similar to those of TeX. </p>
<p> Omega is experimental software.  </p>
<h2>OPTIONS</h2>
<p> This version of Omega understands the following command line options. </p>
<dl>
<dt><code>--oft</code><i>&nbsp;<wbr>format</i></dt>
<dd> <p> Use <i>format</i> as the name of the format to be used, instead of the name by which Omega was called or a <i>%&amp;</i> line. </p>
 </dd>
<dt><code>-halt-on-error</code></dt>
<dd> <p> Exit with an error code when an error is encountered during processing. </p>
 </dd>
<dt><code>--help</code></dt>
<dd> <p> Print help message and exit. </p>
 </dd>
<dt><code>--ini</code></dt>
<dd> <p> Be <code>iniomega</code>, for dumping formats; this is implicitly true if the program is called as <code>iniomega</code>. </p>
 </dd>
<dt><code>--interaction</code><i>&nbsp;<wbr>mode</i></dt>
<dd> <p> Sets the interaction mode. The mode can be one of <i>batchmode</i>, <i>nonstopmode</i>, <i>scrollmode</i>, and <i>errorstopmode</i>. The meaning of these modes is the same as that of the corresponding \commands. </p>
 </dd>
<dt><code>--ipc</code></dt>
<dd> <p> Send DVI output to a socket as well as the usual output file. Whether this option is available is the choice of the installer. </p>
 </dd>
<dt><code>--ipc-start</code></dt>
<dd> <p> As <code>--ipc</code>, and starts the server at the other end as well. Whether this option is available is the choice of the installer. </p>
 </dd>
<dt><code>--kpathsea-debug</code><i>&nbsp;<wbr>bitmask</i></dt>
<dd> <p> Sets path searching debugging flags according to the bitmask. See the <i>Kpathsea</i> manual for details. </p>
 </dd>
<dt><code>--maketex</code><i>&nbsp;<wbr>fmt</i></dt>
<dd> <p> Enable mktex <i>fmt</i>, where <i>fmt</i> must be one of <i>tex</i> or <i>tfm</i>. </p>
 </dd>
<dt><code>--no-maketex</code><i>&nbsp;<wbr>fmt</i></dt>
<dd> <p> Disable mktex <i>fmt</i>, where <i>fmt</i> must be one of <i>tex</i> or <i>tfm</i>. </p>
 </dd>
<dt><code>--output-comment</code><i>&nbsp;<wbr>string</i></dt>
<dd> <p> Use <i>string</i> for the DVI file comment instead of the date. </p>
 </dd>
<dt><code>-output-directory</code><i>&nbsp;<wbr>directory</i></dt>
<dd> <p> <i>directory</i> instead of the current directory. Look up input files in <i>directory</i> first, the along the normal search path. </p>
 </dd>
<dt><code>--parse-first-line</code></dt>
<dd> <p> If the first line of the main input file begins with <i>%&amp;</i> parse it to look for a dump name. </p>
 </dd>
<dt><code>--progname</code><i>&nbsp;<wbr>name</i></dt>
<dd> <p> Pretend to be program <i>name</i>. This affects both the format used and the search paths. </p>
 </dd>
<dt><code>--recorder</code></dt>
<dd> <p> Enable the filename recorder. This leaves a trace of the files opened for input and output in a file with extension <i>.ofl</i>. (This option is always on.) </p>
 </dd>
<dt><code>--shell-escape</code></dt>
<dd> <p> Enable the <code>\write18{</code><i>command</i><code>}</code> construct. The <i>command</i> can be any Bourne shell command. This construct is normally disallowed for security reasons. </p>
 </dd>
<dt><code>--version</code></dt>
<dd> <p> Print version information and exit. </p>
 </dd></dl>
<h2>ENVIRONMENT</h2>
<p> See the Kpathsearch library documentation (the `Path specifications&#8217; node) for precise details of how the environment variables are used. The <code>kpsewhich</code> utility can be used to query the values of the variables. </p>
<p> One caveat: In most Omega formats, you cannot use ~ in a filename you give directly to Omega, because ~ is an active character, and hence is expanded, not taken as part of the filename. Other programs, such as Metafont, do not have this problem. </p>
<dl>
<dt>TEXMFOUTPUT</dt>
<dd> <p> Normally, Omega puts its output files in the current directory. If any output file cannot be opened there, it tries to open it in the directory specified in the environment variable TEXMFOUTPUT. There is no default value for that variable. For example, if you say <i>tex paper</i> and the current directory is not writable, if TEXMFOUTPUT has the value <i>/tmp</i>, Omega attempts to create <i>/tmp/paper.log</i> (and <i>/tmp/paper.dvi</i>, if any output is produced.) </p>
 </dd>
<dt>TEXINPUTS</dt>
<dd> <p> Search path for <i>\input</i> and <i>\openin</i> files. This should probably start with ``.&#8216;&#8216;, so that user files are found before system files. An empty path component will be replaced with the paths defined in the <i>texmf.cnf</i> file. For example, set TEXINPUTS to &quot;.:/home/usr/tex:&quot; to prepend the current direcory and ``/home/user/tex&#8217;&#8216; to the standard search path. </p>
 </dd>
<dt>TEXEDIT</dt>
<dd> <p> Command template for switching to editor. The default, usually <code>vi</code>, is set when Omega is compiled. </p>
 </dd></dl>
<h2>FILES</h2>
<p> The location of the files mentioned below varies from system to system. Use the <code>kpsewhich</code> utility to find their locations. </p>
<dl>
<dt><i>omega.pool</i></dt>
<dd> <p> Encoded text of Omega&#8217;s messages. </p>
 </dd>
<dt><i>*.oft</i></dt>
<dd> <p> Predigested Omega format (.oft) files. <br />
 </p>
 </dd></dl>
<h2>NOTES</h2>
<p> This manual page is not meant to be exhaustive. The complete documentation for this version of Omega can be found in the info manual <i>Web2C: A TeX implementation</i>.  </p>
<h2>BUGS</h2>
<p> This version of Omega implements a number of optional extensions. In fact, many of these extensions conflict to a greater or lesser extent with the definition of Omega. When such extensions are enabled, the banner printed when Omega starts is changed to print <code>Omegak</code> instead of <code>Omega</code>. </p>
<p> This version of Omega fails to trap arithmetic overflow when dimensions are added or subtracted. Cases where this occurs are rare, but when it does the generated <i>DVI</i> file will be invalid. </p>
<p> The <i>DVI</i> files produced by Omega may use extensions which make them incompatible with most software designed to handle <i>DVI</i> files. In order to print or preview them, you should use <code>odvips</code> to generate a PostScript file. </p>
<p> Omega is experimental software, and if you are an active user it is strongly recommended that you subscribe to the Omega mailing list. Visit the Omega website <code><a rel="nofollow" href="http://omega.cse.unsw.edu.au">http://omega.cse.unsw.edu.au</a></code> for information on how to subscribe.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1), <code><a href="/docs/linux/man/1-mf/">mf</a></code>(1), <a href="/docs/linux/man/1-odvips/">odvips</a><code>(1),</code>  </p>
<h2>AUTHORS</h2>
<p> The primary authors of Omega are John Plaice and Yannis Haralambous. </p>
