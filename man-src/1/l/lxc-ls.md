---
title: "lxc-ls(1)"
name: "lxc-ls"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lxc-ls/"
description: "lxc-ls – list the containers existing on the system"
---

<h2>NAME</h2>
<p> lxc-ls &#8211; list the containers existing on the system</p>
<h2>SYNOPSIS</h2>
<p> <code>lxc-ls</code> [-1] [-P <i>lxcpath</i>] [&#8211;active] [&#8211;frozen] [&#8211;running] [&#8211;stopped] [-f] [-F <i>format</i>] [&#8211;nesting] [filter] [&#8211;version]</p>
<h2>DESCRIPTION</h2>
<p> <code>lxc-ls</code> list the containers existing on the system.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>[-1]</code></dt>
<dd> Show one entry per line. (default when /dev/stdout isn&#8217;t a tty)</dd>
<dt><code>[-P, &#8211;lxcpath]</code></dt>
<dd> Use an alternate container path. The default is /var/lib/lxc.</dd>
<dt><code>[&#8211;active]</code></dt>
<dd> List only active containers (same as &#8211;frozen &#8211;running).</dd>
<dt><code>[&#8211;frozen]</code></dt>
<dd> List only frozen containers.</dd>
<dt><code>[&#8211;running]</code></dt>
<dd> List only running containers.</dd>
<dt><code>[&#8211;stopped]</code></dt>
<dd> List only stopped containers.</dd>
<dt><code>[-f, &#8211;fancy]</code></dt>
<dd> Use a fancy, column-based output.</dd>
<dt><code>[-F, &#8211;fancy-format </code><i>format</i><code>]</code></dt>
<dd> Comma separated list of column to show in the fancy output. The list of accepted and default fields is listed in &#8211;help.</dd>
<dt><code>[&#8211;nesting]</code></dt>
<dd> Show nested containers.</dd>
<dt><code>[filter]</code></dt>
<dd> The filter passed to <code>lxc-ls</code> will be applied to the container name. The format is a regular expression.</dd>
<dt><code>[&#8211;version]</code></dt>
<dd> Show the version number.</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>lxc-ls &#8211;fancy</dt>
<dd> list all the containers, listing one per line along with its name, state, ipv4 and ipv6 addresses.</dd>
<dt>lxc-ls &#8211;active -1</dt>
<dd> list active containers and display the list in one column.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-lxc/">lxc</a></code>(7), <code><a href="/docs/linux/man/1-lxc-create/">lxc-create</a></code>(1), <code><a href="/docs/linux/man/1-lxc-destroy/">lxc-destroy</a></code>(1), <code><a href="/docs/linux/man/1-lxc-start/">lxc-start</a></code>(1), <code><a href="/docs/linux/man/1-lxc-stop/">lxc-stop</a></code>(1), <code><a href="/docs/linux/man/1-lxc-execute/">lxc-execute</a></code>(1), <code><a href="/docs/linux/man/1-lxc-console/">lxc-console</a></code>(1), <code><a href="/docs/linux/man/1-lxc-monitor/">lxc-monitor</a></code>(1), <code><a href="/docs/linux/man/1-lxc-wait/">lxc-wait</a></code>(1), <code><a href="/docs/linux/man/1-lxc-cgroup/">lxc-cgroup</a></code>(1), <code><a href="/docs/linux/man/1-lxc-ls/">lxc-ls</a></code>(1), <code><a href="/docs/linux/man/1-lxc-info/">lxc-info</a></code>(1), <code><a href="/docs/linux/man/1-lxc-freeze/">lxc-freeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-unfreeze/">lxc-unfreeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-attach/">lxc-attach</a></code>(1), <code><a href="/docs/linux/man/5-lxc-conf/">lxc.conf</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> St&eacute;phane Graber &lt;stgraber [at] ubuntu.com&gt; </p>
<h2>Index</h2>
