---
title: "pam_tally2(8)"
name: "pam_tally2"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_tally2/"
description: "pam_tally2 – The login counter (tallying) module"
---

<p>pam_tally2 &#8211; The login counter (tallying) module</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_tally2.so</code> [file=<i>/path/to/counter</i>] [onerr=[<i>fail</i>|<i>succeed</i>]] [magic_root] [even_deny_root] [deny=<i>n</i>] [lock_time=<i>n</i>] [unlock_time=<i>n</i>] [root_unlock_time=<i>n</i>] [serialize] [audit] [silent] [no_log_info] [debug]</p>
<dt> <code>pam_tally2</code> [&#8211;file&nbsp;<i>/path/to/counter</i>] [&#8211;user&nbsp;<i>username</i>] [&#8211;reset[=<i>n</i>]] [&#8211;quiet]</dl>
<h2>Description</h2>
<dd>This module maintains a count of attempted accesses, can reset count on success, can deny access if too many attempts fail. </p>
<p> pam_tally2 comes in two parts: <code>pam_tally2.so</code> and <code>pam_tally2</code>. The former is the PAM module and the latter, a stand-alone program. <code>pam_tally2</code> is an (optional) application which can be used to interrogate and manipulate the counter file. It can display user counts, set individual counts, or clear all counts. Setting artificially high counts may be useful for blocking users without changing their passwords. For example, one might find it useful to clear all counts every midnight from a cron job. </p>
<p> Normally, failed attempts to access <i>root</i> will <code>not</code> cause the root account to become blocked, to prevent denial-of-service: if your users aren&#8217;t given shell accounts and root may only login via <code>su</code> or at the machine console (not telnet/rsh, etc), this is safe.</p>
<h2>Options</h2>
<p>GLOBAL OPTIONS</p>
<dl>
<dd>This can be used for <i>auth</i> and <i>account</i> module types. </p>
<p> <code>onerr=[</code><i>fail</i><code>|</code><i>succeed</i><code>]</code></p>
<dl>
<dd>If something weird happens (like unable to open the file), return with <code>PAM_SUCCESS</code> if <code>onerr=</code><i>succeed</i> is given, else with the corresponding PAM error code.</dl>
<p> <code>file=</code><i>/path/to/counter</i></p>
<dl>
<dd>File where to keep counts. Default is /var/log/tallylog.</dl>
<p> <code>audit</code></p>
<dl>
<dd>Will log the user name into the system log if the user is not found.</dl>
<p> <code>silent</code></p>
<dl>
<dd>Don&#8217;t print informative messages.</dl>
<p> <code>no_log_info</code></p>
<dl>
<dd>Don&#8217;t log informative messages via <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3).</dl>
<p> <code>debug</code></p>
<dl>
<dd>Always log tally count when it is incremented as a debug level message to the system log.</dl>
</dl>
<p> AUTH OPTIONS</p>
<dl>
<dd>Authentication phase first increments attempted login counter and checks if user should be denied access. If the user is authenticated and the login process continues on call to <code><a href="/docs/linux/man/3-pam_setcred/">pam_setcred</a></code>(3) it resets the attempts counter. </p>
<p> <code>deny=</code><i>n</i></p>
<dl>
<dd>Deny access if tally for this user exceeds <i>n</i>.</dl>
<p> <code>lock_time=</code><i>n</i></p>
<dl>
<dd>Always deny for <i>n</i> seconds after failed attempt.</dl>
<p> <code>unlock_time=</code><i>n</i></p>
<dl>
<dd>Allow access after <i>n</i> seconds after failed attempt. If this option is used the user will be locked out for the specified amount of time after he exceeded his maximum allowed attempts. Otherwise the account is locked until the lock is removed by a manual intervention of the system administrator.</dl>
<p> <code>magic_root</code></p>
<dl>
<dd>If the module is invoked by a user with uid=0 the counter is not incremented. The sysadmin should use this for user launched services, like <code>su</code>, otherwise this argument should be omitted.</dl>
<p> <code>even_deny_root</code></p>
<dl>
<dd>Root account can become unavailable.</dl>
<p> <code>root_unlock_time=</code><i>n</i></p>
<dl>
<dd>This option implies <code>even_deny_root</code> option. Allow access after <i>n</i> seconds to root account after failed attempt. If this option is used the root user will be locked out for the specified amount of time after he exceeded his maximum allowed attempts.</dl>
<p> <code>serialize</code></p>
<dl>
<dd>Serialize access to the tally file using locks. This option might be used only for non-multithreaded services because it depends on the fcntl locking of the tally file. Also it is a good idea to use this option only in such configurations where the time between auth phase and account or setcred phase is not dependent on the authenticating client. Otherwise the authenticating client will be able to prevent simultaneous authentications by the same user by simply artificially prolonging the time the file record lock is held.</dl>
</dl>
<p> ACCOUNT OPTIONS</p>
<dl>
<dd>Account phase resets attempts counter if the user is <code>not</code> magic root. This phase can be used optionally for services which don&#8217;t call <code><a href="/docs/linux/man/3-pam_setcred/">pam_setcred</a></code>(3) correctly or if the reset should be done regardless of the failure of the account phase of other modules. </p>
<p> <code>magic_root</code></p>
<dl>
<dd>If the module is invoked by a user with uid=0 the counter is not changed. The sysadmin should use this for user launched services, like <code>su</code>, otherwise this argument should be omitted.</dl>
</dl>
<h2>Module Types Provided</h2>
<p>The <code>auth</code> and <code>account</code> module types are provided.</p>
<h2>Return Values</h2>
<p>PAM_AUTH_ERR</p>
<dl>
<dd>A invalid option was given, the module was not able to retrieve the user name, no valid counter file was found, or too many failed logins.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>Everything was successful.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>User not known.</dl>
<h2>Notes</h2>
<p>pam_tally2 is not compatible with the old pam_tally faillog file format. This is caused by requirement of compatibility of the tallylog file format between 32bit and 64bit architectures on multiarch systems. </p>
<p> There is no setuid wrapper for access to the data file such as when the <code>pam_tally2.so</code> module is called from xscreensaver. As this would make it impossible to share PAM configuration with such services the following workaround is used: If the data file cannot be opened because of insufficient permissions (<code>EACCES</code>) the module returns <code>PAM_IGNORE</code>.</p>
<h2>Examples</h2>
<p>Add the following line to /etc/pam.d/login to lock the account after 4 failed logins. Root account will be locked as well. The accounts will be automatically unlocked after 20 minutes. The module does not have to be called in the account phase because the <code>login</code> calls <code><a href="/docs/linux/man/3-pam_setcred/">pam_setcred</a></code>(3) correctly. </p>
<dl>
<dd>
<pre>auth required pam_securetty.so
auth required pam_tally2.so deny=4 even_deny_root unlock_time=1200
auth required pam_env.so
auth required pam_unix.so
auth required pam_nologin.so
account required pam_unix.so
password required pam_unix.so
session required pam_limits.so
session required pam_unix.so
session required pam_lastlog.so nowtmp
session optional pam_mail.so standard</pre>
</dl>
<h2>Files</h2>
<p>/var/log/tallylog</p>
<dl>
<dd>failure count logging file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>pam_tally2 was written by Tim Baverstock and Tomas Mraz.</p>
