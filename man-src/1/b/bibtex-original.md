---
title: "bibtex-original(1)"
name: "bibtex-original"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bibtex-original/"
description: "bibtex – make a bibliography for (La)TeX"
---

<p>bibtex &#8211; make a bibliography for (La)TeX </p>
<h2>Synopsis</h2>
<p><code>bibtex</code> [<code>-min-crossrefs=</code><i>number</i>] [<code>-terse</code>] <i>auxname</i>[<i></i><code>.aux</code>]</p>
<h2>Description</h2>
<p>This manual page is not meant to be exhaustive. The complete documentation for this version of TeX can be found in the info file or manual <i>Web2C: A TeX implementation</i>. </p>
<p> BibTeX reads the top-level auxiliary (<code>.aux</code>) file <i>auxname</i> that was output during the running of <code><a href="/docs/linux/man/1-latex/">latex</a></code>(1) or <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1) and creates a bibliography (<code>.bbl</code>) file that will be incorporated into the document on subsequent runs of LaTeX or TeX. </p>
<p> BibTeX looks up, in bibliographic database (<code>.bib</code>) files specified by the ibliography command, the entries specified by the 
