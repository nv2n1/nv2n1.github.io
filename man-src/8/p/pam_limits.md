---
title: "pam_limits(8)"
name: "pam_limits"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_limits/"
description: "pam_limits – PAM module to limit resources"
---

<p>pam_limits &#8211; PAM module to limit resources</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_limits.so</code> [conf=<i>/path/to/limits.conf</i>] [debug] [set_all] [utmp_early] [noaudit]</dl>
<h2>Description</h2>
<dd>The pam_limits PAM module sets limits on the system resources that can be obtained in a user-session. Users of <i>uid=0</i> are affected by this limits, too. </p>
<p> By default limits are taken from the /etc/security/limits.conf config file. Then individual *.conf files from the /etc/security/limits.d/ directory are read. The files are parsed one after another in the order of &quot;C&quot; locale. The effect of the individual files is the same as if all the files were concatenated together in the order of parsing. If a config file is explicitly specified with a module option then the files in the above directory are not parsed. </p>
<p> The module must not be called by a multithreaded application. </p>
<p> If Linux PAM is compiled with audit support the module will report when it denies access based on limit of maximum number of concurrent login sessions.</p>
<h2>Options</h2>
<p><code>conf=</code><i>/path/to/limits.conf</i></p>
<dl>
<dd>Indicate an alternative limits.conf style configuration file to override the default.</dl>
<p> <code>debug</code></p>
<dl>
<dd>Print debug information.</dl>
<p> <code>set_all</code></p>
<dl>
<dd>Set the limits for which no value is specified in the configuration file to the one from the process with the PID 1. Please note that if the init process is systemd these limits will not be the kernel default limits and this option should not be used.</dl>
<p> <code>utmp_early</code></p>
<dl>
<dd>Some broken applications actually allocate a utmp entry for the user before the user is admitted to the system. If some of the services you are configuring PAM for do this, you can selectively use this module argument to compensate for this behavior and at the same time maintain system-wide consistency with a single limits.conf file.</dl>
<p> <code>noaudit</code></p>
<dl>
<dd>Do not report exceeded maximum logins count to the audit subsystem.</dl>
<h2>Module Types Provided</h2>
<p>Only the <code>session</code> module type is provided.</p>
<h2>Return Values</h2>
<p>PAM_ABORT</p>
<dl>
<dd>Cannot get current limits.</dl>
<p> PAM_IGNORE</p>
<dl>
<dd>No limits found for this user.</dl>
<p> PAM_PERM_DENIED</p>
<dl>
<dd>New limits could not be set.</dl>
<p> PAM_SERVICE_ERR</p>
<dl>
<dd>Cannot read config file.</dl>
<p> PAM_SESSION_ERR</p>
<dl>
<dd>Error recovering account name.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>Limits were changed.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>The user is not known to the system.</dl>
<h2>Files</h2>
<p>/etc/security/limits.conf</p>
<dl>
<dd>Default configuration file</dl>
<h2>Examples</h2>
<p>For the services you need resources limits (login for example) put a the following line in /etc/pam.d/login as the last line for that service (usually after the pam_unix session line): </p>
<dl>
<dd>
<pre>#%PAM-1.0
#
# Resource limits imposed on login sessions via pam_limits
#
session required pam_limits.so</pre>
</dl>
<p> Replace &quot;login&quot; for each service you are using this module.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-limits-conf/">limits.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7).</p>
<h2>Authors</h2>
<p>pam_limits was initially written by Cristian Gafton &lt;gafton [at] redhat.com&gt;</p>
