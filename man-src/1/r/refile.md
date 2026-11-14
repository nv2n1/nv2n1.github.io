---
title: "refile(1)"
name: "refile"
section: "1"
letter: "r"
url: "/docs/linux/man/1-refile/"
description: "refile – file message in other folders"
---

<h2 class="name">NAME</h2>
<p> refile &#8211; file message in other folders </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>refile</code> [<i>msgs</i>] [<code>-draft</code>] [<code>-link</code> | <code>-nolink</code>] [<code>-preserve</code> | <code>-nopreserve</code>] [<code>-retainsequences</code> | <code>-noretainsequences</code>] [<code>-unlink</code> | <code>-nounlink</code>] [<code>-src</code> <i>+folder</i>] [<code>-file</code> <i>file</i>] [<code>-rmmproc</code> <i>program</i>] [<code>-normmproc</code>] <i>+folder1</i> &#8230; [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>Refile</code></p>
<dd>moves (see <i><a href="/docs/linux/man/1-mv/">mv</a></i>(1)) or links (see <i><a href="/docs/linux/man/1-ln/">ln</a></i>(1)) messages from a source folder into one or more destination folders. </p>
<p> If you think of a message as a sheet of paper, this operation is not unlike filing the sheet of paper (or copies) in file cabinet folders. When a message is filed, it is linked into the destination folder(s) if possible, and is copied otherwise. As long as the destination folders are all on the same file system, multiple filing causes little storage overhead. This facility provides a good way to cross-file or multiply-index messages. For example, if a message is received from Jones about the ARPA Map Project, the command </p>
<dl>
<dt>
<dd> refile cur&nbsp;<wbr>+jones&nbsp;<wbr>+Map</dl>
<p> would allow the message to be found in either of the two folders `jones&#8217; or `Map&#8217;. </p>
<p> You may specify the source folder using <code>-src</code> <i>+folder</i>. If this is not given, the current folder is used by default. If no message is specified, then `cur&#8217; is used by default. </p>
<p> The option <code>-file</code> <i>file</i> directs <code>refile</code> to use the specified file as the source message to be filed, rather than a message from a folder. Note that the file should be a validly formatted message, just like any other <code>nmh</code> message. It should <code>NOT</code> be in mail drop format (to convert a file in mail drop format to a folder of <code>nmh</code> messages, see <i><a href="/docs/linux/man/1-inc/">inc</a></i>(1)). </p>
<p> If a destination folder doesn&#8217;t exist, <code>refile</code> will ask if you want to create it. A negative response will abort the file operation. If the standard input for <code>refile</code> is <code>not</code> a tty, then <code>refile</code> will not ask any questions and will proceed as if the user answered &#8220;yes&#8221; to all questions. </p>
<p> The option <code>-link</code> preserves the source folder copy of the message (i.e., it does a <i><a href="/docs/linux/man/1-ln/">ln</a></i>(1) rather than a <i><a href="/docs/linux/man/1-mv/">mv</a></i>(1)), whereas, <code>-nolink</code> (the default) deletes the filed messages from the source folder. </p>
<p> Normally when a message is refiled, for each destination folder it is assigned the number which is one above the current highest message number in that folder. Use of the <code>-preserve</code> switch will override this message renaming, and try to preserve the number of the message. If a conflict for a particular folder occurs when using the <code>-preserve</code> switch, then <code>refile</code> will use the next available message number which is above the message number you wish to preserve. </p>
<p> As message sequences are folder-specific, moving the message from the source folder removes it from all its sequences in that folder. <code>-retainsequences</code> adds it to those same sequences in the destination folder, creating any that don&#8217;t exist. This adding does not apply for the &#8220;cur&#8221; sequence. </p>
<p> If <code>-link</code> is not specified (or <code>-nolink</code> is specified), the filed messages will be removed from the source folder. The default is to remove these messages by renaming them with a site-dependent prefix (usually a comma). Such files will then need to be removed in some manner after a certain amount of time. Many sites arrange for <code>cron</code> to remove these files once a day, so check with your system administrator. </p>
<p> Alternately, if you wish for <code>refile</code> to really remove the files representing these messages from the source folder, you can use the <code>-unlink</code> switch (not to be confused with the <code>-link</code> switch). But messages removed by this method cannot be later recovered. </p>
<p> If you prefer a more sophisticated method of `removing&#8217; the messages from the source folder, you can define the <code>rmmproc</code> profile component. For example, you can add a profile component such as </p>
<dl>
<dt>
<dd> rmmproc:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/home/coleman/bin/rmm_msgs
</dl>
<p> then <code>refile</code> will instead call the named program or script to handle the message files. </p>
<p> The user may specify <code>-rmmproc</code> <i>program</i> on the command line to override this profile specification. The <code>-normmproc</code> option forces the message files to be deleted by renaming or unlinking them as described above. </p>
<p> The <code>-draft</code> switch tells <code>refile</code> to file the &lt;mh-dir&gt;/draft.</p>
<h2>FILES</h2>
<pre>
^$HOME/.mh_profile~^The user profile
</pre>
<h2>PROFILE COMPONENTS</h2>
<pre>
^Path:~^To determine the user's nmh directory
^Current-Folder:~^To find the default current folder
^Folder-Protect:~^To set mode when creating a new folder
^rmmproc:~^Program to delete the message
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-folder/">folder</a></i>(1), <i><a href="/docs/linux/man/5-mh-sequence/">mh-sequence</a></i>(5), <i><a href="/docs/linux/man/1-rmf/">rmf</a></i>(1), <i><a href="/docs/linux/man/1-rmm/">rmm</a></i>(1)</p>
<h2>DEFAULTS</h2>
<pre>
`<code>-src&nbsp;<wbr>+folder</code>' defaults to the current folder
`<code>msgs</code>' defaults to cur
`<code>-nolink</code>'
`<code>-nounlink</code>'
`<code>-nopreserve</code>'
`<code>-noretainsequences</code>'
</pre>
<h2>CONTEXT</h2>
<p> If <code>-src</code> <i>+folder</i> is given, it will become the current folder. If neither <code>-link</code> nor `all&#8217; is specified, the current message in the source folder will be set to the last message specified; otherwise, the current message won&#8217;t be changed. </p>
<p> If the &#8220;Previous-Sequence&#8221; profile entry is set, in addition to defining the named sequences from the source folder, <code>refile</code> will also define those sequences for the destination folders. See <code>mh-sequence (5)</code> for information concerning the previous sequence.</p>
<h2>BUGS</h2>
<p> Since <code>refile</code> and <code>rmm</code> use your <i>rmmproc</i> to delete the message, the <i>rmmproc</i> must <code>NOT</code> call <code>refile</code> or <code>rmm</code> without specifying <code>-normmproc</code>, or you will create an infinite loop. </p>
<h2>Index</h2>
