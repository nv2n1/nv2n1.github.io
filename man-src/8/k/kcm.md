---
title: "kcm(8)"
name: "kcm"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kcm/"
description: "kcm – process-based credential cache for Kerberos tickets."
---

<p><code>kcm</code> &#8211; process-based credential cache for Kerberos tickets.</p>
<h2>Synopsis</h2>
<p>[-<code>-cache-name= </code><i>cachename</i> ] [-<code>c </code><i>file | </i> &#8211;<code>-config-file= </code><i>file</i> ] [-<code>g </code><i>group | </i> &#8211;<code>-group= </code><i>group</i> ] [-<code>-max-request= </code><i>size</i> ] [-<code>-disallow-getting-krbtgt</code> ] [-<code>-detach</code> ] [-<code>h | &#8211;help</code> ] [-<code>k </code><i>principal | </i> &#8211;<code>-system-principal= </code><i>principal</i> ] [-<code>l </code><i>time | </i> &#8211;<code>-lifetime= </code><i>time</i> ] [-<code>m </code><i>mode | </i> &#8211;<code>-mode= </code><i>mode</i> ] [-<code>n | &#8211;no-name-constraints</code> ] [-<code>r </code><i>time | </i> &#8211;<code>-renewable-life= </code><i>time</i> ] [-<code>s </code><i>path | </i> &#8211;<code>-socket-path= </code><i>path</i> ] [ &#8211;<code>-door-path= </code><i>path</i> ] [-<code>S </code><i>principal | </i> &#8211;<code>-server= </code><i>principal</i> ] [-<code>t </code><i>keytab | </i> &#8211;<code>-keytab= </code><i>keytab</i> ] [-<code>u </code><i>user | </i> &#8211;<code>-user= </code><i>user</i> ] [-<code>v | &#8211;version</code> ]</p>
<h2>Description</h2>
<p>is a process based credential cache. To use it, set the <code>KRB5CCNAME</code> enviroment variable to `KCM:&#8217; Ns Ar uid or add the stanza </p>
<pre>[libdefaults]
 default_cc_name = KCM:%{uid}</pre>
<p>to the /etc/krb5.conf configuration file and make sure <code>kcm</code> is started in the system startup files. The daemon can hold the credentials for all users in the system. Access control is done with Unix-like permissions. The daemon checks the access on all operations based on the uid and gid of the user. The tickets are renewed as long as is permitted by the KDC&#8217;s policy. The daemon can also keep a SYSTEM credential that server processes can use to access services. One example of usage might be an nss_ldap module that quickly needs to get credentials and doesn&#8217;t want to renew the ticket itself. Supported options:</p>
<dl>
<dt><code>&#8211;cache-name= </code><i>cachename</i></p>
<dd>system cache name</p>
<dt><code>-c </code><i>file , &#8211;</i><code>-config-file= </code><i>file</i></p>
<dd>location of config file</p>
<dt><code>-g </code><i>group , &#8211;</i><code>-group= </code><i>group</i></p>
<dd>system cache group</p>
<dt><code>&#8211;max-request= </code><i>size</i></p>
<dd>max size for a kcm-request</p>
<dt><code>&#8211;disallow-getting-krbtgt</code></p>
<dd>disallow extracting any krbtgt from the <code>kcm</code> daemon.</p>
<dt><code>&#8211;detach</code></p>
<dd>detach from console</p>
<dt><code>-h , &#8211;help</code></p>
<dd>
<dt><code>-k </code><i>principal , &#8211;</i><code>-system-principal= </code><i>principal</i></p>
<dd>system principal name</p>
<dt><code>-l </code><i>time , &#8211;</i><code>-lifetime= </code><i>time</i></p>
<dd>lifetime of system tickets</p>
<dt><code>-m </code><i>mode , &#8211;</i><code>-mode= </code><i>mode</i></p>
<dd>octal mode of system cache</p>
<dt><code>-n , &#8211;no-name-constraints</code></p>
<dd>disable credentials cache name constraints</p>
<dt><code>-r </code><i>time , &#8211;</i><code>-renewable-life= </code><i>time</i></p>
<dd>renewable lifetime of system tickets</p>
<dt><code>-s </code><i>path , &#8211;</i><code>-socket-path= </code><i>path</i></p>
<dd>path to kcm domain socket</p>
<dt><code>&#8211;door-path= </code><i>path</i></p>
<dd>path to kcm door socket</p>
<dt><code>-S </code><i>principal , &#8211;</i><code>-server= </code><i>principal</i></p>
<dd>server to get system ticket for</p>
<dt><code>-t </code><i>keytab , &#8211;</i><code>-keytab= </code><i>keytab</i></p>
<dd>system keytab name</p>
<dt><code>-u </code><i>user , &#8211;</i><code>-user= </code><i>user</i></p>
<dd>system cache owner</p>
<dt><code>-v , &#8211;version</code></p>
<dd></dl>
