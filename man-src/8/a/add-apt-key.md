---
title: "add-apt-key(8)"
name: "add-apt-key"
section: "8"
letter: "a"
url: "/docs/linux/man/8-add-apt-key/"
description: "add-apt-key – Command line tool to add GPG keys to the APT keyring"
---

<p>add-apt-key &#8211; Command line tool to add GPG keys to the APT keyring</p>
<h2>Synopsis</h2>
<p><code>add-apt-key</code> [ <code>&#8211;help</code> ] [ <code>&#8211;verbose</code> ] [ <code>&#8211;keyserver name</code> ] <code>keyid</code></p>
<h2>Description</h2>
<p>The add-apt-key will request the specified GPG key from a public keyserver and insert it into the APT keyring so that archives signed with that key will be trusted.</p>
<h2>Options</h2>
<p>This program follows the usual GNU command line syntax, with long options starting with two dashes (<code>&#8212;</code>).</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Show online help (usage).</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>verbose mode will show each command before it is executed.</p>
<dt><code>-k</code>, <code>&#8211;keyserver name</code></p>
<dd>Select a specific keyserver to use.</p>
<dt><code>keyid</code></p>
<dd>The GPG key identifier to add.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/default/add-apt-key</code></p>
<dd>Configuration file specifying the public keyserver to use.</dl>
<h2>Exit Values</h2>
<p>The folling exit values are used:</p>
<dl>
<dt><code>0</code></p>
<dd>Adding the keyid was successful.</p>
<dt><code>1</code></p>
<dd>Invalid script arguments.</p>
<dt><code>2</code></p>
<dd>GPG keyid cannot be retrieved (or is malformed).</p>
<dt><code>3</code></p>
<dd>Error in adding keyid to the APT keyring.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-gpg/">gpg</a>(1), <a href="/docs/linux/man/8-apt-key/">apt-key</a>(8) </p>
