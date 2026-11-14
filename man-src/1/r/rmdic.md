---
title: "rmdic(1)"
name: "rmdic"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rmdic/"
description: "rmdic – Tool for deleting a user dictionary"
---

<h2>NAME</h2>
<p> rmdic &#8211; Tool for deleting a user dictionary</p>
<h2>SYNOPSIS</h2>
<p> <code>rmdic [{-cs|-cannaserver} </code><i>canna-server</i>] <i>dicname1</i> [<i>dicname2</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> rmdic deletes the specified user dictionary (or dictionaries). Dictionary directory file &#8212; dics.dir &#8212; is rewritten correspondingly to this. </p>
<p> More than one user dictionary may be specified. </p>
<p> The dictionary in use (i.e., the currently mounted dictionary) cannot be deleted.</p>
<h2>OPTION</h2>
<dl>
<dt>-cs <i>canna-server</i> (or -cannaserver <i>canna-server</i>)</p>
<dd> Specifies the name of the server machine that contains the dictionary to be renamed.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cpdic/">cpdic</a>(1), <a href="/docs/linux/man/1-lsdic/">lsdic</a>(1), <a href="/docs/linux/man/1-mkdic/">mkdic</a>(1), <a href="/docs/linux/man/1-mvdic/">mvdic</a>(1) </p>
<h2>Index</h2>
