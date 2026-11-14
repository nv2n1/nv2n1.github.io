---
title: "procmail(1)"
name: "procmail"
section: "1"
letter: "p"
url: "/docs/linux/man/1-procmail/"
description: "procmail – autonomous mail processor"
---

<h2 class="name">NAME</h2>
<p> procmail &#8211; autonomous mail processor </p>
<h2>SYNOPSIS</h2>
<p> <code>procmail</code> [<code>-ptoY</code>] [<code>-f </code><i>fromwhom</i>]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; [<i>parameter</i><code>=</code>value |<i> rcfile</i>] &#8230;<br />
 <code>procmail</code> [<code>-toY</code>] [<code>-f </code><i>fromwhom</i>] [<code>-a </code><i>argument</i>] &#8230;<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; <code>-d</code> <i>recipient</i> &#8230;<br />
 <code>procmail</code> [<code>-ptY</code>] <code>-m</code> [<i>parameter</i><code>=</code>value] &#8230; <i>rcfile</i><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; [<i>argument</i>] &#8230;<br />
 <code>procmail</code> <code>-v</code> </p>
<h2>DESCRIPTION</h2>
<p> For a quick start, see <code>NOTES</code> at the end. </p>
<p> <code>Procmail</code> should be invoked automatically over the <code>.forward</code> file mechanism as soon as mail arrives. Alternatively, when installed by a system administrator, it can be invoked from within the mailer immediately. When invoked, it first sets some environment variables to default values, reads the mail message from stdin until an EOF, separates the body from the header, and then, if no command line arguments are present, it starts to look for a file named <code>$HOME/.procmailrc</code>. According to the processing recipes in this file, the mail message that just arrived gets distributed into the right folder (and more). If no rcfile is found, or processing of the rcfile falls off the end, procmail will store the mail in the default system mailbox. </p>
<p> If no rcfiles and no <code>-p</code> have been specified on the command line, procmail will, prior to reading $HOME/.procmailrc, interpret commands from <code>/etc/procmailrc</code> (if present). Care must be taken when creating /etc/procmailrc, because, if circumstances permit, it will be executed with root privileges (contrary to the $HOME/.procmailrc file of course). </p>
<p> If running suid root or with root privileges, procmail will be able to perform as a functionally enhanced, backwards compatible mail delivery agent. </p>
<p> Procmail can also be used as a general purpose mail filter, i.e., provisions have been made to enable procmail to be invoked in a special sendmail rule. </p>
<p> The rcfile format is described in detail in the <code><a href="/docs/linux/man/5-procmailrc/">procmailrc</a></code>(5) man page. </p>
<p> The weighted scoring technique is described in detail in the <code><a href="/docs/linux/man/5-procmailsc/">procmailsc</a></code>(5) man page. </p>
<p> Examples for rcfile recipes can be looked up in the <code><a href="/docs/linux/man/5-procmailex/">procmailex</a></code>(5) man page. </p>
<h3>Signals</h3>
<p> Tp 1.2i <code>TERMINATE</code> Terminate prematurely and requeue the mail.<br />
 Tp <code>HANGUP</code> Terminate prematurely and bounce the mail.<br />
 Tp <code>INTERRUPT</code> Terminate prematurely and bounce the mail.<br />
 Tp <code>QUIT</code> Terminate prematurely and silently lose the mail.<br />
 Tp <code>ALARM</code> Force a timeout (see <code>TIMEOUT).</code><br />
 Tp <code>USR1</code> Equivalent to a <code>VERBOSE</code>=off.<br />
 Tp <code>USR2</code> Equivalent to a <code>VERBOSE</code>=on. </p>
