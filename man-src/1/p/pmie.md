---
title: "pmie(1)"
name: "pmie"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmie/"
description: "pmie – inference engine for performance metrics"
---

<h2>NAME</h2>
<p> <code>pmie</code> &#8211; inference engine for performance metrics</p>
<h2>SYNOPSIS</h2>
<p> <code>pmie</code> [<code>-bCdefHqVvWxz</code>] [<code>-A</code> <i>align</i>] [<code>-a</code> <i>archive</i>] [<code>-c</code> <i>filename</i>] [<code>-h</code> <i>host</i>] [<code>-l</code> <i>logfile</i>] [<code>-j</code> <i>stompfile</i>] [<code>-n</code> <i>pmnsfile</i>] [<code>-O</code> <i>offset</i>] [<code>-S</code> <i>starttime</i>] [<code>-T</code> <i>endtime</i>] [<code>-t</code> <i>interval</i>] [<code>-U</code> <i>username</i>] [<code>-Z</code> <i>timezone</i>] [<i>filename &#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmie</code> accepts a collection of arithmetic, logical, and rule expressions to be evaluated at specified frequencies. The base data for the expressions consists of performance metrics values delivered in real-time from any host running the Performance Metrics Collection Daemon (PMCD), or using historical data from Performance Co-Pilot (PCP) archive logs. </p>
<p> As well as computing arithmetic and logical values, <code>pmie</code> can execute actions (popup alarms, write system log messages, and launch programs) in response to specified conditions. Such actions are extremely useful in detecting, monitoring and correcting performance related problems. </p>
<p> The expressions to be evaluated are read from configuration files specified by one or more <i>filename</i> arguments. In the absence of any <i>filename</i>, expressions are read from standard input. </p>
<p> A description of the command line options specific to <code>pmie</code> follows:</p>
<dl>
<dt><code>-a</code></p>
<dd> <i>archive</i> which is a comma-separated list of names, each of which may be the base name of an archive or the name of a directory containing one or more archives written by <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1). Multiple instances of the <code>-a</code> flag may appear on the command line to specify a list of sets of archives. In this case, it is required that only one set of archives be present for any one host. Also, any explicit host names occurring in a <code>pmie</code> expression must match the host name recorded in one of the archive labels. In the case of multiple sets of archives, timestamps recorded in the archives are used to ensure temporal consistency.</p>
<dt><code>-b</code></p>
<dd> Output will be line buffered and standard output is attached to standard error. This is most useful for background execution in conjunction with the <code>-l</code> option. The <code>-b</code> option is always used for <code>pmie</code> instances launched from <code><a href="/docs/linux/man/1-pmie_check/">pmie_check</a></code>(1).</p>
<dt><code>-C</code></p>
<dd> Parse the configuration file(s) and exit before performing any evaluations. Any errors in the configuration file are reported.</p>
<dt><code>-c</code></p>
<dd> An alternative to specifying <i>filename</i> at the end of the command line.</p>
<dt><code>-d</code></p>
<dd> Normally <code>pmie</code> would be launched as a non-interactive process to monitor and manage the performance of one or more hosts. Given the <code>-d</code> flag however, execution is interactive and the user is presented with a menu of options. Interactive mode is useful mainly for debugging new expressions.</p>
<dt><code>-e</code></p>
<dd> When used with <code>-V</code>, <code>-v</code> or <code>-W</code>, this option forces timestamps to be reported with each expression. The timestamps are in <code><a href="/docs/linux/man/3-ctime/">ctime</a></code>(3) format, enclosed in parenthesis and appear after the expression name and before the expression value, e.g. </p>
<pre>
        expr_1 (Tue Feb  6 19:55:10 2001): 12
