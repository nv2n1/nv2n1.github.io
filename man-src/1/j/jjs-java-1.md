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
<dt><i>options</i></dt>
<dd> One or more options of the <code>jjs</code> command, separated by spaces. For more information, see Options.</dd>
<dt><i>script-files</i></dt>
<dd> One or more script files which you want to interpret using Nashorn, separated by spaces. If no files are specified, an interactive shell is started.</dd>
<dt><i>arguments</i></dt>
<dd> All values after the double hyphen marker (<code>&#8212;</code>) are passed through to the script or the interactive shell as arguments. These values can be accessed by using the <code>arguments</code> property (see ).</dd></dl>
<h2>DESCRIPTION</h2>
<p> The <code>jjs</code> command-line tool is used to invoke the Nashorn engine. You can use it to interpret one or several script files, or to run an interactive shell.</p>
<h2>OPTIONS</h2>
<p> The options of the <code>jjs</code> command control the conditions under which scripts are interpreted by Nashorn.</p>
<dl>
<dt>-ccs=<i>size</i> , &#8211;class-cache-size=<i>size</i></dt>
<dd>
 Sets the class cache size (in bytes). Append the letter <code>k</code> or <code>K</code> to indicate kilobytes (KB), <code>m</code> or <code>M</code> to indicate megabytes (MB), <code>g</code> or <code>G</code> to indicate gigabytes (GB). By default, the class cache size is set to 50 bytes. The following example shows how to set it to 1024 bytes (1 KB): </dd>
<pre>
<code>-css=100</code>
</pre>
<pre>
<code>-css=1k</code>
</pre>
<dt>-co, &#8211;compile-only</dt>
<dd>
 Compiles the script without running it.</dd>
<dt>-cp <i>path</i> , &#8211;classpath <i>path</i></dt>
<dd>
 Specifies the path to the supporting class files To set multiple paths, the option can be repeated, or you can separate each path with a colon (:).</dd>
<dt>-D<i>name</i>=<i>value</i></dt>
<dd>
 Sets a system property to be passed to the script by assigning a value to a property name. The following example shows how to invoke Nashorn in interactive mode and assign <code>myValue</code> to the property named <code>myKey</code>: </dd>
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
<dt>-d=<i>path</i> , &#8211;dump-debug-dir=<i>path</i></dt>
<dd>
 Specifies the path to the directory where class files are dumped.</dd>
<dt>&#8211;debug-lines</dt>
<dd>
 Generates a line number table in the class file. By default, this option is enabled. To disable it, specify <code>&#8211;debug-lines=false</code>.</dd>
<dt>&#8211;debug-locals</dt>
<dd>
 Generates a local variable table in the class file.</dd>
<dt>-doe, &#8211;dump-on-error</dt>
<dd>
 Provides a full stack trace when an arror occurs. By default, only a brief error message is printed.</dd>
<dt>&#8211;early-lvalue-error</dt>
<dd>
 Reports invalid lvalue expressions as early errors (that is, when the code is parsed). By default, this option is enabled. To disable it, specify <code>&#8211;early-lvalue-error=false</code>. When disabled, invalid lvalue expressions will not be reported until the code is executed.</dd>
<dt>&#8211;empty-statements</dt>
<dd>
 Preserves empty statements in the Java abstract syntax tree.</dd>
<dt>-fv, &#8211;fullversion</dt>
<dd>
 Prints the full Nashorn version string.</dd>
<dt>&#8211;function-statement-error</dt>
<dd>
 Prints an error message when a function declaration is used as a statement.</dd>
<dt>&#8211;function-statement-warning</dt>
<dd>
 Prints a warning message when a function declaration is used as a statement.</dd>
<dt>-fx</dt>
<dd>
 Launches the script as a JavaFX application.</dd>
<dt>-h, -help</dt>
<dd>
 Prints the list of options and their descriptions.</dd>
<dt>-J<i>option</i></dt>
<dd>
 Passes the specified <code>java</code> launcher option to the JVM. The following example shows how to invoke Nashorn in interactive mode and set the maximum memory used by the JVM to 4 GB: </dd>
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
<dt>&#8211;lazy-compilation</dt>
<dd>
 Enables lazy code generation strategies (that is, the entire script is not compiled at once). This option is experimental.</dd>
<dt>&#8211;loader-per-compile</dt>
<dd>
 Creates a new class loader per compile. By default, this option is enabled. To disable it, specify <code>&#8211;loader-per-compile=false</code>.</dd>
<dt>&#8211;log=<i>subsystem</i>:<i>level</i></dt>
<dd>
 Performs logging at a given level for the specified subsystems. You can specify logging levels for multiple subsystems separating them with commas. For example: </dd>
<pre>
<code>--log=fields:finest,codegen:info</code>
</pre>
<dt>&#8211;package=<i>name</i></dt>
<dd>
 Specifies the package to which generated class files are added.</dd>
<dt>&#8211;parse-only</dt>
<dd>
 Parses the code without compiling.</dd>
<dt>&#8211;print-ast</dt>
<dd>
 Prints the abstract syntax tree.</dd>
<dt>&#8211;print-code</dt>
<dd>
 Prints bytecode.</dd>
<dt>&#8211;print-lower-ast</dt>
<dd>
 Prints the lowered abstract syntax tree.</dd>
<dt>&#8211;print-lower-parse</dt>
<dd>
 Prints the lowered parse tree.</dd>
<dt>&#8211;print-no-newline</dt>
<dd>
 Forces other <code>&#8211;print*</code> options to print the output on one line.</dd>
<dt>&#8211;print-parse</dt>
<dd>
 Prints the parse tree.</dd>
<dt>&#8211;print-symbols</dt>
<dd>
 Prints the symbol table.</dd>
<dt>-pcs, &#8211;profile-callsites</dt>
<dd>
 Dumps callsite profile data.</dd>
<dt>-scripting</dt>
<dd>
 Enables shell scripting features.</dd>
<dt>&#8211;stderr=<i>filename</i>|<i>stream</i>|<i>tty</i></dt>
<dd>
 Redirects the standard error stream to the specified file, stream (for example, to <code>stdout</code>), or text terminal.</dd>
<dt>&#8211;stdout=<i>filename</i>|<i>stream</i>|<i>tty</i></dt>
<dd>
 Redirects the standard output stream to the specified file, stream (for example, to <code>stderr</code>), or text terminal.</dd>
<dt>-strict</dt>
<dd>
 Enables strict mode, which enforces stronger adherence to the standard (ECMAScript Edition 5.1), making it easier to detect common coding errors.</dd>
<dt>-t=<i>zone</i> , -timezone=<i>zone</i></dt>
<dd>
 Sets the specified time zone for script execution. It overrides the time zone set in the OS and used by the <code>Date</code> object.</dd>
<dt>-tcs=<i>parameter</i> , &#8211;trace-callsites=<i>parameter</i></dt>
<dd>
 Enables callsite trace mode. Possible parameters are the following:</dd>
<dl>
<dl>
<dt>miss</dt>
<dd> Trace callsite misses.</dd>
<dt>enterexit</dt>
<dd> Trace callsite enter/exit.</dd>
<dt>objects</dt>
<dd> Print object properties.</dd></dl>
</dl>
<dt>&#8211;verify-code</dt>
<dd>
 Verifies bytecode before running.</dd>
<dt>-v, -version</dt>
<dd>
 Prints the Nashorn version string.</dd>
<dt>-xhelp</dt>
<dd>
 Prints extended help for command-line options.</dd></dl>
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
