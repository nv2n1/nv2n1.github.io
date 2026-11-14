---
title: "grind(1)"
name: "grind"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grind/"
description: "grind – process WordNet lexicographer files"
---

<h2>NAME</h2>
<p> grind &#8211; process WordNet lexicographer files</p>
<h2>SYNOPSIS</h2>
<p> <code>grind</code> [ <code>-v</code> ] [ <code>-s</code> ] [ <code>-L</code><i>logfile</i> ] [ <code>-a</code> ] [ <code>-d</code> ] [ <code>-i</code> ] [ <code>-o</code> ] [ <code>-n</code> ] <i>filename</i> [ <i>filename</i>&#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> <code>grind()</code> processes WordNet lexicographer files, producing database files suitable for use with the WordNet search and interface code and other applications. The syntactic and structural integrity of the input files is verified. Warnings and errors are reported via <code>stderr</code> and a run-time log is produced on <code>stdout</code>. A database is generated only if there are no errors.</p>
<h3>Input Files</h3>
<p> Input files correspond to the syntactic categories implemented in WordNet &#8211; <code>noun</code>, <code>verb</code>, <code>adjective</code> and <code>adverb</code>. Each input lexicographer file consists of a list of synonym sets (<i>synsets</i>) for one part of speech. Although the basic synset syntax is the same for all of the parts of speech, some parts of the syntax only apply to a particular part of speech. See <code><a href="/docs/linux/man/5-wninput/">wninput</a></code>(5) for a description of the input file format. </p>
<p> Each <i>filename</i> specified is of the form: </p>
<dl>
<dt>
<dd> <i>pathname</i><code>/</code><i>pos</i><code>.</code><i>suffix</i></dl>
<p> where <i>pathname</i> is optional and <i>pos</i> is either <code>noun</code>, <code>verb</code>, <code>adj</code> or <code>adv</code>. <i>suffix</i> may be used to separate groups of synsets into different files, for example <code>noun.animal</code> and <code>noun.plant</code>. One or more input files, in any combination of syntactic categories, may be specified. See <code><a href="/docs/linux/man/5-lexnames/">lexnames</a></code>(5) for a list of the lexicographer files used to build the complete WordNet database.</p>
<h3>Output Files</h3>
<p> <code>grind()</code> produces the following output files: </p>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>Filename</code></td>
<td ALIGN=center>Description
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>index.</code><i>pos</i></td>
<td>Index file for each syntactic category
</td>
</tr>
<tr VALIGN=top>
<td><code>data.</code><i>pos</i></td>
<td>Data file for each syntactic category
</td>
</tr>
<tr VALIGN=top>
<td><code>index.sense</code></td>
<td>Sense index
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> See <code><a href="/docs/linux/man/5-wndb/">wndb</a></code>(5) for a description of the database file formats. </p>
<p> Each time <code>grind()</code> is run, any existing database files are overwritten with the database files generated from the specified input files. If no input files from a syntactic category are specified, the corresponding database files are not overwritten.</p>
<h3>Sense Numbers</h3>
<p> Senses are generally ordered from most to least frequently used, with the most common sense numbered <code>1</code>. Frequency of use is determined by the number of times a sense is tagged in the various semantic concordance texts. Senses that are not semantically tagged follow the ordered senses in an arbitrary order. Note that this ordering is only an estimate based on usage in a small corpus. </p>
<p> The <i>tagsense_cnt</i> field for each entry in the <code>index.</code><i>pos</i> files indicates how many of the senses in the list have been tagged. </p>
<p> The <code>cntlist</code> file provided with the database lists the number of times each sense is tagged in the semantic concordances. <code>grind()</code> uses the data from <code>cntlist</code> to order the senses of each word. When the <code>index</code>.<i>pos</i> files are generated, the <i>synset_offset</i>s are output in sense number order, with sense 1 first in the list. Senses with the same number of semantic tags are assigned unique but consecutive sense numbers. The WordNet <font SIZE="-1"><code>OVERVIEW</code></font> search displays all senses of the specified word, in all syntactic categories, and indicates which of the senses are represented in the semantically tagged texts.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code></p>
<dd> Verify integrity of input without generating database.</p>
<dt><code>-s</code></p>
<dd> Suppress generation of warning messages. Usually <code>grind</code> is run with this option until all syntactic and structural errors are corrected since the warning messages may make it difficult to spot error messages.</p>
<dt><code>-L</code><i>logfile</i></p>
<dd> Write all messages to <i>logfile</i> instead of <code>stderr</code>.</p>
<dt><code>-a</code></p>
<dd> Generate statistical report on input files processed.</p>
<dt><code>-d</code></p>
<dd> Generate distribution of senses by string length report on input files processed.</p>
<dt><code>-i</code></p>
<dd> Generate sense index file.</p>
<dt><code>-o</code></p>
<dd> Order senses using <code>cntlist</code>.</p>
<dt><code>-n</code></p>
<dd> Generate nominalization (derivational morphology) links in database.</p>
<dt><i>filename</i></p>
<dd> Input file of the form described in <font SIZE="-1"><code>Input Files.</code></font></dl>
<h2>FILES</h2>
<dl>
<dt><i>pos</i>.*</p>
<dd> lexicographer files to use to build database</p>
<dt><code>cntlist</code></p>
<dd> file of combined semantic concordance <code>cntlist</code> files. Used to assign sense numbers in WordNet database</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-cntlist/">cntlist</a></code>(5), <code><a href="/docs/linux/man/5-lexnames/">lexnames</a></code>(5), <code><a href="/docs/linux/man/5-senseidx/">senseidx</a></code>(5), <code><a href="/docs/linux/man/5-wndb/">wndb</a></code>(5), <code><a href="/docs/linux/man/5-wninput/">wninput</a></code>(5), <code><a href="/docs/linux/man/7-uniqbeg/">uniqbeg</a></code>(7), <code><a href="/docs/linux/man/7-wngloss/">wngloss</a></code>(7).</p>
<h2>DIAGNOSTICS</h2>
<p> Exit status is normally 0. Exit status is -1 if non-specific error occurs. If syntactic or structural errors exist, exit status is number of errors detected.</p>
<dl>
<dt><code>usage: grind [-v] [-s] [-Llogfile] [-a ] [-d] [-i] [-o] [-n] filename [filename&#8230;]</code></p>
<dd> Invalid options were specified on the command line.</p>
<dt><code>No input files processed.</code></p>
<dd> None of the filenames specified were of the appropriate form.</p>
<dt><i>n</i> syntactic errors found.</p>
<dd> Syntax errors were found while parsing the input files.</p>
<dt><i>n</i> structural errors found.</p>
<dd> Pointer errors were found that could not be automatically corrected.</dl>
<h2>BUGS</h2>
<p> Please report bugs to <code>wordnet [at] princeton.edu</code>. </p>
<h2>Index</h2>
