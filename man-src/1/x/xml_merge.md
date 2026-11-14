---
title: "xml_merge(1)"
name: "xml_merge"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xml_merge/"
---

<h2 class="name">NAME</h2>
 

 <pre>
  xml_merge - merge back XML files split with C&lt;xml_split&gt;
</pre> 

<h2>DESCRIPTION</h2>

 <tt>&quot;xml_merge&quot;</tt> takes several xml files that have been split using <tt>&quot;xml_split&quot;</tt> and recreates a single file.

<h2>OPTIONS</h2>

<dl>
<dt>-o &lt;output_file&gt;
<dd> unless this option is used the program output goes to <font SIZE="-1">STDOUT</font>
<dt>-i
<dd> the files use XInclude instead of processing instructions (they were created using the <tt>&quot;-i&quot;</tt> option in <tt>&quot;xml_split&quot;</tt>)
<dt>-v
<dd> verbose output
<dt>-V
<dd> outputs version and exit
<dt>-h
<dd> short help
<dt>-m
<dd> man (requires pod2text to be in the path)</dl>

<h2>EXAMPLES</h2>

 <pre>
  xml_merge foo-00.xml             # output to stdout
  xml_merge -o foo.xml foo-00.xml  # output to foo.xml
</pre>

<h2>SEE ALSO</h2>

 XML::Twig, xml_split

<h2>TODO/BUGS</h2>

<h2>AUTHOR</h2>

 Michel Rodriguez &lt;mirod [at] cpan.org&gt;

<h2>LICENSE</h2>

 This tool is free software; you can redistribute it and/or modify it under the same terms as Perl itself. 

<h2>Index</h2>


