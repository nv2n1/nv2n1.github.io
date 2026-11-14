---
title: "forbidden_words(5)"
name: "forbidden_words"
section: "5"
letter: "f"
url: "/docs/linux/man/5-forbidden_words/"
---

forbidden_words.conf - configuration file for libreport.

<h2>Description</h2>

This configuration file specifies which words are highlighted in User Interface during the process of reporting a problem for the purpose of warning a user and getting his attention before he publish security sensitive data. 

 The configuration format is one line per forbidden word. 

 Users can provide own file with the list of forbidden words which will be appended to the list of forbidden words loaded from /etc/libreport/forbidden_words.conf

<h2>Examples</h2>

System configuration: 

 /etc/libreport/forbidden_words.conf 

<dl><dd><pre>password
login
mastercard</pre></dl>
 

 User configuration: 

 $XDG_CONFIG_HOME/abrt/settings/forbidden_words.conf 

<dl><dd><pre>usersecretpassword</pre></dl>

<h2>See Also</h2>

<a HREF="/docs/linux/man/1-report-gtk/">report-gtk</a>(1), <a HREF="/docs/linux/man/5-ignored_words-conf/">ignored_words.conf</a>(5)

<h2>Author</h2>

<dl><dd>&bull; ABRT team</dl>
