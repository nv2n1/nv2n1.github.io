---
title: "lefty(1)"
name: "lefty"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lefty/"
description: "lefty – A Programmable Graphics Editor"
---

<h2 class="name">NAME</h2>
<p> lefty &#8211; A Programmable Graphics Editor </p>
<h2>SYNOPSIS</h2>
<p> <code>lefty</code> [ <i>options</i> ] [ <i>file</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>lefty</code> is a two-view graphics editor for technical pictures. This editor has no hardwired knowledge about specific picture layouts or editing operations. Each picture is described by a program that contains functions to draw the picture and functions to perform editing operations that are appropriate for the specific picture. Primitive user actions, like mouse and keyboard events, are also bound to functions in this program. Besides the graphical view of the picture itself, the editor presents a textual view of the program that describes the picture. Programmability and the two-view interface allow the editor to handle a variety of pictures, but are particularly useful for pictures used in technical contexts, e.g., graphs and trees. Also, <code>lefty</code> can communicate with other processes. This feature allows it to use existing tools to compute specific picture layouts and allows external processes to use the editor as a front end to display their data structures graphically.</p>
<h2>USAGE</h2>
<p> The file name is optional. It may be <code>&#8211;</code>, for reading from standard input. <code>lefty</code> uses two environment variables, <code>LEFTYPATH</code> and <code>LEFTYOPTIONS</code>. <code>LEFTYPATH</code> is a colon separated list of directories. When <code>lefty</code> tries to open a file, it searches that path for the file. When <code>lefty</code> tries to start up another process, it searches <code>LEFTYPATH</code> first, then the standard <code>PATH</code> variable. <code>LEFTYOPTIONS</code> can be used to set specific options. Options specified on the command line override options set through this variable.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-x</code></p>
<dd> Instructs the editor to exit after processing <code>file</code>.</p>
<dt><code>-e &lt;expression&gt;</code></p>
<dd> <code>&lt;expression&gt;</code> is parsed and executed.</p>
<dt><code>-el &lt;num&gt;</code></p>
<dd> Set error reporting level. The default value is <code>0</code>. <code>0</code> never prints any messages. <code>1</code> prints severe errors, such as trying to return from a non function. <code>2</code> is the most useful: it reports function calls that cannot be executed, either because there is no function, or because of argument mismatches. <code>3</code> also warns about bad variable names. <code>4,5</code> warn about expressions that do not return a value. Only level <code>1</code> messages are real errors. The rest arise from legal <code>lefty</code> statements, but may be caused by some logic errors.</p>
<dt><code>-sd &lt;num&gt;</code></p>
<dd> Specifies how much of the stack to show, when an error message is to be printed. The default value is <code>2</code>. With <code>0</code>, no part of the stack is shown. With <code>1</code>, only the top stack frame is printed. With <code>2</code>, the full stack is printed.</p>
<dt><code>-sb &lt;num&gt;</code></p>
<dd> Specifies how much of each function in the stack to show, when an error message is to be printed. The default value is <code>2</code>. With <code>0</code>, no part of the function is shown. With <code>1</code>, only the line around the error is printed. With <code>2</code>, the full function body is printed.</p>
<dt><code>-df &lt;string&gt;</code></p>
<dd> Sets the default font. This font is used whenever a requested font cannot be found. The string must be a legal X font. If string is <code>&#8221;</code>, <code>lefty</code> will draw small boxes instead of text.</p>
<dt><code>-ps &lt;file&gt;</code></p>
<dd> Specifies a default file name for postscript files. This name is used when no name is specified in the <code>createwidget</code> call. The default file name is <code>out.ps</code>.</p>
<dt><code>-V</code></p>
<dd> Prints the version.</p>
<dt><code>-?</code></p>
<dd> Prints the usage and exits.</dl>
<h2>SEE ALSO</h2>
<p> <i>lefty</i> user guide. </p>
<h2>Index</h2>
