---
title: "javadoc-java-1(1)"
name: "javadoc-java-1"
section: "1"
letter: "j"
url: "/docs/linux/man/1-javadoc-java-1/"
description: "javadoc – The Java API Documentation Generator"
---

<h2>Name</h2>
<p> javadoc &#8211; The Java API Documentation Generator </p>
<p> Generates HTML pages of API documentation from Java source files. This document contains Javadoc examples for Solaris.</p>
<h2>SYNOPSIS</h2>
<p> <tt>javadoc</tt><i>&nbsp;<wbr>[&nbsp;<wbr></i><i>options</i><i>&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr>packagenames&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr>sourcefilenames&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr>-subpackages</i>&nbsp;<wbr><i>pkg1:pkg2:&#8230;</i><i>&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr></i><i>@argfiles</i><i>&nbsp;<wbr>]</i> </p>
<p> Arguments can be in any order. See processing of Source Files for details on how the Javadoc tool determines which &quot;<i>.java</i>&quot; files to process.</p>
<dl>
<dt>
<dd>
<dl>
<dt>options</p>
<dd> Command-line options, as specified in this document. To see a typical use of javadoc options, see Real-World Example.</p>
<dt>packagenames</p>
<dd> A series of names of packages, separated by spaces, such as <i>java.lang java.lang.reflect java.awt</i>. You must separately specify each package you want to document. Wildcards are not allowed; use -subpackages for recursion. The Javadoc tool uses <i>-sourcepath</i> to look for these package names. See Example &#8211; Documenting One or More Packages</p>
<dt>sourcefilenames</p>
<dd> A series of source file names, separated by spaces, each of which can begin with a path and contain a wildcard such as asterisk (*). The Javadoc tool will process every file whose name ends with &quot;.java&quot;, and whose name, when stripped of that suffix, is actually a legal class name (see the Java Language Specification). Therefore, you can name files with dashes (such as <i>X-Buffer</i>), or other illegal characters, to prevent them from being documented. This is useful for test files and template files The path that precedes the source file name determines where javadoc will look for the file. (The Javadoc tool does <i>not</i> use <i>-sourcepath</i> to look for these source file names.) Relative paths are relative to the current directory, so passing in <i>Button.java</i> is identical to <i>./Button.java</i>. A source file name with an absolute path and a wildcard, for example, is <i>/home/src/java/awt/Graphics*.java</i>. See Example &#8211; Documenting One or More Classes. You can also mix packagenames and sourcefilenames, as in Example &#8211; Documenting Both Packages and Classes</p>
<dt>-subpackages pkg1:pkg2:&#8230;</p>
<dd> Generates documentation from source files in the specified packages and recursively in their subpackages. An alternative to supplying packagenames or sourcefilenames.</p>
<dt>@argfiles</p>
<dd> One or more files that contain a list of Javadoc options, packagenames and sourcefilenames in any order. Wildcards (*) and <i>-J</i> options are not allowed in these files.</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> The <code>Javadoc</code> tool parses the declarations and documentation comments in a set of Java source files and produces a corresponding set of HTML pages describing (by default) the public and protected classes, nested classes (but not anonymous inner classes), interfaces, constructors, methods, and fields. You can use it to generate the API (Application Programming Interface) documentation or the implementation documentation for a set of source files. </p>
<p> You can run the Javadoc tool on entire packages, individual source files, or both. When documenting entire packages, you can either use <i>-subpackages</i> for traversing recursively down from a top-level directory, or pass in an explicit list of package names. When documenting individual source files, you pass in a list of source (<i>.java</i>) filenames. Examples are given at the end of this document. How Javadoc processes source files is covered next.</p>
<h3>Processing of source files</h3>
<p> The Javadoc tool processes files that end in &quot;<i>.java</i>&quot; plus other files described under Source Files. If you run the Javadoc tool by explicitly passing in individual source filenames, you can determine exactly which &quot;<i>.java</i>&quot; files are processed. However, that is not how most developers want to work, as it is simpler to pass in package names. The Javadoc tool can be run three ways without explicitly specifying the source filenames. You can (1) pass in package names, (2) use <i>-subpackages</i>, and (3) use wildcards with source filenames (<i>*.java</i>). In these cases, the Javadoc tool processes a &quot;<i>.java</i>&quot; file only if it fulfills all of the following requirements:</p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> Its name, after stripping off the &quot;<i>.java</i>&quot; suffix, is actually a legal class name (see the Java Language Specification for legal characters)</p>
<dt>o</p>
<dd> Its directory path relative to the root of the source tree is actually a legal package name (after converting its separators to dots)</p>
<dt>o</p>
<dd> Its package statement contains the legal package name (specified in the previous bullet)</dl>
</dl>
<p> <code>Processing of links</code> &#8211; During a run, the Javadoc tool automatically adds cross-reference links to package, class and member names that are being documented as part of that run. Links appear in several places:</p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> Declarations (return types, argument types, field types)</p>
<dt>o</p>
<dd> &quot;See Also&quot; sections generated from <i>@see</i> tags</p>
<dt>o</p>
<dd> In-line text generated from <i>{@link}</i> tags</p>
<dt>o</p>
<dd> Exception names generated from <i>@throws</i> tags</p>
<dt>o</p>
<dd> &quot;Specified by&quot; links to members in interfaces and &quot;Overrides&quot; links to members in classes</p>
<dt>o</p>
<dd> Summary tables listing packages, classes and members</p>
<dt>o</p>
<dd> Package and class inheritance trees</p>
<dt>o</p>
<dd> The index</dl>
</dl>
<p> You can add hyperlinks to existing text for classes not included on the command line (but generated separately) by way of the <i>-link</i> and <i>-linkoffline</i> options. </p>
<p> <code>Other processing details</code> &#8211; The Javadoc tool produces one complete document each time it is run; it cannot do incremental builds &#8212; that is, it cannot modify or <i>directly</i> incorporate results from previous runs of the Javadoc tool. However, it can link to results from other runs, as just mentioned. </p>
<p> As implemented, the Javadoc tool requires and relies on the java compiler to do its job. The Javadoc tool calls part of <i>javac</i> to compile the declarations, ignoring the member implementation. It builds a rich internal representation of the classes, including the class hierarchy, and &quot;use&quot; relationships, then generates the HTML from that. The Javadoc tool also picks up user-supplied documentation from documentation comments in the source code. </p>
<p> In fact, the Javadoc tool will run on <i>.java</i> source files that are pure stub files with no method bodies. This means you can write documentation comments and run the Javadoc tool in the earliest stages of design while creating the API, before writing the implementation. </p>
<p> Relying on the compiler ensures that the HTML output corresponds exactly with the actual implementation, which may rely on implicit, rather than explicit, source code. For example, the Javadoc tool documents default constructors (see Java Language Specification) that are present in the <i>.class</i> files but not in the source code. </p>
<p> In many cases, the Javadoc tool allows you to generate documentation for source files whose code is incomplete or erroneous. This is a benefit that enables you to generate documentation before all debugging and troubleshooting is done. For example, according to the <i>Java Language Specification</i>, a class that contains an abstract method should itself be declared abstract. The Javadoc tool does not check for this, and would proceed without a warning, whereas the javac compiler stops on this error. The Javadoc tool does do some primitive checking of doc comments. Use the DocCheck doclet to check the doc comments more thoroughly. </p>
<p> When the Javadoc tool builds its internal structure for the documentation, it loads all referenced classes. Because of this, the Javadoc tool must be able to find all referenced classes, whether bootstrap classes, extensions, or user classes. For more about this, see <i>How Classes Are Found</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/technotes/tools/findingclasses.html.">http://docs.oracle.com/javase/7/docs/technotes/tools/findingclasses.html.</a> Generally speaking, classes you create must either be loaded as an extension or in the Javadoc tool&#8217;s class path.</p>
<h3>Javadoc Doclets</h3>
<p> You can customize the content and format of the Javadoc tool&#8217;s output by using doclets. The Javadoc tool has a default &quot;built-in&quot; doclet, called the standard doclet, that generates HTML-formatted API documentation. You can modify or subclass the standard doclet, or write your own doclet to generate HTML, XML, MIF, RTF or whatever output format you&#8217;d like. Information about doclets and their use is at the following locations:</p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> <i>Javadoc Doclets</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/technotes/guides/javadoc/index.html">http://docs.oracle.com/javase/7/docs/technotes/guides/javadoc/index.html</a></p>
<dt>o</p>
<dd> The <i>-doclet</i> command-line option</dl>
</dl>
<p> When a custom doclet is not specified with the <i>-doclet</i> command line option, the Javadoc tool will use the default standard doclet. The javadoc tool has several command line options that are available regardless of which doclet is being used. The standard doclet adds a supplementary set of command line options. Both sets of options are described below in the options section.</p>
<h3>Related Documentation and Doclets</h3>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> <i>Javadoc Enhancements</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/technotes/guides/javadoc/index.html">http://docs.oracle.com/javase/7/docs/technotes/guides/javadoc/index.html</a> for details about improvements added in Javadoc.</p>
<dt>o</p>
<dd> <i>Javadoc FAQ</i> @ <a rel="nofollow" href="http://java.sun.com/j2se/javadoc/faq/index.html">http://java.sun.com/j2se/javadoc/faq/index.html</a> for answers to common questions, information about Javadoc-related tools, and workarounds for bugs.</p>
<dt>o</p>
<dd> <i>How to Write Doc Comments for Javadoc</i> @ <a rel="nofollow" href="http://www.oracle.com/technetwork/java/javase/documentation/index-137868.html">http://www.oracle.com/technetwork/java/javase/documentation/index-137868.html</a> for more information about Sun conventions for writing documentation comments.</p>
<dt>o</p>
<dd> <i>Requirements for Writing API Specifications</i> @ <a rel="nofollow" href="http://java.sun.com/j2se/javadoc/writingapispecs/index.html">http://java.sun.com/j2se/javadoc/writingapispecs/index.html</a> &#8211; Standard requirements used when writing the Java SE Platform Specification. It can be useful whether you are writing API specifications in source file documentation comments or in other formats. It covers requirements for packages, classes, interfaces, fields and methods to satisfy testable assertions.</p>
<dt>o</p>
<dd> <i>Documentation Comment Specification</i> @ <a rel="nofollow" href="http://java.sun.com/docs/books/jls/first_edition/html/18.doc.html">http://java.sun.com/docs/books/jls/first_edition/html/18.doc.html</a> &#8211; The original specification on documentation comments, Chapter 18, Documentation Comments, in the <i>Java Language Specification</i>, First Edition, by James Gosling, Bill Joy, and Guy Steele. (This chapter was removed from the second edition.)</p>
<dt>o</p>
<dd> <i>DocCheck Doclet</i> @ <a rel="nofollow" href="http://www.oracle.com/technetwork/java/javase/documentation/index-141437.html">http://www.oracle.com/technetwork/java/javase/documentation/index-141437.html</a> &#8211; Checks doc comments in source files and generates a report listing the errors and irregularities it finds. It is part of the Doc Check Utilities.</p>
<dt>o</p>
<dd> <i>MIF Doclet</i> @ <a rel="nofollow" href="http://java.sun.com/j2se/javadoc/mifdoclet/">http://java.sun.com/j2se/javadoc/mifdoclet/</a> &#8211; Can automate the generation of API documentation in MIF, FrameMaker and PDF formats. MIF is Adobe FrameMaker&#8217;s interchange format.</dl>
</dl>
<h3>Terminology</h3>
<p> The terms <i>documentation comment</i>, <i>doc comment</i>, <i>main description</i>, <i>tag</i>, <i>block tag</i>, and <i>in-line tag</i> are described at Documentation Comments. These other terms have specific meanings within the context of the Javadoc tool:</p>
<dl>
<dt>
<dd>
<dl>
<dt>generated document</p>
<dd> The document generated by the javadoc tool from the doc comments in Java source code. The default generated document is in HTML and is created by the standard doclet.</dl>
<dl>
<dt>name</p>
<dd> A name of a program element written in the Java Language &#8212; that is, the name of a package, class, interface, field, constructor or method. A name can be fully-qualified, such as <i>java.lang.String.equals(java.lang.Object)</i>, or partially-qualified, such as <i>equals(Object)</i>.</dl>
<dl>
<dt>documented classes</p>
<dd> The classes and interfaces for which detailed documentation is generated during a javadoc run. To be documented, the source files must be available, their source filenames or package names must be passed into the javadoc command, and they must not be filtered out by their access modifier (public, protected, package-private or private). We also refer to these as the classes included in the javadoc output, or the <i>included classes</i>.</dl>
<dl>
<dt>included classes</p>
<dd> Classes and interfaces whose details are documented during a run of the Javadoc tool. Same as <i>documented classes</i>.</dl>
<dl>
<dt>excluded classes</p>
<dd> Classes and interfaces whose details are <i>not</i> documented during a run of the Javadoc tool.</dl>
<dl>
<dt>referenced classes</p>
<dd> The classes and interfaces that are explicitly referred to in the definition (implementation) or doc comments of the documented classes and interfaces. Examples of references include return type, parameter type, cast type, extended class, implemented interface, imported classes, classes used in method bodies, @see, {@link}, {@linkplain}, and {@inheritDoc} tags. (Notice this definition has changed since <i>1.3</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/1.3/docs/tooldocs/solaris/javadoc.html#referencedclasses.)">http://docs.oracle.com/javase/1.3/docs/tooldocs/solaris/javadoc.html#referencedclasses.)</a> When the Javadoc tool is run, it should load into memory all of the referenced classes in javadoc&#8217;s bootclasspath and classpath. (The Javadoc tool prints a &quot;Class not found&quot; warning for referenced classes not found.) The Javadoc tool can derive enough information from the .class files to determine their existence and the fully-qualified names of their members.</dl>
<dl>
<dt>external referenced classes</p>
<dd> The referenced classes whose documentation is not being generated during a javadoc run. In other words, these classes are not passed into the Javadoc tool on the command line. Links in the generated documentation to those classes are said to be <i>external references</i> or <i>external links</i>. For example, if you run the Javadoc tool on only the <i>java.awt</i> package, then any class in <i>java.lang</i>, such as <i>Object</i>, is an external referenced class. External referenced classes can be linked to using the <i>-link</i> and <i>-linkoffline</i> options. An important property of an external referenced class is that its source comments are normally not available to the Javadoc run. In this case, these comments cannot be inherited.</dl>
</dl>
<h2>SOURCE FILES</h2>
<p> The Javadoc tool will generate output originating from four different types of &quot;source&quot; files: Java language source files for classes (<i>.java</i>), package comment files, overview comment files, and miscellaneous unprocessed files. This section also covers test files and template files that can also be in the source tree, but which you want to be sure not to document.</p>
<h3>Class Source Code Files</h3>
<p> Each class or interface and its members can have their own documentation comments, contained in a <i>.java</i> file. For more details about these doc comments, see Documentation Comments.</p>
<h3>Package Comment Files</h3>
<p> Each package can have its own documentation comment, contained in its own &quot;source&quot; file, that the Javadoc tool will merge into the package summary page that it generates. You typically include in this comment any documentation that applies to the entire package. </p>
<p> To create a package comment file, you have a choice of two files to place your comments:</p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> <i>package-info.java</i> &#8211; Can contain a package declaration, package annotations, package comments and Javadoc tags. This file is generally preferred over package.html.</p>
<dt>o</p>
<dd> <i>package.html</i> &#8211; Can contain only package comments and Javadoc tags, no package annotations.</dl>
</dl>
<p> A package may have a single <i>package.html</i> file or a single <i>package-info.java</i> file but not both. Place either file in the package directory in the source tree along with your <i>.java</i> files. </p>
<p> <tt>package-info.java</tt> &#8211; This file can contain a package comment of the following structure &#8212; the comment is placed before the package declaration: </p>
<p> File: <i>java/applet/package-info.java</i> </p>
<pre>
<code>/**
 * Provides the classes necessary to create an  
 * applet and the classes an applet uses 
 * to communicate with its applet context.
 * &lt;p&gt;
 * The applet framework involves two entities:
 * the applet and the applet context.
 * An applet is an embeddable window (see the
 * {@link java.awt.Panel} class) with a few extra
 * methods that the applet context can use to 
 * initialize, start, and stop the applet.
 *
 * @since 1.0
 * @see java.awt
 */
package java.lang.applet;</code>
</pre>
<p> Note that while the comment separators <i>/**</i> and <i>/*</i> must be present, the leading asterisks on the intermediate lines can be omitted. </p>
<p> <tt>package.html</tt> &#8211; This file can contain a package comment of the following structure &#8212; the comment is placed in the <i>&lt;body&gt;</i> element: </p>
<p> File: <i>java/applet/package.html</i> </p>
<pre>
<code>&lt;HTML&gt;
&lt;BODY&gt;
Provides the classes necessary to create an applet and the 
classes an applet uses to communicate with its applet context.
&lt;p&gt;
The applet framework involves two entities: the applet
and the applet context. An applet is an embeddable
window (see the {@link java.awt.Panel} class) with a
few extra methods that the applet context can use to
initialize, start, and stop the applet. 
@since 1.0 
@see java.awt
&lt;/BODY&gt;
&lt;/HTML&gt;</code>
</pre>
<p> Notice this is just a normal HTML file and does not include a package declaration. The content of the package comment file is written in HTML, like all other comments, with one exception: The documentation comment should not include the comment separators <i>/**</i> and <i>*/</i> or leading asterisks. When writing the comment, you should make the first sentence a summary about the package, and not put a title or any other text between <i>&lt;body&gt;</i> and the first sentence. You can include package tags; as with any documentation comment, all block tags must appear after the main description. If you add a <i>@see</i> tag in a package comment file, it must have a fully-qualified name. For more details, see the <i>example of </i><i>package.html</i> @ <a rel="nofollow" href="http://www.oracle.com/technetwork/java/javase/documentation/index-137868.html#packagecomments.">http://www.oracle.com/technetwork/java/javase/documentation/index-137868.html#packagecomments.</a> </p>
<p> <code>Processing of package comment file</code> &#8211; When the Javadoc tool runs, it will automatically look for the package comment file; if found, the Javadoc tool does the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> Copies the comment for processing. (For <i>package.html</i>, copies all content between <i>&lt;body&gt;</i> and <i>&lt;/body&gt;</i> HTML tags. You can include a <i>&lt;head&gt;</i> section to put a <i>&lt;title&gt;</i>, source file copyright statement, or other information, but none of these will appear in the generated documentation.)</p>
<dt>o</p>
<dd> Processes any package tags that are present.</p>
<dt>o</p>
<dd> Inserts the processed text at the bottom of the package summary page it generates, as shown in <i>Package Summary</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/api/java/applet/package-summary.html.">http://docs.oracle.com/javase/7/docs/api/java/applet/package-summary.html.</a></p>
<dt>o</p>
<dd> Copies the first sentence of the package comment to the top of the package summary page. It also adds the package name and this first sentence to the list of packages on the overview page, as shown in <i>Overview Summary</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/api/overview-summary.html.">http://docs.oracle.com/javase/7/docs/api/overview-summary.html.</a> The end-of-sentence is determined by the same rules used for the end of the first sentence of class and member main descriptions.</dl>
</dl>
<h3>Overview Comment File</h3>
<p> Each application or set of packages that you are documenting can have its own overview documentation comment, kept in its own &quot;source&quot; file, that the Javadoc tool will merge into the overview page that it generates. You typically include in this comment any documentation that applies to the entire application or set of packages. </p>
<p> To create an overview comment file, you can name the file anything you want, typically <tt>overview.html</tt> and place it anywhere, typically at the top level of the source tree. For example, if the source files for the <i>java.applet</i> package are contained in <i>/home/user/src/java/applet</i> directory, you could create an overview comment file at <i>/home/user/src/overview.html</i>. </p>
<p> Notice you can have multiple overview comment files for the same set of source files, in case you want to run javadoc multiple times on different sets of packages. For example, you could run javadoc once with -private for internal documentation and again without that option for public documentation. In this case, you could describe the documentation as public or internal in the first sentence of each overview comment file. </p>
<p> The content of the overview comment file is one big documentation comment, written in HTML, like the package comment file described previously. See that description for details. To re-iterate, when writing the comment, you should make the first sentence a summary about the application or set of packages, and not put a title or any other text between <i>&lt;body&gt;</i> and the first sentence. You can include overview tags; as with any documentation comment, all tags except in-line tags, such as <i>{@link}</i>, must appear after the main description. If you add a <i>@see</i> tag, it must have a fully-qualified name. </p>
<p> When you run the Javadoc tool, you specify the overview comment file name with the -overview option. The file is then processed similar to that of a package comment file.</p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> Copies all content between <i>&lt;body&gt;</i> and <i>&lt;/body&gt;</i> tags for processing.</p>
<dt>o</p>
<dd> Processes any overview tags that are present.</p>
<dt>o</p>
<dd> Inserts the processed text at the bottom of the overview page it generates, as shown in <i>Overview Summary</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/api/overview-summary.html.">http://docs.oracle.com/javase/7/docs/api/overview-summary.html.</a></p>
<dt>o</p>
<dd> Copies the first sentence of the overview comment to the top of the overview summary page.</dl>
</dl>
<h3>Miscellaneous Unprocessed Files</h3>
<p> You can also include in your source any miscellaneous files that you want the Javadoc tool to copy to the destination directory. These typically includes graphic files, example Java source (.java) and class (.class) files, and self-standing HTML files whose content would overwhelm the documentation comment of a normal Java source file. </p>
<p> To include unprocessed files, put them in a directory called <tt>doc-files</tt> which can be a subdirectory of any package directory that contains source files. You can have one such subdirectory for each package. You might include images, example code, source files, .class files, applets and HTML files. For example, if you want to include the image of a button <i>button.gif</i> in the <i>java.awt.Button</i> class documentation, you place that file in the <i>/home/user/src/java/awt/doc-files/</i> directory. Notice the <i>doc-files</i> directory should not be located at <i>/home/user/src/java/doc-files</i> because <i>java</i> is not a package &#8212; that is, it does not directly contain any source files. </p>
<p> All links to these unprocessed files must be hard-coded, because the Javadoc tool does not look at the files &#8212; it simply copies the directory and all its contents to the destination. For example, the link in the <i>Button.java</i> doc comment might look like: </p>
<pre>
<code>    /**
     * This button looks like this: 
     * &lt;img src=&quot;doc-files/Button.gif&quot;&gt;
     */</code>
</pre>
<h3>Test Files and Template Files</h3>
<p> Some developers have indicated they want to store test files and templates files in the source tree near their corresponding source files. That is, they would like to put them in the same directory, or a subdirectory, of those source files. </p>
<p> If you run the Javadoc tool by explicitly passing in individual source filenames, you can deliberately omit test and templates files and prevent them from being processed. However, if you are passing in package names or wildcards, you need to follow certain rules to ensure these test files and templates files are not processed. </p>
<p> Test files differ from template files in that the former are legal, compilable source files, while the latter are not, but may end with &quot;.java&quot;. </p>
<p> <code>Test files</code> &#8211; Often developers want to put compilable, runnable test files for a given package in the <i>same</i> directory as the source files for that package. But they want the test files to belong to a package other than the source file package, such as the unnamed package (so the test files have no package statement or a different package statement from the source). In this scenario, when the source is being documented by specifying its package name specified on the command line, the test files will cause warnings or errors. You need to put such test files in a subdirectory. For example, if you want to add test files for source files in <i>com.package1</i>, put them in a subdirectory that would be an invalid package name (because it contains a hyphen): </p>
<pre>
<code>    com/package1/test-files/</code>
</pre>
<p> The test directory will be skipped by the Javadoc tool with no warnings. </p>
<p> If your test files contain doc comments, you can set up a separate run of the Javadoc tool to produce documentation of the test files by passing in their test source filenames with wildcards, such as <i>com/package1/test-files/*.java</i>. </p>
<p> <code>Templates for source files</code> &#8211; Template files have names that often end in &quot;.java&quot; and are not compilable. If you have a template for a source file that you want to keep in the source directory, you can name it with a dash (such as <i>Buffer-Template.java</i>), or any other illegal Java character, to prevent it from being processed. This relies on the fact that the Javadoc tool will only process source files whose name, when stripped of the &quot;.java&quot; suffix, is actually a legal class name (see information about Identifiers in the Java Language Specification).</p>
<h2>GENERATED FILES</h2>
<p> By default, javadoc uses a standard doclet that generates HTML-formatted documentation. This doclet generates the following kinds of files (where each HTML &quot;page&quot; corresponds to a separate file). Note that javadoc generates files with two types of names: those named after classes/interfaces, and those that are not (such as <i>package-summary.html</i>). Files in the latter group contain hyphens to prevent filename conflicts with those in the former group. </p>
<p> <code>Basic Content Pages</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> One <code>class or interface page</code> (<i>classname</i><i>.html</i>) for each class or interface it is documenting.</p>
<dt>o</p>
<dd> One <code>package page</code> (<i>package-summary.html</i>) for each package it is documenting. The Javadoc tool will include any HTML text provided in a file named <i>package.html</i> or <i>package-info.java</i> in the package directory of the source tree.</p>
<dt>o</p>
<dd> One <code>overview page</code> (<i>overview-summary.html</i>) for the entire set of packages. This is the front page of the generated document. The Javadoc tool will include any HTML text provided in a file specified with the <i>-overview</i> option. Note that this file is created only if you pass into javadoc two or more package names. For further explanation, see HTML Frames.)</dl>
</dl>
<p> <code>Cross-Reference Pages</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> One <code>class hierarchy page for the entire set of packages</code> (<i>overview-tree.html</i>). To view this, click on &quot;Overview&quot; in the navigation bar, then click on &quot;Tree&quot;.</p>
<dt>o</p>
<dd> One <code>class hierarchy page for each package</code> (<i>package-tree.html</i>) To view this, go to a particular package, class or interface page; click &quot;Tree&quot; to display the hierarchy for that package.</p>
<dt>o</p>
<dd> One <code>&quot;use&quot; page</code> for each package (<i>package-use.html</i>) and a separate one for each class and interface (<i>class-use/</i><i>classname</i><i>.html</i>). This page describes what packages, classes, methods, constructors and fields use any part of the given class, interface or package. Given a class or interface A, its &quot;use&quot; page includes subclasses of A, fields declared as A, methods that return A, and methods and constructors with parameters of type A. You can access this page by first going to the package, class or interface, then clicking on the &quot;Use&quot; link in the navigation bar.</p>
<dt>o</p>
<dd> A <code>deprecated API page</code> (<i>deprecated-list.html</i>) listing all deprecated names. (A deprecated name is not recommended for use, generally due to improvements, and a replacement name is usually given. Deprecated APIs may be removed in future implementations.)</p>
<dt>o</p>
<dd> A <code>constant field values page</code> (<i>constant-values.html</i>) for the values of static fields.</p>
<dt>o</p>
<dd> A <code>serialized form page</code> (<i>serialized-form.html</i>) for information about serializable and externalizable classes. Each such class has a description of its serialization fields and methods. This information is of interest to re-implementors, not to developers using the API. While there is no link in the navigation bar, you can get to this information by going to any serialized class and clicking &quot;Serialized Form&quot; in the &quot;See also&quot; section of the class comment. The standard doclet automatically generates a serialized form page: any class (public or non-public) that implements Serializable is included, along with <i>readObject</i> and <i>writeObject</i> methods, the fields that are serialized, and the doc comments from the <i>@serial</i>, <i>@serialField</i>, and <i>@serialData</i> tags. Public serializable classes can be excluded by marking them (or their package) with <i>@serial exclude</i>, and package-private serializable classes can be included by marking them (or their package) with <i>@serial include</i>. As of 1.4, you can generate the complete serialized form for public and private classes by running javadoc <i>without</i> specifying the <i>-private</i> option.</p>
<dt>o</p>
<dd> An <code>index</code> (<i>index-*.html</i>) of all class, interface, constructor, field and method names, alphabetically arranged. This is internationalized for Unicode and can be generated as a single file or as a separate file for each starting character (such as A-Z for English).</dl>
</dl>
<p> <code>Support Files</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> A <code>help page</code> (<i>help-doc.html</i>) that describes the navigation bar and the above pages. You can provide your own custom help file to override the default using <i>-helpfile</i>.</p>
<dt>o</p>
<dd> One <code>index.html file</code> which creates the HTML frames for display. This is the file you load to display the front page with frames. This file itself contains no text content.</p>
<dt>o</p>
<dd> Several <code>frame files</code> (<i>*-frame.html</i>) containing lists of packages, classes and interfaces, used when HTML frames are being displayed.</p>
<dt>o</p>
<dd> A <code>package list</code> file (<i>package-list</i>), used by the <i>-link</i> and <i>-linkoffline</i> options. This is a text file, not HTML, and is not reachable through any links.</p>
<dt>o</p>
<dd> A <code>style sheet</code> file (<i>stylesheet.css</i>) that controls a limited amount of color, font family, font size, font style and positioning on the generated pages.</p>
<dt>o</p>
<dd> A <code>doc-files</code> directory that holds any image, example, source code or other files that you want copied to the destination directory. These files are not processed by the Javadoc tool in any manner &#8212; that is, any javadoc tags in them will be ignored. This directory is not generated unless it exists in the source tree.</dl>
</dl>
<p> <code>HTML Frames</code> </p>
<p> The Javadoc tool will generate either two or three HTML frames, as shown in the figure below. It creates the minimum necessary number of frames by omitting the list of packages if there is only one package (or no packages). That is, when you pass a single package name or source files (*.java) belonging to a single package as arguments into the javadoc command, it will create only one frame (C) in the left-hand column &#8212; the list of classes. When you pass into javadoc two or more package names, it creates a third frame (P) listing all packages, as well as an overview page (Detail). This overview page has the filename <i>overview-summary.html</i>. Thus, this file is created only if you pass in two or more package names. You can bypass frames by clicking on the &quot;No Frames&quot; link or entering at overview-summary.html. </p>
<p> If you are unfamiliar with HTML frames, you should be aware that frames can have <i>focus</i> for printing and scrolling. To give a frame focus, click on it. Then on many browsers the arrow keys and page keys will scroll that frame, and the print menu command will print it. </p>
<p> Load one of the following two files as the starting page depending on whether you want HTML frames or not:</p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> <i>index.html</i> (for frames)</p>
<dt>o</p>
<dd> <i>overview-summary.html</i> (for no frames)</dl>
</dl>
<p> <code>Generated File Structure</code> </p>
<p> The generated class and interface files are organized in the same directory hierarchy that Java source files and class files are organized. This structure is one directory per subpackage. </p>
<p> For example, the document generated for the class <i>java.applet.Applet</i> class would be located at <i>java/applet/Applet.html</i>. The file structure for the java.applet package follows, given that the destination directory is named <i>apidocs</i>. All files that contain the word &quot;frame&quot; appear in the upper-left or lower-left frames, as noted. All other HTML files appear in the right-hand frame. </p>
<p> NOTE &#8211; Directories are shown in <code>bold</code>. The asterisks (<i>*</i>) indicate the files and directories that are <i>omitted</i> when the arguments to javadoc are source filenames (*.java) rather than package names. Also when arguments are source filenames, <i>package-list</i> is created but is empty. The doc-files directory will not be created in the destination unless it exists in the source tree. </p>
<pre><code>
apidocs                             Top directory
   index.html                       Initial page that sets up HTML frames
 * overview-summary.html            Lists all packages with first sentence summaries
   overview-tree.html               Lists class hierarchy for all packages
   deprecated-list.html             Lists deprecated API for all packages
   constant-values.html             Lists values of static fields for all packages
   serialized-form.html             Lists serialized form for all packages
 * overview-frame.html              Lists all packages, used in upper-left frame
   allclasses-frame.html            Lists all classes for all packages, used in lower-left frame
   help-doc.html                    Lists user help for how these pages are organized
   index-all.html                   Default index created without -splitindex option
   index-files                      Directory created with -splitindex option
       index-&lt;number&gt;.html          Index files created with -splitindex option
   package-list                     Lists package names, used only for resolving external refs
   stylesheet.css                   HTML style sheet for defining fonts, colors and positions
   java                             Package directory
       applet                       Subpackage directory
            Applet.html             Page for Applet class
            AppletContext.html      Page for AppletContext interface
            AppletStub.html         Page for AppletStub interface
            AudioClip.html          Page for AudioClip interface
          * package-summary.html    Lists classes with first sentence summaries for this package
          * package-frame.html      Lists classes in this package, used in lower left-hand frame
          * package-tree.html       Lists class hierarchy for this package
            package-use             Lists where this package is used
            doc-files               Directory holding image and example files
            class-use               Directory holding pages API is used
                Applet.html         Page for uses of Applet class
                AppletContext.html  Page for uses of AppletContext interface
                AppletStub.html     Page for uses of AppletStub interface
                AudioClip.html      Page for uses of AudioClip interface
   src-html                         Source code directory
       java                         Package directory
           applet                   Subpackage directory
                Applet.html         Page for Applet source code
                AppletContext.html  Page for AppletContext source code
                AppletStub.html     Page for AppletStub source code
                AudioClip.html      Page for AudioClip source code
</code></pre>
<h3>Generated API Declarations</h3>
<p> The Javadoc tool generates a declaration at the start of each class, interface, field, constructor, and method description for that API item. For example, the declaration for the <i>Boolean</i> class is: </p>
<p> <i>public final class Boolean</i><br />
 <i>extends Object</i><br />
 <i>implements Serializable</i> </p>
<p> and the declaration for the <i>Boolean.valueOf</i>method is: </p>
<p> <i>public static Boolean valueOf(String s)</i> </p>
<p> The Javadoc tool can include the modifiers <i>public</i>, <i>protected</i>, <i>private</i>, <i>abstract</i>, <i>final</i>, <i>static</i>, <i>transient</i>, and <i>volatile</i>, but not <i>synchronized</i> or <i>native</i>. These last two modifiers are considered implementation detail and not part of the API specification. </p>
<p> Rather than relying on the keyword <i>synchronized</i>, APIs should document their concurrency semantics in the comment&#8217;s main description, as in &quot;a single <i>Enumeration</i> cannot be used by multiple threads concurrently&quot;. The document should not describe how to achieve these semantics. As another example, while <i>Hashtable</i> should be thread-safe, there&#8217;s no reason to specify that we achieve this by synchronizing all of its exported methods. We should reserve the right to synchronize internally at the bucket level, thus offering higher concurrency.</p>
<h2>DOCUMENTATION COMMENTS</h2>
<p> The original &quot;Documentation Comment Specification&quot; can be found under related documentation.</p>
<h3>Commenting the Source Code</h3>
<p> You can include <i>documentation comments</i> (&quot;doc comments&quot;) in the source code, ahead of declarations for any class, interface, method, constructor, or field. You can also create doc comments for each package and another one for the overview, though their syntax is slightly different. Doc comments are also known informally as &quot;Javadoc comments&quot; (but this term violates its trademark usage). A doc comment consists of the characters between the characters <i>/**</i> that begin the comment and the characters <i>*/</i> that end it. Leading asterisks are allowed on each line and are described further below. The text in a comment can continue onto multiple lines. </p>
<pre>
<code>/**
 * This is the typical format of a simple documentation comment
 * that spans two lines.
 */</code>
</pre>
<p> To save space you can put a comment on one line: </p>
<pre>
<code>/** This comment takes up only one line. */</code>
</pre>
<p> <code>Placement of comments</code> &#8211; Documentation comments are recognized only when placed immediately before class, interface, constructor, method, or field declarations &#8212; see the class example, method example, and field example. Documentation comments placed in the body of a method are ignored. Only one documentation comment per declaration statement is recognized by the Javadoc tool. </p>
<p> A common mistake is to put an <i>import</i> statement between the class comment and the class declaration. Avoid this, as the Javadoc tool will ignore the class comment.<br />
/**<br />
 * This is the class comment for the class Whatever.<br />
 */<br />
import com.sun; // MISTAKE &#8211; Important not to put import statement here<br />
public<br />
class Whatever<br />
{<br />
}</p>
<p> <code>A doc comment is composed of a </code><tt>main description</tt><code> followed by a </code><tt>tag section</tt> &#8211; The <i>main description</i> begins after the starting delimiter <i>/**</i> and continues until the tag section. The <i>tag section</i> starts with the first block tag, which is defined by the first <i>@</i> character that begins a line (ignoring leading asterisks, white space, and leading separator <i>/**</i>). It is possible to have a comment with only a tag section and no main description. The main description cannot continue after the tag section begins. The argument to a tag can span multiple lines. There can be any number of tags &#8212; some types of tags can be repeated while others cannot. For example, this <i>@see</i> starts the tag section: </p>
<pre>
<code>/**
 * This sentence would hold the main description for this doc comment.
 * @see java.lang.Object
 */</code>
</pre>
<p> <code>Block tags and in-line tags</code> &#8211; A <i>tag</i> is a special keyword within a doc comment that the Javadoc tool can process. There are two kinds of tags: block tags, which appear as <i>@tag</i> (also known as &quot;standalone tags&quot;), and in-line tags, which appear within curly braces, as <i>{@tag}</i>. To be interpreted, a block tag must appear at the beginning of a line, ignoring leading asterisks, white space, and separator (<i>/**</i>). This means you can use the <i>@</i> character elsewhere in the text and it will not be interpreted as the start of a tag. If you want to start a line with the <i>@</i> character and not have it be interpreted, use the HTML entity <i>&amp;#064;</i>. Each block tag has associated text, which includes any text following the tag up to, but not including, either the next tag, or the end of the doc comment. This associated text can span multiple lines. An in-line tag is allowed and interpreted anywhere that text is allowed. The following example contains the block tag <i>@deprecated</i> and in-line tag <i>{@link}</i>.<br />
/**<br />
 * @deprecated  As of JDK 1.1, replaced by {@link #setBounds(int,int,int,int)}<br />
 */</p>
<p> <code>Comments are written in HTML</code> &#8211; The text must be written in HTML, in that they should use HTML entities and can use HTML tags. You can use whichever version of HTML your browser supports; we have written the standard doclet to generate HTML 3.2-compliant code elsewhere (outside of the documentation comments) with the inclusion of cascading style sheets and frames. (We preface each generated file with &quot;HTML 4.0&quot; because of the frame sets.) </p>
<p> For example, entities for the less-than (<i>&lt;</i>) and greater-than (<i>&gt;</i>) symbols should be written <i>&lt;</i> and <i>&gt;</i>. Likewise, the ampersand (<i>&amp;</i>) should be written <i>&amp;</i>. The bold HTML tag <i>&lt;b&gt;</i> is shown in the following example. </p>
<p> Here is a doc comment: </p>
<pre>
<code>/**
 * This is a &lt;b&gt;doc&lt;/b&gt; comment.
 * @see java.lang.Object
 */</code>
</pre>
<p> <code>Leading asterisks</code> &#8211; When javadoc parses a doc comment, leading asterisk (<i>*</i>) characters on each line are discarded; blanks and tabs preceding the initial asterisk (<i>*</i>) characters are also discarded. Starting with 1.4, if you omit the leading asterisk on a line, the leading white space is no longer removed. This enables you to paste code examples directly into a doc comment inside a <i>&lt;PRE&gt;</i> tag, and its indentation will be honored. Spaces are generally interpreted by browsers more uniformly than tabs. Indentation is relative to the left margin (rather than the separator <i>/**</i> or <i>&lt;PRE&gt;</i> tag). </p>
<p> <code>First sentence</code> &#8211; The first sentence of each doc comment should be a summary sentence, containing a concise but complete description of the declared entity. This sentence ends at the first period that is followed by a blank, tab, or line terminator, or at the first block tag. The Javadoc tool copies this first sentence to the member summary at the top of the HTML page. </p>
<p> <code>Declaration with multiple fields</code> &#8211; Java allows declaring multiple fields in a single statement, but this statement can have only one documentation comment, which is copied for all fields. Therefore if you want individual documentation comments for each field, you must declare each field in a separate statement. For example, the following documentation comment doesn&#8217;t make sense written as a single declaration and would be better handled as two declarations: </p>
<pre>
<code>/** 
 * The horizontal and vertical distances of point (x,y)
 */
public int x, y;      // Avoid this  </code>
</pre>
<p> The Javadoc tool generates the following documentation from the above code: </p>
<pre>
<code>public int </code><code>x</code>
</pre>
<dl>
<dt>
<dd> The horizontal and vertical distances of point (x,y)</dl>
<pre>
<code>public int </code><code>y</code>
</pre>
<dl>
<dt>
<dd> The horizontal and vertical distances of point (x,y)</dl>
<p> <code>Use header tags carefully</code> &#8211; When writing documentation comments for members, it&#8217;s best not to use HTML heading tags such as &lt;H1&gt; and &lt;H2&gt;, because the Javadoc tool creates an entire structured document and these structural tags might interfere with the formatting of the generated document. However, it is fine to use these headings in class and package comments to provide your own structure.</p>
<h3>Automatic Copying of Method Comments</h3>
<p> The Javadoc tool has the ability to copy or &quot;inherit&quot; method comments in classes and interfaces under the following two circumstances. Constructors, fields and nested classes do not inherit doc comments.</p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> <code>Automatically inherit comment to fill in missing text</code> &#8211; When a main description, or <i>@return</i>, <i>@param</i> or <i>@throws</i> tag is missing from a method comment, the Javadoc tool copies the corresponding main description or tag comment from the method it overrides or implements (if any), according to the algorithm below.</dl>
<p> More specifically, when a <i>@param</i> tag for a particular parameter is missing, then the comment for that parameter is copied from the method further up the inheritance hierarchy. When a <i>@throws</i> tag for a particular exception is missing, the <i>@throws</i> tag is copied <i>only if that exception is declared</i>. </p>
<p> This behavior contrasts with version 1.3 and earlier, where the presence of any main description or tag would prevent all comments from being inherited.</p>
<dl>
<dt>o</p>
<dd> <code>Explicitly inherit comment with {@inheritDoc} tag</code> &#8211; Insert the inline tag <i>{@inheritDoc}</i> in a method main description or <i>@return</i>, <i>@param</i> or <i>@throws</i> tag comment &#8212; the corresponding inherited main description or tag comment is copied into that spot.</dl>
</dl>
<p> The source file for the inherited method need only be on the path specified by -sourcepath for the doc comment to actually be available to copy. Neither the class nor its package needs to be passed in on the command line. This contrasts with 1.3.x and earlier releases, where the class had to be a documented class </p>
<p> <code>Inherit from classes and interfaces</code> &#8211; Inheriting of comments occurs in all three possible cases of inheritance from classes and interfaces:</p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> When a method in a class overrides a method in a superclass</p>
<dt>o</p>
<dd> When a method in an interface overrides a method in a superinterface</p>
<dt>o</p>
<dd> When a method in a class implements a method in an interface</dl>
</dl>
<p> In the first two cases, for method overrides, the Javadoc tool generates a subheading &quot;Overrides&quot; in the documentation for the overriding method, with a link to the method it is overriding, whether or not the comment is inherited. </p>
<p> In the third case, when a method in a given class implements a method in an interface, the Javadoc tool generates a subheading &quot;Specified by&quot; in the documentation for the overriding method, with a link to the method it is implementing. This happens whether or not the comment is inherited. </p>
<p> <code>Algorithm for Inheriting Method Comments</code> &#8211; If a method does not have a doc comment, or has an {@inheritDoc} tag, the Javadoc tool searches for an applicable comment using the following algorithm, which is designed to find the most specific applicable doc comment, giving preference to interfaces over superclasses:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1.</p>
<dd> Look in each directly implemented (or extended) interface in the order they appear following the word implements (or extends) in the method declaration. Use the first doc comment found for this method.</p>
<dt>2.</p>
<dd> If step 1 failed to find a doc comment, recursively apply this entire algorithm to each directly implemented (or extended) interface, in the same order they were examined in step 1.</p>
<dt>3.</p>
<dd> If step 2 failed to find a doc comment and this is a class other than Object (not an interface):</p>
<dl>
<dt>
<dd>
<dl>
<dt>a.</p>
<dd> If the superclass has a doc comment for this method, use it.</p>
<dt>b.</p>
<dd> If step 3a failed to find a doc comment, recursively apply this entire algorithm to the superclass.</dl>
</dl>
</dl>
</dl>
<h2>JAVADOC TAGS</h2>
<p> The Javadoc tool parses special tags when they are embedded within a Java doc comment. These doc tags enable you to autogenerate a complete, well-formatted API from your source code. The tags start with an &quot;at&quot; sign (<i>@</i>) and are case-sensitive &#8212; they must be typed with the uppercase and lowercase letters as shown. A tag must start at the beginning of a line (after any leading spaces and an optional asterisk) or it is treated as normal text. By convention, tags with the same name are grouped together. For example, put all <i>@see</i> tags together. </p>
<p> Tags come in two types:</p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> <code>Block tags</code> &#8211; Can be placed only in the tag section that follows the main description. Block tags are of the form: <i>@tag</i>.</p>
<dt>o</p>
<dd> <code>Inline tags</code> &#8211; Can be placed anywhere in the main description or in the comments for block tags. Inline tags are denoted by curly braces: <i>{@tag}</i>.</dl>
</dl>
<p> For information about tags we might introduce in future releases, see <i>Proposed Tags</i> @ <a rel="nofollow" href="http://java.sun.com/j2se/javadoc/proposed-tags.html.">http://java.sun.com/j2se/javadoc/proposed-tags.html.</a> </p>
<p> The current tags are: </p>
<p>TagIntroduced in JDK / SDK<br />
    @author1 .0<br />
{<br />
    @code<br />
}<br />
1.5<br />
{<br />
    @docRoot<br />
}<br />
1.3<br />
    @deprecated1 .0<br />
    @exception1 .0<br />
{<br />
    @inheritDoc<br />
}<br />
1.4<br />
{<br />
    @link<br />
}<br />
1.2<br />
{<br />
    @linkplain<br />
}<br />
1.4<br />
{<br />
    @literal<br />
}<br />
1.5<br />
    @param1 .0<br />
    @return1 .0<br />
    @see1 .0<br />
    @serial1 .2<br />
    @serialData1 .2<br />
    @serialField1 .2<br />
    @since1 .1<br />
    @throws1 .2<br />
{<br />
    @value<br />
}<br />
1.4<br />
    @version1 .0 For custom tags,<br />
    see the &#8211; tag option.</p>
<p>              @author &amp;nbsp;<br />
name &#8211; text Adds an &#8220;Author&#8221; entry with the specified name &#8211; text to the generated docs when the &#8211; author option is used.A doc comment may contain multiple @author tags.You can specify one name per @author tag or multiple names per tag.In the former case, the Javadoc tool inserts a comma(, ) and space between names.In the latter case, the entire text is simply copied to the generated document without being parsed.Therefore, you can use multiple names per line if you want a localized name separator other than comma.</p>
<p>                                                                                                                                                                                                                                                                                                                                                                                                                                            For more details,<br />
    see Where Tags Can Be Used and writing @author tags @<br />
 <a rel="nofollow" href="http://www.oracle.com/technetwork/java/javase/documentation/index-137868.html#@author.">http://www.oracle.com/technetwork/java/javase/documentation/index-137868.html#@author.</a> </p>
<dl>
<dt>
<dd>
<dl>
<dt>@deprecated&nbsp;<wbr> deprecated-text Note: You can deprecate a program element using the @Deprecated annotation.</p>
<dd></dl>
</dl>
<p> Adds a comment indicating that this API should no longer be used (even though it may continue to work). The Javadoc tool moves the <i>deprecated-text</i> ahead of the main description, placing it in italics and preceding it with a bold warning: &quot;Deprecated&quot;. This tag is valid in all doc comments: overview, package, class, interface, constructor, method and field. </p>
<p> The first sentence of <i>deprecated-text</i> should at least tell the user when the API was deprecated and what to use as a replacement. The Javadoc tool copies just the first sentence to the summary section and index. Subsequent sentences can also explain why it has been deprecated. You should include a <i>{@link}</i> tag (for Javadoc 1.2 or later) that points to the replacement API: </p>
<p> For more details, see <i>writing @deprecated tags</i> @ <a rel="nofollow" href="http://www.oracle.com/technetwork/java/javase/documentation/index-137868.html#@deprecated.">http://www.oracle.com/technetwork/java/javase/documentation/index-137868.html#@deprecated.</a></p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> For Javadoc 1.2 and later, use a <i>{@link}</i> tag. This creates the link in-line, where you want it. For example:<br />
/**<br />
 * @deprecated  As of JDK 1.1, replaced by {@link #setBounds(int,int,int,int)}<br />
 */</p>
<dt>o</p>
<dd> For Javadoc 1.1, the standard format is to create a <i>@see</i> tag (which cannot be in-line) for each <i>@deprecated</i> tag.</dl>
</dl>
<p> For more about deprecation, see <i>The @deprecated tag</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/technotes/guides/javadoc/deprecation/index.html.">http://docs.oracle.com/javase/7/docs/technotes/guides/javadoc/deprecation/index.html.</a> </p>
<dl>
<dt>
<dd>
<dl>
<dt>{@code&nbsp;<wbr> text}</p>
<dd> Equivalent to <i>&lt;code&gt;{@literal}&lt;/code&gt;</i>.</dl>
<p> Displays <i>text</i> in <i>code</i> font without interpreting the text as HTML markup or nested javadoc tags. This enables you to use regular angle brackets (<i>&lt;</i> and <i>&gt;</i>) instead of the HTML entities (<i>&lt;</i> and <i>&gt;</i>) in doc comments, such as in parameter types (<i>&lt;Object&gt;</i>), inequalities (<i>3 &lt; 4</i>), or arrows (<i>&lt;-</i>). For example, the doc comment text: </p>
<pre>
<tt>{@code A&lt;B&gt;C}</tt>
</pre>
<p> displays in the generated HTML page unchanged, as: </p>
<pre>
<tt>A&lt;B&gt;C</tt>
</pre>
<p> The noteworthy point is that the <i>&lt;B&gt;</i> is not interpreted as bold and is in code font. </p>
<p> If you want the same functionality without the code font, use <i>{@literal}</i>. </p>
<dl>
<dt>{@docRoot}</p>
<dd> Represents the relative path to the generated document&#8217;s (destination) root directory from any generated page. It is useful when you want to include a file, such as a copyright page or company logo, that you want to reference from all generated pages. Linking to the copyright page from the bottom of each page is common.</dl>
<p> This <i>{@docRoot}</i> tag can be used both on the command line and in a doc comment: This tag is valid in all doc comments: overview, package, class, interface, constructor, method and field, including the text portion of any tag (such as @return, @param and @deprecated).</p>
<dl>
<dt>
<dd>
<dl>
<dt>1.</p>
<dd> On the command line, where the header/footer/bottom are defined: </p>
<pre>
<code>   javadoc -bottom '&lt;a href=&quot;{@docRoot}/copyright.html&quot;&gt;Copyright&lt;/a&gt;'
            </code>
</pre>
</dl>
<p> NOTE &#8211; When using <i>{@docRoot}</i> this way in a make file, some makefile programs require special escaping for the brace {} characters. For example, the Inprise MAKE version 5.2 running on Windows requires double braces: <i>&#123;&#123;@docRoot}}</i>. It also requires double (rather than single) quotes to enclose arguments to options such as <i>-bottom</i> (with the quotes around the <i>href</i> argument omitted).</p>
<dl>
<dt>2.</p>
<dd> In a doc comment: </p>
<pre>
<code>   /**
    * See the &lt;a href=&quot;{@docRoot}/copyright.html&quot;&gt;Copyright&lt;/a&gt;.
    */
            </code>
</pre>
</dl>
</dl>
<p> The reason this tag is needed is because the generated docs are in hierarchical directories, as deep as the number of subpackages. This expression: </p>
<pre>
<code>  &lt;a href=&quot;{@docRoot}/copyright.html&quot;&gt;
          </code>
</pre>
<p> would resolve to: </p>
<pre>
<code>  &lt;a href=&quot;../../copyright.html&quot;&gt;      for java/lang/Object.java
          </code>
</pre>
<p> and </p>
<pre>
<code>  &lt;a href=&quot;../../../copyright.html&quot;&gt;   for java/lang/ref/Reference.java
          </code>
</pre>
<dl>
<dt>@exception&nbsp;<wbr> class-name&nbsp;<wbr> description</p>
<dd> The <i>@exception</i> tag is a synonym for <i>@throws</i>.</dl>
<dl>
<dt>{@inheritDoc}&nbsp;<wbr></p>
<dd> Inherits (copies) documentation from the &quot;nearest&quot; inheritable class or implementable interface into the current doc comment at this tag&#8217;s location. This allows you to write more general comments higher up the inheritance tree, and to write around the copied text.</dl>
<p> This tag is valid only in these places in a doc comment:</p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> In the main description block of a method. In this case, the main description is copied from a class or interface up the hierarchy.</p>
<dt>o</p>
<dd> In the text arguments of the @return, @param and @throws tags of a method. In this case, the tag text is copied from the corresponding tag up the hierarchy.</dl>
</dl>
<p> See Automatic Copying of Method Comments for a more precise description of how comments are found in the inheritance hierarchy. Note that if this tag is missing, the comment is or is not automatically inherited according to rules described in that section. </p>
<dl>
<dt>{@link&nbsp;<wbr> package.class#member&nbsp;<wbr> label}</p>
<dd> Inserts an in-line link with visible text <i>label</i> that points to the documentation for the specified package, class or member name of a referenced class. This tag is valid in all doc comments: overview, package, class, interface, constructor, method and field, including the text portion of any tag (such as @return, @param and @deprecated).</dl>
<p> This tag is very simliar to <i>@see</i> &#8212; both require the same references and accept exactly the same syntax for <i>package.class</i><i>#</i><i>member</i> and <i>label</i>. The main difference is that <i>{@link}</i> generates an in-line link rather than placing the link in the &quot;See Also&quot; section. Also, the <i>{@link}</i> tag begins and ends with curly braces to separate it from the rest of the in-line text. If you need to use &quot;}&quot; inside the label, use the HTML entity notation &amp;#125; </p>
<p> There is no limit to the number of <i>{@link}</i> tags allowed in a sentence. You can use this tag in the main description part of any documentation comment or in the text portion of any tag (such as @deprecated, @return or @param). </p>
<p> For example, here is a comment that refers to the <i>getComponentAt(int, int)</i> method:<br />
Use the<br />
{<br />
    @link #getComponentAt(int, int) getComponentAt<br />
}<br />
method.</p>
<p> From this, the standard doclet would generate the following HTML (assuming it refers to another class in the same package): </p>
<pre>
<code>Use the &lt;a href=&quot;Component.html#getComponentAt(int, int)&quot;&gt;getComponentAt&lt;/a&gt; method.
        </code>
</pre>
<p> Which appears on the web page as: </p>
<pre>
<code>Use the getComponentAt method.
        </code>
</pre>
<p> You can extend <i>{@link}</i> to link to classes not being documented by using the <i>-link</i> option. </p>
<p> For more details, see <i>writing {@link} tags</i> @ <a rel="nofollow" href="http://www.oracle.com/technetwork/java/javase/documentation/index-137868.html#{@link}.">http://www.oracle.com/technetwork/java/javase/documentation/index-137868.html#{@link}.</a> </p>
<dl>
<dt>{@linkplain&nbsp;<wbr> package.class#member&nbsp;<wbr> label}</p>
<dd> Identical to <i>{@link}</i>, except the link&#8217;s label is displayed in plain text than code font. Useful when the label is plain text. Example: </p>
<pre>
<code>     Refer to {@linkplain add() the overridden method}.
        </code>
</pre>
</dl>
<p> This would display as: </p>
<p> Refer to the overridden method. </p>
<dl>
<dt>{@literal&nbsp;<wbr> text}</p>
<dd> Displays <i>text</i> without interpreting the text as HTML markup or nested javadoc tags. This enables you to use regular angle brackets (<i>&lt;</i> and <i>&gt;</i>) instead of the HTML entities (<i>&lt;</i> and <i>&gt;</i>) in doc comments, such as in parameter types (<i>&lt;Object&gt;</i>), inequalities (<i>3 &lt; 4</i>), or arrows (<i>&lt;-</i>). For example, the doc comment text: </p>
<pre>
<tt>{@literal A&lt;B&gt;C}</tt>
</pre>
</dl>
<p> displays unchanged in the generated HTML page in your browser, as: </p>
<p> <i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></i>A&lt;B&gt;C </p>
<p> The noteworthy point is that the <i>&lt;B&gt;</i> is not interpreted as bold (and it is not in code font). </p>
<p> If you want the same functionality but with the text in code font, use <i>{@code}</i>. </p>
<dl>
<dt>@param&nbsp;<wbr> parameter-name description</p>
<dd> Adds a parameter with the specified <i>parameter-name</i> followed by the specified <i>description</i> to the &quot;Parameters&quot; section. When writing the doc comment, you may continue the <i>description</i> onto multiple lines. This tag is valid only in a doc comment for a method, constructor or class.</dl>
<p> The <i>parameter-name</i> can be the name of a parameter in a method or constructor, or the name of a type parameter of a class, method or constructor. Use angle brackets around this parameter name to specify the use of a type parameter. </p>
<p> Example of a type parameter of a class: </p>
<pre>
<code>     /**
      * @param &lt;E&gt; Type of element stored in a list
      */
     public interface List&lt;E&gt; extends Collection&lt;E&gt; {
     }
        </code>
</pre>
<p> Example of a type parameter of a method: </p>
<pre>
<code>     /**
      * @param string  the string to be converted
      * @param type    the type to convert the string to
      * @param &lt;T&gt;     the type of the element
      * @param &lt;V&gt;     the value of the element
      */
     &lt;T, V extends T&gt; V convert(String string, Class&lt;T&gt; type) {
     }
        </code>
</pre>
<p> For more details, see <i>writing @param tags</i> @ <a rel="nofollow" href="http://www.oracle.com/technetwork/java/javase/documentation/index-137868.html#@param.">http://www.oracle.com/technetwork/java/javase/documentation/index-137868.html#@param.</a> </p>
<dl>
<dt>@return&nbsp;<wbr> description</p>
<dd> Adds a &quot;Returns&quot; section with the <i>description</i> text. This text should describe the return type and permissible range of values. This tag is valid only in a doc comment for a method.</dl>
<p> For more details, see <i>writing @return tags</i> @ <a rel="nofollow" href="http://www.oracle.com/technetwork/java/javase/documentation/index-137868.html#@return.">http://www.oracle.com/technetwork/java/javase/documentation/index-137868.html#@return.</a> </p>
<dl>
<dt>@see&nbsp;<wbr> reference</p>
<dd> Adds a &quot;See Also&quot; heading with a link or text entry that points to <i>reference</i>. A doc comment may contain any number of <i>@see</i> tags, which are all grouped under the same heading. The <i>@see</i> tag has three variations; the third form below is the most common. This tag is valid in any doc comment: overview, package, class, interface, constructor, method or field. For inserting an in-line link within a sentence to a package, class or member, see <i>{@link}</i>.</p>
<dl>
<dt>
<dd>
<dl>
<dt>@see &quot;string&quot;</p>
<dd> Adds a text entry for <i>string</i>. No link is generated. The <i>string</i> is a book or other reference to information not available by URL. The Javadoc tool distinguishes this from the previous cases by looking for a double-quote (<i>&quot;</i>) as the first character. For example: </p>
<pre>
<code>     @see &quot;The Java Programming Language&quot;
            </code>
</pre>
</dl>
<p> This generates text such as:</dl>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>See Also:</p>
<dd> &quot;The Java Programming Language&quot;</dl>
</dl>
</dl>
<dl>
<dt>@see &lt;a href=&quot;URL#value&quot;&gt;label&lt;/a&gt;</p>
<dd> Adds a link as defined by <i>URL</i>#<i>value</i>. The <i>URL</i>#<i>value</i> is a relative or absolute URL. The Javadoc tool distinguishes this from other cases by looking for a less-than symbol (<i>&lt;</i>) as the first character. For example: </p>
<pre>
<code>     @see &lt;a href=&quot;spec.html#section&quot;&gt;Java Spec&lt;/a&gt;</code>
</pre>
<p> This generates a link such as:</p>
<dl>
<dt>
<dd>
<dl>
<dt>See Also:</p>
<dd> Java Spec</dl>
</dl>
<dt>@see&nbsp;<wbr> package.class#member&nbsp;<wbr> label</p>
<dd> Adds a link, with visible text <i>label</i>, that points to the documentation for the specified name in the Java Language that is referenced. The <i>label</i> is optional; if omitted, the name appears instead as the visible text, suitably shortened &#8212; see How a name is displayed. Use -noqualifier to globally remove the package name from this visible text. Use the label when you want the visible text to be different from the auto-generated visible text.</dl>
<p> Only in version 1.2, just the name but not the label would automatically appear in &lt;code&gt; HTML tags, Starting with 1.2.2, the &lt;code&gt; is always included around the visible text, whether or not a label is used. </p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> <tt>package.class</tt><tt>#</tt><tt>member</tt> is any valid program element name that is referenced &#8212; a package, class, interface, constructor, method or field name &#8212; except that the character ahead of the member name should be a hash character (<i>#</i>). The <i>class</i> represents any top-level or nested class or interface. The <i>member</i> represents any constructor, method or field (not a nested class or interface). If this name is in the documented classes, the Javadoc tool will automatically create a link to it. To create links to external referenced classes, use the <i>-link</i> option. Use either of the other two <i>@see</i> forms for referring to documentation of a name that does not belong to a referenced class. This argument is described at greater length below under Specifying a Name.</p>
<dt>o</p>
<dd> <tt>label</tt> is optional text that is visible as the link&#8217;s label. The <i>label</i> can contain whitespace. If <i>label</i> is omitted, then <i>package.class.member</i> will appear, suitably shortened relative to the current class and package &#8212; see How a name is displayed.</p>
<dt>o</p>
<dd> A space is the delimiter between <i>package.class</i><i>#</i><i>member</i> and <i>label</i>. A space inside parentheses does not indicate the start of a label, so spaces may be used between parameters in a method.</dl>
</dl>
<p> <code>Example</code> &#8211; In this example, an <i>@see</i> tag (in the <i>Character</i> class) refers to the <i>equals</i> method in the <i>String</i> class. The tag includes both arguments: the name &quot;<i>String#equals(Object)</i>&quot; and the label &quot;<i>equals</i>&quot;. </p>
<pre>
<code> /**
  * @see String#equals(Object) equals
  */</code>
</pre>
<p> The standard doclet produces HTML something like this: </p>
<pre>
<code>&lt;dl&gt;
&lt;dt&gt;&lt;b&gt;See Also:&lt;/b&gt;
&lt;dd&gt;&lt;a href=&quot;../../java/lang/String#equals(java.lang.Object)&quot;&gt;&lt;code&gt;equals&lt;code&gt;&lt;/a&gt;
&lt;/dl&gt;</code>
</pre>
<p> Which looks something like this in a browser, where the label is the visible link text:</p>
<dl>
<dt>
<dd>
<dl>
<dt>See Also:</p>
<dd> equals</dl>
</dl>
<p> <code>Specifying a name</code> &#8211; This <i>package.class</i><i>#</i><i>member</i> name can be either fully-qualified, such as <i>java.lang.String#toUpperCase()</i> or not, such as <i>String#toUpperCase()</i> or <i>#toUpperCase()</i>. If less than fully-qualified, the Javadoc tool uses the normal Java compiler search order to find it, further described below in Search order for @see. The name can contain whitespace within parentheses, such as between method arguments. </p>
<p> Of course the advantage of providing shorter, &quot;partially-qualified&quot; names is that they are shorter to type and there is less clutter in the source code. The following table shows the different forms of the name, where <i>Class</i> can be a class or interface, <i>Type</i> can be a class, interface, array, or primitive, and <i>method</i> can be a method or constructor. </p>
<p>The following notes apply to the above table: </p>
<p>oThe first set of forms (with no class or package) will cause the Javadoc tool to search only through the current class&#8217;s hierarchy. It will find a member of the current class or interface, one of its superclasses or superinterfaces, or one of its enclosing classes or interfaces (search steps 1-3). It will not search the rest of the current package or other packages (search steps 4-5).<br />
oIf any method or constructor is entered as a name with no parentheses, such as getValue, and if there is no field with the same name, the Javadoc tool will correctly create a link to it, but will print a warning message reminding you to add the parentheses and arguments. If this method is overloaded, the Javadoc tool will link to the first method its search encounters, which is unspecified.<br />
oNested classes must be specified as outer.inner, not simply inner, for all forms.<br />
oAs stated, the hash character (#), rather than a dot (.) separates a member from its class. This enables the Javadoc tool to resolve ambiguities, since the dot also separates classes, nested classes, packages, and subpackages. However, the Javadoc tool is generally lenient and will properly parse a dot if you know there is no ambiguity, though it will print a warning. </p>
<p>Search order for @see &#8211; the Javadoc tool will process a @see tag that appears in a source file (.java), package file (package.html or package-info.java) or overview file (overview.html). In the latter two files, you must fully-qualify the name you supply with @see. In a source file, you can specify a name that is fully-qualified or partially-qualified.<br />
When the Javadoc tool encounters a @see tag in a .java file that is not fully qualified, it searches for the specified name in the same order as the Java compiler would (except the Javadoc tool will not detect certain namespace ambiguities, since it assumes the source code is free of these errors). This search order is formally defined in the Java Language Specification. The Javadoc tool searches for that name through all related and imported classes and packages. In particular, it searches in this order: </p>
<p>1.the current class or interface<br />
2.any enclosing classes and interfaces, searching closest first<br />
3.any superclasses and superinterfaces, searching closest first<br />
4.the current package<br />
5.any imported packages, classes and interfaces, searching in the order of the import statement </p>
<p>The Javadoc tool continues to search recursively through steps 1-3 for each class it encounters until it finds a match. That is, after it searches through the current class and its enclosing class E, it will search through E&#8217;s superclasses before E&#8217;s enclosing classes.  In steps 4 and 5, the Javadoc tool does not search classes or interfaces within a package in any specified order (that order depends on the particular compiler). In step 5, the Javadoc tool looks in java.lang, since that is automatically imported by all programs.<br />
The Javadoc tool does not necessarily look in subclasses, nor will it look in other packages even if their documentation is being generated in the same run. For example, if the @see tag is in the java.awt.event.KeyEvent class and refers to a name in the java.awt package, javadoc does not look in that package unless that class imports it.<br />
How a name is displayed &#8211; If label is omitted, then package.class.member appears. In general, it is suitably shortened relative to the current class and package. By &#8220;shortened&#8221;, we mean the Javadoc tool displays only the minimum name necessary. For example, if the String.toUpperCase() method contains references to a member of the same class and to a member of a different class, the class name is displayed only in the latter case, as shown in the following table.<br />
Use -noqualifier to globally remove the package names.</p>
<p>Type of ReferenceDisplays As<br />
@see String#toLowerCase()<br />
Examples of @see</p>
<p>The comment to the right shows how the name would be displayed if the @see tag is in a class in another package, such as java.applet.Applet. </p>
<p>                                           See also:<br />
@see java.lang.String                   //  String<br />
@see java.lang.String The String class  //  The String class<br />
@see String                             //  String<br />
@see String#equals(Object)              //  String.equals(Object)<br />
@see String#equals                      //  String.equals(java.lang.Object)<br />
@see java.lang.Object#wait(long)        //  java.lang.Object.wait(long)<br />
@see Character#MAX_RADIX                //  Character.MAX_RADIX<br />
@see &lt;a href=&#8221;spec.html&#8221;&gt;Java Spec&lt;/a&gt;  //  Java Spec<br />
@see &#8220;The Java Programming Language&#8221;    //  &#8220;The Java Programming Language&#8221;<br />
 You can extend <i>@see</i> to link to classes not being documented by using the <i>-link</i> option. </p>
<p> For more details, see <i>writing @see tags</i> @ <a rel="nofollow" href="http://www.oracle.com/technetwork/java/javase/documentation/index-137868.html#@see.">http://www.oracle.com/technetwork/java/javase/documentation/index-137868.html#@see.</a></dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>@serial&nbsp;<wbr> field-description | include | exclude</p>
<dd> Used in the doc comment for a default serializable field.</dl>
<p> An optional <i>field-description</i> should explain the meaning of the field and list the acceptable values. If needed, the description can span multiple lines. The standard doclet adds this information to the serialized form page. </p>
<p> If a serializable field was added to a class some time after the class was made serializable, a statement should be added to its main description to identify at which version it was added. </p>
<p> The <i>include</i> and <i>exclude</i> arguments identify whether a class or package should be included or excluded from the serialized form page. They work as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> A public or protected class that implements <i>Serializable</i> is <i>included</i> unless that class (or its package) is marked <i>@serial exclude</i>.</p>
<dt>o</p>
<dd> A private or package-private class that implements <i>Serializable</i> is <i>excluded</i> unless that class (or its package) is marked <i>@serial include</i>.</dl>
</dl>
<p> Examples: The <i>javax.swing</i> package is marked <i>@serial exclude</i> (in <i>package.html</i> or <i>package-info.java</i>). The public class <i>java.security.BasicPermission</i> is marked <i>@serial exclude</i>. The package-private class <i>java.util.PropertyPermissionCollection</i> is marked <i>@serial include</i>. </p>
<p> The tag @serial at a class level overrides @serial at a package level. </p>
<p> For more information about how to use these tags, along with an example, see &quot; <i>Documenting Serializable Fields and Data for a Class</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/platform/serialization/spec/serial-arch.html,">http://docs.oracle.com/javase/7/docs/platform/serialization/spec/serial-arch.html,</a>&quot; Section 1.6 of the <i>Java Object Serialization Specification</i>. Also see the <i>Serialization FAQ</i> @ <a rel="nofollow" href="http://java.sun.com/javase/technologies/core/basic/serializationFAQ.jsp#javadoc_warn_missing,">http://java.sun.com/javase/technologies/core/basic/serializationFAQ.jsp#javadoc_warn_missing,</a> which covers common questions, such as &quot;Why do I see javadoc warnings stating that I am missing @serial tags for private fields if I am not running javadoc with the -private switch?&quot;. Also see <i>Sun&#8217;s criteria</i> @ <a rel="nofollow" href="http://java.sun.com/j2se/javadoc/writingapispecs/serialized-criteria.html">http://java.sun.com/j2se/javadoc/writingapispecs/serialized-criteria.html</a> for including classes in the serialized form specification. </p>
<dl>
<dt>@serialField&nbsp;<wbr> field-name&nbsp;<wbr> field-type&nbsp;<wbr> field-description</p>
<dd> Documents an <i>ObjectStreamField</i> component of a <i>Serializable</i> class&#8217;s <i>serialPersistentFields</i> member. One <i>@serialField</i> tag should be used for each <i>ObjectStreamField</i> component.</dl>
<dl>
<dt>@serialData&nbsp;<wbr> data-description</p>
<dd> The <i>data-description</i> documents the types and order of data in the serialized form. Specifically, this data includes the optional data written by the <i>writeObject</i> method and all data (including base classes) written by the <i>Externalizable.writeExternal</i> method.</dl>
<p> The <i>@serialData</i> tag can be used in the doc comment for the <i>writeObject</i>, <i>readObject</i>, <i>writeExternal</i>, <i>readExternal</i>, <i>writeReplace</i>, and <i>readResolve</i> methods. </p>
<dl>
<dt>@since&nbsp;<wbr> since-text</p>
<dd> Adds a &quot;Since&quot; heading with the specified <i>since-text</i> to the generated documentation. The text has no special internal structure. This tag is valid in any doc comment: overview, package, class, interface, constructor, method or field. This tag means that this change or feature has existed since the software release specified by the <i>since-text</i>. For example: </p>
<pre>
<code>    @since 1.5
        </code>
</pre>
</dl>
<p> For source code in the Java platform, this tag indicates the version of the Java platform API specification (not necessarily when it was added to the reference implementation). Multiple @since tags are allowed and are treated like multiple @author tags. You could use multiple tags if the prgram element is used by more than one API. </p>
<dl>
<dt>@throws&nbsp;<wbr> class-name&nbsp;<wbr> description</p>
<dd> The <i>@throws</i> and <i>@exception</i> tags are synonyms. Adds a &quot;Throws&quot; subheading to the generated documentation, with the <i>class-name</i> and <i>description</i> text. The <i>class-name</i> is the name of the exception that may be thrown by the method. This tag is valid only in the doc comment for a method or constructor. If this class is not fully-specified, the Javadoc tool uses the search order to look up this class. Multiple <i>@throws</i> tags can be used in a given doc comment for the same or different exceptions.</dl>
<p> To ensure that all checked exceptions are documented, if a <i>@throws</i> tag does not exist for an exception in the throws clause, the Javadoc tool automatically adds that exception to the HTML output (with no description) as if it were documented with @throws tag. </p>
<p> The <i>@throws</i> documentation is copied from an overridden method to a subclass only when the exception is explicitly declared in the overridden method. The same is true for copying from an interface method to an implementing method. You can use {@inheritDoc} to force @throws to inherit documentation. </p>
<p> For more details, see <i>writing @throws tags</i> @ <a rel="nofollow" href="http://www.oracle.com/technetwork/java/javase/documentation/index-137868.html#@exception.">http://www.oracle.com/technetwork/java/javase/documentation/index-137868.html#@exception.</a> </p>
<dl>
<dt>{@value&nbsp;<wbr> package.class#field}</p>
<dd> When <i>{@value}</i> is used (without any argument) in the doc comment of a static field, it displays the value of that constant: </p>
<pre>
<code>    /**
     * The value of this constant is {@value}.
     */
    public static final String SCRIPT_START = &quot;&lt;script&gt;&quot;
        </code>
</pre>
</dl>
<p> When used with argument <i>package.class#field</i> in any doc comment, it displays the value of the specified constant:<br />
/**<br />
 * Evaluates the script starting with {@value #SCRIPT_START}.<br />
 */<br />
public<br />
String evalScript(String script)<br />
{<br />
}</p>
<p> The argument <i>package.class#field</i> takes a form identical to that of the @see argument, except that the member must be a static field. </p>
<p> These values of these constants are also displayed on the <i>Constant Field Values</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/api/constant-values.html">http://docs.oracle.com/javase/7/docs/api/constant-values.html</a> page. </p>
<dl>
<dt>@version&nbsp;<wbr> version-text</p>
<dd> Adds a &quot;Version&quot; subheading with the specified <i>version-text</i> to the generated docs when the -version option is used. This tag is intended to hold the current version number of the software that this code is part of (as opposed to @since, which holds the version number where this code was introduced). The <i>version-text</i> has no special internal structure. To see where the version tag can be used, see Where Tags Can Be Used.</dl>
<p> A doc comment may contain multiple <i>@version</i> tags. If it makes sense, you can specify one version number per <i>@version</i> tag or multiple version numbers per tag. In the former case, the Javadoc tool inserts a comma (<i>,</i>) and space between names. In the latter case, the entire text is simply copied to the generated document without being parsed. Therefore, you can use multiple names per line if you want a localized name separator other than comma. </p>
<p> For more details, see <i>writing @version tags</i> @ <a rel="nofollow" href="http://www.oracle.com/technetwork/java/javase/documentation/index-137868.html#@version.">http://www.oracle.com/technetwork/java/javase/documentation/index-137868.html#@version.</a></dl>
<h3>Where Tags Can Be Used</h3>
<p> The following sections describe where the tags can be used. Note that these tags can be used in all doc comments: <i>@see</i>, <i>@since</i>, <i>@deprecated</i>, <i>{@link}</i>, <i>{@linkplain}</i>, and <i>{@docroot}</i>.</p>
<h3>Overview Documentation Tags</h3>
<p> Overview tags are tags that can appear in the documentation comment for the overview page (which resides in the source file typically named <i>overview.html</i>). Like in any other documentation comments, these tags must appear after the main description. </p>
<p> <code>NOTE</code> &#8211; The <i>{@link}</i> tag has a bug in overview documents in version 1.2 &#8212; the text appears properly but has no link. The <i>{@docRoot}</i> tag does not currently work in overview documents. </p>
<p> <code>Overview Tags</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> <i>@see</i></p>
<dt>o</p>
<dd> <i>@since</i></p>
<dt>o</p>
<dd> <i>@author</i></p>
<dt>o</p>
<dd> <i>@version</i></p>
<dt>o</p>
<dd> <i>{@link}</i></p>
<dt>o</p>
<dd> <i>{@linkplain}</i></p>
<dt>o</p>
<dd> <i>{@docRoot}</i></dl>
</dl>
<h3>Package Documentation Tags</h3>
<p> Package tags are tags that can appear in the documentation comment for a package (which resides in the source file named <i>package.html</i> or <i>package-info.java</i>). The <i>@serial</i> tag can only be used here with the <i>include</i> or <i>exclude</i> argument. </p>
<p> <code>Package Tags</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> <i>@see</i></p>
<dt>o</p>
<dd> <i>@since</i></p>
<dt>o</p>
<dd> <i>@serial</i></p>
<dt>o</p>
<dd> <i>@author</i></p>
<dt>o</p>
<dd> <i>@version</i></p>
<dt>o</p>
<dd> <i>{@link}</i></p>
<dt>o</p>
<dd> <i>{@linkplain}</i></p>
<dt>o</p>
<dd> <i>{@docRoot}</i></dl>
</dl>
<h3>Class and Interface Documentation Tags</h3>
<p> The following are tags that can appear in the documentation comment for a class or interface. The <i>@serial</i> tag can only be used here with the <i>include</i> or <i>exclude</i> argument. </p>
<p> <code>Class/Interface Tags</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> <i>@see</i></p>
<dt>o</p>
<dd> <i>@since</i></p>
<dt>o</p>
<dd> <i>@deprecated</i></p>
<dt>o</p>
<dd> <i>@serial</i></p>
<dt>o</p>
<dd> <i>@author</i></p>
<dt>o</p>
<dd> <i>@version</i></p>
<dt>o</p>
<dd> <i>{@link}</i></p>
<dt>o</p>
<dd> <i>{@linkplain}</i></p>
<dt>o</p>
<dd> <i>{@docRoot}</i></dl>
</dl>
<p> <code>An example of a class comment:</code><br />
/**<br />
 * A class representing a window on the screen.<br />
 * For example:<br />
 * &lt;pre&gt;<br />
 *    Window win = new Window(parent);<br />
 *    win.show();<br />
 * &lt;/pre&gt;<br />
 *<br />
 * @author  Sami Shaio<br />
 * @version 1.13, 06/08/06<br />
 * @see     java.awt.BaseWindow<br />
 * @see     java.awt.Button<br />
 */<br />
class Window extends BaseWindow<br />
{<br />
    &#8230;<br />
}</p>
<h3>Field Documentation Tags</h3>
<p> The following are the tags that can appear in </p>
<p> <code>Field Tags</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> <i>@see</i></p>
<dt>o</p>
<dd> <i>@since</i></p>
<dt>o</p>
<dd> <i>@deprecated</i></p>
<dt>o</p>
<dd> <i>@serial</i></p>
<dt>o</p>
<dd> <i>@serialField</i></p>
<dt>o</p>
<dd> <i>{@link}</i></p>
<dt>o</p>
<dd> <i>{@linkplain}</i></p>
<dt>o</p>
<dd> <i>{@docRoot}</i></p>
<dt>o</p>
<dd> <i>{@value}</i></dl>
</dl>
<p> <code>An example of a field comment:</code> </p>
<pre>
<code>    /**
     * The X-coordinate of the component.
     *
     * @see #getLocation()
     */
    int x = 1263732;</code>
</pre>
<h3>Constructor and Method Documentation Tags</h3>
<p> The following are the tags that can appear in the documentation comment for a constructor or method, except for <i>@return</i>, which cannot appear in a constructor, and <i>{@inheritDoc}</i>, which has certain restrictions. The <i>@serialData</i> tag can only be used in the doc comment for certain serialization methods. </p>
<p> <code>Method/Constructor Tags</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> <i>@see</i></p>
<dt>o</p>
<dd> <i>@since</i></p>
<dt>o</p>
<dd> <i>@deprecated</i></p>
<dt>o</p>
<dd> <i>@param</i></p>
<dt>o</p>
<dd> <i>@return</i></p>
<dt>o</p>
<dd> <i>@throws</i> and <i>@exception</i></p>
<dt>o</p>
<dd> <i>@serialData</i></p>
<dt>o</p>
<dd> <i>{@link}</i></p>
<dt>o</p>
<dd> <i>{@linkplain}</i></p>
<dt>o</p>
<dd> <i>{@inheritDoc}</i></p>
<dt>o</p>
<dd> <i>{@docRoot}</i></dl>
</dl>
<p> <code>An example of a method doc comment:</code> </p>
<pre><code>
/**
 * Returns the character at the specified index. An index
 * ranges from &lt;code&gt;0&lt;/code&gt; to &lt;code&gt;length() - 1&lt;/code&gt;.
 *
 * @param     index  the index of the desired character.
 * @return    the desired character.
 * @exception StringIndexOutOfRangeException
 *              if the index is not in the range &lt;code&gt;0&lt;/code&gt;
 *              to &lt;code&gt;length()-1&lt;/code&gt;.
 * @see       java.lang.Character#charValue()
 */
public
char charAt(int index)
{
    ...
}
</code></pre>
<h2>OPTIONS</h2>
<p> The javadoc tool uses doclets to determine its output. The Javadoc tool uses the default standard doclet unless a custom doclet is specified with the -doclet option. The Javadoc tool provides a set of command-line options that can be used with any doclet &#8212; these options are described below under the sub-heading Javadoc Options. The standard doclet provides an additional set of command-line options that are described below under the sub-heading Options Provided by the Standard Doclet. All option names are case-insensitive, though their arguments can be case-sensitive. </p>
<p> The options are: </p>
<pre>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
Options shown in <i>italic</i> are the Javadoc core options, which are provided by the front end of the Javadoc tool and are available to all doclets. The standard doclet itself provides the non-italic options.
</pre>
<h3>Javadoc Options</h3>
<dl>
<dt>
<dd>
<dl>
<dt>-overview &nbsp;<wbr>path/filename</p>
<dd> Specifies that javadoc should retrieve the text for the overview documentation from the &quot;source&quot; file specified by <i>path/filename</i> and place it on the Overview page (<i>overview-summary.html</i>). The <i>path/filename</i> is relative to the current directory. </p>
<p> While you can use any name you want for <i>filename</i> and place it anywhere you want for <i>path</i>, a typical thing to do is to name it <i>overview.html</i> and place it in the source tree at the directory that contains the topmost package directories. In this location, no <i>path</i> is needed when documenting packages, since <i>-sourcepath</i> will point to this file. For example, if the source tree for the <i>java.lang</i> package is <i>/src/classes/java/lang/</i>, then you could place the overview file at <i>/src/classes/overview.html</i>. See Real World Example. </p>
<p> For information about the file specified by <i>path/filename</i>, see overview comment file. </p>
<p> Note that the overview page is created only if you pass into javadoc two or more package names. For further explanation, see HTML Frames.) </p>
<p> The title on the overview page is set by <i>-doctitle</i>.</p>
<dt>-public</p>
<dd> Shows only public classes and members.</p>
<dt>-protected</p>
<dd> Shows only protected and public classes and members. This is the default.</p>
<dt>-package</p>
<dd> Shows only package, protected, and public classes and members.</p>
<dt>-private</p>
<dd> Shows all classes and members.</p>
<dt>-help</p>
<dd> Displays the online help, which lists these javadoc and doclet command line options.</p>
<dt>-doclet&nbsp;<wbr> class</p>
<dd> Specifies the class file that starts the doclet used in generating the documentation. Use the fully-qualified name. This doclet defines the content and formats the output. If the <tt>-doclet</tt> option is not used, javadoc uses the standard doclet for generating the default HTML format. This class must contain the <i>start(Root)</i> method. The path to this starting class is defined by the <i>-docletpath</i> option. </p>
<p> For example, to call the MIF doclet, use: </p>
<pre>
<code>    -doclet com.sun.tools.doclets.mif.MIFDoclet</code>
</pre>
<p> For full, working examples of running a particular doclet, see the <i>MIF Doclet documentation</i> @ <a rel="nofollow" href="http://java.sun.com/j2se/javadoc/mifdoclet/docs/mifdoclet.html.">http://java.sun.com/j2se/javadoc/mifdoclet/docs/mifdoclet.html.</a></p>
<dt>-docletpath&nbsp;<wbr> classpathlist</p>
<dd> Specifies the path to the doclet starting class file (specified with the <i>-doclet</i> option) and any jar files it depends on. If the starting class file is in a jar file, then this specifies the path to that jar file, as shown in the example below. You can specify an absolute path or a path relative to the current directory. If <i>classpathlist</i> contains multiple paths or jar files, they should be separated with a colon (:) on Solaris and a semi-colon (;) on Windows. This option is not necessary if the doclet starting class is already in the search path. </p>
<p> Example of path to jar file that contains the starting doclet class file. Notice the jar filename is included. </p>
<pre>
<code>   -docletpath /home/user/mifdoclet/lib/mifdoclet.jar</code>
</pre>
<p> Example of path to starting doclet class file. Notice the class filename is omitted. </p>
<pre>
<code>   -docletpath /home/user/mifdoclet/classes/com/sun/tools/doclets/mif/</code>
</pre>
<p> For full, working examples of running a particular doclet, see the <i>MIF Doclet documentation</i> @ <a rel="nofollow" href="http://java.sun.com/j2se/javadoc/mifdoclet/docs/mifdoclet.html.">http://java.sun.com/j2se/javadoc/mifdoclet/docs/mifdoclet.html.</a></p>
<dt>-1.1</p>
<dd> <i>This feature has been removed from Javadoc 1.4. There is no replacement for it. This option created documentation with the appearance and functionality of documentation generated by Javadoc 1.1 (it never supported nested classes). If you need this option, use Javadoc 1.2 or 1.3 instead.</i></p>
<dt>-source release</p>
<dd> Specifies the version of source code accepted. The following values for <i>release</i> are allowed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> <code>1.5</code> &#8211; javadoc accepts code containing generics and other language features introduced in JDK 1.5. The compiler defaults to the 1.5 behavior if the <code>-source</code> flag is not used.</p>
<dt>o</p>
<dd> <code>1.4</code> &#8211; javadoc accepts code containing assertions, which were introduced in JDK 1.4.</p>
<dt>o</p>
<dd> <code>1.3</code> &#8211; javadoc does <i>not</i> support assertions, generics, or other language features introduced after JDK 1.3.</dl>
</dl>
<p> Use the value of <i>release</i> corresponding to that used when compiling the code with javac.</p>
<dt>-sourcepath&nbsp;<wbr> sourcepathlist</p>
<dd> Specifies the search paths for finding source files (<i>.java</i>) when passing package names or <i>-subpackages</i> into the <i>javadoc</i> command. The <i>sourcepathlist</i> can contain multiple paths by separating them with a colon (<i>:</i>). The Javadoc tool will search in all subdirectories of the specified paths. Note that this option is not only used to locate the source files being documented, but also to find source files that are not being documented but whose comments are inherited by the source files being documented. </p>
<p> Note that you can use the <i>-sourcepath</i> option only when passing package names into the javadoc command &#8212; it will not locate <i>.java</i> files passed into the <i>javadoc</i> command. (To locate <i>.java</i> files, cd to that directory or include the path ahead of each file, as shown at Documenting One or More Classes.) If <i>-sourcepath</i> is omitted, javadoc uses the class path to find the source files (see -classpath). Therefore, the default -sourcepath is the value of class path. If -classpath is omitted and you are passing package names into javadoc, it looks in the current directory (and subdirectories) for the source files. </p>
<p> Set <i>sourcepathlist</i> to the root directory of the source tree for the package you are documenting. For example, suppose you want to document a package called <i>com.mypackage</i> whose source files are located at: </p>
<pre>
<code>  /home/user/src/com/mypackage/*.java</code>
</pre>
<p> In this case you would specify the <i>sourcepath</i> to <i>/home/user/src</i>, the directory that contains <i>com/mypackage</i>, and then supply the package name <i>com.mypackage</i>: </p>
<pre>
<code>  % </code><code>javadoc -sourcepath /home/user/src/ com.mypackage</code>
</pre>
<p> This is easy to remember by noticing that if you concatenate the value of sourcepath and the package name together and change the dot to a slash &quot;/&quot;, you end up with the full path to the package: <i>/home/user/src/com/mypackage</i>. </p>
<p> To point to two source paths: </p>
<pre>
<code>  % </code><code>javadoc -sourcepath /home/user1/src:/home/user2/src com.mypackage</code>
</pre>
<dt>-classpath&nbsp;<wbr> classpathlist</p>
<dd> Specifies the paths where javadoc will look for referenced classes (<i>.class</i> files) &#8212; these are the documented classes plus any classes referenced by those classes. The <i>classpathlist</i> can contain multiple paths by separating them with a colon (<i>:</i>). The Javadoc tool will search in all subdirectories of the specified paths. Follow the instructions in <i>class path</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/technotes/tools/index.html#general">http://docs.oracle.com/javase/7/docs/technotes/tools/index.html#general</a> documentation for specifying <i>classpathlist</i>. </p>
<p> If <i>-sourcepath</i> is omitted, the Javadoc tool uses <i>-classpath</i> to find the source files as well as class files (for backward compatibility). Therefore, if you want to search for source and class files in separate paths, use both <i>-sourcepath</i> and <i>-classpath</i>. </p>
<p> For example, if you want to document <i>com.mypackage</i>, whose source files reside in the directory <i>/home/user/src/com/mypackage</i>, and if this package relies on a library in <i>/home/user/lib</i>, you would specify: </p>
<pre>
<code>  % </code><code>javadoc -classpath /home/user/lib -sourcepath /home/user/src com.mypackage</code>
</pre>
<p> As with other tools, if you do not specify <i>-classpath</i>, the Javadoc tool uses the CLASSPATH environment variable, if it is set. If both are not set, the Javadoc tool searches for classes from the current directory. </p>
<p> For an in-depth description of how the Javadoc tool uses <i>-classpath</i> to find user classes as it relates to extension classes and bootstrap classes, see <i>How Classes Are Found</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/technotes/tools/findingclasses.html.">http://docs.oracle.com/javase/7/docs/technotes/tools/findingclasses.html.</a> </p>
<p> As a special convenience, a class path element containing a basename of <i>*</i> is considered equivalent to specifying a list of all the files in the directory with the extension <i>.jar</i> or <i>.JAR</i> (a Java program cannot tell the difference between the two invocations). </p>
<p> For example, if directory <i>foo</i> contains <i>a.jar</i> and <i>b.JAR</i>, then the class path element <i>foo/*</i> is expanded to a <i>A.jar:b.JAR</i>, except that the order of jar files is unspecified. All jar files in the specified directory, even hidden ones, are included in the list. A classpath entry consisting simply of <i>*</i> expands to a list of all the jar files in the current directory. The <i>CLASSPATH</i> environment variable, where defined, will be similarly expanded. Any classpath wildcard expansion occurs before the Java virtual machine is started &#8212; no Java program will ever see unexpanded wildcards except by querying the environment. For example; by invoking <i>System.getenv(&quot;CLASSPATH&quot;)</i>.</p>
<dt>-subpackages&nbsp;<wbr>&nbsp;<wbr>package1:package2:&#8230;</p>
<dd> Generates documentation from source files in the specified packages and recursively in their subpackages. This option is useful when adding new subpackages to the source code, as they are automatically included. Each <i>package</i> argument is any top-level subpackage (such as <i>java</i>) or fully qualified package (such as <i>javax.swing</i>) that does not need to contain source files. Arguments are separated by colons (on all operating systmes). Wildcards are not needed or allowed. Use <i>-sourcepath</i> to specify where to find the packages. This option is smart about not processing source files that are in the source tree but do not belong to the packages, as described at processing of source files. </p>
<p> For example: </p>
<pre>
<code>  % </code><code>javadoc -d docs -sourcepath /home/user/src -subpackages java:javax.swing</code>
</pre>
<p> This command generates documentation for packages named &quot;java&quot; and &quot;javax.swing&quot; and all their subpackages. </p>
<p> You can use <i>-subpackages</i> in conjunction with <i>-exclude</i> to exclude specific packages.</p>
<dt>-exclude&nbsp;<wbr>&nbsp;<wbr>packagename1:packagename2:&#8230;</p>
<dd> Unconditionally excludes the specified packages and their subpackages from the list formed by <i>-subpackages</i>. It excludes those packages even if they would otherwise be included by some previous or later <i>-subpackages</i> option. For example: </p>
<pre>
<code>  % </code><code>javadoc -sourcepath /home/user/src -subpackages java -exclude java.net:java.lang</code>
</pre>
<p> would include <i>java.io</i>, <i>java.util</i>, and <i>java.math</i> (among others), but would exclude packages rooted at <i>java.net</i> and <i>java.lang</i>. Notice this excludes <i>java.lang.ref</i>, a subpackage of <i>java.lang</i>).</p>
<dt>-bootclasspath&nbsp;<wbr> classpathlist</p>
<dd> Specifies the paths where the boot classes reside. These are nominally the Java platform classes. The bootclasspath is part of the search path the Javadoc tool will use to look up source and class files. See <i>How Classes Are Found</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/technotes/tools/findingclasses.html#srcfiles.">http://docs.oracle.com/javase/7/docs/technotes/tools/findingclasses.html#srcfiles.</a> for more details. Separate directories in <i>classpathlist</i> with colons (:).</p>
<dt>-extdirs&nbsp;<wbr> dirlist</p>
<dd> Specifies the directories where extension classes reside. These are any classes that use the Java Extension mechanism. The extdirs is part of the search path the Javadoc tool will use to look up source and class files. See <i>-classpath</i> (above) for more details. Separate directories in <i>dirlist</i> with colons (:).</p>
<dt>-verbose</p>
<dd> Provides more detailed messages while javadoc is running. Without the verbose option, messages appear for loading the source files, generating the documentation (one message per source file), and sorting. The verbose option causes the printing of additional messages specifying the number of milliseconds to parse each java source file.</p>
<dt>-quiet</p>
<dd> Shuts off non-error and non-warning messages, leaving only the warnings and errors appear, making them easier to view. Also suppresses the version string.</p>
<dt>-breakiterator&nbsp;<wbr></p>
<dd> Uses the internationalized sentence boundary of <i>java.text.BreakIterator</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/api/java/text/BreakIterator.html">http://docs.oracle.com/javase/7/docs/api/java/text/BreakIterator.html</a> to determine the end of the first sentence for English (all other locales already use <i>BreakIterator</i>), rather than an English language, locale-specific algorithm. By <i>first sentence</i>, we mean the first sentence in the main description of a package, class or member. This sentence is copied to the package, class or member summary, and to the alphabetic index. </p>
<p> From JDK 1.2 forward, the BreakIterator class is already used to determine the end of sentence for all languages but English. Therefore, the <i>-breakiterator</i> option has no effect except for English from 1.2 forward. English has its own default algorithm:</p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> English default sentence-break algorithm &#8211; Stops at a period followed by a space or a HTML block tag, such as <i>&lt;P&gt;</i>.</p>
<dt>o</p>
<dd> Breakiterator sentence-break algorithm &#8211; In general, stops at a period, question mark or exclamation mark followed by a space if the next word starts with a capital letter. This is meant to handle most abbreviations (such as &quot;The serial no. is valid&quot;, but won&#8217;t handle &quot;Mr. Smith&quot;). Doesn&#8217;t stop at HTML tags or sentences that begin with numbers or symbols. Stops at the last period in &quot;../filename&quot;, even if embedded in an HTML tag.</dl>
</dl>
<p> NOTE: We have removed from 1.5.0 the breakiterator warning messages that were in 1.4.x and have left the default sentence-break algorithm unchanged. That is, the -breakiterator option is not the default in 1.5.0, nor do we expect it to become the default. This is a reversal from our former intention that the default would change in the &quot;next major release&quot; (1.5.0). This means if you have not modified your source code to eliminate the breakiterator warnings in 1.4.x, then you don&#8217;t have to do anything, and the warnings go away starting with 1.5.0. The reason for this reversal is because any benefit to having breakiterator become the default would be outweighed by the incompatible source change it would require. We regret any extra work and confusion this has caused.</p>
<dt>-locale&nbsp;<wbr> language_country_variant</p>
<dd> <code>Important</code> &#8211; The <i>-locale</i> option must be placed <i>ahead</i> (to the left) of any options provided by the standard doclet or any other doclet. Otherwise, the navigation bars will appear in English. This is the only command-line option that is order-dependent. </p>
<p> Specifies the locale that javadoc uses when generating documentation. The argument is the name of the locale, as described in java.util.Locale documentation, such as <i>en_US</i> (English, United States) or <i>en_US_WIN</i> (Windows variant). </p>
<p> Specifying a locale causes javadoc to choose the resource files of that locale for messages (strings in the navigation bar, headings for lists and tables, help file contents, comments in stylesheet.css, and so forth). It also specifies the sorting order for lists sorted alphabetically, and the sentence separator to determine the end of the first sentence. It does not determine the locale of the doc comment text specified in the source files of the documented classes.</p>
<dt>-encoding&nbsp;<wbr> name</p>
<dd> Specifies the encoding name of the source files, such as <i>EUCJIS/SJIS</i>. If this option is not specified, the platform default converter is used. </p>
<p> Also see -docencoding and -charset.</p>
<dt>-Jflag</p>
<dd> Passes <i>flag</i> directly to the runtime system java that runs javadoc. Notice there must be no space between the <i>J</i> and the <i>flag</i>. For example, if you need to ensure that the system sets aside 32 megabytes of memory in which to process the generated documentation, then you would call the <i>-Xmx</i> option of java as follows (<i>-Xms</i> is optional, as it only sets the size of initial memory, which is useful if you know the minimum amount of memory required): </p>
<pre>
<code>   % </code><code>javadoc -J-Xmx32m -J-Xms32m</code> <code>com.mypackage</code>
</pre>
<p> To tell what version of javadoc you are using, call the &quot;<i>-version</i>&quot; option of java: </p>
<pre>
<code>   % </code><code>javadoc -J-version</code>
   java version &quot;1.2&quot;
   Classic VM (build JDK-1.2-V, green threads, sunwjit)
</pre>
<p> (The version number of the standard doclet appears in its output stream.)</dl>
</dl>
<h3>Options Provided by the Standard Doclet</h3>
<dl>
<dt>
<dd>
<dl>
<dt>-d&nbsp;<wbr> directory</p>
<dd> Specifies the destination directory where javadoc saves the generated HTML files. (The &quot;d&quot; means &quot;destination.&quot;) Omitting this option causes the files to be saved to the current directory. The value <i>directory</i> can be absolute, or relative to the current working directory. As of 1.4, the destination directory is automatically created when javadoc is run. </p>
<p> For example, the following generates the documentation for the package <i>com.mypackage</i> and saves the results in the <i>/home/user/doc/</i> directory: </p>
<pre>
<code>  % </code><code>javadoc -d /home/user/doc com.mypackage</code>
</pre>
<dt>-use</p>
<dd> Includes one &quot;Use&quot; page for each documented class and package. The page describes what packages, classes, methods, constructors and fields use any API of the given class or package. Given class C, things that use class C would include subclasses of C, fields declared as C, methods that return C, and methods and constructors with parameters of type C. </p>
<p> For example, let us look at what might appear on the &quot;Use&quot; page for String. The <i>getName()</i> method in the <i>java.awt.Font</i> class returns type <i>String</i>. Therefore, <i>getName()</i> uses <i>String</i>, and you will find that method on the &quot;Use&quot; page for <i>String</i>. </p>
<p> Note that this documents only uses of the API, not the implementation. If a method uses <i>String</i> in its implementation but does not take a string as an argument or return a string, that is not considered a &quot;use&quot; of <i>String</i>. </p>
<p> You can access the generated &quot;Use&quot; page by first going to the class or package, then clicking on the &quot;Use&quot; link in the navigation bar.</p>
<dt>-version</p>
<dd> Includes the @version text in the generated docs. This text is omitted by default. To tell what version of the Javadoc tool you are using, use the <i>-J-version</i> option.</p>
<dt>-author</p>
<dd> Includes the @author text in the generated docs.</p>
<dt>-splitindex</p>
<dd> Splits the index file into multiple files, alphabetically, one file per letter, plus a file for any index entries that start with non-alphabetical characters.</p>
<dt>-windowtitle&nbsp;<wbr> title</p>
<dd> Specifies the title to be placed in the HTML &lt;title&gt; tag. This appears in the window title and in any browser bookmarks (favorite places) that someone creates for this page. This title should not contain any HTML tags, as the browser will not properly interpret them. Any internal quotation marks within <i>title</i> may have to be escaped. If -windowtitle is omitted, the Javadoc tool uses the value of -doctitle for this option. </p>
<pre>
<code>  % </code><code>javadoc -windowtitle &quot;Java SE Platform&quot; com.mypackage</code>
</pre>
<dt>-doctitle&nbsp;<wbr> title</p>
<dd> Specifies the title to be placed near the top of the overview summary file. The title will be placed as a centered, level-one heading directly beneath the upper navigation bar. The <i>title</i> may contain html tags and white space, though if it does, it must be enclosed in quotes. Any internal quotation marks within <i>title</i> may have to be escaped. </p>
<pre>
<code>  % </code><code>javadoc -doctitle &quot;Java(TM)&quot; com.mypackage</code>
</pre>
<dt>-title&nbsp;<wbr> title</p>
<dd> <code>This option no longer exists.</code> It existed only in Beta versions of Javadoc 1.2. It has been renamed to <i>-doctitle</i>. This option is being renamed to make it clear that it defines the document title rather than the window title.</p>
<dt>-header&nbsp;<wbr> header</p>
<dd> Specifies the header text to be placed at the top of each output file. The header will be placed to the right of the upper navigation bar. <i>header</i> may contain HTML tags and white space, though if it does, it must be enclosed in quotes. Any internal quotation marks within <i>header</i> may have to be escaped. </p>
<pre>
<code>  % </code><code>javadoc -header &quot;&lt;b&gt;Java 2 Platform &lt;/b&gt;&lt;br&gt;v1.4&quot; com.mypackage</code>
</pre>
<dt>-footer&nbsp;<wbr> footer</p>
<dd> Specifies the footer text to be placed at the bottom of each output file. The footer will be placed to the right of the lower navigation bar. <i>footer</i> may contain html tags and white space, though if it does, it must be enclosed in quotes. Any internal quotation marks within <i>footer</i> may have to be escaped.</p>
<dt>-top</p>
<dd> Specifies the text to be placed at the top of each output file.</p>
<dt>-bottom&nbsp;<wbr> text</p>
<dd> Specifies the text to be placed at the bottom of each output file. The text will be placed at the bottom of the page, below the lower navigation bar. The <i>text</i> may contain HTML tags and white space, though if it does, it must be enclosed in quotes. Any internal quotation marks within <i>text</i> may have to be escaped.</p>
<dt>-link&nbsp;<wbr> extdocURL</p>
<dd> Creates links to existing javadoc-generated documentation of external referenced classes. It takes one argument:</p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> <tt>extdocURL</tt> is the absolute or relative URL of the directory containing the external javadoc-generated documentation you want to link to. Examples are shown below. The package-list file must be found in this directory (otherwise, use <i>-linkoffline</i>). The Javadoc tool reads the package names from the <i>package-list</i> file and then links to those packages at that URL. When the Javadoc tool is run, the <i>extdocURL</i> value is copied literally into the <i>&lt;A href&gt;</i> links that are created. Therefore, <i>extdocURL</i> must be the URL to the <i>directory</i>, not to a file. </p>
<p> You can use an absolute link for <i>extdocURL</i> to enable your docs to link to a document on any website, or can use a relative link to link only to a relative location. If relative, the value you pass in should be the relative path from the destination directory (specified with <i>-d</i>) to the directory containing the packages being linked to. </p>
<p> When specifying an absolute link you normally use an <i>http:</i> link. However, if you want to link to a file system that has no web server, you can use a <i>file:</i> link &#8212; however, do this only if everyone wanting to access the generated documentation shares the same file system. </p>
<p> In all cases, and on all operating systems, you should use a forward slash as the separator, whether the URL is absolute or relative, and &quot;http:&quot; or &quot;file:&quot; based (as specified in the <i>URL Memo</i> @ <a rel="nofollow" href="http://www.ietf.org/rfc/rfc1738.txt">http://www.ietf.org/rfc/rfc1738.txt</a>).</p>
<dl>
<dt>
<dd>
<dl>
<dt>Absolute http: based link:</p>
<dd> <i>-link http://&lt;host&gt;/&lt;directory&gt;/&lt;directory&gt;/&#8230;/&lt;name&gt;</i></p>
<dt>Absolute file: based link:</p>
<dd> <i>-link file://&lt;host&gt;/&lt;directory&gt;/&lt;directory&gt;/&#8230;/&lt;name&gt;</i></p>
<dt>Relative link:</p>
<dd> <i>-link &lt;directory&gt;/&lt;directory&gt;/&#8230;/&lt;name&gt;</i></dl>
</dl>
</dl>
</dl>
<p> You can specify multiple <i>-link</i> options in a given javadoc run to link to multiple documents. </p>
<p> <code>Choosing between -linkoffline and -link</code>: </p>
<p> Use <i>-link</i>:</p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> when using a relative path to the external API document, or</p>
<dt>o</p>
<dd> when using an absolute URL to the external API document, if your shell allows a program to open a connection to that URL for reading.</dl>
</dl>
<p> Use <i>-linkoffline</i>:</p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> when using an absolute URL to the external API document, if your shell <i>does not allow</i> a program to open a connection to that URL for reading. This can occur if you are behind a firewall and the document you want to link to is on the other side.</dl>
</dl>
<p> <code>Example using absolute links to the external docs</code> &#8211; Let us say you want to link to the <i>java.lang</i>, <i>java.io</i> and other Java Platform packages at <i><a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/api/">http://docs.oracle.com/javase/7/docs/api/</a></i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/api/.">http://docs.oracle.com/javase/7/docs/api/.</a> The following command generates documentation for the package <i>com.mypackage</i> with links to the Java SE Platform packages. The generated documentation will contain links to the <i>Object</i> class, for example, in the class trees. (Other options, such as <i>-sourcepath</i> and <i>-d</i>, are not shown.) </p>
<pre>
<code>  % </code><code>javadoc -link <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/api/">http://docs.oracle.com/javase/7/docs/api/</a> com.mypackage</code>
</pre>
<p> <code>Example using relative links to the external docs</code> &#8211; Let us say you have two packages whose docs are generated in different runs of the Javadoc tool, and those docs are separated by a relative path. In this example, the packages are <i>com.apipackage</i>, an API, and <i>com.spipackage</i>, an SPI (Service Provide Interface). You want the documentation to reside in <i>docs/api/com/apipackage</i> and <i>docs/spi/com/spipackage</i>. Assuming the API package documentation is already generated, and that <i>docs</i> is the current directory, you would document the SPI package with links to the API documentation by running: </p>
<pre>
<code>  % </code><code>javadoc -d ./spi -link ../api com.spipackage</code>
</pre>
<p> Notice the <i>-link</i> argument is relative to the destination directory (<i>docs/spi</i>). </p>
<p> <code>Details</code> &#8211; The <i>-link</i> option enables you to link to classes referenced to by your code but <i>not</i> documented in the current javadoc run. For these links to go to valid pages, you must know where those HTML pages are located, and specify that location with <i>extdocURL</i>. This allows, for instance, third party documentation to link to <i>java.*</i> documentation on <i><a rel="nofollow" href="http://java.sun.com">http://java.sun.com</a></i>. </p>
<p> Omit the <i>-link</i> option for javadoc to create links only to API within the documentation it is generating in the current run. (Without the <i>-link</i> option, the Javadoc tool does not create links to documentation for external references, because it does not know if or where that documentation exists.) </p>
<p> This option can create links in several places in the generated documentation. </p>
<p> Another use is for cross-links between sets of packages: Execute javadoc on one set of packages, then run javadoc again on another set of packages, creating links both ways between both sets. </p>
<p> <code>How a Class Must be Referenced</code> &#8211; For a link to an external referenced class to actually appear (and not just its text label), the class must be referenced in the following way. It is not sufficient for it to be referenced in the body of a method. It must be referenced in either an <i>import</i> statement or in a declaration. Here are examples of how the class <i>java.io.File</i> can be referenced:</p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> In any kind of <i>import</i> statement: by wildcard import, import explicitly by name, or automatically import for <i>java.lang.*</i>. For example, this would suffice:<br />
 <i>import java.io.*;</i><br />
 In 1.3.x and 1.2.x, only an explicit import by name works &#8212; a wildcard import statement does not work, nor does the automatic import <i>java.lang.*</i>.</p>
<dt>o</p>
<dd> In a declaration:<br />
 <i>void foo(File f) {}</i><br />
 The reference and be in the return type or parameter type of a method, constructor, field, class or interface, or in an <i>implements</i>, <i>extends</i> or <i>throws</i> statement.</dl>
</dl>
<p> An important corollary is that when you use the <i>-link</i> option, there may be many links that unintentionally do not appear due to this constraint. (The text would appear without a hypertext link.) You can detect these by the warnings they emit. The most innocuous way to properly reference a class and thereby add the link would be to import that class, as shown above. </p>
<p> <code>Package List</code> &#8211; The <i>-link</i> option requires that a file named <i>package-list</i>, which is generated by the Javadoc tool, exist at the URL you specify with <i>-link</i>. The <i>package-list</i> file is a simple text file that lists the names of packages documented at that location. In the earlier example, the Javadoc tool looks for a file named <i>package-list</i> at the given URL, reads in the package names and then links to those packages at that URL. </p>
<p> For example, the package list for the Java SE 6 API is located at <i><a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/api/package-list">http://docs.oracle.com/javase/7/docs/api/package-list</a></i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/api/package-list.">http://docs.oracle.com/javase/7/docs/api/package-list.</a> and starts as follows: </p>
<pre>
<code>  java.applet  
  java.awt
  java.awt.color
  java.awt.datatransfer
  java.awt.dnd
  java.awt.event
  java.awt.font
  etc.</code>
</pre>
<p> When javadoc is run without the <i>-link</i> option, when it encounters a name that belongs to an external referenced class, it prints the name with no link. However, when the <i>-link</i> option is used, the Javadoc tool searches the <i>package-list</i> file at the specified <i>extdocURL</i> location for that package name. If it finds the package name, it prefixes the name with <i>extdocURL</i>. </p>
<p> In order for there to be no broken links, all of the documentation for the external references must exist at the specified URLs. The Javadoc tool will not check that these pages exist &#8212; only that the package-list exists. </p>
<p> <code>Multiple Links</code> &#8211; You can supply multiple <i>-link</i> options to link to any number of external generated documents. &nbsp;<wbr> Javadoc 1.2 has a known bug which prevents you from supplying more than one <i>-link</i> command. This was fixed in 1.2.2. </p>
<p> Specify a different link option for each external document to link to: </p>
<p> &nbsp;<wbr>&nbsp;<wbr> <i>% </i><tt>javadoc -link</tt> <i>extdocURL1</i> <tt>-link</tt> <i>extdocURL2</i> <i>&#8230; </i><tt>-link</tt> <i>extdocURLn</i> <tt>com.mypackage</tt> </p>
<p> where <i>extdocURL1</i>,&nbsp;<wbr> <i>extdocURL2</i>,&nbsp;<wbr> &#8230; <i>extdocURLn</i> point respectively to the roots of external documents, each of which contains a file named <i>package-list</i>. </p>
<p> <code>Cross-links</code> &#8211; Note that &quot;bootstrapping&quot; may be required when cross-linking two or more documents that have not previously been generated. In other words, if <i>package-list</i> does not exist for either document, when you run the Javadoc tool on the first document, the <i>package-list</i> will not yet exist for the second document. Therefore, to create the external links, you must re-generate the first document after generating the second document. </p>
<p> In this case, the purpose of first generating a document is to create its <i>package-list</i> (or you can create it by hand it if you&#8217;re certain of the package names). Then generate the second document with its external links. The Javadoc tool prints a warning if a needed external <i>package-list</i> file does not exist.</p>
<dt>-linkoffline&nbsp;<wbr> extdocURL&nbsp;<wbr> packagelistLoc</p>
<dd> This option is a variation of <i>-link</i>; they both create links to javadoc-generated documentation for external referenced classes. Use the <i>-linkoffline</i> option when linking to a document on the web when the Javadoc tool itself is &quot;offline&quot; &#8212; that is, it cannot access the document through a web connection. </p>
<p> More specifically, use <i>-linkoffline</i> if the external document&#8217;s <i>package-list</i> file is not accessible or does not exist at the <i>extdocURL</i> location but does exist at a different location, which can be specified by <i>packageListLoc</i> (typically local). Thus, if <i>extdocURL</i> is accessible only on the World Wide Web, <i>-linkoffline</i> removes the constraint that the Javadoc tool have a web connection when generating the documentation. </p>
<p> Another use is as a &quot;hack&quot; to update docs: After you have run javadoc on a full set of packages, then you can run javadoc again on onlya smaller set of changed packages, so that the updated files can be inserted back into the original set. Examples are given below. </p>
<p> The <i>-linkoffline</i> option takes two arguments &#8212; the first for the string to be embedded in the <i>&lt;a href&gt;</i> links, the second telling it where to find <i>package-list</i>:</p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> <tt>extdocURL</tt> is the absolute or relative URL of the directory containing the external javadoc-generated documentation you want to link to. If relative, the value should be the relative path from the destination directory (specified with <i>-d</i>) to the root of the packages being linked to. For more details, see <i>extdocURL</i> in the <i>-link</i> option.</p>
<dt>o</p>
<dd> <tt>packagelistLoc</tt> is the path or URL to the directory containing the <i>package-list</i> file for the external documentation. This can be a URL (http: or file:) or file path, and can be absolute or relative. If relative, make it relative to the <i>current</i> directory from where javadoc was run. Do not include the <i>package-list</i> filename.</dl>
</dl>
<p> You can specify multiple <i>-linkoffline</i> options in a given javadoc run. (Prior to 1.2.2, it could be specified only once.) </p>
<p> <code>Example using absolute links to the external docs</code> &#8211; Let us say you want to link to the <i>java.lang</i>, <i>java.io</i> and other Java SE Platform packages at <i><a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/api/">http://docs.oracle.com/javase/7/docs/api/</a></i>, but your shell does not have web access. You could open the <i>package-list</i> file in a browser at <i><a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/api/package-list">http://docs.oracle.com/javase/7/docs/api/package-list</a></i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/api/package-list,">http://docs.oracle.com/javase/7/docs/api/package-list,</a> save it to a local directory, and point to this local copy with the second argument, <i>packagelistLoc</i>. In this example, the package list file has been saved to the current directory &quot;<i>.</i>&quot; . The following command generates documentation for the package <i>com.mypackage</i> with links to the Java SE Platform packages. The generated documentation will contain links to the <i>Object</i> class, for example, in the class trees. (Other necessary options, such as <i>-sourcepath</i>, are not shown.) </p>
<pre>
<code>% </code><code>javadoc -linkoffline <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/api/">http://docs.oracle.com/javase/7/docs/api/</a> . com.mypackage</code>
</pre>
<p> <code>Example using relative links to the external docs</code> &#8211; It&#8217;s not very common to use <i>-linkoffline</i> with relative paths, for the simple reason that <i>-link</i> usually suffices. When using <i>-linkoffline</i>, the <i>package-list</i> file is generally local, and when using relative links, the file you are linking to is also generally local. So it is usually unnecessary to give a different path for the two arguments to <i>-linkoffline</i>. When the two arguments are identical, you can use <i>-link</i>. See the <i>-link</i> relative example. </p>
<p> <code>Manually Creating a </code><tt>package-list</tt><code> File</code> &#8211; If a <i>package-list</i> file does not yet exist, but you know what package names your document will link to, you can create your own copy of this file by hand and specify its path with <i>packagelistLoc</i>. An example would be the previous case where the package list for <i>com.spipackage</i> did not exist when <i>com.apipackage</i> was first generated. This technique is useful when you need to generate documentation that links to new external documentation whose package names you know, but which is not yet published. This is also a way of creating <i>package-list</i> files for packages generated with Javadoc 1.0 or 1.1, where <i>package-list</i> files were not generated. Likewise, two companies can share their unpublished <i>package-list</i> files, enabling them to release their cross-linked documentation simultaneously. </p>
<p> <code>Linking to Multiple Documents</code> &#8211; You can include <i>-linkoffline</i> once for each generated document you want to refer to (each option is shown on a separate line for clarity): </p>
<p> <i>% </i><tt>javadoc -linkoffline</tt> <i>extdocURL1</i> <i>packagelistLoc1</i> <i>\</i><br />
 <i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></i><tt>-linkoffline</tt> <i>extdocURL2</i> <i>packagelistLoc2</i> <i>\</i><br />
 <i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8230;</i> </p>
<p> <code>Updating docs</code> &#8211; Another use for <i>-linkoffline</i> option is useful if your project has dozens or hundreds of packages, if you have already run javadoc on the entire tree, and now, in a separate run, you want to quickly make some small changes and re-run javadoc on just a small portion of the source tree. This is somewhat of a hack in that it works properly only if your changes are only to doc comments and not to declarations. If you were to add, remove or change any declarations from the source code, then broken links could show up in the index, package tree, inherited member lists, use page, and other places. </p>
<p> First, you create a new destination directory (call it <i>update</i>) for this new small run. Let us say the original destination directory was named <i>html</i>. In the simplest example, cd to the parent of <i>html</i>. Set the first argument of <i>-linkoffline</i> to the current directory &quot;.&quot; and set the second argument to the relative path to <i>html</i>, where it can find <i>package-list</i>, and pass in only the package names of the packages you want to update: </p>
<pre>
<code>  % </code><code>javadoc -d update -linkoffline . html com.mypackage</code>
</pre>
<p> When the Javadoc tool is done, copy these generated class pages in <i>update/com/package</i> (not the overview or index), over the original files in <i>html/com/package</i>.</p>
<dt>-linksource&nbsp;<wbr></p>
<dd> Creates an HTML version of each source file (with line numbers) and adds links to them from the standard HTML documentation. Links are created for classes, interfaces, constructors, methods and fields whose declarations are in a source file. Otherwise, links are not created, such as for default constructors and generated classes. </p>
<p> <code>This option exposes </code><tt>all</tt><code> private implementation details in the included source files, including private classes, private fields, and the bodies of private methods, </code><tt>regardless of the </tt><tt>-public</tt><code>, </code><tt>-package</tt><code>, </code><tt>-protected</tt><code> and </code><tt>-private</tt><code> options.</code> Unless you also use the <i>-private</i> option, not all private classes or interfaces will necessarily be accessible via links. </p>
<p> Each link appears on the name of the identifier in its declaration. For example, the link to the source code of the <i>Button</i> class would be on the word &quot;Button&quot;: </p>
<pre>
<code>    public class Button
    extends Component
    implements Accessible</code>
</pre>
<p> and the link to the source code of the <i>getLabel()</i> method in the Button class would be on the word &quot;getLabel&quot;: </p>
<pre>
<code>    public String getLabel()</code>
</pre>
<dt>-group&nbsp;<wbr> groupheading&nbsp;<wbr> packagepattern:packagepattern:&#8230;</p>
<dd> Separates packages on the overview page into whatever groups you specify, one group per table. You specify each group with a different <i>-group</i> option. The groups appear on the page in the order specified on the command line; packages are alphabetized within a group. For a given <i>-group</i> option, the packages matching the list of <i>packagepattern</i> expressions appear in a table with the heading <i>groupheading</i>.</p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> <tt>groupheading</tt> can be any text, and can include white space. This text is placed in the table heading for the group.</p>
<dt>o</p>
<dd> <tt>packagepattern</tt> can be any package name, or can be the start of any package name followed by an asterisk (<i>*</i>). The asterisk is a wildcard meaning &quot;match any characters&quot;. This is the only wildcard allowed. Multiple patterns can be included in a group by separating them with colons (<i>:</i>).</dl>
</dl>
<p> <code>NOTE: If using an asterisk in a pattern or pattern list, the pattern list must be inside quotes, such as </code><tt>&quot;java.lang*:java.util&quot;</tt> </p>
<p> If you do not supply any <i>-group</i> option, all packages are placed in one group with the heading &quot;Packages&quot;. If the all groups do not include all documented packages, any leftover packages appear in a separate group with the heading &quot;Other Packages&quot;. </p>
<p> For example, the following option separates the four documented packages into core, extension and other packages. Notice the trailing &quot;dot&quot; does not appear in &quot;java.lang*&quot; &#8212; including the dot, such as &quot;java.lang.*&quot; would omit the java.lang package. </p>
<pre>
<code>  % </code><code>javadoc -group &quot;Core Packages&quot; &quot;java.lang*:java.util&quot;
            -group &quot;Extension Packages&quot; &quot;javax.*&quot;
            java.lang java.lang.reflect java.util javax.servlet java.new</code>
</pre>
<p> This results in the groupings:</p>
<dl>
<dt>
<dd>
<dl>
<dt>Core Packages</p>
<dd> <i>java.lang</i> <i>java.lang.reflect</i> <i>java.util</i></p>
<dt>Extension Packages</p>
<dd> <i>javax.servlet</i></p>
<dt>Other Packages</p>
<dd> <i>java.new</i></dl>
</dl>
<dt>-nodeprecated</p>
<dd> Prevents the generation of any deprecated API at all in the documentation. This does what -nodeprecatedlist does, plus it does not generate any deprecated API throughout the rest of the documentation. This is useful when writing code and you don&#8217;t want to be distracted by the deprecated code.</p>
<dt>-nodeprecatedlist</p>
<dd> Prevents the generation of the file containing the list of deprecated APIs (deprecated-list.html) and the link in the navigation bar to that page. (However, javadoc continues to generate the deprecated API throughout the rest of the document.) This is useful if your source code contains no deprecated API, and you want to make the navigation bar cleaner.</p>
<dt>-nosince</p>
<dd> Omits from the generated docs the &quot;Since&quot; sections associated with the @since tags.</p>
<dt>-notree</p>
<dd> Omits the class/interface hierarchy pages from the generated docs. These are the pages you reach using the &quot;Tree&quot; button in the navigation bar. The hierarchy is produced by default.</p>
<dt>-noindex</p>
<dd> Omits the index from the generated docs. The index is produced by default.</p>
<dt>-nohelp</p>
<dd> Omits the HELP link in the navigation bars at the top and bottom of each page of output.</p>
<dt>-nonavbar</p>
<dd> Prevents the generation of the navigation bar, header and footer, otherwise found at the top and bottom of the generated pages. Has no affect on the &quot;bottom&quot; option. The <i>-nonavbar</i> option is useful when you are interested only in the content and have no need for navigation, such as converting the files to PostScript or PDF for print only.</p>
<dt>-helpfile&nbsp;<wbr> path/filename</p>
<dd> Specifies the path of an alternate help file <i>path/filename</i> that the HELP link in the top and bottom navigation bars link to. Without this option, the Javadoc tool automatically creates a help file <i>help-doc.html</i> that is hard-coded in the Javadoc tool. This option enables you to override this default. The <i>filename</i> can be any name and is not restricted to <i>help-doc.html</i> &#8212; the Javadoc tool will adjust the links in the navigation bar accordingly. For example: </p>
<pre>
<code>  % </code><code>javadoc -helpfile /home/user/myhelp.html java.awt</code>
</pre>
<dt>-stylesheetfile&nbsp;<wbr> path/filename</p>
<dd> Specifies the path of an alternate HTML stylesheet file. Without this option, the Javadoc tool automatically creates a stylesheet file <i>stylesheet.css</i> that is hard-coded in the Javadoc tool. This option enables you to override this default. The <i>filename</i> can be any name and is not restricted to <i>stylesheet.css</i>. For example: </p>
<pre>
<code>  % </code><code>javadoc -stylesheetfile /home/user/mystylesheet.css com.mypackage</code>
</pre>
<dt>-serialwarn</p>
<dd> Generates compile-time warnings for missing @serial tags. By default, Javadoc 1.2.2 (and later versions) generates no serial warnings. (This is a reversal from earlier versions.) Use this option to display the serial warnings, which helps to properly document default serializable fields and <i>writeExternal</i> methods.</p>
<dt>-charset&nbsp;<wbr> name</p>
<dd> Specifies the HTML character set for this document. The name should be a preferred MIME name as given in the <i>IANA Registry</i> @ <a rel="nofollow" href="http://www.iana.org/assignments/character-sets.">http://www.iana.org/assignments/character-sets.</a> For example: </p>
<pre>
<code>  % </code><code>javadoc -charset &quot;iso-8859-1&quot; mypackage</code>
</pre>
<p> would insert the following line in the head of every generated page: </p>
<pre>
<code>   &lt;META http-equiv=&quot;Content-Type&quot; content=&quot;text/html; charset=ISO-8859-1&quot;&gt;</code>
</pre>
<p> This META tag is described in the <i>HTML standard</i> @ <a rel="nofollow" href="http://www.w3.org/TR/REC-html40/charset.html#h-5.2.2.">http://www.w3.org/TR/REC-html40/charset.html#h-5.2.2.</a> (4197265 and 4137321) </p>
<p> Also see -encoding and -docencoding.</p>
<dt>-docencoding&nbsp;<wbr> name</p>
<dd> Specifies the encoding of the generated HTML files. The name should be a preferred MIME name as given in the <i>IANA Registry</i> @ <a rel="nofollow" href="http://www.iana.org/assignments/character-sets.">http://www.iana.org/assignments/character-sets.</a> If you omit this option but use -encoding, then the encoding of the generated HTML files is determined by -encoding. Example: </p>
<pre>
<code>  % </code><code>javadoc -docencoding &quot;ISO-8859-1&quot; mypackage</code>
</pre>
<p> Also see -encoding and -charset.</p>
<dt>-keywords</p>
<dd> Adds HTML meta keyword tags to the generated file for each class. These tags can help the page be found by search engines that look for meta tags. (Most search engines that search the entire Internet do not look at meta tags, because pages can misuse them; but search engines offered by companies that confine their search to their own website can benefit by looking at meta tags.) </p>
<p> The meta tags include the fully qualified name of the class and the unqualified names of the fields and methods. Constructors are not included because they are identical to the class name. For example, the class String starts with these keywords: </p>
<pre>
<code>     &lt;META NAME=&quot;keywords&quot; CONTENT=&quot;java.lang.String class&quot;&gt;
     &lt;META NAME=&quot;keywords&quot; CONTENT=&quot;CASE_INSENSITIVE_ORDER&quot;&gt;
     &lt;META NAME=&quot;keywords&quot; CONTENT=&quot;length()&quot;&gt;
     &lt;META NAME=&quot;keywords&quot; CONTENT=&quot;charAt()&quot;&gt;</code>
</pre>
<dt>-tag&nbsp;<wbr>&nbsp;<wbr>tagname:Xaoptcmf:&quot;taghead&quot;</p>
<dd> Enables the Javadoc tool to interpret a simple, one-argument custom block tag <i>@</i><i>tagname</i> in doc comments. So the Javadoc tool can &quot;spell-check&quot; tag names, it is important to include a <i>-tag</i> option for every custom tag that is present in the source code, disabling (with <i>X</i>) those that are not being output in the current run. </p>
<p> The colon (<tt>:</tt>) is always the separator. To use a colon in <i>tagname</i>, see Use of Colon in Tag Name. </p>
<p> The <i>-tag</i> option outputs the tag&#8217;s heading <i>taghead</i> in bold, followed on the next line by the text from its single argument, as shown in the example below. Like any block tag, this argument&#8217;s text can contain inline tags, which are also interpreted. The output is similar to standard one-argument tags, such as <i>@return</i> and <i>@author</i>. Omitting <i>taghead</i> causes <i>tagname</i> to appear as the heading. </p>
<p> <code>Placement of tags</code> &#8211; The <tt>Xaoptcmf</tt> part of the argument determines where in the source code the tag is allowed to be placed, and whether the tag can be disabled (using <i>X</i>). You can supply either <tt>a</tt>, to allow the tag in all places, or any combination of the other letters: </p>
<p> <tt>X</tt> (disable tag)<br />
 <tt>a</tt> (all)<br />
 <tt>o</tt> (overview)<br />
 <tt>p</tt> (packages)<br />
 <tt>t</tt> (types, that is classes and interfaces)<br />
 <tt>c</tt> (constructors)<br />
 <tt>m</tt> (methods)<br />
 <tt>f</tt> (fields) </p>
<p> <code>Examples of single tags</code> &#8211; An example of a tag option for a tag that can be used anywhere in the source code is: </p>
<pre>
<code>    -tag todo:a:&quot;To Do:&quot;</code>
</pre>
<p> If you wanted @todo to be used only with constructors, methods and fields, you would use: </p>
<pre>
<code>    -tag todo:cmf:&quot;To Do:&quot;</code>
</pre>
<p> Notice the last colon (<i>:</i>) above is not a parameter separator, but is part of the heading text (as shown below). You would use either tag option for source code that contains the tag <i>@todo</i>, such as: </p>
<pre>
<code>     @todo The documentation for this method needs work.</code>
</pre>
<p> <code>Use of Colon in Tag Name</code> &#8211; A colon can be used in a tag name if it is escaped with a backslash. For this doc comment: </p>
<pre>
<code>    /**
     * @ejb:bean
     */</code>
</pre>
<p> use this tag option: </p>
<pre>
<code>    -tag ejb\:bean:a:&quot;EJB Bean:&quot;</code>
</pre>
<p> <code>Spell-checking tag names (Disabling tags)</code> &#8211; Some developers put custom tags in the source code that they don&#8217;t always want to output. In these cases, it is important to list all tags that are present in the source code, enabling the ones you want to output and disabling the ones you don&#8217;t want to output. The presence of <i>X</i> disables the tag, while its absence enables the tag. This gives the Javadoc tool enough information to know if a tag it encounters is unknown, probably the results of a typo or a misspelling. It prints a warning in these cases. </p>
<p> You can add <i>X</i> to the placement values already present, so that when you want to enable the tag, you can simply delete the <i>X</i>. For example, if @todo is a tag that you want to suppress on output, you would use: </p>
<pre>
<code>    -tag todo:Xcmf:&quot;To Do:&quot;</code>
</pre>
<p> or, if you&#8217;d rather keep it simple: </p>
<pre>
<code>    -tag todo:X</code>
</pre>
<p> The syntax <i>-tag todo:X</i> works even if <i>@todo</i> is defined by a taglet. </p>
<p> <code>Order of tags</code> &#8211; The order of the <i>-tag</i> (and <i>-taglet</i>) options determine the order the tags are output. You can mix the custom tags with the standard tags to intersperse them. The tag options for standard tags are placeholders only for determining the order &#8212; they take only the standard tag&#8217;s name. (Subheadings for standard tags cannot be altered.) This is illustrated in the following example. </p>
<p> If <i>-tag</i> is missing, then the position of <i>-taglet</i> determines its order. If they are both present, then whichever appears last on the command line determines its order. (This happens because the tags and taglets are processed in the order that they appear on the command line. For example, if <i>-taglet</i> and <i>-tag</i> both have the name &quot;todo&quot;, the one that appears last on the command line will determine its order. </p>
<p> <code>Example of a complete set of tags</code> &#8211; This example inserts &quot;To Do&quot; after &quot;Parameters&quot; and before &quot;Throws&quot; in the output. By using &quot;X&quot;, it also specifies that @example is a tag that might be encountered in the source code that should not be output during this run. Notice that if you use @argfile, you can put the tags on separate lines in an argument file like this (no line continuation characters needed): </p>
<pre>
<code>   -tag param
   -tag return
   -tag todo:a:&quot;To Do:&quot;
   -tag throws
   -tag see
   -tag example:X</code>
</pre>
<p> When javadoc parses the doc comments, any tag encountered that is neither a standard tag nor passed in with <i>-tag</i> or <i>-taglet</i> is considered unknown, and a warning is thrown. </p>
<p> The standard tags are initially stored internally in a list in their default order. Whenever <i>-tag</i> options are used, those tags get appended to this list &#8212; standard tags are moved from their default position. Therefore, if a <i>-tag</i> option is omitted for a standard tag, it remains in its default position. </p>
<p> <code>Avoiding Conflicts</code> &#8211; If you want to slice out your own namespace, you can use a dot-separated naming convention similar to that used for packages: <i>com.mycompany.todo</i>. Oracle will continue to create standard tags whose names do not contain dots. Any tag you create will override the behavior of a tag by the same name defined by Oracle. In other words, if you create a tag or taglet <i>@todo</i>, it will always have the same behavior you define, even if Oracle later creates a standard tag of the same name. </p>
<p> <code>Annotations vs. Javadoc Tags</code> &#8211; In general, if the markup you want to add is intended to affect or produce documentation, it should probably be a javadoc tag; otherwise, it should be an annotation. See <i>Comparing Annotations and Javadoc Tags</i> @ <a rel="nofollow" href="http://www.oracle.com/technetwork/java/javase/documentation/index-137868.html#annotations">http://www.oracle.com/technetwork/java/javase/documentation/index-137868.html#annotations</a>&lt; </p>
<p> You can also create more complex block tags, or custom inline tags with the -taglet option.</p>
<dt>-taglet&nbsp;<wbr>&nbsp;<wbr>class</p>
<dd> Specifies the class file that starts the taglet used in generating the documentation for that tag. Use the fully-qualified name for <i>class</i>. This taglet also defines the number of text arguments that the custom tag has. The taglet accepts those arguments, processes them, and generates the output. For extensive documentation with example taglets, see:</p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> <i>Taglet Overview</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/technotes/guides/javadoc/taglet/overview.html">http://docs.oracle.com/javase/7/docs/technotes/guides/javadoc/taglet/overview.html</a></dl>
</dl>
<p> Taglets are useful for block or inline tags. They can have any number of arguments and implement custom behavior, such as making text bold, formatting bullets, writing out the text to a file, or starting other processes. </p>
<p> Taglets can only determine where a tag should appear and in what form. All other decisions are made by the doclet. So a taglet cannot do things such as remove a class name from the list of included classes. However, it can execute side effects, such as printing the tag&#8217;s text to a file or triggering another process. </p>
<p> Use the <i>-tagletpath</i> option to specify the path to the taglet. Here is an example that inserts the &quot;To Do&quot; taglet after &quot;Parameters&quot; and ahead of &quot;Throws&quot; in the generated pages: </p>
<pre>
<code>    -taglet com.sun.tools.doclets.ToDoTaglet
    -tagletpath /home/taglets 
    -tag return
    -tag param
    -tag todo
    -tag throws
    -tag see</code>
</pre>
<p> Alternatively, you can use the <i>-taglet</i> option in place of its <i>-tag</i> option, but that may be harder to read.</p>
<dt>-tagletpath&nbsp;<wbr>&nbsp;<wbr>tagletpathlist</p>
<dd> Specifies the search paths for finding taglet class files (.class). The <i>tagletpathlist</i> can contain multiple paths by separating them with a colon (<i>:</i>). The Javadoc tool will search in all subdirectories of the specified paths.</p>
<dt>-docfilessubdirs&nbsp;<wbr></p>
<dd> Enables deep copying of &quot;<i>doc-files</i>&quot; directories. In other words, subdirectories and all contents are recursively copied to the destination. For example, the directory <i>doc-files/example/images</i> and all its contents would now be copied. There is also an option to exclude subdirectories.</p>
<dt>-excludedocfilessubdir&nbsp;<wbr>&nbsp;<wbr>name1:name2&#8230;</p>
<dd> Excludes any &quot;<i>doc-files</i>&quot; subdirectories with the given names. This prevents the copying of SCCS and other source-code-control subdirectories.</p>
<dt>-noqualifier&nbsp;<wbr>&nbsp;<wbr>all&nbsp;<wbr> | &nbsp;<wbr>packagename1:packagename2:&#8230;</p>
<dd> Omits qualifying package name from ahead of class names in output. The argument to <i>-noqualifier</i> is either &quot;<i>all</i>&quot; (all package qualifiers are omitted) or a colon-separate list of packages, with wildcards, to be removed as qualifiers. The package name is removed from places where class or interface names appear. </p>
<p> The following example omits all package qualifiers: </p>
<pre>
<code>    -noqualifier all</code>
</pre>
<p> The following example omits &quot;java.lang&quot; and &quot;java.io&quot; package qualifiers: </p>
<pre>
<code>    -noqualifier java.lang:java.io</code>
</pre>
<p> The following example omits package qualifiers starting with &quot;java&quot;, and &quot;com.sun&quot; subpackages (but not &quot;javax&quot;): </p>
<pre>
<code>    -noqualifier java.*:com.sun.*</code>
</pre>
<p> Where a package qualifier would appear due to the above behavior, the name can be suitably shortened &#8212; see How a name is displayed. This rule is in effect whether or not <i>-noqualifier</i> is used.</p>
<dt>-notimestamp&nbsp;<wbr></p>
<dd> Suppresses the timestamp, which is hidden in an HTML comment in the generated HTML near the top of each page. Useful when you want to run javadoc on two source bases and diff them, as it prevents timestamps from causing a diff (which would otherwise be a diff on every page). The timestamp includes the javadoc version number, and currently looks like this: </p>
<pre>
<code>     &lt;!-- Generated by javadoc (build 1.5.0_01) on Thu Apr 02 14:04:52 IST 2009 --&gt;</code>
</pre>
<dt>-nocomment&nbsp;<wbr></p>
<dd> Suppress the entire comment body, including the main description and all tags, generating only declarations. This option enables re-using source files originally intended for a different purpose, to produce skeleton HTML documentation at the early stages of a new project.</p>
<dt>-sourcetab tabLength</p>
<dd> Specify the number of spaces each tab takes up in the source.</dl>
</dl>
<h2>COMMAND LINE ARGUMENT FILES</h2>
<p> To shorten or simplify the javadoc command line, you can specify one or more files that themselves contain arguments to the <i>javadoc</i> command (except <i>-J</i> options). This enables you to create javadoc commands of any length on any operating system. </p>
<p> An argument file can include javac options and source filenames in any combination. The arguments within a file can be space-separated or newline-separated. If a filename contains embedded spaces, put the whole filename in double quotes. </p>
<p> Filenames within an argument file are relative to the current directory, not the location of the argument file. Wildcards (*) are not allowed in these lists (such as for specifying <i>*.java</i>). Use of the &#8216;<i>@</i>&#8216; character to recursively interpret files is not supported. The <i>-J</i> options are not supported because they are passed to the launcher, which does not support argument files. </p>
<p> When executing javadoc, pass in the path and name of each argument file with the &#8216;<i>@</i>&#8216; leading character. When javadoc encounters an argument beginning with the character `<i>@</i>&#8216;, it expands the contents of that file into the argument list.</p>
<h3>Example &#8211; Single Arg File</h3>
<p> You could use a single argument file named &quot;<i>argfile</i>&quot; to hold all Javadoc arguments: </p>
<pre>
<code>  % </code><code>javadoc @argfile</code>
</pre>
<p> This argument file could contain the contents of both files shown in the next example.</p>
<h3>Example &#8211; Two Arg Files</h3>
<p> You can create two argument files &#8212; one for the Javadoc options and the other for the package names or source filenames: (Notice the following lists have no line-continuation characters.) </p>
<p> Create a file named &quot;<i>options</i>&quot; containing: </p>
<pre>
<code>     -d docs-filelist 
     -use 
     -splitindex
     -windowtitle 'Java SE 7 API Specification'
     -doctitle 'Java SE 7 API Specification'
     -header '&lt;b&gt;Java(TM) SE 7&lt;/b&gt;'
     -bottom 'Copyright &amp;copy; 1993-2011 Oracle and/or its affiliates. All rights reserved.'
     -group &quot;Core Packages&quot; &quot;java.*&quot;
     -overview /java/pubs/ws/1.7.0/src/share/classes/overview-core.html
     -sourcepath /java/pubs/ws/1.7.0/src/share/classes</code>
</pre>
<p> Create a file named &quot;<i>packages</i>&quot; containing: </p>
<pre>
<code>     com.mypackage1
     com.mypackage2
     com.mypackage3</code>
</pre>
<p> You would then run javadoc with: </p>
<pre>
<code>  % </code><code>javadoc @options @packages</code>
</pre>
<h3>Example &#8211; Arg Files with Paths</h3>
<p> The argument files can have paths, but any filenames inside the files are relative to the current working directory (not <i>path1</i> or <i>path2</i>): </p>
<pre>
<code>  % </code><code>javadoc @path1/options @path2/packages</code>
</pre>
<h3>Example &#8211; Option Arguments</h3>
<p> Here&#8217;s an example of saving just an argument to a javadoc option in an argument file. We&#8217;ll use the <i>-bottom</i> option, since it can have a lengthy argument. You could create a file named &quot;<i>bottom</i>&quot; containing its text argument: </p>
<pre>
<code>&lt;font size=&quot;-1&quot;&gt;
      &lt;a href=&quot;<a rel="nofollow" href="http://bugreport.sun.com/bugreport/">http://bugreport.sun.com/bugreport/</a>&quot;&gt;Submit a bug or feature&lt;/a&gt;&lt;br/&gt;
      Copyright &amp;copy; 1993, 2011, Oracle and/or its affiliates. All rights reserved.&lt;br/&gt;
      Oracle is a registered trademark of Oracle Corporation and/or its affiliates.
      Other names may be trademarks of their respective owners.&lt;/font&gt;</code>
</pre>
<p> Then run the Javadoc tool with: </p>
<pre>
<code>  % </code><code>javadoc -bottom @bottom @packages</code>
</pre>
<p> Or you could include the <i>-bottom</i> option at the start of the argument file, and then just run it as: </p>
<pre>
<code>  % </code><code>javadoc @bottom @packages</code>
</pre>
<h2>Name</h2>
<p> Running</p>
<h2>RUNNING JAVADOC</h2>
<p> <code>Version Numbers</code> &#8211; The version number of javadoc can be determined using <code>javadoc -J-version</code>. The version number of the standard doclet appears in its output stream. It can be turned off with <i>-quiet</i>. </p>
<p> <code>Public programmatic interface</code> &#8211; To invoke the Javadoc tool from within programs written in the Java language. This interface is in <i>com.sun.tools.javadoc.Main</i> (and javadoc is re-entrant). For more details, see <i>Standard Doclet</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/technotes/guides/javadoc/standard-doclet.html#runningprogrammatically.">http://docs.oracle.com/javase/7/docs/technotes/guides/javadoc/standard-doclet.html#runningprogrammatically.</a> </p>
<p> <code>Running Doclets</code> &#8211; The instructions given below are for invoking the standard HTML doclet. To invoke a custom doclet, use the -doclet and -docletpath options. For full, working examples of running a particular doclet, see the <i>MIF Doclet documentation</i> @ <a rel="nofollow" href="http://java.sun.com/j2se/javadoc/mifdoclet/docs/mifdoclet.html.">http://java.sun.com/j2se/javadoc/mifdoclet/docs/mifdoclet.html.</a></p>
<h2>SIMPLE EXAMPLES</h2>
<p> You can run javadoc on entire packages or individual source files. Each package name has a corresponding directory name. In the following examples, the source files are located at <i>/home/src/java/awt/*.java</i>. The destination directory is <i>/home/html</i>.</p>
<h3>Documenting One or More Packages</h3>
<p> To document a package, the source files (<i>*.java</i>) for that package must be located in a directory having the same name as the package. If a package name is made up of several identifiers (separated by dots, such as <i>java.awt.color</i>), each subsequent identifier must correspond to a deeper subdirectory (such as <i>java/awt/color</i>). You may split the source files for a single package among two such directory trees located at different places, as long as <i>-sourcepath</i> points to them both &#8212; for example <i>src1/java/awt/color</i> and <i>src2/java/awt/color</i>. </p>
<p> You can run javadoc either by changing directories (with <i>cd</i>) or by using <i>-sourcepath</i> option. The examples below illustrate both alternatives.</p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> <code>Case 1 &#8211; Run recursively starting from one or more packages</code> &#8211; This example uses -sourcepath so javadoc can be run from any directory and -subpackages (a new 1.4 option) for recursion. It traverses the subpackages of the <i>java</i> directory excluding packages rooted at <i>java.net</i> and <i>java.lang</i>. Notice this excludes <i>java.lang.ref</i>, a subpackage of <i>java.lang</i>). </p>
<pre>
<code>  % </code><code>javadoc </code><code>-d</code><code> /home/html </code><code>-sourcepath</code><code> /home/src </code><code>-subpackages</code><code> java </code><code>-exclude</code><code> java.net:java.lang</code>
</pre>
</dl>
<p> To also traverse down other package trees, append their names to the <i>-subpackages</i> argument, such as <i>java:javax:org.xml.sax</i>.</p>
<dl>
<dt>o</p>
<dd> <code>Case 2 &#8211; Run on explicit packages after changing to the &quot;root&quot; source directory</code> &#8211; Change to the parent directory of the fully-qualified package. Then run javadoc, supplying names of one or more packages you want to document: </p>
<pre>
<code>  % </code><code>cd /home/src/</code>
  % <code>javadoc -d /home/html java.awt java.awt.event</code>
</pre>
<dt>o</p>
<dd> <code>Case 3 &#8211; Run from any directory on explicit packages in a single directory tree</code> &#8211; In this case, it doesn&#8217;t matter what the current directory is. Run javadoc supplying <i>-sourcepath</i> with the parent directory of the top-level package, and supplying names of one or more packages you want to document: </p>
<pre>
<code>  % </code><code>javadoc -d /home/html -sourcepath /home/src java.awt java.awt.event</code>
</pre>
<dt>o</p>
<dd> <code>Case 4 &#8211; Run from any directory on explicit packages in multiple directory trees</code> &#8211; This is the same as case 3, but for packages in separate directory trees. Run javadoc supplying <i>-sourcepath</i> with the path to each tree&#8217;s root (colon-separated) and supply names of one or more packages you want to document. All source files for a given package do not need to be located under a single root directory &#8212; they just need to be found somewhere along the sourcepath. </p>
<pre>
<code>  % </code><code>javadoc -d /home/html -sourcepath /home/src1:/home/src2 java.awt java.awt.event</code>
</pre>
</dl>
</dl>
<p> Result: All cases generate HTML-formatted documentation for the public and protected classes and interfaces in packages <i>java.awt</i> and <i>java.awt.event</i> and save the HTML files in the specified destination directory (<i>/home/html</i>). Because two or more packages are being generated, the document has three HTML frames &#8212; for the list of packages, the list of classes, and the main class pages.</p>
<h3>Documenting One or More Classes</h3>
<p> The second way to run the Javadoc tool is by passing in one or more source files (<i>.java</i>). You can run javadoc either of the following two ways &#8212; by changing directories (with <i>cd</i>) or by fully-specifying the path to the <i>.java</i> files. Relative paths are relative to the current directory. The <i>-sourcepath</i> option is ignored when passing in source files. You can use command line wildcards, such as asterisk (*), to specify groups of classes.</p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> <code>Case 1 &#8211; Changing to the source directory</code> &#8211; Change to the directory holding the <i>.java</i> files. Then run javadoc, supplying names of one or more source files you want to document. </p>
<pre>
<code>  % </code><code>cd /home/src/java/awt</code>
  % <code>javadoc -d /home/html Button.java Canvas.java Graphics*.java</code>
</pre>
<p> This example generates HTML-formatted documentation for the classes <i>Button</i>, <i>Canvas</i> and classes beginning with <i>Graphics</i>. Because source files rather than package names were passed in as arguments to javadoc, the document has two frames &#8212; for the list of classes and the main page.</p>
<dt>o</p>
<dd> <code>Case 2 &#8211; Changing to the package root directory</code> &#8211; This is useful for documenting individual source files from different subpackages off the same root. Change to the package root directory, and supply the source files with paths from the root. </p>
<pre>
<code>  % </code><code>cd /home/src/</code>
  % <code>javadoc -d /home/html java/awt/Button.java java/applet/Applet.java</code>
</pre>
<p> This example generates HTML-formatted documentation for the classes <i>Button</i> and <i>Applet</i>.</p>
<dt>o</p>
<dd> <code>Case 3 &#8211; From any directory</code> &#8211; In this case, it doesn&#8217;t matter what the current directory is. Run javadoc supplying the absolute path (or path relative to the current directory) to the <i>.java</i> files you want to document. </p>
<pre>
<code>  % </code><code>javadoc -d /home/html /home/src/java/awt/Button.java /home/src/java/awt/Graphics*.java</code>
</pre>
<p> This example generates HTML-formatted documentation for the class <i>Button</i> and classes beginning with <i>Graphics</i>.</dl>
</dl>
<h3>Documenting Both Packages and Classes</h3>
<p> You can document entire packages and individual classes at the same time. Here&#8217;s an example that mixes two of the previous examples. You can use <i>-sourcepath</i> for the path to the packages but not for the path to the individual classes. </p>
<pre>
<code>  % </code><code>javadoc -d /home/html -sourcepath /home/src java.awt /home/src/java/applet/Applet.java</code>
</pre>
<p> This example generates HTML-formatted documentation for the package <i>java.awt</i> and class <i>Applet</i>. (The Javadoc tool determines the package name for <i>Applet</i> from the package declaration, if any, in the <i>Applet.java</i> source file.)</p>
<h2>REAL WORLD EXAMPLE</h2>
<p> The Javadoc tool has many useful options, some of which are more commonly used than others. Here is effectively the command we use to run the Javadoc tool on the Java platform API. We use 180MB of memory to generate the documentation for the 1500 (approx.) public and protected classes in the Java SE Platform, Standard Edition, v1.2. </p>
<p> The same example is shown twice &#8212; first as executed on the command line, then as executed from a makefile. It uses absolute paths in the option arguments, which enables the same <i>javadoc</i> command to be run from any directory.</p>
<h3>Command Line Example</h3>
<p> The following example may be too long for some shells such as DOS. You can use a command line argument file (or write a shell script) to workaround this limitation. </p>
<pre>
<code>% javadoc -sourcepath /java/jdk/src/share/classes \ 
    -overview /java/jdk/src/share/classes/overview.html \ 
    -d /java/jdk/build/api \ 
    -use \ 
    -splitIndex \ 
    -windowtitle 'Java Platform, Standard Edition 7 API Specification' \ 
    -doctitle 'Java Platform, Standard Edition 7 API Specification' \ 
    -header '&lt;b&gt;Java(TM) SE 7&lt;/b&gt;' \ 
    -bottom '&lt;font size=&quot;-1&quot;&gt;
      &lt;a href=&quot;<a rel="nofollow" href="http://bugreport.sun.com/bugreport/">http://bugreport.sun.com/bugreport/</a>&quot;&gt;Submit a bug or feature&lt;/a&gt;&lt;br/&gt;
      Copyright &amp;copy; 1993, 2011, Oracle and/or its affiliates. All rights reserved.&lt;br/&gt;
      Oracle is a registered trademark of Oracle Corporation and/or its affiliates.
      Other names may be trademarks of their respective owners.&lt;/font&gt;' \ 
    -group &quot;Core Packages&quot; &quot;java.*:com.sun.java.*:org.omg.*&quot; \ 
    -group &quot;Extension Packages&quot; &quot;javax.*&quot; \ 
    -J-Xmx180m \  
    @packages</code>
</pre>
<p> where <i>packages</i> is the name of a file containing the packages to process, such as <i>java.applet java.lang</i>. None of the options should contain any newline characters between the single quotes. (For example, if you copy and paste this example, delete the newline characters from the <i>-bottom</i> option.) See the other notes listed below.</p>
<h3>Makefile Example</h3>
<p> This is an example of a GNU makefile. For an example of a Windows makefile, see <i>creating a makefile for Windows</i> @ <a rel="nofollow" href="http://java.sun.com/j2se/javadoc/faq/index.html#makefiles.">http://java.sun.com/j2se/javadoc/faq/index.html#makefiles.</a> </p>
<pre>
<code>javadoc -</code><code>sourcepath</code><code> $(SRCDIR)              \   /* Sets path for source files     */
        -</code><code>overview</code><code> $(SRCDIR)/overview.html  \   /* Sets file for overview text    */
        -</code><code>d</code><code> /java/jdk/build/api             \   /* Sets destination directory     */
        -</code><code>use</code><code>                               \   /* Adds &quot;Use&quot; files               */
        -</code><code>splitIndex</code><code>                        \   /* Splits index A-Z               */
        -</code><code>windowtitle</code><code> $(WINDOWTITLE)        \   /* Adds a window title            */
        -</code><code>doctitle</code><code> $(DOCTITLE)              \   /* Adds a doc title               */
        -</code><code>header</code><code> $(HEADER)                  \   /* Adds running header text       */
        -</code><code>bottom</code><code> $(BOTTOM)                  \   /* Adds text at bottom            */
        -</code><code>group</code><code> $(GROUPCORE)                \   /* 1st subhead on overview page   */
        -</code><code>group</code><code> $(GROUPEXT)                 \   /* 2nd subhead on overview page   */
        -</code><code>J</code><code>-Xmx180m                         \   /* Sets memory to 180MB           */
        java.lang java.lang.reflect        \   /* Sets packages to document      */
        java.util java.io java.net         \ 
        java.applet
        
WINDOWTITLE = 'Java(TM) SE 7 API Specification'
DOCTITLE = 'Java(TM) Platform Standard Edition 7 API Specification'
HEADER = '&lt;b&gt;Java(TM) SE 7&lt;/font&gt;'
BOTTOM = '&lt;font size=&quot;-1&quot;&gt;
      &lt;a href=&quot;<a rel="nofollow" href="http://bugreport.sun.com/bugreport/">http://bugreport.sun.com/bugreport/</a>&quot;&gt;Submit a bug or feature&lt;/a&gt;&lt;br/&gt;
      Copyright &amp;copy; 1993, 2011, Oracle and/or its affiliates. All rights reserved.&lt;br/&gt;
      Oracle is a registered trademark of Oracle Corporation and/or its affiliates.
      Other names may be trademarks of their respective owners.&lt;/font&gt;'
GROUPCORE = '&quot;Core Packages&quot; &quot;java.*:com.sun.java.*:org.omg.*&quot;'
GROUPEXT  = '&quot;Extension Packages&quot; &quot;javax.*&quot;'
SRCDIR = '/java/jdk/1.7.0/src/share/classes'</code>
</pre>
<p> Single quotes are used to surround makefile arguments. </p>
<p> <code>NOTES</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> If you omit the <i>-windowtitle</i> option, the Javadoc tool copies the doc title to the window title. The <i>-windowtitle</i> text is basically the same as the <i>-doctitle</i> but without HTML tags, to prevent those tags from appearing as raw text in the window title.</p>
<dt>o</p>
<dd> If you omit the <i>-footer</i> option, as done here, the Javadoc tool copies the header text to the footer.</p>
<dt>o</p>
<dd> Other important options you might want to use but not needed in this example are &#8211;<i>classpath</i> and &#8211;<i>link</i>.</dl>
</dl>
<h2>TROUBLESHOOTING</h2>
<h3>General Troubleshooting</h3>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> <code>Javadoc FAQ</code> &#8211; Commonly-encountered bugs and troubleshooting tips can be found on the <i>Javadoc FAQ</i> @ <a rel="nofollow" href="http://java.sun.com/j2se/javadoc/faq/index.html#B">http://java.sun.com/j2se/javadoc/faq/index.html#B</a></p>
<dt>o</p>
<dd> <code>Bugs and Limitations</code> &#8211; You can also see some bugs listed at Important Bug Fixes and Changes.</p>
<dt>o</p>
<dd> <code>Version number</code> &#8211; See version numbers.</p>
<dt>o</p>
<dd> <code>Documents only legal classes</code> &#8211; When documenting a package, javadoc only reads files whose names are composed of legal class names. You can prevent javadoc from parsing a file by including, for example, a hyphen &quot;-&quot; in its filename.</dl>
</dl>
<h3>Errors and Warnings</h3>
<p> Error and warning messages contain the filename and line number to the declaration line rather than to the particular line in the doc comment.</p>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> <i>&quot;error: cannot read: Class1.java&quot;</i> the Javadoc tool is trying to load the class Class1.java in the current directory. The class name is shown with its path (absolute or relative), which in this case is the same as <i>./Class1.java</i>.</dl>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>
<dd>
<dl>
<dt>CLASSPATH</p>
<dd> Environment variable that provides the path which javadoc uses to find user class files. This environment variable is overridden by the <i>-classpath</i> option. Separate directories with a colon, for example:</dl>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> <a href="/docs/linux/man/1-javac/">javac</a>(1)</p>
<dt>o</p>
<dd> <a href="/docs/linux/man/1-java/">java</a>(1)</p>
<dt>o</p>
<dd> <a href="/docs/linux/man/1-jdb/">jdb</a>(1)</p>
<dt>o</p>
<dd> <a href="/docs/linux/man/1-javah/">javah</a>(1)</p>
<dt>o</p>
<dd> <a href="/docs/linux/man/1-javap/">javap</a>(1)</p>
<dt>o</p>
<dd> <i>Javadoc Home Page</i> @ <a rel="nofollow" href="http://www.oracle.com/technetwork/java/javase/documentation/index-jsp-135444.html">http://www.oracle.com/technetwork/java/javase/documentation/index-jsp-135444.html</a></p>
<dt>o</p>
<dd> <i>How to Write Doc Comments for Javadoc</i> @ <a rel="nofollow" href="http://www.oracle.com/technetwork/java/javase/documentation/index-137868.html">http://www.oracle.com/technetwork/java/javase/documentation/index-137868.html</a></p>
<dt>o</p>
<dd> <i>Setting the Class Path</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/technotes/tools/index.html#general">http://docs.oracle.com/javase/7/docs/technotes/tools/index.html#general</a></p>
<dt>o</p>
<dd> <i>How Javac and Javadoc Find Classes</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/technotes/tools/findingclasses.html#srcfiles">http://docs.oracle.com/javase/7/docs/technotes/tools/findingclasses.html#srcfiles</a> (tools.jar)</dl>
</dl>
<p>&nbsp;<wbr> </p>
<h2>Index</h2>
