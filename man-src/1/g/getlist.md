---
title: "getlist(1)"
name: "getlist"
section: "1"
letter: "g"
url: "/docs/linux/man/1-getlist/"
description: "getlist – Get a list from an NNTP server"
---

<h2 class="name">NAME</h2>
<p> getlist &#8211; Get a list from an NNTP server </p>
<h2>SYNOPSIS</h2>
<p> <code>getlist</code> [<code>-AR</code>] [<code>-h</code> <i>host</i>] [<code>-p</code> <i>port</i>] [<i>list</i> [<i>pattern</i> [<i>types</i>]]]</p>
<h2>DESCRIPTION</h2>
<p> <code>getlist</code> obtains a list from an <font SIZE="-1">NNTP</font> server and sends it to standard output. <i>list</i> may be one of <tt>&quot;active&quot;</tt> (which is the default value), <tt>&quot;active.times&quot;</tt>, <tt>&quot;distrib.pats&quot;</tt>, or <tt>&quot;newsgroups&quot;</tt>. <tt>&quot;active&quot;</tt> contains a list of all newsgroups carried by the server with the high and low article numbers in the group, and the group status field. <tt>&quot;active.times&quot;</tt> is a list of newsgroups, their creation times (in seconds since epoch), and the creator of the group. <tt>&quot;distrib.pats&quot;</tt> is a list of relevant distributions and the newsgroups they apply to. <tt>&quot;newsgroups&quot;</tt> is a list of newsgroups along with their short descriptions. </p>
<p> For more information on the formats of these files, see <i><a href="/docs/linux/man/5-active/">active</a></i>(5), <i><a href="/docs/linux/man/5-active-times/">active.times</a></i>(5), <i><a href="/docs/linux/man/5-distrib-pats/">distrib.pats</a></i>(5) and <i><a href="/docs/linux/man/5-newsgroups/">newsgroups</a></i>(5). </p>
<p> The listing files other than the <i>active</i> file are common extensions to the <font SIZE="-1">NNTP</font> protocol and may not be available on all servers. For instance, <tt>&quot;counts&quot;</tt> <tt>&quot;distributions&quot;</tt>, <tt>&quot;headers&quot;</tt>, <tt>&quot;moderators&quot;</tt>, <tt>&quot;motd&quot;</tt>, <tt>&quot;overview.fmt&quot;</tt> and <tt>&quot;subscriptions&quot;</tt>, amongst other, may be available. Moreover, a <i><a href="/docs/linux/man/3-uwildmat/">uwildmat</a></i>(3) pattern <i>pattern</i> may also be usable for some of these listing files. </p>
<p> For more information on the formats of these files, see <i><a href="/docs/linux/man/5-distributions/">distributions</a></i>(5), <i><a href="/docs/linux/man/5-moderators/">moderators</a></i>(5), <i><a href="/docs/linux/man/5-motd-news/">motd.news</a></i>(5) and <i><a href="/docs/linux/man/5-subscriptions/">subscriptions</a></i>(5). The overview fields obtained with <tt>&quot;overview.fmt&quot;</tt> are the ones for which the overview database is consistent (see <i>extraoverviewadvertised</i> in <i>inn.conf</i> for more information). The list obtained with <tt>&quot;headers&quot;</tt> contains the fields that can be retrieved using the <font SIZE="-1">HDR</font> command (<i>pattern</i> can then be either <tt>&quot;msgid&quot;</tt> or <tt>&quot;range&quot;</tt>). The list obtained with <tt>&quot;counts&quot;</tt> is like the <tt>&quot;active&quot;</tt> one except that the number of articles in a newsgroup is mentioned just before the flag of this newsgroup. </p>
<p> The <i>pattern</i> parameter may be used with a <i>list</i> value of <tt>&quot;active&quot;</tt>, <tt>&quot;active.times&quot;</tt> or <tt>&quot;newsgroups&quot;</tt> to limit the output. If given, only entries corresponding to newsgroups that match the <i><a href="/docs/linux/man/3-uwildmat/">uwildmat</a></i>(3) pattern <i>pattern</i> will be printed. </p>
<p> If the <i>list</i> parameter is <tt>&quot;active&quot;</tt>, a third parameter, <i>types</i>, may also be used to restrict the list. If given, only entries corresponding to newsgroups with a newsgroup mode found in <i>types</i> will be printed. For example, a <i>types</i> value of <tt>&quot;y&quot;</tt> would only show unmoderated groups, and a <i>types</i> value of <tt>&quot;ym&quot;</tt> would show all unmoderated and moderated groups but not aliased groups or groups that disallow postings.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A</code></p>
<dd> Try to authenticate using the username and password information in <i><a href="/docs/linux/man/5-passwd-nntp/">passwd.nntp</a></i>(5) before issuing the <font SIZE="-1">LIST</font> command.</p>
<dt><code>-h</code> <i>host</i></p>
<dd> Connect to the server <i>host</i> rather than to the value of <i>server</i> in <i>inn.conf</i> or the value of the <font SIZE="-1">NNTPSERVER</font> environment variable.</p>
<dt><code>-p</code> <i>port</i></p>
<dd> Connect to the port <i>port</i>, which is by default <tt>119</tt>.</p>
<dt><code>-R</code></p>
<dd> Try to switch to <code>nnrpd</code> with a <font SIZE="-1">MODE</font> <font SIZE="-1">READER</font> command before issuing the <font SIZE="-1">LIST</font> request. It can be useful in case a feeding access exists for the news server: more information can be retrieved from <code>nnrpd</code>, compared with <code>innd</code>.</dl>
<h2>EXAMPLES</h2>
<p> The following command will obtain the one-line descriptions of all newsgroups found on <font SIZE="-1">UUNET:</font> </p>
<pre>
    getlist -h news.uu.net newsgroups
</pre>
<p> The following command will show the active file entries for all moderated comp.* groups on the default server: </p>
<pre>
    getlist active 'comp.*' m
</pre>
<p> The following command lists all groups where local postings are permitted, are moderated or aliased: </p>
<pre>
    getlist active '*' ym=
</pre>
<p> Note that the wildcard character <tt>&quot;*&quot;</tt> has to be quoted by simple quotes to protect it from the shell.</p>
<h2>HISTORY</h2>
<p> Written by Landon Curt Noll &lt;chongo [at] toad.com&gt; for InterNetNews. Rewritten in <font SIZE="-1">POD</font> by Russ Allbery &lt;eagle [at] eyrie.org&gt;. </p>
<p> <tt>$Id:</tt> getlist.pod 9768 2014-12-07 21:22:57Z iulius $</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-active/">active</a></i>(5), <i><a href="/docs/linux/man/5-active-times/">active.times</a></i>(5), <i><a href="/docs/linux/man/5-distrib-pats/">distrib.pats</a></i>(5), <i><a href="/docs/linux/man/5-distributions/">distributions</a></i>(5), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/5-moderators/">moderators</a></i>(5), <i><a href="/docs/linux/man/5-motd-news/">motd.news</a></i>(5), <i><a href="/docs/linux/man/5-newsgroups/">newsgroups</a></i>(5), <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8), <i><a href="/docs/linux/man/5-passwd-nntp/">passwd.nntp</a></i>(5), <i><a href="/docs/linux/man/5-subscriptions/">subscriptions</a></i>(5), <i><a href="/docs/linux/man/3-uwildmat/">uwildmat</a></i>(3). </p>
<h2>Index</h2>
