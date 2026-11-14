---
title: "buffchan(8)"
name: "buffchan"
section: "8"
letter: "b"
url: "/docs/linux/man/8-buffchan/"
description: "buffchan – Buffered file-writing backend for INN"
---

<p>buffchan &#8211; Buffered file-writing backend for INN</p>
<h2>Synopsis</h2>
<p><code>buffchan</code> [<code>-bru</code>] [<code>-c</code> <i>lines</i>] [<code>-C</code> <i>seconds</i>] [<code>-d</code> <i>directory</i>] [<code>-f</code> <i>num-fields</i>] [<code>-l</code> <i>lines</i>] [<code>-L</code> <i>seconds</i>] [<code>-m</code> <i>map</i>] [<code>-p</code> <i>pid-file</i>] [<code>-s</code> <i>format</i>]</p>
<h2>Description</h2>
<p><code>buffchan</code> reads lines from standard input and copies the initial fields in each line to the files named by the remaining fields on the line. <code>buffchan</code> is intended to be called by <code>innd</code> as an exploder feed. </p>
<p> The input is interpreted as a sequence of lines. Each line contains a fixed number of initial fields, followed by a variable number of filename fields. All fields in a line are separated by whitespace and do not contain any whitespace. The default number of initial fields is one. </p>
<p> For each line of input, <code>buffchan</code> writes the initial fields, separated by a space and followed by a newline, to each of the files named in the filename fields. The output files are kept open and are only flushed or closed based on the schedule given by the <code>-c</code>, <code>-C</code>, <code>-l</code>, and <code>-L</code> options. </p>
<p> As an exploder feed (see <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5) for an explanation), <code>buffchan</code> interprets lines beginning with an exclamation point as commands. Besides <tt>&quot;!begin&quot;</tt> (which only marks the start of the feed), there are three supported commands:</p>
<dl>
<dt>!flush [<i>site</i>]</p>
<dd>The flush command closes and reopens all open files. An optional site can be specified, in which case <code>buffchan</code> flushes only that file. This command is analogous to the <tt>&quot;ctlinnd flush&quot;</tt> command. This command can be sent via <code>innd</code> using <tt>&quot;ctlinnd send </tt>buffchan-site<tt> 'flush </tt>site<tt>'&quot;</tt>. </p>
<p> Applications can tell that flush has completed by renaming the file before issuing the command. When the original file name has reappeared, the flush is complete. If <i><a href="/docs/linux/man/3-fchmod/">fchmod</a></i>(3) is available, <code>buffchan</code> also changes the file to read-only while it&#8217;s actively writing to it and changes it back to read/write once it has been closed. It will change the mode back to read-only only if it reopens the same file.</p>
<dt>!drop [<i>site</i>]</p>
<dd>The drop command is similar to the flush command, except that no files are reopened. If given an argument, only the specified site is dropped; otherwise, all sites are dropped. (Note that a site will be restarted if the input stream mentions the site again.) </p>
<p> When a <tt>&quot;ctlinnd drop site&quot;</tt> command is sent, <code>innd</code> will automatically forward the command to <code>buffchan</code> if the site is listed as a funnel feeding into the <code>buffchan</code> exploder. To drop all sites, use <tt>&quot;ctlinnd send </tt>buffchan-site<tt> drop&quot;</tt>.</p>
<dt>!readmap</p>
<dd>The map file specified with the <code>-m</code> option, if given, will be reloaded.</dl>
<p> Once <code>buffchan</code> opens a file, it keeps it open (in the absence of a drop command). The input must therefore never specify more files than the maximum number of files a process may open.</p>
<h2>Options</h2>
<dl>
<dt><code>-b</code></p>
<dd>Force the output to be buffered. (This is generally the default, but it may depend on the operating system.) If <code>-b</code> is given, a buffer size of <font SIZE="-1">BUFSIZ</font> (a constant of the system standard I/O library) is used.</p>
<dt><code>-c</code> <i>lines</i></p>
<dd>If the <code>-c</code> flag is given, <code>buffchan</code> will close and reopen a file after every <i>lines</i> lines are written to the file.</p>
<dt><code>-C</code> <i>seconds</i></p>
<dd>If the <code>-C</code> flag is given, <code>buffchan</code> will close and reopen a file if it has been open for more than <i>seconds</i> seconds.</p>
<dt><code>-d</code> <i>directory</i></p>
<dd>This flag may be used to specify a directory the program should change to before starting. If this flag is used, the default for the <code>-s</code> flag (see below) is changed to be a simple <tt>%s</tt> (in other words, output files are considered to be relative to <i>directory</i>).</p>
<dt><code>-f</code> <i>num-fields</i></p>
<dd>By default, each line is expected to contain one fixed field followed by some number of filename fields. If this flag is given, <i>num-fields</i> will be used as the number of initial fixed fields.</p>
<dt><code>-l</code> <i>lines</i></p>
<dd>If the <code>-l</code> flag is given, <code>buffchan</code> will flush the output after every <i>lines</i> lines are written to a file.</p>
<dt><code>-L</code> <i>seconds</i></p>
<dd>If the <code>-L</code> flag is given, <code>buffchan</code> will flush each output file every <i>seconds</i> seconds.</p>
<dt><code>-m</code> <i>map</i></p>
<dd>Map files translate the names in the filename fields on each line into filenames that should be used instead. It&#8217;s used primarily when short names are used in <i>newsfeeds</i>, but the output files should use the full domain names of remote peers. </p>
<p> In the map file, blank lines and lines starting with a number sign (<tt>&quot;#&quot;</tt>) are ignored. All other lines should have two host names separated by a colon. The first field is the name that may appear in the input stream; the second field names the file to be used when the name in the first field appears. For example: </p>
<pre> # This is a comment
 uunet:news.uu.net
 foo:foo.com
 munnari:munnari.oz.au</pre>
<dt><code>-p</code> <i>pid-file</i></p>
<dd>If the <code>-p</code> option is given, <code>buffchan</code> will write a line containing its process <font SIZE="-1">ID</font> (in text) to the specified file when it starts.</p>
<dt><code>-r</code></p>
<dd>By default, <code>buffchan</code> sends its error messages to <i>pathlog</i>/errlog. To suppress this redirection and send error messages to standard error, use the <code>-r</code> flag.</p>
<dt><code>-s</code></p>
<dd>The <code>-s</code> flag may be used to specify a format that maps a filename from the filename fields at the end of each line to an actual filename. This is a <i><a href="/docs/linux/man/3-sprintf/">sprintf</a></i>(3) format string that should contain a single instance of <tt>%s</tt>, which will be replaced with the value of the filename field (possibly after mapping with the map file from <code>-m</code>). The default value is <i>pathoutgoing</i>/<tt>%s</tt>.</p>
<dt><code>-u</code></p>
<dd>If the <code>-u</code> flag is used, the output will be unbuffered.</dl>
<h2>Examples</h2>
<p>If <code>buffchan</code> is invoked with <tt>&quot;-f 2&quot;</tt> and given the following input: </p>
<pre> news/software/b/132 &lt;1643 [at] munnari.oz.au&gt; foo uunet
 news/software/b/133 &lt;102060 [at] litchi.foo.com&gt; uunet munnari
 comp/sources/unix/2002 &lt;999 [at] news.foo.com&gt; foo uunet munnari</pre>
<p>Then the file <i>foo</i> will have these lines: </p>
<pre> news/software/b/132 &lt;1643 [at] munnari.oz.au&gt;
 comp/sources/unix/2002 &lt;999 [at] news.foo.com&gt;</pre>
<p>the file <i>munnari</i> will have these lines: </p>
<pre> news/software/b/133 &lt;102060 [at] litchi.foo.com&gt;
 comp/sources/unix/2002 &lt;999 [at] news.foo.com&gt;</pre>
<p>and the file <i>uunet</i> will have these lines: </p>
<pre> news/software/b/132 &lt;1643 [at] munnari.oz.au&gt;
 news/software/b/133 &lt;102060 [at] litchi.foo.com&gt;
 comp/sources/unix/2002 &lt;999 [at] news.foo.com&gt;</pre>
<h2>History</h2>
<p>Written by Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. Converted to <font SIZE="-1">POD</font> by Russ Allbery &lt;eagle [at] eyrie.org&gt;. </p>
<p> <tt>$Id:</tt> buffchan.pod 9768 2014-12-07 21:22:57Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8), <i><a href="/docs/linux/man/8-filechan/">filechan</a></i>(8), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8), <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5). </p>
