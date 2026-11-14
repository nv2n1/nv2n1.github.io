---
title: "senseidx(5)"
name: "senseidx"
section: "5"
letter: "s"
url: "/docs/linux/man/5-senseidx/"
description: "index.sense, sense.idx – WordNet’s sense index"
---

<p>index.sense, sense.idx &#8211; WordNet&#8217;s sense index</p>
<h2>Description</h2>
<p>The WordNet sense index provides an alternate method for accessing synsets and word senses in the WordNet database. It is useful to applications that retrieve synsets or other information related to a specific sense in WordNet, rather than all the senses of a word or collocation. It can also be used with tools like <code>grep</code> and Perl to find all senses of a word in one or more parts of speech. A specific WordNet sense, encoded as a <i>sense_key</i>, can be used as an index into this file to obtain its WordNet sense number, the database byte offset of the synset containing the sense, and the number of times it has been tagged in the semantic concordance texts. </p>
<p> Concatenating the <i>lemma</i> and <i>lex_sense</i> fields of a semantically tagged word (represented in a <code>&lt;wf~</code>&#8230;~<code>&gt;</code> attribute/value pair) in a semantic concordance file, using <code>%</code> as the concatenation character, creates the <i>sense_key</i> for that sense, which can in turn be used to search the sense index file. </p>
<p> A <i>sense_key</i> is the best way to represent a sense in semantic tagging or other systems that refer to WordNet senses. <i>sense_key</i>s are independent of WordNet sense numbers and <i>synset_offset</i>s, which vary between versions of the database. Using the sense index and a <i>sense_key</i>, the corresponding synset (via the <i>synset_offset</i>) and WordNet sense number can easily be obtained. A mapping from noun <i>sense_key</i>s in WordNet 1.6 to corresponding 2.0 <i>sense_key</i>s is provided with version 2.0, and is described in <code><a href="/docs/linux/man/5-sensemap/">sensemap</a></code>(5). </p>
<p> See <code><a href="/docs/linux/man/5-wndb/">wndb</a></code>(5) for a thorough discussion of the WordNet database files.</p>
<h3>File Format</h3>
<p>The sense index file lists all of the senses in the WordNet database with each line representing one sense. The file is in alphabetical order, fields are separated by one space, and each line is terminated with a newline character. </p>
<p> Each line is of the form: </p>
<dl>
<dd><i>sense_key~~synset_offset~~sense_number~~tag_cnt</i></dl>
<p> <i>sense_key</i> is an encoding of the word sense. Programs can construct a sense key in this format and use it as a binary search key into the sense index file. The format of a <i>sense_key</i> is described below. </p>
<p> <i>synset_offset</i> is the byte offset that the synset containing the sense is found at in the database &quot;data&quot; file corresponding to the part of speech encoded in the <i>sense_key</i>. <i>synset_offset</i> is an 8 digit, zero-filled decimal integer, and can be used with <code><a href="/docs/linux/man/3-fseek/">fseek</a></code>(3) to read a synset from the data file. When passed to the WordNet library function <code>read_synset()</code> along with the syntactic category, a data structure containing the parsed synset is returned. </p>
<p> <i>sense_number</i> is a decimal integer indicating the sense number of the word, within the part of speech encoded in <i>sense_key</i>, in the WordNet database. See <code><a href="/docs/linux/man/5-wndb/">wndb</a></code>(5) for information about how sense numbers are assigned. </p>
<p> <i>tag_cnt</i> represents the decimal number of times the sense is tagged in various semantic concordance texts. A <i>tag_cnt</i> of <code>0</code> indicates that the sense has not been semantically tagged.</p>
<h3>Sense Key Encoding</h3>
<p>A <i>sense_key</i> is represented as: </p>
<dl>
<dd><i>lemma</i><code>%</code><i>lex_sense</i></dl>
<p> where <i>lex_sense</i> is encoded as: </p>
<dl>
<dd><i>ss_type</i><code>:</code><i>lex_filenum</i><code>:</code><i>lex_id</i><code>:</code><i>head_word</i><code>:</code><i>head_id</i></dl>
<p> <i>lemma</i> is the ASCII text of the word or collocation as found in the WordNet database index file corresponding to <i>pos</i>. <i>lemma</i> is in lower case, and collocations are formed by joining individual words with an underscore (<code>_</code>) character. </p>
<p> <i>ss_type</i> is a one digit decimal integer representing the synset type for the sense. See <font SIZE="-1"><code>&quot;Synset Type&quot;</code></font> below for a listing of the numbers corresponding to each synset type. </p>
<p> <i>lex_filenum</i> is a two digit decimal integer representing the name of the lexicographer file containing the synset for the sense. See <code><a href="/docs/linux/man/5-lexnames/">lexnames</a></code>(5) for the list of lexicographer file names and their corresponding numbers. </p>
<p> <i>lex_id</i> is a two digit decimal integer that, when appended onto <i>lemma</i>, uniquely identifies a sense within a lexicographer file. <i>lex_id</i> numbers usually start with <code>00</code>, and are incremented as additional senses of the word are added to the same file, although there is no requirement that the numbers be consecutive or begin with <code>00</code>. Note that a value of <code>00</code> is the default, and therefore is not present in lexicographer files. Only non-default <i>lex_id</i> values must be explicitly assigned in lexicographer files. See <code><a href="/docs/linux/man/5-wninput/">wninput</a></code>(5) for information on the format of lexicographer files. </p>
<p> <i>head_word</i> is only present if the sense is in an adjective satellite synset. It is the lemma of the first word of the satellite&#8217;s head synset. </p>
<p> <i>head_id</i> is a two digit decimal integer that, when appended onto <i>head_word</i>, uniquely identifies the sense of <i>head_word</i> within a lexicographer file, as described for <i>lex_id</i>. There is a value in this field only if <i>head_word</i> is present.</p>
<h3>Synset Type</h3>
<p>The synset type is encoded as follows: </p>
<dl>
<dd>
<pre><code>1</code> NOUN
<code>2</code> VERB
<code>3</code> ADJECTIVE
<code>4</code> ADVERB
<code>5</code> ADJECTIVE SATELLITE</pre>
</dl>
<h2>Notes</h2>
<p>For non-satellite senses the <i>head_word</i> and <i>head_id</i> fields have no values, however the field separator character (<code>:</code>) is present.</p>
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
<dt><code>index.sense</code></p>
<dd>sense index</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-binsrch/">binsrch</a></code>(3), <code><a href="/docs/linux/man/3-wnsearch/">wnsearch</a></code>(3), <code><a href="/docs/linux/man/5-lexnames/">lexnames</a></code>(5), <code><a href="/docs/linux/man/5-wnintro/">wnintro</a></code>(5), <code><a href="/docs/linux/man/5-sensemap/">sensemap</a></code>(5), <code><a href="/docs/linux/man/5-wndb/">wndb</a></code>(5), <code><a href="/docs/linux/man/5-wninput/">wninput</a></code>(5). </p>
