---
title: "ds-logpipe(1)"
name: "ds-logpipe"
section: "1"
letter: "d"
url: "/docs/linux/man/1-ds-logpipe/"
description: "ds-logpipe.py – Create and read from a named pipe instead of a log file"
---

<h2 class="name">NAME</h2>
<p> ds-logpipe.py &#8211; Create and read from a named pipe instead of a log file </p>
<h2>SYNOPSIS</h2>
<p> <code>ds-logpipe.py</code> /full/path/to/namedpipe<br />
&nbsp;<wbr>[<i>-m maxlinestobuffer</i>]&nbsp;<wbr>[<i>-u userid</i>]&nbsp;<wbr>[<i>-s serverpidfile</i>]&nbsp;<wbr>[<i>-t servertimeout</i>]&nbsp;<wbr>[<i>&#8211;plugin=/path/to/pluginfile.py</i>]&nbsp;<wbr>[<i>pluginfile.arg=value</i>] </p>
<h2>DESCRIPTION</h2>
<p> The Named Pipe Log Script allows you to replace a log file with a named pipe attached to a script. The server can then send the log output to a script instead of to a log file. This allows you to do many different things such as: </p>
<p>&nbsp;<wbr>*&nbsp;<wbr>log only certain events e.g. failed binds, connections from certain ip addresses, etc.<br />
&nbsp;<wbr>*&nbsp;<wbr>log only lines that match a certain pattern<br />
&nbsp;<wbr>*&nbsp;<wbr>log only the last N lines &#8211; useful for enabling full error log debug levels in production environments<br />
&nbsp;<wbr>*&nbsp;<wbr>send an email or other notification when a certain event is detected&nbsp;<wbr> </p>
<p> The script is written in python, and allows plugins. By default, the script will log the last N lines (default 1000). There are two plugins provided &#8211; one to log only failed bind attempts, and one that will log only lines that match given regular expressions. </p>
<h2>OPTIONS</h2>
<p> A summary of options is included below.</p>
<dl>
<dt><code>/full/path/to/namedpipe</code></p>
<dd> Required &#8211; full path and file name of the named pipe. If this does not exist, it will be created. If it exists and is a named pipe, the script will use it. If it exists and is not a pipe, the script will abort. The ownership will be the same as the user running the script (or see the -u option below).</p>
<dt><code>-m|&#8211;maxlines=N</code></p>
<dd> Number of lines to buffer &#8211; default is 1000</p>
<dt><code>-u|&#8211;userid=user</code></p>
<dd> The pipe and any other files created by the script will be chown()&#8217;d to this userid. This may be a string userid name or a numeric userid value.</p>
<dt><code>-s|&#8211;serverpidfile=/path/to/servername.pid</code></p>
<dd> If you want the script to exit when a particular directory server exists, specify the full path to the file containing the server pid. The default is usually something like /var/run/dirsrv/slapd-&lt;instancename&gt;.pid where &lt;instancename&gt; is usually the hostname</p>
<dt><code>-t|&#8211;servertimeout=N</code></p>
<dd> Since the serverpidfile may not exist yet when the script is run, the script will wait by default 60 seconds for the pid file to exist and the server to be started. Use this option to specify a different timeout.</p>
<dt><code>&#8211;serverpid=P</code></p>
<dd> IF the server you want to track is already running, you can specify it using this argument. If the specified pid is not valid, the script will abort.</p>
<dt><code>-p|&#8211;plugin=/full/path/to/pluginname.py</code></p>
<dd> Specify a plugin to use. The plugin must be a python file and must end in <i>.py</i>. It must specify a function called <i>plugin</i> and may specify functions called <i>pre</i> and <i>post</i>.</p>
<dt><code>pluginname.arg1=value &#8230; pluginname.argN=value</code></p>
<dd> You can specify arguments to plugins on the command line. If there is a plugin specified as &#8211;plugin=/full/path/to/pluginname.py, the arguments for that plugin are specified as <i>pluginname.argname=value</i>. The script parses these arguments and passes them to the plugin <i>pre</i> function as a python dict. IF there is more than one argument named <i>pluginname.argname</i> the values are passed as a python list.</dl>
<h2>DIRECTORY SERVER NOTES</h2>
<p> The directory server will usually need to be configured to log to the named pipe instead of the usual log file. For example, use the following LDIF to tell the server to use the file <i>access.pipe</i> for the access log:<br />
&nbsp;<wbr>dn: cn=config<br />
&nbsp;<wbr>changetype: modify<br />
&nbsp;<wbr>replace: nsslapd-accesslog-maxlogsperdir<br />
&nbsp;<wbr>nsslapd-accesslog-maxlogsperdir: 1<br />
&nbsp;<wbr>&#8211;<br />
&nbsp;<wbr>replace: nsslapd-accesslog-logexpirationtime<br />
&nbsp;<wbr>nsslapd-accesslog-logexpirationtime: -1<br />
&nbsp;<wbr>&#8211;<br />
&nbsp;<wbr>replace: nsslapd-accesslog-logrotationtime<br />
&nbsp;<wbr>nsslapd-accesslog-logrotationtime: -1<br />
&nbsp;<wbr>&#8211;<br />
&nbsp;<wbr>replace: nsslapd-accesslog<br />
&nbsp;<wbr>nsslapd-accesslog:&nbsp;<wbr>/var/log/dirsrv/slapd-localhost/access.pipe<br />
&nbsp;<wbr>&#8211;<br />
&nbsp;<wbr>replace: nsslapd-accesslog-logbuffering<br />
&nbsp;<wbr>nsslapd-accesslog-logbuffering: off </p>
<p> NOTE: Before doing this, you should save your current configuration so you can restore it later.<br />
&nbsp;<wbr>ldapsearch &#8230; -s base -b&nbsp;<wbr>&quot;cn=config&quot;&nbsp;<wbr>nsslapd-accesslog-maxlogsperdir nsslapd-accesslog-logexpirationtime&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>nsslapd-accesslog-logrotationtime nsslapd-accesslog nsslapd-accesslog&nbsp;<wbr>&gt;&nbsp;<wbr>savedaccesslog.ldif </p>
<p> The error log and audit log have similarly named configuration attributes e.g. nsslapd-errorlog, nsslapd-auditlog. Note that the audit log is disabled by default &#8211; use nsslapd-auditlog-logging-enabled: on to enable it. </p>
<h2>AUTHOR</h2>
<p> ds-logpipe.py was written by the 389 Project.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="http://bugzilla.redhat.com.">http://bugzilla.redhat.com.</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2009 Red Hat, Inc.<br />
 This is free software. You may redistribute copies of it under the terms of the Directory Server license found in the LICENSE file of this software distribution. This license is essentially the GNU General Public License version 2 with an exception for plug-in distribution. </p>
<h2>Index</h2>
