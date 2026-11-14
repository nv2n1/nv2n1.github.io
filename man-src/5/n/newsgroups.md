---
title: "newsgroups(5)"
name: "newsgroups"
section: "5"
letter: "n"
url: "/docs/linux/man/5-newsgroups/"
description: "newsgroups – List of newsgroups and their short descriptions"
---

<p>newsgroups &#8211; List of newsgroups and their short descriptions</p>
<h2>Description</h2>
<p>The file <i>pathdb</i>/newsgroups contains a list of newsgroups for which a short description is available. This file is generally updated by <i><a href="/docs/linux/man/8-controlchan/">controlchan</a></i>(8) whenever a control message is received; it is used by <code>nnrpd</code> in response to <font SIZE="-1">LIST</font> <font SIZE="-1">NEWSGROUPS</font> and is only meant to provide information to users. News readers often show the list of carried newsgroups along with these descriptions. </p>
<p> It is not necessary that all the groups carried by the news server (that is to say all the groups listed in the <i>active</i> file) be listed in the <i>newsgroups</i> file. And it is also not necessary that all the groups listed in the <i>newsgroups</i> file be carried by the news server. Nonetheless, it is of course better if the <i>active</i> and <i>newsgroups</i> files have exactly the same newsgroups. </p>
<p> If you use <tt>&quot;ctlinnd newgroup&quot;</tt> to manually create a group, only the <i>active</i> file is updated. You should then edit the <i>newsgroups</i> file in order to add a short description for the created group. The same goes for manually removing or changing the status of a newsgroup. </p>
<p> Each line of the <i>newsgroups</i> file consists of two fields separated by at least one tabulation: </p>
<pre> &lt;name&gt;	&lt;description&gt;</pre>
<p>The first field is the name of the newsgroup. The second field is its description. </p>
<p> You can get the <i>newsgroups</i> file of another <font SIZE="-1">NNTP</font> server with <i><a href="/docs/linux/man/1-getlist/">getlist</a></i>(1).</p>
<h2>Preferred Format For A One-Line Newsgroup Description</h2>
<p>As far as the format of the <i>newsgroups</i> file is concerned, there is a preferred format for each line. Since news administrators do not generally have the time to fix up the lines that are being automatically included from newgroup or checkgroups messages, this information is provided so that control message senders can craft better control messages. It will also be useful for news administrators to know how to format the description of their local newsgroups. </p>
<p> There should be at least one hard tab (8 column tab stops) between the group name and the description. If the group name is at least 16 characters, it should be followed with one tab. If the group name is at least 8 characters, it should be followed with two tabs. And in the unlikely event the group name is less than 8 characters, it should be followed with three tabs. For instance: </p>
<pre> misc.transport.rail.europe Railroads &amp; railways in all of Europe.
 news.admin.nocem NoCeM protocol policy issues and information.
 news.groups Discussions and lists of newsgroups.</pre>
<p>The total line length should be at most 79 columns. The description should start with a capital and not be more than 55 characters (79 &#8211; 24) long. If the group name is longer than 24 characters, the description should be correspondingly shorter. If the group is moderated, it should have <tt>&quot; (Moderated)&quot;</tt> (note the space before the opening parenthesis) at the very end of the description, not counted as part of the length of the description. This text must be exactly that, with no variations, as it is used by news software to find moderated groups. </p>
<p> Here is an example of moderated newsgroup: </p>
<pre> news.lists.misc News-related statistics and lists. (Moderated)</pre>
<p>Traditionally, all newsgroup descriptions ended with a period, but this is not necessary and steals away one character that is occasionally useful for forming a better description. </p>
<p> Some over-long descriptions could be made to easily fit the length by dropping useless wordings like <tt>&quot;Discussion of&quot;</tt> which do not meaningfully contribute to the description. Others are usually pretty easy to get to no more than column eighty, except when the group names start getting really long. Hopefully then the group name itself contains quite a bit of description. </p>
<p> In some cases, a longer description really will be necessary; they can of course be used within the <i>newsgroups</i> file. However, they will probably be less readable and less useful for some Usenet users. </p>
<p> Descriptions must not contain any control characters (octets between 0x00 and 0x1F).</p>
<h2>Encoding Of The Descriptions</h2>
<p>There is, at present, no good mechanism for managing the character set of the newsgroup descriptions. Many non-English hierarchies include newsgroup descriptions in their native languages, since this is more useful for their users, and those are included verbatim in the <i>newsgroups</i> file. This unfortunately means that different lines of the file will require different character set settings to read properly, and those character sets are not documented in the file. Hopefully some future standard will provide a way to address this; in the meantime, using <font SIZE="-1">UTF-8</font> for non-ASCII characters is recommended.</p>
<h2>Minimal Newsgroups File</h2>
<p>The minimal <i>newsgroups</i> file shipped with <font SIZE="-1">INN</font> is: </p>
<pre> control Various control messages (no posting).
 control.cancel Cancel messages (no posting).
 control.checkgroups Hierarchy check control messages (no posting).
 control.newgroup Newsgroup creation control messages (no posting).
 control.rmgroup Newsgroup removal control messages (no posting).
 junk Unfiled articles (no posting).</pre>
<p>These lines <i>must</i> be tab-delimited, so please be careful in case you copy and paste them from above.</p>
<h2>History</h2>
<p>Written by Julien Elie for InterNetNews. The preferred format for a one-line newsgroup description is based on the policies by which the <i>newsgroups</i> file in &lt;<a href="ftp://ftp.isc.org/pub/usenet/CONFIG/">ftp://ftp.isc.org/pub/usenet/CONFIG/</a>&gt; is maintained; they were originally written by David Lawrence &lt;tale [at] isc.org&gt; and updated by Russ Allbery &lt;eagle [at] eyrie.org&gt;. </p>
<p> <tt>$Id:</tt> newsgroups.pod 9768 2014-12-07 21:22:57Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-active/">active</a></i>(5), <i><a href="/docs/linux/man/8-controlchan/">controlchan</a></i>(8), <i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8), <i><a href="/docs/linux/man/1-getlist/">getlist</a></i>(1), <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8). </p>
