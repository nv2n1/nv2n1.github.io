---
title: "apachectl(8)"
name: "apachectl"
section: "8"
letter: "a"
url: "/docs/linux/man/8-apachectl/"
description: "apache2ctl – Apache HTTP server control interface"
---

<p>apache2ctl &#8211; Apache HTTP server control interface</p>
<h2>Synopsis</h2>
<p>When acting in SysV init mode, apache2ctl takes simple, one-word commands, defined below. <code>apachectl </code> <i>command</i> <code>apache2ctl </code> <i>command</i> When acting in pass-through mode, apache2ctl can take all the arguments available for the httpd binary. <code>apachectl </code> [<i>httpd-argument</i>] <code>apache2ctl </code> [<i>httpd-argument</i>] </p>
<h2>Description</h2>
<p><code>apache2ctl</code> is a front end to the Apache HyperText Transfer Protocol (HTTP) server. It is designed to help the administrator control the functioning of the Apache <code>apache2</code> daemon. <code>NOTE: </code> The default Debian configuration requires the environment variables <code>APACHE_RUN_USER</code>, <code>APACHE_RUN_GROUP</code>, and <code>APACHE_PID_FILE</code> to be set in <code>/etc/apache2/envvars</code>. The <code>apache2ctl</code> script returns a 0 exit value on success, and &gt;0 if an error occurs. For more details, view the comments in the script. </p>
<h2>Options</h2>
<p>The <i>command</i> can be any one or more of the following options:</p>
<dl>
<dt><code>start</code></p>
<dd>Start the Apache daemon. Gives an error if it is already running.</p>
<dt><code>stop</code></p>
<dd>Stops the Apache daemon.</p>
<dt><code>restart</code></p>
<dd>Restarts the Apache daemon by sending it a SIGHUP. If the daemon is not running, it is started. This command automatically checks the configuration files via <code>configtest</code> before initiating the restart to to catch the most obvious errors. However, it is still possible for the daemon to die because of problems with the configuration.</p>
<dt><code>fullstatus</code></p>
<dd>Displays a full status report from <code>mod_status. </code> For this to work, you need to have mod_status enabled on your server and a text-based browser such as <i>lynx</i> available on your system. The URL used to access the status report can be set by setting the <code>APACHE_STATUSURL</code> variable in <code>/etc/apache2/envvars</code>.</p>
<dt><code>status</code></p>
<dd>Displays a brief status report. Similar to the fullstatus option, except that the list of requests currently being served is omitted.</p>
<dt><code>graceful</code></p>
<dd>Gracefully restarts the Apache daemon by sending it a SIGUSR1. If the daemon is not running, it is started. This differs from a normal restart in that currently open connections are not aborted. A side effect is that old log files will not be closed immediately. This means that if used in a log rotation script, a substantial delay may be necessary to ensure that the old log files are closed before processing them. This command automatically checks the configuration files via apache2ctl configtest before initiating the restart to to catch the most obvious errors. However, it is still possible for the daemon to die because of problems with the configuration.</p>
<dt><code>graceful-stop</code></p>
<dd>Gracefully stops the Apache httpd daemon. This differs from a normal stop in that currently open connections are not aborted. A side effect is that old log files will not be closed immediately.</p>
<dt><code>configtest</code></p>
<dd>Run a configuration file syntax test. It parses the configuration files and either reports <code>Syntax Ok</code> or information about the particular syntax error. This test does not catch all errors.</p>
<dt><code>help</code></p>
<dd>Displays a short help message.</p>
<dt>The following option was available in earlier versions but has been removed.</p>
<dd>
<dt><code>startssl</code></p>
<dd>To start httpd with SSL support, you should edit your configuration file to include the relevant directives and then use the normal apache2ctl start.</dl>
<h2>Environment</h2>
<p>The behaviour of <code>apache2ctl</code> can be influenced with these environment variables: <code>APACHE_HTTPD</code>, <code>APACHE_LYNX</code>, <code>APACHE_STATUSURL</code>, <code>APACHE_ULIMIT_MAX_FILES</code>, <code>APACHE_RUN_DIR</code>, <code>APACHE_LOCK_DIR</code>, <code>APACHE_RUN_USER</code>, <code>APACHE_ARGUMENTS</code>, <code>APACHE_ENVVARS</code>. See the comments in the script for details. These variables (except <code>APACHE_ENVVARS</code>) can be set in <code>/etc/apache2/envvars</code>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-apache2/">apache2</a>(8)</code>, <code>/usr/share/doc/apache2/README.Debian.gz</code> </p>
