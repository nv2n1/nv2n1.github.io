---
title: "javac(1)"
name: "javac"
section: "1"
letter: "j"
url: "/docs/linux/man/1-javac/"
description: "javac – Reads Java class and interface definitions and compiles them into bytecode and class files."
---

<h2>NAME</h2>
<p> javac &#8211; Reads Java class and interface definitions and compiles them into bytecode and class files.</p>
<h2>SYNOPSIS</h2>
<pre><code>
javac[options][sourcefiles][classes][@argfiles]
</code></pre>
<p> Arguments can be in any order:</p>
<dl>
<dt><i>options</i></p>
<dd> Command-line options. See Options.</p>
<dt><i>sourcefiles</i></p>
<dd> One or more source files to be compiled (such as <code>MyClass.java</code>).</p>
<dt><i>classes</i></p>
<dd> One or more classes to be processed for annotations (such as <code>MyPackage.MyClass</code>).</p>
<dt><i>@argfiles</i></p>
<dd> One or more files that list options and source files. The <code>-J</code> options are not allowed in these files. See Command-Line Argument Files.</dl>
<h2>DESCRIPTION</h2>
<p> The <code>javac</code> command reads class and interface definitions, written in the Java programming language, and compiles them into bytecode class files. The <code>javac</code> command can also process annotations in Java source files and classes. </p>
<p> There are two ways to pass source code file names to <code>javac</code>.</p>
<dl>
<dt>&bull;</p>
<dd> For a small number of source files, list the file names on the command line.</p>
<dt>&bull;</p>
<dd> For a large number of source files, list the file names in a file that is separated by blanks or line breaks. Use the list file name preceded by an at sign (@) with the <code>javac</code> command.</dl>
<p> Source code file names must have .java suffixes, class file names must have .class suffixes, and both source and class files must have root names that identify the class. For example, a class called <code>MyClass</code> would be written in a source file called <code>MyClass.java</code> and compiled into a bytecode class file called <code>MyClass.class</code>. </p>
<p> Inner class definitions produce additional class files. These class files have names that combine the inner and outer class names, such as <code>MyClass$MyInnerClass.class</code>. </p>
<p> Arrange source files in a directory tree that reflects their package tree. For example, if all of your source files are in <code>/workspace</code>, then put the source code for <code>com.mysoft.mypack.MyClass</code> in <code>/workspace/com/mysoft/mypack/MyClass.java</code>. </p>
<p> By default, the compiler puts each class file in the same directory as its source file. You can specify a separate destination directory with the <code>-d</code> option.</p>
<h2>OPTIONS</h2>
<p> The compiler has a set of standard options that are supported on the current development environment. An additional set of nonstandard options are specific to the current virtual machine and compiler implementations and are subject to change in the future. Nonstandard options begin with the <code>-X</code> option.</p>
<dl>
<dt>&bull;</p>
<dd> See also Cross-Compilation Options</p>
<dt>&bull;</p>
<dd> See also Nonstandard Options</dl>
<h3>STANDARD OPTIONS</h3>
<dl>
<dt>-A<i>key</i>[<i>=value</i>]</p>
<dd>
 Specifies options to pass to annotation processors. These options are not interpreted by <code>javac</code> directly, but are made available for use by individual processors. The <code>key</code> value should be one or more identifiers separated by a dot (.).</p>
<dt>-cp <i>path</i> or -classpath <i>path</i></p>
<dd>
 Specifies where to find user class files, and (optionally) annotation processors and source files. This class path overrides the user class path in the <code>CLASSPATH</code> environment variable. If neither <code>CLASSPATH</code>, <code>-cp</code> nor <code>-classpath</code> is specified, then the user <i>class path</i> is the current directory. See Setting the Class Path. </p>
<p> If the <code>-sourcepath</code> option is not specified, then the user class path is also searched for source files. </p>
<p> If the <code>-processorpath</code> option is not specified, then the class path is also searched for annotation processors.</p>
<dt>-Djava.ext.dirs=<i>directories</i></p>
<dd>
 Overrides the location of installed extensions.</p>
<dt>-Djava.endorsed.dirs=<i>directories</i></p>
<dd>
 Overrides the location of the endorsed standards path.</p>
<dt>-d <i>directory</i></p>
<dd>
 Sets the destination directory for class files. The directory must already exist because <code>javac</code> does not create it. If a class is part of a package, then <code>javac</code> puts the class file in a subdirectory that reflects the package name and creates directories as needed. </p>
<p> If you specify <code>-d</code><code>/home/myclasses</code> and the class is called <code>com.mypackage.MyClass</code>, then the class file is <code>/home/myclasses/com/mypackage/MyClass.class</code>. </p>
<p> If the <i>-d</i> option is not specified, then <code>javac</code> puts each class file in the same directory as the source file from which it was generated. </p>
<p> <i>Note:</i> The directory specified by the <i>-d</i> option is not automatically added to your user class path.</p>
<dt>-deprecation</p>
<dd>
 Shows a description of each use or override of a deprecated member or class. Without the <code>-deprecation</code> option, <code>javac</code> shows a summary of the source files that use or override deprecated members or classes. The <code>-deprecation</code> option is shorthand for <code>-Xlint:deprecation</code>.</p>
<dt>-encoding <i>encoding</i></p>
<dd>
 Sets the source file encoding name, such as EUC-JP and UTF-8. If the <code>-encoding</code> option is not specified, then the platform default converter is used.</p>
<dt>-endorseddirs <i>directories</i></p>
<dd>
 Overrides the location of the endorsed standards path.</p>
<dt>-extdirs <i>directories</i></p>
<dd>
 Overrides the location of the <code>ext</code> directory. The directories variable is a colon-separated list of directories. Each JAR file in the specified directories is searched for class files. All JAR files found become part of the class path. </p>
<p> If you are cross-compiling (compiling classes against bootstrap and extension classes of a different Java platform implementation), then this option specifies the directories that contain the extension classes. See Cross-Compilation Options for more information.</p>
<dt>-g</p>
<dd>
 Generates all debugging information, including local variables. By default, only line number and source file information is generated.</p>
<dt>-g:none</p>
<dd>
 Does not generate any debugging information.</p>
<dt>-g:[<i>keyword list</i>]</p>
<dd>
 Generates only some kinds of debugging information, specified by a comma separated list of keywords. Valid keywords are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>source</p>
