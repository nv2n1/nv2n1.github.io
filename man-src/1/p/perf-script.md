---
title: "perf-script(1)"
name: "perf-script"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perf-script/"
description: "perf-script – Read perf.data (created by perf record) and display trace output"
---

<h2>SYNOPSIS</h2>
<pre><code>
perf script[&lt;options&gt;] perf script[&lt;options&gt;] record&lt;script&gt;[&lt;record - options&gt;]&lt;command&gt;
    perf script[&lt;options&gt;] report&lt;script&gt;[script - args] perf script[&lt;options&gt;]&lt;script&gt;&lt;required - script - args&gt;[&lt;record - options&gt;]&lt;command&gt;
        perf script[&lt;options&gt;]&lt;top - script&gt;[script - args]
</code></pre>
<h2>DESCRIPTION</h2>
<p> This command reads the input file and displays the trace recorded. </p>
<p> There are several variants of perf script: </p>
<dl>
<dt>
</dt><dd>
<pre>
'perf script' to see a detailed trace of the workload that was
recorded.
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
You can also run a set of pre-canned scripts that aggregate and
summarize the raw trace data in various ways (the list of scripts is
available via 'perf script -l').  The following variants allow you to
record and run those scripts:
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
'perf script record &lt;script&gt; &lt;command&gt;' to record the events required
for 'perf script report'.  &lt;script&gt; is the name displayed in the
output of 'perf script --list' i.e. the actual script name minus any
language extension.  If &lt;command&gt; is not specified, the events are
recorded using the -a (system-wide) 'perf record' option.
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
&#8216;perf script report &lt;script&gt; [args]&#8217; to run and display the results<br />
    of&lt;script&gt;<br />
        .&lt;script&gt;is the name displayed in the output of &#8216;perf trace&#8211; list&#8217; i.e. the actual script name minus any language extension.The perf.data output from a previous run of &#8216;perf script record&lt;script&gt;&#8217; is used and should be present for this command to succeed.[args] refers to the(mainly optional) args expected by<br />
    the script.
