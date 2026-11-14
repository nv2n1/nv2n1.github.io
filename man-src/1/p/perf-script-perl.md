---
title: "perf-script-perl(1)"
name: "perf-script-perl"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perf-script-perl/"
description: "perf-script-perl – Process trace data with a Perl script"
---

<h2 class="name">NAME</h2>
<p> perf-script-perl &#8211; Process trace data with a Perl script </p>
<h2>SYNOPSIS</h2>
<pre><code>
perf script [-s[Perl]:script[.pl]]
</code></pre>
<h2>DESCRIPTION</h2>
<p> This perf script option is used to process perf script data using perf&#8217;s built-in Perl interpreter. It reads and processes the input file and displays the results of the trace analysis implemented in the given Perl script, if any.</p>
<h2>STARTER SCRIPTS</h2>
<p> You can avoid reading the rest of this document by running <i>perf script -g perl</i> in the same directory as an existing perf.data trace file. That will generate a starter script containing a handler for each of the event types in the trace file; it simply prints every available field for each event in the trace file. </p>
<p> You can also look at the existing scripts in ~/libexec/perf-core/scripts/perl for typical examples showing how to do basic things like aggregate event data, print results, etc. Also, the check-perf-script.pl script, while not interesting for its results, attempts to exercise all of the main scripting features.</p>
<h2>EVENT HANDLERS</h2>
<p> When perf script is invoked using a trace script, a user-defined <i>handler function</i> is called for each event in the trace. If there&#8217;s no handler function defined for a given event type, the event is ignored (or passed to a <i>trace_handled</i> function, see below) and the next event is processed. </p>
<p> Most of the event&#8217;s field values are passed as arguments to the handler function; some of the less common ones aren&#8217;t &#8211; those are available as calls back into the perf executable (see below). </p>
<p> As an example, the following perf record command can be used to record all sched_wakeup events in the system: </p>
<dl>
<dt>
<dd>
<pre>
# perf record -a -e sched:sched_wakeup
</pre>
</dl>
<p> Traces meant to be processed using a script should be recorded with the above option: -a to enable system-wide collection. </p>
<p> The format file for the sched_wakep event defines the following fields (see /sys/kernel/debug/tracing/events/sched/sched_wakeup/format): </p>
<dl>
<dt>
<dd>
.ft C<br />
    format : field : unsigned short common_type;<br />
field : unsigned char common_flags;<br />
field : unsigned char common_preempt_count;<br />
field : int common_pid;<br />
field : char comm[TASK_COMM_LEN];<br />
field : pid_t pid;<br />
field : int prio;<br />
field : int success;<br />
field : int target_cpu;<br />
.ft
</dl>
<p> The handler function for this event would be defined as: </p>
<dl>
<dt>
<dd>
<pre>
.ft C
sub sched::sched_wakeup
{
   my ($event_name, $context, $common_cpu, $common_secs,
       $common_nsecs, $common_pid, $common_comm,
       $comm, $pid, $prio, $success, $target_cpu) = @_;
}
.ft
</pre>
</dl>
<p> The handler function takes the form subsystem::event_name. </p>
<p> The $common_* arguments in the handler&#8217;s argument list are the set of arguments passed to all event handlers; some of the fields correspond to the common_* fields in the format file, but some are synthesized, and some of the common_* fields aren&#8217;t common enough to to be passed to every event as arguments but are available as library functions. </p>
<p> Here&#8217;s a brief description of each of the invariant event args: </p>
<dl>
<dt>
<dd>
<pre>
$event_name                the name of the event as text
$context                   an opaque 'cookie' used in calls back into perf
$common_cpu                the cpu the event occurred on
$common_secs               the secs portion of the event timestamp
$common_nsecs              the nsecs portion of the event timestamp
$common_pid                the pid of the current task
$common_comm               the name of the current process
</pre>
</dl>
<p> All of the remaining fields in the event&#8217;s format file have counterparts as handler function arguments of the same name, as can be seen in the example above. </p>
<p> The above provides the basics needed to directly access every field of every event in a trace, which covers 90% of what you need to know to write a useful trace script. The sections below cover the rest.</p>
<h2>SCRIPT LAYOUT</h2>
<p> Every perf script Perl script should start by setting up a Perl module search path and &#8216;use&#8217;ing a few support modules (see module descriptions below): </p>
<dl>
<dt>
<dd>
<pre><code>
.ft C
    use lib "$ENV{'PERF_EXEC_PATH'}/scripts/perl/Perf-Trace-Util/lib";
