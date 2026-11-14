---
title: "trace-cmd-report(1)"
name: "trace-cmd-report"
section: "1"
letter: "t"
url: "/docs/linux/man/1-trace-cmd-report/"
description: "trace-cmd-report – show in ASCII a trace created by trace-cmd record"
---

<h2 class="name">NAME</h2>
<p> trace-cmd-report &#8211; show in ASCII a trace created by trace-cmd record </p>
<h2>SYNOPSIS</h2>
<p> <code>trace-cmd report</code> [<i>OPTIONS</i>] [<i>input-file</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1) report command will output a human readable report of a trace created by trace-cmd record.</p>
<h2>OPTIONS</h2>
<p> <code>-i</code> <i>input-file</i></p>
<dl>
<dt>
<dd> By default, trace-cmd report will read the file <i>trace.dat</i>. But the <code>-i</code> option open up the given <i>input-file</i> instead. Note, the input file may also be specified as the last item on the command line.</dl>
<p> <code>-e</code></p>
<dl>
<dt>
<dd> This outputs the endianess of the file. trace-cmd report is smart enough to be able to read big endian files on little endian machines, and vise versa.</dl>
<p> <code>-f</code></p>
<dl>
<dt>
<dd> This outputs the list of functions that have been recorded in the file.</dl>
<p> <code>-P</code></p>
<dl>
<dt>
<dd> This outputs the list of &quot;trace_printk()&quot; data. The raw trace data points to static pointers in the kernel. This must be stored in the trace.dat file.</dl>
<p> <code>-E</code></p>
<dl>
<dt>
<dd> This lists the possible events in the file (but this list is not necessarily the list of events in the file).</dl>
<p> <code>&#8211;events</code></p>
<dl>
<dt>
<dd> This will list the event formats that are stored in the trace.dat file.</dl>
<p> <code>&#8211;event</code> regex</p>
<dl>
<dt>
<dd> This will print events that match the given regex. If a colon is specified, then the characters before the colon will be used to match the system and the characters after the colon will match the event. </p>
<dl>
<dt>
<dd>
<pre>
trace-cmd report --event sys:read
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
The above will only match events where the system name contains &quot;sys&quot;
and the event name contains &quot;read&quot;.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
trace-cmd report --event read
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
The above will match all events that contain &quot;read&quot; in its name. Also it
may list all events of a system that contains &quot;read&quot; as well.
</pre>
</dl>
</dl>
<p> <code>&#8211;check-events</code></p>
<dl>
<dt>
<dd> This will parse the event format strings that are stored in the trace.dat file and return whether the formats can be parsed correctly. It will load plugins unless <code>-N</code> is specified.</dl>
<p> <code>-t</code></p>
<dl>
<dt>
<dd> Print the full timestamp. The timestamps in the data file are usually recorded to the nanosecond. But the default display of the timestamp is only to the microsecond. To see the full timestamp, add the <code>-t</code> option.</dl>
<p> <code>-F</code> <i>filter</i></p>
<dl>
<dt>
<dd> Add a filter to limit what events are displayed. The format of the filter is:</dl>
<dl>
<dt>
<dd>
<pre><code>
    &lt;events&gt; ':' &lt;filter&gt;
    &lt;events&gt; = SYSTEM'/'EVENT  | SYSTEM | EVENT | &lt;events&gt; ',' &lt;events&gt;
    &lt;filter&gt; = EVENT_FIELD &lt;op&gt; &lt;value&gt; | &lt;filter&gt; '&amp;&amp;' &lt;filter&gt; |
               &lt;filter&gt; '||' &lt;filter&gt; | '(' &lt;filter&gt; ')' | '!' &lt;filter&gt;
    &lt;op&gt; = '==' | '!=' | '&gt;=' | '&lt;=' | '&gt;' | '&lt;' | '&amp;' | '|' | '^' |
           '+' | '-' | '*' | '/' | '%'
    &lt;value&gt; = NUM | STRING | EVENT_FIELD
