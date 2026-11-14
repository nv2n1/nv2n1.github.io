---
title: "xtownselectionincremental(3)"
name: "xtownselectionincremental"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtownselectionincremental/"
description: "XtOwnSelection, XtOwnSelectionIncremental, XtDisownSelection – set selection owner"
---

<p>XtOwnSelection, XtOwnSelectionIncremental, XtDisownSelection &#8211; set selection owner </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>Boolean XtOwnSelection(Widget <i>w</i>, Atom <i>selection</i>, Time <i>time</i>, XtConvertSelectionProc <i>convert_proc</i>, XtLoseSelectionProc <i>lose_selection</i>, XtSelectionDoneProc <i>done_proc</i>);</p>
<dd>Boolean XtOwnSelectionIncremental(Widget <i>w</i>, Atom <i>selection</i>, Time <i>time</i>, XtConvertSelectionIncrProc <i>convert_callback</i>, XtLoseSelectionIncrProc <i>lose_callback</i>, XtSelectionDoneIncrProc <i>done_callback</i>, XtCancelConvertSelectionProc <i>cancel_callback</i>, XtPointer <i>client_data</i>);</p>
<dd>void XtDisownSelection(Widget <i>w</i>, Atom <i>selection</i>, Time <i>time</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>convert_proc</i></p>
<dd>Specifies the procedure that is to be called whenever someone requests the current value of the selection.</p>
<dt><i>done_proc</i></p>
<dd>Specifies the procedure that is called after the requestor has received the selection or NULL if the owner is not interested in being called back.</p>
<dt><i>lose_selection</i></p>
<dd>Specifies the procedure that is to be called whenever the widget has lost selection ownership or NULL if the owner is not interested in being called back.</p>
<dt><i>selection</i></p>
<dd>Specifies an atom that describes the type of the selection (for example, <code>XA_PRIMARY</code>, <code>XA_SECONDARY</code>, or <code>XA_CLIPBOARD</code>).</p>
<dt><i>time</i></p>
<dd>Specifies the timestamp that indicates when the selection ownership should commence or is to be relinquished.</p>
<dt><i>w</i></p>
<dd>Specifies the widget that wishes to become the owner or to relinquish ownership.</dl>
<h2>Description</h2>
<p>The <code>XtOwnSelection</code> function informs the Intrinsics selection mechanism that a widget believes it owns a selection. It returns <code>True</code> if the widget has successfully become the owner and <code>False</code> otherwise. The widget may fail to become the owner if some other widget has asserted ownership at a time later than this widget. Note that widgets can lose selection ownership either because someone else asserted later ownership of the selection or because the widget voluntarily gave up ownership of the selection. Also note that the lose_selection procedure is not called if the widget fails to obtain selection ownership in the first place. </p>
<p> The <code>XtOwnSelectionIncremental</code> procedure informs the Intrinsics incremental selection mechanism that the specified widget wishes to own the selection. It returns <code>True</code> if the specified widget successfully becomes the selection owner or <code>False</code> otherwise. For more information about <i>selection</i>, <i>target</i>, and <i>time</i>, see Section 2.6 of the <i>Inter-Client Communication Conventions Manual</i>. </p>
<p> A widget that becomes the selection owner using <code>XtOwnSelectionIncremental</code> may use <code>XtDisownSelection</code> to relinquish selection ownership. </p>
<p> The <code>XtDisownSelection</code> function informs the Intrinsics selection mechanism that the specified widget is to lose ownership of the selection. If the widget does not currently own the selection either because it lost the selection or because it never had the selection to begin with, <code>XtDisownSelection</code> does nothing. </p>
<p> After a widget has called <code>XtDisownSelection</code>, its convert procedure is not called even if a request arrives later with a timestamp during the period that this widget owned the selection. However, its done procedure will be called if a conversion that started before the call to <code>XtDisownSelection</code> finishes after the call to <code>XtDisownSelection</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtappgetselectiontimeout/">XtAppGetSelectionTimeout</a>(3), <a href="/docs/linux/man/3-xtgetselectionvalue/">XtGetSelectionValue</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
