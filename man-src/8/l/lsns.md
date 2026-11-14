---
title: "lsns(8)"
name: "lsns"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lsns/"
description: "lsns – list namespaces"
---

<p>lsns &#8211; list namespaces</p>
<h2>Synopsis</h2>
<p><code>lsns</code> [options] <i>namespace</i></p>
<h2>Description</h2>
<p><code>lsns</code> lists information about all the currently accessible namespaces or about the given <i>namespace</i>. The <i>namespace</i> identifier is an inode number. </p>
<p> The default output is subject to change. So whenever possible, you should avoid using default outputs in your scripts. Always explicitly define expected columns by using the <code>&#8211;output</code> option together with a columns list in environments where a stable output is required. </p>
<p> The <code>NSFS</code> column, printed when <code>net</code> is specified for the <code>&#8211;type</code> option, is special; it uses multi-line cells. Use the option <code>&#8211;nowrap</code> to switch to &quot;,&quot;-separated single-line representation. </p>
<p> Note that <code>lsns</code> reads information directly from the <i>/proc</i> filesystem and for non-root users it may return incomplete information. The current <i>/proc</i> filesystem may be unshared and affected by a PID namespace (see <code>unshare &#8211;mount-proc</code> for more details). <code>lsns</code> is not able to see persistent namespaces without processes where the namespace instance is held by a bind mount to /proc/<i>pid</i>/ns/<i>type</i>.</p>
<h2>Options</h2>
<p><code>-J</code>, <code>&#8211;json</code></p>
<dl>
<dd>Use JSON output format.</dl>
<p> <code>-l</code>, <code>&#8211;list</code></p>
<dl>
<dd>Use list output format.</dl>
<p> <code>-n</code>, <code>&#8211;noheadings</code></p>
<dl>
<dd>Do not print a header line.</dl>
<p> <code>-o</code>, <code>&#8211;output</code> <i>list</i></p>
<dl>
<dd>Specify which output columns to print. Use <code>&#8211;help</code> to get a list of all supported columns. </p>
<p> The default list of columns may be extended if <i>list</i> is specified in the format <code>+</code><i>list</i> (e.g., <code>lsns -o +PATH</code>).</dl>
<p> <code>&#8211;output-all</code></p>
<dl>
<dd>Output all available columns.</dl>
<p> <code>-p</code>, <code>&#8211;task</code> <i>PID</i></p>
<dl>
<dd>Display only the namespaces held by the process with this <i>PID</i>.</dl>
<p> <code>-r</code>, <code>&#8211;raw</code></p>
<dl>
<dd>Use the raw output format.</dl>
<p> <code>-t</code>, <code>&#8211;type</code> <i>type</i></p>
<dl>
<dd>Display the specified <i>type</i> of namespaces only. The supported types are <code>mnt</code>, <code>net</code>, <code>ipc</code>, <code>user</code>, <code>pid</code>, <code>uts</code>, <code>cgroup</code> and <code>time</code>. This option may be given more than once.</dl>
<p> <code>-u</code>, <code>&#8211;notruncate</code></p>
<dl>
<dd>Do not truncate text in columns.</dl>
<p> <code>-W</code>, <code>&#8211;nowrap</code></p>
<dl>
<dd>Do not use multi-line text in columns.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<h2>Authors</h2>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-nsenter/">nsenter</a></code>(1), <code><a href="/docs/linux/man/1-unshare/">unshare</a></code>(1), <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7), <code><a href="/docs/linux/man/2-ioctl_ns/">ioctl_ns</a>(2)</code></p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>lsns</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
