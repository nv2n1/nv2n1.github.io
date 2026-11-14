---
title: "flow-header(1)"
name: "flow-header"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flow-header/"
description: "flow-header – Display meta information in flow file."
---

<h2>NAME</h2>
<p> flow-header &#8211; Display meta information in flow file.</p>
<h2>SYNOPSIS</h2>
<p> <code>flow-header</code> [ <code>-h</code> ] [ <code>-c</code><i> comment_char</i> ] [ <code>-d</code><i> debug_level</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>flow-header</code> utility will display the flow meta information flow-tools uses internally.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code><i> comment_char</i></p>
<dd> Field header. Defaults to #</p>
<dt><code>-d</code><i> debug_level</i></p>
<dd> Turn on debugging.</p>
<dt><code>-h</code></p>
<dd> Display help.</dl>
<h2>EXAMPLES</h2>
<p> Display the header information in <i>flowfile</i> <code>flow-header &lt; </code><i>flowfile</i> </p>
<pre>
#
# mode:                 normal
# capture hostname:     foo.bar
# exporter IP address:  10.0.0.1
# capture start:        Wed May  1 23:45:02 2001
# compress:             on
# byte order:           little
# stream version:       3
# export version:       5
# lost flows:           480
# corrupt packets:      0
# sequencer resets:     0
# capture end:          Thu May  2 00:00:01 2001
# capture flows:        65880
</pre>
<h2>BUGS</h2>
<p> None known.</p>
<h2>AUTHOR</h2>
<p> Mark Fullmer &lt;maf [at] splintered.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flow-tools/">flow-tools</a></code>(1) </p>
<h2>Index</h2>
