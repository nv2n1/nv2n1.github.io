---
title: "rlm_unix(5)"
name: "rlm_unix"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rlm_unix/"
description: "rlm_unix – FreeRADIUS Module"
---

<p>rlm_unix &#8211; FreeRADIUS Module</p>
<h2>Description</h2>
<p>The <i>rlm_unix</i> module reads <a href="/docs/linux/man/3-crypt/">crypt</a>(3) passwords from the system password file, and allows the server to use them for authentication. The module also provides FreeRADIUS an interface into a radwtmp file (used by &quot;radlast&quot;) when added to the accounting section. </p>
<p> The <i>rlm_unix</i> module does provides the functionality for &quot;Auth-Type = System&quot;. The module should be listed in the &quot;authenticate&quot; section. Please see the default <i>radiusd.conf</i> shipped with the server for an example of the correct usage of this module. </p>
<p> As of FreeRADIUS 1.1.0, the module no longer reads, or caches /etc/passwd, /etc/shadow, or /etc/group. If you wish to cache those files, see <i>rlm_passwd</i>. Most, if not all, configurations should not need those files to be cached. </p>
<p> The main configuration items to be aware of are:</p>
<dl>
<dt>radwtmp</p>
<dd>The path to the system wtmp file to be used for keeping the database of online users as read by the &#8216;radlast&#8217; program.</dl>
<h2>Configuration</h2>
<dl>
<dd>
<pre>modules {
 ...
<br>
 unix {
<br>
 radwtmp = ${logdir}/radwtmp
<br>
 }
<br>
 ...
<br>
}</pre>
</dl>
<h2>Sections</h2>
<p><code>authentication,</code> <code>accounting</code></p>
<h2>Files</h2>
<p><i>/etc/raddb/radiusd.conf,</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-radiusd/">radiusd</a></code>(8), <code><a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a></code>(5), <code><a href="/docs/linux/man/5-rlm_passwd/">rlm_passwd</a></code>(5), <code><a href="/docs/linux/man/1-radlast/">radlast</a></code>(1)</p>
<h2>Authors</h2>
<p>Chris Parker, cparker [at] segv.org</p>