</pre>
<dt><code>-f</code></p>
<dd> If the <code>-l</code> option is specified and there is no <code>-a</code> option (ie. real-time monitoring) then <code>pmie</code> is run as a daemon in the background (in all other cases foreground is the default). The <code>-f</code> option forces <code>pmie</code> to be run in the foreground, independent of any other options.</p>
<dt><code>-h</code></p>
<dd> By default performance data is fetched from the local host (in real-time mode) or the host for the first named set of archives on the command line (in archive mode). The <i>host</i> argument overrides this default. It does not override hosts explicitly named in the expressions being evaluated. The <i>host</i> argument is interpreted as a connection specification for <i>pmNewContext</i>, and is later mapped to the remote pmcd&#8217;s self-reported host name for reporting purposes. See also the %h vs. %c substitutions in rule action strings below.</p>
<dt><code>-l</code></p>
<dd> Standard error is sent to <i>logfile</i>.</p>
<dt><code>-j</code></p>
<dd> An alternative STOMP protocol configuration is loaded from <i>stompfile</i>. If this option is not used, and the <i>stomp</i> action is used in any rule, the default location <i>$PCP_SYSCONF_DIR/pmie/config/stomp</i> will be used.</p>
<dt><code>-n</code></p>
<dd> An alternative Performance Metrics Name Space (PMNS) is loaded from the file <i>pmnsfile</i>.</p>
<dt><code>-q</code></p>
<dd> Suppresses diagnostic messages that would be printed to standard output by default, especially the &quot;evaluator exiting&quot; message as this can confuse scripts.</p>
<dt><code>-t</code></p>
<dd> The <i>interval</i> argument follows the syntax described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), and in the simplest form may be an unsigned integer (the implied units in this case are seconds). The value is used to determine the sample interval for expressions that do not explicitly set their sample interval using the <code>pmie</code> variable <tt>delta</tt> described below. The default is 10.0 seconds.</p>
<dt><code>-U</code> <i>username</i></p>
<dd> User account under which to run <code>pmie</code>. The default is the current user account for interactive use. When run as a daemon, the unprivileged &quot;pcp&quot; account is used in current versions of PCP, but in older versions the superuser account (&quot;root&quot;) was used by default.</p>
<dt><code>-v</code></p>
<dd> Unless one of the verbose options <code>-V</code>, <code>-v</code> or <code>-W</code> appears on the command line, expressions are evaluated silently, the only output is as a result of any actions being executed. In the verbose mode, specified using the <code>-v</code> flag, the value of each expression is printed as it is evaluated. The values are in canonical units; bytes in the dimension of &#8220;space&#8221;, seconds in the dimension of &#8220;time&#8221; and events in the dimension of &#8220;count&#8221;. See <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3) for details of the supported dimension and scaling mechanisms for performance metrics. The verbose mode is useful in monitoring the value of given expressions, evaluating derived performance metrics, passing these values on to other tools for further processing and in debugging new expressions.</p>
<dt><code>-V</code></p>
<dd> This option has the same effect as the <code>-v</code> option, except that the name of the host and instance (if applicable) are printed as well as expression values.</p>
<dt><code>-W</code></p>
<dd> This option has the same effect as the <code>-V</code> option described above, except that for boolean expressions, only those names and values that make the expression true are printed. These are the same names and values accessible to rule actions as the %h, %i, %c and %v bindings, as described below.</p>
<dt><code>-x</code></p>
<dd> Execute in domain agent mode. This mode is used within the Performance Co-Pilot product to derive values for summary metrics, see <code><a href="/docs/linux/man/1-pmdasummary/">pmdasummary</a></code>(1). Only restricted functionality is available in this mode (expressions with actions may <code>not</code> be used).</p>
<dt><code>-Z</code></p>
<dd> Change the reporting timezone to <i>timezone</i> in the format of the environment variable <code>TZ</code> as described in <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7).</p>
<dt><code>-z</code></p>
<dd> Change the reporting timezone to the timezone of the host that is the source of the performance metrics, as identified via either the <code>-h</code> option or the first named set of archives (as described above for the <code>-a</code> option).</dl>
<p> The <code>-S</code>, <code>-T</code>, <code>-O</code>, and <code>-A</code> options may be used to define a time window to restrict the samples retrieved, set an initial origin within the time window, or specify a &#8220;natural&#8221; alignment of the sample times; refer to <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) for a complete description of these options. </p>
<p> Output from <code>pmie</code> is directed to standard output and standard error as follows:</p>
<dl>
<dt><code>stdout</code></p>
<dd> Expression values printed in the verbose <code>-v</code> mode and the output of <code>print</code> actions.</p>
<dt><code>stderr</code></p>
<dd> Error and warning messages for any syntactic or semantic problems during expression parsing, and any semantic or performance metrics availability problems during expression evaluation.</dl>
<h2>EXAMPLES</h2>
<p> The following example expressions demonstrate some of the capabilities of the inference engine. </p>
<p> The directory <i>$PCP_DEMOS_DIR/pmie</i> contains a number of other annotated examples of <code>pmie</code> expressions. </p>
<p> The variable delta controls expression evaluation frequency. Specify that subsequent expressions be evaluated once a second, until further notice: </p>
<pre>
delta = 1 sec;
</pre>
<p> If the total context switch rate exceeds 10000 per second per CPU, then display an alarm notifier: </p>
<pre>
kernel.all.pswitch / hinv.ncpu &gt; 10000 count/sec
-&gt; alarm &quot;high context switch rate %v&quot;;
</pre>
<p> If the high context switch rate is sustained for 10 consecutive samples, then launch <code><a href="/docs/linux/man/1-top/">top</a></code>(1) in an <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1) window to monitor processes, but do this at most once every 5 minutes: </p>
<pre>
all_sample (
    kernel.all.pswitch @0..9 &gt; 10 Kcount/sec * hinv.ncpu
) -&gt; shell 5 min &quot;xterm -e 'top'&quot;;
</pre>
<p> The following rules are evaluated once every 20 seconds: </p>
<pre>
delta = 20 sec;
</pre>
<p> If any disk is performing more than 60 I/Os per second, then print a message identifying the busy disk to standard output and launch <code><a href="/docs/linux/man/1-dkvis/">dkvis</a></code>(1): </p>
<pre>
some_inst (
    disk.dev.total &gt; 60 count/sec
) -&gt; print &quot;busy disks:&quot; &quot; %i&quot; &amp;
     shell 5 min &quot;dkvis&quot;;
