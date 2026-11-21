---
title: "scalac(1)"
name: "scalac"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scalac/"
description: "scalac – Compiler for the Scala 2 language"
---
<h2 class="name">NAME</h2>
<p> <code>scalac</code> - Compiler for the Scala 2 language </p>
<h2>SYNOPSIS</h2>
<p> <code>scalac</code> [ &lt;<i>options</i>&gt; ] &lt;<i>source files</i>&gt;  </p>
<h2>PARAMETERS</h2>
<dl>
<dt>&lt;<i>options</i>&gt;</dt>
<dd> <p> Command line options. See <code>OPTIONS</code> below. </p>
 </dd>
<dt>&lt;<i>source files</i>&gt;</dt>
<dd> <p> One or more source files to be compiled (such as MyClass.scala). </p>
 </dd></dl>
<h2>DESCRIPTION</h2>
<p> The <code>scalac</code> tool reads class and object definitions, written in the Scala programming language, and compiles them into bytecode class files. </p>
<p> By default, the compiler puts each class file in the same directory as its source file. You can specify a separate destination directory with -d (see <code>OPTIONS</code>, below).  </p>
<h2>OPTIONS</h2>
<p> The compiler has a set of standard options that are supported on the current development environment and will be supported in future releases. An additional set of non-standard options are specific to the current virtual machine implementation and are subject to change in the future. Non-standard options begin with <code>-X</code>.  </p>
<h3>Standard Options</h3>
<dl>
<dt><code>-D</code>property=value </dt>
<dd> <p> Pass <code>-D</code>property=value directly to the runtime system. </p>
 </dd>
<dt><code>-J</code>&lt;<i>flag</i>&gt; </dt>
<dd> <p> Pass &lt;<i>flag</i>&gt; directly to the runtime system. </p>
 </dd>
<dt><code>-P:</code>&lt;<i>plugin:opt</i>&gt; </dt>
<dd> <p> Pass an option to a plugin </p>
 </dd>
<dt><code>-X</code></dt>
<dd> <p> Print a synopsis of advanced options. </p>
 </dd>
<dt><code>-bootclasspath</code> &lt;<i>path</i>&gt; </dt>
<dd> <p> Override location of bootstrap class files (where to find the standard built-in classes, such as &quot;scala.List&quot;). </p>
 </dd>
<dt><code>-classpath</code> &lt;<i>path</i>&gt; </dt>
<dd> <p> Specify where to find user class files (on Unix-based systems a colon-separated list of paths, on Windows-based systems, a semicolon-separate list of paths). This does not override the built-in (&quot;boot&quot;) search path. </p>
 </dd>
<dd> <p> The default class path is the current directory. Setting the CLASSPATH variable or using the -classpath command-line option overrides that default, so if you want to include the current directory in the search path, you must include &quot;.&quot; in the new settings. </p>
 </dd>
<dd>  </dd>
<dt><code>-d</code> &lt;<i>directory|jar</i>&gt; </dt>
<dd> <p> Specify where to place generated class files. </p>
 </dd>
<dt><code>-deprecation</code></dt>
<dd> <p> Emit warning and location for usages of deprecated APIs. </p>
 </dd>
<dd> <p> Available since Scala version 2.2.1 </p>
 </dd>
<dd>  </dd>
<dt><code>-encoding</code> &lt;<i>encoding</i>&gt; </dt>
<dd> <p> Specify character encoding used by source files. </p>
 </dd>
<dd> <p> The default value is platform-specific (Linux: &quot;UTF8&quot;, Windows: &quot;Cp1252&quot;). Executing the following code in the Scala interpreter will return the default value on your system: </p>
 </dd>
<dd> <p> <code> scala&gt; </code>new java.io.InputStreamReader(System.in).getEncoding </p>
 </dd>
<dd>  </dd>
<dt><code>-explaintypes</code></dt>
<dd> <p> Explain type errors in more detail. </p>
 </dd>
<dt><code>-extdirs</code> &lt;<i>dirs</i>&gt; </dt>
<dd> <p> Override location of installed extensions. </p>
 </dd>
<dt><code>-g:</code>{none,source,line,vars,notailcalls} </dt>
<dd> <p> &quot;none&quot; generates no debugging info, </p>
 </dd>
<dd> <p> &quot;source&quot; generates only the source file attribute, </p>
 </dd>
<dd> <p> &quot;line&quot; generates source and line number information, </p>
 </dd>
<dd> <p> &quot;vars&quot; generates source, line number and local variable information, </p>
 </dd>
