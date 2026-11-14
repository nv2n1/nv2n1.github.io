---
title: "tk_ownselection(3)"
name: "tk_ownselection"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_ownselection/"
description: "Tk_OwnSelection – make a window the owner of the primary selection"
---

<p>Tk_OwnSelection &#8211; make a window the owner of the primary selection </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
<code>Tk_OwnSelection</code>(<i>tkwin, selection, proc, clientData</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Window <i>tkwin</i> (in) Window that is to become new selection owner.</p>
<dd>Atom <i>selection</i> (in) The name of the selection to be owned, such as XA_PRIMARY.</p>
<dd>Tk_LostSelProc <i>*proc</i> (in) Procedure to invoke when <i>tkwin</i> loses selection ownership later.</p>
<dd>ClientData <i>clientData</i> (in) Arbitrary one-word value to pass to <i>proc</i>. </p>
</dl>
<h2>Description</h2>
<p><code>Tk_OwnSelection</code> arranges for <i>tkwin</i> to become the new owner of the selection specified by the atom <i>selection</i>. After this call completes, future requests for the selection will be directed to handlers created for <i>tkwin</i> using <code>Tk_CreateSelHandler</code>. When <i>tkwin</i> eventually loses the selection ownership, <i>proc</i> will be invoked so that the window can clean itself up (e.g. by unhighlighting the selection). <i>Proc</i> should have arguments and result that match the type <code>Tk_LostSelProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef void Tk_LostSelProc(ClientData <i>clientData</i>);</pre>
</dl>
<p> The <i>clientData</i> parameter to <i>proc</i> is a copy of the <i>clientData</i> argument given to <code>Tk_OwnSelection</code>, and is usually a pointer to a data structure containing application-specific information about <i>tkwin</i>. </p>
<h2>Keywords</h2>
<p>own, selection owner</p>
