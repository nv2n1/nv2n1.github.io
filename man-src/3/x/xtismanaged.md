---
title: "xtismanaged(3)"
name: "xtismanaged"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtismanaged/"
description: "XtManageChildren, XtManageChild, XtUnmanageChildren, XtUnmanageChild, XtChangeManagedSet, XtIsManaged – manage and unmanage children"
---

<p>XtManageChildren, XtManageChild, XtUnmanageChildren, XtUnmanageChild, XtChangeManagedSet, XtIsManaged &#8211; manage and unmanage children </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>typedef Widget *WidgetList;</p>
<dd>void XtManageChildren(WidgetList <i>children</i>, Cardinal <i>num_children</i>);</p>
<dd>void XtManageChild(Widget <i>child</i>);</p>
<dd>void XtUnmanageChildren(WidgetList <i>children</i>, Cardinal <i>num_children</i>);</p>
<dd>void XtUnmanageChild(Widget <i>child</i>);</p>
<dd>void XtChangeManagedSet(WidgetList <i>unmanage_children</i>, Cardinal <i>num_unmanage_children</i>, XtDoChangeProc <i>do_change_proc</i>, XtPointer <i>client_data</i>, WidgetList <i>manage_children</i>, Cardinal <i>num_manage_children</i>);</p>
<dd>Boolean XtIsManaged(Widget <i>widget</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>child</i></p>
<dd>Specifies the child.</p>
<dt><i>children</i></p>
<dd>Specifies a list of child widgets.</p>
<dt><i>num_children</i></p>
<dd>Specifies the number of children.</p>
<dt><i>widget</i></p>
<dd>Specifies the widget.</p>
<dt><i>manage_children</i></p>
<dd>Specifies the list of widget children to add to the managed set.</p>
<dt><i>num_manage_children</i></p>
<dd>Specifies the number of entries in the manage_children list.</p>
<dt><i>unmanage_children</i></p>
<dd>Specifies the list of widget children to remove from the managed set.</p>
<dt><i>num_unmanage_children</i></p>
<dd>Specifies the number of entries in the unmanage_children list.</p>
<dt><i>do_change_proc</i></p>
<dd>Specifies the post unmanage, pre manage hook procedure to invoke.</p>
<dt><i>client_data</i></p>
<dd>Specifies the client data to be passed to the hook procedure.</dl>
<h2>Description</h2>
<p>The <code>XtManageChildren</code> function performs the following:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Issues an error if the children do not all have the same parent or if the parent is not a subclass of <code>compositeWidgetClass</code>.</p>
<dt>&bull;</p>
<dd>Returns immediately if the common parent is being destroyed; otherwise, for each unique child on the list, <code>XtManageChildren</code> ignores the child if it already is managed or is being destroyed and marks it if not.</p>
<dt>&bull;</p>
<dd>If the parent is realized and after all children have been marked, it makes some of the newly managed children viewable:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&#8211;</p>
<dd>Calls the change_managed routine of the widgets&#8217; parent.</p>
<dt>&#8211;</p>
<dd>Calls <code>XtRealizeWidget</code> on each previously unmanaged child that is unrealized.</p>
<dt>&#8211;</p>
<dd>Maps each previously unmanaged child that has map_when_managed <code>True</code>.</dl>
</dl>
</dl>
<p> Managing children is independent of the ordering of children and independent of creating and deleting children. The layout routine of the parent should consider children whose managed field is <code>True</code> and should ignore all other children. Note that some composite widgets, especially fixed boxes, call <code>XtManageChild</code> from their insert_child procedure. </p>
<p> If the parent widget is realized, its change_managed procedure is called to notify it that its set of managed children has changed. The parent can reposition and resize any of its children. It moves each child as needed by calling <code>XtMoveWidget</code>, which first updates the x and y fields and then calls <code>XMoveWindow</code> if the widget is realized. </p>
<p> The <code>XtManageChild</code> function constructs a <code>WidgetList</code> of length one and calls <code>XtManageChildren</code>. </p>
<p> The <code>XtUnmanageChildren</code> function performs the following:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Issues an error if the children do not all have the same parent or if the parent is not a subclass of <code>compositeWidgetClass</code>.</p>
<dt>&bull;</p>
<dd>Returns immediately if the common parent is being destroyed; otherwise, for each unique child on the list, <code>XtUnmanageChildren</code> performs the following:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&#8211;</p>
<dd>Ignores the child if it already is unmanaged or is being destroyed and marks it if not.</p>
<dt>&#8211;</p>
<dd>If the child is realized, it makes it nonvisible by unmapping it.</dl>
</dl>
<dt>&bull;</p>
<dd>Calls the change_managed routine of the widgets&#8217; parent after all children have been marked if the parent is realized.</dl>
<p> <code>XtUnmanageChildren</code> does not destroy the children widgets. Removing widgets from a parent&#8217;s managed set is often a temporary banishment, and, some time later, you may manage the children again. </p>
<p> The <code>XtUnmanageChild</code> function constructs a widget list of length one and calls <code>XtUnmanageChildren</code>. </p>
<p> The <code>XtChangeManagedSet</code> function performs the following:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Issues an error if the widgets specified in the <i>manage_children</i> and the <i>unmanage_children</i> lists to no all have the same parent, or if that parent is not a subclass of compositeWidgetClass.</p>
<dt>&bull;</p>
<dd>Returns immediately if the common parent is being destroyed.</p>
<dt>&bull;</p>
<dd>If no <code>CompositeClassExtension</code> is defined, or a <code>CompositeClassExtension</code> is defined but with an <i>allows_change_managed_set</i> field with a value of <code>False</code>, and <code>XtChangeManagedSet</code> was invoked with a non-NULL <i>do_change_proc</i> procedure then <code>XtChangeManagedSet</code> performs the following:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&#8211;</p>
<dd>Calls <code>XtUnmanageChildren</code> (<i>unmanage_children</i>, <i>num_unmanage_children</i>).</p>
<dt>&#8211;</p>
<dd>Calls the <i>do_change_proc</i> specified.</p>
<dt>&#8211;</p>
<dd>Calls <code>XtManageChildren</code> (<i>manage_children</i>, <i>num_manage_children</i>) and then returns immediately.</dl>
</dl>
<dt>&bull;</p>
<dd>Otherwise, if a <code>CompositeClassExtension</code> is defined with an <i>allows_change_managed_set</i> field with a value of <code>True</code>, or if no <code>CompositeClassExtension</code> is defined, and <code>XtChangeManagedSet </code> was invoked with a NULL <i>do_change_proc</i> procedure, then the following is performed:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&#8211;</p>
<dd>For each child on the <i>unmanage_children</i> list; if the child is already unmanaged or is being destroyed it is ignored, otherwise it is marked as being unmanaged and if it is realized it is made nonvisible by being unmapped.</p>
<dt>&#8211;</p>
<dd>If the <i>do_change_proc</i> procedure is non-NULL then it is invoked as specified.</p>
<dt>&#8211;</p>
<dd>For each child on the <i>manage_children</i> list; if the child is already managed or it is being destroyed it is ignored, otherwise it is marked as managed</dl>
</dl>
<dt>&bull;</p>
<dd>If the parent is realized and after all children have been marked, the change_managed method of the parent is invoked and subsequently some of the newly managed children are made viewable by:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&#8211;</p>
<dd>Calling <code>XtRealizeWidget</code> on each of the previously unmanaged child that is unrealized.</p>
<dt>&#8211;</p>
<dd>Mapping each previously unmanaged child that has <i>map_when_managed</i> <code>True</code>.</dl>
</dl>
</dl>
<p> The <code>XtIsManaged</code> function returns <code>True</code> if the specified widget is of class RectObj or any subclass thereof and is managed, or <code>False</code> otherwise.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtmapwidget/">XtMapWidget</a>(3), <a href="/docs/linux/man/3-xtrealizewidget/">XtRealizeWidget</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
