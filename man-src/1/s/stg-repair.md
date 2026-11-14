---
title: "stg-repair(1)"
name: "stg-repair"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-repair/"
description: "stg-repair – Fix StGit metadata if branch was modified with git commands"
---

<h2 class="name">NAME</h2>
<p> stg-repair &#8211; Fix StGit metadata if branch was modified with git commands </p>
<h2>SYNOPSIS</h2>
<pre>
<i>stg</i> repair
</pre>
<h2>DESCRIPTION</h2>
<p> If you modify an StGit stack (branch) with some git commands &#8212; such as commit, pull, merge, and rebase &#8212; you will leave the StGit metadata in an inconsistent state. In that situation, you have two options: </p>
<dl>
<dt>
<dd> 1. Use &quot;stg undo&quot; to undo the effect of the git commands. (If you know what you are doing and want more control, &quot;git reset&quot; or similar will work too.)</dl>
<dl>
<dt>
<dd> 2. Use &quot;stg repair&quot;. This will fix up the StGit metadata to accommodate the modifications to the branch. Specifically, it will do the following: </p>
<dl>
<dt>
<dd> &bull; If you have made regular git commits on top of your stack of StGit patches, &quot;stg repair&quot; makes new StGit patches out of them, preserving their contents.</dl>
<dl>
<dt>
<dd> &bull; However, merge commits cannot become patches; if you have committed a merge on top of your stack, &quot;repair&quot; will simply mark all patches below the merge unapplied, since they are no longer reachable. If this is not what you want, use &quot;stg undo&quot; to get rid of the merge and run &quot;stg repair&quot; again.</dl>
<dl>
<dt>
<dd> &bull; The applied patches are supposed to be precisely those that are reachable from the branch head. If you have used e.g. &quot;git reset&quot; to move the head, some applied patches may no longer be reachable, and some unapplied patches may have become reachable. &quot;stg repair&quot; will correct the appliedness of such patches. </p>
<dl>
<dt>
<dd>
<pre>
&quot;stg repair&quot; will fix these inconsistencies reliably, so as long
as you like what it does, you have no reason to avoid causing
them in the first place. For example, you might find it
convenient to make commits with a graphical tool and then have
&quot;stg repair&quot; make proper patches of the commits.
</pre>
</dl>
</dl>
</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 If using git commands on the stack was a mistake, running &quot;stg repair&quot; is <i>not</i> what you want. In that case, what you want is option (1) above. </p>
</dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
<h2>Index</h2>
