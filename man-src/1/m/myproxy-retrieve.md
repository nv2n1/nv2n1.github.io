---
title: "myproxy-retrieve(1)"
name: "myproxy-retrieve"
section: "1"
letter: "m"
url: "/docs/linux/man/1-myproxy-retrieve/"
description: "myproxy-retrieve – retrieve an end-entity credential"
---

<h2>NAME</h2>
<p> myproxy-retrieve &#8211; retrieve an end-entity credential</p>
<h2>SYNOPSIS</h2>
<p> <code>myproxy-retrieve</code> [ <i>options</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>myproxy-retrieve</code> command retrieves a credential directly from the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) that was previously stored using <code><a href="/docs/linux/man/1-myproxy-init/">myproxy-init</a></code>(1) or <code><a href="/docs/linux/man/1-myproxy-store/">myproxy-store</a></code>(1). Unlike <code><a href="/docs/linux/man/1-myproxy-logon/">myproxy-logon</a></code>(1), this command transfers the private key in the repository over the network (over a private channel). To obtain a proxy credential, we recommend using <code><a href="/docs/linux/man/1-myproxy-logon/">myproxy-logon</a></code>(1) instead. </p>
<p> In the default mode, the command prompts for the pass phrase associated with the credential to be retrieved and stores the retrieved credential in the standard location ( <i>~/.globus/usercert.pem</i> and <i>~/.globus/userkey.pem</i>). You could then run <code>grid-proxy-init</code> to create a proxy credential from the retrieved credentials.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Displays command usage text and exits.</p>
<dt><code>-u, &#8211;usage</code></p>
<dd> Displays command usage text and exits.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Enables verbose debugging output to the terminal.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Displays version information and exits.</p>
<dt><code>-s</code><i> hostname[:port], </i><code>&#8211;pshost</code><i> hostname[:port]</i></p>
<dd> Specifies the hostname(s) of the myproxy-server(s). Multiple hostnames, each hostname optionally followed by a &#8216;:&#8217; and port number, may be specified in a comma-separated list. This option is required if the <code>MYPROXY_SERVER</code> environment variable is not defined. If specified, this option overrides the <code>MYPROXY_SERVER</code> environment variable. If a port number is specified with a hostname, it will override the -p option as well as the <code>MYPROXY_SERVER_PORT</code> environment variable for that host.</p>
<dt><code>-p</code><i> port, </i><code>&#8211;psport</code><i> port</i></p>
<dd> Specifies the TCP port number of the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8). Default: 7512</p>
<dt><code>-l</code><i> username, </i><code>&#8211;username</code><i> username</i></p>
<dd> Specifies the MyProxy account under which the credential to retrieve is stored. By default, the command uses the value of the <code>LOGNAME</code> environment variable. Use this option to specify a different account username on the MyProxy server. The MyProxy username need not correspond to a real Unix username.</p>
<dt><code>-d, &#8211;dn_as_username</code></p>
<dd> Use the certificate subject (DN) as the default username, instead of the <code>LOGNAME </code> environment variable. When used with the <code>-a</code> option, the certificate subject of the authorization credential is used. Otherwise, the certificate subject of the default credential is used.</p>
<dt><code>-t</code><i> hours, </i><code>&#8211;proxy_lifetime</code><i> hours</i></p>
<dd> Specifies the lifetime of credentials retrieved from the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) using the stored credential. The resulting lifetime is the shorter of the requested lifetime and the lifetime specified when the credential was stored using <code><a href="/docs/linux/man/1-myproxy-init/">myproxy-init</a></code>(1). Default: 12 hours</p>
<dt><code>-c</code><i> filename, </i><code>&#8211;certfile</code><i> filename</i></p>
<dd> Specifies the filename of where the certificate will be stored.</p>
<dt><code>-y</code><i> filename, </i><code>&#8211;keyfile</code><i> filename</i></p>
<dd> Specifies the filename of where the private key will be stored.</p>
<dt><code>-a</code><i> file, </i><code>&#8211;authorization</code><i> file</i></p>
<dd> Use this option to specify an existing, valid credential that you want to renew. Renewing a credential generally requires two certificate-based authentications. The client authenticates with its identity, using the credential in the standard location or specified by <code>X509_USER_PROXY</code> or <code>X509_USER_CERT</code> and <code>X509_USER_KEY</code> in addition to authenticating with the existing credential, in the location specified by this option, that it wants to renew.</p>
<dt><code>-k</code><i> name, </i><code>&#8211;credname</code><i> name</i></p>
<dd> Specifies the name of the credential that is to be retrieved or renewed.</p>
<dt><code>-S, &#8211;stdin_pass</code></p>
<dd> By default, the command prompts for a passphrase and reads the passphrase from the active tty. When running the command non-interactively, there may be no associated tty. Specifying this option tells the command to read passphrases from standard input without prompts or confirmation.</p>
<dt><code>-T, &#8211;trustroots</code></p>
<dd> Retrieve CA certificates directory from server (if available) to store in the location specified by the <code>X509_CERT_DIR</code> environment variable if set or <i>/etc/grid-security/certificates</i> if running as root or <i>~/.globus/certificates</i> if running as non-root.</p>
<dt><code>-n, &#8211;no_passphrase</code></p>
<dd> Don&#8217;t prompt for a credential passphrase. Use other methods for authentication, such as Kerberos ticket or X.509 certificate.</dl>
<h2>EXIT STATUS</h2>
<p> 0 on success, &gt;0 on error</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>GLOBUS_GSSAPI_NAME_COMPATIBILITY</code></p>
<dd> This client will, by default, perform a reverse-DNS lookup to determine the FQHN (Fully Qualified Host Name) to use in verifying the identity of the server by checking the FQHN against the CN in server&#8217;s certificate. Setting this variable to <code>STRICT_RFC2818</code> will cause the reverse-DNS lookup to NOT be performed and the user-specified name to be used instead. This variable setting will be ignored if <code>MYPROXY_SERVER_DN</code> (described later) is set.</p>
<dt><code>MYPROXY_SERVER</code></p>
<dd> Specifies the hostname(s) where the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) is running. Multiple hostnames can be specified in a comma separated list with each hostname optionally followed by a &#8216;:&#8217; and port number. This environment variable can be used in place of the <code>-s</code> option.</p>
<dt><code>MYPROXY_SERVER_PORT</code></p>
<dd> Specifies the port where the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) is running. This environment variable can be used in place of the <code>-p</code> option.</p>
<dt><code>MYPROXY_SERVER_DN</code></p>
<dd> Specifies the distinguished name (DN) of the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8). All MyProxy client programs authenticate the server&#8217;s identity. By default, MyProxy servers run with host credentials, so the MyProxy client programs expect the server to have a distinguished name with &quot;/CN=host/&lt;fqhn&gt;&quot; or &quot;/CN=myproxy/&lt;fqhn&gt;&quot; or &quot;/CN=&lt;fqhn&gt;&quot; (where &lt;fqhn&gt; is the fully-qualified hostname of the server). If the server is running with some other DN, you can set this environment variable to tell the MyProxy clients to accept the alternative DN. Also see <code>GLOBUS_GSSAPI_NAME_COMPATIBILITY</code> above.</p>
<dt><code>MYPROXY_TCP_PORT_RANGE</code></p>
<dd> Specifies a range of valid port numbers in the form &quot;min,max&quot; for the client side of the network connection to the server. By default, the client will bind to any available port. Use this environment variable to restrict the ports used to a range allowed by your firewall. If unset, MyProxy will follow the setting of the <code>GLOBUS_TCP_PORT_RANGE</code> environment variable.</p>
<dt><code>X509_USER_CERT</code></p>
<dd> Specifies a non-standard location for the certificate to be used for authentication to the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8). Also specifies the location for where the retrieved certificate will be stored unless the <code>-c</code> option is given.</p>
<dt><code>X509_USER_KEY</code></p>
<dd> Specifies a non-standard location for the private key to be used for authentication to the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8). Also specifies the location for where the retrieved private key will be stored unless the <code>-y</code> option is given.</p>
<dt><code>X509_USER_PROXY</code></p>
<dd> Specifies a non-standard location for the proxy credential to be used for authentication to the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8).</p>
<dt><code>X509_CERT_DIR</code></p>
<dd> Specifies a non-standard location for the CA certificates directory.</dl>
<h2>AUTHORS</h2>
<p> See <code><a rel="nofollow" href="http://grid.ncsa.illinois.edu/myproxy/about">http://grid.ncsa.illinois.edu/myproxy/about</a></code> for the list of MyProxy authors.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-myproxy-change-pass-phrase/">myproxy-change-pass-phrase</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-destroy/">myproxy-destroy</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-get-trustroots/">myproxy-get-trustroots</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-info/">myproxy-info</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-init/">myproxy-init</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-logon/">myproxy-logon</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-store/">myproxy-store</a></code>(1), <code><a href="/docs/linux/man/5-myproxy-server-config/">myproxy-server.config</a></code>(5), <code><a href="/docs/linux/man/8-myproxy-admin-adduser/">myproxy-admin-adduser</a></code>(8), <code><a href="/docs/linux/man/8-myproxy-admin-change-pass/">myproxy-admin-change-pass</a></code>(8), <code><a href="/docs/linux/man/8-myproxy-admin-load-credential/">myproxy-admin-load-credential</a></code>(8), <code><a href="/docs/linux/man/8-myproxy-admin-query/">myproxy-admin-query</a></code>(8), <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) </p>
<h2>Index</h2>
