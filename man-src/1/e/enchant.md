---
title: "enchant(1)"
name: "enchant"
section: "1"
letter: "e"
url: "/docs/linux/man/1-enchant/"
description: "Enchant – a spellchecker"
---

<h2 class="name">NAME</h2>
<p> Enchant &#8211; a spellchecker </p>
<h2>SYNOPSIS</h2>
<p> <code>enchant</code> [<code>-a</code>] [<code>-d dict</code>] [<code>-h</code>] [<code>-l</code>] [<code>-L</code>] [<code>-v</code>] </p>
<h2>DESCRIPTION</h2>
<p> <code>Enchant</code> is an ispell-compatible spellchecker.</p>
<h3>OPTIONS</h3>
<dl>
<dt><code>-a</code></p>
<dd> List suggestions in ispell pipe mode format.</p>
<dt><code>-d dict</code></p>
<dd> Use dictionary &lt;dict&gt;.</p>
<dt><code>-h</code></p>
<dd> Show short help.</p>
<dt><code>-l</code></p>
<dd> List only the misspellings.</p>
<dt><code>-L</code></p>
<dd> Include the line number in the output.</p>
<dt><code>-v</code></p>
<dd> Prints the program&#8217;s version.</dl>
<h2>ENCHANT ORDERING FILE</h2>
<p> Enchant has a global and a per-user ordering file named <i>enchant.ordering</i>. It lets the user specify which spelling backend to use for individual languages in the case when you care which backend gets used. The global file is located in <i>$(datadir)/enchant</i> and the per-user file is located in <i>~/.enchant</i>. The per-user file takes precedence, if found. </p>
<p> The ordering file takes the form language_tag:&lt;comma-separated list of spelling backends&gt;. I am currently aware of the following backends: aspell, myspell, ispell, uspell, hspell, voikko, and zemberek. &#8216;*&#8217; is used to mean &quot;use this ordering for all languages, unless instructed otherwise.&quot; For example: </p>
<p> *:aspell,myspell,ispell<br />
 en:aspell,myspell,ispell<br />
 en_UK:myspell,aspell,ispell<br />
 fr:myspell,ispell:aspell</p>
<h2>DIRECTORIES IMPORTANT TO ENCHANT</h2>
<p> Unless configured otherwise, Enchant&#8217;s Myspell, Ispell, and Uspell backends will look for dictionaries in directories specific to Enchant, and will not use your system-wide installed dictionaries. This is for pragmatic reasons since many distributions install these dictionaries into different locations. </p>
<p> Like the <i>enchant.ordering</i> file described above, Enchant looks in the global directory for these dictionaries and a per-user directory. The per-user directory takes precedence if it is found. Enchant looks for Myspell dictionaries in <i>$(datadir)/enchant/myspell</i> and <i>~/.enchant/myspell</i>. Enchant looks for Ispell dictionaries in <i>$(datadir)/enchant/ispell</i> and <i>~/.enchant/ispell</i>. Enchant looks for Uspell dictionaries in <i>$(datadir)/enchant/uspell</i> and <i>~/.enchant/uspell</i>. </p>
<p> Packagers and users may wish to make symbolic links to the system-wide dictionary directories. Or, preferably, use the &#8211;with-myspell-dir, &#8211;with-ispell-dir, and &#8211;with-uspell-dir &#8216;configure&#8217; arguments.</p>
<h2>MORE INFORMATION</h2>
<p> <a rel="nofollow" href="http://www.abisource.com/enchant/">http://www.abisource.com/enchant/</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-aspell/">aspell</a>(1),</code> <code><a href="/docs/linux/man/1-ispell/">ispell</a>(1),</code></p>
<h2>AUTHOR</h2>
<p>&nbsp;Dom Lachowicz<br />
&nbsp;WEB:&nbsp;<a rel="nofollow" href="http://www.abisource.com/enchant/">http://www.abisource.com/enchant/</a><br />
&nbsp;MAIL: domlachowicz [at] gmail.com </p>
<h2>Index</h2>
