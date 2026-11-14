---
title: "pam_time(8)"
name: "pam_time"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_time/"
description: "pam_time – PAM module for time control access"
---

<p>pam_time &#8211; PAM module for time control access</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_time.so</code> [conffile=conf-file] [debug] [noaudit]</dl>
<h2>Description</h2>
<dd>The pam_time PAM module does not authenticate the user, but instead it restricts access to a system and or specific applications at various times of the day and on specific days or over various terminal lines. This module can be configured to deny access to (individual) users based on their name, the time of day, the day of week, the service they are applying for and their terminal from which they are making their request. </p>
<p> By default rules for time/port access are taken from config file /etc/security/time.conf. An alternative file can be specified with the <i>conffile</i> option. </p>
<p> If Linux PAM is compiled with audit support the module will report when it denies access.</p>
<h2>Options</h2>
<p><code>conffile=/path/to/time.conf</code></p>
<dl>
<dd>Indicate an alternative time.conf style configuration file to override the default.</dl>
<p> <code>debug</code></p>
<dl>
<dd>Some debug information is printed with <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3).</dl>
<p> <code>noaudit</code></p>
<dl>
<dd>Do not report logins at disallowed time to the audit subsystem.</dl>
<h2>Module Types Provided</h2>
<p>Only the <code>account</code> type is provided.</p>
<h2>Return Values</h2>
<p>PAM_SUCCESS</p>
<dl>
<dd>Access was granted.</dl>
<p> PAM_ABORT</p>
<dl>
<dd>Not all relevant data could be gotten.</dl>
<p> PAM_BUF_ERR</p>
<dl>
<dd>Memory buffer error.</dl>
<p> PAM_PERM_DENIED</p>
<dl>
<dd>Access was not granted.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>The user is not known to the system.</dl>
<h2>Files</h2>
<p>/etc/security/time.conf</p>
<dl>
<dd>Default configuration file</dl>
<h2>Examples</h2>
<dl>
<dd>
<pre>#%PAM-1.0
#
# apply pam_time accounting to login requests
#
login account required pam_time.so</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-time-conf/">time.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7).</p>
<h2>Author</h2>
<p>pam_time was written by Andrew G. Morgan &lt;morgan [at] kernel.org&gt;.</p>
