---
title: "babeltrace-log(1)"
name: "babeltrace-log"
section: "1"
letter: "b"
url: "/docs/linux/man/1-babeltrace-log/"
description: "babeltrace-log — Babeltrace Log Converter"
---

<h2 class="name">NAME</h2>
<p> babeltrace-log &#8212; Babeltrace Log Converter</p>
<h2>SYNOPSIS</h2>
<pre>
babeltrace-log [OPTIONS] OUTPUT
</pre>
<h2>DESCRIPTION</h2>
<p> Convert for a text log (read from standard input) to CTF. </p>
<p> This program follow the usual GNU command line syntax with long options starting with two dashes. Below is a summary of the available options. </p>
<dl>
<dt><code>OUTPUT</code></p>
<dd> Output trace path</p>
<dt><code>-t</code></p>
<dd> With timestamps (format: [sec.usec] string
)</p>
<dt>
<dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-babeltrace/">babeltrace</a>(1), <a href="/docs/linux/man/1-lttng/">lttng</a>(1), <a href="/docs/linux/man/3-lttng-ust/">lttng-ust</a>(3), <a href="/docs/linux/man/8-lttng-sessiond/">lttng-sessiond</a>(8) </p>
<h2>BUGS</h2>
<p> No knows bugs at this point. </p>
<p> If you encounter any issues or usability problem, please report it on our mailing list &lt;lttng-dev [at] lists.lttng.org&gt; to help improve this project.</p>
<h2>CREDITS</h2>
<p> Babeltrace and the babeltrace library are distributed under the MIT license. See the files LICENSE and mit-license.txt for details. </p>
<p> A Web site is available at <a rel="nofollow" href="http://www.efficios.com/babeltrace">http://www.efficios.com/babeltrace</a> for more information on Babeltrace and the Common Trace Format. See <a rel="nofollow" href="http://lttng.org">http://lttng.org</a> for more information on the LTTng project. </p>
<p> Mailing list for support and development: &lt;lttng-dev [at] lists.lttng.org&gt;. </p>
<p> You can find us on IRC server irc.oftc.net (OFTC) in #lttng. </p>
<h2>THANKS</h2>
<p> Thanks to the Linux Foundation and Ericsson for funding part of this work. Thanks to the Multicore Association Tool Infrastructure Working Group for their active role in the creation of the Common Trace Format. </p>
<h2>AUTHORS</h2>
<p> Babeltrace was originally written by Mathieu Desnoyers, with additional contributions from various other people. It is currently maintained by Mathieu Desnoyers &lt;mathieu.desnoyers [at] efficios.com&gt;. </p>
<h2>Index</h2>
