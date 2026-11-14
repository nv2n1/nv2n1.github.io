---
title: "keyring(1)"
name: "keyring"
section: "1"
letter: "k"
url: "/docs/linux/man/1-keyring/"
description: "keyring – Python-Keyring command-line utility"
---

<h2 class="name">NAME</h2>
<p> keyring &#8211; Python-Keyring command-line utility</p>
<h2>SYNOPSIS</h2>
<p> <code>keyring</code> [<i>,get|set|del/</i>] <i>,SERVICE USERNAME/</i> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show the help message and exit.</p>
<dt><code>-p</code> KEYRING_PATH, <code>&#8211;keyring-path</code>=<i>,KEYRING_PATH/</i></p>
<dd> Specify path to the keyring backend to use.</p>
<dt><code>-b</code> KEYRING_BACKEND, <code>&#8211;keyring-backend</code>=<i>,KEYRING_BACKEND/</i></p>
<dd> Specify name of the keyring backend to use.</p>
<dt><code>&#8211;list-backends</code></p>
<dd> List the available keyring backends and exit.</p>
<dt><code>&#8211;disable</code></p>
<dd> Create a configuration file disabling keyring and exit. </p>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>keyring</code> provides a way to store, lookup and delete passwords in various backends supported by Python-Keyring. </p>
<p> Usage example: </p>
<pre>
$ keyring set service username
Password for 'username' in 'service':
$ keyring get service username
password
</pre>
<p> How the <i>,SERVICE/</i> and <i>,USERNAME/</i> parameters are handled depends on the backend, with the default Secret Service backend they are stored as item lookup attributes. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-secret-tool/">secret-tool</a></code>(1) </p>
<h2>Index</h2>
