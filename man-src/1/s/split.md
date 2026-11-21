---

title: "split(1)"
name: "split"
section: "1"
letter: "s"
url: "/docs/linux/man/1-split/"
description: "split – split a file into pieces"
---

<p> split - split a file into pieces </p>
<h2>SYNOPSIS</h2>
<p> <code>split</code> [<i>,OPTION/</i>]... [<i>,FILE /</i>[<i>,PREFIX/</i>]]  </p>
<h2>DESCRIPTION</h2>
<p> Output pieces of FILE to PREFIXaa, PREFIXab, ...; default size is 1000 lines, and default PREFIX is &#8216;x&#8217;. </p>
<p> With no FILE, or when FILE is -, read standard input. </p>
<p> Mandatory arguments to long options are mandatory for short options too. </p>
<dl>
<dt><code>-a</code>, <code>--suffix-length</code>=<i>,N/</i></dt>
<dd> <p> generate suffixes of length N (default 2) </p>
 </dd>
<dt><code>--additional-suffix</code>=<i>,SUFFIX/</i></dt>
<dd> <p> append an additional SUFFIX to file names </p>
 </dd>
<dt><code>-b</code>, <code>--bytes</code>=<i>,SIZE/</i></dt>
<dd> <p> put SIZE bytes per output file </p>
 </dd>
<dt><code>-C</code>, <code>--line-bytes</code>=<i>,SIZE/</i></dt>
<dd> <p> put at most SIZE bytes of records per output file </p>
 </dd>
<dt><code>-d</code></dt>
<dd> <p> use numeric suffixes starting at 0, not alphabetic </p>
 </dd>
<dt><code>--numeric-suffixes</code>[=<i>,FROM/</i>]</dt>
<dd> <p> same as <code>-d</code>, but allow setting the start value </p>
 </dd>
<dt><code>-x</code></dt>
<dd> <p> use hex suffixes starting at 0, not alphabetic </p>
 </dd>
<dt><code>--hex-suffixes</code>[=<i>,FROM/</i>]</dt>
<dd> <p> same as <code>-x</code>, but allow setting the start value </p>
 </dd>
<dt><code>-e</code>, <code>--elide-empty-files</code></dt>
<dd> <p> do not generate empty output files with &#8216;-n&#8217; </p>
 </dd>
<dt><code>--filter</code>=<i>,COMMAND/</i></dt>
<dd> <p> write to shell COMMAND; file name is $FILE </p>
 </dd>
<dt><code>-l</code>, <code>--lines</code>=<i>,NUMBER/</i></dt>
<dd> <p> put NUMBER lines/records per output file </p>
 </dd>
<dt><code>-n</code>, <code>--number</code>=<i>,CHUNKS/</i></dt>
<dd> <p> generate CHUNKS output files; see explanation below </p>
 </dd>
<dt><code>-t</code>, <code>--separator</code>=<i>,SEP/</i></dt>
<dd> <p> use SEP instead of newline as the record separator; &#8216;\0&#8217; (zero) specifies the NUL character </p>
 </dd>
<dt><code>-u</code>, <code>--unbuffered</code></dt>
<dd> <p> immediately copy input to output with &#8216;-n r/...&#8216; </p>
 </dd>
<dt><code>--verbose</code></dt>
<dd> <p> print a diagnostic just before each output file is opened </p>
 </dd>
<dt><code>--help</code></dt>
<dd> <p> display this help and exit </p>
 </dd>
<dt><code>--version</code></dt>
<dd> <p> output version information and exit </p>
 </dd></dl>
<p> The SIZE argument is an integer and optional unit (example: 10K is 10*1024). Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000). Binary prefixes can be used, too: KiB=K, MiB=M, and so on.  </p>
<h3>CHUNKS may be:</h3>
<dl>
<dt>N</dt>
<dd> <p> split into N files based on size of input </p>
 </dd>
<dt>K/N</dt>
<dd> <p> output Kth of N to stdout </p>
 </dd>
<dt>l/N</dt>
<dd> <p> split into N files without splitting lines/records </p>
 </dd>
<dt>l/K/N</dt>
<dd> <p> output Kth of N to stdout without splitting lines/records </p>
 </dd>
<dt>r/N</dt>
<dd> <p> like &#8216;l&#8217; but use round robin distribution </p>
 </dd>
<dt>r/K/N</dt>
<dd> <p> likewise but only output Kth of N to stdout </p>
 </dd></dl>
<h2>AUTHOR</h2>
<p> Written by Torbjorn Granlund and Richard M. Stallman.  </p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt; <br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;  </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;. <br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.  </p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/split">https://www.gnu.org/software/coreutils/split</a>&gt; <br />
 or available locally via: info &#8216;(coreutils) split invocation&#8217; </p>
