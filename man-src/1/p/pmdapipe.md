---
title: "pmdapipe(1)"
name: "pmdapipe"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdapipe/"
description: "pmdapipe – command output capture performance metrics domain agent (PMDA)"
---

<h2>NAME</h2>
<p> <code>pmdapipe</code> &#8211; command output capture performance metrics domain agent (PMDA)</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_PMDAS_DIR/pipe/pmdapipe</code> [<code>-c</code> <i>configfile</i>] [<code>-d</code> <i>domain</i>] [<code>-l</code> <i>logfile</i>] [<code>-m</code> <i>memory</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdapipe</code> is a configurable command output monitoring Performance Metrics Domain Agent (PMDA). It can be seen as analogous to a restricted shell, where options can be passed to preset commands, and each line of their output is converted into a performance event. These events can be consumed by client tools like <code><a href="/docs/linux/man/1-pmval/">pmval</a></code>(1). </p>
<p> The <code>pipe</code> PMDA exports both event-style metrics reflecting timestamped event records for text-oriented command output, as well as the more orthodox sample-style metrics such as event counts and throughput size values. </p>
<p> The PMDA is configured via a <i>configfile</i> which contains one line for each process from which output can be captured, as described in the &#8220;CONFIGURATION&#8221; section below. </p>
<p> A brief description of the <code>pmdapipe</code> command line options follows:</p>
<dl>
<dt><code>-c</code></p>
<dd> specifies an alternate configuration file for the PMDA. By default, a file named <i>$PCP_PMDAS_DIR/pipe/pipe.conf</i> and any files below the <i>$PCP_SYSCONF_DIR/pipe.conf.d/</i> directory are used.</p>
<dt><code>-d</code></p>
<dd> It is absolutely crucial that the performance metrics <i>domain</i> number specified here is unique and consistent. That is, <i>domain</i> should be different for every PMDA on the one host, and the same <i>domain</i> number should be used for the same PMDA on all hosts.</p>
<dt><code>-l</code></p>
<dd> Location of the log file. By default, a log file named <i>pipe.log</i> is written in the current directory of <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when <code>pmdapipe</code> is started, i.e. <code>$PCP_LOG_DIR/pmcd</code>. If the log file cannot be created or is not writable, output is written to the standard error instead.</p>
<dt><code>-m</code></p>
<dd> Limit the physical memory used by the PMDA to buffer event records to <i>maxsize</i> bytes. As log events arrive at the PMDA, they must be buffered until individual client tools request the next batch since their previous batch of events. The default maximum is 2 megabytes.</dl>
<h2>CONFIGURATION</h2>
<p> The set of allowed pipe commands is configured by simple text file(s). The format is a single line for each command followed by an optional access control section. </p>
<p> Blank lines and comments are permitted (even encouraged) in the configuration file. A comment begins with a &#8220;#&#8221; character and finishes at the end of the line. </p>
<p> Each command configuration line is of the form:</p>
<dl>
<dt>
<dd> <i>instance</i> <i>username</i> <i>command</i> <i>options</i></dl>
<p> Where,</p>
<dl>
<dt>
<dd> <i>instance</i> is a string identifying the pipe command, also exported as the metric instance identifier.</dl>
<dl>
<dt><i>username</i></p>
<dd> is the name of the user account under which the command should run (e.g. &quot;root&quot;)</dl>
<dl>
<dt><i>command</i></p>
<dd> is the path to the binary which will be run to generate piped output</dl>
<dl>
<dt><i>options</i></p>
<dd> is an optional space-separated list of parameters to pass to the <i>command</i></p>
<dt>
<dd> This <i>options</i> list may contain numeric parameters prefixed by the dollar-sign, and these will be substituted with user-supplied values at the time the <i>command</i> is run (similar to shell parameter substitution).</dl>
<p> Parameters are passed as a single space-separated or comma-separated string to the <i>pipe.firehose</i> metric, using the <code>pmStore (3)</code> interface. The <code>pmval</code> command provides store access via its <code>-x</code> option. User-supplied parameters are restricted to containing alphanumeric characters. </p>
<p> The access control section of the file must start with a line of the form:</p>
<dl>
<dt><code>[access]</code></p>
<dd></dl>
<p> Leading and trailing whitespace may appear around and within the brackets and the case of the <code>access</code> keyword is ignored. No other text may appear on the line except a trailing comment. </p>
<p> Following this line, the remainder of the configuration file should contain lines that allow or disallow use of <i>commands</i> from particular users or groups. </p>
<p> User names and group names will be verified using the local <code>/etc/passwd</code> and <code>/etc/groups</code> files (or an alternative directory service), using the <code><a href="/docs/linux/man/3-getpwent/">getpwent</a></code>(3) and <code><a href="/docs/linux/man/3-getgrent/">getgrent</a></code>(3) routines. </p>
<p> Access for users or groups are allowed or disallowed by specifying statements of the form:</p>
<dl>
<dt>
<dd> <code>allow user</code> <i>username</i> <code>:</code> <i>instance</i><br />
 <code>disallow user</code> <i>username</i> <code>:</code> <i>instance</i><br />
 <code>allow group</code> <i>groupname</i> <code>:</code> <i>instance</i><br />
 <code>disallow group</code> <i>groupname</i> <code>:</code> <i>instance</i></dl>
