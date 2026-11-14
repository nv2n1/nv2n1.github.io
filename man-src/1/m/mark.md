---
title: "mark(1)"
name: "mark"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mark/"
description: "mark – manipulate message sequences"
---

<h2 class="name">NAME</h2>
<p> mark &#8211; manipulate message sequences </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mark</code> [<i>+folder</i>] [<i>msgs</i>] [<code>-sequence</code> <i>name</i> &#8230;] [<code>-add</code> | <code>-delete</code>] [<code>-list</code>] [<code>-public</code> | <code>-nopublic</code>] [<code>-zero</code> | <code>-nozero</code>] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>mark</code> command manipulates message sequences by adding or deleting message numbers from folder-specific message sequences, or by listing those sequences and messages. </p>
<p> A message sequence is a keyword, just like one of the &#8220;reserved&#8221; message names, such as &#8220;first&#8221; or &#8220;next&#8221;. Unlike the &#8220;reserved&#8221; message names, which have a fixed semantics on a per-folder basis, the semantics of a message sequence may be defined, modified, and removed by the user. Message sequences are folder-specific, e.g., the sequence name &#8220;seen&#8221; in the context of folder &#8220;<i>+inbox</i>&#8221; need not have any relation whatsoever to the sequence of the same name in a folder of a different name. </p>
<p> Three action switches direct the operation of <code>mark</code>. These switches are mutually exclusive: the last occurrence of any of them overrides any previous occurrence of the other two. </p>
<p> The <code>-add</code> switch tells <code>mark</code> to add messages to sequences or to create a new sequence. For each sequence named via the <code>-sequence</code> <i>name</i> argument (which must occur at least once) the messages named via <i>msgs</i> (which defaults to &#8220;cur&#8221; if no <i>msgs</i> are given), are added to the sequence. The messages to be added need not be absent from the sequence. If the <code>-zero</code> switch is specified, the sequence will be emptied prior to adding the messages. Hence, <code>-add</code> <code>-zero</code> means that each sequence should be initialized to the indicated messages, while <code>-add</code> <code>-nozero</code> means that each sequence should be appended to by the indicated messages. </p>
<p> The <code>-delete</code> switch tells <code>mark</code> to delete messages from sequences, and is the dual of <code>-add</code>. For each of the named sequences, the named messages are removed from the sequence. These messages need not be already present in the sequence. If the <code>-zero</code> switch is specified, then all messages in the folder are added to the sequence (first creating the sequence, if necessary) before removing the messages. Hence, <code>-delete</code> <code>-zero</code> means that each sequence should contain all messages except those indicated, while <code>-delete</code> <code>-nozero</code> means that only the indicated messages should be removed from each sequence. As expected, the command &#8220;<code>mark</code> <code>-sequence</code> <i>foo</i> <code>-delete</code> all&#8221; empties the sequence &#8220;foo&#8221;, and therefore removes that sequence from the current folder&#8217;s list of sequences. </p>
<p> When creating or modifying sequences, you can specify the switches <code>-public</code> or <code>-nopublic</code> to force the new or modified sequences to be &#8220;public&#8221; or &#8220;private&#8221;. The switch <code>-public</code> indicates that the sequences should be made &#8220;public&#8221;. These sequences will then be readable by all <code>nmh</code> users with permission to read the relevant folders. In contrast, the <code>-nopublic</code> switch indicates that the sequences should be made &#8220;private&#8221;, and will only be accessible by you. If neither of these switches is specified, then existing sequences will maintain their current status, and new sequences will default to &#8220;public&#8221; if you have write permission for the relevant folder. Check the <i><a href="/docs/linux/man/5-mh-sequence/">mh-sequence</a></i>(5) man page for more details about the difference between &#8220;public&#8221; and &#8220;private&#8221; sequences. </p>
<p> The <code>-list</code> switch tells <code>mark</code> to list both the sequences defined for the folder and the messages associated with those sequences. <code>Mark</code> will list the name of each sequence given by <code>-sequence</code> <i>name</i> and the messages associated with that sequence. If the sequence is private, this will also be indicated. If no sequence is specified by the <code>-sequence</code> switch, then all sequences for this folder will be listed. The <code>-zero</code> switch does not affect the operation of <code>-list</code>. </p>
<p> The restrictions on sequences are: </p>
<dl>
<dt>&bull;</p>
<dd> The name used to denote a message sequence must consist of an alphabetic character followed by zero or more alphanumeric characters, and cannot be one of the (reserved) message names &#8220;new&#8221;, &#8220;first&#8221;, &#8220;last&#8221;, &#8220;all&#8221;, &#8220;next&#8221;, or &#8220;prev&#8221;.</dl>
<dl>
<dt>&bull;</p>
<dd> Message ranges with user-defined sequence names are restricted to the form &#8220;name:n&#8221;, &#8220;name:+n&#8221;, or &#8220;name:-n&#8221;, and refer to the first or last `n&#8217; messages of the sequence `name&#8217;, respectively. Constructs of the form &#8220;name1-name2&#8221; are forbidden for user defined sequences.</dl>
<h2>FILES</h2>
<dl>
<dt>$HOME/.mh_profile</p>
<dd> The user&#8217;s profile.</dl>
<h2>PROFILE COMPONENTS</h2>
<dl>
<dt>Path:</p>
<dd> To determine the user&#8217;s nmh directory.</p>
<dt>Current-Folder:</p>
<dd> To find the default current folder.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-flist/">flist</a></i>(1), <i><a href="/docs/linux/man/1-pick/">pick</a></i>(1), <i><a href="/docs/linux/man/5-mh-sequence/">mh-sequence</a></i>(5)</p>
<h2>DEFAULTS</h2>
<dl>
<dt>+folder</p>
<dd> The current folder.</p>
<dt>-add</p>
<dd> If <code>-sequence</code> is specified, <code>-list</code> otherwise.</p>
<dt>msgs</p>
<dd> The current message, or <code>all</code> if <code>-list</code> is specified.</p>
<dt>-nozero</p>
<dd></dl>
<h2>CONTEXT</h2>
<p> If a folder is given, it will become the current folder.</p>
<h2>HELPFUL HINTS</h2>
<p> Use <code>flist</code> to find folders with a given sequence, and &#8220;<code>pick</code> <i>sequence</i> <code>-list</code>&#8221; to enumerate those messages in the sequence (such as for use by a shell script). </p>
<h2>Index</h2>
