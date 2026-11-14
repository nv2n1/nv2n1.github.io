---
title: "clvmd(8)"
name: "clvmd"
section: "8"
letter: "c"
url: "/docs/linux/man/8-clvmd/"
description: "clvmd — cluster LVM daemon"
---

<p>clvmd &#8212; cluster LVM daemon</p>
<h2>Synopsis</h2>
<p><code>clvmd</code> [<code>-C</code>] [<code>-d</code> [<i>value</i>]] [<code>-E</code> <i>lock_uuid</i>] [<code>-f</code>] [<code>-h</code>] [<code>-I</code> <i>cluster_manager</i>] [<code>-R</code>] [<code>-S</code>] [<code>-t</code> <i>timeout</i>] [<code>-T</code> <i>start_timeout</i>] [<code>-V</code>]</p>
<h2>Description</h2>
<p>clvmd is the daemon that distributes LVM metadata updates around a cluster. It must be running on all nodes in the cluster and will give an error if a node in the cluster does not have this daemon running.</p>
<h2>Options</h2>
<dl>
<dt> <code>-C</code></p>
<dd>
<dd>Only valid if <code>-d</code> is also specified. Tells all clvmds in a cluster to enable/disable debug logging. Without this switch, only the local clvmd will change its debug level to that given with <code>-d</code>.<br />
 This does not work correctly if specified on the command-line that starts clvmd. If you want to start clvmd <code>and</code> enable cluster-wide logging then the command needs to be issued twice, eg:<br />
 <code>clvmd</code><br />
 <code>clvmd -d2</code></p>
<dt> <code>-d</code> [<i>value</i>]</p>
<dd>
<dd>Set debug logging level. If <code>-d</code> is specified without a <i>value</i> then 1 is assumed. <i>Value</i> can be:</p>
<dd><code>0</code> &#8212; Disabled</p>
<dd><code>1</code> &#8212; Sends debug logs to stderr (implies <code>-f</code>)</p>
<dd><code>2</code> &#8212; Sends debug logs to <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3)</p>
<dt> <code>-E</code> <i>lock_uuid</i></p>
<dd>
<dd>Pass lock uuid to be reacquired exclusively when clvmd is restarted.</p>
<dt> <code>-f</code></p>
<dd>
<dd>Don&#8217;t fork, run in the foreground.</p>
<dt> <code>-h</code></p>
<dd>
<dd>Show help information.</p>
<dt> <code>-I</code> <i>cluster_manager</i></p>
<dd>
<dd>Selects the cluster manager to use for locking and internal communications. As it is quite possible to have multiple managers available on the same system you might have to manually specify this option to override the search. </p>
<p> By default, omit <code>-I</code> is equivalent to <code>-Iauto</code>. Clvmd will use the first cluster manager that succeeds, and it checks them in a predefined order <code>cman</code>, <code>corosync</code>, <code>openais</code>. The available managers will be listed by order as part of the <code>clvmd -h</code> output.</p>
<dt> <code>-R</code></p>
<dd>
<dd>Tells all the running instance of <code>clvmd</code> in the cluster to reload their device cache and re-read the lvm configuration file <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5). This command should be run whenever the devices on a cluster system are changed.</p>
<dt> <code>-S</code></p>
<dd>
<dd>Tells the running <code>clvmd</code> to exit and reexecute itself, for example at the end of a package upgrade. The new instance is instructed to reacquire any locks in the same state as they were previously held. (Alternative methods of restarting the daemon have the side effect of changing exclusive LV locks into shared locks.)</p>
<dt> <code>-t</code> <i>timeout</i></p>
<dd>
<dd>Specifies the <i>timeout</i> for commands to run around the cluster. This should not be so small that commands with many disk updates to do will fail, so you may need to increase this on systems with very large disk farms. The default is 60 seconds.</p>
<dt> <code>-T</code> <i>start_timeout</i></p>
<dd>
<dd>Specifies the start timeout for <code>clvmd</code> daemon startup. If the daemon does not report that it has started up within this time then the parent command will exit with status of 5. This does NOT mean that <code>clvmd</code> has not started! What it means is that the startup has been delayed for some reason; the most likely cause of this is an inquorate cluster though it could be due to locking latencies on a cluster with large numbers of logical volumes. If you get the return code of 5 it is usually not necessary to restart <code>clvmd</code> it will start as soon as that blockage has cleared. This flag is to allow startup scripts to exit in a timely fashion even if the cluster is stalled for some reason. </p>
<p> The default is <code>0</code> (no timeout) and the value is in seconds. Don&#8217;t set this too small or you will experience spurious errors. 10 or 20 seconds might be sensible. </p>
<p> This timeout will be ignored if you start <code>clvmd</code> with the <code>-d</code>.</p>
<dt> <code>-V</code></p>
<dd>
<dd>Display the version of the cluster LVM daemon.</dl>
<h2>Environment Variables</h2>
<dl>
<dt><code>LVM_CLVMD_BINARY</code></p>
<dd>The CLVMD binary to use when <code>clvmd</code> restart is requested. Defaults to <i>/usr/sbin/clvmd</i>.</p>
<dt><code>LVM_BINARY</code></p>
<dd>The LVM2 binary to use. Defaults to <i>/usr/sbin/lvm</i>.</dl>
<h2>Files</h2>
<p><i>/usr/sbin/clvmd</i><br />
 <i>/usr/sbin/lvm</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3), <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5), <code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8) </p>
