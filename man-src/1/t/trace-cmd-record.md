---
title: "trace-cmd-record(1)"
name: "trace-cmd-record"
section: "1"
letter: "t"
url: "/docs/linux/man/1-trace-cmd-record/"
description: "trace-cmd-record – record a trace from the Ftrace Linux internal tracer"
---

<h2 class="name">NAME</h2>
<p> trace-cmd-record &#8211; record a trace from the Ftrace Linux internal tracer </p>
<h2>SYNOPSIS</h2>
<p> <code>trace-cmd record</code> [<i>OPTIONS</i>] [<i>command</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1) record command will set up the Ftrace Linux kernel tracer to record the specified plugins or events that happen while the <i>command</i> executes. If no command is given, then it will record until the user hits Ctrl-C. </p>
<p> The record command of trace-cmd will set up the Ftrace tracer to start tracing the various events or plugins that are given on the command line. It will then create a number of tracing processes (one per CPU) that will start recording from the kernel ring buffer straight into temporary files. When the command is complete (or Ctrl-C is hit) all the files will be combined into a trace.dat file that can later be read (see <a href="/docs/linux/man/1-trace-cmd-report/">trace-cmd-report</a>(1)).</p>
<h2>OPTIONS</h2>
<p> <code>-p</code> <i>plugin</i></p>
<dl>
<dt>
<dd> Specify a trace plugin. Plugins are special Ftrace tracers that usually do more than just trace an event. Common plugins are <code>function</code>, <code>function_graph</code>, <code>preemptirqsoff</code>, <code>irqsoff</code>, <code>preemptoff</code>, and <code>wakeup</code>. A plugin must be supported by the running kernel. To see a list of available plugins, see <a href="/docs/linux/man/1-trace-cmd-list/">trace-cmd-list</a>(1).</dl>
<p> <code>-e</code> <i>event</i></p>
<dl>
<dt>
<dd> Specify an event to trace. Various static trace points have been added to the Linux kernel. They are grouped by subsystem where you can enable all events of a given subsystem or specify specific events to be enabled. The <i>event</i> is of the format &quot;subsystem:event-name&quot;. You can also just specify the subsystem without the <i>:event-name</i> or the event-name without the &quot;subsystem:&quot;. Using &quot;-e sched_switch&quot; will enable the &quot;sched_switch&quot; event where as, &quot;-e sched&quot; will enable all events under the &quot;sched&quot; subsystem. </p>
<dl>
<dt>
<dd>
<pre>
The 'event' can also contain glob expressions. That is, &quot;*stat*&quot; will
select all events (or subsystems) that have the characters &quot;stat&quot; in their
names.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
The keyword 'all' can be used to enable all events.
</pre>
</dl>
</dl>
<p> <code>-a</code></p>
<dl>
<dt>
<dd> Every event that is being recorded has its output format file saved in the output file to be able to display it later. But if other events are enabled in the trace without trace-cmd&#8217;s knowledge, the formats of those events will not be recorded and trace-cmd report will not be able to display them. If this is the case, then specify the <code>-a</code> option and the format for all events in the system will be saved.</dl>
<p> <code>-T</code></p>
<dl>
<dt>
<dd> Enable a stacktrace on each event. For example: </p>
<dl>
<dt>
<dd>
<pre><code>
          &lt;idle&gt;-0     [003] 58549.289091: sched_switch:         kworker/0:1:0 [120] R ==&gt; trace-cmd:2603 [120]
          &lt;idle&gt;-0     [003] 58549.289092: kernel_stack:         &lt;stack trace&gt;
