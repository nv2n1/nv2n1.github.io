---
title: "american-english(5)"
name: "american-english"
section: "5"
letter: "a"
url: "/docs/linux/man/5-american-english/"
description: "american-english – a list of English words"
---

<p>american-english &#8211; a list of English words</p>
<h2>Description</h2>
<p><code>/usr/share/dict/american-english</code> is an ASCII file which contains an alphabetic list of words, one per line.</p>
<h2>Files</h2>
<p>There may be any number of word lists in /usr/share/dict/. <i>/etc/dictionaries-common/words</i> is a symbolic link to the currently-chosen <i>/usr/share/dict/&lt;language&gt;</i> file. <i>/usr/share/dict/words</i> is a symbolic link to <i>/etc/dictionaries-common/words</i>, and is the name by which other software should refer to the system word list. See <code><a href="/docs/linux/man/8-select-default-wordlist/">select-default-wordlist</a></code>(8) for more information, and/or to change the currently-chosen word list. </p>
<p> The directory <i>/usr/share/dict</i> can contain word lists for many languages, with name of the language in English, e.g., <i>/usr/share/dict/french</i> and <i>/usr/share/dict/danish</i> contain respectively lists of French and Danish words if they exist. Such lists should be coded using the ISO 8859-1 character set encoding.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ispell/">ispell</a></code>(1), <code><a href="/docs/linux/man/8-select-default-wordlist/">select-default-wordlist</a></code>(8), and the <i>Filesystem Hierarchy</i> <i>Standard</i>.</p>
<h2>History</h2>
<p>The words lists are not specific, and may be generated from any number of sources. </p>
<p> The system word list used to be <i>/usr/dict/words</i>. For compatibility, software should check that location if <i>/usr/share/dict/words</i> does not exist.</p>
<h2>Author</h2>
<p>Word lists are collected and maintained by various authors. The Debian English word lists are built from the SCOWL (Spell- Checker Oriented Word Lists) package, whose upstream editor is Kevin Atkinson &lt;kevina [at] users.sourceforge.net&gt;.</p>
