---

title: "cyradm(1)"
name: "cyradm"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cyradm/"
description: "cyradm – Cyrus administration shell, alter ego of Cyrus::IMAP::Shell"
---

<p> cyradm &#8211; Cyrus administration shell, alter ego of Cyrus::IMAP::Shell </p>
<h2>SYNOPSIS</h2>
<pre><code>
$ cyradm[--user user][--[no] rc][--systemrc file][--userrc file] &gt; [--port n][--auth mechanism][--tlskey keyfile][--notls] &gt; [--server] server
</code></pre>
<p> but possibly </p>
<pre>
  $ perl -MCyrus::IMAP::Shell -e 'run(&quot;myscript&quot;)'
</pre>
<p> or even (not recommended) </p>
<pre><code>
use Cyrus::IMAP::Admin::Shell;
run('myscriptname');
</code></pre>
<h2>DESCRIPTION</h2>
<p> This module implements <code>cyradm</code> in Perl. It is a shell around Cyrus::IMAP::Admin. Commands are provided in both Tcl-compatible forms and GNU-style long option forms.</p>
<h2>COMMANDS</h2>
<dl>
<dt>&quot;authenticate&quot; [&quot;&#8211;minssf&quot; <i>N</i>] [&quot;&#8211;maxssf&quot; <i>N</i>] [&quot;&#8211;mechanisms&quot; <i>list</i>] [<i>user</i>]</dt>
<dd>
</dd><dt>&quot;auth&quot; [&quot;&#8211;minssf&quot; <i>N</i>] [&quot;&#8211;maxssf&quot; <i>N</i>] [&quot;&#8211;mechanisms&quot; <i>list</i>] [<i>user</i>]</dt>
<dd>
</dd><dt>&quot;login&quot; [&quot;&#8211;minssf&quot; <i>N</i>] [&quot;&#8211;maxssf&quot; <i>N</i>] [&quot;&#8211;mechanisms&quot; <i>list</i>] [<i>user</i>]</dt>
<dd> Authenticate to server. You must already be connected to a server and Cyrus imapd will refuse to allow you to re-authenticate once you have authenticated once.</dd>
<dt>&quot;chdir&quot; <i>directory</i></dt>
<dd>
</dd><dt>&quot;cd&quot; <i>directory</i></dt>
<dd> Change directory. A <tt>&quot;pwd&quot;</tt> builtin is not provided, but the default command action will run <tt>&quot;pwd&quot;</tt> from a shell if invoked.</dd>
<dt>&quot;createmailbox&quot; [&quot;&#8211;partition&quot; <i>partition</i>] <i>mailbox</i></dt>
<dd>
</dd><dt>&quot;createmailbox&quot; <i>mailbox</i> <i>partition</i></dt>
<dd>
</dd><dt>&quot;create&quot; [&quot;&#8211;partition&quot; <i>partition</i>] <i>mailbox</i></dt>
<dd>
</dd><dt>&quot;create&quot; <i>mailbox</i> <i>partition</i></dt>
<dd>
</dd><dt>&quot;cm&quot; [&quot;&#8211;partition&quot; <i>partition</i>] <i>mailbox</i></dt>
<dd>
</dd><dt>&quot;cm&quot; <i>mailbox</i> <i>partition</i></dt>
<dd> Create a mailbox on the default or a specified partition. Both old-style and getopt-style usages are accepted (combining them will produce an error).</dd>
<dt>&quot;deleteaclmailbox&quot; <i>mailbox</i> <i>id</i> [&#8230;]</dt>
<dd>
</dd><dt>&quot;deleteacl&quot; <i>mailbox</i> <i>id</i> [&#8230;]</dt>
<dd>
</dd><dt>&quot;dam&quot; <i>mailbox</i> <i>id</i> [&#8230;]</dt>
<dd> Remove ACLs from the specified mailbox.</dd>
<dt>&quot;deletemailbox&quot; <i>mailbox</i></dt>
<dd>
</dd><dt>&quot;delete&quot; <i>mailbox</i></dt>
<dd>
</dd><dt>&quot;dm&quot; <i>mailbox</i></dt>
<dd> Delete the specified mailbox. </dd>
<p> Administrators do not have implicit delete rights on mailboxes. Use the <code>setaclmailbox</code> command to grant the <tt>&quot;x&quot;</tt> permission to your principal if you need to delete a mailbox you do not own. </p>
<p> Note that the online help admits to an optional host argument. This argument is not currently used, and will be rejected with an error if specified; it is reserved for IMSP.</p>
<dt>&quot;disconnect&quot;</dt>
<dd>
</dd><dt>&quot;disc&quot;</dt>
<dd> Disconnect from the current server. The prompt will revert to <tt>&quot;cyradm&gt;&quot;</tt>.</dd>
<dt>&quot;exit&quot; [<i>number</i>]</dt>
<dd>
</dd><dt>&quot;quit&quot; [<i>number</i>]</dt>
<dd> Exit <code>cyradm</code>, optionally with a specific exit status; the exit status of the last command will be used if one is not specified.</dd>
<dt>help [command]</dt>
<dd>
</dd><dt>? [command]</dt>
<dd> Show help for <tt>&quot;command&quot;</tt> or all commands.</dd>
<dt>&quot;info&quot; [<i>mailbox</i>]</dt>
<dd> Display the mailbox/server metadata.</dd>
<dt>&quot;listaclmailbox&quot; <i>mailbox</i></dt>
<dd>
</dd><dt>&quot;listacl&quot; <i>mailbox</i></dt>
<dd>
</dd><dt>&quot;lam&quot; <i>mailbox</i></dt>
<dd> List ACLs on the specified mailbox.</dd>
<dt>&quot;listmailbox&quot; [&quot;&#8211;subscribed&quot;] [<i>pattern</i> [<i>reference</i>]]</dt>
<dd>
</dd><dt>&quot;list&quot; [&quot;&#8211;subscribed&quot;] [<i>pattern</i> [<i>reference</i>]]</dt>
<dd>
</dd><dt>&quot;lm&quot; [&quot;&#8211;subscribed&quot;] [<i>pattern</i> [<i>reference</i>]]</dt>
<dd> List all, or all subscribed, mailboxes matching the specified pattern. The pattern may have embedded wildcards <tt>'*'</tt> or <tt>'%'</tt>, which match anything or anything except the separator character, respectively. </dd>
<p> Mailboxes returned will be relative to the specified reference if one is specified. This allows a mailbox list to be limited to a particular hierarchy. </p>
<p> In some cases when the <tt>'%'</tt> wildcard is used to end a pattern, it may match an entry which is not a mailbox but which contains other mailboxes. In this case, the entry will be parenthesized to indicate that it is a root for other mailboxes, as opposed to a mailbox itself.</p>
<dt>&quot;listquota&quot; <i>root</i></dt>
<dd>
</dd><dt>&quot;lq&quot; <i>root</i></dt>
<dd> List quotas on specified root. If the specified mailbox path does not have a quota assigned, an error will be raised; see <i>listquotaroot</i> for a way to find the quota root for a mailbox.</dd>
<dt>&quot;listquotaroot&quot; <i>mailbox</i></dt>
<dd>
</dd><dt>&quot;lqm&quot; <i>mailbox</i></dt>
<dd>
</dd><dt>&quot;lqr&quot; <i>mailbox?</i></dt>
<dd> show quota roots and quotas for mailbox</dd>
<dt>&quot;mboxconfig&quot; <i>mailbox</i> <i>attribute</i> <i>value</i></dt>
<dd>
</dd><dt>&quot;mboxcfg&quot; <i>mailbox</i> <i>attribute</i> <i>value</i></dt>
<dd> Set mailbox metadata. A value of &#8220;none&#8221; will remove the attribute. The currently supported attributes are:</dd>
<dl>
<dl>
<dt>&quot;comment&quot;</dt>
<dd> Sets a comment or description associated with the mailbox.</dd>
<dt>&quot;expire&quot;</dt>
<dd> Sets the number of days after which messages will be expired from the mailbox.</dd>
<dt>&quot;news2mail&quot;</dt>
<dd> Sets an email address to which messages injected into the server via NNTP  will be sent.</dd>
<dt>&quot;sharedseen&quot;</dt>
<dd> Enables the use of a shared \Seen flag on messages rather than a per-user \Seen flag. The &#8216;s&#8217; right in the mailbox ACL still controls whether a user can set the shared \Seen flag.</dd>
<dt>&quot;sieve&quot;</dt>
<dd> Indicates the name of the global sieve script that should be run when a message is delivered to the shared mailbox (not used for personal mailboxes).</dd>
<dt>&quot;squat&quot;</dt>
<dd> Indicates that the mailbox should have a squat index created for it.</dd>
<dt>&quot;/explicit/annotation&quot;</dt>
<dd> Sets the annotation <i>/explicit/annotation</i> on <i>mailbox</i> to <i>value</i>.</dd></dl>
</dl>
<dl>
</dl>
<dt>&quot;renamemailbox&quot; [&quot;&#8211;partition&quot; <i>partition</i>] <i>oldname</i> <i>newname</i></dt>
<dd>
</dd><dt>&quot;rename&quot; [&quot;&#8211;partition&quot; <i>partition</i>] <i>oldname</i> <i>newname</i></dt>
<dd>
</dd><dt>&quot;renm&quot; [&quot;&#8211;partition&quot; <i>partition</i>] <i>oldname</i> <i>newname</i></dt>
<dd>
</dd><dt>&quot;renamemailbox&quot; <i>oldname</i> <i>newname</i> [<i>partition</i>]</dt>
<dd>
</dd><dt>&quot;rename&quot; <i>oldname</i> <i>newname</i> [<i>partition</i>]</dt>
<dd>
</dd><dt>&quot;renm&quot; <i>oldname</i> <i>newname</i> [<i>partition</i>]</dt>
<dd> Rename the specified mailbox, optionally moving it to a different partition. Both old-style and getopt-style usages are accepted; combining them will produce an error.</dd>
<dt>server [&#8211;noauthenticate] [server]</dt>
<dd>
</dd><dt>connect [&#8211;noauthenticate] [server]</dt>
<dd>
</dd><dt>servername [&#8211;noauthenticate] [server]</dt>
<dd> With no arguments, show the current server. With an argument, connect to that server. It will prompt for automatic login unless the <tt>&quot;--noauthenticate&quot;</tt> option is specified. (This may change; in particular, either automatic authentication will be removed or all <tt>&quot;authenticate&quot;</tt> options will be added.) </dd>
<p> When connected to a server, <code>cyradm</code>&#8216;s prompt changes from <tt>&quot;cyradm&gt;&quot;</tt> to <tt>&quot;servername&gt;&quot;</tt>, where <i>servername</i> is the fully qualified domain name of the connected server.</p>
<dt>&quot;setaclmailbox&quot; <i>mailbox</i> <i>id</i> <i>rights</i> [<i>id</i> <i>rights</i> &#8230;]</dt>
<dd>
</dd><dt>&quot;setacl&quot; <i>mailbox</i> <i>id</i> <i>rights</i> [<i>id</i> <i>rights</i> &#8230;]</dt>
<dd>
</dd><dt>&quot;sam&quot; <i>mailbox</i> <i>id</i> <i>rights</i> [<i>id</i> <i>rights</i> &#8230;]</dt>
<dd> Set ACLs on a mailbox. The ACL may be one of the special strings <tt>&quot;none&quot;</tt>, <tt>&quot;read&quot;</tt> (<tt>&quot;lrs&quot;</tt>), <tt>&quot;post&quot;</tt> (<tt>&quot;lrsp&quot;</tt>), <tt>&quot;append&quot;</tt> (<tt>&quot;lrsip&quot;</tt>), <tt>&quot;write&quot;</tt> (<tt>&quot;lrswipkxte&quot;</tt>), <tt>&quot;delete&quot;</tt> (<tt>&quot;lrxte&quot;</tt>), or <tt>&quot;all&quot;</tt> (<tt>&quot;lrswipkxte&quot;</tt>), or any combinations of the ACL codes:</dd>
<dl>
<dl>
<dt>l</dt>
<dd> Lookup (mailbox is visible to LIST/LSUB, SUBSCRIBE mailbox)</dd>
<dt>r</dt>
<dd> Read (SELECT/EXAMINE the mailbox, perform STATUS)</dd>
<dt>s</dt>
<dd> Seen (set/clear \SEEN flag via STORE, also set \SEEN flag during<br/>
&nbsp;<wbr>APPEND/COPY/FETCH&nbsp;<wbr>BODY[&#8230;])</dd>
<dt>w</dt>
<dd> Write flags other than \SEEN and \DELETED</dd>
<dt>i</dt>
<dd> Insert (APPEND, COPY destination)</dd>
<dt>p</dt>
<dd> Post (send mail to mailbox)</dd>
<dt>k</dt>
<dd> Create mailbox (CREATE new sub-mailboxes, parent for new mailbox in RENAME)</dd>
<dt>x</dt>
<dd> Delete mailbox (DELETE mailbox, old mailbox name in RENAME)</dd>
<dt>t</dt>
<dd> Delete messages (set/clear \DELETED flag via STORE, also set \DELETED<br/>
&nbsp;<wbr>flag during&nbsp;<wbr>APPEND/COPY)</dd>
<dt>e</dt>
<dd> Perform EXPUNGE and expunge as part of CLOSE</dd>
<dt>a</dt>
<dd> Administer (SETACL/DELETEACL/GETACL/LISTRIGHTS)</dd></dl>
</dl>
<dl>
</dl>
<dt>&quot;setinfo&quot; <i>attribute</i> <i>value</i></dt>
<dd> Set server metadata. A value of &#8220;none&#8221; will remove the attribute. The currently supported attributes are:</dd>
<dl>
<dl>
<dt>&quot;motd&quot;</dt>
<dd> Sets a &#8220;message of the day&#8221;. The message gets displayed as an ALERT after authentication.</dd>
<dt>&quot;comment&quot;</dt>
<dd> Sets a comment or description associated with the server.</dd>
<dt>&quot;admin&quot;</dt>
<dd> Sets the administrator email address for the server.</dd>
<dt>&quot;shutdown&quot;</dt>
<dd> Sets a shutdown message. The message gets displayed as an ALERT and all users are disconnected from the server (subsequent logins are disallowed).</dd>
<dt>&quot;expire&quot;</dt>
<dd> Sets the number of days after which messages will be expired from the server (unless overridden by a mailbox annotation).</dd>
<dt>&quot;squat&quot;</dt>
<dd> Indicates that all mailboxes should have a squat indexes created for them (unless overridden by a mailbox annotation).</dd></dl>
</dl>
<dl>
</dl>
<dt>&quot;setquota&quot; <i>root</i> <i>resource</i> <i>value</i> [<i>resource</i> <i>value</i> &#8230;]</dt>
<dd>
</dd><dt>&quot;sq&quot; <i>root</i> <i>resource</i> <i>value</i> [<i>resource</i> <i>value</i> &#8230;]</dt>
<dd> Set a quota on the specified root, which may or may not be an actual mailbox. The only <i>resource</i> understood by <code>Cyrus</code> is <tt>&quot;STORAGE&quot;</tt>. The <i>value</i> may be the special string <tt>&quot;none&quot;</tt> which will remove the quota.</dd>
<dt>&quot;version&quot;</dt>
<dd>
</dd><dt>&quot;ver&quot;</dt>
<dd> Display the version info of the current server.</dd>
<dt>&quot;xfermailbox&quot; [&quot;&#8211;partition&quot; <i>partition</i>] <i>mailbox</i> <i>server</i></dt>
<dd>
</dd><dt>&quot;xfer&quot; [&quot;&#8211;partition&quot; <i>partition</i>] <i>mailbox</i> <i>server</i></dt>
<dd>
</dd><dt>&quot;xfermailbox&quot; <i>mailbox</i> <i>server</i> [<i>partition</i>]</dt>
<dd>
</dd><dt>&quot;xfer&quot; <i>mailbox</i> <i>server</i> [<i>partition</i>]</dt>
<dd> Transfer (relocate) the specified mailbox to a different server. Both old-style and getopt-style usages are accepted; combining them will produce an error.</dd></dl>
<h2>NOTES</h2>
<p> GNU-style long options must be given in their entirety; Tcl-style options may be abbreviated. </p>
<p> Tcl-style options are provided as a compatibility feature. They will probably go away in the future. </p>
<p> Multiple commands can be given on a line, separated by <tt>';'</tt> characters. </p>
<p> All commands set an exit status, which at present is not useful. </p>
<p> Unknown commands are passed to a subshell for execution. </p>
<p> The Tcl version of <code>cyradm</code> is used for scripting as well as interactively. While this is possible to a limited extent by use of the <tt>&quot;run&quot;</tt> method, scripting would normally be done with <tt>&quot;Cyrus::IMAP::Admin&quot;</tt>, which is far more flexible than either interactive <tt>&quot;cyradm&quot;</tt> or the Tcl scripting mechanism for Cyrus. </p>
<p> <code>cyradm</code> understands <code>/bin/sh</code>-style redirection: any command can have its standard or error output redirected, with all <code>sh</code>-style redirections (except <tt>&quot;&lt;&gt;&quot;</tt>) supported. It does not currently understand pipes or backgrounding. </p>
<p> If the <tt>&quot;Term::Readline::Perl&quot;</tt> or <tt>&quot;Term::Readline::GNU&quot;</tt> modules are available, <code>cyradm</code> will use it. </p>
<p> An alias facility is implemented internally, but no access is currently provided to it. This will change, if only to allow some of the predefined aliases to be removed if they conflict with useful shell commands.</p>
<h2>AUTHOR</h2>
<p> Brandon S. Allbery, allbery [at] ece.cmu.edu</p>
<h2>SEE ALSO</h2>
<p> Cyrus::IMAP::Admin Term::ReadLine <i><a href="/docs/linux/man/1-sh/">sh</a></i>(1), <i><a href="/docs/linux/man/1-perl/">perl</a></i>(1), <i>imapd</i>(8). </p>
