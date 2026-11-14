---
title: "mh-folders(5)"
name: "mh-folders"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mh-folders/"
description: "mh-folders – specification of storage format used by nmh message system"
---

<p>mh-folders &#8211; specification of storage format used by nmh message system</p>
<h2>Description</h2>
<p><code>nmh</code> stores messages in the files and directories of the host filesystem according to the following rules: </p>
<p> <code>one folder per directory</code></p>
<dl>
<dd>A <code>nmh</code> folder corresponds to directory. There are no limits on folder names beyond those of the host filesystem.</dl>
<p> <code>one message per file</code></p>
<dl>
<dd>The file name is a positive integer. Other files containing metadata or arbitrary names can exist in a folder; while the preference is that non-message files begin with &#8220;.&#8221;, all files that are not positive integers <code>must</code> be ignored by a <code>MH</code>-compatible implementation. However, implementations are free to indicate to the user the existence of non-message files that are not prefixed with a &#8220;.&#8221;. </p>
<p> The filename for a new message is one greater than the highest numbered message in the folder; its full path can be accessed by the pseudo-sequence <i>new</i> (e.g., <code>mhpath</code> <i>new</i>). New messages are <code>only</code> permitted to be added to a folder at the end of the message number range. </p>
<p> To add a new message to a folder, the recommended sequence is: </p>
<dl>
<dt>&bull;</p>
<dd>Create a temporary file in the desired folder.</p>
<dt>&bull;</p>
<dd>Attempt to link the temporary file to the new message number.</p>
<dt>&bull;</p>
<dd>If successful, remove the temporary file. If the link fails, increment the message number and try again.</dl>
</dl>
<p> <code>context</code></p>
<dl>
<dd>There is one context file. Its default location is in the user&#8217;s Path and default name is <i>context</i>, but those can be overridden with the $MHCONTEXT environment variable. <code>context</code> has the following format: </p>
<dl>
<dd><code>Current-Folder: +</code><i>folder</i></dl>
<dl>
<dd><code>atr-</code><i>sequence-path</i><code>: </code><i>m[-n] [&#8230;]</i></dl>
<p> where <i>folder</i> is the directory name of the current folder. Lines beginning with &#8220;atr&#8221; are used for private sequences. <i>sequence</i> is the name of the private sequence, <i>path</i> is the full path to the folder with the private sequence, and <i>m[-n]</i> is a message number or range of message numbers in the sequence.</dl>
<p> <code>sequences</code></p>
<dl>
<dd>There is one sequences file in each <code>nmh</code> folder. Its default name is <i>.mh_sequences</i>, but that can be overridden with the &#8220;mh-sequences&#8221; profile entry. <code>sequences</code> has the following format: </p>
<dl>
<dd><code>sequence: </code><i>m[-n] [&#8230;]</i></dl>
<p> showing the (possibly empty) message numbers and/or ranges of message numbers in each sequence. The <code>cur</code> sequence has at most just a single message number, not a range. </p>
<p> Sequence names have a maximum size of 998 characters. Each line is also limited to a maximum of 998 characters, but RFC 822 continuation rules apply; sequences can be continued across multiple lines by prefixing continuation lines with a whitespace character. </p>
<p> If an implementation finds messages in a sequence that do not exist, the sequence file should be updated to remove the missing messages from the sequence. If a sequence contains no messages, it should be removed from the sequence file. The exception to this is the <code>cur</code> sequence, which can refer to a nonexistant message.</dl>
<h3>Locking</h3>
<p><code>nmh</code> programs read and write the context and sequences files, and lock these files when accessing them. There should not be a need to access these files directly; instead, programs such as <code>flist</code>, <code>folder</code>, <code>mark</code>, <code>pick</code>, and <code>rcvstore</code> should be used to query and update their contents. Any program outside of <code>nmh</code> that accesses these files must be sure to lock them using the same locking method as <code>nmh</code>. The default data locking method is selected when <code>nmh</code> is configured and can be accessed as a string using <code>mhparam datalocking</code>. By default, fcntl locking is used, but this may be overridden with the <code>datalocking</code> profile entry. </p>
<p> A second, possibly different, locking method is used by <code><a href="/docs/linux/man/1-inc/">inc</a></code>(1) when accessing the user&#8217;s mail spool file or by <code>nmh</code> programs that open any mbox file. This locking method is selected when <code>nmh</code> is configured and can be accessed as a string using <code>mhparam spoollocking</code>. By default, kernel-level locking is used if appropriate for the platform, and it is for popular platforms. That default should also be the same as used by the <code>mail</code> program, if provided on the platform.</p>
<h2>Files</h2>
<pre>^&lt;mh-dir&gt;/context~^The user context
^or $MHCONTEXT~^Rather than the standard context
^&lt;folder&gt;/.mh_sequences~^Public sequences for &lt;folder&gt;</pre>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-flist/">flist</a></i>(1), <i><a href="/docs/linux/man/1-folder/">folder</a></i>(1), <i><a href="/docs/linux/man/1-mail/">mail</a></i>(1), <i><a href="/docs/linux/man/1-mark/">mark</a></i>(1), <i><a href="/docs/linux/man/1-mh-param/">mh-param</a></i>(1), <i><a href="/docs/linux/man/1-mh-path/">mh-path</a></i>(1), <i><a href="/docs/linux/man/5-mh-profile/">mh-profile</a></i>(5), <i><a href="/docs/linux/man/5-mh-sequence/">mh-sequence</a></i>(5), <i><a href="/docs/linux/man/1-pick/">pick</a></i>(1), <i><a href="/docs/linux/man/1-rcvstore/">rcvstore</a></i>(1) </p>
