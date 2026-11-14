---
title: "k5login(5)"
name: "k5login"
section: "5"
letter: "k"
url: "/docs/linux/man/5-k5login/"
description: "k5login – Kerberos V5 acl file for host access"
---

<p>k5login &#8211; Kerberos V5 acl file for host access</p>
<h2>Description</h2>
<p>The .k5login file, which resides in a user&#8217;s home directory, contains a list of the Kerberos principals. Anyone with valid tickets for a principal in the file is allowed host access with the UID of the user in whose home directory the file resides. One common use is to place a .k5login file in root&#8217;s home directory, thereby granting system administrators remote root access to the host via Kerberos.</p>
<h2>Examples</h2>
<p>Suppose the user <code>alice</code> had a .k5login file in her home directory containing just the following line: </p>
<pre>bob [at] FOOBAR.ORG</pre>
<p>This would allow <code>bob</code> to use Kerberos network applications, such as <a href="/docs/linux/man/1-ssh/">ssh</a>(1), to access <code>alice</code>&#8216;s account, using <code>bob</code>&#8216;s Kerberos tickets. In a default configuration (with <code>k5login_authoritative</code> set to true in <i><a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a>(5)</i>), this .k5login file would not let <code>alice</code> use those network applications to access her account, since she is not listed! With no .k5login file, or with <code>k5login_authoritative</code> set to false, a default rule would permit the principal <code>alice</code> in the machine&#8217;s default realm to access the <code>alice</code> account. </p>
<p> Let us further suppose that <code>alice</code> is a system administrator. Alice and the other system administrators would have their principals in root&#8217;s .k5login file on each host: </p>
<pre>alice [at] BLEEP.COM
joeadmin/root [at] BLEEP.COM</pre>
<p>This would allow either system administrator to log in to these hosts using their Kerberos tickets instead of having to type the root password. Note that because <code>bob</code> retains the Kerberos tickets for his own principal, <code>bob [at] FOOBAR.ORG</code>, he would not have any of the privileges that require <code>alice</code>&#8216;s tickets, such as root access to any of the site&#8217;s hosts, or the ability to change <code>alice</code>&#8216;s password.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-kerberos/">kerberos</a>(1)</p>
<h2>Author</h2>
<p>MIT</p>
<h2>Copyright</h2>
<p>1985-2017, MIT</p>
