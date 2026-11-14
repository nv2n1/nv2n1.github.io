---
title: "maildrop(1)"
name: "maildrop"
section: "1"
letter: "m"
url: "/docs/linux/man/1-maildrop/"
description: "maildrop – mail delivery filter/agent"
---

<h2 class="name">NAME</h2>
<p> maildrop &#8211; mail delivery filter/agent </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>maildrop</code> [option&#8230;] [-d&nbsp;<wbr><i>user</i>] [<i>arg</i>&#8230;]</p>
<dt> <code>maildrop</code> [option&#8230;] [<i>filename</i>] [<i>arg</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>maildrop</code></p>
<dd>is a replacement local mail delivery agent that includes a mail filtering language. The system administrator can either replace the existing mail delivery agent with <code>maildrop</code>, or users may run <code>maildrop</code> using the &#8216;forward to program&#8217; mechanism of the existing mail delivery agent. </p>
<p> <code>maildrop</code> first reads the E-mail message on standard input. Trailing carriage return characters are automatically stripped. An E-mail message consists of header lines, followed by a blank line, followed by the contents of the message. </p>
<p> <code>maildrop</code> does not accept an mbox-style From_ line before the first header line. <code>maildrop</code> does not accept leading empty lines before the first non-blank header line. If the message can possibly start with empty lines, and a From_ line, use <code>reformail -f0</code> to remove any initial empty lines, and replace a From_ line with a proper &#8220;Return-Path:&#8221; header; then pipe it to <code>maildrop</code>. </p>
<p> If the file /etc/maildroprc exists, mail delivery or mail filtering instructions are read from that file. <code>maildrop</code>&#8216;s delivery/filtering instructions may direct <code>maildrop</code> to save the message in specific mailbox, discard it, return it to sender, or forward it to a different E-mail address. </p>
<p> If /etc/maildroprc does not exist, or its mail delivery instructions do not completely dispose of this message, <code>maildrop</code> then reads the mail delivery instructions from $HOME/.mailfilter. If it doesn&#8217;t exist, or its mail delivery instructions do not completely dispose of the message, <code>maildrop</code> then saves the E-mail message in the default mailbox. </p>
<p> <code>maildrop</code> knows how to deliver mail to an standard mailbox files; it also knows how to deliver to maildirs. A maildir is a directory-based mail format used by the m[blue]<code>Courier</code>m[]<font SIZE="-2">[1]</font> and m[blue]<code>Qmail</code>m[]<font SIZE="-2">[2]</font> mail servers. Many other mail servers also know how to read maildirs. When delivering to mailbox files, <code>maildrop</code> will lock the mailbox for the duration of the delivery. </p>
<p> This is the general mail delivery behavior. There are minor differences in behavior depending on <code>maildrop</code> delivery mode, which is determined based on how <code>maildrop</code> was started. <code>maildrop</code> uses three different primary operating modes: </p>
<p> Manual mode</p>
<dl>
<dt>
<dd> A file containing filtering instructions &#8211; <i>filename</i> is specified as an argument to the <code>maildrop</code> command. <code>maildrop</code> reads this <i>filename</i> (after /etc/maildroprc) and follows the instructions in it. Unless the message is explicitly forwarded, bounced, deleted, or delivered to a specific mailbox, it will be delivered to the user&#8217;s system mailbox.</dl>
<p> Delivery mode</p>
<dl>
<dt>
<dd> <code>maildrop</code> is the mail server&#8217;s mail delivery agent. <code>maildrop</code> runs in delivery mode when no <i>filename</i> is specified on the command line. <code>maildrop</code> changes the current directory to the user&#8217;s home directory, then reads /etc/maildroprc, then $HOME/.mailfilter.</dl>
<p> Embedded mode</p>
<dl>
<dt>
<dd> <code>maildrop</code> functions as a part of another application. The embedded mode is used by the m[blue]<code>Courier</code>m[]<font SIZE="-2">[1]</font> mail server to integrate mail filtering directly into the process of receiving mail from a remote mail relay, thus rejecting unwanted mail before it is even accepted for local mail delivery. Embedded mode is used when either the -m, or the -M, option is specified, and is described below. See below for a more extensive description of the embedded mode.</dl>
<h2>SECURITY</h2>
<p> It is safe to install <code>maildrop</code> as a root setuid program. m[blue]<code>The Courier mail server</code>m[]<font SIZE="-2">[1]</font> installs <code>maildrop</code> as a root setuid program by default, in order to be able to use <code>maildrop</code> in embedded mode. If root runs <code>maildrop</code> (or it is setuided to root) the <code>-d</code> option may be used to specify the message&#8217;s recipient. <code>maildrop</code> immediately resets its userid to the one specified by the <code>-d</code> option. The user&#8217;s $HOME/.mailfilter is read (if it exists), and the message is delivered to the indicated user. </p>
<p> The system administrator can configure <code>maildrop</code> to restrict the <code>-d</code> option for everyone except the mail system itself. </p>
<p> If in delivery mode the user&#8217;s home directory has the sticky bit set, <code>maildrop</code> immediately terminates with an exit code of <code>EX_TEMPFAIL</code>, without doing anything. Mail servers interpret the <code>EX_TEMPFAIL</code> exit code as a request to reschedule the message for another delivery attempt later. Setting the sticky bit allows $HOME/.mailfilter to be edited while temporarily holding all incoming mail. </p>
<p> <code>maildrop</code> also terminates with <code>EX_TEMPFAIL</code> if the user&#8217;s home directory has world write permissions. </p>
<p> <code>maildrop</code> immediately terminates with <code>EX_TEMPFAIL</code> if the filename is not owned by the user, or if it has any group or world permissions. This includes read permissions. The permissions on $HOME/.mailfilter may only include read and write privileges to the user. </p>
<p> When using the special embedded mode (see below) <code>maildrop</code> immediately terminates with the exit code set to <code>EX_TEMPFAIL</code> if $HOME/.mailfilters is not owned by the user, or if it has any group or world permissions.</p>
<h2>TEMPORARY FILES</h2>
<p> <code>maildrop</code> is heavily optimized and tries to use as little resources as possible. <code>maildrop</code> reads small messages into memory, then filters and/or delivers the message directly from memory. For larger messages, <code>maildrop</code> accesses the message directly from the file. If the standard input is not a file, <code>maildrop</code> writes the message to a temporary file, then accesses the message from the temporary file. The temporary file is automatically removed when the message is delivered.</p>
<h2>OPTIONS</h2>
<p> -a</p>
<dl>
<dt>
<dd> Makes the Courier Authentication Library usage mandatory, i.e. maildrop will throw a temporary error code if the call to the authlib mechanism fails for some reason, such as authdaemon being inaccessible. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 This setting may already be the default, depending on maildrop&#8217;s configuration. </p>
</dl>
</dl>
<p> -A &quot;<i>Header: value</i>&quot;</p>
<dl>
<dt>
<dd> Adds an additional header to the message. Specifying <i>-A &quot;Foo: Bar&quot;</i> effectively adds this header to the message being delivered. </p>
<p> The mail transport agent usually adds additional headers when delivering a message to a local mailbox. The way it&#8217;s usually done is by the mail transport agent sending the message using a pipe to the local delivery agent &#8211; such as <code>maildrop</code> &#8211; and adding some additional headers in the process. Because <code>maildrop</code> receives the message from a pipe, <code>maildrop</code> must either save the message in memory or write the message into a temporary file. </p>
<p> The <code>-A</code> option enables the file containing the message to be provided to <code>maildrop</code> directly, as standard input, and the additional headers specified on the command line. Because the standard input is a file, <code>maildrop</code> will not need a temporary file. Multiple <code>-A</code> options may be specified.</dl>
<p> -d <i>user</i></p>
<dl>
<dt>
<dd> Run <code>maildrop</code> in delivery mode for this user ID. </p>
<p> The system administrator may optionally restrict the <code>-d</code> option to be available to the mail system only, so it may not be available to you. In all cases, the <code>-d</code> option is allowed if <i>user</i> is the same user who is running <code>maildrop</code>. Also, for the <code>-d</code> option to work at all, <code>maildrop</code> must be executed by root, or <code>maildrop</code> must be a root-owned program with the setuid bit set. Absence of a filename on <code>maildrop</code>&#8216;s command line implies the <code>-d</code> option for the user running <code>maildrop</code>. </p>
<p> If <code>-d</code> is not specified, the first argument following all the options is a name of the file containing filtering instructions. The remaining arguments, if any, are assigned to the variables <i>$1</i>, <i>$2</i>, and so on (see m[blue]<code>&quot;Environment&quot;</code>m[]<font SIZE="-2">[3]</font> and m[blue]<code>&quot;Variable substitution&quot;</code>m[]<font SIZE="-2">[4]</font>).</dl>
<p> -f <i>address</i></p>
<dl>
<dt>
<dd> Sets the FROM variable (message envelope sender) to <i>address</i>. The system administrator may optionally disable the <code>-f</code> option for users, so it may not be available to you.</dl>
<p> -m</p>
<dl>
<dt>
<dd> Run <code>maildrop</code> in embedded mode. It&#8217;s possible to use both the <code>-m</code>, and the <code>-d</code> options, but it doesn&#8217;t make much sense to do so. Even if you really wanted to run your message through someone else&#8217;s .mailfilter, that .mailfilter probably has at least one instruction which is not allowed in the embedded mode. </p>
<p> The filename argument to <code>maildrop</code> should be specified. filename is a file that includes filtering instructions to be processed in embedded mode. The -m option is used for debugging filter files which are later placed in $HOME/.mailfilters, and used with the <code>-M</code> option.</dl>
<p> -M <i>filterfile</i></p>
<dl>
<dt>
<dd> Run <code>maildrop</code> in a special embedded mode. The <code>-d</code> option is implied when <code>-M</code> is used, and if absent it defaults to the userid running <code>maildrop</code>. </p>
<p> All the requirements for the <code>-d</code> option apply. <code>maildrop</code> must either be executed by root, or the <code>maildrop</code> program must be owned by root with the setuid bit set. <code>maildrop</code> immediately gives up root privileges by changing its user ID to the one specified by <code>-d</code>, then reads $HOME/.mailfilters/<i>filterfile</i>. For security reasons the name of the file may not begin with a slash or include periods. <code>maildrop</code> is very paranoid: both $HOME/.mailfilters, and $HOME/.mailfilters/<i>filterfile</i> must be owned by the user, and may not have any group or world permissions. </p>
<p> The <code>-M</code> option allows for some friendly cooperation between the user running the application, and the user who provides a filter for the embedded mode. The user running the application can use someone else&#8217;s canned filter and be assured that the filter is not going to run amok and start sending mail or create files all over the place. The user who provides the filter can be assured that the environment variables are clean, and that there are no surprises. </p>
<p> <code>maildrop</code> supports the concept of &quot;default&quot; filter files. If the file specified by the <code>-M</code> option cannot be found in $HOME/.mailfilters, <code>maildrop</code> will try to open $HOME/.mailfilters/<i>filterfileprefix</i>-default. <i>filterfileprefix</i> is the initial part of <i>filterfile</i> up until the last &#8216;-&#8216; character in <i>filterfile</i>. </p>
<p> If $HOME/.mailfilters/<i>filterfileprefix</i>-default does not exist, and there are any other dashes left in <i>filterfileprefix</i>, maildrop removes the last dash and everything following it, then tries again. </p>
<p> As a last resort <code>maildrop</code> tries to open $HOME/.mailfilters/default. </p>
<p> For example, if the parameter to the <code>-M</code> option is <i>mailfilter-lists-maildrop</i>, <code>maildrop</code> will try to open the following files, in order: </p>
<p> Note that <code>maildrop</code> looks for -default files ONLY if <code>-M</code> is used.</dl>
<p> -D <i>uuu/ggg</i></p>
<dl>
<dt>
<dd> This option is reserved for use by the version of <code>maildrop</code> that comes integrated with the m[blue]<code>Courier mail server</code>m[]<font SIZE="-2">[1]</font>.</dl>
<p> -V <i>level</i></p>
<dl>
<dt>
<dd> Initialize the <i>VERBOSE</i> variable to <i>level</i>. Because <code>maildrop</code> parses the entire file before running it, this option is used to produce debugging output in the parsing phase. Otherwise, if filename has syntax errors, then no debugging output is possible because the <i>VERBOSE</i> variable is not yet set. </p>
<p> <code>-V</code> is ignored when <code>maildrop</code> runs in delivery mode.</dl>
<p> -w <i>N</i></p>
<dl>
<dt>
<dd> The <code>-w N</code> option places a warning message into the maildir if the maildir has a quota setting, and after the message was successfully delivered the maildir was at least <i>N</i> percent full.</dl>
<p> -W <i>filename</i></p>
<dl>
<dt>
<dd> Copy the warning message from <i>filename</i>, or from /etc/quotawarnmsg if this option is not specified, with the addition of the &quot;Date:&quot; and &quot;Message-Id:&quot; headers. The warning is repeated every 24 hours (at least), until the maildir drops below <i>N</i> percent full.</dl>
<p> -t <i>socket</i></p>
<dl>
<dt>
<dd> This option is available if maildrop is compiled with optional Dovecot authentication support. <i>socket</i> specifies the location of Dovecot master authentication socket, for example /var/run/dovecot/auth-master.</dl>
<h2>DELIVERY MODE</h2>
<p> If a filename is not specified on the command line, or if the <code>-d</code> option is used, <code>maildrop</code> will run in delivery mode. In delivery mode, <code>maildrop</code> changes to the home directory of the user specified by the <code>-d</code> option (or the user who is running <code>maildrop</code> if the <code>-d</code> option was not given) and reads $HOME/.mailfilter for filtering instructions. $HOME/.mailfilter must be owned by the user, and have no group or global permissions (<code>maildrop</code> terminates if it does). </p>
<p> If $HOME/.mailfilter does not exist, <code>maildrop</code> will simply deliver the message to the user&#8217;s mailbox. </p>
<p> If the file /etc/maildroprc exists, <code>maildrop</code> reads filtering instructions from this file first, before reading $HOME/.mailfilter. This allows the system administrator to provide global filtering instructions for all users. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> /etc/maildroprc is read only in delivery mode. </p>
</dl>
<h2>VIRTUAL ACCOUNTS</h2>
<p> The <code>-d</code> option can also specify a name of a virtual account or mailbox. See the <code><a href="/docs/linux/man/1-makeuserdb/">makeuserdb</a></code>(1) manual page in the Courier Authentication library&#8217;s documentation for more information.</p>
<h2>EMBEDDED MODE</h2>
<p> The embedded mode is used when <code>maildrop</code>&#8216;s filtering abilities are desired, but no actual mail delivery is needed. In embedded mode <code>maildrop</code> is executed by another application, and m[blue]<code>is passed the -m or the -M option.</code>m[]<font SIZE="-2">[5]</font><code>maildrop</code> reads the message, then runs the filtering rules specified in filename. </p>
<p> filename may contain any filtering instructions EXCEPT the following: </p>
<p> ` &#8230; `</p>
<dl>
<dt>
<dd> Text strings delimited by back-tick characters (run shell command) are not allowed.</dl>
<p> m[blue]<code>cc</code>m[]<font SIZE="-2">[6]</font></p>
<dl>
<dt>
<dd> The <code>cc</code> command is not allowed in embedded mode.</dl>
<p> m[blue]<code>dotlock</code>m[]<font SIZE="-2">[7]</font></p>
<dl>
<dt>
<dd> The <code>dotlock</code> command is not allowed in embedded mode.</dl>
<p> m[blue]<code>flock</code>m[]<font SIZE="-2">[8]</font></p>
<dl>
<dt>
<dd> The <code>flock</code> command is not allowed in embedded mode.</dl>
<p> m[blue]<code>gdbmopen</code>m[]<font SIZE="-2">[9]</font></p>
<dl>
<dt>
<dd> In embedded mode, GDBM databases may be opened only for reading.</dl>
<p> m[blue]<code>log</code>m[]<font SIZE="-2">[10]</font></p>
<dl>
<dt>
<dd> The <code>log</code> command is not allowed in embedded mode.</dl>
<p> m[blue]<code>logfile</code>m[]<font SIZE="-2">[10]</font></p>
<dl>
<dt>
<dd> The <code>logfile</code> command is not allowed in embedded mode.</dl>
<p> m[blue]<code>to</code>m[]<font SIZE="-2">[11]</font></p>
<dl>
<dt>
<dd> The <code>to</code> command is not allowed in embedded mode.</dl>
<p> m[blue]<code>xfilter</code>m[]<font SIZE="-2">[12]</font></p>
<dl>
<dt>
<dd> The <code>xfilter</code> command is not allowed in embedded mode.</dl>
<p> Normally when the filename does not explicitly delivers a message, <code>maildrop</code> will deliver the message to the user&#8217;s default mailbox. This is also disabled in embedded mode. </p>
<p> The filename may communicate with the parent application by using the m[blue]<code>echo</code>m[]<font SIZE="-2">[13]</font> statement and the <i>EXITCODE</i> environment variable.</p>
<h3>/etc/maildroprcs</h3>
<p> If <code>maildrop</code> encounters an m[blue]<code>include</code>m[]<font SIZE="-2">[14]</font> statement where the filename starts with /etc/maildroprcs/, the normal restrictions for the embedded mode are suspended while executing the filter file in the /etc/maildroprcs directory. The restrictions are also suspended for any additional filter files that are included from /etc/maildroprcs. The restrictions resume once <code>maildrop</code> finishes executing the file from /etc/maildroprcs. </p>
<p> This allows the system administrator to have a controlled environment for running external commands (via the backticks, or the m[blue]<code>xfilter</code>m[]<font SIZE="-2">[12]</font> command). </p>
<p> The name of the file may not contain any periods (so that a creative individual can&#8217;t write <i>include &quot;/etc/maildroprcs/../../home/user/recipe&quot;</i>). </p>
<p> Before executing the commands in the /etc/maildroprcs file, <code>maildrop</code> automatically resets the following variables to their initial values: <i>DEFAULT</i>, <i>HOME</i>, <i>LOCKEXT</i>, <i>LOCKSLEEP</i>, <i>LOCKTIMEOUT</i>, <i>LOCKREFRESH</i>, <i>LOGNAME</i>, <i>PATH</i>, <i>SENDMAIL</i>, and <i>SHELL</i>. Please note that the previous values of these variables (if they were changed) will NOT be restored once <code>maildrop</code> finishes executing the commands from /etc/maildroprcs.</p>
<h2>WATCHDOG TIMER</h2>
<p> <code>maildrop</code> has a watchdog timer that attempts to abort runaway filtering. If filtering is not complete within a predefined time interval (defined by the system administrator, usually five minutes), <code>maildrop</code> terminates.</p>
<h2>FILES</h2>
<p> /etc/passwd</p>
<dl>
<dt>
<dd> Sets user&#8217;s home directory, and related variables. If NIS/YP is install, that will be used as well.</dl>
<p> /etc/maildroprc</p>
<dl>
<dt>
<dd> Global filtering instructions for delivery mode.</dl>
<p> /var/mail</p>
<dl>
<dt>
<dd> System mailbox (actual directory defined by the system administrator).</dl>
<p> /usr/lib/sendmail</p>
<dl>
<dt>
<dd> Program to forward mail (exact program defined by the system administrator).</dl>
<p> $HOME/.mailfilter</p>
<dl>
<dt>
<dd> Filtering instructions in delivery mode.</dl>
<p> $HOME/.mailfilters</p>
<dl>
<dt>
<dd> Directory containing files used in special embedded mode.</dl>
<h2>SEE ALSO</h2>
<p> m[blue]<code><a href="/docs/linux/man/1-lockmail/">lockmail</a></code>(1)m[]<font SIZE="-2">[15]</font>, m[blue]<code><a href="/docs/linux/man/7-maildropfilter/">maildropfilter</a></code>(7)m[]<font SIZE="-2">[16]</font>, m[blue]<code><a href="/docs/linux/man/1-makedat/">makedat</a></code>(1)m[]<font SIZE="-2">[17]</font>, m[blue]<code><a href="/docs/linux/man/7-maildropgdbm/">maildropgdbm</a></code>(7)m[]<font SIZE="-2">[9]</font>, m[blue]<code><a href="/docs/linux/man/7-maildropex/">maildropex</a></code>(7)m[]<font SIZE="-2">[18]</font>, m[blue]<code><a href="/docs/linux/man/1-reformail/">reformail</a></code>(1)m[]<font SIZE="-2">[19]</font>, m[blue]<code><a href="/docs/linux/man/1-makemime/">makemime</a></code>(1)m[]<font SIZE="-2">[20]</font>, m[blue]<code><a href="/docs/linux/man/1-reformime/">reformime</a></code>(1)m[]<font SIZE="-2">[21]</font>, <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1), <code><a href="/docs/linux/man/1-grep/">grep</a></code>(1), , m[blue]<code><a href="/docs/linux/man/8-courier/">courier</a></code>(8)m[]<font SIZE="-2">[22]</font>, <code><a href="/docs/linux/man/8-sendmail/">sendmail</a></code>(8), m[blue]<code><a rel="nofollow" href="http://www.qmail.org">http://www.qmail.org</a></code>m[].</p>
<h2>AUTHOR</h2>
<p> <code>Sam Varshavchik</code></p>
<dl>
<dt>
<dd> Author</dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Courier</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.courier-mta.org">http://www.courier-mta.org</a></dl>
<dt> 2.</p>
<dd> Qmail</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.qmail.org">http://www.qmail.org</a></dl>
<dt> 3.</p>
<dd> &quot;Environment&quot;</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.courier-mta.org/maildrop/maildropfilter.html#environment">http://www.courier-mta.org/maildrop/maildropfilter.html#environment</a></dl>
<dt> 4.</p>
<dd> &quot;Variable substitution&quot;</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.courier-mta.org/maildrop/maildropfilter.html#varsubst">http://www.courier-mta.org/maildrop/maildropfilter.html#varsubst</a></dl>
<dt> 5.</p>
<dd> is passed the -m or the -M option.</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.courier-mta.org/maildrop/#options">http://www.courier-mta.org/maildrop/#options</a></dl>
<dt> 6.</p>
<dd> cc</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.courier-mta.org/maildrop/maildropfilter.html#cc">http://www.courier-mta.org/maildrop/maildropfilter.html#cc</a></dl>
<dt> 7.</p>
<dd> dotlock</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.courier-mta.org/maildrop/maildropfilter.html#dotlock">http://www.courier-mta.org/maildrop/maildropfilter.html#dotlock</a></dl>
<dt> 8.</p>
<dd> flock</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.courier-mta.org/maildrop/maildropfilter.html#flock">http://www.courier-mta.org/maildrop/maildropfilter.html#flock</a></dl>
<dt> 9.</p>
<dd> gdbmopen</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.courier-mta.org/maildrop/maildropgdbm.html">http://www.courier-mta.org/maildrop/maildropgdbm.html</a></dl>
<dt>10.</p>
<dd> log</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.courier-mta.org/maildrop/maildropfilter.html#log">http://www.courier-mta.org/maildrop/maildropfilter.html#log</a></dl>
<dt>11.</p>
<dd> to</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.courier-mta.org/maildrop/maildropfilter.html#to">http://www.courier-mta.org/maildrop/maildropfilter.html#to</a></dl>
<dt>12.</p>
<dd> xfilter</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.courier-mta.org/maildrop/maildropfilter.html#xfilter">http://www.courier-mta.org/maildrop/maildropfilter.html#xfilter</a></dl>
<dt>13.</p>
<dd> echo</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.courier-mta.org/maildrop/maildropfilter.html#echo">http://www.courier-mta.org/maildrop/maildropfilter.html#echo</a></dl>
<dt>14.</p>
<dd> include</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.courier-mta.org/maildrop/maildropfilter.html#include">http://www.courier-mta.org/maildrop/maildropfilter.html#include</a></dl>
<dt>15.</p>
<dd> <code><a href="/docs/linux/man/1-lockmail/">lockmail</a></code>(1)</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.courier-mta.org/maildrop/lockmail.html">http://www.courier-mta.org/maildrop/lockmail.html</a></dl>
<dt>16.</p>
<dd> <code><a href="/docs/linux/man/7-maildropfilter/">maildropfilter</a></code>(7)</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.courier-mta.org/maildrop/maildropfilter.html">http://www.courier-mta.org/maildrop/maildropfilter.html</a></dl>
<dt>17.</p>
<dd> <code><a href="/docs/linux/man/1-makedat/">makedat</a></code>(1)</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.courier-mta.org/maildrop/makedat.html">http://www.courier-mta.org/maildrop/makedat.html</a></dl>
<dt>18.</p>
<dd> <code><a href="/docs/linux/man/7-maildropex/">maildropex</a></code>(7)</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.courier-mta.org/maildrop/maildropex.html">http://www.courier-mta.org/maildrop/maildropex.html</a></dl>
<dt>19.</p>
<dd> <code><a href="/docs/linux/man/1-reformail/">reformail</a></code>(1)</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.courier-mta.org/maildrop/reformail.html">http://www.courier-mta.org/maildrop/reformail.html</a></dl>
<dt>20.</p>
<dd> <code><a href="/docs/linux/man/1-makemime/">makemime</a></code>(1)</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.courier-mta.org/maildrop/makemime.html">http://www.courier-mta.org/maildrop/makemime.html</a></dl>
<dt>21.</p>
<dd> <code><a href="/docs/linux/man/1-reformime/">reformime</a></code>(1)</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.courier-mta.org/maildrop/reformime.html">http://www.courier-mta.org/maildrop/reformime.html</a></dl>
<dt>22.</p>
<dd> <code><a href="/docs/linux/man/8-courier/">courier</a></code>(8)</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.courier-mta.org/maildrop/courier.html">http://www.courier-mta.org/maildrop/courier.html</a></dl>
</dl>
<h2>Index</h2>
