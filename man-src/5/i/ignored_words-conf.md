---
title: "ignored_words-conf(5)"
name: "ignored_words-conf"
section: "5"
letter: "i"
url: "/docs/linux/man/5-ignored_words-conf/"
description: "ignored_words.conf – configuration file for libreport."
---

<p>ignored_words.conf &#8211; configuration file for libreport.</p>
<h2>Description</h2>
<p>This configuration file specifies which words are <code>NOT</code> highlighted in User Interface during the process of reporting a problem for the purpose of warning a user and getting his attention before he publish security sensitive data. </p>
<p> The configuration format is one line per ignored word. </p>
<p> Users can provide own file with the list of ignored words which will be appended to the list of ignored words loaded from /etc/libreport/ignored_words.conf</p>
<h2>Examples</h2>
<p>System configuration: </p>
<p> /etc/libreport/ignored_words.conf </p>
<dl>
<dd>
<pre>USER=
login.so
SSH_ASKPASS=</pre>
</dl>
<p> User configuration: </p>
<p> $XDG_CONFIG_HOME/abrt/settings/ignored_words.conf </p>
<dl>
<dd>
<pre>libpassword.so</pre>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-report-gtk/">report-gtk</a>(1), <a href="/docs/linux/man/5-forbidden_words-conf/">forbidden_words.conf</a>(5)</p>
<h2>Author</h2>
<dl>
<dd>&bull; ABRT team</dl>