</pre>
<p> Refine the preceding rule to apply only between the hours of 9am and 5pm, and to require 3 of 4 consecutive samples to exceed the threshold before executing the action: </p>
<pre><code>
$hour &gt;= 9 &amp;&amp; $hour &lt;= 17 &amp;&amp;
    some_inst(
        75 % _sample(
                 disk.dev.total @0..3 &gt; 60 count / sec))
        -&gt;print "disks busy for 20 sec:"
                " [%h]%i";
</code></pre>
<p> The following two rules are evaluated once every 10 minutes: </p>
<pre>
delta = 10 min;
</pre>
<p> If either the / or the /usr filesystem is more than 95% full, display an alarm popup, but not if it has already been displayed during the last 4 hours: </p>
<p>filesys.free #&#8217;/dev/root&#8217; /<br />
        filesys.capacity #&#8217;/dev/root&#8217; &lt;<br />
    0.05<br />
        -&gt;alarm 4 hour &#8220;root filesystem (almost) full&#8221;;<br />
filesys.free #&#8217;/dev/usr&#8217; /<br />
        filesys.capacity #&#8217;/dev/usr&#8217; &lt;<br />
    0.05<br />
        -&gt;alarm 4 hour &#8220;/usr filesystem (almost) full&#8221;;</p>
<p> The following rule requires a machine that supports the PCP environment metrics. If the machine environment temperature rises more than 2 degrees over a 10 minute interval, write an entry in the system log: </p>
<pre>
environ.temp @0 - environ.temp @1 &gt; 2
-&gt; alarm &quot;temperature rising fast&quot; &amp;
   syslog &quot;machine room temperature rise alarm&quot;;
</pre>
<p> And something interesting if you have performance problems with your Oracle database: </p>
<p>// back to 30sec evaluations<br />
delta = 30 sec;<br />
sid = &#8220;ptg1&#8221;;<br />
#$ORACLE_SID setting<br />
    lid = &#8220;223&#8221;;<br />
#latch ID from v$latch<br />
    lru = &#8220;#&#8217;$sid/$lid cache buffers lru chain'&#8221;;<br />
host = &#8220;:moomba.melbourne.sgi.com&#8221;;<br />
gets = &#8220;oracle.latch.gets $host $lru&#8221;;<br />
total = &#8220;oracle.latch.gets $host $lru +<br />
                oracle.latch.misses $host $lru +<br />
                oracle.latch.immisses $host $lru &#8220;;<br />
                $total &gt;<br />
            100 &amp;&amp;<br />
        $gets / $total &lt; 0.2<br />
                             -&gt;alarm &#8220;high lru latch contention in database $sid&#8221;;</p>
<p> The following ruleset will emit exactly one message depending on the availability and value of the 1-minute load average. </p>
<pre><code>
delta = 1 minute;
ruleset
        kernel.all.load #'1 minute' &gt; 10 * hinv.ncpu-&gt;print "extreme load average %v" else kernel.all.load #'1 minute' &gt;
    2 * hinv.ncpu-&gt;print "moderate load average %v" unknown-&gt;print "load average unavailable" otherwise-&gt;print "load average OK";
