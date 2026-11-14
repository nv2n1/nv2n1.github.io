---
title: "tk_deleteselhandler(3)"
name: "tk_deleteselhandler"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_deleteselhandler/"
description: "Tk_CreateSelHandler, Tk_DeleteSelHandler – arrange to handle requests for a selection"
---

<p>Tk_CreateSelHandler, Tk_DeleteSelHandler &#8211; arrange to handle requests for a selection </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
<code>Tk_CreateSelHandler</code>(<i>tkwin, selection, target, proc, clientData, format</i>)
<code>Tk_DeleteSelHandler</code>(<i>tkwin, selection, target</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Window <i>tkwin</i> (in) Window for which <i>proc</i> will provide selection information.</p>
<dd>Atom <i>selection</i> (in) The name of the selection for which <i>proc</i> will provide selection information.</p>
<dd>Atom <i>target</i> (in) Form in which <i>proc</i> can provide the selection (e.g. STRING or FILE_NAME). Corresponds to <i>type</i> arguments in <code>selection</code> commands.</p>
<dd>Tk_SelectionProc <i>*proc</i> (in) Procedure to invoke whenever the selection is owned by <i>tkwin</i> and the selection contents are requested in the format given by <i>target</i>.</p>
<dd>ClientData <i>clientData</i> (in) Arbitrary one-word value to pass to <i>proc</i>.</p>
<dd>Atom <i>format</i> (in) If the selection requestor is not in this process, <i>format</i> determines the representation used to transmit the selection to its requestor.
</dl>
<h2>Description</h2>
<p><code>Tk_CreateSelHandler</code> arranges for a particular procedure (<i>proc</i>) to be called whenever <i>selection</i> is owned by <i>tkwin</i> and the selection contents are requested in the form given by <i>target</i>. <i>Target</i> should be one of the entries defined in the left column of Table 2 of the X Inter-Client Communication Conventions Manual (ICCCM) or any other form in which an application is willing to present the selection. The most common form is STRING. </p>
<p> <i>Proc</i> should have arguments and result that match the type <code>Tk_SelectionProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef int Tk_SelectionProc(
 ClientData <i>clientData</i>,
 int <i>offset</i>,
 char *<i>buffer</i>,
 int <i>maxBytes</i>);</pre>
</dl>
<p> The <i>clientData</i> parameter to <i>proc</i> is a copy of the <i>clientData</i> argument given to <code>Tk_CreateSelHandler</code>. Typically, <i>clientData</i> points to a data structure containing application-specific information that is needed to retrieve the selection. <i>Offset</i> specifies an offset position into the selection, <i>buffer</i> specifies a location at which to copy information about the selection, and <i>maxBytes</i> specifies the amount of space available at <i>buffer</i>. <i>Proc</i> should place a NULL-terminated string at <i>buffer</i> containing <i>maxBytes</i> or fewer characters (not including the terminating NULL), and it should return a count of the number of non-NULL characters stored at <i>buffer</i>. If the selection no longer exists (e.g. it once existed but the user deleted the range of characters containing it), then <i>proc</i> should return -1. </p>
<p> When transferring large selections, Tk will break them up into smaller pieces (typically a few thousand bytes each) for more efficient transmission. It will do this by calling <i>proc</i> one or more times, using successively higher values of <i>offset</i> to retrieve successive portions of the selection. If <i>proc</i> returns a count less than <i>maxBytes</i> it means that the entire remainder of the selection has been returned. If <i>proc</i>&#8216;s return value is <i>maxBytes</i> it means there may be additional information in the selection, so Tk must make another call to <i>proc</i> to retrieve the next portion. </p>
<p> <i>Proc</i> always returns selection information in the form of a character string. However, the ICCCM allows for information to be transmitted from the selection owner to the selection requestor in any of several formats, such as a string, an array of atoms, an array of integers, etc. The <i>format</i> argument to <code>Tk_CreateSelHandler</code> indicates what format should be used to transmit the selection to its requestor (see the middle column of Table 2 of the ICCCM for examples). If <i>format</i> is not STRING, then Tk will take the value returned by <i>proc</i> and divided it into fields separated by white space. If <i>format</i> is ATOM, then Tk will return the selection as an array of atoms, with each field in <i>proc</i>&#8216;s result treated as the name of one atom. For any other value of <i>format</i>, Tk will return the selection as an array of 32-bit values where each field of <i>proc</i>&#8216;s result is treated as a number and translated to a 32-bit value. In any event, the <i>format</i> atom is returned to the selection requestor along with the contents of the selection. </p>
<p> If <code>Tk_CreateSelHandler</code> is called when there already exists a handler for <i>selection</i> and <i>target</i> on <i>tkwin</i>, then the existing handler is replaced with a new one. </p>
<p> <code>Tk_DeleteSelHandler</code> removes the handler given by <i>tkwin</i>, <i>selection</i>, and <i>target</i>, if such a handler exists. If there is no such handler then it has no effect. </p>
<h2>Keywords</h2>
<p>format, handler, selection, target</p>
