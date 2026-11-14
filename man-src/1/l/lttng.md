---
title: "lttng(1)"
name: "lttng"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lttng/"
description: "lttng — LTTng 2.x tracer control command line tool"
---

<h2 class="name">NAME</h2>
<p> lttng &#8212; LTTng 2.x tracer control command line tool</p>
<h2>SYNOPSIS</h2>
<p> lttng [OPTIONS] &lt;COMMAND&gt;</p>
<h2>DESCRIPTION</h2>
<p> The LTTng project aims at providing highly efficient tracing tools for Linux. Its tracers help track down performance issues and debug problems involving multiple concurrent processes and threads. Tracing across multiple systems is also possible. </p>
<p> The <code>lttng</code> command line tool from the lttng-tools package is used to control both kernel and user-space tracing. Every interaction with the tracer should be done by this tool or by the liblttng-ctl library provided by the lttng-tools package. </p>
<p> LTTng uses a session daemon (<a href="/docs/linux/man/8-lttng-sessiond/">lttng-sessiond</a>(8)), acting as a tracing registry, which allows you to interact with multiple tracers (kernel and user-space) inside the same container, a tracing session. Traces can be gathered from the kernel and/or instrumented applications (<a href="/docs/linux/man/3-lttng-ust/">lttng-ust</a>(3)). Aggregating and reading those traces is done using the <a href="/docs/linux/man/1-babeltrace/">babeltrace</a>(1) text viewer. </p>
<p> We introduce the notion of <code>tracing domains</code> which is essentially a type of tracer (kernel, user space or JUL for now). In the future, we could see more tracer like for instance an hypervisor. For some commands, you&#8217;ll need to specify on which domain the command operates (-u, -k or -j). For instance, the kernel domain must be specified when enabling a kernel event. </p>
<p> In order to trace the kernel, the session daemon needs to be running as root. LTTng provides the use of a <code>tracing group</code> (default: tracing). Whomever is in that group can interact with the root session daemon and thus trace the kernel. Session daemons can co-exist, meaning that you can have a session daemon running as Alice that can be used to trace her applications along side with a root daemon or even a Bob daemon. We highly recommend starting the session daemon at boot time for stable and long term tracing. </p>
<p> Each user-space application instrumented with <a href="/docs/linux/man/3-lttng-ust/">lttng-ust</a>(3) will automatically register with the root session daemon and its user session daemon. This allows each daemon to list the available traceable applications and tracepoints at any given moment (See the <code>list</code> command).</p>
<h2>OPTIONS</h2>
<p> This program follow the usual GNU command line syntax with long options starting with two dashes. Below is a summary of the available options. </p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of possible options and commands.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Increase verbosity. Three levels of verbosity are available which are triggered by putting additional v to the option (-vv or -vvv)</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Suppress all messages (even errors).</p>
<dt><code>-g, &#8211;group NAME</code></p>
<dd> Set unix tracing group name. (default: tracing)</p>
<dt><code>-n, &#8211;no-sessiond</code></p>
<dd> Don&#8217;t automatically spawn a session daemon.</p>
<dt><code>&#8211;sessiond-path PATH</code></p>
<dd> Set session daemon full binary path.</p>
<dt><code>&#8211;list-options</code></p>
<dd> Simple listing of lttng options.</p>
<dt><code>&#8211;list-commands</code></p>
<dd> Simple listing of lttng commands.</dl>
<h2>COMMANDS</h2>
<p> <code>add-context</code> [OPTIONS]</p>
<dl>
<dt>
<dd> Add context to event(s) and/or channel(s). </p>
<p> A context is basically extra information appended to a channel. For instance, you could ask the tracer to add the PID information for all events in a channel. You can also add performance monitoring unit counters (perf PMU) using the perf kernel API). </p>
<p> For example, this command will add the context information &#8216;prio&#8217; and two perf counters (hardware branch misses and cache misses), to all events in the trace data output: </p>
<pre>
# lttng add-context -k -t prio -t perf:branch-misses \
                -t perf:cache-misses
