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
<p>The <font SIZE="-1">AFS</font> session service module for <font SIZE="-1">PAM</font>, typically installed at <i>/lib/security/pam_afs_session.so</i>, establishes new <font SIZE="-1">AFS</font> sessions and obtains <font SIZE="-1">AFS</font> tokens when a new session is opened for a user. It is a shared object that is dynamically loaded by the <font SIZE="-1">PAM</font> subsystem as necessary, based on the system <font SIZE="-1">PAM</font> configuration. <font SIZE="-1">PAM</font> is a system for plugging in external authentication and session management modules so that each application doesn&#8217;t have to know the best way to check user authentication or create a user session on that system. For details on how to configure <font SIZE="-1">PAM</font> on your system, see the <font SIZE="-1">PAM</font> man page, often <i><a href="/docs/linux/man/7-pam/">pam</a></i>(7). </p>
<p> This module provides pam_setcred, pam_open_session, and pam_close_session implementations for <font SIZE="-1">AFS</font>. Because pam_setcred is part of the auth <font SIZE="-1">PAM</font> group, it also implements a dummy pam_authenticate that always succeeds (otherwise, it can&#8217;t provide a pam_setcred). </p>
<p> Make sure that this module is <font SIZE="-1">NEVER</font> listed as <tt>&quot;sufficient&quot;</tt> or as the only <tt>&quot;required&quot;</tt> module in the auth group. Doing so will potentially allow users to log on without any password. There unfortunately isn&#8217;t a way to work around this and still provide pam_setcred without running afoul of a bug in (at least) Linux <font SIZE="-1">PAM</font> 0.99.7.1 and probably earlier that causes authentication to fail when the final module in the auth group returns <font SIZE="-1">PAM_IGNORE</font> and <tt>&quot;[default=done]&quot;</tt> was given as the action. </p>
<p> Here are the actions of this module:</p>
<dl>
<dt>pam_open_session</p>
<dd>When a new session is opened, this module will first check to see if <font SIZE="-1">AFS</font> is running on the system. If not, it will log a message and exit successfully. If <font SIZE="-1">AFS</font> is running, it will place the user&#8217;s session in a new <font SIZE="-1">PAG</font> (Process Authentication Group, often implemented as supplemental groups, which limits user tokens to only processes in that <font SIZE="-1">PAG</font>). It will then attempt to obtain tokens, either directly if built with the Heimdal libkafs library and Kerberos support or by running an external <code>aklog</code> program. If <font SIZE="-1">PAG</font> creation fails, the module will fail; if obtaining tokens fails, the module will log a warning but still return success. </p>
<p> The module will only attempt to obtain tokens if the environment variable <font SIZE="-1">KRB5CCNAME</font> is set in the environment, unless otherwise configured (see the always_aklog option). It will always create a new <font SIZE="-1">PAG</font>, however.</p>
<dt>pam_close_session</p>
<dd>If and only if pam_open_session successfully obtained <font SIZE="-1">AFS</font> tokens and <font SIZE="-1">AFS</font> is still running on the system, pam_close_session will delete the tokens in the current <font SIZE="-1">PAG</font> (equivalent to running <code>unlog</code>). To leave the tokens after session close, set the retain_after_close option.</p>
<dt>pam_setcred</p>
<dd>When pam_setcred is called with the <font SIZE="-1">PAM_ESTABLISH_CRED</font> flag, it will do the same as if pam_open_session was called. When pam_setcred is called with the <font SIZE="-1">PAM_DELETE_CRED</font> flag, it will do the same as if pam_close_session was called. When called with the <font SIZE="-1">PAM_REINITIALIZE_CRED</font> flag or the <font SIZE="-1">PAM_REFRESH_CRED</font> flag, it won&#8217;t create a new <font SIZE="-1">PAG</font> but instead will only attempt to get new tokens (still skipping this unless <font SIZE="-1">KRB5CCNAME</font> is set in the environment or always_aklog is set).</dl>
<p> This module is primarily intended for use with a Kerberos v5 authentication module. It does not itself do any user authentication; it cannot, for instance, be used to authenticate users to a <code>kaserver</code>. While it is intended for use with an <code>aklog</code> that uses Kerberos v5 ticket caches to obtain tokens, it can be used with any <code>aklog</code> implementation (always_aklog may have to be set if no Kerberos v5 ticket cache will be present). </p>
<p> This module performs no authorization checks and does not hook into password changes; it only implements the session functions and pam_setcred.</p>
<h2>Configuration</h2>
<p>The <font SIZE="-1">AFS</font> session <font SIZE="-1">PAM</font> module supports the following configuration options, which may be set in the <font SIZE="-1">PAM</font> configuration as arguments listed after <tt>&quot;pam_afs_session.so&quot;</tt> or in the system <i>krb5.conf</i>. </p>
<p> Some of them take arguments, in which case the argument will be given after <tt>&quot;=&quot;</tt>. The rest are boolean options. To set a boolean option in the <font SIZE="-1">PAM</font> configuration, just give the name of the option in the arguments. To set an option that takes an argument, follow the option name with an equal sign (<tt>&quot;=&quot;</tt>) and the value, with no separating whitespace. Whitespace in option arguments is not supported in the <font SIZE="-1">PAM</font> configuration files of most <font SIZE="-1">PAM</font> implementations. </p>
<p> To set an option for the <font SIZE="-1">PAM</font> module in the system <i>krb5.conf</i> file, put that option in the [appdefaults] section. The <font SIZE="-1">AFS</font> session <font SIZE="-1">PAM</font> module will look for options either at the top level of the [appdefaults] section or in a subsection named <tt>&quot;pam-afs-session&quot;</tt> (currently, realm-specific configuration is not checked). For example, the following fragment of a <i>krb5.conf</i> file would set <i>aklog_homedir</i> to true and <i>minimum_uid</i> to 100. </p>
<pre> [appdefaults]
 aklog_homedir = true
 pam-afs-session = {
 minimum_uid = 100
 }</pre>
<p>There is no difference to the <font SIZE="-1">PAM</font> module whether options are specified at the top level or in a <tt>&quot;pam-afs-session&quot;</tt> section; the <tt>&quot;pam-afs-session&quot;</tt> section is supported in case there are options that should be set for the <font SIZE="-1">PAM</font> module but not for other applications. For more information on the syntax of <i>krb5.conf</i>, see <i><a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a></i>(5). </p>
<p> If the same option is set in <i>krb5.conf</i> and in the <font SIZE="-1">PAM</font> configuration, the latter takes precedent. Note, however, that due to the configuration syntax, there&#8217;s no way to turn off a boolean option in the <font SIZE="-1">PAM</font> configuration that was turned on in <i>krb5.conf</i>.</p>
<dl>
<dt>afs_cells=<i>cell</i>[,<i>cell</i>&#8230;]</p>
<dd>Obtain tokens for the listed cells instead of the default local cell. If more than one cell is listed, try to obtain tokens for each cell. If specified in <i>krb5.conf</i>, the cells can be separated by any combination of spaces and commas; if specified in the <font SIZE="-1">PAM</font> configuration, they must be separated by commas. </p>
<p> If the <font SIZE="-1">AFS</font> session <font SIZE="-1">PAM</font> module is running an external program, this option is implemented by passing a <code>-c</code> flag with the cell as its argument for each listed cell to that program. If aklog_homedir is also set, the <code>-c</code> flags and the <code>-p</code> flag will all be passed to the external program.</p>
<dt>aklog_homedir</p>
<dd>Try to obtain the necessary tokens to access the user&#8217;s home directory. If the libkafs token-obtaining <font SIZE="-1">API</font> is used, setting this will cause the <font SIZE="-1">AFS</font> session <font SIZE="-1">PAM</font> module to pass the user&#8217;s home directory into that <font SIZE="-1">API</font> and request that the appropriate tokens be obtained. If running an external <code>aklog</code> program, <code>aklog</code> will be called with <code>-p</code> <i>home-directory</i> where <i>home-directory</i> is the home directory of the local user for which the session is being opened or refreshed. This generally will tell <code>aklog</code> to check that path, find all <font SIZE="-1">AFS</font> cells involved in access to that path, and attempt to obtain tokens for each one. Note that this means that if the user&#8217;s home directory is not in <font SIZE="-1">AFS</font>, no tokens will be obtained. </p>
<p> In either case, the user&#8217;s home directory is obtained via <i>getpwnam()</i> based on the username <font SIZE="-1">PAM</font> says we are authenticating.</p>
<dt>always_aklog</p>
<dd>Normally, the <font SIZE="-1">AFS</font> session <font SIZE="-1">PAM</font> module only tries to obtain tokens if <font SIZE="-1">KRB5CCNAME</font> is set in the <font SIZE="-1">PAM</font> environment. If this option is set, it will always attempt to obtain tokens. This is only useful if it is configured to run an external <code>aklog</code> program. </p>
<p> This can be used if your environment doesn&#8217;t correctly set <font SIZE="-1">KRB5CCNAME</font> in the environment for some reason, or if your <code>aklog</code> doesn&#8217;t rely on a Kerberos ticket cache to obtain tokens (or can find the cache on its own via some other means).</p>
<dt>debug</p>
<dd>If this option is set, additional trace information will be logged to syslog with priority <font SIZE="-1">LOG_DEBUG</font>.</p>
<dt>ignore_root</p>
<dd>If this option is set, the <font SIZE="-1">AFS</font> session <font SIZE="-1">PAM</font> module won&#8217;t take any action (and will exit successfully) if the account for which the session is being established is named <tt>&quot;root&quot;</tt>.</p>
<dt>kdestroy</p>
<dd>If this option is set and the <font SIZE="-1">AFS</font> session <font SIZE="-1">PAM</font> module was built with Kerberos support, the user&#8217;s ticket cache will be destroyed after tokens are obtained successfully. If tokens are not obtained successfully, the ticket cache will be left intact. Please note that this is not properly a security feature, since the ticket cache will still be written to disk between the time the Kerberos <font SIZE="-1">PAM</font> module authenticates the user and the time the <font SIZE="-1">AFS</font> session <font SIZE="-1">PAM</font> module is run. It can, however, be used to reduce the window during which Kerberos ticket caches are lying about if the only use one has for ticket caches is to obtain <font SIZE="-1">AFS</font> tokens.</p>
<dt>minimum_uid=<i>uid</i></p>
<dd>If this option is set, the <font SIZE="-1">AFS</font> session <font SIZE="-1">PAM</font> module won&#8217;t take any action (and will exit successfully) if the account for which the session is being established has a <font SIZE="-1">UID</font> lower than <i>uid</i>.</p>
<dt>nopag</p>
<dd>If this option is set, no <font SIZE="-1">PAG</font> will be created. Be careful when using this option, since it means that the user will inherit a <font SIZE="-1">PAG</font> from the process managing the login. If <code>sshd</code>, for instance, is started in a <font SIZE="-1">PAG</font>, every user who logs in via ssh will be put in the same <font SIZE="-1">PAG</font> and will share tokens if this option is used. </p>
<p> This is the default on Mac <font SIZE="-1">OS</font> X, where PAGs are not supported.</p>
<dt>notokens</p>
<dd>If this option is set, the <font SIZE="-1">AFS</font> session <font SIZE="-1">PAM</font> module will only create a <font SIZE="-1">PAG</font> and not attempt to obtain tokens. Setting this option overrides all other settings related to acquiring tokens, including always_aklog. If both nopag and notokens are set, the module essentially does nothing. </p>
<p> Setting notokens also implies retain_after_close, meaning that the <font SIZE="-1">AFS</font> session <font SIZE="-1">PAM</font> module will also not attempt to delete tokens when the user&#8217;s session ends.</p>
<dt>program=<i>path</i></p>
<dd>The path to the <code>aklog</code> program to run. Setting this option tells the <font SIZE="-1">AFS</font> session <font SIZE="-1">PAM</font> module to always run an external program to obtain tokens and never use the libkafs interface, even if the latter is available. </p>
<p> You may pass options to this program by separating them with commas (or spaces or tabs in <i>krb5.conf</i> or if the configuration syntax of your <font SIZE="-1">PAM</font> configuration allows this). For example, the setting: </p>
<pre> program=/usr/bin/aklog,-noprdb,-524</pre>
<p>will run <tt>&quot;/usr/bin/aklog -noprdb -524&quot;</tt> as the program to obtain tokens. The arguments are passed directly, not parsed by the shell. </p>
<p> If this option is not set, the default behavior is to call the libkafs function to obtain tokens, if available, and otherwise to use a default path to <code>aklog</code> determined at compile time (the first <code>aklog</code> found on the compiler&#8217;s path by default). If no <code>aklog</code> could be found at compile time and libkafs isn&#8217;t used, this option must be set.</p>
<dt>retain_after_close</p>
<dd>If this option is set, pam_close_session will do nothing (successfully) rather than deleting tokens. This will allow programs started in the user&#8217;s <font SIZE="-1">PAG</font> that are still running when the log out to continue to use the user&#8217;s tokens until they expire. Normally, the <font SIZE="-1">AFS</font> kernel module will automatically clean up tokens once every process in that <font SIZE="-1">PAG</font> has terminated.</dl>
<h2>Environment</h2>
<dl>
<dt><font SIZE="-1">KRB5CCNAME</font></p>
<dd>This module looks for <font SIZE="-1">KRB5CCNAME</font> in the <font SIZE="-1">PAM</font> environment and by default does not run <code>aklog</code> if it is not set.</dl>
<p> The entire <font SIZE="-1">PAM</font> environment is passed to <code>aklog</code> as its environment (rather than the environment of the process running the <font SIZE="-1">PAM</font> functions).</p>
<h2>Warnings</h2>
<p>As mentioned above, this module implements a dummy pam_authenticate function so that it can provide a pam_setcred function. Never list this module as <tt>&quot;sufficient&quot;</tt> or as the only <tt>&quot;required&quot;</tt> module or you may allow users to log on without a password. </p>
<p> While spawning an external <code>aklog</code> program, the <font SIZE="-1">AFS</font> session <font SIZE="-1">PAM</font> module resets the <font SIZE="-1">SIGCHLD</font> signal handler to the default handler while the program runs and then restores it afterward. This is done to avoid having aklog interfere with process handling in the calling application, but it means that there&#8217;s a race condition that can cause children to be incorrectly handled if they exit while aklog is running. There is unfortunately no good solution to this other than building against Heimdal and using the libkafs interface to obtain tokens instead of an external program. </p>
<p> To detect whether <font SIZE="-1">AFS</font> is running on the system, the <font SIZE="-1">AFS</font> session <font SIZE="-1">PAM</font> module temporarily sets a <font SIZE="-1">SIGSYS</font> handler before attempting an <font SIZE="-1">AFS</font> system call. That handler may also modify a static variable. Neither of these should ideally be done in a <font SIZE="-1">PAM</font> module, but there is no other good way of checking for the non-existence of a system call that doesn&#8217;t crash the application on some operating systems. The <font SIZE="-1">PAM</font> module will attempt to restore the previous <font SIZE="-1">SIGSYS</font> handler, if any, after the test is done, and the static variable is used in such a way that running it from multiple threads shouldn&#8217;t be an issue, but be aware that the <font SIZE="-1">PAM</font> module is doing this behind the back of the application and may interfere with unusual <font SIZE="-1">SIGSYS</font> handlers or similar application actions.</p>
<h2>Notes</h2>
<p>When using the libkafs interface to obtain tokens, be sure that it is configured properly for the type of <font SIZE="-1">AFS</font> tokens expected at your site. As of Heimdal 0.7, the default behavior is to contact the krb524 service to translate Kerberos v5 tickets into Kerberos v4 tickets to use as tokens. <font SIZE="-1">AFS</font> cells running current server software no longer need this, and if your site doesn&#8217;t run the krb524 service, this may break token acquisition. Sites running <font SIZE="-1">AFS</font> servers that understand Kerberos-v5-derived tokens should add configuration like: </p>
<pre><code>libkafs = {
    EXAMPLE.ORG = {
        afs-use-524 = no
    }
}</code></pre>
<p> to the [appdefaults] section of their <i>krb5.conf</i> files to disable use of the krb524 service. See the Heimdal <i><a href="/docs/linux/man/3-kafs/">kafs</a></i>(3) man page for more information.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-aklog/">aklog</a></i>(1), <i><a href="/docs/linux/man/3-kafs/">kafs</a></i>(3), <i><a href="/docs/linux/man/7-pam/">pam</a></i>(7), <i><a href="/docs/linux/man/3-syslog/">syslog</a></i>(3), <i><a href="/docs/linux/man/1-unlog/">unlog</a></i>(1) </p>
