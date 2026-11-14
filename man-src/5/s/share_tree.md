---
title: "share_tree(5)"
name: "share_tree"
section: "5"
letter: "s"
url: "/docs/linux/man/5-share_tree/"
description: "share_tree – xxQS_NAMExx share tree file format"
---

<p>share_tree &#8211; xxQS_NAMExx share tree file format</p>
<h2>Description</h2>
<p>The share tree defines the long-term resource entitlements of users/projects and of a hierarchy of arbitrary groups thereof. Note that it is normally necessary to maintain users explicitly to use a share tree, rather than use automatic creation and (specifically) destruction, or at least set <code>auto_user_delete_time</code> to 0; see </p>
<p> The current share tree can be displayed via the <code>-sstree</code> or <code>-sst</code> options. The output follows the <i>share_tree</i> format description. A share tree can be created and an existing one can be modified via the <code>-astree</code> and <code>-mstree</code> options to The <code>-sst</code> option shows a formatted share tree (tree view). Individual share tree nodes can be created, modified, deleted, or shown via the <code>-astnode</code>, <code>-dstnode</code>, <code>-mstnode</code>, and <code>-sstnode</code> options to </p>
<p> Note, xxQS_NAMExx allows backslashes (\) be used to escape newline characters. The backslash and the newline are replaced with a space character before any interpretation.</p>
<h2>Format</h2>
<p>The format of a share tree file is defined as follows:</p>
<dl>
<dt>&bull;</p>
<dd>A new node starts with the attribute <code>id</code>, an equal sign and the numeric identification number of the node. Further attributes of that node follow until another <code>id</code> keyword is encountered.</p>
<dt>&bull;</p>
<dd>The attribute <code>type</code> defines whether a sharetree node references a user (type=0), or a project (type=1).</p>
<dt>&bull;</p>
<dd>The attribute <code>childnodes</code> contains a comma-separated list of child nodes to this node.</p>
<dt>&bull;</p>
<dd>The parameter <code>name</code> refers to an arbitrary name for the node, or to a corresponding user (see or project (see if the node is a leaf node of the share tree. The name of the root node of the tree is &quot;Root&quot; by convention.</p>
<dt>&bull;</p>
<dd>The parameter <code>shares</code> defines the share of the node among the nodes with the same parent node.</p>
<dt>&bull;</p>
<dd>A user leaf node named &#8216;default&#8217; can be defined as a descendant of a node in the share tree. The default node defines the number of shares for users who are running in the project, but who do not have a user node defined under the project. The default user node is a convenient way of specifying a single node for all users which should receive an equal share of the project resources. The default node may be specified by itself or with other nodes at the same level below a project. All users, whether explicitly specified as a user node or those which map to the &#8216;default&#8217; user node, must have a corresponding object defined in order to get shares. Do not configure a object named &#8216;default&#8217;. </p>
</dl>
<h2>Examples</h2>
<p>Jobs of projects P1 and P2 get 50 shares, all other jobs get 10 shares. </p>
<pre>id=0
name=Root
type=0
shares=1
childnodes=1,2,3
id=1
name=P1
type=1
shares=50
childnodes=NONE
id=2
name=P2
type=1
shares=50
childnodes=NONE
id=3
name=default
type=0
shares=10
childnodes=NONE</pre>
<h2>See Also</h2>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
