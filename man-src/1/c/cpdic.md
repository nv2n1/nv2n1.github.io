---
title: "cpdic(1)"
name: "cpdic"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cpdic/"
description: "cpdic – User Dictionary Copy Tool"
---

<h2>NAME</h2>
<p> cpdic &#8211; User Dictionary Copy Tool</p>
<h2>SYNOPSIS</h2>
<p> <code>cpdic [{-cs|-cannaserver} </code><i>canna-server</i>] [-i|-u <i>user-name</i>] <i>from-dic</i> <i>to-dic</i></p>
<h2>DESCRIPTION</h2>
<p> cpdic copies user dictionary <i>from-dic</i> to <i>to-dic</i> to rewrite dictionary directory file &#8212; dics.dir &#8212; . </p>
<p> If the user dictionary directory does not exist, cpdic creates it and creates dics.dir under it. </p>
<p> If the -i option is specified, the system dictionary will be copied. If the -u option is specified, another user dictionary will be copied.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-cs <i>canna-server</i> (or -cannaserver <i>canna-server</i>)</p>
<dd></dl>
<p> Specifies the name of the server machine that contains a dictionary to be copied.</p>
<dl>
<dt>-i</p>
<dd> Copies the system dictionary.</p>
<dt>-u <i>user-name</i></p>
<dd> Copies the dictionary of the specified user.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-lsdic/">lsdic</a>(1), <a href="/docs/linux/man/1-mkdic/">mkdic</a>(1), <a href="/docs/linux/man/1-mvdic/">mvdic</a>(1), <a href="/docs/linux/man/1-rmdic/">rmdic</a>(1) </p>
<h2>Index</h2>
