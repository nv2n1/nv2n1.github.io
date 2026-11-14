---
title: "autogsdoc(1)"
name: "autogsdoc"
section: "1"
letter: "a"
url: "/docs/linux/man/1-autogsdoc/"
description: "autogsdoc – GNUstep API documentation generator and XML->HTML converter"
---

<h2>NAME</h2>
<p> autogsdoc &#8211; GNUstep API documentation generator and XML-&gt;HTML converter </p>
<h2>SYNOPSIS</h2>
<p> <code>autogsdoc</code> [<code>-Files</code> <i>filename</i>] [<code>-GenerateHtml</code> <i>YES|no</i>] [<code>-Clean</code> <i>yes|NO</i>] [<code>-CleanTemplates</code> <i>yes|NO</i>] [<code>-IgnoreDependencies</code> <i>yes|NO</i>] [<code>-MakeDependencies</code> <i>yes|NO</i>] [<code>-ShowDependencies</code> <i>yes|NO</i>] [<code>-HeaderDirectory</code> <i>path</i>] [<code>-DocumentationDirectory</code> <i>path</i>] [<code>-Declared</code> <i>location</i>] [<code>-Project</code> <i>title</i>] [<code>-Standards</code> <i>yes|NO</i>] [<code>-DocumentAllInstanceVariables</code> <i>yes|NO</i>] [<code>-DocumentInstanceVariables</code> <i>YES|no</i>] [<code>-InstanceVariablesAtEnd</code> <i>yes|NO</i>] [<code>-ConstantsTemplate</code> <i>filename</i>] [<code>-FunctionsTemplate</code> <i>filename</i>] [<code>-MacrosTemplate</code> <i>filename</i>] [<code>-TypedefsTemplate</code> <i>filename</i>] [<code>-VariablesTemplate</code> <i>filename</i>] [<code>-SystemProjects</code> <i>string</i>] [<code>-LocalProjects</code> <i>string</i>] [<code>-Projects</code> <i>dictString</i>] [<code>-Verbose</code> <i>yes|NO</i>] [<code>-Warn</code> <i>yes|NO</i>] [<code>-WordMap</code> <i>dictString</i>] <i>[</i>files<i>]</i> </p>
<h2>DESCRIPTION</h2>
<p> The autogsdoc tool is a command-line utility that helps developers produce reference documentation for GNUstep APIs. It also enables developers to write and maintain other documentation in XML and have it converted to HTML. In detail, autogsdoc will:</p>
<dl>
<dt>&#8211;</p>
<dd> Extract special comments describing the public interfaces of classes, categories, protocols, functions, and macros from Objective C source code (header files and optionally source files) into GSDoc XML files.</p>
<dt>&#8211;</p>
<dd> Convert GSDoc XML files, whether generated from source code or written manually by developers, into HTML.</p>
<dt>&#8211;</p>
<dd> Construct indices based on GSDoc XML file sets, and convert those to HTML as well. </p>
</dl>
<p> The most common usage this is to run the command with one or more header file names as arguments &#8230; the tool will automatically parse corresponding source files in the same directory as the headers (or the current directory, or the directory specified using the DocumentationDirectory default), and produce GSDoc and HTML files as output. For best results this mode should be run from the directory containing the source files. (Note that since C is a subset of Objective C, this tool can operate to document functions and other C structures in plain C source.) </p>
<p> GSDoc files may also be given directly in addition or by themselves, and will be converted to HTML. See the GSDoc HTML documentation or the <a href="/docs/linux/man/7-gsdoc/">gsdoc</a>(7) man page for information on the GSDoc format. </p>
<p> Finally, HTML files may be given on the command line. Cross-references to other parts of code documentation found within them will be rewritten based on what is found in the project currently. </p>
<h2>SOURCE CODE MARKUP</h2>
<p> The source code parser will automatically produce GSDoc documents listing the methods in the classes found in the source files, and it will include text from specially formatted comments from the source files. </p>
<p> Any comment beginning with slash and <i>two</i> asterisks rather than the common slash and single asterisk, is taken to be GSDoc markup, to be use as the description of the class or method following it. This comment text is reformatted and then inserted into the output.</p>
<dl>
<dt>
<dd> Where multiple comments are associated with the same item, they are joined together with a line break (&lt;br/&gt;) between each if necessary. </p>
<p> The tool can easily be used to document programs as well as libraries, simply by giving it the name of the source file containing the main() function of the program &#8211; it takes the special comments from that function and handles them specially, inserting them as a section at the end of the first chapter of the document (it creates the first chapter if necessary). </p>
<p> <code>Options</code> are described in the section <i>Arguments and Defaults</i> below. </p>
</dl>
<h2>EXTRA MARKUP</h2>
<p> There are some cases where special extra processing is performed, predominantly in the first comment found in the source file, from which various chunks of GSDoc markup may be extracted and placed into appropriate locations in the output document &#8211;</p>
<dl>
<dt><code>AutogsdocSource:</p>
<dd> In any line where </code><i>AutogsdocSource:</i> is found, the remainder of the line is taken as a source file name to be used instead of making the assumption that each .h file processed uses a .m file of the same name. You may supply multiple <i>AutogsdocSource:</i> lines where a header file declares items which are defined in multiple source files. If a file name is absolute, it is used just as supplied. If on the other hand, it is a relative path, the software looks for the source file first relative to the location of the header file, and if not found there, relative to the current directory in which autogsdoc is running, and finally relative to the directory specified by the <i>DocumentationDirectory</i> default.</p>
<dt><code>&lt;abstract&gt;</p>
<dd> An abstract of the content of the document &#8230; placed in the head of the GSDoc output.</p>
<dt>&lt;author&gt;</p>
<dd> A description of the author of the code &#8211; may be repeated to handle the case where a document has multiple authors. Placed in the head of the GSDoc output. As an aid to readability of the source, some special additional processing is performed related to the document author &#8211; Any line of the form </code><font SIZE="-1"><code>&#8216;Author:</code></font><code> name &lt;email-address&gt;&#8217;, or </code><font SIZE="-1"><code>&#8216;By:</code></font><code> name &lt;email-address&gt;&#8217;, or </code><font SIZE="-1"><code>&#8216;Author:</code></font><code> name&#8217; or </code><font SIZE="-1"><code>&#8216;By:</code></font><code> name&#8217; will be recognised and converted to an </code><i>author</i> element, possibly containing an <i>email</i> element.</p>
<dt><code>&lt;back&gt;</p>
<dd> Placed in the GSDoc output just before the end of the body of the document &#8211; intended to be used for appendices, index etc..</p>
<dt>&lt;chapter&gt;</p>
<dd> Placed immediately before any generated class documentation &#8230; intended to be used to provide overall description of how the code being documented works. Any documentation for the main() function of a program is inserted as a section at the end of this chapter.</p>
<dt>&lt;copy&gt;</p>
<dd> Copyright of the content of the document &#8230; placed in the head of the GSDoc output. As an aid to readability of the source, some special additional processing is performed &#8211; Any line of the form &#8216;Copyright (C) text&#8217; will be recognised and converted to a </code><i>copy</i> element.</p>
<dt><code>&lt;date&gt;</p>
<dd> Date of the revision of the document &#8230; placed in the head of the GSDoc output. If this is omitted the tool will try to construct a value from the RCS Date tag (if available).</p>
<dt>&lt;front&gt;</p>
<dd> Inserted into the document at the start of the body &#8230; intended to provide for introduction or contents pages etc.</p>
<dt>&lt;title&gt;</p>
<dd> Title of the document &#8230; placed in the head of the GSDoc output. If this is omitted the tool will generate a (probably poor) title of its own &#8211; so you should include this markup manually.</p>
<dt>&lt;version&gt;</p>
<dd> Version identifier of the document &#8230; placed in the head of the GSDoc output. If this is omitted the tool will try to construct a value from the RCS Revision tag (if available).</dl>
<p> NB</code> The markup just described may be used within class, category, or protocol documentation &#8230; if so, it is extracted and wrapped round the rest of the documentation for the class as the class&#8217;s chapter. The rest of the class documentation is normally inserted at the end of the chapter, but may instead be substituted in in place of the &lt;unit&gt; pseudo-element within the &lt;chapter&gt; element. </p>
<h2>METHOD MARKUP</h2>
<p> In comments being used to provide text for a method description, the following markup is removed from the text and handled specially &#8211;</p>
<dl>
<dt><code>&lt;init&gt;</p>
<dd> The method is marked as being the designated initialiser for the class.</p>
<dt>&lt;override-subclass&gt;</p>
<dd> The method is marked as being one which subclasses must override (e.g. an abstract method).</p>
<dt>&lt;override-never&gt;</p>
<dd> The method is marked as being one which subclasses should </code><i>NOT</i> override.</p>
<dt><code>&lt;standards&gt;</p>
<dd> The markup is removed from the description and placed </code><i>after</i> it in the GSDoc output &#8211; so that the method is described as conforming (or not conforming) to the specified standards. </p>
</dl>
<h2>AUTOMATED MARKUP</h2>
<p> Generally, the text in comments is reformatted to standardise and indent it nicely &#8230; the reformatting is <i>not</i> performed on any text inside an &lt;example&gt; element. When the text is reformatted, it is broken into whitespace separated &#8220;words&#8221; which are then subjected to some extra processing &#8230;</p>
<dl>
<dt>
<dd> Certain well known constants such as YES, NO, and nil are enclosed in &lt;code&gt; &#8230; &lt;/code&gt; markup.</p>
<dt>
<dd> The names of method arguments within method descriptions are enclosed in &lt;var&gt; &#8230; &lt;/var&gt; markup.</p>
<dt>
<dd> Method names (beginning with a plus or minus) are enclosed in &lt;ref&#8230;&gt; &#8230; &lt;/ref&gt; markup. E.g. &quot;-init&quot; (without the quotes) would be wrapped in a GSDoc reference element to point to the init method of the current class or, if only one known class had an init method, it would refer to the method of that class. Note the fact that the method name must be surrounded by whitespace to be recognized (though a comma, fullstop, or semicolon at the end of the specifier will act like whitespace).</p>
<dt>
<dd> Method specifiers including class names (beginning and ending with square brackets) are enclosed in &lt;ref&#8230;&gt; &#8230; &lt;/ref&gt; markup. e.g. &#8216;[NSObject-init]&#8217;, will create a reference to the init method of NSObject (either the class proper, or any of its categories), while &#8216;[(NSCopying)-copyWithZone:]&#8217;, creates a reference to a method in the NSCopying protocol. Note that no spaces must appear between the square brackets in these specifiers. Protocol names are enclosed in round brackets rather than the customary angle brackets, because GSDoc is an XML language, and XML treats angle brackets specially.</p>
<dt>
<dd> Function names (ending with &#8216;()&#8217;) other than &#8216;main()&#8217; are enclosed in &lt;ref&#8230;&gt; &#8230; &lt;/ref&gt; markup. E.g. &quot;NSLogv()&quot; (without the quotes) would be wrapped in a GSDoc reference element to point to the documentation of the NSLog function. Note the fact that the function name must be surrounded by whitespace (though a comma, fullstop, or semicolon at the end of the specifier will also act as a whitespace terminator). </p>
</dl>
<h2>ARGUMENTS AND DEFAULTS</h2>
<p> The tool accepts certain user defaults (which can of course be supplied as command-line arguments by prepending &#8216;-&#8216; before the default name and giving the value afterwards, as in -Clean YES):</p>
<dl>
<dt><code>Clean</p>
<dd> If this boolean value is set to YES, then rather than generating documentation, the tool removes all GSDoc files generated in the project, and all html files generated from them (as well as any which would be generated from GSDoc files listed explicitly), and finally removes the project index file. The only exception to this is that template GSDoc files (i.e. those specified using &quot;-ConstantsTemplate &#8230;&quot;, &quot;-FunctionsTemplate &#8230;&quot; arguments etc) are not deleted unless the CleanTemplates flag is set.</p>
<dt>CleanTemplates</p>
<dd> This flag specifies whether template GSDoc files are to be removed along with other files when the Clean option is specified. The default is for them not to be removed &#8230; since these templates may have been produced manually and just had data inserted into them.</p>
<dt>ConstantsTemplate</p>
<dd> Specify the name of a template document into which documentation about constants should be inserted from all files in the project. This is useful if constants in the source code are scattered around many files, and you need to group them into one place. You are responsible for ensuring that the basic template document (into which individual constant documentation is inserted) contains all the other information you want, but as a convenience autogsdoc will generate a simple template (which you may then edit) for you if the file does not exist. Insertion takes place immediately before the </code><i>back</i> element (or if that does not exist, immediately before the end of the <i>body</i> element) in the template.</p>
<dt><code>Declared</p>
<dd> Specify where headers are to be documented as being found. The actual name produced in the documentation is formed by appending the last component of the header file name to the value of this default. If this default is not specified, the full name of the header file (as supplied on the command line), with the HeaderDirectory default prepended, is used. A typical usage of this might be &#8216;&quot;-Declared Foundation&quot;&#8217; when generating documentation for the GNUstep base library. This would result in the documentation saying that NSString is declared in &#8216;Foundation/NSString.h&#8217;</p>
<dt>DocumentAllInstanceVariables</p>
<dd> This flag permits you to generate documentation for all instance variables. Normally, only those explicitly declared &#8216;public&#8217; or &#8216;protected&#8217; will be documented.</p>
<dt>DocumentInstanceVariables</p>
<dd> This flag permits you to turn off documentation for instance variables completely. Normally, explicitly declared &#8216;public&#8217; or &#8216;protected&#8217; instance variables will be documented.</p>
<dt>InstanceVariablesAtEnd</p>
<dd> This flag, if set, directs the HTML generator to place instance variable documentation at the end of the class, instead of the beginning. This is useful if you use a lot of protected instance variables which are only going to be of secondary interest to general users of the class.</p>
<dt>DocumentationDirectory</p>
<dd> May be used to specify the directory in which generated documentation is to be placed. If this is not set, output is placed in the current directory. This directory is also used as a last resort to locate source files (not headers), and more importantly, it is used as the </code><i>first and only</i> resort to locate any .gsdoc files that are passed in on the command line. Any path information given for these files is <code>removed</code> and they are searched for in &#8216;DocumentationDirectory&#8217; (even though they may not have been autogenerated).</p>
<dt><code>Files</p>
<dd> Specifies the name of a file containing a list of file names as a property list array </code><i>(name1,name2,&#8230;)</i> format. If this is present, filenames in the program argument list are ignored and the names in this file are used as the list of names to process.</p>
<dt><code>FunctionsTemplate</p>
<dd> Specify the name of a template document into which documentation about functions should be inserted from all files in the project. This is useful if function source code is scattered around many files, and you need to group it into one place. You are responsible for ensuring that the basic template document (into which individual function documentation is inserted) contains all the other information you want, but as a convenience autogsdoc will generate a simple template (which you may then edit) for you if the file does not exist. Insertion takes place immediately before the </code><i>back</i> element (or if that does not exist, immediately before the end of the <i>body</i> element) in the template.</p>
<dt><code>GenerateHtml</p>
<dd> May be used to specify if HTML output is to be generated. Defaults to YES.</p>
<dt>HeaderDirectory</p>
<dd> May be used to specify the directory to be searched for header files. When supplied, this value is prepended to relative header names, otherwise the relative header names are interpreted relative to the current directory. Header files specified as absolute paths are not influenced by this default.</p>
<dt>IgnoreDependencies</p>
<dd> A boolean value which may be used to specify that the program should ignore file modification times and regenerate files anyway. Provided for use in conjunction with the &#8216;make&#8217; system, which is expected to manage dependency checking itsself.</p>
<dt>LocalProjects</p>
<dd> This value is used to control the automatic inclusion of local external projects into the indexing system for generation of cross-references in final document output. If set to &#8216;None&#8217;, then no local project references are done, otherwise, the &#8216;Local&#8217; GNUstep documentation directory is recursively searched for files with a &#8216;.igsdoc&#8217; extension, and the indexing information from those files is used. The value of this string is also used to generate the filenames in the cross reference &#8230; if it is an empty string, the path to use is assumed to be a file in the same directory where the igsdoc file was found, otherwise it is used as a prefix to the name in the index. NB. Local projects with the same name as the project currently being documented will </code><i>not</i> be included by this mechanism. If you wish to include such projects, you must do so explicitly using <i>-Projects &#8230;</i></p>
<dt><code>MacrosTemplate</p>
<dd> Specify the name of a template document into which documentation about macros should be inserted from all files in the project. This is useful if macro code is scattered around many files, and you need to group it into one place. You are responsible for ensuring that the basic template document (into which individual macro documentation is inserted) contains all the other information you want, but as a convenience autogsdoc will generate a simple template (which you may then edit) for you if the file does not exist. Insertion takes place immediately before the </code><i>back</i> element (or if that does not exist, immediately before the end of the <i>body</i><br />
&nbsp;<wbr>element)&nbsp;<wbr>in the template.</p>
<dt><code>MakeDependencies</p>
<dd> A filename to be used to output dependency information for make. This will take the form of listing all header and source files known for the project as dependencies of the project name (see &#8216;Project&#8217;).</p>
<dt>Project</p>
<dd> May be used to specify the name of this project &#8230; determines the name of the index reference file produced as part of the documentation to provide information enabling other projects to cross-reference to items in this project.</p>
<dt>Projects</p>
<dd> This value may be supplied as a dictionary containing the paths to the igsdoc index/reference files used by external projects, along with values to be used to map the filenames found in the indexes. For example, if a project index (igsdoc) file says that the class &#8216;Foo&#8217; is found in the file &#8216;Foo&#8217;, and the path associated with that project index is &#8216;/usr/doc/proj&#8217;, Then generated html output may reference the class as being in &#8216;/usr/doc/prj/Foo.html&#8217; . Note that a dictionary may be given on the command line by using the standard PropertyList format (not the XML format of OS X), using semicolons as line-separators, and enclosing it in single quotes.</p>
<dt>ShowDependencies</p>
<dd> A boolean value which may be used to specify that the program should log which files are being regenerated because of their dependencies on other files.</p>
<dt>Standards</p>
<dd> A boolean value used to specify whether the program should insert information about standards complience into the documentation. This should only be used when documenting the GNUstep libraries and tools themselves as it assumes that the code being documented is part of GNUstep and possibly complies with the OpenStep standard or implements MacOS-X compatible methods.</p>
<dt>SystemProjects</p>
<dd> This value is used to control the automatic inclusion of system external projects into the indexing system for generation of cross-references in final document output. If set to &#8216;None&#8217;, then no system project references are done, otherwise, the &#8216;System&#8217; GNUstep documentation directory is recursively searched for files with a &#8216;.igsdoc&#8217; extension, and the indexing information from those files is used. The value of this string is also used to generate the filenames in the cross reference &#8230; if it is an empty string, the path to use is assumed to be a file in the same directory where the igsdoc file was found, otherwise it is used as a prefix to the name in the index. NB. System projects with the same name as the project currently being documented will </code><i>not</i> be included by this mechanism. If you wish to include such projects, you must do so explicitly using <i>-Projects &#8230;</i></p>
<dt><code>TypedefsTemplate</p>
<dd> Specify the name of a template document into which documentation about typedefs should be inserted from all files in the project. This is useful if typedef source code is scattered around many files, and you need to group it into one place. You are responsible for ensuring that the basic template document (into which individual typedef documentation is inserted) contains all the other information you want, but as a convenience autogsdoc will generate a simple template (which you may then edit) for you if the file does not exist. Insertion takes place immediately before the </code><i>back</i> element (or if that does not exist, immediately before the end of the <i>body</i> element) in the template.</p>
<dt><code>Up</p>
<dd> A string used to supply the name to be used in the &#8216;up&#8217; link from generated GSDoc documents. This should normally be the name of a file which contains an index of the contents of a project. If this is missing or set to an empty string, then no &#8216;up&#8217; link will be provided in the documents.</p>
<dt>VariablesTemplate</p>
<dd> Specify the name of a template document into which documentation about variables should be inserted from all files in the project. This is useful if variable source code is scattered around many files, and you need to group it into one place. You are responsible for ensuring that the basic template document (into which individual variable documentation is inserted) contains all the other information you want, but as a convenience autogsdoc will generate a simple template (which you may then edit) for you if the file does not exist. Insertion takes place immediately before the </code><i>back</i> element (or if that does not exist, immediately before the end of the <i>body</i> element) in the template.</p>
<dt><code>Verbose</p>
<dd> A boolean used to specify whether you want verbose debug/warning output to be produced.</p>
<dt>Warn</p>
<dd> A boolean used to specify whether you want standard warning output (e.g. report of undocumented methods) produced.</p>
<dt>WordMap</p>
<dd> This value is a dictionary used to map identifiers/keywords found in the source files to other words. Generally you will not have to use this, but it is sometimes helpful to avoid the parser being confused by the use of C preprocessor macros. You can effectively redefine the macro to something less confusing. The value you map the identifier to must be one of &#8211; Another identifier, An empty string &#8211; the value is ignored, Two slashes (&#8216;//&#8217;) &#8211; the rest of the line is ignored. Note that a dictionary may be given on the command line by using the standard PropertyList format (not the XML format of OS X), using semicolons as line-separators, and enclosing it in single quotes. </p>
</dl>
<p> </code></p>
<h2>INTER-DOCUMENT LINKAGE</h2>
<p> The &#8216;Up&#8217; default is used to specify the name of a document which should be used as the &#8216;up&#8217; link for any other documents used. This name must not include a path or extension. Generally, the document referred to by this default should be a hand-edited GSDoc document which should have a &lt;em&gt;back&lt;/em&gt; section containing a project index. e.g. </p>
<p> &lt;?xml version=&quot;1.0&quot;?&gt;</p>
<dl>
<dt>
<dd> &lt;!DOCTYPE gsdoc PUBLIC &quot;-//GNUstep//DTD gsdoc 1.0.3//EN&quot;</p>
<dl>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&quot;<a rel="nofollow" href="http://www.gnustep.org/gsdoc-1_0_3.xml">http://www.gnustep.org/gsdoc-1_0_3.xml</a>&quot;&gt;</p>
<dl>
<dt>
<dd> &lt;gsdoc base=&quot;index&quot;&gt;</p>
<dl>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&lt;head&gt;</p>
<dl>
<dt>
<dd>
&nbsp;<wbr>&lt;title&gt;My project reference&lt;/title&gt;</p>
<dl>
<dt>
<dd>
&nbsp;<wbr>&lt;author name=&quot;my name&quot;&gt;&lt;/author&gt;</p>
<dl>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&lt;/head&gt;</p>
<dl>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&lt;body&gt;</p>
<dl>
<dt>
<dd>
&nbsp;<wbr>&lt;chapter&gt;</p>
<dl>
<dt>
<dd>
&lt;heading&gt;My project reference&lt;/heading&gt;</p>
<dl>
<dt>
<dd>
&nbsp;<wbr>&lt;/chapter&gt;</p>
<dl>
<dt>
<dd>
&nbsp;<wbr>&lt;back&gt;</p>
<dl>
<dt>
<dd>
&lt;index scope=&quot;project&quot;&nbsp;<wbr>type=&quot;title&quot;&nbsp;<wbr>/&gt;</p>
<dl>
<dt>
<dd>
&nbsp;<wbr>&lt;/back&gt;</p>
<dl>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&lt;/body&gt;</p>
<dl>
<dt>
<dd> &lt;/gsdoc&gt;</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd></dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
<h2>FILES</h2>
<p> Source: .h, .m, .c</p>
<dl>
<dt>
<dd> GSDoc: .gsdoc</p>
<dl>
<dt>
<dd> Index: .igsdoc</p>
<dl>
<dt>
<dd> HTML: .html </p>
</dl>
</dl>
</dl>
<h2>BUGS</h2>
<p> Several GSDoc elements are not rendered properly into HTML yet. These are: &lt;prjref&gt;, &lt;EOEntity&gt;, &lt;EOModel&gt;. </p>
<h2>DIAGNOSTICS</h2>
<p> Error messages and warnings can come from each of the stages of the pipeline: top-level control, source parsing, GSDoc parsing, and indexing. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-gsdoc/">gsdoc</a>(7), <a href="/docs/linux/man/7-gnustep/">GNUstep</a>(7) </p>
<h2>HISTORY</h2>
<p> Autogsdoc combined the capabilities of two earlier tools, &#8216;autodoc&#8217; and &#8216;gsdoc&#8217;, which performed the source-&gt;GSDoc and GSDoc-&gt;HTML translations respectively. These earlier tools and the GSDoc format were developed for GNUstep based on the earlier GDML SGML language. </p>
<p> This manual page first appeared in gnustep-base 1.9.2 (March 2004). </p>
<h2>AUTHORS</h2>
<p> <code>autogsdoc</code> was written by Richard Frith-Macdonald &lt;rfm [at] gnu.org&gt; </p>
<p> This manual page added by Adrian Robert &lt;arobert [at] cogsci.ucsd.edu&gt;. </p>
<h2>Index</h2>
