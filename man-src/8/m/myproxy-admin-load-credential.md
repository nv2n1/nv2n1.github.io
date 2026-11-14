---
title: "myproxy-admin-load-credential(8)"
name: "myproxy-admin-load-credential"
section: "8"
letter: "m"
url: "/docs/linux/man/8-myproxy-admin-load-credential/"
description: "myproxy-admin-load-credential – directly load repository"
---

<p>myproxy-admin-load-credential &#8211; directly load repository</p>
<h2>Synopsis</h2>
<p><code>myproxy-admin-load-credential</code> [ <i>options</i> ]</p>
<h2>Description</h2>
<p>The <code>myproxy-admin-load-credential</code> command stores a credential directly in the local MyProxy repository. It must be run from the account that owns the repository. Many of the options are similar to <code><a href="/docs/linux/man/1-myproxy-init/">myproxy-init</a></code>(1). However, unlike <code>myproxy-init</code>, <code>myproxy-admin-load-credential</code> does not create a proxy from the source credential but instead directly loads a copy of the source credential into the repository. The pass phrase of the source credential is unchanged. Use <code><a href="/docs/linux/man/8-myproxy-admin-change-pass/">myproxy-admin-change-pass</a></code>(8) to change the pass phrase after the credential is stored if desired. Proxy credentials with default lifetime of 12 hours can then be retrieved by <code><a href="/docs/linux/man/1-myproxy-logon/">myproxy-logon</a></code>(1) using the MyProxy passphrase. The command&#8217;s behavior is controlled by the following options.</p>
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
<dt><code>-s</code><i> dir, </i><code>&#8211;storage</code><i> dir</i></p>
<dd>Specifies the location of the credential storage directory. The directory must be accessible only by the user running the <code>myproxy-server</code> process for security reasons. Default: /var/lib/myproxy or /var/myproxy or $GLOBUS_LOCATION/var/myproxy</p>
<dt><code>-c</code><i> filename, </i><code>&#8211;certfile</code><i> filename</i></p>
<dd>Specifies the filename of the source certificate. This is a required parameter.</p>
<dt><code>-y</code><i> filename, </i><code>&#8211;keyfile</code><i> filename</i></p>
<dd>Specifies the filename of the source private key. This is a required parameter. If the private key is encrypted, MyProxy clients will be required to give the encryption passphrase to access the key. When used with <code>-R</code> or <code>-Z</code>, it is common for the private key to not be encrypted, so MyProxy clients can access the credentials using only certificate-based authentication and authorization.</p>
<dt><code>-l</code><i> username, </i><code>&#8211;username</code><i> username</i></p>
<dd>Specifies the MyProxy account under which the credential should be stored. By default, the command uses the value of the <code>LOGNAME</code> environment variable. Use this option to specify a different account username on the MyProxy server. The MyProxy username need not correspond to a real Unix username.</p>
<dt><code>-t</code><i> hours, </i><code>&#8211;proxy_lifetime</code><i> hours</i></p>
<dd>Specifies the maximum lifetime of credentials retrieved from the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) using the stored credential. Default: 12 hours</p>
<dt><code>-d, &#8211;dn_as_username</code></p>
<dd>Use the certificate subject (DN) as the username.</p>
<dt><code>-a, &#8211;allow_anonymous_retrievers</code></p>
<dd>Allow credentials to be retrieved with just pass phrase authentication. By default, only entities with credentials that match the <code><a href="/docs/linux/man/5-myproxy-server-config/">myproxy-server.config</a></code>(5) default retriever policy may retrieve credentials. This option allows entities without existing credentials to retrieve a credential using pass phrase authentication by including &quot;anonymous&quot; in the set of allowed retrievers. The <code><a href="/docs/linux/man/5-myproxy-server-config/">myproxy-server.config</a></code>(5) server-wide policy must also allow &quot;anonymous&quot; clients for this option to have an effect.</p>
<dt><code>-A, &#8211;allow_anonymous_renewers</code></p>
<dd>Allow credentials to be renewed by any client. Any client with a valid credential with a subject name that matches the stored credential may retrieve a new credential from the MyProxy repository if this option is given. Since this effectively defeats the purpose of proxy credential lifetimes, it is not recommended. It is included only for sake of completeness.</p>
<dt><code>-r</code><i> name, </i><code>&#8211;retrievable_by</code><i> name</i></p>
<dd>Allow the specified entity to retrieve credentials. See <code>-x</code> and <code>-X</code> options for controlling name matching behavior.</p>
<dt><code>-E</code><i> name, </i><code>&#8211;retrieve_key</code><i> name</i></p>
<dd>Allow the specified entity to retrieve end-entity credentials. See <code>-x</code> and <code>-X</code> options for controlling name matching behavior.</p>
<dt><code>-R</code><i> name, </i><code>&#8211;renewable_by</code><i> name</i></p>
<dd>Allow the specified entity to renew credentials. See <code>-x</code> and <code>-X</code> options for controlling name matching behavior.</p>
<dt><code>-Z</code><i> name, </i><code>&#8211;retrievable_by_cert</code><i> name</i></p>
<dd>Allow the specified entity to retrieve credentials without a passphrase. See <code>-x</code> and <code>-X</code> options for controlling name matching behavior.</p>
<dt><code>-x, &#8211;regex_dn_match</code></p>
<dd>Specifies that names used with following options <code>-r</code>, <code>-E</code>, <code>-R</code>, and <code>-Z</code> will be matched against the full certificate subject distinguished name (DN) according to <code>REGULAR EXPRESSIONS</code> in <code><a href="/docs/linux/man/5-myproxy-server-config/">myproxy-server.config</a></code>(5).</p>
<dt><code>-X, &#8211;match_cn_only</code></p>
<dd>Specifies that names used with following options <code>-r</code>, <code>-E</code>, <code>-R</code>, and <code>-Z</code> will be matched against the certificate subject common name (CN) according to <code>REGULAR EXPRESSIONS</code> in <code><a href="/docs/linux/man/5-myproxy-server-config/">myproxy-server.config</a></code>(5). For example, if an argument of <code>-r </code> &quot;Jim Basney&quot; is specified, then the resulting policy will be &quot;*/CN=Jim Basney&quot;. This is the default behavior.</p>
<dt><code>-k</code><i> name, </i><code>&#8211;credname</code><i> name</i></p>
<dd>Specifies the credential name.</p>
<dt><code>-K</code><i> description, </i><code>&#8211;creddesc</code><i> description</i></p>
<dd>Specifies credential description.</dl>
<h2>Exit Status</h2>
<p>0 on success, &gt;0 on error</p>
<h2>Authors</h2>
<p>See <code><a rel="nofollow" href="http://grid.ncsa.illinois.edu/myproxy/about">http://grid.ncsa.illinois.edu/myproxy/about</a></code> for the list of MyProxy authors.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-myproxy-change-pass-phrase/">myproxy-change-pass-phrase</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-destroy/">myproxy-destroy</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-info/">myproxy-info</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-init/">myproxy-init</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-logon/">myproxy-logon</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-retrieve/">myproxy-retrieve</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-store/">myproxy-store</a></code>(1), <code><a href="/docs/linux/man/5-myproxy-server-config/">myproxy-server.config</a></code>(5), <code><a href="/docs/linux/man/8-myproxy-admin-adduser/">myproxy-admin-adduser</a></code>(8), <code><a href="/docs/linux/man/8-myproxy-admin-change-pass/">myproxy-admin-change-pass</a></code>(8), <code><a href="/docs/linux/man/8-myproxy-admin-query/">myproxy-admin-query</a></code>(8), <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) </p>