</code></pre>
<p> The following rule will emit a message when some filesystem is more than 75% full and is filling at a rate that if sustained would fill the filesystem to 100% in less than 30 minutes. </p>
<pre>
some_inst (
    100 * filesys.used / filesys.capacity &gt; 75 &amp;&amp;
    filesys.used + 30min * (rate filesys.used) &gt; filesys.capacity
) -&gt; print &quot;filesystem will be full within 30 mins:&quot; &quot; %i&quot;;
</pre>
<p> If the metric <tt>mypmda.errors</tt> counts errors then the following rule will emit a message if the rate of errors exceeds 1 per second provided the error count is less than 100. </p>
<pre>
mypmda.errors &gt; 1 &amp;&amp; instant mypmda.errors &lt; 100
-&gt; print &quot;high error rate: %v&quot;;
</pre>
<h2>QUICK START</h2>
<p> The <code>pmie</code> specification language is powerful and large. </p>
<p> To expedite rapid development of <code>pmie</code> rules, the <code><a href="/docs/linux/man/1-pmieconf/">pmieconf</a></code>(1) tool provides a facility for generating a <code>pmie</code> configuration file from a set of generalized <code>pmie</code> rules. The supplied set of rules covers a wide range of performance scenarios. </p>
<p> The <i>Performance Co-Pilot User&#8217;s and Administrator&#8217;s Guide</i> provides a detailed tutorial-style chapter covering <code>pmie</code>.</p>
<h2>EXPRESSION SYNTAX</h2>
<p> This description is terse and informal. For a more comprehensive description see the <i>Performance Co-Pilot User&#8217;s and Administrator&#8217;s Guide</i>. </p>
<p> A <code>pmie</code> specification is a sequence of semicolon terminated expressions. </p>
<p> Basic operators are modeled on the arithmetic, relational and Boolean operators of the C programming language. Precedence rules are as expected, although the use of parentheses is encouraged to enhance readability and remove ambiguity. </p>
<p> Operands are performance metric names (see <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5)) and the normal literal constants. </p>
<p> Operands involving performance metrics may produce sets of values, as a result of enumeration in the dimensions of <code>hosts</code>, <code>instances</code> and <code>time</code>. Special qualifiers may appear after a performance metric name to define the enumeration in each dimension. For example, </p>
<p> kernel.percpu.cpu.user :foo :bar #cpu0 @0..2 </p>
<p> defines 6 values corresponding to the time spent executing in user mode on CPU 0 on the hosts &#8220;foo&#8221; and &#8220;bar&#8221; over the last 3 consecutive samples. The default interpretation in the absence of <code>:</code> (host), <code>#</code> (instance) and <code>@</code> (time) qualifiers is all instances at the most recent sample time for the default source of PCP performance metrics. </p>
<p> Host and instance names that do not follow the rules for variables in programming languages, ie. alphabetic optionally followed by alphanumerics, should be enclosed in single quotes. </p>
<p> Expression evaluation follows the law of &#8220;least surprises&#8221;. Where performance metrics have the semantics of a counter, <code>pmie</code> will automatically convert to a rate based upon consecutive samples and the time interval between these samples. All expressions are evaluated in double precision, and where appropriate, automatically scaled into canonical units of &#8220;bytes&#8221;, &#8220;seconds&#8221; and &#8220;counts&#8221;. </p>
<p> A <code>rule</code> is a special form of expression that specifies a condition or logical expression, a special operator (<code>-&gt;</code>) and actions to be performed when the condition is found to be true. </p>
<p> The following table summarizes the basic <code>pmie</code> operators: </p>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center>Operators</td>
<td ALIGN=center>Explanation
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>+ &#8211; * /</td>
<td>Arithmetic
</td>
</tr>
<tr VALIGN=top>
<td>&lt; &lt;= == &gt;= &gt; !=</td>
<td>Relational (value comparison)
</td>
</tr>
<tr VALIGN=top>
<td>! &amp;&amp; ||</td>
<td>Boolean
</td>
</tr>
<tr VALIGN=top>
<td>-&gt;</td>
<td>Rule
</td>
</tr>
<tr VALIGN=top>
<td>rising</td>
<td>Boolean, false to true transition
</td>
</tr>
<tr VALIGN=top>
<td>falling</td>
<td>Boolean, true to false transition
</td>
</tr>
<tr VALIGN=top>
<td>rate</td>
<td>Explicit rate conversion (rarely required)
</td>
</tr>
<tr VALIGN=top>
<td>instant</td>
<td>No automatic rate conversion (rarely required)
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> The rate and instant operators are the logical inverse of one another, so an arithmetic expression <i>expr</i> is equal to rate instant <i>expr</i>. The more useful cases involve using rate with a metric that is not a counter to determine the rate of change over time or instant with a metric that is a counter to determine if the current value is above or below some threshold. </p>
<p> Aggregate operators may be used to aggregate or summarize along one dimension of a set-valued expression. The following aggregate operators map from a logical expression to a logical expression of lower dimension. </p>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center>Operators</td>
<td ALIGN=center>Type</td>
<td ALIGN=center>Explanation
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code> some_inst<br />
 some_host<br />
 some_sample </code></td>