<dd> <p> &quot;notailcalls&quot; generates all of the above and <i>will not</i> perform tail call optimization. </p>
 </dd>
<dd>  </dd>
<dt><code>-help</code></dt>
<dd> <p> Print a synopsis of standard options. </p>
 </dd>
<dt><code>-javabootclasspath</code> &lt;<i>path</i>&gt; </dt>
<dd> <p> Override Java boot classpath. </p>
 </dd>
<dt><code>-javaextdirs</code> &lt;<i>path</i>&gt; </dt>
<dd> <p> Override Java extdirs classpath. </p>
 </dd>
<dt><code>-no-specialization</code></dt>
<dd> <p> Ignore <i>@specialize</i> annotations. </p>
 </dd>
<dt><code>-nobootcp</code></dt>
<dd> <p> Do not use the boot classpath for the Scala jar files. </p>
 </dd>
<dt><code>-nowarn</code></dt>
<dd> <p> Generate no warnings </p>
 </dd>
<dt><code>-optimise</code></dt>
<dd> <p> Generates faster bytecode by applying optimisations to the program. </p>
 </dd>
<dt><code>-print</code></dt>
<dd> <p> Print program with all Scala-specific features removed. </p>
 </dd>
<dt><code>-sourcepath</code> &lt;<i>path</i>&gt; </dt>
<dd> <p> Specify location(s) of source files. </p>
 </dd>
<dt><code>-target:</code>&lt;<i>target</i>&gt; </dt>
<dd> <p> Specify which backend to use (jvm-1.5,msil). </p>
 </dd>
<dd> <p> The default value is &quot;jvm-1.5&quot; (was &quot;jvm-1.4&quot; up to Scala version 2.6.1). </p>
 </dd>
<dd>  </dd>
<dt><code>-toolcp</code> &lt;<i>path</i>&gt; </dt>
<dd> <p> Add to the runner classpath. </p>
 </dd>
<dt><code>-unchecked</code></dt>
<dd> <p> Enable detailed unchecked (erasure) warnings </p>
 </dd>
<dd> <p> Non variable type-arguments in type patterns are unchecked since they are eliminated by erasure </p>
 </dd>
<dd> <p> Available since Scala version 2.3.0 </p>
 </dd>
<dd>  </dd>
<dt><code>-uniqid</code></dt>
<dd> <p> Uniquely tag all identifiers in debugging output. </p>
 </dd>
<dt><code>-verbose</code></dt>
<dd> <p> Output messages about what the compiler is doing </p>
 </dd>
<dt><code>-version</code></dt>
<dd> <p> Print product version and exit. </p>
 </dd>
<dt><code>@</code>&lt;<i>file</i>&gt;</dt>
<dd> <p> A text file containing compiler arguments (options and source files) </p>
 </dd></dl>
<h3>Advanced Options</h3>
<dl>
<dt><code>-Xassem-extdirs</code> &lt;<i>dirs</i>&gt; </dt>
<dd> <p> (Requires -target:msil) List of directories containing assemblies. default:lib. </p>
 </dd>
<dt><code>-Xassem-name</code> &lt;<i>file</i>&gt; </dt>
<dd> <p> (Requires -target:msil) Name of the output assembly. </p>
 </dd>
<dt><code>-Xassem-path</code> &lt;<i>path</i>&gt; </dt>
<dd> <p> (Requires -target:msil) List of assemblies referenced by the program. </p>
 </dd>
<dt><code>-Xcheck-null</code></dt>
<dd> <p> Warn upon selection of nullable reference </p>
 </dd>
<dt><code>-Xcheckinit</code></dt>
<dd> <p> Wrap field accessors to throw an exception on uninitialized access. </p>
 </dd>
<dt><code>-Xdisable-assertions</code></dt>
<dd> <p> Generate no assertions and assumptions </p>
 </dd>
<dt><code>-Xelide-below</code> &lt;<i>n</i>&gt; </dt>
<dd> <p> Calls to <i>@elidable</i> methods are omitted if method priority is lower than argument. </p>
 </dd>
<dt><code>-Xexperimental</code></dt>
<dd> <p> Enable experimental extensions </p>
 </dd>
<dt><code>-Xfatal-warnings</code></dt>
<dd> <p> Fail the compilation if there are any warnings. </p>
 </dd>
<dt><code>-Xfuture</code></dt>
<dd> <p> Turn on future language features. </p>
 </dd>
