---
title: "pam_rhosts(8)"
name: "pam_rhosts"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_rhosts/"
description: "pam_rhosts – The rhosts PAM module"
---

<p>pam_rhosts &#8211; The rhosts PAM module</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_rhosts.so</code></dl>
<h2>Description</h2>
<dd>This module performs the standard network authentication for services, as used by traditional implementations of <code>rlogin</code> and <code>rsh</code> etc. </p>
<p> The authentication mechanism of this module is based on the contents of two files; /etc/hosts.equiv (or and ~/.rhosts. Firstly, hosts listed in the former file are treated as equivalent to the localhost. Secondly, entries in the user&#8217;s own copy of the latter file is used to map &quot;<i>remote-host remote-user</i>&quot; pairs to that user&#8217;s account on the current host. Access is granted to the user if their host is present in /etc/hosts.equiv and their remote account is identical to their local one, or if their remote account has an entry in their personal configuration file. </p>
<p> The module authenticates a remote user (internally specified by the item <i>PAM_RUSER</i> connecting from the remote host (internally specified by the item <code>PAM_RHOST</code>). Accordingly, for applications to be compatible this authentication module they must set these items prior to calling <code>pam_authenticate()</code>. The module is not capable of independently probing the network connection for such information.</p>
<h2>Options</h2>
<p><code>debug</code></p>
<dl>
<dd>Print debug information.</dl>
<p> <code>silent</code></p>
<dl>
<dd>Don&#8217;t print informative messages.</dl>
<p> <code>superuser=</code><i>account</i></p>
<dl>
<dd>Handle <i>account</i> as root.</dl>
<h2>Module Types Provided</h2>
<p>Only the <code>auth</code> module type is provided.</p>
<h2>Return Values</h2>
<p>PAM_AUTH_ERR</p>
<dl>
<dd>The remote host, remote user name or the local user name couldn&#8217;t be determined or access was denied by .rhosts file.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>User is not known to system.</dl>
<h2>Examples</h2>
<p>To grant a remote user access by /etc/hosts.equiv or .rhosts for <code>rsh</code> add the following lines to /etc/pam.d/rsh:</p>
<dl>
<dd>
<pre>#%PAM-1.0
#
auth required pam_rhosts.so
auth required pam_nologin.so
auth required pam_env.so
auth required pam_unix.so</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-rootok/">rootok</a></code>(3), <code><a href="/docs/linux/man/5-hosts-equiv/">hosts.equiv</a></code>(5), <code><a href="/docs/linux/man/5-rhosts/">rhosts</a></code>(5), <code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>pam_rhosts was written by Thorsten Kukuk &lt;kukuk [at] thkukuk.de&gt;</p>
