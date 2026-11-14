---
title: "dmeventd(8)"
name: "dmeventd"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dmeventd/"
description: "dmeventd — Device-mapper event daemon"
---

<p>dmeventd &#8212; Device-mapper event daemon</p>
<h2>Synopsis</h2>
<p><code>dmeventd</code> [<code>-d</code> [<code>-d</code> [<code>-d</code>]]] [<code>-f</code>] [<code>-h</code>] [<code>-l</code>] [<code>-R</code>] [<code>-V</code>] [<code>-?</code>]</p>
<h2>Description</h2>
<p>dmeventd is the event monitoring daemon for device-mapper devices. Library plugins can register and carry out actions triggered when particular events occur.</p>
<h2>Options</h2>
<dl>
<dt> <code>-d</code></p>
<dd>
<dd>Repeat from 1 to 3 times ( <code>-d</code>, <code>-dd</code>, <code>-ddd</code> ) to increase the detail of debug messages sent to syslog. Each extra d adds more debugging information.</p>
<dt> <code>-f</code></p>
<dd>
<dd>Don&#8217;t fork, run in the foreground.</p>
<dt> <code>-h</code></p>
<dd>
<dd>Show help information.</p>
<dt> <code>-l</code></p>
<dd>
<dd>Log through stdout and stderr instead of syslog. This option works only with option -f, otherwise it is ignored.</p>
<dt> <code>-?</code></p>
<dd>
<dd>Show help information on stderr.</p>
<dt> <code>-R</code></p>
<dd>
<dd>Replace a running dmeventd instance. The running dmeventd must be version 2.02.77 or newer. The new dmeventd instance will obtain a list of devices and events to monitor from the currently running daemon.</p>
<dt> <code>-V</code></p>
<dd>
<dd>Show version of dmeventd.</dl>
<h2>Lvm Plugins</h2>
<dl>
<dt> <code>Mirror</code></p>
<dd>
<dd>Attempts to handle device failure automatically. See <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5).</p>
<dt> <code>Raid</code></p>
<dd>
<dd>Attempts to handle device failure automatically. See <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5).</p>
<dt> <code>Snapshot</code></p>
<dd>
<dd>Monitors how full a snapshot is becoming and emits a warning to syslog when it exceeds 80% full. The warning is repeated when 85%, 90% and 95% of the snapshot is filled. See <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5). Snapshot which runs out of space gets invalid and when it is mounted, it gets umounted if possible.</p>
<dt> <code>Thin</code></p>
<dd>
<dd>Monitors how full a thin pool data and metadata is becoming and emits a warning to syslog when it exceeds 80% full. The warning is repeated when more then 85%, 90% and 95% of the thin pool is filled. See <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5). When a thin pool fills over 50% (data or metadata) thin plugin calls configured <i>dmeventd/thin_command</i> with every 5% increase. With default setting it calls internal <code>lvm lvextend &#8211;use-policies</code> to resize thin pool when it&#8217;s been filled above configured threshold <i>activation/thin_pool_autoextend_threshold</i>. If the command fails, dmeventd thin plugin will keep retrying execution with increasing time delay between retries upto 42 minutes. User may also configure external command to support more advanced maintenance operations of a thin pool. Such external command can e.g. remove some unneeded snapshots, use <code><a href="/docs/linux/man/8-fstrim/">fstrim</a></code>(8) to free recover space in a thin pool, but also can use <code>lvextend &#8211;use-policies</code> if other actions have not released enough space. Command is executed with environmental variable <code>LVM_RUN_BY_DMEVENTD=1</code> so any lvm2 command executed in this environment will not try to interact with dmeventd. To see the fullness of a thin pool command may check these two environmental variables <code>DMEVENTD_THIN_POOL_DATA</code> and <code>DMEVENTD_THIN_POOL_METADATA</code>. Command can also read status with tools like <code><a href="/docs/linux/man/8-lvs/">lvs</a></code>(8). </p>
<dt> <code>Vdo</code></p>
<dd>
<dd>Monitors how full a VDO pool data is becoming and emits a warning to syslog when it exceeds 80% full. The warning is repeated when more then 85%, 90% and 95% of the VDO pool is filled. See <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5). When a VDO pool fills over 50% vdo plugin calls configured <i>dmeventd/vdo_command</i> with every 5% increase. With default setting it calls internal <code>lvm lvextend &#8211;use-policies</code> to resize VDO pool when it&#8217;s been filled above the configured threshold <i>activation/vdo_pool_autoextend_threshold</i>. If the command fails, dmeventd vdo plugin will keep retrying execution with increasing time delay between retries upto 42 minutes. User may also configure external command to support more advanced maintenance operations of a VDO pool. Such external command can e.g. remove some unneeded space with <code><a href="/docs/linux/man/8-fstrim/">fstrim</a></code>(8), but also can use <code>lvextend &#8211;use-policies</code> if other actions have not released enough space. Command is executed with environmental variable <code>LVM_RUN_BY_DMEVENTD=1</code> so any lvm2 command executed in this environment will not try to interact with dmeventd. To see the fullness of a VDO pool command may check this environmental variable <code>DMEVENTD_VDO_POOL</code>. Command can also read status with tools like <code><a href="/docs/linux/man/8-lvs/">lvs</a></code>(8).</dl>
<h2>Environment Variables</h2>
<dl>
<dt><code>DMEVENTD_THIN_POOL_DATA</code></p>
<dd>Variable is set by thin plugin and is available to executed program. Value present actual usage of thin pool data volume. Variable is not set when error event is processed.</p>
<dt><code>DMEVENTD_THIN_POOL_METADATA</code></p>
<dd>Variable is set by thin plugin and is available to executed program. Value present actual usage of thin pool metadata volume. Variable is not set when error event is processed.</p>
<dt><code>DMEVENTD_VDO_POOL</code></p>
<dd>Variable is set by vdo plugin and is available to executed program. Value present actual usage of VDO pool data volume. Variable is not set when error event is processed.</p>
<dt><code>LVM_RUN_BY_DMEVENTD</code></p>
<dd>Variable is set by thin and vdo plugin to prohibit recursive interation with dmeventd by any executed lvm2 command from a thin_command, vdo_command environment.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8), <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) </p>
