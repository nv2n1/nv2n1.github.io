---
title: "subscriptions(5)"
name: "subscriptions"
section: "5"
letter: "s"
url: "/docs/linux/man/5-subscriptions/"
---

subscriptions - Default recommended subscriptions

<h2>Description</h2>

The <i>pathetc</i>/subscriptions file contains a list of newsgroups that is returned by the <font SIZE="-1">NNTP</font> command <font SIZE="-1">LIST</font> <font SIZE="-1">SUBSCRIPTIONS</font>. 

 Clients that support this command usually send it the first time they connect to a new news server. They use the returned list to initialize the list of subscribed newsgroups. The <i>subscriptions</i> file therefore should contain groups intended for new users, for testing, or that contain FAQs and other useful information for first-time Usenet users. 

 The syntax of the <i>subscriptions</i> file is trivial; it is a simple list of newsgroup names, one per line. The order of newsgroups may be significant; the news reading client may present the groups in that order to the user. 

 Be aware that use of the <font SIZE="-1">LIST</font> <font SIZE="-1">SUBSCRIPTIONS</font> command is not widespread (though documented in <font SIZE="-1">RFC</font>&nbsp;<wbr>6048) and most news clients will never ask for this file.

<h2>Example</h2>

A typical <i>subscriptions</i> file may look like: 

 <pre> news.announce.newusers
 news.newusers.questions
 local.test
 local.general
 local.talk
 misc.test
 misc.test.moderated
 news.answers
 news.announce.newgroups</pre>This gives the client the FAQs and question newsgroup for new users first, then a local newsgroup for testing and various commonly-read local discussion groups, followed by the world-wide test groups, all the FAQs, and announcements of new world-wide newsgroups. If there is a local new users group, one might want to list it first.

<h2>History</h2>

Written by Bettina Fink &lt;laura [at] hydrophil.de&gt; for InterNetNews. 

 <tt>$Id:</tt> subscriptions.pod 9138 2010-10-29 18:09:50Z iulius $

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8). 