<h2>OPTIONS</h2>
<p> Tp 0.5i <code>-v</code> Procmail will print its version number, display its compile time configuration and exit.<br />
 Tp <code>-p</code> Preserve any old environment. Normally procmail clears the environment upon startup, except for the value of TZ. However, in any case: any default values will override any preexisting environment variables, i.e., procmail will not pay any attention to any predefined environment variables, it will happily overwrite them with its own defaults. For the list of environment variables that procmail will preset see the <code><a href="/docs/linux/man/5-procmailrc/">procmailrc</a></code>(5) man page. If both -p and -m are specified, the list of preset environment variables shrinks to just: LOGNAME, HOME, SHELL, ORGMAIL and MAILDIR.<br />
 Tp <code>-t</code> Make procmail fail softly, i.e., if procmail cannot deliver the mail to any of the destinations you gave, the mail will not bounce, but will return to the mailqueue. Another delivery-attempt will be made at some time in the future.<br />
 Tp <i></i><code>-f</code> fromwhom Causes procmail to regenerate the leading `From &#8216; line with <i>fromwhom</i> as the sender (instead of -f one could use the alternate and obsolete -r). If <i>fromwhom</i> consists merely of a single `-&#8216;, then procmail will only update the timestamp on the `From &#8216; line (if present, if not, it will generate a new one).<br />
 Tp <code>-o</code> Instead of allowing anyone to generate `From &#8216; lines, simply override the fakes.<br />
 Tp <code>-Y</code> Assume traditional Berkeley mailbox format, ignore any <code>Content-Length:</code> fields.<br />
 Tp <i></i><code>-a</code> argument This will set $1 to be equal to <i>argument</i>. Each succeeding <i></i><code>-a</code> argument will set the next number variable ($2, $3, etc). It can be used to pass meta information along to procmail. This is typically done by passing along the $@x information from the sendmail mailer rule.<br />
 Tp <i></i><code>-d</code> recipient &#8230; This turns on explicit delivery mode, delivery will be to the local user <i>recipient</i>. This, of course, only is possible if procmail has root privileges (or if procmail is already running with the recipient&#8217;s euid and egid). Procmail will setuid to the intended recipients and delivers the mail as if it were invoked by the recipient with no arguments (i.e., if no rcfile is found, delivery is like ordinary mail). This option is incompatible with <code>-p</code>.<br />
 Tp <code>-m</code> Turns procmail into a general purpose mail filter. In this mode one rcfile must be specified on the command line. After the rcfile, procmail will accept an unlimited number of arguments. If the rcfile is an absolute path starting with <code>/etc/procmailrcs/</code> without backward references (i.e. the parent directory cannot be mentioned) procmail will, only if no security violations are found, take on the identity of the owner of the rcfile (or symbolic link). For some advanced usage of this option you should look in the <code>EXAMPLES</code> section below. </p>
<h2>ARGUMENTS</h2>
<p> Any arguments containing an &#8216;=&#8217; are considered to be environment variable assignments, they will <i>all</i> be evaluated after the default values have been assigned and before the first rcfile is opened. </p>
<p> Any other arguments are presumed to be rcfile paths (either absolute, or if they start with `./&#8217; relative to the current directory; <code>any other relative</code> path is relative to $HOME, unless the <code>-m</code> option has been given, in which case all relative paths are relative to the current directory); procmail will start with the first one it finds on the command line. The following ones will only be parsed if the preceding ones have a not matching HOST-directive entry, or in case they should not exist. </p>
<p> If no rcfiles are specified, it looks for <code>$HOME/.procmailrc</code>. If not even that can be found, processing will continue according to the default settings of the environment variables and the ones specified on the command line. </p>
<h2>EXAMPLES</h2>
<p> Examples for rcfile recipes can be looked up in the <code><a href="/docs/linux/man/5-procmailex/">procmailex</a></code>(5) man page. A small sample rcfile can be found in the <code>NOTES</code> section below. </p>
<p> Skip the rest of this EXAMPLES section unless you are a system administrator who is vaguely familiar with sendmail.cf syntax. </p>
<p> The <code>-m</code> option is typically used when procmail is called from within a rule in the sendmail.cf file. In order to be able to do this it is convenient to create an extra `procmail&#8217; mailer in your sendmail.cf file (in addition to the perhaps already present `local&#8217; mailer that starts up procmail). To create such a `procmail&#8217; mailer I&#8217;d suggest something like: </p>
<pre>
<dl><dt><dd>Mprocmail, P=/usr/bin/procmail, F=mSDFMhun, S=11, R=21,
        A=procmail -m $h $g $u
