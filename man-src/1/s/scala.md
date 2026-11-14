---
title: "scala(1)"
name: "scala"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scala/"
description: "scala – Run code in the Scala 2 language"
---

<h2 class="name">NAME</h2>
<p> <code>scala</code> &#8211; Run code in the Scala 2 language </p>
<h2>SYNOPSIS</h2>
<p> <code>scala</code> [ &lt;<i>option</i>&gt; ]&#8230; [ &lt;<i>torun</i>&gt; &lt;<i>argument</i>&gt;&#8230; ]</p>
<h2>PARAMETERS</h2>
<dl>
<dt>&lt;<i>compiler-option</i>&gt;</p>
<dd> Any scalac option. See <code><a href="/docs/linux/man/1-scalac/">scalac</a></code>(1).</p>
<dt><code>-howtorun:</code>&lt;<i>how</i>&gt;</p>
<dd> How to execute &lt;<i>torun</i>&gt;, if it is present. Options for &lt;<i>how</i>&gt; are guess (the default), script, and object.</p>
<dt><code>-i</code></p>
<dd> Requests that a file be pre-loaded. It is only meaningful for interactive shells.</p>
<dt><code>-e</code></p>
<dd> Requests that its argument be executed as Scala code.</p>
<dt><code>-savecompiled</code></p>
<dd> Save this compiled version of scripts in order to speed up later executions of the same script. When running a script, save the compiled version of in a file with the same name as the script but with an extension of .jar. On subsequent runs of the same script, the pre-compiled .jar file will be used if it is newer than the script file.</p>
<dt><code>-nocompdaemon</code></p>
<dd> Do not use the <code>fsc</code> offline compiler.</p>
<dt><code>-D</code>property=value</p>
<dd> Set a Java system property. If no value is specified, then the property is set to the empty string.</p>
<dt>&lt;<i>torun</i>&gt;</p>
<dd> A top-level object or a script file to run.</p>
<dt>&lt;<i>argument</i>&gt;</p>
<dd> An arguments to pass to &lt;<i>torun</i>&gt;.</dl>
<h2>DESCRIPTION</h2>
<p> The <code>scala</code> utility runs Scala code using a Java runtime environment. The Scala code to run is specified in one of three ways:</p>
<dl>
<dt> 1.</p>
<dd> With no arguments specified, a Scala shell starts and reads commands interactively.</p>
<dt> 2.</p>
<dd> With -howtorun:object specified, the fully qualified name of a top-level Scala object may be specified. The object should previously have been compiled using <code><a href="/docs/linux/man/1-scalac/">scalac</a></code>(1).</p>
<dt> 3.</p>
<dd> With -howtorun:script specified, a file containing Scala code may be specified.</dl>
<p> If -howtorun: is left as the default (guess), then the <code>scala</code> command will check whether a file of the specified name exists. If it does, then it will treat it as a script file; if it does not, then it will treat it as the name of an object. </p>
<p> In all three cases, arbitrary scalac options may be specified. The most common option is to specify a classpath with -classpath, but see the <code><a href="/docs/linux/man/1-scalac/">scalac</a></code>(1) page for full details. </p>
<p> If an object is specified to run, then that object must be a top-level Scala object with the specified name. The object must define a method <code>main</code> with the following signature:</p>
<dl>
<dt><code>def</code> main(args: Array[String]): Unit</p>
<dd></dl>
<p> The method must return a <code>Unit</code> value, and it must accept a <code>String</code> array as a parameter. All arguments specified on the command line will be passed as arguments to the <code>main</code> method. </p>
<p> If a script file is specified to run, then the file is read and all Scala statements and declarations in the file are processed in order. Any arguments specified will be available via the argsvariable. </p>
<p> Script files may have an optional header that is ignored if present. There are two ways to format the header: either beginning with #! and ending with !#, or beginning with ::#! and ending with ::!#. </p>
<p> Such a header must have each header boundary start at the beginning of a line. Headers can be used to make stand-alone script files, as shown in the examples below. </p>
<p> If scala is run from an <a href="/docs/linux/man/1-sbaz/">sbaz</a>(1) directory, then it will add to its classpath any jars installed in the lib directory of the sbaz directory. Additionally, if no -classpath option is specified, then scala will add &quot;.&quot;, the current directory, to the end of the classpath.</p>
<h2>OPTIONS</h2>
<p> If any compiler options are specified, they must be first in the command line and must be followed by a bare hypen (&quot;-&quot;) character. If no arguments are specified after the optional compiler arguments, then an interactive Scala shell is started. Otherwise, either a script file is run, or a pre-compiled Scala object is run. It is possible to distinguish the last two cases by using an explicit -object or -script flag, but usually the program can guess correctly.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>JAVACMD</code></p>
<dd> Specify the <code>java</code> command to be used for running the Scala code. Arguments may be specified as part of the environment variable; spaces, quotation marks, etc., will be passed directly to the shell for expansion.</p>
<dt><code>JAVA_HOME</code></p>
<dd> Specify JDK/JRE home directory. This directory is used to locate the <code>java</code> command unless <code>JAVACMD</code> variable set.</p>
<dt><code>JAVA_OPTS</code></p>
<dd> Specify the options to be passed to the <code>java</code> command defined by <code>JAVACMD</code>.</p>
<dt>
<dd> With Java 1.5 (or newer) one may for example configure the memory usage of the JVM as follows: JAVA_OPTS=&quot;-Xmx512M -Xms16M -Xss16M&quot;</p>
<dt>
<dd> With GNU Java one may configure the memory usage of the GIJ as follows: JAVA_OPTS=&quot;&#8211;mx512m &#8211;ms16m&quot;</p>
<dt>
<dd>
</dl>
<h2>EXAMPLES</h2>
<p> Here are some examples of running Scala code: </p>
<dl>
<dt>Execute a Scala program generated in the current directory</p>
<dd> <code>scala</code> hello.HelloWorld</p>
<dt>Execute a Scala program generated in a user-defined directory <code>classes</code></p>
<dd> <code>scala</code> <code>-classpath</code> classes hello.HelloWorld</p>
<dt>Execute a Scala program using a user-defined <code>java</code> command</p>
<dd> <code>env JAVACMD</code>=/usr/local/bin/cacao <code>scala</code> <code>-classpath</code> classes hello.HelloWorld</p>
<dt>Execute a Scala program using JVM options</p>
<dd> <code>env JAVACMD</code>=java <code>JAVA_OPTS</code>=&quot;-Dmsg=hello -enableassertions&quot; <code>scala</code> <code>-classpath</code> classes hello.HelloWorld</dl>
<p> Here is a complete Scala script for Unix: </p>
<pre>
#!/bin/sh
exec scala &quot;$0&quot; &quot;$@&quot;
!#
Console.println(&quot;Hello, world!&quot;)
argv.toList foreach Console.println
</pre>
<p> Here is a complete Scala script for MS Windows: </p>
<pre>
::#!
@echo off
call scala %0 %*
goto :eof
::!#
Console.println(&quot;Hello, world!&quot;)
argv.toList foreach Console.println
</pre>
<p> If you want to use the compilation cache to speed up multiple executions of the script, then add -savecompiled to the scala command: </p>
<pre>
#!/bin/sh
exec scala -savecompiled &quot;$0&quot; &quot;$@&quot;
!#
Console.println(&quot;Hello, world!&quot;)
argv.toList foreach Console.println
</pre>
<h2>EXIT STATUS</h2>
<p> The <code>scala</code> command returns a zero exit status if it succeeds. Non zero is returned in case of any error. If a script or top-level object is executed and returns a value, then that return value is passed on to <code>scala</code>.</p>
<h2>AUTHOR</h2>
<p> Written by Martin Odersky and other members of the Scala team.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="https://issues.scala-lang.org/.">https://issues.scala-lang.org/.</a></p>
<h2>COPYRIGHT</h2>
<p> This is open-source software, available to you under a BSD-like license. See accomponying &quot;copyright&quot; or &quot;LICENSE&quot; file for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fsc/">fsc</a></code>(1), <code><a href="/docs/linux/man/1-scalac/">scalac</a></code>(1), <code><a href="/docs/linux/man/1-scaladoc/">scaladoc</a></code>(1), <code><a href="/docs/linux/man/1-scalap/">scalap</a></code>(1) </p>
<h2>Index</h2>
