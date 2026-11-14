---
title: "jjs-java-1(1)"
name: "jjs-java-1"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jjs-java-1/"
description: "jjs – Invokes the Nashorn engine."
---

<h2>NAME</h2>
<p> jjs &#8211; Invokes the Nashorn engine.</p>
<h2>SYNOPSIS</h2>
<pre><code>
jjs[options][script - files][--arguments]
</code></pre>
<dl>
<dt><i>options</i></p>
<dd> One or more options of the <code>jjs</code> command, separated by spaces. For more information, see Options.</p>
<dt><i>script-files</i></p>
<dd> One or more script files which you want to interpret using Nashorn, separated by spaces. If no files are specified, an interactive shell is started.</p>
<dt><i>arguments</i></p>
<dd> All values after the double hyphen marker (<code>&#8212;</code>) are passed through to the script or the interactive shell as arguments. These values can be accessed by using the <code>arguments</code> property (see ).</dl>
<h2>DESCRIPTION</h2>
<p> The <code>jjs</code> command-line tool is used to invoke the Nashorn engine. You can use it to interpret one or several script files, or to run an interactive shell.</p>
<h2>OPTIONS</h2>
<p> The options of the <code>jjs</code> command control the conditions under which scripts are interpreted by Nashorn.</p>
<dl>
<dt>-ccs=<i>size</i> , &#8211;class-cache-size=<i>size</i></p>
<dd>
 Sets the class cache size (in bytes). Append the letter <code>k</code> or <code>K</code> to indicate kilobytes (KB), <code>m</code> or <code>M</code> to indicate megabytes (MB), <code>g</code> or <code>G</code> to indicate gigabytes (GB). By default, the class cache size is set to 50 bytes. The following example shows how to set it to 1024 bytes (1 KB): </p>
<pre>
<code>-css=100</code>
</pre>
<pre>
<code>-css=1k</code>
</pre>
<dt>-co, &#8211;compile-only</p>
<dd>
 Compiles the script without running it.</p>
<dt>-cp <i>path</i> , &#8211;classpath <i>path</i></p>
<dd>
 Specifies the path to the supporting class files To set multiple paths, the option can be repeated, or you can separate each path with a colon (:).</p>
<dt>-D<i>name</i>=<i>value</i></p>
<dd>
 Sets a system property to be passed to the script by assigning a value to a property name. The following example shows how to invoke Nashorn in interactive mode and assign <code>myValue</code> to the property named <code>myKey</code>: </p>
<pre>
<code>&gt;&gt; </code><i>jjs -DmyKey=myValue</i>
</pre>
<pre>
<code>jjs&gt; </code><i>java.lang.System.getProperty(&quot;myKey&quot;)</i>
</pre>
<pre>
<code>myValue</code>
</pre>
<pre>
<code>jjs&gt;</code>
</pre>
<p> This option can be repeated to set multiple properties.</p>
<dt>-d=<i>path</i> , &#8211;dump-debug-dir=<i>path</i></p>
<dd>
 Specifies the path to the directory where class files are dumped.</p>
<dt>&#8211;debug-lines</p>
<dd>
 Generates a line number table in the class file. By default, this option is enabled. To disable it, specify <code>&#8211;debug-lines=false</code>.</p>
<dt>&#8211;debug-locals</p>
<dd>
 Generates a local variable table in the class file.</p>
<dt>-doe, &#8211;dump-on-error</p>
<dd>
 Provides a full stack trace when an arror occurs. By default, only a brief error message is printed.</p>
<dt>&#8211;early-lvalue-error</p>
<dd>
 Reports invalid lvalue expressions as early errors (that is, when the code is parsed). By default, this option is enabled. To disable it, specify <code>&#8211;early-lvalue-error=false</code>. When disabled, invalid lvalue expressions will not be reported until the code is executed.</p>
<dt>&#8211;empty-statements</p>
<dd>
 Preserves empty statements in the Java abstract syntax tree.</p>
<dt>-fv, &#8211;fullversion</p>
<dd>
 Prints the full Nashorn version string.</p>
<dt>&#8211;function-statement-error</p>
<dd>
 Prints an error message when a function declaration is used as a statement.</p>
<dt>&#8211;function-statement-warning</p>
<dd>
 Prints a warning message when a function declaration is used as a statement.</p>
<dt>-fx</p>
<dd>
 Launches the script as a JavaFX application.</p>
<dt>-h, -help</p>
<dd>
 Prints the list of options and their descriptions.</p>
<dt>-J<i>option</i></p>
<dd>
 Passes the specified <code>java</code> launcher option to the JVM. The following example shows how to invoke Nashorn in interactive mode and set the maximum memory used by the JVM to 4 GB: </p>
<pre>
<code>&gt;&gt; </code><i>jjs -J-Xmx4g</i>
</pre>
<pre>
<code>jjs&gt; </code><i>java.lang.Runtime.getRuntime().maxMemory()</i>
</pre>
<pre>
<code>3817799680</code>
</pre>
<pre>
<code>jjs&gt;</code>
</pre>
<p> This option can be repeated to pass multiple <code>java</code> command options.</p>
<dt>&#8211;lazy-compilation</p>
<dd>
 Enables lazy code generation strategies (that is, the entire script is not compiled at once). This option is experimental.</p>
<dt>&#8211;loader-per-compile</p>
<dd>
 Creates a new class loader per compile. By default, this option is enabled. To disable it, specify <code>&#8211;loader-per-compile=false</code>.</p>
<dt>&#8211;log=<i>subsystem</i>:<i>level</i></p>
<dd>
 Performs logging at a given level for the specified subsystems. You can specify logging levels for multiple subsystems separating them with commas. For example: </p>
<pre>
<code>--log=fields:finest,codegen:info</code>
</pre>
<dt>&#8211;package=<i>name</i></p>
<dd>
 Specifies the package to which generated class files are added.</p>
<dt>&#8211;parse-only</p>
<dd>
 Parses the code without compiling.</p>
<dt>&#8211;print-ast</p>
<dd>
 Prints the abstract syntax tree.</p>
<dt>&#8211;print-code</p>
<dd>
 Prints bytecode.</p>
<dt>&#8211;print-lower-ast</p>
<dd>
 Prints the lowered abstract syntax tree.</p>
<dt>&#8211;print-lower-parse</p>
<dd>
 Prints the lowered parse tree.</p>
<dt>&#8211;print-no-newline</p>
<dd>
 Forces other <code>&#8211;print*</code> options to print the output on one line.</p>
<dt>&#8211;print-parse</p>
<dd>
 Prints the parse tree.</p>
<dt>&#8211;print-symbols</p>
<dd>
 Prints the symbol table.</p>
<dt>-pcs, &#8211;profile-callsites</p>
<dd>
 Dumps callsite profile data.</p>
<dt>-scripting</p>
<dd>
 Enables shell scripting features.</p>
<dt>&#8211;stderr=<i>filename</i>|<i>stream</i>|<i>tty</i></p>
<dd>
 Redirects the standard error stream to the specified file, stream (for example, to <code>stdout</code>), or text terminal.</p>
<dt>&#8211;stdout=<i>filename</i>|<i>stream</i>|<i>tty</i></p>
<dd>
 Redirects the standard output stream to the specified file, stream (for example, to <code>stderr</code>), or text terminal.</p>
<dt>-strict</p>
<dd>
 Enables strict mode, which enforces stronger adherence to the standard (ECMAScript Edition 5.1), making it easier to detect common coding errors.</p>
<dt>-t=<i>zone</i> , -timezone=<i>zone</i></p>
<dd>
 Sets the specified time zone for script execution. It overrides the time zone set in the OS and used by the <code>Date</code> object.</p>
<dt>-tcs=<i>parameter</i> , &#8211;trace-callsites=<i>parameter</i></p>
<dd>
 Enables callsite trace mode. Possible parameters are the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt>miss</p>
<dd> Trace callsite misses.</p>
<dt>enterexit</p>
<dd> Trace callsite enter/exit.</p>
<dt>objects</p>
<dd> Print object properties.</dl>
</dl>
<dt>&#8211;verify-code</p>
<dd>
 Verifies bytecode before running.</p>
<dt>-v, -version</p>
<dd>
 Prints the Nashorn version string.</p>
<dt>-xhelp</p>
<dd>
 Prints extended help for command-line options.</dl>
<h2>EXAMPLES</h2>
<p> <code>Example 1 Running a Script with Nashorn</code> </p>
<pre>
<code>jjs script.js</code>
</pre>
<p> <code>Example 2 Running Nashorn in Interactive Mode</code> </p>
<pre>
<code>&gt;&gt; </code><i>jjs</i>
</pre>
<pre>
<code>jjs&gt; </code><i>println(&quot;Hello, World!&quot;)</i>
</pre>
<pre>
<code>Hello, World!</code>
</pre>
<pre>
<code>jjs&gt; </code><i>quit()</i>
</pre>
<pre>
<code>&gt;&gt;</code>
</pre>
<p> <code>Example 3 Passing Arguments to Nashorn</code> </p>
<pre>
<code>&gt;&gt; </code><i>jjs -- a b c</i>
</pre>
<pre>
<code>jjs&gt; </code><i>arguments.join(&quot;, &quot;)</i>
</pre>
<pre>
<code>a, b, c</code>
</pre>
<pre>
<code>jjs&gt;</code>
</pre>
<h2>SEE ALSO</h2>
<p> <code>jrunscript</code> </p>
<h2>Index</h2>