<td>Existential</td>
<td> True if at least one set member is true in the associated dimension
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code> all_inst<br />
 all_host<br />
 all_sample </code></td>
<td>Universal</td>
<td> True if all set members are true in the associated dimension
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code> N%_inst<br />
 N%_host<br />
 N%_sample </code></td>
<td>Percentile</td>
<td> True if at least <i>N</i> percent of set members are true in the associated dimension
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> The following instantial operators may be used to filter or limit a set-valued logical expression, based on regular expression matching of instance names. The logical expression must be a set involving the dimension of instances, and the regular expression is of the form used by <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1) or the Extended Regular Expressions of <code><a href="/docs/linux/man/3-regcomp/">regcomp</a></code>(3). </p>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center>Operators</td>
<td ALIGN=center>Explanation
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>match_inst</code></td>
<td> For each value of the logical expression that is &#8220;true&#8221;, the result is &#8220;true&#8221; if the associated instance name matches the regular expression. Otherwise the result is &#8220;false&#8221;.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>nomatch_inst</code></td>
<td> For each value of the logical expression that is &#8220;true&#8221;, the result is &#8220;true&#8221; if the associated instance name does <code>not</code> match the regular expression. Otherwise the result is &#8220;false&#8221;.
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> For example, the expression below will be &#8220;true&#8221; for disks attached to controllers 2 or 3 performing more than 20 operations per second: </p>
<pre>
match_inst &quot;^dks[23]d&quot; disk.dev.total &gt; 20;
</pre>
<p> The following aggregate operators map from an arithmetic expression to an arithmetic expression of lower dimension. </p>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center>Operators</td>
<td ALIGN=center>Type</td>
<td ALIGN=center>Explanation
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code> min_inst<br />
 min_host<br />
 min_sample </code></td>
<td>Extrema</td>
<td> Minimum value across all set members in the associated dimension
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code> max_inst<br />
 max_host<br />
 max_sample </code></td>
<td>Extrema</td>
<td> Maximum value across all set members in the associated dimension
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code> sum_inst<br />
 sum_host<br />
 sum_sample </code></td>
<td>Aggregate</td>
<td> Sum of values across all set members in the associated dimension
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code> avg_inst<br />
 avg_host<br />
 avg_sample </code></td>
