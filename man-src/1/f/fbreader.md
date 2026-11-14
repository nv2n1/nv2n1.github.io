---
title: "fbreader(1)"
name: "fbreader"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fbreader/"
description: "FBReader – e-book reader"
---

<p>FBReader &#8211; e-book reader </p>
<h2>Synopsis</h2>
<p><code>FBReader [-zlui </code><i>ui-type</i>] [<i>ui-specific options</i>] [<code>-lang </code><i>language</i>] [<i>e-book</i>]</p>
<h2>Description</h2>
<p>FBReader is an e-book reader. It supports most open e-book formats, and can read compressed e-book archives. </p>
<p> For more information on using the program, see the &quot;About FBReader&quot; button on its toolbar.</p>
<h2>Options</h2>
<dl>
<dt><code>-zlui </code><i>ui-type</i></p>
<dd>Try to start FBReader with the specified uu type. Supported ui types are <code>gtk</code> (to use Gtk+ library), <code>qt</code> (Qt 3 library) and <code>qt4</code> (Qt 4 library).</p>
<dt><i>ui-specific options</i></p>
<dd>Standard options from the UI library you use (Gtk+, Qt3 or Qt4).</p>
<dt><code>-lang </code><i>language</i></p>
<dd>Language for user interface. Current version (0.12.0) of fbreader supports Arabic (specify <code>-lang ar</code> option), Chinese (<code>-lang zh</code>), Czech (<code>-lang cs</code>), Dutch (<code>-lang nl</code>), English (<code>-lang en</code>), Finnish (<code>-lang fi</code>), French (<code>-lang fr</code>), German (<code>-lang de</code>), Hungarian (<code>-lang hu</code>), Indonesian (<code>-lang id</code>), Italian (<code>-lang it</code>), Lithuanian (<code>-lang lt</code>), Russian (<code>-lang ru</code>), Spanish (<code>-lang es</code>) and Swedish (<code>-lang sv</code>) and Ukrainian (<code>-lang uk</code>).</p>
<dt><i>e-book</i></p>
<dd>Name of file to open. If this parameter is missing or if FBReader cannot open the specified file, the last opened file will be reopened. If you start FBReader for the first time or the last opened file is missing, &quot;About FBReader&quot; text will be opened.</dl>
<h2>Author</h2>
<p>This man page was written by Joey Hess &lt;joeyh [at] debian.org&gt; and Nikolay Pultsin &lt;geometer [at] fbreader.org&gt; for the Debian system, but may be freely reused on other systems.</p>
