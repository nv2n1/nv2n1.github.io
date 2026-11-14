---
title: "tcl_setstartupscript(3)"
name: "tcl_setstartupscript"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_setstartupscript/"
description: "Tcl_Main, Tcl_SetStartupScript, Tcl_GetStartupScript, Tcl_SetMainLoop – main program, startup script, and event loop definition for Tcl-based applications"
---

<p>Tcl_Main, Tcl_SetStartupScript, Tcl_GetStartupScript, Tcl_SetMainLoop &#8211; main program, startup script, and event loop definition for Tcl-based applications </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
<code>Tcl_Main</code>(<i>argc, argv, appInitProc</i>)
<code>Tcl_SetStartupScript</code>(<i>path, encoding</i>)
Tcl_Obj *
<code>Tcl_GetStartupScript</code>(<i>encodingPtr</i>)
<code>Tcl_SetMainLoop</code>(<i>mainLoopProc</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>int <i>argc</i> (in) Number of elements in <i>argv</i>.</p>
<dd>char <i>*argv[]</i> (in) Array of strings containing command-line arguments. On Windows, when using -DUNICODE, the parameter type changes to wchar_t *.</p>
<dd>Tcl_AppInitProc <i>*appInitProc</i> (in) Address of an application-specific initialization procedure. The value for this argument is usually <code>Tcl_AppInit</code>.</p>
<dd>Tcl_Obj <i>*path</i> (in) Name of file to use as startup script, or NULL.</p>
<dd>const char <i>*encoding</i> (in) Encoding of file to use as startup script, or NULL.</p>
<dd>const char <i>**encodingPtr</i> (out) If non-NULL, location to write a copy of the (const char *) pointing to the encoding name.</p>
<dd>Tcl_MainLoopProc <i>*mainLoopProc</i> (in) Address of an application-specific event loop procedure.
</dl>
<h2>Description</h2>
<p><code>Tcl_Main</code> can serve as the main program for Tcl-based shell applications. A &#8220;shell application&#8221; is a program like tclsh or wish that supports both interactive interpretation of Tcl and evaluation of a script contained in a file given as a command line argument. <code>Tcl_Main</code> is offered as a convenience to developers of shell applications, so they do not have to reproduce all of the code for proper initialization of the Tcl library and interactive shell operation. Other styles of embedding Tcl in an application are not supported by <code>Tcl_Main</code>. Those must be achieved by calling lower level functions in the Tcl library directly. </p>
<p> The <code>Tcl_Main</code> function has been offered by the Tcl library since release Tcl 7.4. In older releases of Tcl, the Tcl library itself defined a function <code>main</code>, but that lacks flexibility of embedding style and having a function <code>main</code> in a library (particularly a shared library) causes problems on many systems. Having <code>main</code> in the Tcl library would also make it hard to use Tcl in C++ programs, since C++ programs must have special C++ <code>main</code> functions. </p>
<p> Normally each shell application contains a small <code>main</code> function that does nothing but invoke <code>Tcl_Main</code>. <code>Tcl_Main</code> then does all the work of creating and running a <code>tclsh</code>-like application. </p>
<p> <code>Tcl_Main</code> is not provided by the public interface of Tcl&#8217;s stub library. Programs that call <code>Tcl_Main</code> must be linked against the standard Tcl library. Extensions (stub-enabled or not) are not intended to call <code>Tcl_Main</code>. </p>
<p> <code>Tcl_Main</code> is not thread-safe. It should only be called by a single master thread of a multi-threaded application. This restriction is not a problem with normal use described above. </p>
<p> <code>Tcl_Main</code> and therefore all applications based upon it, like <code>tclsh</code>, use <code>Tcl_GetStdChannel</code> to initialize the standard channels to their default values. See <code>Tcl_StandardChannels</code> for more information. </p>
<p> <code>Tcl_Main</code> supports two modes of operation, depending on whether the filename and encoding of a startup script has been established. The routines <code>Tcl_SetStartupScript</code> and <code>Tcl_GetStartupScript</code> are the tools for controlling this configuration of <code>Tcl_Main</code>. </p>
<p> <code>Tcl_SetStartupScript</code> registers the value <i>path</i> as the name of the file for <code>Tcl_Main</code> to evaluate as its startup script. The value <i>encoding</i> is Tcl&#8217;s name for the encoding used to store the text in that file. A value of <code>NULL</code> for <i>encoding</i> is a signal to use the system encoding. A value of <code>NULL</code> for <i>path</i> erases any existing registration so that <code>Tcl_Main</code> will not evaluate any startup script. </p>
<p> <code>Tcl_GetStartupScript</code> queries the registered file name and encoding set by the most recent <code>Tcl_SetStartupScript</code> call in the same thread. The stored file name is returned, and the stored encoding name is written to space pointed to by <i>encodingPtr</i>, when that is not NULL. </p>
<p> The file name and encoding values managed by the routines <code>Tcl_SetStartupScript</code> and <code>Tcl_GetStartupScript</code> are stored per-thread. Although the storage and retrieval functions of these routines work in any thread, only those calls in the same master thread as <code>Tcl_Main</code> can have any influence on it. </p>
<p> The caller of <code>Tcl_Main</code> may call <code>Tcl_SetStartupScript</code> first to establish its desired startup script. If <code>Tcl_Main</code> finds that no such startup script has been established, it consults the first few arguments in <i>argv</i>. If they match ?<code>-encoding </code><i>name</i>? <i>fileName</i>, where <i>fileName</i> does not begin with the character <i>&#8211;</i>, then <i>fileName</i> is taken to be the name of a file containing a <i>startup script</i>, and <i>name</i> is taken to be the name of the encoding of the contents of that file. <code>Tcl_Main</code> then calls <code>Tcl_SetStartupScript</code> with these values. </p>
<p> <code>Tcl_Main</code> then defines in its master interpreter the Tcl variables <i>argc</i>, <i>argv</i>, <i>argv0</i>, and <i>tcl_interactive</i>, as described in the documentation for <code>tclsh</code>. </p>
<p> When it has finished its own initialization, but before it processes commands, <code>Tcl_Main</code> calls the procedure given by the <i>appInitProc</i> argument. This procedure provides a &#8220;hook&#8221; for the application to perform its own initialization of the interpreter created by <code>Tcl_Main</code>, such as defining application-specific commands. The application initialization routine might also call <code>Tcl_SetStartupScript</code> to (re-)set the file and encoding to be used as a startup script. The procedure must have an interface that matches the type <code>Tcl_AppInitProc</code>: </p>
<dl COMPACT>
<dd>
<pre>typedef int <code>Tcl_AppInitProc</code>(
 Tcl_Interp *<i>interp</i>);</pre>
</dl>
<p> <i>AppInitProc</i> is almost always a pointer to <code>Tcl_AppInit</code>; for more details on this procedure, see the documentation for <code>Tcl_AppInit</code>. </p>
<p> When the <i>appInitProc</i> is finished, <code>Tcl_Main</code> calls <code>Tcl_GetStartupScript</code> to determine what startup script has been requested, if any. If a startup script has been provided, <code>Tcl_Main</code> attempts to evaluate it. Otherwise, interactive mode begins with examination of the variable <i>tcl_rcFileName</i> in the master interpreter. If that variable exists and holds the name of a readable file, the contents of that file are evaluated in the master interpreter. Then interactive operations begin, with prompts and command evaluation results written to the standard output channel, and commands read from the standard input channel and then evaluated. The prompts written to the standard output channel may be customized by defining the Tcl variables <i>tcl_prompt1</i> and <i>tcl_prompt2</i> as described in the documentation for <code>tclsh</code>. The prompts and command evaluation results are written to the standard output channel only if the Tcl variable <i>tcl_interactive</i> in the master interpreter holds a non-zero integer value. </p>
<p> <code>Tcl_SetMainLoop</code> allows setting an event loop procedure to be run. This allows, for example, Tk to be dynamically loaded and set its event loop. The event loop will run following the startup script. If you are in interactive mode, setting the main loop procedure will cause the prompt to become fileevent based and then the loop procedure is called. When the loop procedure returns in interactive mode, interactive operation will continue. The main loop procedure must have an interface that matches the type <code>Tcl_MainLoopProc</code>: </p>
<dl COMPACT>
<dd>
<pre>typedef void <code>Tcl_MainLoopProc</code>(void);</pre>
</dl>
<p> <code>Tcl_Main</code> does not return. Normally a program based on <code>Tcl_Main</code> will terminate when the <code>exit</code> command is evaluated. In interactive mode, if an EOF or channel error is encountered on the standard input channel, then <code>Tcl_Main</code> itself will evaluate the <code>exit</code> command after the main loop procedure (if any) returns. In non-interactive mode, after <code>Tcl_Main</code> evaluates the startup script, and the main loop procedure (if any) returns, <code>Tcl_Main</code> will also evaluate the <code>exit</code> command.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-tclsh/">tclsh</a>(1), <a href="/docs/linux/man/3-tcl_getstdchannel/">Tcl_GetStdChannel</a>(3), <a href="/docs/linux/man/3-tcl_standardchannels/">Tcl_StandardChannels</a>(3), <a href="/docs/linux/man/3-tcl_appinit/">Tcl_AppInit</a>(3), <a href="/docs/linux/man/n-exit/">exit</a>(n), <a href="/docs/linux/man/n-encoding/">encoding</a>(n)</p>
<h2>Keywords</h2>
<p>application-specific initialization, command-line arguments, main program</p>
