---
title: "mairix(1)"
name: "mairix"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mairix/"
description: "mairix – index and search mail folders"
---

<h2 class="name">NAME</h2>
<p> mairix &#8211; index and search mail folders </p>
<h2>SYNOPSIS</h2>
<h3>Indexing</h3>
<p> <code>mairix</code> [ <code>-v</code>|<code>&#8211;verbose</code> ] [ <code>-p</code>|<code>&#8211;purge</code> ] [ <code>-f</code>|<code>&#8211;rcfile</code> <i>mairixrc</i> ] [ <code>-F</code>|<code>&#8211;fast-index</code> ] </p>
<h3>Searching</h3>
<p> <code>mairix</code> [ <code>-v</code>|<code>&#8211;verbose</code> ] [ <code>-f</code>|<code>&#8211;rcfile</code> <i>mairixrc</i> ] [ <code>-r</code>|<code>&#8211;raw-output</code> ] [ <code>-x</code>|<code>&#8211;excerpt-output</code> ] [ <code>-o</code>|<code>&#8211;mfolder</code> <i>mfolder</i> ] [ <code>-a</code>|<code>&#8211;augment</code> ] [ <code>-t</code>|<code>&#8211;threads</code> ] <i>search-patterns</i> </p>
<h3>Other</h3>
<p> <code>mairix</code> [ <code>-h</code>|<code>&#8211;help</code> ] </p>
<p> <code>mairix</code> [ <code>-V</code>|<code>&#8211;version</code> ] </p>
<p> <code>mairix</code> [ <code>-d</code>|<code>&#8211;dump</code> ] </p>
<h2>DESCRIPTION</h2>
<p> <i>mairix</i> indexes and searches a collection of email messages. The folders containing the messages for indexing are defined in the configuration file. The indexing stage produces a database file. The database file provides rapid access to details of the indexed messages during searching operations. A search normally produces a folder (so-called <code>mfolder</code>) containing the matched messages. However, a raw mode (<code>-r</code>) exists which just lists the matched messages instead. </p>
<p> It can operate with the following folder types</p>
<dl>
<dt>*</p>
<dd> maildir</p>
<dt>*</p>
<dd> MH (compatible with the MH folder formats used by xmh, sylpheed, nnml (Gnus) and evolution)</p>
<dt>*</p>
<dd> mbox (including mboxes that have been compressed with gzip or bzip2)</dl>
<p> If maildir or MH source folders are used, and a search outputs its matches to an mfolder in maildir or MH format, symbolic links are used to reference the original messages inside the mfolder. However, if mbox folders are involved, copies of messages are made instead. </p>
<h2>OPTIONS</h2>
<p> <code>mairix</code> decides whether indexing or searching is required by looking for the presence of any <i>search-patterns</i> on the command line. </p>
<h3>Special modes</h3>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>
 Show usage summary and exit </p>
<dt><code>-V, &#8211;version</code></p>
<dd> Show program version and exit </p>
<dt><code>-d</code></p>
<dd>
 Dump the database&#8217;s contents in human-readable form to stdout. </p>
</dl>
<h3>General options</h3>
<dl>
<dt><code>-f </code><i>mairixrc</i></p>
<dd>
<dt><code>&#8211;rcfile </code><i>mairixrc</i></p>
<dd>
 Specify an alternative configuration file to use. The default configuration file is <i>~/.mairixrc</i>. </p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>
 Make the output more verbose </p>
<dt><code>-Q, &#8211;no-integrity-checks</code></p>
<dd>
 Normally <i>mairix</i> will do some internal integrity tests on the database. The <code>-Q</code> option removes these checks, making <i>mairix</i> run faster, but it will be less likely to detect internal problems if any bugs creep in. </p>
<p> The <i>nochecks</i> directive in the rc file has the same effect. </p>
<dt><code>&#8211;unlock</code></p>
<dd>
 <i>mairix</i> locks its database file during any indexing or searching operation to prevent multiple indexing runs intefering with each other, or an indexing run interfering with search runs. The <code>&#8211;unlock</code> option removes the lockfile before doing the requested indexing or searching operation. This is a convenient way of cleaning up a stale lockfile if an earlier run crashed for some reason or was aborted. </p>
</dl>
<h3>Indexing options</h3>
<dl>
<dt><code>-p, &#8211;purge</code></p>
<dd>
 Cause stale (dead) messages to be purged from the database during an indexing run. (Normally, stale messages are left in the database because of the additional const of compacting away the storage that they take up.) </p>
<dt><code>-F, &#8211;fast-index</code></p>
<dd>
 When processing maildir and MH folders, <i>mairix</i> normally compares the mtime and size of each message against the values stored in the database. If they have changed, the message will be rescanned. This check requires each message file to be stat&#8217;ed. For large numbers of messages in these folder types, this can be a sizeable overhead. </p>
<p> This option tells <i>mairix</i> to assume that when a message currently on-disc has a name matching one already in the database, it should assume the message is unchanged. </p>
<p> A later indexing run without using this option will fix up any rescans that were missed due to its use. </p>
</dl>
<h3>Search options</h3>
<dl>
<dt><code>-a, &#8211;augment</code></p>
<dd>
 Append newly matches messages to the current mfolder instead of creating the mfolder from scratch. </p>
<dt><code>-t, &#8211;threads</code></p>
<dd>
 As well as returning the matched messages, also return every message in the same thread as one of the real matches. </p>
<dt><code>-r, &#8211;raw-output</code></p>
<dd>
 Instead of creating an mfolder containing the matched messages, just show their paths on stdout. </p>
<dt><code>-x, &#8211;excerpt-output</code></p>
<dd>
 Intead of creating an mfolder containing the matched messages, display an excerpt from their headers on stdout. The excerpt shows To, Cc, From, Subject and Date. </p>
<dt><code>-o </code><i>mfolder</i></p>
<dd>
<dt><code>&#8211;mfolder </code><i>mfolder</i></p>
<dd>
 Specify a temporary alternative path for the mfolder to use, overriding the <i>mfolder</i> directive in the rc file. </p>
<p> <code>mairix</code> will refuse to output search results into any folder that appears to be amongst those that are indexed. This is to prevent accidental deletion of emails. </p>
</dl>
<h3>Search patterns</h3>
<dl>
<dt><code>t:</code><i>word</i></p>
<dd>
 Match <i>word</i> in the To: header. </p>
<dt><code>c:</code><i>word</i></p>
<dd>
 Match <i>word</i> in the Cc: header. </p>
<dt><code>f:</code><i>word</i></p>
<dd>
 Match <i>word</i> in the From: header. </p>
<dt><code>s:</code><i>word</i></p>
<dd>
 Match <i>word</i> in the Subject: header. </p>
<dt><code>m:</code><i>word</i></p>
<dd>
 Match <i>word</i> in the Message-ID: header. </p>
<dt><code>b:</code><i>word</i></p>
<dd>
 Match <i>word</i> in the message body. </p>
<p> <code>Message body</code> is taken to mean any body part of type text/plain or text/html. For text/html, text within meta tags is ignored. In particular, the URLs inside &lt;A href=&quot;&#8230;&quot;&gt; tags are not currently indexed. Non-text attachments are ignored. If there&#8217;s an attachment of type message/rfc822, this is parsed and the match is performed on this sub-message too. If a hit occurs, the enclosing message is treated as having a hit. </p>
<dt><code>d:</code><i>[start-datespec]</i><code>&#8211;</code><i>[end-datespec]</i></p>
<dd>
 Match messages with Date: headers lying in the specific range. </p>
<dt><code>z:</code><i>[low-size]</i><code>&#8211;</code><i>[high-size]</i></p>
<dd>
 Match messages whose size lies in the specified range. If the <i>low-size</i> argument is omitted it defaults to zero. If the <i>high-size</i> argument is omitted it defaults to infinite size. </p>
<p> For example, to match messages between 10kbytes and 20kbytes in size, the following search term can be used: <code>1</code> mairix z:10k-20k</p>
<dt>
<dd>
<p> The suffix &#8216;k&#8217; on a number means multiply by 1024, and the suffix &#8216;M&#8217; on a number means multiply by 1024*1024. </p>
<dt><code>n:</code><i>word</i></p>
<dd>
 Match <i>word</i> occurring as the name of an attachment in the message. Since attachment names are usually long, this option would usually be used in the substring form. So <code>1</code> mairix n:mairix=</p>
<dt>
<dd>
<p> would match all messages which have attachments whose names contain the substring <i>mairix</i>. </p>
<p> The attachment name is determined from the name=xxx or filename=xxx qualifiers on the Content-Type: and Content-Disposition: headers respectively. </p>
<dt><code>F:</code><i>flags</i></p>
<dd>
 Match messages with particular flag settings. The available flags are &#8216;s&#8217; meaning seen, &#8216;r&#8217; meaning replied, and &#8216;f&#8217; meaning flagged. The flags are case-insensitive. A flag letter may be prefixed by a &#8216;-&#8216; to negate its sense. Thus </p>
<p> <code>1</code> mairix F:-s d:1w-</p>
<dt>
<dd>
<p> would match any unread message less than a week old, and </p>
<p> <code>1</code> mairix F:f-r d:-1m</p>
<dt>
<dd>
<p> would match any flagged message older than a month which you haven&#8217;t replied to yet. </p>
<p> Note that the flag characters and their meanings agree with those used as the suffix letters on message filenames in maildir folders. </p>
</dl>
<h3>Searching for a match amongst more than one part of a message</h3>
<p> Multiple body parts may be grouped together, if a match in any of them is sought. Common examples follow. </p>
<dl>
<dt><code>tc:</code><i>word</i></p>
<dd>
 Match <i>word</i> in either the To: or Cc: headers (or both). </p>
<dt><code>bs:</code><i>word</i></p>
<dd>
 Match <i>word</i> in either the Subject: header or the message body (or both). </p>
</dl>
<p> The <code>a:</code> search pattern is an abbreviation for <code>tcf:</code>; i.e. match the word in the To:, Cc: or From: headers. (&quot;a&quot; stands for &quot;address&quot; in this case.) </p>
<h3>Match words</h3>
<p> The <i>word</i> argument to the search strings can take various forms. </p>
<dl>
<dt><i>~word</i></p>
<dd>
 Match messages <code>not</code> containing the word. </p>
<dt><i>word1,word2</i></p>
<dd>
 This matches if both the words are matched in the specified message part. </p>
<dt><i>word1/word2</i></p>
<dd>
 This matches if either of the words are matched in the specified message part. </p>
<dt><i>substring=</i></p>
<dd>
 Match any word containing <i>substring</i> as a substring </p>
<dt><i>substring=N</i></p>
<dd>
 Match any word containing <i>substring</i>, allowing up to <i>N</i> errors in the match. For example, if <i>N</i> is 1, a single error is allowed, where an error can be</p>
<dt>*</p>
<dd> a missing letter</p>
<dt>*</p>
<dd> an extra letter</p>
<dt>*</p>
<dd> a different letter. </p>
<dt><i>^substring=</i></p>
<dd>
 Match any word containing <i>substring</i> as a substring, with the requirement that <i>substring</i> occurs at the beginning of the matched word. </p>
</dl>
<h3>Precedence matters</h3>
<p> The binding order of the constructions is: </p>
<dl>
<dt>1.</p>
<dd> Individual command line arguments define separate conditions which are AND-ed together </p>
<dt>2.</p>
<dd> Within a single argument, the letters before the colon define which message parts the expression applies to. If there is no colon, the expression applies to all the headers listed earlier and the body. </p>
<dt>3.</p>
<dd> After the colon, commas delineate separate disjuncts, which are OR-ed together. </p>
<dt>4.</p>
<dd> Each disjunct may contain separate conjuncts, which are separated by plus signs. These conditions are AND-ed together. </p>
<dt>5.</p>
<dd> Each conjunct may start with a tilde to negate it, and may be followed by a slash to indicate a substring match, optionally followed by an integer to define the maximum number of errors allowed. </p>
</dl>
<h3>Date specification</h3>
<p> This section describes the syntax used for specifying dates when searching using the `d:&#8217; option. </p>
<p> Dates are specified as a range. The start and end of the range can both be specified. Alternatively, if the start is omitted, it is treated as being the beginning of time. If the end is omitted, it is treated as the current time. </p>
<p> There are 4 basic formats:</p>
<dl>
<dt><code>d:</code><i>start-end</i></p>
<dd>
 Specify both start and end explicitly</p>
<dt><code>d:</code><i>start-</i></p>
<dd> Specify start, end is the current time</p>
<dt><code>d:</code><i>-end</i></p>
<dd> Specify end, start is &#8216;a long time ago&#8217; (i.e. early enough to include any message).</p>
<dt><code>d:</code><i>period</i></p>
<dd> Specify start and end implicitly, as the start and end of the period given. </p>
</dl>
<p> The start and end can be specified either absolute or relative. A relative endpoint is given as a number followed by a single letter defining the scaling: </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><code>letter </code></td>
<td><code> short for </code></td>
<td><code> example </code></td>
<td><code> meaning</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>d </td>
<td> days </td>
<td> 3d </td>
<td> 3 days
</td>
</tr>
<tr VALIGN=top>
<td>w </td>
<td> weeks </td>
<td> 2w </td>
<td> 2 weeks (14 days)
</td>
</tr>
<tr VALIGN=top>
<td>m </td>
<td> months </td>
<td> 5m </td>
<td> 5 months (150 days)
</td>
</tr>
<tr VALIGN=top>
<td>y </td>
<td> years </td>
<td> 4y </td>
<td> 4 years (4*365 days)
</td>
</tr>
</table>
</table>
<p> Months are always treated as 30 days, and years as 365 days, for this purpose. </p>
<p> Absolute times can be specified in many forms. Some forms have different meanings when they define a start date from that when they define an end date. Where a single expression specifies both the start and end (i.e. where the argument to d: doesn&#8217;t contain a `-&#8216;), it will usually have different interpretations in the two cases. </p>
<p> In the examples below, suppose the current date is Sunday May 18th, 2003 (when I started to write this material.) </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td>Example </td>
<td> Start date </td>
<td> End date </td>
<td> Notes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>d:20030301-20030425 </td>
<td> March 1st, 2003 </td>
<td> 25th April, 2003</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>d:030301-030425 </td>
<td> March 1st, 2003 </td>
<td> April 25th, 2003 </td>
<td> century assumed
</td>
</tr>
<tr VALIGN=top>
<td>d:mar1-apr25 </td>
<td> March 1st, 2003 </td>
<td> April 25th, 2003</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>d:Mar1-Apr25 </td>
<td> March 1st, 2003 </td>
<td> April 25th, 2003 </td>
<td> case insensitive
</td>
</tr>
<tr VALIGN=top>
<td>d:MAR1-APR25 </td>
<td> March 1st, 2003 </td>
<td> April 25th, 2003 </td>
<td> case insensitive
</td>
</tr>
<tr VALIGN=top>
<td>d:1mar-25apr </td>
<td> March 1st, 2003 </td>
<td> April 25th, 2003 </td>
<td> date and month in either order
</td>
</tr>
<tr VALIGN=top>
<td>d:2002 </td>
<td> January 1st, 2002 </td>
<td> December 31st, 2002 </td>
<td> whole year
</td>
</tr>
<tr VALIGN=top>
<td>d:mar </td>
<td> March 1st, 2003 </td>
<td> March 31st, 2003 </td>
<td> most recent March
</td>
</tr>
<tr VALIGN=top>
<td>d:oct </td>
<td> October 1st, 2002 </td>
<td> October 31st, 2002 </td>
<td> most recent October
</td>
</tr>
<tr VALIGN=top>
<td>d:21oct-mar </td>
<td> October 21st, 2002 </td>
<td> March 31st, 2003 </td>
<td> start before end
</td>
</tr>
<tr VALIGN=top>
<td>d:21apr-mar </td>
<td> April 21st, 2002 </td>
<td> March 31st, 2003 </td>
<td> start before end
</td>
</tr>
<tr VALIGN=top>
<td>d:21apr- </td>
<td> April 21st, 2003 </td>
<td> May 18th, 2003 </td>
<td> end omitted
</td>
</tr>
<tr VALIGN=top>
<td>d:-21apr </td>
<td> January 1st, 1900 </td>
<td> April 21st, 2003 </td>
<td> start omitted
</td>
</tr>
<tr VALIGN=top>
<td>d:6w-2w </td>
<td> April 6th, 2003 </td>
<td> May 4th, 2003 </td>
<td> both dates relative
</td>
</tr>
<tr VALIGN=top>
<td>d:21apr-1w </td>
<td> April 21st, 2003 </td>
<td> May 11th, 2003 </td>
<td> one date relative
</td>
</tr>
<tr VALIGN=top>
<td>d:21apr-2y </td>
<td> April 21st, 2001 </td>
<td> May 11th, 2001 </td>
<td> start before end
</td>
</tr>
<tr VALIGN=top>
<td>d:99-11 </td>
<td> January 1st, 1999 </td>
<td> May 11th, 2003 </td>
<td> 2 digits are a day of the month if possible, otherwise a year
</td>
</tr>
<tr VALIGN=top>
<td>d:99oct-1oct </td>
<td> October 1st, 1999 </td>
<td> October 1st, 2002 </td>
<td> end before now, single digit is a day of the month
</td>
</tr>
<tr VALIGN=top>
<td>d:99oct-01oct </td>
<td> October 1st, 1999 </td>
<td> October 31st, 2001 </td>
<td> 2 digits starting with zero treated as a year
</td>
</tr>
<tr VALIGN=top>
<td>d:oct99-oct1 </td>
<td> October 1st, 1999 </td>
<td> October 1st, 2002 </td>
<td> day and month in either order
</td>
</tr>
<tr VALIGN=top>
<td>d:oct99-oct01 </td>
<td> October 1st, 1999 </td>
<td> October 31st, 2001 </td>
<td> year and month in either order
</td>
</tr>
</table>
</table>
<p> The principles in the table work as follows.</p>
<dl>
<dt>*</p>
<dd> When the expression defines a period of more than a day (i.e. if a month or year is specified), the earliest day in the period is taken when the start date is defined, and the last day in the period if the end of the range is being defined.</p>
<dt>*</p>
<dd> The end date is always taken to be on or before the current date.</p>
<dt>*</p>
<dd> The start date is always taken to be on or before the end date. </p>
</dl>
<h2>SETTING UP THE MATCH FOLDER</h2>
<p> If the match folder does not exist when running in search mode, it is automatically created. For &#8216;mformat=maildir&#8217; (the default), this should be all you need to do. If you use &#8216;mformat=mh&#8217;, you may have to run some commands before your mailer will recognize the folder. e.g. for mutt, you could do </p>
<pre>
<dl><dt><dd>mkdir -p /home/richard/Mail/mfolder
touch /home/richard/Mail/mfolder/.mh_sequences
</dl>
</pre>
<p> which seems to work. Alternatively, within mutt, you could set MBOX_TYPE to in advance. </p>
<p> If you use Sylpheed, the best way seems to be to create the new folder from within Sylpheed before letting mairix write into it. </p>
<h2>EXAMPLES</h2>
<p> Suppose my email address is &lt;richard [at] doesnt.exist&gt;. </p>
<p> Either of the following will match all messages newer than 3 months from me with the word &#8216;chrony&#8217; in the subject line: </p>
<pre>
<dl><dt><dd>mairix d:3m- f:richard+doesnt+exist s:chrony
mairix d:3m- f:richard [at] doesnt.exist s:chrony
</dl>
</pre>
<p> Suppose I don&#8217;t mind a few spurious matches on the address, I want a wider date range, and I suspect that some messages I replied to might have had the subject keyword spelt wrongly (let&#8217;s allow up to 2 errors): </p>
<pre>
<dl><dt><dd>mairix d:6m- f:richard s:chrony=2
</dl>
</pre>
<h2>NOTES</h2>
<p> <code>mairix</code> works exclusively in terms of <i>words</i>. The index that&#8217;s built in indexing mode contains a table of which words occur in which messages. Hence, the search capability is based on finding messages that contain particular words. <code>mairix</code> defines a word as any string of alphanumeric characters + underscore. Any whitespace, punctuation, hyphens etc are treated as word boundaries. </p>
<p> <code>mairix</code> has special handling for the To:, Cc: and From: headers. Besides the normal word scan, these headers are scanned a second time, where the characters &#8216;@&#8217;, &#8216;-&#8216; and &#8216;.&#8217; are also treated as word characters. This allows most (if not all) email addresses to appear in the database as single words. So if you have a mail from wibble [at] foobar.zzz, it will match on both these searches </p>
<pre>
<dl><dt><dd>mairix f:foobar
mairix f:wibble [at] foobar.zzz
</dl>
</pre>
<p> It should be clear by now that the searching cannot be used to find messages matching general regular expressions. This has never been much of a limitation. Most searches are for particular keywords that were in the messages, or details of the recipients, or the approximate date. </p>
<p> It&#8217;s also worth pointing out that there is no &#8216;locality&#8217; information stored, so you can&#8217;t search for messages that have one words &#8216;close&#8217; to some other word. For every message and every word, there is a simple yes/no condition stored &#8211; whether the message contains the word in a particular header or in the body. So far this has proved to be adequate. <code>mairix</code> has a similar feel to using an Internet search engine. </p>
<h2>FILES</h2>
<p> <i>~/.mairixrc</i> </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2002-2006 Richard P. Curnow &lt;rc [at] rc0.org.uk&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-mairixrc/">mairixrc</a>(5)</p>
<h2>BUGS</h2>
<p> We need a plugin scheme to allow more types of attachment to be scanned and indexed. </p>
<h2>Index</h2>
