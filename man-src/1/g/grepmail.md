---
title: "grepmail(1)"
name: "grepmail"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grepmail/"
description: "grepmail – search mailboxes for mail matching a regular expression"
---

<h2 class="name">NAME</h2>
<p> grepmail &#8211; search mailboxes for mail matching a regular expression </p>
<h2>SYNOPSIS</h2>
<pre><code>
grepmail[--help | --version][-abBDFhHilLmrRuvVw][-C&lt;cache - file&gt;]
        [-j&lt;status&gt;][-s&lt;sizespec&gt;][-d&lt;date - specification&gt;]
        [-X&lt;signature - pattern&gt;][-Y&lt;header - pattern&gt;]
        [[-e]&lt;pattern&gt; | -E&lt;expr&gt; | -f&lt;pattern - file&gt;]&lt;files...&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<dl>
<dt>
<dd> <i>grepmail</i> looks for mail messages containing a pattern, and prints the resulting messages on standard out. </p>
<p> By default <i>grepmail</i> looks in both header and body for the specified pattern. </p>
<p> When redirected to a file, the result is another mailbox, which can, in turn, be handled by standard User Agents, such as <i>elm</i>, or even used as input for another instance of <i>grepmail</i>. </p>
<p> At least one of <code>-E</code>, <code>-e</code>, <code>-d</code>, <code>-s</code>, or <code>-u</code> must be specified. The pattern is optional if <code>-d</code>, <code>-s</code>, and/or <code>-u</code> is used. The <code>-e</code> flag is optional if there is no file whose name is the pattern. The <code>-E</code> option can be used to specify complex search expressions involving logical operators. (See below.) </p>
<p> If a mailbox can not be found, grepmail first searches the directory specified by the <font SIZE="-1">MAILDIR</font> environment variable (if one is defined), then searches the <tt>$HOME</tt>/mail, <tt>$HOME</tt>/Mail, and <tt>$HOME</tt>/Mailbox directories.</dl>
<h2>OPTIONS AND ARGUMENTS</h2>
<p> Many of the options and arguments are analogous to those of grep.</p>
<dl>
<dt><code>pattern</code></p>
<dd> The pattern to search for in the mail message. May be any Perl regular expression, but should be quoted on the command line to protect against globbing (shell expansion). To search for more than one pattern, use the form &#8220;(pattern1|pattern2|&#8230;)&#8221;. </p>
<p> Note that complex pattern features such as &#8220;(?&gt;&#8230;)&#8221; require that you use a version of perl which supports them. You can use the pattern &#8220;()&#8221; to indicate that you do not want to match anything. This is useful if you want to initialize the cache without printing any output.</p>
<dt><code>mailbox</code></p>
<dd> Mailboxes must be traditional, <font SIZE="-1">UNIX</font> <tt>&quot;/bin/mail&quot;</tt> mailbox format. The mailboxes may be compressed by gzip, or bzip2, in which case gunzip, or bzip2 must be installed on the system. </p>
<p> If no mailbox is specified, takes input from stdin, which can be compressed or not. grepmail&#8217;s behavior is undefined when <font SIZE="-1">ASCII</font> and binary data is piped together as input.</p>
<dt><code>-a</code></p>
<dd> Use arrival date instead of sent date.</p>
<dt><code>-b</code></p>
<dd> Asserts that the pattern must match in the body of the email.</p>
<dt><code>-B</code></p>
<dd> Print the body but with only minimal (&#8216;From &#8216;, &#8216;From:&#8217;, &#8216;Subject:&#8217;, &#8216;Date:&#8217;) headers. This flag can be used with -H, in which case it will print only short headers and no email bodies.</p>
<dt><code>-C</code></p>
<dd> Specifies the location of the cache file. The default is <tt>$HOME</tt>/.grepmail-cache.</p>
<dt><code>-D</code></p>
<dd> Enable debug mode, which prints diagnostic messages.</p>
<dt><code>-d</code></p>
<dd> Date specifications must be of the form of:<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; a date like&nbsp;<wbr>&#8220;today&#8221;,&nbsp;<wbr>&#8220;yesterday&#8221;,&nbsp;<wbr>&#8220;5/18/93&#8221;,&nbsp;<wbr>&#8220;5 days ago&#8221;,&nbsp;<wbr>&#8220;5 weeks ago&#8221;,<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr><font SIZE="-1">OR</font>&nbsp;<wbr>&#8220;before&#8221;,&nbsp;<wbr>&#8220;after&#8221;, or&nbsp;<wbr>&#8220;since&#8221;, followed by a date as defined above,<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr><font SIZE="-1">OR</font>&nbsp;<wbr>&#8220;between&nbsp;<wbr>&lt;date&gt;&nbsp;<wbr>and&nbsp;<wbr>&lt;date&gt;&#8221;, where&nbsp;<wbr>&lt;date&gt;&nbsp;<wbr>is defined as above. </p>
<p> Simple date expressions will first be parsed by Date::Parse. If this fails, grepmail will attempt to parse the date with Date::Manip, if the module is installed on the system. Use an empty pattern (i.e. <code>-d &quot;&quot;</code>) to find emails without a &#8220;Date: &#8230;&#8221; line in the header. </p>
<p> Date specifications without times are interpreted as having a time of midnight of that day (which is the morning), except for &#8220;after&#8221; and &#8220;since&#8221; specifications, which are interpreted as midnight of the following day. For example, &#8220;between today and tomorrow&#8221; is the same as simply &#8220;today&#8221;, and returns emails whose date has the current day. (&#8220;now&#8221; is interpreted as &#8220;today&#8221;.) The date specification &#8220;after July 5th&#8221; will return emails whose date is midnight July 6th or later.</p>
<dt><code>-E</code></p>
<dd> Specify a complex search expression using logical operators. The current syntax allows the user to specify search expressions using Perl syntax. Three values can be used: <tt>$email</tt> (the entire email message), <tt>$email_header</tt> (just the header), or <tt>$email_body</tt> (just the body). A search is specified in the form &#8220;$email =~ /pattern/&#8221;, and multiple searches can be combined using &#8220;&amp;&amp;&#8221; and &#8220;||&#8221; for &#8220;and&#8221; and &#8220;or&#8221;. </p>
<p> For example, the expression </p>
<pre>
  $email_header =~ /^From: .*\@coppit.org/ &amp;&amp; $email =~ /grepmail/i
</pre>
<p> will find all emails which originate from coppit.org (you must escape the &#8220;@&#8221; sign with a backslash), and which contain the keyword &#8220;grepmail&#8221; anywhere in the message, in any capitalization. </p>
<p> <code>-E</code> is incompatible with <code>-b</code>, <code>-h</code>, and <code>-e</code>. <code>-i</code>, <code>-M</code>, <code>-S</code>, and <code>-Y</code> have not yet been implemented. </p>
<p> <font SIZE="-1">NOTE:</font> The syntax of search expressions may change in the future. In particular, support for size, date, and other constraints may be added. The syntax may also be simplified in order to make expression formation easier to use (and perhaps at the expense of reduced functionality).</p>
<dt><code>-e</code></p>
<dd> Explicitly specify the search pattern. This is useful for specifying patterns that begin with &#8220;-&#8221;, which would otherwise be interpreted as a flag.</p>
<dt><code>-f</code></p>
<dd> Obtain patterns from <font SIZE="-1">FILE</font>, one per line. The empty file contains zero patterns, and therefore matches nothing.</p>
<dt><code>-F</code></p>
<dd> Force grepmail to process all files and streams as though they were mailboxes. (i.e. Skip checks for non-mailbox <font SIZE="-1">ASCII</font> files or binary files that don&#8217;t look like they are compressed using known schemes.)</p>
<dt><code>-h</code></p>
<dd> Asserts that the pattern must match in the header of the email.</p>
<dt><code>-H</code></p>
<dd> Print the header but not body of matching emails.</p>
<dt><code>-i</code></p>
<dd> Make the search case-insensitive (by analogy to <i>grep -i</i>).</p>
<dt><code>-j</code></p>
<dd> Asserts that the email &#8220;Status:&#8221; header must contain the given flags. Order and case are not important, so use <i>-j </i><font SIZE="-1"><i>AR</i></font><i></i> or <i>-j ra</i> to search for emails which have been read and answered.</p>
<dt><code>-l</code></p>
<dd> Output the names of files having an email matching the expression, (by analogy to <i>grep -l</i>).</p>
<dt><code>-L</code></p>
<dd> Follow symbolic links. (Implies <i>-R</i>)</p>
<dt><code>-M</code></p>
<dd> Causes grepmail to ignore non-text <font SIZE="-1">MIME</font> attachments. This removes false positives resulting from binaries encoded as <font SIZE="-1">ASCII</font> attachments.</p>
<dt><code>-m</code></p>
<dd> Append &#8220;X-Mailfolder: &lt;folder&gt;&#8221; to all email headers, indicating which folder contained the matched email.</p>
<dt><code>-n</code></p>
<dd> Prefix each line with line number information. If multiple files are specified, the filename will precede the line number. <font SIZE="-1">NOTE:</font> When used in conjunction with <code>-m</code>, the X-Mailfolder header has the same line number as the next (blank) line.</p>
<dt><code>-q</code></p>
<dd> Quiet mode. Suppress the output of warning messages about non-mailbox files, directories, etc.</p>
<dt><code>-r</code></p>
<dd> Generate a report of the names of the files containing emails matching the expression, along with a count of the number of matching emails.</p>
<dt><code>-R</code></p>
<dd> Causes grepmail to recurse any directories encountered.</p>
<dt><code>-s</code></p>
<dd> Return emails which match the size (in bytes) specified with this flag. Note that this size includes the length of the header. </p>
<p> Size constraints must be of the form of:<br />
&nbsp;<wbr>&#8211; 12345: match size of exactly 12345<br />
&nbsp;<wbr>&#8211;&nbsp;<wbr>&lt;12345,&nbsp;<wbr>&lt;=12345,&nbsp;<wbr>&gt;12345,&nbsp;<wbr>&gt;=12345: match size less than, less than or equal,<br />
greater than, or greater than or equal to 12345<br />
&nbsp;<wbr>&#8211; 10000-12345: match size between 10000 and 12345 inclusive</p>
<dt><code>-S</code></p>
<dd> Ignore signatures. The signature consists of everything after a line consisting of &#8220;&#8211; &#8221;.</p>
<dt><code>-u</code></p>
<dd> Output only unique emails, by analogy to <i>sort -u</i>. Grepmail determines email uniqueness by the Message-ID header.</p>
<dt><code>-v</code></p>
<dd> Invert the sense of the search, by analogy to <i>grep -v</i>. This results in the set of emails printed being the complement of those that would be printed without the <code>-v</code> switch.</p>
<dt><code>-V</code></p>
<dd> Print the version and exit.</p>
<dt><code>-w</code></p>
<dd> Search for only those lines which contain the pattern as part of a word group. That is, the start of the pattern must match the start of a word, and the end of the pattern must match the end of a word. (Note that the start and end need not be for the <i>same</i> word.) </p>
<p> If you are familiar with Perl regular expressions, this flag simply puts a &#8220;&#8221; before and after the search pattern.</p>
<dt><code>-X</code></p>
<dd> Specify a regular expression for the signature separator. By default this pattern is &#8216;^&#8211; $&#8217;.</p>
<dt><code>-Y</code></p>
<dd> Specify a pattern which indicates specific headers to be searched. The search will automatically treat headers which span multiple lines as one long line. This flag implies <code>-h</code>. </p>
<p> In the style of procmail, special strings in the pattern will be expanded as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> If the regular expression contains &#8220;^TO:&#8221; it will be substituted by </p>
<pre>
  ^((Original-)?(Resent-)?(To|Cc|Bcc)|(X-Envelope|Apparently(-Resent)?)-To):
</pre>
<p> which should match all headers with destination addresses. </p>
<p> If the regular expression contains &#8220;^FROM_DAEMON:&#8221; it will be substituted by </p>
<p>  (^(Mailing-List:|Precedence:.*(junk|bulk|list)|To: Multiple recipients of |(((Resent-)?(From|Sender)|X-Envelope-From):|&gt;?From )([^&gt;]*[^(.% [at] a-z0-9])?(Post(ma?(st(e?r)?|n)|office)|(send)?Mail(er)?|daemon|m(mdf|ajordomo)|n?uucp|LIST(SERV|proc)|NETSERV|o(wner|ps)|r(e(quest|sponse)|oot)|b(ounce|bs\.smtp)|echo|mirror|s(erv(ices?|er)|mtp(error)?|ystem)|A(dmin(istrator)?|MMGR|utoanswer))(([^).!:a-z0-9][-_a-z0-9]*)?[%@&gt;	 ][^&lt;)]*(\(.*\).*)?)?</p>
<p> which should catch mails coming from most daemons. </p>
<p> If the regular expression contains &#8220;^FROM_MAILER:&#8221; it will be substituted by </p>
<pre><code>
  (^(((Resent-)?(From|Sender)|X-Envelope-From):|&gt;?From)([^&gt;]*[^(.% [at] a-z0-9])?(Post(ma(st(er)?|n)|office)|(send)?Mail(er)?|daemon|mmdf|n?uucp|ops|r(esponse|oot)|(bbs\.)?smtp(error)?|s(erv(ices?|er)|ystem)|A(dmin(istrator)?|MMGR))(([^).!:a-z0-9][-_a-z0-9]*)?[%@&gt;	][^&lt;)]*(\(.*\).*)?)?$([^&gt;]|$))
</code></pre>
<p> (a stripped down version of &#8220;^FROM_DAEMON:&#8221;), which should catch mails coming from most mailer-daemons. </p>
<p> So, to search for all emails to or from &#8220;Andy&#8221;: </p>
<pre>
  grepmail -Y '(^TO:|^From:)' Andy mailbox
</pre>
</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;help</code></p>
<dd> Print a help message summarizing the usage.</p>
<dt><code>&#8212;</code></p>
<dd> All arguments following <i>&#8212;</i> are treated as mail folders.</dl>
<h2>EXAMPLES</h2>
<p> Count the number of emails. (&#8220;.&#8221; matches every email.) </p>
<pre>
  grepmail -r . sent-mail
</pre>
<p> Get all email between 2000 and 3000 bytes about books </p>
<pre>
  grepmail books -s 2000-3000 sent-mail
</pre>
<p> Get all email that you mailed yesterday </p>
<pre>
  grepmail -d yesterday sent-mail
</pre>
<p> Get all email that you mailed before the first thursday in June 1998 that pertains to research (requires Date::Manip): </p>
<pre>
  grepmail research -d &quot;before 1st thursday in June 1998&quot; sent-mail
</pre>
<p> Get all email that you mailed before the first of June 1998 that pertains to research: </p>
<pre>
  grepmail research -d &quot;before 6/1/98&quot; sent-mail
</pre>
<p> Get all email you received since 8/20/98 that wasn&#8217;t about research or your job, ignoring case: </p>
<pre>
  grepmail -iv &quot;(research|job)&quot; -d &quot;since 8/20/98&quot; saved-mail
</pre>
<p> Get all email about mime but not about Netscape. Constrain the search to match the body, since most headers contain the text &#8220;mime&#8221;: </p>
<pre>
  grepmail -b mime saved-mail | grepmail Netscape -v
</pre>
<p> Print a list of all mailboxes containing a message from Rodney. Constrain the search to the headers, since quoted emails may match the pattern: </p>
<pre>
  grepmail -hl &quot;^From.*Rodney&quot; saved-mail*
</pre>
<p> Find all emails with the text &#8220;Pilot&#8221; in both the header and the body: </p>
<pre>
  grepmail -hb &quot;Pilot&quot; saved-mail*
</pre>
<p> Print a count of the number of messages about grepmail in all saved-mail mailboxes: </p>
<pre>
  grepmail -br grepmail saved-mail*
</pre>
<p> Remove any duplicates from a mailbox: </p>
<pre>
  grepmail -u saved-mail
</pre>
<p> Convert a Gnus mailbox to mbox format: </p>
<pre>
  grepmail . gnus-mailbox-dir/* &gt; mbox
</pre>
<p> Search for all emails to or from an address (taking into account wrapped headers and different header names): </p>
<pre>
  grepmail -Y '(^TO:|^From:)' my [at] email.address saved-mail
</pre>
<p> Find all emails from postmasters: </p>
<pre>
  grepmail -Y '^FROM_MAILER:' . saved-mail
</pre>
<h2>FILES</h2>
<p> grepmail will <i>not</i> create temporary files while decompressing compressed archives. The last version to do this was 3.5. While the new design uses more memory, the code is much simpler, and there is less chance that email can be read by malicious third parties. Memory usage is determined by the size of the largest email message in the mailbox.</p>
<h2>ENVIRONMENT</h2>
<p> The <font SIZE="-1">MAILDIR</font> environment variable can be used to specify the default mail directory. This directory will be searched if the specified mailbox can not be found directly. </p>
<p> The <font SIZE="-1">HOME</font> environment variable is also used to find mailboxes if they can not be found directly. It is also used to store grepmail state information such as its cache file.</p>
<h2>BUGS AND LIMITATIONS</h2>
<dl>
<dt>Patterns containing $ may cause problems</p>
<dd> Currently I look for &#8220;$&#8221; followed by a non-word character and replace it with the line ending for the current file (either &#8220;
&#8221; or &#8220;
&#8221;). This may cause problems with complex patterns specified with -E, but I&#8217;m not aware of any.</p>
<dt>Mails without bodies cause problems</p>
<dd> According to <font SIZE="-1">RFC</font> 822, mail messages need not have message bodies. I&#8217;ve found and removed one bug related to this. I&#8217;m not sure if there are others.</p>
<dt>Complex single-point dates not parsed correctly</p>
<dd> If you specify a point date like &#8220;September 1, 2004&#8221;, grepmail creates a date range that includes the entire day of September 1, 2004. If you specify a complex point date such as &#8220;today&#8221;, &#8220;1st Monday in July&#8221;, or &#8220;9/1/2004 at 0:00&#8221; grepmail may parse the time incorrectly. </p>
<p> The reason for this problem is that Date::Manip, as of version 5.42, forces default values for parsed dates and times. This means that grepmail has a hard time determining whether the user supplied certain time/date fields. (e.g. Did Date::Manip provide a default time of 0:00, or did the user specify it?) grepmail tries to work around this problem, but the workaround is inherently incomplete in some rare cases.</p>
<dt>File names that look like flags cause problems.</p>
<dd> In some special circumstances, grepmail will be confused by files whose names look like flags. In such cases, use the <code>-e</code> flag to specify the search pattern.</dl>
<h2>LICENSE</h2>
<p> This code is distributed under the <font SIZE="-1">GNU</font> General Public License (<font SIZE="-1">GPL</font>). See the file <font SIZE="-1">LICENSE</font> in the distribution, <a rel="nofollow" href="http://www.opensource.org/gpl-license.html,">http://www.opensource.org/gpl-license.html,</a> and <a rel="nofollow" href="http://www.opensource.org/.">http://www.opensource.org/.</a></p>
<h2>AUTHOR</h2>
<p> David Coppit &lt;david [at] coppit.org&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-elm/">elm</a></i>(1), <i><a href="/docs/linux/man/1-mail/">mail</a></i>(1), <i><a href="/docs/linux/man/1-grep/">grep</a></i>(1), <i><a href="/docs/linux/man/1-perl/">perl</a></i>(1), <i><a href="/docs/linux/man/1-printmail/">printmail</a></i>(1), <i><a href="/docs/linux/man/3-mail--internet/">Mail::Internet</a></i>(3), <i><a href="/docs/linux/man/5-procmailrc/">procmailrc</a></i>(5). Crocker, D. H., Standard for the Format of Arpa Internet Text Messages, <font SIZE="-1">RFC</font> 822. </p>
<h2>Index</h2>
