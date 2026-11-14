---
title: "myproxy-admin-change-pass(8)"
name: "myproxy-admin-change-pass"
section: "8"
letter: "m"
url: "/docs/linux/man/8-myproxy-admin-change-pass/"
description: "myproxy-admin-change-pass – change credential passphrase"
---

<p>myproxy-admin-change-pass &#8211; change credential passphrase</p>
<h2>Synopsis</h2>
<p><code>myproxy-admin-change-pass</code> [ <i>options</i> ]</p>
<h2>Description</h2>
<p>The <code>myproxy-admin-change-pass</code> command changes the passphrase used to encrypt a credential in the MyProxy repository. The command first prompts for the current passphrase for the credential, then prompts twice for the new passphrase. If an empty passphrase is given, the credential will not be encrypted. It accesses the repository directly and must be run on the machine where the <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) is installed from the account that owns the repository.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Displays command usage text and exits.</p>
<dt><code>-u</code></p>
<dd>Displays command usage text and exits.</p>
<dt><code>-s</code><i> dir</i></p>
<dd>Specifies the location of the credential storage directory. The directory must be accessible only by the user running the <code>myproxy-server</code> process for security reasons. Default: /var/lib/myproxy or /var/myproxy or $GLOBUS_LOCATION/var/myproxy</p>
<dt><code>-l</code><i> username</i></p>
<dd>Specifies the MyProxy account under which the credential should be stored.</p>
<dt><code>-k</code><i> name</i></p>
<dd>Specifies the credential name.</p>
<dt><code>-S, &#8211;stdin_pass</code></p>
<dd>By default, the command prompts for a passphrase and reads the passphrase from the active tty. When running the command non-interactively, there may be no associated tty. Specifying this option tells the command to read passphrases from standard input without prompts or confirmation.</dl>
<h2>Exit Status</h2>
<p>0 on success, &gt;0 on error</p>
<h2>Authors</h2>
<p>See <code><a rel="nofollow" href="http://grid.ncsa.illinois.edu/myproxy/about">http://grid.ncsa.illinois.edu/myproxy/about</a></code> for the list of MyProxy authors.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-myproxy-change-pass-phrase/">myproxy-change-pass-phrase</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-destroy/">myproxy-destroy</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-info/">myproxy-info</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-init/">myproxy-init</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-logon/">myproxy-logon</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-retrieve/">myproxy-retrieve</a></code>(1), <code><a href="/docs/linux/man/1-myproxy-store/">myproxy-store</a></code>(1), <code><a href="/docs/linux/man/5-myproxy-server-config/">myproxy-server.config</a></code>(5), <code><a href="/docs/linux/man/8-myproxy-admin-adduser/">myproxy-admin-adduser</a></code>(8), <code><a href="/docs/linux/man/8-myproxy-admin-load-credential/">myproxy-admin-load-credential</a></code>(8), <code><a href="/docs/linux/man/8-myproxy-admin-query/">myproxy-admin-query</a></code>(8), <code><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></code>(8) </p>
