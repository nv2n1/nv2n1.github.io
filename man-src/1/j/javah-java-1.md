---
title: "javah-java-1(1)"
name: "javah-java-1"
section: "1"
letter: "j"
url: "/docs/linux/man/1-javah-java-1/"
description: "javah – C Header and Stub File Generator"
---

<h2>Name</h2>
<p> javah &#8211; C Header and Stub File Generator </p>
<p> <code>javah</code> produces C header files and C source files from a Java class. These files provide the connective glue that allow your Java and C code to interact. </p>
<h2>SYNOPSIS</h2>
<pre>
<code>javah [ </code><code>options</code><code> ] fully-qualified-classname. . .</code>
</pre>
<h2>DESCRIPTION</h2>
<p> <code>javah</code> generates C header and source files that are needed to implement native methods. The generated header and source files are used by C programs to reference an object&#8217;s instance variables from native source code. The .h file contains a struct definition whose layout parallels the layout of the corresponding class. The fields in the struct correspond to instance variables in the class. </p>
<p> The name of the header file and the structure declared within it are derived from the name of the class. If the class passed to <code>javah</code> is inside a package, the package name is prepended to both the header file name and the structure name. Underscores (_) are used as name delimiters. </p>
<p> By default <code>javah</code> creates a header file for each class listed on the command line and puts the files in the current directory. Use the <i>-stubs</i> option to create source files. Use the <i>-o</i> option to concatenate the results for all listed classes into a single file. </p>
<p> The new native method interface, Java Native Interface (JNI), does not require header information or stub files. <code>javah</code> can still be used to generate native method function proptotypes needed for JNI-style native methods. <code>javah</code> produces JNI-style output by default, and places the result in the .h file. </p>
<h2>OPTIONS</h2>
<dl>
<dt>
<dd>
<dl>
<dt>-o outputfile</p>
<dd> Concatenates the resulting header or source files for all the classes listed on the command line into <i>outputfile</i>. Only one of <code>-o</code> or <code>-d</code> may be used.</p>
<dt>-d directory</p>
<dd> Sets the directory where <code>javah</code> saves the header files or the stub files. Only one of <code>-d</code> or <code>-o</code> may be used.</p>
<dt>-stubs</p>
<dd> Causes <code>javah</code> to generate C declarations from the Java object file.</p>
<dt>-verbose</p>
<dd> Indicates verbose output and causes <code>javah</code> to print a message to stdout concerning the status of the generated files.</p>
<dt>-help</p>
<dd> Print help message for <code>javah</code> usage.</p>
<dt>-version</p>
<dd> Print out <code>javah</code> version information.</p>
<dt>-jni</p>
<dd> Causes <code>javah</code> to create an output file containing JNI-style native method function prototypes. This is the default output, so use of <code>-jni</code> is optional.</p>
<dt>-classpath path</p>
<dd> Specifies the path <code>javah</code> uses to look up classes. Overrides the default or the CLASSPATH environment variable if it is set. Directories are separated by colons. Thus the general format for <i>path</i> is: </p>
<pre>
<code>   .:&lt;your_path&gt;</code>
</pre>
<p> For example: </p>
<pre>
<code>   .:/home/avh/classes:/usr/local/java/classes</code>
</pre>
<p> As a special convenience, a class path element containing a basename of <i>*</i> is considered equivalent to specifying a list of all the files in the directory with the extension <i>.jar</i> or <i>.JAR</i> (a java program cannot tell the difference between the two invocations). </p>
<p> For example, if directory <i>foo</i> contains <i>a.jar</i> and <i>b.JAR</i>, then the class path element <i>foo/*</i> is expanded to a <i>A.jar:b.JAR</i>, except that the order of jar files is unspecified. All jar files in the specified directory, even hidden ones, are included in the list. A classpath entry consisting simply of <i>*</i> expands to a list of all the jar files in the current directory. The <i>CLASSPATH</i> environment variable, where defined, will be similarly expanded. Any classpath wildcard expansion occurs before the Java virtual machine is started &#8212; no Java program will ever see unexpanded wildcards except by querying the environment. For example; by invoking <i>System.getenv(&quot;CLASSPATH&quot;)</i>.</p>
<dt>-bootclasspath path</p>
<dd> Specifies path from which to load bootstrap classes. By default, the bootstrap classes are the classes implementing the core Java 2 platform located in <i>jre/lib/rt.jar</i> and several other jar files.</p>
<dt>-old</p>
<dd> Specifies that old JDK1.0-style header files should be generated.</p>
<dt>-force</p>
<dd> Specifies that output files should always be written.</p>
<dt>-Joption</p>
<dd> Pass <i>option</i> to the Java virtual machine, where <i>option</i> is one of the options described on the reference page for the <a href="/docs/linux/man/1-java/">java</a>(1). For example, <code>-J-Xms48m</code> sets the startup memory to 48 megabytes.</dl>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt>
<dd>
<dl>
<dt>CLASSPATH</p>
<dd> Used to provide the system a path to user-defined classes. Directories are separated by colons, for example,</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-javac/">javac</a>(1), <a href="/docs/linux/man/1-java/">java</a>(1), <a href="/docs/linux/man/1-jdb/">jdb</a>(1), <a href="/docs/linux/man/1-javap/">javap</a>(1), <a href="/docs/linux/man/1-javadoc/">javadoc</a>(1) </p>
<p>&nbsp;<wbr> </p>
<h2>Index</h2>
