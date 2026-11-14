---
title: "teamdctl(8)"
name: "teamdctl"
section: "8"
letter: "t"
url: "/docs/linux/man/8-teamdctl/"
description: "teamdctl — team daemon control tool"
---

<p>teamdctl &#8212; team daemon control tool</p>
<h2>Synopsis</h2>
<p><code>teamdctl</code> [<i>options</i>] <i>team_device command </i>[<i>command_args</i>&#8230;]<br />
 <code>teamdctl -h</code></p>
<h2>Description</h2>
<p>teamdctl is a tool that allows a user to interact with a running teamd instance. It defaults to using Unix Domain Sockets, but will fall back to using the D-Bus API, to ensure reliable operation in all environments.</p>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Print help text to console and exit.</p>
<dt><code>-v, &#8211;verbosity</code></p>
<dd>Increase output verbosity.</p>
<dt><code>-o, &#8211;oneline</code></p>
<dd>Force output to one line if possible.</p>
<dt><code>-D, &#8211;force-dbus</code></p>
<dd>Force to use D-Bus interface.</p>
<dt><code>-Z </code><i>address</i><code>, &#8211;force-zmq </code><i>address</i></p>
<dd>Force to use ZMQ interface. Possible address formats are &quot;<a href="tcp://ip:port">tcp://ip:port</a>&quot;, &quot;<a href="ipc://path">ipc://path</a>&quot; and others. Detailed description of ZMQ library is in page <a rel="nofollow" href="http://zguide.zeromq.org/page:all.">http://zguide.zeromq.org/page:all.</a></p>
<dt><code>-U, &#8211;force-usock</code></p>
<dd>Force to use UNIX domain socket interface. This is the default behavior.</dl>
<h2>Command</h2>
<dl>
<dt><code>config dump</code></p>
<dd>Dumps teamd JSON config.</p>
<dt><code>config dump noports</code></p>
<dd>Dumps teamd JSON configuration without &quot;ports&quot; section included.</p>
<dt><code>config dump actual</code></p>
<dd>Dumps teamd actual JSON configuration. It includes ports which are currently present.</p>
<dt><code>state dump | state</code></p>
<dd>Dumps teamd JSON state document.</p>
<dt><code>state view</code></p>
<dd>Prints out state of teamd parsed from JSON state document.</p>
<dt><code>state item get </code><i>state_item_path</i></p>
<dd>Finds state item in JSON state document and returns its value. </p>
<p> If PORTIFNAME in state_item_path has any sensitive character, use double quotation marks to escape it, like: ports.&quot;eth1.1&quot;.link_watches.up. To process state_item_path of &#8216;state item set&#8217; is the same as here.</p>
<dt><code>state item set </code><i>state_item_path value</i></p>
<dd>Finds state item in JSON state document and sets its value by value parameter. This is available only for a limited number of paths:</p>
<dl>
<dd><code>setup.debug_level &#8212;</code> User can set debug level. Higher level is more verbose. </p>
<p> <code>ports.PORTIFNAME.runner.aggregator.selected &#8212;</code> This is available for lacp runner. User can manually select the aggregator. </p>
<p> <code>runner.active_port &#8212;</code> This is available for activebackup runner. User can manually select the active port.</dl>
<dt><code>port add </code><i>portdev</i></p>
<dd>Takes port device name as argument. Adds port device into team.</p>
<dt><code>port remove </code><i>portdev</i></p>
<dd>Takes port device name as argument. Removes port device from team.</p>
<dt><code>port present </code><i>portdev</i></p>
<dd>Takes port device name as argument. Checks if the port device is present in team.</p>
<dt><code>port config update </code><i>portdev portconfig-string</i></p>
<dd>Takes port device name as the first argument and JSON format configuration string as the second argument. Updates port device configuration.</p>
<dt><code>port config dump </code><i>portdev</i></p>
<dd>Takes port device name as the first argument. Dumps port device JSON configuration to standard output.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-teamd/">teamd</a></code>(8), <code><a href="/docs/linux/man/8-teamnl/">teamnl</a></code>(8), <code><a href="/docs/linux/man/5-teamd-conf/">teamd.conf</a></code>(5)</p>
<h2>Author</h2>
<p>Jiri Pirko is the original author and current maintainer of libteam.</p>
