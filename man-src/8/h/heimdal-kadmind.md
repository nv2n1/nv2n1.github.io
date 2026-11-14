---
title: "heimdal-kadmind(8)"
name: "heimdal-kadmind"
section: "8"
letter: "h"
url: "/docs/linux/man/8-heimdal-kadmind/"
description: "kadmind – server for administrative access to Kerberos database"
---

<p><code>kadmind</code> &#8211; server for administrative access to Kerberos database</p>
<h2>Synopsis</h2>
<p>-words [-<code>c </code><i>file | </i> &#8211;<code>-config-file= </code><i>file</i> ] [-<code>k </code><i>file | </i> &#8211;<code>-key-file= </code><i>file</i> ] [-<code>-keytab= </code><i>keytab</i> ] [-<code>r </code><i>realm | </i> &#8211;<code>-realm= </code><i>realm</i> ] [-<code>d | &#8211;debug</code> ] [-<code>p </code><i>port | </i> &#8211;<code>-ports= </code><i>port</i> ]</p>
<h2>Description</h2>
<p>listens for requests for changes to the Kerberos database and performs these, subject to permissions. When starting, if stdin is a socket it assumes that it has been started by <a href="/docs/linux/man/8-inetd/">inetd</a>(8), otherwise it behaves as a daemon, forking processes for each new connection. The &#8211;<code>-debug</code> option causes to accept exactly one connection, which is useful for debugging. The <a href="/docs/linux/man/8-kpasswdd/">kpasswdd</a>(8) daemon is responsible for the Kerberos 5 password changing protocol (used by <a href="/docs/linux/man/1-kpasswd/">kpasswd</a>(1)). This daemon should only be run on the master server, and not on any slaves. Principals are always allowed to change their own password and list their own principal. Apart from that, doing any operation requires permission explicitly added in the ACL file /var/heimdal/kadmind.acl The format of this file is: <i>principal</i> <i>rights</i> [<i>principal-pattern</i> ] Where rights is any (comma separated) combination of: </p>
<ul>
<li> change-password or cpw
<li> list
<li> delete
<li> modify
<li> add
<li> get
<li> get-keys
<li> all </ul>
<p> And the optional <i>principal-pattern</i> restricts the rights to operations on principals that match the glob-style pattern. Supported options:</p>
<dl>
<dt><code>-c </code><i>file , &#8211;</i><code>-config-file= </code><i>file</i></p>
<dd>location of config file</p>
<dt><code>-k </code><i>file , &#8211;</i><code>-key-file= </code><i>file</i></p>
<dd>location of master key file</p>
<dt><code>&#8211;keytab= </code><i>keytab</i></p>
<dd>what keytab to use</p>
<dt><code>-r </code><i>realm , &#8211;</i><code>-realm= </code><i>realm</i></p>
<dd>realm to use</p>
<dt><code>-d , &#8211;debug</code></p>
<dd>enable debugging</p>
<dt><code>-p </code><i>port , &#8211;</i><code>-ports= </code><i>port</i></p>
<dd>ports to listen to. By default, if run as a daemon, it listens to port 749, but you can add any number of ports with this option. The port string is a whitespace separated list of port specifications, with the special string &#8220;+&#8221; representing the default port.</dl>
<h2>Files</h2>
<p>/var/heimdal/kadmind.acl</p>
<h2>Examples</h2>
<p>This will cause to listen to port 4711 in addition to any compiled in defaults: </p>
<p> This acl file will grant Joe all rights, and allow Mallory to view and add host principals, as well as extract host principal keys (e.g., into keytabs). </p>
<blockquote>
<pre>joe/admin [at] EXAMPLE.COM all
mallory/admin [at] EXAMPLE.COM add,get-keys host/*@EXAMPLE.COM</pre>
</blockquote>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-kpasswd/">kpasswd</a>(1), <a href="/docs/linux/man/8-kadmin/">kadmin</a>(8), <a href="/docs/linux/man/8-kdc/">kdc</a>(8), <a href="/docs/linux/man/8-kpasswdd/">kpasswdd</a>(8) </p>
