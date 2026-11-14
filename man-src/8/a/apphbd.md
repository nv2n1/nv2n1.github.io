---
title: "apphbd(8)"
name: "apphbd"
section: "8"
letter: "a"
url: "/docs/linux/man/8-apphbd/"
description: "apphbd – Application Heartbeat Monitor for High-Availability Linux"
---

<p>apphbd &#8211; Application Heartbeat Monitor for High-Availability Linux</p>
<h2>Synopsis</h2>
<p><code>apphbd</code> [ -srkdh ] [ -c configure file ]</p>
<h2>Description</h2>
<p><code>apphbd</code> is a basic application heartbeat monitor daemon for Linux-HA. A group of Application Heartbeat APIs are defined for this heartbeat monitoring service. Applications may register with the daemon in order to be monitored. If an application fails to send a heartbeat within the specified interval, the daemon will log an event. apphbd may use watchdog timer to monitor itself. apphbd extends its functionality by using plugins. Currently a plugin <code>recmgr</code> is implemented to notify Recovery Manager daemon if some events (specified in apphb_notify.h) happen (e.g. an application fails to heartbeat). The Recovery Manager daemon <code>recoverymgrd</code> receives notification from recmgr plugin, then it tries to execute recovery scripts as configured. See recoverymgrd default configure file recoverymgrd.conf for detail. recoverymgrd registers itself with apphbd as a client application. apphbd should be started first with plugin recmgr loaded. Then configure and start recoverymgrd. For details relating to the Application Heartbeat API, see <code>apphb.h</code> . </p>
<h2>Options</h2>
<dl>
<dt>-s</p>
<dd>Show the status of apphbd, running or stopped.</p>
<dt>-k</p>
<dd>Stop (kill) the daemon</p>
<dt>-r</p>
<dd>Restart the daemon. apphbd will reload configure file when restarted.</p>
<dt>-d</p>
<dd>Set debug level</p>
<dt>-h</p>
<dd>Show help message</p>
<dt>-c configure file</p>
<dd>Configure file for apphbd. Default configure file is <code>./apphbd.cf</code>. User can configure debug setting, log file, watchdog setting, plugins and real time setting. For details, see sample configure file apphbd.cf.</dl>
<h2>Files</h2>
<p><i>/var/run/apphbd.pid </i> Default PID file. </p>
<p> <i>apphbd.cf </i> Default configure file for apphbd. apphbd searches the file in its working directory. This sample configure file is installed together with other Heartbeat documents. </p>
<p> <i>apphb.h</i> Header for Application Heartbeat API. </p>
<p> <i>recoverymgrd.conf</i> Default configure file for recoverymgrd. recoverymgrd searches the file in its working directory. Other configure file can also be specified in the command line. This sample configure file is installed together with other Heartbeat documents. </p>
<p> <i>/usr/lib/heartbeat/plugins/AppHBNotification</i> Directory contains plugins for apphbd.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-heartbeat/">heartbeat</a>(8) </p>
<h2>Documentation</h2>
<p>More information may be found at <a rel="nofollow" href="http://www.linux-ha.org.">http://www.linux-ha.org.</a></p>
<h2>Authors</h2>
<pre>apphbd - Alan Robertson &lt;alanr [at] unix.sh&gt; et al.
recoverymgrd - Andrea Brugger &lt;andrea.l.brugger [at] intel.com&gt; et al.
man page - Andrea Brugger &lt;andrea.l.brugger [at] intel.com&gt;
 - Adam Li &lt;adam.li [at] intel.com&gt;</pre>
