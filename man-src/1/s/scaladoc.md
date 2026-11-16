---
title: "scaladoc(1)"
name: "scaladoc"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scaladoc/"
description: "scaladoc – Documentation generator for the Scala 2 language"
---

<h2 class="name">NAME</h2>
<p> <code>scaladoc</code> &#8211; Documentation generator for the Scala 2 language </p>
<h2>SYNOPSIS</h2>
<p> <code>scaladoc</code> [ &lt;<i>options</i>&gt; ] &lt;<i>source files</i>&gt;</p>
<h2>PARAMETERS</h2>
<dl>
<dt>&lt;<i>options</i>&gt;</dt>
<dd> Command line options. See <code>OPTIONS</code> below.</dd>
<dt>&lt;<i>source files</i>&gt;</dt>
<dd> One or more source files to be compiled (such as MyClass.scala).</dd></dl>
<h2>DESCRIPTION</h2>
<p> The <code>scaladoc</code> tool reads class and object definitions, written in the Scala 2 programming language, and generates their API as HTML files. </p>
<p> By default, the generator puts each HTML file in the same directory as its source file. You can specify a separate destination directory with <code>-d</code> (see <code>OPTIONS</code>, below). </p>
<p> The recognised format of comments in source is described in the online documentation</p>
<h2>OPTIONS</h2>
<h3>Standard Options</h3>
<dl>
<dt><code>-d</code> &lt;<i>directory</i>&gt;</dt>
<dd> Specify where to generate documentation.</dd>
<dt><code>-version</code></dt>
<dd> Print product version and exit.</dd>
<dt><code>-help</code></dt>
<dd> Print a synopsis of available options.</dd></dl>
<h3>Documentation Options</h3>
<dl>
<dt><code>-doc-title</code> &lt;<i>title</i>&gt;</dt>
<dd> Define the overall title of the documentation, typically the name of the library being documented.</dd>
<dt><code>-doc-version</code> &lt;<i>version</i>&gt;</dt>
<dd> Define the overall version number of the documentation, typically the version of the library being documented.</dd>
<dt><code>-doc-source-url</code> &lt;<i>url</i>&gt;</dt>
<dd> Define a URL to be concatenated with source locations for link to source files.</dd>
<dt><code>-doc-external-doc</code> &lt;<i>external-doc</i>&gt;</dt>
<dd> Define a comma-separated list of classpath_entry_path#doc_URL pairs describing external dependencies.</dd></dl>
<h3>Compiler Options</h3>
<dl>
<dt><code>-verbose</code></dt>
<dd> Output messages about what the compiler is doing</dd>
<dt><code>-deprecation</code></dt>
<dd> Indicate whether source should be compiled with deprecation information; defaults to off (accepted values are: on, off, yes and no)</dd>
<dt>
</dt><dd> Available since Scala version 2.2.1</dd>
<dt><code>-classpath</code> &lt;<i>path</i>&gt;</dt>
<dd> Specify where to find user class files (on Unix-based systems a colon-separated list of paths, on Windows-based systems, a semicolon-separate list of paths). This does not override the built-in (&quot;boot&quot;) search path.</dd>
<dt>
</dt><dd> The default class path is the current directory. Setting the CLASSPATH variable or using the -classpath command-line option overrides that default, so if you want to include the current directory in the search path, you must include &quot;.&quot; in the new settings.</dd>
<dt><code>-sourcepath</code> &lt;<i>path</i>&gt;</dt>
<dd> Specify where to find input source files.</dd>
<dt><code>-bootclasspath</code> &lt;<i>path</i>&gt;</dt>
<dd> Override location of bootstrap class files (where to find the standard built-in classes, such as &quot;scala.List&quot;).</dd>
<dt><code>-extdirs</code> &lt;<i>dirs</i>&gt;</dt>
<dd> Override location of installed extensions.</dd>
<dt><code>-encoding</code> &lt;<i>encoding</i>&gt;</dt>
<dd> Specify character encoding used by source files.</dd>
<dt>
</dt><dd> The default value is platform-specific (Linux: &quot;UTF8&quot;, Windows: &quot;Cp1252&quot;). Executing the following code in the Scala interpreter will return the default value on your system:</dd>
<dt>
</dt><dd> <code> scala&gt; </code>new java.io.InputStreamReader(System.in).getEncoding</dd>
</dl>
<h2>EXIT STATUS</h2>
<p> <code>scaladoc</code> returns a zero exit status if it succeeds at processing the specified input files. Non zero is returned in case of failure.</p>
<h2>AUTHORS</h2>
<p> This version of Scaladoc was written by Gilles Dubochet with contributions by Pedro Furlanetto and Johannes Rudolph. It is based on the original Scaladoc (Sean McDirmid, Geoffrey Washburn, Vincent Cremet and St?phane Micheloud), on vScaladoc (David Bernard), as well as on an unreleased version of Scaladoc 2 (Manohar Jonnalagedda).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fsc/">fsc</a></code>(1), <code><a href="/docs/linux/man/1-scala/">scala</a></code>(1), <code><a href="/docs/linux/man/1-scalac/">scalac</a></code>(1), <code><a href="/docs/linux/man/1-scalap/">scalap</a></code>(1) </p>
<h2>Index</h2>
