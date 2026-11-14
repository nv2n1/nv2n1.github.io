---
title: "ha_logger(1)"
name: "ha_logger"
section: "1"
letter: "h"
url: "/docs/linux/man/1-ha_logger/"
description: "ha_logger – Log a message to files/syslog through the HA Logging Daemon"
---

<h2>NAME</h2>
<p> <code>ha_logger </code> &#8211; Log a message to files/syslog through the HA Logging Daemon</p>
<h2>SYNOPSIS</h2>
<p> <code>ha_logger</code> [-D ha-log/ha-debug] [-t tag] [message &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>ha_logger </code> is used to log a message to files/syslog through the HA Logging Daemon </p>
<dl>
<dt><code>-D</code> <i>ha-log/ha-debug</i></p>
<dd> Log the message to different files. Ha-log will log the message to the log file and the debug file, while ha-debug will log the message to the debug file only.</p>
<dt><code>-t</code> <i>tag</i></p>
<dd> Mark every line in the log with the specified</p>
<dt><code>message</code></p>
<dd> The message you want to log on.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-ha_logd/">ha_logd</a>(8) <a href="/docs/linux/man/8-heartbeat/">heartbeat</a>(8) </p>
<h2>DOCUMENTATION</h2>
<p> More information may be found at <a rel="nofollow" href="http://www.linux-ha.org/">http://www.linux-ha.org/</a> </p>
<h2>AUTHORS</h2>
<pre><code>
Guochun Shi&lt;gshi[at] ncsa.uiuc.edu&gt;
        Alan Robertson&lt;alanr[at] unix.sh&gt;
            Lars Marowsky - Bree&lt;lmb[at] suse.de&gt;
</code></pre>
<h2>Index</h2>
