---
title: "bibtool(1)"
name: "bibtool"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bibtool/"
description: "BibTool – BibTeX file manipulation tool"
---

<h2>NAME</h2>
<p> BibTool &#8211; BibTeX file manipulation tool</p>
<h2>SYNOPSIS</h2>
<p> <code>bibtool</code> [options] [files]</p>
<h2>DESCRIPTION</h2>
<p> This manual is not meant to be exhaustive. The complete documentation for <code>BibTool</code> can be found in the <i>BibTool Manual</i>. BibTeX provides an easy to use means to integrate citations and bibliographies into LaTeX documents. But the user is left alone with the management of the BibTeX files. <code>BibTool</code> is intended to fill this gap. <code>BibTool</code> allows the manipulation of BibTeX files which goes beyond the possibilities &#8211; and intentions &#8211; of BibTeX. </p>
<p> <code>BibTool</code> manipulates BibTeX database files through the command line front-end <code>bibtool</code> which accepts numerous options. Modifications are performed through resource instructions that allow the modification of the various internal parameters determining the behavior of <code>BibTool</code>; resource instructions can be grouped in resource files. The original <code>BibTool</code> distribution contains a sufficient set of resource file samples to perform basic, relevant manipulations.</p>
<h2>OPTIONS</h2>
<p> <code>bibtool</code> accepts the following options.</p>
<h3>Resource files</h3>
<dl>
<dt><code>-R</code></p>
<dd> Immediately evaluate the instructions from the default resource file.</p>
<dt><code>-r&nbsp;<wbr></code><i>rsc_file</i></p>
<dd> Immediately evaluate the instructions from the resource file <i>rsc_file</i>.</p>
<dt><code>&#8212;&nbsp;<wbr></code><i>rsc_cmd</i></p>
<dd> Evaluate the resource instruction <i>rsc_cmd</i>.</dl>
<h3>Input file</h3>
<dl>
<dt><code>-i&nbsp;<wbr></code><i>bib_file</i></p>
<dd> Add the BibTeX database file <i>bib_file</i> to the list of input files. If <code>-i</code> omitted the file name may not start with a -. If absent stdin is taken to read from. Input files should follow the <code><a href="/docs/linux/man/1-bibtex/">bibtex</a></code>(1) conventions.</dl>
<h3>Output file</h3>
<dl>
<dt><code>-o&nbsp;<wbr></code><i>output_file</i></p>
<dd> Direct output to the file <i>output_file</i>. If absent the output is directed to stdout.</dl>
<h3>Status reporting</h3>
<dl>
<dt><code>-q</code></p>
<dd> Suppress warnings. Errors can not be suppressed.</p>
<dt><code>-v</code></p>
<dd> Enable informative messages on the activities of BibTool.</dl>
<h3>Sorting</h3>
<dl>
<dt><code>-s</code></p>
<dd> Enable sorting of entries.</p>
<dt><code>-S</code></p>
<dd> Enable sorting of entries in reverse order.</p>
<dt><code>-A&nbsp;<wbr></code><i>type</i></p>
<dd> Determine key disambuguation; <i>type</i> in 0, a, A.</dl>
<h3>Selecting items</h3>
<dl>
<dt><code>-x&nbsp;<wbr></code><i>aux_file</i></p>
<dd> Extract the entries from the auxiliary (<i>.aux</i>) LaTeX <i>aux_file</i> file.</p>
<dt><code>-X&nbsp;<wbr></code><i>regex</i></p>
<dd> Select certain entries according to the regular expression <i>regex</i>.</p>
<dt><code>-c</code></p>
<dd> Turn on the additional selection of crossreferenced entries.</dl>
<h3>Key generation</h3>
<dl>
<dt><code>-f&nbsp;<wbr></code><i>key_format</i></p>
<dd> Set the specification for key generation to <i>key_format</i>.</p>
<dt><code>-F</code></p>
<dd> Turn on key generation.</p>
<dt><code>-k</code></p>
<dd> Generate short format keys.</p>
<dt><code>-K</code></p>
<dd> Generate long format keys.</dl>
<h3>Semantic checks</h3>
<dl>
<dt><code>-d</code></p>
<dd> Find and mark (or delete) entries with identical sort keys.</dl>
<h3>Strings/Macros</h3>
<dl>
<dt><code>-m&nbsp;<wbr></code><i>mac_file</i></p>
<dd> Write the macro definitions to the file <i>mac_file</i> (- is stdout).</p>
<dt><code>-M&nbsp;<wbr></code><i>mac_file</i></p>
<dd> Write the used macro definitions to the file <i>mac_file</i> (- is stdout).</dl>
<h3>Getting help</h3>
<dl>
<dt><code>-h</code></p>
<dd> Print short help and exit.</p>
<dt><code>-V</code></p>
<dd> Print version and exit.</dl>
<h3>Statistics</h3>
<dl>
<dt><code>-#</code></p>
<dd> Print statistics about all known entry types (long).</p>
<dt><code>-@</code></p>
<dd> Print statistics about the used entry types only (short).</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>BIBINPUTS</code></p>
<dd> Search path for BibTeX database (<i>.bib</i>) files.</p>
<dt><code>BIBTOOL</code></p>
<dd> Search path for BibTool resource (<i>.rsc</i>) files.</p>
<dt><code>BIBTOOLRSC</code></p>
<dd> List of resource file names separated by colon.</dl>
<h2>FILES</h2>
<dl>
<dt><i>./.bibtoolrsc</i></p>
<dd> The default current directory <code>BibTool</code> resource file.</p>
<dt><i>~/.bibtoolrsc</i></p>
<dd> The default individual <code>BibTool</code> resource file.</p>
<dt><i>/usr/local/lib/BibTool/*.rsc</i></p>
<dd> The BibTool resource files included in the original distribution.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-bibtex/">bibtex</a></i>(1), <i><a href="/docs/linux/man/1-latex/">latex</a></i>(1), <i><a href="/docs/linux/man/1-tex/">tex</a></i>(1)<br />
 The <i>BibTool Manual</i>.</p>
<h2>BUGS</h2>
<p> Some arrays are allocated statically which may result in an overflow.<br />
 Most memory is allocated but not returned to the OS: A garbage collection algorithm might be integrated in a future release.<br />
 This man page is updated only occasionally, so it is very likely out of date. For complete, current documentation, refer to the <i>BibTool Manual</i> which is distributed as LaTeX source file (<code>bibtool.tex</code>) in the original <code>BibTool</code> source distribution.</p>
<h2>AUTHOR</h2>
<p> BibTool is designed and maintained by Gerd Neugebauer. </p>
<h2>Index</h2>
