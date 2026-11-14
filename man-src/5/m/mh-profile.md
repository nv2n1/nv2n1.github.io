---
title: "mh-profile(5)"
name: "mh-profile"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mh-profile/"
description: "mh-profile – user profile customization for nmh message handler"
---

<p>mh-profile &#8211; user profile customization for nmh message handler</p>
<h2>Description</h2>
<p>Each user of <code>nmh</code> is expected to have a file named <i>.mh_profile</i> in his or her home directory. This file contains a set of user parameters used by some or all of the <code>nmh</code> family of programs. Each entry in the file is of the format </p>
<dl>
<dd><i>profile-component</i>: <i>value</i></dl>
<p> If the text of profile entry is long, you may extend it across several real lines by indenting the continuation lines with leading spaces or tabs. Comments may be introduced by a line starting with `#:&#8217;: </p>
<dl>
<dd><i>#</i>: This is a comment.</dl>
<p> Blank lines are not permitted in <i>.mh_profile.</i> The shell quoting conventions are not available in the <i>.mh_profile</i>; each token is separated by whitespace.</p>
<h3>Standard Profile Entries</h3>
<p>The possible profile components are exemplified below. The only mandatory entry is `Path:&#8217;. The others are optional; some have default values if they are not present. In the notation used below, (profile, default) indicates whether the information is kept in the user&#8217;s <code>nmh</code> profile or <code>nmh</code> context, and indicates what the default value is. Note that a profile component can only appear once. Multiple appearances with trigger a warning that all appearances after the first are ignored. </p>
<p> <code>Path</code>: Mail</p>
<dl>
<dd>Locates <code>nmh</code> transactions in directory &#8220;Mail&#8221;. This is the only mandatory profile entry. (profile, no default)</dl>
<p> <code>context</code>: context</p>
<dl>
<dd>Declares the location of the <code>nmh</code> context file. This is overridden by the environment variable <code>$MHCONTEXT</code>. See the <code>HISTORY</code> section below. (profile, default: &lt;nmh-dir&gt;/context)</dl>
<p> <code>Current-Folder</code>: inbox</p>
<dl>
<dd>Keeps track of the current open folder. (context, default: folder specified by &#8220;Inbox&#8221;)</dl>
<p> <code>Inbox</code>: inbox</p>
<dl>
<dd>Defines the name of your default inbox. (profile, default: inbox)</dl>
<p> <code>Previous-Sequence</code>: <i>pseq</i></p>
<dl>
<dd>Names the sequence or sequences which should be defined as the `msgs&#8217; or `msg&#8217; argument given to any <code>nmh</code> command. If not present or empty, no such sequences are defined. Otherwise, for each name given, the sequence is first zero&#8217;d and then each message is added to the sequence. Read the <i><a href="/docs/linux/man/5-mh-sequence/">mh-sequence</a></i>(5) man page for the details about this sequence. (profile, no default)</dl>
<p> <code>Sequence-Negation</code>: not</p>
<dl>
<dd>Defines the string which, when prefixed to a sequence name, negates that sequence. Hence, &#8220;notseen&#8221; means all those messages that are not a member of the sequence &#8220;seen&#8221;. Read the <i><a href="/docs/linux/man/5-mh-sequence/">mh-sequence</a></i>(5) man page for the details. (profile, no default)</dl>
<p> <code>Unseen-Sequence</code>: unseen</p>
<dl>
<dd>Names the sequence or sequences which should be defined as those messages which are unread. The commands <code>inc</code>, <code>rcvstore</code>, <code>mhshow</code>, and <code>show</code> will add or remove messages from these sequences when they are incorporated or read. If not present or empty, no such sequences are defined. Otherwise, each message is added to, or removed from, each sequence name given. Read the <i><a href="/docs/linux/man/5-mh-sequence/">mh-sequence</a></i>(5) man page for the details about this sequence. (profile, no default)</dl>
<p> <code>mh-sequences</code>: .mh_sequences</p>
<dl>
<dd>The name of the file in each folder which defines public sequences. To disable the use of public sequences, leave the value portion of this entry blank. (profile, default: .mh_sequences)</dl>
<p> <code>atr-</code><i>seq</i><code>&#8211;</code><i>folder</i><code>:</code> 172 178-181 212</p>
<dl>
<dd>Keeps track of the private sequence called &#8220;seq&#8221; in the specified folder. Private sequences are generally used for read-only folders. See the <i><a href="/docs/linux/man/5-mh-sequence/">mh-sequence</a></i>(5) man page for details about private sequences. (context, no default)</dl>
<p> <code>Editor</code>: vi</p>
<dl>
<dd>Defines the editor to be used by the commands <code>comp</code>, <code>dist</code>, <code>forw</code>, and <code>repl</code>. If not set in profile the value will be taken from the VISUAL and EDITOR environment variables. (profile, default: vi)</dl>
<p> <code>Msg-Protect</code>: 600</p>
<dl>
<dd>An octal number which defines the permission bits for new message files. See <i><a href="/docs/linux/man/1-chmod/">chmod</a></i>(1) for an explanation of the octal number. Note that some filesystems, such as FAT32, do not support removal of read file permissions. (profile, default: 0600)</dl>
<p> <code>Folder-Protect</code>: 700</p>
<dl>
<dd>An octal number which defines the permission bits for new folder directories. See <i><a href="/docs/linux/man/1-chmod/">chmod</a></i>(1) for an explanation of the octal number. (profile, default: 700)</dl>
<p> <code>datalocking</code>: fcntl</p>
<dl>
<dd>The locking algorithm used to lock changes to any <code>nmh</code> data files, such as sequences or the context. The locking algorithm is any one of the following entries: </p>
<dl>
<dd>
<pre>fcntl dot flock lockf</pre>
</dl>
<p> Available locking algorithms can vary depending on what is supported by the operating system. Note: currently transactional locking is only supported on public sequences; see <i><a href="/docs/linux/man/5-mh-sequence/">mh-sequence</a></i>(5) for more information. (profile, default: fcntl)</dl>
<p> <i>program</i>: <i>default switches</i></p>
<dl>
<dd>Sets default switches to be used whenever the mh program <i>program</i> is invoked. For example, one could override the &#8220;Editor:&#8221; profile component when replying to messages by adding a component such as: </p>
<dl>
<dd>repl: -editor /bin/ed</dl>
<p> (profile, no defaults)</dl>
<p> <i>lasteditor</i><code>-next:</code> <i>nexteditor</i></p>
<dl>
<dd>Names &#8220;nexteditor&#8221; to be the default editor after using &#8220;lasteditor&#8221;. This takes effect at &#8220;What now?&#8221; prompt in <code>comp</code>, <code>dist</code>, <code>forw</code>, and <code>repl</code>. After editing the draft with &#8220;lasteditor&#8221;, the default editor is set to be &#8220;nexteditor&#8221;. If the user types &#8220;edit&#8221; without any arguments to &#8220;What now?&#8221;, then &#8220;nexteditor&#8221; is used. (profile, no default)</dl>
<p> <code>Folder-Stack</code>: <i>folders</i></p>
<dl>
<dd>The contents of the folder-stack for the <code>folder</code> command. (context, no default)</dl>
<p> <code>Local-Mailbox</code>: Your Username &lt;user [at] some.host&gt;</p>
<dl>
<dd>Tells the various MH tools what your local mailbox is. If set, will be used by the default component files by tools like <code>comp</code> and <code>repl</code> to construct your default &#8220;From&#8221; header. The text used here will be copied exactly to your From: header, so it should already be RFC 822 compliant. If this is set, the <code>Signature</code> profile entry is NOT used, so it should include a signature as well. (profile, default: userid [at] local.hostname)</dl>
<p> <code>Alternate-Mailboxes</code>: mh [at] uci-750a, bug-mh*</p>
<dl>
<dd>Tells <code>repl</code> and <code>scan</code> which addresses are really yours. In this way, <code>repl</code> knows which addresses should be included in the reply, and scan knows if the message really originated from you. Addresses must be separated by a comma, and the hostnames listed should be the &#8220;official&#8221; hostnames for the mailboxes you indicate, as local nicknames for hosts are not replaced with their official site names. For each address, if a host is not given, then that address on any host is considered to be you. In addition, an asterisk (`*&#8217;) may appear at either or both ends of the mailbox and host to indicate wild-card matching. (profile, default: your user-id)</dl>
<p> <code>Aliasfile</code>: aliases <i>other-alias</i></p>
<dl>
<dd>Indicates aliases files for <code>ali</code>, <code>whom</code>, and <code>send</code>. This may be used instead of the <code>-alias</code> <i>file</i> switch. (profile, no default)</dl>
<p> <code>Draft-Folder</code>: drafts</p>
<dl>
<dd>Indicates a default draft folder for <code>comp</code>, <code>dist</code>, <code>forw</code>, <code>refile</code>, and <code>repl</code>. Read the <i><a href="/docs/linux/man/5-mh-draft/">mh-draft</a></i>(5) man page for details. (profile, no default)</dl>
<p> <code>digest-issue-</code><i>list</i><code>:</code> 1</p>
<dl>
<dd>Tells <code>forw</code> the last issue of the last volume sent for the digest <i>list</i>. (context, no default)</dl>
<p> <code>digest-volume-</code><i>list</i><code>:</code> 1</p>
<dl>
<dd>Tells <code>forw</code> the last volume sent for the digest <i>list</i>. (context, no default)</dl>
<p> <code>MailDrop</code>: .mail</p>
<dl>
<dd>Tells <code>inc</code> your maildrop, if different from the default. This is superseded by the environment variable <code>$MAILDROP</code>. (profile, default: /var/mail/$USER)</dl>
<p> <code>Signature</code>: RAND MH System (agent: Marshall Rose)</p>
<dl>
<dd>Tells front-end programs such as <code>comp,</code> <code>forw,</code> and <code>repl</code> your mail signature. This is superseded by the environment variable <code>$SIGNATURE</code>. If <code>$SIGNATURE</code> is not set and this profile entry is not present, the &#8220;gcos&#8221; field of the <i>/etc/passwd</i> file will be used. Your signature will be added to the address <code>send</code> puts in the &#8220;From:&#8221; header; do not include an address in the signature text. The &#8220;Local-Mailbox&#8221; profile component supersedes all of this. (profile, no default)</dl>
<p> <code>credentials</code>: legacy</p>
<dl>
<dd>Indicates how the username and password credentials will be retrieved for access to external servers, such as those that provide SMTP or POP service. The supported entry values are &#8220;legacy&#8221; and &#8220;file:<i>netrc</i>&#8221;. With &#8220;legacy&#8221;, or if there is no credentials entry, the username is the first of: </p>
<dl>
<dd>1) <code>-user</code> switch to <code>send</code>, <code>post</code>, <code>whom</code>, <code>inc</code>, or <code>msgchk</code> program<br />
 2) the login name on the local machine</dl>
