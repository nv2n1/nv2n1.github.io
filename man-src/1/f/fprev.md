---
title: "fprev(1)"
name: "fprev"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fprev/"
description: "new – report on folders with new messages"
---

<h2 class="name">NAME</h2>
<p> new &#8211; report on folders with new messages </p>
<p> fnext &#8211; set current folder to next folder with new messages </p>
<p> fprev &#8211; set current folder to previous folder with new messages </p>
<p> unseen &#8211; scan new messages in all folders with new messages </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>new</code> [<i>sequences</i>] [<code>-mode</code> <i>mode</i>] [<code>-folders</code> <i>foldersfile</i>] [<code>-version</code>] [<code>-help</code>]</dl>
<dl>
<dt> <code>fnext</code></p>
<dd>is equivalent to <code>new -mode fnext</code></dl>
<dl>
<dt> <code>fprev</code></p>
<dd>is equivalent to <code>new -mode fprev</code></dl>
<dl>
<dt> <code>unseen</code></p>
<dd>is equivalent to <code>new -mode unseen</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>New</code> in its default mode produces a one-line-per-folder listing of all folders containing messages in the listed <i>sequences</i> or in the sequences listed in the profile entry &#8220;<i>Unseen-Sequence</i>&#8221;. Each line contains the folder, the number of messages in the desired sequences, and the message lists from the .mh_sequences file. For example: </p>
<dl>
<dt>
<dd>
<pre>
foo     11.* 40-50
bar    380.  760-772 824-828
 total    391.
</pre>
</dl>
<p> The `*&#8217; on foo indicates that it is the current folder. The last line shows the total number of messages in the desired sequences. </p>
<p> <code>New</code> crawls the folder hierarchy recursively to find all folders, and prints them in lexicographic order. Override this behavior by providing <i>foldersfile</i> containing the pre-sorted list of folders <code>new</code> should check, one per line. </p>
<p> In <code>fnext</code> and <code>fprev</code> modes, <code>new</code> instead changes to the next or previous matching folder, respectively. </p>
<p> In <code>unseen</code> mode, <code>new</code> executes <code>scan sequences</code> for each matching folder.</p>
<h2>FILES</h2>
<pre>
^$HOME/.mh_profile~^The user profile
</pre>
<h2>PROFILE COMPONENTS</h2>
<pre>
^Path:~^To determine the user's nmh directory
^Current-Folder:~^To find the default current folder
^Unseen-Sequence:~^The name of the unseen message sequence
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-scan/">scan</a></i>(1), <i><a href="/docs/linux/man/5-mh-format/">mh-format</a></i>(5) </p>
<h2>Index</h2>
