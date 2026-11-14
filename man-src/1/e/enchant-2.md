---
title: "enchant-2(1)"
name: "enchant-2"
section: "1"
letter: "e"
url: "/docs/linux/man/1-enchant-2/"
description: "Enchant – a spellchecker"
---

<h2 class="name">NAME</h2>
<p> Enchant &#8211; a spellchecker </p>
<h2>SYNOPSIS</h2>
<p> <code>enchant-2</code> <code>-a</code>|<code>-l</code>|<code>-h</code>|<code>-v</code> [<code>-L</code>] [<code>-d</code> <i>DICTIONARY</i>] [<i>FILE</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>Enchant</code> is an ispell-compatible spellchecker.</p>
<dl>
<dt><code>-d </code><i>DICTIONARY</i></p>
<dd> use the given dictionary</p>
<dt><code>-p </code><i>WORDLIST</i></p>
<dd> use the given personal wordlist</p>
<dt><code>-a</code></p>
<dd> list suggestions in ispell pipe mode format</p>
<dt><code>-l</code></p>
<dd> list only the misspellings</p>
<dt><code>-L</code></p>
<dd> display line numbers</p>
<dt><code>-h</code></p>
<dd> display help and exit</p>
<dt><code>-v</code></p>
<dd> display version information and exit</dl>
<h2>ENCHANT ORDERING FILE</h2>
<p> Enchant uses global and per-user ordering files named <i>enchant.ordering</i> to decide which spelling provider to use for particular languages. The per-user file takes precedence. </p>
<p> The ordering file takes the form <i>language_tag:&lt;comma-separated list of spelling providers&gt;</i>. The language tag is an IETF BCP 47 language tag, typically of the form <i>COUNTRY_LANGUAGE</i>. To see what dictionaries are available, run <i>enchant-lsmod-2</i>. &#8216;*&#8217; is used to mean &quot;use this ordering for all languages, unless instructed otherwise.&quot; For example: </p>
<p> *:aspell,hunspell,nuspell<br />
 en:aspell,hunspell,nuspell<br />
 en_GB:hunspell,nuspell,aspell<br />
 fr:hunspell,nuspell,aspell</p>
<h2>FILES AND DIRECTORIES</h2>
<p> Enchant looks in the following places for files, in decreasing order of precedence:</p>
<dl>
<dt><i>ENCHANT_CONFIG_DIR</i></p>
<dd> (If the environment variable is set.)</p>
<dt><i>XDG_CONFIG_HOME/enchant</i> (non-Windows systems)</p>
<dd> Default: <i>~/.config/enchant</i></p>
<dt><i>CSIDL_LOCAL_APPDATAnchant</i> (Windows systems)</p>
<dd> Default: <i>C:\Documents and Settings\</i>username<i>\Local Settings\Application Datanchant</p>
<dt>/usr/share/enchant</i></p>
<dd> (Or the equivalent location relative to the enchant library for a relocatable build.)</dl>
<p> Dictionaries are looked for in a subdirectory with the same name as the provider; for example, <i>/usr/share/enchant/hunspell</i> and <i>~/.config/enchant/hunspell</i>. </p>
<p> Some providers may also look in a standard system directory for their dictionaries; the hunspell provider can be configured to do so at build time.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-aspell/">aspell</a></code>(1), <code><a href="/docs/linux/man/1-enchant-lsmod-2/">enchant-lsmod-2</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Written by Dom Lachowicz and Reuben Thomas. </p>
<h2>Index</h2>
