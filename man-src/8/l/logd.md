---
title: "logd(8)"
name: "logd"
section: "8"
letter: "l"
url: "/docs/linux/man/8-logd/"
description: "logd – job output logging daemon"
---

<p>logd &#8211; job output logging daemon</p>
<h2>Synopsis</h2>
<p><code>logd</code> [<i>OPTION</i>]&#8230;</p>
<h2>Description</h2>
<p><code>logd</code> is started by <code><a href="/docs/linux/man/8-init/">init</a></code>(8) to receive the output of jobs with <i>console logged</i> in their job definition, which is the default if no other <i>console</i> setting is given. </p>
<p> Output is timestamped and written, with the job name, to <i>/var/log/boot</i> or stored in memory until the file is writable.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;daemon</code></p>
<dd>Detaches from the terminal and runs in the background.</dl>
<h2>Startup</h2>
<p>To eliminate race conditions on startup, such as not being ready to receive connections when the first job is started, the following procedure is used. </p>
<p> Once ready to receive connections, <code>logd</code> raises the <i>SIGSTOP</i> signal, putting itself to sleep until continued by another process. </p>
<p> After starting <code>logd</code>, <code><a href="/docs/linux/man/8-init/">init</a></code>(8) waits for the process to stop if it hasn&#8217;t already, and then sends it the <i>SIGCONT</i> signal so that it can proceed. Only once this has happened, will <code><a href="/docs/linux/man/8-init/">init</a></code>(8) start other jobs. </p>
<p> When the <i>&#8211;daemon</i> option is given, this is not performed; instead <code>logd</code> will not detach from the console until it is listening on the socket.</p>
<h2>Socket Protocol</h2>
<p><code>logd</code> listens on a <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7) stream socket in the abstract namespace, bound to <i>/com/ubuntu/upstart/logd</i>. </p>
<p> <code><a href="/docs/linux/man/8-init/">init</a></code>(8) opens a new connection for each job that is to be logged, binding the socket to the standard input, output and error file descriptors for the job. </p>
<p> Before running the job, it sends the job name on the socket so that it can be logged along with the messages. This is sent as a <i>size_t</i> that contains the length of the name to read, followed by that many character bytes. The NULL terminator is not sent as part of the protocol, it is up to the receiver to add that if required. </p>
<p> Further information about the job, such as its description, can be obtained by opening an ordinary connection to the <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon and querying it using the name received.</p>
<h2>Author</h2>
<p>Written by Scott James Remnant.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs at <a rel="nofollow" href="https://launchpad.net/products/upstart/+bugs">https://launchpad.net/products/upstart/+bugs</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2006 Canonical Ltd.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-init/">init</a></code>(8) </p>
