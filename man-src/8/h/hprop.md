---
title: "hprop(8)"
name: "hprop"
section: "8"
letter: "h"
url: "/docs/linux/man/8-hprop/"
description: "hprop – propagate the KDC database"
---

<p><code>hprop</code> &#8211; propagate the KDC database</p>
<h2>Synopsis</h2>
<p>-words [-<code>m </code><i>file | </i> &#8211;<code>-master-key= file </code> ] [-<code>d </code><i>file | </i> &#8211;<code>-database= file </code> ] [-<code>-source= </code><i>heimdal|mit-dump</i> ] [-<code>r </code><i>string | </i> &#8211;<code>-v4-realm= </code><i>string</i> ] [-<code>c </code><i>cell | </i> &#8211;<code>-cell= </code><i>cell</i> ] [-<code>k </code><i>keytab | </i> &#8211;<code>-keytab= </code><i>keytab</i> ] [-<code>R </code><i>string | </i> &#8211;<code>-v5-realm= </code><i>string</i> ] [-<code>D | &#8211;decrypt</code> ] [-<code>E | &#8211;encrypt</code> ] [-<code>n | &#8211;stdout</code> ] [-<code>v | &#8211;verbose</code> ] [-<code>-version</code> ] [-<code>h | &#8211;help</code> ] [<i>host </i>[: <i>port</i> ] ] <i>&#8230;</i></p>
<h2>Description</h2>
<p>takes a principal database in a specified format and converts it into a stream of Heimdal database records. This stream can either be written to standard out, or (more commonly) be propagated to a <a href="/docs/linux/man/8-hpropd/">hpropd</a>(8) server running on a different machine. If propagating, it connects to all <i>hosts</i> specified on the command by opening a TCP connection to port 754 (service hprop) and sends the database in encrypted form. Supported options:</p>
<dl>
<dt><code>-m </code><i>file , &#8211;</i><code>-master-key= file </code></p>
<dd>Where to find the master key to encrypt or decrypt keys with.</p>
<dt><code>-d </code><i>file , &#8211;</i><code>-database= file </code></p>
<dd>The database to be propagated.</p>
<dt><code>&#8211;source= </code><i>heimdal|mit-dump|krb4-dump|kaserver</i></p>
<dd>Specifies the type of the source database. Alternatives include: </p>
<dt><code>heimdal</code></p>
<dd>a Heimdal database</p>
<dt><code>mit-dump</code></p>
<dd>a MIT Kerberos 5 dump file</dl>
<p> +.It Fl k Ar keytab , Fl Fl keytab= Ns Ar keytab The keytab to use for fetching the key to be used for authenticating to the propagation daemon(s). The key hprop/hostname is used from this keytab. The default is to fetch the key from the KDC database.</p>
<dt><code>-R </code><i>string , &#8211;</i><code>-v5-realm= </code><i>string</i></p>
<dd>Local realm override.</p>
<dt><code>-D , &#8211;decrypt</code></p>
<dd>The encryption keys in the database can either be in clear, or encrypted with a master key. This option transmits the database with unencrypted keys.</p>
<dt><code>-E , &#8211;encrypt</code></p>
<dd>This option transmits the database with encrypted keys.</p>
<dt><code>-n , &#8211;stdout</code></p>
<dd>Dump the database on stdout, in a format that can be fed to hpropd.</dl>
<h2>Examples</h2>
<p>The following will propagate a database to another machine (which should run <a href="/docs/linux/man/8-hpropd/">hpropd</a>(8)): </p>
<blockquote>
<pre>$ hprop slave-1 slave-2</pre>
</blockquote>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-hpropd/">hpropd</a>(8) </p>
