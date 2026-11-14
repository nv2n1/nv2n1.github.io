---
title: "alter_language(7)"
name: "alter_language"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_language/"
description: "ALTER LANGUAGE – change the definition of a procedural language"
---

<p>ALTER LANGUAGE &#8211; change the definition of a procedural language </p>
<h2>Synopsis</h2>
<pre>ALTER [ PROCEDURAL ] LANGUAGE <i>name</i> RENAME TO <i>newname</i>
ALTER [ PROCEDURAL ] LANGUAGE <i>name</i> OWNER TO <i>new_owner</i></pre>
<h2>Description</h2>
<p><code>ALTER LANGUAGE</code> changes the definition of a procedural language. The only functionality is to rename the language or assign a new owner. You must be superuser or owner of the language to use <code>ALTER LANGUAGE</code>.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>Name of a language</p>
<dt><i>newname</i></p>
<dd>The new name of the language</p>
<dt><i>new_owner</i></p>
<dd>The new owner of the language</dl>
<h2>Compatibility</h2>
<p>There is no <code>ALTER LANGUAGE</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>CREATE LANGUAGE [<code><a href="/docs/linux/man/7-create_language/">create_language</a></code>(7)], DROP LANGUAGE [<code><a href="/docs/linux/man/7-drop_language/">drop_language</a></code>(7)] </p>
