---
title: "tk_pathname(3)"
name: "tk_pathname"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_pathname/"
description: "Tk_Name, Tk_PathName, Tk_NameToWindow – convert between names and window tokens"
---

<p>Tk_Name, Tk_PathName, Tk_NameToWindow &#8211; convert between names and window tokens </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
Tk_Uid
<code>Tk_Name</code>(<i>tkwin</i>)
char *
<code>Tk_PathName</code>(<i>tkwin</i>)
Tk_Window
<code>Tk_NameToWindow</code>(<i>interp, pathName, tkwin</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Window <i>tkwin</i> (in) Token for window.</p>
<dd>Tcl_Interp <i>*interp</i> (out) Interpreter to use for error reporting.</p>
<dd>const char <i>*pathName</i> (in) Character string containing path name of window. </p>
</dl>
<h2>Description</h2>
<p>Each window managed by Tk has two names, a short name that identifies a window among children of the same parent, and a path name that identifies the window uniquely among all the windows belonging to the same main window. The path name is used more often in Tk than the short name; many commands, like <code>bind</code>, expect path names as arguments. </p>
<p> The <code>Tk_Name</code> macro returns a window&#8217;s short name, which is the same as the <i>name</i> argument passed to <code>Tk_CreateWindow</code> when the window was created. The value is returned as a Tk_Uid, which may be used just like a string pointer but also has the properties of a unique identifier (see the manual entry for <code>Tk_GetUid</code> for details). </p>
<p> The <code>Tk_PathName</code> macro returns a hierarchical name for <i>tkwin</i>. Path names have a structure similar to file names in Unix but with dots between elements instead of slashes: the main window for an application has the path name &#8220;.&#8221;; its children have names like &#8220;.a&#8221; and &#8220;.b&#8221;; their children have names like &#8220;.a.aa&#8221; and &#8220;.b.bb&#8221;; and so on. A window is considered to be a child of another window for naming purposes if the second window was named as the first window&#8217;s <i>parent</i> when the first window was created. This is not always the same as the X window hierarchy. For example, a pop-up is created as a child of the root window, but its logical parent will usually be a window within the application. </p>
<p> The procedure <code>Tk_NameToWindow</code> returns the token for a window given its path name (the <i>pathName</i> argument) and another window belonging to the same main window (<i>tkwin</i>). It normally returns a token for the named window, but if no such window exists <code>Tk_NameToWindow</code> leaves an error message in <i>interp-&gt;result</i> and returns NULL. The <i>tkwin</i> argument to <code>Tk_NameToWindow</code> is needed because path names are only unique within a single application hierarchy. If, for example, a single process has opened two main windows, each will have a separate naming hierarchy and the same path name might appear in each of the hierarchies. Normally <i>tkwin</i> is the main window of the desired hierarchy, but this need not be the case: any window in the desired hierarchy may be used. </p>
<h2>Keywords</h2>
<p>name, path name, token, window</p>
