---
title: "privoxy(1)"
name: "privoxy"
section: "1"
letter: "p"
url: "/docs/linux/man/1-privoxy/"
description: "privoxy – Privacy Enhancing Proxy"
---

<h2>NAME</h2>
<p> privoxy &#8211; Privacy Enhancing Proxy</p>
<h2>SYNOPSIS</h2>
<p> <code>privoxy</code> [<code>&#8211;chroot</code> ] [<code>&#8211;config-test</code> ] [<code>&#8211;help</code> ] [<code>&#8211;no-daemon</code> ] [<code>&#8211;pidfile </code><i>pidfile</i> ] [<code>&#8211;pre-chroot-nslookup </code><i>hostname</i> ] [<code>&#8211;user </code><i>user[.group]</i> ] [<code>&#8211;version</code> ] [<i>configfile</i> ] </p>
<h2>OPTIONS</h2>
<p> <code>Privoxy</code> may be invoked with the following command line options:</p>
<dl>
<dt><code>&#8211;chroot</code></p>
<dd> Before changing to the user ID given in the &#8211;user option, chroot to that user&#8217;s home directory, i.e. make the kernel pretend to the <code>Privoxy</code> process that the directory tree starts there. If set up carefully, this can limit the impact of possible vulnerabilities in <code>Privoxy</code> to the files contained in that hierarchy.</p>
<dt><code>&#8211;config-test</code></p>
<dd> Exit after loading the configuration files before binding to the listen address. The exit code signals whether or not the configuration files have been successfully loaded. </p>
<p> If the exit code is 1, at least one of the configuration files is invalid, if it is 0, all the configuration files have been successfully loaded (but may still contain errors that can currently only be detected at run time). </p>
<p> This option doesn&#8217;t affect the log setting, combination with &quot;&#8211;no-daemon&quot; is recommended if a configured log file shouldn&#8217;t be used.</p>
<dt><code>&#8211;help</code></p>
<dd> Print brief usage info and exit.</p>
<dt><code>&#8211;no-daemon</code></p>
<dd> Don&#8217;t become a daemon, i.e. don&#8217;t fork and become process group leader, don&#8217;t detach from controlling tty, and do all logging there.</p>
<dt><code>&#8211;pidfile </code><i>pidfile</i></p>
<dd> On startup, write the process ID to <i>pidfile</i>. Delete the <i>pidfile</i> on exit. Failure to create or delete the <i>pidfile</i> is non-fatal. If no <code>&#8211;pidfile</code> option is given, no PID file will be used.</p>
<dt><code>&#8211;pre-chroot-nslookup </code><i>hostname</i></p>
<dd> Initialize the resolver library using <i>hostname</i> before chroot&#8217;ing. On some systems this reduces the number of files that must be copied into the chroot tree.</p>
<dt><code>&#8211;user </code><i>user[.group]</i></p>
<dd> After (optionally) writing the PID file, assume the user ID of <i>user</i> and the GID of <i>group</i>, or, if the optional <i>group</i> was not given, the default group of <i>user</i>. Exit if the privileges are not sufficient to do so.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version info and exit.</dl>
<p> If the <i>configfile</i> is not specified on the command line, <code>Privoxy</code> will look for a file named <i>config</i> in the current directory. If no <i>configfile</i> is found, <code>Privoxy</code> will fail to start.</p>
<h2>DESCRIPTION</h2>
<p> Privoxy is a non-caching web proxy with advanced filtering capabilities for enhancing privacy, modifying web page data and HTTP headers, controlling access, and removing ads and other obnoxious Internet junk. Privoxy has a flexible configuration and can be customized to suit individual needs and tastes. It has application for both stand-alone systems and multi-user networks. </p>
<p> Privoxy is Free Software and licensed under the GNU GPLv2. </p>
<p> Privoxy is an associated project of Software in the Public Interest (SPI). </p>
<p> Helping hands and donations are welcome:</p>
<dl>
<dt>&bull;</p>
<dd> <a rel="nofollow" href="https://www.privoxy.org/faq/general.html#PARTICIPATE">https://www.privoxy.org/faq/general.html#PARTICIPATE</a></p>
<dt>&bull;</p>
<dd> <a rel="nofollow" href="https://www.privoxy.org/faq/general.html#DONATE">https://www.privoxy.org/faq/general.html#DONATE</a></dl>
<h2>INSTALLATION AND USAGE</h2>
<p> Browsers can either be individually configured to use <code>Privoxy</code> as a HTTP proxy (recommended), or <code>Privoxy</code> can be combined with a packet filter to build an intercepting proxy (see <i>config</i>). The default setting is for localhost, on port 8118 (configurable in the main config file). To set the HTTP proxy in Firefox, go through: <code>Tools</code>; <code>Options</code>; <code>General</code>; <code>Connection Settings</code>; <code>Manual Proxy Configuration</code>. </p>
<p> For Internet Explorer, go through: <code>Tools</code>; <code>Internet Properties</code>; <code>Connections</code>; <code>LAN Settings</code>. </p>
<p> The Secure (SSL) Proxy should also be set to the same values, otherwise https: URLs will not be proxied. Note: <code>Privoxy</code> can only proxy HTTP and HTTPS traffic. Do not try it with FTP or other protocols. HTTPS presents some limitations, and not all features will work with HTTPS connections. </p>
<p> For other browsers, check the documentation.</p>
<h2>CONFIGURATION</h2>
<p> <code>Privoxy</code> can be configured with the various configuration files. The default configuration files are: <i>config</i>, <i>default.filter</i>, <i>default.action</i> and <i>default.action</i>. <i>user.action</i> should be used for locally defined exceptions to the default rules in <i>match-all.action</i> and <i>default.action</i>, and <i>user.filter</i> for locally defined filters. These are well commented. On Unix and Unix-like systems, these are located in <i>/etc/privoxy/</i> by default. </p>
<p> <code>Privoxy</code> uses the concept of <code>actions</code> in order to manipulate the data stream between the browser and remote sites. There are various actions available with specific functions for such things as blocking web sites, managing cookies, etc. These actions can be invoked individually or combined, and used against individual URLs, or groups of URLs that can be defined using wildcards and regular expressions. The result is that the user has greatly enhanced control and freedom. </p>
<p> The actions list (ad blocks, etc) can also be configured with your web browser at <a rel="nofollow" href="http://config.privoxy.org/">http://config.privoxy.org/</a> (assuming the configuration allows it). <code>Privoxy&#8217;s</code> configuration parameters can also be viewed at the same page. In addition, <code>Privoxy</code> can be toggled on/off. This is an internal page, and does not require Internet access. </p>
<p> See the <i>User Manual</i> for a detailed explanation of installation, general usage, all configuration options, new features and notes on upgrading.</p>
<h2>FILES</h2>
<pre>
 <i>/usr/sbin/privoxy</i>
 <i>/etc/privoxy/config</i>
 <i>/etc/privoxy/match-all.action</i>
 <i>/etc/privoxy/default.action</i>
 <i>/etc/privoxy/user.action</i>
 <i>/etc/privoxy/default.filter</i>
 <i>/etc/privoxy/user.filter</i>
 <i>/etc/privoxy/trust</i>
 <i>/etc/privoxy/templates/*</i>
 <i>/var/log/privoxy/logfile</i>
</pre>
<p> Various other files should be included, but may vary depending on platform and build configuration. Additional documentation should be included in the local documentation directory.</p>
<h2>SIGNALS</h2>
<p> <code>Privoxy</code> terminates on the <code>SIGINT</code> and <code>SIGTERM</code> signals. Log rotation scripts may cause a re-opening of the logfile by sending a <code>SIGHUP</code> to <code>Privoxy</code>. Note that unlike other daemons, <code>Privoxy</code> does not need to be made aware of config file changes by <code>SIGHUP</code> &#8212; it will detect them automatically. Signals other than the ones listed above aren&#8217;t explicitly handled and result in the default action defined by the operating system.</p>
<h2>NOTES</h2>
<p> Please see the <i>User Manual</i> on how to contact the developers, for feature requests, reporting problems, and other questions.</p>
<h2>SEE ALSO</h2>
<p> Other references and sites of interest to <code>Privoxy</code> users: </p>
<p> <a rel="nofollow" href="https://www.privoxy.org/,">https://www.privoxy.org/,</a> the <code>Privoxy</code> Home page. </p>
<p> <a rel="nofollow" href="https://www.privoxy.org/faq/,">https://www.privoxy.org/faq/,</a> the <code>Privoxy</code> FAQ. </p>
<p> <a rel="nofollow" href="https://www.privoxy.org/developer-manual/,">https://www.privoxy.org/developer-manual/,</a> the <code>Privoxy</code> developer manual. </p>
<p> <a rel="nofollow" href="https://sourceforge.net/projects/ijbswa/,">https://sourceforge.net/projects/ijbswa/,</a> the Project Page for <code>Privoxy</code> on SourceForge. </p>
<p> <a rel="nofollow" href="http://config.privoxy.org/,">http://config.privoxy.org/,</a> the web-based user interface. <code>Privoxy</code> must be running for this to work. Shortcut: <a rel="nofollow" href="http://p.p/">http://p.p/</a> </p>
<p> <a rel="nofollow" href="https://sourceforge.net/tracker/?group_id=11118">https://sourceforge.net/tracker/?group_id=11118</a>&amp;atid=460288, to submit &#8220;misses&#8221; and other configuration related suggestions to the developers.</p>
<h2>DEVELOPMENT TEAM</h2>
<pre>
 Fabian Keil, lead developer
 David Schmidt
 Hal Burgiss
 Lee Rian
 Roland Rosenfeld
 Ian Silvester
</pre>
<h2>COPYRIGHT AND LICENSE</h2>
<h3>COPYRIGHT</h3>
<p> Copyright (C) 2001-2016 by Privoxy Developers &lt;privoxy-devel [at] lists.privoxy.org&gt; </p>
<p> Some source code is based on code Copyright (C) 1997 by Anonymous Coders and Junkbusters, Inc. and licensed under the <i>GNU General Public License</i>.</p>
<h3>LICENSE</h3>
<p> <code>Privoxy</code> is free software; you can redistribute it and/or modify it under the terms of the <i>GNU General Public License</i>, version 2, as published by the Free Software Foundation. </p>
<p> <code>Privoxy</code> is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the <i>license</i> for details. </p>
<h2>Index</h2>
