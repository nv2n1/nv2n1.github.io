---
title: "gssproxy(8)"
name: "gssproxy"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gssproxy/"
description: "gssproxy – GssProxy Daemon"
---

<p>gssproxy &#8211; GssProxy Daemon</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>gssproxy</code> [<i>options</i>]</dl>
<h2>Description</h2>
<p><code>gssproxy</code></p>
<dd>provides a daemon to manage access to GSSAPI credentials. </p>
<p> <code>gssproxy</code> consists of the <code>gssproxy</code> daemon (configured by the <code><a href="/docs/linux/man/5-gssproxy-conf/">gssproxy.conf</a></code>(5) file) and a GSSAPI interposer plugin (<code><a href="/docs/linux/man/8-gssproxy-mech/">gssproxy-mech</a></code>(8)).</p>
<h2>Options</h2>
<p><code>-D</code>,<code>&#8211;daemon</code></p>
<dl>
<dd>Become a daemon after starting up.</dl>
<p> <code>-i</code>,<code>&#8211;interactive</code></p>
<dl>
<dd>Run in the foreground, don&#8217;t become a daemon.</dl>
<p> <code>-c</code>,<code>&#8211;config</code></p>
<dl>
<dd>Specify a config file to use as the main config file (read before the rest of the config directory). The default is to use the file /etc/gssproxy/gssproxy.conf. For reference on the config file syntax and options, consult the <code><a href="/docs/linux/man/5-gssproxy-conf/">gssproxy.conf</a></code>(5) manual page.</dl>
<p> <code>-C</code>,<code>&#8211;configdir</code></p>
<dl>
<dd>Specify a non-default config dir. Files named of the form &quot;##-foo.conf&quot; (that is, beginning with two digits and a dash, and ending in &quot;.conf&quot;) will be read in numeric order from this directory, in addition to the config file itself. The default is /etc/gssproxy. For reference on the config file syntax and options, consult the <code><a href="/docs/linux/man/5-gssproxy-conf/">gssproxy.conf</a></code>(5) manual page.</dl>
<p> <code>-s</code>,<code>&#8211;socket</code></p>
<dl>
<dd>Specify a custom default socket name. This socket will be used by all sections that do not define an explicit socket.</dl>
<p> <code>-d</code>,<code>&#8211;debug</code></p>
<dl>
<dd>Turn on debugging.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Print version number and exit.</dl>
<h2>Signals</h2>
<p>SIGTERM/SIGINT</p>
<dl>
<dd>Informs the GssProxy to gracefully terminate all of its child processes and then shut down.</dl>
<p> SIGHUP</p>
<dl>
<dd>Request a reload of all configuration for gssproxy. If there is an error in the configuration files, the existing configuration will not be replaced; if there is a problem applying the new configuration, gssproxy will exit.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-gssproxy-conf/">gssproxy.conf</a></code>(5) and <code><a href="/docs/linux/man/8-gssproxy-mech/">gssproxy-mech</a></code>(8).</p>
<h2>Authors</h2>
<p><code>GSS-Proxy &#8211; <a rel="nofollow" href="http://fedorahosted.org/gss-proxy">http://fedorahosted.org/gss-proxy</a></code></p>
