---
title: "rhino(1)"
name: "rhino"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rhino/"
description: "rhino – invokes the JavaScript shell for running scripts in batch mode or interactive"
---

<h2 class="name">NAME</h2>
<p> rhino &#8211; invokes the JavaScript shell for running scripts in batch mode or interactive</p>
<h2>SYNOPSIS</h2>
<p> <code>rhino</code> <i>[options]</i> <i>script_filename_or_url</i> <i>[script_arguments]</i> </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>rhino</code> command. </p>
<p> <code>rhino</code> is a start script for the rhino JavaScript shell which provides a simple way to run scripts in batch mode or an interactive environment for exploratory programming. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-?, -help</p>
<dd> Displays help messages.</p>
<dt>-w</p>
<dd> Enable warnings.</p>
<dt>-e&nbsp;<wbr><i>script_source</i></p>
<dd> Executes script_source as a JavaScript script.</p>
<dt>-f&nbsp;<wbr><i>script_filename_or_url</i></p>
<dd> Reads script_filename_or_url content and execute it as a JavaScript script.</p>
<dt>-opt, -O&nbsp;<wbr><i>optLevel</i></p>
<dd> Optimizes at level optLevel, which must be an integer between 0 and 9.</p>
<dt>-version&nbsp;<wbr><i>versionNumber</i></p>
<dd> Specifies the language version to compile with. The string versionNumber must be one of 100, 110, 120, 130, 140, 150, 160, 170 or 180. See JavaScript Language Versions for more information on language versions.</p>
<dt>-modules&nbsp;<wbr><i>uri</i></p>
<dd> Add a single path or URL element to the CommonJS module search path. (implies -require)</p>
<dt>-require</p>
<dd> Enable CommonJS module support.</p>
<dt>-sandbox</p>
<dd> Enable CommonJS sandbox mode. (implies -require)</p>
<dt>-debug</p>
<dd> Generate debug code.</p>
<dt>-strict</p>
<dd> Enable strict mode warnings.</p>
<dt>-fatal-warnings</p>
<dd> Treat warnings as errors.</p>
<dt>-encoding&nbsp;<wbr><i>charset</i></p>
<dd> Use specified character encoding as default when reading scripts. </p>
</dl>
<h2>PREDEFINED PROPERTIES</h2>
<p> Scripts executing in the shell have access to some additional properties of the top-level object. </p>
<dl>
<dt>arguments</p>
<dd> The arguments object is an array containing the strings of all the arguments given at the command line when the shell was invoked.</p>
<dt>environment</p>
<dd> Returns the current environment object.</p>
<dt>history</p>
<dd> Displays the shell command history.</p>
<dt>help()</p>
<dd> Executing the help function will print usage and help messages.</p>
<dt>defineClass(<i>className</i>)</p>
<dd> Define an extension using the Java class named with the string argument className. Uses ScriptableObject.defineClass() to define the extension.</p>
<dt>deserialize(<i>filename</i>)</p>
<dd> Restore from the specified file an object previously written by a call to serialize.</p>
<dt>gc()</p>
<dd> Runs the garbage collector.</p>
<dt>load(<i>[filename,&#8230;]</i>)</p>
<dd> Load JavaScript source files named by string arguments. If multiple arguments are given, each file is read in and executed in turn.</p>
<dt>loadClass(<i>className</i>)</p>
<dd> Load and execute the class named by the string argument className. The class must be a class that implements the Script interface, as will any script compiled by jsc.</p>
<dt>print(<i>[expr&#8230;]</i>)</p>
<dd> Evaluate and print expressions. Evaluates each expression, converts the result to a string, and prints it.</p>
<dt>readFile(<i>path[,characterCoding]</i>)</p>
<dd> Read given file and convert its bytes to a string using the specified character coding or default character coding if explicit coding argument is not given.</p>
<dt>readUrl(<i>url[,characterCoding]</i>)</p>
<dd> Open an input connection to the given string url, read all its bytes and convert them to a string using the specified character coding or default character coding if explicit coding argument is not given.</p>
<dt>runCommand(<i>commandName,[arg,&#8230;][options]</i>)</p>
<dd> Execute the specified command with the given argument and options as a separate process and return the exit status of the process. For details, see JavaDoc for org.mozilla.javascript.tools.shell.Global#runCommand.</p>
<dt>seal(<i>object</i>)</p>
<dd> Seal the specified object so any attempt to add, delete or modify its properties would throw an exception.</p>
<dt>serialize(<i>object,filename</i>)</p>
<dd> Serialize the given object to the specified file.</p>
<dt>spawn(<i>functionOrScript</i>)</p>
<dd> Run the given function or script in a different thread.</p>
<dt>sync(<i>function</i>)</p>
<dd> creates a synchronized function (in the sense of a Java synchronized method) from an existing function. The new function synchronizes on the this object of its invocation.</p>
<dt>quit()</p>
<dd> Quit shell. The shell will also quit in interactive mode if an end-of-file character is typed at the prompt.</p>
<dt>version(<i>[number]</i>)</p>
<dd> Get or set JavaScript version number. If no argument is supplied, the current version number is returned. If an argument is supplied, it is expected to be one of 100, 110, 120, 130, 140, 150, 160, 170 or 180 to indicate JavaScript version 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7 or 1.8 respectively. </p>
</dl>
<h2>SEE ALSO</h2>
<p> The online documentation under <i><a rel="nofollow" href="http://www.mozilla.org/rhino/shell.html">http://www.mozilla.org/rhino/shell.html</a></i> </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Wolfgang Baer &lt;WBaer [at] gmx.de&gt;, with modifications by Elliott Baron &lt;ebaron [at] redhat.com&gt;. </p>
<h2>Index</h2>