=&gt; schedule (ffffffff814b260e)
=&gt; cpu_idle (ffffffff8100a38c)
=&gt; start_secondary (ffffffff814ab828)
</code></pre>
</dl>
</dl>
<p> <code>&#8211;func-stack</code></p>
<dl>
<dt>
<dd> Enable a stack trace on all functions. Note this is only applicable for the &quot;function&quot; plugin tracer, and will only take effect if the -l option is used and succeeds in limiting functions. If the function tracer is not filtered, and the stack trace is enabled, you can live lock the machine.</dl>
<p> <code>-f</code> <i>filter</i></p>
<dl>
<dt>
<dd> Specify a filter for the previous event. This must come after a <code>-e</code>. This will filter what events get recorded based on the content of the event. Filtering is passed to the kernel directly so what filtering is allowed may depend on what version of the kernel you have. Basically, it will let you use C notation to check if an event should be processed or not.</dl>
<dl>
<dt>
<dd>
==, &gt;=, &lt;=, &gt;, &lt;, &amp;, |, &amp;&amp;and ||
</dl>
<dl>
<dt>
<dd>
<pre>
The above are usually safe to use to compare fields.
</pre>
</dl>
<p> <code>-R</code> <i>trigger</i></p>
<dl>
<dt>
<dd> Specify a trigger for the previous event. This must come after a <code>-e</code>. This will add a given trigger to the given event. To only enable the trigger and not the event itself, then place the event after the <code>-v</code> option. </p>
<dl>
<dt>
<dd>
<pre>
See Documentation/trace/events.txt in the Linux kernel source for more
information on triggers.
</pre>
</dl>
</dl>
<p> <code>-v</code></p>
<dl>
<dt>
<dd> This will cause all events specified after it on the command line to not be traced. This is useful for selecting a subsystem to be traced but to leave out various events. For Example: &quot;-e sched -v -e &quot;*stat\*&quot;&quot; will enable all events in the sched subsystem except those that have &quot;stat&quot; in their names. </p>
<dl>
<dt>
<dd>
<pre>
Note: the *-v* option was taken from the way <a href="//www.systutorials.com/docs/linux/man/1-grep/">grep</a>(1) inverts the following
matches.
</pre>
</dl>
</dl>
<p> <code>-F</code></p>
<dl>
<dt>
<dd> This will filter only the executable that is given on the command line. If no command is given, then it will filter itself (pretty pointless). Using <code>-F</code> will let you trace only events that are caused by the given command.</dl>
<p> <code>-P</code> <i>pid</i></p>
<dl>
<dt>
<dd> Similar to <code>-F</code> but lets you specify a process ID to trace.</dl>
<p> <code>-c</code></p>
<dl>
<dt>
<dd> Used with either <code>-F</code> to trace the process&#8217; children too.</dl>
<p> <code>-C</code> <i>clock</i></p>
<dl>
<dt>
<dd> Set the trace clock to &quot;clock&quot;. </p>
<dl>
<dt>
<dd>
<pre>
Use <a href="//www.systutorials.com/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1) list -C to see what clocks are available.
</pre>
</dl>
</dl>
<p> <code>-o</code> <i>output-file</i></p>
<dl>
<dt>
<dd> By default, trace-cmd report will create a <i>trace.dat</i> file. You can specify a different file to write to with the <code>-o</code> option.</dl>
<p> <code>-l</code> <i>function-name</i></p>
<dl>
<dt>
<dd> This will limit the <i>function</i> and <i>function_graph</i> tracers to only trace the given function name. More than one <code>-l</code> may be specified on the command line to trace more than one function. The limited use of glob expressions are also allowed. These are <i>match*</i> to only filter functions that start with <i>match</i>. <i>*match</i> to only filter functions that end with <i>match</i>. <i>*match\*</i> to only filter on functions that contain <i>match</i>.</dl>
<p> <code>-g</code> <i>function-name</i></p>
<dl>
<dt>
<dd> This option is for the function_graph plugin. It will graph the given function. That is, it will only trace the function and all functions that it calls. You can have more than one <code>-g</code> on the command line.</dl>
<p> <code>-n</code> <i>function-name</i></p>
<dl>
<dt>
<dd> This has the opposite effect of <code>-l</code>. The function given with the <code>-n</code> option will not be traced. This takes precedence, that is, if you include the same function for both <code>-n</code> and <code>-l</code>, it will not be traced.</dl>
<p> <code>-d</code></p>
<dl>
<dt>
<dd> Some tracer plugins enable the function tracer by default. Like the latency tracers. This option prevents the function tracer from being enabled at start up.</dl>
<p> <code>-D</code></p>
<dl>
<dt>
<dd> The option <code>-d</code> will try to use the function-trace option to disable the function tracer (if available), otherwise it defaults to the proc file: /proc/sys/kernel/ftrace_enabled, but will not touch it if the function-trace option is available. The <code>-D</code> option will disable both the ftrace_enabled proc file as well as the function-trace option if it exists. </p>
<dl>
<dt>
<dd>
<pre>
Note, this disable function tracing for all users, which includes users
outside of ftrace tracers (stack_tracer, perf, etc).
</pre>
</dl>
</dl>
<p> <code>-O</code> <i>option</i></p>
<dl>
<dt>
<dd> Ftrace has various options that can be enabled or disabled. This allows you to set them. Appending the text <i>no</i> to an option disables it. For example: &quot;-O nograph-time&quot; will disable the &quot;graph-time&quot; Ftrace option.</dl>
<p> <code>-s</code> <i>interval</i></p>
<dl>
<dt>
<dd> The processes that trace-cmd creates to record from the ring buffer need to wake up to do the recording. Setting the <i>interval</i> to zero will cause the processes to wakeup every time new data is written into the buffer. But since Ftrace is recording kernel activity, the act of this processes going back to sleep may cause new events into the ring buffer which will wake the process back up. This will needlessly add extra data into the ring buffer. </p>
<dl>
<dt>
<dd>
<pre>
The 'interval' metric is microseconds. The default is set to 1000 (1 ms).
This is the time each recording process will sleep before waking up to
record any new data that was written to the ring buffer.
</pre>
</dl>
</dl>
<p> <code>-r</code> <i>priority</i></p>
<dl>
<dt>
<dd> The priority to run the capture threads at. In a busy system the trace capturing threads may be staved and events can be lost. This increases the priority of those threads to the real time (FIFO) priority. But use this option with care, it can also change the behaviour of the system being traced.</dl>
<p> <code>-b</code> <i>size</i></p>
<dl>
<dt>
<dd> This sets the ring buffer size to <i>size</i> kilobytes. Because the Ftrace ring buffer is per CPU, this size is the size of each per CPU ring buffer inside the kernel. Using &quot;-b 10000&quot; on a machine with 4 CPUs will make Ftrace have a total buffer size of 40 Megs.</dl>
<p> <code>-B</code> <i>buffer-name</i></p>
<dl>
<dt>
<dd> If the kernel supports multiple buffers, this will add a buffer with the given name. If the buffer name already exists, that buffer is just reset and will not be deleted at the end of record execution. If the buffer is created, it will be removed at the end of execution (unless the <code>-k</code> is set, or <i>start</i> command was used). </p>
<dl>
<dt>
<dd>
<pre>
After a buffer name is stated, all events added after that will be
associated with that buffer. If no buffer is specified, or an event
is specified before a buffer name, it will be associated with the
main (toplevel) buffer.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
trace-cmd record -e sched -B block -e block -B time -e timer sleep 1
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
The above is will enable all sched events in the main buffer. It will
then create a 'block' buffer instance and enable all block events within
that buffer. A 'time' buffer instance is created and all timer events
will be enabled for that event.
</pre>
</dl>
</dl>
<p> <code>-m</code> <i>size</i></p>
<dl>
<dt>
<dd> The max size in kilobytes that a per cpu buffer should be. Note, due to rounding to page size, the number may not be totally correct. Also, this is performed by switching between two buffers that are half the given size thus the output may not be of the given size even if much more was written. </p>
<dl>
<dt>
<dd>
<pre>
Use this to prevent running out of diskspace for long runs.
</pre>
</dl>
</dl>
<p> <code>-M</code> <i>cpumask</i></p>
<dl>
<dt>
<dd> Set the cpumask for to trace. It only affects the last buffer instance given. If supplied before any buffer instance, then it affects the main buffer. The value supplied must be a hex number. </p>
<dl>
<dt>
<dd>
<pre>
trace-cmd record -p function -M c -B events13 -e all -M 5
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
If the -M is left out, then the mask stays the same. To enable all
CPUs, pass in a value of '-1'.
</pre>
</dl>
</dl>
<p> <code>-k</code></p>
<dl>
<dt>
<dd> By default, when trace-cmd is finished tracing, it will reset the buffers and disable all the tracing that it enabled. This option keeps trace-cmd from disabling the tracer and reseting the buffer. This option is useful for debugging trace-cmd. </p>
<dl>
<dt>
<dd>
<pre>
Note: usually trace-cmd will set the &quot;tracing_on&quot; file back to what it
was before it was called. This option will leave that file set to zero.
</pre>
</dl>
</dl>
<p> <code>-i</code></p>
<dl>
<dt>
<dd> By default, if an event is listed that trace-cmd does not find, it will exit with an error. This option will just ignore events that are listed on the command line but are not found on the system.</dl>
<p> <code>-N</code> <i>host:port</i></p>
<dl>
<dt>
<dd> If another machine is running &quot;trace-cmd listen&quot;, this option is used to have the data sent to that machine with UDP packets. Instead of writing to an output file, the data is sent off to a remote box. This is ideal for embedded machines with little storage, or having a single machine that will keep all the data in a single repository. </p>
<dl>
<dt>
<dd>
<pre>
Note: This option is not supported with latency tracer plugins:
  wakeup, wakeup_rt, irqsoff, preemptoff and preemptirqsoff
