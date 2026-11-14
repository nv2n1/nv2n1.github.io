---
title: "po4a-build-conf(5)"
name: "po4a-build-conf"
section: "5"
letter: "p"
url: "/docs/linux/man/5-po4a-build-conf/"
---

po4a-build.conf - configuration file for building translated content

<h2>Introduction</h2>

<i>po4a-build.conf</i> describes how <tt>&quot;po4a-build&quot;</tt> should build translated and untranslated documentation from a set of untranslated source documents and corresponding <font SIZE="-1">PO</font> files. 

 All supported formats, in all supported combinations, can be handled in a single <i>po4a-build.conf</i> configuration file and in a single call to <tt>&quot;po4a-build&quot;</tt>. However, you can also choose to separate the <i>po/</i> directories and have one configuration file for each run. (Call <tt>&quot;po4a-build -f FILE&quot;</tt> for each one.) 

 Note that although <i>po4a-build</i> includes support for adding gettext support for translation of script output messages, <i>po4a-build.conf</i> itself has no bearing on such translations. <i>po4a-build.conf</i> only relates to translating static content like manpages. 

 For <i>po4a-build</i> support of runtime message translation, see <i><a HREF="/docs/linux/man/7-po4a-runtime/">po4a-runtime</a></i>(7).

<h2>Supported formats</h2>

Currently, <tt>&quot;po4a-build&quot;</tt> supports the following combinations:
<dl><dt>DocBook <font SIZE="-1">XML</font> for sections 1 and 3
<dd>Typically used for manpages for shell scripts or other interpreters that do not have their own documentation format like <font SIZE="-1">POD.</font> Suitable <font SIZE="-1">XML</font> can be generated directly from an existing manpage using <tt>&quot;doclifter&quot;</tt> and <tt>&quot;po4a-build&quot;</tt> will then generate a <font SIZE="-1">POT</font> file with no extra workload. The <font SIZE="-1">POT</font> file can then be offered for translation and the <font SIZE="-1">PO</font> files added to the relevant <i>po/</i> directory. <tt>&quot;po4a-build&quot;</tt> will then prepare not only the untranslated manpage from the <tt>&quot;doclifter&quot;</tt> <font SIZE="-1">XML</font> but also use <tt>&quot;po4a&quot;</tt> to prepare translated <font SIZE="-1">XML</font> from the <font SIZE="-1">PO</font> files and then build translated manpages from the <font SIZE="-1">XML.</font> 

 Manpages are generated using default support in docbook-xsl - the stylesheet used can be overridden using the <tt>&quot;XSLFILE&quot;</tt> setting in the <tt>&quot;po4a-build&quot;</tt> configuration file.
<dt>DocBook <font SIZE="-1">XML</font> for <font SIZE="-1">HTML</font>
<dd>The default stylesheet used to prepare the final <font SIZE="-1">HTML</font> can be overridden using the <tt>&quot;HTMLXSL&quot;</tt> setting in the <tt>&quot;po4a-build&quot;</tt> configuration file.
<dt><font SIZE="-1">POD</font> for sections 1, 3, 5 and 7
<dd>pod2man is used to convert <font SIZE="-1">POD</font> content for each of the supported sections. 

 Use <tt>&quot;PODFILE&quot;</tt> for section 1, <tt>&quot;PODMODULES&quot;</tt> for section 3, <tt>&quot;POD5FILES&quot;</tt> for section 5 and <tt>&quot;POD7FILES&quot;</tt> for section 7. 

 For content in sections 5 or 7 (which tends to need a filename which is also used for section 1 content), if the filename includes the 5 or 7 as part of the filename, this (and any filename extension) will be automatically stripped. 

 e.g. to prepare <i>/usr/share/man/man7/po4a.7.gz</i>: 

 <pre> # POD files for section 7
 POD7FILES=&quot;doc/po4a.7.pod&quot;</pre></dl>

<h2>File contents</h2>

Configuration values can appear in any order in the configuration file. 

 Any content after a '#' is ignored. 

 Any value that would always be empty can be dropped from the file. 

 Some configuration fields are required - <i>po4a-build</i> could end up with nothing to do if required fields are empty.
<dl><dt><font SIZE="-1">CONFIG</font>
<dd>Required. 

 Name and location of the (temporary) <tt>&quot;po4a&quot;</tt> configuration file that <tt>&quot;po4a-build&quot;</tt> will generate and maintain. This file does not need to live in your version control system and can be safely cleaned up during the package build. 

 <pre> # name and location of the config file
 CONFIG=&quot;_build/po4a.config&quot;</pre><dt><font SIZE="-1">PODIR</font>
