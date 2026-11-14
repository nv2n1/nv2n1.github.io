---
title: "tk_managegeometry(3)"
name: "tk_managegeometry"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_managegeometry/"
description: "Tk_ManageGeometry – arrange to handle geometry requests for a window"
---

<p>Tk_ManageGeometry &#8211; arrange to handle geometry requests for a window </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
<code>Tk_ManageGeometry</code>(<i>tkwin, mgrPtr, clientData</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Window <i>tkwin</i> (in) Token for window to be managed.</p>
<dd>const Tk_GeomMgr <i>*mgrPtr</i> (in) Pointer to data structure containing information about the geometry manager, or NULL to indicate that <i>tkwin</i>&#8216;s geometry should not be managed anymore. The data structure pointed to by <i>mgrPtr</i> must be static: Tk keeps a reference to it as long as the window is managed.</p>
<dd>ClientData <i>clientData</i> (in) Arbitrary one-word value to pass to geometry manager callbacks.
</dl>
<h2>Description</h2>
<p><code>Tk_ManageGeometry</code> arranges for a particular geometry manager, described by the <i>mgrPtr</i> argument, to control the geometry of a particular slave window, given by <i>tkwin</i>. If <i>tkwin</i> was previously managed by some other geometry manager, the previous manager loses control in favor of the new one. If <i>mgrPtr</i> is NULL, geometry management is cancelled for <i>tkwin</i>. </p>
<p> The structure pointed to by <i>mgrPtr</i> contains information about the geometry manager:</p>
<dl COMPACT>
<dd>
<pre>typedef struct {
 const char *<i>name</i>;
 Tk_GeomRequestProc *<i>requestProc</i>;
 Tk_GeomLostSlaveProc *<i>lostSlaveProc</i>;
} Tk_GeomMgr;</pre>
</dl>
<p> The <i>name</i> field is the textual name for the geometry manager, such as <code>pack</code> or <code>place</code>; this value will be returned by the command <code>winfo manager</code>. </p>
<p> <i>requestProc</i> is a procedure in the geometry manager that will be invoked whenever <code>Tk_GeometryRequest</code> is called by the slave to change its desired geometry. <i>requestProc</i> should have arguments and results that match the type <code>Tk_GeomRequestProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef void Tk_GeomRequestProc(
 ClientData <i>clientData</i>,
 Tk_Window <i>tkwin</i>);</pre>
</dl>
<p> The parameters to <i>requestProc</i> will be identical to the corresponding parameters passed to <code>Tk_ManageGeometry</code>. <i>clientData</i> usually points to a data structure containing application-specific information about how to manage <i>tkwin</i>&#8216;s geometry. </p>
<p> The <i>lostSlaveProc</i> field of <i>mgrPtr</i> points to another procedure in the geometry manager. Tk will invoke <i>lostSlaveProc</i> if some other manager calls <code>Tk_ManageGeometry</code> to claim <i>tkwin</i> away from the current geometry manager. <i>lostSlaveProc</i> is not invoked if <code>Tk_ManageGeometry</code> is called with a NULL value for <i>mgrPtr</i> (presumably the current geometry manager has made this call, so it already knows that the window is no longer managed), nor is it called if <i>mgrPtr</i> is the same as the window&#8217;s current geometry manager. <i>lostSlaveProc</i> should have arguments and results that match the following prototype:</p>
<dl COMPACT>
<dd>
<pre>typedef void Tk_GeomLostSlaveProc(
 ClientData <i>clientData</i>,
 Tk_Window <i>tkwin</i>);</pre>
</dl>
<p> The parameters to <i>lostSlaveProc</i> will be identical to the corresponding parameters passed to <code>Tk_ManageGeometry</code>. </p>
<h2>Keywords</h2>
<p>callback, geometry, managed, request, unmanaged</p>
