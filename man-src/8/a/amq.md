---
title: "amq(8)"
name: "amq"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amq/"
description: "amq – automounter query tool"
---

<p>amq &#8211; automounter query tool</p>
<h2>Synopsis</h2>
<p><code>amq</code> [ <code>-fimpqsvwHTU</code> ] [ <code>-h</code><i> hostname</i> ] [ <code>-l</code><i> log_file</i> ] [ <code>-x</code><i> log_options</i> ] [ <code>-D</code><i> debug_options</i> ] [ <code>-P</code><i> program_number</i> ] [[ <code>-u</code> ] <i>directory &#8230;</i> ]</p>
<h2>Description</h2>
<p><code>Amq</code> provides a simple way of determining the current state of <code>amd</code> program. Communication is by <font SIZE="-1">RPC.</font> Three modes of operation are supported by the current protocol. By default a list of mount points and auto-mounted filesystems is output. An alternative host can be specified using the <i>-h</i> option. </p>
<p> If <i>directory</i> names are given, as output by default, then per-filesystem information is displayed.</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code></p>
<dd>Ask the automounter to flush the internal caches and reload all the maps. </p>
<dt><code>-h</code><i> hostname</i></p>
<dd>Specify an alternate host to query. By default the local host is used. In an <font SIZE="-1">HP-UX</font> cluster, the root server is queried by default, since that is the system on which the automounter is normally run. </p>
<dt><code>-i</code></p>
<dd>Print information about the mount maps. </p>
<dt><code>-l</code><i> log_file</i></p>
<dd>Tell amd to use <i>log_file</i> as the log file name. For security reasons, this must be the same log file which amd used when started. This option is therefore only useful to refresh amd&#8217;s open file handle on the log file, so that it can be rotated and compressed via daily cron jobs. </p>
<dt><code>-m</code></p>
<dd>Ask the automounter to provide a list of mounted filesystems, including the number of references to each filesystem and any error which occurred while mounting. </p>
<dt><code>-p</code></p>
<dd>Return the process ID of the remote or locally running amd. Useful when you need to send a signal to the local amd process, and would rather not have to search through the process table. This option is used in the <i>ctl-amd</i> script. </p>
<dt><code>-q</code></p>
<dd>Suppress error messages produced when attempting synchronous unmounts with the <code>-u</code> option. </p>
<dt><code>-s</code></p>
<dd>Ask the automounter to provide system-wide mount statistics. </p>
<dt><code>-u</code></p>
<dd>Ask the automounter to unmount the filesystems named in <i>directory</i> instead of providing information about them. Unmounts are requested, not forced. They merely cause the mounted filesystem to timeout, which will be picked up by <code>amd</code>&#8216;s main scheduler thus causing the normal timeout action to be taken. If the <code>-u</code> option is repeated, <code>amq</code> will attempt to unmount the file system synchronously by waiting until the timeout action is taken and returning an error if the unmount fails. Any error messages produced may be suppressed with the <code>-q</code> option. </p>
<dt><code>-v</code></p>
<dd>Ask the automounter for its version information. This is a subset of the information output by <code>amd</code>&#8216;s <i>-v</i> option. </p>
<dt><code>-w</code></p>
<dd>Translate a full pathname as returned by <i><a href="/docs/linux/man/3-getcwd/">getcwd</a></i>(3) into a short <code>Amd</code> pathname that goes through its mount points. This option requires that <code>Amd</code> is running. </p>
<dt><code>-x</code><i> log_options</i></p>
<dd>Ask the automounter to use the logging options specified in <i>log_options</i> from now on. Note that the &quot;fatal&quot; and &quot;error&quot; options cannot be turned off. </p>
<dt><code>-D</code><i> debug_options</i></p>
<dd>Ask the automounter to use the debugging options specified in <i>debug_options</i> from now on. </p>
<dt><code>-H</code></p>
<dd>Display short usage message. </p>
<dt><code>-P</code><i> program_number</i></p>
<dd>Contact an alternate running amd that had registered itself on a different RPC <i>program_number</i> and apply all other operations to that instance of the automounter. This is useful when you run multiple copies of amd, and need to manage each one separately. If not specified, amq will use the default program number for amd, 300019. For security reasons, the only alternate program numbers amd can use range from 300019 to 300029, inclusive. </p>
<dt><code>-T</code></p>
<dd>Contact <code>amd</code> using the TCP transport only. Normally <code>amq</code> will try TCP, and if that failed, will try UDP. </p>
<dt><code>-U</code></p>
<dd>Contact <code>amd</code> using UDP (connectionless) transport only. Normally <code>amq</code> will try TCP, and if that failed, will try UDP. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><code>amq.x</code></p>
<dd><font SIZE="-1">RPC</font> protocol description. </p>
</dl>
<h2>Caveats</h2>
<p><code>Amq</code> uses a Sun registered <font SIZE="-1">RPC</font> program number (300019 decimal) which may not be in the /etc/rpc database. </p>
<p> If the TCP wrappers library is available, and the <code>use_tcpwrappers</code> global <code>amd.conf</code> option is set to &#8220;yes&#8221;, then <code>amd</code> will verify that the host running <code>amq</code> is authorized to connect. The <i>amd</i> service name must used in the <code>/etc/hosts.allow</code> and <code>/etc/hosts.deny</code> files. For example, to allow only localhost to connect to <code>amd,</code> add this line to <code>/etc/hosts.allow:</code> </p>
<dl>
<dd>amd: localhost</dl>
<p> and this line to <code>/etc/hosts.deny:</code> </p>
<dl>
<dd>amd: ALL</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amd/">amd</a></code>(8), <code><a href="/docs/linux/man/5-amd-conf/">amd.conf</a></code>(5), <code><a href="/docs/linux/man/5-hosts_access/">hosts_access</a></code>(5). &#8220;am-utils&#8221; <code><a href="/docs/linux/man/1-info/">info</a></code>(1) entry. <i>Linux NFS and Automounter Administration</i> by Erez Zadok, ISBN 0-7821-2739-8, (Sybex, 2001). <i><a rel="nofollow" href="http://www.am-utils.org">http://www.am-utils.org</a></i> <i>Amd &#8211; The 4.4 BSD Automounter</i> </p>
<h2>Authors</h2>
<p>Jan-Simon Pendry &lt;jsp [at] doc.ic.ac.uk&gt;, Department of Computing, Imperial College, London, UK. </p>
<p> Erez Zadok &lt;ezk [at] cs.sunysb.edu&gt;, Computer Science Department, Stony Brook University, Stony Brook, New York, USA. </p>
<p> Other authors and contributors to am-utils are listed in the <code>AUTHORS</code> file distributed with am-utils.</p>
