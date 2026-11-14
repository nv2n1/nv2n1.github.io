---
title: "amanda-taperscan(7)"
name: "amanda-taperscan"
section: "7"
letter: "a"
url: "/docs/linux/man/7-amanda-taperscan/"
description: "amanda-taperscan – Amanda Taperscan Algorithms"
---

<p>amanda-taperscan &#8211; Amanda Taperscan Algorithms</p>
<h2>Description</h2>
<p>Amanda uses a <i>taperscan algorithm</i> to select volumes on which to store dumps. Historically Amanda has provided only one, fairly complex taperscan algorithm, but this algorithm did not suit the needs of all users. Now Amanda offers a wide array of algorithms to suit varied needs. Adding new algorithms is not difficult. </p>
<p> The taperscan algorithm is specified with the <code>taperscan</code> parameter, which has a default value of <code>traditional</code>. </p>
<p> Taperscan algorithms are implemented as perl packages with the prefix Amanda::Taper::Scan::. See the perl documentation for Amanda::Taper::Scan for more information.</p>
<h2>Defining A Taperscan</h2>
<p>An taperscan is defined in <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5) as follows: </p>
<pre>define taperscan $taperscan_name {
 comment &quot;$comment&quot;
 plugin &quot;$pluginname&quot;
 property &quot;$PROPERTY_NAME&quot; &quot;$PROPERTY_VALUE&quot;
 ...
}</pre>
<p>and then referenced in the global section as </p>
<pre> taperscan &quot;$taperscan_name&quot;</pre>
<p>Taperscan properties, like Amanda configuration parameters, are insensitive to case, and &#8211; (dash) and _ (underscore) may be used interchangeably. </p>
<p> See the individual plugin documentation below for properties applicable to each plugin.</p>
<h2>Taperscan Algorithms</h2>
<p>In general, these algorithms will only select reusable volumes. These are volumes which are listed in the <code><a href="/docs/linux/man/5-tapelist/">tapelist</a></code>(5) with the <i>reuse</i> flag, and which are not among the <i>tapecycle-1</i> most recent volumes in the list. Put another way, reusable volumes do not contain data that must be retained. Note that if fewer than <i>tapecycle-1</i> volumes have been written then there are no reusable volumes. Newly labeled volumes (volumes that have been labeled with <code>amlabel</code> but never used) are considered reusable. </p>
<p> Many of these algorithms look for the oldest reusable volume. In most cases, this is the best volume to overwrite, as the data it contains is older than that on any other volume. If there are no reusable volumes, then there is no oldest reusable volume.</p>
<h3>traditional</h3>
<p>This algorithm duplicates Amanda&#8217;s historical behavior, and it operates in two stages. </p>
<p> First, if there is an oldest reusable volume and if the changer supports &quot;fast&quot; searches, then the algorithm uses the changer to search for that volume. Newly labeled volumes are not considered when calculating the oldest reusable volume. Consequently, this taperscan algorithm prefers volumes which have been used before to newly-labeled volumes when a fast-searchable changer is in use. </p>
<p> Second, if there is no oldest reusable volume, or if that volume is not available in the changer, then the algorithm begins a sequential scan of the changer, starting at the current slot. It selects the first suitable volume it finds: a reusable volume (perhaps newly-labeled) or, if <code>autolabel</code> includes <code>empty</code>, a blank volume. Even across multiple invocations (when <i>runtapes &gt; 1</i>), it will not return the same slot twice. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 This algorithm shows an undue preference for volumes already containing data, by omitting newly-labeled volumes from its first stage. Historically, many Amanda changer scripts were not fast-searchable (including <i>chg-multi</i>, <i>chg-disk</i> and, if <i>havereader=0</i>, <i>chg-zd-mtx</i>), and thus skipped the first stage, allowing new volumes to find their way into the tape cycle. New changers are almost all fast-searchable, so both stages of the algorithm are used and new tapes may be unexpectedly excluded. If this causes an undesirable change in behavior, consider one of the other taperscan algorithms..sp .5v</dl>
<h3>oldest</h3>
<p>This algorithm works with the Changer API (see <code><a href="/docs/linux/man/7-amanda-changers/">amanda-changers</a></code>(7)), using the inventory returned by the changer to locate the oldest acceptable volume available. Note that this will not work with changers that do not support inventory (old changers). The algorithms scans unknown slots only if no known usable volume is found in the inventory. </p>
<p> An acceptable volume is a reusable volume, a new labeled volume or an unlabeled volume that can be labeled according to <code>autolabel</code>. Note that changers do not always know the contents of every slot &#8211; for example, a tape with an unknown barcode will not be considered usable. </p>
<p> Use <code>amtape CONF inventory</code> to see the changer&#8217;s inventory, and use <code>amtape CONF update</code> to update it.</p>
<h3>lexical</h3>
<p>This algorithm also works with the Changer API, using the inventory to determine the acceptable volumes; it then uses the volume which follows the last-used volume in lexical order. For volume labels containing leading zeros, e.g., CORP-010, this algorithm will run through the volumes in the natural order. </p>
<p> It scans unknown slots only if no usable volume is found in the inventory. </p>
<p> See <code>oldest</code>, above, for a definition of acceptable volumes.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), <code><a href="/docs/linux/man/5-tapelist/">tapelist</a></code>(5), <code><a href="/docs/linux/man/7-amanda-changers/">amanda-changers</a></code>(7), <code><a href="/docs/linux/man/7-amanda-interactivity/">amanda-interactivity</a></code>(7) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Author</h2>
<p><code>Dustin J. Mitchell</code> &lt;dustin [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
