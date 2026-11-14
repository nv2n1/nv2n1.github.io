---
title: "sd-readahead(3)"
name: "sd-readahead"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd-readahead/"
description: "sd-readahead – Reference implementation of APIs for controlling boot-time read-ahead"
---

<p>sd-readahead &#8211; Reference implementation of APIs for controlling boot-time read-ahead</p>
<h2>Synopsis</h2>
<pre><code>#include &quot;sd-readahead.h&quot;</code></pre>
<h2>Description</h2>
<p>sd-readahead.c and sd-readahead.h provide a reference implementation for APIs for controlling boot-time read-ahead, as implemented by the read-ahead subsystem of the <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) init system. </p>
<p> See <code><a href="/docs/linux/man/3-sd_readahead/">sd_readahead</a></code>(3) for more information about the function implemented.</p>
<h2>Notes</h2>
<p>This interface is provided by the reference implementation of APIs for controlling boot-time read-ahead and distributed with the systemd package. The algorithms it implements are simple, and can easily be reimplemented in daemons if it is important to support this interface without using the reference implementation. See the respective function man pages for details. </p>
<p> In addition, for details about the algorithms, check the liberally licensed reference implementation sources: m[blue]<code><a rel="nofollow" href="http://cgit.freedesktop.org/systemd/systemd/plain/src/readahead/sd-readahead.c">http://cgit.freedesktop.org/systemd/systemd/plain/src/readahead/sd-readahead.c</a></code>m[] and m[blue]<code><a rel="nofollow" href="http://cgit.freedesktop.org/systemd/systemd/plain/src/systemd/sd-readahead.h">http://cgit.freedesktop.org/systemd/systemd/plain/src/systemd/sd-readahead.h</a></code>m[] </p>
<p> These APIs are implemented in the reference implementation&#8217;s drop-in sd-readahead.c and sd-readahead.h files. It is recommended that applications consuming these APIs copy the implementation into their source tree, either verbatim or in excerpts. These interfaces are currently not available in a dynamic library. </p>
<p> The functions provided by this interface become NOPs when -DDISABLE_SYSTEMD is set during compilation. In addition, if sd-readhead.c is compiled on non-Linux systems it becomes NOPs.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd_readahead/">sd_readahead</a></code>(3), <code><a href="/docs/linux/man/3-sd-daemon/">sd-daemon</a></code>(3) </p>
