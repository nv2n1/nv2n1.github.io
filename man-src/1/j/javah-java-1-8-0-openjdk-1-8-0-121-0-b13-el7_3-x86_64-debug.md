---
title: "javah-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64-debug(1)"
name: "javah-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64-debug"
section: "1"
letter: "j"
url: "/docs/linux/man/1-javah-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64-debug/"
description: "javah – Generates C header and source files from a Java class."
---

<p>javah &#8211; Generates C header and source files from a Java class.</p>
<h2>Synopsis</h2>
<pre><code>javah</code> [ <i>options</i> ] f<i>ully-qualified-class-name ...</i></pre>
<dl>
<dt><i>options</i></dt>
<dd>The command-line options. See Options.</dd>
<dt><i>fully-qualified-class-name</i></dt>
<dd>The fully qualified location of the classes to be converted to C header and source files.</dd></dl>
<h2>Description</h2>
<p>The <code>javah</code> command generates C header and source files that are needed to implement native methods. The generated header and source files are used by C programs to reference an object&#8217;s instance variables from native source code. The <code>.h</code> file contains a <code>struct</code> definition with a layout that parallels the layout of the corresponding class. The fields in the <code>struct</code> correspond to instance variables in the class. </p>
<p> The name of the header file and the structure declared within it are derived from the name of the class. When the class passed to the <code>javah</code> command is inside a package, the package name is added to the beginning of both the header file name and the structure name. Underscores (_) are used as name delimiters. </p>
<p> By default the <code>javah</code> command creates a header file for each class listed on the command line and puts the files in the current directory. Use the <code>-stubs</code> option to create source files. Use the <code>-o</code> option to concatenate the results for all listed classes into a single file. </p>
<p> The Java Native Interface (JNI) does not require header information or stub files. The <code>javah</code> command can still be used to generate native method function prototypes needed for JNI-style native methods. The <code>javah</code> command produces JNI-style output by default and places the result in the <code>.h</code> file.</p>
<h2>Options</h2>
<dl>
<dt>-o <i>outputfile</i></dt>
<dd>Concatenates the resulting header or source files for all the classes listed on the command line into an output file. Only one of <code>-o</code> or <code>-d</code> can be used.</dd>
<dt>-d <i>directory</i></dt>
<dd>Sets the directory where the <code>javah</code> command saves the header files or the stub files. Only one of <code>-d</code> or <code>-o</code> can be used.</dd>
<dt>-stubs</dt>
<dd>Causes the <code>javah</code> command to generate C declarations from the Java object file.</dd>
<dt>-verbose</dt>
<dd>Indicates verbose output and causes the <code>javah</code> command to print a message to <code>stdout</code> about the status of the generated files.</dd>
<dt>-help</dt>
<dd>Prints a help message for <code>javah</code> usage.</dd>
<dt>-version</dt>
<dd>Prints <code>javah</code> command release information.</dd>
<dt>-jni</dt>
<dd>Causes the <code>javah</code> command to create an output file containing JNI-style native method function prototypes. This is the default output; use of <code>-jni</code> is optional.</dd>
<dt>-classpath <i>path</i></dt>
<dd>Specifies the path the <code>javah</code> command uses to look up classes. Overrides the default or the <code>CLASSPATH</code> environment variable when it is set. Directories are separated by colons on Oracle Solaris and semicolons on Windows. The general format for path is: </dd>
<p> <i>Oracle Solaris</i>: </p>
<p> .:<i>your-path</i> </p>
<p> Example: <code>.:/home/avh/classes:/usr/local/java/classes</code> </p>
<p> <i>Windows</i>: </p>
<p> .;<i>your-path</i> </p>
<p> Example: <code>.;C:
</p></dl>
</code>
