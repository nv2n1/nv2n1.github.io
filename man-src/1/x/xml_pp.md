---
title: "xml_pp(1)"
name: "xml_pp"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xml_pp/"
---

<h2 class="name">NAME</h2>
 

 xml_pp - xml pretty-printer 

<h2>SYNOPSYS</h2>

 xml_pp [options] [&lt;files&gt;]

<h2>DESCRIPTION</h2>

 <font SIZE="-1">XML</font> pretty printer using XML::Twig

<h2>OPTIONS</h2>

<dl>
<dt>-i[&lt;extension&gt;]
<dd> edits the file(s) in place, if an extension is provided (no space between <tt>&quot;-i&quot;</tt> and the extension) then the original file is backed-up with that extension 

 The rules for the extension are the same as Perl's (see perldoc perlrun): if the extension includes no ``*'' then it is appended to the original file name, If the extension does contain one or more ``*'' characters, then each ``*'' is replaced with the current filename.
<dt>-s &lt;style&gt;
<dd> the style to use for pretty printing: none, nsgmls, nice, indented, record, or record_c (see XML::Twig docs for the exact description of those styles), 'indented' by default
<dt>-p &lt;tag(s)&gt;
<dd> preserves white spaces in tags. You can use several <tt>&quot;-p&quot;</tt> options or quote the tags if you need more than one
<dt>-e &lt;encoding&gt;
<dd> use XML::Twig output_encoding (based on Text::Iconv or Unicode::Map8 and Unicode::String) to set the output encoding. By default the original encoding is preserved. 

 If this option is used the <font SIZE="-1">XML</font> declaration is updated (and created if there was none). 

 Make sure that the encoding is supported by the parser you use if you want to be able to process the pretty_printed file (XML::Parser does not support 'latin1' for example, you have to use 'iso-8859-1')
<dt>-l
<dd> loads the documents in memory instead of outputing them as they are being parsed. 

 This prevents a bug (see <font SIZE="-1">BUGS</font>) but uses more memory
<dt>-f &lt;file&gt;
<dd> read the list of files to process from &lt;file&gt;, one per line
<dt>-v
<dd> verbose (list the current file being processed)
<dt>--
<dd> stop argument processing (to process files that start with -)
<dt>-h
<dd> display help</dl>

<h2>EXAMPLES</h2>

 <pre>
  xml_pp foo.xml &gt; foo_pp.xml           # pretty print foo.xml 
  xml_pp &lt; foo.xml &gt; foo_pp.xml         # pretty print from standard input
  xml_pp -v -i.bak *.xml                # pretty print .xml files, with backups
  xml_pp -v -i'orig_*' *.xml            # backups are named orig_&lt;filename&gt;
  xml_pp -i -p pre foo.xhtml            # preserve spaces in pre tags
  
  xml_pp -i.bak -p 'pre code' foo.xml   # preserve spaces in pre and code tags
  xml_pp -i.bak -p pre -p code foo.xml  # same
  xml_pp -i -s record mydb_export.xml   # pretty print using the record style
  xml_pp -e utf8 -i foo.xml             # output will be in utf8
  xml_pp -e iso-8859-1 -i foo.xml       # output will be in iso-8859-1
  xml_pp -v -i.bak -f lof               # pretty print in place files from lof
  
  xml_pp -- -i.xml                      # pretty print the -i.xml file
  xml_pp -l foo.xml                     # loads the entire file in memory 
                                        # before pretty printing it
  xml_pp -h                             # display help
</pre>

<h2>BUGS</h2>

 Elements with mixed content that start with an embedded element get an extra \n 

 <pre>
  &lt;elt&gt;&lt;b&gt;b&lt;/b&gt;toto&lt;b&gt;bold&lt;/b&gt;&lt;/elt&gt;
</pre> 

 will be output as 

 <pre>
  &lt;elt&gt;
    &lt;b&gt;b&lt;/b&gt;toto&lt;b&gt;bold&lt;/b&gt;&lt;/elt&gt;
</pre> 

 Using the <tt>&quot;-l&quot;</tt> option solves this bug (but uses more memory)

<h2>TODO</h2>

 update XML::Twig to use Encode with perl 5.8.0

<h2>AUTHOR</h2>

 Michel Rodriguez &lt;mirod [at] xmltwig.com&gt; 

<h2>Index</h2>