<td>Aggregate</td>
<td> Average value across all set members in the associated dimension
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> The aggregate operators <tt>count_inst</tt>, <tt>count_host</tt> and <tt>count_sample</tt> map from a logical expression to an arithmetic expression of lower dimension by counting the number of set members for which the expression is true in the associated dimension. </p>
<p> For action rules, the following actions are defined: <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center>Operators</td>
<td ALIGN=center>Explanation
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>alarm</code></td>
<td>Raise a visible alarm with <code><a href="/docs/linux/man/1-xconfirm/">xconfirm</a></code>(1)
</td>
</tr>
<tr VALIGN=top>
<td><code>print</code></td>
<td>Display on standard output
</td>
</tr>
<tr VALIGN=top>
<td><code>shell</code></td>
<td>Execute with <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1)
</td>
</tr>
<tr VALIGN=top>
<td><code>stomp</code></td>
<td>Send a STOMP message to a JMS server
</td>
</tr>
<tr VALIGN=top>
<td><code>syslog</code></td>
<td>Append a message to system log file
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> Multiple actions may be separated by the <tt>&amp;</tt> and <tt>|</tt> operators to specify respectively sequential execution (both actions are executed) and alternate execution (the second action will only be executed if the execution of the first action returns a non-zero error status. </p>
<p> Arguments to actions are an optional suppression time, and then one or more expressions (a string is an expression in this context). Strings appearing as arguments to an action may include the following special selectors that will be replaced at the time the action is executed.</p>
<dl>
<dt>%h</p>
<dd> Host name(s) that make the left-most top-level expression in the condition true.</p>
<dt>%c</p>
<dd> Connection specification string(s) or files for a PCP tool to reach the hosts or archives that make the left-most top-level expression in the condition true.</p>
<dt>%i</p>
<dd> Instance(s) that make the left-most top-level expression in the condition true.</p>
<dt>%v</p>
<dd> One value from the left-most top-level expression in the condition for each host and instance pair that makes the condition true.</dl>
<p> Note that expansion of the special selectors is done by repeating the whole argument once for each unique binding to any of the qualifying special selectors. For example if a rule were true for the host <code>mumble</code> with instances <code>grunt</code> and <code>snort</code>, and for host <code>fumble</code> the instance <code>puff</code> makes the rule true, then the action </p>
<pre>
...
-&gt; shell myscript &quot;Warning: %h:%i busy &quot;;
</pre>
<p> will execute <code>myscript</code> with the argument string &quot;Warning: mumble:grunt busy Warning: mumble:snort busy Warning: fumble:puff busy&quot;. </p>
<p> By comparison, if the action </p>
<pre>
...
-&gt; shell myscript &quot;Warning! busy:&quot; &quot; %h:%i&quot;;
</pre>
<p> were executed under the same circumstances, then <code>myscript</code> would be executed with the argument string &quot;Warning! busy: mumble:grunt mumble:snort fumble:puff&quot;. </p>
<p> The semantics of the expansion of the special selectors leads to a common usage pattern in an action, where one argument is a constant (contains no special selectors) the second argument contains the desired special selectors with minimal separator characters, and an optional third argument provides a constant postscript (e.g. to terminate any argument quoting from the first argument). If necessary post-processing (eg. in <code>myscript</code>) can provide the necessary enumeration over each unique expansion of the string containing just the special selectors. </p>
<p> For complex conditions, the bindings to these selectors is not obvious. It is strongly recommended that <code>pmie</code> be used in the debugging mode (specify the <code>-W</code> command line option in particular) during rule development.</p>
<h2>BOOLEAN EXPRESSIONS</h2>
<p> <code>pmie</code> expressions that have the semantics of a Boolean, e.g. <tt>foo.bar &gt; 10</tt> or some_inst<tt> ( my.table &lt; 0 ) </tt> are assigned the values true or false or unknown. A value is unknown if one or more of the underlying metric values is unavailable, e.g. <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) on the host cannot be contacted, the metric is not in the PCP archive, no values are currently available, insufficient values have been fetched to allow a rate converted value to be computed or insufficient values have been fetched to instantiate the required number of samples in the temporal domain. </p>
<p> Boolean operators follow the normal rules of Kleene logic (aka 3-valued logic) when combining values that include unknown: <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center VALIGN=center COLSPAN=2 ROWSPAN=2>A and B</td>
<td ALIGN=center>B</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>true</td>
<td ALIGN=center>false</td>
<td ALIGN=center>unknown</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center VALIGN=center ROWSPAN=2>A</td>
<td ALIGN=center>true</td>
<td ALIGN=center>true</td>
<td ALIGN=center>false</td>
<td ALIGN=center>unknown
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>false</td>
<td ALIGN=center>false</td>
<td ALIGN=center>false</td>
<td ALIGN=center>false</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>unknown</td>
<td ALIGN=center>unknown</td>
<td ALIGN=center>false</td>
<td ALIGN=center>unknown</td>
</tr>
</table>
</table>
<p></center> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center VALIGN=center COLSPAN=2 ROWSPAN=2>A or B</td>
<td ALIGN=center>B</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>true</td>
<td ALIGN=center>false</td>
<td ALIGN=center>unknown</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center VALIGN=center ROWSPAN=2>A</td>
<td ALIGN=center>true</td>
<td ALIGN=center>true</td>
<td ALIGN=center>true</td>
<td ALIGN=center>true
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>false</td>
<td ALIGN=center>true</td>
<td ALIGN=center>false</td>
<td ALIGN=center>unknown</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>unknown</td>
<td ALIGN=center>true</td>
<td ALIGN=center>unknown</td>
<td ALIGN=center>unknown</td>
</tr>
</table>
</table>
<p></center> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center>A</td>
<td ALIGN=center>not A
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>true</td>
<td ALIGN=center>false
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>false</td>
<td ALIGN=center>true
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>unknown</td>
<td ALIGN=center>unknown
</td>
</tr>
</table>
</table>
<p></center></p>
<h2>RULESETS</h2>
<p> The ruleset clause is used to define a set of rules and actions that are evaluated in order until some action is executed, at which point the remaining rules and actions are skipped until the ruleset is again scheduled for evaluation. The keyword else is used to separate rules. After one or more regular rules (with a predicate and an action), a ruleset may include an optional </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> unknown -&gt; action<br />
 clause, optionally followed by a </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> otherwise -&gt; action<br />
 clause. </p>
