---
title: "active-times(5)"
name: "active-times"
section: "5"
letter: "a"
url: "/docs/linux/man/5-active-times/"
description: "active.times – List of local creation times of newsgroups"
---

<p>active.times &#8211; List of local creation times of newsgroups</p>
<h2>Description</h2>
<p>The file <i>pathdb</i>/active.times provides a chronological record of when newsgroups were created on the local server. This file is normally updated by <code>mod-active</code> and <code>innd</code> whenever a newgroup control message is processed or a <tt>&quot;ctlinnd newgroup&quot;</tt> command is issued, and is used by <code>nnrpd</code> to answer <font SIZE="-1">NEWGROUPS</font> requests. Each line consists of three fields: </p>
<pre><code>&lt;name&gt; &lt;time&gt; &lt;creator&gt;</code></pre>
<p> The first field is the name of the newsgroup. The second field is the time it was created, expressed as the number of seconds since the epoch. The third field is plain text intended to describe the entity that created the newsgroup. This field is encoded in <font SIZE="-1">UTF-8</font> and is usually the e-mail address of the person who created the group, as specified in the control message or on the <code>ctlinnd</code> command line, or the newsmaster specified at configure time if no creator argument was given to <code>ctlinnd</code> (by default, it is <tt>&quot;usenet&quot;</tt>). You can get the <i>active.times</i> file of another <font SIZE="-1">NNTP</font> server with <i><a href="/docs/linux/man/1-getlist/">getlist</a></i>(1).</p>
<h2>Example</h2>
<p>The line: </p>
<pre> news.admin.moderation 1175716803 &lt;group-admin [at] isc.org&gt;</pre>
<p>shows that the newsgroup news.admin.moderation was created on April 4th, 2007, at 20:00:03 <font SIZE="-1">UTC</font>. This date can be obtained for instance with <tt>&quot;convdate -c 1175716803&quot;</tt> (<i><a href="/docs/linux/man/1-convdate/">convdate</a></i>(1) is shipped with <font SIZE="-1">INN</font>) or <tt>&quot;date -u -d &quot;Jan 1, 1970 00:00:00 +0000 + 1175716803 seconds&quot;&quot;</tt>. It is when the newsgroup was locally created; in this example, it is when a control message sent by <tt>&quot;group-admin [at] isc.org&quot;</tt> was received and processed by the news server (see <i><a href="/docs/linux/man/5-control-ctl/">control.ctl</a></i>(5) for more details). Therefore, the time is not necessarily the same on every news server.</p>
<h2>History</h2>
<p>Written by Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. Converted to <font SIZE="-1">POD</font> by Russ Allbery &lt;eagle [at] eyrie.org&gt;. </p>
<p> <tt>$Id:</tt> active.times.pod 9768 2014-12-07 21:22:57Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-active/">active</a></i>(5), <i><a href="/docs/linux/man/1-convdate/">convdate</a></i>(1), <i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8), <i><a href="/docs/linux/man/1-getlist/">getlist</a></i>(1), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8), <i><a href="/docs/linux/man/8-mod-active/">mod-active</a></i>(8), <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8). </p>
