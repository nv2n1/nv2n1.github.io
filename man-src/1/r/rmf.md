---
title: "rmf(1)"
name: "rmf"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rmf/"
description: "rmf – remove an nmh folder"
---

<h2 class="name">NAME</h2>
<p> rmf &#8211; remove an nmh folder </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>rmf </code> [<i>+folder</i>] [<code>-interactive</code> | <code>-nointeractive</code>] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>Rmf</code></p>
<dd>removes all of the messages (files) within the specified (or default) folder, and then removes the folder (directory) itself. </p>
<p> If there are any files within the folder which are not a part of <code>nmh</code>, they will <code>not</code> be removed, and an error will be produced. If the folder is given explicitly or the <code>-nointeractive</code> option is given, then the folder will be removed without confirmation. Otherwise, the user will be asked for confirmation. If <code>rmf</code> can&#8217;t find the current folder, for some reason, the folder to be removed defaults to `+inbox&#8217; (unless overridden by user&#8217;s profile entry &#8220;Inbox&#8221;) with confirmation. </p>
<p> If the folder being removed is a subfolder, the parent folder will become the new current folder, and <code>rmf</code> will produce a message telling the user this has happened. This provides an easy mechanism for selecting a set of messages, operating on the list, then removing the list and returning to the current folder from which the list was extracted. </p>
<p> If <code>rmf</code> is used on a read-only folder, it will delete all the private sequences (i.e., &#8220;atr-<i>seq</i>&#8211;<i>folder</i>&#8221; entries) for this folder from your context without affecting the folder itself. </p>
<p> <code>Rmf</code> irreversibly deletes messages that don&#8217;t have other links, so use it with caution.</p>
<h2>FILES</h2>
<pre>
^$HOME/.mh_profile~^The user profile
</pre>
<h2>PROFILE COMPONENTS</h2>
<pre>
^Path:~^To determine the user's nmh directory
^Current-Folder:~^To find the default current folder
^Inbox:~^To find the default inbox
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-rmm/">rmm</a></i>(1), <i><a href="/docs/linux/man/1-folder/">folder</a></i>(1)</p>
<h2>DEFAULTS</h2>
<pre>
`<code>+folder</code>' defaults to the current folder, usually with confirmation
`<code>-interactive</code>' if +folder' not given, `-nointeractive' otherwise
</pre>
<h2>CONTEXT</h2>
<p> <code>Rmf</code> will set the current folder to the parent folder if a subfolder is removed; or if the current folder is removed, it will make &#8220;inbox&#8221; current. Otherwise, it doesn&#8217;t change the current folder or message.</p>
<h2>BUGS</h2>
<p> Although intuitively one would suspect that <code>rmf</code> works recursively, it does not. Hence if you have a sub-folder within a folder, in order to <code>rmf</code> the parent, you must first <code>rmf</code> each of the children. </p>
<h2>Index</h2>
