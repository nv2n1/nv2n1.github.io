---
title: "pam_mapi(8)"
name: "pam_mapi"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_mapi/"
description: "pam_mapi – Module for authentication via MAPI against a Kopano or Zarafa server"
---

<p>pam_mapi &#8211; Module for authentication via MAPI against a Kopano or Zarafa server</p>
<h2>Synopsis</h2>
<p><code>pam_mapi.so</code> [socket=<i><a rel="nofollow" href="http://localhost:236/kopano">http://localhost:236/kopano</a></i>] [socket=<i><a href="http://localhost:236/zarafa">http://localhost:236/zarafa</a></i>] [service=<i>pop3|imap|mobile|outlook</i>] [try_first_pass] [use_first_pass] [quiet] [debug]</p>
<h2>Description</h2>
<p>The pam_mapi module is used to verify a username/password pair via MAPI in SOAP against a Kopano server of Kopano Core and a Zarafa server of the Zarafa Collaboration Platform, respectively.</p>
<h2>Options</h2>
<p><code>socket=</code><i><a rel="nofollow" href="http://localhost:236/kopano">http://localhost:236/kopano</a></i><br />
 <code>socket=</code><i><a rel="nofollow" href="http://localhost:236/zarafa">http://localhost:236/zarafa</a></i></p>
<dl>
<dd>Use the socket <i><a rel="nofollow" href="http://localhost:236/kopano">http://localhost:236/kopano</a></i> for the Kopano login or <i><a href="http://localhost:236/zarafa">http://localhost:236/zarafa</a></i> for the Zarafa login. This also can be HTTPS if the Kopano or Zarafa server is not running on the same machine. The default socket <i><a href="http://localhost:236/kopano">http://localhost:236/kopano</a></i> or <i><a href="http://localhost:236/zarafa">http://localhost:236/zarafa</a></i> is used, if none has been set. </p>
<p> Be very careful when specifying the UNIX socket here, because the default Kopano or Zarafa configuration option <code>local_admin_users</code> in <i>/etc/kopano/server.cfg</i> or <i>/etc/zarafa/server.cfg</i> contains the root user and saslauthd runs as root user by default, too. In this case, any authentication would succeed, even if wrong credentials are provided, which could make the SMTP service an open relay.</dl>
<p> <code>service=</code><i>pop3|imap|mobile|outlook</i></p>
<dl>
<dd>Try authentication by using the given service/feature. Since Kopano 8.0.0 and Zarafa 7.0.0 some features can be enabled and disabled on a per-user basis. If e.g. IMAP is disabled for a specific user any IMAP login will fail. Using this option the same behaviour can be applied to pam_mapi for e.g. SMTP authentication. </p>
<p> Valid values are values from option <code>disabled_features</code> in <i>/etc/kopano/server.cfg</i> or <i>/etc/zarafa/server.cfg</i>. Multiple services can be listed using a pipe character and behave like a digital logic OR gate. So <i>service=pop3|imap</i> will permit authentication if either the feature POP3 or IMAP has been enabled for this user.</dl>
<p> <code>try_first_pass</code></p>
<dl>
<dd>Use the authentication token previously obtained by another module that did the conversation with the application. If this token can not be obtained then the module will try to converse. This option can be used for stacking different modules that need to deal with the authentication tokens.</dl>
<p> <code>use_first_pass</code></p>
<dl>
<dd>Use the authentication token previously obtained by another module that did the conversation with the application. If this token can not be obtained then the module will fail. This option can be used for stacking different modules that need to deal with the authentication tokens.</dl>
<p> <code>quiet</code></p>
<dl>
<dd>Do not treat <code>MAPI_E_LOGON_FAILED</code> authentication failures as errors that need to be logged to <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3). This option can be used for stacking different modules, because the existence of an account can be only assured after a succeeded authentication due to limited PAM account functionality.</dl>
<p> <code>debug</code></p>
<dl>
<dd>Turns on debugging via <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3).</dl>
<p> Invalid arguments are logged with <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3).</p>
<h2>Module Types Provided</h2>
<p>The <code>auth</code> and <code>account</code> module types are provided.</p>
<h2>Return Values</h2>
<p>PAM_AUTHINFO_UNAVAIL</p>
<dl>
<dd>Authentication service cannot retrieve authentication info.</dl>
<p> PAM_AUTHTOK_ERR</p>
<dl>
<dd>Authentication token manipulation error.</dl>
<p> PAM_AUTHTOK_RECOVERY_ERR</p>
<dl>
<dd>Authentication information cannot be recovered.</dl>
<p> PAM_AUTH_ERR</p>
<dl>
<dd>Authentication failure.</dl>
<p> PAM_IGNORE</p>
<dl>
<dd>Ignore this module.</dl>
<p> PAM_SERVICE_ERR</p>
<dl>
<dd>Error in service module.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>Success.</dl>
<h2>Examples</h2>
<p>The most typical usage in <i>/etc/pam.d/smtp</i> when authenticating only against Kopano or Zarafa users would be: </p>
<dl>
<dd>
<pre>#%PAM-1.0
auth required pam_mapi.so try_first_pass
account required pam_mapi.so</pre>
</dl>
<p> Since Kopano 8.0.0 and Zarafa 7.0.0 some features can be enabled and disabled on per-user basis. Previous configuration would pass authentication even if e.g. IMAP is disabled for a specific user. By adding the service option one of the given features has to be enabled to pass authentication: </p>
<dl>
<dd>
<pre>#%PAM-1.0
auth required pam_mapi.so try_first_pass service=imap
account required pam_mapi.so</pre>
</dl>
<p> Another common usage in <i>/etc/pam.d/smtp</i> could be authenticating against Linux system and Kopano/Zarafa users. However this configuration depends heavily on the used Linux distribution. Fortunately in many cases the following two lines simply have to be added (before the existing lines): </p>
<dl>
<dd>
<pre>auth sufficient pam_mapi.so try_first_pass quiet
account sufficient pam_mapi.so</pre>
</dl>
<p> On Red Hat Enterprise Linux 5 (and derivates such as CentOS) the authentication against Linux system and Kopano/Zarafa users looks like this: </p>
<dl>
<dd>
<pre>#%PAM-1.0
auth sufficient pam_mapi.so try_first_pass quiet
auth include system-auth
account sufficient pam_mapi.so
account include system-auth</pre>
</dl>
<p> The same configuration for Red Hat Enterprise Linux 6 and 7 (including CentOS): </p>
<dl>
<dd>
<pre>#%PAM-1.0
auth sufficient pam_mapi.so try_first_pass quiet
auth include password-auth
account sufficient pam_mapi.so
account include password-auth</pre>
</dl>
<p> Keep in mind while editing, that <i>/etc/pam.d/smtp</i> could be a symbolic link at various Linux systems.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8), <code><a href="/docs/linux/man/5-kopano-server-cfg/">kopano-server.cfg</a></code>(5), <code><a href="/docs/linux/man/1-kopano-server/">kopano-server</a></code>(1), <code><a href="/docs/linux/man/5-zarafa-server-cfg/">zarafa-server.cfg</a></code>(5), <code><a href="/docs/linux/man/1-zarafa-server/">zarafa-server</a></code>(1), <code><a href="/docs/linux/man/8-saslauthd/">saslauthd</a></code>(8)</p>
<h2>Author</h2>
<p>pam_mapi was written by Robert Scheck &lt;kopano [at] robert-scheck.de&gt;.</p>
