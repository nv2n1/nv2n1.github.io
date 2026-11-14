---
title: "hunspell(3)"
name: "hunspell"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hunspell/"
---

<h2 class="name">NAME</h2>
 

 <b>hunspell</b> - spell checking, stemming, morphological generation and analysis 

<h2>SYNOPSIS</h2>

 <b>#include &lt;hunspell/hunspell.hxx&gt; /* or */</b> 
 <b>#include &lt;hunspell/hunspell.h&gt;</b> 
 

 <b>Hunspell(const char *</b><i>affpath</i><b>, const char *</b><i>dpath</i><b>);</b> 

 <b>Hunspell(const char *</b><i>affpath</i><b>, const char *</b><i>dpath</i><b>, const char * </b><i>key</i><b>);</b> 

 <b>~Hunspell(</b><i>);</i> 

 <b>int add_dic(const char *</b><i>dpath</i><b>);</b> 

 <b>int add_dic(const char *</b><i>dpath</i><b>, const char *</b><i>key</i><b>);</b> 

 <b>int spell(const char *</b><i>word</i><b>);</b> 

 <b>int spell(const char *</b><i>word</i><b>, int *</b><i>info</i><b>, char **</b><i>root</i><b>);</b> 

 <b>int suggest(char***</b><i>slst</i><b>, const char *</b><i>word);</i> 

 <b>int analyze(char***</b><i>slst</i><b>, const char *</b><i>word);</i> 

 <b>int stem(char***</b><i>slst</i><b>, const char *</b><i>word);</i> 

 <b>int stem(char***</b><i>slst</i><b>, char **</b><i>morph</i><b>, int </b><i>n);</i> 

 <b>int generate(char***</b><i>slst</i><b>, const char *</b><i>word</i><b>, const char *</b><i>word2);</i> 

 <b>int generate(char***</b><i>slst</i><b>, const char *</b><i>word</i><b>, char **</b><i>desc</i><b>, int </b><i>n);</i> 

 <b>void free_list(char ***</b><i>slst</i><b>, int </b><i>n);</i> 

 <b>int add(const char *</b><i>word);</i> 

 <b>int add_with_affix(const char *</b><i>word</i><b>, const char *</b><i>example);</i> 

 <b>int remove(const char *</b><i>word);</i> 

 <b>char * get_dic_encoding(</b><i>);</i> 

 <b>const char * get_wordchars(</b><i>);</i> 

 <b>unsigned short * get_wordchars_utf16(int *</b><i>len);</i> 

 <b>struct cs_info * get_csconv(</b><i>);</i> 

 <b>const char * get_version(</b><i>);</i>

<h2>DESCRIPTION</h2>

 The <b>Hunspell</b> library routines give the user word-level linguistic functions: spell checking and correction, stemming, morphological generation and analysis in item-and-arrangement style. 

 The optional C header contains the C interface of the C++ library with Hunspell_create and Hunspell_destroy constructor and destructor, and an extra HunHandle parameter (the allocated object) in the wrapper functions (see in the C header file <b>hunspell.h</b>). 

 The basic spelling functions, <b>spell()</b> and <b>suggest()</b> can be used for stemming, morphological generation and analysis by XML input texts (see XML API).

<h3>Constructor and destructor</h3>

 Hunspell's constructor needs paths of the affix and dictionary files. See the <b><a HREF="/docs/linux/man/4-hunspell/">hunspell</a></b>(4) manual page for the dictionary format. Optional <b>key</b> parameter is for dictionaries encrypted by the <b>hzip</b> tool of the Hunspell distribution.

<h3>Extra dictionaries</h3>

 The add_dic() function load an extra dictionary file. The extra dictionaries use the affix file of the allocated Hunspell object. Maximal number of the extra dictionaries is limited in the source code (20).

<h3>Spelling and correction</h3>

 The spell() function returns non-zero, if the input word is recognised by the spell checker, and a zero value if not. Optional reference variables return a bit array (info) and the root word of the input word. Info bits checked with the SPELL_COMPOUND, SPELL_FORBIDDEN or SPELL_WARN macros sign compound words, explicit forbidden and probably bad words. From version 1.3, the non-zero return value is 2 for the dictionary words with the flag &quot;WARN&quot; (probably bad words). 

 The suggest() function has two input parameters, a reference variable of the output suggestion list, and an input word. The function returns the number of the suggestions. The reference variable will contain the address of the newly allocated suggestion list or NULL, if the return value of suggest() is zero. Maximal number of the suggestions is limited in the source code. 

 The spell() and suggest() can recognize XML input, see the XML API section.

