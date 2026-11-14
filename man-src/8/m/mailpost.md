---
title: "mailpost(8)"
name: "mailpost"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mailpost/"
description: "mailpost – Feed an e-mail message into a newsgroup"
---

<p>mailpost &#8211; Feed an e-mail message into a newsgroup</p>
<h2>Synopsis</h2>
<p><code>mailpost</code> [<code>-hn</code>] [<code>-a</code> <i>addr</i>] [<code>-b</code> <i>database</i>] [<code>-c</code> <i>wait-time</i>] [<code>-d</code> <i>distribution</i>] [<code>-f</code> <i>addr</i>] [<code>-m</code> <i>mailing-list</i>] [<code>-o</code> <i>output-command</i>] [<code>-p</code> <i>port</i>] [<code>-r</code> <i>addr</i>] [<code>-t</code> <i>tempdir</i>] [<code>-x</code> <i>header</i>[<code>:</code><i>header</i>&#8230;]] <i>newsgroups</i></p>
<h2>Description</h2>
<p>The <code>mailpost</code> program reads a properly formatted e-mail message from stdin and feeds it to <code>inews</code> for posting to a news server. <i>newsgroups</i> is a whitespace-separated list of group names to which to post the article (at least one newsgroup must be specified). </p>
<p> Before feeding the article to <code>inews</code>, it checks that the article has not been seen before, and it changes some headers (cleans up some address headers, removes X-Trace: and X-Complaints-To:, and puts <tt>&quot;X-&quot;</tt> in front of unknown headers). </p>
<p> If the article has been seen before (<code>mailpost</code> records the Message-ID of each article it handles), then the article will be dropped with a non-zero error status. Other errors will cause the article to be mailed to the newsmaster (selected at configure time and defaulting to <tt>&quot;usenet&quot;</tt>). </p>
<p> Normally, <code>mailpost</code> is run by <i><a href="/docs/linux/man/8-sendmail/">sendmail</a></i>(8) via an alias entry: </p>
<pre> local-mail-wreck-bikes: &quot;|&lt;pathbin in inn.conf&gt;/mailpost
 -b /var/tmp -t /var/tmp -d local local.mail.rec.bicycles.racing&quot;</pre>
<p>The <code>-b</code> and <code>-t</code> flags are useful to change the directories used by <code>mailpost</code> by default. As a matter of fact, though it is recommended to run <code>mailpost</code> as the news user, it is as often as not run as another user, for instance the mail user. Therefore, you should make sure to create and set to be writable by the user that <code>mailpost</code> runs as the directories where to put the database and the temporary files. </p>
<p> Instead of <i>/var/tmp</i>, the mail spool directory can be specified, or any other directory where the <code>mailpost</code> process has write access.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code> <i>addr</i></p>
<dd>If the <code>-a</code> flag is used, the value given is added to the article as an Approved: header.</p>
<dt><code>-b</code> <i>database</i></p>
<dd>If the <code>-b</code> flag is used, then it defines the location of the persistent database used to store the Message-IDs of articles sent on. This is to prevent articles looping around if a news-to-mail gateway sends them back here. This option may be required if the <code>mailpost</code> process does not have write access to the news temporary directory. The default value is <i>pathtmp</i> as set in <i>inn.conf</i>.</p>
<dt><code>-c</code> <i>wait-time</i></p>
<dd>The <code>-c</code> flag indicates a length of time to sleep before posting. If duplicate messages are received in this interval (by any instance of <code>mailpost</code> using the same database), the article is only posted once, but with Newsgroups: header modified to crosspost the article to all indicated groups. The units for <i>wait-time</i> are seconds; a reasonable value may be anywhere from tens to hundreds of seconds, or even higher, depending on how long mail can be delayed on its way to your system.</p>
<dt><code>-d</code> <i>distribution</i></p>
<dd>If the <code>-d</code> flag is used, the value given is added to the article as a Distribution: header.</p>
<dt><code>-f</code> <i>addr</i></p>
<dd>The <code>-f</code> flag is a synonym for the <code>-r</code> flag.</p>
<dt><code>-h</code></p>
<dd>Print usage information and exit.</p>
<dt><code>-m</code> <i>mailing-list</i></p>
<dd>If the <code>-m</code> flag is used, the value given is added to the article in a Mailing-List: header, if such a header doesn&#8217;t already exist.</p>
<dt><code>-n</code></p>
<dd>If the <code>-n</code> flag is used, neither an article is posted nor a mail is sent in case an error occurs. Everything is written to the standard output.</p>
<dt><code>-o</code> <i>output-command</i></p>
<dd>Specifies the program to which the resulting article processed by <code>mailpost</code> should be sent. For debugging purpose, <tt>&quot;-o cat&quot;</tt> can be used. The default value is <tt>&quot;inews -S -h&quot;</tt>.</p>
<dt><code>-p</code> <i>port</i></p>
<dd>Specifies the port on which <code>nnrpd</code> is listening, used for article posting. If given, <code>-p</code> is passed along to <code>inews</code>.</p>
<dt><code>-r</code> <i>addr</i></p>
<dd>A heuristic is used to determine a reasonable value for the Path: header. The <code>-r</code> flag indicates what to use if no other value can be determined.</p>
<dt><code>-t</code> <i>tempdir</i></p>
<dd>If the <code>-t</code> flag is used, then it defines the location of the directory to use to temporarily store error messages that are sent to the newsmaster. This option may be required if the default value refers to a path that does not exist or the <code>mailpost</code> process does not have write access to. Two paths are tried by default: <i>pathtmp</i> as set in <i>inn.conf</i>, and then <i>/var/tmp</i> if <i>pathtmp</i> is not writable.</p>
<dt><code>-x</code> <i>header</i>[<code>:</code><i>header</i>&#8230;]</p>
<dd>A colon-separated list of additional headers which should be treated as known headers; these headers will be passed through to <code>inews</code> without having <tt>&quot;X-&quot;</tt> prepended. </p>
<p> Known headers are: </p>
<pre> Approved
 Content-*
 Date
 Distribution
 From
 Mailing-List
 Message-ID
 MIME-*
 References
 Return-Path
 Sender
 Subject</pre>
</dl>
<h2>Files</h2>
<dl>
<dt><i>pathbin</i>/mailpost</p>
<dd>The Perl script itself used to feed an e-mail message to a newsgroup.</p>
<dt><i>pathtmp</i>/mailpost-msgid.dir and <i>pathtmp</i>/mailpost-msgid.pag</p>
<dd>The default database files which record previously seen Message-IDs.</dl>
<h2>History</h2>
<p>Written by Paul Vixie long ago and then hacked up by James Brister for <font SIZE="-1">INN</font> integration. </p>
<p> <tt>$Id:</tt> mailpost.in 9831 2015-04-23 19:07:39Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-active/">active</a></i>(5), <i><a href="/docs/linux/man/1-inews/">inews</a></i>(1), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8), <i><a href="/docs/linux/man/3-uwildmat/">uwildmat</a></i>(3). </p>