</code></pre>
</dl>
<dl>
<dt>
<dd>
<pre>
SYSTEM is the name of the system to filter on. If the EVENT is left out,
then it applies to all events under the SYSTEM. If only one string is used
without the '/' to deliminate between SYSTEM and EVENT, then the filter
will be applied to all systems and events that match the given string.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
Whitespace is ignored, such that &quot;sched:next_pid==123&quot; is equivalent to
&quot;sched : next_pid == 123&quot;.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
STRING is defined with single or double quotes (single quote must end with
single quote, and double with double). Whitespace within quotes are not
ignored.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
The representation of a SYSTEM or EVENT may also be a regular expression
as defined by '<a href="//www.systutorials.com/docs/linux/man/3-regcomp/">regcomp</a>(3)'.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
The EVENT_FIELD is the name of the field of an event that is being
filtered. If the event does not contain the EVENT_FIELD, that part of the
equation will be considered false.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
    -F 'sched : bogus == 1 || common_pid == 2'
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
The &quot;bogus == 1&quot; will always evaluate to FALSE because no event has a
field called &quot;bogus&quot;, but the &quot;common_pid == 2&quot; will still be evaluated
since all events have the field &quot;common_pid&quot;. Any &quot;sched&quot; event that was
traced by the process with the PID of 2 will be shown.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
Note, the EVENT_FIELD is the field name as shown by an events format
(as displayed with *--events*), and not what is found in the output.
If the output shows &quot;ID:foo&quot; but the field that &quot;foo&quot; belongs to was
called &quot;name&quot; in the event format, then &quot;name&quot; must be used in the filter.
The same is true about values. If the value that is displayed is converted
by to a string symbol, the filter checks the original value and not the
value displayed. For example, to filter on all tasks that were in the
running state at a context switch:
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
    -F 'sched/sched_switch : prev_state==0'
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
Although the output displays 'R', having 'prev_stat==&quot;R&quot;' will not work.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
Note: You can also specify 'COMM' as an EVENT_FIELD. This will use the
task name (or comm) of the record to compare. For example, to filter out
all of the &quot;trace-cmd&quot; tasks:
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
    -F '.*:COMM != &quot;trace-cmd&quot;'
