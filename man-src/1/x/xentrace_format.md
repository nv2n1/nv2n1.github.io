---
title: "xentrace_format(1)"
name: "xentrace_format"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xentrace_format/"
description: "xentrace_format – pretty-print Xen trace data"
---

<h2>NAME</h2>
<p> xentrace_format &#8211; pretty-print Xen trace data</p>
<h2>SYNOPSIS</h2>
<p> <code>xentrace_format</code> [ <i>DEFS-FILE</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>xentrace_format</code> parses trace data in <code>xentrace</code> binary format from standard input and reformats it according to the rules in a file of definitions (<i>DEFS-FILE</i>), printing to standard output. </p>
<p> The rules in <i>DEFS-FILE</i> should have the format shown below: </p>
<p> <i>event_id</i> <i>whitespace</i> <i>format</i> </p>
<p> Each rule should start on a new line. </p>
<p> The format string may include format specifiers, such as: %(cpu)d, %(tsc)d, %(event)d, %(1)d, %(2)d, %(3)d, %(4)d, %(5)d </p>
<p> [ the `d&#8217; format specifier output in decimal, alternatively `x&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>will output in hexadecimal and&nbsp;<wbr>`o&#8217;&nbsp;<wbr>will output in octal&nbsp;<wbr>] </p>
<p> These correspond to the CPU number, event ID, timestamp counter and the 5 data fields from the trace record. There should be one such rule for each type of event to be pretty-printed (events which do not have formatting rules are ignored). </p>
<p> A sample format file for Xen&#8217;s predefined trace events is available in the file tools/xentrace/formats in the Xen source tree. </p>
<p> Depending on your system and the rate at which trace data is produced, this script may not be able to keep up with the output of <code>xentrace</code> if it is piped directly. In these circumstances you should have <code>xentrace</code> output to a file for processing off-line. </p>
<h2>AUTHOR</h2>
<p> Mark A. Williamson &lt;mark.a.williamson [at] intel.com&gt; </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-xentrace/">xentrace</a>(8), <a href="/docs/linux/man/1-xentrace_cpusplit/">xentrace_cpusplit</a>(1) </p>
<h2>Index</h2>
