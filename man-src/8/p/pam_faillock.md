---
title: "pam_faillock(8)"
name: "pam_faillock"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_faillock/"
description: "pam_faillock – Module counting authentication failures during a specified interval"
---

<p>pam_faillock &#8211; Module counting authentication failures during a specified interval</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>auth &#8230; pam_faillock.so</code> {preauth|authfail|authsucc} [conf=<i>/path/to/config-file</i>] [dir=<i>/path/to/tally-directory</i>] [even_deny_root] [deny=<i>n</i>] [fail_interval=<i>n</i>] [unlock_time=<i>n</i>] [root_unlock_time=<i>n</i>] [admin_group=<i>name</i>] [audit] [silent] [no_log_info]</p>
<dt> <code>account &#8230; pam_faillock.so</code> [dir=<i>/path/to/tally-directory</i>] [no_log_info]</dl>
<h2>Description</h2>
<dd>This module maintains a list of failed authentication attempts per user during a specified interval and locks the account in case there were more than <i>deny</i> consecutive failed authentications. </p>
<p> Normally, failed attempts to authenticate <i>root</i> will <code>not</code> cause the root account to become blocked, to prevent denial-of-service: if your users aren&#8217;t given shell accounts and root may only login via <code>su</code> or at the machine console (not telnet/rsh, etc), this is safe.</p>
<h2>Options</h2>
<p><code>{preauth|authfail|authsucc}</code></p>
<dl>
<dd>This argument must be set accordingly to the position of this module instance in the PAM stack. </p>
<p> The <i>preauth</i> argument must be used when the module is called before the modules which ask for the user credentials such as the password. The module just examines whether the user should be blocked from accessing the service in case there were anomalous number of failed consecutive authentication attempts recently. This call is optional if <i>authsucc</i> is used. </p>
<p> The <i>authfail</i> argument must be used when the module is called after the modules which determine the authentication outcome, failed. Unless the user is already blocked due to previous authentication failures, the module will record the failure into the appropriate user tally file. </p>
<p> The <i>authsucc</i> argument must be used when the module is called after the modules which determine the authentication outcome, succeeded. Unless the user is already blocked due to previous authentication failures, the module will then clear the record of the failures in the respective user tally file. Otherwise it will return authentication error. If this call is not done, the pam_faillock will not distinguish between consecutive and non-consecutive failed authentication attempts. The <i>preauth</i> call must be used in such case. Due to complications in the way the PAM stack can be configured it is also possible to call <i>pam_faillock</i> as an account module. In such configuration the module must be also called in the <i>preauth</i> stage.</dl>
<p> <code>conf=/path/to/config-file</code></p>
<dl>
<dd>Use another configuration file instead of the default /etc/security/faillock.conf.</dl>
<p> The options for configuring the module behavior are described in the <code><a href="/docs/linux/man/5-faillock-conf/">faillock.conf</a></code>(5) manual page. The options specified on the module command line override the values from the configuration file.</p>
<h2>Module Types Provided</h2>
<p>The <code>auth</code> and <code>account</code> module types are provided.</p>
<h2>Return Values</h2>
<p>PAM_AUTH_ERR</p>
<dl>
<dd>An invalid option was given, the module was not able to retrieve the user name, no valid counter file was found, or too many failed logins.</dl>
<p> PAM_BUF_ERR</p>
<dl>
<dd>Memory buffer error.</dl>
<p> PAM_CONV_ERR</p>
<dl>
<dd>The conversation method supplied by the application failed to obtain the username.</dl>
<p> PAM_INCOMPLETE</p>
<dl>
<dd>The conversation method supplied by the application returned PAM_CONV_AGAIN.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>Everything was successful.</dl>
<p> PAM_IGNORE</p>
<dl>
<dd>User not present in passwd database.</dl>
<h2>Notes</h2>
<p>Configuring options on the module command line is not recommend. The /etc/security/faillock.conf should be used instead. </p>
<p> The setup of <i>pam_faillock</i> in the PAM stack is different from the <i>pam_tally2</i> module setup. </p>
<p> Individual files with the failure records are created as owned by the user. This allows <code>pam_faillock.so</code> module to work correctly when it is called from a screensaver. </p>
<p> Note that using the module in <code>preauth</code> without the <code>silent</code> option specified in /etc/security/faillock.conf or with <i>requisite</i> control field leaks an information about existence or non-existence of an user account in the system because the failures are not recorded for the unknown users. The message about the user account being locked is never displayed for non-existing user accounts allowing the adversary to infer that a particular account is not existing on a system.</p>
<h2>Examples</h2>
<p>Here are two possible configuration examples for /etc/pam.d/login. They make <i>pam_faillock</i> to lock the account after 4 consecutive failed logins during the default interval of 15 minutes. Root account will be locked as well. The accounts will be automatically unlocked after 20 minutes. </p>
<p> In the first example the module is called only in the <i>auth</i> phase and the module does not print any information about the account being blocked by <i>pam_faillock</i>. The <i>preauth</i> call can be added to tell users that their logins are blocked by the module and also to abort the authentication without even asking for password in such case. </p>
<p> /etc/security/faillock.conf file example: </p>
<dl>
<dd>
<pre>deny=4
unlock_time=1200
silent</pre>
</dl>
<p> /etc/pam.d/config file example: </p>
<dl>
<dd>
<pre>auth required pam_securetty.so
auth required pam_env.so
auth required pam_nologin.so
# optionally call: auth requisite pam_faillock.so preauth
# to display the message about account being locked
auth [success=1 default=bad] pam_unix.so
auth [default=die] pam_faillock.so authfail
auth sufficient pam_faillock.so authsucc
auth required pam_deny.so
account required pam_unix.so
password required pam_unix.so shadow
session required pam_selinux.so close
session required pam_loginuid.so
session required pam_unix.so
session required pam_selinux.so open</pre>
</dl>
<p> In the second example the module is called both in the <i>auth</i> and <i>account</i> phases and the module informs the authenticating user when the account is locked if <code>silent</code> option is not specified in the faillock.conf. </p>
<dl>
<dd>
<pre>auth required pam_securetty.so
auth required pam_env.so
auth required pam_nologin.so
auth required pam_faillock.so preauth
# optionally use requisite above if you do not want to prompt for the password
# on locked accounts
auth sufficient pam_unix.so
auth [default=die] pam_faillock.so authfail
auth required pam_deny.so
account required pam_faillock.so
# if you drop the above call to pam_faillock.so the lock will be done also
# on non-consecutive authentication failures
account required pam_unix.so
password required pam_unix.so shadow
session required pam_selinux.so close
session required pam_loginuid.so
session required pam_unix.so
session required pam_selinux.so open</pre>
</dl>
<h2>Files</h2>
<p>/var/run/faillock/*</p>
<dl>
<dd>the files logging the authentication failures for users</dl>
<p> /etc/security/faillock.conf</p>
<dl>
<dd>the config file for pam_faillock options</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-faillock/">faillock</a></code>(8), <code><a href="/docs/linux/man/5-faillock-conf/">faillock.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8)</p>
<h2>Author</h2>
<p>pam_faillock was written by Tomas Mraz.</p>
