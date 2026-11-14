---
title: "moderators(5)"
name: "moderators"
section: "5"
letter: "m"
url: "/docs/linux/man/5-moderators/"
description: "moderators – Submission addresses for moderated groups"
---

<p>moderators &#8211; Submission addresses for moderated groups</p>
<h2>Description</h2>
<p>When an unapproved article is posted locally to a moderated newsgroup, it is not passed off to <code>innd</code> for normal handling; instead, it is sent via e-mail to the submission address for that newsgroup. The submission address is determined using this configuration file. </p>
<p> The file <i>pathetc</i>/moderators is a list of associations between <i><a href="/docs/linux/man/3-uwildmat/">uwildmat</a></i>(3) patterns matching newsgroups and the submission address for those newsgroups. Blank lines and lines starting with a number sign (<tt>&quot;#&quot;</tt>) are ignored. All other lines should consist of two fields separated by a colon: </p>
<pre> &lt;pattern&gt;:&lt;address&gt;</pre>
<p>The first field is a <i><a href="/docs/linux/man/3-uwildmat/">uwildmat</a></i>(3) pattern matching the group or groups to which this line applies. The first matching line is used, so more specific patterns should be listed before general patterns. </p>
<p> The second field, the submission address, should be a simple e-mail address with one exception: at most one <tt>%s</tt> may occur anywhere in the address. If present, it will be replaced by the name of the newsgroup, with all periods in the name changed to dashes (<tt>&quot;-&quot;</tt>). If there is a literal <tt>&quot;%&quot;</tt> in the submission address, it must be written as <tt>&quot;%%&quot;</tt>, even if not followed by an <tt>&quot;s&quot;</tt>. </p>
<p> With the <tt>%s</tt> syntax, periods are converted to dashes for historical reasons, from back in the days when periods in the local part of addresses were not always handled correctly. It&#8217;s probably no longer necessary, but so much now depends on it that it can&#8217;t be easily changed. </p>
<p> It&#8217;s intended that the sample <i>moderators</i> file included in the <font SIZE="-1">INN</font> distribution always be sufficient for all world-wide newsgroups. The hosts behind moderators.isc.org have graciously volunteered to handle forwarding tasks for all world-wide newsgroups so that individual sites don&#8217;t have to keep track of the submission addresses for moderated groups. The forwarding database used by moderators.isc.org is coordinated by &lt;moderators-request [at] isc.org&gt;; if you know of a world-wide newsgroup hierarchy that is not correctly handled by moderators.isc.org, please send the details to that address. </p>
<p> Given that, the only thing you should have to add to the sample file under normal circumstances are the forwarding addresses for local or limited-distribution moderated groups. </p>
<p> If this file doesn&#8217;t exist, or if a post is made to a moderated group that has no matching entry in this file, <code>nnrpd</code> falls back on the value of <i>moderatormailer</i> set in <i>inn.conf</i> and, failing that, rejects the post.</p>
<h2>Examples</h2>
<p>Here is a sample file: </p>
<pre> example.important:announce [at] example.com
 example.*:%s [at] smtp.example.com
 *:%s [at] moderators.isc.org</pre>
<p>Using the above file, postings to the moderated newsgroup in the left column below will be sent to the address shown in the right column below: </p>
<pre> example.important announce [at] example.com
 example.x-announce example-x-announce [at] smtp.example.com
 alt.dev.null alt-dev-null [at] moderators.isc.org</pre>
<p>Note that periods are changed to dashes and dashes are left alone with the <tt>%s</tt> syntax, so two moderated newsgroups whose names differ only by changing a period to a dash would go to the same address. Such newsgroup pairs should therefore not be created.</p>
<h2>History</h2>
<p>Written by Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. Rewritten in <font SIZE="-1">POD</font> by Russ Allbery &lt;eagle [at] eyrie.org&gt;. </p>
<p> <tt>$Id:</tt> moderators.pod 9768 2014-12-07 21:22:57Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8), <i><a href="/docs/linux/man/3-uwildmat/">uwildmat</a></i>(3). </p>
