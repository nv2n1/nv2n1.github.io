---
title: "myproxy-init(1)"
name: "myproxy-init"
section: "1"
letter: "m"
url: "/docs/linux/man/1-myproxy-init/"
description: "myproxy-init – store a credential for later retrieval"
---

<h2>NAME</h2>
<p> myproxy-init &#8211; store a credential for later retrieval</p>
<h2>SYNOPSIS</h2>
<p> <code>myproxy-init </code> [ <i>options</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>myproxy-init</code> command uploads a credential to a <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) for later retrieval. In the default mode, the command first prompts for the user&#8217;s Grid pass phrase (if needed), which is used to create a proxy credential. The command then prompts for a MyProxy pass phrase, which will be required to later retrieve the credential. The MyProxy pass phrase must be entered a second time for confirmation. A credential with a lifetime of one week (by default) is then delegated to the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) and stored with the given MyProxy pass phrase. Proxy credentials with default lifetime of 12 hours can then be retrieved by <code><a href="/docs/linux/man/1-myproxy-logon/">myproxy-logon</a></code>(1) using the MyProxy passphrase. The default behavior can be overridden by options specified below. </p>
<p> The <code>myproxy-init</code> command can also upload a credential to a <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) to support credential renewal. Renewal allows a trusted service (for example, a batch job scheduler) to obtain a new credential for a user before the existing credential it has for that user expires. The <code>-R</code> argument to <code>myproxy-init</code> configures the credential for renewal by the specified service. Renewal requires two authentications. The renewing service must authenticate with its own credentials, matching the distinquished name specified by the <code>-R</code> argument, and must also authenticate with an existing credential that matches the distinguished name of the stored credential, to retrieve a new credential. </p>
<p> A credential may be used either for retrieval or renewal but not both. If both are desired, upload a different credential for each use, with a different name using the <code>-k</code> option. </p>
<p> The hostname where the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) is running must be specified by either defining the <code>MYPROXY_SERVER</code> environment variable or the <code>-s</code> option. </p>
<p> By default, <code>myproxy-init</code> will create a proxy credential from the user&#8217;s end-entity credentials at <i>~/.globus/usercert.pem</i> and <i>~/.globus/userkey.pem</i> to delegate to the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8). To specify an alternate location for the source certificate and key to delegate, use the <code>X509_USER_CERT</code> and <code>X509_USER_KEY</code> environment variables. To use a proxy credential as the source of the delegation, set both environment variables to the location of the proxy credential. To delegate a &quot;legacy globus proxy&quot;, set the <code>GT_PROXY_MODE</code> environment variable to &quot;old&quot;. To delegate an &quot;RFC 3820 compliant proxy&quot;, set the <code>GT_PROXY_MODE</code> environment variable to &quot;rfc&quot;.</p>
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
<dd> Specifies the MyProxy account under which the credential should be stored. By default, the command uses the value of the <code>LOGNAME</code> environment variable. Use this option to specify a different account username on the MyProxy server. The MyProxy username need not correspond to a real Unix username.</p>
<dt><code>-c</code><i> hours, </i><code>&#8211;cred_lifetime</code><i> hours</i></p>
<dd> Specifies the lifetime of the credential stored on the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) in hours. Specify <i>0</i> for the maximum possible lifetime, i.e., the lifetime of the original credential. Default: 1 week (168 hours)</p>
<dt><code>-t</code><i> hours, </i><code>&#8211;proxy_lifetime</code><i> hours</i></p>
<dd> Specifies the maximum lifetime of credentials retrieved from the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) using the stored credential. Default: 12 hours</p>
<dt><code>-C</code><i> filename, </i><code>&#8211;certfile</code><i> filename</i></p>
<dd> Specifies the filename of the source certificate.</p>
<dt><code>-y</code><i> filename, </i><code>&#8211;keyfile</code><i> filename</i></p>
<dd> Specifies the filename of the source private key.</p>
<dt><code>-d, &#8211;dn_as_username</code></p>
<dd> Use the certificate subject (DN) as the default username, instead of the <code>LOGNAME </code> environment variable.</p>
<dt><code>-a, &#8211;allow_anonymous_retrievers</code></p>
<dd> Allow credentials to be retrieved with just pass phrase authentication. By default, only entities with credentials that match the <code><a href="/docs/linux/man/5-myproxy-server-config/">myproxy-server.config</a></code>(5) default retriever policy may retrieve credentials. This option allows entities without existing credentials to retrieve a credential using pass phrase authentication by including &quot;anonymous&quot; in the set of allowed retrievers. The <code><a href="/docs/linux/man/5-myproxy-server-config/">myproxy-server.config</a></code>(5) server-wide policy must also allow &quot;anonymous&quot; clients for this option to have an effect.</p>
<dt><code>-A, &#8211;allow_anonymous_renewers</code></p>
<dd> Allow credentials to be renewed by any client. Any client with a valid credential with a subject name that matches the stored credential may retrieve a new credential from the MyProxy repository if this option is given. Since this effectively defeats the purpose of proxy credential lifetimes, it is not recommended. It is included only for sake of completeness.</p>
<dt><code>-r</code><i> name, </i><code>&#8211;retrievable_by</code><i> name</i></p>
<dd> Allow the specified entity to retrieve credentials. See <code>-x</code> and <code>-X</code> options for controlling name matching behavior.</p>
<dt><code>-R</code><i> name, </i><code>&#8211;renewable_by</code><i> name</i></p>
<dd> Allow the specified entity to renew credentials. See <code>-x</code> and <code>-X</code> options for controlling name matching behavior. This option implies <code>-n</code> since passphrase authentication is not used for credential renewal.</p>
<dt><code>-Z</code><i> name, </i><code>&#8211;retrievable_by_cert</code><i> name</i></p>
<dd> Allow the specified entity to retrieve credentials without a passphrase. See <code>-x</code> and <code>-X</code> options for controlling name matching behavior. This option implies <code>-n</code>.</p>
<dt><code>-x, &#8211;regex_dn_match</code></p>
<dd> Specifies that names used with following options <code>-r</code>, <code>-R</code>, and <code>-Z</code> will be matched against the full certificate subject distinguished name (DN) according to <code>REGULAR EXPRESSIONS</code> in <code><a href="/docs/linux/man/5-myproxy-server-config/">myproxy-server.config</a></code>(5).</p>
<dt><code>-X, &#8211;match_cn_only</code></p>
<dd> Specifies that names used with following options <code>-r</code>, <code>-R</code>, and <code>-Z</code> will be matched against the certificate subject common name (CN) according to <code>REGULAR EXPRESSIONS</code> in <code><a href="/docs/linux/man/5-myproxy-server-config/">myproxy-server.config</a></code>(5). For example, if an argument of <code>-r </code> &quot;Jim Basney&quot; is specified, then the resulting policy will be &quot;*/CN=Jim Basney&quot;. This is the default behavior.</p>
<dt><code>-k</code><i> name, </i><code>&#8211;credname</code><i> name</i></p>
<dd> Specifies the credential name.</p>
<dt><code>-K</code><i> description, </i><code>&#8211;creddesc</code><i> description</i></p>
<dd> Specifies credential description.</p>
<dt><code>-S, &#8211;stdin_pass</code></p>
<dd> By default, the command prompts for a passphrase and reads the passphrase from the active tty. When running the command non-interactively, there may be no associated tty. Specifying this option tells the command to read passphrases from standard input without prompts or confirmation.</p>
<dt><code>-L, &#8211;local_proxy</code></p>
<dd> In addition to storing a proxy credential on the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) with lifetime set by <code>&#8211;cred_lifetime</code> (default 1 week), create a local proxy credential with lifetime set by <code>&#8211;proxy_lifetime</code> (default 12 hours).</p>
<dt><code>-n, &#8211;no_passphrase</code></p>
<dd> Don&#8217;t prompt for a credential passphrase. Store credentials without a credential passphrase, to be protected by other methods, such as PAM, SASL, or certificate-based authentication. This option is implied by <code>-R</code> since passphrase authentication is not used for credential renewal. Note that the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) always requires some type of authentication for retrieving credentials, so if you store a credential with no passphrase and other authentication methods are not configured, the credential will not be accessible.</p>
<dt><code>-m</code><i> voms, </i><code>&#8211;voms</code><i> voms</i></p>
<dd> Add VOMS attributes to the credential by running <code>voms-proxy-init</code> on the client-side before storing the credential on the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8). The VOMS VO name must be provided, as required by <code>voms-proxy-init -voms</code>. The <code>voms-proxy-init</code> command must be installed and configured to use this option. For example, the <code>VOMS_USERCONF</code> environment variable may need to be set for <code>voms-proxy-init</code> to run correctly.</dl>
<h2>EXIT STATUS</h2>
<p> 0 on success, &gt;0 on error</p>
<h2>FILES</h2>
<dl>
<dt><i>~/.globus/usercert.pem</i></p>
<dd> Default location of the certificate from which the proxy credential is created. Set the <code>X509_USER_CERT</code> environment variable to override.</p>
<dt><i>~/.globus/userkey.pem</i></p>
<dd> Default location of the private key from which the proxy credential is created. Set the <code>X509_USER_KEY</code> environment variable to override.</p>
<dt><i>/tmp/myproxy-proxy.&lt;uid&gt;.&lt;pid&gt;</i></p>
<dd> Location of the temporary proxy credential that is delegated to the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8). It is removed after the delegation is completed.</dl>
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
<dt><code>X509_USER_CERT</code></p>
<dd> Specifies a non-standard location for the certificate from which the proxy credential is created. The location may be the path to an end-entity certificate (ex. <i>~/.globus/usercert.pem</i>) or a proxy (ex. <i>/tmp/x509up_u&lt;uid&gt;</i>).</p>
<dt><code>X509_USER_KEY</code></p>
<dd> Specifies a non-standard location for the private key from which the proxy credential is created. The location may be the path to an end-entity private key (ex. <i>~/.globus/userkey.pem</i>) or a proxy (ex. <i>/tmp/x509up_u&lt;uid&gt;</i>).</p>
<dt><code>X509_CERT_DIR</code></p>
<dd> Specifies a non-standard location for the CA certificates directory.</p>
<dt><code>GT_PROXY_MODE</code></p>
<dd> Set to &quot;old&quot; to store a &quot;legacy globus proxy&quot; in the MyProxy repository. Set to &quot;rfc&quot; to store an &quot;RFC 3820 compliant proxy&quot; in the MyProxy repository.</p>
<dt><code>MYPROXY_TCP_PORT_RANGE</code></p>
<dd> Specifies a range of valid port numbers in the form &quot;min,max&quot; for the client side of the network connection to the server. By default, the client will bind to any available port. Use this environment variable to restrict the ports used to a range allowed by your firewall. If unset, MyProxy will follow the setting of the <code>GLOBUS_TCP_PORT_RANGE</code> environment variable.</p>
<dt><code>MYPROXY_KEYBITS</code></p>
<dd> Specifies the size for RSA keys generated by MyProxy. By default, MyProxy generates 2048 bit RSA keys. Set this environment variable to &quot;1024&quot; for 1024 bit RSA keys.</dl>
<h2>AUTHORS</h2>
<p> See <code><a rel="nofollow" href="http://grid.ncsa.illinois.edu/myproxy/about">http://grid.ncsa.illinois.edu/myproxy/about</a></code> for the list of MyProxy authors.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-myproxy-change-pass-phrase/">myproxy-change-pass-phrase</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-destroy/">myproxy-destroy</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-get-trustroots/">myproxy-get-trustroots</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-info/">myproxy-info</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-logon/">myproxy-logon</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-retrieve/">myproxy-retrieve</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-store/">myproxy-store</a></code>(1), <code><a href="/docs/linux/man/5-myproxy-server-config/">myproxy-server.config</a></code>(5), <code><a href="/docs/linux/man/8-myproxy-admin-adduser/">myproxy-admin-adduser</a></code>(8), <code><a href="/docs/linux/man/8-myproxy-admin-change-pass/">myproxy-admin-change-pass</a></code>(8), <code><a href="/docs/linux/man/8-myproxy-admin-load-credential/">myproxy-admin-load-credential</a></code>(8), <code><a href="/docs/linux/man/8-myproxy-admin-query/">myproxy-admin-query</a></code>(8), <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) </p>
<h2>Index</h2>