</dl>
</pre>
<p> This enables you to use rules like the following (most likely in ruleset 0) to filter mail through the procmail mailer (please note the leading tab to continue the rule, and the tab to separate the comments): </p>
<pre>
<dl><dt><dd>R$*&lt;@some.where&gt;$*
        $#procmail $@/etc/procmailrcs/some.rc $:$1@some.where.procmail$2
R$*&lt;@$*.procmail&gt;$*
        $1&lt;@$2&gt;$3       Already filtered, map back
</dl>
</pre>
<p> And /etc/procmailrcs/some.rc could be as simple as: </p>
<pre>
<dl><dt><dd>SENDER = &quot;&lt;$1&gt;&quot;                 # fix for empty sender addresses
SHIFT = 1                       # remove it from $@
:0                              # sink all junk mail
* ^Subject:.*junk
/dev/null
:0 w                            # pass along all other mail
! -oi -f &quot;$SENDER&quot; &quot;$@&quot;
</dl>
</pre>
<p> Do watch out when sending mail from within the /etc/procmailrcs/some.rc file, if you send mail to addresses which match the first rule again, you could be creating an endless mail loop. </p>
<h2>FILES</h2>
<p> Tp 2.3i <code>/etc/passwd</code> to set the recipient&#8217;s LOGNAME, HOME and SHELL variable defaults<br />
 Tp <code>/var/mail/$LOGNAME</code> system mailbox; both the system mailbox and the immediate directory it is in will be created every time procmail starts and either one is not present<br />
 Tp <code>/etc/procmailrc</code> initial global rcfile<br />
 Tp <code>/etc/procmailrcs/</code> special privileges path for rcfiles<br />
 Tp <code>$HOME/.procmailrc</code> default rcfile<br />
 Tp <code>/var/mail/$LOGNAME.lock</code> lockfile for the system mailbox (not automatically used by procmail, unless $DEFAULT equals /var/mail/$LOGNAME and procmail is delivering to $DEFAULT)<br />
 Tp <code>/usr/sbin/sendmail</code> default mail forwarder<br />
 Tp <code>_????`hostname`</code> temporary `unique&#8217; zero-length files created by procmail </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-procmailrc/">procmailrc</a></code>(5), <code><a href="/docs/linux/man/5-procmailsc/">procmailsc</a></code>(5), <code><a href="/docs/linux/man/5-procmailex/">procmailex</a></code>(5), <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), <code><a href="/docs/linux/man/1-csh/">csh</a></code>(1), <code><a href="/docs/linux/man/1-mail/">mail</a></code>(1), <code><a href="/docs/linux/man/1-mailx/">mailx</a></code>(1), <code><a href="/docs/linux/man/1-uucp/">uucp</a></code>(1), <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5), <code><a href="/docs/linux/man/8-sendmail/">sendmail</a></code>(8), <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1), <code><a href="/docs/linux/man/1-grep/">grep</a></code>(1), <code><a href="/docs/linux/man/1-biff/">biff</a></code>(1), <code><a href="/docs/linux/man/8-comsat/">comsat</a></code>(8), <code><a href="/docs/linux/man/1-lockfile/">lockfile</a></code>(1), <code><a href="/docs/linux/man/1-formail/">formail</a></code>(1), <code><a href="/docs/linux/man/1-cron/">cron</a></code>(1) </p>
<h2>DIAGNOSTICS</h2>
<p> Tp 2.3i Autoforwarding mailbox found The system mailbox had its suid or sgid bit set, procmail terminates with EX_NOUSER assuming that this mailbox must not be delivered to.<br />
 Tp Bad substitution of &quot;x&quot; Not a valid environment variable name specified.<br />
 Tp Closing brace unexpected There was no corresponding opening brace (nesting block).<br />
 Tp Conflicting options Not all option combinations are useful<br />
 Tp Conflicting x suppressed Flag x is not compatible with some other flag on this recipe.<br />
 Tp Couldn&#8217;t create &quot;x&quot; The system mailbox was missing and could not/will not be created.<br />
 Tp Couldn&#8217;t create maildir part &quot;x&quot; The maildir folder &quot;x&quot; is missing one or more required subdirectories and procmail could not create them.<br />
 Tp Couldn&#8217;t create or rename temp file &quot;x&quot; An error occurred in the mechanics of delivering to the directory folder &quot;x&quot;.<br />
 Tp Couldn&#8217;t determine implicit lockfile from &quot;x&quot; There were no `&gt;&gt;&#8217; redirectors to be found, using simply `$LOCKEXT&#8217; as locallockfile.<br />
 Tp Couldn&#8217;t read &quot;x&quot; Procmail was unable to open an rcfile or it was not a regular file, or procmail couldn&#8217;t open an MH directory to find the highest numbered file.<br />
 Tp Couldn&#8217;t unlock &quot;x&quot; Lockfile was already gone, or write permission to the directory where the lockfile is has been denied.<br />
 Tp Deadlock attempted on &quot;x&quot; The locallockfile specified on this recipe is equal to a still active $LOCKFILE.<br />
 Tp Denying special privileges for &quot;x&quot; Procmail will not take on the identity that comes with the rcfile because a security violation was found (e.g. <code>-p</code> or variable assignments on the command line) or procmail had insufficient privileges to do so.<br />
 Tp Descriptor &quot;x&quot; was not open As procmail was started, stdin, stdout or stderr was not connected (possibly an attempt to subvert security)<br />
 Tp Enforcing stricter permissions on &quot;x&quot; The system mailbox of the recipient was found to be unsecured, procmail secured it.<br />
 Tp Error while writing to &quot;x&quot; Nonexistent subdirectory, no write permission, pipe died or disk full.<br />
 Tp Exceeded LINEBUF Buffer overflow detected, LINEBUF was too small, PROCMAIL_OVERFLOW has been set.<br />
 Tp MAILDIR is not an absolute path<br />
 Tp MAILDIR path too long<br />
 Tp ORGMAIL is not an absolute path<br />
 Tp ORGMAIL path too long<br />
 Tp default rcfile is not an absolute path<br />
 Tp default rcfile path too long The specified item&#8217;s full path, when expanded, was longer than LINEBUF or didn&#8217;t start with a file separator.<br />
 Tp Excessive output quenched from &quot;x&quot; The program or filter &quot;x&quot; tried to produce too much output for the current LINEBUF, the rest was discarded and PROCMAIL_OVERFLOW has been set.<br />
 Tp Extraneous x ignored The action line or other flags on this recipe makes flag x meaningless.<br />
 Tp Failed forking &quot;x&quot; Process table is full (and NORESRETRY has been exhausted).<br />
 Tp Failed to execute &quot;x&quot; Program not in path, or not executable.<br />
 Tp Forced unlock denied on &quot;x&quot; No write permission in the directory where <code>lockfile</code> &quot;x&quot; resides, or more than one procmail trying to force a lock at exactly the same time.<br />
 Tp Forcing lock on &quot;x&quot; <code>Lockfile</code> &quot;x&quot; is going to be removed by force because of a timeout (see also: <code>LOCKTIMEOUT</code>).<br />
 Tp Incomplete recipe The start of a recipe was found, but it stranded in an EOF.<br />
 Tp Insufficient privileges Procmail either needs root privileges, or must have the right (e)uid <code>and</code> (e)gid to run in delivery mode. The mail will bounce.<br />
 Tp Invalid regexp &quot;x&quot; The regular expression &quot;x&quot; contains errors (most likely some missing or extraneous parens).<br />
 Tp Kernel-lock failed While trying to use the kernel-supported locking calls, one of them failed (usually indicates an OS error), procmail ignores this error and proceeds.<br />
 Tp Kernel-unlock failed See above.<br />
 Tp Lock failure on &quot;x&quot; Can only occur if you specify some real weird (and illegal) lockfilenames or if the <code>lockfile</code> could not be created because of insufficient permissions or nonexistent subdirectories.<br />
 Tp Lost &quot;x&quot; Procmail tried to clone itself but could not find back rcfile &quot;x&quot; (it either got removed or it was a relative path and you changed directory since procmail opened it last time).<br />
 Tp Missing action The current recipe was found to be incomplete.<br />
 Tp Missing closing brace A nesting block was started, but never finished.<br />
 Tp Missing name The -f option needs an extra argument.<br />
 Tp Missing argument You specified the -a option but forgot the argument.<br />
 Tp Missing rcfile You specified the -m option, procmail expects the name of an rcfile as argument.<br />
 Tp Missing recipient You specified the -d option or called procmail under a different name, it expects one or more recipients as arguments.<br />
 Tp No space left to finish writing &quot;x&quot; The filesystem containing &quot;x&quot; does not have enough free space to permit delivery of the message to the file.<br />
 Tp Out of memory The system is out of swap space (and NORESRETRY has been exhausted).<br />
 Tp Processing continued The unrecognised options on the command line are ignored, proceeding as usual.<br />
 Tp Program failure (nnn) of &quot;x&quot; Program that was started by procmail returned nnn instead of EXIT_SUCCESS (=0); if nnn is negative, then this is the signal the program died on.<br />
 Tp Quota exceeded while writing &quot;x&quot; The filesize quota for the recipient on the filesystem containing &quot;x&quot; does not permit delivering the message to the file.<br />
 Tp Renaming bogus &quot;x&quot; into &quot;x&quot; The system mailbox of the recipient was found to be bogus, procmail performed evasive actions.<br />
 Tp Rescue of unfiltered data succeeded/failed A filter returned unsuccessfully, procmail tried to get back the original text.<br />
 Tp Skipped: &quot;x&quot; Couldn&#8217;t do anything with &quot;x&quot; in the rcfile (syntax error), ignoring it.<br />
 Tp Suspicious rcfile &quot;x&quot; The owner of the rcfile was not the recipient or root, the file was world writable, or the directory that contained it was world writable, or this was the default rcfile ($HOME/.procmailrc) and either it was group writable or the directory that contained it was group writable (the rcfile was not used).<br />
 Tp Terminating prematurely whilst waiting for &#8230; Procmail received a signal while it was waiting for &#8230;<br />
 Tp Timeout, terminating &quot;x&quot; Timeout has occurred on program or filter &quot;x&quot;.<br />
 Tp Timeout, was waiting for &quot;x&quot; Timeout has occurred on program, filter or file &quot;x&quot;. If it was a program or filter, then it didn&#8217;t seem to be running anymore.<br />
 Tp Truncated file to former size The file could not be delivered to successfully, so the file was truncated to its former size.<br />
 Tp Truncating &quot;x&quot; and retrying lock &quot;x&quot; does not seem to be a valid filename or the file is not empty.<br />
 Tp Unable to treat as directory &quot;x&quot; Either the suffix on &quot;x&quot; would indicate that it should be an MH or maildir folder, or it was listed as an second folder into which to link, but it already exists and is not a directory.<br />
 Tp Unexpected EOL Missing closing quote, or trying to escape EOF.<br />
 Tp Unknown user &quot;x&quot; The specified recipient does not have a corresponding uid. </p>
