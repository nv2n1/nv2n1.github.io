---
title: "bibdoiadd(1)"
name: "bibdoiadd"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bibdoiadd/"
description: "bibdoiadd.pl – add DOI numbers to papers in a given bib file"
---

<h2 class="name">NAME</h2>
<p> bibdoiadd.pl &#8211; add DOI numbers to papers in a given bib file </p>
<h2>SYNOPSIS</h2>
<p> bibdoiadd [<code>-c</code> <i>config_file</i>] [<code>-C</code> 1|0] [<code>-e</code> 1|0] [<code>-f</code>] [<code>-o</code> <i>output</i>] <i>bib_file</i></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> <i>config_file</i></p>
<dd> Configuration file. If this file is absent, some defaults are used. See below for its format.</p>
<dt><code>-C</code> 1|0</p>
<dd> Whether to canonize names in the output (1) or not (0). By default, 1.</p>
<dt><code>-e</code></p>
<dd> If 1 (default), add empty doi if a doi cannot be found. This prevents repeated searches for the same entries if you add new entries to the file. Calling <tt>&quot;-e 0&quot;</tt> suppresses this behavior.</p>
<dt><code>-f</code></p>
<dd> Force checking doi number even if one is present</p>
<dt><code>-o</code> <i>output</i></p>
<dd> Output file. If this option is not used, the name for the output file is formed by adding <tt>&quot;_doi&quot;</tt> to the input file</dl>
<h2>DESCRIPTION</h2>
<p> The script reads a BibTeX file. It checks whether the entries have DOIs. If not, it tries to contact <a rel="nofollow" href="http://www.crossref.org">http://www.crossref.org</a> to get the corresponding <font SIZE="-1">DOI.</font> The result is a BibTeX file with the fields <tt>&quot;doi=...&quot;</tt> added. </p>
<p> The name of the output file is either set by the <code>-o</code> option or is derived by adding the suffix <tt>&quot;_doi&quot;</tt> to the output file. </p>
<p> There are two options for making queries with Crossref: free account and paid membership. In the first case you still must register with Crossref and are limited to a small number of queries, see the agreement at <tt>&quot;<a rel="nofollow" href="http://www.crossref.org/01company/free_services_agreement.html">http://www.crossref.org/01company/free_services_agreement.html</a>&quot;</tt>. In the second case you have a username and password, and can use them for automatic queries. I am not sure whether the use of this script is allowed for the free account holders. Anyway if you try to add <font SIZE="-1">DOI</font> to a large number of entries, you should register as a paid member.</p>
<h2>CONFIGURATION FILE</h2>
<p> The configuration file is mostly self-explanatory: it has comments (starting with <tt>&quot;#&quot;</tt>) and assginments in the form </p>
<pre>
   $field = value ;
</pre>
<p> The important parameters are <tt>$mode</tt> (<tt>'free'</tt> or <tt>'paid'</tt>), <tt>$email</tt> (for free users) and <tt>$username</tt> &amp; <tt>$password</tt> for paid members.</p>
<h2>EXAMPLES</h2>
<pre>
   bibdoiadd -c bibdoiadd.cfg -o - citations.bib &gt; result.bib
   bibdoiadd -c bibdoiadd.cfg -o result.bib citations.bib
</pre>
<h2>AUTHOR</h2>
<p> Boris Veytsman</p>
<h2>COPYRIGHT AND LICENSE</h2>
<p> Copyright (C) 2014-2021 Boris Veytsman </p>
<p> This is free software. You may redistribute copies of it under the terms of the <font SIZE="-1">GNU</font> General Public License &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&gt;. There is <font SIZE="-1">NO WARRANTY,</font> to the extent permitted by law. </p>
<h2>Index</h2>
