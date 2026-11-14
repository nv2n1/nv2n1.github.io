---
title: "perfalloc(1)"
name: "perfalloc"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perfalloc/"
description: "perfalloc – notify pmdaperfevent(1) to disable hardware counter allocation."
---

<h2>NAME</h2>
<p> <code>perfalloc</code> &#8211; notify <code><a href="/docs/linux/man/1-pmdaperfevent/">pmdaperfevent</a></code>(1) to disable hardware counter allocation.</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_PMDAS_DIR/perfevent/perfalloc</code> [<code>-D</code>] [<code>-d</code>] [<code>-f</code> <i>lockfile</i>] [<code>-h</code>] [<code>-v</code>] [<code>COMMAND</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>perfalloc</code> is a command that notifies the <code><a href="/docs/linux/man/1-pmdaperfevent/">pmdaperfevent</a></code>(1) to disable hardware counter event collection. This allow unprivileged processes to use the hardware counters. </p>
<p> If the reservation request fails, then perfalloc exits immediately with exit code EXIT_FAILURE. If successful, the perfalloc will run until a kill signal is received. The reservation request persists while perfalloc is running. </p>
<p> Note that <code>pmdaperfevent</code> is affected by the value of the <i>kernel.perf_event_paranoid</i> setting, which can be adjusted by <code><a href="/docs/linux/man/8-sysctl/">sysctl</a></code>(8). </p>
<p> If a commandline is given, this is executed as a subprocess of the agent. When the command dies, so does the agent. </p>
<p> A brief description of the command line options follows:</p>
<dl>
<dt><code>-D</code></p>
<dd> run in the foreground (the default)</p>
<dt><code>-d</code></p>
<dd> run in the background</p>
<dt><code>-f FILE</code></p>
<dd> use FILE as the lock file (default $PCP_PMDAS_DIR/perfevent/perflock)</p>
<dt><code>-h</code></p>
<dd> display a help message and exit</p>
<dt><code>-v</code></p>
<dd> output version number and exit</dl>
<h2>BUGS</h2>
<p> There may be a delay of up to 100 miliseconds between perfalloc requesting the hardware counter disabling and the perfevent pmda processing the request. </p>
<p> The perfalloc process does not check the status of the request and therefore is not able to provide a positive confirmation that the request succeeded and the hardware counters are disabled.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmdaperfevent/">pmdaperfevent</a></code>(1), <code><a href="/docs/linux/man/3-perfevent-conf/">perfevent.conf</a></code>(3) and <code><a href="/docs/linux/man/8-sysctl/">sysctl</a></code>(8). </p>
<h2>Index</h2>
