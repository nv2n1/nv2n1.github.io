---
title: "kstash(8)"
name: "kstash"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kstash/"
description: "kstash – store the KDC master password in a file"
---

<p><code>kstash</code> &#8211; store the KDC master password in a file</p>
<h2>Synopsis</h2>
<p>-words [-<code>e </code><i>string | </i> &#8211;<code>-enctype= </code><i>string</i> ] [-<code>k </code><i>file | </i> &#8211;<code>-key-file= </code><i>file</i> ] [-<code>-convert-file</code> ] [-<code>-random-key</code> ] [-<code>-master-key-fd= </code><i>fd</i> ] [-<code>-random-key</code> ] [-<code>h | &#8211;help</code> ] [-<code>-version</code> ]</p>
<h2>Description</h2>
<p>reads the Kerberos master key and stores it in a file that will be used by the KDC. Supported options:</p>
<dl>
<dt><code>-e </code><i>string , &#8211;</i><code>-enctype= </code><i>string</i></p>
<dd>the encryption type to use, defaults to DES3-CBC-SHA1.</p>
<dt><code>-k </code><i>file , &#8211;</i><code>-key-file= </code><i>file</i></p>
<dd>the name of the master key file.</p>
<dt><code>&#8211;convert-file</code></p>
<dd>don&#8217;t ask for a new master key, just read an old master key file, and write it back in the new keyfile format.</p>
<dt><code>&#8211;random-key</code></p>
<dd>generate a random master key.</p>
<dt><code>&#8211;master-key-fd= </code><i>fd</i></p>
<dd>filedescriptor to read passphrase from, if not specified the passphrase will be read from the terminal.</dl>
<h2>Files</h2>
<p>/var/heimdal/m-key is the default keyfile if no other keyfile is specified. The format of a Heimdal master key is the same as a keytab, so <code>ktutil</code> list can be used to list the content of the file.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-kdc/">kdc</a>(8) </p>
