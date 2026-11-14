---
title: "pam_tally(8)"
name: "pam_tally"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_tally/"
description: "pam_tally – The login counter (tallying) module"
---

<p>pam_tally &#8211; The login counter (tallying) module</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_tally.so</code> [file=<i>/path/to/counter</i>] [onerr=[<i>fail</i>|<i>succeed</i>]] [magic_root] [even_deny_root_account] [deny=<i>n</i>] [lock_time=<i>n</i>] [unlock_time=<i>n</i>] [per_user] [no_lock_time] [no_reset] [audit] [silent] [no_log_info]</p>
<dt> <code>pam_tally</code> [&#8211;file&nbsp;<i>/path/to/counter</i>] [&#8211;user&nbsp;<i>username</i>] [&#8211;reset[=<i>n</i>]] [&#8211;quiet]</dl>
<h2>Description</h2>
<dd>This module maintains a count of attempted accesses, can reset count on success, can deny access if too many attempts fail. </p>
<p> pam_tally has several limitations, which are solved with pam_tally2. For this reason pam_tally is deprecated and will be removed in a future release. </p>
<p> pam_tally comes in two parts: <code>pam_tally.so</code> and <code>pam_tally</code>. The former is the PAM module and the latter, a stand-alone program. <code>pam_tally</code> is an (optional) application which can be used to interrogate and manipulate the counter file. It can display user counts, set individual counts, or clear all counts. Setting artificially high counts may be useful for blocking users without changing their passwords. For example, one might find it useful to clear all counts every midnight from a cron job. The <code><a href="/docs/linux/man/8-faillog/">faillog</a></code>(8) command can be used instead of pam_tally to to maintain the counter file. </p>
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
<dd>File where to keep counts. Default is /var/log/faillog.</dl>
<p> <code>audit</code></p>
<dl>
<dd>Will log the user name into the system log if the user is not found.</dl>
<p> <code>silent</code></p>
<dl>
<dd>Don&#8217;t print informative messages.</dl>
<p> <code>no_log_info</code></p>
<dl>
<dd>Don&#8217;t log informative messages via <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3).</dl>
</dl>
<p> AUTH OPTIONS</p>
<dl>
<dd>Authentication phase first checks if user should be denied access and if not it increments attempted login counter. Then on call to <code><a href="/docs/linux/man/3-pam_setcred/">pam_setcred</a></code>(3) it resets the attempts counter. </p>
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
<p> <code>no_lock_time</code></p>
<dl>
<dd>Do not use the .fail_locktime field in /var/log/faillog for this user.</dl>
<p> <code>no_reset</code></p>
<dl>
<dd>Don&#8217;t reset count on successful entry, only decrement.</dl>
<p> <code>even_deny_root_account</code></p>
<dl>
<dd>Root account can become unavailable.</dl>
<p> <code>per_user</code></p>
<dl>
<dd>If /var/log/faillog contains a non-zero .fail_max/.fail_locktime field for this user then use it instead of <code>deny=</code><i>n</i>/ <code>lock_time=</code><i>n</i> parameter.</dl>
<p> <code>no_lock_time</code></p>
<dl>
<dd>Don&#8217;t use .fail_locktime filed in /var/log/faillog for this user.</dl>
</dl>
<p> ACCOUNT OPTIONS</p>
<dl>
<dd>Account phase resets attempts counter if the user is <code>not</code> magic root. This phase can be used optionally for services which don&#8217;t call <code><a href="/docs/linux/man/3-pam_setcred/">pam_setcred</a></code>(3) correctly or if the reset should be done regardless of the failure of the account phase of other modules. </p>
<p> <code>magic_root</code></p>
<dl>
<dd>If the module is invoked by a user with uid=0 the counter is not incremented. The sysadmin should use this for user launched services, like <code>su</code>, otherwise this argument should be omitted.</dl>
<p> <code>no_reset</code></p>
<dl>
<dd>Don&#8217;t reset count on successful entry, only decrement.</dl>
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
<h2>Examples</h2>
<p>Add the following line to /etc/pam.d/login to lock the account after too many failed logins. The number of allowed fails is specified by /var/log/faillog and needs to be set with pam_tally or <code><a href="/docs/linux/man/8-faillog/">faillog</a></code>(8) before. </p>
<dl>
<dd>
<pre>auth required pam_securetty.so
auth required pam_tally.so per_user
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
<p>/var/log/faillog</p>
<dl>
<dd>failure logging file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-faillog/">faillog</a></code>(8), <code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>pam_tally was written by Tim Baverstock and Tomas Mraz.</p>
