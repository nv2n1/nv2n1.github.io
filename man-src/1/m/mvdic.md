---
title: "mvdic(1)"
name: "mvdic"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mvdic/"
description: "mvdic – Tool for renaming a user dictionary"
---

<h2>NAME</h2>
<p> mvdic &#8211; Tool for renaming a user dictionary</p>
<h2>SYNOPSIS</h2>
<p> <code>mvdic [{-cs|-cannaserver} </code><i>canna-server</i>] <i>from-dic</i> <i>to-dic</i></p>
<h2>DESCRIPTION</h2>
<p> mvdic changes the name of the specified user dictionary from <i>from-dic</i> to <i>to-dic</i>. Dictionary directory file &#8212; dics.dir &#8212; is rewritten correspondingly to this. </p>
<p> After the changing, the old dictionary name of the customize file must be deleted. </p>
<p> The dictionary in use (i.e., the currently mounted dictionary) cannot be deleted.</p>
<h2>OPTION</h2>
<dl>
<dt>-cs <i>canna-server</i> (or -cannaserver <i>canna-server</i>)</p>
<dd> Specifies the name of the server machine that contains the dictionary to be renamed.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cpdic/">cpdic</a>(1), <a href="/docs/linux/man/1-lsdic/">lsdic</a>(1), <a href="/docs/linux/man/1-mkdic/">mkdic</a>(1), <a href="/docs/linux/man/1-rmdic/">rmdic</a>(1) </p>
<h2>Index</h2>
