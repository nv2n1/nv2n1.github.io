---
title: "jjs(1)"
name: "jjs"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jjs/"
description: "jjs – Invokes the Nashorn engine."
---

<h2 class="name">NAME</h2>
<p> jjs &#8211; Invokes the Nashorn engine. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
<dd>
<pre><code>
jjs[options][script - files][--arguments]
</code></pre>
</dl>
<p> <i>options</i></p>
<dl>
<dt>
<dd> One or more options of the <code>jjs</code> command, separated by spaces. For more information, see Options.</dl>
<p> <i>script-files</i></p>
<dl>
<dt>
<dd> One or more script files which you want to interpret using Nashorn, separated by spaces. If no files are specified, an interactive shell is started.</dl>
<p> <i>arguments</i></p>
<dl>
<dt>
<dd> All values after the double hyphen marker (<code>&#8212;</code>) are passed through to the script or the interactive shell as arguments. These values can be accessed by using the <code>arguments</code> property (see Example 3).</dl>
<h2>DESCRIPTION</h2>
<p> The <code>jjs</code> command-line tool is used to invoke the Nashorn engine. You can use it to interpret one or several script files, or to run an interactive shell.</p>
<h2>OPTIONS</h2>
<p> The options of the <code>jjs</code> command control the conditions under which scripts are interpreted by Nashorn. </p>
<p> -cp <i>path</i><br />
 -classpath <i>path</i></p>
<dl>
<dt>
<dd> Specifies the path to the supporting class files To set multiple paths, the option can be repeated, or you can separate each path with a colon (:).</dl>
<p> -D<i>name</i>=<i>value</i></p>
<dl>
<dt>
<dd> Sets a system property to be passed to the script by assigning a value to a property name. The following example shows how to invoke Nashorn in interactive mode and assign <code>myValue</code> to the property named <code>myKey</code>: </p>
<dl>
<dt>
<dd>
<pre>
<code>&gt;&gt; </code><code>jjs -DmyKey=myValue</code>
<code>jjs&gt; </code><code>java.lang.System.getProperty(&quot;myKey&quot;)</code>
<code>myValue</code>
<code>jjs&gt;</code>
 
</pre>
</dl>
<p> This option can be repeated to set multiple properties.</dl>
<p> -doe<br />
 &#8211;dump-on-error</p>
<dl>
<dt>
<dd> Provides a full stack trace when an error occurs. By default, only a brief error message is printed.</dl>
<p> -fv<br />
 &#8211;fullversion</p>
<dl>
<dt>
<dd> Prints the full Nashorn version string.</dl>
<p> -fx</p>
<dl>
<dt>
<dd> Launches the script as a JavaFX application.</dl>
<p> -h<br />
 -help</p>
<dl>
<dt>
<dd> Prints the list of options and their descriptions.</dl>
<p> &#8211;language=[es5]</p>
<dl>
<dt>
<dd> Specifies the ECMAScript language version. The default version is ES5.</dl>
<p> -ot<br />
 &#8211;optimistic-types=[true|false]</p>
<dl>
<dt>
<dd> Enables or disables optimistic type assumptions with deoptimizing recompilation. Running with optimistic types will yield higher final speed, but may increase warmup time.</dl>
<p> -scripting</p>
<dl>
<dt>
<dd> Enables shell scripting features.</dl>
<p> -strict</p>
<dl>
<dt>
<dd> Enables strict mode, which enforces stronger adherence to the standard (ECMAScript Edition 5.1), making it easier to detect common coding errors.</dl>
<p> -t=<i>zone</i><br />
 -timezone=<i>zone</i></p>
<dl>
<dt>
<dd> Sets the specified time zone for script execution. It overrides the time zone set in the OS and used by the <code>Date</code> object.</dl>
<p> -v<br />
 -version</p>
<dl>
<dt>
<dd> Prints the Nashorn version string.</dl>
<h2>EXAMPLES</h2>
<p> <code>Example 1 </code>Running a Script with Nashorn</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>jjs script.js</code>
 
</pre>
</dl>
</dl>
<p> <code>Example 2 </code>Running Nashorn in Interactive Mode</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>&gt;&gt; </code><code>jjs</code>
<code>jjs&gt; </code><code>println(&quot;Hello, World!&quot;)</code>
<code>Hello, World!</code>
<code>jjs&gt; </code><code>quit()</code>
<code>&gt;&gt;</code>
 
</pre>
</dl>
</dl>
<p> <code>Example 3 </code>Passing Arguments to Nashorn</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>&gt;&gt; </code><code>jjs -- a b c</code>
<code>jjs&gt; </code><code>arguments.join(&quot;, &quot;)</code>
<code>a, b, c</code>
<code>jjs&gt;</code>
 
</pre>
</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code>jrunscript</code> </p>
<h2>Index</h2>
