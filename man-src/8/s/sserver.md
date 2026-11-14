---
title: "sserver(8)"
name: "sserver"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sserver/"
description: "sserver – sample Kerberos version 5 server"
---

<p>sserver &#8211; sample Kerberos version 5 server</p>
<h2>Synopsis</h2>
<p><code>sserver</code> [ <code>-p</code> <i>port</i> ] [ <code>-S</code> <i>keytab</i> ] [ <i>server_port</i> ]</p>
<h2>Description</h2>
<p>sserver and <i><a href="/docs/linux/man/1-sclient/">sclient</a>(1)</i> are a simple demonstration client/server application. When sclient connects to sserver, it performs a Kerberos authentication, and then sserver returns to sclient the Kerberos principal which was used for the Kerberos authentication. It makes a good test that Kerberos has been successfully installed on a machine. </p>
<p> The service name used by sserver and sclient is sample. Hence, sserver will require that there be a keytab entry for the service <code>sample/hostname.domain.name [at] REALM.NAME</code>. This keytab is generated using the <i><a href="/docs/linux/man/1-kadmin/">kadmin</a>(1)</i> program. The keytab file is usually installed as <code>FILE:/etc/krb5.keytab</code>. </p>
<p> The <code>-S</code> option allows for a different keytab than the default. </p>
<p> sserver is normally invoked out of <a href="/docs/linux/man/8-inetd/">inetd</a>(8), using a line in <code>/etc/inetd.conf</code> that looks like this: </p>
<pre>sample stream tcp nowait root /usr/local/sbin/sserver sserver</pre>
<p>Since <code>sample</code> is normally not a port defined in <code>/etc/services</code>, you will usually have to add a line to <code>/etc/services</code> which looks like this: </p>
<pre>sample 13135/tcp</pre>
<p>When using sclient, you will first have to have an entry in the Kerberos database, by using <i><a href="/docs/linux/man/1-kadmin/">kadmin</a>(1)</i>, and then you have to get Kerberos tickets, by using <i><a href="/docs/linux/man/1-kinit/">kinit</a>(1)</i>. Also, if you are running the sclient program on a different host than the sserver it will be connecting to, be sure that both hosts have an entry in /etc/services for the sample tcp port, and that the same port number is in both files. </p>
<p> When you run sclient you should see something like this: </p>
<pre>sendauth succeeded, reply is:
reply len 32, contents:
You are nlgilman [at] JIMI.MIT.EDU</pre>
<h2>Common Error Messages</h2>
<dl>
<dt>1.</p>
<dd>kinit returns the error: </p>
<pre>kinit: Client not found in Kerberos database while getting
 initial credentials</pre>
<p>This means that you didn&#8217;t create an entry for your username in the Kerberos database.</p>
<dt>2.</p>
<dd>sclient returns the error: </p>
<pre>unknown service sample/tcp; check /etc/services</pre>
<p>This means that you don&#8217;t have an entry in /etc/services for the sample tcp port.</p>
<dt>3.</p>
<dd>sclient returns the error: </p>
<pre>connect: Connection refused</pre>
<p>This probably means you didn&#8217;t edit /etc/inetd.conf correctly, or you didn&#8217;t restart inetd after editing inetd.conf.</p>
<dt>4.</p>
<dd>sclient returns the error: </p>
<pre>sclient: Server not found in Kerberos database while using
 sendauth</pre>
<p>This means that the <code>sample/hostname [at] LOCAL.REALM</code> service was not defined in the Kerberos database; it should be created using <i><a href="/docs/linux/man/1-kadmin/">kadmin</a>(1)</i>, and a keytab file needs to be generated to make the key for that service principal available for sclient.</p>
<dt>5.</p>
<dd>sclient returns the error: </p>
<pre>sendauth rejected, error reply is:
 &quot;No such file or directory&quot;</pre>
<p>This probably means sserver couldn&#8217;t find the keytab file. It was probably not installed in the proper directory.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-sclient/">sclient</a>(1)</i>, <a href="/docs/linux/man/5-services/">services</a>(5), <a href="/docs/linux/man/8-inetd/">inetd</a>(8)</p>
<h2>Author</h2>
<p>MIT</p>
<h2>Copyright</h2>
<p>1985-2016, MIT</p>
