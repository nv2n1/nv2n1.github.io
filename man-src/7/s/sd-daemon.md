---
title: "sd-daemon(7)"
name: "sd-daemon"
section: "7"
letter: "s"
url: "/docs/linux/man/7-sd-daemon/"
description: "sd-daemon – Reference implementation of APIs for new-style daemons"
---
<p>sd-daemon &#8211; Reference implementation of APIs for new-style daemons </p>
<h2>SYNOPSIS</h2>
<pre><code>#include &lt;systemd/sd-daemon.h&gt;
</code></pre>
<dl>
<dt><code>pkg-config --cflags --libs libsystemd-daemon</code></dt>
</dl>
<h2>DESCRIPTION</h2>
<dd> <p> sd-daemon.c and sd-daemon.h provide a reference implementation of various APIs for new-style daemons, as implemented by the <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) init system. </p>
<p>See <code><a href="/docs/linux/man/3-sd_listen_fds/">sd_listen_fds</a></code>(3), <code><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></code>(3), <code><a href="/docs/linux/man/3-sd_booted/">sd_booted</a></code>(3), <code><a href="/docs/linux/man/3-sd_is_fifo/">sd_is_fifo</a></code>(3) for more information about the functions implemented. In addition to these functions a couple of logging prefixes are defined as macros: </p>
 </dd>
<dl>
<dd> <pre><code>#define SD_EMERG &quot;&lt;0&gt;&quot; /* system is unusable */
#define SD_ALERT &quot;&lt;1&gt;&quot; /* action must be taken immediately */
#define SD_CRIT &quot;&lt;2&gt;&quot; /* critical conditions */
#define SD_ERR &quot;&lt;3&gt;&quot; /* error conditions */
#define SD_WARNING &quot;&lt;4&gt;&quot; /* warning conditions */
#define SD_NOTICE &quot;&lt;5&gt;&quot; /* normal but significant condition */
#define SD_INFO &quot;&lt;6&gt;&quot; /* informational */
#define SD_DEBUG &quot;&lt;7&gt;&quot; /* debug-level messages */
</code></pre>
 </dd></dl>
<p>These prefixes are intended to be used in conjunction with STDERR-based logging as implemented by systemd. If a systemd service definition file is configured with <i>StandardError=syslog</i> or <i>StandardError=kmsg</i> these prefixes can be used to encode a log level in lines printed. This is similar to the kernel <code>printk()</code>-style logging. See <code>klogctl</code>(2) for more information. </p>
<p>The log levels are identical to <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3)&#8216;s log level system. To use these prefixes simply prefix every line with one of these strings. A line that is not prefixed will be logged at the default log level SD_INFO. </p>
<p> <code>Example 1. Hello World</code> </p>
<p>A daemon may log with the log level NOTICE by issuing this call: </p>
<dl>
<dd> <pre><code>fprintf(stderr, SD_NOTICE &quot;Hello World!\n&quot;);
</code></pre>
 </dd></dl>
<h2>NOTES</h2>
<p>These interfaces are provided by the reference implementation of APIs for new-style daemons and distributed with the systemd package. The algorithms they implement are simple, and can easily be reimplemented in daemons if it is important to support this interface without using the reference implementation. See the respective function man pages for details. </p>
<p>In addition, for details about the algorithms check the liberally licensed reference implementation sources: m[blue]<code><a rel="nofollow" href="http://cgit.freedesktop.org/systemd/systemd/plain/src/sd-daemon.c">http://cgit.freedesktop.org/systemd/systemd/plain/src/sd-daemon.c</a></code>m[] resp. m[blue]<code><a rel="nofollow" href="http://cgit.freedesktop.org/systemd/systemd/plain/src/systemd/sd-daemon.h">http://cgit.freedesktop.org/systemd/systemd/plain/src/systemd/sd-daemon.h</a></code>m[] </p>
<p>These APIs are implemented in the reference implementation&#8217;s sd-daemon.c and sd-daemon.h files. These interfaces are available as shared library, which can be compiled and linked to with the libsystemd-daemon <code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file. Alternatively, applications consuming these APIs may copy the implementation into their source tree, either verbatim or in excerpts. </p>
<p>The functions directly related to new-style daemons become NOPs when -DDISABLE_SYSTEMD is set during compilation and the reference implementation is used as drop-in files. In addition, if sd-daemon.c is compiled on non-Linux systems they become NOPs.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd_listen_fds/">sd_listen_fds</a></code>(3), <code><a href="/docs/linux/man/3-sd_notify/">sd_notify</a></code>(3), <code><a href="/docs/linux/man/3-sd_booted/">sd_booted</a></code>(3), <code><a href="/docs/linux/man/3-sd_is_fifo/">sd_is_fifo</a></code>(3), <code><a href="/docs/linux/man/7-daemon/">daemon</a></code>(7), <code>systemd.service</code>(5), <code>systemd.socket</code>(5), <code><a href="/docs/linux/man/3-fprintf/">fprintf</a></code>(3), <code><a href="/docs/linux/man/7-sd-readahead/">sd-readahead</a></code>(7), <code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1)  </p>
<h2>AUTHOR</h2>
<p> <code>Lennart Poettering</code> &lt;lennart [at] poettering.net&gt; </p>
<dl>
<dd> <p> Developer </p>
 </dd></dl>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">NOTES</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">SEE ALSO</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">AUTHOR</a></dt>
<dd>  </dd></dl>
