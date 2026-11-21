---

title: "apt-java-1(1)"
name: "apt-java-1"
section: "1"
letter: "a"
url: "/docs/linux/man/1-apt-java-1/"
description: "apt – annotation processing tool"
---

<p> <i>apt</i> &#8211; annotation processing tool</p>
<h2>SYNOPSIS</h2>
<p> <i>apt [-classpath </i><i>classpath</i>] [-sourcepath <i>sourcepath</i>] [-d <i>directory</i>] [-s <i>directory</i>] [-factorypath <i>path</i>] [-factory <i>class</i>] [-print] [-nocompile] [-A<i>key</i>[<i>=val</i>] &#8230;] [<i>javac option</i>] sourcefiles [@files] </p>
<h2>PARAMETERS</h2>
<p> Options may be in any order. For a discussion of parameters which apply to a specific option, see OPTIONS below. </p>
<dl>
<dl>
<dt>sourcefiles</dt>
<dd> Zero or more source files to be processed.</dd>
<dt>@files</dt>
<dd> One or more files that list source files or other options</dd></dl>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>Note</code>: The <i>apt</i> tool and its associated API contained in the package <i>com.sun.mirror</i> have been deprecated since JDK 7 and are planned to be removed in the next major JDK release. Use the options available in the <i><a href="/docs/linux/man/1-javac/">javac</a>(1)</i> tool and the APIs contained in the packages <i>javax.annotation.processing</i> and <i>javax.lang.model</i> to process annotations. </p>
<p> The tool <i>apt</i>, annotation processing tool, includes reflective APIs and supporting infrastructure to process program annotations. The <i>apt</i> reflective APIs provide a build-time, source-based, read-only view of program structure. These reflective APIs are designed to cleanly model the Java(TM) programming language&#8217;s type system after the addition of generics. First, <i>apt</i> runs annotation processors that can produce new source code and other files. Next, <i>apt</i> can cause compilation of both original and generated source files, easing development. The reflective APIs and other APIs used to interact with the tool are subpackages of <i>com.sun.mirror</i>. </p>
<p> A fuller discussion of how the tool operates as well as instructions for developing with <i>apt</i> are in <tt>Getting Started with </tt><tt>apt</tt>. @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/technotes/guides/apt/GettingStarted.html">http://docs.oracle.com/javase/7/docs/technotes/guides/apt/GettingStarted.html</a> </p>
<h2>OPTIONS</h2>
<h3>apt specific options</h3>
<dl>
<dl>
<dt>-s dir</dt>
<dd> Specify the directory root under which processor-generated source files will be placed; files are placed in subdirectories based on package namespace.</dd>
<dt>-nocompile</dt>
<dd> Do not compile source files to class files.</dd>
<dt>-print</dt>
<dd> Print out textual representation of specified types; perform no annotation processing or compilation.</dd>
<dt>-A[key[=val]]</dt>
<dd> Options to pass to annotation processors &#8212; these are not interpreted by <i>apt</i> directly, but are made available for use by individual processors</dd>
<dt>-factorypath path</dt>
<dd> Specify where to find annotation processor factories; if this option is used, the classpath is <i>not</i> searched for factories.</dd>
<dt>-factory classname</dt>
<dd> Name of annotation processor factory to use; bypasses default discovery process</dd>
<dt>-version</dt>
<dd> Print version information.</dd>
<dt>-X</dt>
<dd> Display information about non-standard options.</dd></dl>
</dl>
<h3>Options shared with javac</h3>
<dl>
<dl>
<dt>-d dir</dt>
<dd> Specify where to place processor and javac generated class files</dd>
<dt>-cp path or -classpath path</dt>
<dd> Specify where to find user class files and annotation processor factories. If <i>-factorypath</i> is given, the classpath is not searched for factories.</dd></dl>
</dl>
<p> Consult the <a href="/docs/linux/man/1-javac/">javac</a>(1) man page for information on <i>javac</i> options. </p>
<h3>Non-Standard Options</h3>
<dl>
<dl>
<dt>-XListAnnotationTypes</dt>
<dd> List found annotation types.</dd>
<dt>-XListDeclarations</dt>
<dd> List specified and included declarations.</dd>
<dt>-XPrintAptRounds</dt>
<dd> Print information about initial and recursive <i>apt</i> rounds.</dd>
<dt>-XPrintFactoryInfo</dt>
<dd> Print information about which annotations a factory is asked to process.</dd>
<dt>-XclassesAsDecls</dt>
<dd> Treat both class and source files as declarations to process.</dd></dl>
</dl>
<p> <code>Note</code>: Because these options are non-standard, they are subject to change without notice. </p>
<h2>NOTES</h2>
<p> The <i>apt</i> tool and its associated API contained in the package <i>com.sun.mirror</i> have been deprecated since JDK 7 and are planned to be removed in the next major JDK release. Use the options available in the <i><a href="/docs/linux/man/1-javac/">javac</a>(1)</i> tool and the APIs contained in the packages <i>javax.annotation.processing</i> and <i>javax.lang.model</i> to process annotations. </p>
<h2>SEE ALSO</h2>
<dl>
<dl>
<dt>o</dt>
<dd> <a href="/docs/linux/man/1-javac/">javac</a>(1), <a href="/docs/linux/man/1-java/">java</a>(1)</dd></dl>
</dl>
<p>&nbsp;<wbr> </p>
