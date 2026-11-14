---
title: "xml_split(1)"
name: "xml_split"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xml_split/"
---

<h2 class="name">NAME</h2>
 

 <pre>
  xml_split - cut a big XML file into smaller chunks
</pre> 

<h2>DESCRIPTION</h2>

 <tt>&quot;xml_split&quot;</tt> takes a (presumably big) <font SIZE="-1">XML</font> file and split it in several smaller files. The memory used is the memory needed for the biggest chunk (ie memory is reused for each new chunk). 

 It can split at a given level in the tree (the default, splits children of the root), or on a condition (using the subset of XPath understood by XML::Twig, so <tt>&quot;section&quot;</tt> or <tt>&quot;/doc/section&quot;</tt>). 

 Each generated file is replaced by a processing instruction that will allow <tt>&quot;xml_merge&quot;</tt> to rebuild the original document. The processing instruction format is <tt>&quot;&lt;?merge subdocs=[01] :&lt;filename&gt; ?&gt;&quot;</tt> 

 File names are &lt;file&gt;-&lt;nb&gt;.xml, with &lt;file&gt;-00.xml holding the main document.

<h2>OPTIONS</h2>

<dl>
<dt>-l &lt;level&gt;
<dd> level to cut at: 1 generates a file for each child of the root, 2 for each grand child 

 defaults to 1
<dt>-c &lt;condition&gt;
<dd> generate a file for each element that passes the condition 

 xml_split -c &lt;section&gt; will put each <tt>&quot;section&quot;</tt> element in its own file (nested sections are handled too) 

 Note that at the moment this option is a lot slower than using <tt>&quot;-l&quot;</tt>
<dt>-s &lt;size&gt;
<dd> generates files of (approximately) &lt;size&gt;. The content of each file is enclosed in a new element (<tt>&quot;xml_split::root&quot;</tt>), so it's well-formed <font SIZE="-1">XML.</font> The size can be given in bytes, Kb, Mb or Gb.
<dt>-g &lt;nb&gt;
<dd> groups &lt;nb&gt; elements in a single file. The content of each file is enclosed in a new element (<tt>&quot;xml_split::root&quot;</tt>), so it's well-formed <font SIZE="-1">XML.</font>
<dt>-b &lt;name&gt;
<dd> base name for the output, files will be named &lt;base&gt;-&lt;nb&gt;&lt;.ext&gt; 

 &lt;nb&gt; is a sequence number, see below <tt>&quot;--nb_digits&quot;</tt> &lt;ext&gt; is an extension, see below <tt>&quot;--extension&quot;</tt> 

 defaults to the original file name (if available) or <tt>&quot;out&quot;</tt> (if input comes from the standard input)
<dt>-n &lt;nb&gt;
<dd> number of digits in the sequence number for each file 

 if more digits than &lt;nb&gt; are needed, then they are used: if <tt>&quot;--nb_digits 2&quot;</tt> is used and 112 files are generated they will be named <tt>&quot;&lt;file&gt;-01.xml&quot;</tt> to <tt>&quot;&lt;file&gt;-112.xml&quot;</tt> 

 defaults to 2
<dt>-e &lt;ext&gt;
<dd> extension to use for generated files 

 defaults to the original file extension or <tt>&quot;.xml&quot;</tt>
<dt>-i
<dd> use XInclude elements instead of Processing Instructions to mark where sub files need to be included
<dt>-v
<dd> verbose output 

 Note that this option can slow down processing considerably (by an order of magnitude) when generating lots of small documents
<dt>-V
<dd> outputs version and exit
<dt>-h
<dd> short help
<dt>-m
<dd> man (requires pod2text to be in the path)</dl>

<h2>EXAMPLES</h2>

 <pre>
  xml_split foo.xml             # split at level 1
  xml_split -l 2 foo.xml        # split at level 2
  xml_split -c section foo.xml  # a file is generated for each section element
                                # nested sections are split properly
</pre>

<h2>SEE ALSO</h2>

 XML::Twig, xml_merge

<h2>TODO</h2>

<dl>
<dt>optimize the code
<dd> any idea welcome! I have already implemented most of what I thought would improve performances.
<dt>provide other methods that PIs to keep merge information
<dd> XInclude is a good candidate (alpha support added in 0.04). 

 using entities, which would seem the natural way to do it, doesn't work, as they make it impossible to have both the main document and the sub docs to be well-formed if the sub docs include sub-sub docs (you can't have entity declarations in an entity)</dl>

<h2>AUTHOR</h2>

 Michel Rodriguez &lt;mirod [at] cpan.org&gt;

<h2>LICENSE</h2>

 This tool is free software; you can redistribute it and/or modify it under the same terms as Perl itself. 

<h2>Index</h2>