</pre>
</dl>
</dl>
<p> <code>-t</code></p>
<dl>
<dt>
<dd> This option is used with <code>-N</code>, when there&#8217;s a need to send the live data with TCP packets instead of UDP. Although TCP is not nearly as fast as sending the UDP packets, but it may be needed if the network is not that reliable, the amount of data is not that intensive, and a guarantee is needed that all traced information is transfered successfully.</dl>
<p> <code>&#8211;date</code></p>
<dl>
<dt>
<dd> With the <code>&#8211;date</code> option, &quot;trace-cmd&quot; will write timestamps into the trace buffer after it has finished recording. It will then map the timestamp to gettimeofday which will allow wall time output from the timestamps reading the created <i>trace.dat</i> file.</dl>
<p> <code>&#8211;profile</code></p>
<dl>
<dt>
<dd> With the <code>&#8211;profile</code> option, &quot;trace-cmd&quot; will enable tracing that can be used with <a href="/docs/linux/man/1-trace-cmd-report/">trace-cmd-report</a>(1) &#8211;profile option. If a tracer <code>-p</code> is not set, and function graph depth is supported by the kernel, then the function_graph tracer will be enabled with a depth of one (only show where userspace enters into the kernel). It will also enable various tracepoints with stack tracing such that the report can show where tasks have been blocked for the longest time. </p>
<dl>
<dt>
<dd>
<pre>
See <a href="//www.systutorials.com/docs/linux/man/1-trace-cmd-profile/">trace-cmd-profile</a>(1) for more details and examples.
</pre>
</dl>
</dl>
<p> <code>-H</code> <i>event-hooks</i></p>
<dl>
<dt>
<dd> Add custom event matching to connect any two events together. When not used with <code>&#8211;profile</code>, it will save the parameter and this will be used by trace-cmd report &#8211;profile, too. That is: </p>
<dl>
<dt>
<dd>
<pre>
trace-cmd record -H hrtimer_expire_entry,hrtimer/hrtimer_expire_exit,hrtimer,sp
trace-cmd report --profile
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
Will profile hrtimer_expire_entry and hrtimer_expire_ext times.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
See <a href="//www.systutorials.com/docs/linux/man/1-trace-cmd-profile/">trace-cmd-profile</a>(1) for format.
</pre>
</dl>
</dl>
<p> <code>&#8211;stderr</code></p>
<dl>
<dt>
<dd> Have output go to stderr instead of stdout, but the output of the command executed will not be changed. This is useful if you want to monitor the output of the command being executed, but not see the output from trace-cmd.</dl>
<h2>EXAMPLES</h2>
<p> The basic way to trace all events: </p>
<dl>
<dt>
<dd>
#trace &#8211; cmd record &#8211; e all ls&gt; / dev / null<br />
#trace &#8211; cmd report<br />
trace &#8211; cmd &#8211; 13541 [003] 106260.693809 : filemap_fault : address = 0x128122 offset = 0xce trace &#8211; cmd &#8211; 13543 [001] 106260.693809 : kmalloc : call_site = 81128dd4 ptr = 0xffff88003dd83800 bytes_req = 768 bytes_alloc = 1024 gfp_flags = GFP_KERNEL | GFP_ZERO<br />
                                                                                                                                                                                                                                                                 ls &#8211;<br />
                                                                                                                                                                                                                                                             13545 [002] 106260.693809 : kfree : call_site = 810a7abb ptr = 0x0 ls &#8211; 13545 [002] 106260.693818 : sys_exit_write : 0x1
