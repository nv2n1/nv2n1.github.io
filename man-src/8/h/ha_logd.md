---
title: "ha_logd(8)"
name: "ha_logd"
section: "8"
letter: "h"
url: "/docs/linux/man/8-ha_logd/"
description: "ha_logd – Logging Daemon for High-Availability Linux"
---

<p>ha_logd &#8211; Logging Daemon for High-Availability Linux</p>
<h2>Synopsis</h2>
<p><code>ha_logd</code> [ -skdh ] [ -c configure file ]</p>
<h2>Description</h2>
<p><code>ha_logd</code> is a logging daemon for Linux-HA. It receives messages from a local domain socket <code>/var/lib/log_daemon</code>, writes them to appropriate files and syslog if enabled. The reason the logging daemon is written is that occationally Heartbeat suffers from disk I/O delays. By sending log messages to logging daemon, heatbeat can avoid disk I/O delays. </p>
<h2>Options</h2>
<dl>
<dt>-s</p>
<dd>Show the status of ha_logd, running or stopped.</p>
<dt>-k</p>
<dd>Stop (kill) the daemon</p>
<dt>-d</p>
<dd>Make the logging daemon a daemon</p>
<dt>-h</p>
<dd>Show help message</p>
<dt>-c configure file</p>
<dd>Configure file for ha_logd. User can configure log file, debuf file, log facility, entity and useapphbd.<br />
&nbsp;<wbr>For details, see sample configure file ha_logd.cf.</dl>
<h2>Files</h2>
<p><i>/var/run/ha_logd.pid </i> Default PID file. </p>
<p> <i>ha_logd.cf </i> Sample config file for ha_logd. This file is installed together with other Heartbeat documents.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-heartbeat/">heartbeat</a>(8) <a href="/docs/linux/man/8-ha_logger/">ha_logger</a>(8) </p>
<h2>Documentation</h2>
<p>More information may be found at <a rel="nofollow" href="http://www.linux-ha.org.">http://www.linux-ha.org.</a></p>
<h2>Authors</h2>
<pre> Guochun Shi &lt;gshi [at] ncsa.uiuc.edu&gt;
 Alan Robertson &lt;alanr [at] unix.sh&gt;
 Lars Marowsky-Bree &lt;lmb [at] suse.de&gt; </pre>
