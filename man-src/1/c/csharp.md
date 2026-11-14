---
title: "csharp(1)"
name: "csharp"
section: "1"
letter: "c"
url: "/docs/linux/man/1-csharp/"
description: "csharp, gsharp – Interactive C# Shell"
---

<h2>NAME</h2>
<p> csharp, gsharp &#8211; Interactive C# Shell</p>
<h2>SYNOPSIS</h2>
<p> <code>csharp [&#8211;attach PID] [-e EXPRESSION] [file1 [file2]]</code> [options] </p>
<p> <code>gsharp [file1 [file2]]</code></p>
<h2>DESCRIPTION</h2>
<p> The <i>csharp</i> is an interactive C# shell that allows the user to enter and evaluate C# statements and expressions from the command line. The regular <i>mcs</i> command line options can be used in this version of the compiler. </p>
<p> The <i>gsharp</i> command is a GUI version of the C# interpreter that uses Gtk# and provides an area to attach widgets as well. This version can be attached to other Gtk# applications in a safe way as it injects itself into the main loop of a Gtk# application, avoiding any problems arising from the multi-threaded nature of injecting itself into a target process. </p>
<p> Files specified in the command line will be loaded and executed as scripts. </p>
<p> Starting with Mono 2.10, the <i>csharp</i> command can be used as an interpreter executed by executables flagged with the Unix execute attribute. To do this, make the first line of your C# source code look like this: </p>
<pre>
&quot;#!/usr/bin/csharp&quot; 
Console.WriteLine (&quot;Hello, World&quot;);
</pre>
<h2>OPTIONS</h2>
<p> The commands accept all of the commands that are available to the <i>mcs</i> command, so you can reference assemblies, specify paths, language level and so on from the command line. In addition, the following command line options are supported:</p>
<dl>
<dt><i>&#8211;attach</i></p>
<dd> This is an advanced option and should only be used if you have a deep understanding of multi-threading. This option is availble on the <i>csharp</i> command and allows the compiler to be injected into other processes. This is done by injecting the C# shell in a separate thread that runs concurrently with your application. This means that you must take special measures to avoid crashing the target application while using it. For example, you might have to take the proper locks before issuing any commands that might affect the target process state, or sending commands through a method dispatcher.</p>
<dt><i>-e EXPRESSION</i></p>
<dd> This will evaluate the specified C# EXPRESSION and exit</dl>
<h2>OPERATION</h2>
<p> Once you launch the csharp command, you will be greeted with the interactive prompt: </p>
<pre>
$ csharp
Mono C# Shell, type &quot;help;&quot; for help
 
Enter statements below.
csharp&gt;
</pre>
<p> A number of namespaces are pre-defined with C# these include System, System.Linq, System.Collections and System.Collections.Generic. Unlike the compiled mode, it is possible to add new using statements as you type code, for example: </p>
<pre><code>
csharp &gt; new XmlDocument();
&lt;interactive&gt;(1, 6)
    : error CS0246 : The type or namespace name `XmlDocument' could not be found. Are you missing a using directive or an assembly reference? csharp &gt; using System.Xml;
csharp &gt; new XmlDocument();
System.Xml.XmlDocument
</code></pre>
<p> Every time a command is typed, the scope of that command is one of a class that derives from the class Mono.CSharp.InteractiveBase. This class defines a number of static properties and methods. To display a list of available commands access the `help&#8217; property:<br />
csharp &gt; help;<br />
&#8220;Static methods:<br />
    LoadPackage(pkg);<br />
&#8211; Loads the given Package(like &#8211; pkg:FILE)<br />
    [&#8230;] ShowVars();<br />
&#8211; Shows defined local variables.ShowUsing();<br />
&#8211; Show active using decltions.help;<br />
&#8221;<br />
    csharp &gt;</p>
<p> When expressions are entered, the C# shell will display the result of executing the expression: </p>
<p>csharp &gt; Math.Sin(Math.PI / 4);<br />
0.707106781186547 csharp &gt; 1 + 1;<br />
2 csharp &gt; &#8220;Hello, world&#8221;.IndexOf(&#8216;,&#8217;);<br />
5</p>
<p> The C# shell uses the ToString() method on the returned object to display the object, this sometimes can be limiting since objects that do not override the ToString() method will get the default behavior from System.Object which is merely to display their type name: </p>
<p>csharp &gt; var a = new XmlDocument();<br />
csharp &gt; a;<br />
System.Xml.Document<br />
        csharp &gt; csharp &gt; a.Name;<br />
&#8220;#document&#8221; csharp &gt;</p>
<p> A few datatypes are handled specially by the C# interactive shell like arrays, System.Collections.Hashtable, objects that implement System.Collections.IEnumerable and IDictionary and are rendered specially instead of just using ToString (): </p>
<p>csharp &gt; var pages = new Hashtable(){<br />
    &gt; {&#8220;Mono&#8221;, &#8220;http://www.mono-project.com/&#8221;},<br />
    &gt; {&#8220;Linux&#8221;, &#8220;http://kernel.org&#8221;}};<br />
csharp &gt; pages;<br />
{<br />
    {&#8220;Mono&#8221;, &#8220;http://www.mono-project.com/&#8221;},<br />
    {<br />
        &#8220;Linux&#8221;, &#8220;http://kernel.org&#8221;<br />
    }<br />
}</p>
<p> It is possible to use LINQ directly in the C# interactive shell since the System.Linq namespace has been imported at startup. The following sample gets a list of all the files that have not been accessed in a week from /tmp: </p>
<p>csharp &gt; using System.IO;<br />
csharp &gt; var last_week = DateTime.Now &#8211; TimeSpan.FromDays(7);<br />
csharp &gt; var old_files = from f in Directory.GetFiles(&#8220;/tmp&#8221;) &gt; let fi = new FileInfo(f) &gt; where fi.LastAccessTime &lt; LastWeek select f;<br />
csharp &gt;</p>
<p> You can of course print the results in a single statement as well: </p>
<p>csharp &gt; using System.IO;<br />
csharp &gt; var last_week = DateTime.Now &#8211; TimeSpan.FromDays(7);<br />
csharp &gt; from f in Directory.GetFiles(&#8220;/tmp&#8221;) &gt; let fi = new FileInfo(f) &gt; where fi.LastAccessTime &lt; last_week select f;<br />
[&#8230;] csharp &gt;</p>
<p> LINQ and its functional foundation produce on-demand code for IEnumerable return values. For instance, the return value from a using `from&#8217; is an IEnumerable that is evaluated on demand. The automatic rendering of IEnumerables on the command line will trigger the IEnumerable pipeline to execute at that point instead of having its execution delayed until a later point. </p>
<p> If you want to avoid having the IEnumerable rendered at this point, simply assign the value to a variable. </p>
<p> Unlike compiled C#, the type of a variable can be changed if a new declaration is entered, for example: </p>
<p>csharp &gt; var a = 1;<br />
csharp &gt; a.GetType();<br />
System.Int32<br />
        csharp &gt; var a = &#8220;Hello&#8221;;<br />
csharp &gt; a.GetType();<br />
System.String<br />
        csharp &gt; ShowVars();<br />
string a = &#8220;Hello&#8221;</p>
<p> In the case that an expression or a statement is not completed in a single line, a continuation prompt is displayed, for example: </p>
<p>csharp &gt; var protocols = new string[]{<br />
    &gt; &#8220;ftp&#8221;,<br />
    &gt; &#8220;http&#8221;,<br />
    &gt; &#8220;gopher&#8221; &gt; };<br />
csharp &gt; protocols;<br />
{<br />
    &#8220;ftp&#8221;, &#8220;http&#8221;, &#8220;gopher&#8221;<br />
}</p>
<p> Long running computations can be interrupted by using the Control-C sequence: </p>
<p>csharp &gt; var done = false;<br />
csharp &gt; while (!done)<br />
{<br />
}<br />
Interrupted !System.Threading.ThreadAbortException : Thread was being aborted<br />
                                                         at Class1.Host(System.Object &amp; $retval)[0x00000] at Mono.CSharp.InteractiveShell.ExecuteBlock(Mono.CSharp.Class host, Mono.CSharp.Undo undo)[0x00000] csharp &gt;</p>
<h2>INTERACTIVE EDITING</h2>
<p> The C# interactive shell contains a line-editor that provides a more advanced command line editing functionality than the operating system provides. These are available in the command line version, the GUI versions uses the standard Gtk# key bindings. </p>
<p> The command set is similar to many other applications (cursor keys) and incorporates some of the Emacs commands for editing as well as a history mechanism to </p>
<p> The following keyboard input is supported:</p>
<dl>
<dt><i>Home Key, Control-a</i></p>
<dd> Goes to the beginning of the line.</p>
<dt><i>End Key, Control-e</i></p>
<dd> Goes to the end of the line.</p>
<dt><i>Left Arrow Key, Control-b</i></p>
<dd> Moves the cursor back one character.</p>
<dt><i>Right Arrow Key, Control-f</i></p>
<dd> Moves the cursor forward one character.</p>
<dt><i>Up Arrow Key, Control-p</i></p>
<dd> Goes back in the history, replaces the current line with the previous line in the history.</p>
<dt><i>Down Arrow Key, Control-n</i></p>
<dd> Moves forward in the history, replaces the current line with the next lien in the history.</p>
<dt><i>Return</i></p>
<dd> Executes the current line if the statement or expression is complete, or waits for further input.</p>
<dt><i>Control-C</i></p>
<dd> Cancel the current line being edited. This will kill any currently in-progress edits or partial editing and go back to a toplevel definition.</p>
<dt><i>Backspace Key</i></p>
<dd> Deletes the character before the cursor</p>
<dt><i>Delete Key, Control-d</i></p>
<dd> Deletes the character at the current cursor position.</p>
<dt><i>Control-k</i></p>
<dd> Erases the contents of the line until the end of the line and places the result in the cut and paste buffer.</p>
<dt><i>Alt-D</i></p>
<dd> Deletes the word starting at the cursor position and appends into the cut and paste buffer. By pressing Alt-d repeatedly, multiple words can be appended into the paste buffer.</p>
<dt><i>Control-Y</i></p>
<dd> Pastes the content of the kill buffer at the current cursor position.</p>
<dt><i>Control-Q</i></p>
<dd> This is the quote character. It allows the user to enter control-characters that are otherwise taken by the command editing facility. Press Control-Q followed by the character you want to insert, and it will be inserted verbatim into the command line.</p>
<dt><i>Control-D</i></p>
<dd> Terminates the program. This terminates the input for the program.</dl>
<h2>STATIC PROPERTIES AND METHODS</h2>
<p> Since the methods and properties of the base class from where the statements and expressions are executed are static, they can be invoked directly from the shell. These are the available properties and methods:</p>
<dl>
<dt><i>void LoadAssembly(string assembly)</i></p>
<dd> Loads the given assembly. This is equivalent to passing the compiler the -r: flag with the specified string.</p>
<dt><i>void LoadPackage(string package)</i></p>
<dd> Imports the package specified. This is equivalent to invoking the compiler with the -pkg: flag with the specified string.</p>
<dt><i>string Prompt { get; set } </i></p>
<dd> The prompt used by the shell. It defaults to the value &quot;csharp&gt; &quot;. <i>string ContinuationPrompt { get; set; } </i> The prompt used by the shell when further input is required to complete the expression or statement.</p>
<dt><i>void ShowVars()</i></p>
<dd> Displays all the variables that have been defined so far and their types. In the csharp shell declaring new variables will shadow previous variable declarations, this is different than C# when compiled. <i>void ShowUsing()</i> Displays all the using statements in effect. <i>TimeSpan Time (Action a)</i> Handy routine to time the time that some code takes to execute. The parameter is an Action delegate, and the return value is a TimeSpan. For example:</dl>
<pre><code>
csharp &gt; Time(() = &gt; { for (int i = 0; i &lt; 5; i++) Console.WriteLine (i); });
0 1 2 3 4 00 : 00 : 00.0043230 csharp &gt;
</code></pre>
<p> The return value is a TimeSpan, that you can store in a variable for benchmarking purposes.</p>
<h2>GUI METHODS AND PROPERTIES</h2>
<p> In addition to the methods and properties available in the console version there are a handful of extra properties available on the GUI version. For example a &quot;PaneContainer&quot; Gtk.Container is exposed that you can use to host Gtk# widgets while prototyping or the &quot;MainWindow&quot; property that gives you access to the current toplevel window.</p>
<h2>STARTUP FILES</h2>
<p> The C# shell will load all the Mono assemblies and C# script files located in the ~/.config/csharp directory on Unix. The assemblies are loaded before the source files are loaded. </p>
<p> C# script files are files that have the extension .cs and they should only contain statements and expressions, they can not contain full class definitions (at least not as of Mono 2.0). Full class definitions should be compiled into dlls and stored in that directory.</p>
<h2>AUTHORS</h2>
<p> The Mono C# Compiler was written by Miguel de Icaza, Ravi Pratap, Martin Baulig, Marek Safar and Raja Harinath. The development was funded by Ximian, Novell and Marek Safar.</p>
<h2>LICENSE</h2>
<p> The Mono Compiler Suite is released under the terms of the GNU GPL or the MIT X11. Please read the accompanying `COPYING&#8217; file for details. Alternative licensing for the compiler is available from Novell.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gmcs/">gmcs</a>(1), <a href="/docs/linux/man/1-mcs/">mcs</a>(1), <a href="/docs/linux/man/1-mdb/">mdb</a>(1), <a href="/docs/linux/man/1-mono/">mono</a>(1), <a href="/docs/linux/man/1-pkg-config/">pkg-config</a>(1)</p>
<h2>BUGS</h2>
<p> To report bugs in the compiler, you must file them on our bug tracking system, at: <a rel="nofollow" href="http://www.mono-project.com/community/bugs/">http://www.mono-project.com/community/bugs/</a></p>
<h2>MAILING LIST</h2>
<p> The Mono Mailing lists are listed at <a rel="nofollow" href="http://www.mono-project.com/community/help/mailing-lists/">http://www.mono-project.com/community/help/mailing-lists/</a></p>
<h2>MORE INFORMATION</h2>
<p> The Mono C# compiler was developed by Novell, Inc (<a rel="nofollow" href="http://www.novell.com,">http://www.novell.com,</a> http) and is based on the ECMA C# language standard available here: <a rel="nofollow" href="http://www.ecma.ch/ecma1/STAND/ecma-334.htm">http://www.ecma.ch/ecma1/STAND/ecma-334.htm</a> </p>
<p> The home page for the Mono C# compiler is at <a rel="nofollow" href="http://www.mono-project.com/docs/about-mono/languages/csharp/">http://www.mono-project.com/docs/about-mono/languages/csharp/</a> information about the interactive mode for C# is available in <a rel="nofollow" href="http://mono-project.com/docs/tools+libraries/tools/repl/">http://mono-project.com/docs/tools+libraries/tools/repl/</a> </p>
<h2>Index</h2>