</dl>
<p> To use the function tracer with sched switch tracing: </p>
<dl>
<dt>
<dd>
#trace &#8211; cmd record &#8211; p function &#8211; e sched_switch ls&gt; / dev / null<br />
#trace &#8211; cmd report<br />
ls &#8211; 13587 [002] 106467.860310 : function : hrtick_start_fair&lt;&#8211;pick_next_task_fair<br />
                                                                      ls &#8211;<br />
                                                                  13587 [002] 106467.860313 : sched_switch : prev_comm = trace &#8211; cmd prev_pid = 13587 prev_prio = 120 prev_state = R ==&gt;<br />
                                                next_comm = trace &#8211; cmd next_pid = 13583 next_prio = 120 trace &#8211; cmd &#8211; 13585 [001] 106467.860314 : function : native_set_pte_at &lt; &#8211;__do_fault<br />
                                                                                                                                                                                          trace &#8211;<br />
                                                                                                                                                                                      cmd &#8211; 13586 [003] 106467.860314 : function : up_read &lt;<br />
                                                                                                     &#8211;do_page_fault<br />
                                                                                                             ls &#8211;<br />
                                                                                                         13587 [002] 106467.860317 : function : __phys_addr &lt;<br />
                                                                                                     &#8211;schedule<br />
                                                                                                             trace &#8211;<br />
                                                                                                         cmd &#8211; 13585 [001] 106467.860318 : function : _raw_spin_unlock &lt;<br />
                                                                                                     &#8211;__do_fault<br />
                                                                                                             ls &#8211;<br />
                                                                                                         13587 [002] 106467.860320 : function : native_load_sp0 &lt;<br />
                                                                                                     &#8211;__switch_to<br />
                                                                                                             trace &#8211;<br />
                                                                                                         cmd &#8211; 13586 [003] 106467.860322 : function : down_read_trylock &lt;<br />
                                                                                                     &#8211;do_page_fault
