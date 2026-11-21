---

title: "fincore(1)"
name: "fincore"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fincore/"
description: "fincore – count pages of file contents in core"
---

<p> <code>fincore</code> [options] <i>file</i>...  </p>
<p> <code>fincore</code> counts pages of file contents being resident in memory (in core), and reports the numbers. If an error occurs during counting, then an error message is printed to the stderr and <code>fincore</code> continues processing the rest of files listed in a command line. </p>
<p> The default output is subject to change. So whenever possible, you should avoid using default outputs in your scripts. Always explicitly define expected columns by using <code>--output</code> <i>columns-list</i> in environments where a stable output is required.  </p>
<h2>OPTIONS</h2>
<p> <code>-n</code>, <code>--noheadings</code> </p>
<dl>
<dd> <p> Do not print a header line in status output. </p>
 </dd></dl>
<p> <code>-b</code>, <code>--bytes</code> </p>
<dl>
<dd> <p> Print the SIZE column in bytes rather than in a human-readable format. </p>
 </dd></dl>
<p> <code>-o</code>, <code>--output</code> <i>list</i> </p>
<dl>
<dd> <p> Define output columns. See the <code>--help</code> output to get a list of the currently supported columns. The default list of columns may be extended if <i>list</i> is specified in the format <i>+list</i>. </p>
 </dd></dl>
<p> <code>-r</code>, <code>--raw</code> </p>
<dl>
<dd> <p> Produce output in raw format. All potentially unsafe characters are hex-escaped (\x&lt;code&gt;). </p>
 </dd></dl>
<p> <code>-J</code>, <code>--json</code> </p>
<dl>
<dd> <p> Use JSON output format. </p>
 </dd></dl>
<p> <code>-V</code>, <code>--version</code> </p>
<dl>
<dd> <p> Display version information and exit. </p>
 </dd></dl>
<p> <code>-h</code>, <code>--help</code> </p>
<dl>
<dd> <p> Display help text and exit. </p>
 </dd></dl>
<h2>AUTHORS</h2>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-mincore/">mincore</a></code>(2), <code><a href="/docs/linux/man/2-getpagesize/">getpagesize</a></code>(2), <code>getconf</code>(1p)  </p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.  </p>
<h2>AVAILABILITY</h2>
<p> The <code>fincore</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
