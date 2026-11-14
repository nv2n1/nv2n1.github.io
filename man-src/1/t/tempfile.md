---
title: "tempfile(1)"
name: "tempfile"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tempfile/"
description: "tempfile – create a temporary file in a safe manner"
---

<h2 class="name">NAME</h2>
<p> tempfile &#8211; create a temporary file in a safe manner </p>
<h2>SYNOPSIS</h2>
<p> <code>tempfile</code> [-d DIR] [-p STRING] [-s STRING] [-m MODE] [-n FILE] [&#8211;directory=DIR] [&#8211;prefix=STRING] [&#8211;suffix=STRING] [&#8211;mode=MODE] [&#8211;name=FILE] [&#8211;help] [&#8211;version]</p>
<h2>DESCRIPTION</h2>
<p> <code>tempfile</code> creates a temporary file in a safe manner. It uses <code><a href="/docs/linux/man/3-mkstemps/">mkstemps</a></code>(3) to choose the name and opens it with O_RDWR | O_CREAT | O_EXCL. The filename is printed on standard output. </p>
<p> The directory in which to create the file might be searched for in this order:</p>
<dl>
<dt>a)</p>
<dd> In case the environment variable <code>TMPDIR</code> exists and contains the name of an appropriate directory, that is used.</p>
<dt>b)</p>
<dd> Otherwise, if the <i>&#8211;directory</i> argument is specified and appropriate, it is used.</p>
<dt>c)</p>
<dd> Otherwise, <i>P_tmpdir</i> (as defined in <i>&lt;stdio.h&gt;</i>) is used when appropriate.</p>
<dt>d)</p>
<dd> Finally an implementation-defined directory (<i>/tmp</i>) may be used.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d, &#8211;directory </code><i>DIR</i></p>
<dd> Place the file in DIR.</p>
<dt><code>-m, &#8211;mode </code><i>MODE</i></p>
<dd> Open the file with MODE instead of 0600.</p>
<dt><code>-n, &#8211;name </code><i>FILE</i></p>
<dd> Use FILE for the name instead of <code><a href="/docs/linux/man/3-tempnam/">tempnam</a></code>(3)<code>.</code> The options -d, -p, and -s are ignored if this option is given.</p>
<dt><code>-p, &#8211;prefix </code><i>STRING</i></p>
<dd> Use up to five letters of STRING to generate the name.</p>
<dt><code>-s, &#8211;suffix </code><i>STRING</i></p>
<dd> Generate the file with STRING as the suffix.</p>
<dt><code>&#8211;help</code></p>
<dd> Print a usage message on standard output and exit successfully.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version information on standard output and exit successfully.</dl>
<h2>RETURN VALUES</h2>
<p> An exit status of 0 means the temporary file was created successfully. Any other exit status indicates an error.</p>
<h2>BUGS</h2>
<p> Exclusive creation is not guaranteed when creating files on NFS partitions. tempfile cannot make temporary directories. tempfile is deprecated; you should use <code><a href="/docs/linux/man/1-mktemp/">mktemp</a></code>(1) instead.</p>
<h2>EXAMPLE</h2>
<pre><code>
#!/ bin / sh
#[...]
t = $(tempfile) || exit
                           trap "rm -f -- '$t'" EXIT
#[...]
                               rm -
                       f-- "$t" trap - EXIT exit
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-tempnam/">tempnam</a></code>(3), <code><a href="/docs/linux/man/1-mktemp/">mktemp</a></code>(1) </p>
<h2>Index</h2>
