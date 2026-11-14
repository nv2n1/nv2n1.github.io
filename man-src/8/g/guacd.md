---
title: "guacd(8)"
name: "guacd"
section: "8"
letter: "g"
url: "/docs/linux/man/8-guacd/"
description: "guacd – Guacamole proxy daemon"
---

<p>guacd &#8211; Guacamole proxy daemon</p>
<h2>Synopsis</h2>
<p><code>guacd</code> [<code>-b</code> <i>HOST</i>] [<code>-l</code> <i>PORT</i>] [<code>-p</code> <i>PID FILE</i>] [<code>-L</code> <i>LOG LEVEL</i>] [<code>-C</code> <i>CERTIFICATE FILE</i>] [<code>-K</code> <i>KEY FILE</i>] [<code>-f</code>]</p>
<h2>Description</h2>
<p><code>guacd</code> is the Guacamole proxy daemon used by the Guacamole web application and framework. As JavaScript cannot handle binary protocols (like VNC and remote desktop) efficiently, a new text-based protocol was developed which would contain a common superset of the operations needed for efficient remote desktop access, but would be easy for JavaScript programs to process. <code>guacd</code> is the proxy which translates between arbitrary protocols and the Guacamole protocol.</p>
<h2>Options</h2>
<dl>
<dt><code>-b</code> <i>HOST</i></p>
<dd>Changes the host or address that <code>guacd</code> listens on.</p>
<dt><code>-l</code> <i>PORT</i></p>
<dd>Changes the port that <code>guacd</code> listens on (the default is port 4822).</p>
<dt><code>-p</code> <i>FILE</i></p>
<dd>Causes <code>guacd</code> to write the PID of the daemon process to the specified file. This is useful for init scripts and is used by the provided init script.</p>
<dt><code>-L</code> <i>LEVEL</i></p>
<dd>Sets the maximum level at which <code>guacd</code> will log messages to syslog and, if running in the foreground, the console. Legal values are <code>debug,</code> <code>info,</code> <code>warning,</code> and <code>error.</code> The default value is <code>info.</code></p>
<dt><code>-f</code></p>
<dd>Causes <code>guacd</code> to run in the foreground, rather than automatically forking into the background.</dl>
<h2>Ssl/Tls Options</h2>
<p>If libssl was present at the time <code>guacd</code> was compiled, it will contain SSL/TLS support, and connections between the web application and <code>guacd</code> can be encrypted if a certificate file is given. </p>
<p> When using a chain of certificates, you must append the additional certificates to your server certificate. This can be done easily with the standard <code>cat</code> command. Beware that the certificate for <code>guacd</code> <i>must</i> be the first certificate in the file.</p>
<dl>
<dt><code>-C</code> <i>CERTIFICATE FILE</i></p>
<dd>Enables SSL/TLS using the given cerficiate file. Future connections to this instance of <code>guacd</code> will require SSL/TLS enabled in the client (the web application). If this option is not given, communication with guacd must be unencrypted.</p>
<dt><code>-K</code> <i>KEY FILE</i></p>
<dd>Enables SSL/TLS using the given private key file. Future connections to this instance of <code>guacd</code> will require SSL/TLS enabled in the client (the web application). If this option is not given, communication with guacd must be unencrypted.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-guacd-conf/">guacd.conf</a></code>(5)</p>
<h2>Author</h2>
<p>Written by Michael Jumper &lt;mike.jumper [at] guac-dev.org&gt;</p>
