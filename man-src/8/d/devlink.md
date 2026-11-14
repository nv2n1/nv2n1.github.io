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
<dt><code>-V</code>,<code> &#8211;Version</code></p>
<dd>Print the version of the <code>devlink</code> utility and exit. </p>
<dt><code>-b,</code> -batch <code>&lt;FILENAME&gt;</code></p>
<dd>Read commands from provided file or standard input and invoke them. First failure will cause termination of devlink. </p>
<dt><code>-force</code></p>
<dd>Don&#8217;t terminate devlink on errors in batch mode. If there were any errors during execution of the commands, the application return code will be non zero. </p>
<dt><code>-n</code>,<code> &#8211;no-nice-names</code></p>
<dd>Turn off printing out nice names, for example netdevice ifnames instead of devlink port identification. </p>
<dt><code>-j</code>,<code> &#8211;json</code></p>
<dd>Generate JSON output. </p>
<dt><code>-p</code>,<code> &#8211;pretty</code></p>
<dd>When combined with -j generate a pretty JSON output. </p>
<dt><code>-v</code>,<code> &#8211;verbose</code></p>
<dd>Turn on verbose output. </p>
<dt><code>-s</code>,<code> &#8211;statistics</code></p>
<dd>Output statistics. </p>
<dt><code>-N,</code> -Netns <code>&lt;NETNSNAME&gt;</code></p>
<dd>Switches to the specified network namespace. </p>
<dt><code>-i,</code> &#8211;iec</p>
<dd>Print human readable rates in IEC units (e.g. 1Ki = 1024). </p>
</dl>
<h3><i>OBJECT</i></h3>
<dl>
<dt><code>dev</code></p>
<dd>&#8211; devlink device. </p>
<dt><code>port</code></p>
<dd>&#8211; devlink port. </p>
<dt><code>monitor</code></p>
<dd>&#8211; watch for netlink messages. </p>
<dt><code>sb</code></p>
<dd>&#8211; devlink shared buffer configuration. </p>
<dt><code>resource</code></p>
<dd>&#8211; devlink device resource configuration. </p>
<dt><code>region</code></p>
<dd>&#8211; devlink address region access </p>
<dt><code>health</code></p>
<dd>&#8211; devlink reporting and recovery </p>
<dt><code>trap</code></p>
<dd>&#8211; devlink trap configuration </p>
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
