---
title: "alpine(1)"
name: "alpine"
section: "1"
letter: "a"
url: "/docs/linux/man/1-alpine/"
description: "alpine – an Alternatively Licensed Program for Internet News and Email"
---

<h2>NAME</h2>
<p> alpine &#8211; an Alternatively Licensed Program for Internet News and Email</p>
<h2>SYNTAX</h2>
<p> <code>alpine</code> [ <i>options</i> ] [ <i>address</i> , <i>address</i> ] </p>
<p> <code>alpinef</code> [ <i>options</i> ] [ <i>address</i> , <i>address</i> ]</p>
<h2>DESCRIPTION</h2>
<p> Alpine is a screen-oriented message-handling tool. In its default configuration, Alpine offers an intentionally limited set of functions geared toward the novice user, but it also has a large list of optional &quot;power-user&quot; and personal-preference features. <i>alpinef </i> is a variant of Alpine that uses function keys rather than mnemonic single-letter commands. Alpine&#8217;s basic feature set includes:</p>
<dl>
<dt>
</dt><dd> View, Save, Export, Delete, Print, Reply and Forward messages.</dd>
<dt>
</dt><dd> Compose messages in a simple editor (Pico) with word-wrap and a spelling checker. Messages may be postponed for later completion.</dd>
<dt>
</dt><dd> Full-screen selection and management of message folders.</dd>
<dt>
</dt><dd> Address book to keep a list of long or frequently-used addresses. Personal distribution lists may be defined. Addresses may be taken into the address book from incoming mail without retyping them.</dd>
<dt>
</dt><dd> New mail checking and notification occurs automatically every 2.5 minutes and after certain commands, e.g. refresh-screen (Ctrl-L).</dd>
<dt>
</dt><dd> On-line, context-sensitive help screens.</dd></dl>
<p> Alpine supports MIME (Multipurpose Internet Mail Extensions), an Internet Standard for representing multipart and multimedia data in email. Alpine allows you to save MIME objects to files, and in some cases, can also initiate the correct program for viewing the object. It uses the system&#8217;s <i>mailcap </i> configuration file to determine what program can process a particular MIME object type. Alpine&#8217;s message composer does not have integral multimedia capability, but any type of data file &#8211;including multimedia&#8211; can be attached to a text message and sent using MIME&#8217;s encoding rules. This allows any group of individuals with MIME-capable mail software (e.g. Alpine, PC-Alpine, or many other programs) to exchange formatted documents, spread-sheets, image files, etc, via Internet email. </p>
<p> Alpine uses the <i>c-client</i> messaging API to access local and remote mail folders. This library provides a variety of low-level message-handling functions, including drivers for a variety of different mail file formats, as well as routines to access remote mail and news servers, using IMAP (Internet Message Access Protocol) and NNTP (Network News Transport Protocol). Outgoing mail is usually posted directly via SMTP (Simple Mail Transfer Protocol).</p>
<h2>OPTIONS</h2>
<p> The command line options/arguments are:</p>
<dl>
<dt><i>address</i></dt>
<dd> Send mail to <i>address.</i> This will cause Alpine to go directly into the message composer.</dd>
<dt><code>-attach&nbsp;<wbr></code><i>file</i></dt>
<dd> Send mail with the listed <i>file</i> as an attachment.</dd>
<dt><code>-attachlist&nbsp;<wbr></code><i>file-list</i></dt>
<dd> Send mail with the listed <i>file-list</i> as an attachments.</dd>
<dt><code>-attach_and_delete&nbsp;<wbr></code><i>file</i></dt>
<dd> Send mail with the listed <i>file</i> as an attachment, and remove the file after the message is sent.</dd>
<dt><code>-aux&nbsp;<wbr></code><i>local_directory</i></dt>
<dd> PC-Alpine only. When using a remote configuration (-p &lt;remote_config&gt;) this tells PC-Alpine the local directory to use for storing auxiliary files, like debug files, address books, and signature files.</dd>
<dt><code>-bail</code></dt>
<dd> Exit if the pinerc file does not exist. This might be useful if the config file is accessed using some remote filesystem protocol. If the remote mount is missing this will cause Alpine to quit instead of creating a new pinerc.</dd>
<dt><code>-c&nbsp;<wbr></code><i>context-number</i></dt>
<dd> context-number is the number corresponding to the folder-collection to which the <i>-f</i> command line argument should be applied. By default the <i>-f</i> argument is applied to the first defined folder-collection.</dd>
<dt><code>-conf</code></dt>
<dd> Produce a sample/fresh copy of the system-wide configuration file, <i>pine.conf,</i> on the standard output. This is distinct from the per-user <i>.pinerc</i> file.</dd>
<dt><code>-convert_sigs&nbsp;<wbr></code><i>-p pinerc</i></dt>
<dd> Convert signature files into literal signatures.</dd>
<dt><code>-copy_abook&nbsp;<wbr>&lt;</code><i>local_abook</i>&gt;&nbsp;<wbr>&lt;<i>remote_abook</i>&gt;</dt>
<dd> Copy the local address book file to a remote address book folder.</dd>
<dt><code>-copy_pinerc&nbsp;<wbr>&lt;</code><i>local_pinerc</i>&gt;&nbsp;<wbr>&lt;<i>remote_pinerc</i>&gt;</dt>
<dd> Copy the local pinerc file to a remote pinerc folder.</dd>
<dt><code>-d&nbsp;<wbr></code><i>debug-level</i></dt>
<dd> Output diagnostic info at <i>debug-level</i> (0-9) to the current <i>.pine-debug[1-4]</i> file. A value of 0 turns debugging off and suppresses the <i>.pine-debug</i> file.</dd>
<dt><code>-d&nbsp;<wbr></code><i>key[=val]</i></dt>
<dd> Fine tuned output of diagnostic messages where &quot;flush&quot; causes debug file writing without buffering, &quot;timestamp&quot; appends each message with a timestamp, &quot;imap=n&quot; where n is between 0 and 4 representing none to verbose IMAP telemetry reporting, &quot;numfiles=n&quot; where n is between 0 and 31 corresponding to the number of debug files to maintain, and &quot;verbose=n&quot; where n is between 0 and 9 indicating an inverse threshold for message output.</dd>
<dt><code>-f&nbsp;<wbr></code><i>folder</i></dt>
<dd> Open <i>folder </i> (in first defined folder collection, use <i>-c n</i> to specify another collection) instead of INBOX.</dd>
<dt><code>-F&nbsp;<wbr></code><i>file</i></dt>
<dd> Open named text file and view with Alpine&#8217;s browser.</dd>
<dt><code>-h</code></dt>
<dd> Help: list valid command-line options.</dd>
<dt><code>-i</code></dt>
<dd> Start up in the FOLDER INDEX screen.</dd>
<dt><code>-I&nbsp;<wbr></code><i>keystrokes</i></dt>
<dd> Initial (comma separated list of) keystrokes which Alpine should execute on startup.</dd>
<dt><code>-install</code></dt>
<dd> For PC-Alpine only, this option causes PC-Alpine to prompt for some basic setup information, then exits.</dd>
<dt><code>-k</code></dt>
<dd> Use function keys for commands. This is the same as running the command <i>alpinef</i>.</dd>
<dt><code>-n&nbsp;<wbr></code><i>number</i></dt>
<dd> Start up with current message-number set to <i>number.</i></dd>
<dt><code>-noutf8</code></dt>
<dd> Warns Alpine that piped input is not encoded in UTF-8.</dd>
<dt><code>-o</code></dt>
<dd> Open first folder read-only.</dd>
<dt><code>-p&nbsp;<wbr></code><i>config-file</i></dt>
<dd> Use <i>config-file</i> as the personal configuration file instead of the default <i>.pinerc</i>.</dd>
<dt><code>-P&nbsp;<wbr></code><i>config-file</i></dt>
<dd> Use <i>config-file</i> as the configuration file instead of default system-wide configuration file <i>pine.conf</i>.</dd>
<dt><code>-pinerc&nbsp;<wbr></code><i>file</i></dt>
<dd> Output fresh pinerc configuration to <i>file, preserving the settings of variables that the user has made.</i> Use <i>file</i> set to &#8220;-&#8221; to make output go to standard out. &lt;IP&gt; <code>-registry&nbsp;<wbr></code><i>cmd</i> 20 For PC-Alpine only, this option affects the values of Alpine&#8217;s registry entries. Possible values for <i>cmd</i> are set, clear, and dump. <i>Set</i> will always reset Alpine&#8217;s registry entries according to its current settings. <i>Clear</i> will clear the registry values. <i>Clearsilent</i> will silently clear the registry values. <i>Dump</i> will display the values of current registry settings. Note that the dump command is currently disabled. Without the -registry option, PC-Alpine will write values into the registry only if there currently aren&#8217;t any values set.</dd>
<dt><code>-r</code></dt>
<dd> Use restricted/demo mode. <i>Alpine</i> will only send mail to itself and functions like save and export are restricted.</dd>
<dt><code>-sort&nbsp;<wbr></code><i>order</i></dt>
<dd> Sort the FOLDER INDEX display in one of the following orders: <i>arrival, date, subject, orderedsubj, thread, from, size, score, to, cc,</i> or <i>reverse. Arrival </i> order is the default. The OrderedSubj choice simulates a threaded sort. Any sort may be reversed by adding <i>/reverse</i> to it. <i>Reverse</i> by itself is the same as <i>arrival/reverse</i>.</dd>
<dt><code>-supported</code></dt>
<dd> Some options may or may not be supported depending on how Alpine was compiled. This is a way to determine which options are supported in the particular copy of Alpine you are using.</dd>
<dt><code>-uninstall</code></dt>
<dd> For PC-Alpine only, this option causes PC-Alpine to remove references to Alpine in Windows settings.</dd>
<dt><code>-url&nbsp;<wbr></code><i>url</i></dt>
<dd> Open the given <i>url.</i> Cannot be used with <i>-f</i> or <i>-F</i> options.</dd>
<dt><code>-v</code></dt>
<dd> Version: Print version information.</dd>
<dt><code>-version</code></dt>
<dd> Version: Print version information.</dd>
<dt><code>-x&nbsp;<wbr></code><i>config</i></dt>
<dd> Use configuration exceptions in <i>config.</i> Exceptions are used to override your default pinerc settings for a particular platform, can be a local file or a remote folder.</dd>
<dt><code>-z</code></dt>
<dd> Enable ^Z and SIGTSTP so alpine may be suspended.</dd>
<dt><i>-option=value</i></dt>
<dd> Assign <i>value</i> to the config option <i>option</i> e.g. -signature-file=sig1 or -feature-list=signature-at-bottom (Note: feature-list values are additive)</dd></dl>
<h2>CONFIGURATION</h2>
<p> There are several levels of Alpine configuration. Configuration values at a given level over-ride corresponding values at lower levels. In order of increasing precedence: </p>
<p>&nbsp;<wbr>o built-in defaults. </p>
<p>&nbsp;<wbr>o system-wide&nbsp;<wbr> <i>pine.conf </i> file. </p>
<p>&nbsp;<wbr>o personal&nbsp;<wbr> <i>.pinerc </i> file (may be set via built-in Setup/Config menu.) </p>
<p>&nbsp;<wbr>o command-line options. </p>
<p>&nbsp;<wbr>o system-wide&nbsp;<wbr> <i>pine.conf.fixed </i> file. </p>
<p> There is one exception to the rule that configuration values are replaced by the value of the same option in a higher-precedence file: the feature-list variable has values that are additive, but can be negated by prepending &quot;no-&quot; in front of an individual feature name. Unix Alpine also uses the following environment variables: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>TERM </p>
<p>&nbsp;<wbr>&nbsp;<wbr>DISPLAY&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(determines if Alpine can display IMAGE attachments.) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>SHELL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(if not set, default is&nbsp;<wbr>/bin/sh&nbsp;<wbr>) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>MAILCAPS&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(semicolon delimited list of path names to mailcap files)</p>
<h2>FILES</h2>
<p> /usr/spool/mail/xxxx<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Default folder for incoming mail.</p>
<p> ~/mail<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Default directory for mail folders.</p>
<p> ~/.addressbook<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Default address book file.</p>
<p> ~/.pine-debug[1-4]<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Diagnostic log for debugging.</p>
<p> ~/.pinerc<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Personal alpine config file.</p>
<p> ~/.pine-crash<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Debug information useful to debug a crash.</p>
<p> ~/.newsrc<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>News subscription/state file.</p>
<p> ~/.mailcap<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Personal mail capabilities file.</p>
<p> ~/.mime.types<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Personal file extension to MIME type mapping</p>
<p> /etc/mailcap<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>System-wide mail capabilities file.</p>
<p> /etc/mime.types<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>System-wide file ext. to MIME type mapping</p>
<p> /usr/local/lib/pine.info<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Local pointer to system administrator.</p>
<p> /usr/local/lib/pine.conf<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>System-wide configuration file.</p>
<p> /usr/local/lib/pine.conf.fixed Non-overridable configuration file.</p>
<p> /tmp/.\usr\spool\mail\xxxx <code>&nbsp;<wbr></code>Per-folder mailbox lock files.<br />
 <br />
 ~/.pine-interrupted-mail <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>Message which was interrupted.<br />
 <br />
 ~/mail/postponed-msgs <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>For postponed messages.<br />
 <br />
 ~/mail/sent-mail <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>Outgoing message archive (FCC).<br />
 <br />
 ~/mail/saved-messages <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code>Default destination for Saving messages.<br />
  </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pico/">pico</a>(1), <a href="/docs/linux/man/1-binmail/">binmail</a>(1), <a href="/docs/linux/man/5-aliases/">aliases</a>(5), <a href="/docs/linux/man/7-mailaddr/">mailaddr</a>(7), <a href="/docs/linux/man/8-sendmail/">sendmail</a>(8), <a href="/docs/linux/man/1-spell/">spell</a>(1), <a href="/docs/linux/man/8-imapd/">imapd</a>(8) </p>
<p> <br />
 Newsgroup: comp.mail.pine </p>
<p> <br />
 Mailing List: <br />
 Alpine-info, at <a rel="nofollow" href="https://www.washington.edu/alpine/alpine-info/">https://www.washington.edu/alpine/alpine-info/</a> </p>
<p> <br />
 Main Alpine distribution site: <br />
 <a rel="nofollow" href="http://patches.freeiz.com/alpine/release/">http://patches.freeiz.com/alpine/release/</a> </p>
<p> <br />
 Alpine Technical Notes, included in the source distribution. </p>
<p> <br />
 C-Client messaging API library, included in the source distribution.  </p>
<h2>ACKNOWLEDGMENTS</h2>
<pre><code>This software is the result of the contribution of many individuals
who have dedicated their time to support, improve and suggest ways
to improve Alpine through the years. This software would not be
possible without the support of the University of Washington in
Seattle, Washington. The Alpine community extends its most sincere
thanks to all contributors and invites everyone to join in and
contribute to this project.
</code></pre>
<h2>Index</h2>
