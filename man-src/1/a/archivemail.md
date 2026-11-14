---
title: "archivemail(1)"
name: "archivemail"
section: "1"
letter: "a"
url: "/docs/linux/man/1-archivemail/"
description: "archivemail – archive and compress your old email"
---

<h2 class="name">NAME</h2>
<p> archivemail &#8211; archive and compress your old email </p>
<h2>SYNOPSIS</h2>
<p> <code>archivemail</code> [ <code>options</code> ] <i>MAILBOX</i><i> &#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> archivemail is a tool for archiving and compressing old email in mailboxes. By default it will read the mailbox <i>MAILBOX</i>, moving messages that are older that the specified number of days (180 by default) to a <code><a href="/docs/linux/man/5-mbox/">mbox</a></code>(5)-format mailbox in the same directory that is compressed with <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1). It can also just delete old email rather than archive it. </p>
<p> <code>archivemail</code> supports reading <code>IMAP</code>, <code>Maildir</code>, <code>MH</code> and <code>mbox</code>-format mailboxes, but always writes <code>mbox</code>-format archives. </p>
<p> Messages that are flagged important are not archived or deleted unless explicitely requested with the <code>&#8211;include-flagged</code> option. Also, <code>archivemail</code> can be configured not to archive unread mail, or to only archive messages larger than a specified size. </p>
<p> To archive an <code>IMAP</code>-format mailbox, use the format <i><a href="imap://username:password@server/mailbox">imap://username:password@server/mailbox</a></i> to specify the mailbox. You can omit the password from the URL; use the <code>&#8211;pwfile</code> option to make <code>archivemail</code> read the password from a file, or alternatively just enter it upon request. If the <code>&#8211;pwfile</code> option is set, <code>archivemail</code> does not look for a password in the URL, and the colon is not considered a delimiter. Substitute &#8216;<code>imap</code>&#8216; with &#8216;<code>imaps</code>&#8216;, and <code>archivemail</code> will establish a secure SSL connection. See below for more <code>IMAP</code> peculiarities. </p>
<p> <code>archivemail</code> has some support for being run as the root user on user mailboxes. When running as root, it will <code><a href="/docs/linux/man/2-seteuid/">seteuid</a></code>(2) to the owner of the mailbox it is reading, creating any archive files as that user. <code>Warning:</code> this automatic seteuid feature is insecure and deprecated. It will be removed from later versions of <code>archivemail</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code> -d </code><i>NUM</i><code>, &#8211;days=</code><i>NUM</i></p>
<dd> Archive messages older than <i>NUM</i> days. The default is 180. This option is incompatible with the <code>&#8211;date</code> option below.</p>
<dt><code> -D </code><i>DATE</i><code>, &#8211;date=</code><i>DATE</i></p>
<dd> Archive messages older than <i>DATE</i>. <i>DATE</i> can be a date string in ISO format (eg &#8216;2002-04-23&#8242;), Internet format (eg &#8217;23 Apr 2002&#8242;) or Internet format with full month names (eg &#8217;23 April 2002&#8217;). Two-digit years are not supported. This option is incompatible with the <code>&#8211;days</code> option above.</p>
<dt><code> -o </code><i>PATH</i><code>, &#8211;output-dir=</code><i>PATH</i></p>
<dd> Use the directory name <i>PATH</i> to store the mailbox archives. The default is the same directory as the mailbox to be read.</p>
<dt><code> -P </code><i>FILE</i><code>, &#8211;pwfile=</code><i>FILE</i></p>
<dd> Read IMAP password from file <i>FILE</i> instead of from the command line. Note that this will probably not work if you are archiving folders from more than one IMAP account.</p>
<dt><code> -F </code><i>STRING</i><code>, &#8211;filter-append=</code><i>STRING</i></p>
<dd> Append <i>STRING</i> to the IMAP filter string. For IMAP wizards.</p>
<dt><code> -s </code><i>NAME</i><code>, &#8211;suffix=</code><i>NAME</i></p>
<dd> Use the suffix <i>NAME</i> to create the filename used for archives. The default is <i>_archive</i>. For example, if you run <code>archivemail</code> on a mailbox called <i>exsouthrock</i>, the archive will be created with the filename <i>exsouthrock_archive.gz</i>. </p>
<p> <i>NAME</i> is run through the <code><a href="/docs/linux/man/1-python/">python</a></code>(1) <code>time.strftime()</code> function, which means that you can specify any of the following special directives in <i>NAME</i> to make archives named after the archive cut-off date:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> <code>%a</code> Locale&#8217;s abbreviated weekday name.</p>
<dt>*</p>
<dd> <code>%A</code> Locale&#8217;s full weekday name.</p>
<dt>*</p>
<dd> <code>%b</code> Locale&#8217;s abbreviated month name.</p>
<dt>*</p>
<dd> <code>%B</code> Locale&#8217;s full month name.</p>
<dt>*</p>
<dd> <code>%c</code> Locale&#8217;s appropriate date and time representation.</p>
<dt>*</p>
<dd> <code>%d</code> Day of the month as a decimal number [01,31].</p>
<dt>*</p>
<dd> <code>%H</code> Hour (24-hour clock) as a decimal number [00,23].</p>
<dt>*</p>
<dd> <code>%I</code> Hour (12-hour clock) as a decimal number [01,12].</p>
<dt>*</p>
<dd> <code>%j</code> Day of the year as a decimal number [001,366].</p>
<dt>*</p>
<dd> <code>%m</code> Month as a decimal number [01,12].</p>
<dt>*</p>
<dd> <code>%M</code> Minute as a decimal number [00,59].</p>
<dt>*</p>
<dd> <code>%p</code> Locale&#8217;s equivalent of either AM or PM.</p>
<dt>*</p>
<dd> <code>%S</code> Second as a decimal number [00,61]. (1)</p>
<dt>*</p>
<dd> <code>%U</code> Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.</p>
<dt>*</p>
<dd> <code>%w</code> Weekday as a decimal number [0(Sunday),6].</p>
<dt>*</p>
<dd> <code>%W</code> Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.</p>
<dt>*</p>
<dd> <code>%x</code> Locale&#8217;s appropriate date representation.</p>
<dt>*</p>
<dd> <code>%X</code> Locale&#8217;s appropriate time representation.</p>
<dt>*</p>
<dd> <code>%y</code> Year without century as a decimal number [00,99].</p>
<dt>*</p>
<dd> <code>%Y</code> Year with century as a decimal number.</p>
<dt>*</p>
<dd> <code>%Z</code> Time zone name (or by no characters if no time zone exists).</p>
<dt>*</p>
<dd> <code>%%</code> A literal &quot;%&quot; character.</dl>
</dl>
<dt><code> -S </code><i>NUM</i><code>, &#8211;size=</code><i>NUM</i></p>
<dd> Only archive messages that are <i>NUM</i> bytes or greater.</p>
<dt><code> -n, &#8211;dry-run</code></p>
<dd> Don&#8217;t write to any files &#8212; just show what would have been done. This is useful for testing to see how many messages would have been archived.</p>
<dt><code> -u, &#8211;preserve-unread</code></p>
<dd> Do not archive any messages that have not yet been read. <code>archivemail</code> determines if a message in a <code>mbox</code>-format or <code>MH</code>-format mailbox has been read by looking at the <code>Status</code> header (if it exists). If the status header is equal to &#8216;RO&#8217; or &#8216;OR&#8217; then <code>archivemail</code> assumes the message has been read. <code>archivemail</code> determines if a <code>maildir</code> message has been read by looking at the filename. If the filename contains an &#8216;S&#8217; after <i>:2,</i> then it assumes the message has been read.</p>
<dt><code> &#8211;dont-mangle</code></p>
<dd> Do not mangle lines in message bodies beginning with &quot;From &quot;. When archiving a message from a mailbox not in <code>mbox</code> format, by default <code>archivemail</code> mangles such lines by prepending a &#8216;&gt;&#8217; to them, since mail user agents might otherwise interpret these lines as message separators. Messages from <code>mbox</code> folders are never mangled. See <code><a href="/docs/linux/man/5-mbox/">mbox</a></code>(5) for more information.</p>
<dt><code> &#8211;delete</code></p>
<dd> Delete rather than archive old mail. Use this option with caution!</p>
<dt><code> &#8211;copy</code></p>
<dd> Copy rather than archive old mail. Creates an archive, but the archived messages are not deleted from the originating mailbox, which is left unchanged. This is a complement to the <code>&#8211;delete</code> option, and mainly useful for testing purposes.</p>
<dt><code> &#8211;include-flagged</code></p>
<dd> Normally messages that are flagged important are not archived or deleted. If you specify this option, these messages can be archived or deleted just like any other message.</p>
<dt><code> &#8211;no-compress</code></p>
<dd> Do not compress any archives.</p>
<dt><code> &#8211;warn-duplicate</code></p>
<dd> Warn about duplicate <code>Message-ID</code>s that appear in the input mailbox.</p>
<dt><code> -v, &#8211;verbose</code></p>
<dd> Reports lots of extra debugging information about what is going on.</p>
<dt><code> -q, &#8211;quiet</code></p>
<dd> Turns on quiet mode. Do not print any statistics about how many messages were archived. This should be used if you are running <code>archivemail</code> from cron.</p>
<dt><code> -V, &#8211;version</code></p>
<dd> Display the version of <code>archivemail</code> and exit.</p>
<dt><code> -h, &#8211;help</code></p>
<dd> Display brief summary information about how to run <code>archivemail</code>.</dl>
<h2>NOTES</h2>
<p> <code>archivemail</code> requires <code><a href="/docs/linux/man/1-python/">python</a></code>(1) version 2.3 or later. When reading an <code>mbox</code>-format mailbox, <code>archivemail</code> will create a lockfile with the extension <i>.lock</i> so that procmail will not deliver to the mailbox while it is being processed. It will also create an advisory lock on the mailbox using <code><a href="/docs/linux/man/2-flock/">flock</a></code>(2). <code>archivemail</code> will also complain and abort if a 3rd-party modifies the mailbox while it is being read. </p>
<p> <code>archivemail</code> will always attempt to preserve the mode, last-access and last-modify times of the input mailbox. However, archive mailboxes are always created with a mode of <code>0600</code>. If <code>archivemail</code> finds a pre-existing archive mailbox it will append rather than overwrite that archive. <code>archivemail</code> will refuse to operate on mailboxes that are symbolic links or create tempfiles or archives in world-writable directories. </p>
<p> <code>archivemail</code> attempts to find the delivery date of a message by looking for valid dates in the following headers, in order of precedence: <code>Delivery-date</code>, <code>Date</code> and <code>Resent-Date</code>. If it cannot find any valid date in these headers, it will use the last-modified file timestamp on <code>MH</code> and <code>Maildir</code> format mailboxes, or the date on the <code>From</code> line on <code>mbox</code>-format mailboxes. </p>
<p> A conversion from other formats to <code><a href="/docs/linux/man/5-mbox/">mbox</a></code>(5) will silently overwrite existing <code>Status</code> and <code>X-Status</code> message headers.</p>
<h3>IMAP</h3>
<p> When <code>archivemail</code> processes an <code>IMAP</code> folder, all messages in that folder will have their \Recent flag unset, and they will probably not show up as &#8216;new&#8217; in your user agent later on. There is no way around this, it&#8217;s just how <code>IMAP</code> works. This does not apply, however, if you run <code>archivemail</code> with the options <code>&#8211;dry-run</code> or <code>&#8211;copy</code>. </p>
<p> <code>archivemail</code> relies on server-side searches to determine the messages that should be archived. When matching message dates, <code>IMAP</code> servers refer to server internal message dates, and these may differ from both delivery time of a message and its <code>Date</code> header. Also, there exist broken servers which do not implement server side searches.</p>
<h3>IMAP URLS</h3>
<p> <code>archivemail</code>&#8216;s <code>IMAP</code> URL parser was written with the RFC 2882 (<i>Internet Message Format</i>) rules for the local-part of email addresses in mind. So, rather than enforcing an URL-style encoding of non-ascii and reserved characters, it allows to double-quote the username and password. If your username or password contains the delimiter characters &#8216;@&#8217; or &#8216;:&#8217;, just quote it like this: <i>imap://&quot;username [at] bogus.com&quot;:&quot;password&quot;@imap.bogus.com/mailbox</i>. You can use a backslash to escape double-quotes that are part of a quoted username or password. Note that quoting only a substring will not work, and be aware that your shell will probably remove unprotected quotes or backslashes. </p>
<p> <code>IMAP</code> servers supporting subfolders may use any character as a mailbox path separator, that is, as an equivalent to the slash character on Unix systems. If you are archiving an IMAP subfolder, first <code>archivemail</code> will try to open a given mailbox name unchanged; if this fails, it will interpret any slashes in the URL as path separators and try again.</p>
<h2>EXAMPLES</h2>
<p> To archive all messages in the mailbox <i>debian-user</i> that are older than 180 days to a compressed mailbox called <i>debian-user_archive.gz</i> in the current directory: </p>
<pre>
bash$ <code>archivemail debian-user</code>
</pre>
<p> To archive all messages in the mailbox <i>debian-user</i> that are older than 180 days to a compressed mailbox called <i>debian-user_October_2001.gz</i> (where the current month and year is April, 2002) in the current directory: </p>
<pre>
bash$ <code>archivemail --suffix '_%B_%Y' debian-user</code>
</pre>
<p> To archive all messages in the mailbox <i>cm-melb</i> that are older than the first of January 2002 to a compressed mailbox called <i>cm-melb_archive.gz</i> in the current directory: </p>
<pre>
bash$ <code>archivemail --date'1 Jan 2002' cm-melb</code>
</pre>
<p> Exactly the same as the above example, using an ISO date format instead: </p>
<pre>
bash$ <code>archivemail --date=2002-01-01 cm-melb</code>
</pre>
<p> To delete all messages in the mailbox <i>spam</i> that are older than 30 days: </p>
<pre>
bash$ <code>archivemail --delete --days=30 spam</code>
</pre>
<p> To archive all read messages in the mailbox <i>incoming</i> that are older than 180 days to a compressed mailbox called <i>incoming_archive.gz</i> in the current directory: </p>
<pre>
bash$ <code>archivemail --preserve-unread incoming</code>
</pre>
<p> To archive all messages in the mailbox <i>received</i> that are older than 180 days to an uncompressed mailbox called <i>received_archive</i> in the current directory: </p>
<pre>
bash$ <code>archivemail --no-compress received</code>
</pre>
<p> To archive all mailboxes in the directory <i>$HOME/Mail</i> that are older than 90 days to compressed mailboxes in the <i>$HOME/Mail/Archive</i> directory: </p>
<pre>
bash$ <code>archivemail -d90 -o $HOME/Mail/Archive $HOME/Mail/*</code>
</pre>
<p> To archive all mails older than 180 days from the given <code>IMAP</code> INBOX to a compressed mailbox INBOX_archive.gz in the <i>$HOME/Mail/Archive</i> directory, quoting the password and reading it from the environment variable <code>PASSWORD</code>: </p>
<pre>
bash$ <code>archivemail -o $HOME/Mail/Archive <a href="imaps://user:'">imaps://user:'</a>&quot;'$PASSWORD'&quot;'@example.org/INBOX</code> 
</pre>
<p> Note the protected quotes.</p>
<h2>TIPS</h2>
<p> Probably the best way to run <code>archivemail</code> is from your <code><a href="/docs/linux/man/5-crontab/">crontab</a></code>(5) file, using the <code>&#8211;quiet</code> option. Don&#8217;t forget to try the <code>&#8211;dry-run</code> and perhaps the <code>&#8211;copy</code> option for non-destructive testing.</p>
<h2>EXIT STATUS</h2>
<p> Normally the exit status is 0. Nonzero indicates an unexpected error.</p>
<h2>BUGS</h2>
<p> If an <code>IMAP</code> mailbox path contains slashes, the archive filename will be derived from the basename of the mailbox. If the server&#8217;s folder separator differs from the Unix slash and is used in the <code>IMAP</code> URL, however, the whole path will be considered the basename of the mailbox. E.g. the two URLs <code><a href="imap://user@example.com/folder/subfolder">imap://user@example.com/folder/subfolder</a></code> and <code><a href="imap://user@example.com/folder.subfolder">imap://user@example.com/folder.subfolder</a></code> will be archived in <i>subfolder_archive.gz</i> and <i>folder.subfolder_archive.gz</i>, respectively, although they might refer to the same <code>IMAP</code> mailbox. </p>
<p> <code>archivemail</code> does not support reading <code>MMDF</code> or <code>Babyl</code>-format mailboxes. In fact, it will probably think it is reading an <code>mbox</code>-format mailbox and cause all sorts of problems. </p>
<p> <code>archivemail</code> is still too slow, but if you are running from <code><a href="/docs/linux/man/5-crontab/">crontab</a></code>(5) you won&#8217;t care. Archiving <code>maildir</code>-format mailboxes should be a lot quicker than <code>mbox</code>-format mailboxes since it is less painful for the original mailbox to be reconstructed after selective message removal.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-python/">python</a></code>(1), <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1), <code><a href="/docs/linux/man/1-mutt/">mutt</a></code>(1), <code><a href="/docs/linux/man/1-procmail/">procmail</a></code>(1)</p>
<h2>URL</h2>
<p> The <code>archivemail</code> home page is currently hosted at sourceforge &lt;URL:<a rel="nofollow" href="http://archivemail.sourceforge.net">http://archivemail.sourceforge.net</a>&gt;</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Paul Rodger &lt;paul at paulrodger dot com&gt;. Updated and supplemented by Nikolaus Schulz &lt;microschulz [at] web.de&gt; </p>
<h2>Index</h2>
