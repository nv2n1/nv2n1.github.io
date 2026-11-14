---
title: "oddjobd(8)"
name: "oddjobd"
section: "8"
letter: "o"
url: "/docs/linux/man/8-oddjobd/"
description: "oddjobd – privileged operations for unprivileged processes"
---

<p>oddjobd &#8211; privileged operations for unprivileged processes</p>
<h2>Synopsis</h2>
<p>oddjobd [-n] [-d] [-p pidfile] [-c configfile] [-S] [-t timeout] </p>
<h2>Description</h2>
<p>The <i>oddjobd</i> daemon provides the com.redhat.oddjob service on the system-wide message bus. Each facility which <i>oddjobd</i> provides is provided as a separate D-Bus method. Any method can be invoked by name by any user, subject to access controls enforced by both D-Bus and <i>oddjobd</i>. Most methods are implemented as helper programs. </p>
<h2>Options</h2>
<dl>
<dt>-n</p>
<dd>Do not fork and become a daemon process.</p>
<dt>-d</p>
<dd>Print debugging messages to stderr. Implies <code>-n</code>.</p>
<dt>-p pidfile</p>
<dd>Store the daemon&#8217;s process ID in the named file.</p>
<dt>-c /etc/oddjobd.conf</p>
<dd>Read the daemon&#8217;s configuration from the named file.</p>
<dt>-S</p>
<dd>Connect to the session bus instead of the system bus. Used for testing only.</p>
<dt>-t timeout</p>
<dd>Specifies the amount of time which will pass between attempts to reconnect to the bus if oddjobd is disconnected for any reason. If the specified timeout is above 5, then oddjobd will first attempt to connect up to 10 times at intervals of 5 seconds. The default reconnect timeout is 30 seconds. </p>
</dl>
<h2>Signals</h2>
<dl>
<dt>SIGHUP</p>
<dd>Reload the configuration. Client requests which are in the process of being served will run to completion even if the newly-loaded configuration does not include the service, object, interface, or method. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-oddjob_request/">oddjob_request</a></code>(1) <code><a href="/docs/linux/man/5-oddjob-conf/">oddjob.conf</a></code>(5) <code><a href="/docs/linux/man/5-oddjobd-conf/">oddjobd.conf</a></code>(5) </p>
