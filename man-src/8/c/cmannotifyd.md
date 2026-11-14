---
title: "cmannotifyd(8)"
name: "cmannotifyd"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cmannotifyd/"
description: "cmannotifyd – CMAN Notification Daemon"
---

<p>cmannotifyd &#8211; CMAN Notification Daemon</p>
<h2>Synopsis</h2>
<p><code>cmannotifyd [-f] [-d] </code></p>
<h2>Description</h2>
<p>The <code>cmannotifyd</code> daemon talks to CMAN and provides a mechanism to notify external entities about cluster changes. CMAN dispatches 3 kind of notifications: &#8211; CMAN_REASON_TRY_SHUTDOWN when cman requests to all clients if it is allowed to shutdown. &#8211; CMAN_REASON_STATECHANGE when cman detects a node joining or leaving the cluster. &#8211; CMAN_REASON_CONFIG_UPDATE when a configuration change event has been detected/requested. These notifications are then dispatched to the shell script <code>cman_notify </code> in the environment variable CMAN_NOTIFICATION. <code>cman_notify</code> will then execute all the scripts in the configured notification directory (default: /etc/cluster/cman-notify.d) passing a very minimal set of envvars including, of course, the CMAN_NOTIFICATION= type. The execution order is set by the filename as shown by &quot;LC_ALL=C ls -las&quot;. <code>cmannotifyd </code> logs are stored in the default log file (/var/log/cluster/cmannotifyd.log). <code>cman_notify </code> logs are stored in the default log file (/var/log/cluster/cman_notify.log). By default the output from the scripts executed by <code>cman_notify</code> is redirected to /dev/null. Users can either set CMAN_NOTIFICATION_DEBUG=1 in their environment or set proper debug configuration in cluster.conf to redirect scripts output to the cman_notify log file. </p>
<h2>Notes</h2>
<p>cmannotifyd does not block on cman_notify nor check the exit status of the script. Notifications are dispatched in the same order as they arrive, one by one. CMAN_REASON_TRY_SHUTDOWN is passed to scripts for information only, they can not influence cman&#8217;s decsion about whether or not to shut down. CMAN_REASON_STATECHANGE also implies CMAN_NOTIFICATION_QUORUM exported in the environment. CMAN_NOTIFICATION_QUORUM will be set to 1 (when the node is part of a quorate cluster) or 0 (otherwise). A template for cman_notify scripts can be found in the doc/ directory. </p>
<h2>Options</h2>
<dl>
<dt>-f</p>
<dd>Run in the foreground (do not fork / daemonize).</p>
<dt>-d</p>
<dd>Enable debug output. </p>
</dl>
