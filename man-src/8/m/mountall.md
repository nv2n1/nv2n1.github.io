---
title: "mountall(8)"
name: "mountall"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mountall/"
description: "mountall – Mount filesystems during boot"
---

<p>mountall &#8211; Mount filesystems during boot</p>
<h2>Synopsis</h2>
<p><code>mountall</code> [<i>OPTIONS</i>]&#8230;</p>
<h2>Description</h2>
<p><code>mountall</code> is an Upstart <code><a href="/docs/linux/man/8-init/">init</a></code>(8) helper that mounts filesystems. </p>
<p> It reads <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5) and supplements the entries found with a set of built-in entries (generally found in <i>/lib/init/fstab</i>) and calls <code><a href="/docs/linux/man/8-fsck/">fsck</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) and <code><a href="/docs/linux/man/8-swapon/">swapon</a></code>(8) in the correct order to mount filesystems once the underlying devices have been created by <code><a href="/docs/linux/man/8-udevd/">udevd</a></code>(8).</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;daemon</code></p>
<dd>Detach and run in the background.</p>
<dt><code>&#8211;force-fsck</code></p>
<dd>Force check of all filesystems.</p>
<dt><code>&#8211;fsck-fix</code></p>
<dd>Attempt to fix all fsck errors.</p>
<dt><code>&#8211;no-events</code></p>
<dd>Do not emit events after mounting filesystems.</p>
<dt><code>&#8211;dev-wait-time=</code><i>value</i> (in seconds)</p>
<dd>In case of bootwait or timeout: specify the time to wait for device to be detected. The default is 30 seconds. Legal values are between 1 and 2147483647 seconds.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Reduce output to errors only.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Increase output to include informational messages.</p>
<dt><code>&#8211;help</code></p>
<dd>Display this help and exit.</p>
<dt><code>&#8211;version</code></p>
<dd>Output version information and exit.</dl>
<h2>Author</h2>
<p>Written by Scott James Remnant &lt;<code>scott [at] netsplit.com</code>&gt;</p>
<h2>Bugs</h2>
<p>Report bugs at &lt;<code><a rel="nofollow" href="https://launchpad.net/ubuntu/+source/mountall/+bugs">https://launchpad.net/ubuntu/+source/mountall/+bugs</a></code>&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009-2013 Canonical Ltd. </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-all-swaps/">all-swaps</a></code>(7), <code><a href="/docs/linux/man/7-filesystem/">filesystem</a></code>(7), <code><a href="/docs/linux/man/8-init/">init</a></code>(8), <code><a href="/docs/linux/man/7-local-filesystems/">local-filesystems</a></code>(7), <code><a href="/docs/linux/man/7-mounted/">mounted</a></code>(7), <code><a href="/docs/linux/man/7-mounting/">mounting</a></code>(7), <code><a href="/docs/linux/man/7-remote-filesystems/">remote-filesystems</a></code>(7), <code><a href="/docs/linux/man/7-virtual-filesystems/">virtual-filesystems</a></code>(7). </p>
