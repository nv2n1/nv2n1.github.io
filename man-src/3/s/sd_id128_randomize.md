---
title: "sd_id128_randomize(3)"
name: "sd_id128_randomize"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_id128_randomize/"
description: "sd_id128_randomize – Generate 128-bit IDs"
---

<p>sd_id128_randomize &#8211; Generate 128-bit IDs</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;systemd/sd-id128.h&gt;

int sd_id128_randomize(sd_id128_t *ret);</code></pre>
<h2>Description</h2>
<p><code>sd_id128_randomize()</code></p>
<dd>generates a new randomized 128-bit ID and returns it in <i>ret</i>. Every invocation returns a new randomly generated ID. This uses the /dev/urandom kernel random number generator. </p>
<p> Note that <code>sd_id128_randomize()</code> always returns a UUID v4-compatible ID. </p>
<p> For more information about the &quot;sd_id128_t&quot; type, see <code><a href="/docs/linux/man/3-sd-id128/">sd-id128</a></code>(3). </p>
<p> <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1)&#8217;s <code>&#8211;new-id</code> option may be used as a command line front-end for <code>sd_id128_randomize()</code>.</p>
<h2>Return Value</h2>
<p>The call returns 0 on success (in which case <i>ret</i> is filled in), or a negative errno-style error code.</p>
<h2>Notes</h2>
<p>The <code>sd_id128_randomize()</code> interface is available as a shared library, which can be compiled and linked to with the &quot;libsystemd&quot;&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd-id128/">sd-id128</a></code>(3), <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5), <code><a href="/docs/linux/man/4-random/">random</a></code>(4), <code><a href="/docs/linux/man/3-sd_id128_get_machine/">sd_id128_get_machine</a></code>(3) </p>
