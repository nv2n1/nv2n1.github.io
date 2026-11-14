---
title: "wndb(5)"
name: "wndb"
section: "5"
letter: "w"
url: "/docs/linux/man/5-wndb/"
description: "index.noun, data.noun, index.verb, data.verb, index.adj, data.adj, index.adv, data.adv – WordNet database files"
---

<p>index.noun, data.noun, index.verb, data.verb, index.adj, data.adj, index.adv, data.adv &#8211; WordNet database files </p>
<p> noun.exc, verb.exc. adj.exc adv.exc &#8211; morphology exception lists </p>
<p> sentidx.vrb, sents.vrb &#8211; files used by search code to display sentences illustrating the use of some specific verbs</p>
<h2>Description</h2>
<p>For each syntactic category, two files are needed to represent the contents of the WordNet database &#8211; <code>index.</code><i>pos</i> and <code>data.</code><i>pos</i>, where <i>pos</i> is <code>noun</code>, <code>verb</code>, <code>adj</code> and <code>adv</code>. The other auxiliary files are used by the WordNet library&#8217;s searching functions and are needed to run the various WordNet browsers. Each index file is an alphabetized list of all the words found in WordNet in the corresponding part of speech. On each line, following the word, is a list of byte offsets (<i>synset_offset</i>s) in the corresponding data file, one for each synset containing the word. Words in the index file are in lower case only, regardless of how they were entered in the lexicographer files. This folds various orthographic representations of the word into one line enabling database searches to be case insensitive. See <code><a href="/docs/linux/man/5-wninput/">wninput</a></code>(5) for a detailed description of the lexicographer files A data file for a syntactic category contains information corresponding to the synsets that were specified in the lexicographer files, with relational pointers resolved to <i>synset_offset</i>s. Each line corresponds to a synset. Pointers are followed and hierarchies traversed by moving from one synset to another via the <i>synset_offset</i>s. The exception list files, <i>pos</i><code>.exc</code>, are used to help the morphological processor find base forms from irregular inflections. The files <code>sentidx.vrb</code> and <code>sents.vrb</code> contain sentences illustrating the use of specific senses of some verbs. These files are used by the searching software in response to a request for verb sentence frames. Generic sentence frames are displayed when an illustrative sentence is not present. The various database files are in ASCII formats that are easily read by both humans and machines. All fields, unless otherwise noted, are separated by one space character, and all lines are terminated by a newline character. Fields enclosed in italicized square brackets may not be present. See <code><a href="/docs/linux/man/7-wngloss/">wngloss</a></code>(7) for a glossary of WordNet terminology and a discussion of the database&#8217;s content and logical organization.</p>
<h3>Index File Format</h3>
<p>Each index file begins with several lines containing a copyright notice, version number and license agreement. These lines all begin with two spaces and the line number so they do not interfere with the binary search algorithm that is used to look up entries in the index files. All other lines are in the following format. In the field descriptions, <code>number</code> always refers to a decimal integer unless otherwise defined. </p>
<pre><i>lemma~~pos~~synset_cnt~~p_cnt~~[ptr_symbol...]~~sense_cnt~~tagsense_cnt ~~synset_offset~~[synset_offset...]</i></pre>
<dl>
<dt><i>lemma</i></p>
<dd>lower case ASCII text of word or collocation. Collocations are formed by joining individual words with an underscore (<code>_</code>) character.</p>
<dt><i>pos</i></p>
<dd>Syntactic category: <code>n</code> for noun files, <code>v</code> for verb files, <code>a</code> for adjective files, <code>r</code> for adverb files.  All remaining fields are with respect to senses of <i>lemma</i> in <i>pos</i>.</p>
<dl>
<dt><i>synset_cnt</i></p>
<dd>Number of synsets that <i>lemma</i> is in. This is the number of senses of the word in WordNet. See <font SIZE="-1"><code>Sense Numbers</code></font> below for a discussion of how sense numbers are assigned and the order of <i>synset_offset</i>s in the index files.</p>
<dt><i>p_cnt</i></p>
<dd>Number of different pointers that <i>lemma</i> has in all synsets containing it.</p>
<dt><i>ptr_symbol</i></p>
<dd>A space separated list of <i>p_cnt</i> different types of pointers that <i>lemma</i> has in all synsets containing it. See <code><a href="/docs/linux/man/5-wninput/">wninput</a></code>(5) for a list of <i>pointer_symbol</i>s. If all senses of <i>lemma</i> have no pointers, this field is omitted and <i>p_cnt</i> is <code>0</code>.</p>
<dt><i>sense_cnt</i></p>
<dd>Same as <i>sense_cnt</i> above. This is redundant, but the field was preserved for compatibility reasons.</p>
<dt><i>tagsense_cnt</i></p>
<dd>Number of senses of <i>lemma</i> that are ranked according to their frequency of occurrence in semantic concordance texts.</p>
<dt><i>synset_offset</i></p>
<dd>Byte offset in <code>data.</code><i>pos</i> file of a synset containing <i>lemma</i>. Each <i>synset_offset</i> in the list corresponds to a different sense of <i>lemma</i> in WordNet. <i>synset_offset</i> is an 8 digit, zero-filled decimal integer that can be used with <code><a href="/docs/linux/man/3-fseek/">fseek</a></code>(3) to read a synset from the data file. When passed to <code><a href="/docs/linux/man/3-read_synset/">read_synset</a></code>(3) along with the syntactic category, a data structure containing the parsed synset is returned.</dl>
<h3>Data File Format</h3>
<p>Each data file begins with several lines containing a copyright notice, version number and license agreement. These lines all begin with two spaces and the line number. All other lines are in the following format. Integer fields are of fixed length, and are zero-filled. </p>
<pre><i>synset_offset~~lex_filenum~~ss_type~~w_cnt~~word~~lex_id~~[word~~lex_id...]~~p_cnt~~[ptr...]~~[frames...]~~</i><code>|</code><i>~~gloss</i></pre>
<dl>
<dt><i>synset_offset</i></p>
<dd>Current byte offset in the file represented as an 8 digit decimal integer.</p>
<dt><i>lex_filenum</i></p>
<dd>Two digit decimal integer corresponding to the lexicographer file name containing the synset. See <code><a href="/docs/linux/man/5-lexnames/">lexnames</a></code>(5) for the list of filenames and their corresponding numbers.</p>
<dt><i>ss_type</i></p>
<dd>One character code indicating the synset type:</p>
<dl>
<dd>
<pre><code>n</code> NOUN
<code>v</code> VERB
<code>a</code> ADJECTIVE
<code>s</code> ADJECTIVE SATELLITE
<code>r</code> ADVERB</pre>
</dl>
<dt><i>w_cnt</i></p>
<dd>Two digit hexadecimal integer indicating the number of words in the synset.</p>
<dt><i>word</i></p>
<dd>ASCII form of a word as entered in the synset by the lexicographer, with spaces replaced by underscore characters (<code>_</code>). The text of the word is case sensitive, in contrast to its form in the corresponding <code>index.</code><i>pos</i> file, that contains only lower-case forms. In <code>data.adj</code>, a <i>word</i> is followed by a syntactic marker if one was specified in the lexicographer file. A syntactic marker is appended, in parentheses, onto <i>word</i> without any intervening spaces. See <code><a href="/docs/linux/man/5-wninput/">wninput</a></code>(5) for a list of the syntactic markers for adjectives.</p>
<dt><i>lex_id</i></p>
<dd>One digit hexadecimal integer that, when appended onto <i>lemma</i>, uniquely identifies a sense within a lexicographer file. <i>lex_id</i> numbers usually start with <code>0</code>, and are incremented as additional senses of the word are added to the same file, although there is no requirement that the numbers be consecutive or begin with <code>0</code>. Note that a value of <code>0</code> is the default, and therefore is not present in lexicographer files.</p>
<dt><i>p_cnt</i></p>
<dd>Three digit decimal integer indicating the number of pointers from this synset to other synsets. If <i>p_cnt</i> is <code>000</code> the synset has no pointers.</p>
<dt><i>ptr</i></p>
<dd>A pointer from this synset to another. <i>ptr</i> is of the form: </p>
<pre><i>pointer_symbol~~synset_offset~~pos~~source/target</i></pre>
<p>where <i>synset_offset</i> is the byte offset of the target synset in the data file corresponding to <i>pos</i>. The <i>source/target</i> field distinguishes lexical and semantic pointers. It is a four byte field, containing two two-digit hexadecimal integers. The first two digits indicates the word number in the current (source) synset, the last two digits indicate the word number in the target synset. A value of <code>0000</code> means that <i>pointer_symbol</i> represents a semantic relation between the current (source) synset and the target synset indicated by <i>synset_offset</i>. A lexical relation between two words in different synsets is represented by non-zero values in the source and target word numbers. The first and last two bytes of this field indicate the word numbers in the source and target synsets, respectively, between which the relation holds. Word numbers are assigned to the <i>word</i> fields in a synset, from left to right, beginning with <code>1</code>. See <code><a href="/docs/linux/man/5-wninput/">wninput</a></code>(5) for a list of <i>pointer_symbol</i>s, and semantic and lexical pointer classifications.</p>
<dt><i>frames</i></p>
<dd>In <code>data.verb</code> only, a list of numbers corresponding to the generic verb sentence frames for <i>word</i>s in the synset. <i>frames</i> is of the form: </p>
<pre><i>f_cnt~~</i> <code>+</code> <i>~~f_num~~w_num~~[</i> <code>+</code> <i>~~f_num~~w_num...]</i></pre>
<p>where <i>f_cnt</i> a two digit decimal integer indicating the number of generic frames listed, <i>f_num</i> is a two digit decimal integer frame number, and <i>w_num</i> is a two digit hexadecimal integer indicating the word in the synset that the frame applies to. As with pointers, if this number is <code>00</code>, <i>f_num</i> applies to all <i>word</i>s in the synset. If non-zero, it is applicable only to the word indicated. Word numbers are assigned as described for pointers. Each <i>f_num~~w_num</i> pair is preceded by a <code>+</code>. See <code><a href="/docs/linux/man/5-wninput/">wninput</a></code>(5) for the text of the generic sentence frames.</p>
<dt><i>gloss</i></p>
<dd>Each synset contains a gloss. A <i>gloss</i> is represented as a vertical bar (<code>|</code>), followed by a text string that continues until the end of the line. The gloss may contain a definition, one or more example sentences, or both.</dl>
<h3>Sense Numbers</h3>
<p>Senses in WordNet are generally ordered from most to least frequently used, with the most common sense numbered <code>1</code>. Frequency of use is determined by the number of times a sense is tagged in the various semantic concordance texts. Senses that are not semantically tagged follow the ordered senses. The <i>tagsense_cnt</i> field for each entry in the <code>index.</code><i>pos</i> files indicates how many of the senses in the list have been tagged. The <code><a href="/docs/linux/man/5-cntlist/">cntlist</a></code>(5) file provided with the database lists the number of times each sense is tagged in the semantic concordances. The data from <code>cntlist</code> is used by <code><a href="/docs/linux/man/1-grind/">grind</a></code>(1) to order the senses of each word. When the <code>index</code>.<i>pos</i> files are generated, the <i>synset_offset</i>s are output in sense number order, with sense 1 first in the list. Senses with the same number of semantic tags are assigned unique but consecutive sense numbers. The WordNet <font SIZE="-1"><code>OVERVIEW</code></font> search displays all senses of the specified word, in all syntactic categories, and indicates which of the senses are represented in the semantically tagged texts.</p>
<h3>Exception List File Format</h3>
<p>Exception lists are alphabetized lists of inflected forms of words and their base forms. The first field of each line is an inflected form, followed by a space separated list of one or more base forms of the word. There is one exception list file for each syntactic category. Note that the noun and verb exception lists were automatically generated from a machine-readable dictionary, and contain many words that are not in WordNet. Also, for many of the inflected forms, base forms could be easily derived using the standard rules of detachment programmed into Morphy (See <code><a href="/docs/linux/man/7-morph/">morph</a></code>(7)). These anomalies are allowed to remain in the exception list files, as they do no harm.</p>
<h3>Verb Example Sentences</h3>
<p>For some verb senses, example sentences illustrating the use of the verb sense can be displayed. Each line of the file <code>sentidx.vrb</code> contains a <i>sense_key</i> followed by a space and a comma separated list of example sentence template numbers, in decimal. The file <code>sents.vrb</code> lists all of the example sentence templates. Each line begins with the template number followed by a space. The rest of the line is the text of a template example sentence, with <code>%s</code> used as a placeholder in the text for the verb. Both files are sorted alphabetically so that the <i>sense_key</i> and template sentence number can be used as indices, via <code><a href="/docs/linux/man/3-binsrch/">binsrch</a></code>(3), into the appropriate file. When a request for <font SIZE="-1"><code>FRAMES</code></font> is made, the WordNet search code looks for the sense in <code>sentidx.vrb</code>. If found, the sentence template(s) listed is retrieved from <code>sents.vrb</code>, and the <code>%s</code> is replaced with the verb. If the sense is not found, the applicable generic sentence frame(s) listed in <i>frames</i> is displayed.</p>
<h2>Notes</h2>
<p>Information in the <code>data.</code><i>pos</i> and <code>index.</code><i>pos</i> files represents all of the word senses and synsets in the WordNet database. The <i>word</i>, <i>lex_id</i>, and <i>lex_filenum</i> fields together uniquely identify each word sense in WordNet. These can be encoded in a <i>sense_key</i> as described in <code><a href="/docs/linux/man/5-senseidx/">senseidx</a></code>(5). Each synset in the database can be uniquely identified by combining the <i>synset_offset</i> for the synset with a code for the syntactic category (since it is possible for synsets in different <code>data.</code><i>pos</i> files to have the same <i>synset_offset</i>). </p>
<p> The WordNet system provide both command line and window-based browser interfaces to the database. Both interfaces utilize a common library of search and morphology code. The source code for the library and interfaces is included in the WordNet package. See <code><a href="/docs/linux/man/3-wnintro/">wnintro</a></code>(3) for an overview of the WordNet source code.</p>
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
<dt><code>index.</code><i>pos</i></p>
<dd>database index files</p>
<dt><code>data.</code><i>pos</i></p>
<dd>database data files</p>
<dt><code>*.vrb</code></p>
<dd>files of sentences illustrating the use of verbs</p>
<dt><i>pos</i>.exc</p>
<dd>morphology exception lists</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-grind/">grind</a></code>(1), <code><a href="/docs/linux/man/1-wn/">wn</a></code>(1), <code><a href="/docs/linux/man/1-wnb/">wnb</a></code>(1), <code><a href="/docs/linux/man/3-wnintro/">wnintro</a></code>(3), <code><a href="/docs/linux/man/3-binsrch/">binsrch</a></code>(3), <code><a href="/docs/linux/man/5-wnintro/">wnintro</a></code>(5), <code><a href="/docs/linux/man/5-cntlist/">cntlist</a></code>(5), <code><a href="/docs/linux/man/5-lexnames/">lexnames</a></code>(5), <code><a href="/docs/linux/man/5-senseidx/">senseidx</a></code>(5), <code><a href="/docs/linux/man/5-wninput/">wninput</a></code>(5), <code><a href="/docs/linux/man/7-morphy/">morphy</a></code>(7), <code><a href="/docs/linux/man/7-wngloss/">wngloss</a></code>(7), <code><a href="/docs/linux/man/7-wngroups/">wngroups</a></code>(7), <code><a href="/docs/linux/man/7-wnstats/">wnstats</a></code>(7). </p>
