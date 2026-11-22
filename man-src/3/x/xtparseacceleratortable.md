---
title: "xtparseacceleratortable(3)"
name: "xtparseacceleratortable"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtparseacceleratortable/"
description: "XtParseAcceleratorTable, XtInstallAccelerators, XtInstallAllAccelerators – managing accelerator tables"
---

<p>XtParseAcceleratorTable, XtInstallAccelerators, XtInstallAllAccelerators &#8211; managing accelerator tables </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>XtAccelerators XtParseAcceleratorTable(const char * <i>source</i>);</dd>
<dd>void XtInstallAccelerators(Widget <i>destination</i>, Widget <i>source</i>);</dd>
<dd>void XtInstallAllAccelerators(Widget <i>destination</i>, Widget <i>source</i>);</dd></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>source</i></dt>
<dd>Specifies the accelerator table to compile.</dd>
<dt><i>destination</i></dt>
<dd>Specifies the widget on which the accelerators are to be installed.</dd>
<dt><i>source</i></dt>
<dd>Specifies the widget or the root widget of the widget tree from which the accelerators are to come.</dd></dl>
<h2>Description</h2>
<p>The <code>XtParseAcceleratorTable</code> function compiles the accelerator table into the opaque internal representation. </p>
<p> The <code>XtInstallAccelerators</code> function installs the accelerators from source onto destination by augmenting the destination translations with the source accelerators. If the source display_accelerator method is non-NULL, <code>XtInstallAccelerators</code> calls it with the source widget and a string representation of the accelerator table, which indicates that its accelerators have been installed and that it should display them appropriately. The string representation of the accelerator table is its canonical translation table representation. </p>
<p> The <code>XtInstallAllAccelerators</code> function recursively descends the widget tree rooted at source and installs the accelerators of each widget encountered onto destination. A common use os to call <code>XtInstallAllAccelerators</code> and pass the application main window as the source.</p>
<h2>See Also</h2>
<p>XtParseTranslationTable(1)<br/>
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br/>
 <i>Xlib &#8211; C Language X Interface</i></p>
