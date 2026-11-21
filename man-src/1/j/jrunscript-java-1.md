---
title: "jrunscript-java-1(1)"
name: "jrunscript-java-1"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jrunscript-java-1/"
description: "jrunscript – command line script shell"
---

<h2>Name</h2>
<p> jrunscript &#8211; command line script shell </p>
<h2>SYNOPSIS</h2>
<pre><code>
jrunscript[options][arguments...]
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dl>
<dt>options</dt>
<dd> Options, if used, should follow immediately after the command name.</dd>
<dt>arguments</dt>
<dd> Arguments, if used, should follow immediately after options or command name.</dd></dl>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>jrunscript</code> is a command line script shell. jrunscript supports both an interactive (read-eval-print) mode and a batch (-f option) mode of script execution. This is a scripting language independent shell. By default, JavaScript is the language used, but the -l option can be used to specify a different language. Through Java to scripting language communication, jrunscript supports &quot;exploratory programming&quot; style. </p>
<p> <code>NOTE:</code> This tool is <code>experimental</code> and may <code>not</code> be available in future versions of the JDK. </p>
<h2>OPTIONS</h2>
<dl>
<dl>
<dt>-classpath path</dt>
<dd> Specify where to find the user&#8217;s .class files that are accessed by the script.</dd>
<dt>-cp path</dt>
<dd> This is a synonym for -classpath <i>path</i></dd>
<dt>-Dname=value</dt>
<dd> Set a Java system property.</dd>
<dt>-J&lt;flag&gt;</dt>
<dd> Pass &lt;flag&gt; directly to the Java virtual machine on which jrunscript is run.</dd>
<dt>-l language</dt>
<dd> Use the specified scripting language. By default, JavaScript is used. Note that to use other scripting languages, you also need to specify the corresponding script engine&#8217;s jar file using -cp or -classpath option.</dd>
<dt>-e script</dt>
<dd> Evaluate the given script. This option can be used to run &quot;one liner&quot; scripts specified completely on the command line.</dd>
<dt>-encoding encoding</dt>
<dd> Specify the character encoding used while reading script files.</dd>
<dt>-f script-file</dt>
<dd> Evaluate the given script file (batch mode).</dd>
<dt>-f &#8211;</dt>
<dd> Read and evaluate a script from standard input (interactive mode).</dd>
<dt>-help&nbsp;<wbr></dt>
<dd> Output help message and exit.</dd>
<dt>-?&nbsp;<wbr></dt>
<dd> Output help message and exit.</dd>
<dt>-q&nbsp;<wbr></dt>
<dd> List all script engines available and exit.</dd></dl>
</dl>
<h2>ARGUMENTS</h2>
<p> If [arguments&#8230;] are present and if no <code>-e</code> or <code>-f</code> option is used, then the first argument is the script file and the rest of the arguments, if any, are passed as script arguments. If [arguments..] and <code>-e</code> or <code>-f</code> option are used, then all [arguments..] are passed as script arguments. If [arguments..], <code>-e</code> and <code>-f</code> are missing, interactive mode is used. Script arguments are available to a script in an engine variable named &quot;arguments&quot; of type String array. </p>
<h2>EXAMPLES</h2>
<h3>Executing inline scripts</h3>
<pre>
<code>jrunscript -e &quot;print('hello world')&quot;
jrunscript -e &quot;cat('<a rel="nofollow" href="http://java.sun.com')">http://java.sun.com')</a>&quot;</code>
</pre>
<h3>Use specified language and evaluate given script file</h3>
<pre>
<code>jrunscript -l js -f test.js</code>
</pre>
<h3>Interactive mode</h3>
<pre><code>
jrunscript
        js &gt; print('Hello World
');
Hello World
        js &gt; 34 + 55 89.0 js &gt;
    t = new java.lang.Thread(function() { print('Hello World
'); })
            Thread[Thread - 0, 5, main] js &gt; t.start()
                                                 js
        &gt; Hello World
        js
        &gt;
</code></pre>
<h3>Run script file with script arguments</h3>
<pre>
<code>jrunscript test.js arg1 arg2 arg3</code>
</pre>
<p> test.js is script file to execute and arg1, arg2 and arg3 are passed to script as script arguments. Script can access these using &quot;arguments&quot; array.</p>
<h2>SEE ALSO</h2>
<p> If JavaScript is used, then before evaluating any user defined script, jrunscript initializes certain built-in functions and objects. These JavaScript built-ins are documented in <i>jsdocs</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/technotes/tools/share/jsdocs/allclasses-noframe.html.">http://docs.oracle.com/javase/7/docs/technotes/tools/share/jsdocs/allclasses-noframe.html.</a> </p>
<p>&nbsp;<wbr> </p>
