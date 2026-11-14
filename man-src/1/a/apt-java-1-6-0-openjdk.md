---
title: "apt-java-1-6-0-openjdk(1)"
name: "apt-java-1-6-0-openjdk"
section: "1"
letter: "a"
url: "/docs/linux/man/1-apt-java-1-6-0-openjdk/"
---

<i>apt</i> - annotation processing tool
<h2>Synopsis</h2><i>apt [-classpath </i><i>classpath</i>] [-sourcepath <i>sourcepath</i>] [-d <i>directory</i>] [-s <i>directory</i>] [-factorypath <i>path</i>] [-factory <i>class</i>] [-print] [-nocompile] [-A<i>key</i>[<i>=val</i>] ...] [<i>javac option</i>] sourcefiles [@files] 

<h2>Parameters</h2>Options may be in any order. For a discussion of parameters which apply to a specific option, see OPTIONS below. 

<dl><dt>sourcefiles
<dd>Zero or more source files to be processed.
<dt>@files
<dd>One or more files that list source files or other options</dl><h2>Description</h2>The tool <i>apt</i>, annotation processing tool, includes a set of new reflective APIs and supporting infrastructure to process program annotations. The <i>apt</i> reflective APIs provide a build-time, source-based, read-only view of program structure. These reflective APIs are designed to cleanly model the Java(TM) programming language's type system after the addition of generics. First, <i>apt</i> runs annotation processors that can produce new source code and other files. Next, <i>apt</i> can cause compilation of both original and generated source files, easing development. The reflective APIs and other APIs used to interact with the tool are subpackages of <i>com.sun.mirror</i>. 

 

 A fuller discussion of how the tool operates as well as instructions for developing with <i>apt</i> are in <tt>Getting Started with </tt><tt>apt</tt>. @ <a rel="nofollow" HREF="http://java.sun.com/javase/6/docs/technotes/guides/apt/GettingStarted.html">http://java.sun.com/javase/6/docs/technotes/guides/apt/GettingStarted.html</a> 

<dl><dt>Note:
<dd><i>The functionality of </i><i>apt</i> has been subsumed by the annotation-processing infrastructure that is now part of the <i>javac</i> tool [ <i>Solaris and Linux</i> @ <a rel="nofollow" HREF="http://java.sun.com/javase/6/docs/technotes/tools/solaris/javac.html]">http://java.sun.com/javase/6/docs/technotes/tools/solaris/javac.html]</a> [Windows] and standardized for use by all Java compilers. This new infrastructure relies on the language model and annotation-processing APIs that are now part of the Java Platform. It is recommended that new annotation processor development be based on the new APIs and the <i>javac</i> tool.</dl><h2>Options</h2><h3>apt specific options</h3><dl><dt>-s dir
<dd>Specify the directory root under which processor-generated source files will be placed; files are placed in subdirectories based on package namespace.
<dt>-nocompile
<dd>Do not compile source files to class files.
<dt>-print
<dd>Print out textual representation of specified types; perform no annotation processing or compilation.
<dt>-A[key[=val]]
<dd>Options to pass to annotation processors -- these are not interpreted by <i>apt</i> directly, but are made available for use by individual processors
<dt>-factorypath path
<dd>Specify where to find annotation processor factories; if this option is used, the classpath is <i>not</i> searched for factories.
<dt>-factory classname
<dd>Name of annotation processor factory to use; bypasses default discovery process</dl><h3>Options shared with javac</h3><dl><dt>-d dir
<dd>Specify where to place processor and javac generated class files
<dt>-cp path or -classpath
<dd>path Specify where to find user class files and annotation processor factories. If <i>-factorypath</i> is given, the classpath is not searched for factories.</dl>
 

 

 Consult the <a HREF="/docs/linux/man/1-javac/">javac</a>(1) man page for information on <i>javac</i> options. 

<h2>Notes</h2>The functionality of <i>apt</i> has been subsumed by the standard annotation-processing infrastructure now offered by <i>javac</i>. Support for <i>apt</i> and its associated APIs may be discontinued in some future JDK release. 

<h2>See Also</h2><dl><dd><dl><dt>*
<dd>javac: [ <i>Solaris and Linux</i> @ <a rel="nofollow" HREF="http://java.sun.com/javase/6/docs/technotes/tools/solaris/javac.html]">http://java.sun.com/javase/6/docs/technotes/tools/solaris/javac.html]</a> [Windows]
<dt>*
<dd>java: [ <i>Solaris</i> @ <a rel="nofollow" HREF="http://java.sun.com/javase/6/docs/technotes/tools/solaris/java.html]">http://java.sun.com/javase/6/docs/technotes/tools/solaris/java.html]</a> [ <i>Linux</i> @ <a rel="nofollow" HREF="http://java.sun.com/javase/6/docs/technotes/tools/linux/java.html]">http://java.sun.com/javase/6/docs/technotes/tools/linux/java.html]</a> [Windows]</dl></dl>
 

 

 
&nbsp;<wbr>