<dd>Required. 

 Directory containing the <font SIZE="-1">PO</font> files for <font SIZE="-1">ALL</font> translations handled by this configuration file. All strings will be merged into a <font SIZE="-1">POT</font> file in this directory and all <font SIZE="-1">PO</font> files merged with that <font SIZE="-1">POT</font> file. Any <font SIZE="-1">KEEP</font> threshold (see below) will be applied across all strings from all input files specified in this file and all <font SIZE="-1">PO</font> files in this directory. The directory does not need to be called 'po'. Please note, however, that some statistic tools expect the name to be 'po', therefor it is recommended to keep this name. 

 <pre> # po directory for manpages/docs
 PODIR=&quot;po/pod&quot;</pre><dt><font SIZE="-1">POTFILE</font>
<dd>Required. 

 Path to the <font SIZE="-1">POT</font> file (relative to the location of this configuration file) that will be generated, maintained and updated by <tt>&quot;po4a-build&quot;</tt> for these translations. 

 <pre> # POT file path
 POTFILE=&quot;po/pod/po4a-pod.pot&quot;</pre><dt><font SIZE="-1">BASEDIR</font>
<dd>Required. 

 Base directory for writing out the translated content. 

 <pre> # base directory for generated files, e.g. doc
 BASEDIR=&quot;_build&quot;</pre><dt><font SIZE="-1">BINARIES</font>
<dd>Required. 

 Even if only one package is built, at least one value is required here. 

 The string itself is arbitrary but typically consists of the package name. Generated content will then appear in subdirectories of <i></i><font SIZE="-1"><i>BASEDIR/BINARIES</i></font><i></i>: 

 <pre> _build/po4a/man/man1/foo.1</pre>If the package builds more than one binary package (i.e. one source package and multiple .deb or .rpm files), this field can help isolate content intended for each target, making it easier to automate the build process. 

 Separate strings with a space. 

 <pre> # binary packages that will contain generated manpages
 BINARIES=&quot;po4a&quot;</pre><dt><font SIZE="-1">KEEP</font>
<dd>Value to be passed directly to <tt>&quot;po4a -k&quot;</tt> to specify the threshold for correctly translated content before a particular translation is omitted from the build. Leave empty or remove to use the default (80%) or specify zero to force the inclusion of all content, even if completely untranslated. 

 For full control over such behaviour, consider carefully which files are assigned to which <i>po4a-build.conf</i> configuration file. 

 Note that having lots of files in one <font SIZE="-1">POT</font> file can be more convenient for translators, especially if files have strings in common. Conversely, <font SIZE="-1">POT</font> files with thousands of long strings are daunting for translators, leading to long string freezes. 

 <pre> # minimal threshold for translation percentage to keep
 KEEP=</pre><dt><font SIZE="-1">XMLMAN1</font>
<dd>DocBook <font SIZE="-1">XML</font> files to generate manpages in section 1. Separate filenames with spaces. All files need to be in the <font SIZE="-1">XMLDIR</font> directory. 

 It is common practice to fold multiple <font SIZE="-1">XML</font> files into one book, in order to provide a table of contents etc. If the book contains files also specified in <font SIZE="-1">XMLMAN3,</font> only specify the <font SIZE="-1">XML</font> files for section 1 here, not the book itself. If the book only contains content for this section, only specify the book file. 

 <pre> # DocBook XML files for section 1
 XMLMAN1=&quot;po4a-build.xml po4aman-display-po.xml po4apod-display-po.xml&quot;</pre><dt><font SIZE="-1">XMLMAN3</font>
<dd>DocBook <font SIZE="-1">XML</font> files to generate manpages in section 3. Separate filenames with spaces. All files need to be in the <font SIZE="-1">XMLDIR</font> directory. 

 It is common practice to fold multiple <font SIZE="-1">XML</font> files into one book, in order to provide a table of contents etc. If the book contains files also specified in <font SIZE="-1">XMLMAN1,</font> only specify the <font SIZE="-1">XML</font> files for section 3 here, not the book itself. If the book only contains content for this section, only specify the book file. 

 <pre> # DocBook XML files for section 3
 XMLMAN3=&quot;&quot;</pre><dt><font SIZE="-1">XMLDIR</font>
<dd>Location of all the DocBook <font SIZE="-1">XML</font> files. Currently, <tt>&quot;po4a-build&quot;</tt> expects to be able to find all files listed in <font SIZE="-1">XMLMAN1</font> and <font SIZE="-1">XMLMAN3</font> by looking for *.xml files in this directory. 

 Must be specified if <font SIZE="-1">XMLMAN1</font> or <font SIZE="-1">XMLMAN3</font> are used. Paths are relative to the location of the configuration file. 

 <pre> # location of the XML files
 XMLDIR=&quot;share/doc/&quot;</pre><dt><font SIZE="-1">XMLPACKAGES</font>
<dd>Which packages, out of the list in <font SIZE="-1">BINARIES,</font> use <font SIZE="-1">XML</font> source content. 

 If any values are given in <font SIZE="-1">XMLMAN1</font> or <font SIZE="-1">XMLMAN3,</font> a value must be given here as well. 

 <pre> # binary packages using DocBook XML &amp; xsltproc
 XMLPACKAGES=&quot;po4a&quot;</pre><dt><font SIZE="-1">DOCBOOKDIR</font>
