---
title: "sd_readahead(3)"
name: "sd_readahead"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_readahead/"
description: "sd_readahead – Control ongoing disk boot-time read-ahead operations"
---

<p>sd_readahead &#8211; Control ongoing disk boot-time read-ahead operations</p>
<h2>Synopsis</h2>
<pre><code>#include &quot;sd-readahead.h&quot;

int sd_readahead(const char *action);</code></pre>
<h2>Description</h2>
<p><code>sd_readahead()</code></p>
<dd>may be called by programs involved with early boot-up to control ongoing boot-time disk read-ahead operations. It may be used to terminate read-ahead operations in case an uncommon disk access pattern is to be expected and hence read-ahead replay or collection is unlikely to have the desired speed-up effect on the current or future boot-ups. </p>
<p> The <i>action</i> should be one of the following strings: </p>
<p> cancel</p>
<dl>
<dd>Terminates read-ahead data collection, and drops all read-ahead data collected during this boot-up.</dl>
<p> done</p>
<dl>
<dd>Terminates read-ahead data collection, but keeps all read-ahead data collected during this boot-up around for use during subsequent boot-ups.</dl>
<p> noreplay</p>
<dl>
<dd>Terminates read-ahead replay.</dl>
<h2>Return Value</h2>
<p>On failure, these calls return a negative errno-style error code. It is generally recommended to ignore the return value of this call.</p>
<h2>Notes</h2>
<p>This function is provided by the reference implementation of APIs for controlling boot-time read-ahead and distributed with the systemd package. The algorithm it implements is simple, and can easily be reimplemented in daemons if it is important to support this interface without using the reference implementation. </p>
<p> Internally, this function creates a file in /run/systemd/readahead/ which is then used as flag file to notify the read-ahead subsystem. </p>
<p> For details about the algorithm check the liberally licensed reference implementation sources: m[blue]<code><a rel="nofollow" href="http://cgit.freedesktop.org/systemd/systemd/plain/src/readahead/sd-readahead.c">http://cgit.freedesktop.org/systemd/systemd/plain/src/readahead/sd-readahead.c</a></code>m[] and m[blue]<code><a rel="nofollow" href="http://cgit.freedesktop.org/systemd/systemd/plain/src/systemd/sd-readahead.h">http://cgit.freedesktop.org/systemd/systemd/plain/src/systemd/sd-readahead.h</a></code>m[] </p>
<p> <code>sd_readahead()</code> is implemented in the reference implementation&#8217;s drop-in sd-readahead.c and sd-readahead.h files. It is recommended that applications consuming this API copy the implementation into their source tree. For more details about the reference implementation, see <code><a href="/docs/linux/man/3-sd-readahead/">sd-readahead</a></code>(3) </p>
<p> If -DDISABLE_SYSTEMD is set during compilation, this function will always return 0 and otherwise become a NOP.</p>
<h2>Examples</h2>
<p><code>Example 1. Cancelling all read-ahead operations</code> </p>
<p> During boots where SELinux has to relabel the file system hierarchy, it will create a large amount of disk accesses that are not necessary during normal boots. Hence it is a good idea to disable both read-ahead replay and read-ahead collection. </p>
<dl>
<dd>
<pre>sd_readahead(&quot;cancel&quot;);
sd_readahead(&quot;noreplay&quot;);</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd-readahead/">sd-readahead</a></code>(3), <code><a href="/docs/linux/man/7-daemon/">daemon</a></code>(7) </p>
