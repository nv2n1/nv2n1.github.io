---
title: "beanstalkd(1)"
name: "beanstalkd"
section: "1"
letter: "b"
url: "/docs/linux/man/1-beanstalkd/"
description: "beanstalkd – simple, fast work queue"
---

<h2>NAME</h2>
<p> <code>beanstalkd</code> &#8211; simple, fast work queue</p>
<h2>SYNOPSIS</h2>
<p> <code>beanstalkd</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Beanstalkd</code> is a simple work-queue service. Its interface is generic, though it was originally designed for reducing the latency of page views in high-volume web applications by running time-consuming tasks asynchronously. </p>
<p> When started, <code>beanstalkd</code> opens a socket (or uses a file descriptor provided by the <a href="/docs/linux/man/1-init/">init</a>(1) system, see <i>ENVIRONMENT</i>) and listens for incoming connections. For each connection, it reads a sequence of commands to create, reserve, delete, and otherwise manipulate &quot;jobs&quot;, units of work to be done. See file <code>doc/protocol.txt</code> in the <code>beanstalkd</code> distribution for a thorough description of the meaning and format of the <code>beanstalkd</code> protocol.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code> <i>path</i></p>
<dd> Use a binlog to keep jobs on persistent storage in directory <i>path</i>. Upon startup, <code>beanstalkd</code> will recover any binlog that is present in <i>path</i>, then, during normal operation, append new jobs and changes in state to the binlog.</p>
<dt><code>-c</code></p>
<dd> Perform online, incremental compaction of binlog files. Negates <code>-n</code>. This is the default behavior.</p>
<dt>
<dd> (Do not use this option, except to negate <code>-n</code>. Both <code>-c</code> and <code>-n</code> will likely be removed in a future <code>beanstalkd</code> release.)</p>
<dt><code>-f</code> <i>ms</i></p>
<dd> Call <a href="/docs/linux/man/2-fsync/">fsync</a>(2) at most once every <i>ms</i> milliseconds. Larger values for <i>ms</i> reduce disk activity and improve speed at the cost of safety. A power failure could result in the loss of up to <i>ms</i> milliseconds of history.</p>
<dt>
<dd> A <i>ms</i> value of 0 will cause <code>beanstalkd</code> to call fsync every time it writes to the binlog.</p>
<dt>
<dd> (This option has no effect without <code>-b</code>.)</p>
<dt><code>-F</code></p>
<dd> Never call <a href="/docs/linux/man/2-fsync/">fsync</a>(2). Equivalent to <code>-f</code> with an infinite <i>ms</i> value.</p>
<dt>
<dd> This is the default behavior.</p>
<dt>
<dd> (This option has no effect without <code>-b</code>.)</p>
<dt><code>-h</code></p>
<dd> Show a brief help message and exit.</p>
<dt><code>-l</code> <i>addr</i></p>
<dd> Listen on address <i>addr</i> (default is 0.0.0.0).</p>
<dt>
<dd> (Option <code>-l</code> has no effect if <a href="/docs/linux/man/5-sd-daemon/">sd-daemon</a>(5) socket activation is being used. See also <i>ENVIRONMENT</i>.)</p>
<dt><code>-n</code></p>
<dd> Turn off binlog compaction, negating <code>-c</code>.</p>
<dt>
<dd> (Do not use this option. Both <code>-c</code> and <code>-n</code> will likely be removed in a future <code>beanstalkd</code> release.)</p>
<dt><code>-p</code> <i>port</i></p>
<dd> Listen on TCP port <i>port</i> (default is 11300).</p>
<dt>
<dd> (Option <code>-p</code> has no effect if <a href="/docs/linux/man/5-sd-daemon/">sd-daemon</a>(5) socket activation is being used. See also <i>ENVIRONMENT</i>.)</p>
<dt><code>-s</code> <i>bytes</i></p>
<dd> The size in bytes of each binlog file.</p>
<dt>
<dd> (This option has no effect without <code>-b</code>.)</p>
<dt><code>-u</code> <i>user</i></p>
<dd> Become the user <i>user</i> and its primary group.</p>
<dt><code>-V</code></p>
<dd> Increase verbosity. May be used more than once to produce more verbose output. The output format is subject to change.</p>
<dt><code>-v</code></p>
<dd> Print the version string and exit.</p>
<dt><code>-z</code> <i>bytes</i></p>
<dd> The maximum size in bytes of a job.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>LISTEN_PID</code>, <code>LISTEN_FDS</code></p>
<dd> These variables can be set by <a href="/docs/linux/man/1-init/">init</a>(1). See <a href="/docs/linux/man/3-sd_listen_fds/">sd_listen_fds</a>(3) for details.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-sd-daemon/">sd-daemon</a>(5), <a href="/docs/linux/man/5-sd_listen_fds/">sd_listen_fds</a>(5) </p>
<p> Files <code>README</code> and <code>doc/protocol.txt</code> in the <code>beanstalkd</code> distribution. </p>
<p> <i><a rel="nofollow" href="http://kr.github.com/beanstalkd/">http://kr.github.com/beanstalkd/</a></i></p>
<h2>AUTHOR</h2>
<p> <code>Beanstalkd</code> is written and maintained by Keith Rarick with the help of many others. </p>
<h2>Index</h2>