</dl>
<p> Here is a nice way to find what interrupts have the highest latency: </p>
<dl>
<dt>
<dd>
<pre><code>
#trace - cmd record - p function_graph - e irq_handler_entry - l do_IRQ sleep 10
#trace - cmd report
&lt;idle&gt; - 0 [000] 157412.933969 : funcgraph_entry : | do_IRQ(){
    &lt;idle&gt; - 0 [000] 157412.933974 : irq_handler_entry : irq = 48 name = eth0&lt;idle&gt; - 0 [000] 157412.934004 : funcgraph_exit : +36.358 us |
}&lt;idle&gt; - 0 [000] 157413.895004 : funcgraph_entry : |
                                                    do_IRQ(){
                                                        &lt;idle&gt; - 0 [000] 157413.895011 : irq_handler_entry : irq = 48 name = eth0&lt;idle&gt; - 0 [000] 157413.895026 : funcgraph_exit : +24.014 us |
                                                    }&lt;idle&gt; -
                                                        0 [000] 157415.891762 : funcgraph_entry : |
                                                                                                  do_IRQ(){
                                                                                                      &lt;idle&gt; - 0 [000] 157415.891769 : irq_handler_entry : irq = 48 name = eth0&lt;idle&gt; - 0 [000] 157415.891784 : funcgraph_exit : +22.928 us |
                                                                                                  }&lt;idle&gt; -
                                                                                                      0 [000] 157415.934869 : funcgraph_entry : |
                                                                                                                                                do_IRQ(){
                                                                                                                                                    &lt;idle&gt; - 0 [000] 157415.934874 : irq_handler_entry : irq = 48 name = eth0&lt;idle&gt; - 0 [000] 157415.934906 : funcgraph_exit : +37.512 us |
                                                                                                                                                }&lt;idle&gt; -
                                                                                                                                                    0 [000] 157417.888373 : funcgraph_entry : |
                                                                                                                                                                                              do_IRQ()
{
    &lt;idle&gt; - 0 [000] 157417.888381 : irq_handler_entry : irq = 48 name = eth0&lt;idle&gt; - 0 [000] 157417.888398 : funcgraph_exit : +25.943 us |
}
</code></pre>
</dl>
<p> An example of the profile: </p>
<dl>
<dt>
<dd>
<pre>
 # trace-cmd record --profile sleep 1
 # trace-cmd report --profile --comm sleep
