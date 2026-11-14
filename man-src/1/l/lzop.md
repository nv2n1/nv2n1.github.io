---
title: "lzop(1)"
name: "lzop"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lzop/"
description: "lzop – compress or expand files"
---

<h2 class="name">NAME</h2>
<p> lzop &#8211; compress or expand files </p>
<h2>ABSTRACT</h2>
<p> <code>lzop</code> is a file compressor very similar to <code>gzip</code>. <code>lzop</code> favors speed over compression ratio.</p>
<h2>SYNOPSIS</h2>
<p> <code>lzop</code> [&nbsp;<i>command</i>&nbsp;] [&nbsp;<i>options</i>&nbsp;] [&nbsp;<i>filename</i>&nbsp;&#8230;&nbsp;<wbr>&nbsp;] </p>
<p> <code>lzop</code> [<code>-dxlthIVL19</code>] [<code>-qvcfFnNPkU</code>] [<code>-o</code>&nbsp;<i>file</i>] [<code>-p</code>[<i>path</i>]] [<code>-S</code>&nbsp;<i>suffix</i>] [<i>filename</i>&nbsp;&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>lzop</code> reduces the size of the named files. Whenever possible, each file is compressed into one with the extension <code>.lzo</code>, while keeping the same ownership modes, access and modification times. If no files are specified, or if a file name is &#8220;-&#8221;, lzop tries to compress the standard input to the standard output. lzop will only attempt to compress regular files or symbolic links to regular files. In particular, it will ignore directories. </p>
<p> If the compressed file name is too long for its file system, <code>lzop</code> truncates it. </p>
<p> Compressed files can be restored to their original form using <code>lzop -d</code>. <code>lzop -d</code> takes a list of files on its command line and decompresses each file whose name ends with <code>.lzo</code> and which begins with the correct magic number to an uncompressed file without the original extension. <code>lzop -d</code> also recognizes the special extension <code>.tzo</code> as shorthand for <code>.tar.lzo</code>. When compressing, lzop uses the <code>.tzo</code> extension if necessary instead of truncating a file with a <code>.tar</code> extension. </p>
<p> <code>lzop</code> stores the original file name, mode and time stamp in the compressed file. These can be used when decompressing the file with the <code>-d</code> option. This is useful when the compressed file name was truncated or when the time stamp was not preserved after a file transfer. </p>
<p> <code>lzop</code> preserves the ownership, mode and time stamp of files when compressing. When decompressing lzop restores the mode and time stamp if present in the compressed files. See the options <code>-n</code>, <code>-N</code>, <code>&#8211;no-mode</code> and <code>&#8211;no-time</code> for more information. </p>
<p> <code>lzop</code> always keeps original files unchanged unless you use the option <code>-U</code>. </p>
<p> <code>lzop</code> uses the <i></i><font SIZE="-1"><i>LZO</i></font><i> data compression library</i> for compression services. The amount of compression obtained depends on the size of the input and the distribution of common substrings. Typically, text such as source code or English is compressed into 40-50% of the original size, and large files usually compress much better than small ones. Compression and decompression speed is generally much faster than that achieved by <code>gzip</code>, but compression ratio is worse.</p>
<h3><font SIZE="-1">COMPRESSION LEVELS</font></h3>
<p> lzop offers the following compression levels of the <font SIZE="-1">LZO1X</font> algorithm:</p>
<dl>
<dt>-3</p>
<dd> the default level offers pretty fast compression. -2, -3, -4, -5 and -6 are currently all equivalent &#8211; this may change in a future release.</p>
<dt>-1, &#8211;fast</p>
<dd> can be even a little bit faster in some cases &#8211; but most times you won&#8217;t notice the difference</p>
<dt>-7, -8, -9, &#8211;best</p>
<dd> these compression levels are mainly intended for generating pre-compressed data &#8211; especially <code>-9</code> can be somewhat slow</dl>
<p> Decompression is <i>very</i> fast for all compression levels, and decompression speed is not affected by the compression level.</p>
<h2>MAIN COMMAND</h2>
<p> If no other command is given then lzop defaults to compression (using compression level -3).</p>
<dl>
<dt>-#, &#8211;fast, &#8211;best</p>
<dd> Regulate the speed of compression using the specified digit <code>#</code>, where -1 or &#8211;fast indicates the fastest compression method (less compression) and -9 or &#8211;best indicates the slowest compression method (best compression). The default compression level is -3.</p>
<dt>-d, &#8211;decompress, &#8211;uncompress</p>
<dd> Decompress. Each file will be placed into same the directory as the compressed file.</p>
<dt>-x, &#8211;extract</p>
<dd> Extract compressed files to the current working directory. This is the same as &#8216;-dPp&#8217;.</p>
<dt>-t, &#8211;test</p>
<dd> Test. Check the compressed file integrity.</p>
<dt>-l, &#8211;list</p>
<dd> For each compressed file, list the following fields: </p>
<pre>
  method: compression method
  compressed: size of the compressed file
  uncompr.: size of the uncompressed file
  ratio: compression ratio
  uncompressed_name: name of the uncompressed file
</pre>
<p> In combination with the &#8211;verbose option, the following fields are also displayed: </p>
<pre>
  date &amp; time: time stamp for the uncompressed file
</pre>
<p> With &#8211;name, the uncompressed name, date and time are those stored within the compress file if present. </p>
<p> With &#8211;verbose, the size totals and compression ratio for all files is also displayed. With &#8211;quiet, the title and totals lines are not displayed. </p>
<p> Note that lzop defines compression ratio as compressed_size / uncompressed_size.</p>
<dt>&#8211;ls, &#8211;ls=<i></i><font SIZE="-1"><i>FLAGS</i></font><i></i></p>
<dd> List each compressed file in a format similar to <code>ls -ln</code>. </p>
<p> The following flags are currently honoured:<br />
&nbsp;<wbr>&nbsp;F&nbsp;<wbr>&nbsp;Append a&nbsp;&#8216;*&#8217;&nbsp;for executable files.<br />
&nbsp;<wbr>&nbsp;G&nbsp;<wbr>&nbsp;Inhibit display of group information.<br />
&nbsp;<wbr>&nbsp;Q&nbsp;<wbr>&nbsp;Enclose file names in double quotes.</p>
<dt>&#8211;info</p>
<dd> For each compressed file, list the internal header fields.</p>
<dt>-I, &#8211;sysinfo</p>
<dd> Display information about the system and quit.</p>
<dt>-L, &#8211;license</p>
<dd> Display the lzop license and quit.</p>
<dt>-h, -H, &#8211;help</p>
<dd> Display a help screen and quit.</p>
<dt>-V</p>
<dd> Version. Display the version number and compilation options and quit.</p>
<dt>&#8211;version</p>
<dd> Version. Display the version number and quit.</dl>
<h2>OPTIONS</h2>
<dl>
<dt>-c, &#8211;stdout, &#8211;to-stdout</p>
<dd> Write output on standard output. If there are several input files, the output consists of a sequence of independently (de)compressed members. To obtain better compression, concatenate all input files before compressing them.</p>
<dt>-o <i></i><font SIZE="-1"><i>FILE</i></font><i></i>, &#8211;output=<i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> Write output to the file <i></i><font SIZE="-1"><i>FILE</i></font><i></i>. If there are several input files, the output consists of a sequence of independently (de)compressed members.</p>
<dt>-p, -p<i></i><font SIZE="-1"><i>DIR</i></font><i></i>, &#8211;path=<i></i><font SIZE="-1"><i>DIR</i></font><i></i></p>
<dd> Write output files into the directory <i></i><font SIZE="-1"><i>DIR</i></font><i></i> instead of the directory determined by the input file. If <i></i><font SIZE="-1"><i>DIR</i></font><i></i> is omitted, then write to the current working directory.</p>
<dt>-f, &#8211;force</p>
<dd> Force lzop to </p>
<pre>
 - overwrite existing files
 - (de-)compress from stdin even if it seems a terminal
 - (de-)compress to stdout even if it seems a terminal
 - allow option -c in combination with -U
</pre>
<p> Using <code>-f</code> two or more times forces things like </p>
<pre>
 - compress files that already have a .lzo suffix
 - try to decompress files that do not have a valid suffix
 - try to handle compressed files with unknown header flags
</pre>
<p> Use with care.</p>
<dt>-F, &#8211;no-checksum</p>
<dd> Do not store or verify a checksum of the uncompressed file when compressing or decompressing. This speeds up the operation of lzop a little bit (especially when decompressing), but as unnoticed data corruption can happen in case of damaged compressed files the usage of this option is not generally recommended. Also, a checksum is always stored when compressing with one of the slow compression levels (-7, -8 or -9), regardless of this option.</p>
<dt>-n, &#8211;no-name</p>
<dd> When decompressing, do not restore the original file name if present (remove only the lzop suffix from the compressed file name). This option is the default under <font SIZE="-1">UNIX.</font></p>
<dt>-N, &#8211;name</p>
<dd> When decompressing, restore the original file name if present. This option is useful on systems which have a limit on file name length. If the original name saved in the compressed file is not suitable for its file system, a new name is constructed from the original one to make it legal. This option is the default under <font SIZE="-1">DOS,</font> Windows and <font SIZE="-1">OS/2.</font></p>
<dt>-P</p>
<dd> When decompressing, restore the original path and file name if present. When compressing, store the relative (and cleaned) path name. This option is mainly useful when using <code>archive mode</code> &#8211; see usage examples below.</p>
<dt>&#8211;no-mode</p>
<dd> When decompressing, do not restore the original mode (permissions) saved in the compressed file.</p>
<dt>&#8211;no-time</p>
<dd> When decompressing, do not restore the original time stamp saved in the compressed file.</p>
<dt>-S <i>.suf</i>, &#8211;suffix=<i>.suf</i></p>
<dd> Use suffix <i>.suf</i> instead of <i>.lzo</i>. The suffix must not contain multiple dots and special characters like &#8216;+&#8217; or &#8216;*&#8217;, and suffixes other than <i>.lzo</i> should be avoided to avoid confusion when files are transferred to other systems.</p>
<dt>-k, &#8211;keep</p>
<dd> Do not delete input files. This is the default.</p>
<dt>-U, &#8211;unlink, &#8211;delete</p>
<dd> Delete input files after successful compression or decompression. Use this option to make lzop behave like <code>gzip</code> and <code>bzip2</code>. Note that explicitly giving <code>-k</code> overrides <code>-U</code>.</p>
<dt>&#8211;crc32</p>
<dd> Use a crc32 checksum instead of an adler32 checksum.</p>
<dt>&#8211;no-warn</p>
<dd> Suppress all warnings.</p>
<dt>&#8211;ignore-warn</p>
<dd> Suppress all warnings, and never exit with exit status 2.</p>
<dt>-q, &#8211;quiet, &#8211;silent</p>
<dd> Suppress all warnings and decrease the verbosity of some commands like <code>&#8211;list</code> or <code>&#8211;test</code>.</p>
<dt>-v, &#8211;verbose</p>
<dd> Verbose. Display the name for each file compressed or decompressed. Multiple <code>-v</code> can be used to increase the verbosity of some commands like <code>&#8211;list</code> or <code>&#8211;test</code>.</p>
<dt>&#8212;</p>
<dd> Specifies that this is the end of the options. Any file name after <code>&#8212;</code> will not be interpreted as an option even if it starts with a hyphen.</dl>
<h2>OTHER OPTIONS</h2>
<dl>
<dt>&#8211;no-stdin</p>
<dd> Do not try to read standard input (but a file name &#8220;-&#8221; will still override this option). In old versions of <code>lzop</code>, this option was necessary when used in cron jobs (which do not have a controlling terminal).</p>
<dt>&#8211;filter=<i></i><font SIZE="-1"><i>NUMBER</i></font><i></i></p>
<dd> Rarely useful. Preprocess data with a special &#8220;multimedia&#8221; filter before compressing in order to improve compression ratio. <i></i><font SIZE="-1"><i>NUMBER</i></font><i></i> must be a decimal number from 1 to 16, inclusive. Using a filter slows down both compression and decompression quite a bit, and the compression ratio usually doesn&#8217;t improve much either&#8230; More effective filters may be added in the future, though. </p>
<p> You can try &#8211;filter=1 with data like 8-bit sound samples, &#8211;filter=2 with 16-bit samples or depth-16 images, etc. </p>
<p> Un-filtering during decompression is handled automatically.</p>
<dt>-C, &#8211;checksum</p>
<dd> Deprecated. Only for compatibility with very old versions as lzop now uses a checksum by default. This option will get removed in a future release.</p>
<dt>&#8211;no-color</p>
<dd> Do not use any color escape sequences.</p>
<dt>&#8211;mono</p>
<dd> Assume a mono <font SIZE="-1">ANSI</font> terminal. This is the default under <font SIZE="-1">UNIX</font> (if console support is compiled in).</p>
<dt>&#8211;color</p>
<dd> Assume a color <font SIZE="-1">ANSI</font> terminal or try full-screen access. This is the default under <font SIZE="-1">DOS</font> and in a Linux virtual console (if console support is compiled in).</dl>
<h2>ADVANCED USAGE</h2>
<p> lzop allows you to deal with your files in many flexible ways. Here are some usage examples:</p>
<dl>
<dt><code>backup mode</code></p>
<dd>
<pre>
  tar --use-compress-program=lzop -cf archive.tar.lzo files..
  This is the recommended mode for creating backups.
  Requires GNU tar or a compatible version which accepts the
  '--use-compress-program=XXX' option.
</pre>
<dt><code>single file mode:</code> individually (de)compress each file</p>
<dd>
<pre><code>
create
        lzop a.c-&gt;create a.c.lzo
            lzop a.c b.c-&gt;create a.c.lzo &amp;b.c.lzo
                lzop -
    U a.c b.c-&gt;create a.c.lzo &amp;b.c.lzo and delete a.c &amp;b.c
        lzop *.c
            extract
                lzop -
    d a.c.lzo-&gt;restore a.c
        lzop -
    df a.c.lzo-&gt;restore a.c,
    overwrite if already exists
            lzop -
        d *.lzo
            list
                lzop -
        l a.c.lzo
            lzop -
        l *.lzo
            lzop -
        lv *.lzo-&gt;be verbose
            test
                lzop -
        t a.c.lzo
            lzop -
        tq *.lzo-&gt;be quiet
</code></pre>
<dt><code>pipe mode:</code> (de)compress from stdin to stdout</p>
<dd>
<pre>
 create
   lzop &lt; a.c &gt; y.lzo
   cat a.c | lzop &gt; y.lzo
   tar -cf - *.c | lzop &gt; y.tar.lzo     -&gt; create a compressed tar file
 extract
   lzop -d &lt; y.lzo &gt; a.c
   lzop -d &lt; y.tar.lzo | tar -xvf -     -&gt; extract a tar file
 list
   lzop -l &lt; y.lzo
   cat y.lzo | lzop -l
   lzop -d &lt; y.tar.lzo | tar -tvf -     -&gt; list a tar file
 test
   lzop -t &lt; y.lzo
   cat y.lzo | lzop -t
</pre>
<dt><code>stdout mode:</code> (de)compress to stdout</p>
<dd>
<pre>
 create
   lzop -c a.c &gt; y.lzo
 extract
   lzop -dc y.lzo &gt; a.c
   lzop -dc y.tar.lzo | tar -xvf -      -&gt; extract a tar file
 list
   lzop -dc y.tar.lzo | tar -tvf -      -&gt; list a tar file
</pre>
<dt><code>archive mode:</code> compress/extract multiple files into a single archive file</p>
<dd>
create<br />
        lzop a.c b.c &#8211;<br />
    o sources.lzo-&gt;create an archive<br />
        lzop &#8211;<br />
    P src/*.c -o sources.lzo       -&gt; create an archive, store path name<br />
   lzop -c *.c &gt; sources.lzo            -&gt; another way to create an archive<br />
   lzop -c *.h &gt;&gt; sources.lzo           -&gt; add files to archive<br />
 extract<br />
   lzop -dN sources.lzo<br />
   lzop -x ../src/sources.lzo           -&gt; extract to current directory<br />
   lzop -x -p/tmp &lt; ../src/sources.lzo  -&gt; extract to /tmp directory<br />
 list<br />
   lzop -lNv sources.lzo<br />
 test<br />
   lzop -t sources.lzo<br />
   lzop -tvv sources.lzo                -&gt; be very verbose
</dl>
<p> If you wish to create a single archive file with multiple members so that members can later be extracted independently, you should prefer a full-featured archiver such as tar. The latest version of <font SIZE="-1">GNU</font> tar supports the <code>&#8211;use-compress-program=lzop</code> option to invoke lzop transparently. lzop is designed as a complement to tar, not as a replacement.</p>
<h2>ENVIRONMENT</h2>
<p> The environment variable <font SIZE="-1"><code>LZOP</code></font> can hold a set of default options for lzop. These options are interpreted first and can be overwritten by explicit command line parameters. For example: </p>
<pre><code>
    for
        sh / ksh / zsh : LZOP = "-1v --name"; export LZOP
    for csh/tcsh:      setenv LZOP "-1v --name"
    for DOS/Windows:   set LZOP=-1v --name
</code></pre>
<p> On Vax/VMS, the name of the environment variable is <font SIZE="-1">LZOP_OPT,</font> to avoid a conflict with the symbol set for invocation of the program. </p>
<p> Not all of the options are valid in the environment variable &#8211; lzop will tell you.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1), <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1), <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1), <code><a href="/docs/linux/man/1-xz/">xz</a></code>(1) </p>
<p> Precompiled binaries for some platforms are available from the lzop home page. </p>
<pre>
    see <a rel="nofollow" href="http://www.oberhumer.com/opensource/lzop/">http://www.oberhumer.com/opensource/lzop/</a>
</pre>
<p> lzop uses the <font SIZE="-1">LZO</font> data compression library for compression services. </p>
<pre>
    see <a rel="nofollow" href="http://www.oberhumer.com/opensource/lzo/">http://www.oberhumer.com/opensource/lzo/</a>
</pre>
<h2>DIAGNOSTICS</h2>
<p> Exit status is normally 0; if an error occurs, exit status is 1. If a warning occurs, exit status is 2 (unless option <code>&#8211;ignore-warn</code> is in effect). </p>
<p> <code>lzop&#8217;s</code> diagnostics are intended to be self-explanatory.</p>
<h2>BUGS</h2>
<p> No bugs are known. Please report all problems immediately to the author.</p>
<h2>AUTHOR</h2>
<p> Markus Franz Xaver Johannes Oberhumer &lt;markus [at] oberhumer.com&gt; <a rel="nofollow" href="http://www.oberhumer.com/opensource/lzop/">http://www.oberhumer.com/opensource/lzop/</a></p>
<h2>COPYRIGHT</h2>
<p> lzop and the <font SIZE="-1">LZO</font> library are Copyright (C) 1996-2017 Markus Franz Xaver Oberhumer &lt;markus [at] oberhumer.com&gt;. All Rights Reserved. </p>
<p> lzop and the <font SIZE="-1">LZO</font> library are distributed under the terms of the <font SIZE="-1">GNU</font> General Public License (<font SIZE="-1">GPL</font>). </p>
<p> Legal info: If want to integrate lzop into your commercial (backup-)system please carefully read the <font SIZE="-1">GNU GPL FAQ</font> at <a rel="nofollow" href="http://www.gnu.org/licenses/gpl-faq.html">http://www.gnu.org/licenses/gpl-faq.html</a> about possible implications. </p>
<h2>Index</h2>
<dt><a href="#lbAG">MAIN COMMAND</a></p>
<dd>
<dt><a href="#lbAH">OPTIONS</a></p>
<dd>
<dt><a href="#lbAI">OTHER OPTIONS</a></p>
<dd>
<dt><a href="#lbAJ">ADVANCED USAGE</a></p>
<dd>
<dt><a href="#lbAK">ENVIRONMENT</a></p>
<dd>
<dt><a href="#lbAL">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAM">DIAGNOSTICS</a></p>
<dd>
<dt><a href="#lbAN">BUGS</a></p>
<dd>
<dt><a href="#lbAO">AUTHOR</a></p>
<dd>
<dt><a href="#lbAP">COPYRIGHT</a></p>
<dd></dl>