<dt><code>-Xgenerate-phase-graph</code> &lt;<i>file</i>&gt; </dt>
<dd> <p> Generate the phase graphs (outputs .dot files) to fileX.dot. </p>
 </dd>
<dt><code>-Xlint</code></dt>
<dd> <p> Enable recommended additional warnings. </p>
 </dd>
<dt><code>-Xlog-implicits</code></dt>
<dd> <p> Show more detail on why some implicits are not applicable. </p>
 </dd>
<dt><code>-Xmax-classfile-name</code> &lt;<i>n</i>&gt; </dt>
<dd> <p> Maximum filename length for generated classes. </p>
 </dd>
<dt><code>-Xmigration</code></dt>
<dd> <p> Warn about constructs whose behavior may have changed between 2.7 and 2.8. </p>
 </dd>
<dt><code>-Xno-forwarders</code></dt>
<dd> <p> Do not generate static forwarders in mirror classes. </p>
 </dd>
<dt><code>-Xno-uescape</code></dt>
<dd> <p> Disable handling of \u unicode escapes </p>
 </dd>
<dt><code>-Xnojline</code></dt>
<dd> <p> Do not use JLine for editing. </p>
 </dd>
<dt><code>-Xplugin:</code>&lt;<i>file</i>&gt; </dt>
<dd> <p> Load a plugin from a file </p>
 </dd>
<dt><code>-Xplugin-disable:</code>&lt;<i>plugin</i>&gt; </dt>
<dd> <p> Disable a plugin </p>
 </dd>
<dt><code>-Xplugin-list</code></dt>
<dd> <p> Print a synopsis of loaded plugins </p>
 </dd>
<dt><code>-Xplugin-require:</code>&lt;<i>plugin</i>&gt; </dt>
<dd> <p> Abort unless the given plugin(s) are available </p>
 </dd>
<dt><code>-Xpluginsdir</code> &lt;<i>path</i>&gt; </dt>
<dd> <p> Path to search compiler plugins. </p>
 </dd>
<dt><code>-Xprint:</code>&lt;<i>phases</i>&gt; </dt>
<dd> <p> Print out program after &lt;<i>phases</i>&gt; (see below). </p>
 </dd>
<dt><code>-Xprint-icode</code></dt>
<dd> <p> Log internal icode to *.icode files. </p>
 </dd>
<dt><code>-Xprint-pos</code></dt>
<dd> <p> Print tree positions, as offsets. </p>
 </dd>
<dt><code>-Xprint-types</code></dt>
<dd> <p> Print tree types (debugging option). </p>
 </dd>
<dt><code>-Xprompt</code></dt>
<dd> <p> Display a prompt after each error (debugging option). </p>
 </dd>
<dt><code>-Xresident</code></dt>
<dd> <p> Compiler stays resident, files to compile are read from standard input. </p>
 </dd>
<dt><code>-Xscript</code> &lt;<i>object</i>&gt; </dt>
<dd> <p> Treat the source file as a script and wrap it in a main method. </p>
 </dd>
<dt><code>-Xshow-class</code> &lt;<i>class</i>&gt; </dt>
<dd> <p> Show internal representation of class. </p>
 </dd>
<dt><code>-Xshow-object</code> &lt;<i>object</i>&gt; </dt>
<dd> <p> Show internal representation of object. </p>
 </dd>
<dt><code>-Xshow-phases</code></dt>
<dd> <p> Print a synopsis of compiler phases. </p>
 </dd>
<dt><code>-Xsource-reader</code> &lt;<i>classname</i>&gt; </dt>
<dd> <p> Specify a custom method for reading source files. </p>
 </dd>
<dt><code>-Xsourcedir</code> &lt;<i>path</i>&gt; </dt>
<dd> <p> (Requires -target:msil) Mirror source folder structure in output directory.. </p>
 </dd>
<dt><code>-Xverify</code></dt>
<dd> <p> Verify generic signatures in generated bytecode. </p>
 </dd>
<dt><code>-Y</code></dt>
<dd> <p> Print a synopsis of private options. </p>
 </dd></dl>
<h3>Compilation Phases</h3>
<dl>
<dt><i>initial</i></dt>
<dd> <p> initializing compiler </p>
 </dd>
<dt><i>parse</i></dt>
<dd> <p> parse source files </p>
 </dd>
<dt><i>namer</i></dt>
<dd> <p> create symbols </p>
 </dd>
<dt><i>analyze</i></dt>
<dd> <p> name and type analysis </p>
 </dd>
