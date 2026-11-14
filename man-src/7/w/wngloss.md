---
title: "wngloss(7)"
name: "wngloss"
section: "7"
letter: "w"
url: "/docs/linux/man/7-wngloss/"
description: "wngloss – glossary of terms used in WordNet system"
---

<p>wngloss &#8211; glossary of terms used in WordNet system</p>
<h2>Description</h2>
<p>The <i>WordNet Reference Manual</i> consists of Unix-style manual pages divided into sections as follows: </p>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>Section</code></td>
<td ALIGN=center><code>Description</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>1</td>
<td>WordNet User Commands
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>3</td>
<td>WordNet Library Functions
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>5</td>
<td>WordNet File Formats
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>7</td>
<td>Miscellaneous Information about WordNet
</td>
</tr>
</table>
</table>
<p></center></p>
<h3>System Description</h3>
<p>The WordNet system consists of lexicographer files, code to convert these files into a database, and search routines and interfaces that display information from the database. The lexicographer files organize nouns, verbs, adjectives and adverbs into groups of synonyms, and describe relations between synonym groups. <code><a href="/docs/linux/man/1-grind/">grind</a></code>(1) converts the lexicographer files into a database that encodes the relations between the synonym groups. The different interfaces to the WordNet database utilize a common library of search routines to display these relations. Note that the lexicographer files and <code><a href="/docs/linux/man/1-grind/">grind</a></code>(1) program are not generally distributed.</p>
<h3>Database Organization</h3>
<p>Information in WordNet is organized around logical groupings called synsets. Each synset consists of a list of synonymous words or collocations (eg. <code>&quot;fountain pen&quot;</code>, <code>&quot;take in&quot;</code>), and pointers that describe the relations between this synset and other synsets. A word or collocation may appear in more than one synset, and in more than one part of speech. The words in a synset are grouped such that they are interchangeable in some context. </p>
<p> Two kinds of relations are represented by pointers: lexical and semantic. Lexical relations hold between semantically related word forms; semantic relations hold between word meanings. These relations include (but are not limited to) hypernymy/hyponymy (superordinate/subordinate), antonymy, entailment, and meronymy/holonymy. </p>
<p> Nouns and verbs are organized into hierarchies based on the hypernymy/hyponymy relation between synsets. Additional pointers are be used to indicate other relations. </p>
<p> Adjectives are arranged in clusters containing head synsets and satellite synsets. Each cluster is organized around antonymous pairs (and occasionally antonymous triplets). The antonymous pairs (or triplets) are indicated in the head synsets of a cluster. Most head synsets have one or more satellite synsets, each of which represents a concept that is similar in meaning to the concept represented by the head synset. One way to think of the adjective cluster organization is to visualize a wheel, with a head synset as the hub and satellite synsets as the spokes. Two or more wheels are logically connected via antonymy, which can be thought of as an axle between the wheels. </p>
<p> Pertainyms are relational adjectives and do not follow the structure just described. Pertainyms do not have antonyms; the synset for a pertainym most often contains only one word or collocation and a lexical pointer to the noun that the adjective is &quot;pertaining to&quot;. Participial adjectives have lexical pointers to the verbs that they are derived from. </p>
<p> Adverbs are often derived from adjectives, and sometimes have antonyms; therefore the synset for an adverb usually contains a lexical pointer to the adjective from which it is derived. </p>
<p> See <code><a href="/docs/linux/man/5-wndb/">wndb</a></code>(5) for a detailed description of the database files and how the data are represented.</p>
<h2>Glossary Of Terms</h2>
<p>Many terms used in the <i>WordNet Reference Manual</i> are unique to the WordNet system. Other general terms have specific meanings when used in the WordNet documentation. Definitions for many of these terms are given to help with the interpretation and understanding of the reference manual, and in the use of the WordNet system. </p>
<p> In following definitions <code>word</code> is used in place of <code>word or collocation</code>.</p>
<dl>
<dt><code>adjective cluster</code></p>
<dd>A group of adjective synsets that are organized around antonymous pairs or triplets. An adjective cluster contains two or more <code>head synsets</code> which represent antonymous concepts. Each head synset has one or more <code>satellite synsets</code>.</p>
<dt><code>attribute</code></p>
<dd>A noun for which adjectives express values. The noun <code>weight</code> is an attribute, for which the adjectives <code>light</code> and <code>heavy</code> express values.</p>
<dt><code>base form</code></p>
<dd>The base form of a word or collocation is the form to which inflections are added.</p>
<dt><code>basic synset</code></p>
<dd>Syntactically, same as <code>synset</code>. Term is used in <code><a href="/docs/linux/man/5-wninput/">wninput</a></code>(5) to help explain differences in entering synsets in lexicographer files.</p>
<dt><code>collocation</code></p>
<dd>A collocation in WordNet is a string of two or more words, connected by spaces or hyphens. Examples are: <code>man-eating~shark</code>, <code>blue-collar</code>, <code>depend~on</code>, <code>line~of~products</code>. In the database files spaces are represented as underscore (<code>_</code>) characters.</p>
<dt><code>coordinate</code></p>
<dd>Coordinate terms are nouns or verbs that have the same <code>hypernym</code>.</p>
<dt><code>cross-cluster pointer</code></p>
<dd>A <code>semantic pointer</code> from one adjective cluster to another.</p>
<dt><code>derivationally related forms</code></p>
<dd>Terms in different syntactic categories that have the same root form and are semantically related.</p>
<dt><code>direct antonyms</code></p>
<dd>A pair of words between which there is an associative bond resulting from their frequent co-occurrence. In <code>adjective clusters</code>, direct antonyms appears only in <code>head synsets</code>.</p>
<dt><code>domain</code></p>
<dd>A topical classification to which a synset has been linked with a CATEGORY, REGION or USAGE pointer.</p>
<dt><code>domain term</code></p>
<dd>A synset belonging to a topical class. A domain term is further identified as being a CATEGORY_TERM, REGION_TERM or USAGE_TERM.</p>
<dt><code>entailment</code></p>
<dd>A verb <code>X</code> entails <code>Y</code> if <code>X</code> cannot be done unless <code>Y</code> is, or has been, done.</p>
<dt><code>exception list</code></p>
<dd>Morphological transformations for words that are not regular and therefore cannot be processed in an algorithmic manner.</p>
<dt><code>group</code></p>
<dd>Verb senses that similar in meaning and have been manually grouped together.</p>
<dt><code>gloss</code></p>
<dd>Each synset contains <code>gloss</code> consisting of a definition and optionally example sentences.</p>
<dt><code>head synset</code></p>
<dd>Synset in an adjective <code>cluster</code> containing at least one word that has a <code>direct antonym</code>.</p>
<dt><code>holonym</code></p>
<dd>The name of the whole of which the meronym names a part. <code>Y</code> is a holonym of <code>X</code> if <code>X</code> is a part of <code>Y</code>.</p>
<dt><code>hypernym</code></p>
<dd>The generic term used to designate a whole class of specific instances. <code>Y</code> is a hypernym of <code>X</code> if <code>X</code> is a (kind of) <code>Y</code>.</p>
<dt><code>hyponym</code></p>
<dd>The specific term used to designate a member of a class. <code>X</code> is a hyponym of <code>Y</code> if <code>X</code> is a (kind of) <code>Y</code>.</p>
<dt><code>indirect antonym</code></p>
<dd>An adjective in a <code>satellite synset</code> that does not have a <code>direct antonym</code> has an indirect antonyms via the direct antonym of the <code>head synset</code>.</p>
<dt><code>instance</code></p>
<dd>A proper noun that refers to a particular, unique referent (as distinguished from nouns that refer to classes). This is a specific form of hyponym.</p>
<dt><code>lemma</code></p>
<dd>Lower case ASCII text of word as found in the WordNet database index files. Usually the <code>base form</code> for a word or collocation.</p>
<dt><code>lexical pointer</code></p>
<dd>A lexical pointer indicates a relation between words in synsets (word forms).</p>
<dt><code>lexicographer file</code></p>
<dd>Files containing the raw data for WordNet synsets, edited by lexicographers, that are input to the <code>grind</code> program to generate a WordNet database.</p>
<dt><code>lexicographer id (lex id)</code></p>
<dd>A decimal integer that, when appended onto <code>lemma</code>, uniquely identifies a sense within a lexicographer file.</p>
<dt><code>monosemous</code></p>
<dd>Having only one sense in a syntactic category.</p>
<dt><code>meronym</code></p>
<dd>The name of a constituent part of, the substance of, or a member of something. <code>X</code> is a meronym of <code>Y</code> if <code>X</code> is a part of <code>Y</code>.</p>
<dt><code>part of speech</code></p>
<dd>WordNet defines &quot;part of speech&quot; as either noun, verb, adjective, or adverb. Same as <code>syntactic category</code>.</p>
<dt><code>participial adjective</code></p>
<dd>An adjective that is derived from a verb.</p>
<dt><code>pertainym</code></p>
<dd>A relational adjective. Adjectives that are pertainyms are usually defined by such phrases as &quot;of or pertaining to&quot; and do not have antonyms. A pertainym can point to a noun or another pertainym.</p>
<dt><code>polysemous</code></p>
<dd>Having more than one sense in a syntactic category.</p>
<dt><code>polysemy count</code></p>
<dd>Number of senses of a word in a syntactic category, in WordNet.</p>
<dt><code>postnominal</code></p>
<dd>A postnominal adjective occurs only immediately following the noun that it modifies.</p>
<dt><code>predicative</code></p>
<dd>An adjective that can be used only in predicate positions. If <code>X</code> is a predicate adjective, it can only be used in such phrases as &quot;it is <code>X</code>&quot; and never prenominally.</p>
<dt><code>prenominal</code></p>
<dd>An adjective that can occur only before the noun that it modifies: it cannot be used predicatively.</p>
<dt><code>satellite synset</code></p>
<dd>Synset in an adjective <code>cluster</code> representing a concept that is similar in meaning to the concept represented by its <code>head synset</code>.</p>
<dt><code>semantic concordance</code></p>
<dd>A textual corpus (e.g. the Brown Corpus) and a lexicon (e.g. WordNet) so combined that every substantive word in the text is linked to its appropriate sense in the lexicon via a <code>semantic tag</code>.</p>
<dt><code>semantic tag</code></p>
<dd>A pointer from a word in a text file to a specific sense of that word in the WordNet database. A semantic tag in a semantic concordance is represented by a <code>sense key</code>.</p>
<dt><code>semantic pointer</code></p>
<dd>A semantic pointer indicates a relation between synsets (concepts).</p>
<dt><code>sense</code></p>
<dd>A meaning of a word in WordNet. Each sense of a word is in a different <code>synset</code>.</p>
<dt><code>sense key</code></p>
<dd>Information necessary to find a sense in the WordNet database. A sense key combines a <code>lemma</code> field and codes for the synset type, lexicographer id, lexicographer file number, and information about a satellite&#8217;s <code>head synset</code>, if required. See <code><a href="/docs/linux/man/5-senseidx/">senseidx</a></code>(5) for a description of the format of a sense key.</p>
<dt><code>subordinate</code></p>
<dd>Same as <code>hyponym</code>.</p>
<dt><code>superordinate</code></p>
<dd>Same as <code>hypernym</code>.</p>
<dt><code>synset</code></p>
<dd>A synonym set; a set of words that are interchangeable in some context without changing the truth value of the preposition in which they are embedded.</p>
<dt><code>troponym</code></p>
<dd>A verb expressing a specific manner elaboration of another verb. <code>X</code> is a troponym of <code>Y</code> if <code>to X</code> is <code>to Y</code> in some manner.</p>
<dt><code>unique beginner</code></p>
<dd>A noun synset with no <code>superordinate</code>. </p>
</dl>
