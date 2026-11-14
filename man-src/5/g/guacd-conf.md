---
title: "guacd-conf(5)"
name: "guacd-conf"
section: "5"
letter: "g"
url: "/docs/linux/man/5-guacd-conf/"
description: "/etc/guacamole/guacd.conf – Configuration file for guacd"
---

<p>/etc/guacamole/guacd.conf &#8211; Configuration file for guacd</p>
<h2>Description</h2>
<p><code>/etc/guacamole/guacd.conf</code> is the configuration file for the Guacamole proxy daemon used by the Guacamole web application and framework, <code>guacd.</code> Use of this file is entirely optional, and all of its options can be specified from the command line when running <code>guacd.</code> If you provide both the <code>guacd.conf</code> file and command line options, the command line options will take precedence.</p>
<h2>Syntax</h2>
<p><code>guacd.conf</code> is made up of sections, where each section contains a set of parameter/value pairs. The parameters available are dictated by the section in use, and parameters may only be specified within a section. </p>
<p> The beginning of each section is denoted with a section name in brackets, and each section ends implicitly with the beginning of a new section, or at the end of the file.</p>
<dl>
<dt><code>[server]</code></p>
<dd>Contains parameters which control how <code>guacd</code> behaves as a server, from a network perspective.</p>
<dt><code>[daemon]</code></p>
<dd>Parameters which configure how <code>guacd</code> behaves as a daemon, such as what file should contain the PID, if any.</p>
<dt><code>[ssl]</code></p>
<dd>Parameters which control the SSL support of <code>guacd,</code> such as the certificate and private key used for encryption of the Guacamole protocol. This section and its parameters are only valid if <code>guacd</code> was built with SSL support.</dl>
<p> Parameters within sections are written as a parameter name, followed by an equals sign, followed by the parameter value, all on one line. Comments may be placed anywhere, and consist of arbitrary text following a <code>#</code> symbol until end-of-line:</p>
<dl>
<dt><i>name</i> <code>=</code> <i>value</i> <code>#</code> <i>Some arbitrary comment text</i></p>
<dd></dl>
<p> Beware that it is the combination of the section name with the parameter name that makes up the fully qualified name of a parameter. Each parameter absolutely <i>must</i> be placed only within its proper section, or <code>guacd.conf</code> will fail to be parsed, and <code>guacd</code> will not start. </p>
<p> If special characters need to be placed within a parameter value, such as whitespace, <code>#</code>, <code>&quot;</code>, or <code>\</code>, the entire value must be enclosed in double quotes, and each occurrence of <code>&quot;</code> or <code>\</code> within the value must be escaped with backslashes:</p>
<dl>
<dt><i>name</i> <code>=</code> <code>&quot;</code><i>quoted # value \ with \&quot; special characters</i><code>&quot;</code></p>
<dd></dl>
<h2>Server Parameters</h2>
<dl>
<dt><code>bind_host</code> <code>=</code> <i>HOSTNAME</i></p>
<dd>Requires <code>guacd</code> to bind to a specific host when listening for connections. By default, <code>guacd</code> will bind to localhost only.</p>
<dt><code>bind_port</code> <code>=</code> <i>PORT</i></p>
<dd>Requires <code>guacd</code> to bind to a specific port when listening for connections. By default, <code>guacd</code> will bind to port 4822.</dl>
<h2>Daemon Parameters</h2>
<dl>
<dt><code>log_level</code> <code>=</code> <i>LEVEL</i></p>
<dd>Sets the maximum level at which <code>guacd</code> will log messages to syslog and, if running in the foreground, the console. Legal values are <code>debug,</code> <code>info,</code> <code>warning,</code> and <code>error.</code> The default value is <code>info.</code></p>
<dt><code>pid_file</code> <code>=</code> <i>FILE</i></p>
<dd>Causes <code>guacd</code> to write its PID to the specified file upon startup. Note that <code>guacd</code> must have sufficient privileges to create or write this file, or it will fail to start. This parameter is typically needed for startup scripts, such that the script can report on the status of <code>guacd</code> and kill it if necessary.</dl>
<h2>Ssl Parameters</h2>
<p>If <code>guacd</code> was built with SSL support, then connections between the web application and <code>guacd</code> can be encrypted if an SSL certificate and key file are given. </p>
<p> When using a chain of certificates, you must append the additional certificates to your server certificate. This can be done easily with the standard <code>cat</code> command. Beware that the certificate for <code>guacd</code> <i>must</i> be the first certificate in the file.</p>
<dl>
<dt><code>server_certificate</code> <code>=</code> <i>CERTIFICATE FILE</i></p>
<dd>Enables SSL/TLS using the given cerficiate file. Future connections to <code>guacd</code> will require SSL/TLS enabled in the client (the web application).</p>
<dt><code>server_key</code> <code>=</code> <i>KEY FILE</i></p>
<dd>Enables SSL/TLS using the given private key file. Future connections to <code>guacd</code> will require SSL/TLS enabled in the client (the web application).</dl>
<h2>Example</h2>
<pre><dl><dt><dd>#
# guacd.conf example
#
[daemon]
pid_file = /var/run/guacd.pid
[server]
bind_host = localhost
bind_port = 4822
[ssl]
server_certificate = /etc/ssl/certs/guacd.crt
server_key = /etc/ssl/private/guacd.key
</dl></pre>
<h2>Author</h2>
<p>Written by Michael Jumper &lt;mike.jumper [at] guac-dev.org&gt;</p>
