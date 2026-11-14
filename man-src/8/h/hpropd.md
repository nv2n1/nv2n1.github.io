---
title: "hpropd(8)"
name: "hpropd"
section: "8"
letter: "h"
url: "/docs/linux/man/8-hpropd/"
description: "hpropd – receive a propagated database"
---

<p><code>hpropd</code> &#8211; receive a propagated database</p>
<h2>Synopsis</h2>
<p>-words [-<code>d </code><i>file | </i> &#8211;<code>-database= </code><i>file</i> ] [-<code>n | &#8211;stdin</code> ] [-<code>-print</code> ] [-<code>i | &#8211;no-inetd</code> ] [-<code>k </code><i>keytab | </i> &#8211;<code>-keytab= </code><i>keytab</i> ] [-<code>4 | &#8211;v4dump</code> ]</p>
<h2>Description</h2>
<p>receives a database sent by <code>hprop</code> and writes it as a local database. By default, expects to be started from <code>inetd</code> if stdin is a socket and expects to receive the dumped database over stdin otherwise. If the database is sent over the network, it is authenticated and encrypted. Only connections authenticated with the principal <code>kadmin / hprop</code> are accepted. Options supported:</p>
<dl>
<dt><code>-d </code><i>file , &#8211;</i><code>-database= </code><i>file</i></p>
<dd>database</p>
<dt><code>-n , &#8211;stdin</code></p>
<dd>read from stdin</p>
<dt><code>&#8211;print</code></p>
<dd>print dump to stdout</p>
<dt><code>-i , &#8211;no-inetd</code></p>
<dd>not started from inetd</p>
<dt><code>-k </code><i>keytab , &#8211;</i><code>-keytab= </code><i>keytab</i></p>
<dd>keytab to use for authentication</p>
<dt><code>-4 , &#8211;v4dump</code></p>
<dd>create v4 type DB</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-hprop/">hprop</a>(8) </p>
