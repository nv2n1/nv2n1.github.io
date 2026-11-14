---
title: "tclsh8(1)"
name: "tclsh8"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tclsh8/"
description: "tclsh – Simple shell containing Tcl interpreter"
---

<h2 class="name">NAME</h2>
<p> tclsh &#8211; Simple shell containing Tcl interpreter </p>
<h2>SYNOPSIS</h2>
<p> <code>tclsh</code> ?<code>-encoding </code><i>name</i>? ?<i>fileName arg arg &#8230;</i>? </p>
<h2>DESCRIPTION</h2>
<p> <code>Tclsh</code> is a shell-like application that reads Tcl commands from its standard input or from a file and evaluates them. If invoked with no arguments then it runs interactively, reading Tcl commands from standard input and printing command results and error messages to standard output. It runs until the <code>exit</code> command is invoked or until it reaches end-of-file on its standard input. If there exists a file <code>.tclshrc</code> (or <code>tclshrc.tcl</code> on the Windows platforms) in the home directory of the user, interactive <code>tclsh</code> evaluates the file as a Tcl script just before reading the first command from standard input.</p>
<h2>SCRIPT FILES</h2>
<p> If <code>tclsh</code> is invoked with arguments then the first few arguments specify the name of a script file, and, optionally, the encoding of the text data stored in that script file. Any additional arguments are made available to the script as variables (see below). Instead of reading commands from standard input <code>tclsh</code> will read Tcl commands from the named file; <code>tclsh</code> will exit when it reaches the end of the file. The end of the file may be marked either by the physical end of the medium, or by the character, &#8220;&#8221; (&#8220;&#8221;, control-Z). If this character is present in the file, the <code>tclsh</code> application will read text up to but not including the character. An application that requires this character in the file may safely encode it as &#8220;&#8221;, &#8220;&#8221;, or &#8220;&#8221;; or may generate it by use of commands such as <code>format</code> or <code>binary</code>. There is no automatic evaluation of <code>.tclshrc</code> when the name of a script file is presented on the <code>tclsh</code> command line, but the script file can always <code>source</code> it if desired. </p>
<p> If you create a Tcl script in a file whose first line is </p>
<dl>
<dt>
<dd>
<pre>
<code>#!/usr/local/bin/tclsh</code>
</pre>
</dl>
<p> then you can invoke the script file directly from your shell if you mark the file as executable. This assumes that <code>tclsh</code> has been installed in the default location in /usr/local/bin; if it is installed somewhere else then you will have to modify the above line to match. Many UNIX systems do not allow the <code>#!</code> line to exceed about 30 characters in length, so be sure that the <code>tclsh</code> executable can be accessed with a short file name. </p>
<p> An even better approach is to start your script files with the following three lines: </p>
<dl>
<dt>
<dd>
<pre>
<code>#!/bin/sh
# the next line restarts using tclsh \
exec tclsh &quot;$0&quot; ${1+&quot;$@&quot;}</code>
</pre>
</dl>
<p> This approach has three advantages over the approach in the previous paragraph. First, the location of the <code>tclsh</code> binary does not have to be hard-wired into the script: it can be anywhere in your shell search path. Second, it gets around the 30-character file name limit in the previous approach. Third, this approach will work even if <code>tclsh</code> is itself a shell script (this is done on some systems in order to handle multiple architectures or operating systems: the <code>tclsh</code> script selects one of several binaries to run). The three lines cause both <code>sh</code> and <code>tclsh</code> to process the script, but the <code>exec</code> is only executed by <code>sh</code>. <code>sh</code> processes the script first; it treats the second line as a comment and executes the third line. The <code>exec</code> statement cause the shell to stop processing and instead to start up <code>tclsh</code> to reprocess the entire script. When <code>tclsh</code> starts up, it treats all three lines as comments, since the backslash at the end of the second line causes the third line to be treated as part of the comment on the second line. </p>
<p> You should note that it is also common practice to install tclsh with its version number as part of the name. This has the advantage of allowing multiple versions of Tcl to exist on the same system at once, but also the disadvantage of making it harder to write scripts that start up uniformly across different versions of Tcl.</p>
<h2>VARIABLES</h2>
<p> <code>Tclsh</code> sets the following global Tcl variables in addition to those created by the Tcl library itself (such as <code>env</code>, which maps environment variables such as <code>PATH</code> into Tcl):</p>
<dl>
<dt><code>argc</code></p>
<dd> Contains a count of the number of <i>arg</i> arguments (0 if none), not including the name of the script file.</p>
<dt><code>argv</code></p>
<dd> Contains a Tcl list whose elements are the <i>arg</i> arguments, in order, or an empty string if there are no <i>arg</i> arguments.</p>
<dt><code>argv0</code></p>
<dd> Contains <i>fileName</i> if it was specified. Otherwise, contains the name by which <code>tclsh</code> was invoked.</p>
<dt><code>tcl_interactive</code></p>
<dd> Contains 1 if <code>tclsh</code> is running interactively (no <i>fileName</i> was specified and standard input is a terminal-like device), 0 otherwise.</dl>
<h2>PROMPTS</h2>
<p> When <code>tclsh</code> is invoked interactively it normally prompts for each command with &#8220;<code>% </code>&#8221;. You can change the prompt by setting the global variables <code>tcl_prompt1</code> and <code>tcl_prompt2</code>. If variable <code>tcl_prompt1</code> exists then it must consist of a Tcl script to output a prompt; instead of outputting a prompt <code>tclsh</code> will evaluate the script in <code>tcl_prompt1</code>. The variable <code>tcl_prompt2</code> is used in a similar way when a newline is typed but the current command is not yet complete; if <code>tcl_prompt2</code> is not set then no prompt is output for incomplete commands.</p>
<h2>STANDARD CHANNELS</h2>
<p> See <code>Tcl_StandardChannels</code> for more explanations.</p>
<h2>SEE ALSO</h2>
<p> auto_path(3tcl), encoding(3tcl), env(3tcl), fconfigure(3tcl)</p>
<h2>KEYWORDS</h2>
<p> application, argument, interpreter, prompt, script file, shell </p>
<h2>Index</h2>
