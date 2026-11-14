---
title: "remove-default-ispell(8)"
name: "remove-default-ispell"
section: "8"
letter: "r"
url: "/docs/linux/man/8-remove-default-ispell/"
---

remove-default-ispell - remove default ispell dictionary

<h2>Synopsis</h2>

<pre> remove-default-ispell &lt;package&gt;</pre>

<h2>Description</h2>

<font SIZE="-1">WARNING:</font> Not to be used from the command line unless you know very well what you are doing. 

 When called from package postrm, this program will take care of removing the entries associated to a ispell package from the dictionaries-common database and call for the new selection if it was the default one.

<h2>See Also</h2>

The dictionaries-common policy document

<h2>Authors</h2>

Rafael Laboissiere
