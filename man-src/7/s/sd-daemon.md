---
title: "sd-daemon(7)"
name: "sd-daemon"
section: "7"
letter: "s"
url: "/docs/linux/man/7-sd-daemon/"
description: "sd-daemon – Reference implementation of APIs for new-style daemons"
---

<p>sd-daemon &#8211; Reference implementation of APIs for new-style daemons</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;systemd/sd-daemon.h&gt;





pkg-config --cflags --libs libsystemd-daemon</code></pre>
<h2>Description</h2>
<dd>sd-daemon.c and sd-daemon.h provide a reference implementation of various APIs for new-style daemons, as implemented by the <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) init system. See <code><a href="/docs/linux/man/3-sd_listen_fds/">sd_listen_fds</a></code>(3), <code><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></code>(3), <code><a href="/docs/linux/man/3-sd_booted/">sd_booted</a></code>(3), <code><a href="/docs/linux/man/3-sd_is_fifo/">sd_is_fifo</a></code>(3) for more information about the functions implemented. In addition to these functions a couple of logging prefixes are defined as macros: fprintf(stderr, SD_NOTICE &quot;Hello World!
&quot;); These prefixes are intended to be used in conjunction with STDERR-based logging as implemented by systemd. If a systemd service definition file is configured with <i>StandardError=syslog</i> or <i>StandardError=kmsg</i> these prefixes can be used to encode a log level in lines printed. This is similar to the kernel <code>printk()</code>-style logging. See <code><a href="/docs/linux/man/2-klogctl/">klogctl</a></code>(2) for more information. The log levels are identical to <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3)&#8217;s log level system. To use these prefixes simply prefix every line with one of these strings. A line that is not prefixed will be logged at the default log level SD_INFO. <code>Example 1. Hello World</code> A daemon may log with the log level NOTICE by issuing this call: </p>
<pre><code>fprintf(stderr, SD_NOTICE &quot;Hello World!
&quot;);</code></pre>
<h2>Notes</h2>
<p>These interfaces are provided by the reference implementation of APIs for new-style daemons and distributed with the systemd package. The algorithms they implement are simple, and can easily be reimplemented in daemons if it is important to support this interface without using the reference implementation. See the respective function man pages for details. </p>
<p> In addition, for details about the algorithms check the liberally licensed reference implementation sources: m[blue]<code><a rel="nofollow" href="http://cgit.freedesktop.org/systemd/systemd/plain/src/sd-daemon.c">http://cgit.freedesktop.org/systemd/systemd/plain/src/sd-daemon.c</a></code>m[] resp. m[blue]<code><a rel="nofollow" href="http://cgit.freedesktop.org/systemd/systemd/plain/src/systemd/sd-daemon.h">http://cgit.freedesktop.org/systemd/systemd/plain/src/systemd/sd-daemon.h</a></code>m[] </p>
<p> These APIs are implemented in the reference implementation&#8217;s sd-daemon.c and sd-daemon.h files. These interfaces are available as shared library, which can be compiled and linked to with the libsystemd-daemon <code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file. Alternatively, applications consuming these APIs may copy the implementation into their source tree, either verbatim or in excerpts. </p>
<p> The functions directly related to new-style daemons become NOPs when -DDISABLE_SYSTEMD is set during compilation and the reference implementation is used as drop-in files. In addition, if sd-daemon.c is compiled on non-Linux systems they become NOPs.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd_listen_fds/">sd_listen_fds</a></code>(3), <code><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></code>(3), <code><a href="/docs/linux/man/3-sd_booted/">sd_booted</a></code>(3), <code><a href="/docs/linux/man/3-sd_is_fifo/">sd_is_fifo</a></code>(3), <code><a href="/docs/linux/man/7-daemon/">daemon</a></code>(7), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/5-systemd-socket/">systemd.socket</a></code>(5), <code><a href="/docs/linux/man/3-fprintf/">fprintf</a></code>(3), <code><a href="/docs/linux/man/7-sd-readahead/">sd-readahead</a></code>(7), <code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1)</p>
<h2>Author</h2>
<p><code>Lennart Poettering</code> &lt;lennart [at] poettering.net&gt;</p>
<dl>
<dd>Developer</dl>
