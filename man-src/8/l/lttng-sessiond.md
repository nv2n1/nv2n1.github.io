---
title: "lttng-sessiond(8)"
name: "lttng-sessiond"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lttng-sessiond/"
description: "lttng-sessiond — LTTng 2.x central tracing registry session daemon."
---

<p>lttng-sessiond &#8212; LTTng 2.x central tracing registry session daemon.</p>
<h2>Synopsis</h2>
<pre>lttng-sessiond [OPTIONS]</pre>
<h2>Description</h2>
<p>The LTTng project aims at providing highly efficient tracing tools for Linux. It&#8217;s tracers help tracking down performance issues and debugging problems involving multiple concurrent processes and threads. Tracing across multiple systems is also possible. </p>
<p> The session daemon, acting as a tracing registry, allow you to interact with multiple tracers (kernel and user-space) inside the same container, a tracing session. Trace can be gathered from the kernel and/or instrumented applications (<a href="/docs/linux/man/3-lttng-ust/">lttng-ust</a>(3)). Aggregating those traces is done using a viewer, like the <a href="/docs/linux/man/1-babeltrace/">babeltrace</a>(1) text viewer. </p>
<p> In order to trace the kernel, the session daemon needs to be running as root. LTTng provides the use of a <code>tracing group</code> (default: tracing). Whomever is in that group can interact with the root session daemon and thus trace the kernel. Session daemons can co-exist meaning that you can have a session daemon running as Alice that can be used to trace her applications along side with a root daemon or even a Bob daemon. We highly recommend to start the session daemon at boot time for stable and long term tracing. </p>
<p> The session daemon is in charge of managing trace data consumers by spawning them when the time has come. The user don&#8217;t need to manage the lttng-consumerd.</p>
<h2>Options</h2>
<p>This program follow the usual GNU command line syntax with long options starting with two dashes. Below is a summary of the available options. </p>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd>Show summary of possible options and commands</dd>
<dt><code>-v, &#8211;verbose</code></dt>
<dd>Increase verbosity </dd>
<p> There is three debugging level which will print on stderr. Maximum verbosity is <code>-vvv</code>.</p>
<dt><code> &#8211;verbose-consumer</code></dt>
<dd>Verbose mode for consumer. Activate DBG() macro.</dd>
<dt><code>-d, &#8211;daemonize</code></dt>
<dd>Start as a daemon</dd>
<dt><code>-b, &#8211;background</code></dt>
<dd>Start as a daemon, keeping console open</dd>
<dt><code>-g, &#8211;group=NAME</code></dt>
<dd>Specify the tracing group name. (default: tracing)</dd>
<dt><code>-V, &#8211;version</code></dt>
<dd>Show version number</dd>
<dt><code>-S, &#8211;sig-parent</code></dt>
<dd>Send SIGUSR1 to parent pid to notify readiness. </dd>
<p> This is used by <code><a href="/docs/linux/man/1-lttng/">lttng</a>(1)</code> to get notified when the session daemon is ready to accept command. When building a third party tool over liblttng-ctl, this option can be very handy to synchronize the control tool and the session daemon.</p>
<dt><code>-q, &#8211;quiet</code></dt>
<dd>No output at all.</dd>
<dt><code> &#8211;no-kernel</code></dt>
<dd>No kernel tracer support</dd>
<dt><code> &#8211;jul-tcp-port</code></dt>
<dd>JUL application registration TCP port (default: 5345)</dd>
<dt><code>-c, &#8211;client-sock=PATH</code></dt>
<dd>Specify path for the client unix socket</dd>
<dt><code>-a, &#8211;apps-sock PATH</code></dt>
<dd>Specify path for apps unix socket</dd>
<dt><code> &#8211;kconsumerd-err-sock=PATH</code></dt>
<dd>Specify path for the kernel consumer error socket</dd>
<dt><code> &#8211;kconsumerd-cmd-sock=PATH</code></dt>
<dd>Specify path for the kernel consumer command socket</dd>
<dt><code> &#8211;ustconsumerd32-err-sock=PATH</code></dt>
<dd>Specify path for the 32-bit UST consumer error socket</dd>
<dt><code> &#8211;ustconsumerd64-err-sock=PATH</code></dt>
<dd>Specify path for the 64-bit UST consumer error socket</dd>
<dt><code> &#8211;ustconsumerd32-cmd-sock=PATH</code></dt>
<dd>Specify path for the 32-bit UST consumer command socket</dd>
<dt><code> &#8211;ustconsumerd64-cmd-sock=PATH</code></dt>
<dd>Specify path for the 64-bit UST consumer command socket</dd>
<dt><code> &#8211;consumerd32-path=PATH</code></dt>
<dd>Specify path for the 32-bit UST consumer daemon binary</dd>
<dt><code> &#8211;consumerd32-libdir=PATH</code></dt>
<dd>Specify path for the 32-bit UST consumer daemon libraries</dd>
<dt><code> &#8211;consumerd64-path=PATH</code></dt>
<dd>Specify path for the 64-bit UST consumer daemon binary</dd>
<dt><code> &#8211;consumerd64-libdir=PATH</code></dt>
<dd>Specify path for the 64-bit UST consumer daemon libraries</dd></dl>
<h2>Environment Variables</h2>
<p>Note that all command line options will override environment variables. </p>
<dl>
<dt>LTTNG_CONSUMERD32_BIN</dt>
<dd>Specify the 32-bit consumer binary path. <code>&#8211;consumerd32-path</code> override this variable.</dd>
<dt>LTTNG_CONSUMERD64_BIN</dt>
<dd>Specify the 64-bit consumer binary path. <code>&#8211;consumerd64-path</code> override this variable.</dd>
<dt>LTTNG_CONSUMERD32_LIBDIR</dt>
<dd>Specifiy the 64-bit library path containing libconsumer.so. <code>&#8211;consumerd32-libdir</code> override this variable.</dd>
<dt>LTTNG_CONSUMERD64_LIBDIR</dt>
<dd>Specifiy the 32-bit library path containing libconsumer.so. <code>&#8211;consumerd64-libdir</code> override this variable.</dd>
<dt>LTTNG_DEBUG_NOCLONE</dt>
<dd>Debug-mode disabling use of clone/fork. Insecure, but required to allow debuggers to work with sessiond on some operating systems.</dd>
<dt>LTTNG_APP_SOCKET_TIMEOUT</dt>
<dd>Control the timeout of application&#8217;s socket when sending and receiving commands. Takes an integer parameter: the timeout value, in seconds. After this period of time, the application is unregistered by the session daemon. A value of 0 or -1 means an infinite timeout. Default value is 5 seconds.</dd>
<dt>LTTNG_NETWORK_SOCKET_TIMEOUT</dt>
<dd>Control timeout of socket connection, receive and send. Takes an integer parameter: the timeout value, in milliseconds. A value of 0 or -1 uses the timeout of the operating system (this is the default).</dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-babeltrace/">babeltrace</a>(1), <a href="/docs/linux/man/3-lttng-ust/">lttng-ust</a>(3), <a href="/docs/linux/man/1-lttng/">lttng</a>(1) </p>
<h2>Limitations</h2>
<p>For unprivileged user running lttng-sessiond, the maximum number of file descriptors per process is usually 1024. This limits the number of traceable applications since for each instrumented application there is two file descriptors per-CPU and one more socktet for bidirectional communication. </p>
<p> For the root user, the limit is bumped to 65535. Future version will deal with this limitation.</p>
<h2>Bugs</h2>
<p>No show stopper bugs are known yet in this version. </p>
<p> If you encounter any issues or usability problem, please report it on our mailing list &lt;lttng-dev [at] lists.lttng.org&gt; to help improve this project.</p>
<h2>Credits</h2>
<p>lttng-sessiond is distributed under the GNU General Public License version 2. See the file COPYING for details. </p>
<p> A Web site is available at <a rel="nofollow" href="http://lttng.org">http://lttng.org</a> for more information on the LTTng project. </p>
<p> You can also find our git tree at <a rel="nofollow" href="http://git.lttng.org.">http://git.lttng.org.</a> </p>
<p> Mailing lists for support and development: &lt;lttng-dev [at] lists.lttng.org&gt;. </p>
<p> You can find us on IRC server irc.oftc.net (OFTC) in #lttng.</p>
<h2>Thanks</h2>
<p>Thanks to Yannick Brosseau without whom this project would never have been so lean and mean! Also thanks to the Ericsson teams working on tracing which helped us greatly with detailed bug reports and unusual test cases. </p>
<p> Thanks to our beloved packager Alexandre Montplaisir-Goncalves (Ubuntu and PPA maintainer) and Jon Bernard for our Debian packages. </p>
<p> Special thanks to Michel Dagenais and the DORSAL laboratory at Polytechnique de Montreal for the LTTng journey.</p>
<h2>Authors</h2>
<p>lttng-tools was originally written by Mathieu Desnoyers, Julien Desfossez and David Goulet. More people have since contributed to it. It is currently maintained by David Goulet &lt;dgoulet [at] efficios.com&gt;.</p>