</dd></dl>
<dl>
<dt>
</dt><dd>
&#8216;perf script &lt;script&gt; &lt;required-script-args&gt; &lt;command&gt;&#8217; to both<br />
record the events required for &lt;script&gt; and to run the &lt;script&gt;<br />
using &#8216;live-mode&#8217; i.e. without writing anything to disk.  &lt;script&gt;<br />
is the name displayed in the output of &#8216;perf script &#8211;list&#8217; i.e. the<br />
actual script name minus any language extension.  If &lt;command&gt; is<br />
not specified, the events are recorded using the -a (system-wide)<br />
&#8216;perf record&#8217; option.  If &lt;script&gt; has any required args, they<br />
should be specified before &lt;command&gt;.  This mode doesn&#8217;t allow for<br />
optional script args to be specified;<br />
if optional<br />
script args are<br />
    desired,<br />
    they can be specified using separate &#8216;perf script record&#8217; and &#8216;perf script report&#8217; commands, with the stdout of the record step piped to the stdin of the report script, using the &#8216;-o -&#8216; and &#8216;-i -&#8216; options of the corresponding commands.
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
'perf script &lt;top-script&gt;' to both record the events required for
&lt;top-script&gt; and to run the &lt;top-script&gt; using 'live-mode'
i.e. without writing anything to disk.  &lt;top-script&gt; is the name
displayed in the output of 'perf script --list' i.e. the actual
script name minus any language extension; a &lt;top-script&gt; is defined
as any script name ending with the string 'top'.
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre><code>
[&lt;record-options&gt;] can be passed to the record steps of 'perf script
record' and 'live-mode' variants; this isn't possible however for
&lt;top-script&gt; 'live-mode' or 'perf script report' variants.
</code></pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
See the 'SEE ALSO' section for links to language-specific
information on how to write and run your own trace scripts.
</pre>
</dd></dl>
<h2>OPTIONS</h2>
<p> &lt;command&gt;&#8230;</p>
<dl>
<dt>
</dt><dd> Any command you can specify in a shell.</dd></dl>
<p> -D, &#8211;dump-raw-script=</p>
<dl>
<dt>
</dt><dd> Display verbose dump of the trace data.</dd></dl>
<p> -L, &#8211;Latency=</p>
<dl>
<dt>
</dt><dd> Show latency attributes (irqs/preemption disabled, etc).</dd></dl>
<p> -l, &#8211;list=</p>
<dl>
<dt>
</dt><dd> Display a list of available trace scripts.</dd></dl>
<p> -s [<i>lang</i>], &#8211;script=</p>
<dl>
<dt>
</dt><dd> Process trace data with the given script ([lang]:script[.ext]). If the string <i>lang</i> is specified in place of a script name, a list of supported languages will be displayed instead.</dd></dl>
<p> -g, &#8211;gen-script=</p>
<dl>
<dt>
</dt><dd> Generate perf-script.[ext] starter script for given language, using current perf.data.</dd></dl>
<p> -a</p>
<dl>
<dt>
</dt><dd> Force system-wide collection. Scripts run without a &lt;command&gt; normally use -a by default, while scripts run with a &lt;command&gt; normally don&#8217;t &#8211; this option allows the latter to be run in system-wide mode.</dd></dl>
<p> -i, &#8211;input=</p>
<dl>
<dt>
</dt><dd> Input file name. (default: perf.data unless stdin is a fifo)</dd></dl>
<p> -d, &#8211;debug-mode</p>
<dl>
<dt>
</dt><dd> Do various checks like samples ordering and lost events.</dd></dl>
<p> -f, &#8211;fields</p>
<dl>
<dt>
</dt><dd> Comma separated list of fields to print. Options are: comm, tid, pid, time, cpu, event, trace, ip, sym, dso, addr, symoff, srcline, period. Field list can be prepended with the type, trace, sw or hw, to indicate to which event type the field list applies. e.g., -f sw:comm,tid,time,ip,sym and -f trace:time,cpu,trace </dd>
<dl>
<dt>
</dt><dd>
<pre>
perf script -f &lt;fields&gt;
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
is equivalent to:
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
perf script -f trace:&lt;fields&gt; -f sw:&lt;fields&gt; -f hw:&lt;fields&gt;
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
i.e., the specified fields apply to all event types if the type string
is not given.
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
The arguments are processed in the order received. A later usage can
reset a prior request. e.g.:
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
-f trace: -f comm,tid,time,ip,sym
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
The first -f suppresses trace events (field list is &quot;&quot;), but then the
second invocation sets the fields to comm,tid,time,ip,sym. In this case a
warning is given to the user:
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
&quot;Overriding previous field request for all events.&quot;
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
Alternatively, consider the order:
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
-f comm,tid,time,ip,sym -f trace:
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
The first -f sets the fields for all events and the second -f
suppresses trace events. The user is given a warning message about
the override, and the result of the above is that only S/W and H/W
events are displayed with the given fields.
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
For the 'wildcard' option if a user selected field is invalid for an
event type, a message is displayed to the user that the option is
ignored for that type. For example:
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
$ perf script -f comm,tid,trace
'trace' not valid for hardware events. Ignoring.
'trace' not valid for software events. Ignoring.
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
Alternatively, if the type is given an invalid field is specified it
is an error. For example:
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
perf script -v -f sw:comm,tid,trace
'trace' not valid for software events.
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
At this point usage is displayed, and perf-script exits.
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
Finally, a user may not set fields to none for all event types.
i.e., -f &quot;&quot; is not allowed.
</pre>
</dd></dl>
</dl>
<p> -k, &#8211;vmlinux=&lt;file&gt;</p>
<dl>
<dt>
</dt><dd> vmlinux pathname</dd></dl>
<p> &#8211;kallsyms=&lt;file&gt;</p>
<dl>
<dt>
</dt><dd> kallsyms pathname</dd></dl>
<p> &#8211;symfs=&lt;directory&gt;</p>
<dl>
<dt>
</dt><dd> Look for files with symbols relative to this directory.</dd></dl>
<p> -G, &#8211;hide-call-graph</p>
<dl>
<dt>
</dt><dd> When printing symbols do not display call chain.</dd></dl>
<p> -C, &#8211;cpu</p>
<dl>
<dt>
</dt><dd> Only report samples for the list of CPUs provided. Multiple CPUs can be provided as a comma-separated list with no space: 0,1. Ranges of CPUs are specified with -: 0-2. Default is to report samples on all CPUs.</dd></dl>
<p> -c, &#8211;comms=</p>
<dl>
<dt>
</dt><dd> Only display events for these comms. CSV that understands m[blue]<code>file://filename</code>m[] entries.</dd></dl>
<p> -I, &#8211;show-info</p>
<dl>
<dt>
</dt><dd> Display extended information about the perf.data file. This adds information which may be very large and thus may clutter the display. It currently includes: cpu and numa topology of the host system. It can only be used with the perf script report mode.</dd></dl>
<p> &#8211;show-kernel-path</p>
<dl>
<dt>
</dt><dd> Try to resolve the path of [kernel.kallsyms]</dd></dl>
<p> &#8211;show-task-events Display task related events (e.g. FORK, COMM, EXIT). </p>
<p> &#8211;show-mmap-events Display mmap related events (e.g. MMAP, MMAP2). </p>
<p> &#8211;header Show perf.data header. </p>
<p> &#8211;header-only Show only perf.data header.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perf-record/">perf-record</a></code>(1), <code><a href="/docs/linux/man/1-perf-script-perl/">perf-script-perl</a></code>(1), <code><a href="/docs/linux/man/1-perf-script-python/">perf-script-python</a></code>(1) </p>
