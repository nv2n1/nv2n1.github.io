---
title: "apache2(8)"
name: "apache2"
section: "8"
letter: "a"
url: "/docs/linux/man/8-apache2/"
description: "apache2 – Apache Hypertext Transfer Protocol Server"
---

<p>apache2 &#8211; Apache Hypertext Transfer Protocol Server</p>
<h2>Synopsis</h2>
<p><code>apache2</code> [ &#8211;<code>d</code> <i>serverroot</i> ] [ &#8211;<code>f</code> <i>config</i> ] [ &#8211;<code>C</code> <i>directive</i> ] [ &#8211;<code>c</code> <i>directive</i> ] [ &#8211;<code>D</code> <i>parameter</i> ] [ &#8211;<code>e</code> <i>level</i> ] [ &#8211;<code>E</code> <i>file</i> ] [ <code>-k</code> start|restart|graceful|stop|graceful-stop ] [ &#8211;<code>R</code> <i>directory</i> ] [ &#8211;<code>h</code> ] [ &#8211;<code>l</code> ] [ &#8211;<code>L</code> ] [ &#8211;<code>S</code> ] [ &#8211;<code>t</code> ] [ &#8211;<code>v</code> ] [ &#8211;<code>V</code> ] [ &#8211;<code>X</code> ] [ &#8211;<code>M</code> ]</p>
<h2>Summary</h2>
<p>apache2 is the Apache HyperText Transfer Protocol (HTTP) server program. It is designed to be run as a standalone daemon process. When used like this it will create a pool of child processes or threads to handle requests. </p>
<p> In general, apache2 should not be invoked directly, but rather should be invoked via /etc/init.d/apache2 or apache2ctl. The default Debian configuration requires environment variables that are defined in /etc/apache2/envvars and are not available if apache2 is started directly. However, apache2ctl can be used to pass arbitrary arguments to apache2.</p>
<h2>Documentation</h2>
<p>The full documentation is available in the apache2-doc package or at <a rel="nofollow" href="http://httpd.apache.org/docs/2.2/">http://httpd.apache.org/docs/2.2/</a> . Information about Debian specific changes and configuration can be found in /usr/share/doc/apache2/README.Debian.gz .</p>
<h2>Options</h2>
<dl>
<dt>-d <i>serverroot</i></p>
<dd>Set the initial value for the ServerRoot directive to <i>serverroot</i>. This can be overridden by the ServerRoot directive in the configuration file.</p>
<dt>-f <i>config</i></p>
<dd>Uses the directives in the file <i>config</i> on startup. If <i>config</i> does not begin with a /, then it is taken to be a path relative to the ServerRoot. The default is /etc/apache2/apache2.conf.</p>
<dt>-k start|restart|graceful|stop|graceful-stop</p>
<dd>Signals apache2 to start, restart, or stop. See Stopping Apache for more information.</p>
<dt>-C <i>directive</i></p>
<dd>Process the configuration <i>directive</i> before reading config files.</p>
<dt>-c <i>directive</i></p>
<dd>Process the configuration <i>directive</i> after reading config files.</p>
<dt>-D <i>parameter</i></p>
<dd>Sets a configuration <i>parameter </i>which can be used with &lt;IfDefine&gt; sections in the configuration files to conditionally skip or process commands at server startup and restart.</p>
<dt>-e <i>level</i></p>
<dd>Sets the LogLevel to <i>level</i> during server startup. This is useful for temporarily increasing the verbosity of the error messages to find problems during startup.</p>
<dt>-E <i>file</i></p>
<dd>Send error messages during server startup to <i>file</i>.</p>
<dt>-R <i>directory</i></p>
<dd>When the server is compiled using the SHARED_CORE rule, this specifies the <i>directory</i> for the shared object files.</p>
<dt>-h</p>
<dd>Output a short summary of available command line options.</p>
<dt>-l</p>
<dd>Output a list of modules compiled into the server. This will <code>not</code> list dynamically loaded modules included using the LoadModule directive.</p>
<dt>-L</p>
<dd>Output a list of directives together with expected arguments and places where the directive is valid.</p>
<dt>-M</p>
<dd>Dump a list of loaded Static and Shared Modules.</p>
<dt>-S</p>
<dd>Show the settings as parsed from the config file (currently only shows the virtualhost settings).</p>
<dt>-t</p>
<dd>Run syntax tests for configuration files only. The program immediately exits after these syntax parsing tests with either a return code of 0 (Syntax OK) or return code not equal to 0 (Syntax Error). If -D <i>DUMP</i>_<i>VHOSTS </i>is also set, details of the virtual host configuration will be printed. If -D <i>DUMP</i>_<i>MODULES </i> is set, all loaded modules will be printed.</p>
<dt>-v</p>
<dd>Print the version of apache2, and then exit.</p>
<dt>-V</p>
<dd>Print the version and build parameters of apache2, and then exit.</p>
<dt>-X</p>
<dd>Run apache2 in debug mode. Only one worker will be started and the server will not detach from the console.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-apache2ctl/">apache2ctl</a></code>(8), <code>/usr/share/doc/apache2/README.Debian.gz</code> </p>