<h3>Morphological functions</h3>

 The plain stem() and analyze() functions are similar to the suggest(), but instead of suggestions, return stems and results of the morphological analysis. The plain generate() waits a second word, too. This extra word and its affixation will be the model of the morphological generation of the requested forms of the first word. 

 The extended stem() and generate() use the results of a morphological analysis: 

<dl>
<dt>
<dd> <pre><code>
char **result, result2;
int n1 = analyze(&amp;result, "words");
int n2 = stem(&amp;result2, result, n1);
</code></pre></dl>
 

 The morphological annotation of the Hunspell library has fixed (two letter and a colon) field identifiers, see the <b><a HREF="/docs/linux/man/4-hunspell/">hunspell</a></b>(4) manual page. 

<dl>
<dt>
<dd> <pre><code>
char **result;
char *affix = "is:plural"; // description depends from dictionaries, too
int n = generate(&amp;result, "word", &amp;affix, 1);
for (int i = 0; i &lt; n; i++) printf("%s, result[i]);
</code></pre></dl>
 

<h3>Memory deallocation</h3>

 The free_list() function frees the memory allocated by suggest(), analyze, generate and stem() functions.

<h3>Other functions</h3>

 The add(), add_with_affix() and remove() are helper functions of a personal dictionary implementation to add and remove words from the base dictionary in run-time. The add_with_affix() uses a second word as a model of the enabled affixation of the new word. 

 The get_dic_encoding() function returns &quot;ISO8859-1&quot; or the character encoding defined in the affix file with the &quot;SET&quot; keyword. 

 The get_csconv() function returns the 8-bit character case table of the encoding of the dictionary. 

 The get_wordchars() and get_wordchars_utf16() return the extra word characters definied in affix file for tokenization by the &quot;WORDCHARS&quot; keyword. 

 The get_version() returns the version string of the library.

<h3>XML API</h3>

 The spell() function returns non-zero for the &quot;&lt;?xml?&gt;&quot; input indicating the XML API support. 

 The suggest() function stems, analyzes and generates the forms of the input word, if it was added by one of the following &quot;SPELLML&quot; syntaxes: 

<dl>
<dt>
<dd> <pre>
&lt;?xml?&gt;
&lt;query type=&quot;analyze&quot;&gt;
&lt;word&gt;dogs&lt;/word&gt;
&lt;/query&gt;
</pre></dl>
 

 

 

<dl>
<dt>
<dd> <pre>
&lt;?xml?&gt;
&lt;query type=&quot;stem&quot;&gt;
&lt;word&gt;dogs&lt;/word&gt;
&lt;/query&gt;
</pre></dl>
 

 

 

<dl>
<dt>
<dd> <pre>
&lt;?xml?&gt;
&lt;query type=&quot;generate&quot;&gt;
&lt;word&gt;dog&lt;/word&gt;
&lt;word&gt;cats&lt;/word&gt;
&lt;/query&gt;
</pre></dl>
 

 

 

<dl>
<dt>
<dd> <pre>
&lt;?xml?&gt;
&lt;query type=&quot;generate&quot;&gt;
&lt;word&gt;dog&lt;/word&gt;
&lt;code&gt;&lt;a&gt;is:pl&lt;/a&gt;&lt;a&gt;is:poss&lt;/a&gt;&lt;/code&gt;
&lt;/query&gt;
</pre></dl>
 

 

 The outputs of the type=&quot;stem&quot; query and the stem() library function are the same. The output of the type=&quot;analyze&quot; query is a string contained a &lt;code&gt;&lt;a&gt;result1&lt;/a&gt;&lt;a&gt;result2&lt;/a&gt;...&lt;/code&gt; element. This element can be used in the second syntax of the type=&quot;generate&quot; query.

<h2>EXAMPLE</h2>

 See analyze.cxx in the Hunspell distribution.

<h2>AUTHORS</h2>

 Hunspell based on Ispell's spell checking algorithms and OpenOffice.org's Myspell source code. 

 Author of International Ispell is Geoff Kuenning. 

 Author of MySpell is Kevin Hendricks. 

 Author of Hunspell is László Németh. 

 Author of the original C API is Caolan McNamara. 

 Author of the Aspell table-driven phonetic transcription algorithm and code is Björn Jacke. 

 See also THANKS and Changelog files of Hunspell distribution. 

<h2>Index</h2>


