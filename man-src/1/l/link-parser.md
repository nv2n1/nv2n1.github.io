---
title: "link-parser(1)"
name: "link-parser"
section: "1"
letter: "l"
url: "/docs/linux/man/1-link-parser/"
description: "link-parser – parses natural language sentences"
---

<h2 class="name">NAME</h2>
<p> link-parser &#8211; parses natural language sentences </p>
<h2>SYNOPSIS</h2>
<p> <code>link-parser</code> [language] [-pp pp_knowledge_file] [-c constituent_knowledge_file] [-a affix_file] [-ppoff] [-coff] [-aoff] [-batch] [-&lt;special &quot;!&quot; command&gt;]</p>
<h2>DESCRIPTION</h2>
<p> In Selator, D. and Temperly, D. &quot;Parsing English with a Link Grammar&quot; (1991), the authors defined a new formal grammatical system called a &quot;link grammar&quot;. A sequence of words is in the language of a link grammar if there is a way to draw &quot;links&quot; between words in such a way that the local requirements of each word are satisfied, the links do not cross, and the words form a consistent connected graph. The authors encoded English grammar into such a system, and wrote <code>link-parser</code> to parse English using this grammar. </p>
<p> This package can be used for linguistic parsing for information retrieval or extraction from natural language documents. Abiword also uses it as a grammar checker.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-pp pp_knowledge_file</code></p>
<dd>
<dt><code>-c constituent_knowledge_file</code></p>
<dd>
<dt><code>-a affix_file</code></p>
<dd>
<dt><code>-ppoff</code></p>
<dd>
<dt><code>-coff</code></p>
<dd>
<dt><code>-aoff</code></p>
<dd>
<dt><code>-batch</code></p>
<dd>
<dt><code>-&lt;special ! command&gt;</dl>
<p> </code></p>
<h2>USE</h2>
<dd>
<p> link-parser, when invoked manually, will take control of the terminal; link-parser will then attempt to analyze the grammar of all input, unless escaped with an exclamation mark, according to the dictionary file provided as an argument. If escaped, the input will be treated as a &quot;special command&quot;; &quot;!help&quot; lists all special commands available. </p>
<p> link-parser depends on a link-grammar dictionary which contains lists of words and associated metadata about their grammatical properties in order to analyze sentences. A link-grammar dictionary provided by the authors of link-grammar is usually included with the link-grammar package, and can often be found somewhere in the /usr/share/link-grammar/ hierarchy. When this is the case, only the two-letter language code needs to be specified on the command-line. Alternatively, a user can provide their own dictionary as an argument, in which case the dictionary&#8217;s directory should be specified. Hence, either of the commands</p>
<dl>
<dt><code>link-parser en</code></p>
<dd>
<dt><code>link-parser /usr/share/link-grammar/en</code></p>
<dd> will run link-parser using the english dictionary included with the parser.</dl>
<p> While in a link-parser session, some example output could be: </p>
<dl>
<dt>
<dd> <code>linkparser&gt; Reading a man page is informative.</code> </p>
<p> ++++Time 0.00 seconds (0.01 total) </p>
<p> Found 1 linkage (1 had no P.P. violations)<br />
&nbsp;<wbr>&nbsp;<wbr>Unique linkage, cost vector&nbsp;<wbr>=&nbsp;<wbr>(UNUSED=0 DIS=0 AND=0 LEN=12) </p>
<p>&nbsp;<wbr>+&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;Xp&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;+<br />
&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+&#8212;&#8212;&#8212;Ss*g&#8212;&#8212;&#8212;+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+&#8212;&#8212;-Os&#8212;&#8212;-+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+&#8212;-Ds&#8212;-+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>+&#8212;-Wd&#8212;+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+&#8211;AN&#8211;+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+&#8212;Pa&#8212;+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| </p>
<p> LEFT-WALL reading.g a man.n page.n is.v informative.a .</dl>
<p> A P.P. violation is a post-processing violation; it is a post-linkage step used to reject invalid parses. The link types shown are specific to English; other langauges will have different link types. </p>
<p> link-parser can also be used non-interactively, either through its API, or via the -batch option. When used with the -batch option, link-parser passively receives input from standard input, and when the stream finishes, it then outputs its analysis. So one could construct an ad-hoc grammar checker by piping text through link-parser with a batch option, and seeing what sentences fail to parse as valid:</p>
<dl>
<dt>
<dd> <code>cat thesis.txt | link-parser /usr/share/link-grammar/en/4.0.dict -batch</code></dl>
<h2>SEE ALSO</h2>
<p> Information on the shared-library API and the link types used in the parse is avavailable at the Abiword website at <code><a rel="nofollow" href="http://www.abisource.com/projects/link-grammar/dict/index.html">http://www.abisource.com/projects/link-grammar/dict/index.html</a></code><br />
 Peer-reviewed papers explaining link-parser can be found at the original CMU site at <code><a rel="nofollow" href="http://www.link.cs.cmu.edu/link/papers/index.html.">http://www.link.cs.cmu.edu/link/papers/index.html.</a></code></p>
<h2>AUTHOR</h2>
<p> link-parser was written by Daniel Sleator &lt;sleator [at] cs.cmu.edu&gt;, Davy Temperley &lt;dtemp [at] theory.esm.rochester.edu&gt;, and John Lafferty &lt;lafferty [at] cs.cmu.edu&gt; </p>
<p> This manual page was written by Ken Bloom &lt;kbloom [at] gmail.com&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
