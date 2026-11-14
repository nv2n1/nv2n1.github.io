---
title: "inews(1)"
name: "inews"
section: "1"
letter: "i"
url: "/docs/linux/man/1-inews/"
description: "inews – Post a Usenet article to the local news server"
---

<h2 class="name">NAME</h2>
<p> inews &#8211; Post a Usenet article to the local news server </p>
<h2>SYNOPSIS</h2>
<p> <code>inews</code> [<code>-ADhNORSVW</code>] [<code>-acdeFfnortwx</code> <i>value</i>] [<code>-p</code> <i>port</i>] [<i>file</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>inews</code> reads a Usenet news article, perhaps with headers, from <i>file</i> or standard input if no file is given. It adds some headers and performs some consistency checks. If the article does not meet those checks, the article is rejected. If it passes the checks, <code>inews</code> sends the article to the local news server as specified in <i>inn.conf</i>. </p>
<p> By default, if a file named <i>.signature</i> exists in the home directory of the posting user, it is appended to the post, preceded by a line that contains only <tt>&quot;-- &quot;</tt>. Signatures are not allowed to be more than four lines long. </p>
<p> Cancel messages can only be posted with <code>inews</code> if the sender of the cancel message matches the sender of the original message being cancelled. The same check is also applied to Supersedes. Sender in this case means the contents of the Sender header if present, otherwise the From header. </p>
<p> Control messages other than cancel messages are only allowed if <code>inews</code> is being run by the news user or by a user in the news group and if the control message is recognized. If the article contains a Distribution header with a distribution that matches one of the bad distribution patterns in <i>inn/options.h</i> (anything containing a period by default), the message will be rejected. The message will also be rejected if <i>checkincludedtext</i> is true in <i>inn.conf</i>, it contains more quoted text than original text, and it is over 40 lines long. </p>
<p> If not provided, the Path header of an article is constructed as follows: The basic Path header will be &#8220;not-for-mail&#8221;. If <i>pathhost</i> is specified in <i>inn.conf</i>, it will be added to the beginning Path. Otherwise, if <i>server</i> is specified, the full domain of the local host will be added to the beginning of the Path. Then, if <code>-x</code> was given, its value will be added to the beginning of the Path. </p>
<p> If posting fails, a copy of the failed post will be saved in a file named <i>dead.article</i> in the home directory of the user running <code>inews</code>. <code>inews</code> exits with a non-zero status if posting failed or with a zero status if posting was successful.</p>
<h2>OPTIONS</h2>
<p> Most of the options to <code>inews</code> take a single value and set the corresponding header in the message that is posted. If the value is more than one word or contains any shell metacharacters, it must be quoted to protect it from the shell. Here are all the options that set header fields and the corresponding header: </p>
<pre>
    -a  Approved
    -c  Control
    -d  Distribution
    -e  Expires
    -F  References
    -f  From
    -n  Newsgroups
    -o  Organization
    -r  Reply-To
    -t  Subject
    -w  Followup-To
    -x  Path prefix
</pre>
<p> The <code>-x</code> argument will be added to the beginning of the normal Path header; it will not replace it.</p>
<dl>
<dt><code>-A</code>, <code>-V</code>, <code>-W</code></p>
<dd> Accepted for compatibility with C News. These options have no affect.</p>
<dt><code>-D</code>, <code>-N</code></p>
<dd> Perform the consistency checks and add headers where appropriate, but then print the article to standard output rather than sending it to the server. <code>-N</code> is accepted as as synonym for compatibility with C News.</p>
<dt><code>-h</code></p>
<dd> Normally, this flag should always be given. It indicates that the article consists of headers, a blank line, and then the message body. If it is omitted, the input is taken to be just the body of the message, and any desired headers have to be specified with command-line options as described above.</p>
<dt><code>-O</code></p>
<dd> By default, an Organization header will be added if none is present in the article. To prevent adding the default (from <i>organization</i> in <i>inn.conf</i>), use this flag.</p>
<dt><code>-p</code> <i>port</i></p>
<dd> Connect to the specified port on the server rather than to the default (port 119).</p>
<dt><code>-R</code></p>
<dd> Reject all control messages.</p>
<dt><code>-S</code></p>
<dd> Do not attempt to append <i>~/.signature</i> to the message, even if it exists.</dl>
<h2>NOTES</h2>
<p> If the <font SIZE="-1">NNTP</font> server requests authentication, <code>inews</code> will try to read <i>passwd.nntp</i> to get the username and password to use and will therefore need read access to that file. This is typically done by making that file group-readable and adding all users who should be able to use <code>inews</code> to post to that server to the appropriate group. </p>
<p> <code>inews</code> used to do even more than it does now, and all of the remaining checks that are not dependent on the user running <code>inews</code> should probably be removed in favor of letting the news server handle them. </p>
<p> Since <font SIZE="-1">INN</font>&#8216;s <code>inews</code> uses <i>inn.conf</i> and some other corners of an <font SIZE="-1">INN</font> installation, it&#8217;s not very appropriate as a general stand-alone <code>inews</code> program for general use on a system that&#8217;s not running a news server. Other, more suitable versions of <code>inews</code> are available as part of various Unix news clients or by themselves.</p>
<h2>HISTORY</h2>
<p> Written by Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. Rewritten in <font SIZE="-1">POD</font> by Russ Allbery &lt;eagle [at] eyrie.org&gt;. </p>
<p> <tt>$Id:</tt> inews.pod 9768 2014-12-07 21:22:57Z iulius $</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/5-passwd-nntp/">passwd.nntp</a></i>(5), <i><a href="/docs/linux/man/1-rnews/">rnews</a></i>(1). </p>
<h2>Index</h2>
