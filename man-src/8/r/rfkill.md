---
title: "rfkill(8)"
name: "rfkill"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rfkill/"
description: "rfkill – tool for enabling and disabling wireless devices"
---

<p>rfkill &#8211; tool for enabling and disabling wireless devices</p>
<h2>Synopsis</h2>
<p><code>rfkill</code> [options] [<i>command</i>] [<i>ID</i>|<i>type</i> &#8230;]</p>
<h2>Description</h2>
<p><code>rfkill</code> lists, enabling and disabling wireless devices. </p>
<p> The command &quot;list&quot; output format is deprecated and maintained for backward compatibility only. The new output format is the default when no command is specified or when the option <code>&#8211;output</code> is used. </p>
<p> The default output is subject to change. So whenever possible, you should avoid using default outputs in your scripts. Always explicitly define expected columns by using the <code>&#8211;output</code> option together with a columns list in environments where a stable output is required.</p>
<h2>Options</h2>
<p><code>-J</code>, <code>&#8211;json</code></p>
<dl>
<dd>Use JSON output format.</dl>
<p> <code>-n</code>, <code>&#8211;noheadings</code></p>
<dl>
<dd>Do not print a header line.</dl>
<p> <code>-o</code>, <code>&#8211;output</code></p>
<dl>
<dd>Specify which output columns to print. Use <code>&#8211;help</code> to get a list of available columns.</dl>
<p> <code>&#8211;output-all</code></p>
<dl>
<dd>Output all available columns.</dl>
<p> <code>-r</code>, <code>&#8211;raw</code></p>
<dl>
<dd>Use the raw output format.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<h2>Commands</h2>
<p><code>help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<p> <code>event</code></p>
<dl>
<dd>Listen for rfkill events and display them on stdout.</dl>
<p> <code>list</code> [<i>id</i>|<i>type</i> &#8230;]</p>
<dl>
<dd>List the current state of all available devices. The command output format is deprecated, see the section DESCRIPTION. It is a good idea to check with <code>list</code> command <i>id</i> or <i>type</i> scope is appropriate before setting <code>block</code> or <code>unblock</code>. Special <i>all</i> type string will match everything. Use of multiple <i>ID</i> or <i>type</i> arguments is supported.</dl>
<p> <code>block id</code>|<code>type</code> [&#8230;]</p>
<dl>
<dd>Disable the corresponding device.</dl>
<p> <code>unblock id</code>|<code>type</code> [&#8230;]</p>
<dl>
<dd>Enable the corresponding device. If the device is hard-blocked, for example via a hardware switch, it will remain unavailable though it is now soft-unblocked.</dl>
<p> <code>toggle id</code>|<code>type</code> [&#8230;]</p>
<dl>
<dd>Enable or disable the corresponding device.</dl>
<h2>Example</h2>
<dl>
<dd>
<pre> rfkill --output ID,TYPE
 rfkill block all
 rfkill unblock wlan
 rfkill block bluetooth uwb wimax wwan gps fm nfc</pre>
</dl>
<h2>Authors</h2>
<p><code>rfkill</code> was originally written by and The code has been later modified by and for the util-linux project. </p>
<p> This manual page was written by for the Debian project (and may be used by others).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-powertop/">powertop</a></code>(8), <code><a href="/docs/linux/man/8-systemd-rfkill/">systemd-rfkill</a></code>(8), <i>Linux kernel documentation</i> &lt;<a rel="nofollow" href="https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/driver-api/rfkill.rst">https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/driver-api/rfkill.rst</a>&gt;</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>rfkill</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
