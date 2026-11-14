---
title: "sieve-filter(1)"
name: "sieve-filter"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sieve-filter/"
description: "sieve-filter – Pigeonhole’s Sieve mailbox filter tool"
---

<h2>NAME</h2>
<p> sieve-filter &#8211; Pigeonhole&#8217;s Sieve mailbox filter tool </p>
<p> <code>WARNING: </code>This tool is still experimental. Read this manual carefully, and backup any important mail before using this tool. Also note that some of the features documented here are not actually implemented yet; this is clearly indicated where applicable.</p>
<h2>SYNOPSIS</h2>
<p> <code>sieve-filter</code> [<i>options</i>] <i>script-file</i> <i>source-mailbox</i> [<i>discard-action</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>sieve-filter</code> command is part of the Pigeonhole Project (<code><a href="/docs/linux/man/7-pigeonhole/">pigeonhole</a></code>(7)), which adds Sieve (RFC 5228) support to the Dovecot secure IMAP and POP3 server (<code><a href="/docs/linux/man/1-dovecot/">dovecot</a></code>(1)). </p>
<p> The Sieve language was originally meant for filtering messages upon delivery. However, there are occasions when it is desirable to filter messages that are already stored in a mailbox, for instance when a bug in a Sieve script caused many messages to be delivered incorrectly. Using the sieve-filter tool it is possible to apply a Sieve script on all messages in a particular <i>source-mailbox</i>, making it possible to delete messages, to store them in a different mailbox, to change their content, and to change the assigned IMAP flags and keywords. Attempts to send messages to the outside world are ignored by default for obvious reasons, but, using the proper command line options, it is possible to capture and handle outgoing mail as well. </p>
<p> If no options are specified, the sieve-filter command runs in a simulation mode in which it only prints what would be performed, without actually doing anything. Use the <code>-e</code> option to activate true script execution. Also, the <i>source-mailbox</i> is opened read-only by default, meaning that it normally always remains unchanged. Use the <code>-W</code> option to allow changes in the <i>source-mailbox</i>. </p>
<p> Even with the <code>-W</code> option enabled, messages in the <i>source-mailbox</i> are only potentially modified or moved to a different folder. Messages are never lost unless a <i>discard-action</i> argument other than <code>keep</code> (the default) is specified. If the Sieve filter decides to store the message in the <i>source-mailbox</i>, where it obviously already exists, it is never duplicated there. In that case, the IMAP flags of the original message can be modified by the Sieve interpreter using the <i>imap4flags</i> extension, provided that <code>-W</code> is specified. If the message itself is modified by the Sieve interpreter (e.g. using the <i>editheader</i> extension), a new message is stored and the old one is expunged. However, if <code>-W</code> is omitted, the original message is left untouched and the modifications are discarded. </p>
<h3>CAUTION</h3>
<p> Although this is a very useful tool, it can also be very destructive when used improperly. A small bug in your Sieve script in combination with the wrong command line options could cause it to discard the wrong e-mails. And, even if the <i>source-mailbox</i> is opened in read-only mode to prevent such mishaps, it can still litter other mailboxes with spurious copies of your e-mails if your Sieve script decides to do so. Therefore, users are advised to read this manual carefully and to use the simulation mode first to check what the script will do. And, of course: </p>
<p> <code>MAKING A BACKUP IS IMPERATIVE FOR ANY IMPORTANT MAIL!</code> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c&nbsp;<wbr></code><i>config-file</i></p>
<dd> Alternative Dovecot configuration file path.</p>
<dt><code>-C</code></p>
<dd> Force compilation. By default, the compiled binary is stored on disk. When this binary is found during the next execution of <code>sieve-filter</code> and its modification time is more recent than the script file, it is used and the script is not compiled again. This option forces the script to be compiled, thus ignoring any present binary. Refer to <code><a href="/docs/linux/man/1-sievec/">sievec</a></code>(1) for more information about Sieve compilation.</p>
<dt><code>-D</code></p>
<dd> Enable Sieve debugging.</p>
<dt><code>-e</code></p>
<dd> Turns on execution mode. By default, the sieve-filter command runs in simulation mode in which it changes nothing, meaning that no mailbox is altered in any way and no actions are performed. It only prints what would be done. Using this option, the sieve-filter command becomes active and performs the requested actions.</p>
<dt><code>-m&nbsp;<wbr></code><i>default-mailbox</i></p>
<dd> The mailbox where the (implicit) <code>keep</code> Sieve action stores messages. This is equal to the <i>source-mailbox</i> by default. Specifying a different folder will have the effect of moving (or copying if <code>-W</code> is omitted) all kept messages to the indicated folder, instead of just leaving them in the <i>source-mailbox</i>. Refer to the explanation of the <i>source-mailbox</i> argument for more information on mailbox naming.</p>
<dt><code>-q&nbsp;<wbr></code><i>output-mailbox&nbsp;<wbr></i><code>[not implemented yet]</code></p>
<dd> Store outgoing e-mail into the indicated <i>output-mailbox</i>. By default, the sieve-filter command ignores Sieve actions such as redirect, reject, vacation and notify, but using this option outgoing messages can be appended to the indicated mailbox. This option has no effect in simulation mode. Flags of redirected messages are not preserved.</p>
<dt><code>-Q&nbsp;<wbr></code><i>mail-command&nbsp;<wbr></i><code>[not implemented yet]</code></p>
<dd> Send outgoing e-mail (e.g. as produced by redirect, reject and vacation) through the specified program. By default, the sieve-filter command ignores Sieve actions such as redirect, reject, vacation and notify, but using this option outgoing messages can be fed to the <code>stdin</code> of an external shell command. This option has no effect in simulation mode. Unless you really know what you are doing, <code>DO NOT USE THIS TO FEED MAIL TO SENDMAIL!</code>.</p>
<dt><code>-s&nbsp;<wbr></code><i>script-file&nbsp;<wbr></i><code>[not implemented yet]</code></p>
<dd> Specify additional scripts to be executed before the main script. Multiple <code>-s</code> arguments are allowed and the specified scripts are executed sequentially in the order specified at the command line.</p>
<dt><code>-u&nbsp;<wbr></code><i>user</i></p>
<dd> Run the Sieve script for the given <i>user</i>.</p>
<dt><code>-v</code></p>
<dd> Produce verbose output during filtering.</p>
<dt><code>-W</code></p>
<dd> Enables write access to the <i>source-mailbox</i>. This allows (re)moving the messages from the <i>source-mailbox</i>, changing their contents, and changing the assigned IMAP flags and keywords.</p>
<dt><code>-x&nbsp;<wbr></code><i>extensions</i></p>
<dd> Set the available extensions. The parameter is a space-separated list of the active extensions. By prepending the extension identifiers with <code>+</code> or <code>&#8211;</code>, extensions can be included or excluded relative to the configured set of active extensions. If no extensions have a <code>+</code> or <code>&#8211;</code> prefix, only those extensions that are explicitly listed will be enabled. Unknown extensions are ignored and a warning is produced. </p>
<p> For example <code>-x</code> &quot;+imapflags -enotify&quot; will enable the deprecated imapflags extension and disable the enotify extension. The rest of the active extensions depends on the <i>sieve_extensions</i> and <i>sieve_global_extensions</i> settings. By default, i.e. when <i>sieve_extensions</i> and <i>sieve_global_extensions</i> remain unconfigured, all supported extensions are available, except for deprecated extensions or those that are still under development. </p>
</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>script-file</i></p>
<dd> Specifies the Sieve script to (compile and) execute. </p>
<p> Note that this tool looks for a pre-compiled binary file with a <i>.svbin</i> extension and with basename and path identical to the specified script. Use the <code>-C</code> option to disable this behavior by forcing the script to be compiled into a new binary.</p>
<dt><i>source-mailbox</i></p>
<dd> Specifies the source mailbox containing the messages that the Sieve filter will act upon. </p>
<p> This is the name of a mailbox, as visible to IMAP clients, except in UTF-8 format. The hierarchy separator between a parent and child mailbox is commonly &#8216;<code>/</code>&#8216; or &#8216;<code>.</code>&#8216;, but this depends on your selected mailbox storage format and namespace configuration. The mailbox names may also require a namespace prefix. </p>
<p> This mailbox is not modified unless the <code>-W</code> option is specified.</p>
<dt><i>discard-action</i></p>
<dd> Specifies what is done with messages in the <i>source-mailbox</i> that where not kept or otherwise stored by the Sieve script; i.e. those messages that would normally be discarded if the Sieve script were executed at delivery. The <i>discard-action</i> parameter accepts one of the following values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>keep&nbsp;<wbr></code>(default)</p>
<dd> Keep discarded messages in source mailbox.</p>
<dt><code>move&nbsp;<wbr></code><i>mailbox</i></p>
<dd> Move discarded messages to the indicated <i>mailbox</i>. This is for instance useful to move messages to a Trash mailbox. Refer to the explanation of the <i>source-mailbox</i> argument for more information on mailbox naming.</p>
<dt><code>delete</code></p>
<dd> Flag discarded messages as \DELETED.</p>
<dt><code>expunge</code></p>
<dd> Expunge discarded messages, meaning that these are removed irreversibly when the tool finishes filtering.</dl>
</dl>
<dt>
<dd> When the <code>-W</code> option is not specified, the <i>source-mailbox</i> is immutable and the specified <i>discard-action</i> has no effect. This means that messages are at most <i>copied</i> to a new location. In contrast, when the <code>-W</code> is specified, messages that are successfully stored somewhere else by the Sieve script are <code>always</code> expunged from the <i>source-mailbox</i>, with the effect that these are thus <i>moved</i> to the new location. This happens irrespective of the specified <i>discard-action</i>. Remember: only discarded messages are affected by the specified <i>discard-action</i>. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>[&#8230;]</p>
<dd>
</dl>
<h2>EXIT STATUS</h2>
<p> <code>sieve-filter</code> will exit with one of the following values:</p>
<dl>
<dt><code>0</code></p>
<dd> Sieve filter applied successfully. (EX_OK, EXIT_SUCCESS)</p>
<dt><code>1</code></p>
<dd> Operation failed. This is returned for almost all failures. (EXIT_FAILURE)</p>
<dt><code>64</code></p>
<dd> Invalid parameter given. (EX_USAGE)</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/dovecot/dovecot.conf</i></p>
<dd> Dovecot&#8217;s main configuration file.</p>
<dt><i>/etc/dovecot/conf.d/90-sieve.conf</i></p>
<dd> Sieve interpreter settings (included from Dovecot&#8217;s main configuration file)</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting Dovecot and Pigeonhole bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dovecot/">dovecot</a></code>(1), <code><a href="/docs/linux/man/1-dovecot-lda/">dovecot-lda</a></code>(1), <code><a href="/docs/linux/man/1-sieve-dump/">sieve-dump</a></code>(1), <code><a href="/docs/linux/man/1-sieve-test/">sieve-test</a></code>(1), <code><a href="/docs/linux/man/1-sievec/">sievec</a></code>(1), <code><a href="/docs/linux/man/7-pigeonhole/">pigeonhole</a></code>(7) </p>
<h2>Index</h2>
