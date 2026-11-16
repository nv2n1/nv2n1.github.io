---
title: "devlink(8)"
name: "devlink"
section: "8"
letter: "d"
url: "/docs/linux/man/8-devlink/"
description: "devlink – Devlink tool"
---

<p>devlink &#8211; Devlink tool</p>
<h2>Synopsis</h2>
<pre><code>devlink
[ OPTIONS ] { dev|port|monitor|sb|resource|region|health|trap } { COMMAND |
    help }
</code></pre>
<p> <code>devlink</code> [ <code>-force</code> ] <code>-batch </code><i>filename</i> </p>
<h2>Options</h2>
<dl>
<dt><code>-V</code>,<code> &#8211;Version</code></dt>
<dd>Print the version of the <code>devlink</code> utility and exit. </dd>
<dt><code>-b,</code> -batch <code>&lt;FILENAME&gt;</code></dt>
<dd>Read commands from provided file or standard input and invoke them. First failure will cause termination of devlink. </dd>
<dt><code>-force</code></dt>
<dd>Don&#8217;t terminate devlink on errors in batch mode. If there were any errors during execution of the commands, the application return code will be non zero. </dd>
<dt><code>-n</code>,<code> &#8211;no-nice-names</code></dt>
<dd>Turn off printing out nice names, for example netdevice ifnames instead of devlink port identification. </dd>
<dt><code>-j</code>,<code> &#8211;json</code></dt>
<dd>Generate JSON output. </dd>
<dt><code>-p</code>,<code> &#8211;pretty</code></dt>
<dd>When combined with -j generate a pretty JSON output. </dd>
<dt><code>-v</code>,<code> &#8211;verbose</code></dt>
<dd>Turn on verbose output. </dd>
<dt><code>-s</code>,<code> &#8211;statistics</code></dt>
<dd>Output statistics. </dd>
<dt><code>-N,</code> -Netns <code>&lt;NETNSNAME&gt;</code></dt>
<dd>Switches to the specified network namespace. </dd>
<dt><code>-i,</code> &#8211;iec</dt>
<dd>Print human readable rates in IEC units (e.g. 1Ki = 1024). </dd>
</dl>
<h3><i>OBJECT</i></h3>
<dl>
<dt><code>dev</code></dt>
<dd>&#8211; devlink device. </dd>
<dt><code>port</code></dt>
<dd>&#8211; devlink port. </dd>
<dt><code>monitor</code></dt>
<dd>&#8211; watch for netlink messages. </dd>
<dt><code>sb</code></dt>
<dd>&#8211; devlink shared buffer configuration. </dd>
<dt><code>resource</code></dt>
<dd>&#8211; devlink device resource configuration. </dd>
<dt><code>region</code></dt>
<dd>&#8211; devlink address region access </dd>
<dt><code>health</code></dt>
<dd>&#8211; devlink reporting and recovery </dd>
<dt><code>trap</code></dt>
<dd>&#8211; devlink trap configuration </dd>
</dl>
<h3><i>COMMAND</i></h3>
<p>Specifies the action to perform on the object. The set of possible actions depends on the object type. As a rule, it is possible to <code>show</code> (or <code>list</code> ) objects, but some objects do not allow all of these operations or have some additional commands. The <code>help</code> command is available for all objects. It prints out a list of available commands and argument syntax conventions. </p>
<p> If no command is given, some default command is assumed. Usually it is <code>list</code> or, if the objects of this class cannot be listed, <code>help</code>.</p>
<h2>Exit Status</h2>
<p>Exit status is 0 if command was successful or a positive integer upon failure.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-devlink-dev/">devlink-dev</a></code>(8), <code><a href="/docs/linux/man/8-devlink-port/">devlink-port</a></code>(8), <code><a href="/docs/linux/man/8-devlink-monitor/">devlink-monitor</a></code>(8), <code><a href="/docs/linux/man/8-devlink-sb/">devlink-sb</a></code>(8), <code><a href="/docs/linux/man/8-devlink-resource/">devlink-resource</a></code>(8), <code><a href="/docs/linux/man/8-devlink-region/">devlink-region</a></code>(8), <code><a href="/docs/linux/man/8-devlink-health/">devlink-health</a></code>(8), <code><a href="/docs/linux/man/8-devlink-trap/">devlink-trap</a></code>(8), </p>
<h2>Reporting Bugs</h2>
<p>Report any bugs to the Network Developers mailing list <code>&lt;netdev [at] vger.kernel.org&gt;</code> where the development and maintenance is primarily done. You do not have to be subscribed to the list to send a message there.</p>
<h2>Author</h2>
<p>Jiri Pirko &lt;jiri [at] mellanox.com&gt;</p>
