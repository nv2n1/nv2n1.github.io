---
title: "krb5-auth-dialog(1)"
name: "krb5-auth-dialog"
section: "1"
letter: "k"
url: "/docs/linux/man/1-krb5-auth-dialog/"
description: "krb5-auth-dialog – Kerberos 5 credential checking"
---

<h2 class="name">NAME</h2>
<p> krb5-auth-dialog &#8211; Kerberos 5 credential checking</p>
<h2>SYNOPSIS</h2>
<p> <code>krb5-auth-dialog [&#8211;always|&#8211;auto]</code> </p>
<h2>DESCRIPTION</h2>
<p> The krb5-auth-dialog application will periodically check (every 30 seconds) if the user has Kerberos credentials, and if so, if they will expire soon (in less than 30 minutes). If it determines that this is the case, krb5-auth-dialog will attempt to obtain fresh credentials, prompting the user for whatever information is necessary. </p>
<h2>ARGUMENTS</h2>
<dl>
<dt>&#8211;always</p>
<dd> By default, krb5-auth-dialog will exit if it finds that the user has no Kerberos credentials. If this option is specified, then it will instead attempt to get credentials. </p>
<dt>&#8211;auto</p>
<dd> Overrides the &#8211;always option, restoring the default behavior. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a></code>(5) </p>
<h2>BUGS</h2>
<p> Probably, but let&#8217;s hope not. If you find any, please file them in the bug database at <a rel="nofollow" href="http://bugzilla.gnome.org/">http://bugzilla.gnome.org/</a> against the &quot;krb5-auth-dialog&quot; component. </p>
<h2>AUTHORS</h2>
<p> Christopher Aillon &lt;caillon [at] redhat.com&gt;<br />
 Jonathan Blandford &lt;jrb [at] redhat.com&gt; </p>
<h2>Index</h2>
