---
title: "wnsearch(3)"
name: "wnsearch"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wnsearch/"
description: "findtheinfo, findtheinfo_ds, is_defined, in_wn, index_lookup, parse_index, getindex, read_synset, parse_synset, free_syns, free_synset, free_index, traceptrs_ds, do_trace – functions for searching ..."
---

<p>findtheinfo, findtheinfo_ds, is_defined, in_wn, index_lookup, parse_index, getindex, read_synset, parse_synset, free_syns, free_synset, free_index, traceptrs_ds, do_trace &#8211; functions for searching the WordNet database</p>
<h2>Synopsis</h2>
<pre><code>#include &quot;wn.h&quot;
char *findtheinfo(char *searchstr, int pos, int ptr_type, int sense_num);</code></pre>
<p> <code>SynsetPtr findtheinfo_ds(char *searchstr, int pos, int ptr_type, int sense_num );</code> unsigned int is_defined(char *searchstr, int pos);<br />
unsigned int in_wn(char *searchstr, int pos); <code>IndexPtr index_lookup(char *searchstr, int pos);</code> <code>IndexPtr parse_index(long offset, int dabase, char *line);</code> <code>IndexPtr getindex(char *searchstr, int pos);</code> <code>SynsetPtr read_synset(int pos, long synset_offset, char *searchstr);</code> <code>SynsetPtr parse_synset(FILE *fp, int pos, char *searchstr);</code> void free_syns(SynsetPtr synptr);<br />
void free_synset(SynsetPtr synptr);<br />
void free_index(IndexPtr idx); <code>SynsetPtr traceptrs_ds(SynsetPtr synptr, int ptr_type, int pos, int depth);</code> </p>
<pre><code>char *do_trace(SynsetPtr synptr, int ptr_type, int pos, int depth);</code></pre>
<h2>Description</h2>
<p>These functions are used for searching the WordNet database. They generally fall into several categories: functions for reading and parsing index file entries; functions for reading and parsing synsets in data files; functions for tracing pointers and hierarchies; functions for freeing space occupied by data structures allocated with <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3). </p>
<p> In the following function descriptions, <i>pos</i> is one of the following: </p>
<dl>
<dd>
<pre><code>1</code> NOUN
<code>2</code> VERB
<code>3</code> ADJECTIVE
<code>4</code> ADVERB</pre>
</dl>
<p> <code>findtheinfo()</code> is the primary search algorithm for use with database interface applications. Search results are automatically formatted, and a pointer to the text buffer is returned. All searches listed in <code>WNHOME/include/wn.h</code> can be done by <code>findtheinfo()</code>. <code>findtheinfo_ds()</code> can be used to perform most of the searches, with results returned in a linked list data structure. This is for use with applications that need to analyze the search results rather than just display them. </p>
<p> Both functions are passed the same arguments: <i>searchstr</i> is the word or collocation to search for; <i>pos</i> indicates the syntactic category to search in; <i>ptr_type</i> is one of the valid search types for <i>searchstr</i> in <i>pos</i>. (Available searches can be obtained by calling <code>is_defined()</code> described below.) <i>sense_num</i> should be <font SIZE="-1"><code>ALLSENSES</code></font> if the search is to be done on all senses of <i>searchstr</i> in <i>pos</i>, or a positive integer indicating which sense to search. </p>
<p> <code>findtheinfo_ds()</code> returns a linked list data structures representing synsets. Senses are linked through the <i>nextss</i> field of a <code>Synset</code> data structure. For each sense, synsets that match the search specified with <i>ptr_type</i> are linked through the <i>ptrlist</i> field. See <font SIZE="-1"><code>&quot;Synset Navigation&quot;,</code></font> below, for detailed information on the linked lists returned. </p>
<p> <code>is_defined()</code> sets a bit for each search type that is valid for <i>searchstr</i> in <i>pos</i>, and returns the resulting unsigned integer. Each bit number corresponds to a pointer type constant defined in <code>WNHOME/include/wn.h</code>. For example, if bit 2 is set, the <font SIZE="-1"><code>HYPERPTR</code></font> search is valid for <i>searchstr</i>. There are 29 possible searches. </p>
<p> <code>in_wn()</code> is used to find the syntactic categories in the WordNet database that contain one or more senses of <i>searchstr</i>. If <i>pos</i> is <font SIZE="-1"><code>ALL_POS,</code></font> all syntactic categories are checked. Otherwise, only the part of speech passed is checked. An unsigned integer is returned with a bit set corresponding to each syntactic category containing <i>searchstr</i>. The bit number matches the number for the part of speech. <code>0</code> is returned if <i>searchstr</i> is not present in <i>pos</i>. </p>
<p> <code>index_lookup()</code> finds <i>searchstr</i> in the index file for <i>pos</i> and returns a pointer to the parsed entry in an <code>Index</code> data structure. <i>searchstr</i> must exactly match the form of the word (lower case only, hyphens and underscores in the same places) in the index file. <font SIZE="-1"><code>NULL </code></font> is returned if a match is not found. </p>
<p> <code>parse_index()</code> parses an entry from an index file and returns a pointer to the parsed entry in an <code>Index</code> data structure. Passed the byte <i>offset</i> and syntactic category, it reads the index entry at the desired location in the corresponding file. If passed <i>line</i>, <i>line</i> contains an index file entry and the database index file is not consulted. However, <i>offset</i> and <i>dbase</i> should still be passed so the information can be stored in the <code>Index</code> structure. </p>
<p> <code>getindex()</code> is a &quot;smart&quot; search for <i>searchstr</i> in the index file corresponding to <i>pos</i>. It applies to <i>searchstr</i> an algorithm that replaces underscores with hyphens, hyphens with underscores, removes hyphens and underscores, and removes periods in an attempt to find a form of the string that is an exact match for an entry in the index file corresponding to <i>pos</i>. <code>index_lookup()</code> is called on each transformed string until a match is found or all the different strings have been tried. It returns a pointer to the parsed <code>Index</code> data structure for <i>searchstr</i>, or <font SIZE="-1"><code>NULL</code></font> if a match is not found. </p>
<p> <code>read_synset()</code> is used to read a synset from a byte offset in a data file. It performs an <code><a href="/docs/linux/man/3-fseek/">fseek</a></code>(3) to <i>synset_offset</i> in the data file corresponding to <i>pos</i>, and calls <code>parse_synset()</code> to read and parse the synset. A pointer to the <code>Synset</code> data structure containing the parsed synset is returned. </p>
<p> <code>parse_synset()</code> reads the synset at the current offset in the file indicated by <i>fp</i>. <i>pos</i> is the syntactic category, and <i>searchstr</i>, if not <font SIZE="-1"><code>NULL,</code></font> indicates the word in the synset that the caller is interested in. An attempt is made to match <i>searchstr</i> to one of the words in the synset. If an exact match is found, the <i>whichword</i> field in the <code>Synset</code> structure is set to that word&#8217;s number in the synset (beginning to count from <code>1</code>). </p>
<p> <code>free_syns()</code> is used to free a linked list of <code>Synset</code> structures allocated by <code>findtheinfo_ds()</code>. <i>synptr</i> is a pointer to the list to free. </p>
<p> <code>free_synset()</code> frees the <code>Synset</code> structure pointed to by <i>synptr</i>. </p>
<p> <code>free_index()</code> frees the <code>Index</code> structure pointed to by <i>idx</i>. </p>
<p> <code>traceptrs_ds()</code> is a recursive search algorithm that traces pointers matching <i>ptr_type</i> starting with the synset pointed to by <i>synptr</i>. Setting <i>depth</i> to <code>1</code> when <code>traceptrs_ds()</code> is called indicates a recursive search; <code>0</code> indicates a non-recursive call. <i>synptr</i> points to the data structure representing the synset to search for a pointer of type <i>ptr_type</i>. When a pointer type match is found, the synset pointed to is read is linked onto the <i>nextss</i> chain. Levels of the tree generated by a recursive search are linked via the <i>ptrlist</i> field structure until <font SIZE="-1"><code>NULL</code></font> is found, indicating the top (or bottom) of the tree. This function is usually called from <code>findtheinfo_ds()</code> for each sense of the word. See <font SIZE="-1"><code>&quot;Synset Navigation&quot;,</code></font> below, for detailed information on the linked lists returned. </p>
<p> <code>do_trace()</code> performs the search indicated by <i>ptr_type</i> on synset synptr in syntactic category <i>pos</i>. <i>depth</i> is defined as above. <code>do_trace()</code> returns the search results formatted in a text buffer.</p>
<h3>Synset Navigation</h3>
<p>Since the <code>Synset</code> structure is used to represent the synsets for both word senses and pointers, the <i>ptrlist</i> and <i>nextss</i> fields have different meanings depending on whether the structure is a word sense or pointer. This can make navigation through the lists returned by <code>findtheinfo_ds()</code> confusing. </p>
<p> Navigation through the returned list involves the following: </p>
<p> Following the <i>nextss</i> chain from the synset returned moves through the various senses of <i>searchstr</i>. <font SIZE="-1"><code>NULL</code></font> indicates that end of the chain of senses. </p>
<p> Following the <i>ptrlist</i> chain from a <code>Synset</code> structure representing a sense traces the hierarchy of the search results for that sense. Subsequent links in the <i>ptrlist</i> chain indicate the next level (up or down, depending on the search) in the hierarchy. <font SIZE="-1"><code>NULL</code></font> indicates the end of the chain of search result synsets. </p>
<p> If a synset pointed to by <i>ptrlist</i> has a value in the <i>nextss</i> field, it represents another pointer of the same type at that level in the hierarchy. For example, some noun synsets have two hypernyms. Following this <i>nextss</i> pointer, and then the <i>ptrlist</i> chain from the <code>Synset</code> structure pointed to, traces another, parallel, hierarchy, until the end is indicated by <font SIZE="-1"><code>NULL</code></font> on that <i>ptrlist</i> chain. So, a <code>synset</code> representing a pointer (versus a sense of <i>searchstr</i>) having a non-NULL value in <i>nextss</i> has another chain of search results linked through the <i>ptrlist</i> chain of the synset pointed to by <i>nextss</i>. </p>
<p> If <i>searchstr</i> contains more than one base form in WordNet (as in the noun <code>axes</code>, which has base forms <code>axe</code> and <code>axis</code>), synsets representing the search results for each base form are linked through the <i>nextform</i> pointer of the <code>Synset</code> structure.</p>
<h3>WordNet Searches</h3>
<p>There is no extensive description of what each search type is or the results returned. Using the WordNet interface, examining the source code, and reading <code><a href="/docs/linux/man/5-wndb/">wndb</a></code>(5) are the best ways to see what types of searches are available and the data returned for each. </p>
<p> Listed below are the valid searches that can be passed as <i>ptr_type</i> to <code>findtheinfo()</code>. Passing a negative value (when applicable) causes a recursive, hierarchical search by setting <i>depth</i> to <code>1</code> when <code>traceptrs()</code> is called. </p>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><code>ptr_type</code></td>
<td ALIGN=center><code>Value</code></td>
<td ALIGN=center><code>Pointer</code></td>
<td><code>Search</code>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td ALIGN=center></td>
<td ALIGN=center><code>Symbol</code></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>ANTPTR</td>
<td ALIGN=center>1</td>
<td ALIGN=center>!</td>
<td>Antonyms
</td>
</tr>
<tr VALIGN=top>
<td>HYPERPTR</td>
<td ALIGN=center>2</td>
<td ALIGN=center>@</td>
<td>Hypernyms
</td>
</tr>
<tr VALIGN=top>
<td>HYPOPTR</td>
<td ALIGN=center>3</td>
<td ALIGN=center>&asymp;</td>
<td>Hyponyms
</td>
</tr>
<tr VALIGN=top>
<td>ENTAILPTR</td>
<td ALIGN=center>4</td>
<td ALIGN=center>*</td>
<td>Entailment
</td>
</tr>
<tr VALIGN=top>
<td>SIMPTR</td>
<td ALIGN=center>5</td>
<td ALIGN=center>&amp;</td>
<td>Similar
</td>
</tr>
<tr VALIGN=top>
<td>ISMEMBERPTR</td>
<td ALIGN=center>6</td>
<td ALIGN=center>#m</td>
<td>Member meronym
</td>
</tr>
<tr VALIGN=top>
<td>ISSTUFFPTR</td>
<td ALIGN=center>7</td>
<td ALIGN=center>#s</td>
<td>Substance meronym
</td>
</tr>
<tr VALIGN=top>
<td>ISPARTPTR</td>
<td ALIGN=center>8</td>
<td ALIGN=center>#p</td>
<td>Part meronym
</td>
</tr>
<tr VALIGN=top>
<td>HASMEMBERPTR</td>
<td ALIGN=center>9</td>
<td ALIGN=center>%m</td>
<td>Member holonym
</td>
</tr>
<tr VALIGN=top>
<td>HASSTUFFPTR</td>
<td ALIGN=center>10</td>
<td ALIGN=center>%s</td>
<td>Substance holonym
</td>
</tr>
<tr VALIGN=top>
<td>HASPARTPTR</td>
<td ALIGN=center>11</td>
<td ALIGN=center>%p</td>
<td>Part holonym
</td>
</tr>
<tr VALIGN=top>
<td>MERONYM</td>
<td ALIGN=center>12</td>
<td ALIGN=center>%</td>
<td>All meronyms
</td>
</tr>
<tr VALIGN=top>
<td>HOLONYM</td>
<td ALIGN=center>13</td>
<td ALIGN=center>#</td>
<td>All holonyms
</td>
</tr>
<tr VALIGN=top>
<td>CAUSETO</td>
<td ALIGN=center>14</td>
<td ALIGN=center>&gt;</td>
<td>Cause
</td>
</tr>
<tr VALIGN=top>
<td>PPLPTR</td>
<td ALIGN=center>15</td>
<td ALIGN=center>&lt;</td>
<td>Participle of verb
</td>
</tr>
<tr VALIGN=top>
<td>SEEALSOPTR</td>
<td ALIGN=center>16</td>
<td ALIGN=center>^</td>
<td>Also see
</td>
</tr>
<tr VALIGN=top>
<td>PERTPTR</td>
<td ALIGN=center>17</td>
<td ALIGN=center>\</td>
<td>Pertains to noun or derived from adjective
</td>
</tr>
<tr VALIGN=top>
<td>ATTRIBUTE</td>
<td ALIGN=center>18</td>
<td ALIGN=center>\=</td>
<td>Attribute
</td>
</tr>
<tr VALIGN=top>
<td>VERBGROUP</td>
<td ALIGN=center>19</td>
<td ALIGN=center>$</td>
<td>Verb group
</td>
</tr>
<tr VALIGN=top>
<td>DERIVATION</td>
<td ALIGN=center>20</td>
<td ALIGN=center>+</td>
<td>Derivationally related form
</td>
</tr>
<tr VALIGN=top>
<td>CLASSIFICATION</td>
<td ALIGN=center>21</td>
<td ALIGN=center>;</td>
<td>Domain of synset
</td>
</tr>
<tr VALIGN=top>
<td>CLASS</td>
<td ALIGN=center>22</td>
<td ALIGN=center>&#8211;</td>
<td>Member of this domain
</td>
</tr>
<tr VALIGN=top>
<td>SYNS</td>
<td ALIGN=center>23</td>
<td ALIGN=center><i>n/a</i></td>
<td>Find synonyms
</td>
</tr>
<tr VALIGN=top>
<td>FREQ</td>
<td ALIGN=center>24</td>
<td ALIGN=center><i>n/a</i></td>
<td>Polysemy
</td>
</tr>
<tr VALIGN=top>
<td>FRAMES</td>
<td ALIGN=center>25</td>
<td ALIGN=center><i>n/a</i></td>
<td>Verb example sentences and generic frames
</td>
</tr>
<tr VALIGN=top>
<td>COORDS</td>
<td ALIGN=center>26</td>
<td ALIGN=center><i>n/a</i></td>
<td>Noun coordinates
</td>
</tr>
<tr VALIGN=top>
<td>RELATIVES</td>
<td ALIGN=center>27</td>
<td ALIGN=center><i>n/a</i></td>
<td>Group related senses
</td>
</tr>
<tr VALIGN=top>
<td>HMERONYM</td>
<td ALIGN=center>28</td>
<td ALIGN=center><i>n/a</i></td>
<td>Hierarchical meronym search
</td>
</tr>
<tr VALIGN=top>
<td>HHOLONYM</td>
<td ALIGN=center>29</td>
<td ALIGN=center><i>n/a</i></td>
<td>Hierarchical holonym search
</td>
</tr>
<tr VALIGN=top>
<td>WNGREP</td>
<td ALIGN=center>30</td>
<td ALIGN=center><i>n/a</i></td>
<td>Find keywords by substring
</td>
</tr>
<tr VALIGN=top>
<td>OVERVIEW</td>
<td ALIGN=center>31</td>
<td ALIGN=center><i>n/a</i></td>
<td>Show all synsets for word
</td>
</tr>
<tr VALIGN=top>
<td>CLASSIF_CATEGORY</td>
<td ALIGN=center>32</td>
<td ALIGN=center>;c</td>
<td>Show domain topic
</td>
</tr>
<tr VALIGN=top>
<td>CLASSIF_USAGE</td>
<td ALIGN=center>33</td>
<td ALIGN=center>;u</td>
<td>Show domain usage
</td>
</tr>
<tr VALIGN=top>
<td>CLASSIF_REGIONAL</td>
<td ALIGN=center>34</td>
<td ALIGN=center>;r</td>
<td>Show domain region
</td>
</tr>
<tr VALIGN=top>
<td>CLASS_CATEGORY</td>
<td ALIGN=center>35</td>
<td ALIGN=center>-c</td>
<td>Show domain terms for topic
</td>
</tr>
<tr VALIGN=top>
<td>CLASS_USAGE</td>
<td ALIGN=center>36</td>
<td ALIGN=center>-u</td>
<td>Show domain terms for usage
</td>
</tr>
<tr VALIGN=top>
<td>CLASS_REGIONAL</td>
<td ALIGN=center>37</td>
<td ALIGN=center>-r</td>
<td>Show domain terms for region
</td>
</tr>
<tr VALIGN=top>
<td>INSTANCE</td>
<td ALIGN=center>38</td>
<td ALIGN=center>@i</td>
<td>Instance of
</td>
</tr>
<tr VALIGN=top>
<td>INSTANCES</td>
<td ALIGN=center>39</td>
<td ALIGN=center>&asymp;i</td>
<td>Show instances
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> <code>findtheinfo_ds()</code> cannot perform the following searches: </p>
<dl>
<dd>
<pre>SEEALSOPTR
PERTPTR
VERBGROUP
FREQ
FRAMES
RELATIVES
WNGREP
OVERVIEW</pre>
</dl>
<h2>Notes</h2>
<p>Applications that use WordNet and/or the morphological functions must call <code>wninit()</code> at the start of the program. See <code><a href="/docs/linux/man/3-wnutil/">wnutil</a></code>(3) for more information. In all function calls, <i>searchstr</i> may be either a word or a collocation formed by joining individual words with underscore characters (<code>_</code>). The <code>SearchResults</code> structure defines fields in the <i>wnresults</i> global variable that are set by the various search functions. This is a way to get additional information, such as the number of senses the word has, from the search functions. The <i>searchds</i> field is set by <code>findtheinfo_ds()</code>. The <i>pos</i> passed to <code>traceptrs_ds()</code> is not used. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-wn/">wn</a></code>(1), <code><a href="/docs/linux/man/1-wnb/">wnb</a></code>(1), <code><a href="/docs/linux/man/3-wnintro/">wnintro</a></code>(3), <code><a href="/docs/linux/man/3-binsrch/">binsrch</a></code>(3), <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-morph/">morph</a></code>(3), <code><a href="/docs/linux/man/3-wnutil/">wnutil</a></code>(3), <code><a href="/docs/linux/man/5-wnintro/">wnintro</a></code>(5).</p>
<h2>Warnings</h2>
<p><code>parse_synset()</code> must find an exact match between the <i>searchstr</i> passed and a word in the synset to set <i>whichword</i>. No attempt is made to translate hyphens and underscores, as is done in <code>getindex()</code>. </p>
<p> The WordNet database and exception list files must be opened with <code>wninit</code> prior to using any of the searching functions. </p>
<p> A large search may cause <code>findtheinfo()</code> to run out of buffer space. The maximum buffer size is determined by computer platform. If the buffer size is exceeded the following message is printed in the output buffer: <code>&quot;Search too large. Narrow search and try again&#8230;&quot;</code>. </p>
<p> Passing an invalid <i>pos</i> will probably result in a core dump.</p>
