---
title: "zarafa-spooler(1)"
name: "zarafa-spooler"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zarafa-spooler/"
description: "zarafa-spooler – Start the Zarafa spooler."
---

<h2 class="name">NAME</h2>
<p> zarafa-spooler &#8211; Start the Zarafa spooler. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>zarafa-spooler</code> [<i>OPTION</i>&#8230;] [<i>SERVERNAME</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>The spooler sends all pending Zarafa e-mail to the recipients. When started, the program will keep running and sending messages whenever needed. </p>
<p> The outgoing mailserver can be overwritten from the config file by specifying this on the commandline. </p>
<p> The default settings of the spooler program are defined in <code><a href="/docs/linux/man/5-zarafa-spooler-cfg/">zarafa-spooler.cfg</a></code>(5).</p>
<h2>OPTIONS</h2>
<p> Various options are possible. None of these options are required. </p>
<p> <code>&#8211;config</code>, <code>-c</code> <i>spooler.cfg</i></p>
<dl>
<dt>
<dd> Specify the location of the spooler.cfg file. If the spooler.cfg file is not specified, the spooler will try to load /etc/zarafa/spooler.cfg. If that file is not present, it will continue using it&#8217;s default settings.</dl>
<p> <code>&#8211;host</code>, <code>-h</code> <i>path</i></p>
<dl>
<dt>
<dd> Connect to the Zarafa server through <i>path</i>, e.g. file:///path/to/socket. Default: file:///var/run/zarafa. Overrides the config file setting.</dl>
<p> <code>&#8211;foreground</code>, <code>-F</code></p>
<dl>
<dt>
<dd> Run in the foreground. Normally the spooler will daemonize and run in the background.</dl>
<p> <code>&#8211;ignore-unknown-config-options</code></p>
<dl>
<dt>
<dd> When unknown options exists in the configuration file the spooler will report an error and shutdown. Pass this option to ignore unknown options so the spooler will start.</dl>
<h2>USAGE</h2>
<p> To start the spooler delivering e-mail to recipients: </p>
<p> <code>zarafa-spooler</code> </p>
<p> To start the spooler delivering e-mail through smtp.example.com: </p>
<p> <code>zarafa-spooler</code>smtp.example.com </p>
<p> The spooler process will keep running and watching the outgoing queue for new mail to send. You may also use the init.d scripts: </p>
<p> <code>/etc/init.d/zarafa-spooler</code> [<i>start</i>| <i>stop</i>| <i>restart</i>]</p>
<h2>SIGNALS</h2>
<p> The following signals can be sent to the zarafa-spooler process: </p>
<p> <code>HUP</code></p>
<dl>
<dt>
<dd> When the HUP signal is received, some options from the configuration file are reloaded. The reloadable options are listed in the <code><a href="/docs/linux/man/5-zarafa-spooler-cfg/">zarafa-spooler.cfg</a></code>(5) manual page. </p>
<p> Also, when using <i>log_method = file</i>, the logfile will be closed and a new logfile will be opened. You can use this signal in your logrotate system.</dl>
<p> <code>TERM</code></p>
<dl>
<dt>
<dd> To gracefully let the service exit, the normal TERM signal is used. Because of multiple running threads, it may take up to 60 seconds for the server to completely shutdown.</dl>
<h2>AUTHOR</h2>
<p> Written by Zarafa.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-zarafa-spooler-cfg/">zarafa-spooler.cfg</a></code>(5)<code><a href="/docs/linux/man/1-zarafa-server/">zarafa-server</a></code>(1) </p>
<h2>Index</h2>
