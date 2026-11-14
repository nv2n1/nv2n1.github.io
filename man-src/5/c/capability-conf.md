---
title: "capability-conf(5)"
name: "capability-conf"
section: "5"
letter: "c"
url: "/docs/linux/man/5-capability-conf/"
description: "capablity.conf – configuration file for the pam_cap module"
---

<p>capablity.conf &#8211; configuration file for the pam_cap module</p>
<h2>Description</h2>
<p>Each line of the file consists of two fields; the fields define: </p>
<pre><code>&lt;capability-list&gt;</code></pre>
<dl>
<dd>One or more comma-separated capabilities, specified as either the textual capability name, or numeric capability value. Text name(s) and numeric value(s) may be intermixed. The special capability name <code>all</code> may be used to enable all capabilities known to the local system. The special capability name <code>none</code> may be used to disable all current inheritable capabilities.</dl>
<dl>
<dd><code>NOTE:</code> No whitespace is pemitted between the values. The names all and none may not be combined with any other capabilities.</dl>
<pre><code>&lt;username&gt;</code></pre>
<dl>
<dd>One or more whitespace-separated usernames, or the wildcard <code>*</code>.</dl>
<dl>
<dd><code>NOTE:</code> The first matching entry is used. Thus, only a single matching username entry, and/or a single wildcard entry, may be used. A matching username entry must <i>precede</i> the wildcard entry in order to be effective.</dl>
<p> <code>IMPORTANT:</code> &lt;capability-list&gt; <i>replaces</i> the current process&#8217; inherited capabilities; i.e. there is no provision for adding/subtracting from the current set. In most environments, the inheritable set of the process performing user authentication is 0 (empty). If any capability name or numeric value is invalid/unknown to the local system, the capabilities will be rejected, and the inheritable set will <code>not</code> be modified.</p>
<h2>Examples</h2>
<p>These are some example lines which might be specified in /etc/security/capability.conf. </p>
<dl>
<dd>
<pre># Simple
cap_sys_ptrace developer
cap_net_raw user1
# Multiple capablities
cap_net_admin,cap_net_raw jrnetadmin
# Identical, but with numeric values
12,13 jrnetadmin
# Combining names and numerics
cap_sys_admin,22,25 jrsysadmin
# Next line has no effect; user1 already matched above
5,12,13 user1
# Insure any potential capailities from calling process are dropped
none luser1 luser2
# Allow anyone to manipulate capabilities
# Will NOT apply to users matched above !
cap_setpcap *</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pam_cap/">pam_cap</a></code>(8), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)</p>
<h2>Author</h2>
<p>pam_cap was initially written by Andrew G. Morgan &lt;morgan [at] kernel.org&gt;</p>
