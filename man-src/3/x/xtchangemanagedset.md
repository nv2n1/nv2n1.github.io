---
title: "xtchangemanagedset(3)"
name: "xtchangemanagedset"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtchangemanagedset/"
---

XtManageChildren, XtManageChild, XtUnmanageChildren, XtUnmanageChild, XtChangeManagedSet, XtIsManaged - manage and unmanage children 

<h2>Syntax</h2>#include &lt;X11/Intrinsic.h&gt;
<dl COMPACT><dd>typedef Widget *WidgetList;
<dd>void XtManageChildren(WidgetList <i>children</i>, Cardinal <i>num_children</i>);
<dd>void XtManageChild(Widget <i>child</i>);
<dd>void XtUnmanageChildren(WidgetList <i>children</i>, Cardinal <i>num_children</i>);
<dd>void XtUnmanageChild(Widget <i>child</i>);
<dd>void XtChangeManagedSet(WidgetList <i>unmanage_children</i>, Cardinal <i>num_unmanage_children</i>, XtDoChangeProc <i>do_change_proc</i>, XtPointer <i>client_data</i>, WidgetList <i>manage_children</i>, Cardinal <i>num_manage_children</i>);
<dd>Boolean XtIsManaged(Widget <i>widget</i>);</dl><h2>Arguments</h2><dl COMPACT><dt><i>child</i>
<dd>Specifies the child.
<dt><i>children</i>
<dd>Specifies a list of child widgets.
<dt><i>num_children</i>
<dd>Specifies the number of children.
<dt><i>widget</i>
<dd>Specifies the widget.
<dt><i>manage_children</i>
<dd>Specifies the list of widget children to add to the managed set.
<dt><i>num_manage_children</i>
<dd>Specifies the number of entries in the manage_children list.
<dt><i>unmanage_children</i>
<dd>Specifies the list of widget children to remove from the managed set.
<dt><i>num_unmanage_children</i>
<dd>Specifies the number of entries in the unmanage_children list.
<dt><i>do_change_proc</i>
<dd>Specifies the post unmanage, pre manage hook procedure to invoke.
<dt><i>client_data</i>
<dd>Specifies the client data to be passed to the hook procedure.</dl><h2>Description</h2>The <b>XtManageChildren</b> function performs the following:
<dl COMPACT><dt>&bull;
<dd>Issues an error if the children do not all have the same parent or if the parent is not a subclass of <b>compositeWidgetClass</b>.
<dt>&bull;
<dd>Returns immediately if the common parent is being destroyed; otherwise, for each unique child on the list, <b>XtManageChildren</b> ignores the child if it already is managed or is being destroyed and marks it if not.
<dt>&bull;
<dd>If the parent is realized and after all children have been marked, it makes some of the newly managed children viewable:
<dl COMPACT><dd><dl COMPACT><dt>-
<dd>Calls the change_managed routine of the widgets' parent.
<dt>-
<dd>Calls <b>XtRealizeWidget</b> on each previously unmanaged child that is unrealized.
<dt>-
<dd>Maps each previously unmanaged child that has map_when_managed <b>True</b>.</dl></dl>
</dl>
 

 Managing children is independent of the ordering of children and independent of creating and deleting children. The layout routine of the parent should consider children whose managed field is <b>True</b> and should ignore all other children. Note that some composite widgets, especially fixed boxes, call <b>XtManageChild</b> from their insert_child procedure. 

 If the parent widget is realized, its change_managed procedure is called to notify it that its set of managed children has changed. The parent can reposition and resize any of its children. It moves each child as needed by calling <b>XtMoveWidget</b>, which first updates the x and y fields and then calls <b>XMoveWindow</b> if the widget is realized. 

 The <b>XtManageChild</b> function constructs a <b>WidgetList</b> of length one and calls <b>XtManageChildren</b>. 

 The <b>XtUnmanageChildren</b> function performs the following:
<dl COMPACT><dt>&bull;
<dd>Issues an error if the children do not all have the same parent or if the parent is not a subclass of <b>compositeWidgetClass</b>.
<dt>&bull;
<dd>Returns immediately if the common parent is being destroyed; otherwise, for each unique child on the list, <b>XtUnmanageChildren</b> performs the following:
<dl COMPACT><dd><dl COMPACT><dt>-
<dd>Ignores the child if it already is unmanaged or is being destroyed and marks it if not.
<dt>-
<dd>If the child is realized, it makes it nonvisible by unmapping it.</dl></dl><dt>&bull;
<dd>Calls the change_managed routine of the widgets' parent after all children have been marked if the parent is realized.</dl>
 

 <b>XtUnmanageChildren</b> does not destroy the children widgets. Removing widgets from a parent's managed set is often a temporary banishment, and, some time later, you may manage the children again. 

 The <b>XtUnmanageChild</b> function constructs a widget list of length one and calls <b>XtUnmanageChildren</b>. 

 The <b>XtChangeManagedSet</b> function performs the following:
<dl COMPACT><dt>&bull;
<dd>Issues an error if the widgets specified in the <i>manage_children</i> and the <i>unmanage_children</i> lists to no all have the same parent, or if that parent is not a subclass of compositeWidgetClass.
<dt>&bull;
<dd>Returns immediately if the common parent is being destroyed.
<dt>&bull;
<dd>If no <b>CompositeClassExtension</b> is defined, or a <b>CompositeClassExtension</b> is defined but with an <i>allows_change_managed_set</i> field with a value of <b>False</b>, and <b>XtChangeManagedSet</b> was invoked with a non-NULL <i>do_change_proc</i> procedure then <b>XtChangeManagedSet</b> performs the following:
<dl COMPACT><dd><dl COMPACT><dt>-
<dd>Calls <b>XtUnmanageChildren</b> (<i>unmanage_children</i>, <i>num_unmanage_children</i>).
<dt>-
<dd>Calls the <i>do_change_proc</i> specified.
<dt>-
<dd>Calls <b>XtManageChildren</b> (<i>manage_children</i>, <i>num_manage_children</i>) and then returns immediately.</dl></dl><dt>&bull;
<dd>Otherwise, if a <b>CompositeClassExtension</b> is defined with an <i>allows_change_managed_set</i> field with a value of <b>True</b>, or if no <b>CompositeClassExtension</b> is defined, and <b>XtChangeManagedSet </b> was invoked with a NULL <i>do_change_proc</i> procedure, then the following is performed:
<dl COMPACT><dd><dl COMPACT><dt>-
<dd>For each child on the <i>unmanage_children</i> list; if the child is already unmanaged or is being destroyed it is ignored, otherwise it is marked as being unmanaged and if it is realized it is made nonvisible by being unmapped.
<dt>-
<dd>If the <i>do_change_proc</i> procedure is non-NULL then it is invoked as specified.
<dt>-
<dd>For each child on the <i>manage_children</i> list; if the child is already managed or it is being destroyed it is ignored, otherwise it is marked as managed</dl></dl><dt>&bull;
<dd>If the parent is realized and after all children have been marked, the change_managed method of the parent is invoked and subsequently some of the newly managed children are made viewable by:
<dl COMPACT><dd><dl COMPACT><dt>-
<dd>Calling <b>XtRealizeWidget</b> on each of the previously unmanaged child that is unrealized.
<dt>-
<dd>Mapping each previously unmanaged child that has <i>map_when_managed</i> <b>True</b>.</dl></dl>
</dl>
 

 The <b>XtIsManaged</b> function returns <b>True</b> if the specified widget is of class RectObj or any subclass thereof and is managed, or <b>False</b> otherwise.
<h2>See Also</h2><a HREF="/docs/linux/man/3-xtmapwidget/">XtMapWidget</a>(3), <a HREF="/docs/linux/man/3-xtrealizewidget/">XtRealizeWidget</a>(3) 
 <i>X Toolkit Intrinsics - C Language Interface</i> 
 <i>Xlib - C Language X Interface</i>
