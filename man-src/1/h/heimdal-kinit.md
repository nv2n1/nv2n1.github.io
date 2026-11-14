---
title: "heimdal-kinit(1)"
name: "heimdal-kinit"
section: "1"
letter: "h"
url: "/docs/linux/man/1-heimdal-kinit/"
description: "kinit – acquire initial tickets"
---

<h2 class="name">NAME</h2>
<p> <code>kinit</code> &#8211; acquire initial tickets </p>
<h2>SYNOPSIS</h2>
<p> <code>kinit</code> [-<code>-afslog</code> ] [-<code>c </code><i>cachename | </i> &#8211;<code>-cache= </code><i>cachename</i> ] [-<code>f | &#8211;no-forwardable</code> ] [-<code>t </code><i>keytabname | </i> &#8211;<code>-keytab= </code><i>keytabname</i> ] [-<code>l </code><i>time | </i> &#8211;<code>-lifetime= </code><i>time</i> ] [-<code>p | &#8211;proxiable</code> ] [-<code>R | &#8211;renew</code> ] [-<code>-renewable</code> ] [-<code>r </code><i>time | </i> &#8211;<code>-renewable-life= </code><i>time</i> ] [-<code>S </code><i>principal | </i> &#8211;<code>-server= </code><i>principal</i> ] [-<code>s </code><i>time | </i> &#8211;<code>-start-time= </code><i>time</i> ] [-<code>k | &#8211;use-keytab</code> ] [-<code>v | &#8211;validate</code> ] [-<code>e </code><i>enctypes | </i> &#8211;<code>-enctypes= </code><i>enctypes</i> ] [-<code>a </code><i>addresses | </i> &#8211;<code>-extra-addresses= </code><i>addresses</i> ] [-<code>-password-file= </code><i>filename</i> ] [-<code>-fcache-version= </code><i>version-number</i> ] [-<code>A | &#8211;no-addresses</code> ] [-<code>-anonymous</code> ] [-<code>-enterprise</code> ] [-<code>-version</code> ] [-<code>-help</code> ] [<i>principal </i>[<i>command</i> ] ]</p>
<h2>DESCRIPTION</h2>
<p> <code>kinit</code> is used to authenticate to the Kerberos server as <i>principal</i> or if none is given, a system generated default (typically your login name at the default realm), and acquire a ticket granting ticket that can later be used to obtain tickets for other services. </p>
<p> Supported options:</p>
<dl>
<dt><code>-c </code><i>cachename &#8211;</i><code>-cache= </code><i>cachename</i></p>
<dd> The credentials cache to put the acquired ticket in, if other than default.</p>
<dt><code>-f &#8211;forwardable</code></p>
<dd> Obtain a ticket than can be forwarded to another host.</p>
<dt><code>-F &#8211;no-forwardable</code></p>
<dd> Do not obtain a forwardable ticket.</p>
<dt><code>-t </code><i>keytabname , &#8211;</i><code>-keytab= </code><i>keytabname</i></p>
<dd> Don&#8217;t ask for a password, but instead get the key from the specified keytab.</p>
<dt><code>-l </code><i>time , &#8211;</i><code>-lifetime= </code><i>time</i></p>
<dd> Specifies the lifetime of the ticket. The argument can either be in seconds, or a more human readable string like `1h&#8217;</p>
<dt><code>-p , &#8211;proxiable</code></p>
<dd> Request tickets with the proxiable flag set.</p>
<dt><code>-R , &#8211;renew</code></p>
<dd> Try to renew ticket. The ticket must have the `renewable&#8217; flag set, and must not be expired.</p>
<dt><code>&#8211;renewable</code></p>
<dd> The same as &#8211;<code>-renewable-life</code> with an infinite time.</p>
<dt><code>-r </code><i>time , &#8211;</i><code>-renewable-life= </code><i>time</i></p>
<dd> The max renewable ticket life.</p>
<dt><code>-S </code><i>principal , &#8211;</i><code>-server= </code><i>principal</i></p>
<dd> Get a ticket for a service other than krbtgt/LOCAL.REALM.</p>
<dt><code>-s </code><i>time , &#8211;</i><code>-start-time= </code><i>time</i></p>
<dd> Obtain a ticket that starts to be valid <i>time</i> (which can really be a generic time specification, like `1h&#8217; seconds into the future.</p>
<dt><code>-k , &#8211;use-keytab</code></p>
<dd> The same as &#8211;<code>-keytab</code> but with the default keytab name (normally <i>FILE:/etc/krb5.keytab )</i></p>
<dt><code>-v , &#8211;validate</code></p>
<dd> Try to validate an invalid ticket.</p>
<dt><code>-e , &#8211;enctypes= </code><i>enctypes</i></p>
<dd> Request tickets with this particular enctype.</p>
<dt><code>&#8211;password-file= </code><i>filename</i></p>
<dd> read the password from the first line of <i>filename</i> If the <i>filename</i> is <i>STDIN</i> the password will be read from the standard input.</p>
<dt><code>&#8211;fcache-version= </code><i>version-number</i></p>
<dd> Create a credentials cache of version <i>version-number</i></p>
<dt><code>-a , &#8211;extra-addresses= </code><i>enctypes</i></p>
<dd> Adds a set of addresses that will, in addition to the systems local addresses, be put in the ticket. This can be useful if all addresses a client can use can&#8217;t be automatically figured out. One such example is if the client is behind a firewall. Also settable via <code>libdefaults/extra_addresses</code> in krb5.conf5.</p>
<dt><code>-A , &#8211;no-addresses</code></p>
<dd> Request a ticket with no addresses.</p>
<dt><code>&#8211;anonymous</code></p>
<dd> Request an anonymous ticket (which means that the ticket will be issued to an anonymous principal, typically &#8220;anonymous [at] REALM )&#8221;</p>
<dt><code>&#8211;enterprise</code></p>
<dd> Parse principal as a enterprise (KRB5-NT-ENTERPRISE) name. Enterprise names are email like principals that are stored in the name part of the principal, and since there are two @ characters the parser needs to know that the first is not a realm. An example of an enterprise name is &#8220;lha [at] e.kth.se@KTH.SE&#8221; and this option is usually used with canonicalize so that the principal returned from the KDC will typically be the real principal name.</p>
<dt><code>&#8211;afslog</code></p>
<dd> Gets AFS tickets, converts them to version 4 format, and stores them in the kernel. Only useful if you have AFS.</dl>
<p> The <i>forwardable</i> <i>proxiable</i> <i>ticket_life</i> and <i>renewable_life</i> options can be set to a default value from the <code>appdefaults</code> section in krb5.conf, see krb5_appdefault3. </p>
<p> If a <i>command</i> is given, <code>kinit</code> will set up new credentials caches, and AFS PAG, and then run the given command. When it finishes the credentials will be removed.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>KRB5CCNAME</code></p>
<dd> Specifies the default credentials cache.</p>
<dt><code>KRB5_CONFIG</code></p>
<dd> The file name of krb5.conf the default being /etc/krb5.conf</p>
<dt><code>KRBTKFILE</code></p>
<dd> Specifies the Kerberos 4 ticket file to store version 4 tickets in.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-kdestroy/">kdestroy</a>(1), <a href="/docs/linux/man/1-klist/">klist</a>(1), krb5_appdefault3, krb5.conf5 </p>
<h2>Index</h2>
