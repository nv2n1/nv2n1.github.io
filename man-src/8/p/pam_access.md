---
title: "pam_access(8)"
name: "pam_access"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_access/"
description: "pam_access – PAM module for logdaemon style login access control"
---

<p>pam_access &#8211; PAM module for logdaemon style login access control</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_access.so</code> [debug] [nodefgroup] [noaudit] [accessfile=<i>file</i>] [fieldsep=<i>sep</i>] [listsep=<i>sep</i>]</dl>
<h2>Description</h2>
<dd>The pam_access PAM module is mainly for access management. It provides logdaemon style login access control based on login names, host or domain names, internet addresses or network numbers, or on terminal line names, X <i>$DISPLAY</i> values, or PAM service names in case of non-networked logins. </p>
<p> By default rules for access management are taken from config file /etc/security/access.conf if you don&#8217;t specify another file. Then individual *.conf files from the /etc/security/access.d/ directory are read. The files are parsed one after another in the order of the system locale. The effect of the individual files is the same as if all the files were concatenated together in the order of parsing. This means that once a pattern is matched in some file no further files are parsed. If a config file is explicitly specified with the <code>accessfile</code> option the files in the above directory are not parsed. </p>
<p> If Linux PAM is compiled with audit support the module will report when it denies access based on origin (host, tty, etc.).</p>
<h2>Options</h2>
<p><code>accessfile=</code><i>/path/to/access.conf</i></p>
<dl>
<dd>Indicate an alternative access.conf style configuration file to override the default. This can be useful when different services need different access lists.</dl>
<p> <code>debug</code></p>
<dl>
<dd>A lot of debug information is printed with <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3).</dl>
<p> <code>noaudit</code></p>
<dl>
<dd>Do not report logins from disallowed hosts and ttys to the audit subsystem.</dl>
<p> <code>fieldsep=</code><i>separators</i></p>
<dl>
<dd>This option modifies the field separator character that pam_access will recognize when parsing the access configuration file. For example: <code>fieldsep=|</code> will cause the default `:&#8217; character to be treated as part of a field value and `|&#8217; becomes the field separator. Doing this may be useful in conjunction with a system that wants to use pam_access with X based applications, since the <code>PAM_TTY</code> item is likely to be of the form &quot;hostname:0&quot; which includes a `:&#8217; character in its value. But you should not need this.</dl>
<p> <code>listsep=</code><i>separators</i></p>
<dl>
<dd>This option modifies the list separator character that pam_access will recognize when parsing the access configuration file. For example: <code>listsep=,</code> will cause the default ` &#8216; (space) and `	&#8217; (tab) characters to be treated as part of a list element value and `,&#8217; becomes the only list element separator. Doing this may be useful on a system with group information obtained from a Windows domain, where the default built-in groups &quot;Domain Users&quot;, &quot;Domain Admins&quot; contain a space.</dl>
<p> <code>nodefgroup</code></p>
<dl>
<dd>User tokens which are not enclosed in parentheses will not be matched against the group database. The backwards compatible default is to try the group database match even for tokens not enclosed in parentheses.</dl>
<h2>Module Types Provided</h2>
<p>All module types (<code>auth</code>, <code>account</code>, <code>password</code> and <code>session</code>) are provided.</p>
<h2>Return Values</h2>
<p>PAM_SUCCESS</p>
<dl>
<dd>Access was granted.</dl>
<p> PAM_PERM_DENIED</p>
<dl>
<dd>Access was not granted.</dl>
<p> PAM_IGNORE</p>
<dl>
<dd><code>pam_setcred</code> was called which does nothing.</dl>
<p> PAM_ABORT</p>
<dl>
<dd>Not all relevant data or options could be gotten.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>The user is not known to the system.</dl>
<h2>Files</h2>
<p>/etc/security/access.conf</p>
<dl>
<dd>Default configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-access-conf/">access.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7).</p>
<h2>Authors</h2>
<p>The logdaemon style login access control scheme was designed and implemented by Wietse Venema. The pam_access PAM module was developed by Alexei Nogin &lt;alexei [at] nogin.dnttm.ru&gt;. The IPv6 support and the network(address) / netmask feature was developed and provided by Mike Becher &lt;mike.becher [at] lrz-muenchen.de&gt;.</p>
