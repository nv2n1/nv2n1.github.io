---
title: "pod2usage(1)"
name: "pod2usage"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pod2usage/"
description: "pod2usage – print usage messages from embedded pod docs in files"
---

<h2 class="name">NAME</h2>
<p> pod2usage &#8211; print usage messages from embedded pod docs in files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>pod2usage</code></p>
<dd> [<code>-help</code>] [<code>-man</code>] [<code>-exit</code> <i>exitval</i>] [<code>-output</code> <i>outfile</i>] [<code>-verbose</code> <i>level</i>] [<code>-pathlist</code> <i>dirlist</i>] [<code>-formatter</code> <i>module</i>] [<code>-utf8</code>] <i>file</i></dl>
<h2>OPTIONS AND ARGUMENTS</h2>
<dl>
<dt><code>-help</code></p>
<dd> Print a brief help message and exit.</p>
<dt><code>-man</code></p>
<dd> Print this command&#8217;s manual page and exit.</p>
<dt><code>-exit</code> <i>exitval</i></p>
<dd> The exit status value to return.</p>
<dt><code>-output</code> <i>outfile</i></p>
<dd> The output file to print to. If the special names &#8220;-&#8221; or &#8220;&gt;&amp;1&#8221; or &#8220;&gt;&amp;STDOUT&#8221; are used then standard output is used. If &#8220;&gt;&amp;2&#8221; or &#8220;&gt;&amp;STDERR&#8221; is used then standard error is used.</p>
<dt><code>-verbose</code> <i>level</i></p>
<dd> The desired level of verbosity to use: </p>
<pre>
    1 : print SYNOPSIS only
    2 : print SYNOPSIS sections and any OPTIONS/ARGUMENTS sections
    3 : print the entire manpage (similar to running pod2text)
</pre>
<dt><code>-pathlist</code> <i>dirlist</i></p>
<dd> Specifies one or more directories to search for the input file if it was not supplied with an absolute path. Each directory path in the given list should be separated by a &#8216;:&#8217; on Unix (&#8216;;&#8217; on MSWin32 and <font SIZE="-1">DOS</font>).</p>
<dt><code>-formatter</code> <i>module</i></p>
<dd> Which text formatter to use. Default is Pod::Text, or for very old Perl versions Pod::PlainText. An alternative would be e.g. Pod::Text::Termcap.</p>
<dt><code>-utf8</code></p>
<dd> This option assumes that the formatter (see above) understands the option &#8220;utf8&#8221;. It turns on generation of utf8 output.</p>
<dt><i>file</i></p>
<dd> The pathname of a file containing pod documentation to be output in usage message format. If omitted, standard input is read &#8211; but the output is then formatted with Pod::Text only &#8211; unless a specific formatter has been specified with <code>-formatter</code>.</dl>
<h2>DESCRIPTION</h2>
<p> <code>pod2usage</code> will read the given input file looking for pod documentation and will print the corresponding usage message. If no input file is specified then standard input is read. </p>
<p> <code>pod2usage</code> invokes the <code>pod2usage()</code> function in the <code>Pod::Usage</code> module. Please see &#8220;<code>pod2usage()</code>&#8221; in Pod::Usage.</p>
<h2>SEE ALSO</h2>
<p> Pod::Usage, pod2text, Pod::Text, Pod::Text::Termcap, perldoc</p>
<h2>AUTHOR</h2>
<p> Please report bugs using &lt;<a rel="nofollow" href="http://rt.cpan.org">http://rt.cpan.org</a>&gt;. </p>
<p> Brad Appleton &lt;bradapp [at] enteract.com&gt; </p>
<p> Based on code for <code><a href="/docs/linux/man/1-pod2text/">pod2text</a>(1)</code> written by Tom Christiansen &lt;tchrist [at] mox.perl.com&gt; </p>
<h2>Index</h2>
