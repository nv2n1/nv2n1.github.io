---
title: "scalac(1)"
name: "scalac"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scalac/"
description: "scalac – Compiler for the Scala 2 language"
---

<h2 class="name">NAME</h2>
<p> <code>scalac</code> &#8211; Compiler for the Scala 2 language </p>
<h2>SYNOPSIS</h2>
<p> <code>scalac</code> [ &lt;<i>options</i>&gt; ] &lt;<i>source files</i>&gt;</p>
<h2>PARAMETERS</h2>
<dl>
<dt>&lt;<i>options</i>&gt;</p>
<dd> Command line options. See <code>OPTIONS</code> below.</p>
<dt>&lt;<i>source files</i>&gt;</p>
<dd> One or more source files to be compiled (such as MyClass.scala).</dl>
<h2>DESCRIPTION</h2>
<p> The <code>scalac</code> tool reads class and object definitions, written in the Scala programming language, and compiles them into bytecode class files. </p>
<p> By default, the compiler puts each class file in the same directory as its source file. You can specify a separate destination directory with -d (see <code>OPTIONS</code>, below).</p>
<h2>OPTIONS</h2>
<p> The compiler has a set of standard options that are supported on the current development environment and will be supported in future releases. An additional set of non-standard options are specific to the current virtual machine implementation and are subject to change in the future. Non-standard options begin with <code>-X</code>.</p>
<h3>Standard Options</h3>
<dl>
<dt><code>-D</code>property=value</p>
<dd> Pass <code>-D</code>property=value directly to the runtime system.</p>
<dt><code>-J</code>&lt;<i>flag</i>&gt;</p>
<dd> Pass &lt;<i>flag</i>&gt; directly to the runtime system.</p>
<dt><code>-P:</code>&lt;<i>plugin:opt</i>&gt;</p>
<dd> Pass an option to a plugin</p>
<dt><code>-X</code></p>
<dd> Print a synopsis of advanced options.</p>
<dt><code>-bootclasspath</code> &lt;<i>path</i>&gt;</p>
<dd> Override location of bootstrap class files (where to find the standard built-in classes, such as &quot;scala.List&quot;).</p>
<dt><code>-classpath</code> &lt;<i>path</i>&gt;</p>
<dd> Specify where to find user class files (on Unix-based systems a colon-separated list of paths, on Windows-based systems, a semicolon-separate list of paths). This does not override the built-in (&quot;boot&quot;) search path.</p>
<dt>
<dd> The default class path is the current directory. Setting the CLASSPATH variable or using the -classpath command-line option overrides that default, so if you want to include the current directory in the search path, you must include &quot;.&quot; in the new settings.</p>
<dt>
<dd>
<dt><code>-d</code> &lt;<i>directory|jar</i>&gt;</p>
<dd> Specify where to place generated class files.</p>
<dt><code>-deprecation</code></p>
<dd> Emit warning and location for usages of deprecated APIs.</p>
<dt>
<dd> Available since Scala version 2.2.1</p>
<dt>
<dd>
<dt><code>-encoding</code> &lt;<i>encoding</i>&gt;</p>
<dd> Specify character encoding used by source files.</p>
<dt>
<dd> The default value is platform-specific (Linux: &quot;UTF8&quot;, Windows: &quot;Cp1252&quot;). Executing the following code in the Scala interpreter will return the default value on your system:</p>
<dt>
<dd> <code> scala&gt; </code>new java.io.InputStreamReader(System.in).getEncoding</p>
<dt>
<dd>
<dt><code>-explaintypes</code></p>
<dd> Explain type errors in more detail.</p>
<dt><code>-extdirs</code> &lt;<i>dirs</i>&gt;</p>
<dd> Override location of installed extensions.</p>
<dt><code>-g:</code>{none,source,line,vars,notailcalls}</p>
<dd> &quot;none&quot; generates no debugging info,</p>
<dt>
<dd> &quot;source&quot; generates only the source file attribute,</p>
<dt>
<dd> &quot;line&quot; generates source and line number information,</p>
<dt>
<dd> &quot;vars&quot; generates source, line number and local variable information,</p>
<dt>
<dd> &quot;notailcalls&quot; generates all of the above and <i>will not</i> perform tail call optimization.</p>
<dt>
<dd>
<dt><code>-help</code></p>
<dd> Print a synopsis of standard options.</p>
<dt><code>-javabootclasspath</code> &lt;<i>path</i>&gt;</p>
<dd> Override Java boot classpath.</p>
<dt><code>-javaextdirs</code> &lt;<i>path</i>&gt;</p>
<dd> Override Java extdirs classpath.</p>
<dt><code>-no-specialization</code></p>
<dd> Ignore <i>@specialize</i> annotations.</p>
<dt><code>-nobootcp</code></p>
<dd> Do not use the boot classpath for the Scala jar files.</p>
<dt><code>-nowarn</code></p>
<dd> Generate no warnings</p>
<dt><code>-optimise</code></p>
<dd> Generates faster bytecode by applying optimisations to the program.</p>
<dt><code>-print</code></p>
<dd> Print program with all Scala-specific features removed.</p>
<dt><code>-sourcepath</code> &lt;<i>path</i>&gt;</p>
<dd> Specify location(s) of source files.</p>
<dt><code>-target:</code>&lt;<i>target</i>&gt;</p>
<dd> Specify which backend to use (jvm-1.5,msil).</p>
<dt>
<dd> The default value is &quot;jvm-1.5&quot; (was &quot;jvm-1.4&quot; up to Scala version 2.6.1).</p>
<dt>
<dd>
<dt><code>-toolcp</code> &lt;<i>path</i>&gt;</p>
<dd> Add to the runner classpath.</p>
<dt><code>-unchecked</code></p>
<dd> Enable detailed unchecked (erasure) warnings</p>
<dt>
<dd> Non variable type-arguments in type patterns are unchecked since they are eliminated by erasure</p>
<dt>
<dd> Available since Scala version 2.3.0</p>
<dt>
<dd>
<dt><code>-uniqid</code></p>
<dd> Uniquely tag all identifiers in debugging output.</p>
<dt><code>-verbose</code></p>
<dd> Output messages about what the compiler is doing</p>
<dt><code>-version</code></p>
<dd> Print product version and exit.</p>
<dt><code>@</code>&lt;<i>file</i>&gt;</p>
<dd> A text file containing compiler arguments (options and source files)</dl>
<h3>Advanced Options</h3>
<dl>
<dt><code>-Xassem-extdirs</code> &lt;<i>dirs</i>&gt;</p>
<dd> (Requires -target:msil) List of directories containing assemblies. default:lib.</p>
<dt><code>-Xassem-name</code> &lt;<i>file</i>&gt;</p>
<dd> (Requires -target:msil) Name of the output assembly.</p>
<dt><code>-Xassem-path</code> &lt;<i>path</i>&gt;</p>
<dd> (Requires -target:msil) List of assemblies referenced by the program.</p>
<dt><code>-Xcheck-null</code></p>
<dd> Warn upon selection of nullable reference</p>
<dt><code>-Xcheckinit</code></p>
<dd> Wrap field accessors to throw an exception on uninitialized access.</p>
<dt><code>-Xdisable-assertions</code></p>
<dd> Generate no assertions and assumptions</p>
<dt><code>-Xelide-below</code> &lt;<i>n</i>&gt;</p>
<dd> Calls to <i>@elidable</i> methods are omitted if method priority is lower than argument.</p>
<dt><code>-Xexperimental</code></p>
<dd> Enable experimental extensions</p>
<dt><code>-Xfatal-warnings</code></p>
<dd> Fail the compilation if there are any warnings.</p>
<dt><code>-Xfuture</code></p>
<dd> Turn on future language features.</p>
<dt><code>-Xgenerate-phase-graph</code> &lt;<i>file</i>&gt;</p>
<dd> Generate the phase graphs (outputs .dot files) to fileX.dot.</p>
<dt><code>-Xlint</code></p>
<dd> Enable recommended additional warnings.</p>
<dt><code>-Xlog-implicits</code></p>
<dd> Show more detail on why some implicits are not applicable.</p>
<dt><code>-Xmax-classfile-name</code> &lt;<i>n</i>&gt;</p>
<dd> Maximum filename length for generated classes.</p>
<dt><code>-Xmigration</code></p>
<dd> Warn about constructs whose behavior may have changed between 2.7 and 2.8.</p>
<dt><code>-Xno-forwarders</code></p>
<dd> Do not generate static forwarders in mirror classes.</p>
<dt><code>-Xno-uescape</code></p>
<dd> Disable handling of 
