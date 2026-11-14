---
title: "zarafa-gateway(1)"
name: "zarafa-gateway"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zarafa-gateway/"
description: "zarafa-gateway – Start the Zarafa IMAP/POP3 Gateway."
---

<h2 class="name">NAME</h2>
<p> zarafa-gateway &#8211; Start the Zarafa IMAP/POP3 Gateway. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>zarafa-gateway</code> [<i>OPTION</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>The gateway enables other e-mail clients to connect through POP3 or IMAP to the Zarafa server to read their e-mail. With IMAP, it is also possible to view the contents of other folders and subfolders. The gateway can be configured to listen for POP3, POP3S, IMAP and/or IMAPS. </p>
<p> The default settings of the gateway program are defined in <code><a href="/docs/linux/man/5-zarafa-gateway-cfg/">zarafa-gateway.cfg</a></code>(5).</p>
<h2>OPTIONS</h2>
<p> Various options are possible. None of these options are required. </p>
<p> <code>&#8211;config</code>, <code>-c</code> <i>gateway.cfg</i></p>
<dl>
<dt>
<dd> Specify the location of the gateway.cfg file. If the gateway.cfg file is not specified, the gateway will continue using its default settings. </p>
<p> Default: <i>/etc/zarafa/gateway.cfg</i></dl>
<p> <code>&#8211;host</code>, <code>-h</code> <i>path</i></p>
<dl>
<dt>
<dd> Connect to the Zarafa server through <i>path</i>, e.g. file:///path/to/socket. Default: file:///var/run/zarafa. Overrides the config file setting.</dl>
<p> <code>&#8211;foreground</code>, <code>-F</code></p>
<dl>
<dt>
<dd> Run in the foreground. Normally the gateway will daemonize and run in the background.</dl>
<p> <code>&#8211;ignore-unknown-config-options</code></p>
<dl>
<dt>
<dd> When unknown options exists in the configuration file the gateway will report an error and shutdown. Pass this option to ignore unknown options so the gateway will start.</dl>
<h2>SIGNALS</h2>
<p> The following signals can be sent to the zarafa-gateway process: </p>
<p> <code>HUP</code></p>
<dl>
<dt>
<dd> When the HUP signal is received, some options from the configuration file are reloaded. The reloadable options are listed in the <code><a href="/docs/linux/man/5-zarafa-gateway-cfg/">zarafa-gateway.cfg</a></code>(5) manual page. </p>
<p> Also, when using <i>log_method = file</i>, the logfile will be closed and a new logfile will be opened. You can use this signal in your logrotate system.</dl>
<p> <code>TERM</code></p>
<dl>
<dt>
<dd> To gracefully let the service exit, the normal TERM signal is used.</dl>
<h2>USAGE</h2>
<p> To start the gateway: </p>
<p> <code>zarafa-gateway</code> </p>
<p> The gateway process will keep running. You may also use the init.d scripts: </p>
<p> <code>/etc/init.d/zarafa-gateway</code> [<i>start</i>| <i>stop</i>| <i>restart</i>]</p>
<h2>AUTHOR</h2>
<p> Written by Zarafa.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-zarafa-gateway-cfg/">zarafa-gateway.cfg</a></code>(5)<code><a href="/docs/linux/man/1-zarafa-server/">zarafa-server</a></code>(1) </p>
<h2>Index</h2>
