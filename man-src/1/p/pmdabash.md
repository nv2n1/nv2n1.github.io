---
title: "pmdabash(1)"
name: "pmdabash"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdabash/"
description: "pmdabash – Bourne-Again SHell trace performance metrics domain agent"
---

<h2>NAME</h2>
<p> <code>pmdabash</code> &#8211; Bourne-Again SHell trace performance metrics domain agent</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_PMDAS_DIR/bash/pmdabash</code> [<code>-C</code>] [<code>-d</code> <i>domain</i>] [<code>-l</code> <i>logfile</i>] [<code>-I</code> <i>interval</i>] [<code>-t</code> <i>timeout</i>] [<code>-U</code> <i>username</i>] <i>configfile</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>pmdabash</code> is an experimental Performance Metrics Domain Agent (PMDA) which exports &quot;xtrace&quot; events from a traced <code><a href="/docs/linux/man/1-bash/">bash</a></code>(1) process. This includes the command execution information that would usually be sent to standard error with the <code>set -x</code> option to the shell. </p>
<p> Event metrics are exported showing each command executed, the function name and line number in the script, and a timestamp. Additionally, the process identifier for the shell and its parent process are exported. </p>
<p> This requires <code>bash</code> version 4 or later. </p>
<p> A brief description of the <code>pmdabash</code> command line options follows:</p>
<dl>
<dt><code>-d</code></p>
<dd> It is absolutely crucial that the performance metrics <i>domain</i> number specified here is unique and consistent. That is, <i>domain</i> should be different for every PMDA on the one host, and the same <i>domain</i> number should be used for the same PMDA on all hosts.</p>
<dt><code>-l</code></p>
<dd> Location of the log file. By default, a log file named <i>bash.log</i> is written in the current directory of <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when <code>pmdabash</code> is started, i.e. <code>$PCP_LOG_DIR/pmcd</code>. If the log file cannot be created or is not writable, output is written to the standard error instead.</p>
<dt><code>-s</code></p>
<dd> Amount of time (in seconds) between subsequent evaluations of the shell trace file descriptor(s). The default is 2 seconds.</dl>
<dl>
<dt><code>-m</code></p>
<dd> Maximum amount of memory to be allowed for each event queue (one per traced process). The default is 2 megabytes.</p>
<dt><code>-U</code></p>
<dd> User account under which to run the agent. The default is the unprivileged &quot;pcp&quot; account in current versions of PCP, but in older versions the superuser account (&quot;root&quot;) was used by default.</dl>
<h2>INSTALLATION</h2>
<p> In order for a host to export the names, help text and values for the bash performance metrics, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/bash
# ./Install
</pre>
<p> As soon as an instrumented shell script (see INSTRUMENTATION selection below) is run, with tracing enabled, new metric values will appear &#8211; no further setup of the agent is required. </p>
<p> If you want to undo the installation, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/bash
# ./Remove
</pre>
<p> <code>pmdabash</code> is launched by <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and should never be executed directly. The Install and Remove scripts notify <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when the agent is installed or removed.</p>
<h2>INSTRUMENTATION</h2>
<p> In order to allow the flow of event data between a <code><a href="/docs/linux/man/1-bash/">bash</a></code>(1) script and <code>pmdabash</code>, the script should take the following actions: </p>
<pre>
#!/bin/sh
source $PCP_DIR/etc/pcp.sh
pcp_trace on $@       # enable tracing
echo &quot;awoke, $count&quot;
pcp_trace off         # disable tracing
</pre>
<p> The tracing can be enabled and disabled any number of times by the script. On successful installation of the agent, several metrics will be available: </p>
<pre>
$ pminfo bash
bash.xtrace.numclients
bash.xtrace.maxmem
bash.xtrace.queuemem
bash.xtrace.count
bash.xtrace.records
bash.xtrace.parameters.pid
bash.xtrace.parameters.parent
bash.xtrace.parameters.lineno
bash.xtrace.parameters.function
bash.xtrace.parameters.command
</pre>
<p> When an instrumented script is running, the generation of event records can be verified using the <code><a href="/docs/linux/man/1-pmevent/">pmevent</a></code>(1) command, as follows: </p>
<pre><code>
$ pmevent - t 1 - x '' bash.xtrace.records host : localhost samples : all bash.xtrace.records["4538 ./test-trace.sh 1 2 3"] : 5 event records 10 : 00 : 05.000 -- -event record[0] flags 0x19(point, id, parent)-- -
    bash.xtrace.parameters.pid 4538 bash.xtrace.parameters.parent 4432 bash.xtrace.parameters.lineno 43 bash.xtrace.parameters.command "true" 10 : 00 : 05.000 -- -event record[1] flags 0x19(point, id, parent)-- -
    bash.xtrace.parameters.pid 4538 bash.xtrace.parameters.parent 4432 bash.xtrace.parameters.lineno 45 bash.xtrace.parameters.command "((  count++  ))" 10 : 00 : 05.000 -- -event record[2] flags 0x19(point, id, parent)-- -
    bash.xtrace.parameters.pid 4538 bash.xtrace.parameters.parent 4432 bash.xtrace.parameters.lineno 46 bash.xtrace.parameters.command "echo 'awoke, 3'" 10 : 00 : 05.000 -- -event record[3] flags 0x19(point, id, parent)-- -
    bash.xtrace.parameters.pid 4538 bash.xtrace.parameters.parent 4432 bash.xtrace.parameters.lineno 47 bash.xtrace.parameters.command "tired 2" 10 : 00 : 05.000 -- -event record[4] flags 0x19(point, id, parent)-- -
    bash.xtrace.parameters.pid 4538 bash.xtrace.parameters.parent 4432 bash.xtrace.parameters.lineno 38 bash.xtrace.parameters.function "tired" bash.xtrace.parameters.command "sleep 2"
</code></pre>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMCDCONF_PATH</code></p>
<dd> command line options used to launch <code>pmdabash</code></p>
<dt><code>$PCP_PMDAS_DIR/bash/help</code></p>
<dd> default help text file for the bash metrics</p>
<dt><code>$PCP_PMDAS_DIR/bash/Install</code></p>
<dd> installation script for the <code>pmdabash</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/bash/Remove</code></p>
<dd> undo installation script for <code>pmdabash</code></p>
<dt><code>$PCP_LOG_DIR/pmcd/bash.log</code></p>
<dd> default log file for error messages and other information from <code>pmdabash</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-bash/">bash</a></code>(1), <code><a href="/docs/linux/man/1-pmevent/">pmevent</a></code>(1) and <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1). </p>
<h2>Index</h2>
