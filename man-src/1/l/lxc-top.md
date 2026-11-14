---
title: "lxc-top(1)"
name: "lxc-top"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lxc-top/"
description: "lxc-top – monitor container statistics"
---

<h2>NAME</h2>
<p> lxc-top &#8211; monitor container statistics</p>
<h2>SYNOPSIS</h2>
<p> <code>lxc-top</code> [&#8211;help] [&#8211;max <i>count</i>] [&#8211;delay <i>delay</i>] [&#8211;sort <i>sortby</i>] [&#8211;reverse]</p>
<h2>DESCRIPTION</h2>
<p> <code>lxc-top</code> displays container statistics. The output is updated every <i>delay</i> seconds, and is ordered according to the <i>sortby</i> value given. Specifying <i>count</i> will limit the number of containers displayed, otherwise <code>lxc-top</code> will display as many containers as can fit in your terminal.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>[-m, &#8211;max </code><i>count</i><code>]</code></p>
<dd> Limit the number of containers displayed to <i>count</i>.</p>
<dt><code>[-d, &#8211;delay </code><i>delay</i><code>]</code></p>
<dd> Amount of time in seconds to delay between screen updates. This can be specified as less than a second by giving a rational number, for example 0.5 for a half second delay. The default is 3 seconds.</p>
<dt><code>[-s, &#8211;sort </code><i>sortby</i><code>]</code></p>
<dd> Sort the containers by name, cpu use, or memory use. The <i>sortby</i> argument should be one of the letters n,c,d,m,k to sort by name, cpu use, disk I/O, memory, or kernel memory use respectively. The default is &#8216;n&#8217;.</p>
<dt><code>[-r, &#8211;reverse]</code></p>
<dd> Reverse the default sort order. By default, names sort in ascending alphabetical order and values sort in descending amounts (ie. largest value first).</dl>
<h2>EXAMPLE</h2>
<dl>
<dt>lxc-top &#8211;delay 1 &#8211;sort m</p>
<dd> Display containers, updating every second, sorted by memory use.</dl>
<h2>NOTES</h2>
<p> For performance reasons the kernel does not account kernel memory use unless a kernel memory limit is set. If a limit is not set, <code> lxc-top</code> will display kernel memory use as 0. If no containers are being accounted, the KMem column will not be displayed. A limit can be set by specifying </p>
<pre>
      lxc.cgroup.memory.kmem.limit_in_bytes = <i>number</i>
      
</pre>
<p> in your container configuration file, see <code><a href="/docs/linux/man/5-lxc-conf/">lxc.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-lxc/">lxc</a></code>(7), <code><a href="/docs/linux/man/1-lxc-create/">lxc-create</a></code>(1), <code><a href="/docs/linux/man/1-lxc-destroy/">lxc-destroy</a></code>(1), <code><a href="/docs/linux/man/1-lxc-start/">lxc-start</a></code>(1), <code><a href="/docs/linux/man/1-lxc-stop/">lxc-stop</a></code>(1), <code><a href="/docs/linux/man/1-lxc-execute/">lxc-execute</a></code>(1), <code><a href="/docs/linux/man/1-lxc-console/">lxc-console</a></code>(1), <code><a href="/docs/linux/man/1-lxc-monitor/">lxc-monitor</a></code>(1), <code><a href="/docs/linux/man/1-lxc-wait/">lxc-wait</a></code>(1), <code><a href="/docs/linux/man/1-lxc-cgroup/">lxc-cgroup</a></code>(1), <code><a href="/docs/linux/man/1-lxc-ls/">lxc-ls</a></code>(1), <code><a href="/docs/linux/man/1-lxc-info/">lxc-info</a></code>(1), <code><a href="/docs/linux/man/1-lxc-freeze/">lxc-freeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-unfreeze/">lxc-unfreeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-attach/">lxc-attach</a></code>(1), <code><a href="/docs/linux/man/5-lxc-conf/">lxc.conf</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> Dwight Engen &lt;dwight.engen [at] oracle.com&gt; </p>
<h2>Index</h2>