use lib "./Perf-Trace-Util/lib";
use Perf::Trace::Core;
use Perf::Trace::Context;
use Perf::Trace::Util;
.ft
</code></pre>
</dl>
<p> The rest of the script can contain handler functions and support functions in any order. </p>
<p> Aside from the event handler functions discussed above, every script can implement a set of optional functions: </p>
<p> <code>trace_begin</code>, if defined, is called before any event is processed and gives scripts a chance to do setup tasks: </p>
<dl>
<dt>
<dd>
<pre>
.ft C
 sub trace_begin
 {
 }
.ft
</pre>
</dl>
<p> <code>trace_end</code>, if defined, is called after all events have been processed and gives scripts a chance to do end-of-script tasks, such as display results: </p>
<dl>
<dt>
<dd>
<pre>
.ft C
sub trace_end
{
}
.ft
</pre>
</dl>
<p> <code>trace_unhandled</code>, if defined, is called after for any event that doesn&#8217;t have a handler explicitly defined for it. The standard set of common arguments are passed into it: </p>
<dl>
<dt>
<dd>
<pre>
.ft C
sub trace_unhandled
{
    my ($event_name, $context, $common_cpu, $common_secs,
        $common_nsecs, $common_pid, $common_comm) = @_;
}
.ft
</pre>
</dl>
<p> The remaining sections provide descriptions of each of the available built-in perf script Perl modules and their associated functions.</p>
<h2>AVAILABLE MODULES AND FUNCTIONS</h2>
<p> The following sections describe the functions and variables available via the various Perf::Trace::* Perl modules. To use the functions and variables from the given module, add the corresponding <i>use Perf::Trace::XXX</i> line to your perf script script.</p>
<h3>Perf::Trace::Core Module</h3>
<p> These functions provide some essential functions to user scripts. </p>
<p> The <code>flag_str</code> and <code>symbol_str</code> functions provide human-readable strings for flag and symbolic fields. These correspond to the strings and values parsed from the <i>print fmt</i> fields of the event format files: </p>
<dl>
<dt>
<dd>
<pre>
flag_str($event_name, $field_name, $field_value) - returns the string representation corresponding to $field_value for the flag field $field_name of event $event_name
symbol_str($event_name, $field_name, $field_value) - returns the string representation corresponding to $field_value for the symbolic field $field_name of event $event_name
</pre>
</dl>
<h3>Perf::Trace::Context Module</h3>
<p> Some of the <i>common</i> fields in the event format file aren&#8217;t all that common, but need to be made accessible to user scripts nonetheless. </p>
<p> Perf::Trace::Context defines a set of functions that can be used to access this data in the context of the current event. Each of these functions expects a $context variable, which is the same as the $context variable passed into every event handler as the second argument. </p>
<dl>
<dt>
<dd>
<pre>
common_pc($context) - returns common_preempt count for the current event
common_flags($context) - returns common_flags for the current event
common_lock_depth($context) - returns common_lock_depth for the current event
</pre>
</dl>
<h3>Perf::Trace::Util Module</h3>
<p> Various utility functions for use with perf script: </p>
<dl>
<dt>
<dd>
<pre>
nsecs($secs, $nsecs) - returns total nsecs given secs/nsecs pair
nsecs_secs($nsecs) - returns whole secs portion given nsecs
nsecs_nsecs($nsecs) - returns nsecs remainder given nsecs
nsecs_str($nsecs) - returns printable string in the form secs.nsecs
avg($total, $n) - returns average given a sum and a total number of values
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perf-script/">perf-script</a></code>(1) </p>
<h2>Index</h2>
