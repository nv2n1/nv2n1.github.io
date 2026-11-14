---
title: "munin-node(5)"
name: "munin-node"
section: "5"
letter: "m"
url: "/docs/linux/man/5-munin-node/"
description: "munin-node.conf – Munin-node configuration file"
---

<p>munin-node.conf &#8211; Munin-node configuration file</p>
<h2>Description</h2>
<p>Munin-node is the node that Munin fetches data from, graphs, htmlifies and optionaly warns nagios about data it gathers. It&#8217;s designed to let it be very easy to graph new datasources. </p>
<p> &#8220;munin-node.conf&#8221; is the configuration file for munin-node. </p>
<p> The format of the file is dictated by the use of Net::Server. A look at &#8220;perldoc Net::Server&#8221; will give a list of options that the file supports by using the module. </p>
<p> The following options are of special interest:</p>
<dl>
<dt><code>allow </code><font SIZE="-1"><code>RE</code></font></p>
<dd><font SIZE="-1">IP</font> based access list is implemented through this. The statement may be repeated many times. It&#8217;s important to note that it&#8217;s actually a regular expression after the keyword so to allow localhost it must be written like this: </p>
<pre> allow ^127\.0\.0\.1$</pre>
<dt><code>host </code><font SIZE="-1"><code>IP</code></font></p>
<dd>The <font SIZE="-1">IP</font> number of the interface munin-node should listen on. By default munin-node listens to all interfaces. To make munin-node listen only on the localhost interface &#8211; making it unavailable from the network do this: </p>
<pre> host 127.0.0.1</pre>
</dl>
<h2>Additional options:</h2>
<dl>
<dt><code>host_name &lt;host&gt;</code></p>
<dd>If set, overrides the hostname munin-node uses in its &#8216;hello&#8217;-negotiation with munin. A &#8220;telnet localhost 4949&#8221; will show the hostname munin-node is currently using. If munin-node and the main munin installation do not agree on the hostname, munin will skip all the plugins of the machine in question.</p>
<dt><code>paranoia &lt;yes|no|true|false|on|off|1|0&gt;</code></p>
<dd>If set, checks permissions of plugin files, and only tries to run files owned by root. Default on.</p>
<dt><code>ignore_file &lt;regex&gt;</code></p>
<dd>Files matching &lt;regex&gt; in the node.d/ and node-conf.d/ directories will be overlooked.</p>
<dt><code>tls</code> &lt;value&gt;</p>
<dd>Can have four values. <tt>&quot;paranoid&quot;</tt>, <tt>&quot;enabled&quot;</tt>, <tt>&quot;auto&quot;</tt>, and <tt>&quot;disabled&quot;</tt>. <tt>&quot;Paranoid&quot;</tt> and <tt>&quot;enabled&quot;</tt> require a <font SIZE="-1">TLS</font> connection, while <tt>&quot;disabled&quot;</tt> will not attempt one at all. </p>
<p> The current default is <tt>&quot;disabled&quot;</tt> because <tt>&quot;auto&quot;</tt> is broken. <tt>&quot;Auto&quot;</tt> causes bad interaction between munin-update and munin-node if the node is unprepared to go to <font SIZE="-1">TLS</font>. </p>
<p> If you see data dropouts (gaps in graphs) please try to disable <font SIZE="-1">TLS</font>.</p>
<dt><code>tls_verify_certificate</code> &lt;value&gt;</p>
<dd>This directive can be <tt>&quot;yes&quot;</tt> or <tt>&quot;no&quot;</tt>. It determines if the remote certificate needs to be signed by a <font SIZE="-1">CA</font> that is known locally. Default is <tt>&quot;no&quot;</tt>.</p>
<dt><code>tls_private_key</code> &lt;value&gt;</p>
<dd>This directive sets the location of the private key to be used for <font SIZE="-1">TLS</font>. Default is @@CONFDIR@@/munin-node.pem. The private key and certificate can be stored in the same file.</p>
<dt><code>tls_certificate</code> &lt;value&gt;</p>
<dd>This directive sets the location of the <font SIZE="-1">TLS</font> certificate to be used for <font SIZE="-1">TLS</font>. Default is @@CONFDIR@@/munin-node.pem. The private key and certificate can be stored in the same file.</p>
<dt><code>tls_ca_certificate</code> &lt;value&gt;</p>
<dd>This directive sets the <font SIZE="-1">CA</font> certificate to be used to verify the node&#8217;s certificate, if tls_verify_certificate is set to <tt>&quot;yes&quot;</tt>. Default is @@CONFDIR@@/cacert.pem.</p>
<dt><code>tls_verify_depth</code> &lt;value&gt;</p>
<dd>This directive sets how many signings up a chain of signatures <font SIZE="-1">TLS</font> is willing to go to reach a known, trusted <font SIZE="-1">CA</font> when verifying a certificate. Default is <tt>5</tt>.</p>
<dt><code>tls_match</code> &lt;value&gt;</p>
<dd>This directive, if defined, searches a dump of the certificate provided by the remote host for the given regex. The dump of the certificate is two lines of the form: </p>
<pre> Subject Name: /C=c/ST=st/L=l/O=o/OU=ou/CN=cn/emailAddress=email
 Issuer Name: /C=c/ST=st/O=o/OU=ou/CN=cn/emailAddress=email</pre>
<p>So, for example, one could match the subject distinguished name by the directive: </p>
<pre> tls_match Subject Name: /C=c/ST=st/L=l/O=o/OU=ou/CN=cn/emailAddress=email</pre>
<p>Note that the fields are dumped in the order they appear in the certificate. It&#8217;s best to view the dump of the certificate by running munin-update in debug mode and reviewing the logs. </p>
<p> Unfortunately, due to the limited functionality of the <font SIZE="-1">SSL</font> module in use, it is not possible to provide finer-grained filtering. By default this value is not defined.</dl>
<h2>Example</h2>
<p>A pretty normal configuration file: </p>
<pre> log_level 4
 log_file /var/log/munin/munin-node.log
 port 4949
 pid_file /var/run/munin-node.pid
 background 1
 setsid 1
 host *
 user root
 group root
 setsid yes
 ignore_file \.bak$
 ignore_file \.rpm(save|new)$
 ignore_file ^README$
 allow ^127\.0\.0\.1$
 ignore_file \.dpkg-(old|new)$
 ignore_file \.rpm(save|new)$</pre>
<p>See the documentation or Munin homepage &lt;<a rel="nofollow" href="http://munin.projects.linpro.no/">http://munin.projects.linpro.no/</a>&gt; for more info.</p>
<h2>Authors</h2>
<p>Jimmy Olsen.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2002-2006 Audun Ytterdal, Jimmy Olsen, Dagfin Ilmari Mansa&#176;ker, Nicolai Langfeldt </p>
<p> This is free software; see the source for copying conditions. There is <font SIZE="-1">NO</font> warranty; not even for <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS</font> <font SIZE="-1">FOR</font> A <font SIZE="-1">PARTICULAR</font> <font SIZE="-1">PURPOSE</font>. </p>
<p> This program is released under the <font SIZE="-1">GNU</font> General Public License</p>
