---

title: "aleph(1)"
name: "aleph"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aleph/"
description: "aleph – extended Unicode TeX"
---

<p> <code>aleph</code> [<i>options</i>] [<i></i><code>&amp;</code>format] [<i>file</i>|<i></i><code>\</code>commands]  </p>
<p> Run the Aleph typesetter on <i>file</i>, usually creating <i>file.dvi</i>. If the file argument has no extension, &quot;.tex&quot; will be appended to it. Instead of a filename, a set of Aleph commands can be given, the first of which must start with a backslash. With a <code>&amp;</code><i>format</i> argument Aleph uses a different set of precompiled commands, contained in <i>format</i><code>.fmt</code>; it is usually better to use the <code>-fmt</code> <i>format</i> option instead. </p>
<p> Aleph is a version of the TeX program modified for multilingual typesetting. It uses Unicode, and has additional primitives for (among other things) bidirectional typesetting. </p>
<p> Aleph&#8217;s command line options are similar to those of TeX. </p>
<p> Aleph is no longer being actively developed; see LuaTeX for current activity.  </p>
<h2>OPTIONS</h2>
<p> Run aleph --help to see the complete list of options; this is not exhaustive. </p>
<dl>
<dt><code>-cnf-line</code><i>&nbsp;string</i></dt>
<dd> <p> Parse <i>string</i> as a <i>texmf.cnf</i> configuration line. See the Kpathsea manual. </p>
 </dd>
<dt><code>--fmt</code><i>&nbsp;format</i></dt>
<dd> <p> Use <i>format</i> as the name of the format to be used, instead of the name by which Aleph was called or a <i>%&amp;</i> line. </p>
 </dd>
<dt><code>--halt-on-error</code></dt>
<dd> <p> Exit with an error code when an error is encountered during processing. </p>
 </dd>
<dt><code>--help</code></dt>
<dd> <p> Print help message and exit. </p>
 </dd>
<dt><code>--ini</code></dt>
<dd> <p> Be `initial&#8217; Aleph for dumping formats; this is implicitly true if the program is called as <code>inialeph</code>. </p>
 </dd>
<dt><code>--interaction</code><i>&nbsp;mode</i></dt>
<dd> <p> Sets the interaction mode. The mode can be one of <i>batchmode</i>, <i>nonstopmode</i>, <i>scrollmode</i>, and <i>errorstopmode</i>. The meaning of these modes is the same as that of the corresponding \commands. </p>
 </dd>
<dt><code>--ipc</code></dt>
<dd> <p> Send DVI output to a socket as well as the usual output file. Whether this option is available is the choice of the installer. </p>
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
<dt><code>--output-directory</code><i>&nbsp;directory</i></dt>
<dd> <p> Write output files in <i>directory</i> instead of the current directory. Look up input files in <i>directory</i> first, the along the normal search path. </p>
 </dd>
<dt><code>--parse-first-line</code></dt>
<dd> <p> If the first line of the main input file begins with <i>%&amp;</i> parse it to look for a dump name. </p>
 </dd>
<dt><code>--progname</code><i>&nbsp;name</i></dt>
<dd> <p> Pretend to be program <i>name</i>. This affects both the format used and the search paths. </p>
 </dd>
<dt><code>--recorder</code></dt>
<dd> <p> Enable the filename recorder. This leaves a trace of the files opened for input and output in a file with extension <i>.ofl</i>. (This option is always on.) </p>
 </dd>
<dt><code>--shell-escape</code></dt>
<dd> <p> Enable the <code>\write18{</code><i>command</i><code>}</code> construct. The <i>command</i> can be any Bourne shell command. By default, this construct is enabled in a restricted mode, for security reasons. </p>
 </dd>
<dt><code>--version</code></dt>
<dd> <p> Print version information and exit. </p>
 </dd></dl>
<h2>ENVIRONMENT</h2>
<p> See the Kpathsearch library documentation (the `Path specifications&#8217; node) for precise details of how the environment variables are used. The <code>kpsewhich</code> utility can be used to query the values of the variables. </p>
<p> One caveat: In most Aleph formats, you cannot use ~ in a filename you give directly to Aleph, because ~ is an active character, and hence is expanded, not taken as part of the filename. Other programs, such as Metafont, do not have this problem. </p>
<dl>
<dt><code>TEXMFOUTPUT</code></dt>
<dd> <p> Normally, Aleph puts its output files in the current directory. If any output file cannot be opened there, it tries to open it in the directory specified in the environment variable TEXMFOUTPUT. There is no default value for that variable. For example, if you say <i>tex paper</i> and the current directory is not writable, if TEXMFOUTPUT has the value <i>/tmp</i>, Aleph attempts to create <i>/tmp/paper.log</i> (and <i>/tmp/paper.dvi</i>, if any output is produced.) TEXMFOUTPUT is also checked for input files, as TeX often generates files that need to be subsequently read; for input, no suffixes (such as ``.tex&#8217;&#8216;) are added by default, the input name is simply checked as given. </p>
 </dd>
<dt><code>TEXINPUTS</code></dt>
<dd> <p> Search path for <i>\input</i> and <i>\openin</i> files. This should start with ``.&#8216;&#8216;, so that user files are found before system files. An empty path component will be replaced with the paths defined in the <i>texmf.cnf</i> file. For example, set TEXINPUTS to &quot;.:/home/user/tex:&quot; to prepend the current directory and ``/home/user/tex&#8217;&#8216; to the standard search path. </p>
 </dd>
<dt><code>TEXEDIT</code></dt>
<dd> <p> Command template for switching to editor. The default, usually <code>vi</code>, is set when Aleph is compiled. </p>
 </dd></dl>
<h2>NOTES</h2>
<p> This manual page is not meant to be exhaustive. The complete documentation for this version of Aleph can be found in the info manual <i>Web2C: A TeX implementation</i>. See <a rel="nofollow" href="http://tug/org/web2c.">http://tug/org/web2c.</a>  </p>
<h2>BUGS</h2>
<p> This version of Aleph implements a number of optional extensions. In fact, many of these extensions conflict to a greater or lesser extent with the definition of Aleph. When such extensions are enabled, the banner printed when Aleph starts is changed to print <code>Alephk</code> instead of <code>Aleph</code>. </p>
<p> This version of Aleph fails to trap arithmetic overflow when dimensions are added or subtracted. Cases where this occurs are rare, but when it does the generated <i>DVI</i> file will be invalid.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1), <code><a href="/docs/linux/man/1-mf/">mf</a></code>(1)  </p>
<h2>AUTHORS</h2>
<p> The primary authors of Aleph are John Plaice and Yannis Haralambous. </p>
