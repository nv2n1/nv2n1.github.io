---
title: "zarafa-ical-cfg(5)"
name: "zarafa-ical-cfg"
section: "5"
letter: "z"
url: "/docs/linux/man/5-zarafa-ical-cfg/"
description: "zarafa-ical.cfg – The Zarafa iCal/CalDAV gateway configuration file"
---

<p>zarafa-ical.cfg &#8211; The Zarafa iCal/CalDAV gateway configuration file</p>
<h2>Synopsis</h2>
<p><code>ical.cfg</code></p>
<h2>Description</h2>
<p>The ical.cfg is a configuration file for the Zarafa iCal/CalDAV Gateway. ical.cfg contains instructions for the software to set up the logging system and to enable or disable the normal or SSL part of the service.</p>
<h2>File Format</h2>
<p>The file consists of one big section, but parameters can be grouped by functionality. </p>
<p> The parameters are written in the form: </p>
<p> <code>name</code> = <i>value</i> </p>
<p> The file is line-based. Each newline-terminated line represents either a comment, nothing, a parameter or a directive. A line beginning with `#&#8217; is considered a comment, and will be ignored by Zarafa. Parameter names are case sensitive. Lines beginning with `!&#8217; are directives. </p>
<p> Directives are written in the form: </p>
<p> !<code>directive</code><i>[argument(s)] </i> </p>
<p> The following directives exist: </p>
<p> <code>include</code></p>
<dl>
<dd>Include and process <i>argument</i> </p>
<p> Example: !include common.cfg</dl>
<h2>Explanation Of Each Parameter</h2>
<p><code>server_bind</code></p>
<dl>
<dd>IP address to bind to. 0.0.0.0 for any address. </p>
<p> Default: <i>0.0.0.0</i></dl>
<p> <code>ical_enable</code></p>
<dl>
<dd>Enable iCal/CalDAV service with value yes. All other values disable the service. </p>
<p> Default: <i>yes</i></dl>
<p> <code>ical_port</code></p>
<dl>
<dd>The iCal/CalDAV service will listen on this port for incoming connections. </p>
<p> Default: <i>8080</i></dl>
<p> <code>icals_enable</code></p>
<dl>
<dd>Enable SSL iCal/CalDAV service with value yes. All other values disable the service. </p>
<p> Default: <i>yes</i></dl>
<p> <code>icals_port</code></p>
<dl>
<dd>The SSL iCal/CalDAV service will listen on this port for incoming connections. </p>
<p> Default: <i>8443</i></dl>
<p> <code>server_socket</code></p>
<dl>
<dd>The http address of the Zarafa server. </p>
<p> Default: <i><a rel="nofollow" href="http://localhost:236/zarafa">http://localhost:236/zarafa</a></i> </p>
<p> It is not advised to specify the UNIX socket here, but the http address instead. In default configuration the gateway will then be trusted by the Zarafa server (as set in its local_admin_users configuration setting). Unless is run as an untrusted user, by specifying the <code>run_as_user</code>, the gateway always authenticates users even if they provide no or wrong credentials!</dl>
<p> <code>run_as_user</code></p>
<dl>
<dd>After correctly starting, the iCal/CalDAV gateway process will become this user, dropping root privileges. Note that the log file needs to be writeable by this user, and the directory too to create new logfiles after logrotation. This can also be achieved by setting the correct group and permissions. </p>
<p> Default value is empty, not changing the user after starting.</dl>
<p> <code>run_as_group</code></p>
<dl>
<dd>After correctly starting, the iCal/CalDAV gateway process will become this group, dropping root privileges. </p>
<p> Default value is empty, not changing the group after starting.</dl>
<p> <code>pid_file</code></p>
<dl>
<dd>Write the process ID number to this file. This is used by the init.d script to correctly stop/restart the service. </p>
<p> Default: <i>/var/run/zarafa-ical.pid</i></dl>
<p> <code>running_path</code></p>
<dl>
<dd>Change directory to this path when running in daemonize mode. When using the -F switch to run in the foreground the directory will not be changed. </p>
<p> Default: <i>/</i></dl>
<p> <code>process_model</code></p>
<dl>
<dd>You can change the process model between <i>fork</i> and <i>thread</i>. The forked model uses somewhat more resources, but if a crash is triggered, this will only affect one user. In the threaded model, a crash means all users are affected, and will not be able to use the service. </p>
<p> Default: <i>fork</i></dl>
<p> <code>ssl_private_key_file</code></p>
<dl>
<dd>The iCal/CalDAV gateway will use this file as private key for SSL TLS. This file can be created with: <code>openssl genrsa -out /etc/zarafa/ical/privkey.pem 2048</code>. </p>
<p> Default: <i>/etc/zarafa/ical/privkey.pem</i></dl>
<p> <code>ssl_certificate_file</code></p>
<dl>
<dd>The iCal/CalDAV gateway will use this file as certificate for SSL TLS. A self-signed certificate can be created with: <code>openssl req -new -x509 -key /etc/zarafa/ical/privkey.pem -out /etc/zarafa/ical/cert.pem -days 1095</code>. </p>
<p> Default: <i>/etc/zarafa/ical/cert.pem</i></dl>
<p> <code>ssl_verify_client</code></p>
<dl>
<dd>Enable client certificate verification with value yes. All other values disable the verification. </p>
<p> Default: <i>no</i></dl>
<p> <code>ssl_verify_file</code></p>
<dl>
<dd>The file to verify the clients certificates with. </p>
<p> Default: value not set.</dl>
<p> <code>ssl_verify_path</code></p>
<dl>
<dd>The path with the files to verify the clients certificates with. </p>
<p> Default: value not set.</dl>
<p> <code>ssl_protocols</code></p>
<dl>
<dd>Disabled or enabled protocol names. Supported protocol names are <i>SSLv2</i>, <i>SSLv3</i> and <i>TLSv1</i>. If Zarafa was linked against OpenSSL 1.0.1 or later there is additional support for the new protocols <i>TLSv1.1</i> and <i>TLSv1.2</i>. To exclude both, SSLv2 and SSLv3 set <code>ssl_protocols</code> to <i>!SSLv2 !SSLv3</i>. SSLv2 is considered unsafe and these connections should not be accepted. </p>
<p> Default: <i>!SSLv2</i></dl>
<p> <code>ssl_ciphers</code></p>
<dl>
<dd>SSL ciphers to use, set to <i>ALL</i> for backward compatibility. </p>
<p> Default: <i>ALL:!LOW:!SSLv2:!EXP:!aNULL</i></dl>
<p> <code>ssl_prefer_server_ciphers</code></p>
<dl>
<dd>Prefer the server&#8217;s order of SSL ciphers over client&#8217;s. </p>
<p> Default: <i>no</i></dl>
<p> <code>log_method</code></p>
<dl>
<dd>The method which should be used for logging. Valid values are: </p>
<p> <i>syslog</i></p>
<dl>
<dd>Use the Linux system log. All messages will be written to the mail facility. See also <code><a href="/docs/linux/man/5-syslog-conf/">syslog.conf</a></code>(5).</dl>
<p> <i>file</i></p>
<dl>
<dd>Log to a file. The filename will be specified in <code>log_file</code>.</dl>
<p> Default: <i>file</i></dl>
<p> <code>log_file</code></p>
<dl>
<dd>When logging to a file, specify the filename in this parameter. Use <i>&#8211;</i> (minus sign) for stderr output. </p>
<p> Default: <i>/var/log/zarafa/ical.log</i></dl>
<p> <code>log_level</code></p>
<dl>
<dd>The level of output for logging in the range from 0 to 5. 0=no logging, 5=full logging. </p>
<p> Default: <i>2</i></dl>
<p> <code>log_timestamp</code></p>
<dl>
<dd>Specify whether to prefix each log line with a timestamp in &#8216;file&#8217; logging mode. </p>
<p> Default: <i>1</i></dl>
<p> <code>enable_ical_get</code></p>
<dl>
<dd>Enable the ical GET method to download an entire calendar. When set to &#8216;yes&#8217;, the GET method is enabled and allowed. If not, then calendars can only be retrieved with the CalDAV PROPFIND method, which is much more efficient. This option allows you to force the use of CalDAV which lowers load on your server.</dl>
<h2>Reloading</h2>
<p>The following options are reloadable by sending the zarafa-ical process a HUP signal: </p>
<p> log_level</p>
<dl>
<dd></dl>
<h2>Files</h2>
<p>/etc/zarafa/ical.cfg</p>
<dl>
<dd>The Zarafa iCal/CalDAV gateway configuration file.</dl>
<h2>Author</h2>
<p>Written by Zarafa.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-zarafa-ical/">zarafa-ical</a></code>(1) </p>
