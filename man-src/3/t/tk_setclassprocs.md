---
title: "tk_setclassprocs(3)"
name: "tk_setclassprocs"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_setclassprocs/"
description: "Tk_SetClassProcs – register widget specific procedures"
---

<p>Tk_SetClassProcs &#8211; register widget specific procedures </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
<code>Tk_SetClassProcs</code>(<i>tkwin, procs, instanceData</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Window <i>tkwin</i> (in) Token for window to modify.</p>
<dd>Tk_ClassProcs <i>*procs</i> (in) Pointer to data structure containing widget specific procedures. The data structure pointed to by <i>procs</i> must be static: Tk keeps a reference to it as long as the window exists.</p>
<dd>ClientData <i>instanceData</i> (in) Arbitrary one-word value to pass to widget callbacks. </p>
</dl>
<h2>Description</h2>
<p><code>Tk_SetClassProcs</code> is called to register a set of procedures that are used as callbacks in different places. </p>
<p> The structure pointed to by <i>procs</i> contains the following:</p>
<dl COMPACT>
<dd>
<pre>typedef struct Tk_ClassProcs {
 unsigned int <i>size</i>;
 Tk_ClassWorldChangedProc *<i>worldChangedProc</i>;
 Tk_ClassCreateProc *<i>createProc</i>;
 Tk_ClassModalProc *<i>modalProc</i>;
} Tk_ClassProcs;</pre>
</dl>
<p> The <i>size</i> field is used to simplify future expansion of the structure. It should always be set to (literally) <code>sizeof(Tk_ClassProcs)</code>. </p>
<p> <i>worldChangedProc</i> is invoked when the system has altered in some way that requires some reaction from the widget. For example, when a font alias (see the <code>font</code> manual entry) is reconfigured, widgets configured to use that font alias must update their display accordingly. <i>worldChangedProc</i> should have arguments and results that match the type <code>Tk_ClassWorldChangedProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef void Tk_ClassWorldChangedProc(
 ClientData <i>instanceData</i>);</pre>
</dl>
<p> The <i>instanceData</i> parameter passed to the <i>worldChangedProc</i> will be identical to the <i>instanceData</i> parameter passed to <code>Tk_SetClassProcs</code>. </p>
<p> <i>createProc</i> is used to create platform-dependant windows. It is invoked by <code>Tk_MakeWindowExist</code>. <i>createProc</i> should have arguments and results that match the type <code>Tk_ClassCreateProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef Window Tk_ClassCreateProc(
 Tk_Window <i>tkwin</i>,
 Window <i>parent</i>,
 ClientData <i>instanceData</i>);</pre>
</dl>
<p> The <i>tkwin</i> and <i>instanceData</i> parameters will be identical to the <i>tkwin</i> and <i>instanceData</i> parameters passed to <code>Tk_SetClassProcs</code>. The <i>parent</i> parameter will be the parent of the window to be created. The <i>createProc</i> should return the created window. </p>
<p> <i>modalProc</i> is invoked after all bindings on a widget have been triggered in order to handle a modal loop. <i>modalProc</i> should have arguments and results that match the type <code>Tk_ClassModalProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef void Tk_ClassModalProc(
 Tk_Window <i>tkwin</i>,
 XEvent *<i>eventPtr</i>);</pre>
</dl>
<p> The <i>tkwin</i> parameter to <i>modalProc</i> will be identical to the <i>tkwin</i> parameter passed to <code>Tk_SetClassProcs</code>. The <i>eventPtr</i> parameter will be a pointer to an XEvent structure describing the event being processed. </p>
<h2>Keywords</h2>
<p>callback, class</p>
