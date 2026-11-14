---
title: "kerberos(1)"
name: "kerberos"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kerberos/"
description: "kerberos – introduction to the Kerberos system"
---

<h2>NAME</h2>
<p> kerberos &#8211; introduction to the Kerberos system</p>
<h2>DESCRIPTION</h2>
<p> The Kerberos system authenticates individual users in a network environment. After authenticating yourself to Kerberos, you can use Kerberos-enabled programs without having to present passwords. </p>
<p> If you enter your username and <i>kinit</i> responds with this message: </p>
<p> kinit(v5): Client not found in Kerberos database while getting initial credentials </p>
<p> you haven&#8217;t been registered as a Kerberos user. See your system administrator. </p>
<p> A Kerberos name usually contains three parts. The first is the <i>primary</i>, which is usually a user&#8217;s or service&#8217;s name. The second is the <i>instance</i>, which in the case of a user is usually null. Some users may have privileged instances, however, such as &#8220;root&#8221; or &#8220;admin&#8221;. In the case of a service, the instance is the fully qualified name of the machine on which it runs; i.e. there can be an <i>rlogin</i> service running on the machine ABC, which is different from the rlogin service running on the machine XYZ. The third part of a Kerberos name is the <i>realm</i>. The realm corresponds to the Kerberos service providing authentication for the principal. </p>
<p> When writing a Kerberos name, the principal name is separated from the instance (if not null) by a slash, and the realm (if not the local realm) follows, preceded by an &#8220;@&#8221; sign. The following are examples of valid Kerberos names: </p>
<pre><code>
david
        jennifer /
    admin
        joeuser[at] BLEEP.COM
            cbrown /
    root[at] FUBAR.ORG
</code></pre>
<p> When you authenticate yourself with Kerberos you get an initial Kerberos <i>ticket</i>. (A Kerberos ticket is an encrypted protocol message that provides authentication.) Kerberos uses this ticket for network utilities such as <i>rlogin</i> and <i>rcp</i>. The ticket transactions are done transparently, so you don&#8217;t have to worry about their management. </p>
<p> Note, however, that tickets expire. Privileged tickets, such as those with the instance &#8220;root&#8221;, expire in a few minutes, while tickets that carry more ordinary privileges may be good for several hours or a day, depending on the installation&#8217;s policy. If your login session extends beyond the time limit, you will have to re-authenticate yourself to Kerberos to get new tickets. Use the <i>kinit</i> command to re-authenticate yourself. </p>
<p> If you use the <i>kinit</i> command to get your tickets, make sure you use the <i>kdestroy</i> command to destroy your tickets before you end your login session. You should put the <i>kdestroy</i> command in your <i>.logout</i> file so that your tickets will be destroyed automatically when you logout. For more information about the <i>kinit</i> and <i>kdestroy</i> commands, see the <i><a href="/docs/linux/man/1-kinit/">kinit</a></i>(1) and <i><a href="/docs/linux/man/1-kdestroy/">kdestroy</a></i>(1) manual pages. </p>
<p> Kerberos tickets can be forwarded. In order to forward tickets, you must request <i>forwardable</i> tickets when you <i>kinit</i>. Once you have forwardable tickets, most Kerberos programs have a command line option to forward them to the remote host.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> Several environment variables affect the operation of Kerberos-enabled programs. These include:</p>
<dl>
<dt><code>KRB5CCNAME</code></p>
<dd> Specifies the location of the credential cache, in the form <i>TYPE</i>:<i>residual</i>. If no type prefix is present, the <code>FILE</code> type is assumed and <i>residual</i> is the pathname of the cache file. A collection of multiple caches may be used by specifying the <code>DIR</code> type and the pathname of a private directory (which must already exist). The default cache file is /tmp/krb5cc_<i>uid</i> where <i>uid</i> is the decimal user ID of the user.</p>
<dt><code>KRB5_KTNAME</code></p>
<dd> Specifies the location of the keytab file, in the form <i>TYPE</i>:<i>residual</i>. If no type is present, the <code>FILE</code> type is assumed and <i>residual</i> is the pathname of the keytab file. The default keytab file is /etc/krb5.keytab.</p>
<dt><code>KRB5_CONFIG</code></p>
<dd> Specifies the location of the Kerberos configuration file. The default is /etc/krb5.conf.</p>
<dt><code>KRB5_KDC_PROFILE</code></p>
<dd> Specifies the location of the KDC configuration file, which contains additional configuration directives for the Key Distribution Center daemon and associated programs. The default is /var/kerberos/krb5kdc/kdc.conf.</p>
<dt><code>KRB5RCACHETYPE</code></p>
<dd> Specifies the default type of replay cache to use for servers. Valid types include &quot;dfl&quot; for the normal file type and &quot;none&quot; for no replay cache. <code>KRB5RCACHEDIR</code> Specifies the default directory for replay caches used by servers. The default is the value of the <code>TMPDIR</code> environment variable, or /var/tmp if <code>TMPDIR</code> is not set.</p>
<dt><code>KRB5_TRACE</code></p>
<dd> Specifies a filename to write trace log output to. Trace logs can help illuminate decisions made internally by the Kerberos libraries. The default is not to write trace log output anywhere.</dl>
<p> Most environment variables are disabled for certain programs, such as login system programs and setuid programs, which are designed to be secure when run within an untrusted process environment.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-kdestroy/">kdestroy</a>(1), <a href="/docs/linux/man/1-kinit/">kinit</a>(1), <a href="/docs/linux/man/1-klist/">klist</a>(1), <a href="/docs/linux/man/1-kswitch/">kswitch</a>(1), <a href="/docs/linux/man/1-kpasswd/">kpasswd</a>(1), <a href="/docs/linux/man/1-ksu/">ksu</a>(1), <a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a>(5), <a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5), <a href="/docs/linux/man/1-kadmin/">kadmin</a>(1), <a href="/docs/linux/man/8-kadmind/">kadmind</a>(8), <a href="/docs/linux/man/8-kdb5_util/">kdb5_util</a>(8), <a href="/docs/linux/man/8-krb5kdc/">krb5kdc</a>(8)</p>
<h2>BUGS</h2>
<h2>AUTHORS</h2>
<p> Steve Miller, MIT Project Athena/Digital Equipment Corporation<br />
 Clifford Neuman, MIT Project Athena<br />
 Greg Hudson, MIT Kerberos Consortium</p>
<h2>HISTORY</h2>
<p> The MIT Kerberos 5 implementation was developed at MIT, with contributions from many outside parties. It is currently maintained by the MIT Kerberos Consortium.</p>
<h2>RESTRICTIONS</h2>
<p> Copyright 1985,1986,1989-1996,2002,2011 Massachusetts Institute of Technology </p>
<h2>Index</h2>
