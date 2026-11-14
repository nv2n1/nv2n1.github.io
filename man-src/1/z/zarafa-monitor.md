---
title: "zarafa-monitor(1)"
name: "zarafa-monitor"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zarafa-monitor/"
description: "zarafa-monitor – Start the Zarafa monitor."
---

<h2 class="name">NAME</h2>
<p> zarafa-monitor &#8211; Start the Zarafa monitor. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>zarafa-monitor</code> [<i>OPTION</i>&#8230;] [<i>SERVERNAME</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>The monitor checks user mailbox sizes. When the quota is reached the monitor sends a quota email. When started, the program will keep running. </p>
<p> The defaults can be overwritten in the config file. </p>
<p> The default settings of the monitor program are defined in <code><a href="/docs/linux/man/5-zarafa-monitor-cfg/">zarafa-monitor.cfg</a></code>(5).</p>
<h2>OPTIONS</h2>
<p> Various options are possible. None of these options are required. </p>
<p> <code>&#8211;config</code>, <code>-c</code> <i>monitor.cfg</i></p>
<dl>
<dt>
<dd> Specify the location of the monitor.cfg file. If the monitor.cfg file is not specified, the monitor will try to load /etc/zarafa/monitor.cfg. If that file is not present, it will continue using it&#8217;s default settings. </p>
<p> Default: <i>/etc/zarafa/monitor.cfg</i></dl>
<p> <code>&#8211;host</code>, <code>-h</code> <i>path</i></p>
<dl>
<dt>
<dd> Connect to the Zarafa server through <i>path</i>, e.g. file:///path/to/socket. Default: file:///var/run/zarafa.</dl>
<p> <code>&#8211;foreground</code>, <code>-F</code></p>
<dl>
<dt>
<dd> Run in the foreground. Normally the monitor will daemonize and run in the background.</dl>
<p> <code>&#8211;ignore-unknown-config-options</code></p>
<dl>
<dt>
<dd> When unknown options exists in the configuration file the monitor service will report an error and shutdown. Pass this option to ignore unknown options so the monitor service will start.</dl>
<h2>SIGNALS</h2>
<p> The following signals can be sent to the zarafa-monitor process: </p>
<p> <code>HUP</code></p>
<dl>
<dt>
<dd> When the HUP signal is received, some options from the configuration file are reloaded. The reloadable options are listed in the <code><a href="/docs/linux/man/5-zarafa-monitor-cfg/">zarafa-monitor.cfg</a></code>(5) manual page. </p>
<p> Also, when using <i>log_method = file</i>, the logfile will be closed and a new logfile will be opened. You can use this signal in your logrotate system.</dl>
<p> <code>TERM</code></p>
<dl>
<dt>
<dd> To gracefully let the service exit, the normal TERM signal is used.</dl>
<h2>USAGE</h2>
<p> The monitor checks user mailbox sizes. The monitor sends a quota email when the warning quota limit is reached. When started, the program will keep running. You may also use the init.d scripts: </p>
<p> <code>/etc/init.d/zarafa-monitor</code> [<i>start</i>| <i>stop</i>| <i>restart</i>]</p>
<h2>AUTHOR</h2>
<p> Written by Zarafa.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-zarafa-monitor-cfg/">zarafa-monitor.cfg</a></code>(5)<code><a href="/docs/linux/man/1-zarafa-server/">zarafa-server</a></code>(1) </p>
<h2>Index</h2>
