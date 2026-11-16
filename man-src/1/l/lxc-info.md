---
title: "lxc-info(1)"
name: "lxc-info"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lxc-info/"
description: "lxc-info – query information about a container"
---

<h2>NAME</h2>
<p> lxc-info &#8211; query information about a container</p>
<h2>SYNOPSIS</h2>
<p> <code>lxc-info</code> {-n <i>name</i>} [-c <i>KEY</i>] [-s] [-p] [-i] [-S] [-H]</p>
<h2>DESCRIPTION</h2>
<p> <code>lxc-info</code> queries and shows information about a container.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>[-c </code><i>KEY</i><code>]</code></dt>
<dd> Print a configuration key from the container. This option may be given multiple times to print out multiple key = value pairs.</dd>
<dt><code>[-s]</code></dt>
<dd> Just print the container&#8217;s state.</dd>
<dt><code>[-p]</code></dt>
<dd> Just print the container&#8217;s pid.</dd>
<dt><code>[-i]</code></dt>
<dd> Just print the container&#8217;s IP addresses.</dd>
<dt><code>[-S]</code></dt>
<dd> Just print the container&#8217;s statistics. Note that for performance reasons the kernel does not account kernel memory use unless a kernel memory limit is set. If a limit is not set, <code>lxc-info</code> will display kernel memory use as 0. A limit can be set by specifying </dd>
<pre>
            lxc.cgroup.memory.kmem.limit_in_bytes = <i>number</i>
</pre>
<p> in your container configuration file, see <code><a href="/docs/linux/man/5-lxc-conf/">lxc.conf</a></code>(5).</p>
<dt><code>[-H]</code></dt>
<dd> Print the container&#8217;s statistics in raw, non-humanized form. The default is to print statistics in humanized form.</dd></dl>
<h2>COMMON OPTIONS</h2>
<p> These options are common to most of lxc commands.</p>
<dl>
<dt><code>-?, -h, &#8211;help</code></dt>
<dd> Print a longer usage message than normal.</dd>
<dt><code>&#8211;usage</code></dt>
<dd> Give the usage message</dd>
<dt><code>-q, &#8211;quiet</code></dt>
<dd> mute on</dd>
<dt><code>-P, &#8211;lxcpath=</code><i>PATH</i></dt>
<dd> Use an alternate container path. The default is /var/lib/lxc.</dd>
<dt><code>-o, &#8211;logfile=</code><i>FILE</i></dt>
<dd> Output to an alternate log <i>FILE</i>. The default is no log.</dd>
<dt><code>-l, &#8211;logpriority=</code><i>LEVEL</i></dt>
<dd> Set log priority to <i>LEVEL</i>. The default log priority is ERROR. Possible values are : FATAL, CRIT, WARN, ERROR, NOTICE, INFO, DEBUG. </dd>
<p> Note that this option is setting the priority of the events log in the alternate log file. It do not have effect on the ERROR events log on stderr.</p>
<dt><code>-n, &#8211;name=</code><i>NAME</i></dt>
<dd> Use container identifier <i>NAME</i>. The container identifier format is an alphanumeric string.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show the version number.</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>lxc-info -n foo</dt>
<dd> Show information for foo.</dd>
<dt>lxc-info -n &#8216;ubuntu.*&#8217;</dt>
<dd> Show information for all containers whose name starts with ubuntu.</dd>
<dt>lxc-info -n foo -c lxc.network.0.veth.pair</dt>
<dd> prints the veth pair name of foo.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-lxc/">lxc</a></code>(7), <code><a href="/docs/linux/man/1-lxc-create/">lxc-create</a></code>(1), <code><a href="/docs/linux/man/1-lxc-destroy/">lxc-destroy</a></code>(1), <code><a href="/docs/linux/man/1-lxc-start/">lxc-start</a></code>(1), <code><a href="/docs/linux/man/1-lxc-stop/">lxc-stop</a></code>(1), <code><a href="/docs/linux/man/1-lxc-execute/">lxc-execute</a></code>(1), <code><a href="/docs/linux/man/1-lxc-console/">lxc-console</a></code>(1), <code><a href="/docs/linux/man/1-lxc-monitor/">lxc-monitor</a></code>(1), <code><a href="/docs/linux/man/1-lxc-wait/">lxc-wait</a></code>(1), <code><a href="/docs/linux/man/1-lxc-cgroup/">lxc-cgroup</a></code>(1), <code><a href="/docs/linux/man/1-lxc-ls/">lxc-ls</a></code>(1), <code><a href="/docs/linux/man/1-lxc-info/">lxc-info</a></code>(1), <code><a href="/docs/linux/man/1-lxc-freeze/">lxc-freeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-unfreeze/">lxc-unfreeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-attach/">lxc-attach</a></code>(1), <code><a href="/docs/linux/man/5-lxc-conf/">lxc.conf</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> St&eacute;phane Graber &lt;stgraber [at] ubuntu.com&gt; </p>
<h2>Index</h2>
