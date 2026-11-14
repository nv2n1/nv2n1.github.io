---
title: "lvmetad(8)"
name: "lvmetad"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lvmetad/"
description: "lvmetad — LVM metadata cache daemon"
---

<p>lvmetad &#8212; LVM metadata cache daemon</p>
<h2>Synopsis</h2>
<p><code>lvmetad</code> [<code>-l</code> <i>level</i>[,level&#8230;]] [<code>-p</code> <i>pidfile_path</i>] [<code>-s</code> <i>socket_path</i>] [<code>-t</code> <i>timeout_value</i>] [<code>-f</code>] [<code>-h</code>] [<code>-V</code>] [<code>-?</code>] </p>
<h2>Description</h2>
<p>The lvmetad daemon caches LVM metadata so that LVM commands can read metadata from the cache rather than scanning disks. This can be an advantage because scanning disks is time consuming and may interfere with the normal work of the system. lvmetad can be a disadvantage when disk event notifications from the system are unreliable. lvmetad does not read metadata from disks itself. Instead, it relies on an LVM command, like pvscan &#8211;cache, to read metadata from disks and send it to lvmetad to be cached. New LVM disks that appear on the system must be scanned before lvmetad knows about them. If lvmetad does not know about a disk, then LVM commands using lvmetad will also not know about it. When disks are added or removed from the system, lvmetad must be updated. lvmetad is usually combined with event-based system services that automatically run pvscan &#8211;cache on disks added or removed. This way, the cache is automatically updated with metadata from new disks when they appear. LVM udev rules and systemd services implement this automation. Automatic scanning is usually combined with automatic activation. For more information, see <code><a href="/docs/linux/man/8-pvscan/">pvscan</a></code>(8). If lvmetad is started or restarted after disks have been added to the system, or if the global_filter has changed, the cache must be updated. This can be done by running pvscan &#8211;cache, or it will be done automatically by the next LVM command that&#8217;s run. When lvmetad is not used, LVM commands revert to scanning disks for LVM metadata. In some cases, lvmetad will be temporarily disabled while it continues running. In this state, LVM commands will ignore the lvmetad cache and revert to scanning disks. A warning will also be printed which includes the reason why lvmetad is not being used. The most common reasons are the existence of duplicate PVs (lvmetad cannot cache data for duplicate PVs), or an &#8216;lvconvert &#8211;repair&#8217; command has been run (the lvmetad cache may not be reliable while repairs are neeeded.) Once duplicates have been resolved, or repairs have been completed, the lvmetad cache is can be updated with pvscan &#8211;cache and commands will return to using the cache. Use of lvmetad is enabled/disabled by:<br />
 <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) <code>global/use_lvmetad</code> For more information on this setting, see:<br />
 <code>lvmconfig &#8211;withcomments global/use_lvmetad</code> To ignore disks from LVM at the system level, e.g. lvmetad, pvscan use:<br />
 <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5) <code>devices/global_filter</code> For more information on this setting, see<br />
 <code>lvmconfig &#8211;withcomments devices/global_filter</code> </p>
<h2>Options</h2>
<p>To run the daemon in a test environment both the pidfile_path and the socket_path should be changed from the defaults.</p>
<dl>
<dt><code>-f</code></p>
<dd>Don&#8217;t fork, but run in the foreground.</p>
<dt><code>-h</code>, <code>-?</code></p>
<dd>Show help information.</p>
<dt><code>-l </code><i>levels</i></p>
<dd>Specify the levels of log messages to generate as a comma separated list. Messages are logged by syslog. Additionally, when -f is given they are also sent to standard error. Possible levels are: all, fatal, error, warn, info, wire, debug.</p>
<dt><code>-p </code><i>pidfile_path</i></p>
<dd>Path to the pidfile. This overrides both the built-in default (/run/lvmetad.pid) and the environment variable <code>LVM_LVMETAD_PIDFILE</code>. This file is used to prevent more than one instance of the daemon running simultaneously.</p>
<dt><code>-s </code><i>socket_path</i></p>
<dd>Path to the socket file. This overrides both the built-in default (/run/lvm/lvmetad.socket) and the environment variable <code>LVM_LVMETAD_SOCKET</code>. To communicate successfully with lvmetad, all LVM2 processes should use the same socket path.</p>
<dt><code>-t </code><i>timeout_value</i></p>
<dd>The daemon may shutdown after being idle for the given time (in seconds). When the option is omitted or the value given is zero the daemon never shutdowns on idle.</p>
<dt><code>-V</code></p>
<dd>Display the version of lvmetad daemon.</dl>
<h2>Environment Variables</h2>
<dl>
<dt><code>LVM_LVMETAD_PIDFILE</code></p>
<dd>Path for the pid file.</p>
<dt><code>LVM_LVMETAD_SOCKET </code></p>
<dd>Path for the socket file. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lvm/">lvm</a></code>(8), <code><a href="/docs/linux/man/8-lvmconfig/">lvmconfig</a></code>(8), <code><a href="/docs/linux/man/5-lvm-conf/">lvm.conf</a></code>(5), <code><a href="/docs/linux/man/8-pvscan/">pvscan</a></code>(8) </p>
