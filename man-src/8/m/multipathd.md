---
title: "multipathd(8)"
name: "multipathd"
section: "8"
letter: "m"
url: "/docs/linux/man/8-multipathd/"
description: "multipathd – multipath daemon"
---

<p>multipathd &#8211; multipath daemon </p>
<h2>Synopsis</h2>
<p><code>multipathd</code> [<code>options</code>] </p>
<h2>Description</h2>
<p>The <code>multipathd </code> daemon is in charge of checking for failed paths. When this happens, it will reconfigure the multipath map the path belongs to, so that this map regains its maximum performance and redundancy. This daemon executes the external multipath config tool when events occur. In turn, the multipath tool signals the multipathd daemon when it is done with devmap reconfiguration, so that it can refresh its failed path list. </p>
<h2>Options</h2>
<dl>
<dt><code>-d</code></p>
<dd>Forground Mode. Don&#8217;t daemonize, and print all messages to stdout and stderr.</p>
<dt><code>-v level</code></p>
<dd>Verbosity level. Print additional information while running multipathd. A level of 0 means only print errors. A level of 3 or greater prints debugging information as well.</p>
<dt><code>-k </code></p>
<dd>multipathd will enter interactive mode. From this mode, the available commands can be viewed by entering &quot;help&quot;. When you are finished entering commands, press CTRL-D to quit. </p>
</dl>
<h2>Commands</h2>
<dl>
<dt>The following commands can be used in interactive mode:</p>
<dd>
<dt><code>list|show paths</code></p>
<dd>Show the paths that multipathd is monitoring, and their state.</p>
<dt><code>list|show paths format $format</code></p>
<dd>Show the paths that multipathd is monitoring, using a format string with path format wildcards.</p>
<dt><code>list|show maps|multipaths</code></p>
<dd>Show the multipath devices that the multipathd is monitoring.</p>
<dt><code>list|show daemon</code></p>
<dd>Show the current state of the multipathd daemon</p>
<dt><code>list|show maps|multipaths format $format</code></p>
<dd>Show the status of all multipath devices that the multipathd is monitoring, using a format string with multipath format wildcards.</p>
<dt><code>list|show maps|multipaths status</code></p>
<dd>Show the status of all multipath devices that the multipathd is monitoring.</p>
<dt><code>list|show maps|multipaths stats</code></p>
<dd>Show some statistics of all multipath devices that multipathd is monitoring.</p>
<dt><code>list|show maps|multipaths topology</code></p>
<dd>Show the current multipath topology. Same as &quot;multipath -ll&quot;.</p>
<dt><code>list|show maps|multipaths json</code></p>
<dd>Show the multipath devices that multipathd is monitoring, using JSON formatted output.</p>
<dt><code>list|show topology</code></p>
<dd>Show the current multipath topology. Same as &quot;multipath -ll&quot;.</p>
<dt><code>list|show map|multipath $map topology</code></p>
<dd>Show topology of a single multipath device specified by $map, e.g. 36005076303ffc56200000000000010aa. This map could be obtained from &quot;list maps&quot;.</p>
<dt><code>list|show map|multipath $map json</code></p>
<dd>Show a single multipath device specified by $map, using JSON formatted output.</p>
<dt><code>list|show wildcards</code></p>
<dd>Show the format wildcards used in interactive commands taking $format</p>
<dt><code>list|show config</code></p>
<dd>Show the currently used configuration, derived from default values and values specified within the configuration file /etc/multipath.conf.</p>
<dt><code>list|show blacklist</code></p>
<dd>Show the currently used blacklist rules, derived from default values and values specified within the configuration file /etc/multipath.conf.</p>
<dt><code>list|show devices</code></p>
<dd>Show all available block devices by name including the information if they are blacklisted or not.</p>
<dt><code>list|show status</code></p>
<dd>Show the number of path checkers in each possible state, the number of monitored paths, and whether multipathd is currently handling a uevent.</p>
<dt><code>add path $path</code></p>
<dd>Add a path to the list of monitored paths. $path is as listed in /sys/block (e.g. sda).</p>
<dt><code>remove|del path $path</code></p>
<dd>Stop monitoring a path. $path is as listed in /sys/block (e.g. sda).</p>
<dt><code>add map|multipath $map</code></p>
<dd>Add a multipath device to the list of monitored devices. $map can either be a device-mapper device as listed in /sys/block (e.g. dm-0) or it can be the alias for the multipath device (e.g. mpath1) or the uid of the multipath device (e.g. 36005076303ffc56200000000000010aa).</p>
<dt><code>remove|del map|multipath $map</code></p>
<dd>Stop monitoring a multipath device.</p>
<dt><code>resize map|multipath $map</code></p>
<dd>Resizes map $map to the given size</p>
<dt><code>switch|switchgroup map|multipath $map group $group</code></p>
<dd>Force a multipath device to switch to a specific path group. $group is the path group index, starting with 1.</p>
<dt><code>reconfigure</code></p>
<dd>Reconfigures the multipaths. This should be triggered automatically after any hotplug event.</p>
<dt><code>suspend map|multipath $map</code></p>
<dd>Sets map $map into suspend state.</p>
<dt><code>resume map|multipath $map</code></p>
<dd>Resumes map $map from suspend state.</p>
<dt><code>reset map|multipath $map</code></p>
<dd>Reassign existing device-mapper table(s) use use the multipath device, instead of its path devices.</p>
<dt><code>reload map|multipath $map</code></p>
<dd>Reload a multipath device.</p>
<dt><code>fail path $path</code></p>
<dd>Sets path $path into failed state.</p>
<dt><code>reinstate path $path</code></p>
<dd>Resumes path $path from failed state.</p>
<dt><code>disablequeueing maps|multipaths</code></p>
<dd>Disable queueing on all multipath devices.</p>
<dt><code>restorequeueing maps|multipaths</code></p>
<dd>Restore queueing on all multipath devices.</p>
<dt><code>disablequeueing map|multipath $map</code></p>
<dd>Disable queuing on multipathed map $map</p>
<dt><code>restorequeueing map|multipath $map</code></p>
<dd>Restore queuing on multipathed map $map</p>
<dt><code>forcequeueing daemon</code></p>
<dd>Forces multipathd into queue_without_daemon mode, so that no_path_retry queueing will not be disabled when the daemon stops</p>
<dt><code>restorequeueing daemon</code></p>
<dd>Restores configured queue_without_daemon mode</p>
<dt><code>map|multipath $map setprstatus</code></p>
<dd>Enable persistent reservation management on $map</p>
<dt><code>map|multipath $map unsetprstatus</code></p>
<dd>Disable persistent reservation management on $map</p>
<dt><code>map|multipath $map getprstatus</code></p>
<dd>Get the current persistent reservation management status of $map</p>
<dt><code>quit|exit</code></p>
<dd>End interactive session.</p>
<dt><code>shutdown</code></p>
<dd>Stop multipathd. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-multipath/">multipath</a></code>(8) <code><a href="/docs/linux/man/8-kpartx/">kpartx</a></code>(8) <code><a href="/docs/linux/man/8-hotplug/">hotplug</a></code>(8)</p>
<h2>Authors</h2>
<p><code>multipathd</code> was developed by Christophe Varoqui, &lt;christophe.varoqui [at] opensvc.com&gt; and others.</p>
