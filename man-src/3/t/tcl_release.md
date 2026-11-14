---
title: "tcl_release(3)"
name: "tcl_release"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_release/"
description: "Tcl_Preserve, Tcl_Release, Tcl_EventuallyFree – avoid freeing storage while it is being used"
---

<p>Tcl_Preserve, Tcl_Release, Tcl_EventuallyFree &#8211; avoid freeing storage while it is being used </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
<code>Tcl_Preserve</code>(<i>clientData</i>)
<code>Tcl_Release</code>(<i>clientData</i>)
<code>Tcl_EventuallyFree</code>(<i>clientData, freeProc</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>ClientData <i>clientData</i> (in) Token describing structure to be freed or reallocated. Usually a pointer to memory for structure.</p>
<dd>Tcl_FreeProc <i>*freeProc</i> (in) Procedure to invoke to free <i>clientData</i>. </p>
</dl>
<h2>Description</h2>
<p>These three procedures help implement a simple reference count mechanism for managing storage. They are designed to solve a problem having to do with widget deletion, but are also useful in many other situations. When a widget is deleted, its widget record (the structure holding information specific to the widget) must be returned to the storage allocator. However, it is possible that the widget record is in active use by one of the procedures on the stack at the time of the deletion. This can happen, for example, if the command associated with a button widget causes the button to be destroyed: an X event causes an event-handling C procedure in the button to be invoked, which in turn causes the button&#8217;s associated Tcl command to be executed, which in turn causes the button to be deleted, which in turn causes the button&#8217;s widget record to be de-allocated. Unfortunately, when the Tcl command returns, the button&#8217;s event-handling procedure will need to reference the button&#8217;s widget record. Because of this, the widget record must not be freed as part of the deletion, but must be retained until the event-handling procedure has finished with it. In other situations where the widget is deleted, it may be possible to free the widget record immediately. </p>
<p> <code>Tcl_Preserve</code> and <code>Tcl_Release</code> implement short-term reference counts for their <i>clientData</i> argument. The <i>clientData</i> argument identifies an object and usually consists of the address of a structure. The reference counts guarantee that an object will not be freed until each call to <code>Tcl_Preserve</code> for the object has been matched by calls to <code>Tcl_Release</code>. There may be any number of unmatched <code>Tcl_Preserve</code> calls in effect at once. </p>
<p> <code>Tcl_EventuallyFree</code> is invoked to free up its <i>clientData</i> argument. It checks to see if there are unmatched <code>Tcl_Preserve</code> calls for the object. If not, then <code>Tcl_EventuallyFree</code> calls <i>freeProc</i> immediately. Otherwise <code>Tcl_EventuallyFree</code> records the fact that <i>clientData</i> needs eventually to be freed. When all calls to <code>Tcl_Preserve</code> have been matched with calls to <code>Tcl_Release</code> then <i>freeProc</i> will be called by <code>Tcl_Release</code> to do the cleanup. </p>
<p> All the work of freeing the object is carried out by <i>freeProc</i>. <i>FreeProc</i> must have arguments and result that match the type <code>Tcl_FreeProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef void Tcl_FreeProc(char *<i>blockPtr</i>);</pre>
</dl>
<p> The <i>blockPtr</i> argument to <i>freeProc</i> will be the same as the <i>clientData</i> argument to <code>Tcl_EventuallyFree</code>. The type of <i>blockPtr</i> (<code>char *</code>) is different than the type of the <i>clientData</i> argument to <code>Tcl_EventuallyFree</code> for historical reasons, but the value is the same. </p>
<p> When the <i>clientData</i> argument to <code>Tcl_EventuallyFree</code> refers to storage allocated and returned by a prior call to <code>Tcl_Alloc</code>, <code>ckalloc</code>, or another function of the Tcl library, then the <i>freeProc</i> argument should be given the special value of <code>TCL_DYNAMIC</code>. </p>
<p> This mechanism can be used to solve the problem described above by placing <code>Tcl_Preserve</code> and <code>Tcl_Release</code> calls around actions that may cause undesired storage re-allocation. The mechanism is intended only for short-term use (i.e. while procedures are pending on the stack); it will not work efficiently as a mechanism for long-term reference counts. The implementation does not depend in any way on the internal structure of the objects being freed; it keeps the reference counts in a separate structure. </p>
<h2>See Also</h2>
<p>Tcl_Interp, Tcl_Alloc </p>
<h2>Keywords</h2>
<p>free, reference count, storage</p>