</pre>
</dl>
<p> <code>-v</code></p>
<dl>
<dt>
<dd> This causes the following filters of <code>-F</code> to filter out the matching events.</dl>
<dl>
<dt>
<dd>
<pre>
    -v -F 'sched/sched_switch : prev_state == 0'
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
Will not display any sched_switch events that have a prev_state of 0.
Removing the *-v* will only print out those events.
</pre>
</dl>
<p> <code>-T</code></p>
<dl>
<dt>
<dd> Test the filters of -F. After processing a filter string, the resulting filter will be displayed for each event. This is useful for using a filter for more than one event where a field may not exist in all events. Also it can be used to make sure there are no misspelled event field names, as they will simply be ignored. <code>-T</code> is ignored if <code>-F</code> is not specified.</dl>
<p> <code>-V</code></p>
<dl>
<dt>
<dd> Show the plugins that are loaded.</dl>
<p> <code>-L</code></p>
<dl>
<dt>
<dd> This will not load system wide plugins. It loads &quot;local only&quot;. That is what it finds in the ~/.trace-cmd/plugins directory.</dl>
<p> <code>-N</code></p>
<dl>
<dt>
<dd> This will not load any plugins.</dl>
<p> <code>-n</code> <i>event-re</i></p>
<dl>
<dt>
<dd> This will cause all events that match the option to ignore any registered handler (by the plugins) to print the event. The normal event will be printed instead. The <i>event-re</i> is a regular expression as defined by <i><a href="/docs/linux/man/3-regcomp/">regcomp</a>(3)</i>.</dl>
<p> <code>&#8211;profile</code></p>
<dl>
<dt>
<dd> With the <code>&#8211;profile</code> option, &quot;trace-cmd report&quot; will process all the events first, and then output a format showing where tasks have spent their time in the kernel, as well as where they are blocked the most, and where wake up latencies are. </p>
<dl>
<dt>
<dd>
<pre>
See <a href="//www.systutorials.com/docs/linux/man/1-trace-cmd-profile/">trace-cmd-profile</a>(1) for more details and examples.
</pre>
</dl>
</dl>
<p> <code>-G</code></p>
<dl>
<dt>
<dd> Set interrupt (soft and hard) events as global (associated to CPU instead of tasks). Only works for &#8211;profile.</dl>
<p> <code>-H</code> <i>event-hooks</i></p>
<dl>
<dt>
<dd> Add custom event matching to connect any two events together. </p>
<dl>
<dt>
<dd>
<pre>
See <a href="//www.systutorials.com/docs/linux/man/1-trace-cmd-profile/">trace-cmd-profile</a>(1) for format.
</pre>
</dl>
</dl>
<p> <code>-R</code></p>
<dl>
<dt>
<dd> This will show the events in &quot;raw&quot; format. That is, it will ignore the event&#8217;s print formatting and just print the contents of each field.</dl>
<p> <code>-r</code> <i>event-re</i></p>
<dl>
<dt>
<dd> This will cause all events that match the option to print its raw fields. The <i>event-re</i> is a regular expression as defined by <i><a href="/docs/linux/man/3-regcomp/">regcomp</a>(3)</i>.</dl>
<p> <code>-l</code></p>
<dl>
<dt>
<dd> This adds a &quot;latency output&quot; format. Information about interrupts being disabled, soft irq being disabled, the &quot;need_resched&quot; flag being set, preempt count, and big kernel lock are all being recorded with every event. But the default display does not show this information. This option will set display this information with 6 characters. When one of the fields is zero or N/A a &#8216;.\&#8217; is shown.</dl>
<dl>
<dt>
<dd>
<pre>
      &lt;idle&gt;-0       0d.h1. 106467.859747: function:             ktime_get &lt;-- tick_check_idle
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
The 0d.h1. denotes this information. The first character is never a '.'
and represents what CPU the trace was recorded on (CPU 0). The 'd' denotes
that interrupts were disabled. The 'h' means that this was called inside
an interrupt handler. The '1' is the preemption disabled (preempt_count)
was set to one.  The two '.'s are &quot;need_resched&quot; flag and kernel lock
counter.  If the &quot;need_resched&quot; flag is set, then that character would be a
'N'.
</pre>
</dl>
<p> <code>-w</code></p>
<dl>
<dt>
<dd> If both the <i>sched_switch</i> and <i>sched_wakeup</i> events are enabled, then this option will report the latency between the time the task was first woken, and the time it was scheduled in.</dl>
<p> <code>-q</code></p>
<dl>
<dt>
<dd> Quiet non critical warnings.</dl>
<p> <code>-O</code></p>
<dl>
<dt>
<dd> Pass options to the trace-cmd plugins that are loaded. </p>
<dl>
<dt>
<dd>
<pre>
-O plugin:var=value
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
The 'plugin:' and '=value' are optional. Value may be left off for options
that are boolean. If the 'plugin:' is left off, then any variable that matches
in all plugins will be set.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
Example:  -O fgraph:tailprint
</pre>
</dl>
</dl>
<p> <code>&#8211;stat</code></p>
<dl>
<dt>
<dd> If the trace.dat file recorded the final stats (outputed at the end of record) the <code>&#8211;stat</code> option can be used to retrieve them.</dl>
<p> <code>&#8211;uname</code></p>
<dl>
<dt>
<dd> If the trace.dat file recorded uname during the run, this will retrieve that information.</dl>
<h2>EXAMPLES</h2>
<p> Using a trace.dat file that was created with: </p>
<dl>
<dt>
<dd>
<pre>
    # trace-cmd record -p function -e all sleep 5
