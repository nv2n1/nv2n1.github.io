---
title: "wish8(1)"
name: "wish8"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wish8/"
description: "wish – Simple windowing shell"
---

<h2 class="name">NAME</h2>
<p> wish &#8211; Simple windowing shell </p>
<h2>SYNOPSIS</h2>
<p> <code>wish</code> ?<code>-encoding </code><i>name</i>? ?<i>fileName arg arg &#8230;</i>?</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-encoding </code><i>name</i></p>
<dd> Specifies the encoding of the text stored in <i>fileName</i>. This option is only recognized prior to the <i>fileName</i> argument.</p>
<dt><code>-colormap </code><i>new</i></p>
<dd> Specifies that the window should have a new private colormap instead of using the default colormap for the screen.</p>
<dt><code>-display </code><i>display</i></p>
<dd> Display (and screen) on which to display window.</p>
<dt><code>-geometry </code><i>geometry</i></p>
<dd> Initial geometry to use for window. If this option is specified, its value is stored in the <code>geometry</code> global variable of the application&#8217;s Tcl interpreter.</p>
<dt><code>-name </code><i>name</i></p>
<dd> Use <i>name</i> as the title to be displayed in the window, and as the name of the interpreter for <code>send</code> commands.</p>
<dt><code>-sync</code></p>
<dd> Execute all X server commands synchronously, so that errors are reported immediately. This will result in much slower execution, but it is useful for debugging.</p>
<dt><code>-use</code> <i>id</i></p>
<dd> Specifies that the main window for the application is to be embedded in the window whose identifier is <i>id</i>, instead of being created as an independent toplevel window. <i>Id</i> must be specified in the same way as the value for the <code>-use</code> option for toplevel widgets (i.e. it has a form like that returned by the <code>winfo id</code> command).</p>
<dl>
<dt>
<dd> Note that on some platforms this will only work correctly if <i>id</i> refers to a Tk <code>frame</code> or <code>toplevel</code> that has its <code>-container</code> option enabled.</dl>
<dt><code>-visual </code><i>visual</i></p>
<dd> Specifies the visual to use for the window. <i>Visual</i> may have any of the forms supported by the <code>Tk_GetVisual</code> procedure.</p>
<dt><code>&#8212;</code></p>
<dd> Pass all remaining arguments through to the script&#8217;s <code>argv</code> variable without interpreting them. This provides a mechanism for passing arguments such as <code>-name</code> to a script instead of having <code>wish</code> interpret them.
</dl>
<h2>DESCRIPTION</h2>
<p> <code>Wish</code> is a simple program consisting of the Tcl command language, the Tk toolkit, and a main program that reads commands from standard input or from a file. It creates a main window and then processes Tcl commands. If <code>wish</code> is invoked with arguments, then the first few arguments, ?<code>-encoding </code><i>name</i>? ?<i>fileName</i>?, specify the name of a script file, and, optionally, the encoding of the text data stored in that script file. A value for <i>fileName</i> is recognized if the appropriate argument does not start with &#8220;-&#8221;. </p>
<p> If there are no arguments, or the arguments do not specify a <i>fileName</i>, then wish reads Tcl commands interactively from standard input. It will continue processing commands until all windows have been deleted or until end-of-file is reached on standard input. If there exists a file &#8220;<code>.wishrc</code>&#8221; in the home directory of the user, <code>wish</code> evaluates the file as a Tcl script just before reading the first command from standard input. </p>
<p> If arguments to <code>wish</code> do specify a <i>fileName</i>, then <i>fileName</i> is treated as the name of a script file. <code>Wish</code> will evaluate the script in <i>fileName</i> (which presumably creates a user interface), then it will respond to events until all windows have been deleted. Commands will not be read from standard input. There is no automatic evaluation of &#8220;<code>.wishrc</code>&#8221; when the name of a script file is presented on the <code>wish</code> command line, but the script file can always <code>source</code> it if desired. </p>
<p> Note that on Windows, the <code>wish</code><i>version</i><code>.exe</code> program varies from the <code>tclsh</code><i>version</i><code>.exe</code> program in an additional important way: it does not connect to a standard Windows console and is instead a windowed program. Because of this, it additionally provides access to its own <code>console</code> command.</p>
<h2>OPTION PROCESSING</h2>
<p> <code>Wish</code> automatically processes all of the command-line options described in the <code>OPTIONS</code> summary above. Any other command-line arguments besides these are passed through to the application using the <code>argc</code> and <code>argv</code> variables described later.</p>
<h2>APPLICATION NAME AND CLASS</h2>
<p> The name of the application, which is used for purposes such as <code>send</code> commands, is taken from the <code>-name</code> option, if it is specified; otherwise it is taken from <i>fileName</i>, if it is specified, or from the command name by which <code>wish</code> was invoked. In the last two cases, if the name contains a &#8220;/&#8221; character, then only the characters after the last slash are used as the application name. </p>
<p> The class of the application, which is used for purposes such as specifying options with a <code>RESOURCE_MANAGER</code> property or .Xdefaults file, is the same as its name except that the first letter is capitalized.</p>
<h2>VARIABLES</h2>
<p> <code>Wish</code> sets the following Tcl variables:</p>
<dl>
<dt><code>argc</code></p>
<dd> Contains a count of the number of <i>arg</i> arguments (0 if none), not including the options described above.</p>
<dt><code>argv</code></p>
<dd> Contains a Tcl list whose elements are the <i>arg</i> arguments that follow a <code>&#8212;</code> option or do not match any of the options described in <code>OPTIONS</code> above, in order, or an empty string if there are no such arguments.</p>
<dt><code>argv0</code></p>
<dd> Contains <i>fileName</i> if it was specified. Otherwise, contains the name by which <code>wish</code> was invoked.</p>
<dt><code>geometry</code></p>
<dd> If the <code>-geometry</code> option is specified, <code>wish</code> copies its value into this variable. If the variable still exists after <i>fileName</i> has been evaluated, <code>wish</code> uses the value of the variable in a <code>wm geometry</code> command to set the main window&#8217;s geometry.</p>
<dt><code>tcl_interactive</code></p>
<dd> Contains 1 if <code>wish</code> is reading commands interactively (<i>fileName</i> was not specified and standard input is a terminal-like device), 0 otherwise.</dl>
<h2>SCRIPT FILES</h2>
<p> If you create a Tcl script in a file whose first line is</p>
<dl>
<dt>
<dd>
<pre>
<code>#!/usr/local/bin/wish</code>
</pre>
</dl>
<p> then you can invoke the script file directly from your shell if you mark it as executable. This assumes that <code>wish</code> has been installed in the default location in /usr/local/bin; if it is installed somewhere else then you will have to modify the above line to match. Many UNIX systems do not allow the <code>#!</code> line to exceed about 30 characters in length, so be sure that the <code>wish</code> executable can be accessed with a short file name. </p>
<p> An even better approach is to start your script files with the following three lines:</p>
<dl>
<dt>
<dd>
<pre>
<code>#!/bin/sh
# the next line restarts using wish \
exec wish &quot;$0&quot; ${1+&quot;$@&quot;}</code>
</pre>
</dl>
<p> This approach has three advantages over the approach in the previous paragraph. First, the location of the <code>wish</code> binary does not have to be hard-wired into the script: it can be anywhere in your shell search path. Second, it gets around the 30-character file name limit in the previous approach. Third, this approach will work even if <code>wish</code> is itself a shell script (this is done on some systems in order to handle multiple architectures or operating systems: the <code>wish</code> script selects one of several binaries to run). The three lines cause both <code>sh</code> and <code>wish</code> to process the script, but the <code>exec</code> is only executed by <code>sh</code>. <code>sh</code> processes the script first; it treats the second line as a comment and executes the third line. The <code>exec</code> statement cause the shell to stop processing and instead to start up <code>wish</code> to reprocess the entire script. When <code>wish</code> starts up, it treats all three lines as comments, since the backslash at the end of the second line causes the third line to be treated as part of the comment on the second line. </p>
<p> The end of a script file may be marked either by the physical end of the medium, or by the character, &#8220;&#8221; (&#8220;&#8221;, control-Z). If this character is present in the file, the <code>wish</code> application will read text up to but not including the character. An application that requires this character in the file may encode it as &#8220;&#8221;, &#8220;&#8221;, or &#8220;&#8221;; or may generate it by use of commands such as <code>format</code> or <code>binary</code>.</p>
<h2>PROMPTS</h2>
<p> When <code>wish</code> is invoked interactively it normally prompts for each command with &#8220;<code>% </code>&#8221;. You can change the prompt by setting the variables <code>tcl_prompt1</code> and <code>tcl_prompt2</code>. If variable <code>tcl_prompt1</code> exists then it must consist of a Tcl script to output a prompt; instead of outputting a prompt <code>wish</code> will evaluate the script in <code>tcl_prompt1</code>. The variable <code>tcl_prompt2</code> is used in a similar way when a newline is typed but the current command is not yet complete; if <code>tcl_prompt2</code> is not set then no prompt is output for incomplete commands.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-tclsh/">tclsh</a>(1), <a href="/docs/linux/man/n-toplevel/">toplevel</a>(n), <a href="/docs/linux/man/3-tk_main/">Tk_Main</a>(3), <a href="/docs/linux/man/3-tk_mainloop/">Tk_MainLoop</a>(3), <a href="/docs/linux/man/3-tk_mainwindow/">Tk_MainWindow</a>(3)</p>
<h2>KEYWORDS</h2>
<p> application, argument, interpreter, prompt, script file, shell, toolkit, toplevel </p>
<h2>Index</h2>
