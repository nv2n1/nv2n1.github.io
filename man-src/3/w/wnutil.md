---
title: "wnutil(3)"
name: "wnutil"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wnutil/"
description: "wninit, re_wninit, cntwords, strtolower, ToLowerCase, strsubst, getptrtype, getpos, getsstype, StrToPos, GetSynsetForSense, GetDataOffset, GetPolyCount, WNSnsToStr, GetValidIndexPointer, GetWNSense..."
---

<p>wninit, re_wninit, cntwords, strtolower, ToLowerCase, strsubst, getptrtype, getpos, getsstype, StrToPos, GetSynsetForSense, GetDataOffset, GetPolyCount, WNSnsToStr, GetValidIndexPointer, GetWNSense, GetSenseIndex, default_display_message &#8211; utility functions used by the interface code</p>
<h2>Synopsis</h2>
<pre><code>#include &quot;wn.h&quot;
int wninit(void);
int re_wninit(void);
int cntwords(char *str, char separator);
char *strtolower(char *str);
char *ToLowerCase(char *str);
char *strsubst(char *str, char from, char to);
int getptrtype(char *ptr_symbol);
int getpos(char *ss_type);
int getsstype(char *ss_type);
int StrToPos(char **pos);</code></pre>
<p> <code>SynsetPtr GetSynsetForSense(char *sense_key);</code> long GetDataOffset(char *sense_key);<br />
int GetPolyCount(char *sense_key);<br />
char *WNSnsToStr(IndexPtr idx, int sense_num); <code>IndexPtr GetValidIndexPointer(char *str, int pos);</code> int GetWNSense(char *lemma, *lex_sense); <code>SnsIndexPtr GetSenseIndex(char *sense_key);</code> </p>
<pre><code>int GetTagcnt(IndexPtr idx, int sense);
int default_display_message(char *msg);</code></pre>
<h2>Description</h2>
<p>The WordNet library contains many utility functions used by the interface code, other library functions, and various applications and tools. Only those of importance to the WordNet search code, or which are generally useful are described here. </p>
<p> <code>wninit()</code> opens the files necessary for using WordNet with the WordNet library functions. The database files are opened, and <code>morphinit()</code> is called to open the exception list files. Returns <code>0</code> if successful, <code>-1</code> otherwise. The database and exception list files must be open before the WordNet search and morphology functions are used. If the database is successfully opened, the global variable <code>OpenDB</code> is set to <code>1</code>. Note that it is possible for the database files to be opened (<code>OpenDB == 1</code>), but not the exception list files. </p>
<p> <code>re_wninit()</code> is used to close the database files and reopen them, and is used exclusively for WordNet development. <code>re_morphinit() </code> is called to close and reopen the exception list files. Return codes are as described above. </p>
<p> <code>cntwords()</code> counts the number of underscore or space separated words in <i>str</i>. A hyphen is passed in <i>separator</i> if is is to be considered a word delimiter. Otherwise <i>separator</i> can be any other character, or an underscore if another character is not desired. </p>
<p> <code>strtolower()</code> converts <i>str</i> to lower case and removes a trailing adjective marker, if present. <i>str</i> is actually modified by this function, and a pointer to the modified string is returned. </p>
<p> <code>ToLowerCase()</code> converts <i>str</i> to lower case as above, without removing an adjective marker. </p>
<p> <code>strsubst()</code> replaces all occurrences of <i>from</i> with <i>to</i> in <i>str</i> and returns resulting string. </p>
<p> <code>getptrtype()</code> returns the integer <i>ptr_type</i> corresponding to the pointer character passed in <i>ptr_symbol</i>. See <code><a href="/docs/linux/man/3-wnsearch/">wnsearch</a></code>(3) for a table of pointer symbols and types. </p>
<p> <code>getpos()</code> returns the integer constant corresponding to the synset type passed. <i>ss_type</i> may be one of the following: <code>n, v, a, r, s</code>. If <code>s</code> is passed, <font SIZE="-1"><code>ADJ</code></font> is returned. Exits with <code>-1</code> if <i>ss_type</i> is invalid. </p>
<p> <code>getsstype()</code> works like <code>getpos()</code>, but returns <font SIZE="-1"><code>SATELLITE</code></font> if <i>ss_type</i> is <code>s</code>. </p>
<p> <code>StrToPos()</code> returns the integer constant corresponding to the syntactic category passed in <i>pos</i>. <i>string</i> must be one of the following: <code>noun, verb, adj, adv</code>. <code>-1</code> is returned if <i>pos</i> is invalid. </p>
<p> <code>GetSynsetForSense()</code> returns the synset that contains the word sense <i>sense_key</i> and <font SIZE="-1"><code>NULL</code></font> in case of error. </p>
<p> <code>GetDataOffset()</code> returns the synset offset for synset that contains the word sense <i>sense_key</i>, and <code>0</code> if <i>sense_key</i> is not in sense index file. </p>
<p> <code>GetPolyCount()</code> returns the polysemy count (number of senses in WordNet) for <i>lemma</i> encoded in <i>sense_key</i> and <code>0</code> if word is not found. </p>
<p> <code>WNSnsToStr()</code> returns sense key encoding for <i>sense_num</i> entry in <i>idx</i>. </p>
<p> <code>GetValidIndexPointer()</code> returns the Index structure for <i>word</i> in <i>pos</i>. Calls <code><a href="/docs/linux/man/3-morphstr/">morphstr</a></code>(3) to find a valid base form if <i>word</i> is inflected. </p>
<p> <code>GetWNSense()</code> returns the WordNet sense number for the sense key encoding represented by <i>lemma</i> and <i>lex_sense</i>. </p>
<p> <code>GetSenseIndex()</code> returns parsed sense index entry for <i>sense_key</i> and <font SIZE="-1"><code>NULL</code></font> if <i>sense_key</i> is not in sense index. </p>
<p> <code>GetTagcnt()</code> returns the number of times the sense passed has been tagged according to the <i>cntlist</i> file. </p>
<p> <code>default_display_message()</code> simply returns <code>-1</code>. This is the default value for the global variable <code>display_message</code>, that points to a function to call to display an error message. In general, applications (including the WordNet interfaces) define an application specific function and set <code>display_message</code> to point to it.</p>
<h2>Notes</h2>
<p><code>include/wn.h</code> lists all the pointer and search types and their corresponding constant values. There is no description of what each search type is or the results returned. Using the WordNet interface is the best way to see what types of searches are available, and the data returned for each.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-wnintro/">wnintro</a></code>(3), <code><a href="/docs/linux/man/3-wnsearch/">wnsearch</a></code>(3), <code><a href="/docs/linux/man/3-morph/">morph</a></code>(3), <code><a href="/docs/linux/man/5-wnintro/">wnintro</a></code>(5), <code><a href="/docs/linux/man/7-wnintro/">wnintro</a></code>(7). </p>
<h2>Warnings</h2>
<p>Error checking on passed arguments is not rigorous. Passing <font SIZE="-1"><code>NULL</code></font> pointers or invalid values will often cause an application to die.</p>
