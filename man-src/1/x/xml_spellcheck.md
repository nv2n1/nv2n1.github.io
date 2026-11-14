---
title: "xml_spellcheck(1)"
name: "xml_spellcheck"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xml_spellcheck/"
---

<h2 class="name">NAME</h2>
 

 xml_spellcheck - spellcheck XML files 

<h2>SYNOPSIS</h2>

 <pre>
  xml_spellcheck [options] &lt;files&gt;
</pre>

<h2>DESCRIPTION</h2>

 xml_spellcheck lets you spell check the content of an <font SIZE="-1">XML</font> file. It extracts the text (the content of elements and optionally of attributes), call a spell checker on it and then recreates the <font SIZE="-1">XML</font> document.

<h2>OPTIONS</h2>

 Note that all options can be abbreviated to the first letter
<dl>
<dt>--conf &lt;configuration_file&gt;
<dd> Gets the options from a configuration file. <font SIZE="-1">NOT IMPLEMENTED YET.</font>
<dt>--spellchecker &lt;spellchecker&gt;
<dd> The command to use for spell checking, including any option 

 By default <tt>&quot;aspell -c&quot;</tt> is used
<dt>--backup-extension &lt;extension&gt;
<dd> By default the original file is saved with a <tt>&quot;.bak&quot;</tt> extension. This option changes the extension
<dt>--attributes
<dd> Spell check attribute content. By default attribute values are <font SIZE="-1">NOT</font> spell checked. <font SIZE="-1">NOT YET IMPLEMENTED</font>
<dt>--exclude_elements &lt;list_of_excluded_elements&gt;
<dd> A list of elements that should not be spell checked
<dt>--include_elements &lt;list_of_included_elements&gt;
<dd> A list of elements that should be spell checked (by default all elements are spell checked). 

 <tt>&quot;--exclude_elements&quot;</tt> and <tt>&quot;--include_elements&quot;</tt> are mutually exclusive
<dt>--pretty_print &lt;optional_pretty_print_style&gt;
<dd> A pretty print style for the document, as defined in XML::Twig. If the option is provided without a value then the <tt>&quot;indented&quot;</tt> style is used
<dt>--version
<dd> Dislay the tool version and exit
<dt>--help
<dd> Display help message and exit
<dt>--man
<dd> Display longer help message and exit</dl>

<h2>EXAMPLES</h2>

<h2>BUGS</h2>

<h2>TODO</h2>

<dl>
<dt>--conf option
<dd>
<dt>--attribute option
<dd></dl>

<h2>PRE-REQUISITE</h2>

 XML::Twig, Getopt::Long, Pod::Usage, File::Temp XML::Twig requires XML::Parser.

<h2>SEE ALSO</h2>

 XML::Twig

<h2>COPYRIGHT AND DISCLAIMER</h2>

 This program is Copyright 2003 by Michel Rodriguez 

 This program is free software; you can redistribute it and/or modify it under the terms of the Perl Artistic License or the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation either version 2 of the License, or (at your option) any later version. 

 This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MER- CHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. 

 If you do not have a copy of the <font SIZE="-1">GNU</font> General Public License write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA 02139, USA.</font>

<h2>AUTHOR</h2>

 Michel Rodriguez &lt;mirod [at] xmltwig.com&gt; 

 xml_spellcheck is available at <a rel="nofollow" HREF="http://www.xmltwig.com/xmltwig/">http://www.xmltwig.com/xmltwig/</a> 

<h2>Index</h2>


