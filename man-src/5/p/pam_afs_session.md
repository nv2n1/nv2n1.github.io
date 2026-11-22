---
title: "pam_afs_session(5)"
name: "pam_afs_session"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pam_afs_session/"
description: "pam_afs_session – AFS PAG and token PAM module"
---

<p>pam_afs_session &#8211; AFS PAG and token PAM module</p>
<h2>Synopsis</h2>
<pre> auth optional pam_afs_session.so
 session required pam_afs_session.so</pre>
<h2>Description</h2>
<p>The AFS session service module for PAM, typically installed at <i>/lib/security/pam_afs_session.so</i>, establishes new AFS sessions and obtains AFS tokens when a new session is opened for a user. It is a shared object that is dynamically loaded by the PAM subsystem as necessary, based on the system PAM configuration. PAM is a system for plugging in external authentication and session management modules so that each application doesn&#8217;t have to know the best way to check user authentication or create a user session on that system. For details on how to configure PAM on your system, see the PAM man page, often <i><a href="/docs/linux/man/7-pam/">pam</a></i>(7). </p>
<p> This module provides pam_setcred, pam_open_session, and pam_close_session implementations for AFS. Because pam_setcred is part of the auth PAM group, it also implements a dummy pam_authenticate that always succeeds (otherwise, it can&#8217;t provide a pam_setcred). </p>
<p> Make sure that this module is NEVER listed as <tt>&quot;sufficient&quot;</tt> or as the only <tt>&quot;required&quot;</tt> module in the auth group. Doing so will potentially allow users to log on without any password. There unfortunately isn&#8217;t a way to work around this and still provide pam_setcred without running afoul of a bug in (at least) Linux PAM 0.99.7.1 and probably earlier that causes authentication to fail when the final module in the auth group returns PAM_IGNORE and <tt>&quot;[default=done]&quot;</tt> was given as the action. </p>
<p> Here are the actions of this module:</p>
<dl>
<dt>pam_open_session</dt>
<dd>When a new session is opened, this module will first check to see if AFS is running on the system. If not, it will log a message and exit successfully. If AFS is running, it will place the user&#8217;s session in a new PAG (Process Authentication Group, often implemented as supplemental groups, which limits user tokens to only processes in that PAG). It will then attempt to obtain tokens, either directly if built with the Heimdal libkafs library and Kerberos support or by running an external <code>aklog</code> program. If PAG creation fails, the module will fail; if obtaining tokens fails, the module will log a warning but still return success. </dd>
<p> The module will only attempt to obtain tokens if the environment variable KRB5CCNAME is set in the environment, unless otherwise configured (see the always_aklog option). It will always create a new PAG, however.</p>
<dt>pam_close_session</dt>
<dd>If and only if pam_open_session successfully obtained AFS tokens and AFS is still running on the system, pam_close_session will delete the tokens in the current PAG (equivalent to running <code>unlog</code>). To leave the tokens after session close, set the retain_after_close option.</dd>
<dt>pam_setcred</dt>
<dd>When pam_setcred is called with the PAM_ESTABLISH_CRED flag, it will do the same as if pam_open_session was called. When pam_setcred is called with the PAM_DELETE_CRED flag, it will do the same as if pam_close_session was called. When called with the PAM_REINITIALIZE_CRED flag or the PAM_REFRESH_CRED flag, it won&#8217;t create a new PAG but instead will only attempt to get new tokens (still skipping this unless KRB5CCNAME is set in the environment or always_aklog is set).</dd></dl>
<p> This module is primarily intended for use with a Kerberos v5 authentication module. It does not itself do any user authentication; it cannot, for instance, be used to authenticate users to a <code>kaserver</code>. While it is intended for use with an <code>aklog</code> that uses Kerberos v5 ticket caches to obtain tokens, it can be used with any <code>aklog</code> implementation (always_aklog may have to be set if no Kerberos v5 ticket cache will be present). </p>
<p> This module performs no authorization checks and does not hook into password changes; it only implements the session functions and pam_setcred.</p>
<h2>Configuration</h2>
<p>The AFS session PAM module supports the following configuration options, which may be set in the PAM configuration as arguments listed after <tt>&quot;pam_afs_session.so&quot;</tt> or in the system <i>krb5.conf</i>. </p>
<p> Some of them take arguments, in which case the argument will be given after <tt>&quot;=&quot;</tt>. The rest are boolean options. To set a boolean option in the PAM configuration, just give the name of the option in the arguments. To set an option that takes an argument, follow the option name with an equal sign (<tt>&quot;=&quot;</tt>) and the value, with no separating whitespace. Whitespace in option arguments is not supported in the PAM configuration files of most PAM implementations. </p>
<p> To set an option for the PAM module in the system <i>krb5.conf</i> file, put that option in the [appdefaults] section. The AFS session PAM module will look for options either at the top level of the [appdefaults] section or in a subsection named <tt>&quot;pam-afs-session&quot;</tt> (currently, realm-specific configuration is not checked). For example, the following fragment of a <i>krb5.conf</i> file would set <i>aklog_homedir</i> to true and <i>minimum_uid</i> to 100. </p>
<pre> [appdefaults]
 aklog_homedir = true
 pam-afs-session = {
 minimum_uid = 100
 }</pre>
<p>There is no difference to the PAM module whether options are specified at the top level or in a <tt>&quot;pam-afs-session&quot;</tt> section; the <tt>&quot;pam-afs-session&quot;</tt> section is supported in case there are options that should be set for the PAM module but not for other applications. For more information on the syntax of <i>krb5.conf</i>, see <i><a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a></i>(5). </p>
<p> If the same option is set in <i>krb5.conf</i> and in the PAM configuration, the latter takes precedent. Note, however, that due to the configuration syntax, there&#8217;s no way to turn off a boolean option in the PAM configuration that was turned on in <i>krb5.conf</i>.</p>
<dl>
<dt>afs_cells=<i>cell</i>[,<i>cell</i>&#8230;]</dt>
<dd>Obtain tokens for the listed cells instead of the default local cell. If more than one cell is listed, try to obtain tokens for each cell. If specified in <i>krb5.conf</i>, the cells can be separated by any combination of spaces and commas; if specified in the PAM configuration, they must be separated by commas. </dd>
<p> If the AFS session PAM module is running an external program, this option is implemented by passing a <code>-c</code> flag with the cell as its argument for each listed cell to that program. If aklog_homedir is also set, the <code>-c</code> flags and the <code>-p</code> flag will all be passed to the external program.</p>
<dt>aklog_homedir</dt>
<dd>Try to obtain the necessary tokens to access the user&#8217;s home directory. If the libkafs token-obtaining API is used, setting this will cause the AFS session PAM module to pass the user&#8217;s home directory into that API and request that the appropriate tokens be obtained. If running an external <code>aklog</code> program, <code>aklog</code> will be called with <code>-p</code> <i>home-directory</i> where <i>home-directory</i> is the home directory of the local user for which the session is being opened or refreshed. This generally will tell <code>aklog</code> to check that path, find all AFS cells involved in access to that path, and attempt to obtain tokens for each one. Note that this means that if the user&#8217;s home directory is not in AFS, no tokens will be obtained. </dd>
<p> In either case, the user&#8217;s home directory is obtained via <i>getpwnam()</i> based on the username PAM says we are authenticating.</p>
<dt>always_aklog</dt>
<dd>Normally, the AFS session PAM module only tries to obtain tokens if KRB5CCNAME is set in the PAM environment. If this option is set, it will always attempt to obtain tokens. This is only useful if it is configured to run an external <code>aklog</code> program. </dd>
<p> This can be used if your environment doesn&#8217;t correctly set KRB5CCNAME in the environment for some reason, or if your <code>aklog</code> doesn&#8217;t rely on a Kerberos ticket cache to obtain tokens (or can find the cache on its own via some other means).</p>
<dt>debug</dt>
<dd>If this option is set, additional trace information will be logged to syslog with priority LOG_DEBUG.</dd>
<dt>ignore_root</dt>
<dd>If this option is set, the AFS session PAM module won&#8217;t take any action (and will exit successfully) if the account for which the session is being established is named <tt>&quot;root&quot;</tt>.</dd>
<dt>kdestroy</dt>
<dd>If this option is set and the AFS session PAM module was built with Kerberos support, the user&#8217;s ticket cache will be destroyed after tokens are obtained successfully. If tokens are not obtained successfully, the ticket cache will be left intact. Please note that this is not properly a security feature, since the ticket cache will still be written to disk between the time the Kerberos PAM module authenticates the user and the time the AFS session PAM module is run. It can, however, be used to reduce the window during which Kerberos ticket caches are lying about if the only use one has for ticket caches is to obtain AFS tokens.</dd>
<dt>minimum_uid=<i>uid</i></dt>
<dd>If this option is set, the AFS session PAM module won&#8217;t take any action (and will exit successfully) if the account for which the session is being established has a UID lower than <i>uid</i>.</dd>
<dt>nopag</dt>
<dd>If this option is set, no PAG will be created. Be careful when using this option, since it means that the user will inherit a PAG from the process managing the login. If <code>sshd</code>, for instance, is started in a PAG, every user who logs in via ssh will be put in the same PAG and will share tokens if this option is used. </dd>
<p> This is the default on Mac OS X, where PAGs are not supported.</p>
<dt>notokens</dt>
<dd>If this option is set, the AFS session PAM module will only create a PAG and not attempt to obtain tokens. Setting this option overrides all other settings related to acquiring tokens, including always_aklog. If both nopag and notokens are set, the module essentially does nothing. </dd>
<p> Setting notokens also implies retain_after_close, meaning that the AFS session PAM module will also not attempt to delete tokens when the user&#8217;s session ends.</p>
<dt>program=<i>path</i></dt>
<dd>The path to the <code>aklog</code> program to run. Setting this option tells the AFS session PAM module to always run an external program to obtain tokens and never use the libkafs interface, even if the latter is available. </dd>
<p> You may pass options to this program by separating them with commas (or spaces or tabs in <i>krb5.conf</i> or if the configuration syntax of your PAM configuration allows this). For example, the setting: </p>
<pre> program=/usr/bin/aklog,-noprdb,-524</pre>
<p>will run <tt>&quot;/usr/bin/aklog -noprdb -524&quot;</tt> as the program to obtain tokens. The arguments are passed directly, not parsed by the shell. </p>
<p> If this option is not set, the default behavior is to call the libkafs function to obtain tokens, if available, and otherwise to use a default path to <code>aklog</code> determined at compile time (the first <code>aklog</code> found on the compiler&#8217;s path by default). If no <code>aklog</code> could be found at compile time and libkafs isn&#8217;t used, this option must be set.</p>
<dt>retain_after_close</dt>
<dd>If this option is set, pam_close_session will do nothing (successfully) rather than deleting tokens. This will allow programs started in the user&#8217;s PAG that are still running when the log out to continue to use the user&#8217;s tokens until they expire. Normally, the AFS kernel module will automatically clean up tokens once every process in that PAG has terminated.</dd></dl>
<h2>Environment</h2>
<dl>
<dt>KRB5CCNAME</dt>
<dd>This module looks for KRB5CCNAME in the PAM environment and by default does not run <code>aklog</code> if it is not set.</dd></dl>
<p> The entire PAM environment is passed to <code>aklog</code> as its environment (rather than the environment of the process running the PAM functions).</p>
<h2>Warnings</h2>
<p>As mentioned above, this module implements a dummy pam_authenticate function so that it can provide a pam_setcred function. Never list this module as <tt>&quot;sufficient&quot;</tt> or as the only <tt>&quot;required&quot;</tt> module or you may allow users to log on without a password. </p>
<p> While spawning an external <code>aklog</code> program, the AFS session PAM module resets the SIGCHLD signal handler to the default handler while the program runs and then restores it afterward. This is done to avoid having aklog interfere with process handling in the calling application, but it means that there&#8217;s a race condition that can cause children to be incorrectly handled if they exit while aklog is running. There is unfortunately no good solution to this other than building against Heimdal and using the libkafs interface to obtain tokens instead of an external program. </p>
<p> To detect whether AFS is running on the system, the AFS session PAM module temporarily sets a SIGSYS handler before attempting an AFS system call. That handler may also modify a static variable. Neither of these should ideally be done in a PAM module, but there is no other good way of checking for the non-existence of a system call that doesn&#8217;t crash the application on some operating systems. The PAM module will attempt to restore the previous SIGSYS handler, if any, after the test is done, and the static variable is used in such a way that running it from multiple threads shouldn&#8217;t be an issue, but be aware that the PAM module is doing this behind the back of the application and may interfere with unusual SIGSYS handlers or similar application actions.</p>
<h2>Notes</h2>
<p>When using the libkafs interface to obtain tokens, be sure that it is configured properly for the type of AFS tokens expected at your site. As of Heimdal 0.7, the default behavior is to contact the krb524 service to translate Kerberos v5 tickets into Kerberos v4 tickets to use as tokens. AFS cells running current server software no longer need this, and if your site doesn&#8217;t run the krb524 service, this may break token acquisition. Sites running AFS servers that understand Kerberos-v5-derived tokens should add configuration like: </p>
<pre><code>libkafs = {
    EXAMPLE.ORG = {
        afs-use-524 = no
    }
}</code></pre>
<p> to the [appdefaults] section of their <i>krb5.conf</i> files to disable use of the krb524 service. See the Heimdal <i><a href="/docs/linux/man/3-kafs/">kafs</a></i>(3) man page for more information.</p>
<h2>See Also</h2>
<p><i>aklog</i>(1), <i><a href="/docs/linux/man/3-kafs/">kafs</a></i>(3), <i><a href="/docs/linux/man/7-pam/">pam</a></i>(7), <i><a href="/docs/linux/man/3-syslog/">syslog</a></i>(3), <i>unlog</i>(1) </p>
