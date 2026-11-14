---
title: "pam_cap(8)"
name: "pam_cap"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_cap/"
description: "pam_cap – PAM module to set inheritable capabilities"
---

<p>pam_cap &#8211; PAM module to set inheritable capabilities</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_cap.so</code> [config=<i>/path/to/capability.conf</i>] [debug]</dl>
<h2>Description</h2>
<dd>The pam_cap PAM module sets the current process&#8217; inheritable capabilities. Capabilities are read from the /etc/security/capability.conf config file, or alternate file specified with the config= option. The module must not be called by a multithreaded application. </p>
<h2>Options</h2>
<p><code>config=</code><i>/path/to/capability.conf</i></p>
<dl>
<dd>Indicate an alternative capability.conf style configuration file to override the default.</dl>
<p> <code>debug</code></p>
<dl>
<dd>Print debug information.</dl>
<h2>Module Types Provided</h2>
<p>Only the <code>authentication</code> module type is provided.</p>
<h2>Return Values</h2>
<p>PAM_AUTH_ERR</p>
<dl>
<dd>The user is not known to the system.</dl>
<p> PAM_IGNORE</p>
<dl>
<dd>No capabilities found for this user.</dl>
<p> PAM_INCOMPLETE</p>
<dl>
<dd>Indicates a PAM-Conversation failure.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>Capabilities were set.</dl>
<h2>Files</h2>
<p>/etc/security/capability.conf</p>
<dl>
<dd>Default configuration file</dl>
<h2>Examples</h2>
<p>Nearly all applications/daemons which use PAM for authentication contain a configuration line: <i>@include common-auth</i>. Thus, to set inheritable capabilities in <code>all</code> of these applications, add the following as the last line to /etc/pam.d/common-auth</p>
<dl>
<dd>auth optional pam_cap.so</dl>
<p> To set inheritable capabilities for a user in a <code>specific</code> application, or in application(s) which do not @include common-auth, add the line below to the application-specific file; e.g. /etc/pam.d/myapp</p>
<dl>
<dd>auth optional pam_cap.so</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-capability-conf/">capability.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7).</p>
<h2>Authors</h2>
<p>pam_cap was initially written by Andrew G. Morgan &lt;morgan [at] kernel.org&gt;</p>
