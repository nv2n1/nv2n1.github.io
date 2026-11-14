---
title: "sd_id128_get_machine(3)"
name: "sd_id128_get_machine"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_id128_get_machine/"
description: "sd_id128_get_machine, sd_id128_get_boot – Retrieve 128-bit IDs"
---

<p>sd_id128_get_machine, sd_id128_get_boot &#8211; Retrieve 128-bit IDs</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;systemd/sd-id128.h&gt;

int sd_id128_get_machine(sd_id128_t *ret);

int sd_id128_get_boot(sd_id128_t *ret);</code></pre>
<h2>Description</h2>
<p><code>sd_id128_get_machine()</code></p>
<dd>returns the machine ID of the executing host. This reads and parses the <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5) file. This function caches the machine ID internally to make retrieving the machine ID a cheap operation. </p>
<p> <code>sd_id128_get_boot()</code> returns the boot ID of the executing kernel. This reads and parses the /proc/sys/kernel/random/boot_id file exposed by the kernel. It is randomly generated early at boot and is unique for every running kernel instance. See <code><a href="/docs/linux/man/4-random/">random</a></code>(4) for more information. This function also internally caches the returned ID to make this call a cheap operation. </p>
<p> Note that <code>sd_id128_get_boot()</code> always returns a UUID v4 compatible ID. <code>sd_id128_get_machine()</code> will also return a UUID v4-compatible ID on new installations but might not on older. It is possible to convert the machine ID into a UUID v4-compatible one. For more information, see <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5). </p>
<p> For more information about the &quot;sd_id128_t&quot; type see <code><a href="/docs/linux/man/3-sd-id128/">sd-id128</a></code>(3).</p>
<h2>Return Value</h2>
<p>The two calls return 0 on success (in which case <i>ret</i> is filled in), or a negative errno-style error code.</p>
<h2>Notes</h2>
<p>The <code>sd_id128_get_machine()</code> and <code>sd_id128_get_boot()</code> interfaces are available as a shared library, which can be compiled and linked to with the &quot;libsystemd&quot;&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd-id128/">sd-id128</a></code>(3), <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5), <code><a href="/docs/linux/man/4-random/">random</a></code>(4), <code><a href="/docs/linux/man/3-sd_id128_randomize/">sd_id128_randomize</a></code>(3) </p>