<dd> Source file debugging information.</p>
<dt>lines</p>
<dd> Line number debugging information.</p>
<dt>vars</p>
<dd> Local variable debugging information.</dl>
</dl>
<dt>-help</p>
<dd>
 Prints a synopsis of standard options.</p>
<dt>-implicit:[<i>class, none</i>]</p>
<dd>
 Controls the generation of class files for implicitly loaded source files. To automatically generate class files, use <code>-implicit:class</code>. To suppress class file generation, use <code>-implicit:none</code>. If this option is not specified, then the default is to automatically generate class files. In this case, the compiler issues a warning if any such class files are generated when also doing annotation processing. The warning is not issued when the <code>-implicit</code> option is set explicitly. See Searching for Types.</p>
<dt>-J<i>option</i></p>
<dd>
 Passes <code>option</code> to the Java Virtual Machine (JVM), where option is one of the options described on the reference page for the Java launcher. For example, <code>-J-Xms48m</code> sets the startup memory to 48 MB. See <a href="/docs/linux/man/1-java/">java</a>(1). </p>
<p> <i>Note:</i> The <i>CLASSPATH</i>, <code>-classpath</code>, <code>-bootclasspath</code>, and <code>-extdirs</code> options do not specify the classes used to run <code>javac</code>. Trying to customize the compiler implementation with these options and variables is risky and often does not accomplish what you want. If you must customize the complier implementation, then use the <code>-J</code> option to pass options through to the underlying Java launcher.</p>
<dt>-nowarn</p>
<dd>
 Disables warning messages. This option operates the same as the <code>-Xlint:none</code> option.</p>
<dt>-parameters</p>
<dd>
 Stores formal parameter names of constructors and methods in the generated class file so that the method <code>java.lang.reflect.Executable.getParameters</code> from the Reflection API can retrieve them.</p>
<dt>-proc: [<i>none</i>, <i>only</i>]</p>
<dd>
 Controls whether annotation processing and compilation are done. <code>-proc:none</code> means that compilation takes place without annotation processing. <code>-proc:only</code> means that only annotation processing is done, without any subsequent compilation.</p>
