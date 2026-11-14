---
title: "kdestroy(1)"
name: "kdestroy"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kdestroy/"
description: "kdestroy – destroy Kerberos tickets"
---

<h2>NAME</h2>
<p> kdestroy &#8211; destroy Kerberos tickets</p>
<h2>SYNOPSIS</h2>
<p> <code>kdestroy</code> [<code>-A</code>] [<code>-q</code>] [<code>-c</code> <i>cache_name</i>]</p>
<h2>DESCRIPTION</h2>
<p> The kdestroy utility destroys the user&#8217;s active Kerberos authorization tickets by overwriting and deleting the credentials cache that contains them. If the credentials cache is not specified, the default credentials cache is destroyed.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A</code></p>
<dd> Destroys all caches in the collection, if a cache collection is available.</p>
<dt><code>-q</code></p>
<dd> Run quietly. Normally kdestroy beeps if it fails to destroy the user&#8217;s tickets. The <code>-q</code> flag suppresses this behavior.</p>
<dt><code>-c</code> <i>cache_name</i></p>
<dd> Use <i>cache_name</i> as the credentials (ticket) cache name and location; if this option is not used, the default cache name and location are used. </p>
<p> The default credentials cache may vary between systems. If the <code>KRB5CCNAME</code> environment variable is set, its value is used to name the default ticket cache.</dl>
<h2>NOTE</h2>
<p> Most installations recommend that you place the kdestroy command in your .logout file, so that your tickets are destroyed automatically when you log out.</p>
<h2>ENVIRONMENT</h2>
<p> kdestroy uses the following environment variable:</p>
<dl>
<dt><code>KRB5CCNAME</code></p>
<dd> Location of the default Kerberos 5 credentials (ticket) cache, in the form <i>type</i>:<i>residual</i>. If no <i>type</i> prefix is present, the <code>FILE</code> type is assumed. The type of the default cache may determine the availability of a cache collection; for instance, a default cache of type <code>DIR</code> causes caches within the directory to be present in the collection.</dl>
<h2>FILES</h2>
<dl>
<dt><code>FILE:/tmp/krb5cc_%{uid}</code></p>
<dd> Default location of Kerberos 5 credentials cache</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-kinit/">kinit</a>(1)</i>, <i><a href="/docs/linux/man/1-klist/">klist</a>(1)</i></p>
<h2>AUTHOR</h2>
<p> MIT</p>
<h2>COPYRIGHT</h2>
<p> 1985-2017, MIT </p>
<h2>Index</h2>