<dd>Similar to <font SIZE="-1">XMLDIR</font> but only used to prepare the translated DocBook files. If your package wants to use .sgml files, please discuss how these should be built on the po4a-devel mailing list. 

 <pre> # pattern to find the .docbook files
 DOCBOOKDIR=&quot;&quot;</pre><dt><font SIZE="-1">XSLFILE</font>
<dd><font SIZE="-1">XSL</font> stylesheet used to prepare the translated and untranslated content from the DocBook <font SIZE="-1">XML</font> files. 

 <pre> # XSL file to use for DocBook XML
 XSLFILE=&quot;<a rel="nofollow" HREF="http://docbook.sourceforge.net/release/xsl/current/manpages/docbook.xsl">http://docbook.sourceforge.net/release/xsl/current/manpages/docbook.xsl</a>&quot;</pre><dt><font SIZE="-1">PODFILE</font>
<dd><font SIZE="-1">POD</font> files for generating manpage content in section 1. Separate <font SIZE="-1">POD</font> files with spaces. Paths, if used, need to be relative to the location of the specified configuration file. 

 <pre> # POD files for section 1
 PODFILE=&quot;po4a po4a-gettextize po4a-normalize scripts/msguntypot&quot;</pre><dt><font SIZE="-1">PODMODULES</font>
<dd>Specialised support for Perl modules containing <font SIZE="-1">POD</font> content - the module name will be reconstructed from the path (so this should be the typical Perl layout) and manpages are automatically put into section 3. 

 <pre> # POD files for section 3 - module names regenerated from the path
 PODMODULES=&quot;lib/Locale/Po4a/*.pm&quot;</pre><dt><font SIZE="-1">POD5FILES</font>
<dd>Arbitrary <font SIZE="-1">POD</font> content for use generating manpages for section 5. Paths, if used, need to be relative to the location of the specified configuration file. 

 For content in sections 5 or 7 (which tends to need a filename which is also used for section 1 content), if the filename includes the 5 or 7 as part of the filename, this (and any filename extension) will be automatically stripped. 

 <pre> # POD files for section 5
 POD5FILES=&quot;doc/po4a-build.conf.5.pod&quot;</pre><dt><font SIZE="-1">POD7FILES</font>
<dd>Arbitrary <font SIZE="-1">POD</font> content for use generating manpages for section 7. Paths, if used, need to be relative to the location of the specified configuration file. 

 For content in sections 5 or 7 (which tends to need a filename which is also used for section 1 content), if the filename includes the 5 or 7 as part of the filename, this (and any filename extension) will be automatically stripped. 

 <pre> # POD files for section 7
 POD7FILES=&quot;doc/po4a.7.pod&quot;</pre><dt><font SIZE="-1">PODPACKAGES</font>
<dd>Similar to <font SIZE="-1">XMLPACKAGES -</font> any package expecting content to be built from <font SIZE="-1">POD</font> files needs to include a value in <font SIZE="-1">PODPACKAGES.</font> Required if any values are specified for <font SIZE="-1">PODFILE, PODMODULES, POD5FILES</font> or <font SIZE="-1">POD7FILES.</font> 

 <pre> # binary packages using POD
 PODPACKAGES=&quot;po4a&quot;</pre><dt><font SIZE="-1">HTMLDIR</font>
<dd>Subdirectory of <font SIZE="-1">BASEDIR</font> to be used to output the untranslated and translated <font SIZE="-1">HTML</font> output. 

 <pre> # HTML output (subdirectory of BASEDIR)
 HTMLDIR=&quot;&quot;</pre><dt><font SIZE="-1">HTMLFILE</font>
<dd>DocBook file to be converted to <font SIZE="-1">HTML </font>(may be the same as one of the files in <font SIZE="-1">XMLMAN1</font> or <font SIZE="-1">XMLMAN3</font>). Sections are not relevant to <font SIZE="-1">HTML</font> output, so feel free to use the single book file here so that the <font SIZE="-1">HTML</font> has a table of contents etc. 

 <pre> # HTML DocBook file
 HTMLFILE=&quot;&quot;</pre><dt><font SIZE="-1">HTMLXSL</font>
<dd>The default is to use a chunked <font SIZE="-1">XSL</font> stylesheet. It is not currently supported to use more than one stylesheet per <font SIZE="-1">HTML</font> run. 

 <pre> # XSL file to use for HTML
 HTMLXSL=&quot;<a rel="nofollow" HREF="http://docbook.sourceforge.net/release/xsl/current/html/chunk.xsl">http://docbook.sourceforge.net/release/xsl/current/html/chunk.xsl</a>&quot;</pre></dl>

<h2>Authors</h2>

<pre> Neil Williams &lt;linux [at] codehelp.co.uk&gt;</pre>