<dt>-processor <i>class1</i> [,<i>class2</i>,<i>class3</i>&#8230;]</p>
<dd>
 Names of the annotation processors to run. This bypasses the default discovery process.</p>
<dt>-processorpath <i>path</i></p>
<dd>
 Specifies where to find annotation processors. If this option is not used, then the class path is searched for processors.</p>
<dt>-s <i>dir</i></p>
<dd>
 Specifies the directory where to place the generated source files. The directory must already exist because <code>javac</code> does not create it. If a class is part of a package, then the compiler puts the source file in a subdirectory that reflects the package name and creates directories as needed. </p>
<p> If you specify <code>-s /home/mysrc</code> and the class is called <code>com.mypackage.MyClass</code>, then the source file is put in <code>/home/mysrc/com/mypackage/MyClass.java</code>.</p>
<dt>-source <i>release</i></p>
<dd>
 Specifies the version of source code accepted. The following values for <code>release</code> are allowed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1.3</p>
<dd> The compiler does not support assertions, generics, or other language features introduced after Java SE 1.3.</p>
<dt>1.4</p>
<dd> The compiler accepts code containing assertions, which were introduced in Java SE 1.4.</p>
<dt>1.5</p>
<dd> The compiler accepts code containing generics and other language features introduced in Java SE 5.</p>
<dt>5</p>
<dd> Synonym for 1.5.</p>
<dt>1.6</p>
<dd> No language changes were introduced in Java SE 6. However, encoding errors in source files are now reported as errors instead of warnings as in earlier releases of Java Platform, Standard Edition.</p>
<dt>6</p>
<dd> Synonym for 1.6.</p>
<dt>1.7</p>
<dd> The compiler accepts code with features introduced in Java SE 7.</p>
<dt>7</p>
<dd> Synonym for 1.7.</p>
<dt>1.8</p>
<dd> This is the default value. The compiler accepts code with features introduced in Java SE 8.</p>
<dt>8</p>
<dd> Synonym for 1.8.</dl>
</dl>
<dt>-sourcepath <i>sourcepath</i></p>
<dd>
 Specifies the source code path to search for class or interface definitions. As with the user class path, source path entries are separated by colons (:) on Oracle Solaris and semicolons on Windows and can be directories, JAR archives, or ZIP archives. If packages are used, then the local path name within the directory or archive must reflect the package name. </p>
<p> <i>Note:</i> Classes found through the class path might be recompiled when their source files are also found. See Searching for Types.</p>
<dt>-verbose</p>
<dd>
 Uses verbose output, which includes information about each class loaded and each source file compiled.</p>
<dt>-version</p>
<dd>
 Prints release information.</p>
<dt>-werror</p>
<dd>
 Terminates compilation when warnings occur.</p>
<dt>-X</p>
<dd>
 Displays information about nonstandard options and exits.</dl>
<h3>CROSS-COMPILATION OPTIONS</h3>
<p> By default, classes are compiled against the bootstrap and extension classes of the platform that <code>javac</code> shipped with. But <code>javac</code> also supports cross-compiling, where classes are compiled against a bootstrap and extension classes of a different Java platform implementation. It is important to use the <code>-bootclasspath</code> and <code>-extdirs</code> options when cross-compiling.</p>
<dl>
<dt>-target <i>version</i></p>
<dd>
 Generates class files that target a specified release of the virtual machine. Class files will run on the specified target and on later releases, but not on earlier releases of the JVM. Valid targets are 1.1, 1.2, 1.3, 1.4, 1.5 (also 5), 1.6 (also 6), 1.7 (also 7), and 1.8 (also 8). </p>
<p> The default for the <code>-target</code> option depends on the value of the <code>-source</code> option:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> If the <code>-source</code> option is not specified, then the value of the <code>-target</code> option is 1.8</p>
<dt>&bull;</p>
<dd> If the <code>-source</code> option is 1.2, then the value of the <code>-target</code> option is 1.4</p>
<dt>&bull;</p>
<dd> If the <code>-source</code> option is 1.3, then the value of the <code>-target</code> option is 1.4</p>
<dt>&bull;</p>
<dd> If the <code>-source</code> option is 1.5, then the value of the <code>-target</code> option is 1.8</p>
<dt>&bull;</p>
<dd> If the <code>-source</code> option is 1.6, then the value of the <code>-target</code> is option 1.8</p>
<dt>&bull;</p>
<dd> If the <code>-source</code> option is 1.7, then the value of the <code>-target</code> is option 1.8</p>
<dt>&bull;</p>
<dd> For all other values of the <code>-source</code> option, the value of the <code>-target</code> option is the value of the <code>-source</code> option.</dl>
</dl>
<dt>-bootclasspath <i>bootclasspath</i></p>
<dd>
 Cross-compiles against the specified set of boot classes. As with the user class path, boot class path entries are separated by colons (:) and can be directories, JAR archives, or ZIP archives.</dl>
<h3>COMPACT PROFILE OPTION</h3>
<p> Beginning with JDK 8, the <code>javac</code> compiler supports compact profiles. With compact profiles, applications that do not require the entire Java platform can be deployed and run with a smaller footprint. The compact profiles feature could be used to shorten the download time for applications from app stores. This feature makes for more compact deployment of Java applications that bundle the JRE. This feature is also useful in small devices. </p>
<p> The supported profile values are <code>compact1</code>, <code>compact2</code>, and <code>compact3</code>. These are additive layers. Each higher-numbered compact profile contains all of the APIs in profiles with smaller number names.</p>
<dl>
<dt>-profile</p>
<dd>
 When using compact profiles, this option specifies the profile name when compiling. For example: </p>
<pre>
<code>javac -profile compact1 Hello.java</code>
</pre>
<pre>
</pre>
<p> javac does not compile source code that uses any Java SE APIs that is not in the specified profile. Here is an example of the error message that results from attempting to compile such source code: </p>
<pre>
<code>cd jdk1.8.0/bin</code>
</pre>
<pre>
<code>./javac -profile compact1 Paint.java</code>
</pre>
<pre>
<code>Paint.java:5: error: Applet is not available in profile 'compact1'</code>
</pre>
<pre>
<code>import java.applet.Applet;</code>
</pre>
<pre>
</pre>
<p> In this example, you can correct the error by modifying the source to not use the <code>Applet</code> class. You could also correct the error by compiling without the -profile option. Then the compilation would be run against the full set of Java SE APIs. (None of the compact profiles include the <code>Applet</code> class.) </p>
<p> An alternative way to compile with compact profiles is to use the <code>-bootclasspath</code> option to specify a path to an <code>rt.jar</code> file that specifies a profile&#8217;s image. Using the <code>-profile</code> option instead does not require a profile image to be present on the system at compile time. This is useful when cross-compiling.</dl>
<h3>NONSTANDARD OPTIONS</h3>
<dl>
<dt>-Xbootclasspath/p:<i>path</i></p>
<dd>
 Adds a suffix to the bootstrap class path.</p>
<dt>-Xbootclasspath/a:<i>path</i></p>
<dd>
 Adds a prefix to the bootstrap class path.</p>
<dt>-Xbootclasspath/:<i>path</i></p>
<dd>
 Overrides the location of the bootstrap class files.</p>
<dt>-Xdoclint:[-]<i>group</i> [<i>/access</i>]</p>
<dd>
 Enables or disables specific groups of checks, where <i>group</i> is one of the following values: <code>accessibility</code>, <code>syntax</code>, <code>reference</code>, <code>html</code> or <code>missing</code>. For more information about these groups of checks see the <code>-Xdoclint</code> option of the <code>javadoc</code> command. The <code>-Xdoclint</code> option is disabled by default in the <code>javac</code> command. </p>
<p> The variable <i>access</i> specifies the minimum visibility level of classes and members that the <code>-Xdoclint</code> option checks. It can have one of the following values (in order of most to least visible) : <code>public</code>, <code>protected</code>, <code>package</code> and <code>private</code>. For example, the following option checks classes and members (with all groups of checks) that have the access level protected and higher (which includes protected, package and public): </p>
<pre>
<code>-Xdoclint:all/protected</code>
</pre>
<pre>
</pre>
<p> The following option enables all groups of checks for all access levels, except it will not check for HTML errors for classes and members that have access level package and higher (which includes package and public): </p>
<pre>
<code>-Xdoclint:all,-html/package</code>
</pre>
<pre>
</pre>
<dt>-Xdoclint:none</p>
<dd>
 Disables all groups of checks.</p>
<dt>-Xdoclint:all[<i>/access</i>]</p>
<dd>
 Enables all groups of checks.</p>
<dt>-Xlint</p>
<dd>
 <i></i>Enables all recommended warnings. In this release, enabling all available warnings is recommended.</p>
<dt>-Xlint:all</p>
<dd>
 <i></i>Enables all recommended warnings. In this release, enabling all available warnings is recommended.</p>
<dt>-Xlint:none</p>
<dd>
 Disables all warnings.</p>
<dt>-Xlint:<i>name</i></p>
<dd>
 Disables warning name. See Enable or Disable Warnings with the -Xlint Option for a list of warnings you can disable with this option.</p>
<dt>-Xlint:<i>-name</i></p>
<dd>
 Disables warning name. See Enable or Disable Warnings with the -Xlint Option with the <code>-Xlint</code> option to get a list of warnings that you can disable with this option.</p>
<dt>-Xmaxerrs <i>number</i></p>
<dd>
 Sets the maximum number of errors to print.</p>
<dt>-Xmaxwarns <i>number</i></p>
<dd>
 Sets the maximum number of warnings to print.</p>
<dt>-Xstdout <i>filename</i></p>
<dd>
 Sends compiler messages to the named file. By default, compiler messages go to <code>System.err</code>.</p>
<dt>-Xprefer:[<i>newer,source</i>]</p>
<dd>
 Specifies which file to read when both a source file and class file are found for a type. (See Searching for Types). If the <code>-Xprefer:newer</code> option is used, then it reads the newer of the source or class file for a type (default). If the <code>-Xprefer:source</code> option is used, then it reads the source file. Use &#8211;<code>Xprefer:source</code> when you want to be sure that any annotation processors can access annotations declared with a retention policy of <code>SOURCE</code>.</p>
<dt>-Xpkginfo:[<i>always</i>,<i>legacy</i>,<i>nonempty</i>]</p>
<dd>
 Control whether javac generates <code>package-info.class</code> files from package-info.java files. Possible mode arguments for this option include the following.</p>
<dl>
<dt>
<dd>
<dl>
<dt>always</p>
<dd> Always generate a <code>package-info.class</code> file for every <code>package-info.java</code> file. This option may be useful if you use a build system such as Ant, which checks that each <code>.java</code> file has a corresponding <code>.class</code> file.</p>
<dt>legacy</p>
<dd> Generate a <code>package-info.class</code> file only if package-info.java contains annotations. Don&#8217;t generate a <code>package-info.class</code> file if package-info.java only contains comments. </p>
<p> <i>Note:</i> A <code>package-info.class</code> file might be generated but be empty if all the annotations in the package-info.java file have <code>RetentionPolicy.SOURCE</code>.</p>
<dt>nonempty</p>
<dd> Generate a <code>package-info.class</code> file only if package-info.java contains annotations with <code>RetentionPolicy.CLASS</code> or <code>RetentionPolicy.RUNTIME</code>.</dl>
</dl>
<dt>-Xprint</p>
<dd>
 Prints a textual representation of specified types for debugging purposes. Perform neither annotation processing nor compilation. The format of the output could change.</p>
<dt>-XprintProcessorInfo</p>
<dd>
 Prints information about which annotations a processor is asked to process.</p>
<dt>-XprintRounds</p>
<dd>
 Prints information about initial and subsequent annotation processing rounds.</dl>
<h2>ENABLE OR DISABLE WARNINGS WITH THE -XLINT OPTION</h2>
<p> Enable warning <i>name</i> with the <code>-Xlint:name</code> option, where <code>name</code> is one of the following warning names. Note that you can disable a warning with the <code>-Xlint:-name:</code> option.</p>
<dl>
<dt>cast</p>
<dd> Warns about unnecessary and redundant casts, for example: </p>
<pre>
<code>String s = (String) &quot;Hello!&quot;</code>
</pre>
<pre>
</pre>
<dt>classfile</p>
<dd> Warns about issues related to class file contents.</p>
<dt>deprecation</p>
<dd> Warns about the use of deprecated items, for example: </p>
<pre>
<code>java.util.Date myDate = new java.util.Date();</code>
</pre>
<p>int currentDay = myDate.getDay();</p>
<pre>
</pre>
<p> The method <code>java.util.Date.getDay</code> has been deprecated since JDK 1.1</p>
<dt>dep-ann</p>
<dd> Warns about items that are documented with an <code>@deprecated</code> Javadoc comment, but do not have a <code>@Deprecated</code> annotation, for example: </p>
<pre>
<code>/**</code>
</pre>
<pre>
<code>  * @deprecated As of Java SE 7, replaced by {@link #newMethod()}</code>
</pre>
<pre>
<code>  */</code>
</pre>
<p>public<br />
static void deprecatedMethood()<br />
{<br />
}</p>
<p>public<br />
static void newMethod()<br />
{<br />
}</p>
<pre>
</pre>
<dt>divzero</p>
<dd> Warns about division by the constant integer 0, for example: </p>
<pre>
<code>int divideByZero = 42 / 0;</code>
</pre>
<pre>
</pre>
<dt>empty</p>
<dd> Warns about empty statements after <code>if</code>statements, for example: </p>
<pre>
<code>class E {</code>
</pre>
<pre>
<code>    void m() {</code>
</pre>
<p>if (true)<br />
    ;</p>
<pre>
<code>    }</code>
</pre>
<pre>
<code>}</code>
</pre>
<pre>
</pre>
<dt>fallthrough</p>
<dd> Checks the switch blocks for fall-through cases and provides a warning message for any that are found. Fall-through cases are cases in a switch block, other than the last case in the block, whose code does not include a break statement, allowing code execution to fall through from that case to the next case. For example, the code following the case 1 label in this switch block does not end with a break statement: </p>
<pre>
<code>switch (x) {</code>
</pre>
<pre>
<code>case 1:</code>
</pre>
<pre>
<code>  System.out.println(&quot;1&quot;);</code>
</pre>
<pre>
<code>  // No break statement here.</code>
</pre>
<pre>
<code>case 2:</code>
</pre>
<pre>
<code>  System.out.println(&quot;2&quot;);</code>
</pre>
<pre>
<code>}</code>
</pre>
<pre>
</pre>
<p> If the <code>-Xlint:fallthrough</code> option was used when compiling this code, then the compiler emits a warning about possible fall-through into case, with the line number of the case in question.</p>
<dt>finally</p>
<dd> Warns about <code>finally</code> clauses that cannot complete normally, for example: </p>
<pre>
<code>public static int m() {</code>
</pre>
<pre>
<code>  try {</code>
</pre>
<pre>
<code>     throw new NullPointerException();</code>
</pre>
<p>}  catch (NullPointerException(); {</p>
<pre>
<code>     System.err.println(&quot;Caught NullPointerException.&quot;);</code>
</pre>
<pre>
<code>     return 1;</code>
</pre>
<pre>
<code>   } finally {</code>
</pre>
<pre>
<code>     return 0;</code>
</pre>
<pre>
<code>   }</code>
</pre>
<pre>
<code>  }</code>
</pre>
<pre>
</pre>
<p> The compiler generates a warning for the <code>finally</code> block in this example. When the <code>int</code> method is called, it returns a value of 0. A <code>finally</code> block executes when the <code>try</code> block exits. In this example, when control is transferred to the <code>catch</code> block, the <code>int</code> method exits. However, the <code>finally</code> block must execute, so it is executed, even though control was transferred outside the method.</p>
<dt>options</p>
<dd> Warns about issues that related to the use of command-line options. See Cross-Compilation Options.</p>
<dt>overrides</p>
<dd> Warns about issues regarding method overrides. For example, consider the following two classes: </p>
<pre>
<code>public class ClassWithVarargsMethod {</code>
</pre>
<pre>
<code>  void varargsMethod(String... s) { }</code>
</pre>
<pre>
<code>}</code>
</pre>
<pre>
</pre>
<pre>
<code>public class ClassWithOverridingMethod extends ClassWithVarargsMethod {</code>
</pre>
<pre>
<code>   @Override</code>
</pre>
<p>void varargsMethod(String[] s)<br />
{<br />
}</p>
<pre>
<code>}</code>
</pre>
<pre>
</pre>
<p> The compiler generates a warning similar to the following:. </p>
<p>warning : [override] varargsMethod(String[]) in ClassWithOverridingMethod</p>
<pre>
<code>overrides varargsMethod(String...) in ClassWithVarargsMethod; overriding</code>
</pre>
<pre>
<code>method is missing '...'</code>
</pre>
<pre>
</pre>
<p> When the compiler encounters a <code>varargs</code> method, it translates the <code>varargs</code> formal parameter into an array. In the method <code>ClassWithVarargsMethod.varargsMethod</code>, the compiler translates the <code>varargs</code> formal parameter <code>String&#8230; s</code> to the formal parameter <code>String[] s</code>, an array, which matches the formal parameter of the method <code>ClassWithOverridingMethod.varargsMethod</code>. Consequently, this example compiles.</p>
<dt>path</p>
<dd> Warns about invalid path elements and nonexistent path directories on the command line (with regard to the class path, the source path, and other paths). Such warnings cannot be suppressed with the <code>@SuppressWarnings</code> annotation, for example: </p>
<pre>
<code>javac -Xlint:path -classpath /nonexistentpath Example.java</code>
</pre>
<pre>
</pre>
<dt>processing</p>
<dd> Warn about issues regarding annotation processing. The compiler generates this warning when you have a class that has an annotation, and you use an annotation processor that cannot handle that type of exception. For example, the following is a simple annotation processor: </p>
<p> <i>Source file AnnocProc.java</i>: </p>
<pre>
<code>import java.util.*;</code>
</pre>
<pre>
<code>import javax.annotation.processing.*;</code>
</pre>
<pre>
<code>import javax.lang.model.*;</code>
</pre>
<pre>
<code>import.javaz.lang.model.element.*;</code>
</pre>
<pre>
</pre>
<pre>
<code>@SupportedAnnotationTypes(&quot;NotAnno&quot;)</code>
</pre>
<pre>
<code>public class AnnoProc extends AbstractProcessor {</code>
</pre>
<pre>
<code>  public boolean process(Set&lt;? extends TypeElement&gt; elems, RoundEnvironment renv){</code>
</pre>
<pre>
<code>     return true;</code>
</pre>
<pre>
<code>  }</code>
</pre>
<pre>
</pre>
<pre>
<code>  public SourceVersion getSupportedSourceVersion() {</code>
</pre>
<p>return SourceVersion.latest();</p>
<pre>
<code>   }</code>
</pre>
<pre>
<code>}</code>
</pre>
<pre>
</pre>
<p> <i>Source file AnnosWithoutProcessors.java</i>: </p>
<pre>
<code>@interface Anno { }</code>
</pre>
<pre>
</pre>
<pre>
<code>@Anno</code>
</pre>
<pre>
<code>class AnnosWithoutProcessors { }</code>
</pre>
<pre>
</pre>
<p> The following commands compile the annotation processor <code>AnnoProc</code>, then run this annotation processor against the source file <code>AnnosWithoutProcessors.java</code>: </p>
<pre>
<code>javac AnnoProc.java</code>
</pre>
<pre>
<code>javac -cp . -Xlint:processing -processor AnnoProc -proc:only AnnosWithoutProcessors.java</code>
</pre>
<pre>
</pre>
<p> When the compiler runs the annotation processor against the source file <code>AnnosWithoutProcessors.java</code>, it generates the following warning: </p>
<pre>
<code>warning: [processing] No processor claimed any of these annotations: Anno</code>
</pre>
<pre>
</pre>
<p> To resolve this issue, you can rename the annotation defined and used in the class <code>AnnosWithoutProcessors</code> from <code>Anno</code> to <code>NotAnno</code>.</p>
<dt>rawtypes</p>
<dd> Warns about unchecked operations on raw types. The following statement generates a <code>rawtypes</code> warning: </p>
<pre>
<code>void countElements(List l) { ... }</code>
</pre>
<pre>
</pre>
<p> The following example does not generate a <code>rawtypes</code> warning </p>
<pre>
<code>void countElements(List&lt;?&gt; l) { ... }</code>
</pre>
<pre>
</pre>
<p> <code>List</code> is a raw type. However, <code>List&lt;?&gt;</code> is an unbounded wildcard parameterized type. Because <code>List</code> is a parameterized interface, always specify its type argument. In this example, the <code>List</code> formal argument is specified with an unbounded wildcard (<code>?</code>) as its formal type parameter, which means that the <code>countElements</code> method can accept any instantiation of the <code>List</code> interface.</p>
<dt>Serial</p>
<dd> Warns about missing <code>serialVersionUID</code> definitions on serializable classes, for example: </p>
<pre>
<code>public class PersistentTime implements Serializable</code>
</pre>
<pre>
<code>{</code>
</pre>
<pre>
<code>  private Date time;</code>
</pre>
<pre>
</pre>
<pre>
<code>   public PersistentTime() {</code>
</pre>
<pre>
<code>     time = Calendar.getInstance().getTime();</code>
</pre>
<pre>
<code>   }</code>
</pre>
<pre>
</pre>
<pre>
<code>   public Date getTime() {</code>
</pre>
<pre>
<code>     return time;</code>
</pre>
<pre>
<code>   }</code>
</pre>
<pre>
<code>}</code>
</pre>
<pre>
</pre>
<p> The compiler generates the following warning: </p>
<pre>
<code>warning: [serial] serializable class PersistentTime has no definition of</code>
</pre>
<pre>
<code>serialVersionUID</code>
</pre>
<pre>
</pre>
<p> If a serializable class does not explicitly declare a field named <code>serialVersionUID</code>, then the serialization runtime environment calculates a default <code>serialVersionUID</code> value for that class based on various aspects of the class, as described in the Java Object Serialization Specification. However, it is strongly recommended that all serializable classes explicitly declare <code>serialVersionUID</code> values because the default process of computing <code>serialVersionUID</code> vales is highly sensitive to class details that can vary depending on compiler implementations, and as a result, might cause an unexpected <code>InvalidClassExceptions</code> during deserialization. To guarantee a consistent <code>serialVersionUID</code> value across different Java compiler implementations, a serializable class must declare an explicit <code>serialVersionUID</code> value.</p>
<dt>static</p>
<dd> Warns about issues relating to the use of statics, for example: </p>
<pre>
<code>class XLintStatic {</code>
</pre>
<p>static void m1()<br />
{<br />
}</p>
<p>void m2()<br />
{<br />
    this.m1();<br />
}</p>
<pre>
<code>}</code>
</pre>
<pre>
</pre>
<p> The compiler generates the following warning: </p>
<p>warning : [static] static method should be qualified by type name,</p>
<pre>
<code>XLintStatic, instead of by an expression</code>
</pre>
<pre>
</pre>
<p> To resolve this issue, you can call the <code>static</code> method <code>m1</code> as follows: </p>
<pre>
<code>XLintStatic.m1();</code>
</pre>
<pre>
</pre>
<p> Alternately, you can remove the <code>static</code> keyword from the declaration of the method <code>m1</code>.</p>
<dt>try</p>
<dd> Warns about issues relating to use of <code>try</code> blocks, including try-with-resources statements. For example, a warning is generated for the following statement because the resource <code>ac</code> declared in the <code>try</code> block is not used: </p>
<pre>
<code>try ( AutoCloseable ac = getResource() ) {    // do nothing}</code>
</pre>
<pre>
</pre>
<dt>unchecked</p>
<dd> Gives more detail for unchecked conversion warnings that are mandated by the Java Language Specification, for example: </p>
<pre>
<code>List l = new ArrayList&lt;Number&gt;();</code>
</pre>
<pre>
<code>List&lt;String&gt; ls = l;       // unchecked warning</code>
</pre>
<pre>
</pre>
<p> During type erasure, the types <code>ArrayList&lt;Number&gt;</code> and <code>List&lt;String&gt;</code> become <code>ArrayList</code> and <code>List</code>, respectively. </p>
<p> The <code>ls</code> command has the parameterized type <code>List&lt;String&gt;</code>. When the <code>List</code> referenced by <code>l</code> is assigned to <code>ls</code>, the compiler generates an unchecked warning. At compile time, the compiler and JVM cannot determine whether <code>l</code> refers to a <code>List&lt;String&gt;</code> type. In this case, <code>l</code> does not refer to a <code>List&lt;String&gt;</code> type. As a result, heap pollution occurs. </p>
<p> A heap pollution situation occurs when the <code>List</code> object <code>l</code>, whose static type is <code>List&lt;Number&gt;</code>, is assigned to another <code>List</code> object, <code>ls</code>, that has a different static type, <code>List&lt;String&gt;</code>. However, the compiler still allows this assignment. It must allow this assignment to preserve backward compatibility with releases of Java SE that do not support generics. Because of type erasure, <code>List&lt;Number&gt;</code> and <code>List&lt;String&gt;</code> both become <code>List</code>. Consequently, the compiler allows the assignment of the object <code>l</code><code>,</code> which has a raw type of <code>List</code>, to the object <code>ls</code>.</p>
<dt>varargs</p>
<dd> Warns about unsafe usages of variable arguments (<code>varargs</code>) methods, in particular, those that contain non-reifiable arguments, for example: </p>
<pre>
<code>public class ArrayBuilder {</code>
</pre>
<pre>
<code>  public static &lt;T&gt; void addToList (List&lt;T&gt; listArg, T... elements) {</code>
</pre>
<pre>
<code>    for (T x : elements) {</code>
</pre>
<pre>
<code>      listArg.add(x);</code>
</pre>
<pre>
<code>    }</code>
</pre>
<pre>
<code>  }</code>
</pre>
<pre>
<code>}</code>
</pre>
<pre>
</pre>
<p> <i>Note:</i> A non-reifiable type is a type whose type information is not fully available at runtime. </p>
<p> The compiler generates the following warning for the definition of the method <code>ArrayBuilder.addToList</code> </p>
<pre>
<code>warning: [varargs] Possible heap pollution from parameterized vararg type T</code>
</pre>
<pre>
</pre>
<p> When the compiler encounters a varargs method, it translates the <code>varargs</code> formal parameter into an array. However, the Java programming language does not permit the creation of arrays of parameterized types. In the method <code>ArrayBuilder.addToList</code>, the compiler translates the <code>varargs</code> formal parameter <code>T&#8230;</code> elements to the formal parameter <code>T[]</code> elements, an array. However, because of type erasure, the compiler converts the <code>varargs</code> formal parameter to <code>Object[]</code> elements. Consequently, there is a possibility of heap pollution.</dl>
<h2>COMMAND-LINE ARGUMENT FILES</h2>
<p> To shorten or simplify the <code>javac</code> command, you can specify one or more files that contain arguments to the <code>javac</code> command (except <code>-J</code> options). This enables you to create <code>javac</code> commands of any length on any operating system. </p>
<p> An argument file can include <code>javac</code> options and source file names in any combination. The arguments within a file can be separated by spaces or new line characters. If a file name contains embedded spaces, then put the whole file name in double quotation marks. </p>
<p> File Names within an argument file are relative to the current directory, not the location of the argument file. Wild cards (*) are not allowed in these lists (such as for specifying <code>*.java</code>). Use of the at sign (@) to recursively interpret files is not supported. The <code>-J</code> options are not supported because they are passed to the launcher, which does not support argument files. </p>
<p> When executing the <code>javac</code> command, pass in the path and name of each argument file with the at sign (@) leading character. When the <code>javac</code> command encounters an argument beginning with the at sign (@), it expands the contents of that file into the argument list. </p>
<p> <code>Example 1 Single Argument File</code> </p>
<p> You could use a single argument file named <code>argfile</code> to hold all <code>javac</code> arguments: </p>
<pre>
<code>javac @argfile</code>
</pre>
<pre>
</pre>
<p> This argument file could contain the contents of both files shown in Example 2 </p>
<p> <code>Example 2 Two Argument Files</code> </p>
<p> You can create two argument files: one for the <code>javac</code> options and the other for the source file names. Note that the following lists have no line-continuation characters. </p>
<p> Create a file named options that contains the following: </p>
<pre>
<code>-d classes</code>
</pre>
<pre>
<code>-g</code>
</pre>
<pre>
<code>-sourcepath /java/pubs/ws/1.3/src/share/classes</code>
</pre>
<pre>
</pre>
<p> Create a file named classes that contains the following: </p>
<pre>
<code>MyClass1.java</code>
</pre>
<pre>
<code>MyClass2.java</code>
</pre>
<pre>
<code>MyClass3.java</code>
</pre>
<pre>
</pre>
<p> Then, run the <code>javac</code> command as follows: </p>
<pre>
<code>javac @options @classes</code>
</pre>
<pre>
</pre>
<p> <code>Example 3 Argument Files with Paths</code> </p>
<p> The argument files can have paths, but any file names inside the files are relative to the current working directory (not <code>path1</code> or <code>path2</code>): </p>
<pre>
<code>javac @path1/options @path2/classes</code>
</pre>
<pre>
</pre>
<h2>ANNOTATION PROCESSING</h2>
<p> The <code>javac</code> command provides direct support for annotation processing, superseding the need for the separate annotation processing command, <code>apt</code>. </p>
<p> The API for annotation processors is defined in the <code>javax.annotation.processing</code> and j<code>avax.lang.model</code> packages and subpackages.</p>
<h3>HOW ANNOTATION PROCESSING WORKS</h3>
<p> Unless annotation processing is disabled with the <code>-proc:none</code> option, the compiler searches for any annotation processors that are available. The search path can be specified with the <code>-processorpath</code> option. If no path is specified, then the user class path is used. Processors are located by means of service provider-configuration files named <code>META-INF/services/javax.annotation.processing</code>.Processor on the search path. Such files should contain the names of any annotation processors to be used, listed one per line. Alternatively, processors can be specified explicitly, using the <code>-processor</code> option. </p>
<p> After scanning the source files and classes on the command line to determine what annotations are present, the compiler queries the processors to determine what annotations they process. When a match is found, the processor is called. A processor can claim the annotations it processes, in which case no further attempt is made to find any processors for those annotations. After all of the annotations are claimed, the compiler does not search for additional processors. </p>
<p> If any processors generate new source files, then another round of annotation processing occurs: Any newly generated source files are scanned, and the annotations processed as before. Any processors called on previous rounds are also called on all subsequent rounds. This continues until no new source files are generated. </p>
<p> After a round occurs where no new source files are generated, the annotation processors are called one last time, to give them a chance to complete any remaining work. Finally, unless the <code>-proc:only</code> option is used, the compiler compiles the original and all generated source files.</p>
<h3>IMPLICITLY LOADED SOURCE FILES</h3>
<p> To compile a set of source files, the compiler might need to implicitly load additional source files. See Searching for Types. Such files are currently not subject to annotation processing. By default, the compiler gives a warning when annotation processing occurred and any implicitly loaded source files are compiled. The <code>-implicit</code> option provides a way to suppress the warning.</p>
<h2>SEARCHING FOR TYPES</h2>
<p> To compile a source file, the compiler often needs information about a type, but the type definition is not in the source files specified on the command line. The compiler needs type information for every class or interface used, extended, or implemented in the source file. This includes classes and interfaces not explicitly mentioned in the source file, but that provide information through inheritance. </p>
<p> For example, when you create a subclass <code>java.applet.Applet</code>, you are also using the ancestor classes of <code>Applet</code>: <code>java.awt.Panel</code>, <code>java.awt.Container</code>, <code>java.awt.Component</code>, and <code>java.lang.Object</code>. </p>
<p> When the compiler needs type information, it searches for a source file or class file that defines the type. The compiler searches for class files first in the bootstrap and extension classes, then in the user class path (which by default is the current directory). The user class path is defined by setting the <code>CLASSPATH</code> environment variable or by using the <code>-classpath</code> option. </p>
<p> If you set the <code>-sourcepath</code> option, then the compiler searches the indicated path for source files. Otherwise, the compiler searches the user class path for both class files and source files. </p>
<p> You can specify different bootstrap or extension classes with the <code>-bootclasspath</code> and the <code>-extdirs</code> options. See Cross-Compilation Options. </p>
<p> A successful type search may produce a class file, a source file, or both. If both are found, then you can use the <code>-Xprefer</code> option to instruct the compiler which to use. If <code>newer</code> is specified, then the compiler uses the newer of the two files. If <code>source</code> is specified, the compiler uses the source file. The default is <code>newer</code>. </p>
<p> If a type search finds a source file for a required type, either by itself, or as a result of the setting for the <code>-Xprefer</code> option, then the compiler reads the source file to get the information it needs. By default the compiler also compiles the source file. You can use the <code>-implicit</code> option to specify the behavior. If <code>none</code> is specified, then no class files are generated for the source file. If <code>class</code> is specified, then class files are generated for the source file. </p>
<p> The compiler might not discover the need for some type information until after annotation processing completes. When the type information is found in a source file and no <code>-implicit</code> option is specified, the compiler gives a warning that the file is being compiled without being subject to annotation processing. To disable the warning, either specify the file on the command line (so that it will be subject to annotation processing) or use the <code>-implicit</code> option to specify whether or not class files should be generated for such source files.</p>
<h2>PROGRAMMATIC INTERFACE</h2>
<p> The <code>javac</code> command supports the new Java Compiler API defined by the classes and interfaces in the <code>javax.tools</code> package.</p>
<h3>EXAMPLE</h3>
<p> To compile as though providing command-line arguments, use the following syntax: </p>
<pre>
<code>JavaCompiler javac = ToolProvider.getSystemJavaCompiler();</code>
</pre>
<pre>
</pre>
<p> The example writes diagnostics to the standard output stream and returns the exit code that <code>javac</code> would give when called from the command line. </p>
<p> You can use other methods in the <code>javax.tools.JavaCompiler</code> interface to handle diagnostics, control where files are read from and written to, and more.</p>
<h3>OLD INTERFACE</h3>
<p> <i>Note:</i> This API is retained for backward compatibility only. All new code should use the newer Java Compiler API. </p>
<p> The <code>com.sun.tools.javac.Main</code> class provides two static methods to call the compiler from a program: </p>
<p>public<br />
static int compile(String[] args);</p>
<p>public<br />
static int compile(String[] args, PrintWriter out);</p>
<pre>
</pre>
<p> The <code>args</code> parameter represents any of the command-line arguments that would typically be passed to the compiler. </p>
<p> The <code>out</code> parameter indicates where the compiler diagnostic output is directed. </p>
<p> The <code>return</code> value is equivalent to the <code>exit</code> value from <code>javac</code>. </p>
<p> <i>Note:</i> All other classes and methods found in a package with names that start with <code>com.sun.tools.javac</code> (subpackages of <code>com.sun.tools.javac</code>) are strictly internal and subject to change at any time.</p>
<h2>EXAMPLES</h2>
<p> <code>Example 1 Compile a Simple Program</code> </p>
<p> This example shows how to compile the <code>Hello.java</code> source file in the greetings directory. The class defined in <code>Hello.java</code> is called <code>greetings.Hello</code>. The greetings directory is the package directory both for the source file and the class file and is underneath the current directory. This makes it possible to use the default user class path. It also makes it unnecessary to specify a separate destination directory with the <code>-d</code> option. </p>
<p> The source code in <code>Hello.java</code>: </p>
<pre>
<code>package greetings;</code>
</pre>
<pre>
</pre>
<pre>
<code>public class Hello {</code>
</pre>
<p>public<br />
static void main(String[] args)<br />
{</p>
<pre><code>
for (int i = 0; i &lt; args.length; i++) {
</code></pre>
<pre>
<code>            System.out.println(&quot;Hello &quot; + args[i]);</code>
</pre>
<pre>
<code>        }</code>
</pre>
<pre>
<code>    }</code>
</pre>
<pre>
<code>}</code>
</pre>
<pre>
</pre>
<p> Compile greetings.Hello: </p>
<pre>
<code>javac greetings/Hello.java</code>
</pre>
<pre>
</pre>
<p> Run <code>greetings.Hello</code>: </p>
<pre>
<code>java greetings.Hello World Universe Everyone</code>
</pre>
<pre>
<code>Hello World</code>
</pre>
<pre>
<code>Hello Universe</code>
</pre>
<pre>
<code>Hello Everyone</code>
</pre>
<pre>
</pre>
<p> <code>Example 2 Compile Multiple Source Files</code> </p>
<p> This example compiles the <code>Aloha.java</code>, <code>GutenTag.java</code>, <code>Hello.java</code>, and <code>Hi.java</code> source files in the <code>greetings</code> package. </p>
<pre>
<code>% javac greetings/*.java</code>
</pre>
<pre>
<code>% ls greetings</code>
</pre>
<pre>
<code>Aloha.class         GutenTag.class      Hello.class         Hi.class</code>
</pre>
<pre>
<code>Aloha.java          GutenTag.java       Hello.java          Hi.java</code>
</pre>
<pre>
</pre>
<p> <code>Example 3 Specify a User Class Path</code> </p>
<p> After changing one of the source files in the previous example, recompile it: </p>
<pre>
<code>pwd</code>
</pre>
<pre>
<code>/examples</code>
</pre>
<pre>
<code>javac greetings/Hi.java</code>
</pre>
<pre>
</pre>
<p> Because <code>greetings.Hi</code> refers to other classes in the <code>greetings</code> package, the compiler needs to find these other classes. The previous example works because the default user class path is the directory that contains the package directory. If you want to recompile this file without concern for which directory you are in, then add the examples directory to the user class path by setting <code>CLASSPATH</code>. This example uses the <code>-classpath</code> option. </p>
<pre>
<code>javac -classpath /examples /examples/greetings/Hi.java</code>
</pre>
<pre>
</pre>
<p> If you change <code>greetings.Hi</code> to use a banner utility, then that utility also needs to be accessible through the user class path. </p>
<pre>
<code>javac -classpath /examples:/lib/Banners.jar \</code>
</pre>
<pre>
<code>            /examples/greetings/Hi.java</code>
</pre>
<pre>
</pre>
<p> To execute a class in the <code>greetings</code> package, the program needs access to the <code>greetings</code> package, and to the classes that the <code>greetings</code> classes use. </p>
<pre>
<code>java -classpath /examples:/lib/Banners.jar greetings.Hi</code>
</pre>
<pre>
</pre>
<p> <code>Example 4 Separate Source Files and Class Files</code> </p>
<p> The following example uses <code>javac</code> to compile code that runs on JVM 1.7. </p>
<pre>
<code>javac -source 1.7 -target 1.7 -bootclasspath jdk1.7.0/lib/rt.jar \ </code>
</pre>
<pre>
<code>-extdirs &quot;&quot; OldCode.java</code>
</pre>
<pre>
</pre>
<p> The <code>-source 1.7</code> option specifies that release 1.7 (or 7) of the Java programming language be used to compile <code>OldCode.java</code>. The option <code>-target 1.7</code> option ensures that the generated class files are compatible with JVM 1.7. Note that in most cases, the value of the <code>-target</code> option is the value of the <code>-source</code> option; in this example, you can omit the <code>-target</code> option. </p>
<p> You must specify the <code>-bootclasspath</code> option to specify the correct version of the bootstrap classes (the <code>rt.jar</code> library). If not, then the compiler generates a warning: </p>
<pre>
<code>javac -source 1.7 OldCode.java</code>
</pre>
<pre>
<code>warning: [options] bootstrap class path not set in conjunction with </code>
</pre>
<pre>
<code>-source 1.7</code>
</pre>
<pre>
</pre>
<p> If you do not specify the correct version of bootstrap classes, then the compiler uses the old language rules (in this example, it uses version 1.7 of the Java programming language) combined with the new bootstrap classes, which can result in class files that do not work on the older platform (in this case, Java SE 7) because reference to nonexistent methods can get included. </p>
<p> <code>Example 5 Cross Compile</code> </p>
<p> This example uses <code>javac</code> to compile code that runs on JVM 1.7. </p>
<pre>
<code>javac -source 1.7 -target 1.7 -bootclasspath jdk1.7.0/lib/rt.jar \</code>
</pre>
<pre>
<code>            -extdirs &quot;&quot; OldCode.java</code>
</pre>
<pre>
</pre>
<p> The<code>-source 1.7</code> option specifies that release 1.7 (or 7) of the Java programming language to be used to compile OldCode.java. The <code>-target 1.7</code> option ensures that the generated class files are compatible with JVM 1.7. </p>
<p> You must specify the <code>-bootclasspath</code> option to specify the correct version of the bootstrap classes (the <code>rt.jar</code> library). If not, then the compiler generates a warning: </p>
<pre>
<code>javac -source 1.7 OldCode.java</code>
</pre>
<pre>
<code>warning: [options] bootstrap class path not set in conjunction with -source 1.7</code>
</pre>
<pre>
</pre>
<p> If you do not specify the correct version of bootstrap classes, then the compiler uses the old language rules combined with the new bootstrap classes. This combination can result in class files that do not work on the older platform (in this case, Java SE 7) because reference to nonexistent methods can get included. In this example, the compiler uses release 1.7 of the Java programming language.</p>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-java/">java</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-jdb/">jdb</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-javadoc/">javadoc</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-jar/">jar</a>(1)</p>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-jdb/">jdb</a>(1) </p>
</dl>
<h2>Index</h2>
