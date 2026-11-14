---
title: "tinyproxy-conf(5)"
name: "tinyproxy-conf"
section: "5"
letter: "t"
url: "/docs/linux/man/5-tinyproxy-conf/"
description: "tinyproxy.conf – Tinyproxy HTTP proxy daemon configuration file"
---

<p>tinyproxy.conf &#8211; Tinyproxy HTTP proxy daemon configuration file</p>
<h2>Synopsis</h2>
<p><code>tinyproxy.conf</code></p>
<h2>Description</h2>
<p><a href="/docs/linux/man/8-tinyproxy/">tinyproxy</a>(8) reads its configuration file, typically stored in /etc/tinyproxy/tinyproxy.conf (or passed to Tinyproxy with -c on the command line). This manpage describes the syntax and contents of the configuration file. </p>
<p> The Tinyproxy configuration file contains key-value pairs, one per line. Lines starting with # and empty lines are comments and are ignored. Keywords are case-insensitive, whereas values are case-sensitive. Values may be enclosed in double-quotes (&quot;) if they contain spaces. </p>
<p> The possible keywords and their descriptions are as follows: </p>
<p> <code>User</code></p>
<dl>
<dd>The user which the Tinyproxy process should run as, after the initial port-binding has been done as the root user. Either the user name or the UID may be specified.</dl>
<p> <code>Group</code></p>
<dl>
<dd>The group which the Tinyproxy process should run as, after the initial port-binding has been done as the root user. Either the group name or the GID may be specified.</dl>
<p> <code>Port</code></p>
<dl>
<dd>The port which the Tinyproxy service will listen on. If the port is less than 1024, you will need to start the Tinyproxy process as the root user.</dl>
<p> <code>Listen</code></p>
<dl>
<dd>By default, Tinyproxy listens for connections on all available interfaces (i.e. it listens on the wildcard address 0.0.0.0). With this configuration parameter, Tinyproxy can be told to listen only on one specific address.</dl>
<p> <code>Bind</code></p>
<dl>
<dd>This allows you to specify which address Tinyproxy will bind to for outgoing connections to web servers or upstream proxies.</dl>
<p> <code>BindSame</code></p>
<dl>
<dd>If this boolean parameter is set to yes, then Tinyproxy will bind the outgoing connection to the IP address of the incoming connection that triggered the outgoing request.</dl>
<p> <code>Timeout</code></p>
<dl>
<dd>The maximum number of seconds of inactivity a connection is allowed to have before it is closed by Tinyproxy.</dl>
<p> <code>ErrorFile</code></p>
<dl>
<dd>This parameter controls which HTML file Tinyproxy returns when a given HTTP error occurs. It takes two arguments, the error number and the location of the HTML error file.</dl>
<p> <code>DefaultErrorFile</code></p>
<dl>
<dd>This parameter controls the HTML template file returned when an error occurs for which no specific error file has been set.</dl>
<p> <code>StatHost</code></p>
<dl>
<dd>This configures the host name or IP address that is treated as the stat host: Whenever a request for this host is received, Tinyproxy will return an internal statistics page instead of forwarding the request to that host. The template for this page can be configured with the StatFile configuration option. The default value of StatHost is tinyproxy.stats.</dl>
<p> <code>StatFile</code></p>
<dl>
<dd>This configures the HTML file that Tinyproxy sends when a request for the stathost is received. If this parameter is not set, Tinyproxy returns a hard-coded basic statistics page. See the STATHOST section in the <a href="/docs/linux/man/8-tinyproxy/">tinyproxy</a>(8) manual page for details. </p>
<p> Note that the StatFile and the error files configured with ErrorFile and DefaultErrorFile are template files that can contain a few template variables that Tinyproxy expands prior to delivery. Examples are &quot;{cause}&quot; for an abbreviated error description and &quot;{detail}&quot; for a detailed error message. The <a href="/docs/linux/man/8-tinyproxy/">tinyproxy</a>(8) manual page contains a description of all template variables.</dl>
<p> <code>LogFile</code></p>
<dl>
<dd>This controls the location of the file to which Tinyproxy writes its debug output. Alternatively, Tinyproxy can log to syslog &#8212; see the Syslog option.</dl>
<p> <code>Syslog</code></p>
<dl>
<dd>When set to On, this option tells Tinyproxy to write its debug messages to syslog instead of to a log file configured with LogFile. These two options are mutually exclusive.</dl>
<p> <code>LogLevel</code></p>
<dl>
<dd>Sets the log level. Messages from the set level and above are logged. For example, if the LogLevel was set to Warning, then all log messages from Warning to Critical would be output, but Notice and below would be suppressed. Allowed values are: </p>
<dl>
<dd>&bull; Critical (least verbose)</dl>
<dl>
<dd>&bull; Error</dl>
<dl>
<dd>&bull; Warning</dl>
<dl>
<dd>&bull; Notice</dl>
<dl>
<dd>&bull; Connect (log connections without Info&#8217;s noise)</dl>
<dl>
<dd>&bull; Info (most verbose)</dl>
</dl>
<p> <code>PidFile</code></p>
<dl>
<dd>This option controls the location of the file where the main Tinyproxy process stores its process ID for signaling purposes.</dl>
<p> <code>XTinyproxy</code></p>
<dl>
<dd>Setting this option to Yes tells Tinyproxy to add a header X-Tinyproxy containing the client&#8217;s IP address to the request.</dl>
<p> <code>Upstream</code>, <code>No Upstream</code></p>
<dl>
<dd>This option allows you to set up a set of rules for deciding whether an upstream proxy server is to be used, based on the host or domain of the site being accessed. The rules are stored in the order encountered in the configuration file and the LAST matching rule wins. There are three possible forms for specifying upstream rules: </p>
<dl>
<dd>&bull; <i>upstream host:port</i> turns proxy upstream support on generally.</dl>
<dl>
<dd>&bull; <i>upstream host:port &quot;site_spec&quot;</i> turns on the upstream proxy for the sites matching site_spec.</dl>
<dl>
<dd>&bull; <i>no upstream &quot;site_spec&quot;</i> turns off upstream support for sites matching site_spec. </p>
<dl>
<dd>
<pre>The site can be specified in various forms as a hostname, domain
name or as an IP range:</pre>
</dl>
</dl>
<dl>
<dd>&bull; <i>name</i> matches host exactly</dl>
<dl>
<dd>&bull; <i>.name</i> matches any host in domain &quot;name&quot;</dl>
<dl>
<dd>&bull; <i>.</i> matches any host with no domain (in <i>empty</i> domain)</dl>
<dl>
<dd>&bull; <i>IP/bits</i> matches network/mask</dl>
<dl>
<dd>&bull; <i>IP/mask</i> matches network/mask</dl>
</dl>
<p> <code>MaxClients</code></p>
<dl>
<dd>Tinyproxy creates one child process for each connected client. This options specifies the absolute highest number processes that will be created. With other words, only MaxClients clients can be connected to Tinyproxy simultaneously.</dl>
<p> <code>MinSpareServers</code>, <code>MaxSpareServers</code></p>
<dl>
<dd>Tinyproxy always keeps a certain number of idle child processes so that it can handle new incoming client requests quickly. MinSpareServer and MaxSpareServers control the lower and upper limits for the number of spare processes. I.e. when the number of spare servers drops below MinSpareServers then Tinyproxy will start forking new spare processes in the background and when the number of spare processes exceeds MaxSpareServers then Tinyproxy will kill off extra processes.</dl>
<p> <code>StartServers</code></p>
<dl>
<dd>The number of servers to start initially. This should usually be set to a value between MinSpareServers and MaxSpareServers.</dl>
<p> <code>MaxRequestsPerChild</code></p>
<dl>
<dd>This limits the number of connections that a child process will handle before it is killed. The default value is 0 which disables this feature. This option is meant as an emergency measure in the case of problems with memory leakage. In that case, setting MaxRequestsPerChild to a value of e.g. 1000, or 10000 can be useful.</dl>
<p> <code>Allow</code>, <code>Deny</code></p>
<dl>
<dd>The Allow and Deny options provide a means to customize which clients are allowed to access Tinyproxy. Allow and Deny lines can be specified multiple times to build the access control list for Tinyproxy. The order in the config file is important. If there are no Allow or Deny lines, then all clients are allowed. Otherwise, the default action is to deny access. The argument to Allow or Deny can be a single IP address of a client host, like 127.0.0.1, an IP address range, like 192.168.0.1/24 or a string that will be matched against the end of the client host name, i.e, this can be a full host name like host.example.com or a domain name like .example.com or even a top level domain name like .com.</dl>
<p> <code>AddHeader</code></p>
<dl>
<dd>Configure one or more HTTP request headers to be added to outgoing HTTP requests that Tinyproxy makes. Note that this option will not work for HTTPS traffic, as Tinyproxy has no control over what headers are exchanged.</dl>
<dl>
<dd>
<pre>AddHeader &quot;X-My-Header&quot; &quot;Powered by Tinyproxy&quot;</pre>
</dl>
<p> <code>ViaProxyName</code></p>
<dl>
<dd>RFC 2616 requires proxies to add a Via header to the HTTP requests, but using the real host name can be a security concern. If the ViaProxyname option is present, then its string value will be used as the host name in the Via header. Otherwise, the server&#8217;s host name will be used.</dl>
<p> <code>DisableViaHeader</code></p>
<dl>
<dd>When this is set to yes, Tinyproxy does NOT add the Via header to the requests. This virtually puts Tinyproxy into stealth mode. Note that RFC 2616 requires proxies to set the Via header, so by enabling this option, you break compliance. Don&#8217;t disable the Via header unless you know what you are doing&#8230;</dl>
<p> <code>Filter</code></p>
<dl>
<dd>Tinyproxy supports filtering of web sites based on URLs or domains. This option specifies the location of the file containing the filter rules, one rule per line.</dl>
<p> <code>FilterURLs</code></p>
<dl>
<dd>If this boolean option is set to Yes or On, filtering is performed for URLs rather than for domains. The default is to filter based on domains.</dl>
<p> <code>FilterExtended</code></p>
<dl>
<dd>If this boolean option is set to Yes, then extended POSIX regular expressions are used for matching the filter rules. The default is to use basic POSIX regular expressions.</dl>
<p> <code>FilterCaseSensitive</code></p>
<dl>
<dd>If this boolean option is set to Yes, then the filter rules are matched in a case sensitive manner. The default is to match case-insensitively.</dl>
<p> <code>FilterDefaultDeny</code></p>
<dl>
<dd>The default filtering policy is to allow everything that is not matched by a filtering rule. Setting FilterDefaultDeny to Yes changes the policy do deny everything but the domains or URLs matched by the filtering rules.</dl>
<p> <code>Anonymous</code></p>
<dl>
<dd>If an Anonymous keyword is present, then anonymous proxying is enabled. The headers listed with Anonymous are allowed through, while all others are denied. If no Anonymous keyword is present, then all headers are allowed through. You must include quotes around the headers. </p>
<p> Most sites require cookies to be enabled for them to work correctly, so you will need to allow cookies through if you access those sites. </p>
<p> Example:</dl>
<dl>
<dd>
<pre>Anonymous &quot;Host&quot;
Anonymous &quot;Authorization&quot;
Anonymous &quot;Cookie&quot;</pre>
</dl>
<p> <code>ConnectPort</code></p>
<dl>
<dd>This option can be used to specify the ports allowed for the CONNECT method. If no ConnectPort line is found, then all ports are allowed. To disable CONNECT altogether, include a single ConnectPort line with a value of 0.</dl>
<p> <code>ReversePath</code></p>
<dl>
<dd>Configure one or more ReversePath directives to enable reverse proxy support. With reverse proxying it&#8217;s possible to make a number of sites appear as if they were part of a single site. </p>
<p> If you uncomment the following two directives and run Tinyproxy on your own computer at port 8888, you can access example.com, using <a rel="nofollow" href="http://localhost:8888/example/.">http://localhost:8888/example/.</a></dl>
<dl>
<dd>
<pre>ReversePath &quot;/example/&quot; &quot;<a rel="nofollow" href="http://www.example.com/">http://www.example.com/</a>&quot;</pre>
</dl>
<p> <code>ReverseOnly</code></p>
<dl>
<dd>When using Tinyproxy as a reverse proxy, it is STRONGLY recommended that the normal proxy is turned off by setting this boolean option to Yes.</dl>
<p> <code>ReverseMagic</code></p>
<dl>
<dd>Setting this option to Yes, makes Tinyproxy use a cookie to track reverse proxy mappings. If you need to reverse proxy sites which have absolute links you must use this option.</dl>
<p> <code>ReverseBaseURL</code></p>
<dl>
<dd>The URL that is used to access this reverse proxy. The URL is used to rewrite HTTP redirects so that they won&#8217;t escape the proxy. If you have a chain of reverse proxies, you&#8217;ll need to put the outermost URL here (the address which the end user types into his/her browser). If this option is not set then no rewriting of redirects occurs.</dl>
<h2>Bugs</h2>
<p>To report bugs in Tinyproxy, please visit &lt;<a rel="nofollow" href="https://www.banu.com/tinyproxy/">https://www.banu.com/tinyproxy/</a>&gt;.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-tinyproxy/">tinyproxy</a>(8)</p>
<h2>Author</h2>
<p>Written by the Tinyproxy project team.</p>
<h2>Copyright</h2>
<p>Copyright (c) 1998-2000 Steven Young; Copyright (c) 2000-2001 Robert James Kaes; Copyright (c) 2009-2010 Mukund Sivaraman; Copyright (c) 2009-2010 Michael Adam. </p>
<p> This program is distributed under the terms of the GNU General Public License version 2 or above. See the COPYING file for additional information.</p>
