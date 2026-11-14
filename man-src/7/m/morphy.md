---
title: "morphy(7)"
name: "morphy"
section: "7"
letter: "m"
url: "/docs/linux/man/7-morphy/"
description: "morphy – discussion of WordNet’s morphological processing"
---

<p>morphy &#8211; discussion of WordNet&#8217;s morphological processing</p>
<h2>Description</h2>
<p>Although only base forms of words are usually stored in WordNet, searches may be done on inflected forms. A set of morphology functions, Morphy, is applied to the search string to generate a form that is present in WordNet. </p>
<p> Morphology in WordNet uses two types of processes to try to convert the string passed into one that can be found in the WordNet database. There are lists of inflectional endings, based on syntactic category, that can be detached from individual words in an attempt to find a form of the word that is in WordNet. There are also exception list files, one for each syntactic category, in which a search for an inflected form is done. Morphy tries to use these two processes in an intelligent manner to translate the string passed to the base form found in WordNet. Morphy first checks for exceptions, then uses the rules of detachment. The Morphy functions are not independent from WordNet. After each transformation, WordNet is searched for the resulting string in the syntactic category specified. </p>
<p> The Morphy functions are passed a string and a syntactic category. A string is either a single word or a collocation. Since some words, such as <code>axes</code> can have more than one base form (<code>axe</code> and <code>axis</code>), Morphy works in the following manner. The first time that Morphy is called with a specific string, it returns a base form. For each subsequent call to Morphy made with a <font SIZE="-1"><code>NULL </code></font> string argument, Morphy returns another base form. Whenever Morphy cannot perform a transformation, whether on the first call for a word or subsequent calls, <font SIZE="-1"><code>NULL </code></font> is returned. A transformation to a valid English string will return <font SIZE="-1"><code>NULL</code></font> if the base form of the string is not in WordNet. </p>
<p> The morphological functions are found in the WordNet library. See <code><a href="/docs/linux/man/3-morph/">morph</a></code>(3) for information on using these functions.</p>
<h3>Rules of Detachment</h3>
<p>The following table shows the rules of detachment used by Morphy. If a word ends with one of the suffixes, it is stripped from the word and the corresponding ending is added. Then WordNet is searched for the resulting string. No rules are applicable to adverbs. </p>
<p> <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>POS</code></td>
<td ALIGN=center><code>Suffix</code></td>
<td ALIGN=center><code>Ending</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>NOUN</td>
<td>&quot;s&quot;</td>
<td>&quot;&quot;
</td>
</tr>
<tr VALIGN=top>
<td>NOUN</td>
<td>&quot;ses&quot;</td>
<td>&quot;s&quot;
</td>
</tr>
<tr VALIGN=top>
<td>NOUN</td>
<td>&quot;xes&quot;</td>
<td>&quot;x&quot;
</td>
</tr>
<tr VALIGN=top>
<td>NOUN</td>
<td>&quot;zes&quot;</td>
<td>&quot;z&quot;
</td>
</tr>
<tr VALIGN=top>
<td>NOUN</td>
<td>&quot;ches&quot;</td>
<td>&quot;ch&quot;
</td>
</tr>
<tr VALIGN=top>
<td>NOUN</td>
<td>&quot;shes&quot;</td>
<td>&quot;sh&quot;
</td>
</tr>
<tr VALIGN=top>
<td>NOUN</td>
<td>&quot;men&quot;</td>
<td>&quot;man&quot;
</td>
</tr>
<tr VALIGN=top>
<td>NOUN</td>
<td>&quot;ies&quot;</td>
<td>&quot;y&quot;
</td>
</tr>
<tr VALIGN=top>
<td>VERB</td>
<td>&quot;s&quot;</td>
<td>&quot;&quot;
</td>
</tr>
<tr VALIGN=top>
<td>VERB</td>
<td>&quot;ies&quot;</td>
<td>&quot;y&quot;
</td>
</tr>
<tr VALIGN=top>
<td>VERB</td>
<td>&quot;es&quot;</td>
<td>&quot;e&quot;
</td>
</tr>
<tr VALIGN=top>
<td>VERB</td>
<td>&quot;es&quot;</td>
<td>&quot;&quot;
</td>
</tr>
<tr VALIGN=top>
<td>VERB</td>
<td>&quot;ed&quot;</td>
<td>&quot;e&quot;
</td>
</tr>
<tr VALIGN=top>
<td>VERB</td>
<td>&quot;ed&quot;</td>
<td>&quot;&quot;
</td>
</tr>
<tr VALIGN=top>
<td>VERB</td>
<td>&quot;ing&quot;</td>
<td>&quot;e&quot;
</td>
</tr>
<tr VALIGN=top>
<td>VERB</td>
<td>&quot;ing&quot;</td>
<td>&quot;&quot;
</td>
</tr>
<tr VALIGN=top>
<td>ADJ</td>
<td>&quot;er&quot;</td>
<td>&quot;&quot;
</td>
</tr>
<tr VALIGN=top>
<td>ADJ</td>
<td>&quot;est&quot;</td>
<td>&quot;&quot;
</td>
</tr>
<tr VALIGN=top>
<td>ADJ</td>
<td>&quot;er&quot;</td>
<td>&quot;e&quot;
</td>
</tr>
<tr VALIGN=top>
<td>ADJ</td>
<td>&quot;est&quot;</td>
<td>&quot;e&quot;
</td>
</tr>
</table>
<p></center></p>
<h3>Exception Lists</h3>
<p>There is one exception list file for each syntactic category. The exception lists contain the morphological transformations for strings that are not regular and therefore cannot be processed in an algorithmic manner. Each line of an exception list contains an inflected form of a word or collocation, followed by one or more base forms. The list is kept in alphabetical order and a binary search is used to find words in these lists. See <code><a href="/docs/linux/man/5-wndb/">wndb</a></code>(5) for information on the format of the exception list files.</p>
<h3>Single Words</h3>
<p>In general, single words are relatively easy to process. Morphy first looks for the word in the exception list. If it is found the first base form is returned. Subsequent calls with a <font SIZE="-1"><code>NULL </code></font> argument return additional base forms, if present. A <font SIZE="-1"><code>NULL</code></font> is returned when there are no more base forms of the word. </p>
<p> If the word is not found in the exception list corresponding to the syntactic category, an algorithmic process using the rules of detachment looks for a matching suffix. If a matching suffix is found, a corresponding ending is applied (sometimes this ending is a <font SIZE="-1"><code>NULL</code></font> string, so in effect the suffix is removed from the word), and WordNet is consulted to see if the resulting word is found in the desired part of speech.</p>
<h3>Collocations</h3>
<p>As opposed to single words, collocations can be quite difficult to transform into a base form that is present in WordNet. In general, only base forms of words, even those comprising collocations, are stored in WordNet, such as <code>attorney~general</code>. Transforming the collocation <code>attorneys~general</code> is then simply a matter of finding the base forms of the individual words comprising the collocation. This usually works for nouns, therefore non-conforming nouns, such as <code>customs~duty</code> are presently entered in the noun exception list. </p>
<p> Verb collocations that contain prepositions, such as <code>ask~for~it</code>, are more difficult. As with single words, the exception list is searched first. If the collocation is not found, special code in Morphy determines whether a verb collocation includes a preposition. If it does, a function is called to try to find the base form in the following manner. It is assumed that the first word in the collocation is a verb and that the last word is a noun. The algorithm then builds a search string with the base forms of the verb and noun, leaving the remainder of the collocation (usually just the preposition, but more words may be involved) in the middle. For example, passed <code>asking~for~it</code>, the database search would be performed with <code>ask~for~it</code>, which is found in WordNet, and therefore returned from Morphy. If a verb collocation does not contain a preposition, then the base form of each word in the collocation is found and WordNet is searched for the resulting string.</p>
<h3>Hyphenation</h3>
<p>Hyphenation also presents special difficulties when searching WordNet. It is often a subjective decision as to whether a word is hyphenated, joined as one word, or is a collocation of several words, and which of the various forms are entered into WordNet. When Morphy breaks a string into &quot;words&quot;, it looks for both spaces and hyphens as delimiters. It also looks for periods in strings and removes them if an exact match is not found. A search for an abbreviation like <code>oct.</code> return the synset for <code>{~October,~Oct~}</code>. Not every pattern of hyphenated and collocated string is searched for properly, so it may be advantageous to specify several search strings if the results of a search attempt seem incomplete.</p>
<h3>Special Processing for nouns ending with &#8216;ful&#8217;</h3>
<p>Morphy contains code that searches for nouns ending with <code>ful</code> and performs a transformation on the substring preceeding it. It then appends &#8216;ful&#8217; back onto the resulting string and returns it. For example, if passed the nouns <code>boxesful</code>, it will return <code>boxful</code>.</p>
<h2>Bugs</h2>
<p>Since many noun collocations contains prepositions, such as <code>line~of~products</code>, an algorithm similar to that used for verbs should be written for nouns. In the present scheme, if Morphy is passed <code>lines~of~products</code>, the search string becomes <code>line~of~product</code>, which is not in WordNet </p>
<p> Morphy will allow non-words to be converted to words, if they follow one of the rules described above. For example, it will happily convert <code>plantes</code> to <code>plants</code>.</p>
<h2>Environment Variables (Unix)</h2>
<dl>
<dt><code>WNHOME</code></p>
<dd>Base directory for WordNet. Default is <code>/usr/local/WordNet-3.0</code>.</p>
<dt><code>WNSEARCHDIR</code></p>
<dd>Directory in which the WordNet database has been installed. Default is <code>WNHOME/dict</code>.</dl>
<h2>Registry (Windows)</h2>
<dl>
<dt><code>HKEY_LOCAL_MACHINE\SOFTWARE\WordNet\3.0\WNHome</code></p>
<dd>Base directory for WordNet. Default is <code>C:\Program~Files\WordNet\3.0</code>.</dl>
<h2>Files</h2>
<dl>
<dt><i>pos</i>.exc</p>
<dd>morphology exception lists</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-wn/">wn</a></code>(1), <code><a href="/docs/linux/man/1-wnb/">wnb</a></code>(1), <code><a href="/docs/linux/man/3-binsrch/">binsrch</a></code>(3), <code><a href="/docs/linux/man/3-morph/">morph</a></code>(3), <code><a href="/docs/linux/man/5-wndb/">wndb</a></code>(5), <code><a href="/docs/linux/man/7-wninput/">wninput</a></code>(7). </p>
