---
title: "xmcreatebulletinboarddialog(3)"
name: "xmcreatebulletinboarddialog"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreatebulletinboarddialog/"
description: "XmCreateBulletinBoardDialog — The BulletinBoard BulletinBoardDialog convenience creation function"
---

<p><code>XmCreateBulletinBoardDialog</code> &#8212; The BulletinBoard BulletinBoardDialog convenience creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/BulletinB.h&gt;
<code>Widget XmCreateBulletinBoardDialog</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateBulletinBoardDialog</code> is a convenience creation function that creates a DialogShell and an unmanaged BulletinBoard child of the DialogShell. A BulletinBoardDialog is used for interactions not supported by the standard dialog set. This function does not automatically create any labels, buttons, or other dialog components. Such components should be added by the application after the BulletinBoardDialog is created. </p>
<p> Use <code>XtManageChild</code> to pop up the BulletinBoardDialog (passing the BulletinBoard as the widget parameter); use <code>XtUnmanageChild</code> to pop it down. </p>
<p> <code>XmCreateBulletinBoardDialog</code> forces the value of the Shell resource <code>XmNallowShellResize</code> to True.</p>
<dl COMPACT>
<dt><i>parent</i></dt>
<dd>Specifies the parent widget ID</dd>
<dt><i>name</i></dt>
<dd>Specifies the name of the created widget</dd>
<dt><i>arglist</i></dt>
<dd>Specifies the argument list</dd>
<dt><i>argcount</i></dt>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dd></dl>
<p> For a complete definition of BulletinBoard and its associated resources, see <code><a href="/docs/linux/man/3-xmbulletinboard/">XmBulletinBoard</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the BulletinBoard widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmbulletinboard/">XmBulletinBoard</a></code>(3).</p>
