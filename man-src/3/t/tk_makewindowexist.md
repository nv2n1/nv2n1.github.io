---
title: "tk_makewindowexist(3)"
name: "tk_makewindowexist"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_makewindowexist/"
description: "Tk_CreateWindow, Tk_CreateWindowFromPath, Tk_DestroyWindow, Tk_MakeWindowExist – create or delete window"
---

<p>Tk_CreateWindow, Tk_CreateWindowFromPath, Tk_DestroyWindow, Tk_MakeWindowExist &#8211; create or delete window </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
Tk_Window
<code>Tk_CreateWindow</code>(<i>interp, parent, name, topLevScreen</i>)
Tk_Window
<code>Tk_CreateAnonymousWindow</code>(<i>interp, parent, topLevScreen</i>)
Tk_Window
<code>Tk_CreateWindowFromPath</code>(<i>interp, tkwin, pathName, topLevScreen</i>)
<code>Tk_DestroyWindow</code>(<i>tkwin</i>)
<code>Tk_MakeWindowExist</code>(<i>tkwin</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (out) Tcl interpreter to use for error reporting. If no error occurs, then <i>*interp</i> is not modified.</p>
<dd>Tk_Window <i>parent</i> (in) Token for the window that is to serve as the logical parent of the new window.</p>
<dd>const char <i>*name</i> (in) Name to use for this window. Must be unique among all children of the same <i>parent</i>.</p>
<dd>const char <i>*topLevScreen</i> (in) Has same format as <i>screenName</i>. If NULL, then new window is created as an internal window. If non-NULL, new window is created as a top-level window on screen <i>topLevScreen</i>. If <i>topLevScreen</i> is an empty string (&#8220;&#8221;) then new window is created as top-level window of <i>parent</i>&#8216;s screen.</p>
<dd>Tk_Window <i>tkwin</i> (in) Token for window.</p>
<dd>const char <i>*pathName</i> (in) Name of new window, specified as path name within application (e.g. <code>.a.b.c</code>).
</dl>
<h2>Description</h2>
<p>The procedures <code>Tk_CreateWindow</code>, <code>Tk_CreateAnonymousWindow</code>, and <code>Tk_CreateWindowFromPath</code> are used to create new windows for use in Tk-based applications. Each of the procedures returns a token that can be used to manipulate the window in other calls to the Tk library. If the window could not be created successfully, then NULL is returned and <i>interp-&gt;result</i> is modified to hold an error message. </p>
<p> Tk supports two different kinds of windows: internal windows and top-level windows. An internal window is an interior window of a Tk application, such as a scrollbar or menu bar or button. A top-level window is one that is created as a child of a screen&#8217;s root window, rather than as an interior window, but which is logically part of some existing main window. Examples of top-level windows are pop-up menus and dialog boxes. </p>
<p> New windows may be created by calling <code>Tk_CreateWindow</code>. If the <i>topLevScreen</i> argument is NULL, then the new window will be an internal window. If <i>topLevScreen</i> is non-NULL, then the new window will be a top-level window: <i>topLevScreen</i> indicates the name of a screen and the new window will be created as a child of the root window of <i>topLevScreen</i>. In either case Tk will consider the new window to be the logical child of <i>parent</i>: the new window&#8217;s path name will reflect this fact, options may be specified for the new window under this assumption, and so on. The only difference is that new X window for a top-level window will not be a child of <i>parent</i>&#8216;s X window. For example, a pull-down menu&#8217;s <i>parent</i> would be the button-like window used to invoke it, which would in turn be a child of the menu bar window. A dialog box might have the application&#8217;s main window as its parent. </p>
<p> <code>Tk_CreateAnonymousWindow</code> differs from <code>Tk_CreateWindow</code> in that it creates an unnamed window. This window will be manipulable only using C interfaces, and will not be visible to Tcl scripts. Both interior windows and top-level windows may be created with <code>Tk_CreateAnonymousWindow</code>. </p>
<p> <code>Tk_CreateWindowFromPath</code> offers an alternate way of specifying new windows. In <code>Tk_CreateWindowFromPath</code> the new window is specified with a token for any window in the target application (<i>tkwin</i>), plus a path name for the new window. It produces the same effect as <code>Tk_CreateWindow</code> and allows both top-level and internal windows to be created, depending on the value of <i>topLevScreen</i>. In calls to <code>Tk_CreateWindowFromPath</code>, as in calls to <code>Tk_CreateWindow</code>, the parent of the new window must exist at the time of the call, but the new window must not already exist. </p>
<p> The window creation procedures do not actually issue the command to X to create a window. Instead, they create a local data structure associated with the window and defer the creation of the X window. The window will actually be created by the first call to <code>Tk_MapWindow</code>. Deferred window creation allows various aspects of the window (such as its size, background color, etc.) to be modified after its creation without incurring any overhead in the X server. When the window is finally mapped all of the window attributes can be set while creating the window. </p>
<p> The value returned by a window-creation procedure is not the X token for the window (it cannot be, since X has not been asked to create the window yet). Instead, it is a token for Tk&#8217;s local data structure for the window. Most of the Tk library procedures take Tk_Window tokens, rather than X identifiers. The actual X window identifier can be retrieved from the local data structure using the <code>Tk_WindowId</code> macro; see the manual entry for <code>Tk_WindowId</code> for details. </p>
<p> <code>Tk_DestroyWindow</code> deletes a window and all the data structures associated with it, including any event handlers created with <code>Tk_CreateEventHandler</code>. In addition, <code>Tk_DestroyWindow</code> will delete any children of <i>tkwin</i> recursively (where children are defined in the Tk sense, consisting of all windows that were created with the given window as <i>parent</i>). If <i>tkwin</i> is an internal window, then event handlers interested in destroy events are invoked immediately. If <i>tkwin</i> is a top-level or main window, then the event handlers will be invoked later, after X has seen the request and returned an event for it. </p>
<p> If a window has been created but has not been mapped, so no X window exists, it is possible to force the creation of the X window by calling <code>Tk_MakeWindowExist</code>. This procedure issues the X commands to instantiate the window given by <i>tkwin</i>. </p>
<h2>Keywords</h2>
<p>create, deferred creation, destroy, display, internal window, screen, top-level window, window</p>
