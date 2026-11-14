---
title: "motd-news(5)"
name: "motd-news"
section: "5"
letter: "m"
url: "/docs/linux/man/5-motd-news/"
description: "motd.news – Message of the day information for feeders or readers"
---

<p>motd.news &#8211; Message of the day information for feeders or readers</p>
<h2>Description</h2>
<p>Two files, found in <i>pathetc</i>, contain local information for news feeders or news readers in a free-form format. The entire files are returned verbatim to any client that issues the <font SIZE="-1">LIST</font> <font SIZE="-1">MOTD</font> command. This might be used for new information, notification of upcoming downtime, or similar purposes. </p>
<p> These files are named <i>motd.innd</i> (for news feeders) and <i>motd.nnrpd</i> (for news readers); they are used by <code>innd</code> and <code>nnrpd</code>, respectively. </p>
<p> Make sure that these files are encoded in <font SIZE="-1">UTF-8</font>. They should also be &#8220;dot-stuffed&#8221;, that is to say that a line beginning with a dot should have that dot doubled. </p>
<p> Be aware that use of the <font SIZE="-1">LIST</font> <font SIZE="-1">MOTD</font> command is not widespread (though documented in <font SIZE="-1">RFC</font>&nbsp;<wbr>6048) and most news clients will never ask for this file. </p>
<p> If one or both of these files are missing, it is not an error. The server will just send the client the appropriate response for an unmaintained <i>motd.innd</i> or <i>motd.nnrpd</i> file. </p>
<p> On a fresh <font SIZE="-1">INN</font> install, samples for these files are installed in <i>pathec</i>; you will therefore find in <i>motd.innd.sample</i> and <i>motd.nnrpd.sample</i> a few examples of messages that can be communicated to news clients.</p>
<h2>History</h2>
<p>Rewritten in <font SIZE="-1">POD</font> by Russ Allbery &lt;eagle [at] eyrie.org&gt; for InterNetNews. </p>
<p> <tt>$Id:</tt> motd.news.pod 9768 2014-12-07 21:22:57Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5). </p>