<h2>EXTENDED DIAGNOSTICS</h2>
<p> Extended diagnostics can be turned on and off through setting the VERBOSE variable.<br />
 Tp 2.3i [pid] time &amp; date Procmail&#8217;s pid and a timestamp. Generated whenever procmail logs a diagnostic and at least a second has elapsed since the last timestamp.<br />
 Tp Acquiring kernel-lock Procmail now tries to kernel-lock the most recently opened file (descriptor).<br />
 Tp Assigning &quot;x&quot; Environment variable assignment.<br />
 Tp Assuming identity of the recipient, VERBOSE=off Dropping all privileges (if any), implicitly turns off extended diagnostics.<br />
 Tp Bypassed locking &quot;x&quot; The mail spool directory was not accessible to procmail, it relied solely on kernel locks.<br />
 Tp Executing &quot;x&quot; Starting program &quot;x&quot;. If it is started by procmail directly (without an intermediate shell), procmail will show where it separated the arguments by inserting commas.<br />
 Tp HOST mismatched &quot;x&quot; This host was called &quot;x&quot;, HOST contained something else.<br />
 Tp Locking &quot;x&quot; Creating lockfile &quot;x&quot;.<br />
 Tp Linking to &quot;x&quot; Creating a hardlink between directory folders.<br />
 Tp Match on &quot;x&quot; Condition matched.<br />
 Tp Matched &quot;x&quot; Assigned &quot;x&quot; to <code>MATCH</code>.<br />
 Tp No match on &quot;x&quot; Condition didn&#8217;t match, recipe skipped.<br />
 Tp Non-zero exitcode (nnn) by &quot;x&quot; Program that was started by procmail as a condition or as the action of a recipe with the `W&#8217; flag returned nnn instead of EXIT_SUCCESS (=0); the usage indicates that this is not an entirely unexpected condition.<br />
 Tp Notified comsat: &quot;$LOGNAME [at] offset:file&quot; Sent comsat/biff a notice that mail arrived for user $LOGNAME at `offset&#8217; in `file&#8217;.<br />
 Tp Opening &quot;x&quot; Opening file &quot;x&quot; for appending.<br />
 Tp Rcfile: &quot;x&quot; Rcfile changed to &quot;x&quot;.<br />
 Tp Reiterating kernel-lock While attempting several locking methods, one of these failed. Procmail will reiterate until they all succeed in rapid succession.<br />
 Tp Score: added newtotal &quot;x&quot; This condition scored `added&#8217; points, which resulted in a `newtotal&#8217; score.<br />
 Tp Unlocking &quot;x&quot; Removing lockfile &quot;x&quot; again. </p>
