---
title: "myproxy-admin-query(8)"
name: "myproxy-admin-query"
section: "8"
letter: "m"
url: "/docs/linux/man/8-myproxy-admin-query/"
description: "myproxy-admin-query – query MyProxy repository contents"
---

<p>myproxy-admin-query &#8211; query MyProxy repository contents</p>
<h2>Synopsis</h2>
<p><code>myproxy-admin-query</code> [ <i>options</i> ]</p>
<h2>Description</h2>
<p>The <code>myproxy-admin-query</code> command displays information about the credentials stored in the MyProxy repository. It can also be used to remove credentials from the repository, by combining query options with <code>&#8211;remove</code>. It accesses the repository directly and must be run on the machine where the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) is installed from the account that owns the repository. </p>
<p> An example cron job for running <code>myproxy-admin-query</code> periodically to remove invalid (expired, revoked, etc.) credentials from the repository is provided at <i>$GLOBUS_LOCATION/share/myproxy/myproxy.cron</i>.</p>
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
<dt><code>-l</code><i> username, </i><code>&#8211;username</code><i> username</i></p>
<dd>Return information on credentials for a single username. By default, the command returns information on all credentials for all usernames.</p>
<dt><code>-k</code><i> name, </i><code>&#8211;credname</code><i> name</i></p>
<dd>Return information on the credentials with the specified name.</p>
<dt><code>-o</code><i> DN, </i><code>&#8211;owner</code><i> DN</i></p>
<dd>Return information on the credentials owned by the specified distinguished name.</p>
<dt><code>-e</code><i> hours, </i><code>&#8211;expiring_in</code><i> hours</i></p>
<dd>Return information on credentials with remaining lifetime less than the specified number of hours. For example, <code>-e</code><i> 0</i> will return all expired credentials.</p>
<dt><code>-t</code><i> hours, </i><code>&#8211;time_left</code><i> hours</i></p>
<dd>Return information on credentials with remaining lifetime greater than the specified number of hours.</p>
<dt><code>-i, &#8211;invalid</code></p>
<dd>Return information on invalid (expired, revoked, etc.) credentials.</p>
<dt><code>-s</code><i> dir, </i><code>&#8211;storage</code><i> dir</i></p>
<dd>Specifies the location of the credential storage directory. The directory must be accessible only by the user running the <code>myproxy-server</code> process for security reasons. Default: /var/lib/myproxy or /var/myproxy or $GLOBUS_LOCATION/var/myproxy</p>
<dt><code>-c</code><i> file, </i><code>&#8211;config</code><i> file</i></p>
<dd>Specifies the location of the <code>myproxy-server</code> configuration file, for OCSP options. Default: /etc/myproxy-server.config or $GLOBUS_LOCATION/etc/myproxy-server.config</p>
<dt><code>-r, &#8211;remove</code></p>
<dd>Remove the credentials matching the query from the repository. For example, <i>myproxy-admin-query -e 0 -r</i> will remove all expired credentials from the repository.</p>
<dt><code>-L</code><i> &#8216;msg&#8217;, </i><code>&#8211;lock</code><i> &#8216;msg&#8217;</i></p>
<dd>Places the credentials matching the query under an administrative lock and specifies a message to be returned on access attempts. Be sure to put the message in quotes so it is captured as one argument to the command.</p>
<dt><code>-U, &#8211;unlock</code></p>
<dd>Removes any administrative locks for the credentials matching the query.</dl>
<h2>Exit Status</h2>
<p>0 on success, &gt;0 on error</p>
<h2>Authors</h2>
<p>See <code><a rel="nofollow" href="http://grid.ncsa.illinois.edu/myproxy/about">http://grid.ncsa.illinois.edu/myproxy/about</a></code> for the list of MyProxy authors.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-myproxy-change-pass-phrase/">myproxy-change-pass-phrase</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-destroy/">myproxy-destroy</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-init/">myproxy-init</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-logon/">myproxy-logon</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-retrieve/">myproxy-retrieve</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-store/">myproxy-store</a></code>(1), <code><a href="/docs/linux/man/5-myproxy-server-config/">myproxy-server.config</a></code>(5), <code><a href="/docs/linux/man/8-myproxy-admin-adduser/">myproxy-admin-adduser</a></code>(8), <code><a href="/docs/linux/man/8-myproxy-admin-change-pass/">myproxy-admin-change-pass</a></code>(8), <code><a href="/docs/linux/man/8-myproxy-admin-load-credential/">myproxy-admin-load-credential</a></code>(8), <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) </p>