<dt><i>refcheck</i></dt>
<dd> <p> reference checking </p>
 </dd>
<dt><i>uncurry</i></dt>
<dd> <p> uncurry function types and applications </p>
 </dd>
<dt><i>lambdalift</i></dt>
<dd> <p> lambda lifter </p>
 </dd>
<dt><i>typesasvalues</i></dt>
<dd> <p> represent types as values </p>
 </dd>
<dt><i>addaccessors</i></dt>
<dd> <p> add accessors for constructor arguments </p>
 </dd>
<dt><i>explicitouterclasses</i></dt>
<dd> <p> make links from inner classes to enclosing one explicit </p>
 </dd>
<dt><i>addconstructors</i></dt>
<dd> <p> add explicit constructor for each class </p>
 </dd>
<dt><i>tailcall</i></dt>
<dd> <p> add tail-calls </p>
 </dd>
<dt><i>wholeprog</i></dt>
<dd> <p> perform whole program analysis </p>
 </dd>
<dt><i>addinterfaces</i></dt>
<dd> <p> add one interface per class </p>
 </dd>
<dt><i>expandmixins</i></dt>
<dd> <p> expand mixins by code copying </p>
 </dd>
<dt><i>boxing</i></dt>
<dd> <p> makes boxing explicit </p>
 </dd>
<dt><i>erasure</i></dt>
<dd> <p> type eraser </p>
 </dd>
<dt><i>icode</i></dt>
<dd> <p> generate icode </p>
 </dd>
<dt><i>codegen</i></dt>
<dd> <p> enable code generation </p>
 </dd>
<dt><i>terminal</i></dt>
<dd> <p> compilation terminated </p>
 </dd>
<dt><i>all</i></dt>
<dd> <p> matches all phases </p>
 </dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>JAVACMD</code></dt>
<dd> <p> Specify the <code>java</code> command to be used for running the Scala code. Arguments may be specified as part of the environment variable; spaces, quotation marks, etc., will be passed directly to the shell for expansion. </p>
 </dd>
<dt><code>JAVA_HOME</code></dt>
<dd> <p> Specify JDK/JRE home directory. This directory is used to locate the <code>java</code> command unless <code>JAVACMD</code> variable set. </p>
 </dd>
<dt><code>JAVA_OPTS</code></dt>
<dd> <p> Specify the options to be passed to the <code>java</code> command defined by <code>JAVACMD</code>. </p>
 </dd>
<dd> <p> With Java 1.5 (or newer) one may for example configure the memory usage of the JVM as follows: JAVA_OPTS=&quot;-Xmx512M -Xms16M -Xss16M&quot; </p>
 </dd>
<dd> <p> With GNU Java one may configure the memory usage of the GIJ as follows: JAVA_OPTS=&quot;--mx512m --ms16m&quot; </p>
 </dd>
<dd>  </dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Compile a Scala program to the current directory</dt>
<dd> <p> <code>scalac</code> HelloWorld </p>
 </dd>
<dt>Compile a Scala program to the destination directory <code>classes</code></dt>
<dd> <p> <code>scalac</code> <code>-d</code> classes HelloWorld.scala </p>
 </dd>
<dt>Compile a Scala program using a user-defined <code>java</code> command</dt>
<dd> <p> <code>env JAVACMD</code>=/usr/local/bin/cacao <code>scalac</code> <code>-d</code> classes HelloWorld.scala </p>
 </dd>
<dt>Compile all Scala files found in the source directory <code>src</code> to the destination directory <code>classes</code></dt>
<dd> <p> <code>scalac</code> <code>-d</code> classes src/*.scala </p>
 </dd></dl>
<h2>EXIT STATUS</h2>
<p> <code>scalac</code> returns a zero exist status if it succeeds to compile the specified input files. Non zero is returned in case of failure.  </p>
<h2>AUTHOR</h2>
<p> Written by Martin Odersky and other members of the Scala team.  </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="https://issues.scala-lang.org/.">https://issues.scala-lang.org/.</a>  </p>
<h2>COPYRIGHT</h2>
<p> This is open-source software, available to you under a BSD-like license. See accomponying &quot;copyright&quot; or &quot;LICENSE&quot; file for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fsc/">fsc</a></code>(1), <code><a href="/docs/linux/man/1-scala/">scala</a></code>(1), <code><a href="/docs/linux/man/1-scaladoc/">scaladoc</a></code>(1), <code><a href="/docs/linux/man/1-scalap/">scalap</a></code>(1) </p>
