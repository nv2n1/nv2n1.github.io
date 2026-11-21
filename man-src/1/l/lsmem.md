---
title: "lsmem(1)"
name: "lsmem"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lsmem/"
description: "lsmem – list the ranges of available memory with their online status"
---
<h2 class="name">NAME</h2>
<p> lsmem - list the ranges of available memory with their online status </p>
<h2>SYNOPSIS</h2>
<p> <code>lsmem</code> [options]  </p>
<h2>DESCRIPTION</h2>
<p> The <code>lsmem</code> command lists the ranges of available memory with their online status. The listed memory blocks correspond to the memory block representation in sysfs. The command also shows the memory block size and the amount of memory in online and offline state. </p>
<p> The default output compatible with original implementation from s390-tools, but it&#8217;s strongly recommended to avoid using default outputs in your scripts. Always explicitly define expected columns by using the <code>--output</code> option together with a columns list in environments where a stable output is required. </p>
<p> The <code>lsmem</code> command lists a new memory range always when the current memory block distinguish from the previous block by some output column. This default behavior is possible to override by the <code>--split</code> option (e.g., <code>lsmem --split=ZONES</code>). The special word &quot;none&quot; may be used to ignore all differences between memory blocks and to create as large as possible continuous ranges. The opposite semantic is <code>--all</code> to list individual memory blocks. </p>
<p> Note that some output columns may provide inaccurate information if a split policy forces <code>lsmem</code> to ignore differences in some attributes. For example if you merge removable and non-removable memory blocks to the one range than all the range will be marked as non-removable on <code>lsmem</code> output. </p>
<p> Not all columns are supported on all systems. If an unsupported column is specified, <code>lsmem</code> prints the column but does not provide any data for it. </p>
<p> Use the <code>--help</code> option to see the columns description.  </p>
<h2>OPTIONS</h2>
<p> <code>-a</code>, <code>--all</code> </p>
<dl>
<dd> <p> List each individual memory block, instead of combining memory blocks with similar attributes. </p>
 </dd></dl>
<p> <code>-b</code>, <code>--bytes</code> </p>
<dl>
<dd> <p> Print the SIZE column in bytes rather than in a human-readable format. </p>
 </dd></dl>
<p> <code>-h</code>, <code>--help</code> </p>
<dl>
<dd> <p> Display help text and exit. </p>
 </dd></dl>
<p> <code>-J</code>, <code>--json</code> </p>
<dl>
<dd> <p> Use JSON output format. </p>
 </dd></dl>
<p> <code>-n</code>, <code>--noheadings</code> </p>
<dl>
<dd> <p> Do not print a header line. </p>
 </dd></dl>
<p> <code>-o</code>, <code>--output</code> <i>list</i> </p>
<dl>
<dd> <p> Specify which output columns to print. Use <code>--help</code> to get a list of all supported columns. The default list of columns may be extended if <i>list</i> is specified in the format <code>+</code><i>list</i> (e.g., <code>lsmem -o +NODE</code>). </p>
 </dd></dl>
<p> <code>--output-all</code> </p>
<dl>
<dd> <p> Output all available columns. </p>
 </dd></dl>
<p> <code>-P</code>, <code>--pairs</code> </p>
<dl>
<dd> <p> Produce output in the form of key=&quot;value&quot; pairs. All potentially unsafe value characters are hex-escaped (\x&lt;code&gt;). </p>
 </dd></dl>
<p> <code>-r</code>, <code>--raw</code> </p>
<dl>
<dd> <p> Produce output in raw format. All potentially unsafe characters are hex-escaped (\x&lt;code&gt;). </p>
 </dd></dl>
<p> <code>-S</code>, <code>--split</code> <i>list</i> </p>
<dl>
<dd> <p> Specify which columns (attributes) use to split memory blocks to ranges. The supported columns are STATE, REMOVABLE, NODE and ZONES, or &quot;none&quot;. The other columns are silently ignored. For more details see DESCRIPTION above. </p>
 </dd></dl>
<p> <code>-s</code>, <code>--sysroot</code> <i>directory</i> </p>
<dl>
<dd> <p> Gather memory data for a Linux instance other than the instance from which the <code>lsmem</code> command is issued. The specified <i>directory</i> is the system root of the Linux instance to be inspected. </p>
 </dd></dl>
<p> <code>-V</code>, <code>--version</code> </p>
<dl>
<dd> <p> Display version information and exit. </p>
 </dd></dl>
<p> <code>--summary</code>[=<i>when</i>] </p>
<dl>
<dd> <p> This option controls summary lines output. The optional argument <i>when</i> can be <code>never</code>, <code>always</code> or <code>only</code>. If the <i>when</i> argument is omitted, it defaults to <code>&quot;only&quot;</code>. The summary output is suppressed for <code>--raw</code>, <code>--pairs</code> and <code>--json</code>. </p>
 </dd></dl>
<h2>AUTHORS</h2>
<p> <code>lsmem</code> was originally written by Gerald Schaefer for s390-tools in Perl. The C version for util-linux was written by Clemens von Mann, Heiko Carstens and Karel Zak.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-chmem/">chmem</a></code>(8)  </p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.  </p>
<h2>AVAILABILITY</h2>
<p> The <code>lsmem</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">OPTIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">AUTHORS</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">SEE ALSO</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">REPORTING BUGS</a></dt>
<dd>  </dd>
<dt><a href="#lbAI">AVAILABILITY</a></dt>
<dd>  </dd></dl>