<p> The password for SMTP services is the first of: </p>
<dl>
<dd>1) password value from matching entry in file named &#8220;.netrc&#8221; in the user&#8217;s home directory<br />
 2) password obtained by interactively prompting the user</dl>
<p> The password for POP service when the <code>-sasl</code> switch is used with one of these programs is the login name on the local machine. </p>
<p> With a &#8220;file:<i>netrc</i>&#8221; <code>credentials</code> entry, the username is the first of: </p>
<dl>
<dd>1) <code>-user</code> switch to program<br />
 2) login name from matching entry in <i>netrc</i> file<br />
 3) value provided by user in response to interactive query</dl>
<p> Similarly, the password is provided either in the <i>netrc</i> file or interactively. <i>netrc</i> can be any valid filename, either absolute or relative to Path or $HOME. The <i>netrc</i> file contains authentication information, for each server, using a line of the following form. Replace the words <i>myserver</i>, <i>mylogin</i>, and <i>mypassword</i> with your own account information: </p>
<dl>
<dd><code>machine</code> <i>myserver</i> <code>login</code> <i>mylogin</i> <code>password</code> <i>mypassword</i></dl>
<p> This <i>netrc</i> file must be owned and readable only by you. (profile, default: legacy)</dl>
<h3>Process Profile Entries</h3>
<p>The following profile elements are used whenever an <code>nmh</code> program invokes some other program such as <code>more</code>. The <i>.mh_profile</i> can be used to select alternate programs if the user wishes. The default values are given in the examples. </p>
<p> If the profile element contains spaces, the element is split at spaces into tokens and each token is given as a separate argument to the <i><a href="/docs/linux/man/2-execvp/">execvp</a></i>(2) system call. If the element contains shell metacharacters then the entire element is executed using <code>/bin/sh</code>. </p>
<p> <code>buildmimeproc</code>: /usr/bin/mhbuild</p>
<dl>
<dd>This is the program used by <code>whatnow</code> to process drafts which are MIME composition files.</dl>
<p> <code>fileproc</code>: /usr/bin/refile</p>
<dl>
<dd>This program is used to refile or link a message to another folder. It is used by <code>send</code> to file a copy of a message into a folder given by a &#8220;Fcc:&#8221; field. It is used by the draft folder facility in <code>comp</code>, <code>dist</code>, <code>forw</code>, and <code>repl</code> to refile a draft message into another folder. It is used to refile a draft message in response to the <code>refile</code> directive at the &#8220;What now?&#8221; prompt.</dl>
<p> <code>formatproc</code>:</p>
<dl>
<dd>Program called by <code>mhl</code> to filter a component when it is tagged with the &#8220;format&#8221; variable in the mhl filter. See <i><a href="/docs/linux/man/5-mhl/">mhl</a></i>(5) for more information.</dl>
<p> <code>incproc</code>: /usr/bin/inc</p>
<dl>
<dd>Program called by <code>mhmail</code> to incorporate new mail when it is invoked with no arguments.</dl>
<p> <code>lproc</code>: more</p>
<dl>
<dd>This program is used to list the contents of a message in response to the <code>list</code> directive at the &#8220;What now?&#8221; prompt. It is also used by the draft folder facility in <code>comp</code>, <code>dist</code>, <code>forw</code>, and <code>repl</code> to display the draft message. (Note that <code>$PAGER</code> supersedes the default built-in pager command.)</dl>
<p> <code>mailproc</code>: /usr/bin/mhmail</p>
<dl>
<dd>This is the program used to automatically mail various messages and notifications. It is used by <code>conflict</code> when using the <code>-mail</code> option. It is used by <code>send</code> to post failure notices. It is used to retrieve an external-body with access-type `mail-server&#8217; (such as when storing the body with <code>mhstore</code>).</dl>
<p> <code>mhlproc</code>: /usr/libexec/nmh/mhl</p>
<dl>
<dd>This is the program used to filter messages in various ways. It is used by <code>mhshow</code> to filter and display the message headers of MIME messages. When the <code>-format</code> or <code>-filter</code> option is used by <code>forw</code> or <code>repl</code>, the <i>mhlproc</i> is used to filter the message that you are forwarding, or to which you are replying. When the <code>-filter</code> option is given to <code>send</code>, the <i>mhlproc</i> is used to filter the copy of the message that is sent to &#8220;Bcc:&#8221; recipients.</dl>
<p> <code>moreproc</code>: more</p>
<dl>
<dd>This is the program used by <code>mhl</code> to page the <code>mhl</code> formatted message when displaying to a terminal. It is also the default program used by <code>mhshow</code> to display message bodies (or message parts) of type text/plain. (Note that <code>$PAGER</code> supersedes the default built-in pager command.)</dl>
<p> <code>mshproc</code>: /usr/bin/msh</p>
<dl>
<dd>Currently not used.</dl>
<p> <code>packproc</code>: /usr/bin/packf</p>
<dl>
<dd>Currently not used.</dl>
<p> <code>postproc</code>: /usr/libexec/nmh/post</p>
<dl>
<dd>This is the program used by <code>send</code>, <code>mhmail</code>, <code>rcvdist</code>, and <code>viamail</code> (used by the <code>sendfiles</code> shell script) to post a message to the mail transport system. It is also called by <code>whom</code> (called with the switches <code>-whom</code> and <code>-library</code>) to do address verification.</dl>
<p> <code>rmmproc</code>: none</p>
<dl>
<dd>This is the program used by <code>rmm</code>, <code>refile</code>, and <code>mhfixmsg</code> to delete a message from a folder.</dl>
<p> <code>sendproc</code>: /usr/bin/send</p>
<dl>
<dd>This is the program to use by <code>whatnow</code> to actually send the message</dl>
<p> <code>showmimeproc</code>: /usr/bin/mhshow</p>
<dl>
<dd>This is the program used by <code>show</code> to process and display non-text (MIME) messages.</dl>
<p> <code>showproc</code>: /usr/libexec/nmh/mhl</p>
<dl>
<dd>This is the program used by <code>show</code> to filter and display text (non-MIME) messages.</dl>
<p> <code>whatnowproc</code>: /usr/bin/whatnow</p>
<dl>
<dd>This is the program invoked by <code>comp</code>, <code>forw</code>, <code>dist</code>, and <code>repl</code> to query about the disposition of a composed draft message.</dl>
<p> <code>whomproc</code>: /usr/bin/whom</p>
<dl>
<dd>This is the program used by <code>whatnow</code> to determine to whom a message would be sent.</dl>
<h3>Profile Lookup</h3>
<p>After consulting .mh_profile, some programs read an optional profile specified by a program-specific environment variable, and then the system-wide profile /etc/nmh/mhn.defaults. These programs are mhbuild, mhshow, mhstore, and mhn. mhfixmsg is similar, but has no optional profile. </p>
<p> The first occurrence of a component is used, e.g. .mh_profile&#8217;s trumps $MHSHOW&#8217;s. A component with no value still stops further occurrences being used, but is considered absent.</p>
<h3>Environment Variables</h3>
<p>The operation of <code>nmh</code> and its commands it also controlled by the presence of certain environment variables. </p>
<p> Many of these environment variables are used internally by the &#8220;What now?&#8221; interface. It&#8217;s amazing all the information that has to get passed via environment variables to make the &#8220;What now?&#8221; interface look squeaky clean to the <code>nmh</code> user, isn&#8217;t it? The reason for all this is that the <code>nmh</code> user can select <code>any</code> program as the <i>whatnowproc</i>, including one of the standard shells. As a result, it&#8217;s not possible to pass information via an argument list. The convention is that environment variables whose names are all upper-case are user-settable; those whose names are lower-case only are used internally by nmh and should not generally be set by the user. </p>
<p> <code>$MH</code></p>
<dl>
<dd>With this environment variable, you can specify a profile other than <i>.mh_profile</i> to be read by the <code>nmh</code> programs that you invoke. If the value of <code>$MH</code> is not absolute, (i.e., does not begin with a &#8220;/&#8221;), it will be presumed to start from the current working directory. This is one of the very few exceptions in <code>nmh</code> where non-absolute pathnames are not considered relative to the user&#8217;s <code>nmh</code> directory.</dl>
<p> <code>$MHCONTEXT</code></p>
<dl>
<dd>With this environment variable, you can specify a context other than the normal context file (as specified in the <code>nmh</code> profile). As always, unless the value of <code>$MHCONTEXT</code> is absolute, it will be presumed to start from your <code>nmh</code> directory.</dl>
<p> <code>$MHBUILD</code></p>
<dl>
<dd>With this environment variable, you can specify an additional user profile (file) to be read by <code>mhbuild</code>, in addition to the mhn.defaults profile.</dl>
<p> <code>$MHN</code></p>
<dl>
<dd>With this environment variable, you can specify an additional user profile (file) to be read by <code>mhn</code>, in addition to the mhn.defaults profile. <code>mhn</code> is deprecated, so this support for this variable will be removed from a future nmh release.</dl>
<p> <code>$MHSHOW</code></p>
<dl>
<dd>With this environment variable, you can specify an additional user profile (file) to be read by <code>mhshow</code>, in addition to the mhn.defaults profile.</dl>
<p> <code>$MHSTORE</code></p>
<dl>
<dd>With this environment variable, you can specify an additional user profile (file) to be read by <code>mhstore</code>, in addition to the mhn.defaults profile.</dl>
<p> <code>$MAILDROP</code></p>
<dl>
<dd>This variable tells <code>inc</code> the default maildrop. This supersedes the &#8220;MailDrop&#8221; profile entry.</dl>
<p> <code>$MAILHOST</code></p>
<dl>
<dd>This variable tells <code>inc</code> the POP host to query for mail to incorporate. See the <a href="/docs/linux/man/1-inc/">inc</a>(1) man page for more information.</dl>
<p> <code>$USERNAME_EXTENSION</code></p>
<dl>
<dd>This variable is for use with username_extension masquerading. See the <a href="/docs/linux/man/5-mh-tailor/">mh-tailor</a>(5) man page.</dl>
<p> <code>$SIGNATURE</code></p>
<dl>
<dd>This variable tells <code>send</code> and <code>post</code> your mail signature. This supersedes the &#8220;Signature&#8221; profile entry, and is not used when the &#8220;Local-Mailbox&#8221; profile component is set.</dl>
<p> <code>$USER</code></p>
<dl>
<dd>This variable tells <code>repl</code> your user name and <code>inc</code> your default maildrop: see the &#8220;MailDrop&#8221; profile entry.</dl>
<p> <code>$HOME</code></p>
<dl>
<dd>This variable tells all <code>nmh</code> programs your home directory</dl>
<p> <code>$TERM</code></p>
<dl>
<dd>This variable tells <code>nmh</code> your terminal type. </p>
<p> The environment variable <code>$TERMCAP</code> is also consulted. In particular, these tell <code>scan</code> and <code>mhl</code> how to clear your terminal, and how many columns wide your terminal is. They also tell <code>mhl</code> how many lines long your terminal screen is.</dl>
<p> <code>$MHMTSCONF</code></p>
<dl>
<dd>If this variable is set to a non-null value, it specifies the name of the mail transport configuration file to use by <code>post</code>, <code>inc</code>, and other programs that interact with the mail transport system, instead of the default. See <a href="/docs/linux/man/5-mh-tailor/">mh-tailor</a>(5).</dl>
<p> <code>$MHMTSUSERCONF</code></p>
<dl>
<dd>If this variable is set to a non-null value, it specifies the name of a mail transport configuration file to be read in addition to the default. See <a href="/docs/linux/man/5-mh-tailor/">mh-tailor</a>(5).</dl>
<p> <code>$MHTMPDIR</code> <code>$TMPDIR</code></p>
<dl>
<dd>These variables are searched, in order, for the directory in which to create some temporary files.</dl>
<p> <code>$MHLDEBUG</code></p>
<dl>
<dd>If this variable is set to a non-null value, <code>mhl</code> will emit debugging information.</dl>
<p> <code>$MHPDEBUG</code></p>
<dl>
<dd>If this variable is set to a non-null value, <code>pick</code> will emit a representation of the search pattern.</dl>
<p> <code>$MHWDEBUG</code></p>
<dl>
<dd>If this variable is set to a non-null value, <code>nmh</code> commands that use the <code>Alternate-Mailboxes</code> profile entry will display debugging information about the values in that entry.</dl>
<p> <code>$PAGER</code></p>
<dl>
<dd>If set to a non-null value, this supersedes the value of the default built-in pager command.</dl>
<p> <code>$editalt</code></p>
<dl>
<dd>This is the alternate message. </p>
<p> This is set by <code>dist</code> and <code>repl</code> during edit sessions so you can peruse the message being distributed or replied to. The message is also available, when the <code>-atfile</code> switch is used, through a link called &#8220;@&#8221; in the current directory if your current working directory and the folder the message lives in are on the same UNIX filesystem, and if your current working directory is writable.</dl>
<p> <code>$mhdraft</code></p>
<dl>
<dd>This is the path to the working draft. </p>
<p> This is set by <code>comp</code>, <code>dist</code>, <code>forw</code>, and <code>repl</code> to tell the <i>whatnowproc</i> which file to ask &#8220;What now?&#8221; questions about.</dl>
<p> <code>$mhaltmsg</code></p>
<dl>
<dd><code>dist</code> and <code>repl</code> set <code>$mhaltmsg</code> to tell the <i>whatnowproc</i> about an alternate message associated with the draft (the message being distributed or replied to).</dl>
<p> <code>$mhfolder</code></p>
<dl>
<dd>This is the folder containing the alternate message. </p>
<p> This is set by <code>dist</code> and <code>repl</code> during edit sessions so you can peruse other messages in the current folder besides the one being distributed or replied to. The environment variable <code>$mhfolder</code> is also set by <code>show</code>, <code>prev</code>, and <code>next</code> for use by <code>mhl</code>.</dl>
<p> <code>$mhdist</code></p>
<dl>
<dd><code>dist</code> sets <code>$mhdist</code> to tell the <i>whatnowproc</i> that message re-distribution is occurring.</dl>
<p> <code>$mheditor</code></p>
<dl>
<dd>This is set by <code>comp</code>, <code>repl</code>, <code>forw</code>, and <code>dist</code> to tell the <i>whatnowproc</i> the user&#8217;s choice of editor (unless overridden by <code>-noedit</code>).</dl>
<p> <code>$mhuse</code></p>
<dl>
<dd>This may be set by <code>comp</code>.</dl>
<p> <code>$mhmessages</code></p>
<dl>
<dd>This is set by <code>dist</code>, <code>forw</code>, and <code>repl</code> if annotations are to occur.</dl>
<p> <code>$mhannotate</code></p>
<dl>
<dd>This is set by <code>dist</code>, <code>forw</code>, and <code>repl</code> if annotations are to occur.</dl>
<p> <code>$mhinplace</code></p>
<dl>
<dd>This is set by <code>dist</code>, <code>forw</code>, and <code>repl</code> if annotations are to occur.</dl>
<h2>Files</h2>
<pre>^$HOME/.mh_profile~^The user profile
^or $MH~^Rather than the standard profile
^&lt;mh-dir&gt;/context~^The user context
^or $MHCONTEXT~^Rather than the standard context
^&lt;folder&gt;/.mh_sequences~^Public sequences for &lt;folder&gt;</pre>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-environ/">environ</a></i>(5), <i><a href="/docs/linux/man/5-mh-sequence/">mh-sequence</a></i>(5), <i><a href="/docs/linux/man/7-nmh/">nmh</a></i>(7)</p>
<h2>History</h2>
<p>The <i>.mh_profile</i> contains only static information, which <code>nmh</code> programs will <code>NOT</code> update. Changes in context are made to the <i>context</i> file kept in the users <code>nmh</code> directory. This includes, but is not limited to: the &#8220;Current-Folder&#8221; entry and all private sequence information. Public sequence information is kept in each folder in the file determined by the &#8220;mh-sequences&#8221; profile entry (default is <i>.mh_sequences</i>). </p>
<p> The <i>.mh_profile</i> may override the path of the <i>context</i> file, by specifying a &#8220;context&#8221; entry (this must be in lower-case). If the entry is not absolute (does not start with a &#8220;/&#8221;), then it is interpreted relative to the user&#8217;s <code>nmh</code> directory. As a result, you can actually have more than one set of private sequences by using different context files.</p>
<h2>Bugs</h2>
<p>There is some question as to what kind of arguments should be placed in the profile as options. In order to provide a clear answer, recall command line semantics of all <code>nmh</code> programs: conflicting switches (e.g. <code>-header</code> and <code>-noheader</code>) may occur more than one time on the command line, with the last switch taking effect. Other arguments, such as message sequences, filenames and folders, are always remembered on the invocation line and are not superseded by following arguments of the same type. Hence, it is safe to place only switches (and their arguments) in the profile. If one finds that an <code>nmh</code> program is being invoked again and again with the same arguments, and those arguments aren&#8217;t switches, then there are a few possible solutions to this problem. The first is to create a (soft) link in your <i>$HOME/bin</i> directory to the <code>nmh</code> program of your choice. By giving this link a different name, you can create a new entry in your profile and use an alternate set of defaults for the <code>nmh</code> command. Similarly, you could create a small shell script which called the <code>nmh</code> program of your choice with an alternate set of invocation line switches (using links and an alternate profile entry is preferable to this solution). Finally, the <code>csh</code> user could create an alias for the command of the form:</p>
<dl>
<dd>alias cmd &#8216;cmd arg1 arg2 &#8230;&#8217;</dl>
<p> In this way, the user can avoid lengthy type-in to the shell, and still give <code>nmh</code> commands safely. (Recall that some <code>nmh</code> commands invoke others, and that in all cases, the profile is read, meaning that aliases are disregarded beyond an initial command invocation) </p>
