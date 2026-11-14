---
title: "javah-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64(1)"
name: "javah-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64"
section: "1"
letter: "j"
url: "/docs/linux/man/1-javah-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64/"
description: "javah – Generates C header and source files from a Java class."
---

<p>javah &#8211; Generates C header and source files from a Java class.</p>
<h2>Synopsis</h2>
<pre><code>javah</code> [ <i>options</i> ] f<i>ully-qualified-class-name ...</i></pre>
<dl>
<dt><i>options</i></p>
<dd>The command-line options. See Options.</p>
<dt><i>fully-qualified-class-name</i></p>
<dd>The fully qualified location of the classes to be converted to C header and source files.</dl>
<h2>Description</h2>
<p>The <code>javah</code> command generates C header and source files that are needed to implement native methods. The generated header and source files are used by C programs to reference an object&#8217;s instance variables from native source code. The <code>.h</code> file contains a <code>struct</code> definition with a layout that parallels the layout of the corresponding class. The fields in the <code>struct</code> correspond to instance variables in the class. </p>
<p> The name of the header file and the structure declared within it are derived from the name of the class. When the class passed to the <code>javah</code> command is inside a package, the package name is added to the beginning of both the header file name and the structure name. Underscores (_) are used as name delimiters. </p>
<p> By default the <code>javah</code> command creates a header file for each class listed on the command line and puts the files in the current directory. Use the <code>-stubs</code> option to create source files. Use the <code>-o</code> option to concatenate the results for all listed classes into a single file. </p>
<p> The Java Native Interface (JNI) does not require header information or stub files. The <code>javah</code> command can still be used to generate native method function prototypes needed for JNI-style native methods. The <code>javah</code> command produces JNI-style output by default and places the result in the <code>.h</code> file.</p>
<h2>Options</h2>
<dl>
<dt>-o <i>outputfile</i></p>
<dd>Concatenates the resulting header or source files for all the classes listed on the command line into an output file. Only one of <code>-o</code> or <code>-d</code> can be used.</p>
<dt>-d <i>directory</i></p>
<dd>Sets the directory where the <code>javah</code> command saves the header files or the stub files. Only one of <code>-d</code> or <code>-o</code> can be used.</p>
<dt>-stubs</p>
<dd>Causes the <code>javah</code> command to generate C declarations from the Java object file.</p>
<dt>-verbose</p>
<dd>Indicates verbose output and causes the <code>javah</code> command to print a message to <code>stdout</code> about the status of the generated files.</p>
<dt>-help</p>
<dd>Prints a help message for <code>javah</code> usage.</p>
<dt>-version</p>
<dd>Prints <code>javah</code> command release information.</p>
<dt>-jni</p>
<dd>Causes the <code>javah</code> command to create an output file containing JNI-style native method function prototypes. This is the default output; use of <code>-jni</code> is optional.</p>
<dt>-classpath <i>path</i></p>
<dd>Specifies the path the <code>javah</code> command uses to look up classes. Overrides the default or the <code>CLASSPATH</code> environment variable when it is set. Directories are separated by colons on Oracle Solaris and semicolons on Windows. The general format for path is: </p>
<p> <i>Oracle Solaris</i>: </p>
<p> .:<i>your-path</i> </p>
<p> Example: <code>.:/home/avh/classes:/usr/local/java/classes</code> </p>
<p> <i>Windows</i>: </p>
<p> .;<i>your-path</i> </p>
<p> Example: <code>.;C:
