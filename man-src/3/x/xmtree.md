---
title: "xmtree(3)"
name: "xmtree"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtree/"
---

XmTree - The Tree widget class
<h2>Synopsis</h2>#include &lt;Xm/XTree.h&gt;
<h2>Description</h2><table> <tr VALIGN=top></tr><tr VALIGN=top><td><font SIZE="+9">&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></font></td></tr> </table> 

 The Tree widget is a container that shows the relationship of its children in a graphical tree-like format. Each child of the Tree widget is a node in the Tree. The parent-child relationships between these nodes are completely distinct from the widget hierarch.. The hierarchy of nodes is created by specifying the tree &quot;parent&quot; of each node as a constraint resource. If a node's parent is NULL then it is assumed to be a root of the tree. Although each widget can only have one parent, the Tree widget supports adding more than one &quot;root&quot; node to a single Tree. 

 Note: the Tree widget assumes that is will be totally responsible for mapping and unmapping its children. Therefore no child of this widget should ever modify its mappedWhenManaged resource. If a child does modify this resource the behavior is undefined. 

<h2>User Interaction</h2>Each node in the tree can be in four states: open, closed, always open, and hidden. The state of a node changes how it appears to the user and what actions are available to the user.
<dl COMPACT><dd>Open<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>This node will have an open folder shown to its left that 
 may be selected by the user to close this node. When a node is open all of its children will be visible to the user. 

<dd>Closed<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>This node will have a closed folder shown to its left that 
 may be selected by the user to open this node. When a node is closed none of its children will be visible to the user. 

<dd>Always Open<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>This node will have no folder button associated with it. 
 All of its children will be visible to the user. 

<dd>Hidden<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>This node will not be shown to the user and all of its 
 children will appear and act exactly as if they were children of this node's parent. It will appear to the user as if this node does not exist.</dl>
 

 To maintain consistency of the user interface we have found that it is bestto use the node state &quot;Always Open&quot; for nodes with no children. This way the user will only see a folder button next to a node that has children to display. A folder button associated with a node that has no children has no defined semantics. 

<h2>Normal Resources</h2><table> <tr VALIGN=top><td>Name</td><td>Class</td><td>Type</td><td>Initial Value
</td></tr><tr VALIGN=top><td>connectStyle</td><td>ConnectStyle</td><td>unsigned char</td><td>XmTreeDirect
</td></tr><tr VALIGN=top><td>horizontalNodeSpace</td><td>Dimension</td><td>HorizontalDimension</td><td>20
</td></tr><tr VALIGN=top><td>verticalNodeSpace</td><td>Dimension</td><td>VerticalDimension</td><td>2
</td></tr> </table> 

 All resource names begin with XmN and all resource class names begin with XmC. 

<h2>connectStyle</h2>The style of the lines visually connecting parent nodes to children nodes. The valid styles are XmTreeDirect or XmTreeLadder.
<h2>horizontalNodeSpace</h2><h2>verticalNodeSpace</h2>The amount of space between each node in the tree and it nearest neighbor. 

 The following resources are inherited from the XmHierarchy widget: 

 <table> <tr VALIGN=top><td>Name</td><td>Class</td><td>Type</td><td>Initial Value
</td></tr><tr VALIGN=top><td>autoClose</td><td>AutoClose</td><td>Boolean</td><td>True
</td></tr><tr VALIGN=top><td>closeFolderPixmap</td><td>Pixmap</td><td>Pixmap</td><td>XmUNSPECIFIED_PIXMAP
</td></tr><tr VALIGN=top><td>horizontalMargin</td><td>Dimension</td><td>HorizontalDimension</td><td>2
</td></tr><tr VALIGN=top><td>openFolderPixmap</td><td>Pixmap</td><td>Pixmap</td><td>XmUNSPECIFIED_PIXMAP
</td></tr><tr VALIGN=top><td>refigureMode</td><td>Boolean</td><td>Boolean</td><td>True
</td></tr><tr VALIGN=top><td>verticalMargin</td><td>Dimension</td><td>VerticalDimension</td><td>2
</td></tr> </table> 

 All resource names begin with XmN and all resource class names begin with XmC. 

<h2>Constraint Resources</h2><table> <tr VALIGN=top><td>Name</td><td>Class</td><td>Type</td><td>Initial Value
</td></tr><tr VALIGN=top><td>openClosePadding</td><td>OpenClosePadding</td><td>Int</td><td>0
</td></tr><tr VALIGN=top><td>lineColor</td><td>Foreground</td><td>Pixel</td><td>&lt;dynamic&gt;
</td></tr><tr VALIGN=top><td>lineWidth</td><td>LineWidth</td><td>Dimension</td><td>0
</td></tr> </table> 

 All resource names begin with XmN and all resource class names begin with XmC. openClosePadding 

 The number of pixels between the folder button and the node it is associated with. 

<h2>lineColor</h2>The color of the line connecting a node to its parent. The default value for this resource is the foreground color of the Tree widget. 

<h2>lineWidth</h2>The width of a connection line between a node and its parent 

 The following constraint resources are inherited from the XmHierarchy widget: 

 <table> <tr VALIGN=top><td>Name</td><td>Class</td><td>Type</td><td>Initial Value
</td></tr><tr VALIGN=top><td>insertBefore</td><td>InsertBefore</td><td>Widget</td><td>NULL
</td></tr><tr VALIGN=top><td>nodeState</td><td>NodeState</td><td>XmHierarchyNodeState</td><td>Open
</td></tr><tr VALIGN=top><td>parentNode</td><td>ParentNode</td><td>Widget</td><td>NULL
</td></tr> </table> 

 All resource names begin with XmN and all resource class names begin with XmC. Geometry Management: 

 The layout is performed by assigning each node a box that is just large enough to con- tain itself and all of its children. A recursive layout is then performed that centers each node vertically in its box and at the extreme left horizontally. The children's boxes are then placed to the right of the node separated by the horizontalNodeSpace from their parent, stacked above each other and separated by verticalNodeSpace. This process is repeated recursively for each child in the tree. 

 The preferred size of the entire tree will be just large enough to contain all nodes in the hierarchy. As the state of nodes change the tree will attempt to resize itself to con- tain its current configuration. If the tree is forced larger than the desired size the nodes will be centered vertically and flush to the left edge of the tree widget. If the tree is forced smaller, some nodes may be moved or drawn outside the end of the tree. For this reason it is usually desirable to put the tree into a Scrolled Window widget. 

<h2>See Also</h2><a HREF="//www.systutorials.com/docs/linux/man/3X-XmColumn/">XmColumn</a>(3X) 

<h2>Copyright</h2>Copyright (c) 1992 by Integrated Computer Solutions, Inc.