</pre>
<p> Please take a look at the help (-h/&#8211;help) for a detailed list of available contexts. </p>
<p> If no channel is given (-c), the context is added to all channels that were already enabled. If the session has no channel, a default channel is created. Otherwise the context will be added only to the given channel (-c). </p>
<p> If <code>-s, &#8211;session</code> is omitted, the session name is taken from the .lttngrc file. </p>
<p> <code>OPTIONS:</code> </p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of possible options and commands.</p>
<dt><code>-s, &#8211;session NAME</code></p>
<dd> Apply on session name.</p>
<dt><code>-c, &#8211;channel NAME</code></p>
<dd> Apply on channel name.</p>
<dt><code>-k, &#8211;kernel</code></p>
<dd> Apply for the kernel tracer</p>
<dt><code>-u, &#8211;userspace</code></p>
<dd> Apply for the user-space tracer</p>
<dt><code>-t, &#8211;type TYPE</code></p>
<dd> Context type. You can repeat this option on the command line. Please use &quot;lttng add-context -h&quot; to list all available types.</dl>
</dl>
<p> <code>calibrate</code> [OPTIONS]</p>
<dl>
<dt>
<dd> Quantify LTTng overhead </p>
<p> The LTTng calibrate command can be used to find out the combined average overhead of the LTTng tracer and the instrumentation mechanisms used. This overhead can be calibrated in terms of time or using any of the PMU performance counter available on the system. </p>
<p> For now, the only calibration implemented is that of the kernel function instrumentation (kretprobes). </p>
<p> * Calibrate kernel function instrumentation </p>
<p> Let&#8217;s use an example to show this calibration. We use an i7 processor with 4 general-purpose PMU registers. This information is available by issuing dmesg, looking for &quot;generic registers&quot;. </p>
<p> This sequence of commands will gather a trace executing a kretprobe hooked on an empty function, gathering PMU counters LLC (Last Level Cache) misses information (see lttng add-context &#8211;help to see the list of available PMU counters). </p>
<pre><code>
#lttng create calibrate - function
#lttng enable - event calibrate-- kernel-- function lttng_calibrate_kretprobe
#lttng add - context-- kernel - t perf : LLC - load - misses - t perf : LLC - store - misses - t perf : LLC - prefetch - misses
#lttng start
#for a in $(seq 1 10); do lttng calibrate-- kernel-- function;
done
#lttng destroy
#babeltrace $(ls - 1drt ~ / lttng - traces / calibrate - function - * | tail - n 1)
</code></pre>
<p> The output from babeltrace can be saved to a text file and opened in a spreadsheet (e.g. oocalc) to focus on the per-PMU counter delta between consecutive &quot;calibrate_entry&quot; and &quot;calibrate_return&quot; events. Note that these counters are per-CPU, so scheduling events would need to be present to account for migration between CPU. Therefore, for calibration purposes, only events staying on the same CPU must be considered. </p>
<p> The average result, for the i7, on 10 samples: </p>
<pre>
                          Average     Std.Dev.
perf_LLC_load_misses:       5.0       0.577
perf_LLC_store_misses:      1.6       0.516
perf_LLC_prefetch_misses:   9.0      14.742
</pre>
<p> As we can notice, the load and store misses are relatively stable across runs (their standard deviation is relatively low) compared to the prefetch misses. We can conclude from this information that LLC load and store misses can be accounted for quite precisely, but prefetches within a function seems to behave too erratically (not much causality link between the code executed and the CPU prefetch activity) to be accounted for. </p>
<p> <code>OPTIONS:</code> </p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of possible options and commands.</p>
<dt><code>-k, &#8211;kernel</code></p>
<dd> Apply for the kernel tracer</p>
<dt><code>-u, &#8211;userspace</code></p>
<dd> Apply for the user-space tracer</p>
<dt><code>&#8211;function</code></p>
<dd> Dynamic function entry/return probe (default)</dl>
</dl>
<p> <code>create</code> [NAME] [OPTIONS]</p>
<dl>
<dt>
<dd> Create tracing session. </p>
<p> A tracing session contains channel(s) which contains event(s). It is domain agnostic, meaning that channels and events can be enabled for the user-space tracer and/or the kernel tracer. It acts like a container aggregating multiple tracing sources. </p>
<p> On creation, a <code>.lttngrc</code> file is created in your $HOME directory containing the current session name. If NAME is omitted, a session name is automatically created having this form: &#8216;auto-yyyymmdd-hhmmss&#8217;. </p>
<p> If no <code>-o, &#8211;output</code> is specified, the traces will be written in $HOME/lttng-traces. </p>
<p> The $HOME environment variable can be overridden by defining the environment variable LTTNG_HOME. This is useful when the user running the commands has a non-writeable home directory. </p>
<p> The session name MUST NOT contain the character &#8216;/&#8217;. </p>
<p> <code>OPTIONS:</code> </p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of possible options and commands.</p>
<dt><code>&#8211;list-options</code></p>
<dd> Simple listing of options</p>
<dt><code>-o, &#8211;output PATH</code></p>
<dd> Specify output path for traces</p>
<dt><code>&#8211;no-output</code></p>
<dd> Traces will not be output</p>
<dt><code>&#8211;snapshot</code></p>
<dd> Set the session in snapshot mode. Created in no-output mode and uses the URL, if one is specified, as the default snapshot output. Every channel will be set in overwrite mode and with mmap output (splice not supported).</p>
<dt><code>&#8211;live [USEC]</code></p>
<dd> Set the session exclusively in live mode. The paremeter is the delay in micro seconds before the data is flushed and streamed. The live mode allows you to stream the trace and view it while it&#8217;s being recorded by any tracer. For that, you need a lttng-relayd and this session requires a network URL (-U or -C/-D). If no USEC nor URL is provided, the default is to use a timer value set to 1000000 and the network URL set to <a href="net://127.0.0.1.">net://127.0.0.1.</a> </p>
<p> To read a live session, you can use <a href="/docs/linux/man/1-babeltrace/">babeltrace</a>(1) or the live streaming protocol in doc/live-reading-protocol.txt. Here is an example: </p>
<pre>
$ lttng-relayd -o /tmp/lttng
$ lttng create --live 200000 -U <a href="net://localhost">net://localhost</a>
$ lttng enable-event -a --userspace
$ lttng start
</pre>
<p> After the start, you&#8217;ll be able to read the events while they are being recorded in /tmp/lttng. </p>
<dt><code>-U, &#8211;set-url=URL</code></p>
<dd> Set URL for the consumer output destination. It is persistent for the session lifetime. Redo the command to change it. This will set both data and control URL for network.</p>
<dt><code>-C, &#8211;ctrl-url=URL</code></p>
<dd> Set control path URL. (Must use -D also)</p>
<dt><code>-D, &#8211;data-url=URL</code></p>
<dd> Set data path URL. (Must use -C also)</dl>
<p> Using these options, each API call can be controlled individually. For instance, -C does not enable the consumer automatically. You&#8217;ll need the -e option for that. </p>
<p> <code>URL FORMAT:</code> </p>
<p> <a href="proto://[HOST|IP][:PORT1[:PORT2]][/TRACE_PATH]">proto://[HOST|IP][:PORT1[:PORT2]][/TRACE_PATH]</a> </p>
<p> Supported protocols are (proto):</p>
<dl>
<dt><code>file://&#8230;</code></p>
<dd> Local filesystem full path. </p>
<dt><code><a href="net://...">net://&#8230;</a></code></p>
<dd> This will use the default network transport layer which is TCP for both control (PORT1) and data port (PORT2). The default ports are respectively 5342 and 5343. Note that net[6]:// is not yet supported. </p>
<dt><code>tcp[6]://&#8230;</code></p>
<dd> Can only be used with -C and -D together </p>
<p> NOTE: IPv6 address MUST be enclosed in brackets &#8216;[]&#8217; (rfc2732) </p>
<p> <code>EXAMPLES:</code> </p>
<pre>
# lttng create -U <a href="net://192.168.1.42">net://192.168.1.42</a>
</pre>
<p> Uses TCP and default ports for the given destination. </p>
<pre>
# lttng create -U net6://[fe80::f66d:4ff:fe53:d220]
</pre>
<p> Uses TCP, default ports and IPv6. </p>
<pre>
# lttng create s1 -U <a href="net://myhost.com:3229">net://myhost.com:3229</a>
</pre>
<p> Create session s1 and set its consumer to myhost.com on port 3229 for control.</dl>
</dl>
<p> <code>destroy</code> [NAME] [OPTIONS]</p>
<dl>
<dt>
<dd> Teardown tracing session </p>
<p> Free memory on the session daemon and tracer side. It&#8217;s gone! </p>
<p> If NAME is omitted, the session name is taken from the .lttngrc file. </p>
<p> <code>OPTIONS:</code> </p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of possible options and commands.</p>
<dt><code>-a, &#8211;all</code></p>
<dd> Destroy all sessions</p>
<dt><code>&#8211;list-options</code></p>
<dd> Simple listing of options</dl>
</dl>
<p> <code>enable-channel</code> NAME[,NAME2,&#8230;] (-k | -u) [OPTIONS]</p>
<dl>
<dt>
<dd> Enable tracing channel </p>
<p> To enable an event, you must enable both the event and the channel that contains it. </p>
<p> If <code>-s, &#8211;session</code> is omitted, the session name is taken from the .lttngrc file. </p>
<p> Exactly one of -k or -u must be specified. </p>
<p> It is important to note that if a certain type of buffers is used, the session will be set with that type and all other subsequent channel needs to have the same type. </p>
<p> Note that once the session has been started and enabled on the tracer side, it&#8217;s not possible anymore to enable a new channel for that session. </p>
<p> <code>OPTIONS:</code> </p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show this help</p>
<dt><code>&#8211;list-options</code></p>
<dd> Simple listing of options</p>
<dt><code>-s, &#8211;session NAME</code></p>
<dd> Apply on session name</p>
<dt><code>-k, &#8211;kernel</code></p>
<dd> Apply to the kernel tracer</p>
<dt><code>-u, &#8211;userspace</code></p>
<dd> Apply to the user-space tracer</p>
<dt><code>&#8211;discard</code></p>
<dd> Discard event when subbuffers are full (default)</p>
<dt><code>&#8211;overwrite</code></p>
<dd> Flight recorder mode : overwrites events when subbuffers are full</p>
<dt><code>&#8211;subbuf-size SIZE</code></p>
<dd> Subbuffer size in bytes {+k,+M,+G}. (default UST uid: 131072, UST pid: 4096, kernel: 262144, metadata: 4096) Rounded up to the next power of 2. </p>
<p> The minimum subbuffer size, for each tracer, is the max value between the default above and the system page size. You can issue this command to get the current page size on your system: <code>$ getconf PAGE_SIZE</code></p>
<dt><code>&#8211;num-subbuf NUM</code></p>
<dd> Number of subbuffers. (default UST uid: 4, UST pid: 4, kernel: 4, metadata: 2) Rounded up to the next power of 2.</p>
<dt><code>&#8211;switch-timer USEC</code></p>
<dd> Switch subbuffer timer interval in µsec. (default UST uid: 0, UST pid: 0, kernel: 0, metadata: 0)</p>
<dt><code>&#8211;read-timer USEC</code></p>
<dd> Read timer interval in µsec. (default UST uid: 0, UST pid: 0, kernel: 200000, metadata: 0)</p>
<dt><code>&#8211;output TYPE</code></p>
<dd> Channel output type. Possible values: mmap, splice (default UST uid: mmap, UST pid: mmap, kernel: splice, metadata: mmap)</p>
<dt><code>&#8211;buffers-uid</code></p>
<dd> Use per UID buffer (-u only). Buffers are shared between applications that have the same UID.</p>
<dt><code>&#8211;buffers-pid</code></p>
<dd> Use per PID buffer (-u only). Each application has its own buffers.</p>
<dt><code>&#8211;buffers-global</code></p>
<dd> Use shared buffer for the whole system (-k only)</p>
<dt><code>-C, &#8211;tracefile-size SIZE</code></p>
<dd> Maximum size of each tracefile within a stream (in bytes). 0 means unlimited. (default: 0)</p>
<dt><code>-W, &#8211;tracefile-count COUNT</code></p>
<dd> Used in conjunction with -C option, this will limit the number of files created to the specified count. 0 means unlimited. (default: 0) </p>
<p> <code>EXAMPLES:</code> </p>
<pre>
$ lttng enable-channel -k -C 4096 -W 32 chan1
</pre>
<p> For each stream, the maximum size of each trace file will be 4096 bytes and there will be a maximum of 32 different files. The file count is appended after the stream number as seen in the following example. The last trace file is smaller than 4096 since it was not completely filled. </p>
<p>~ / lttng &#8211; traces / [&#8230;] / chan1_0_0(4096) ~ / lttng &#8211; traces / [&#8230;] / chan1_0_1(4096) ~ / lttng &#8211; traces / [&#8230;] / chan1_0_2(3245) ~ / lttng &#8211; traces / [&#8230;] / chan1_1_0(4096)&#8230;</p>
<pre>
$ lttng enable-channel -k -C 4096
</pre>
<p> This will create trace files of 4096 bytes and will create new ones as long as there is data available.</dl>
</dl>
<p> <code>enable-event</code> NAME[,NAME2,&#8230;] [-k|-u] [OPTIONS]</p>
<dl>
<dt>
<dd> Enable tracing event </p>
<p> A tracing event is always assigned to a channel. If <code>-c, &#8211;channel</code> is omitted, a default channel named &#8216;<code>channel0</code>&#8216; is created and the event is added to it. If <code>-c, &#8211;channel</code> is omitted, but a non-default channel already exists within the session, an error is returned. For the user-space tracer, using <code>-a, &#8211;all</code> is the same as using the wildcard &quot;*&quot;. </p>
<p> If <code>-s, &#8211;session</code> is omitted, the session name is taken from the .lttngrc file. </p>
<p> <code>OPTIONS:</code> </p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of possible options and commands.</p>
<dt><code>&#8211;list-options</code></p>
<dd> Simple listing of options</p>
<dt><code>-s, &#8211;session NAME</code></p>
<dd> Apply on session name</p>
<dt><code>-c, &#8211;channel NAME</code></p>
<dd> Apply on channel name</p>
<dt><code>-a, &#8211;all</code></p>
<dd> Enable all tracepoints and syscalls. This actually enables a single wildcard event &quot;*&quot;.</p>
<dt><code>-k, &#8211;kernel</code></p>
<dd> Apply for the kernel tracer</p>
<dt><code>-u, &#8211;userspace</code></p>
<dd> Apply for the user-space tracer</p>
<dt><code>-j, &#8211;jul</code></p>
<dd> Apply for Java application using Java Util Logging interface (JUL)</p>
<dt><code>&#8211;tracepoint</code></p>
<dd> Tracepoint event (default). Userspace tracer supports wildcards at the end of string. Don&#8217;t forget to quote to deal with bash expansion. e.g.: </p>
<pre>
        &quot;*&quot;
        &quot;app_component:na*&quot;
</pre>
<dt><code>&#8211;loglevel NAME</code></p>
<dd> Tracepoint loglevel range from 0 to loglevel. Listed in the help (-h). For the JUL domain, the loglevel ranges are detailed with the &#8211;help option thus starting from SEVERE to FINEST.</p>
<dt><code>&#8211;loglevel-only NAME</code></p>
<dd> Tracepoint loglevel (only this loglevel). The loglevel or loglevel-only options should be combined with a tracepoint name or tracepoint wildcard.</p>
<dt><code>&#8211;probe (addr | symbol | symbol+offset)</code></p>
<dd> Dynamic probe. Addr and offset can be octal (0NNN&#8230;), decimal (NNN&#8230;) or hexadecimal (0xNNN&#8230;)</p>
<dt><code>&#8211;function (addr | symbol | symbol+offset)</code></p>
<dd> Dynamic function entry/return probe. Addr and offset can be octal (0NNN&#8230;), decimal (NNN&#8230;) or hexadecimal (0xNNN&#8230;)</p>
<dt><code>&#8211;syscall</code></p>
<dd> System call event. Enabling syscalls tracing (kernel tracer), you will not be able to disable them with disable-event. This is a known limitation. You can disable the entire channel to do the trick.</p>
<dt><code>&#8211;filter &#8216;expression&#8217;</code></p>
<dd> Set a filter on a newly enabled event. Filter expression on event fields and context. The event will be recorded if the filter&#8217;s expression evaluates to TRUE. Only specify on first activation of a given event within a session. Specifying a filter is only allowed when enabling events within a session before tracing is started. If the filter fails to link with the event within the traced domain, the event will be discarded. Filtering is currently only implemented for the user-space tracer. </p>
<p> Expression examples: </p>
<p>&#8216;intfield &gt; 500 &amp;&amp; intfield &lt; 503&#8217; &#8216;(strfield == &#8220;test&#8221; || intfield != 10) &amp;&amp; intfield &gt; 33&#8217; &#8216;doublefield &gt; 1.1 &amp;&amp; intfield &lt; 5.3&#8217;</p>
<p> Wildcards are allowed at the end of strings:<br />
&nbsp;<wbr>&nbsp;<wbr>&#8216;seqfield1&nbsp;<wbr>==&nbsp;<wbr>&quot;te*&quot;&#8217; In string literals, the escape character is a &#8216;\&#8217;. Use &#8216;\*&#8217; for the &#8216;*&#8217; character, and &#8216;\&#8217; for the &#8216;\&#8217; character sequence. Wildcard matches any sequence of characters, including an empty sub-string (matches 0 or more characters). </p>
<p> Context information can be used for filtering. The examples below shows usage of context filtering on the process name (using a wildcard), process ID range, and unique thread ID. The process and thread IDs of running applications can be found under columns &quot;PID&quot; and &quot;LWP&quot; of the &quot;ps -eLf&quot; command. </p>
<pre><code>
'$ctx.procname == "demo*"' '$ctx.vpid &gt;= 4433 &amp;&amp; $ctx.vpid &lt; 4455' '$ctx.vtid == 1234'
</code></pre>
<dt><code>-x, &#8211;exclude LIST</code></p>
<dd> Add exclusions to UST tracepoints: Events that match any of the items in the comma-separated LIST are not enabled, even if they match a wildcard definition of the event. </p>
<p> This option is also applicable with the <code>-a, &#8211;all</code> option, in which case all UST tracepoints are enabled except the ones whose names match any of the items in LIST.</dl>
</dl>
<p> <code>disable-channel</code> NAME[,NAME2,&#8230;] (-k | -u) [OPTIONS]</p>
<dl>
<dt>
<dd> Disable tracing channel </p>
<p> Disabling a channel disables the tracing of all of the channel&#8217;s events. A channel can be reenabled by calling <code>lttng enable-channel NAME</code> again. </p>
<p> If <code>-s, &#8211;session</code> is omitted, the session name is taken from the .lttngrc file. </p>
<p> <code>OPTIONS:</code> </p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of possible options and commands.</p>
<dt><code>&#8211;list-options</code></p>
<dd> Simple listing of options</p>
<dt><code>-s, &#8211;session NAME</code></p>
<dd> Apply on session name</p>
<dt><code>-k, &#8211;kernel</code></p>
<dd> Apply for the kernel tracer</p>
<dt><code>-u, &#8211;userspace</code></p>
<dd> Apply for the user-space tracer</dl>
</dl>
<p> <code>disable-event</code> NAME[,NAME2,&#8230;] (-k | -u) [OPTIONS]</p>
<dl>
<dt>
<dd> Disable tracing event </p>
<p> The event, once disabled, can be re-enabled by calling <code>lttng enable-event NAME</code> again. </p>
<p> If <code>-s, &#8211;session</code> is omitted, the session name is taken from the .lttngrc file. </p>
<p> If <code>-c, &#8211;channel</code> is omitted, the default channel name is used. If <code>-c, &#8211;channel</code> is omitted, but a non-default channel already exists within the session, an error is returned. </p>
<p> <code>OPTIONS:</code> </p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of possible options and commands.</p>
<dt><code>&#8211;list-options</code></p>
<dd> Simple listing of options</p>
<dt><code>-s, &#8211;session NAME</code></p>
<dd> Apply on session name</p>
<dt><code>-c, &#8211;channel NAME</code></p>
<dd> Apply on channel name</p>
<dt><code>-a, &#8211;all-events</code></p>
<dd> Disable all events. This does NOT disable &quot;*&quot; but rather every known events of the session.</p>
<dt><code>-k, &#8211;kernel</code></p>
<dd> Apply for the kernel tracer</p>
<dt><code>-u, &#8211;userspace</code></p>
<dd> Apply for the user-space tracer</p>
<dt><code>-j, &#8211;jul</code></p>
<dd> Apply for Java application using Java Util Logging interface (JUL)</dl>
</dl>
<p> <code>list</code> [OPTIONS] [SESSION [SESSION OPTIONS]]</p>
<dl>
<dt>
<dd> List tracing session information. </p>
<p> With no arguments, it will list available tracing session(s). </p>
<p> With the session name, it will display the details of the session including the trace file path, the associated channels and their state (activated and deactivated), the activated events and more. </p>
<p> With -k alone, it will list all available kernel events (except the system calls events). With -j alone, the available JUL event from registered application will be list. The event corresponds to the Logger name in the Java JUL application. With -u alone, it will list all available user-space events from registered applications. Here is an example of &#8216;lttng list -u&#8217;: </p>
<pre>
PID: 7448 - Name: /tmp/lttng-ust/tests/hello/.libs/lt-hello
      ust_tests_hello:tptest_sighandler (type: tracepoint)
      ust_tests_hello:tptest (type: tracepoint)
</pre>
<p> You can now enable any event listed by using the name : <code>ust_tests_hello:tptest</code>. </p>
<p> <code>OPTIONS:</code> </p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of possible options and commands.</p>
<dt><code>&#8211;list-options</code></p>
<dd> Simple listing of options</p>
<dt><code>-k, &#8211;kernel</code></p>
<dd> Select kernel domain</p>
<dt><code>-u, &#8211;userspace</code></p>
<dd> Select user-space domain.</p>
<dt><code>-j, &#8211;jul</code></p>
<dd> Apply for Java application using JUL</p>
<dt><code>-f, &#8211;fields</code></p>
<dd> List event fields </p>
</dl>
<p> <code>SESSION OPTIONS:</code> </p>
<dl>
<dt><code>-c, &#8211;channel NAME</code></p>
<dd> List details of a channel</p>
<dt><code>-d, &#8211;domain</code></p>
<dd> List available domain(s)</dl>
</dl>
<p> <code>set-session</code> NAME [OPTIONS]</p>
<dl>
<dt>
<dd> Set current session name </p>
<p> Will change the session name in the .lttngrc file. </p>
<p> <code>OPTIONS:</code> </p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of possible options and commands.</p>
<dt><code>&#8211;list-options</code></p>
<dd> Simple listing of options</dl>
</dl>
<p> <code>snapshot</code> [OPTIONS] ACTION</p>
<dl>
<dt>
<dd> Snapshot command for LTTng session. </p>
<p> <code>OPTIONS:</code> </p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of possible options and commands.</p>
<dt><code>&#8211;list-options</code></p>
<dd> Simple listing of options </p>
</dl>
<p> <code>ACTION:</code> </p>
<dl>
<dt><code>add-output</code> [-m &lt;SIZE&gt;] [-s &lt;NAME&gt;] [-n &lt;NAME&gt;] &lt;URL&gt; | -C &lt;URL&gt; -D &lt;URL&gt;</p>
<dd>
<p> Setup and add an snapshot output for a session. Output are the destination where the snapshot will be sent. Only one output is permitted. To change it, you&#8217;ll need to delete it and add back the new one. </p>
<dt><code>del-output</code> ID | NAME [-s &lt;NAME&gt;]</p>
<dd>
<p> Delete an output for a session using the ID. You can either specify the output&#8217;s ID that can be found with list-output or the name. </p>
<dt><code>list-output</code> [-s &lt;NAME&gt;]</p>
<dd>
<p> List the output of a session. Attributes of the output are printed. </p>
<dt><code>record</code> [-m &lt;SIZE&gt;] [-s &lt;NAME&gt;] [-n &lt;NAME&gt;] [&lt;URL&gt; | -C &lt;URL&gt; -D &lt;URL&gt;]</p>
<dd>
<p> Snapshot a session&#8217;s buffer(s) for all domains. If an URL is specified, it is used instead of a previously added output. Specifying only a name or/and a max size will override the current output values. For instance, you can record a snapshot with a custom maximum size or with a different name. </p>
<pre>
$ lttng snapshot add-output -n mysnapshot file:///data/snapshot
[...]
$ lttng snapshot record -n new_name_snapshot
</pre>
<p> The above will create a snapshot in /data/snapshot/new_name_snapshot* directory rather then in mysnapshot*/ </p>
</dl>
<p> <code>DETAILED ACTION OPTIONS</code> </p>
<dl>
<dt><code>-s, &#8211;session NAME</code></p>
<dd> Apply to session name.</p>
<dt><code>-n, &#8211;name NAME</code></p>
<dd> Name of the snapshot&#8217;s output.</p>
<dt><code>-m, &#8211;max-size SIZE</code></p>
<dd> Maximum size in bytes of the snapshot. The maxium size does not include the metadata file. Human readable format is accepted: {+k,+M,+G}. For instance, &#8211;max-size 5M</p>
<dt><code>-C, &#8211;ctrl-url URL</code></p>
<dd> Set control path URL. (Must use -D also)</p>
<dt><code>-D, &#8211;data-url URL</code></p>
<dd> Set data path URL. (Must use -C also)</dl>
</dl>
<p> <code>start</code> [NAME] [OPTIONS]</p>
<dl>
<dt>
<dd> Start tracing </p>
<p> It will start tracing for all tracers for a specific tracing session. If NAME is omitted, the session name is taken from the .lttngrc file. </p>
<p> <code>OPTIONS:</code> </p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of possible options and commands.</p>
<dt><code>&#8211;list-options</code></p>
<dd> Simple listing of options</dl>
</dl>
<p> <code>stop</code> [NAME] [OPTIONS]</p>
<dl>
<dt>
<dd> Stop tracing </p>
<p> It will stop tracing for all tracers for a specific tracing session. Before returning, the command checks for data availability meaning that it will wait until the trace is readable for the session. Use &#8211;no-wait to avoid this behavior. </p>
<p> If NAME is omitted, the session name is taken from the .lttngrc file. </p>
<p> <code>OPTIONS:</code> </p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of possible options and commands.</p>
<dt><code>&#8211;list-options</code></p>
<dd> Simple listing of options</p>
<dt><code>&#8211;no-wait</code></p>
<dd> Don&#8217;t wait for data availability.</dl>
</dl>
<p> <code>version</code></p>
<dl>
<dt>
<dd> Show version information </p>
<p> <code>OPTIONS:</code> </p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of possible options and commands.</p>
<dt><code>&#8211;list-options</code></p>
<dd> Simple listing of options</dl>
</dl>
<p> <code>view</code> [SESSION_NAME] [OPTIONS]</p>
<dl>
<dt>
<dd> View traces of a tracing session. By default, the babeltrace viewer will be used for text viewing. If SESSION_NAME is omitted, the session name is taken from the .lttngrc file. </p>
<p> <code>OPTIONS:</code> </p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show this help</p>
<dt><code>&#8211;list-options</code></p>
<dd> Simple listing of options</p>
<dt><code>-t, &#8211;trace-path PATH</code></p>
<dd> Trace directory path for the viewer</p>
<dt><code>-e, &#8211;viewer CMD</code></p>
<dd> Specify viewer and/or options to use This will completely override the default viewers so please make sure to specify the full command. The trace directory path of the session will be appended at the end to the arguments</dl>
</dl>
<h2>JUL DOMAIN</h2>
<p> This section explains the JUL domain (-j, &#8211;jul) where JUL stands for Java Util Logging. You can use that feature by using the <code>liblttng-ust-jul.so</code> from the <a href="/docs/linux/man/3-lttng-ust/">lttng-ust</a>(3) project. </p>
<p> The LTTng Java Agent uses JNI to link the UST tracer to the Java application that uses the agent. Thus, it behaves similarly to the UST domain (-u). When enabling events with the JUL domain, you enable a Logger name that will then be mapped to a default UST tracepoint called <code>lttng_jul:jul_event</code> in the <code>lttng_jul_channel</code>. Using the lttng-ctl API, any JUL events must use the tracepoint event type (same as &#8211;tracepoint). </p>
<p> Because of the default immutable channel (<code>lttng_jul_channel</code>), the <code>enable-channel</code> command CAN NOT be used with the JUL domain thus not having any -j option. </p>
<p> For JUL event, loglevels are supported with the JUL ABI values. Use <code>lttng enable-event -h</code> to list them. Wildcards are NOT supported except the &quot;*&quot; meaning all events (same as -a). </p>
<p> Exactly like the UST domain, if the Java application has the same UID as you, you can trace it. Same goes for the tracing group accessing root applications. </p>
<p> Finally, you can list every Logger name that are available from JUL registered applications to the session daemon by using <code>lttng list -j</code>. </p>
<p> Here is an example on how to use this domain. </p>
<pre>
$ lttng list -j
[...]
$ lttng create aSession
$ lttng enable-event -s aSession -j MyCustomLoggerName
$ lttng start
</pre>
<p> More information can be found in the lttng-ust documentation, see java-util-logging.txt </p>
<h2>EXIT VALUES</h2>
<p> On success 0 is returned and a positive value on error. Value of 1 means a command error, 2 an undefined command, 3 a fatal error and 4 a command warning meaning that something went wrong during the command. </p>
<p> Any other value above 10, please refer to <code>&lt;lttng/lttng-error.h&gt;</code> for a detailed list or use lttng_strerror() to get a human readable string of the error code. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> Note that all command line options override environment variables. </p>
<dl>
<dt>LTTNG_SESSIOND_PATH</p>
<dd> Allows one to specify the full session daemon binary path to lttng command line tool. You can also use &#8211;sessiond-path option having the same effect.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-babeltrace/">babeltrace</a>(1),</code> <code><a href="/docs/linux/man/3-lttng-ust/">lttng-ust</a>(3),</code> <code><a href="/docs/linux/man/8-lttng-sessiond/">lttng-sessiond</a>(8),</code> <code><a href="/docs/linux/man/8-lttng-relayd/">lttng-relayd</a>(8),</code> </p>
<h2>BUGS</h2>
<p> If you encounter any issues or usability problem, please report it on our mailing list &lt;lttng-dev [at] lists.lttng.org&gt; to help improve this project or at <a rel="nofollow" href="https://bugs.lttng.org">https://bugs.lttng.org</a> which is a bugtracker. </p>
<h2>CREDITS</h2>
<p> lttng is distributed under the GNU General Public License version 2. See the file COPYING for details. </p>
<p> A Web site is available at <a rel="nofollow" href="http://lttng.org">http://lttng.org</a> for more information on the LTTng project. </p>
<p> You can also find our git tree at <a rel="nofollow" href="http://git.lttng.org.">http://git.lttng.org.</a> </p>
<p> Mailing lists for support and development: &lt;lttng-dev [at] lists.lttng.org&gt;. </p>
<p> You can find us on IRC server irc.oftc.net (OFTC) in #lttng. </p>
<h2>THANKS</h2>
<p> Thanks to Yannick Brosseau without whom this project would never have been so lean and mean! Also thanks to the Ericsson teams working on tracing which helped us greatly with detailed bug reports and unusual test cases. </p>
<p> Thanks to our beloved packager Alexandre Montplaisir-Goncalves (Ubuntu and PPA maintainer) and Jon Bernard for our Debian packages. </p>
<p> Special thanks to Michel Dagenais and the DORSAL laboratory at Polytechnique de Montreal for the LTTng journey. </p>
<h2>AUTHORS</h2>
<p> lttng-tools was originally written by Mathieu Desnoyers, Julien Desfossez and David Goulet. More people have since contributed to it. It is currently maintained by David Goulet &lt;dgoulet [at] efficios.com&gt;. </p>
<h2>Index</h2>
