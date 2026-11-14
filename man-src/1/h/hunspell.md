---
title: "hunspell(1)"
name: "hunspell"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hunspell/"
description: "hunspell – spell checker, stemmer and morphological analyzer"
---

<h2 class="name">NAME</h2>
<p> hunspell &#8211; spell checker, stemmer and morphological analyzer </p>
<h2>SYNOPSIS</h2>
<p> hunspell [-1aDGHhLlmnrstvw] [&#8211;check-url] [-d dict[,dict2,&#8230;]] [&#8211;help] [-i enc] [-p dict] [-vv] [&#8211;version] [file(s)]</p>
<h2>DESCRIPTION</h2>
<p> <i>Hunspell</i> is fashioned after the <i>Ispell</i> program. The most common usage is &quot;hunspell&quot; or &quot;hunspell filename&quot;. Without filename parameter, hunspell checks the standard input. Typing &quot;cat&quot; and &quot;exsample&quot; in two input lines, we got an asterisk (it means &quot;cat&quot; is a correct word) and a line with corrections: </p>
<dl>
<dt>
<dd>
<pre>
$ hunspell -d en_US
Hunspell 1.2.3
*
&amp; exsample 4 0: example, examples, ex sample, ex-sample
</pre>
</dl>
<p> Correct words signed with an &#8216;*&#8217;, &#8216;+&#8217; or &#8216;-&#8216;, unrecognized words signed with &#8216;#&#8217; or &#8216;&amp;&#8217; in output lines (see later). (Close the standard input with Ctrl-d on Unix/Linux and Ctrl-Z Enter or Ctrl-C on Windows.) </p>
<p> With filename parameters, <i>hunspell</i> will display each word of the files which does not appear in the dictionary at the top of the screen and allow you to change it. If there are &quot;near misses&quot; in the dictionary, then they are also displayed on following lines. Finally, the line containing the word and the previous line are printed at the bottom of the screen. If your terminal can display in reverse video, the word itself is highlighted. You have the option of replacing the word completely, or choosing one of the suggested words. Commands are single characters as follows (case is ignored): </p>
<dl>
<dt>
<dd>
<dl>
<dt>R</p>
<dd> Replace the misspelled word completely.</p>
<dt>Space</p>
<dd> Accept the word this time only.</p>
<dt>A</p>
<dd> Accept the word for the rest of this <i>hunspell</i> session.</p>
<dt>I</p>
<dd> Accept the word, capitalized as it is in the file, and update private dictionary.</p>
<dt>U</p>
<dd> Accept the word, and add an uncapitalized (actually, all lower-case) version to the private dictionary.</p>
<dt>S</p>
<dd> Ask a stem and a model word and store them in the private dictionary. The stem will be accepted also with the affixes of the model word.</p>
<dt>0-<i>n</i></p>
<dd> Replace with one of the suggested words.</p>
<dt>X</p>
<dd> Write the rest of this file, ignoring misspellings, and start next file.</p>
<dt>Q</p>
<dd> Exit immediately and leave the file unchanged.</p>
<dt>^Z</p>
<dd> Suspend hunspell.</p>
<dt>?</p>
<dd> Give help screen.</dl>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-1</code></p>
<dd> Check only first field in lines (delimiter = tabulator).</p>
<dt><code>-a</code></p>
<dd> The <code>-a</code> option is intended to be used from other programs through a pipe. In this mode, <i>hunspell</i> prints a one-line version identification message, and then begins reading lines of input. For each input line, a single line is written to the standard output for each word checked for spelling on the line. If the word was found in the main dictionary, or your personal dictionary, then the line contains only a &#8216;*&#8217;. If the word was found through affix removal, then the line contains a &#8216;+&#8217;, a space, and the root word. If the word was found through compound formation (concatenation of two words, then the line contains only a &#8216;-&#8216;.</p>
<dt>
<dd> If the word is not in the dictionary, but there are near misses, then the line contains an &#8216;&amp;&#8217;, a space, the misspelled word, a space, the number of near misses, the number of characters between the beginning of the line and the beginning of the misspelled word, a colon, another space, and a list of the near misses separated by commas and spaces.</p>
<dt>
<dd> Also, each near miss or guess is capitalized the same as the input word unless such capitalization is illegal; in the latter case each near miss is capitalized correctly according to the dictionary.</p>
<dt>
<dd> Finally, if the word does not appear in the dictionary, and there are no near misses, then the line contains a &#8216;#&#8217;, a space, the misspelled word, a space, and the character offset from the beginning of the line. Each sentence of text input is terminated with an additional blank line, indicating that <i>hunspell</i> has completed processing the input line.</p>
<dt>
<dd> These output lines can be summarized as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>OK:</p>
<dd> *</p>
<dt>Root:</p>
<dd> + &lt;root&gt;</p>
<dt>Compound:</p>
<dd> &#8211;</p>
<dt>Miss:</p>
<dd> &amp; &lt;original&gt; &lt;count&gt; &lt;offset&gt;: &lt;miss&gt;, &lt;miss&gt;, &#8230;</p>
<dt>None:</p>
<dd> # &lt;original&gt; &lt;offset&gt;</dl>
</dl>
<dt>
<dd> For example, a dummy dictionary containing the words &quot;fray&quot;, &quot;Frey&quot;, &quot;fry&quot;, and &quot;refried&quot; might produce the following response to the command &quot;echo &#8216;frqy refries | hunspell -a&quot;:</p>
<dl>
<dt>
<dd>
<pre>
(#) Hunspell 0.4.1 (beta), 2005-05-26
&amp; frqy 3 0: fray, Frey, fry
&amp; refries 1 5: refried
</pre>
</dl>
<dt>
<dd> This mode is also suitable for interactive use when you want to figure out the spelling of a single word (but this is the default behavior of hunspell without -a, too).</p>
<dt>
<dd> When in the <code>-a</code> mode, <i>hunspell</i> will also accept lines of single words prefixed with any of &#8216;*&#8217;, &#8216;&amp;&#8217;, &#8216;@&#8217;, &#8216;+&#8217;, &#8216;-&#8216;, &#8216;~&#8217;, &#8216;#&#8217;, &#8216;!&#8217;, &#8216;%&#8217;, &#8216;`&#8217;, or &#8216;^&#8217;. A line starting with &#8216;*&#8217; tells <i>hunspell</i> to insert the word into the user&#8217;s dictionary (similar to the I command). A line starting with &#8216;&amp;&#8217; tells <i>hunspell</i> to insert an all-lowercase version of the word into the user&#8217;s dictionary (similar to the U command). A line starting with &#8216;@&#8217; causes <i>hunspell</i> to accept this word in the future (similar to the A command). A line starting with &#8216;+&#8217;, followed immediately by <code>tex</code> or <code>nroff</code> will cause <i>hunspell</i> to parse future input according the syntax of that formatter. A line consisting solely of a &#8216;+&#8217; will place <i>hunspell</i> in TeX/LaTeX mode (similar to the <code>-t</code> option) and &#8216;-&#8216; returns <i>hunspell</i> to nroff/troff mode (but these commands are obsolete). However, the string character type is <i>not</i> changed; the &#8216;~&#8217; command must be used to do this. A line starting with &#8216;~&#8217; causes <i>hunspell</i> to set internal parameters (in particular, the default string character type) based on the filename given in the rest of the line. (A file suffix is sufficient, but the period must be included. Instead of a file name or suffix, a unique name, as listed in the language affix file, may be specified.) However, the formatter parsing is <i>not</i> changed; the &#8216;+&#8217; command must be used to change the formatter. A line prefixed with &#8216;#&#8217; will cause the personal dictionary to be saved. A line prefixed with &#8216;!&#8217; will turn on <i>terse</i> mode (see below), and a line prefixed with &#8216;%&#8217; will return <i>hunspell</i> to normal (non-terse) mode. A line prefixed with &#8216;`&#8217; will turn on verbose-correction mode (see below); this mode can only be disabled by turning on terse mode with &#8216;%&#8217;.</p>
<dt>
<dd> Any input following the prefix characters &#8216;+&#8217;, &#8216;-&#8216;, &#8216;#&#8217;, &#8216;!&#8217;, &#8216;%&#8217;, or &#8216;`&#8217; is ignored, as is any input following the filename on a &#8216;~&#8217; line. To allow spell-checking of lines beginning with these characters, a line starting with &#8216;^&#8217; has that character removed before it is passed to the spell-checking code. It is recommended that programmatic interfaces prefix every data line with an uparrow to protect themselves against future changes in <i>hunspell</i>.</p>
<dt>
<dd> To summarize these:</p>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> Add to personal dictionary</p>
<dt>@</p>
<dd> Accept word, but leave out of dictionary</p>
<dt>#</p>
<dd> Save current personal dictionary</p>
<dt>~</p>
<dd> Set parameters based on filename</p>
<dt>+</p>
<dd> Enter TeX mode</p>
<dt>&#8211;</p>
<dd> Exit TeX mode</p>
<dt>!</p>
<dd> Enter terse mode</p>
<dt>%</p>
<dd> Exit terse mode</p>
<dt>`</p>
<dd> Enter verbose-correction mode</p>
<dt>^</p>
<dd> Spell-check rest of line</dl>
</dl>
<dt>
<dd> In <i>terse</i> mode, <i>hunspell</i> will not print lines beginning with &#8216;*&#8217;, &#8216;+&#8217;, or &#8216;-&#8216;, all of which indicate correct words. This significantly improves running speed when the driving program is going to ignore correct words anyway.</p>
<dt>
<dd> In <i>verbose-correction</i> mode, <i>hunspell</i> includes the original word immediately after the indicator character in output lines beginning with &#8216;*&#8217;, &#8216;+&#8217;, and &#8216;-&#8216;, which simplifies interaction for some programs. </p>
<dt><code>&#8211;check-url</code></p>
<dd> Check URLs, e-mail addresses and directory paths. </p>
<dt><code>-D</code></p>
<dd> Show detected path of the loaded dictionary, and list of the search path and the available dictionaries. </p>
<dt><code>-d dict,dict2,&#8230;</code></p>
<dd> Set dictionaries by their base names with or without paths. Example of the syntax:</dl>
<p> -d en_US,en_geo,en_med,de_DE,de_med </p>
<p> en_US and de_DE are base dictionaries, they consist of aff and dic file pairs: en_US.aff, en_US.dic and de_DE.aff, de_DE.dic. En_geo, en_med, de_med are special dictionaries: dictionaries without affix file. Special dictionaries are optional extension of the base dictionaries usually with special (medical, law etc.) terms. There is no naming convention for special dictionaries, only the &quot;.dic&quot; extension: dictionaries without affix file will be an extension of the preceding base dictionary (right order of the parameter list needs for good suggestions). First item of -d parameter list must be a base dictionary. </p>
<dl>
<dt><code>-G</code></p>
<dd> Print only correct words or lines. </p>
<dt><code>-H</code></p>
<dd> The input file is in SGML/HTML format. </p>
<dt><code>-h, &#8211;help</code></p>
<dd> Short help. </p>
<dt><code>-i enc</code></p>
<dd> Set input encoding. </p>
<dt><code>-L</code></p>
<dd> Print lines with misspelled words. </p>
<dt><code>-l</code></p>
<dd> The &quot;list&quot; option is used to produce a list of misspelled words from the standard input. </p>
<dt><code>-m</code></p>
<dd> Analyze the words of the input text (see also <a href="/docs/linux/man/4-hunspell/">hunspell</a>(4) about morphological analysis). Without dictionary morphological data, signs the flags of the affixes of the word forms for dictionary developers. </p>
<dt><code>-n</code></p>
<dd> The input file is in nroff/troff format. </p>
<dt><code>-P password</code></p>
<dd> Set password for encrypted dictionaries. </p>
<dt><code>-p dict</code></p>
<dd> Set path of personal dictionary. The default dictionary depends on the locale settings. The following environment variables are searched: LC_ALL, LC_MESSAGES, and LANG. If none are set then the default personal dictionary is $HOME/.hunspell_default. </p>
<p> Setting <i>-d</i> or the <i>DICTIONARY</i> environmental variable, personal dictionary will be <code>$HOME/.hunspell_dicname</code> </p>
<dt><code>-r</code></p>
<dd> Warn of the rare words, wich are also potential spelling mistakes. </p>
<dt><code>-s</code></p>
<dd> Stem the words of the input text (see also <a href="/docs/linux/man/4-hunspell/">hunspell</a>(4) about stemming). It depends from the dictionary data. </p>
<dt><code>-t</code></p>
<dd> The input file is in TeX or LaTeX format. </p>
<dt><code>-v, &#8211;version</code></p>
<dd> Print version number. </p>
<dt><code>-vv</code></p>
<dd> Print <a href="/docs/linux/man/1-ispell/">ispell</a>(1) compatible version number. </p>
<dt><code>-w</code></p>
<dd> Print misspelled words (= lines) from one word/line input. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>hunspell -d en_US english.html</code></p>
<dd>
<dt><code>hunspell -d en_US,en_US_med medical.txt</code></p>
<dd>
<dt><code>hunspell -d ~/openoffice.org2.4/share/dict/ooo/de_DE</code></p>
<dd>
<dt><code>hunspell *.html</code></p>
<dd>
<dt><code>hunspell -l text.html</code></p>
<dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DICTIONARY</code></p>
<dd> Similar to <i>-d. </i></p>
<dt><code>DICPATH</code></p>
<dd> Dictionary path.</p>
<dt><code>WORDLIST</code></p>
<dd> Equivalent to <i>-p.</i></dl>
<h2>FILES</h2>
<p> The default dictionary depends on the locale settings. The following environment variables are searched: LC_ALL, LC_MESSAGES, and LANG. If none are set then the following fallbacks are used: </p>
<p> <code>/usr/share/myspell/default.aff</code> Path of default affix file. See <a href="/docs/linux/man/4-hunspell/">hunspell</a>(4). </p>
<p> <code>/usr/share/myspell/default.dic</code> Path of default dictionary file. See <a href="/docs/linux/man/4-hunspell/">hunspell</a>(4). </p>
<p> <code>$HOME/.hunspell_default.</code> Default path to personal dictionary.</p>
<h2>SEE ALSO</h2>
<p> <code>hunspell (3), <a href="/docs/linux/man/4-hunspell/">hunspell</a>(4)</code></p>
<h2>AUTHOR</h2>
<p> Author of Hunspell executable is László Németh. For Hunspell library, see <a href="/docs/linux/man/3-hunspell/">hunspell</a>(3). </p>
<p> This manual based on Ispell&#8217;s manual. See <a href="/docs/linux/man/1-ispell/">ispell</a>(1).</p>
<h2>BUGS</h2>
<p> There are some layout problems with long lines. </p>
<h2>Index</h2>