<p> The <i>username</i> and <i>groupname</i> names will be verified using the local <code>/etc/passwd</code> and <code>/etc/groups</code> files (or an alternative directory service), using the <code><a href="/docs/linux/man/3-getpwent/">getpwent</a></code>(3) and <code><a href="/docs/linux/man/3-getgrent/">getgrent</a></code>(3) routines. </p>
<p> The wildcard &#8220;*&#8221; can be used to refer to all <i>instance</i> names.</p>
<h2>INSTALLATION</h2>
<p> If you want access to the names, help text and values for the pipe performance metrics, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/pipe
# ./Install
</pre>
<p> This is an interactive installation process which prompts for each log file path to be monitored (or command to be run), a metric instance name to identify it, and whether access should be restricted (refer to the <code>-x</code> option to <code><a href="/docs/linux/man/1-pmval/">pmval</a></code>(1) for further details). </p>
<p> If you want to undo the installation, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/pipe
# ./Remove
</pre>
<p> <code>pmdapipe</code> is launched by <code>pmcd</code> and should never be executed directly. The Install and Remove scripts notify <code>pmcd</code> when the agent is installed or removed.</p>
<h2>EXAMPLES</h2>
<p> Following is a simple example of <code>pmdapipe</code> configuration and use of the pipe metrics to run the <code>btrace</code> command, by user <code>bob</code>: </p>
<pre><code>
bob &gt; cat $PCP_PMDAS_DIR / pipe / pipe.conf
#instance user command
                                      rw_syscalls root perf script rw -
          by - file $1 bdev_trace root btrace - w $1 / dev / $2[access] allow user bob : *;
allow user jane : bdev_trace;
allow group perf : rw_syscalls;
bob &gt; pmval - i bdev_trace - x '5 sda' pipe.firehose 8, 2 5 1 0.000000000 25227 A WS 734332384 + 24 &lt; -(253, 2)734330336 8, 0 5 2 0.000000414 25227 A WS 735358432 + 24 &lt; -(8, 2)734332384 8, 0 5 3 0.000000756 25227 Q WS 735358432 + 24 [qemu - kvm][... 5 seconds worth] bob &gt;
</code></pre>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMCDCONF_PATH</code></p>
<dd> command line options used to launch <code>pmdapipe</code></p>
<dt><code>$PCP_PMDAS_DIR/pipe/pipe.conf</code></p>
<dd> default configuration file for the pipe metrics</p>
<dt><code>$PCP_PMDAS_DIR/pipe/help</code></p>
<dd> default help text file for the pipe metrics</p>
<dt><code>$PCP_PMDAS_DIR/pipe/Install</code></p>
<dd> installation script for the <code>pmdapipe</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/pipe/Remove</code></p>
<dd> undo installation script for the <code>pmdapipe</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/pipe.log</code></p>
<dd> default log file for error messages and other information from <code>pmdapipe</code></p>
<dt><code>$PCP_SYSCONF_DIR/pipe.conf.d</code></p>
<dd> directory containing additional configuration files for the pipe metrics</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmval/">pmval</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/3-getpwent/">getpwent</a></code>(3), <code><a href="/docs/linux/man/3-getgrent/">getgrent</a></code>(3), <code><a href="/docs/linux/man/3-pmstore/">pmStore</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
