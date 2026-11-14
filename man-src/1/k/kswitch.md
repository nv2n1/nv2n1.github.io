---
title: "kswitch(1)"
name: "kswitch"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kswitch/"
description: "kswitch – switch primary ticket cache"
---

<h2>NAME</h2>
<p> kswitch &#8211; switch primary ticket cache</p>
<h2>SYNOPSIS</h2>
<p> <code>kswitch</code> {<code>-c</code> <i>cachename</i>|<code>-p</code> <i>principal</i>}</p>
<h2>DESCRIPTION</h2>
<p> kswitch makes the specified credential cache the primary cache for the collection, if a cache collection is available.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> <i>cachename</i></p>
<dd> Directly specifies the credential cache to be made primary.</p>
<dt><code>-p</code> <i>principal</i></p>
<dd> Causes the cache collection to be searched for a cache containing credentials for <i>principal</i>. If one is found, that collection is made primary.</dl>
<h2>ENVIRONMENT</h2>
<p> kswitch uses the following environment variables:</p>
<dl>
<dt><code>KRB5CCNAME</code></p>
<dd> Location of the default Kerberos 5 credentials (ticket) cache, in the form <i>type</i>:<i>residual</i>. If no <i>type</i> prefix is present, the <code>FILE</code> type is assumed. The type of the default cache may determine the availability of a cache collection; for instance, a default cache of type <code>DIR</code> causes caches within the directory to be present in the collection.</dl>
<h2>FILES</h2>
<dl>
<dt><code>FILE:/tmp/krb5cc_%{uid}</code></p>
<dd> Default location of Kerberos 5 credentials cache</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-kinit/">kinit</a>(1)</i>, <i><a href="/docs/linux/man/1-kdestroy/">kdestroy</a>(1)</i>, <i><a href="/docs/linux/man/1-klist/">klist</a>(1)</i>), <a href="/docs/linux/man/1-kerberos/">kerberos</a>(1)</p>
<h2>AUTHOR</h2>
<p> MIT</p>
<h2>COPYRIGHT</h2>
<p> 1985-2017, MIT </p>
<h2>Index</h2>