</pre>
</dl>
<p> The default report shows: </p>
<dl>
<dt>
<dd>
#trace &#8211; cmd report<br />
trace &#8211; cmd &#8211; 16129 [002] 158126.498411 : function : __mutex_unlock_slowpath &lt; &#8211;mutex_unlock<br />
                                                                                       trace &#8211;<br />
                                                                                   cmd &#8211; 16131 [000] 158126.498411 : kmem_cache_alloc : call_site = 811223c5 ptr = 0xffff88003ecf2b40 bytes_req = 272 bytes_alloc = 320 gfp_flags = GFP_KERNEL | GFP_ZERO<br />
                                                                                                                                                                                                                                                                 trace &#8211;<br />
                                                                                                                                                                                                                                                             cmd &#8211; 16130 [003] 158126.498411 : function : do_splice_to &lt;<br />
                                                                                                                                                                                                                                                         &#8211;sys_splice<br />
                                                                                                                                                                                                                                                                 sleep &#8211;<br />
                                                                                                                                                                                                                                                             16133 [001] 158126.498412 : function : inotify_inode_queue_event &lt;<br />
                                                                                                                                                                                                                                                         &#8211;vfs_write<br />
                                                                                                                                                                                                                                                                 trace &#8211;<br />
                                                                                                                                                                                                                                                             cmd &#8211; 16129 [002] 158126.498420 : lock_release : 0xffff88003f1fa4f8 &amp;<br />
                                                                                                                                                                                                                                                     sb-&gt;s_type-&gt;i_mutex_key<br />
                                                                                                                                                                                                                                                                 trace &#8211;<br />
                                                                                                                                                                                                                                                             cmd &#8211; 16131 [000] 158126.498421 : function : security_file_alloc &lt;<br />
                                                                                                                                                                                                                                                         &#8211;get_empty_filp<br />
                                                                                                                                                                                                                                                                 sleep &#8211;<br />
                                                                                                                                                                                                                                                             16133 [001] 158126.498422 : function : __fsnotify_parent &lt;<br />
                                                                                                                                                                                                                                                         &#8211;vfs_write<br />
                                                                                                                                                                                                                                                                 trace &#8211;<br />
                                                                                                                                                                                                                                                             cmd &#8211; 16130 [003] 158126.498422 : function : rw_verify_area &lt;<br />
                                                                                                                                                                                                                                                         &#8211;do_splice_to<br />
                                                                                                                                                                                                                                                                 trace &#8211;<br />
                                                                                                                                                                                                                                                             cmd &#8211; 16131 [000] 158126.498424 : function : cap_file_alloc_security &lt;<br />
                                                                                                                                                                                                                                                         &#8211;security_file_alloc<br />
                                                                                                                                                                                                                                                                 trace &#8211;<br />
                                                                                                                                                                                                                                                             cmd &#8211; 16129 [002] 158126.498425 : function : syscall_trace_leave &lt;<br />
                                                                                                                                                                                                                                                         &#8211;int_check_syscall_exit_work<br />
                                                                                                                                                                                                                                                                 sleep &#8211;<br />
                                                                                                                                                                                                                                                             16133 [001] 158126.498426 : function : inotify_dentry_parent_queue_event &lt;<br />
                                                                                                                                                                                                                                                         &#8211;vfs_write<br />
                                                                                                                                                                                                                                                                 trace &#8211;<br />
                                                                                                                                                                                                                                                             cmd &#8211; 16130 [003] 158126.498426 : function : security_file_permission &lt;<br />
                                                                                                                                                                                                                                                         &#8211;rw_verify_area<br />
                                                                                                                                                                                                                                                                 trace &#8211;<br />
                                                                                                                                                                                                                                                             cmd &#8211; 16129 [002] 158126.498428 : function : audit_syscall_exit &lt;<br />
                                                                                                                                                                                                                                                         &#8211;syscall_trace_leave<br />
                                                                                                                                                                                                                                                             [&#8230;]
</dl>
<p> To see everything but the function traces: </p>
<dl>
<dt>
<dd>
#trace &#8211; cmd report &#8211; v &#8211; F &#8216;function&#8217;<br />
trace &#8211; cmd &#8211; 16131 [000] 158126.498411 : kmem_cache_alloc : call_site = 811223c5 ptr = 0xffff88003ecf2b40 bytes_req = 272 bytes_alloc = 320 gfp_flags = GFP_KERNEL | GFP_ZERO<br />
                                                                                                                                                                                  trace &#8211;<br />
                                                                                                                                                                              cmd &#8211; 16129 [002] 158126.498420 : lock_release : 0xffff88003f1fa4f8 &amp;<br />
                                                                                                                                                                          sb-&gt;s_type-&gt;i_mutex_key<br />
                                                                                                                                                                                  trace &#8211;<br />
                                                                                                                                                                              cmd &#8211; 16130 [003] 158126.498436 : lock_acquire : 0xffffffff8166bf78 read all_cpu_access_lock trace &#8211; cmd &#8211; 16131 [000] 158126.498438 : lock_acquire : 0xffff88003df5b520 read &amp;<br />
                                                                                                                                                                          fs-&gt;lock<br />
                                                                                                                                                                                  trace &#8211;<br />
                                                                                                                                                                              cmd &#8211; 16129 [002] 158126.498446 : kfree : call_site = 810a7abb ptr = 0x0 trace &#8211; cmd &#8211; 16130 [003] 158126.498448 : lock_acquire : 0xffff880002250a80 &amp; per_cpu(cpu_access_lock, cpu) trace &#8211; cmd &#8211; 16129 [002] 158126.498450 : sys_exit_splice : 0xfffffff5 trace &#8211; cmd &#8211; 16131 [000] 158126.498454 : lock_release : 0xffff88003df5b520 &amp; fs-&gt;lock sleep &#8211; 16133 [001] 158126.498456 : kfree : call_site = 810a7abb ptr = 0x0 sleep &#8211; 16133 [001] 158126.498460 : sys_exit_write : 0x1 trace &#8211; cmd &#8211; 16130 [003] 158126.498462 : kmalloc : call_site = 810bf95b ptr = 0xffff88003dedc040 bytes_req = 24 bytes_alloc = 32 gfp_flags = GFP_KERNEL | GFP_ZERO
</dl>
<p> To see only the kmalloc calls that were greater than 1000 bytes: </p>
<dl>
<dt>
<dd>
<pre>
 #trace-cmd report -F 'kmalloc: bytes_req &gt; 1000'
          &lt;idle&gt;-0     [000] 158128.126641: kmalloc: call_site=81330635 ptr=0xffff88003c2fd000 bytes_req=2096 bytes_alloc=4096 gfp_flags=GFP_ATOMIC
</pre>
</dl>
<p> To see wakeups and sched switches that left the previous task in the running state: </p>
<dl>
<dt>
<dd>
#trace &#8211; cmd report &#8211; F &#8216;sched: prev_state == 0 || (success == 1)&#8217;<br />
trace &#8211; cmd &#8211; 16132 [002] 158126.499951 : sched_wakeup : comm = trace &#8211; cmd pid = 16129 prio = 120 success = 1 target_cpu = 002 trace &#8211; cmd &#8211; 16132 [002] 158126.500401 : sched_switch : prev_comm = trace &#8211; cmd prev_pid = 16132 prev_prio = 120 prev_state = R == &gt; next_comm = trace &#8211; cmd next_pid = 16129 next_prio = 120 &lt; idle &gt; -0 [003] 158126.500585 : sched_wakeup : comm = trace &#8211; cmd pid = 16130 prio = 120 success = 1 target_cpu = 003 &lt; idle &gt; -0 [003] 158126.501241 : sched_switch : prev_comm = swapper prev_pid = 0 prev_prio = 120 prev_state = R == &gt; next_comm = trace &#8211; cmd next_pid = 16130 next_prio = 120 trace &#8211; cmd &#8211; 16132 [000] 158126.502475 : sched_wakeup : comm = trace &#8211; cmd pid = 16131 prio = 120 success = 1 target_cpu = 000 trace &#8211; cmd &#8211; 16131 [002] 158126.506516 : sched_wakeup : comm = trace &#8211; cmd pid = 16129 prio = 120 success = 1 target_cpu = 002 &lt; idle &gt; -0 [003] 158126.550110 : sched_switch : prev_comm = swapper prev_pid = 0 prev_prio = 120 prev_state = R == &gt; next_comm = trace &#8211; cmd next_pid = 16130 next_prio = 120 trace &#8211; cmd &#8211; 16131 [003] 158126.570243 : sched_wakeup : comm = trace &#8211; cmd pid = 16129 prio = 120 success = 1 target_cpu = 003 trace &#8211; cmd &#8211; 16130 [002] 158126.618202 : sched_switch : prev_comm = trace &#8211; cmd prev_pid = 16130 prev_prio = 120 prev_state = R == &gt; next_comm = yum &#8211; updatesd next_pid = 3088 next_prio = 1 20 trace &#8211; cmd &#8211; 16129 [003] 158126.622379 : sched_wakeup : comm = trace &#8211; cmd pid = 16131 prio = 120 success = 1 target_cpu = 003 trace &#8211; cmd &#8211; 16129 [000] 158126.649287 : sched_wakeup : comm = trace &#8211; cmd pid = 16131 prio = 120 success = 1 target_cpu = 000
</dl>
<p> The above needs a little explanation. The filter specifies the &quot;sched&quot; subsystem, which includes both sched_switch and sched_wakeup events. Any event that does not have the format field &quot;prev_state&quot; or &quot;success&quot;, will evaluate those expressions as FALSE, and will not produce a match. Using &quot;||&quot; will have the &quot;prev_state&quot; test happen for the &quot;sched_switch&quot; event and the &quot;success&quot; test happen for the &quot;sched_wakeup&quot; event. </p>
<dl>
<dt>
<dd>
#trace &#8211; cmd report &#8211; w &#8211; F &#8216;sched_switch, sched_wakeup.*&#8217;<br />
[&#8230;] trace &#8211; cmd &#8211; 16130 [003] 158131.580616 : sched_wakeup : comm = trace &#8211; cmd pid = 16131 prio = 120 success = 1 target_cpu = 003 trace &#8211; cmd &#8211; 16129 [000] 158131.581502 : sched_switch : prev_comm = trace &#8211; cmd prev_pid = 16129 prev_prio = 120 prev_state = S == &gt; next_comm = trace &#8211; cmd next_pid = 16131 next_prio = 120 Latency : 885.901 usecs<br />
                                                                                                                                                                                                                                                                                                                                     trace &#8211;<br />
                                                                                                                                                                                                                                                                                                                                 cmd &#8211; 16131 [000] 158131.582414 : sched_wakeup : comm = trace &#8211; cmd pid = 16129 prio = 120 success = 1 target_cpu = 000 trace &#8211; cmd &#8211; 16132 [001] 158131.583219 : sched_switch : prev_comm = trace &#8211; cmd prev_pid = 16132 prev_prio = 120 prev_state = S == &gt; next_comm = trace &#8211; cmd next_pid = 16129 next_prio = 120 Latency : 804.809 usecs<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        sleep &#8211;<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    16133 [002] 158131.584121 : sched_wakeup : comm = trace &#8211; cmd pid = 16120 prio = 120 success = 1 target_cpu = 002 trace &#8211; cmd &#8211; 16129 [001] 158131.584128 : sched_wakeup : comm = trace &#8211; cmd pid = 16132 prio = 120 success = 1 target_cpu = 001 sleep &#8211; 16133 [002] 158131.584275 : sched_switch : prev_comm = sleep prev_pid = 16133 prev_prio = 120 prev_state = R == &gt; next_comm = trace &#8211; cmd next_pid = 16120 next_prio = 120 Latency : 153.915 usecs<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         trace &#8211;<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     cmd &#8211; 16130 [003] 158131.585284 : sched_switch : prev_comm = trace &#8211; cmd prev_pid = 16130 prev_prio = 120 prev_state = S == &gt; next_comm = trace &#8211; cmd next_pid = 16132 next_prio = 120 Latency : 1155.677 usecs<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   Average wakeup latency : 26626.656 usecs
</dl>
<p> The above trace produces the wakeup latencies of the tasks. The &quot;sched_switch&quot; event reports each individual latency after writing the event information. At the end of the report, the average wakeup latency is reported. </p>
<dl>
<dt>
<dd>
<pre><code>
#trace - cmd report - w - F 'sched_switch, sched_wakeup.*: prio &lt; 100 || next_prio &lt; 100'
&lt;idle&gt; - 0 [003] 158131.516753 : sched_wakeup : comm = ksoftirqd / 3 pid = 13 prio = 49 success = 1 target_cpu = 003 &lt; idle &gt; -0 [003] 158131.516855 : sched_switch : prev_comm = swapper prev_pid = 0 prev_prio = 120 prev_state = R == &gt; next_comm = ksoftirqd / 3 next_pid = 13 next_prio = 49 Latency : 101.244 usecs&lt;idle&gt; - 0 [003] 158131.533781 : sched_wakeup : comm = ksoftirqd / 3 pid = 13 prio = 49 success = 1 target_cpu = 003 &lt; idle &gt; -0 [003] 158131.533897 : sched_switch : prev_comm = swapper prev_pid = 0 prev_prio = 120 prev_state = R == &gt; next_comm = ksoftirqd / 3 next_pid = 13 next_prio = 49 Latency : 115.608 usecs&lt;idle&gt; - 0 [003] 158131.569730 : sched_wakeup : comm = ksoftirqd / 3 pid = 13 prio = 49 success = 1 target_cpu = 003 &lt; idle &gt; -0 [003] 158131.569851 : sched_switch : prev_comm = swapper prev_pid = 0 prev_prio = 120 prev_state = R == &gt; next_comm = ksoftirqd / 3 next_pid = 13 next_prio = 49 Latency : 121.024 usecs
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             Average wakeup latency : 110.021 usecs
</code></pre>
</dl>
<p> The above version will only show the wakeups and context switches of Real Time tasks. The <i>prio</i> used inside the kernel starts at 0 for highest priority. That is <i>prio</i> 0 is equivalent to user space real time priority 99, and priority 98 is equivalent to user space real time priority 1. Prios less than 100 represent Real Time tasks. </p>
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
<p> <a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a>(1), <a href="/docs/linux/man/1-trace-cmd-record/">trace-cmd-record</a>(1), <a href="/docs/linux/man/1-trace-cmd-start/">trace-cmd-start</a>(1), <a href="/docs/linux/man/1-trace-cmd-stop/">trace-cmd-stop</a>(1), <a href="/docs/linux/man/1-trace-cmd-extract/">trace-cmd-extract</a>(1), <a href="/docs/linux/man/1-trace-cmd-reset/">trace-cmd-reset</a>(1), <a href="/docs/linux/man/1-trace-cmd-split/">trace-cmd-split</a>(1), <a href="/docs/linux/man/1-trace-cmd-list/">trace-cmd-list</a>(1), <a href="/docs/linux/man/1-trace-cmd-listen/">trace-cmd-listen</a>(1), <a href="/docs/linux/man/1-trace-cmd-profile/">trace-cmd-profile</a>(1)</p>
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