<h2>WARNINGS</h2>
<p> You should create a shell script that uses <code><a href="/docs/linux/man/1-lockfile/">lockfile</a></code>(1) before invoking your mail shell on any mailbox file other than the system mailbox (unless of course, your mail shell uses the same lockfiles (local or global) you specified in your rcfile). </p>
<p> In the unlikely event that you absolutely need to kill procmail before it has finished, first try and use the regular kill command (i.e., <i>not</i> kill -9, see the subsection <i>Signals</i> for suggestions), otherwise some <i>lockfiles</i> might not get removed. </p>
<p> Beware when using the <code>-t</code> option, if procmail repeatedly is unable to deliver the mail (e.g., due to an incorrect rcfile), the system mailqueue could fill up. This could aggravate both the local postmaster and other users. </p>
<p> The <code>/etc/procmailrc</code> file might be executed with root privileges, so be very careful of what you put in it. <code>SHELL</code> will be equal to that of the current recipient, so if procmail has to invoke the shell, you&#8217;d better set it to some safe value first. See also : <code>DROPPRIVS</code>. </p>
<p> Keep in mind that if <code><a href="/docs/linux/man/1-chown/">chown</a></code>(1) is permitted on files in <code>/etc/procmailrcs/</code>, that they can be chowned to root (or anyone else) by their current owners. For maximum security, make sure this directory is <i>executable</i> to root only. </p>
<p> Procmail is not the proper tool for sharing one mailbox among many users, such as when you have one POP account for all mail to your domain. It can be done if you manage to configure your MTA to add some headers with the envelope recipient data in order to tell Procmail who a message is for, but this is usually not the right thing to do. Perhaps you want to investigate if your MTA offers `virtual user tables&#8217;, or check out the `multidrop&#8217; facility of Fetchmail. </p>
<h2>BUGS</h2>
<p> After removing a lockfile by force, procmail waits $SUSPEND seconds before creating a new lockfile so that another process that decides to remove the stale lockfile will not remove the newly created lock by mistake. </p>
<p> Procmail uses the regular TERMINATE signal to terminate any runaway filter, but it does not check if the filter responds to that signal and it only sends it to the filter itself, not to any of the filter&#8217;s children. </p>
<p> A continued <code>Content-Length:</code> field is not handled correctly. </p>
<p> The embedded newlines in a continued header should be skipped when matching instead of being treated as a single space as they are now. </p>
<h2>MISCELLANEOUS</h2>
<p> If there is an existing <code>Content-Length:</code> field in the header of the mail and the <code>-Y</code> option is not specified, procmail will trim the field to report the correct size. Procmail does not change the fieldwidth. </p>
<p> If there is no <code>Content-Length:</code> field or the <code>-Y</code> option has been specified and procmail appends to regular mailfolders, any lines in the body of the message that look like postmarks are prepended with `&gt;&#8217; (disarms bogus mailheaders). The regular expression that is used to search for these postmarks is: </p>
<pre>
<dl><dt><dd>`
From '
</dl>
</pre>
<p> If the destination name used in explicit delivery mode is not in /etc/passwd, procmail will proceed as if explicit delivery mode was not in effect. If not in explicit delivery mode and should the uid procmail is running under, have no corresponding /etc/passwd entry, then HOME will default to /, LOGNAME will default to #uid, SHELL will default to /bin/sh, and ORGMAIL will default to /tmp/dead.letter. </p>
<p> When in explicit delivery mode, procmail will generate a leading `From &#8216; line if none is present. If one is already present procmail will leave it intact. If procmail is not invoked with one of the following user or group ids : root, daemon, uucp, mail, x400, network, list, slist, lists or news, but still has to generate or accept a new `From &#8216; line, it will generate an additional `&gt;From &#8216; line to help distinguish fake mails. </p>
<p> For security reasons procmail will only use an absolute or $HOME-relative rcfile if it is owned by the recipient or root, not world writable, and the directory it is contained in is not world writable. The $HOME/.procmailrc file has the additional constraint of not being group-writable or in a group-writable directory. </p>
<p> If /var/mail/$LOGNAME is a bogus mailbox (i.e., does not belong to the recipient, is unwritable, is a symbolic link or is a hard link), procmail will upon startup try to rename it into a file starting with `BOGUS.$LOGNAME.&#8217; and ending in an inode-sequence-code. If this turns out to be impossible, <code>ORGMAIL</code> will have <i>no</i> initial value, and hence will inhibit delivery without a proper rcfile. </p>
<p> If /var/mail/$LOGNAME already is a valid mailbox, but has got too loose permissions on it, procmail will correct this. To prevent procmail from doing this make sure the u+x bit is set. </p>
<p> When delivering to directories, MH folders, or maildir folders, you <code>don&#8217;t</code> need to use lockfiles to prevent several concurrently running procmail programs from messing up. </p>
<p> Delivering to MH folders is slightly more time consuming than delivering to normal directories or mailboxes, because procmail has to search for the next available number (instead of having the filename immediately available). </p>
<p> On general failure procmail will return EX_CANTCREAT, unless option <code>-t</code> is specified, in which case it will return EX_TEMPFAIL. </p>
<p> To make `egrepping&#8217; of headers more consistent, procmail concatenates all continued header fields; but only internally. When delivering the mail, line breaks will appear as before. </p>
<p> If procmail is called under a name not starting with `procmail&#8217; (e.g., if it is linked to another name and invoked as such), it comes up in explicit delivery mode, and expects the recipients&#8217; names as command line arguments (as if -d had been specified). </p>
<p> Comsat/biff notifications are done using udp. They are sent off once when procmail generates the regular logfile entry. The notification messages have the following extended format (or as close as you can get when final delivery was not to a file): </p>
<pre>
<dl><dt><dd>$LOGNAME [at] offset_of_message_in_mailbox :absolute_path_to_mailbox
</dl>
</pre>
<p> Whenever procmail itself opens a file to deliver to, it consistently uses the following kernel locking strategies : <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2). </p>
<p> Procmail is NFS-resistant and eight-bit clean. </p>
<h2>NOTES</h2>
<p> Calling up procmail with the -h or -? options will cause it to display a command-line help and recipe flag quick-reference page. </p>
<p> There exists an excellent newbie FAQ about mailfilters (and procmail in particular); it is maintained by Nancy McGough &lt;nancym [at] ii.com&gt; and can be obtained by sending a mail to mail-server [at] rtfm.mit.edu with the following in the body: </p>
<pre>
<dl><dt><dd>send usenet/news.answers/mail/filtering-faq
</dl>
</pre>
<p> If procmail is <i>not</i> installed globally as the default mail delivery agent (ask your system administrator), you have to make sure it is invoked when your mail arrives. In this case your $HOME/.forward (beware, it <code>has</code> to be world readable) file should contain the line below. Be sure to include the single and double quotes, and unless you know your site to be running smrsh (the SendMail Restricted SHell), it must be an <i>absolute</i> path. </p>
<pre>
&quot; |exec /usr/bin/procmail&quot;
</pre>
<p> Some mailers (notably exim) do not currently accept the above syntax. In such case use this instead: </p>
<pre>
|/usr/bin/procmail
</pre>
<p> Procmail can also be invoked to postprocess an already filled system mailbox. This can be useful if you don&#8217;t want to or can&#8217;t use a $HOME/.forward file (in which case the following script could periodically be called from within <code><a href="/docs/linux/man/1-cron/">cron</a></code>(1), or whenever you start reading mail): </p>
<pre><code>
#!/ bin / sh
ORGMAIL = / var / mail / $LOGNAME if cd $HOME &amp;&amp;
          test - s $ORGMAIL &amp;&amp;
          lockfile - r0 - l1024.newmail.lock 2 &gt; / dev / null then trap "rm -f .newmail.lock" 1 2 3 13 15 umask 077 lockfile - l1024 - ml cat $ORGMAIL &gt;&gt;.newmail &amp;&amp;
                                                                                                                                                                 cat /
                                                                                                                                                             dev / null &gt;
              $ORGMAIL
                      lockfile -
                  mu
                      formail -
                  s procmail &lt;
                  .newmail &amp;&amp;
                          rm -
                      f.newmail
                          rm -
                      f.newmail.lock
                          fi
                              exit 0
</code></pre>
<h3>A sample small $HOME/.procmailrc:</h3>
<pre>
PATH=/usr/local/bin:/usr/bin:/bin
MAILDIR=$HOME/Mail      #you'd better make sure it exists
DEFAULT=$MAILDIR/mbox   #completely optional
LOGFILE=$MAILDIR/from   #recommended
:0:
* ^From.*berg
from_me
:0
* ^Subject:.*Flame
/dev/null
</pre>
<p> Other examples for rcfile recipes can be looked up in the <code><a href="/docs/linux/man/5-procmailex/">procmailex</a></code>(5) man page.</p>
<h2>SOURCE</h2>
<p> This program is part of the <i>procmail mail-processing-package</i> (v3.23pre) available at <a rel="nofollow" href="http://www.procmail.org/">http://www.procmail.org/</a> or <a href="ftp://ftp.procmail.org">ftp.procmail.org</a> in <code>pub/procmail/</code>.</p>
<h2>MAILINGLIST</h2>
<p> There exists a mailinglist for questions relating to any program in the procmail package: </p>
<pre>
<dl><dt><dd>&lt;procmail-users [at] procmail.org&gt;
<dl><dt><dd>for submitting questions/answers.
</dl>
</pre>
<p> &lt;procmail-users-request [at] procmail.org&gt; </p>
<pre>
<dl><dt><dd>for subscription requests.
</dl>
</pre>
</dl>
<p> If you would like to stay informed about new versions and official patches send a subscription request to </p>
<pre>
<dl><dt><dd>procmail-announce-request [at] procmail.org
</dl>
</pre>
<p> (this is a readonly list). </p>
<h2>AUTHORS</h2>
<p> Stephen R. van den Berg </p>
<pre>
<dl><dt><dd>&lt;srb [at] cuci.nl&gt;
</dl>
</pre>
<p> Philip A. Guenther </p>
<pre>
<dl><dt><dd>&lt;guenther [at] sendmail.com&gt;
</dl>
</pre>
<h2>Index</h2>
