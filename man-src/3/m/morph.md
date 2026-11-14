---
title: "morph(3)"
name: "morph"
section: "3"
letter: "m"
url: "/docs/linux/man/3-morph/"
description: "morphinit, re_morphinit, morphstr, morphword – WordNet morphological processor functions"
---

<p>morphinit, re_morphinit, morphstr, morphword &#8211; WordNet morphological processor functions</p>
<h2>Synopsis</h2>
<p><code>#include &quot;wn.h&quot;</code> </p>
<p> <code>int morphinit(void);</code> </p>
<p> <code>int re_morphinit(void);</code> </p>
<p> <code>char *morphstr(char *origstr, int pos);</code> </p>
<p> <code>char *morphword(char *word, int pos);</code></p>
<h2>Description</h2>
<p>The WordNet morphological processor, Morphy, is accessed through these functions: </p>
<p> <code>morphinit()</code> is used to open the exception list files. It returns <code>0</code> if successful, <code>-1</code> otherwise. The exception list files must be opened before <code>morphstr() </code> or <code>morphword()</code> are called. </p>
<p> <code>re_morphinit()</code> is used to close the exception list files and reopen them, and is used exclusively for WordNet development. Return codes are as described above. </p>
<p> <code>morphstr()</code> is the basic user interface to Morphy. It tries to find the base form (lemma) of the word or collocation <i>origstr</i> in the specified <i>pos</i>. The first call (with <i>origstr</i> specified) returns a pointer to the first base form found. Subsequent calls requesting base forms of the same string must be made with the first argument of <font SIZE="-1"><code>NULL.</code></font> When no more base forms for <i>origstr</i> can be found, <font SIZE="-1"><code>NULL</code></font> is returned. Note that <code>morphstr()</code> returns a pointer to a static character buffer. A subsequent call to <code>morphstr()</code> with a new string (instead of <code>NULL</code>) will overwrite the string pointed to by a previous call. Users should copy the returned string into a local buffer, or use the C library function <code>strdup</code> to duplicate the returned string into a <i>malloc&#8217;d</i> buffer. </p>
<p> <code>morphword()</code> tries to find the base form of <i>word</i> in the specified <i>pos</i>. This function is called by <code>morphstr()</code> for each individual word in a collocation. Note that <code>morphword()</code> returns a pointer to a static character buffer. A subsequent call to <code>morphword()</code> will overwrite the string pointed to by a previous call. Users should copy the returned string into a local buffer, or use the C library function <code>strdup</code> to duplicate the returned string into a <i>malloc&#8217;d</i> buffer.</p>
<h2>Notes</h2>
<p><code>morphinit()</code> is called by <code>wninit() </code> and is not intended to be called directly by an application. Applications wishing to use WordNet and/or the morphological functions must call <code>wninit()</code> at the start of the program. See <code><a href="/docs/linux/man/3-wnutil/">wnutil</a></code>(3) for more information. </p>
<p> <i>origstr</i> may be either a word or a collocation formed by joining individual words with underscore characters (<code>_</code>). </p>
<p> Usually only <code>morphstr()</code> is called from applications, as it works on both words and collocations. </p>
<p> <i>pos</i> must be one of the following: </p>
<dl COMPACT>
<dd>
<pre><code>1</code> NOUN
<code>2</code> VERB
<code>3</code> ADJECTIVE
<code>4</code> ADVERB
<code>5</code> ADJECTIVE_SATELLITE</pre>
</dl>
<p> If <font SIZE="-1"><code>ADJECTIVE_SATELLITE </code></font> is passed, it is treated by <code>morphstr()</code> as <font SIZE="-1"><code>ADJECTIVE.</code></font></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-wnintro/">wnintro</a></code>(3), <code><a href="/docs/linux/man/3-wnsearch/">wnsearch</a></code>(3), <code><a href="/docs/linux/man/5-wndb/">wndb</a></code>(5), <code><a href="/docs/linux/man/7-morphy/">morphy</a></code>(7). </p>
<h2>Warnings</h2>
<p>Passing an invalid part of speech will result in a core dump. </p>
<p> The WordNet database files must be open to use <code>morphstr()</code> or <code>morphword(). </p>
<p> </code></p>
<h2>Bugs</h2>
<p>Morphy will allow non-words to be converted to words, if they follow one of the rules described above. For example, it will happily convert <code>plantes</code> to <code>plants</code>.</p>
