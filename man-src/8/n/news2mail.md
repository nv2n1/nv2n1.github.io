---
title: "news2mail(8)"
name: "news2mail"
section: "8"
letter: "n"
url: "/docs/linux/man/8-news2mail/"
description: "news2mail – Channel script to gateway news into e-mails"
---

<p>news2mail &#8211; Channel script to gateway news into e-mails</p>
<h2>Synopsis</h2>
<p><code>news2mail</code></p>
<h2>Description</h2>
<p><code>news2mail</code> runs as a channel process underneath <code>innd</code>. It is set up as channel feed in <i>newsfeeds</i>, with different mailing-lists as funnel entries pointing to it (see below); <code>news2mail</code> expects the token of an article followed by a sequence of list names. </p>
<p> <code>news2mail</code> uses the configuration file <i>pathetc</i>/news2mail.cf to map mailing-list names to e-mail addresses. <code>news2mail</code> causes <code>sendmail</code> to queue the messages for later delivery (to avoid <font SIZE="-1">DOS</font> attacks by mass postings). You must run <tt>&quot;sendmail -q&quot;</tt> periodically to get the queue processed.</p>
<h2>Configuration File</h2>
<p>The configuration file format is simple: comments (starting with a hash sign <tt>&quot;#&quot;</tt>) and blank lines are ignored. All other lines have two or three fields on them. The first is the list name and is what <code>innd</code> uses (i.e. the site field of the entry in the <i>newsfeeds</i> file). The second field is the actual e-mail address to send the article to. The third field is optional: it sets the envelope-from address (for instance a list member&#8217;s address; if not set, it defaults to the <tt>&quot;news&quot;</tt> user). </p>
<p> In e-mail messages, the To: header will have the mailing-list address (i.e. the second field). Besides, <code>news2mail</code> strips most article headers from the article before mailing. </p>
<p> In <i>newsfeeds</i>, the channel feed should look like: </p>
<pre> news2mail!:!*:Ac,Tc,Wn*:&lt;pathbin&gt;/news2mail</pre>
<p>and for each mailing-list, you only have to add to <i>newsfeeds</i> an entry list like: </p>
<pre> list-big-red-ants/lists.ucsd.edu:!*,rec.pets.red-ants:Ap,Tm:news2mail!</pre>
<p>Please note the use of <tt>&quot;Ap&quot;</tt> and the exclusion of the list owner domain to protect the list from feeding back new arrivals from the list. The site name used in the <i>newfeeds</i> entry for a mailing-list (above <tt>&quot;list-big-red-ants&quot;</tt>) must be the same as the first field in an entry in <i>news2mail.cf</i>. For instance: </p>
<pre> # Newsfeeds-name List-to-address [List-sender-address]
 list-big-red-ants big-red-ants [at] lists.ucsd.edu news+big-red-ants [at] local.news.server.org</pre>
<h2>Files</h2>
<dl>
<dt><i>pathbin</i>/news2mail</p>
<dd>The Perl program itself used to gateway news into e-mails.</p>
<dt><i>pathetc</i>/news2mail.cf</p>
<dd>The configuration file which specifies the mapping to use for gatewaying.</dl>
<h2>Bugs</h2>
<p>The <code>news2mail</code> program is set up as a funneled channel in <i>newsfeeds</i>, implying multiple matches should be handled as one &#8211; and multiple matching funneled feeds will result in a single call to the script. Therefore, since only one mail is sent, crossposts are not currently properly handled as for the envelope-from address (which then defaults to the <tt>&quot;news&quot;</tt> user).</p>
<h2>History</h2>
<p><code>news2mail</code> was written by Brian Kantor in 1998. This man page was written by James Brister and converted to <font SIZE="-1">POD</font> by Julien Elie. The third optional field in <i>news2mail.cf</i> was added by D. Stussy in 2008. </p>
<p> <tt>$Id:</tt> news2mail.pod 8199 2008-11-30 13:30:47Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-innd/">innd</a></i>(8), <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5). </p>
