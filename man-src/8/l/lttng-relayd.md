---
title: "lttng-relayd(8)"
name: "lttng-relayd"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lttng-relayd/"
description: "lttng-relayd — LTTng remote trace collection daemon"
---

<p>lttng-relayd &#8212; LTTng remote trace collection daemon</p>
<h2>Synopsis</h2>
<pre>lttng-relayd [OPTIONS]</pre>
<h2>Description</h2>
<p>The LTTng project aims at providing highly efficient tracing tools for Linux. It&#8217;s tracers help tracking down performance issues and debugging problems involving multiple concurrent processes and threads. Tracing across multiple systems is also possible. </p>
<p> The relay daemon listens by default on all network interfaces to gather trace data, but only on localhost for viewer connections. This daemon does not require any particular permissions as long as it can write in the output folder and listen on the ports. If a user is within a secured network and/or has proper firewall settings, lttng-relayd can listen to viewer connections from all network interfaces by specifying &#8216;-L <a href="tcp://0.0.0.0:5344'.">tcp://0.0.0.0:5344&#8242;.</a> </p>
<p> Traces can be either viewed &quot;live&quot; (as they are produced) by attaching to the live viewer port using LTTng live protocol, or after tracing has been stopped. Once a trace has been streamed completely, the trace can be processed by any tool that can process a local LTTng CTF trace. </p>
<p> By default, the relayd outputs the traces in : ~/lttng-traces/hostname/session-name/domain-name </p>
<p> The prefix (~/lttng-traces) can be configured on the relayd side (see below for the option), the other folders can be configured when creating the trace on the sessiond side.</p>
<h2>Options</h2>
<p>This program follow the usual GNU command line syntax with long options starting with two dashes. Below is a summary of the available options. </p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Show summary of possible options and commands</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Increase verbosity </p>
<p> There is three debugging level which will print on stderr. Maximum verbosity is <code>-vvv</code>.</p>
<dt><code>-d, &#8211;daemonize</code></p>
<dd>Start as a daemon</p>
<dt><code>-b, &#8211;background</code></p>
<dd>Start as a daemon, keeping console open</p>
<dt><code>-g, &#8211;group NAME</code></p>
<dd>Specify the tracing group name. (default: tracing)</p>
<dt><code>-C, &#8211;control-port</code></p>
<dd>Control port URL (<a href="tcp://0.0.0.0:5342">tcp://0.0.0.0:5342</a> is the default)</p>
<dt><code>-D, &#8211;data-port</code></p>
<dd>Data port URL (<a href="tcp://0.0.0.0:5343">tcp://0.0.0.0:5343</a> is the default)</p>
<dt><code>-L, &#8211;live-port URL</code></p>
<dd>Live view port URL (<a href="tcp://localhost:5344">tcp://localhost:5344</a> is the default).</p>
<dt><code>-o, &#8211;output</code></p>
<dd>Output base directory. Must use an absolute path (~/lttng-traces is the default)</p>
<dt><code>-V, &#8211;version</code></p>
<dd>Show version number</dl>
<h2>Environment Variables</h2>
<dl>
<dt>LTTNG_NETWORK_SOCKET_TIMEOUT</p>
<dd>Control timeout of socket connection, receive and send. Takes an integer parameter: the timeout value, in milliseconds. A value of 0 or -1 uses the timeout of the operating system (this is the default).</p>
<dt>LTTNG_RELAYD_HEALTH</p>
<dd>File path used for relay daemon health check communication.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-babeltrace/">babeltrace</a>(1), <a href="/docs/linux/man/8-lttng-sessiond/">lttng-sessiond</a>(8), <a href="/docs/linux/man/3-lttng-ust/">lttng-ust</a>(3), <a href="/docs/linux/man/1-lttng/">lttng</a>(1) </p>
<h2>Limitations</h2>
<p>For now only TCP is supported on both control and data port. Control will always remain TCP-only since it is low-volume and needs absolutely to be reliable, but eventually the data connection could support UDP. </p>
<p> For unprivileged user running lttng-relayd, the maximum number of file descriptors per process is usually 1024. This limits the number of connections and tracefiles opened. This limit can be configured see <a href="/docs/linux/man/3-ulimit/">ulimit</a>(3).</p>
<h2>Bugs</h2>
<p>No show stopper bugs are known yet in this version. </p>
<p> If you encounter any issues or usability problem, please report it on our mailing list &lt;lttng-dev [at] lists.lttng.org&gt; to help improve this project.</p>
<h2>Credits</h2>
<p>lttng-relayd is distributed under the GNU General Public License version 2. See the file COPYING for details. </p>
<p> A Web site is available at <a rel="nofollow" href="http://lttng.org">http://lttng.org</a> for more information on the LTTng project. </p>
<p> You can also find our git tree at <a rel="nofollow" href="http://git.lttng.org.">http://git.lttng.org.</a> </p>
<p> Mailing lists for support and development: &lt;lttng-dev [at] lists.lttng.org&gt;. </p>
<p> You can find us on IRC server irc.oftc.net (OFTC) in #lttng.</p>
<h2>Authors</h2>
<p>lttng-relay was originally written by Julien Desfossez and David Goulet. More people have since contributed to it. It is currently maintained by Julien Desfossez &lt;jdesfossez [at] efficios.com&gt;.</p>
