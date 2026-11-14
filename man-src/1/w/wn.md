---
title: "wn(1)"
name: "wn"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wn/"
description: "wn – command line interface to WordNet lexical database"
---

<h2>NAME</h2>
<p> wn &#8211; command line interface to WordNet lexical database</p>
<h2>SYNOPSIS</h2>
<p> <code>wn</code> [ <i>searchstr</i> ] [ <code>-h</code>] [ <code>-g</code> ] [ <code>-a</code> ] [ <code>-l</code> ] [ <code>-o</code> ] [ <code>-s</code> ] [ <code>-n</code><i>#</i> ] [ <i>search_option</i>&#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> <code>wn()</code> provides a command line interface to the WordNet database, allowing synsets and relations to be displayed as formatted text. For each word, different searches are provided, based on syntactic category and pointer types. Although only base forms of words are usually stored in WordNet, users may search for inflected forms. A morphological process is applied to the search string to generate a form that is present in WordNet. </p>
<p> The command line interface is often useful when writing scripts to extract information from the WordNet database. Post-processing of the output with various scripting tools can reformat the results as desired.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Print help text before search results.</p>
<dt><code>-g</code></p>
<dd> Display textual glosses associated with synsets.</p>
<dt><code>-a</code></p>
<dd> Display lexicographer file information.</p>
<dt><code>-o</code></p>
<dd> Display synset offset of each synset.</p>
<dt><code>-s</code></p>
<dd> Display each word&#8217;s sense numbers in synsets.</p>
<dt><code>-l</code></p>
<dd> Display the WordNet copyright notice, version number, and license.</p>
<dt><code>-n</code><i>#</i></p>
<dd> Perform search on sense number <i>#</i> only.</p>
<dt><code>-over</code></p>
<dd> Display overview of all senses of <i>searchstr</i> in all syntactic categories.</dl>
<h3>Search Options</h3>
<p> Note that the last letter of <i>search_option</i> generally denotes the part of speech that the search applies to: <code>n</code> for nouns, <code>v</code> for verbs, <code>a</code> for adjectives, and <code>r</code> for adverbs. Multiple searches may be done for <i>searchstr</i> with a single command by specifying all the appropriate search options. </p>
<dl>
<dt><code>-syns</code>(<i>n</i> | <i>v</i> | <i>a</i> | <i>r</i>)</p>
<dd> Display synonyms and immediate hypernyms of synsets containing <i>searchstr</i>. Synsets are ordered by estimated frequency of use. For adjectives, if <i>searchstr</i> is in a head synset, the cluster&#8217;s satellite synsets are displayed in place of hypernyms. If <i>searchstr</i> is in a satellite synset, its head synset is also displayed.</p>
<dt><code>-simsv</code></p>
<dd> Display verb synonyms and immediate hypernyms of synsets containing <i>searchstr</i>. Synsets are grouped by similarity of meaning.</p>
<dt><code>-ants</code>(<i>n</i> | <i>v</i> | <i>a</i> | <i>r</i>)</p>
<dd> Display synsets containing antonyms of <i>searchstr</i>. For adjectives, if <i>searchstr</i> is in a head synset, <i>searchstr</i> has a direct antonym. The head synset for the direct antonym is displayed along with the direct antonym&#8217;s satellite synsets. If <i>searchstr</i> is in a satellite synset, <i>searchstr</i> has an indirect antonym via the head synset, which is displayed.</p>
<dt><code>-faml</code>(<i>n</i> | <i>v</i> | <i>a</i> | <i>r</i>)</p>
<dd> Display familiarity and polysemy information for <i>searchstr</i>.</p>
<dt><code>-hype</code>(<i>n</i> | <i>v</i>)</p>
<dd> Recursively display hypernym (superordinate) tree for <i>searchstr</i> (<i>searchstr</i> <i>IS A KIND OF _____</i> relation).</p>
<dt><code>-hypo</code>(<i>n</i> | <i>v</i>)</p>
<dd> Display immediate hyponyms (subordinates) for <i>searchstr</i> (<i>_____ IS A KIND OF</i> <i>searchstr</i> relation).</p>
<dt><code>-tree</code>(<i>n</i> | <i>v</i>)</p>
<dd> Display hyponym (subordinate) tree for <i>searchstr</i>. This is a recursive search that finds the hyponyms of each hyponym.</p>
<dt><code>-coor</code>(<i>n</i> | <i>v</i>)</p>
<dd> Display the coordinates (sisters) of <i>searchstr</i>. This search prints the immediate hypernym for each synset that contains <i>searchstr</i> and the hypernym&#8217;s immediate hyponyms.</p>
<dt><code>-deri</code>(<i>n</i> | <i>v</i>)</p>
<dd> Display derivational morphology links between noun and verb forms.</p>
<dt><code>-domn</code>(<i>n</i> | <i>v</i> | <i>a</i> | <i>r</i>)</p>
<dd> Display domain that <i>searchstr</i> has been classified in.</p>
<dt><code>-domt</code>(<i>n</i> | <i>v</i> | <i>a</i> | <i>r</i>)</p>
<dd> Display all terms classified as members of the <i>searchstr</i>&#8216;s domain.</p>
<dt><code>-subsn</code></p>
<dd> Display substance meronyms of <i>searchstr</i> (<i>HAS SUBSTANCE</i> relation).</p>
<dt><code>-partn</code></p>
<dd> Display part meronyms of <i>searchstr</i> (<i>HAS PART</i> relation).</p>
<dt><code>-membn</code></p>
<dd> Display member meronyms of <i>searchstr</i> (<i>HAS MEMBER</i> relation).</p>
<dt><code>-meron</code></p>
<dd> Display all meronyms of <i>searchstr</i> (<i>HAS PART, HAS MEMBER, HAS SUBSTANCE</i> relations).</p>
<dt><code>-hmern</code></p>
<dd> Display meronyms for <i>searchstr</i> tree. This is a recursive search that prints all the meronyms of <i>searchstr</i> and all of its hypernyms.</p>
<dt><code>-sprtn</code></p>
<dd> Display <i>part of</i> holonyms of <i>searchstr</i> (<i>PART OF</i> relation).</p>
<dt><code>-smemn</code></p>
<dd> Display <i>member of</i> holonyms of <i>searchstr</i> (<i>MEMBER OF</i> relation).</p>
<dt><code>-ssubn</code></p>
<dd> Display <i>substance of</i> holonyms of <i>searchstr</i> (<i>SUBSTANCE OF</i> relation).</p>
<dt><code>-holon</code></p>
<dd> Display all holonyms of <i>searchstr</i> (<i>PART OF, MEMBER OF, SUBSTANCE OF</i> relations).</p>
<dt><code>-hholn</code></p>
<dd> Display holonyms for <i>searchstr</i> tree. This is a recursive search that prints all the holonyms of <i>searchstr</i> and all of each holonym&#8217;s holonyms.</p>
<dt><code>-entav</code></p>
<dd> Display entailment relations of <i>searchstr</i>.</p>
<dt><code>-framv</code></p>
<dd> Display applicable verb sentence frames for <i>searchstr</i>.</p>
<dt><code>-causv</code></p>
<dd> Display <i>cause to</i> relations of <i>searchstr</i>.</p>
<dt><code> -pert</code>(<i>a</i> | <i>r</i>)</p>
<dd> Display pertainyms of <i>searchstr</i>.</p>
<dt><code> -attr</code>(<i>n</i> | <i>a</i>)</p>
<dd> Display adjective values for noun attribute, or noun attributes of adjective values.</p>
<dt><code>-grep</code>(<i>n</i> | <i>v</i> | <i>a</i> | <i>r</i>)</p>
<dd> List compound words containing <i>searchstr</i> as a substring.</dl>
<h2>SEARCH RESULTS</h2>
<p> The results of a search are written to the standard output. For each search, the output consists a one line description of the search, followed by the search results. </p>
<p> All searches other than <code>-over</code> list all senses matching the search results in the following general format. Items enclosed in italicized square brackets (<i>[~&#8230;~]</i>) may not be present. </p>
<dl>
<dt>
<dd> One line listing the number of senses matching the search request. </p>
<p> Each sense matching the search requested displayed as follows: </p>
<pre><code>
Sense n
    [{synset_offset}][&lt;lex_filename&gt;] ~~word1[#sense_number][, ~~word2...]
</code></pre>
<p> Where <i>n</i> is the sense number of the search word, <i>synset_offset</i> is the byte offset of the synset in the <code>data.</code><i>pos</i> file corresponding to the syntactic category, <i>lex_filename</i> is the name of the lexicographer file that the synset comes from, <i>word1</i> is the first word in the synset (note that this is not necessarily the search word) and <i>sense_number</i> is the WordNet sense number assigned to the preceding word. <i>synset_offset, lex_filename</i>, and <i>sense_number</i> are generated when the <code>-o, -a,</code> and <code>-s</code> options, respectively, are specified. </p>
<p> The synsets matching the search requested are printed below each sense&#8217;s synset output described above. Each line of output is preceded by a marker (usually <code>=&gt;</code>), then a synset, formatted as described above. If a search traverses more one level of the tree, then successive lines are indented by spaces corresponding to its level in the hierarchy. When the <code>-g</code> option is specified, synset glosses are displayed in parentheses at the end of each synset. Each synset is printed on one line. </p>
<p> Senses are generally ordered from most to least frequently used, with the most common sense numbered <code>1</code>. Frequency of use is determined by the number of times a sense is tagged in the various semantic concordance texts. Senses that are not semantically tagged follow the ordered senses. Note that this ordering is only an estimate based on usage in a small corpus. </p>
<p> Verb senses can be grouped by similarity of meaning, rather than ordered by frequency of use. The <code>-simsv</code> search prints all senses that are close in meaning together, with a line of dashes indicating the end of a group. See <code><a href="/docs/linux/man/7-wngroups/">wngroups</a></code>(7) for a discussion of how senses are grouped. </p>
<p> The <code>-over</code> search displays an overview of all the senses of the search word in all syntactic categories. The results of this search are similar to the <code>-syns</code> search, however no additional (ex. hypernym) synsets are displayed, and synset glosses are always printed. The senses are grouped by syntactic category, and each synset is annotated as described above with <i>synset_offset</i>, <i>lex_filename</i>, and <i>sense_number</i> as dictated by the <code>-o, -a,</code> and <code>-s</code> options. The overview search also indicates how many of the senses in each syntactic category are represented in the tagged texts. This is a way for the user to determine whether a sense&#8217;s sense number is based on semantic tagging data, or was arbitrarily assigned. For each sense that has appeared in such texts, the number of semantic tags to that sense are indicated in parentheses after the sense number. </p>
<p> If a search cannot be performed on some senses of <i>searchstr</i>, the search results are headed by a string of the form: </p>
<pre>
        X of Y senses of <i>searchstr</i>
</pre>
<p> The output of the <code>-deri</code> search shows word forms that are morphologically related to <code>searchstr</code>. Each word form pointed to from <i>searchstr</i> is displayed, preceded by <code>RELATED TO-&gt;</code> and the syntactic category of the link, followed, on the next line, by its synset. Printed after the word form is <code>#</code><i>n</i> where <i>n</i> indicates the WordNet sense number of the term pointed to. </p>
<p> The <code>-domn</code> and <code>-domt</code> searches show the domain that a synset has been classified in and, conversely, all of the terms that have been assigned to a specific domain. A domain is either a <code>TOPIC,</code> <code>REGION</code> or <code>USAGE,</code> as reflected in the specific pointer character stored in the database, and displayed in the output. A <code>-domn</code> search on a term shows the domain, if any, that each synset containing <i>searchstr</i> has been classified in. The output display shows the domain type (<code>TOPIC,</code> <code>REGION</code> or <code>USAGE</code>), followed by the syntactic category of the domain synset and the terms in the synset. Each term is followed by <code>#</code><i>n</i> where <i>n</i> indicates the WordNet sense number of the term. The converse search, <code>-domt</code>, shows all of the synsets that have been placed into the domain <i>searchstr</i>, with analogous markers. </p>
<p> When <code>-framv</code> is specified, sample illustrative sentences and generic sentence frames are displayed. If a sample sentence is found, the base form of <i>search</i> is substituted into the sentence, and it is printed below the synset, preceded with the <code>EX:</code> marker. When no sample sentences are found, the generic sentence frames are displayed. Sentence frames that are acceptable for all words in a synset are preceded by the marker <code>*&gt;</code>. If a frame is acceptable for the search word only, it is preceded by the marker <code>=&gt;</code>. </p>
<p> Search results for adjectives are slightly different from those for other parts of speech. When an adjective is printed, its direct antonym, if it has one, is also printed in parentheses. When <i>searchstr</i> is in a head synset, all of the head synset&#8217;s satellites are also displayed. The position of an adjective in relation to the noun may be restricted to the <i>prenominal</i>, <i>postnominal</i> or <i>predicative</i> position. Where present, these restrictions are noted in parentheses. </p>
<p> When an adjective is a participle of a verb, the output indicates the verb and displays its synset. </p>
<p> When an adverb is derived from an adjective, the specific adjectival sense on which it is based is indicated. </p>
<p> The morphological transformations performed by the search code may result in more than one word to search for. WordNet automatically performs the requested search on all of the strings and returns the results grouped by word. For example, the verb <code>saw</code> is both the present tense of <code>saw</code> and the past tense of <code>see</code>. When passed <i>searchstr</i> <code>saw</code>, WordNet performs the desired search first on <code>saw</code> and next on <code>see</code>, returning the list of <code>saw</code> senses and search results, followed by those for <code>see</code>.</dl>
<h2>EXIT STATUS</h2>
<p> <code>wn()</code> normally exits with the number of senses displayed. If <i>searchword</i> is not found in WordNet, it exits with <code>0</code>. </p>
<p> If the WordNet database cannot be opened, an error messages is displayed and <code>wn()</code> exits with <code>-1</code>.</p>
<h2>ENVIRONMENT VARIABLES (UNIX)</h2>
<dl>
<dt><code>WNHOME</code></p>
<dd> Base directory for WordNet. Default is <code>/usr/local/WordNet-3.0</code>.</p>
<dt><code>WNSEARCHDIR</code></p>
<dd> Directory in which the WordNet database has been installed. Default is <code>WNHOME/dict</code>.</dl>
<h2>REGISTRY (WINDOWS)</h2>
<dl>
<dt><code>HKEY_LOCAL_MACHINE\SOFTWARE\WordNet\3.0\WNHome</code></p>
<dd> Base directory for WordNet. Default is <code>C:\Program~Files\WordNet\3.0</code>.</dl>
<h2>FILES</h2>
<dl>
<dt><code>index.</code><i>pos</i></p>
<dd> database index files</p>
<dt><code>data.</code><i>pos</i></p>
<dd> database data files</p>
<dt><code>*.vrb</code></p>
<dd> files of sentences illustrating the use of verbs</p>
<dt><i>pos</i>.exc</p>
<dd> morphology exception lists</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wnintro/">wnintro</a></code>(1), <code><a href="/docs/linux/man/1-wnb/">wnb</a></code>(1), <code><a href="/docs/linux/man/3-wnintro/">wnintro</a></code>(3), <code><a href="/docs/linux/man/5-lexnames/">lexnames</a></code>(5), <code><a href="/docs/linux/man/5-senseidx/">senseidx</a></code>(5) <code><a href="/docs/linux/man/5-wndb/">wndb</a></code>(5), <code><a href="/docs/linux/man/5-wninput/">wninput</a></code>(5), <code><a href="/docs/linux/man/7-morphy/">morphy</a></code>(7), <code><a href="/docs/linux/man/7-wngloss/">wngloss</a></code>(7), <code><a href="/docs/linux/man/7-wngroups/">wngroups</a></code>(7).</p>
<h2>BUGS</h2>
<p> Please report bugs to wordnet [at] princeton.edu. </p>
<h2>Index</h2>
