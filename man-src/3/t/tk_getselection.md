---
title: "tk_getselection(3)"
name: "tk_getselection"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_getselection/"
description: "Tk_GetSelection – retrieve the contents of a selection"
---

<p>Tk_GetSelection &#8211; retrieve the contents of a selection </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
int
<code>Tk_GetSelection</code>(<i>interp, tkwin, selection, target, proc, clientData</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter to use for reporting errors.</p>
<dd>Tk_Window <i>tkwin</i> (in) Window on whose behalf to retrieve the selection (determines display from which to retrieve).</p>
<dd>Atom <i>selection</i> (in) The name of the selection to be retrieved.</p>
<dd>Atom <i>target</i> (in) Form in which to retrieve selection.</p>
<dd>Tk_GetSelProc <i>*proc</i> (in) Procedure to invoke to process pieces of the selection as they are retrieved.</p>
<dd>ClientData <i>clientData</i> (in) Arbitrary one-word value to pass to <i>proc</i>. </p>
</dl>
<h2>Description</h2>
<p><code>Tk_GetSelection</code> retrieves the selection specified by the atom <i>selection</i> in the format specified by <i>target</i>. The selection may actually be retrieved in several pieces; as each piece is retrieved, <i>proc</i> is called to process the piece. <i>Proc</i> should have arguments and result that match the type <code>Tk_GetSelProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef int Tk_GetSelProc(
 ClientData <i>clientData</i>,
 Tcl_Interp *<i>interp</i>,
 char *<i>portion</i>);</pre>
</dl>
<p> The <i>clientData</i> and <i>interp</i> parameters to <i>proc</i> will be copies of the corresponding arguments to <code>Tk_GetSelection</code>. <i>Portion</i> will be a pointer to a string containing part or all of the selection. For large selections, <i>proc</i> will be called several times with successive portions of the selection. The X Inter-Client Communication Conventions Manual allows a selection to be returned in formats other than strings, e.g. as an array of atoms or integers. If this happens, Tk converts the selection back into a string before calling <i>proc</i>. If a selection is returned as an array of atoms, Tk converts it to a string containing the atom names separated by white space. For any other format besides string, Tk converts a selection to a string containing hexadecimal values separated by white space. </p>
<p> <code>Tk_GetSelection</code> returns to its caller when the selection has been completely retrieved and processed by <i>proc</i>, or when a fatal error has occurred (e.g. the selection owner did not respond promptly). <code>Tk_GetSelection</code> normally returns <code>TCL_OK</code>; if an error occurs, it returns <code>TCL_ERROR</code> and leaves an error message in <i>interp-&gt;result</i>. <i>Proc</i> should also return either <code>TCL_OK</code> or <code>TCL_ERROR</code>. If <i>proc</i> encounters an error in dealing with the selection, it should leave an error message in <i>interp-&gt;result</i> and return <code>TCL_ERROR</code>; this will abort the selection retrieval. </p>
<h2>Keywords</h2>
<p>format, get, selection retrieval</p>
