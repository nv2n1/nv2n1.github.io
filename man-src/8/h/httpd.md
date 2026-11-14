---
title: "httpd(8)"
name: "httpd"
section: "8"
letter: "h"
url: "/docs/linux/man/8-httpd/"
description: "httpd – Apache Hypertext Transfer Protocol Server"
---

<p>httpd &#8211; Apache Hypertext Transfer Protocol Server</p>
<h2>Synopsis</h2>
<p> <code>httpd</code> [ &#8211;<code>d</code> <i>serverroot</i> ] [ &#8211;<code>f</code> <i>config</i> ] [ &#8211;<code>C</code> <i>directive</i> ] [ &#8211;<code>c</code> <i>directive</i> ] [ &#8211;<code>D</code> <i>parameter</i> ] [ &#8211;<code>e</code> <i>level</i> ] [ &#8211;<code>E</code> <i>file</i> ] [ <code>-k</code> start|restart|graceful|stop|graceful-stop ] [ &#8211;<code>R</code> <i>directory</i> ] [ &#8211;<code>h</code> ] [ &#8211;<code>l</code> ] [ &#8211;<code>L</code> ] [ &#8211;<code>S</code> ] [ &#8211;<code>t</code> ] [ &#8211;<code>v</code> ] [ &#8211;<code>V</code> ] [ &#8211;<code>X</code> ] [ &#8211;<code>M</code> ] [ &#8211;<code>T</code> ]<br />
&nbsp;<wbr> On Windows systems, the following additional arguments are available:<br />
&nbsp;<wbr> <code>httpd</code> [ &#8211;<code>k</code> install|config|uninstall ] [ &#8211;<code>n</code> <i>name</i> ] [ &#8211;<code>w</code> ]<br />
&nbsp;<wbr> </p>
<h2>Summary</h2>
<p>&nbsp;<wbr> </p>
<p> httpd is the Apache HyperText Transfer Protocol (HTTP) server program. It is designed to be run as a standalone daemon process. When used like this it will create a pool of child processes or threads to handle requests.<br />
&nbsp;<wbr> </p>
<p> In general, httpd should not be invoked directly, but rather should be invoked via apachectl on Unix-based systems or as a service on Windows NT, 2000 and XP and as a console application on Windows 9x and ME.<br />
&nbsp;<wbr></p>
<h2>Options</h2>
<p>&nbsp;<wbr><br />
&nbsp;<wbr></p>
<dl>
<dt>-d <i>serverroot</i></p>
<dd>Set the initial value for the ServerRoot directive to <i>serverroot</i>. This can be overridden by the ServerRoot directive in the configuration file. The default is /etc/httpd.</p>
<dt>-f <i>config</i></p>
<dd>Uses the directives in the file <i>config</i> on startup. If <i>config</i> does not begin with a /, then it is taken to be a path relative to the ServerRoot. The default is conf/httpd.conf.</p>
<dt>-k start|restart|graceful|stop|graceful-stop</p>
<dd>Signals httpd to start, restart, or stop. See Stopping Apache httpd for more information.</p>
<dt>-C <i>directive</i></p>
<dd>Process the configuration <i>directive</i> before reading config files.</p>
<dt>-c <i>directive</i></p>
<dd>Process the configuration <i>directive</i> after reading config files.</p>
<dt>-D <i>parameter</i></p>
<dd>Sets a configuration <i>parameter </i>which can be used with &lt;IfDefine&gt; sections in the configuration files to conditionally skip or process commands at server startup and restart. Also can be used to set certain less-common startup parameters including -DNO_DETACH (prevent the parent from forking) and -DFOREGROUND (prevent the parent from calling setsid() et al).</p>
<dt>-e <i>level</i></p>
<dd>Sets the LogLevel to <i>level</i> during server startup. This is useful for temporarily increasing the verbosity of the error messages to find problems during startup.</p>
<dt>-E <i>file</i></p>
<dd>Send error messages during server startup to <i>file</i>.</p>
<dt>-h</p>
<dd>Output a short summary of available command line options.</p>
<dt>-l</p>
<dd>Output a list of modules compiled into the server. This will <code>not</code> list dynamically loaded modules included using the LoadModule directive.</p>
<dt>-L</p>
<dd>Output a list of directives provided by static modules, together with expected arguments and places where the directive is valid. Directives provided by shared modules are not listed.</p>
<dt>-M</p>
<dd>Dump a list of loaded Static and Shared Modules.</p>
<dt>-S</p>
<dd>Show the settings as parsed from the config file (currently only shows the virtualhost settings).</p>
<dt>-T (Available in 2.3.8 and later)</p>
<dd>Skip document root check at startup/restart.</p>
<dt>-t</p>
<dd>Run syntax tests for configuration files only. The program immediately exits after these syntax parsing tests with either a return code of 0 (Syntax OK) or return code not equal to 0 (Syntax Error). If -D <i>DUMP</i>_<i>VHOSTS </i>is also set, details of the virtual host configuration will be printed. If -D <i>DUMP</i>_<i>MODULES </i> is set, all loaded modules will be printed.</p>
<dt>-v</p>
<dd>Print the version of httpd, and then exit.</p>
<dt>-V</p>
<dd>Print the version and build parameters of httpd, and then exit.</p>
<dt>-X</p>
<dd>Run httpd in debug mode. Only one worker will be started and the server will not detach from the console.<br />
&nbsp;<wbr></dl>
<p> The following arguments are available only on the Windows platform:<br />
&nbsp;<wbr><br />
&nbsp;<wbr></p>
<dl>
<dt>-k install|config|uninstall</p>
<dd>Install Apache httpd as a Windows NT service; change startup options for the Apache httpd service; and uninstall the Apache httpd service.</p>
<dt>-n <i>name</i></p>
<dd>The <i>name</i> of the Apache httpd service to signal.</p>
<dt>-w</p>
<dd>Keep the console window open on error so that the error message can be read.<br />
&nbsp;<wbr> </p>
</dl>
