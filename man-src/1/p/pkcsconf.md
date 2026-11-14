---
title: "pkcsconf(1)"
name: "pkcsconf"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pkcsconf/"
description: "pkcsconf – configuration utility for the pkcsslotd daemon"
---

<h2>NAME</h2>
<p> pkcsconf &#8211; configuration utility for the pkcsslotd daemon </p>
<h2>SYNOPSIS</h2>
<p> <code>pkcsconf</code> [<code>-itsmlIupPh</code>] [<code>-c</code> <i>slotnumber</i> <code>-U</code> <i>userPIN</i> <code>-S</code> <i>SOPin</i> <code>-n</code> <i>newpin</i>] </p>
<h2>DESCRIPTION</h2>
<p> The <code>pkcsconf</code> utility displays and configures the state of the pkcsslotd daemon and the tokens managed by the daemon. </p>
<h2>COMMAND SUMMARY</h2>
<dl>
<dt><code>-i</code></p>
<dd> display PKCS11 info</p>
<dt><code>-t</code></p>
<dd> display token info</p>
<dt><code>-s</code></p>
<dd> display slot info</p>
<dt><code>-m</code></p>
<dd> display mechanism list</p>
<dt><code>-l</code></p>
<dd> display slot description</p>
<dt><code>-I</code></p>
<dd> initialize token</p>
<dt><code>-u</code></p>
<dd> initialize user PIN</p>
<dt><code>-p</code></p>
<dd> set the user PIN</p>
<dt><code>-P</code></p>
<dd> set the SO PIN</p>
<dt><code>-c</code> <i>SLOT</i></p>
<dd> specify the token slot for the operation</p>
<dt><code>-U</code> <i>USERPIN</i></p>
<dd> the current user pin (for use when changing the user pin; -u and -p options); if not specified, user will be prompted</p>
<dt><code>-S</code> <i>SOPIN</i></p>
<dd> the current Security Officer (SO) pin (for use when changing the SO pin; -P option); if not specified, user will be prompted</p>
<dt><code>-n</code> <i>NEWPIN</i></p>
<dd> the new pin (for use when changing either the user pin or the SO pin; -u, -p and -P options); if not specified, user will be prompted</p>
<dt><code>-h</code></p>
<dd> show usage information </p>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt><code><a href="/docs/linux/man/7-opencryptoki/">opencryptoki</a></code>(7),</p>
<dd>
<dt><code><a href="/docs/linux/man/8-pkcsslotd/">pkcsslotd</a></code>(8).</p>
<dd>
</dl>
<h2>Index</h2>