<p> If all of the predicates in the rules evaluate to unknown and an unknown clause has been specified then action associated with the unknown clause will be executed. </p>
<p> If no rule predicate is true and the unknown action is either not specified or not executed and an otherwise clause has been specified, then the action associated with the otherwise clause will be executed.</p>
<h2>SCALE FACTORS</h2>
<p> Scale factors may be appended to arithmetic expressions and force linear scaling of the value to canonical units. Simple scale factors are constructed from the keywords: nanosecond, nanosec, nsec, microsecond, microsec, usec, millisecond, millisec, msec, second, sec, minute, min, hour, byte, Kbyte, Mbyte, Gbyte, Tbyte, count, Kcount and Mcount, and the operator <tt>/</tt>, for example &#8220;Kbytes / hour&#8221;.</p>
<h2>MACROS</h2>
<p> Macros are defined using expressions of the form: </p>
<p> <i>name</i> = <i>constexpr</i>; </p>
<p> Where <i>name</i> follows the normal rules for variables in programming languages, ie. alphabetic optionally followed by alphanumerics. <i>constexpr</i> must be a constant expression, either a string (enclosed in double quotes) or an arithmetic expression optionally followed by a scale factor. </p>
<p> Macros are expanded when their name, prefixed by a dollar (<tt>$</tt>) appears in an expression, and macros may be nested within a <i>constexpr</i> string. </p>
<p> The following reserved macro names are understood.</p>
<dl>
<dt>minute</p>
<dd> Current minute of the hour.</p>
<dt>hour</p>
<dd> Current hour of the day, in the range 0 to 23.</p>
<dt>day</p>
<dd> Current day of the month, in the range 1 to 31.</p>
<dt>month</p>
<dd> Current month of the year, in the range 0 (January) to 11 (December).</p>
<dt>year</p>
<dd> Current year.</p>
<dt>day_of_week</p>
<dd> Current day of the week, in the range 0 (Sunday) to 6 (Saturday).</p>
<dt>delta</p>
<dd> Sample interval in effect for this expression.</dl>
<p> Dates and times are presented in the reporting time zone (see description of <code>-Z</code> and <code>-z</code> command line options above).</p>
<h2>AUTOMATIC RESTART</h2>
<p> It is often useful for <code>pmie</code> processes to be started and stopped when the local host is booted or shutdown, or when they have been detected as no longer running (when they have unexpectedly exited for some reason). Refer to <code><a href="/docs/linux/man/1-pmie_check/">pmie_check</a></code>(1) for details on automating this process.</p>
<h2>EVENT MONITORING</h2>
<p> It is common for production systems to be monitored in a central location. Traditionally on UNIX systems this has been performed by the system log facilities &#8211; see <code><a href="/docs/linux/man/1-logger/">logger</a></code>(1), and <code><a href="/docs/linux/man/1-syslogd/">syslogd</a></code>(1). On Windows, communication with the system event log is handled by <code><a href="/docs/linux/man/1-pcp-eventlog/">pcp-eventlog</a></code>(1). </p>
<p> <code>pmie</code> fits into this model when rules use the <i>syslog</i> action. Note that if the action string begins with -p (priority) and/or -t (tag) then these are extracted from the string and treated in the same way as in <code><a href="/docs/linux/man/1-logger/">logger</a></code>(1) and <code><a href="/docs/linux/man/1-pcp-eventlog/">pcp-eventlog</a></code>(1). </p>
<p> However, it is common to have other event monitoring frameworks also, into which you may wish to incorporate performance events from <code>pmie</code>. You can often use the <i>shell</i> action to send events to these frameworks, as they usually provide their a program for injecting events into the framework from external sources. </p>
<p> A final option is use of the <i>stomp</i> (Streaming Text Oriented Messaging Protocol) action, which allows <code>pmie</code> to connect to a central JMS (Java Messaging System) server and send events to the PMIE topic. Tools can be written to extract these text messages and present them to operations people (via desktop popup windows, etc). Use of the <i>stomp</i> action requires a stomp configuration file to be setup, which specifies the location of the JMS server host, port number, and username/password. </p>
<p> The format of this file is as follows: </p>
<pre>
host=messages.sgi.com   # this is the JMS server (required)
port=61616              # and its listening here (required)
timeout=2               # seconds to wait for server (optional)
username=joe            # (required)
password=j03ST0MP       # (required)
topic=PMIE              # JMS topic for pmie messages (optional)
</pre>
<p> The timeout value specifies the time (in seconds) that <code>pmie</code> should wait for acknowledgements from the JMS server after sending a message (as required by the STOMP protocol). Note that on startup, <code>pmie</code> will wait indefinitely for a connection, and will not begin rule evaluation until that initial connection has been established. Should the connection to the JMS server be lost at any time while <code>pmie</code> is running, <code>pmie</code> will attempt to reconnect on each subsequent truthful evaluation of a rule with a <i>stomp</i> action, but not more than once per minute. This is to avoid contributing to network congestion. In this situation, where the STOMP connection to the JMS server has been severed, the <i>stomp</i> action will return a non-zero error value.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_DEMOS_DIR/pmie/</code><i>*</i></p>
<dd> annotated example rules</p>
<dt><code>$PCP_VAR_DIR/pmns/</code><i>*</i></p>
<dd> default PMNS specification files</p>
<dt><code>$PCP_TMP_DIR/pmie</code></p>
<dd> <code>pmie</code> maintains files in this directory to identify the running <code>pmie</code> instances and to export runtime information about each instance &#8211; this data forms the basis of the pmcd.pmie performance metrics</p>
<dt><code>$PCP_PMIECONTROL_PATH</code></p>
<dd> the default set of <code>pmie</code> instances to start at boot time &#8211; refer to <code><a href="/docs/linux/man/1-pmie_check/">pmie_check</a></code>(1) for details</dl>
<h2>BUGS</h2>
<p> The lexical scanner and parser will attempt to recover after an error in the input expressions. Parsing resumes after skipping input up to the next semi-colon (;), however during this skipping process the scanner is ignorant of comments and strings, so an embedded semi-colon may cause parsing to resume at an unexpected place. This behavior is largely benign, as until the initial syntax error is corrected, <code>pmie </code> will not attempt any expression evaluation.</p>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5). </p>
<p> When executing shell actions, <code>pmie</code> overrides two variables &#8211; IFS and PATH &#8211; in the environment of the child process. IFS is set to &quot;	
&quot;. The PATH is set to a combination of a default path for all platforms (&quot;/usr/sbin:/sbin:/usr/bin:/usr/sbin&quot;) and several configurable components. These are (in this order): <code>$PCP_BIN_DIR</code>, <code>$PCP_BINADM_DIR</code> and <code>$PCP_PLATFORM_PATHS</code>. </p>
<p> When executing popup alarm actions, <code>pmie</code> will use the value of <code>$PCP_XCONFIRM_PROG</code> as the visual notification program to run. This is typically set to <code><a href="/docs/linux/man/1-pmconfirm/">pmconfirm</a></code>(1), a cross-platform dialog box.</p>
<h2>UNIX SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-logger/">logger</a></code>(1).</p>
<h2>WINDOWS SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcp-eventlog/">pcp-eventlog</a></code>(1).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmconfirm/">pmconfirm</a></code>(1), <code><a href="/docs/linux/man/1-pmdumplog/">pmdumplog</a></code>(1), <code><a href="/docs/linux/man/1-pmieconf/">pmieconf</a></code>(1), <code><a href="/docs/linux/man/1-pmie_check/">pmie_check</a></code>(1), <code><a href="/docs/linux/man/1-pminfo/">pminfo</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/1-pmval/">pmval</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5).</p>
<h2>USER GUIDE</h2>
<p> For a more complete description of the <code>pmie</code> language, refer to the <code>Performance Co-Pilot Users and Administrators Guide</code>. This is available online from: </p>
<pre>
<a rel="nofollow" href="http://www.pcp.io/doc/pcp-users-and-administrators-guide.pdf">http://www.pcp.io/doc/pcp-users-and-administrators-guide.pdf</a>
</pre>
<h2>Index</h2>
