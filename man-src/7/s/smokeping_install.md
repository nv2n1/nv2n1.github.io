---
title: "smokeping_install(7)"
name: "smokeping_install"
section: "7"
letter: "s"
url: "/docs/linux/man/7-smokeping_install/"
description: "smokeping_install – How to install SmokePing"
---

<p>smokeping_install &#8211; How to install SmokePing</p>
<h2>Overview</h2>
<p>This document explains how to setup SmokePing at your site.</p>
<h2>Description</h2>
<h3>Prerequisites</h3>
<p>SmokePing does not stand alone. It relies on various other tools and services being present. Apart from a Unix <font SIZE="-1">OS</font> and a working Perl installation you need the following components:</p>
<dl>
<dt>RRDtool 1.2.x or later</p>
<dd>Smokeping uses RRDtool for logging and graphing. If your linux distro provides an rrdtool package with perl support, use this. If you want to get the latest and greatest version, compile your own: &lt;<a rel="nofollow" href="http://oss.oetiker.ch/rrdtool/">http://oss.oetiker.ch/rrdtool/</a>&gt;</p>
<dt>FPing (optional)</p>
<dd>Go to &lt;<a rel="nofollow" href="http://www.fping.org/">http://www.fping.org/</a>&gt; to grab a copy. </p>
<p> Note that fping must be installed setuid root. It seems that older versions of fping report round trip times in 0.1 milliseconds instead of 1 milliseconds as advertised &#8230; SmokePing tries to figure this out. It tells you when it starts &#8230; let me know if it gets it wrong.</p>
<dt>EchoPing (Optional)</p>
<dd>&lt;<a rel="nofollow" href="http://echoping.sourceforge.net/">http://echoping.sourceforge.net/</a>&gt; </p>
<p> You need this to run the EchoPing probes</p>
<dt>Curl (Optional)</p>
<dd>&lt;<a rel="nofollow" href="http://curl.haxx.se/">http://curl.haxx.se/</a>&gt; </p>
<p> You need this for the Curl probe.</p>
<dt>dig (Optional)</p>
<dd>&lt;<a rel="nofollow" href="http://www.isc.org/sw/bind/">http://www.isc.org/sw/bind/</a>&gt; </p>
<p> You need this for the <font SIZE="-1">DNS</font> probe.</p>
<dt><font SIZE="-1">SSH </font>(Optional)</p>
<dd>&lt;<a rel="nofollow" href="http://www.openssh.org/">http://www.openssh.org/</a>&gt; </p>
<p> You need this for the <font SIZE="-1">SSH</font> probe.</p>
<dt>Webserver</p>
<dd>&lt;<a rel="nofollow" href="http://httpd.apache.org/">http://httpd.apache.org/</a>&gt; </p>
<p> Well I won&#8217;t get much into this. The important thing is, to have a webserver which allows you to run <font SIZE="-1">CGI</font> and preferably FastCGI scripts. If you are using Apache I strongly recommend using the <i>suexec</i> system for running <font SIZE="-1">CGI</font> scripts as a particular user. </p>
<p> See &lt;<a rel="nofollow" href="http://httpd.apache.org/mod_fcgid/mod/mod_fcgid.html">http://httpd.apache.org/mod_fcgid/mod/mod_fcgid.html</a>&gt; and &lt;<a rel="nofollow" href="http://httpd.apache.org/docs/2.2/mod/mod_suexec.html">http://httpd.apache.org/docs/2.2/mod/mod_suexec.html</a>&gt; for more information on this.</p>
<dt>Perl 5.8.8 or later.</p>
<dd>If you still have an older version, maybe have a look at perlbrew.</p>
<dt>Various Perl modules (Many are optional)</p>
<dd>The modules are all available from &lt;<a rel="nofollow" href="http://www.cpan.org">http://www.cpan.org</a>&gt; and you may be able to get them as packages from your distro&#8217;s repository. There is also a script provided in the setup folder to install the missing bits. You will be instructed later on how to use the script.</p>
<dl>
<dd>
<dl>
<dt><font SIZE="-1">FCGI</font></p>
<dd>The module for supporting FastCGI operation.</p>
<dt><font SIZE="-1">CGI,</font> CGI::Fast</p>
<dd>Perl CGI/FastCGI support. Might already be installed localy.</p>
<dt>Config::Grammar</p>
<dd>The configuration file parser used in smokeping</p>
<dt><font SIZE="-1">LWP</font></p>
<dd>The master/slave functionality introduced a dependency on LWP::UserAgent from the libwww-perl (also known as <font SIZE="-1">LWP</font>) library. The module is required even if the master/slave mode is not enabled.</p>
<dt>Socket6 (optional)</p>
<dd>The Socket6 module enables smokeping to check hostnames that only resolve to an IPv6 address. If you probe such hosts using ie. the FPing6 probe and get warnings that those hosts don&#8217;t resolve to an <font SIZE="-1">IP</font> address, you need to install it.</p>
<dt>Net::Telnet (optional)</p>
<dd>You need this for the TelnetIOSPing probe.</p>
<dt>Net::OpenSSH (optional)</p>
<dd>You need this for the OpenSSHJunOSPing probe.</p>
<dt>Net::DNS (optional)</p>
<dd>You need this for the AnotherDNS probe.</p>
<dt>Net::LDAP (optional)</p>
<dd>You need this for the <font SIZE="-1">LDAP</font> probe.</p>
<dt>IO::Socket::SSL (optional)</p>
<dd>You need this if you want the <font SIZE="-1">LDAP</font> probe to be able to use the &#8216;starttls&#8217; command.</p>
<dt>Authen::Radius (optional)</p>
<dd>You need this for the Radius probe.</dl>
</dl>
<dl>
<dd></dl>
</dl>
<h3>Installation</h3>
<p>Once the tools listed above are in place, you can start setting up SmokePing itself. Unpack the tar archive and run the included configure script: </p>
<pre> ./configure --prefix=/opt/smokeping</pre>
<p>Configure will verify that all the required perl modules are available. If some are missing it will tell you to run the module build script. Just follow the instructions on screen and then run configure again. Once it completes, you can run </p>
<pre> make install</pre>
<p>to finish your setup.</p>
<h3>Configuration</h3>
<p>Use the <i>etc/config.dist</i> file as a template to create your own smokeping configuration file. See smokeping_config for details.</p>
<dl>
<dt>Installing the webinterface</p>
<dd>Copy the content of the <i>PREFIX/htdocs</i> directory to the place where your webserver expects its data. Maybe to <i>/var/www/smokeping</i>. </p>
<p> Edit the <i>smokeping.fcgi</i> script to point to your smokeping_cgi script. </p>
<p> If you have no FastCGI support in your webserver, you may want to use the <i>smokeping.cgi</i> script.</p>
<dt><i>etc/basepage.html</i></p>
<dd>Edit the html template to your likings. Please do not remove the link to the SmokePing counter and my name from the template. The content of the template will be renderd by smokeping.cgi. This means that all embedded links must be relative to smokeping.cgi. If you are using <font SIZE="-1">HTTP</font> authentication, then the template variable <tt>&quot;authuser&quot;</tt> will be populated from the <tt>$ENV{REMOTE_USER}</tt> environment variable.</p>
<dt><i>etc/smokemail</i></p>
<dd>If you are going to use the <font SIZE="-1"><code>DYNAMIC</code></font> <font SIZE="-1">IP</font> support, customize the contents of this file.</dl>
<h3>Starting the Smokeping Daemon</h3>
<p>With all the scaffolding in place, you can now launch the smokeping daemon and have it gather data for you. First you may want to run it in debug mode to see what it is doing </p>
<pre> ./bin/smokeping --config=/opt/smokeping/etc/config --debug</pre>
<p>once all is well, start it up as a daemon. I would recomend you enable the logfile option so that you can see if it runs into trouble. </p>
<pre> ./bin/smokeping --config=/opt/smokeping/etc/config --logfile=smoke.log</pre>
<p>Once the system works, you may want to put a SmokePing startup script into your <i>/etc/init.d</i> tree. Check out smokeping for further information. </p>
<p> You can now open the smokeping.cgi webpage to look at your data. </p>
<p> See the smokeping_cgi documentation on how to setup the smokeping web interface.</p>
<h2>Copyright</h2>
<p>Copyright (c) 2001, 2011 by Tobias Oetiker. All right reserved.</p>
<h2>License</h2>
<p>This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA 02139, USA.</font></p>
<h2>Author</h2>
<p>Tobias Oetiker &lt;tobi [at] oetiker.ch&gt;</p>
