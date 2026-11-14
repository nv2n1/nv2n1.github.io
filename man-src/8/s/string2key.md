---
title: "string2key(8)"
name: "string2key"
section: "8"
letter: "s"
url: "/docs/linux/man/8-string2key/"
description: "string2key – map a password into a key"
---

<p><code>string2key</code> &#8211; map a password into a key</p>
<h2>Synopsis</h2>
<p>[-<code>5 | &#8211;version5</code> ] [-<code>4 | &#8211;version4</code> ] [-<code>a | &#8211;afs</code> ] [-<code>c </code><i>cell | </i> &#8211;<code>-cell= </code><i>cell</i> ] [-<code>w </code><i>password | </i> &#8211;<code>-password= </code><i>password</i> ] [-<code>p </code><i>principal | </i> &#8211;<code>-principal= </code><i>principal</i> ] [-<code>k </code><i>string | </i> &#8211;<code>-keytype= </code><i>string</i> ] <i>password</i></p>
<h2>Description</h2>
<p>performs the string-to-key function. This is useful when you want to handle the raw key instead of the password. Supported options:</p>
<dl>
<dt><code>-5 , &#8211;version5</code></p>
<dd>Output Kerberos v5 string-to-key</p>
<dt><code>-4 , &#8211;version4</code></p>
<dd>Output Kerberos v4 string-to-key</p>
<dt><code>-a , &#8211;afs</code></p>
<dd>Output AFS string-to-key</p>
<dt><code>-c </code><i>cell , &#8211;</i><code>-cell= </code><i>cell</i></p>
<dd>AFS cell to use</p>
<dt><code>-w </code><i>password , &#8211;</i><code>-password= </code><i>password</i></p>
<dd>Password to use</p>
<dt><code>-p </code><i>principal , &#8211;</i><code>-principal= </code><i>principal</i></p>
<dd>Kerberos v5 principal to use</p>
<dt><code>-k </code><i>string , &#8211;</i><code>-keytype= </code><i>string</i></p>
<dd>Keytype</p>
<dt><code>&#8211;version</code></p>
<dd>print version</p>
<dt><code>&#8211;help</code></p>
<dd></dl>
