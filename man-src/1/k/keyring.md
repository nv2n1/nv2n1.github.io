---

title: "keyring(1)"
name: "keyring"
section: "1"
letter: "k"
url: "/docs/linux/man/1-keyring/"
description: "keyring – Python-Keyring command-line utility"
---

<p> <code>keyring</code> [<i>,get|set|del/</i>] <i>,SERVICE USERNAME/</i> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Show the help message and exit.</dd>
<dt><code>-p</code> KEYRING_PATH, <code>&#8211;keyring-path</code>=<i>,KEYRING_PATH/</i></dt>
<dd> Specify path to the keyring backend to use.</dd>
<dt><code>-b</code> KEYRING_BACKEND, <code>&#8211;keyring-backend</code>=<i>,KEYRING_BACKEND/</i></dt>
<dd> Specify name of the keyring backend to use.</dd>
<dt><code>&#8211;list-backends</code></dt>
<dd> List the available keyring backends and exit.</dd>
<dt><code>&#8211;disable</code></dt>
<dd> Create a configuration file disabling keyring and exit. </dd>
</dl>
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
