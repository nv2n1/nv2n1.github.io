---
title: "myproxy-server(8)"
name: "myproxy-server"
section: "8"
letter: "m"
url: "/docs/linux/man/8-myproxy-server/"
description: "myproxy-server – store credentials in an online repository"
---

<p>myproxy-server &#8211; store credentials in an online repository</p>
<h2>Synopsis</h2>
<p><code>myproxy-server</code> [ <i>options</i> ]</p>
<h2>Description</h2>
<p>The <code>myproxy-server</code> is a server that runs on a trusted, secure host and manages a database of security credentials for use from remote sites. The <code><a href="/docs/linux/man/1-myproxy-init/">myproxy-init</a></code>(1) program stores credentials with associated policies that specify credential lifetimes and who is authorized to retrieve credentials. The <code><a href="/docs/linux/man/5-myproxy-server-config/">myproxy-server.config</a></code>(5) file sets server-wide policies that are used in conjunction with the policies set by <code><a href="/docs/linux/man/1-myproxy-init/">myproxy-init</a></code>(1) to control who is authorized to store and retrieve credentials.</p>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Displays command usage text and exits.</p>
<dt><code>-u, &#8211;usage</code></p>
<dd>Displays command usage text and exits.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Enables verbose debugging output to the terminal.</p>
<dt><code>-V, &#8211;version</code></p>
<dd>Displays version information and exits.</p>
<dt><code>-d, &#8211;debug</code></p>
<dd>Run the server in debug mode. In this mode, the server will run in the foreground, will accept one connection, write log messages to the terminal while processing the incoming request, and exit after completing one request.</p>
<dt><code>-l</code><i> hostname/ipaddr, </i><code>&#8211;listen</code><i> hostname/ipaddr</i></p>
<dd>Specifies the hostname or IP address that the <code>myproxy-server</code> should listen (bind) to. Default: all interfaces on the localhost</p>
<dt><code>-p</code><i> port, </i><code>&#8211;port</code><i> port</i></p>
<dd>Specifies the TCP port number that the <code>myproxy-server</code> should listen on. Default: 7512</p>
<dt><code>-c</code><i> file, </i><code>&#8211;config</code><i> file</i></p>
<dd>Specifies the location of the <code>myproxy-server</code> configuration file. Default: /etc/myproxy-server.config or $GLOBUS_LOCATION/etc/myproxy-server.config</p>
<dt><code>-s</code><i> dir, </i><code>&#8211;storage</code><i> dir</i></p>
<dd>Specifies the location of the credential storage directory. The directory must be accessible only by the user running the <code>myproxy-server</code> process for security reasons. Default: /var/lib/myproxy or /var/myproxy or $GLOBUS_LOCATION/var/myproxy</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/myproxy-server.config</i></p>
<dd>Default location of the server configuration file (see <code><a href="/docs/linux/man/5-myproxy-server-config/">myproxy-server.config</a></code>(5)). If not found, <i>$GLOBUS_LOCATION/etc/myproxy-server.config</i> will be used. An alternate location can be specified by using the <code>-c</code> option.</p>
<dt><i>/var/lib/myproxy</i></p>
<dd>Default location of the credential storage directory. If not found, <i>/var/myproxy</i> or <i>$GLOBUS_LOCATION/var/myproxy</i> will be used. If none of these directories exist, the myproxy-server will first attempt to create <i>/var/lib/myproxy</i> and if that fails will attempt to create <i>$GLOBUS_LOCATION/var/myproxy</i> and use that. The directory must be accessible only by the user running the <code>myproxy-server</code> process for security reasons. An alternate location can be specified by using the <code>-s</code> option.</dl>
<h2>Environment</h2>
<dl>
<dt><code>GLOBUS_LOCATION</code></p>
<dd>Specifies the root of the MyProxy installation, used to find the default location of the <i>myproxy-server.config</i> file and the credential storage directory.</p>
<dt><code>GLOBUS_USAGE_OPTOUT</code></p>
<dd>Setting this environment variable to &quot;1&quot; will disable the reporting of usage metrics.</p>
<dt><code>LD_LIBRARY_PATH</code></p>
<dd>The MyProxy server is typically linked dynamically with Globus security libraries, which must be present in the dynamic linker&#8217;s search path. This typically requires <i>$GLOBUS_LOCATION/lib</i> to be included in the list in the <code>LD_LIBRARY_PATH</code> environment variable, which is set by the <i>$GLOBUS_LOCATION/libexec/globus-script-initializer</i> script, which should be called from any <code>myproxy-server</code> startup script. Alternatively, to set <code>LD_LIBRARY_PATH</code> appropriately for the Globus libraries in an interactive shell, source <i>$GLOBUS_LOCATION/etc/globus-user-env.sh</i> (for sh shells) or <i>$GLOBUS_LOCATION/etc/globus-user.env.csh</i> (for csh shells).</p>
<dt><code>MYPROXY_SERVER_PORT</code></p>
<dd>Specifies the port where the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) is running. This environment variable can be used in place of the <code>-p</code> option.</p>
<dt><code>X509_USER_CERT</code></p>
<dd>Specifies an alternative location for the server&#8217;s certificate. By default, the server uses <i>/etc/grid-security/hostcert.pem</i> when running as root or <i>~/.globus/usercert.pem</i> when running as non-root.</p>
<dt><code>X509_USER_KEY</code></p>
<dd>Specifies an alternative location for the server&#8217;s private key. By default, the server uses <i>/etc/grid-security/hostkey.pem</i> when running as root or <i>~/.globus/userkey.pem</i> when running as non-root.</p>
<dt><code>X509_USER_PROXY</code></p>
<dd>Specifies an alternative location for the server&#8217;s certificate and private key (in the same file). Use when running the server with a proxy credential. Note that the proxy will need to be periodically renewed before expiration to allow the <code>myproxy-server</code> to keep functioning. When the <code>myproxy-server</code> runs with a non-host credential, clients must have the <code>MYPROXY_SERVER_DN</code> environment variable set to the distinguished name of the certificate being used by the server.</p>
<dt><code>X509_CERT_DIR</code></p>
<dd>Specifies a non-standard location for the CA certificates directory.</p>
<dt><code>MYPROXY_KEYBITS</code></p>
<dd>Specifies the size for RSA keys generated by MyProxy. By default, MyProxy generates 2048 bit RSA keys. Set this environment variable to &quot;1024&quot; for 1024 bit RSA keys.</dl>
<h2>Authors</h2>
<p>See <code><a rel="nofollow" href="http://grid.ncsa.illinois.edu/myproxy/about">http://grid.ncsa.illinois.edu/myproxy/about</a></code> for the list of MyProxy authors.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-myproxy-change-pass-phrase/">myproxy-change-pass-phrase</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-destroy/">myproxy-destroy</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-get-trustroots/">myproxy-get-trustroots</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-info/">myproxy-info</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-init/">myproxy-init</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-logon/">myproxy-logon</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-retrieve/">myproxy-retrieve</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-store/">myproxy-store</a></code>(1), <code><a href="/docs/linux/man/5-myproxy-server-config/">myproxy-server.config</a></code>(5), <code><a href="/docs/linux/man/8-myproxy-admin-adduser/">myproxy-admin-adduser</a></code>(8), <code><a href="/docs/linux/man/8-myproxy-admin-change-pass/">myproxy-admin-change-pass</a></code>(8), <code><a href="/docs/linux/man/8-myproxy-admin-load-credential/">myproxy-admin-load-credential</a></code>(8), <code><a href="/docs/linux/man/8-myproxy-admin-query/">myproxy-admin-query</a></code>(8) </p>
