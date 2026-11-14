---
title: "wninput(5)"
name: "wninput"
section: "5"
letter: "w"
url: "/docs/linux/man/5-wninput/"
description: "noun.suffix, verb.suffix, adj.suffix, adv.suffix – WordNet lexicographer files that are input to grind(1)"
---

<p>noun.<i>suffix</i>, verb.<i>suffix</i>, adj.<i>suffix</i>, adv.<i>suffix</i> &#8211; WordNet lexicographer files that are input to <code><a href="/docs/linux/man/1-grind/">grind</a></code>(1)</p>
<h2>Description</h2>
<p>WordNet&#8217;s source files are written by lexicographers. They are the product of a detailed relational analysis of lexical semantics: a variety of lexical and semantic relations are used to represent the organization of lexical knowledge. Two kinds of building blocks are distinguished in the source files: word forms and word meanings. Word forms are represented in their familiar orthography; word meanings are represented by synonym sets (<i>synset</i>s) &#8211; lists of synonymous word forms that are interchangeable in some context. Two kinds of relations are recognized: lexical and semantic. Lexical relations hold between word forms; semantic relations hold between word meanings. Lexicographer files correspond to the syntactic categories implemented in WordNet &#8211; noun, verb, adjective and adverb. All of the synsets in a lexicographer file are in the same syntactic category. Each synset consists of a list of synonymous words or collocations (eg. <code>&quot;fountain pen&quot;</code>, <code>&quot;take in&quot;</code>), and pointers that describe the relations between this synset and other synsets. These relations include (but are not limited to) hypernymy/hyponymy, antonymy, entailment, and meronymy/holonymy. A word or collocation may appear in more than one synset, and in more than one part of speech. Each use of a word in a synset represents a sense of that word in the part of speech corresponding to the synset. Adjectives may be organized into clusters containing head synsets and satellite synsets. Adverbs generally point to the adjectives from which they are derived. See <code><a href="/docs/linux/man/7-wngloss/">wngloss</a></code>(7) for a glossary of WordNet terminology and a discussion of the database&#8217;s content and logical organization.</p>
<h3>Lexicographer File Names</h3>
<p>The names of the lexicographer files are of the form:</p>
<dl>
<dd><i>pos</i>.<i>suffix</i></dl>
<p> where <i>pos</i> is either <code>noun</code>, <code>verb</code>, <code>adj</code> or <code>adv</code>. <i>suffix</i> may be used to organize groups of synsets into different files, for example <code>noun.animal</code> and <code>noun.plant</code>. See <code><a href="/docs/linux/man/5-lexnames/">lexnames</a></code>(5) for a list of lexicographer file names that are used in building WordNet.</p>
<h3>Pointers</h3>
<p>Pointers are used to represent the relations between the words in one synset and another. Semantic pointers represent relations between word meanings, and therefore pertain to all of the words in the source and target synsets. Lexical pointers represent relations between word forms, and pertain only to specific words in the source and target synsets. The following pointer types are usually used to indicate lexical relations: Antonym, Pertainym, Participle, Also See, Derivationally Related. The remaining pointer types are generally used to represent semantic relations. A relation from a source to a target synset is formed by specifying a word from the target synset in the source synset, followed by the <i>pointer_symbol</i> indicating the pointer type. The location of a pointer within a synset defines it as either lexical or semantic. The <font SIZE="-1"><code>&quot;Lexicographer File Format&quot;</code></font> section describes the syntax for entering a semantic pointer, and <font SIZE="-1"><code>&quot;Word Syntax&quot;</code></font> describes the syntax for entering a lexical pointer. Although there are many pointer types, only certain types of relations are permitted between synsets of each syntactic category. The <i>pointer_symbol</i>s for nouns are:</p>
<dl>
<dd>
<pre><code>!</code> Antonym
<code>@</code> Hypernym
<code>@i</code> Instance Hypernym
<code>&asymp;</code> Hyponym
<code>&asymp;i</code> Instance Hyponym
<code>#m</code> Member holonym
<code>#s</code> Substance holonym
<code>#p</code> Part holonym
<code>%m</code> Member meronym
<code>%s</code> Substance meronym
<code>%p</code> Part meronym
<code>=</code> Attribute
<code>+</code> Derivationally related form 
<code>;c</code> Domain of synset - TOPIC
<code>-c</code> Member of this domain - TOPIC
<code>;r</code> Domain of synset - REGION
<code>-r</code> Member of this domain - REGION
<code>;u</code> Domain of synset - USAGE
<code>-u</code> Member of this domain - USAGE
</dl></pre>
<p>The <i>pointer_symbol</i>s for verbs are:</p>
<dl>
<dd>
<pre><code>!</code> Antonym
<code>@</code> Hypernym
<code>&asymp;</code> Hyponym
<code>*</code> Entailment
<code>&gt;</code> Cause
<code>^</code> Also see
<code>$</code> Verb Group
<code>+</code> Derivationally related form 
<code>;c</code> Domain of synset - TOPIC
<code>;r</code> Domain of synset - REGION
<code>;u</code> Domain of synset - USAGE</pre>
</dl>
<p> The <i>pointer_symbol</i>s for adjectives are:</p>
<dl>
<dd>
<pre><code>!</code> Antonym
<code>&amp;</code> Similar to
<code>&lt;</code> Participle of verb
<code>\</code> Pertainym (pertains to noun)
<code>=</code> Attribute
<code>^</code> Also see
<code>;c</code> Domain of synset - TOPIC
<code>;r</code> Domain of synset - REGION
<code>;u</code> Domain of synset - USAGE</pre>
</dl>
<p> The <i>pointer_symbol</i>s for adverbs are:</p>
<dl>
<dd>
<pre><code>!</code> Antonym
<code>\</code> Derived from adjective
<code>;c</code> Domain of synset - TOPIC
<code>;r</code> Domain of synset - REGION
<code>;u</code> Domain of synset - USAGE</pre>
</dl>
<p> Many pointer types are reflexive, meaning that if a synset contains a pointer to another synset, the other synset should contain a corresponding reflexive pointer. <code><a href="/docs/linux/man/1-grind/">grind</a></code>(1) automatically inserts missing reflexive pointers for the following pointer types: <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>Pointer</code></td>
<td ALIGN=center><code>Reflect</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Antonym</td>
<td>Antonym
</td>
</tr>
<tr VALIGN=top>
<td>Hyponym</td>
<td>Hypernym
</td>
</tr>
<tr VALIGN=top>
<td>Hypernym</td>
<td>Hyponym
</td>
</tr>
<tr VALIGN=top>
<td>Instance Hyponym</td>
<td>Instance Hypernym
</td>
</tr>
<tr VALIGN=top>
<td>Instance Hypernym</td>
<td>Instance Hyponym
</td>
</tr>
<tr VALIGN=top>
<td>Holonym</td>
<td>Meronym
</td>
</tr>
<tr VALIGN=top>
<td>Meronym</td>
<td>Holonym
</td>
</tr>
<tr VALIGN=top>
<td>Similar to</td>
<td>Similar to
</td>
</tr>
<tr VALIGN=top>
<td>Attribute</td>
<td>Attribute
</td>
</tr>
<tr VALIGN=top>
<td>Verb Group</td>
<td>Verb Group
</td>
</tr>
<tr VALIGN=top>
<td>Derivationally Related</td>
<td>Derivationally Related
</td>
</tr>
<tr VALIGN=top>
<td>Domain of synset</td>
<td>Member of Doman
</td>
</tr>
</table>
</table>
<p></center></p>
<h3>Verb Frames</h3>
<p>Each verb synset contains a list of generic sentence frames illustrating the types of simple sentences in which the verbs in the synset can be used. For some verb senses, example sentences illustrating actual uses of the verb are provided. (See <font SIZE="-1"><code>&quot;Verb Example Sentences&quot;</code></font> in <code><a href="/docs/linux/man/5-wndb/">wndb</a></code>(5).) Whenever there is no example sentence, the generic sentence frames specified by the lexicographer are used. The generic sentence frames are entered in a synset as a comma-separated list of integer frame numbers. The following list is the text of the generic frames, preceded by their frame numbers:</p>
<dl>
<dd>
<pre>1 Something ----s
2 Somebody ----s
3 It is ----ing
4 Something is ----ing PP
5 Something ----s something Adjective/Noun
6 Something ----s Adjective/Noun
7 Somebody ----s Adjective
8 Somebody ----s something
9 Somebody ----s somebody
10 Something ----s somebody
11 Something ----s something
12 Something ----s to somebody
13 Somebody ----s on something
14 Somebody ----s somebody something
15 Somebody ----s something to somebody
16 Somebody ----s something from somebody
17 Somebody ----s somebody with something
18 Somebody ----s somebody of something
19 Somebody ----s something on somebody
20 Somebody ----s somebody PP
21 Somebody ----s something PP
22 Somebody ----s PP
23 Somebody's (body part) ----s
24 Somebody ----s somebody to INFINITIVE
25 Somebody ----s somebody INFINITIVE
26 Somebody ----s that CLAUSE
27 Somebody ----s to somebody
28 Somebody ----s to INFINITIVE
29 Somebody ----s whether INFINITIVE
30 Somebody ----s somebody into V-ing something
31 Somebody ----s something with something
32 Somebody ----s INFINITIVE
33 Somebody ----s VERB-ing
34 It ----s that CLAUSE
35 Something ----s INFINITIVE</pre>
</dl>
<h3>Lexicographer File Format</h3>
<p>Synsets are entered one per line, and each line is terminated with a newline character. A line containing a synset may be as long as necessary, but no newlines can be entered within a synset. Within a synset, spaces or tabs may be used to separate entities. Items enclosed in italicized square brackets may not be present. The general synset syntax is: </p>
<pre><code>{ ~~words~~pointers~~ ( ~gloss~ )~~}</code></pre>
<p> Synsets of this form are valid for all syntactic categories except verb, and are referred to as basic synsets. At least one <i>word</i> and a <i>gloss</i> are required to form a valid synset. Pointers entered following all the <i>words</i> in a synset represent semantic relations between all the words in the source and target synsets. For verbs, the basic synset syntax is defined as follows: </p>
<pre><code>{ ~~words~~pointers~~frames~~ ( ~gloss~ )~~}</code></pre>
<p> Adjective may be organized into clusters containing one or more head synsets and optional satellite synsets. Adjective clusters are of the form:</p>
<dl>
<dd>
<pre><code>[
</code><i>head synset
[satellite synsets]
[-]
[additional head/satellite synsets]
</i><code>]</code></pre>
</dl>
<p> Each adjective cluster is enclosed in square brackets, and may have one or more parts. Each part consists of a head synset and optional satellite synsets that are conceptually similar to the head synset&#8217;s meaning. Parts of a cluster are separated by one or more hyphens (<code>&#8211;</code>) on a line by themselves, with the terminating square bracket following the last synset. Head and satellite synsets follow the syntax of basic synsets, however a &quot;Similar to&quot; pointer must be specified in a head synset for each of its satellite synsets. Most adjective clusters contain two antonymous parts. See <code><a href="/docs/linux/man/7-wngloss/">wngloss</a></code>(7) for a discussion of adjective clusters, and <font SIZE="-1"><code>&quot;Special Adjective Syntax&quot;</code></font> for more information on adjective cluster syntax. Synsets for relational adjectives (pertainyms) and participial adjectives do not adhere to the cluster structure. They use the basic synset syntax. Comments can be entered in a lexicographer file by enclosing the text of the comment in parentheses. Note that comments <code>cannot</code> appear within a synset, as parentheses within a synset have an entirely different meaning (see <font SIZE="-1"><code>&quot;Gloss Syntax&quot;</code></font> ). However, entire synsets (or adjective clusters) can be &quot;commented out&quot; by enclosing them in parentheses. This is often used by the lexicographers to verify the syntax of files under development or to leave a note to oneself while working on entries.</p>
<h3>Word Syntax</h3>
<p>A synset must have at least one word, and the words of a synset must appear after the opening brace and before any other synset constructs. A word may be entered in either the simple word or word/pointer syntax. A simple word is of the form:</p>
<dl>
<dd>
<pre><i>word[</i> <code>(</code> <i>marker</i> <code>)</code> <i>][lex_id]</i> <code>,</code></pre>
</dl>
<p> <i>word</i> may be entered in any combination of upper and lower case unless it is in an adjective cluster. A collocation is entered by joining the individual words with an underscore character (<code>_</code>). Numbers (integer or real) may be entered, either by themselves or as part of a word string, by following the number with a double quote (<code>&quot;</code>). See <font SIZE="-1"><code>&quot;Special Adjective Syntax&quot;</code></font> for a description of adjective clusters and markers. <i>word</i> may be followed by an integer <i>lex_id</i> from <code>1</code> to <code>15</code>. The <i>lex_id</i> is used to distinguish different senses of the same word within a lexicographer file. The lexicographer assigns <i>lex_id</i> values, usually in ascending order, although there is no requirement that the numbers be consecutive. The default is <code>0</code>, and does not have to be specified. A <i>lex_id</i> must be used on pointers if the desired sense has a non-zero <i>lex_id</i> in its synset specification. Word/pointer syntax is of the form:</p>
<dl>
<dd>
<pre><code>[~~</code> <i>word[</i> <code>(</code> <i>marker</i> <code>)</code> <i>][lex_id]</i> <code>,</code> <i>~~pointers~~</i> <code>]</code></pre>
</dl>
<p> This syntax is used when one or more pointers correspond only to the specific word in the word/pointer set, rather than all the words in the synset, and represents a lexical relation. Note that a word/pointer set appears within a synset, therefore the square brackets used to enclose it are treated differently from those used to define an adjective cluster. Only one word can be specified in each word/pointer set, and any number of pointers may be included. A synset can have any number of word/pointer sets. Each is treated by <code><a href="/docs/linux/man/1-grind/">grind</a></code>(1) essentially as a <i>word</i>, so they all must appear before any synset <i>pointers</i> representing semantic relations. For verbs, the word/pointer syntax is extended in the following manner to allow the user to specify generic sentence frames that, like pointers, correspond only to a specific word, rather than all the words in the synset. In this case, <i>pointers</i> are optional.</p>
<dl>
<dd>
<pre><code>[~~</code> <i>word</i> <code>,</code> ~~<i>[pointers]~~frames~~</i> <code>]</code></pre>
</dl>
<h3>Pointer Syntax</h3>
<p>Pointers are optional in synsets. If a pointer is specified outside of a word/pointer set, the relation is applied to all of the words in the synset, including any words specified using the word/pointer syntax. This indicates a semantic relation between the meanings of the words in the synsets. If specified within a word/pointer set, the relation corresponds only to the word in the set and represents a lexical relation. A pointer is of the form:</p>
<dl>
<dd>
<pre><i>[lex_filename</i><code>:</code> <i>]word[lex_id]</i><code>,</code><i>pointer_symbol</i></pre>
</dl>
<p> or:</p>
<dl>
<dd>
<pre><i>[lex_filename</i><code>:</code> <i>]word[lex_id]</i><code>^</code><i>word[lex_id]</i><code>,</code><i>pointer_symbol</i></pre>
</dl>
<p> For pointers, <i>word</i> indicates a word in another synset. When the second form of a pointer is used, the first <i>word</i> indicates a word in a head synset, and the second is a word in a satellite of that cluster. <i>word</i> may be followed by a <i>lex_id</i> that is used to match the pointer to the correct target synset. The synset containing <i>word</i> may reside in another lexicographer file. In this case, <i>word</i> is preceded by <i>lex_filename</i> as shown. See <font SIZE="-1"><code>&quot;Pointers&quot;</code></font> for a list of <i>pointer_symbol</i>s and their meanings.</p>
<h3>Verb Frame List Syntax</h3>
<p>Frame numbers corresponding to generic sentence frames must be entered in each verb synset. If a frame list is specified outside of a word/pointer set, the verb frames in the list apply to all of the words in the synset, including any words specified using the word/pointer syntax. If specified within a word/pointer set, the verb frames in the list correspond only to the word in the set. A frame number list is entered as follows:</p>
<dl>
<dd><code>frames:</code>~~<i>f_num</i>[<code>,</code><i>f_num&#8230;]</i></dl>
<p> Where <i>f_num</i> specifies a generic frame number. See <font SIZE="-1"><code>&quot;Verb Frames&quot;</code></font> for a list of generic sentences and their corresponding frame numbers.</p>
<h3>Gloss Syntax</h3>
<p>A gloss is included in all synsets. The lexicographer may enter a text string of any length desired. A gloss is simply a string enclosed in parentheses with no embedded carriage returns. It provides a definition of what the synset represents and/or example sentences.</p>
<h3>Special Adjective Syntax</h3>
<p>The syntax for representing antonymous adjective synsets requires several additional conditions. The first word of a head synset <code>must</code> be entered in upper case, and can be thought of as the head word of the head synset. The <i>word</i> part of a pointer from one head synset to another head synset within the same cluster (usually an antonym) must also be entered in upper case. Usually antonymous adjectives are entered using the word/pointer syntax described in <font SIZE="-1"><code>&quot;Word Syntax&quot;</code></font> to indicate a lexical relation. There is no restriction on the number of parts that a cluster may have, and some clusters have three parts, representing antonymous triplets, such as <code>solid</code>, <code>liquid</code>, and <code>gas</code>. A cross-cluster pointer may be specified, allowing a head or satellite synset to point to a head synset in a different cluster. A cross-cluster pointer is indicated by entering the <i>word</i> part of the pointer in upper case. An adjective may be annotated with a syntactic marker indicating a limitation on the syntactic position the adjective may have in relation to noun that it modifies. If so marked, the marker appears between the word and its following comma. If a <i>lex_id</i> is specified, the marker immediately follows it. The syntactic markers are:</p>
<dl>
<dd>
<pre><code>(p)</code> predicate position
<code>(a)</code> prenominal (attributive) position
<code>(ip)</code> immediately postnominal position </pre>
</dl>
<h2>Examples</h2>
<p><i>(Note that these are hypothetical examples not found in the WordNet lexicographer files.)</i> </p>
<p> Sample noun synsets:</p>
<dl>
<dd>
<pre>{ canine, [ dog1, cat,! ] pooch, canid,@ }
{ collie, dog1,@ (large multi-colored dog with pointy nose) }
{ hound, hunting_dog, pack,#m dog1,@ }
{ dog, }</pre>
</dl>
<p> Sample verb synsets:</p>
<dl>
<dd>
<pre>{ [ confuse, clarify,! frames: 1 ] blur, obscure, frames: 8, 10 }
{ [ clarify, confuse,! ] make_clear, interpret,@ frames: 8 }
{ interpret, construe, understand,@ frames: 8 }</pre>
</dl>
<p> Sample adjective clusters:</p>
<dl>
<dd>
<pre>[
{ [ HOT, COLD,! ] lukewarm(a), TEPID,^ (hot to the touch) }
{ warm, }
-
{ [ COLD, HOT,! ] frigid, (cold to the touch) }
{ freezing, }
]</pre>
</dl>
<p> Sample adverb synsets:</p>
<dl>
<dd>
<pre>{ [ basically, adj.all:essential^basic,\ ] [ essentially, adj.all:basic^fundamental,\ ] ( by one's very nature )}
{ pointedly, adj.all:pungent^pointed,\ }
{ [ badly, adj.all:bad,\ well,! ] ill, (&quot;He was badly prepared&quot;) }</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-grind/">grind</a></code>(1), <code><a href="/docs/linux/man/5-wnintro/">wnintro</a></code>(5), <code><a href="/docs/linux/man/5-lexnames/">lexnames</a></code>(5), <code><a href="/docs/linux/man/5-wndb/">wndb</a></code>(5), <code><a href="/docs/linux/man/7-uniqbeg/">uniqbeg</a></code>(7), <code><a href="/docs/linux/man/7-wngloss/">wngloss</a></code>(7). Fellbaum, C. (1998), ed. <i>&quot;WordNet: An Electronic Lexical Database&quot;</i>. MIT Press, Cambridge, MA. </p>
