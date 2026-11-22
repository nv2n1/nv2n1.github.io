---

title: "xml_spellcheck(1)"
name: "xml_spellcheck"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xml_spellcheck/"
---

xml_spellcheck - spellcheck XML files 

<h2>SYNOPSIS</h2>

 <pre>
  xml_spellcheck [options] &lt;files&gt;
</pre>

<h2>DESCRIPTION</h2>

 xml_spellcheck lets you spell check the content of an XML file. It extracts the text (the content of elements and optionally of attributes), call a spell checker on it and then recreates the XML document.

<h2>OPTIONS</h2>

 Note that all options can be abbreviated to the first letter
<dl>
<dt>--conf &lt;configuration_file&gt;
</dt><dd> Gets the options from a configuration file. NOT IMPLEMENTED YET.
</dd><dt>--spellchecker &lt;spellchecker&gt;
</dt><dd> The command to use for spell checking, including any option 
 By default <tt>&quot;aspell -c&quot;</tt> is used
</dd><dt>--backup-extension &lt;extension&gt;
</dt><dd> By default the original file is saved with a <tt>&quot;.bak&quot;</tt> extension. This option changes the extension
</dd><dt>--attributes
</dt><dd> Spell check attribute content. By default attribute values are NOT spell checked. NOT YET IMPLEMENTED
</dd><dt>--exclude_elements &lt;list_of_excluded_elements&gt;
</dt><dd> A list of elements that should not be spell checked
</dd><dt>--include_elements &lt;list_of_included_elements&gt;
</dt><dd> A list of elements that should be spell checked (by default all elements are spell checked). 
 <tt>&quot;--exclude_elements&quot;</tt> and <tt>&quot;--include_elements&quot;</tt> are mutually exclusive
</dd><dt>--pretty_print &lt;optional_pretty_print_style&gt;
</dt><dd> A pretty print style for the document, as defined in XML::Twig. If the option is provided without a value then the <tt>&quot;indented&quot;</tt> style is used
</dd><dt>--version
</dt><dd> Dislay the tool version and exit
</dd><dt>--help
</dt><dd> Display help message and exit
</dd><dt>--man
</dt><dd> Display longer help message and exit</dd></dl>

<h2>EXAMPLES</h2>

<h2>BUGS</h2>

<h2>TODO</h2>

<dl>
<dt>--conf option
</dt><dd>
</dd><dt>--attribute option
</dt><dd></dd></dl>

<h2>PRE-REQUISITE</h2>

 XML::Twig, Getopt::Long, Pod::Usage, File::Temp XML::Twig requires XML::Parser.

<h2>SEE ALSO</h2>

 XML::Twig

<h2>COPYRIGHT AND DISCLAIMER</h2>

 This program is Copyright 2003 by Michel Rodriguez 

 This program is free software; you can redistribute it and/or modify it under the terms of the Perl Artistic License or the GNU General Public License as published by the Free Software Foundation either version 2 of the License, or (at your option) any later version. 

 This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MER- CHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details. 

 If you do not have a copy of the GNU General Public License write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

<h2>AUTHOR</h2>

 Michel Rodriguez &lt;mirod [at] xmltwig.com&gt; 

 xml_spellcheck is available at <a rel="nofollow" HREF="http://www.xmltwig.com/xmltwig/">http://www.xmltwig.com/xmltwig/</a>
