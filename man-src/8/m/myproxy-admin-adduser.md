---
title: "myproxy-admin-adduser(8)"
name: "myproxy-admin-adduser"
section: "8"
letter: "m"
url: "/docs/linux/man/8-myproxy-admin-adduser/"
description: "myproxy-admin-adduser – add a user or service credential"
---

<p>myproxy-admin-adduser &#8211; add a user or service credential</p>
<h2>Synopsis</h2>
<p><code>myproxy-admin-adduser</code> [ <i>options</i> ] </p>
<p> <code>myproxy-admin-addservice</code> [ <i>options</i> ]</p>
<h2>Description</h2>
<p>The <code>myproxy-admin-adduser</code> and <code>myproxy-admin-addservice</code> commands create a new credential for a user or service and load it into the MyProxy repository. They are <code><a href="/docs/linux/man/1-perl/">perl</a></code>(1) scripts that run <code>grid-cert-request</code> (a standard Globus Toolkit program) and <code>grid-ca-sign</code> (from the Globus Simple CA package) to create the credential and then run <code><a href="/docs/linux/man/8-myproxy-admin-load-credential/">myproxy-admin-load-credential</a></code>(8) to load the credential into the MyProxy repository. </p>
<p> The command prompts for the common name to be included in the new certificate (if the <code>-c</code> argument is not specified), the Globus Simple CA key password for signing the certificate, the MyProxy username (if the <code>-l</code> or <code>-d</code> arguments are not specified), and the MyProxy passphrase for the credential. Most of the command-line options for this command are passed directly to the <code><a href="/docs/linux/man/8-myproxy-admin-load-credential/">myproxy-admin-load-credential</a></code>(8) command. </p>
<p> The <code>grid-ca-sign</code> program is not provided in the MyProxy distribution. It must be installed separately, from the Globus Simple CA package.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Displays command usage text and exits.</p>
<dt><code>-u</code></p>
<dd>Displays command usage text and exits.</p>
<dt><code>-v</code></p>
<dd>Enables verbose debugging output to the terminal.</p>
<dt><code>-c</code><i> cn</i></p>
<dd>Specifies the Common Name for the new credential (for example: &quot;Jim Basney&quot;).</p>
<dt><code>-s</code><i> dir</i></p>
<dd>Specifies the location of the credential storage directory. The directory must be accessible only by the user running the <code>myproxy-server</code> process for security reasons. Default: /var/lib/myproxy or /var/myproxy or $GLOBUS_LOCATION/var/myproxy</p>
<dt><code>-l</code><i> username</i></p>
<dd>Specifies the MyProxy account under which the credential should be stored.</p>
<dt><code>-t</code><i> hours</i></p>
<dd>Specifies the maximum lifetime of credentials retrieved from the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) using the stored credential. Default: 12 hours</p>
<dt><code>-p</code><i> CA-password</i></p>
<dd>Specifies the password for the CA&#8217;s private key using the format documented in the PASS PHRASE ARGUMENTS section of <code><a href="/docs/linux/man/1-openssl/">openssl</a></code>(1).</p>
<dt><code>-n</code></p>
<dd>Disables passphrase authentication for the stored credential. If specified, the command will not prompt for a passphrase, the credential will not be encrypted by a passphrase in the repository, and the credential will not be retrievable using passphrase authentication with <code><a href="/docs/linux/man/1-myproxy-logon/">myproxy-logon</a></code>(1). This option is used for storing renewable credentials and is implied by <code>-R</code>.</p>
<dt><code>-d</code></p>
<dd>Use the certificate subject (DN) as the username.</p>
<dt><code>-a</code></p>
<dd>Allow credentials to be retrieved with just pass phrase authentication. By default, only entities with credentials that match the <code><a href="/docs/linux/man/5-myproxy-server-config/">myproxy-server.config</a></code>(5) default retriever policy may retrieve credentials. This option allows entities without existing credentials to retrieve a credential using pass phrase authentication by including &quot;anonymous&quot; in the set of allowed retrievers. The <code><a href="/docs/linux/man/5-myproxy-server-config/">myproxy-server.config</a></code>(5) server-wide policy must also allow &quot;anonymous&quot; clients for this option to have an effect.</p>
<dt><code>-A</code></p>
<dd>Allow credentials to be renewed by any client. Any client with a valid credential with a subject name that matches the stored credential may retrieve a new credential from the MyProxy repository if this option is given. Since this effectively defeats the purpose of proxy credential lifetimes, it is not recommended. It is included only for sake of completeness.</p>
<dt><code>-r</code><i> name</i></p>
<dd>Allow the specified entity to retrieve credentials. See <code>-x</code> and <code>-X</code> options for controlling name matching behavior.</p>
<dt><code>-R</code><i> name</i></p>
<dd>Allow the specified entity to renew credentials. See <code>-x</code> and <code>-X</code> options for controlling name matching behavior. This option implies <code>-n</code> since passphrase authentication is not used for credential renewal.</p>
<dt><code>-Z</code><i> name, </i><code>&#8211;retrievable_by_cert</code><i> name</i></p>
<dd>Allow the specified entity to retrieve credentials without a passphrase. See <code>-x</code> and <code>-X</code> options for controlling name matching behavior. This option implies <code>-n</code>.</p>
<dt><code>-x</code></p>
<dd>Specifies that names used with following options <code>-r</code>, <code>-R</code>, and <code>-Z</code> will be matched against the full certificate subject distinguished name (DN) according to <code>REGULAR EXPRESSIONS</code> in <code><a href="/docs/linux/man/5-myproxy-server-config/">myproxy-server.config</a></code>(5).</p>
<dt><code>-X</code></p>
<dd>Specifies that names used with following options <code>-r</code>, <code>-R</code>, and <code>-Z</code> will be matched against the certificate subject common name (CN) according to <code>REGULAR EXPRESSIONS</code> in <code><a href="/docs/linux/man/5-myproxy-server-config/">myproxy-server.config</a></code>(5). For example, if an argument of <code>-r </code> &quot;Jim Basney&quot; is specified, then the resulting policy will be &quot;*/CN=Jim Basney&quot;. This is the default behavior.</p>
<dt><code>-k</code><i> name</i></p>
<dd>Specifies the credential name.</p>
<dt><code>-K</code><i> description</i></p>
<dd>Specifies credential description.</dl>
<h2>Exit Status</h2>
<p>0 on success, &gt;0 on error</p>
<h2>Authors</h2>
<p>See <code><a rel="nofollow" href="http://grid.ncsa.illinois.edu/myproxy/about">http://grid.ncsa.illinois.edu/myproxy/about</a></code> for the list of MyProxy authors.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-myproxy-change-pass-phrase/">myproxy-change-pass-phrase</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-destroy/">myproxy-destroy</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-info/">myproxy-info</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-init/">myproxy-init</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-logon/">myproxy-logon</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-retrieve/">myproxy-retrieve</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-store/">myproxy-store</a></code>(1), <code><a href="/docs/linux/man/5-myproxy-server-config/">myproxy-server.config</a></code>(5), <code><a href="/docs/linux/man/8-myproxy-admin-change-pass/">myproxy-admin-change-pass</a></code>(8), <code><a href="/docs/linux/man/8-myproxy-admin-load-credential/">myproxy-admin-load-credential</a></code>(8), <code><a href="/docs/linux/man/8-myproxy-admin-query/">myproxy-admin-query</a></code>(8), <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) </p>
