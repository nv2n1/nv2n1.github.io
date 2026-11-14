---
title: "viewres(1)"
name: "viewres"
section: "1"
letter: "v"
url: "/docs/linux/man/1-viewres/"
description: "viewres – graphical class browser for Xt"
---

<h2 class="name">NAME</h2>
<p> viewres &#8211; graphical class browser for Xt </p>
<h2>SYNOPSIS</h2>
<p> <code>viewres</code> [-option &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The <i>viewres</i> program displays a tree showing the widget class hierarchy of the Athena Widget Set. Each node in the tree can be expanded to show the resources that the corresponding class adds (i.e. does not inherit from its parent) when a widget is created. This application allows the user to visually examine the structure and inherited resources for the Athena Widget Set.</p>
<h2>OPTIONS</h2>
<p> <i>Viewres</i> accepts all of the standard toolkit command line options as well as the following:</p>
<dl>
<dt><code>-top </code><i>name</i></p>
<dd> This option specifies the name of the highest widget in the hierarchy to display. This is typically used to limit the display to a subset of the tree. The default is <i>Object</i>.</p>
<dt><code>-variable</code></p>
<dd> This option indicates that the widget variable names (as declared in header files) should be displayed in the nodes rather than the widget class name. This is sometimes useful to distinguish widget classes that share the same name (such as <i>Text</i>).</p>
<dt><code>-vertical</code></p>
<dd> This option indicates that the tree should be displayed top to bottom rather left to right.</dl>
<h2>VIEW MENU</h2>
<p> The way in which the tree is displayed may be changed through the entries in the <code>View</code> menu:</p>
<dl>
<dt><code>Show Variable Names</code></p>
<dd> This entry causes the node labels to be set to the variable names used to declare the corresponding widget class. This operation may also be performed with the <code>SetLabelType(variable)</code> translation.</p>
<dt><code>Show Class Names</code></p>
<dd> This entry causes the node labels to be set to the class names used when specifying resources. This operation may also be performed with the <code>SetLabelType(class)</code> translation.</p>
<dt><code>Layout Horizontal</code></p>
<dd> This entry causes the tree to be laid out from left to right. This operation may also be performed with the <i>SetOrientation(West)</i> translation.</p>
<dt><code>Layout Vertical</code></p>
<dd> This entry causes the tree to be laid out from top to bottom. This operation may also be performed with the <i>SetOrientation(North)</i> translation.</p>
<dt><code>Show Resource Boxes</code></p>
<dd> This entry expands the selected nodes (see next section) to show the new widget and constraint resources. This operation may also be performed with the <i>Resources(on)</i> translation.</p>
<dt><code>Hide Resource Boxes</code></p>
<dd> This entry removes the resource displays from the selected nodes (usually to conserve space). This operation may also be performed with the <i>Resources(off)</i> translation.</dl>
<h2>SELECT MENU</h2>
<p> Resources for a single widget class can be displayed by clicking <code>Button2</code> on the corresponding node, or by adding the node to the selection list with <code>Button1</code> and using the <code>Show Resource Boxes</code> entry in the <code>View</code> menu. Since <code>Button1</code> actually toggles the selection state of a node, clicking on a selected node will cause it to be removed from the selected list. </p>
<p> Collections of nodes may also be selected through the various entries in the <code>Select</code> menu:</p>
<dl>
<dt><code>Unselect All</code></p>
<dd> This entry removes all nodes from the selection list. This operation may also be performed with the <i>Select(nothing)</i> translation.</p>
<dt><code>Select All</code></p>
<dd> This entry adds all nodes to the selection list. This operation may also be performed with the <i>Select(all)</i> translation.</p>
<dt><code>Invert All</code></p>
<dd> This entry adds unselected nodes to, and removes selected nodes from, the selection list. This operation may also be performed with the <i>Select(invert)</i> translation.</p>
<dt><code>Select Parent</code></p>
<dd> This entry selects the immediate parents of all selected nodes. This operation may also be performed with the <i>Select(parent)</i> translation.</p>
<dt><code>Select Ancestors</code></p>
<dd> This entry recursively selects all parents of all selected nodes. This operation may also be performed with the <i>Select(ancestors)</i> translation.</p>
<dt><code>Select Children</code></p>
<dd> This entry selects the immediate children of all selected nodes. This operation may also be performed with the <i>Select(children)</i> translation.</p>
<dt><code>Select Descendants</code></p>
<dd> This entry recursively selects all children of all selected nodes. This operation may also be performed with the <i>Select(descendants)</i> translation.</p>
<dt><code>Select Has Resources</code></p>
<dd> This entry selects all nodes that add new resources (regular or constraint) to their corresponding widget classes. This operation may also be performed with the <i>Select(resources)</i> translation.</p>
<dt><code>Select Shown Resource Boxes</code></p>
<dd> This entry selects all nodes whose resource boxes are currently expanded (usually so that they can be closed with <code>Hide Resource Boxes</code>). This operation may also be performed with the <i>Select(shown)</i> translation.</dl>
<h2>ACTIONS</h2>
<p> The following application actions are provided:</p>
<dl>
<dt><code>Quit()</code></p>
<dd>
 This action causes <i>viewres</i> to exit.</p>
<dt><code>SetLabelType(</code><i>type</i>)</p>
<dd> This action sets the node labels to display the widget <i>variable</i> or <i>class</i> names, according to the argument <i>type</i>.</p>
<dt><code>SetOrientation(</code><i>direction</i>)</p>
<dd> This action sets the root of the tree to be one of the following areas of the window: <i>West</i>, <i>North</i>, <i>East</i>, or <i>South</i>.</p>
<dt><code>Select(</code><i>what</i>)</p>
<dd> This action selects the indicated nodes, as described in the <code>VIEW MENU</code> section: <i>nothing</i> (unselects all nodes), <i>invert</i>, <i>parent</i>, <i>ancestors</i>, <i>children</i>, <i>descendants</i>, <i>resources</i>, <i>shown</i>.</p>
<dt><code>Resources(</code><i>op</i>)</p>
<dd> This action turns <i>on</i>, <i>off</i>, or <i>toggles</i> the resource boxes for the selected nodes. If invoked from within one of the nodes (through the keyboard or pointer), only that node is used.</dl>
<h2>WIDGET HIERARCHY</h2>
<p> Resources may be specified for the following widgets: </p>
<pre>
Viewres viewres
        Paned pane
                Box buttonbox
                        Command quit
                        MenuButton view
                                SimpleMenu viewMenu
                                        SmeBSB layoutHorizontal
                                        SmeBSB layoutVertical
                                        SmeLine line1
                                        SmeBSB namesVariable
                                        SmeBSB namesClass
                                        SmeLine line2
                                        SmeBSB viewResources
                                        SmeBSB viewNoResources
                        MenuButton select
                                SimpleMenu selectMenu
                                        SmeBSB unselect
                                        SmeBSB selectAll
                                        SmeBSB selectInvert
                                        SmeLine line1
                                        SmeBSB selectParent
                                        SmeBSB selectAncestors
                                        SmeBSB selectChildren
                                        SmeBSB selectDescendants
                                        SmeLine line2
                                        SmeBSB selectHasResources
                                        SmeBSB selectShownResources
                Form treeform
                        Porthole porthole
                                Tree tree
                                        Box <i>variable-name</i>
                                                Toggle <i>variable-name</i>
                                                List <i>variable-name</i>
                        Panner panner
</pre>
<p> where <i>variable-name</i> is the widget variable name of each node.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xrdb/">xrdb</a>(1), <a href="/docs/linux/man/1-listres/">listres</a>(1), <a href="/docs/linux/man/1-editres/">editres</a>(1), <a href="/docs/linux/man/1-appres/">appres</a>(1), appropriate widget documents</p>
<h2>COPYRIGHT</h2>
<p> Copyright 1994 X Consortium<br />
 See <i><a href="/docs/linux/man/7-x/">X</a>(7)</i> for a full statement of rights and permissions.</p>
<h2>AUTHOR</h2>
<p> Jim Fulton, MIT X Consortium </p>
<h2>Index</h2>
