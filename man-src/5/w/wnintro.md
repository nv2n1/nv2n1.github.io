---
title: "wnintro(5)"
name: "wnintro"
section: "5"
letter: "w"
url: "/docs/linux/man/5-wnintro/"
description: "wnintro – introduction to descriptions of WordNet file formats"
---

<p>wnintro &#8211; introduction to descriptions of WordNet file formats</p>
<h2>Synopsis</h2>
<p><code>cntlist</code> &#8211; format of <code>cntlist</code> and <code>cntlist.rev</code> files </p>
<p> <code>lexnames</code> &#8211; list of lexicographer file names and numbers </p>
<p> <code>prologdb</code> &#8211; description of Prolog database files </p>
<p> <code>senseidx</code> &#8211; format of sense index file </p>
<p> <code>sensemap</code> &#8211; mapping from senses in WordNet 2.1 to corresponding 3.0 senses </p>
<p> <code>wndb</code> &#8211; format of WordNet database files </p>
<p> <code>wninput</code> &#8211; format of WordNet lexicographer files</p>
<h2>Description</h2>
<p>This section of the <i>WordNet Reference Manual</i> contains manual pages that describe the formats of the various files included in different WordNet 3.0 packages.</p>
<h2>Nomenclature</h2>
<p>All files are in ASCII. Fields are generally separated by one space, unless otherwise noted, and each line is terminated with a newline character. In the file format descriptions, terms in <i>italics</i> refer to field names. Characters or strings in <code>boldface</code> represent an actual character or string as it appears in the file. Items enclosed in italicized square brackets (<i>[~~]</i>) may not be present. Since several files contain fields that have the identical meaning, field names are consistently defined. For example, several WordNet files contain one or more <i>synset_offset</i> fields. In each case, the definition of <i>synset_offset</i> is identical.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-wnintro/">wnintro</a></code>(1), <code><a href="/docs/linux/man/3-wnintro/">wnintro</a></code>(3), <code><a href="/docs/linux/man/5-cntlist/">cntlist</a></code>(5), <code><a href="/docs/linux/man/5-lexnames/">lexnames</a></code>(5), <code><a href="/docs/linux/man/5-prologdb/">prologdb</a></code>(5), <code><a href="/docs/linux/man/5-senseidx/">senseidx</a></code>(5), <code><a href="/docs/linux/man/5-sensemap/">sensemap</a></code>(5), <code><a href="/docs/linux/man/5-wndb/">wndb</a></code>(5), <code><a href="/docs/linux/man/5-wninput/">wninput</a></code>(5), <code><a href="/docs/linux/man/7-wnintro/">wnintro</a></code>(7), <code><a href="/docs/linux/man/7-wngloss/">wngloss</a></code>(7). Fellbaum, C. (1998), ed. <i>&quot;WordNet: An Electronic Lexical Database&quot;</i>. MIT Press, Cambridge, MA. </p>
