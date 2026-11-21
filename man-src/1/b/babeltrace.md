---
title: "babeltrace(1)"
name: "babeltrace"
section: "1"
letter: "b"
url: "/docs/linux/man/1-babeltrace/"
description: "babeltrace — Babeltrace Trace Viewer and Converter"
---

<h2 class="name">NAME</h2>
<p> babeltrace &#8212; Babeltrace Trace Viewer and Converter</p>
<h2>SYNOPSIS</h2>
<pre>
babeltrace [OPTIONS] FILE...
</pre>
<h2>DESCRIPTION</h2>
<p> Babeltrace is a trace viewer and converter reading and writing the Common Trace Format (CTF). Its main use is to pretty-print CTF traces into a human-readable text output ordered by time. </p>
<p> This program follow the usual GNU command line syntax with long options starting with two dashes. Below is a summary of the available options. </p>
<dl>
<dt><code>FILE</code></dt>
<dd> Input trace FILE(s) or directory(ies)</dd>
<dt><code>-w, &#8211;output OUTPUT</code></dt>
<dd> Output trace path (default: stdout)</dd>
<dt><code>-i, &#8211;input-format FORMAT</code></dt>
<dd> Input trace format (default: ctf). CTF is currently the only supported input format.</dd>
<dt><code>-o, &#8211;output-format FORMAT</code></dt>
<dd> Output trace format (default: text)</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> This help message</dd>
<dt><code>-l, &#8211;list</code></dt>
<dd> List available formats</dd>
<dt><code>-v, &#8211;verbose</code></dt>
<dd> Verbose mode (or set BABELTRACE_VERBOSE environment variable)</dd>
<dt><code>-d, &#8211;debug</code></dt>
<dd> Debug mode (or set BABELTRACE_DEBUG environment variable)</dd>
<dt><code>&#8211;no-delta</code></dt>
<dd> Do not print time delta between consecutive events</dd>
<dt><code>-n, &#8211;names name1&lt;,name2,&#8230;&gt;</code></dt>
<dd> Print field names: (payload OR args OR arg), none, all, scope, header, (context OR ctx), (default: payload,context).</dd>
<dt><code>-f, &#8211;fields name1&lt;,name2,&#8230;&gt;</code></dt>
<dd> Print additional fields: all, trace, trace:hostname, trace:domain, trace:procname, trace:vpid, loglevel.</dd>
<dt><code>&#8211;clock-raw</code></dt>
<dd> Disregard internal clock offset (use raw value)</dd>
<dt><code>&#8211;clock-offset seconds</code></dt>
<dd> Clock offset in seconds</dd>
<dt><code>&#8211;clock-seconds</code></dt>
<dd> Print the timestamps as [sec.ns] (default is: [hh:mm:ss.ns])</dd>
<dt><code>&#8211;clock-date</code></dt>
<dd> Print clock date</dd>
<dt><code>&#8211;clock-gmt</code></dt>
<dd> Print clock in GMT time zone (default: local time zone)</dd>
<dt>
</dt><dd> Formats available: ctf, dummy, text. </dd>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> Note that all command line options will override environmenal variables. </p>
<dl>
<dt>BABELTRACE_VERBOSE</dt>
<dd> Activate verbose Babeltrace output.</dd></dl>
<dl>
<dt>BABELTRACE_DEBUG</dt>
<dd> Activate debug Babeltrace output. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-babeltrace-log/">babeltrace-log</a>(1), <a href="/docs/linux/man/1-lttng/">lttng</a>(1), <a href="/docs/linux/man/3-lttng-ust/">lttng-ust</a>(3), <a href="/docs/linux/man/8-lttng-sessiond/">lttng-sessiond</a>(8) </p>
<h2>BUGS</h2>
<p> No known bugs at this point. </p>
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
