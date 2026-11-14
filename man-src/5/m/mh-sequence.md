---
title: "mh-sequence(5)"
name: "mh-sequence"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mh-sequence/"
description: "mh-sequence – sequence specification for nmh message system"
---

<p>mh-sequence &#8211; sequence specification for nmh message system</p>
<h2>Description</h2>
<p>A sequence (or sequence set) is a symbolic name representing a message or collection of messages. <code>nmh</code> has several internally defined sequences, as well as allowing users to define their own sequences.</p>
<h3>Message Specification and Pre-Defined Message Sequences</h3>
<p>Most <code>nmh</code> commands accept a `msg&#8217; or `msgs&#8217; specification, where `msg&#8217; indicates one message and `msgs&#8217; indicates one or more messages. To designate a message, you may use either its number (e.g., 1, 10, 234) or one of these &#8220;reserved&#8221; message names: </p>
<dl>
<dd>
<pre><i>Name Description</i>
first the first message in the folder
last the last message in the folder
cur the most recently accessed message
prev the message numerically preceding ``cur''
next the message numerically following ``cur''</pre>
</dl>
<p> In commands that take a `msg&#8217; argument, the default is &#8220;cur&#8221;. As a shorthand, &#8220;.&#8221; is equivalent to &#8220;cur&#8221;. </p>
<p> For example: In a folder containing five messages numbered 5, 10, 94, 177 and 325, &#8220;first&#8221; is 5 and &#8220;last&#8221; is 325. If &#8220;cur&#8221; is 94, then &#8220;prev&#8221; is 10 and &#8220;next&#8221; is 177. </p>
<p> The word `msgs&#8217; indicates that one or more messages may be specified. Such a specification consists of one message designation or of several message designations, as separate arguments. A message designation consists either of a message name as defined above, or a message range. </p>
<p> A message range is specified as &#8220;name1-name2&#8221; or &#8220;name:n&#8221;, where `name&#8217;, `name1&#8242; and `name2&#8242; are message names, and `n&#8217; is an integer. </p>
<p> The specification &#8220;name1-name2&#8221; designates all currently existing messages from `name1&#8242; to `name2&#8242; inclusive. The &#8220;reserved&#8221; message name &#8220;all&#8221; is a shorthand for the message range &#8220;first-last&#8221;. </p>
<p> The specification &#8220;name:n&#8221; designates up to `n&#8217; messages. These messages start with `name&#8217; if `name&#8217; is a message number or one of the reserved names &#8220;first&#8221; &#8220;cur&#8221;, or &#8220;next&#8221;, The messages end with `name&#8217; if `name&#8217; is &#8220;prev&#8221; or &#8220;last&#8221;. The interpretation of `n&#8217; may be overridden by preceding `n&#8217; with a plus or minus sign; `+n&#8217; always means up to `n&#8217; messages starting with `name&#8217;, and `-n&#8217; always means up to `n&#8217; messages ending with `name&#8217;. </p>
<p> Substituting `=&#8217; for `:&#8217; (i.e., &#8220;name=n&#8221;) will reduce the selection from a range of up to `n&#8217; messages, to a selection of just the `n&#8217;th message. So for example, while &#8220;name:-3&#8221; selects the 3 messages ending with `name&#8217;, &#8220;name=-3&#8221; selects just the 2nd previous message. It is an error if the requested message does not exist (i.e., there aren&#8217;t enough messages in the folder). </p>
<p> In commands which accept a `msgs&#8217; argument, the default is either &#8220;cur&#8221; or &#8220;all&#8221;, depending on which makes more sense for each command (see the individual man pages for details). Repeated specifications of the same message have the same effect as a single specification of the message. </p>
<p> There is also a special &#8220;reserved&#8221; message name &#8220;new&#8221; which is used by the <code>mhpath</code> command.</p>
<h3>User-Defined Message Sequences</h3>
<p>In addition to the &#8220;reserved&#8221; (pre-defined) message names given above, <code>nmh</code> supports user-defined sequence names. User-defined sequences allow the <code>nmh</code> user a tremendous amount of power in dealing with groups of messages in the same folder by allowing the user to bind a group of messages to a meaningful symbolic name. </p>
<p> The name used to denote a message sequence must consist of an alphabetic character followed by zero or more alphanumeric characters, and can not be one of the &#8220;reserved&#8221; message names above. After defining a sequence, it can be used wherever an <code>nmh</code> command expects a `msg&#8217; or `msgs&#8217; argument. </p>
<p> Some forms of message ranges are allowed with user-defined sequences. The specification &#8220;name:n&#8221; may be used, and it designates up to the first `n&#8217; messages (or last `n&#8217; messages for `-n&#8217;) which are elements of the user-defined sequence `name&#8217;. </p>
<p> The specifications &#8220;name:next&#8221; and &#8220;name:prev&#8221; may also be used, and they designate the next or previous message (relative to the current message) which is an element of the user-defined sequence `name&#8217;. The specifications &#8220;name:first&#8221; and &#8220;name:last&#8221; are equivalent to &#8220;name:1&#8221; and &#8220;name:-1&#8221;, respectively. The specification &#8220;name:cur&#8221; is not allowed (use just &#8220;cur&#8221; instead). The syntax of these message range specifications is subject to change in the future. </p>
<p> Single messages (as opposed to ranges) may also be selected by substituting `=&#8217; for `:&#8217;, as in &#8220;name=n&#8221;. This will reduce the selection from being a range of up to `n&#8217; messages, to being a selection of just the `n&#8217;th message. So while &#8220;seq:5&#8221; selects the first 5 messages of seqence `seq&#8217;, &#8220;seq=5&#8221; selects just the 5th message of the sequence. It is an error if the requested message does not exist (i.e., there aren&#8217;t at least `n&#8217; messages in the sequence). </p>
<p> User-defined sequence names are specific to each folder. They are defined using the <code>pick</code> and <code>mark</code> commands.</p>
<h3>Public and Private User-Defined Sequences</h3>
<p>There are two varieties of user-defined sequences: public and private. Public sequences of a folder are accessible to any <code>nmh</code> user that can read that folder. They are kept in each folder in the file determined by the &#8220;mh-sequences&#8221; profile entry (default is <i>.mh_sequences</i>). Private sequences are accessible only to the <code>nmh</code> user that defined those sequences and are kept in the user&#8217;s <code>nmh</code> context file. </p>
<p> In general, the commands that create sequences (such as <code>pick</code> and <code>mark</code>) will create public sequences if the folder for which the sequences are being defined is writable by the <code>nmh</code> user. For most commands, this can be overridden by using the switches <code>-public</code> and <code>-private</code>. But if the folder is read-only, or if the &#8220;mh-sequences&#8221; profile entry is defined but empty, then <i>private</i> sequences will be created instead.</p>
<h3>Sequence Negation</h3>
<p><code>Nmh</code> provides the ability to select all messages not elements of a user-defined sequence. To do this, the user should define the entry &#8220;Sequence-Negation&#8221; in the <code>nmh</code> profile file; its value may be any string. This string is then used to preface an existing user-defined sequence name. This specification then refers to those messages not elements of the specified sequence name. For example, if the profile entry is: </p>
<dl>
<dd>Sequence-Negation: not</dl>
<p> then anytime an <code>nmh</code> command is given &#8220;notfoo&#8221; as a `msg&#8217; or `msgs&#8217; argument, it would substitute all messages that are not elements of the sequence &#8220;foo&#8221;. </p>
<p> Obviously, the user should beware of defining sequences with names that begin with the value of the &#8220;Sequence-Negation&#8221; profile entry.</p>
<h3>The Previous Sequence</h3>
<p><code>Nmh</code> provides the ability to remember the `msgs&#8217; or `msg&#8217; argument last given to an <code>nmh</code> command. The entry &#8220;Previous-Sequence&#8221; should be defined in the <code>nmh</code> profile; its value should be a sequence name or multiple sequence names, as separate arguments. If this entry is defined, when when an <code>nmh</code> command finishes, it will define the sequence(s) named in the value of this entry to be those messages that were specified to the command. Hence, a profile entry of </p>
<dl>
<dd>Previous-Sequence: pseq</dl>
<p> directs any <code>nmh</code> command that accepts a `msg&#8217; or `msgs&#8217; argument to define the sequence &#8220;pseq&#8221; as those messages when it finishes. </p>
<p> <code>Note</code>: there can be a performance penalty in using the &#8220;Previous-Sequence&#8221; facility. If it is used, <code>all</code> <code>nmh</code> programs have to write the sequence information to the <i>.mh_sequences</i> file for the folder each time they run. If the &#8220;Previous-Sequence&#8221; profile entry is not included, only <code>pick</code> and <code>mark</code> will write to the <code>.mh_sequences</code> file.</p>
<h3>The Unseen Sequence</h3>
<p>Finally, many users like to indicate which messages have not been previously seen by them. The commands <code>inc</code>, <code>rcvstore</code>, <code>show</code>, <code>mhshow</code>, and <code>flist</code> honor the profile entry &#8220;Unseen-Sequence&#8221; to support this activity. This entry in the <i>.mh_profile</i> should be defined as one or more sequence names, as separate arguments. If there is a value for &#8220;Unseen-Sequence&#8221; in the profile, then whenever new messages are placed in a folder (using <code>inc</code> or <code>rcvstore</code>), the new messages will also be added to all the sequences named in this profile entry. For example, a profile entry of </p>
<dl>
<dd>Unseen-Sequence: unseen</dl>
<p> directs <code>inc</code> to add new messages to the sequence &#8220;unseen&#8221;. Unlike the behavior of the &#8220;Previous-Sequence&#8221; entry in the profile, however, the sequence(s) will <code>not</code> be zeroed by <code>inc</code>. </p>
<p> Similarly, whenever <code>show</code>, <code>mhshow</code>, <code>next</code>, or <code>prev</code> displays a message, that message will be removed from any sequences named by the &#8220;Unseen-Sequence&#8221; entry in the profile.</p>
<h3>Sequence File Format</h3>
<p>The sequence file format is based on the RFC-5322 message format. Each line of the sequence file corresponds to one sequence. The line starts with the sequence name followed by a `:&#8217;, then followed by a space-separated list of message numbers that correspond to messages that are part of the named sequence. A contiguous range of messages can be represented as &#8220;lownum-highnum&#8221;. </p>
<p> <code>Sample sequence file</code> </p>
<dl>
<dd>
<pre>work: 3 6 8 22-33 46
unseen: 47 49-51 54
cur: 46</pre>
</dl>
<p> <code>Nmh</code> commands that modify the sequence file will silently remove sequences for nonexistant messages when the sequence file is updated. The exception to this is the &#8220;cur&#8221; sequence, which is allowed to point to a nonexistant message.</p>
<h3>Sequence File Locking</h3>
<p>The &#8220;datalocking&#8221; profile entry controls the type of locking used when reading and writing sequence files. The locking mechanisms supported are detailed in <i><a href="/docs/linux/man/5-mh-profile/">mh-profile</a></i>(5). This protects sequence file integrity when multiple <code>nmh</code> commands are run simultaneously. <code>Nmh</code> commands that modify the sequence file use transactional locks; the lock is held from the time the sequence file is read until it it written out. This ensures that modifications to the sequence file will not be lost if multiple commands are run simultaneously. Long-running <code>nmh</code> commands, such as <code>inc</code> and <code>pick</code>, will release the sequence lock during the bulk of their runtime and reread the sequence file after their processing is complete to reduce lock contention time. </p>
<p> <code>Note:</code> Currently transactional locks are <code>only</code> supported for public sequences; private sequences will not get corrupted, but the possibility exists that two <code>nmh</code> commands run simultaneously that add messages to a private sequence could result in one command&#8217;s messages not appearing on the requested sequence.</p>
<h2>Files</h2>
<pre>^$HOME/.mh_profile~^The user profile
^&lt;mh-dir&gt;/context~^The user context
^&lt;folder&gt;/.mh_sequences~^File for public sequences</pre>
<h2>Profile Components</h2>
<pre>^mh-sequences:~^Name of file to store public sequences
^Sequence-Negation:~^To designate messages not in a sequence
^Previous-Sequence:~^The last message specification given
^Unseen-Sequence:~^Those messages not yet seen by the user</pre>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-flist/">flist</a></i>(1), <i><a href="/docs/linux/man/1-mark/">mark</a></i>(1), <i><a href="/docs/linux/man/1-pick/">pick</a></i>(1), <i><a href="/docs/linux/man/5-mh-profile/">mh-profile</a></i>(5)</p>
<h2>Defaults</h2>
<p>None</p>