task: sleep-21611
  Event: sched_switch:R (1) Total: 99442 Avg: 99442 Max: 99442 Min:99442
     &lt;stack&gt; 1 total:99442 min:99442 max:99442 avg=99442
       =&gt; ftrace_raw_event_sched_switch (0xffffffff8105f812)
       =&gt; __schedule (0xffffffff8150810a)
       =&gt; preempt_schedule (0xffffffff8150842e)
       =&gt; ___preempt_schedule (0xffffffff81273354)
       =&gt; cpu_stop_queue_work (0xffffffff810b03c5)
       =&gt; stop_one_cpu (0xffffffff810b063b)
       =&gt; sched_exec (0xffffffff8106136d)
       =&gt; do_execve_common.isra.27 (0xffffffff81148c89)
       =&gt; do_execve (0xffffffff811490b0)
       =&gt; SyS_execve (0xffffffff811492c4)
       =&gt; return_to_handler (0xffffffff8150e3c8)
       =&gt; stub_execve (0xffffffff8150c699)
  Event: sched_switch:S (1) Total: 1000506680 Avg: 1000506680 Max: 1000506680 Min:1000506680
     &lt;stack&gt; 1 total:1000506680 min:1000506680 max:1000506680 avg=1000506680
       =&gt; ftrace_raw_event_sched_switch (0xffffffff8105f812)
       =&gt; __schedule (0xffffffff8150810a)
       =&gt; schedule (0xffffffff815084b8)
       =&gt; do_nanosleep (0xffffffff8150b22c)
       =&gt; hrtimer_nanosleep (0xffffffff8108d647)
       =&gt; SyS_nanosleep (0xffffffff8108d72c)
       =&gt; return_to_handler (0xffffffff8150e3c8)
       =&gt; tracesys_phase2 (0xffffffff8150c304)
  Event: sched_wakeup:21611 (1) Total: 30326 Avg: 30326 Max: 30326 Min:30326
     &lt;stack&gt; 1 total:30326 min:30326 max:30326 avg=30326
       =&gt; ftrace_raw_event_sched_wakeup_template (0xffffffff8105f653)
       =&gt; ttwu_do_wakeup (0xffffffff810606eb)
       =&gt; ttwu_do_activate.constprop.124 (0xffffffff810607c8)
       =&gt; try_to_wake_up (0xffffffff8106340a)
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1), <a href="/docs/linux/man/1-trace-cmd-report/">trace-cmd-report</a>(1), <a href="/docs/linux/man/1-trace-cmd-start/">trace-cmd-start</a>(1), <a href="/docs/linux/man/1-trace-cmd-stop/">trace-cmd-stop</a>(1), <a href="/docs/linux/man/1-trace-cmd-extract/">trace-cmd-extract</a>(1), <a href="/docs/linux/man/1-trace-cmd-reset/">trace-cmd-reset</a>(1), <a href="/docs/linux/man/1-trace-cmd-split/">trace-cmd-split</a>(1), <a href="/docs/linux/man/1-trace-cmd-list/">trace-cmd-list</a>(1), <a href="/docs/linux/man/1-trace-cmd-listen/">trace-cmd-listen</a>(1), <a href="/docs/linux/man/1-trace-cmd-profile/">trace-cmd-profile</a>(1)</p>
<h2>AUTHOR</h2>
<p> Written by Steven Rostedt, &lt;m[blue]<code>rostedt [at] goodmis.org</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>RESOURCES</h2>
<p> <a href="git://git.kernel.org/pub/scm/linux/kernel/git/rostedt/trace-cmd.git">git://git.kernel.org/pub/scm/linux/kernel/git/rostedt/trace-cmd.git</a></p>
<h2>COPYING</h2>
<p> Copyright (C) 2010 Red Hat, Inc. Free use of this software is granted under the terms of the GNU Public License (GPL).</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> rostedt [at] goodmis.org</p>
<dl>
<dt>
<dd> mailto:rostedt [at] goodmis.org</dl>
</dl>
<h2>Index</h2>
