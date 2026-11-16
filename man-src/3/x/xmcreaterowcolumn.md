---
title: "xmcreaterowcolumn(3)"
name: "xmcreaterowcolumn"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreaterowcolumn/"
description: "XmCreateRowColumn — The RowColumn widget creation function"
---

<p><code>XmCreateRowColumn</code> &#8212; The RowColumn widget creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/RowColumn.h&gt;
<code>Widget XmCreateRowColumn</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateRowColumn</code> creates an instance of a RowColumn widget and returns the associated widget ID. If <code>XmNrowColumnType</code> is not specified, then it is created with <code>XmWORK_AREA</code>, which is the default. </p>
<p> If this function is used to create a Popup Menu of type <code>XmMENU_POPUP</code> or a Pulldown Menu of type <code>XmMENU_PULLDOWN</code>, a MenuShell widget is not automatically created as the parent of the menu pane. The application must first create the MenuShell by using either <code>XmCreateMenuShell</code> or the standard toolkit create function.</p>
<dl COMPACT>
<dt><i>parent</i></dt>
<dd>Specifies the parent widget ID</dd>
<dt><i>name</i></dt>
<dd>Specifies the name of the created widget</dd>
<dt><i>arglist</i></dt>
<dd>Specifies the argument list</dd>
<dt><i>argcount</i></dt>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dd></dl>
<p> For a complete definition of RowColumn and its associated resources, see <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the RowColumn widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcreatemenubar/">XmCreateMenuBar</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatemenushell/">XmCreateMenuShell</a></code>(3), <code><a href="/docs/linux/man/3-xmcreateoptionmenu/">XmCreateOptionMenu</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatepopupmenu/">XmCreatePopupMenu</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatepulldownmenu/">XmCreatePulldownMenu</a></code>(3), <code><a href="/docs/linux/man/3-xmcreateradiobox/">XmCreateRadioBox</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatesimplecheckbox/">XmCreateSimpleCheckBox</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatesimplemenubar/">XmCreateSimpleMenuBar</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatesimpleoptionmenu/">XmCreateSimpleOptionMenu</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatesimplepopupmenu/">XmCreateSimplePopupMenu</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatesimplepulldownmenu/">XmCreateSimplePulldownMenu</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatesimpleradiobox/">XmCreateSimpleRadioBox</a></code>(3), <code><a href="/docs/linux/man/3-xmcreateworkarea/">XmCreateWorkArea</a></code>(3), <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatesimplecheckbox/">XmVaCreateSimpleCheckBox</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatesimplemenubar/">XmVaCreateSimpleMenuBar</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatesimpleoptionmenu/">XmVaCreateSimpleOptionMenu</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatesimplepopupmenu/">XmVaCreateSimplePopupMenu</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatesimplepulldownmenu/">XmVaCreateSimplePulldownMenu</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatesimpleradiobox/">XmVaCreateSimpleRadioBox</a></code>(3).</p>
