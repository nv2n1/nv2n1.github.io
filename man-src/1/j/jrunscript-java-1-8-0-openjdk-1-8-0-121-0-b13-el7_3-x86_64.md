---
title: "jrunscript-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64(1)"
name: "jrunscript-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jrunscript-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64/"
description: "jrunscript – Runs a command-line script shell that supports interactive and batch modes. This command is experimental and unsupported."
---

<p>jrunscript &#8211; Runs a command-line script shell that supports interactive and batch modes. This command is experimental and unsupported.</p>
<h2>Synopsis</h2>
<pre><code>jrunscript</code> [<i>options</i>] [<i>arguments</i>]</pre>
<dl>
<dt><i>options</i></p>
<dd>The command-line options. See Options.</p>
<dt><i>arguments</i></p>
<dd>Arguments, when used, follow immediately after options or the command name. See Arguments.</dl>
<h2>Description</h2>
<p>The <code>jrunscript</code> command is a language-independent command-line script shell. The <code>jrunscript</code> command supports both an interactive (read-eval-print) mode and a batch (<code>-f</code> option) mode of script execution. By default, JavaScript is the language used, but the <code>-l</code> option can be used to specify a different language. By using Java to scripting language communication, the <code>jrunscript</code> command supports an exploratory programming style.</p>
<h2>Options</h2>
<dl>
<dt>-classpath <i>path</i></p>
<dd>Indicate where any class files are that the script needs to access.</p>
<dt>-cp <i>path</i></p>
<dd>Same as <code>-classpath</code><code>path</code>.</p>
<dt>-D<i>name</i>=<i>value</i></p>
<dd>Sets a Java system property.</p>
<dt>-J<i>flag</i></p>
<dd>Passes <code>flag</code> directly to the Java Virtual Machine where the <code>jrunscript</code> command is running.</p>
<dt>-I <i>language</i></p>
<dd>Uses the specified scripting language. By default, JavaScript is used. To use other scripting languages, you must specify the corresponding script engine&#8217;s JAR file with the <code>-cp</code> or <code>-classpath</code> option.</p>
<dt>-e <i>script</i></p>
<dd>Evaluates the specified script. This option can be used to run one-line scripts that are specified completely on the command line.</p>
<dt>-encoding <i>encoding</i></p>
<dd>Specifies the character encoding used to read script files.</p>
<dt>-f <i>script-file</i></p>
<dd>Evaluates the specified script file (batch mode).</p>
<dt>-f &#8211;</p>
<dd>Reads and evaluates a script from standard input (interactive mode).</p>
<dt>-help</p>
<dd>Displays a help message and exits.</p>
<dt>-?</p>
<dd>Displays a help message and exits.</p>
<dt>-q</p>
<dd>Lists all script engines available and exits.</dl>
<h2>Arguments</h2>
<p>If arguments are present and if no <code>-e</code> or <code>-f</code> option is used, then the first argument is the script file and the rest of the arguments, if any, are passed to the script. If arguments and <code>-e</code> or the <code>-f</code> option are used, then all arguments are passed to the script. If arguments, <code>-e</code> and <code>-f</code> are missing, then interactive mode is used. Script arguments are available to a script in an engine variable named <code>arguments</code> of type <code>String</code> array.</p>
<h2>Examples</h2>
<h3>Execute Inline Scripts</h3>
<pre><code>jrunscript -e &quot;print('hello world')&quot;</code></pre>
<pre><code>jrunscript -e &quot;cat('<a rel="nofollow" href="http://www.example.com')">http://www.example.com')</a>&quot;</code></pre>
<h3>Use Specified Language And Evaluate The Script File</h3>
<pre><code>jrunscript -l js -f test.js</code></pre>
<h3>Interactive Mode</h3>
<pre><code>jrunscript</code></pre>
<pre><code>js&gt; print('Hello World
');</code></pre>
<pre><code>Hello World</code></pre>
<pre><code>js&gt; 34 + 55</code></pre>
<pre><code>89.0</code></pre>
<pre><code>js&gt; t = new java.lang.Thread(function() { print('Hello World
'); })</code></pre>
<pre><code>Thread[Thread-0,5,main]</code></pre>
<pre><code>js&gt; t.start()</code></pre>
<pre><code>js&gt; Hello World</code></pre>
<pre><code>js&gt;</code></pre>
<h3>Run Script File With Script Arguments</h3>
<p>The test.js file is the script file. The <code>arg1</code>, <code>arg2</code> and <code>arg3</code> arguments are passed to the script. The script can access these arguments with an arguments array. </p>
<pre><code>jrunscript test.js arg1 arg2 arg3</code></pre>
<h2>See Also</h2>
<p>If JavaScript is used, then before it evaluates a user defined script, the <code>jrunscript</code> command initializes certain built-in functions and objects. These JavaScript built-ins are documented in JsDoc-Toolkit at <a rel="nofollow" href="http://code.google.com/p/jsdoc-toolkit/">http://code.google.com/p/jsdoc-toolkit/</a></p>
