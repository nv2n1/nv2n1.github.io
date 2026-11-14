---
title: "aspell(1)"
name: "aspell"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aspell/"
description: "aspell – interactive spell checker"
---

<h2 class="name">NAME</h2>
<p> aspell &#8211; interactive spell checker </p>
<h2>SYNOPSIS</h2>
<p> <code>aspell</code> <i>[options] &lt;command&gt;</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>aspell</code> is a utility program that connects to the Aspell library so that it can function as an <code>ispell -a</code> replacement, as an independent spell checker, as a test utility to test out Aspell library features, and as a utility for managing dictionaries used by the library. </p>
<p> The Aspell library contains an interface allowing other programs direct access to its functions and therefore reducing the complex task of spell checking to simple library calls. The default library does not contain dictionary word lists. To add language dictionaries, please check your distro first for modified dictionaries, otherwise look here for base language dictionaries &lt;<a rel="nofollow" href="http://aspell.net">http://aspell.net</a>&gt;. </p>
<p> The following information describes the commands and options used by the Aspell Utility. </p>
<p> This manual page is maintained separately from the official documentation so it may be out of date or incomplete. The official documentation is maintained as a Texinfo manual. See the `<code>aspell</code>&#8216; entry in <code>info</code> for more complete documentation.</p>
<h2>COMMANDS</h2>
<p> <i>&lt;command&gt;</i> is one of:</p>
<dl>
<dt><code>usage</code>, <code>-?</code></p>
<dd> Send a brief Aspell Utility usage message to standard output. This is a short summary listing more common spell-check commands and options.</p>
<dt><code>help</code></p>
<dd> Send a detailed Aspell Utility help message to standard output. This is a complete list showing all commands, options, filters and dictionaries.</p>
<dt><code>version</code>, <code>-v</code></p>
<dd> Print version number of Aspell Library and Utility to standard output.</p>
<dt><code>check</code> <i>&lt;file&gt;</i>, <code>-c</code> <i>&lt;file&gt;</i></p>
<dd> Spell-check a single file.</p>
<dt><code>pipe</code>, <code>-a</code></p>
<dd> Run Aspell in <i>ispell -a</i> compatibility mode.</p>
<dt><code>list</code></p>
<dd> Produce a list of misspelled words from standard input.</p>
<dt>[<code>dump</code>] <code>config</code></p>
<dd> Dump all current configuration options to standard output.</p>
<dt><code>config </code><i>&lt;key&gt;</i></p>
<dd> Send the current value of <i>&lt;key&gt;</i> to standard output.</p>
<dt><code>soundslike</code></p>
<dd> Output the soundslike equivalent of each word entered.</p>
<dt><code>munch</code></p>
<dd> Generate possible root words and affixes from an input list of words.</p>
<dt><code>expand</code> [<code>1-4</code>]</p>
<dd> Expands the affix flags of each affix compressed word entered.</p>
<dt><code>clean</code> [<code>strict</code>]</p>
<dd> Cleans an input word list so that every line is a valid word.</p>
<dt><code>munch-list</code> [<code>simple</code>] [<code>single</code>|<code>multi</code>] [<code>keep</code>]</p>
<dd> Reduce the size of a word list via affix compression.</p>
<dt><code>conv</code> <i>&lt;from&gt; &lt;to&gt;</i> [<i>&lt;norm-form&gt;</i>]</p>
<dd> Converts <i>&lt;from&gt;</i> one encoding <i>&lt;to&gt;</i> another.</p>
<dt><code>norm</code> (<i>&lt;norm-map&gt;</i>|<i>&lt;from&gt; &lt;norm-map&gt; &lt;to&gt;</i>) [<i>&lt;norm-form&gt;</i>]</p>
<dd> Perform Unicode normalization.</p>
<dt>[<code>dump</code>] <code>dicts</code>|<code>filters</code>|<code>modes</code></p>
<dd> Lists available dictionaries, filters, or modes.</p>
<dt><code>dump</code>|<code>create</code>|<code>merge master</code>|<code>personal</code>|<code>repl</code> <i>&lt;wordlist&gt;</i></p>
<dd> dump, create, or merge a master, personal, or replacement word list.</dl>
<h2>DICTIONARY OPTIONS</h2>
<p> The following options may be used to control which dictionaries to use and how they behave.</p>
<dl>
<dt><code>&#8211;master=</code><i>&lt;name&gt;</i>, <code>-d</code> <i>&lt;name&gt;</i></p>
<dd> Base name of the dictionary to use. If this option is specified then Aspell will either use this dictionary or die.</p>
<dt><code>&#8211;dict-dir=</code><i>&lt;directory&gt;</i></p>
<dd> Location of the main dictionary word list.</p>
<dt><code>&#8211;lang=</code><i>&lt;string&gt;</i>, <code>-l</code> <i>&lt;string&gt;</i></p>
<dd> Language to use. It follows the same format of the LANG environmental variable on most systems. It consists of the two letter ISO 639 language code and an optional two letter ISO 3166 country code after a dash or underscore. The default value is based on the value of the LC_MESSAGES locale.</p>
<dt><code>&#8211;size=</code><i>&lt;string&gt;</i></p>
<dd> The preferred size of the dictionary word list. This consists of a two char digit code describing the size of the list, with typical values of: 10=tiny, 20=really small, 30=small, 40=med-small, 50=med, 60=med-large, 70=large, 80=huge, 90=insane.</p>
<dt><code>&#8211;variety=</code><i>&lt;string&gt;</i></p>
<dd> Any extra information to distinguish this variety of dictionary from other dictionaries which may have the same <i>lang</i> and <i>size</i>.</p>
<dt><code>&#8211;jargon=</code><i>&lt;string&gt;</i></p>
<dd> Please use the <i>variety</i> option since it replaces <i>jargon</i> as a better choice. <i>jargon</i> will be removed in the future.</p>
<dt><code>&#8211;word-list-path=</code><i>&lt;list of directories&gt;</i></p>
<dd> Search path for word list information files.</p>
<dt><code>&#8211;personal=</code><i>&lt;file&gt;</i>, <code>-p</code> <i>&lt;file&gt;</i></p>
<dd> Personal word list file name.</p>
<dt><code>&#8211;repl=</code><i>&lt;file&gt;</i></p>
<dd> Replacements list file name.</p>
<dt><code>&#8211;extra-dicts=</code><i>&lt;list&gt;</i></p>
<dd> Extra dictionaries to use.</p>
<dt><code>&#8211;ignore-accents</code></p>
<dd> This option is not yet implemented.</dl>
<h2>CHECKER OPTIONS</h2>
<p> These options control the behavior of Aspell when checking documents.</p>
<dl>
<dt><code>&#8211;ignore=</code><i>&lt;integer&gt;</i>, <code>-W</code> <i>&lt;integer&gt;</i></p>
<dd> Ignore words &lt;= <i>&lt;integer&gt;</i> characters in length.</p>
<dt><code>&#8211;ignore-case</code>, <code>&#8211;dont-ignore-case</code></p>
<dd> Ignore case when checking words.</p>
<dt><code>&#8211;ignore-repl</code>, <code>&#8211;dont-ignore-repl</code></p>
<dd> Ignore commands to store replacement pairs.</p>
<dt><code>&#8211;save-repl</code>, <code>&#8211;dont-save-repl</code></p>
<dd> Save the replacement word list on save all.</p>
<dt><code>&#8211;sug-mode=</code><i>&lt;mode&gt;</i></p>
<dd> Suggestion <i>&lt;mode&gt;</i> = <code>ultra</code>|<code>fast</code>|<code>normal</code>|<code>bad-spellers</code></dl>
<h2>FILTER OPTIONS</h2>
<p> These options modify the behavior of the various filters.</p>
<dl>
<dt><code>&#8211;add-filter=</code><i>&lt;list&gt;</i>, <code>&#8211;rem-filter=</code><i>&lt;list&gt;</i></p>
<dd> Add or remove a filter.</p>
<dt><code>&#8211;add-filter-path=</code><i>&lt;paths&gt;</i>, <code>&#8211;rem-filter-path=</code><i>&lt;paths&gt;</i></p>
<dd> Add or remove paths searched for filters.</p>
<dt><code>&#8211;mode=</code><i>&lt;string&gt;</i>, <code>-e</code>, <code>-H</code>, <code>-t</code>, <code>-n</code></p>
<dd> Sets the filter mode. <i>Mode</i> is one of none, url, email, html, tex or nroff. The alternative shortcut options are &#8216;-e&#8217; for email, &#8216;-H&#8217; for Html/Sgml, &#8216;-t&#8217; for Tex or &#8216;-n&#8217; for Nroff.</p>
<dt><code>&#8211;encoding=</code><i>&lt;string&gt;</i></p>
<dd> encoding the document is expected to be in. The default depends on the current locale.</p>
<dt><code>&#8211;add-email-quote=</code><i>&lt;list&gt;</i>, <code>&#8211;rem-email-quote=</code><i>&lt;list&gt;</i></p>
<dd> Add or Remove a list of email quote characters.</p>
<dt><code>&#8211;email-margin=</code><i>&lt;integer&gt;</i></p>
<dd> Number of chars that can appear before the quote char.</p>
<dt><code>&#8211;add-html-check=</code><i>&lt;list&gt;</i>, <code>&#8211;rem-html-check=</code><i>&lt;list&gt;</i></p>
<dd> Add or remove a list of HTML attributes to always check. For example, look inside alt= tags.</p>
<dt><code>&#8211;add-html-skip=</code><i>&lt;list&gt;</i>, <code>&#8211;rem-html-skip=</code><i>&lt;list&gt;</i></p>
<dd> Add or remove a list of HTML attributes to always skip while spell checking.</p>
<dt><code>&#8211;add-sgml-check=</code><i>&lt;list&gt;</i>, <code>&#8211;rem-sgml-check=</code><i>&lt;list&gt;</i></p>
<dd> Add or remove a list of SGML attributes to always check for spelling.</p>
<dt><code>&#8211;add-sgml-skip=</code><i>&lt;list&gt;</i>, <code>&#8211;rem-sgml-skip=</code><i>&lt;list&gt;</i></p>
<dd> Add or remove a list of SGML attributes to always skip while spell checking.</p>
<dt><code>&#8211;sgml-extension=</code><i>&lt;list&gt;</i></p>
<dd> SGML file extensions.</p>
<dt><code>&#8211;tex-check-comments</code>, <code>&#8211;dont-tex-check-comments</code></p>
<dd> Check TeX comments.</p>
<dt><code>&#8211;add-tex-command=</code><i>&lt;list&gt;</i>, <code>&#8211;rem-tex-command=</code><i>&lt;list&gt;</i></p>
<dd> Add or Remove a list of TeX commands.</dl>
<h2>RUN-TOGETHER WORD OPTIONS</h2>
<p> These may be used to control the behavior of run-together words.</p>
<dl>
<dt><code>&#8211;run-together</code>, <code>&#8211;dont-run-together</code>, <code>-C</code>, <code>-B</code></p>
<dd> Consider run-together words valid.</p>
<dt><code>&#8211;run-together-limit=</code><i>&lt;integer&gt;</i></p>
<dd> Maximum number of words that can be strung together.</p>
<dt><code>&#8211;run-together-min=</code><i>&lt;integer&gt;</i></p>
<dd> Minimal length of interior words.</dl>
<h2>MISC OPTIONS</h2>
<p> Miscellaneous options that don&#8217;t fall under any other category.</p>
<dl>
<dt><code>&#8211;conf=</code><i>&lt;file name&gt;</i></p>
<dd> Main configuration file. This file overrides Aspell&#8217;s global defaults.</p>
<dt><code>&#8211;conf-dir=</code><i>&lt;directory&gt;</i></p>
<dd> Location of main configuration file.</p>
<dt><code>&#8211;data-dir=</code><i>&lt;directory&gt;</i></p>
<dd> Location of language data files.</p>
<dt><code>&#8211;keyboard=</code><i>&lt;keyboard&gt;</i></p>
<dd> Use this keyboard layout for suggesting possible words. These spelling errors happen if a user accidentally presses a key next to the intended correct key.</p>
<dt><code>&#8211;local-data-dir=</code><i>&lt;directory&gt;</i></p>
<dd> Alternative location of language data files. This directory is searched before data-dir.</p>
<dt><code>&#8211;home-dir=</code><i>&lt;directory&gt;</i></p>
<dd> Directory Location for personal wordlist files.</p>
<dt><code>&#8211;per-conf=</code><i>&lt;file name&gt;</i></p>
<dd> Personal configuration file. This file overrides options found in the global config file.</dl>
<h2>ASPELL UTILITY OPTIONS</h2>
<p> These options are part of the <i>aspell</i> Utility and work independently of the library.</p>
<dl>
<dt><code>&#8211;backup</code>, <code>&#8211;dont-backup</code>, <code>-b</code>, <code>-x</code></p>
<dd> The aspell utility creates a backup file by making a copy and appending <i>.bak</i> to file name. This only applies when the command is <i>check &lt;file&gt;</i> and the backup file is only created if any spelling modifications take place.</p>
<dt><code>&#8211;byte-offsets</code>, <code>&#8211;dont-byte-offsets</code></p>
<dd> Use byte offsets instead of character offsets.</p>
<dt><code>&#8211;guess</code>, <code>&#8211;dont-guess</code>, <code>-m</code>, <code>-P</code></p>
<dd> Create missing root/affix combinations not in the dictionary in <code>pipe</code> mode.</p>
<dt><code>&#8211;keymapping=aspell</code>, <code>&#8211;keymapping=ispell</code></p>
<dd> The keymapping to use, either <i>aspell</i> for the default mapping or <i>ispell</i> to use the same mapping that the Ispell utility uses.</p>
<dt><code>&#8211;reverse</code>, <code>&#8211;dont-reverse</code></p>
<dd> Reverse the order of the suggestions list in pipe mode.</p>
<dt><code>&#8211;suggest</code>, <code>&#8211;dont-suggest</code></p>
<dd> Suggest possible replacements in pipe mode. If false, Aspell will simply report the misspelling and make no attempt at suggestions or possible corrections.</p>
<dt><code>&#8211;time</code>, <code>&#8211;dont-time</code></p>
<dd> Time the load time and suggest a time in pipe mode.</dl>
<p> In addition Aspell will try to make sense out of Ispell&#8217;s command line options so that it can function as a drop in replacement for Ispell. If Aspell is run without any command line options it will display a brief help screen and quit.</p>
<h2>CONFIGURATION</h2>
<p> Aspell can accept options via global or personal configuration files so that you do not need to specify them each time at the command line. The default global configuration file is <i>/etc/aspell.conf</i> or another file specified by option <i>&#8211;conf</i> and is checked first. The default per user configuration file <i>~/.aspell.conf</i> located in the <code>$HOME</code> directory (or another file specified by option <i>&#8211;per-conf</i>) is checked next and overrides options set in the global config file. Options specified at either the command line or via an environmental variable override those specified by either configuration file. </p>
<p> Each line of the configuration file has the format: </p>
<dl>
<dt>
<dd> <code>option</code> <i>[value]</i></dl>
<p> where <code>option</code> is any one of the standard library options above without the leading dashes. For example the following line will set the default language to Swiss German: </p>
<dl>
<dt>
<dd> <code>lang de_CH</code></dl>
<p> There may be any number of spaces between the option and the value, however it can only be spaces, i.e. there is no &#8216;=&#8217; between the option name and the value. Comments may also be included by preceding them with a &#8216;#&#8217; as anything from a &#8216;#&#8217; to a newline is ignored. Blank lines are also allowed. The <i>/etc/aspell.conf</i> file is a good example of how to set these options and the Aspell Manual has more detailed info.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-aspell-import/">aspell-import</a></code>(1), <code><a href="/docs/linux/man/1-prezip-bin/">prezip-bin</a></code>(1), <code><a href="/docs/linux/man/1-run-with-aspell/">run-with-aspell</a></code>(1), <code><a href="/docs/linux/man/1-word-list-compress/">word-list-compress</a></code>(1) </p>
<p> Aspell is fully documented in its Texinfo manual. See the `<code>aspell</code>&#8216; entry in <code>info</code> for more complete documentation.</p>
<h2>SUPPORT</h2>
<p> Support for Aspell can be found on the Aspell mailing lists. Instructions for joining the various mailing lists (and an archive of them) can be found off the Aspell home page at &lt;<a rel="nofollow" href="http://aspell.net">http://aspell.net</a>&gt;. Bug reports should be submitted via GitHub Issues rather than being posted to the mailing lists.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Brian Nelson &lt;pyro [at] debian.org&gt; based on the Aspell User&#8217;s Manual, Copyright &#169; 2002 Kevin Atkinson. Updated Nov 2006 by Jose Da Silva &lt;digital [at] joescat.com&gt;, and Dec 2006 by Kevin Atkinson &lt;kevina [at] gnu.org&gt;. </p>
<h2>Index</h2>
