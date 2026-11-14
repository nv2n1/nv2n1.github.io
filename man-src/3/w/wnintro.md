---
title: "wnintro(3)"
name: "wnintro"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wnintro/"
description: "wnintro – introduction to WordNet library functions"
---

<p>wnintro &#8211; introduction to WordNet library functions</p>
<h2>Description</h2>
<p>This section of the <i>WordNet Reference Manual</i> contains manual pages that describe the WordNet library functions and API. </p>
<p> Functions are organized into the following categories: </p>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><code>Category</code></td>
<td><code>Manual Page</code></td>
<td><code>Object File</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Database Search</td>
<td>wnsearch (3)</td>
<td>search.o
</td>
</tr>
<tr VALIGN=top>
<td>Morphology</td>
<td>morph (3)</td>
<td>morph.o
</td>
</tr>
<tr VALIGN=top>
<td>Misc. Utility</td>
<td>wnutil (3)</td>
<td>wnutil.o
</td>
</tr>
<tr VALIGN=top>
<td>Binary Search</td>
<td>binsrch (3)</td>
<td>binsrch.o
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> The WordNet library is used by all of the searching interfaces provided with the various WordNet packages. Additional programs in the system, such as <code><a href="/docs/linux/man/1-grind/">grind</a></code>(1), also use functions in this library. </p>
<p> The WordNet library is provided in both source and binary forms (on some platforms) to allow users to build applications and tools to their own specifications that utilize the WordNet database. We do not provide programming support or assistance. </p>
<p> The code conforms to ANSI C standards. Functions are defined with function prototypes. If you do not have a compiler that accepts prototypes, you must edit the source code and remove the prototypes before compiling.</p>
<h2>List Of Wordnet Library Functions</h2>
<p>Not all library functions are listed below. Missing are mainly functions that are called by documented ones, or ones that were written for specific applications or tools used during WordNet development. Data structures are defined in <code>wn.h</code>.</p>
<h3>Database Searching Functions (search.o)</h3>
<dl>
<dt><code>findtheinfo </code></p>
<dd>Primary search function for WordNet database. Returns formatted search results in text buffer. Used by WordNet interfaces to perform requested search.</p>
<dt><code>findtheinfo_ds</code></p>
<dd>Primary search function for WordNet database. Returns search results in linked list data structure.</p>
<dt><code>is_defined</code></p>
<dd>Set bit for each search type that is valid for the search word passed and return bit mask.</p>
<dt><code>in_wn</code></p>
<dd>Set bit for each syntactic category that search word is in.</p>
<dt><code>index_lookup</code></p>
<dd>Find word in index file and return parsed entry in data structure. Input word must be exact match of string in database. Called by <code>getindex()</code>.</p>
<dt><code>getindex</code></p>
<dd>Find word in index file, trying different techniques &#8211; replace hyphens with underscores, replace underscores with hyphens, strip hyphens and underscores, strip periods.</p>
<dt><code>read_synset</code></p>
<dd>Read synset from data file at byte offset passed and return parsed entry in data structure. Calls <code>parse_synset()</code>.</p>
<dt><code>parse_synset</code></p>
<dd>Read synset at current byte offset in file and return parsed entry in data structure.</p>
<dt><code>free_syns</code></p>
<dd>Free a synset linked list allocated by <code>findtheinfo_ds()</code>.</p>
<dt><code>free_synset</code></p>
<dd>Free a synset structure.</p>
<dt><code>free_index</code></p>
<dd>Free an index structure.</p>
<dt><code>traceptrs_ds</code></p>
<dd>Recursive search algorithm to trace a pointer tree and return results in linked list.</p>
<dt><code>do_trace</code></p>
<dd>Do requested search on synset passed returning formatted output in buffer. </p>
</dl>
<h3>Morphology Functions (morph.o)</h3>
<dl>
<dt><code>morphinit</code></p>
<dd>Open exception list files.</p>
<dt><code>re_morphinit</code></p>
<dd>Close exception list files and reopen.</p>
<dt><code>morphstr</code></p>
<dd>Try to find base form (lemma) of word or collocation in syntactic category passed. Calls <code>morphword()</code> for each word in string passed.</p>
<dt><code>morphword</code></p>
<dd>Try to find base form (lemma) of individual word in syntactic category passed. </p>
</dl>
<h3>Utility Functions (wnutil.o)</h3>
<dl>
<dt><code>wninit</code></p>
<dd>Top level function to open database files and morphology exception lists.</p>
<dt><code>re_wninit</code></p>
<dd>Top level function to close and reopen database files and morphology exception lists.</p>
<dt><code>cntwords</code></p>
<dd>Count the number of underscore or space separated words in a string.</p>
<dt><code>strtolower</code></p>
<dd>Convert string to lower case and remove trailing adjective marker if found.</p>
<dt><code>ToLowerCase</code></p>
<dd>Convert string passed to lower case.</p>
<dt><code>strsubst</code></p>
<dd>Replace all occurrences of <i>from</i> with <i>to</i> in <i>str</i>.</p>
<dt><code>getptrtype</code></p>
<dd>Return code for pointer type character passed.</p>
<dt><code>getpos</code></p>
<dd>Return syntactic category code for string passed.</p>
<dt><code>getsstype</code></p>
<dd>Return synset type code for string passed.</p>
<dt><code>FmtSynset</code></p>
<dd>Reconstruct synset string from synset pointer.</p>
<dt><code>StrToPos</code></p>
<dd>Passed string for syntactic category, returns corresponding integer value.</p>
<dt><code>GetSynsetForSense</code></p>
<dd>Return synset for sense key passed.</p>
<dt><code>GetDataOffset</code></p>
<dd>Find synset offset for sense.</p>
<dt><code>GetPolyCount</code></p>
<dd>Find polysemy count for sense passed.</p>
<dt><code>GetWORD</code></p>
<dd>Return word part of sense key.</p>
<dt><code>GetPOS</code></p>
<dd>Return syntactic category code for sense key passed.</p>
<dt><code>WNSnsToStr</code></p>
<dd>Generate sense key for index entry passed.</p>
<dt><code>GetValidIndexPointer</code></p>
<dd>Search for string and/or base form of word in database and return index structure for word if found.</p>
<dt><code>GetWNSense</code></p>
<dd>Return sense number in database for sense key.</p>
<dt><code>GetSenseIndex</code></p>
<dd>Return parsed sense index entry for sense key passed.</p>
<dt><code>default_display_message</code></p>
<dd>Default function to use as value of <code>display_message</code>. Simply returns <code>-1</code>. </p>
</dl>
<h3>Binary Search Functions (binsrch.o)</h3>
<dl>
<dt><code>bin_search</code></p>
<dd>General purpose binary search function to search for key as first item on line in sorted file.</p>
<dt><code>copyfile</code></p>
<dd>Copy contents from one file to another.</p>
<dt><code>replace_line</code></p>
<dd>Replace a line in a sorted file.</p>
<dt><code>insert_line</code></p>
<dd>Insert a line into a sorted file.</dl>
<h2>Header File</h2>
<dl>
<dt><code>wn.h</code></p>
<dd>WordNet include file of constants, data structures, external declarations for global variables initialized in <code>wnglobal.c</code>. Also lists function prototypes for library API. It must be included to use any WordNet library functions.</dl>
<h2>Notes</h2>
<p>All library functions that access the database files expect the files to be open. The function <code><a href="/docs/linux/man/3-wninit/">wninit</a></code>(3) must be called before other database access functions such as <code><a href="/docs/linux/man/3-findtheinfo/">findtheinfo</a></code>(3) or <code><a href="/docs/linux/man/3-read_synset/">read_synset</a></code>(3). </p>
<p> Inclusion of the header file <code>wn.h</code> is necessary. </p>
<p> The command line interface is a good example of a simple application that uses several WordNet library functions. </p>
<p> Many of the library functions are passed or return syntactic category or synset type information. The following table lists the possible categories as integer codes, synset type constant names, syntactic category constant names, single characters and character strings. </p>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>Integer</code></td>
<td ALIGN=center><code>Synset Type</code></td>
<td ALIGN=center><code>Syntactic Category</code></td>
<td ALIGN=center><code>Char</code></td>
<td ALIGN=center><code>String</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>1</td>
<td>NOUN</td>
<td>NOUN</td>
<td ALIGN=center>n</td>
<td>noun
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>2</td>
<td>VERB</td>
<td>VERB</td>
<td ALIGN=center>v</td>
<td>verb
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>3</td>
<td>ADJ</td>
<td>ADJ</td>
<td ALIGN=center>a</td>
<td>adj
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>4</td>
<td>ADV</td>
<td>ADV</td>
<td ALIGN=center>r</td>
<td>adv
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>5</td>
<td>SATELLITE</td>
<td>ADJ</td>
<td ALIGN=center>s</td>
<td><i>n/a</i>
</td>
</tr>
</table>
</table>
<p></center></p>
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
<dt><code>lib/libwn.a</code></p>
<dd>WordNet library (Unix)</p>
<dt><code>lib\wn.lib</code></p>
<dd>WordNet library (Windows)</p>
<dt><code>include</code></p>
<dd>header files for use with WordNet library</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-wnintro/">wnintro</a></code>(1), <code><a href="/docs/linux/man/3-binsrch/">binsrch</a></code>(3), <code><a href="/docs/linux/man/3-morph/">morph</a></code>(3), <code><a href="/docs/linux/man/3-wnsearch/">wnsearch</a></code>(3), <code><a href="/docs/linux/man/3-wnutil/">wnutil</a></code>(3), <code><a href="/docs/linux/man/5-wnintro/">wnintro</a></code>(5), <code><a href="/docs/linux/man/7-wnintro/">wnintro</a></code>(7). </p>
<p> Fellbaum, C. (1998), ed. <i>&quot;WordNet: An Electronic Lexical Database&quot;</i>. MIT Press, Cambridge, MA.</p>
<h2>Bugs</h2>
<p>Please report bugs to <code>wordnet [at] princeton.edu</code>. </p>
