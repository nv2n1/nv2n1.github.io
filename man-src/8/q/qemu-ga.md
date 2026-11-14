---
title: "qemu-ga(8)"
name: "qemu-ga"
section: "8"
letter: "q"
url: "/docs/linux/man/8-qemu-ga/"
description: "qemu-ga – QEMU Guest Agent"
---

<p>qemu-ga &#8211; QEMU Guest Agent</p>
<h2>Synopsis</h2>
<p><code>qemu-ga</code> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>]</p>
<h2>Description</h2>
<p>The <font SIZE="-1">QEMU</font> Guest Agent is a daemon intended to be run within virtual machines. It allows the hypervisor host to perform various operations in the guest, such as:</p>
<dl>
<dt>&bull;</p>
<dd>get information from the guest</p>
<dt>&bull;</p>
<dd>set the guest&#8217;s system time</p>
<dt>&bull;</p>
<dd>read/write a file</p>
<dt>&bull;</p>
<dd>sync and freeze the filesystems</p>
<dt>&bull;</p>
<dd>suspend the guest</p>
<dt>&bull;</p>
<dd>reconfigure guest local processors</p>
<dt>&bull;</p>
<dd>set user&#8217;s password</p>
<dt>&bull;</p>
<dd>&#8230;</dl>
<p> qemu-ga will read a system configuration file on startup (located at <i>/etc/qemu/qemu-ga.conf</i> by default), then parse remaining configuration options on the command line. For the same key, the last option wins, but the lists accumulate (see below for configuration file format).</p>
<h2>Options</h2>
<dl>
<dt><code>-m, &#8211;method=</code><i>method</i></p>
<dd>
<pre> Transport method: one of B&lt;unix-listen&gt;, B&lt;virtio-serial&gt;, or
 B&lt;isa-serial&gt; (B&lt;virtio-serial&gt; is the default).</pre>
<dt><code>-p, &#8211;path=</code><i>path</i></p>
<dd>
<pre> Device/socket path (the default for virtio-serial is
 B&lt;/dev/virtio-ports/org.qemu.guest_agent.0&gt;,
 the default for isa-serial is B&lt;/dev/ttyS0&gt;)</pre>
<dt><code>-l, &#8211;logfile=</code><i>path</i></p>
<dd>
<pre> Set log file path (default is stderr).</pre>
<dt><code>-f, &#8211;pidfile=</code><i>path</i></p>
<dd>
<pre> Specify pid file (default is B&lt;/var/run/qemu-ga.pid&gt;).</pre>
<dt><code>-F, &#8211;fsfreeze-hook=</code><i>path</i></p>
<dd>
<pre> Enable fsfreeze hook. Accepts an optional argument that specifies
 script to run on freeze/thaw. Script will be called with
 'freeze'/'thaw' arguments accordingly (default is
 B&lt;/etc/qemu/fsfreeze-hook&gt;). If using -F with an argument, do
 not follow -F with a space (for example:
 B&lt;-F/var/run/fsfreezehook.sh&gt;).</pre>
<dt><code>-t, &#8211;statedir=</code><i>path</i></p>
<dd>
<pre> Specify the directory to store state information (absolute paths only,
 default is B&lt;/var/run&gt;).</pre>
<dt><code>-v, &#8211;verbose</code></p>
<dd>
<pre> Log extra debugging information.</pre>
<dt><code>-V, &#8211;version</code></p>
<dd>
<pre> Print version information and exit.</pre>
<dt><code>-d, &#8211;daemon</code></p>
<dd>
<pre> Daemonize after startup (detach from terminal).</pre>
<dt><code>-b, &#8211;blacklist=</code><i>list</i></p>
<dd>
<pre> Comma-separated list of RPCs to disable (no spaces, B&lt;?&gt; to list
 available RPCs).</pre>
<dt><code>-D, &#8211;dump-conf</code></p>
<dd>
<pre> Dump the configuration in a format compatible with F&lt;qemu-ga.conf&gt;
 and exit.</pre>
<dt><code>-h, &#8211;help</code></p>
<dd>
<pre> Display this help and exit.</pre>
</dl>
<h2>Files</h2>
<p>The syntax of the <i>qemu-ga.conf</i> configuration file follows the Desktop Entry Specification, here is a quick summary: it consists of groups of key-value pairs, interspersed with comments. </p>
<pre> # qemu-ga configuration sample
 [general]
 daemonize = 0
 pidfile = /var/run/qemu-ga.pid
 verbose = 0
 method = virtio-serial
 path = /dev/virtio-ports/org.qemu.guest_agent.0
 statedir = /var/run</pre>
<p>The list of keys follows the command line options:</p>
<dl>
<dt><code>daemon= boolean</code></p>
<dd>
<dt><code>method= string</code></p>
<dd>
<dt><code>path= string</code></p>
<dd>
<dt><code>logfile= string</code></p>
<dd>
<dt><code>pidfile= string</code></p>
<dd>
<dt><code>fsfreeze-hook= string</code></p>
<dd>
<dt><code>statedir= string</code></p>
<dd>
<dt><code>verbose= boolean</code></p>
<dd>
<dt><code>blacklist= string list</code></p>
<dd></dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-qemu/">qemu</a></i>(1)</p>
<h2>Author</h2>
<p>Michael Roth &lt;mdroth [at] linux.vnet.ibm.com&gt;</p>
