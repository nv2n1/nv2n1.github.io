---

title: "whatnow(1)"
name: "whatnow"
section: "1"
letter: "w"
url: "/docs/linux/man/1-whatnow/"
description: "whatnow – prompting front-end for sending messages"
---

<dl>
<dt> <code>whatnow</code> [<code>-draftfolder</code> <i>+folder</i>] [<code>-draftmessage</code> <i>msg</i>] [<code>-nodraftfolder</code>] [<code>-editor</code> <i>editor</i>] [<code>-noedit</code>] [<code>-prompt</code> <i>string</i>] [<i>file</i>] [<code>-version</code>] [<code>-help</code>]</dt></dl>
<p> <code>Whatnow</code></p>
<dd>is the default program that queries the user about the disposition of a composed draft. It is normally automatically invoked by one of the <code>nmh</code> commands <code>comp</code>, <code>dist</code>, <code>forw</code>, or <code>repl</code> after the initial edit. </dd>
<p> When started, the editor is started on the draft (unless <code>-noedit</code> is given, in which case the initial edit is suppressed). Then, <code>whatnow</code> repetitively prompts the user with &#8220;What now?&#8221; and awaits a response. The valid responses are: </p>
<dl>
<dl>
<dt><code>edit</code></dt>
<dd> re-edit using the same editor that was used on the preceding round unless a profile entry &#8220;&lt;lasteditor&gt;-next: &lt;editor&gt;&#8221; names an alternate editor</dd>
<dt><code>edit &lt;editor&gt;</code></dt>
<dd> invoke &lt;editor&gt; for further editing</dd>
<dt><code>refile +folder</code></dt>
<dd> refile the draft into the given folder</dd>
<dt><code>mime</code></dt>
<dd> process the draft as MIME composition file using the <i>buildmimeproc</i> command (<code>mhbuild</code> by default)</dd>
<dt><code>display</code></dt>
<dd> list the message being distributed/replied-to on the terminal</dd>
<dt><code>list</code></dt>
<dd> list the draft on the terminal</dd>
<dt><code>send</code></dt>
<dd> send the message</dd>
<dt><code>send -watch</code></dt>
<dd> send the message and monitor the delivery process</dd>
<dt><code>push</code></dt>
<dd> send the message in the background</dd>
<dt><code>whom</code></dt>
<dd> list the addresses that the message will go to</dd>
<dt><code>whom -check</code></dt>
<dd> list the addresses and verify that they are acceptable to the transport service</dd>
<dt><code>quit</code></dt>
<dd> preserve the draft and exit</dd>
<dt><code>quit -delete</code></dt>
<dd> delete the draft and exit</dd>
<dt><code>delete</code></dt>
<dd> delete the draft and exit</dd>
<dt><code>cd directory</code></dt>
<dd> use the directory when interpreting attachment file names</dd>
<dt><code>pwd</code></dt>
<dd> print the working directory for attachment files</dd>
<dt><code>ls [ls-options]</code></dt>
<dd> list files in the attachment working directory using the ls command</dd>
<dt><code>attach [-v] files</code></dt>
<dd> add the named files to the message as MIME attachments; -v displays the mhbuild directive that <i><a href="/docs/linux/man/1-send/">send</a></i>(1) will use</dd>
<dt><code>alist [-ln]</code></dt>
<dd> list the MIME attachments, either short, long [-l] or numbered [-n]</dd>
<dt><code>detach [-n] files-or-numbers</code></dt>
<dd> remove MIME attachments, either by file name or by number with -n</dd></dl>
</dl>
<p> When entering your response, you need only type enough characters to uniquely identify the response. </p>
<p> For the <code>edit</code> response, any valid switch to the editor is valid. </p>
<p> For the <code>send</code> and <code>push</code> responses, any valid switch to <i><a href="/docs/linux/man/1-send/">send</a></i>(1) is valid (as <code>push</code> merely invokes <code>send</code> with the <code>-push</code> option). </p>
<p> For the <code>whom</code> response, any valid switch to <i><a href="/docs/linux/man/1-whom/">whom</a></i>(1) is valid. </p>
<p> For the <code>refile</code> response, any valid switch to the <i>fileproc</i> is valid. </p>
<p> For the <code>display</code> and <code>list</code> responses, any valid argument to the <i>lproc</i> is valid. If any non-switch arguments are present, then the pathname of the draft will be excluded from the argument list given to the <i>lproc</i> (this is useful for listing another <code>nmh</code> message). </p>
<p> See <i><a href="/docs/linux/man/5-mh-profile/">mh-profile</a></i>(5) for further information about how editors are used by <code>nmh</code>. It also discusses how environment variables can be used to direct <code>whatnow</code>&#8216;s actions in complex ways. </p>
<p> The <code>-prompt</code> <i>string</i> switch sets the prompting string for <code>whatnow</code>. </p>
<p> The <code>-draftfolder</code> <i>+folder</i> and <code>-draftmessage</code> <i>msg</i> switches invoke the <code>nmh</code> draft folder facility. This is an advanced (and highly useful) feature. Consult the <i><a href="/docs/linux/man/5-mh-draft/">mh-draft</a></i>(5) man page for more information. </p>
<p> If your <code>nmh</code> was configured with readline enabled, you&#8217;ll be able to use filename completion and other readline features at the prompt. These are particularly useful with the <code>cd</code>, <code>ls</code>, <code>attach</code>, and <code>detach</code> commands for managing MIME attachments.</p>
<h2>FILES</h2>
<pre>
^$HOME/.mh_profile~^The user profile
^&lt;mh-dir&gt;/draft~^The draft file
</pre>
<h2>PROFILE COMPONENTS</h2>
<pre>
^Path:~^To determine the user's nmh directory
^Draft-Folder:~^To find the default draft-folder
^Editor:~^To override the default editor
^&lt;lasteditor&gt;-next:~^To name an editor to be used after exit
^~^from &lt;lasteditor&gt;
^buildmimeproc:~^Program to translate MIME composition files
^fileproc:~^Program to refile the message
^lproc:~^Program to list the contents of a message
^sendproc:~^Program to use to send the message
^whomproc:~^Program to determine who a message would go to
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-send/">send</a></i>(1), <i><a href="/docs/linux/man/1-whom/">whom</a></i>(1)</p>
<h2>DEFAULTS</h2>
<pre>
`<code>-prompt</code>' defaults to ``What Now?&nbsp;<wbr>''
</pre>
<h2>BUGS</h2>
<p> If the initial edit fails, <code>whatnow</code> deletes your draft (by renaming it with a site-dependent prefix (usually a comma); failure of a later edit preserves the draft. </p>
<p> If the <i>buildmimeproc</i> fails (returns a nonzero status), <code>whatnow</code> simply prints a &#8220;What now?&#8221; prompt. <code>whatnow</code> depends on the <i>buildmimeproc</i> to tell the user that something went wrong. </p>
<p> If <i>whatnowproc</i> is <code>whatnow</code>, then <code>comp</code>, <code>dist</code>, <code>forw</code>, and <code>repl</code> use a built-in <code>whatnow</code>, and do not actually run the <code>whatnow</code> program. Hence, if you define your own <i>whatnowproc</i>, don&#8217;t call it <code>whatnow</code> since it won&#8217;t be run. </p>
<p> If <i>sendproc</i> is <code>send</code>, then <code>whatnow</code> uses a built-in <code>send</code>, it does not actually run the <code>send</code> program. Hence, if you define your own <i>sendproc</i>, don&#8217;t call it <code>send</code> since <code>whatnow</code> won&#8217;t run it. </p>
