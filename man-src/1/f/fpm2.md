---
title: "fpm2(1)"
name: "fpm2"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fpm2/"
description: "fpm2 – Figaro’s Password Manager 2"
---

<h2>NAME</h2>
<p> fpm2 &#8211; Figaro&#8217;s Password Manager 2</p>
<h2>DESCRIPTION</h2>
<p> <code>fpm2</code> is a <font SIZE="-1">GUI</font> password manager using the <font SIZE="-1">GTK2 libraries. Passwords are encrypted using the AES-256 algorithm.</font></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f filename</code></p>
<dd> Use a different file to store fpm data. Must include directory where file is stored.</p>
<dt><code>-t</code></p>
<dd> Start fpm2 hidden in tray. No ask for password on startup.</dl>
<h2>USAGE</h2>
<dl>
<dt><code>launchers</code></p>
<dd> Arbitrary launchers can be defined, in order to automatically launch progammes with parameters from the password entry, eg:</dl>
<dl>
<dt>
<dd> <code>xterm -title $u@$a -e ssh -X $a -l $u</code>.</dl>
<dl>
<dt>
<dd> Possible variables are:</dl>
<dl>
<dt>
<dd> <code>$a</code> &#8211; an arbitrary argument associated with the password entry &#8211; typically a hostname. </p>
<p> <code>$u</code> &#8211; the username associated with the password entry </p>
<p> <code>$p</code> &#8211; the password associated with the password entry</dl>
<dl>
<dt><code>on-the-fly categories</code></p>
<dd> Each password entry can belong to a category, which is generated just by naming it in at least one entry.</p>
<dt><code>password generation</code></p>
<dd> <code>fpm2</code> will generate passwords for you. Up to 24 characters with a boolean choices for <i>lowercase</i>, <i>uppercase</i>, <i>numbers</i>, <i>symbols</i> and <i>ambigous characters</i> (eg. `O` and `0`).</dl>
<h2>SECURITY</h2>
<p> Using the $p variable means that your password ends up in <i>.bash_history</i> in addition to being visible by <code>ps aux</code>! </p>
<p> In order to work around this problem conveniently <code>fpm2</code> can have your password copied to your primary selection, so that you may easily paste it where needed. Then your password should be as secured as your transport.</p>
<h2>COPYRIGHT</h2>
<p> <font SIZE="-1">GNU GPL</font> (GNU GENERAL PUBLIC LICENSE) Version 2, or (at your option) any later version. </p>
<p> The licence text is available on any Debian GNU/Linux system in <i>/usr/share/common-licenses/GPL</i></p>
<h2>AUTHOR</h2>
<p> John Conneely &lt;jconneely [at] figaro.org&gt;<br />
 Aleš Koval &lt;als [at] regnet.cz&gt; </p>
<p> This manual page was written by Lars Bahner &lt;bahner [at] debian.org&gt; for the Debian GNU/Linux system. </p>
<h2>Index</h2>
