---

title: "pkcsconf(1)"
name: "pkcsconf"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pkcsconf/"
description: "pkcsconf – configuration utility for the pkcsslotd daemon"
---

<p> pkcsconf &#8211; configuration utility for the pkcsslotd daemon </p>
<h2>SYNOPSIS</h2>
<p> <code>pkcsconf</code> [<code>-itsmlIupPh</code>] [<code>-c</code> <i>slotnumber</i> <code>-U</code> <i>userPIN</i> <code>-S</code> <i>SOPin</i> <code>-n</code> <i>newpin</i>] </p>
<h2>DESCRIPTION</h2>
<p> The <code>pkcsconf</code> utility displays and configures the state of the pkcsslotd daemon and the tokens managed by the daemon. </p>
<h2>COMMAND SUMMARY</h2>
<dl>
<dt><code>-i</code></dt>
<dd> display PKCS11 info</dd>
<dt><code>-t</code></dt>
<dd> display token info</dd>
<dt><code>-s</code></dt>
<dd> display slot info</dd>
<dt><code>-m</code></dt>
<dd> display mechanism list</dd>
<dt><code>-l</code></dt>
<dd> display slot description</dd>
<dt><code>-I</code></dt>
<dd> initialize token</dd>
<dt><code>-u</code></dt>
<dd> initialize user PIN</dd>
<dt><code>-p</code></dt>
<dd> set the user PIN</dd>
<dt><code>-P</code></dt>
<dd> set the SO PIN</dd>
<dt><code>-c</code> <i>SLOT</i></dt>
<dd> specify the token slot for the operation</dd>
<dt><code>-U</code> <i>USERPIN</i></dt>
<dd> the current user pin (for use when changing the user pin; -u and -p options); if not specified, user will be prompted</dd>
<dt><code>-S</code> <i>SOPIN</i></dt>
<dd> the current Security Officer (SO) pin (for use when changing the SO pin; -P option); if not specified, user will be prompted</dd>
<dt><code>-n</code> <i>NEWPIN</i></dt>
<dd> the new pin (for use when changing either the user pin or the SO pin; -u, -p and -P options); if not specified, user will be prompted</dd>
<dt><code>-h</code></dt>
<dd> show usage information </dd>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt><code><a href="/docs/linux/man/7-opencryptoki/">opencryptoki</a></code>(7),</dt>
<dd>
</dd><dt><code><a href="/docs/linux/man/8-pkcsslotd/">pkcsslotd</a></code>(8).</dt>
<dd>
</dd></dl>
