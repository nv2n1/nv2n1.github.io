---
title: "hspell(1)"
name: "hspell"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hspell/"
description: "hspell – Hebrew spellchecker"
---

<h2>NAME</h2>
<p> hspell &#8211; Hebrew spellchecker</p>
<h2>SYNOPSIS</h2>
<p> <code>hspell</code> [ <code>-acDhHilnsvV</code> ] <code>[</code><i>file&#8230;</i><code>]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>hspell</code> tries to find incorrectly spelled Hebrew words in its input files. </p>
<p> Like the traditional Unix <a href="/docs/linux/man/1-spell/">spell</a>(1), <code>hspell</code> outputs the sorted list of incorrect words, and does not have a more friendly interface for making corrections for you. However, unlike <a href="/docs/linux/man/1-spell/">spell</a>(1), <code>hspell</code> can suggest possible corrections for some spelling errors. Such suggestions can be enabled with the <code>-c</code> (correct) and <code>-n</code> (notes) options. </p>
<p> <code>Hspell</code> currently expects ISO-8859-8-encoded input files. Non-Hebrew characters in the input files are ignored, allowing the easy spellchecking of Hebrew-English texts, as well as HTML or TeX files. If files using a different encoding (e.g., UTF-8) are to be checked, they must be converted first to ISO-8859-8 (e.g., see <a href="/docs/linux/man/1-iconv/">iconv</a>(1), <a href="/docs/linux/man/1-recode/">recode</a>(1)). </p>
<p> The output will also be in ISO-8859-8 encoding, in so-called &quot;logical order&quot;, so it is normally useful to pipe it to <a href="/docs/linux/man/1-bidiv/">bidiv</a>(1) before viewing, as in: </p>
<dl>
<dt>
<dd> <code>hspell -c filename | bidiv | less</code></dl>
<p> If no input file is given, <code>hspell</code> reads from its standard input.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code></p>
<dd> If the <code>-v</code> option is given, <code>hspell</code> prints emacs-oriented version information and exits.</p>
<dt><code>-vv</code></p>
<dd> Repetition of the <code>-v</code> option causes <code>hspell</code> to also show some information on which optional features were enabled at compile time.</p>
<dt><code>-V</code></p>
<dd> With the <code>-V</code> option, <code>hspell</code> prints true and human-oriented version information and exits.</p>
<dt><code>-c</code></p>
<dd> If the <code>-c</code> option is given, <code>hspell</code> will suggest corrections for misspelled words, whenever it can find such corrections. The correction mechanism in this release is especially good at finding corrections for incorrect niqqud-less spellings, with missing or extra &#8216;immot-qri&#8217;a.</p>
<dt><code>-n</code></p>
<dd> The <code>-n</code> option will give some longer &quot;notes&quot; about certain spelling errors, explaining why these are indeed errors (or in what cases using this word is in fact correct). It is recommend to combine the two options, <code>-cn</code> for maximal correction help from <code>hspell</code>.</p>
<dt><code>-l</code></p>
<dd> The <code>-l</code> (linguistic information) option will explain for each <i>correct</i> word why it was recognized (show the basic noun, verb, etc., that this inflection relates to, and its tense, gender, associated Kinnuy, or other relevant information) </p>
<p> If Hspell was built without morphological analysis support, this option will only show the correct splits of the given word into prefix + word, as the full information incurs a 4-fold increase in the installation size. </p>
<p> Giving the <code>-c</code> option in addition to <code>-l</code> results in special behavior. In that case <code>hspell</code> suggests &quot;corrections&quot; to every word (regardless if they are in the dictionary or not), and shows the linguistic information on all those words. This can be useful for a reader application, which may also want to be able to understand misspellings and their possible meanings. </p>
<dt><code>-s</code></p>
<dd> Normally, the words deemed spelling mistakes are shown in alphabetical order. The <code>-s</code> option orders them by <i>severity</i>, i.e., the errors that most frequently appear in the document are shown first. This option is most useful for people helping to build <code>hspell</code>&#8216;s word list, and are looking for common correct words that <code>hspell</code> does not know yet.</p>
<dt><code>-a</code></p>
<dd> With the <code>-a</code> option, <code>hspell</code> tries to emulate (as little as possible of) <code>ispell&#8217;s</code> pipe interface. This allows <code>Lyx, Emacs, Geresh</code> and <code>KDE</code> to use <code>hspell</code> as an external spell-checker.</p>
<dt><code>-i</code></p>
<dd> This option only has any effect when used together with the <code>-a</code> option. Normally, <code>hspell -a</code> only checks the spelling of Hebrew words. If the given file also contains non-Hebrew words (such as English words), these are simply ignored. Adding the <code>-i</code> option tells <code>hspell</code> to pass the non-Hebrew words to <code><a href="/docs/linux/man/1-ispell/">ispell</a></code>(1), and return its answer as an answer from <code>hspell</code>. This allows conveniently spell-checking mixed Hebrew-English documents. </p>
<p> Running <code>hspell</code> with the program name <code>hspell-i</code> also enables the <code>-i</code> option. This is a useful trick when an application expects just the name of a spell-checking program, and adds only the &quot;-a&quot; option (without giving the user an option to also add &quot;-i&quot;). The <code>multispell</code> script supplied with <code>hspell</code> serves a similar purpose, with more control over encodings and which spell-checker to run for non-Hebrew words.</p>
<dt><code>-H</code></p>
<dd> By default, Hspell does not allow the He Ha-sh&#8217;ela prefix. This is because this prefix is not normally used in modern Hebrew, and generates many false-negatives (errors, like He followed by a possessed noun, are thought to be correct). The <code>-H</code> option nevertheless tells Hspell to allow this prefix.</p>
<dt><code>-D base</code></p>
<dd> Load the word lists from the given base pathname, rather than from the compiled-in default path. This is mostly used for testing Hspell, when the dictionaries have been compiled in the current directory and hspell is run as &quot;hspell -Dhebrew.wgz&quot;.</p>
<dt><code>-d, -B, -m, -T, -C, -S, -P, -p, -w, and -W</code></p>
<dd> These options are passed to <code>hspell</code> by <code>lyx</code> or other applications, thinking they are talking to ispell. These options are cordially ignored.</dl>
<h2>SPELLING STANDARD</h2>
<p> Hspell was designed to be 100% and strictly compliant with the official niqqud-less spelling rules (&quot;Ha-ktiv Khasar Ha-niqqud&quot;, colloquially known as &quot;Ktiv Male&quot;) published by the Academy of the Hebrew Language. </p>
<p> This is both an advantage and a disadvantage, depending on your viewpoint. It&#8217;s an advantage because it encourages a <code>correct</code> and consistent spelling style throughout your writing. It is a disadvantage, because a few of the Academia&#8217;s official spelling decisions are relatively unknown to the general public. </p>
<p> Users of Hspell (and all Hebrew writers, for that matter) are encouraged to read the Academia&#8217;s official niqqud-less spelling rules (which are printed at the end of most modern Hebrew dictionaries, and an abridged version is available in <a rel="nofollow" href="http://hebrew-academy.huji.ac.il/decision4.html">http://hebrew-academy.huji.ac.il/decision4.html</a>). Users are also encouraged to refer to Hebrew dictionaries which use the niqqud-less spelling (such as Millon Ha-hove, Rav Milim, and the new Even Shoshan). </p>
<p> Hspell&#8217;s distribution (and Web site) also include a document, <code>niqqudless.odt</code>, which explains Hspell&#8217;s spelling standard in detail (in Hebrew). It explains both the overall principles, and why specific words are spelled the way they are. </p>
<p> A future release may include an option for alternative spelling standards.</p>
<h2>BEHIND THE SCENES</h2>
<p> The <code>hspell</code> program itself is mostly a simple (but efficient) program that checks input words against a long list of valid words. The real &quot;brains&quot; behind it are the word lists (dictionary) provided by the Hspell project. </p>
<p> In order for this dictionary to be completely free of other people&#8217;s copyright restrictions, the Hspell project is a clean-room implementation, not based on pre-existing word lists or spell checkers, or on copying of printed dictionaries. </p>
<p> The word list is also not based on automatic scanning of available Hebrew documents (such as online newspapers), because there is no way to guarantee that such a list will be correct, complete, or consistent in its spelling standard. </p>
<p> Instead, our idea was to write programs which know how to correctly inflect Hebrew nouns and conjugate Hebrew verbs. The input to these programs is a list of noun stems and verb roots, plus hints needed for the correct inflection when these cannot be figured out automatically. Most of the effort that went into the Hspell project went into building these input files. Then, &quot;word list generators&quot; (written in Perl, and are also part of the Hspell project) create the complete inflected word list that will be used by the spellchecking program, hspell. This generation process is only done once, when building <code>hspell</code> from source. </p>
<p> These lists, before and after inflection, may be useful for much more than spellchecking. Morphological analysis (which <code>hspell</code> provides with the <code>-l</code> option) is one example. For more ideas, see Hspell project&#8217;s Web site, at <code><a rel="nofollow" href="http://ivrix.org.il/projects/spell-checker">http://ivrix.org.il/projects/spell-checker</a></code>.</p>
<h2>FILES</h2>
<dl>
<dt>~/.hspell_words, ./hspell_words</p>
<dd> These files, if they exist, should contain a list of Hebrew words that <code>hspell</code> will also accept as correct words. </p>
<p> Note that only these words <i>exactly</i> will be added &#8211; they are not inflected, and prefixes are not automatically allowed. </p>
<dt>/usr/local/share/hspell/*</p>
<dd> The standard Hebrew word lists used by <code>hspell</code>. </p>
</dl>
<h2>EXIT STATUS</h2>
<p> Currently always 0.</p>
<h2>VERSION</h2>
<p> The version of <code>hspell</code> described by this manual page is 1.2.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2000-2012, Nadav Har&#8217;El &lt;nyh [at] math.technion.ac.il&gt; and Dan Kenigsberg &lt;danken [at] cs.technion.ac.il&gt;. </p>
<p> Hspell is free software, released under the GNU Affero General Public License (AGPL) version 3. Note that not only the programs in the distribution, but also the dictionary files and the generated word lists, are licensed under the AGPL. There is no warranty of any kind. </p>
<p> See the LICENSE file for more information and the exact license terms. </p>
<p> The latest version of this software can be found in <code><a rel="nofollow" href="http://hspell.ivrix.org.il/">http://hspell.ivrix.org.il/</a></code></p>
<h2>ACKNOWLEDGMENTS</h2>
<p> The hspell utility and the linguistic databases behind it (collectively called &quot;the Hspell project&quot;) were created by Nadav Har&#8217;El &lt;nyh [at] math.technion.ac.il&gt; and by Dan Kenigsberg &lt;danken [at] cs.technion.ac.il&gt;. </p>
<p> Although we wrote all of Hspell&#8217;s code ourselves, we are truly indebted to the old-style &quot;open source&quot; pioneers &#8211; people who wrote books instead of hiding their knowledge in proprietary software. For the correct noun inflections, Dr. Shaul Barkali&#8217;s &quot;The Complete Noun Book&quot; has been a great help. Prof. Uzzi Ornan&#8217;s booklet &quot;Verb Conjugation in Flow Charts&quot; has been instrumental in the implementation of verb conjugation, and Barkali&#8217;s &quot;The Complete Verb Book&quot; was used too. </p>
<p> During our work we have extensively used a number of Hebrew dictionaries, including Even Shoshan, Millon Ha-hove and Rav-Milim, to ensure the correctness of certain words. Various Hebrew newspapers and books, both printed and online, were used for inspiration and for finding words we still do not recognize. </p>
<p> We wish to thank Cilla Tuviana and Dr. Zvi Har&#8217;El for their assistance with some grammatical questions. </p>
<p> Several other people helped us in various releases, with suggestions, fixes or patches &#8211; they are listed in the WHATSNEW file in the distribution. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-hspell/">hspell</a></code>(3), <code><a href="/docs/linux/man/1-spell/">spell</a></code>(1), <code><a href="/docs/linux/man/1-ispell/">ispell</a></code>(1), <code><a href="/docs/linux/man/1-bidiv/">bidiv</a></code>(1), <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1), <code><a href="/docs/linux/man/1-recode/">recode</a></code>(1)</p>
<h2>BUGS</h2>
<p> This manual page is in English. </p>
<p> For GUI-lovers, <code>hspell</code>&#8216;s user interface is an abomination. However, as more and more applications learn to interface with <code>hspell</code>, and as Hspell&#8217;s data becomes available in multi-lingual spellcheckers (such as aspell and hunspell), this will no longer be an issue. See <code><a rel="nofollow" href="http://hspell.ivrix.org.il/">http://hspell.ivrix.org.il/</a></code> for instructions on how to use Hspell in a variety of applications. </p>
<p> <code>hspell</code>&#8216;s being limited to the ISO-8859-8 encoding, and not recognizing UTF-8 or even CP1255 (including niqqud), is an anachronism today. </p>
<h2>Index</h2>
