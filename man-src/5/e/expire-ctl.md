---
title: "expire-ctl(5)"
name: "expire-ctl"
section: "5"
letter: "e"
url: "/docs/linux/man/5-expire-ctl/"
description: "expire.ctl – Configuration file for article expiration"
---

<p>expire.ctl &#8211; Configuration file for article expiration</p>
<h2>Description</h2>
<p>The file <i>pathetc</i>/expire.ctl is the default configuration file for <code>expire</code> and <code>expireover</code>, which read it at start-up. It serves two purposes: it defines how long history entries for expired or rejected articles are remembered, and it determines how long articles stored on the server are retained. </p>
<p> Normally, if all of the storage methods used by the server are self-expiring (such as <font SIZE="-1">CNFS</font>), all lines except the <tt>&quot;/remember/&quot;</tt> setting (described below) are ignored. This can be changed with the <code>-N</code> option to <code>expire</code> or <code>expireover</code>. </p>
<p> Blank lines and lines beginning with a number sign (<tt>&quot;#&quot;</tt>) are ignored. All other lines should be in one of two formats. The order of the file is significant, and the last matching entry will be used. </p>
<p> The first format specifies how long to keep history entries for articles that aren&#8217;t present in the news spool. These are articles that have either already expired, or articles which the server rejected (when <i>remembertrash</i> is set to true in <i>inn.conf</i>). There should be one and only one line in this format, which looks like: </p>
<pre> /remember/:&lt;days&gt;</pre>
<p>where &lt;days&gt; is a decimal number that specifies the minimum number of days a history record for a given message-ID is retained (from its original posting time), regardless of whether the article is present in the spool. (History entries for articles still present in the spool are always retained.) </p>
<p> The primary reason to retain a record of old articles is in case a peer offers old articles that were previously accepted but have already expired. Without a history record for such articles, the server would accept the article again and readers would see duplicate articles. Articles older than a certain number of days won&#8217;t be accepted by the server at all (see <i>artcutoff</i> in <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5) and the <code>-c</code> flag in <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8)), and this setting should probably match that time period to ensure that the server never accepts duplicates. As the default value for <i>artcutoff</i> is <tt>10</tt> days, it means that <tt>&quot;/remember/&quot;</tt> should be set to <tt>11</tt> days in order to take into account articles whose posting date is one day into the future. </p>
<p> Most of the lines in this file will be in the second format, which consists of either four or five colon-separated fields: </p>
<pre> &lt;pattern&gt;:&lt;flag&gt;:&lt;min&gt;:&lt;default&gt;:&lt;max&gt;</pre>
<p>if <i>groupbaseexpiry</i> is true in <i>inn.conf</i> (the default), and otherwise: </p>
<pre> &lt;classnum&gt;:&lt;min&gt;:&lt;default&gt;:&lt;max&gt;</pre>
<p>All lines must be in the correct format given the current setting of <i>groupbaseexpiry</i>, and therefore the two formats cannot co-exist in the same file. </p>
<p> Normally, a rule matches a newsgroup through the combination of the &lt;pattern&gt; and &lt;flag&gt; fields. &lt;pattern&gt; is a <i><a href="/docs/linux/man/3-uwildmat/">uwildmat</a></i>(3)-style pattern, specifying the newsgroups to which the line is applied. Note that the last matching entry will be used, so general patterns (such as defaults for all groups where &lt;pattern&gt; is <tt>&quot;*&quot;</tt>) should appear at the beginning of the file before more specific settings. </p>
<p> The &lt;flag&gt; field can be used to further limit newsgroups to which the line applies, and should be chosen from the following set: </p>
<pre> M Only moderated groups
 U Only unmoderated groups
 A All groups
 X Remove the article from all groups it appears in</pre>
<p>One of <tt>&quot;M&quot;</tt>, <tt>&quot;U&quot;</tt>, or <tt>&quot;A&quot;</tt> must be specified. <tt>&quot;X&quot;</tt> should be used in combination with one of the other letters, not by itself. </p>
<p> An expiration policy is applied to every article in a newsgroup it matches. There is no way to set an expiration policy for articles crossposted to groups you don&#8217;t carry that&#8217;s different than other articles in the same group. Normally, articles are not completely deleted until they expire out of every group to which they were posted, but if an article is expired following a rule where &lt;flag&gt; contains <tt>&quot;X&quot;</tt>, it is deleted out of all newsgroups to which it was posted immediately. </p>
<p> If <i>groupbaseexpiry</i> is instead set to false, there is no &lt;pattern&gt; and &lt;flag&gt; field and the above does not apply. Instead, there is a single &lt;classnum&gt; field, which is either a number matching the storage class number specified in <i>storage.conf</i> or <tt>&quot;*&quot;</tt> to specify a default for all storage classes. All articles stored in a storage class will be expired following the instructions in the line with a matching &lt;classnum&gt;, and when articles are expired, they&#8217;re always removed from all groups to which they were posted. </p>
<p> The remaining three fields are the same in either format, and are used to determine how long an article should be kept from its original arrival time (unless the <code>-p</code> flag is passed to <i><a href="/docs/linux/man/8-expire/">expire</a></i>(8) or <i><a href="/docs/linux/man/8-expireover/">expireover</a></i>(8), in which case its original posting time is used). Each field should be either a decimal number of days (fractions like <tt>8.5</tt> are allowed, but remember that articles are only removed when <code>expire</code> or <code>expireover</code> is run, normally once a day by <code>news.daily</code>) or the word <tt>&quot;never&quot;</tt>. </p>
<p> The middle field, &lt;default&gt;, will be used as the expiration period for most articles. The other two fields, &lt;min&gt; and &lt;max&gt;, only come into play if the article requests a particular expiration date with an Expires: header. Articles with an Expires: header will be expired at the date given in that header, subject to the constraints that they will be retained at least &lt;min&gt; days and no longer than &lt;max&gt; days. </p>
<p> If &lt;min&gt; is set to <tt>&quot;never&quot;</tt>, no article matching that line will ever be expired. If &lt;default&gt; is set to <tt>&quot;never&quot;</tt>, no article matching that line without an explicit Expires: header will ever be expired. If &lt;max&gt; is set to <tt>&quot;never&quot;</tt>, Expires: headers will be honored no matter how far into the future they are. </p>
<p> One should think of the fields as a lower bound, the default, and an upper bound. Since most articles do not have an Expires: header, the second field is the most important and most commonly applied. </p>
<p> Articles that do not match any expiration rule will not be expired, but this is considered an error and will result in a warning. There should always be a default line (a line with a &lt;pattern&gt; of <tt>&quot;*&quot;</tt> and &lt;flag&gt; of <tt>&quot;A&quot;</tt>, or a line with a &lt;classnum&gt; of <tt>&quot;*&quot;</tt>), which can explicitly state that articles should never expire by default if that&#8217;s the desired configuration. The default line should generally be the first line of the file (except for <tt>&quot;/remember/&quot;</tt>) so that other expiration rules can override it. </p>
<p> It is often useful to honor the Expires: header in articles, especially those in moderated groups. To do this, set &lt;min&gt; to zero, &lt;default&gt; to whatever normal expiration you wish, and &lt;max&gt; to <tt>&quot;never&quot;</tt> or some large number, like <tt>365</tt> days for a maximum article life of a year. </p>
<p> To ignore any Expires: header, set all three fields to the same value.</p>
<h2>Examples</h2>
<p>When <i>groupbaseexpiry</i> is true (the default): </p>
<pre> # Keep expired article history for 11 days, matching artcutoff plus one.
 /remember/:11
 # Most articles stay for two weeks, ignoring Expires: headers.
 *:A:14:14:14
 # Accept Expires: headers in moderated groups for up to a year and
 # retain moderated groups for a bit longer.
 *:M:1:30:365
 # Keep local groups for a long time and local project groups forever.
 example.*:A:1:90:90
 example.project.*:A:never:never:never</pre>
<p>When <i>groupbaseexpiry</i> is false, for class-based expiration: </p>
<pre> # Keep expired article history for 11 days, matching artcutoff plus one.
 /remember/:11
 # Set a default expiration of seven days and honour Expires: headers
 # within reasonable limits.
 *:1:7:35
 # Class 0 is retained for two weeks and honor Expires: headers
 # within reasonable limits.
 0:1:14:65</pre>
<h2>History</h2>
<p>Written by Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. Converted to <font SIZE="-1">POD</font> by Russ Allbery &lt;eagle [at] eyrie.org&gt;. </p>
<p> <tt>$Id:</tt> expire.ctl.pod 9768 2014-12-07 21:22:57Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-expire/">expire</a></i>(8), <i><a href="/docs/linux/man/8-expireover/">expireover</a></i>(8), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8), <i><a href="/docs/linux/man/8-news-daily/">news.daily</a></i>(8), <i><a href="/docs/linux/man/5-storage-conf/">storage.conf</a></i>(5), <i><a href="/docs/linux/man/3-uwildmat/">uwildmat</a></i>(3). </p>
