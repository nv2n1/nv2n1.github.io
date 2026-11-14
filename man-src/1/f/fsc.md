---
title: "fsc(1)"
name: "fsc"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fsc/"
description: "fsc – Fast offline compiler for the Scala 2 language"
---

<h2 class="name">NAME</h2>
<p> <code>fsc</code> &#8211; Fast offline compiler for the Scala 2 language </p>
<h2>SYNOPSIS</h2>
<p> <code>fsc</code> [ &lt;<i>options</i>&gt; ] &lt;<i>source files</i>&gt;</p>
<h2>PARAMETERS</h2>
<dl>
<dt>&lt;<i>options</i>&gt;</p>
<dd> Command line options. See <code>OPTIONS</code> below.</p>
<dt>&lt;<i>source files</i>&gt;</p>
<dd> One or more source files to be compiled (such as MyClass.scala).</dl>
<h2>OPTIONS</h2>
<p> The offline compiler supports all options of <code>scalac</code> plus the following: </p>
<dl>
<dt><code>-reset</code></p>
<dd> Reset compile server caches.</p>
<dt><code>-shutdown</code></p>
<dd> Shut down the compilation daemon. The daemon attempts to restart itself as necessary, but sometimes an explicit shutdown is required. A common example is if jars on the class path have changed.</p>
<dt><code>-server</code> &lt;<i>hostname:portnumber</i>&gt;</p>
<dd> Specify compile server host at port number. Usually this option is not needed. Note that the hostname must be for a host that shares the same filesystem.</p>
<dt><code>-J</code>&lt;<i>flag</i>&gt;</p>
<dd> Pass &lt;<i>flag</i>&gt; directly to the Java VM for the compilation daemon.</dl>
<h2>DESCRIPTION</h2>
<p> The <code>fsc</code> tool submits Scala compilation jobs to a compilation daemon. The first time it is executed, the daemon is started automatically. On subsequent runs, the same daemon can be reused, thus resulting in a faster compilation. The tool is especially effective when repeatedly compiling with the same class paths, because the compilation daemon can reuse a compiler instance. </p>
<p> The compilation daemon is smart enough to flush its cached compiler when the class path changes. However, if the contents of the class path change, for example due to upgrading a library, then the daemon should be explicitly shut down with <code>-shutdown</code>. </p>
<p> Note that the <code>scala</code> script runner will also use the offline compiler by default, with the same advantages and caveats.</p>
<h2>EXAMPLE</h2>
<p> The following session shows a typical speed up due to using the offline compiler. </p>
<pre><code>
&gt; fsc - verbose - d / tmp test.scala... [Port number:32834][Starting new Scala compile server instance][Classpath = ...][loaded directory path... in 692ms]...[parsing test.scala]...[total in 943ms] &gt; fsc - verbose - d / tmp test.scala... [Port number:32834][parsing test.scala]...[total in 60ms] &gt; fsc - verbose - d / tmp test.scala... [Port number:32834][parsing test.scala]...[total in 42ms] &gt; fsc - verbose - shutdown[Scala compile server exited]
</code></pre>
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
<h2>EXIT STATUS</h2>
<p> <code>fsc</code> returns a zero exit status if it succeeds to compile the specified input files. Non zero is returned in case of failure.</p>
<h2>AUTHOR</h2>
<p> Written by Martin Odersky and other members of the Scala team.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="https://issues.scala-lang.org/.">https://issues.scala-lang.org/.</a></p>
<h2>COPYRIGHT</h2>
<p> This is open-source software, available to you under a BSD-like license. See accomponying &quot;copyright&quot; or &quot;LICENSE&quot; file for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-scala/">scala</a></code>(1), <code><a href="/docs/linux/man/1-scalac/">scalac</a></code>(1), <code><a href="/docs/linux/man/1-scaladoc/">scaladoc</a></code>(1), <code><a href="/docs/linux/man/1-scalap/">scalap</a></code>(1) </p>
<h2>Index</h2>
