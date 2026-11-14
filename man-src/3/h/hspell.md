---
title: "hspell(3)"
name: "hspell"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hspell/"
description: "hspell – Hebrew spellchecker (C API)"
---

<h2>NAME</h2>
<p> hspell &#8211; Hebrew spellchecker (C API)</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;hspell.h&gt;</code> </p>
<p> <code>int hspell_init(struct dict_radix **</code>dictp<code>, int </code>flags<code>);</code> </p>
<p> <code>void hspell_uninit(struct dict_radix *</code>dictp<code>);</code> </p>
<p> <code>int hspell_check_word(struct dict_radix *</code>dict<code>, const char *</code>word<code>, int *</code>preflen<code>);</code> </p>
<p> <code>void hspell_trycorrect(struct dict_radix *</code>dict<code>, const char *</code>word<code>, struct corlist *</code>cl<code>);</code> </p>
<p> <code>int corlist_init(struct corlist *</code>cl<code>);</code> </p>
<p> <code>int corlist_free(struct corlist *</code>cl<code>);</code> </p>
<p> <code>int corlist_n(struct corlist *</code>cl<code>);</code> </p>
<p> <code>char *corlist_str(struct corlist *</code>cl<code>, int </code>i<code>);</code> </p>
<p> <code>unsigned int hspell_is_canonic_gimatria(const char *</code>word<code>);</code> </p>
<p> typedef int hspell_word_split_callback_func(const char *word, const char *baseword, int preflen, int prefspec); </p>
<p> <code>int hspell_enum_splits(struct dict_radix *</code>dict<code>, const char *</code>word<code>, hspell_word_split_callback_func *</code>enumf<code>);</code> </p>
<p> <code>void hspell_set_dictionary_path(const char *</code>path<code>);</code> </p>
<p> <code>const char *hspell_get_dictionary_path(void);</code></p>
<h2>DESCRIPTION</h2>
<p> This manual describes the C API of the Hspell Hebrew spellchecker. Please refer to <code><a href="/docs/linux/man/1-hspell/">hspell</a></code>(1) for a description of the Hspell project, its spelling standard, and how it works. </p>
<p> The <code>hspell_init()</code> function must be called first to initialize the Hspell library. It sets up some global structures (see CAVEATS section) and then reads the necessary dictionary files (whose places are fixed when the library is built). The <i>&#8216;dictp&#8217;</i> parameter is a pointer to a <i>struct dict_radix*</i> object, which is modified to point to a newly allocated dictionary. A typical <code>hspell_init()</code> call therefore looks like </p>
<p>struct dict_radix&nbsp;<wbr>*dict;<br />
hspell_init(&amp;dict, flags); </p>
<p> Note that the (struct dict_radix*) type is an opaque pointer &#8211; the library user has no access to the separate fields in this structure. </p>
<p> The <i>&#8216;flags&#8217;</i> parameter can contain a bitwise or&#8217;ing of several flags that modify Hspell&#8217;s default behavior; Turning on HSPELL_OPT_HE_SHEELA allows Hspell to recognize the interrogative He prefix (he ha-she&#8217;ela). HSPELL_OPT_DEFAULT is a synonym for turning on no special flag, i.e., it evaluates to 0. </p>
<p> <code>hspell_init()</code> returns 0 on success, or negative numbers on errors. Currently, the only error is -1, meaning the dictionary files could not be read. </p>
<p> The <code>hspell_uninit()</code> function undoes the effects of <code>hspell_init()</code>, freeing any memory that was allocated during initialization. </p>
<p> The <code>hspell_check_word()</code> function checks whether a certain word is a correct Hebrew word (possibly with prefix particles attached in a syntacticly-correct manner). 1 is returned if the word is correct, or 0 if it is incorrect. </p>
<p> The <i>&#8216;word&#8217;</i> parameter should be a single Hebrew word, in the iso8859-8 encoding, possibly containing the ASCII quote or double-quote characters (signifying the geresh and gershayim used in Hebrew for abbreviations, acronyms, and a few foreign sounds). If the calling programs works with other encodings, it must convert the word to iso8859-8 first. In particular cp1255 (the MS-Windows Hebrew encoding) extensions to iso8859-8 like niqqud characters, geresh or gershayim, are currently not recognized and must be removed from the word prior to calling <code>hspell_check_word()</code>. </p>
<p> Into the <i>&#8216;preflen&#8217;</i> parameter, the function writes back the number of characters it recognized as a prefix particle &#8211; the rest of the &#8216;word&#8217; is a stand-alone word. Because Hebrew words typically can be read in several different ways, this feature (of getting just one prefix from one possible reading) is usually not very useful, and it is likely to be removed in a future version. </p>
<p> The <code>hspell_enum_splits()</code> function provides a way to get all possible splitting of the given <i>&#8216;word&#8217;</i> into an optional prefix particle and a stand-alone word. For each possible (and legal, as some words cannot accept certain prefixes) split, a user-defined callback function is called. This callback function is given the whole word, the length of the prefix, the stand-alone word, and a bitfield which describes what types of words this prefix can get. Note that in some cases, a word beginning with the letter waw gets this waw doubled before a prefix, so sometimes strlen(word)!=strlen(baseword)+preflen. </p>
<p> The <code>hspell_trycorrect()</code> tries to find a list of possible corrections for an incorrect word. Because in Hebrew the word density is high (a random string of letters, especially if short, has a high probability of being a correct word), this function attempts to try corrections based on the assumption of a spelling error (replacement of letters that sound alike, missing or spurious immot qri&#8217;a), not typo (slipped finger on the keyboard, etc.) &#8211; see also CAVEATS. </p>
<p> <code>hspell_trycorrect()</code> returns the correction list into a structure of type <i>struct corlist</i>. This structure must be first allocated with a call to <code>corlist_init()</code> and subsequently freed with <code>corlist_free()</code>. The <code>corlist_n()</code> macro returns the number of words held in an allocated corlist, and <code>corlist_str()</code> returns the i&#8217;th word. Accordingly, here is an example usage of <code>hspell_trycorrect()</code>: </p>
<p>struct corlist cl;<br />
printf&nbsp;<wbr>(&quot;Found misspelled word&nbsp;<wbr>%s. Possible corrections:
&quot;, w);<br />
corlist_init&nbsp;<wbr>(&amp;cl);<br />
hspell_trycorrect&nbsp;<wbr>(dict, w,&nbsp;<wbr>&amp;cl);<br />
for&nbsp;<wbr>(i=0;&nbsp;<wbr>i&lt;corlist_n(&amp;cl);&nbsp;<wbr>i++)&nbsp;<wbr>{<br />
&nbsp;<wbr>printf&nbsp;<wbr>(&quot;%s
&quot;, corlist_str(&amp;cl, i));<br />
} </p>
<p> The <code>hspell_is_canonic_gimatria()</code> function checks whether the given word is a <i>canonic</i> gimatria &#8211; i.e., the proper way to write in gimatria the number it represents. The caller might want to accept canonic gimatria as proper Hebrew words, even if <code>hspell_check_word()</code> previously reported such word to be a non-existent word. <code>hspell_is_canonic_gimatria()</code> returns the number represented as gimatria in &#8216;word&#8217; if it is indeed proper gimatria (in canonic form), or 0 otherwise. </p>
<p> <code>hspell_init()</code> normally reads the dictionary files from a path compiled into the library. This makes sense when the library&#8217;s code and the dictionaries are distributed together, but in some scenarios the library user might want to use the Hspell dictionaries that are already present on the system in an arbitrary path. The function <code>hspell_set_dictionary_path()</code> can be used to set this path, and should be used before calling <code>hspell_init()</code>. The given path is that of the word list, and other input files have that path with an appended prefix. <code>hspell_get_dictionary_path()</code> can be used to find the current path. On many installations, this defaults to &quot;/usr/local/share/hspell/hebrew.wgz&quot;. </p>
<h2>LINKING</h2>
<p> On most systems, the Hspell library is compiled to use the Zlib library for reading the compressed dictionaries. Therefore, a program linking with the Hspell library must also be linked with the Zlib library (usually, by adding &quot;-lz&quot; to the compilation line). </p>
<p> Programs that use <i>autoconf</i> to search for the Hspell library, should remember to tell AC_CHECK_LIB to also link with the -lz library when checking for -lhspell. </p>
<h2>CAVEATS</h2>
<p> While the API described here has been stable for years, it may change in the future. Users are encouraged to compare the values of the integer macros <code>HSPELL_VERSION_MAJOR</code> and <code>HSPELL_VERSION_MINOR</code> to those expected by the writer of the program. A third macro, <code>HSPELL_VERSION_EXTRA</code> contains a string which can describe subrelease modifications (e.g., beta versions). </p>
<p> The current Hspell C API is very low-level, in the sense that it leaves the user to implement many features that some users take for granted that a spell-checker should provide. For example it doesn&#8217;t provide any facilities for a user-defined personal dictionary. It also has separate functions for checking valid Hebrew words and valid gimatria, and no function to do both. It is assumed that the caller &#8211; a bigger spell-checking library or word processor (for example), will already have these facilities. If not, you may wish to look at the sources of <code><a href="/docs/linux/man/1-hspell/">hspell</a></code>(1) for an example implementation. </p>
<p> Currently there is no concept of separate Hspell &quot;contexts&quot; in an application. Some of the context is now global for the entire application: currently, a single list of legal prefix-particles is kept, and the dictionary read by <code>hspell_init()</code> is always read from the global default place. This may be solved in a later version, e.g., by switching to an API like: </p>
<p>context&nbsp;<wbr>=&nbsp;<wbr>hspell_new_context();<br />
hspell_set_dictionary_path(context,&nbsp;<wbr>&quot;/some/path/hebrew.wgz&quot;);<br />
hspell_init(context, flags);<br />
&#8230;<br />
hspell_check_word(context, word, preflenp); </p>
<p> Note that despite the global context mentioned above, after initialization all functions described here are <i>thread-safe</i>, because they only read the dictionary data, not write to it. </p>
<p> <code>hspell_trycorrect()</code> is not as powerful as it could have been, with typos or certain kinds of spelling mistakes not giving useful correction suggestions. Along with more types of corrections, <code>hspell_trycorrect()</code> needs a better way to order the likelihood of the corrections, as an unordered list of 100 corrections would be just as useful (or rather, useless) as none. </p>
<p> In some cases of errors during <code>hspell_init()</code>, warning messages are printed to the standard errors. This is a bad thing for a library to do. </p>
<p> There are too many CAVEATS in this manual. </p>
<h2>VERSION</h2>
<p> The version of <code>hspell</code> described by this manual page is 1.2.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2000-2012, Nadav Har&#8217;El &lt;nyh [at] math.technion.ac.il&gt; and Dan Kenigsberg &lt;danken [at] cs.technion.ac.il&gt;. </p>
<p> Hspell is free software, released under the GNU Affero General Public License (AGPL) version 3. Note that not only the programs in the distribution, but also the dictionary files and the generated word lists, are licensed under the AGPL. There is no warranty of any kind. </p>
<p> See the LICENSE file for more information and the exact license terms. </p>
<p> The latest version of this software can be found in <code><a rel="nofollow" href="http://hspell.ivrix.org.il/">http://hspell.ivrix.org.il/</a></code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-hspell/">hspell</a></code>(1) </p>
<h2>Index</h2>
