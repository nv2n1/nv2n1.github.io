---
title: "javac-java-1-6-0-openjdk(1)"
name: "javac-java-1-6-0-openjdk"
section: "1"
letter: "j"
url: "/docs/linux/man/1-javac-java-1-6-0-openjdk/"
description: "javac – Java programming language compiler"
---

<p>javac &#8211; Java programming language compiler</p>
<h2>Synopsis</h2>
<pre><code>javac</code> [ options ] [ sourcefiles ] [ @argfiles ]</pre>
<p>Arguments may be in any order. </p>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt>options</p>
<dd>Command-line options.</p>
<dt>sourcefiles</p>
<dd>One or more source files to be compiled (such as MyClass.java).</p>
<dt>@argfiles</p>
<dd>One or more files that lists options and source files. The <i>-J</i> options are not allowed in these files.</dl>
</dl>
</dl>
<h2>Description</h2>
<p>The <code>javac</code> tool reads class and interface definitions, written in the Java programming language, and compiles them into bytecode class files. </p>
<p> There are two ways to pass source code filenames to <code>javac</code>: </p>
<dl>
<dd>
<dl>
<dt>o</p>
<dd>For a small number of source files, simply list the file names on the command line.</p>
<dt>o</p>
<dd>For a large number of source files, list the file names in a file, separated by blanks or line breaks. Then use the list file name on the <code>javac</code> command line, preceded by an <code>@</code> character.</dl>
</dl>
<p> Source code file names must have <i>.java</i> suffixes, class file names must have <i>.class</i> suffixes, and both source and class files must have root names that identify the class. For example, a class called <i>MyClass</i> would be written in a source file called <i>MyClass.java</i> and compiled into a bytecode class file called <i>MyClass.class</i>. </p>
<p> Inner class definitions produce additional class files. These class files have names combining the inner and outer class names, such as <i>MyClass$MyInnerClass.class</i>. </p>
<p> You should arrange source files in a directory tree that reflects their package tree. For example, if you keep all your source files in <code>/workspace</code>, the source code for <i>com.mysoft.mypack.MyClass</i> should be in <code>/workspace/com/mysoft/mypack/MyClass.java</code>. </p>
<p> By default, the compiler puts each class file in the same directory as its source file. You can specify a separate destination directory with <code>-d</code> (see Options, below). </p>
<h2>Searching For Types</h2>
<p>When compiling a source file, the compiler often needs information about a type whose definition did not appear in the source files given on the command line. The compiler needs type information for every class or interface used, extended, or implemented in the source file. This includes classes and interfaces not explicitly mentioned in the source file but which provide information through inheritance. </p>
<p> For example, when you subclass <code>java.applet.Applet</code>, you are also using <code>Applet&#8217;s</code> ancestor classes: <code>java.awt.Panel</code>, <code>java.awt.Container</code>, <code>java.awt.Component</code>, and <code>java.lang.Object</code>. </p>
<p> When the compiler needs type information, it looks for a source file or class file which defines the type. The compiler searches for class files first in the bootstrap and extension classes, then in the user class path (which by default is the current directory). The user class path is defined by setting the <code>CLASSPATH</code> environment variable or by using the <code>-classpath</code> command line option. (For details, see Setting the Class Path). </p>
<p> If you set the -sourcepath option, the compiler searches the indicated path for source files; otherwise the compiler searches the user class path for both class files and source files. </p>
<p> You can specify different bootstrap or extension classes with the <code>-bootclasspath</code> and <code>-extdirs</code> options; see Cross-Compilation Options below. </p>
<p> A successful type search may produce a class file, a source file, or both. Here is how <code>javac</code> handles each situation: </p>
<dl>
<dd>
<dl>
<dt>o</p>
<dd><i>Search produces a class file but no source file:</i> <code>javac</code> uses the class file.</p>
<dt>o</p>
<dd><i>Search produces a source file but no class file:</i> <code>javac</code> compiles the source file and uses the resulting class file.</p>
<dt>o</p>
<dd><i>Search produces both a source file and a class file:</i> <code>javac</code> determines whether the class file is out of date. If the class file is out of date, <code>javac</code> recompiles the source file and uses the updated class file. Otherwise, <code>javac</code> just uses the class file.</dl>
<p> <code>javac</code> considers a class file out of date only if it is older than the source file.</dl>
<p> <code>Note:</code> &nbsp;<wbr> <code>javac</code> can silently compile source files not mentioned on the command line. Use the <code>-verbose</code> option to trace automatic compilation. </p>
<h2>Options</h2>
<p>The compiler has a set of standard options that are supported on the current development environment and will be supported in future releases. An additional set of non-standard options are specific to the current virtual machine and compiler implementations and are subject to change in the future. Non-standard options begin with <code>-X</code>. </p>
<h3>Standard Options</h3>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt>-classpath classpath</p>
<dd>Set the user class path, overriding the user class path in the <code>CLASSPATH</code> environment variable. If neither <code>CLASSPATH</code> or <code>-classpath</code> is specified, the user class path consists of the current directory. See Setting the Class Path for more details.</dl>
<p> If the <code>-sourcepath</code> option is not specified, the user class path is searched for both source files and class files. </p>
<p> As a special convenience, a class path element containing a basename of <i>*</i> is considered equivalent to specifying a list of all the files in the directory with the extension <i>.jar</i> or <i>.JAR</i> (a java program cannot tell the difference between the two invocations). </p>
<p> For example, if directory <i>foo</i> contains <i>a.jar</i> and <i>b.JAR</i>, then the class path element <i>foo/*</i> is expanded to a <i>A.jar:b.JAR</i>, except that the order of jar files is unspecified. All jar files in the specified directory, even hidden ones, are included in the list. A classpath entry consisting simply of <i>*</i> expands to a list of all the jar files in the current directory. The <i>CLASSPATH</i> environment variable, where defined, will be similarly expanded. Any classpath wildcard expansion occurs before the Java virtual machine is started &#8212; no Java program will ever see unexpanded wildcards except by querying the environment. For example; by invoking <i>System.getenv(&quot;CLASSPATH&quot;)</i>.</p>
<dl>
<dt>-Djava.ext.dirs=directories</p>
<dd>Override the location of installed extensions.</p>
<dt>-Djava.endorsed.dirs=directories</p>
<dd>Override the location of endorsed standards path.</p>
<dt>-d directory</p>
<dd>Set the destination directory for class files. The destination directory must already exist; javac will not create the destination directory. If a class is part of a package, <code>javac</code> puts the class file in a subdirectory reflecting the package name, creating directories as needed. For example, if you specify <code>-d /home/myclasses</code> and the class is called <i>com.mypackage.MyClass</i>, then the class file is called <i>/home/myclasses/com/mypackage/MyClass.class</i>.</dl>
<p> If <code>-d</code> is not specified, <code>javac</code> puts the class file in the same directory as the source file. </p>
<p> <code>Note:</code> &nbsp;<wbr> The directory specified by <code>-d</code> is not automatically added to your user class path.</p>
<dl>
<dt>-deprecation</p>
<dd>Show a description of each use or override of a deprecated member or class. Without <code>-deprecation</code>, <code>javac</code> shows the names of source files that use or override deprecated members or classes. <code>-deprecation</code> is shorthand for <code>-Xlint:deprecation</code>.</p>
<dt>-encoding encoding</p>
<dd>Set the source file encoding name, such as <i>EUC-JP and UTF-8.</i>. If <code>-encoding</code> is not specified, the platform default converter is used.</p>
<dt>-g</p>
<dd>Generate all debugging information, including local variables. By default, only line number and source file information is generated.</p>
<dt>-g:none</p>
<dd>Do not generate any debugging information.</p>
<dt>-g:{keyword list}</p>
<dd>Generate only some kinds of debugging information, specified by a comma separated list of keywords. Valid keywords are:</p>
<dl>
<dd>
<dl>
<dt>source</p>
<dd>Source file debugging information</p>
<dt>lines</p>
<dd>Line number debugging information</p>
<dt>vars</p>
<dd>Local variable debugging information</dl>
</dl>
<dt>-help</p>
<dd>Print a synopsis of standard options.</p>
<dt>-nowarn</p>
<dd>Disable warning messages. This has the same meaning as <code>-Xlint:none</code>.</dl>
<dl>
<dt>-source release</p>
<dd>Specifies the version of source code accepted. The following values for <i>release</i> are allowed:</p>
<dl>
<dd>
<dl>
<dt>1.3</p>
<dd>The compiler does <i>not</i> support assertions, generics, or other language features introduced after JDK 1.3.</p>
<dt>1.4</p>
<dd>The compiler accepts code containing assertions, which were introduced in JDK 1.4.</p>
<dt>1.5</p>
<dd>The compiler accepts code containing generics and other language features introduced in JDK 5. This is the default.</p>
<dt>5</p>
<dd>Synonym for 1.5</dl>
</dl>
<p> <code>Note:</code> No language changes were introduced in JDK 6, so the values <code>1.6</code> and <code>6</code> are not valid.</p>
<dt>-sourcepath sourcepath</p>
<dd>Specify the source code path to search for class or interface definitions. As with the user class path, source path entries are separated by colons (<code>:</code>) and can be directories, JAR archives, or ZIP archives. If packages are used, the local path name within the directory or archive must reflect the package name.</dl>
<p> <code>Note:</code> &nbsp;<wbr> Classes found through the classpath are subject to automatic recompilation if their sources are found.</p>
<dl>
<dt>-verbose</p>
<dd>Verbose output. This includes information about each class loaded and each source file compiled.</p>
<dt>-X</p>
<dd>Display information about non-standard options and exit.</dl>
</dl>
</dl>
<h3>Cross-Compilation Options</h3>
<dl>
<dd>By default, classes are compiled against the bootstrap and extension classes of the platform that <code>javac</code> shipped with. But <code>javac</code> also supports <i>cross-compiling</i>, where classes are compiled against a bootstrap and extension classes of a different Java platform implementation. It is important to use <code>-bootclasspath</code> and <code>-extdirs</code> when cross-compiling; see Cross-Compilation Example below. </p>
<dl>
<dd>
<dl>
<dt>-target version</p>
<dd>Generate class files that target a specified version of the VM. Class files will run on the specified target and on later versions, but not on earlier versions of the VM. Valid targets are <code>1.1</code> <code>1.2</code> <code>1.3</code> <code>1.4</code> <code>1.5</code> (also <code>5</code>) and <code>1.6</code> (also <code>6</code>).</dl>
<p> The default for <code>-target</code> depends on the value of <code>-source</code>:</p>
<dl>
<dd>
<dl>
<dt>o</p>
<dd>If -source is <code>not specified</code>, the value of -target is <code>1.6</code></p>
<dt>o</p>
<dd>If -source is <code>1.3</code>, the value of -target is <code>1.1</code></p>
<dt>o</p>
<dd>For <code>all other values</code> of -source, the value of -target is the value of <code>-source</code>.</dl>
</dl>
<dl>
<dt>-bootclasspath bootclasspath</p>
<dd>Cross-compile against the specified set of boot classes. As with the user class path, boot class path entries are separated by colons (<code>:</code>) and can be directories, JAR archives, or ZIP archives.</p>
<dt>-extdirs directories</p>
<dd>Cross-compile against the specified extension directories. <i>Directories</i> is a colon-separated list of directories. Each JAR archive in the specified directories is searched for class files.</dl>
</dl>
</dl>
<h3>Non-Standard Options</h3>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt>-Xbootclasspath/p:path</p>
<dd>Prepend to the bootstrap class path.</p>
<dt>-Xbootclasspath/a:path</p>
<dd>Append to the bootstrap class path.</p>
<dt>-Xbootclasspath/:path</p>
<dd>Override location of bootstrap class files.</p>
<dt>-Xlint</p>
<dd>Enable all recommended warnings. In this release, all available warnings are recommended.</p>
<dt>-Xlint:none</p>
<dd>Disable all warnings not mandated by the Java Language Specification.</p>
<dt>-Xlint:-xxx</p>
<dd>Disable warning <code>xxx</code>, where <code>xxx</code> is one of the warning names supported for <code>-Xlint:xxx</code>, below</p>
<dt>-Xlint:unchecked</p>
<dd>Give more detail for unchecked conversion warnings that are mandated by the Java Language Specification.</p>
<dt>-Xlint:path</p>
<dd>Warn about nonexistent path (classpath, sourcepath, etc) directories.</p>
<dt>-Xlint:serial</p>
<dd>Warn about missing <i>serialVersionUID</i> definitions on serializable classes.</p>
<dt>-Xlint:finally</p>
<dd>Warn about <i>finally</i> clauses that cannot complete normally.</p>
<dt>-Xlint:fallthrough</p>
<dd>Check <i>switch</i> blocks for fall-through cases and provide a warning message for any that are found. Fall-through cases are cases in a <i>switch</i> block, other than the last case in the block, whose code does not include a <i>break</i> statement, allowing code execution to &quot;fall through&quot; from that case to the next case. For example, the code following the <i>case 1</i> label in this <i>switch</i> block does not contain a <i>break</i> statement:</p>
<dl>
<dd>
<pre><code>switch (x) {
case 1:
 System.out.println(&quot;1&quot;);
 // No break; statement here.
case 2:
 System.out.println(&quot;2&quot;);
}</code></pre>
</dl>
<p> If the <i>-Xlint:fallthrough</i> flag were used when compiling this code, the compiler would emit a warning about &quot;possible fall-through into case,&quot; along with the line number of the case in question.</p>
<dt>-Xmaxerrors number</p>
<dd>Set the maximum number of errors to print.</p>
<dt>-Xmaxwarns number</p>
<dd>Set the maximum number of warnings to print.</p>
<dt>-Xstdout filename</p>
<dd>Send compiler messages to the named file. By default, compiler messages go to <i>System.err</i>.</dl>
</dl>
</dl>
<h3>The -J Option</h3>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt>-Joption</p>
<dd>Pass <i>option</i> to the <code>java</code> launcher called by <code>javac</code>. For example, <code>-J-Xms48m</code> sets the startup memory to 48 megabytes. Although it does not begin with <code>-X</code>, it is not a `standard option&#8217; of <code>javac</code>. It is a common convention for <code>-J</code> to pass options to the underlying VM executing applications written in Java.</dl>
<p> <code>Note:</code> &nbsp;<wbr> <code>CLASSPATH</code>, <code>-classpath</code>, <code>-bootclasspath</code>, and <code>-extdirs</code> do <i>not</i> specify the classes used to run <code>javac</code>. Fiddling with the implementation of the compiler in this way is usually pointless and always risky. If you do need to do this, use the <code>-J</code> option to pass through options to the underlying <code>java</code> launcher.</dl>
</dl>
<h2>Command Line Argument Files</h2>
<p>To shorten or simplify the javac command line, you can specify one or more files that themselves contain arguments to the <i>javac</i> command (except <i>-J</i> options). This enables you to create javac commands of any length on any operating system. </p>
<p> An argument file can include javac options and source filenames in any combination. The arguments within a file can be space-separated or newline-separated. If a filename contains embedded spaces, put the whole filename in double quotes. </p>
<p> Filenames within an argument file are relative to the current directory, not the location of the argument file. Wildcards (*) are not allowed in these lists (such as for specifying <i>*.java</i>). Use of the &#8216;<i>@</i>&#8216; character to recursively interpret files is not supported. The <i>-J</i> options are not supported because they are passed to the launcher, which does not support argument files. </p>
<p> When executing javac, pass in the path and name of each argument file with the &#8216;<i>@</i>&#8216; leading character. When javac encounters an argument beginning with the character `<i>@</i>&#8216;, it expands the contents of that file into the argument list. </p>
<h3>Example &#8211; Single Arg File</h3>
<p>You could use a single argument file named &quot;<i>argfile</i>&quot; to hold all javac arguments: </p>
<pre><code> C:&gt; </code><code>javac @argfile</code></pre>
<p>This argument file could contain the contents of both files shown in the next example. </p>
<h3>Example &#8211; Two Arg Files</h3>
<p>You can create two argument files &#8212; one for the javac options and the other for the source filenames: (Notice the following lists have no line-continuation characters.) </p>
<p> Create a file named &quot;<i>options</i>&quot; containing: </p>
<pre><code> -d classes
 -g
 -sourcepath \java\pubs\ws\1.3\src\share
