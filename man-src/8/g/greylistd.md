---
title: "greylistd(8)"
name: "greylistd"
section: "8"
letter: "g"
url: "/docs/linux/man/8-greylistd/"
description: "greylistd – simple greylisting system for mail transport agents"
---

<p>greylistd &#8211; simple greylisting system for mail transport agents</p>
<h2>Synopsis</h2>
<p><code>greylistd</code></p>
<h2>Description</h2>
<h3>Greylisting</h3>
<p>This daemon provides a simple greylisting implementation for use with Exim and other mail transport agents (MTAs). For a more elaborate introduction to greylisting, please refer to Evan Harris&#8217; whitepaper at: <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><a rel="nofollow" href="http://projects.puremagic.com/greylisting/">http://projects.puremagic.com/greylisting/</a></p>
<p> Greylisting is a simple but highly effective means to weed out messages that are being delivered via spamware/ratware tools. The idea is to establish whether a prior relationship exists between the sender and the receiver of a message. Most of the time it does, and the delivery proceeds normally. </p>
<p> On the other hand, if no prior relationship exists, the delivery is temporarily rejected, using a 451 SMTP response. Legitimate MTAs will treat this response accordingly, and retry the delivery in a while. In contrast, ratware will usually fail to retry the delivery in a normal fashion. </p>
<p> As a result, greylisting is currently more than 90% effective in blocking incoming junk mail, while nearly all legitimate mail goes through. </p>
<p> Three pieces of information (herafter called a <i>triplet</i>) from the delivery attempt are cached for future reference: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211; The address of the host attempting the delivery<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; The envelope sender address&nbsp;<wbr>(MAIL FROM:)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; The envelope recipient address&nbsp;<wbr>(RCPT TO:) </p>
<p> If a delivery attempt was temporarily rejected, then after an initial timeout (60 minutes by default), but before a retry expiration time (8 hours by default), new delivery attempts with the same <i>triplet</i> are accepted, and the <i>triplet</i> is added to a whitelist. This allows for delivery retries, presumably from legitimate MTAs, and ensures that future mail from the same contact is not subject to greylisting. </p>
<p> If a whitelisted <i>triplet</i> has not been seen for an extended duration (by default 60 days), it is expired. This prevents unlimited growth of the list. </p>
<p> The downside to greylisting is that legitimate mail from people who have never sent you mail in the past (or, at least, within the last 60 days) are subject to a one-hour delay. </p>
<p> The upside is that the current generation of ratware tools will not be able to deliver spam or virii to you. Even if, as a result of lots of sites incorporating the greylisting concept, ratware tools are modified such that temporarily rejected deliveries are retried, you stand an increased chance of blocking such mail. That is because within the mandatory 1-hour initial delay, chances are that the sending host&#8217;s IP address has been listed in one or more DNS block lists (such as bl.spamcop.net, cbl.abuseat.org, etc..), and can be rejected by your MTA by consulting these lists directly, or via anti-spam software like SpamAssassin.</p>
<h3>greylistd</h3>
<p><code>greylistd</code> is meant to be installed on a server that accepts incoming mail. The MTA on this server connects to the greylistd daemon over a UNIX domain socket (by default <i>/var/run/greylistd/socket</i>), or alternatively via the command <code><a href="/docs/linux/man/1-greylist/">greylist</a></code>(1), and submits a string (<i>triplet</i>) that identifies a particular host/sender/recipient relationship. <code>greylistd</code> responds &quot;white&quot;, &quot;grey&quot; or &quot;black&quot;, depending on the current listing status of the provided <i>triplet</i>. Alternatively, if either of the &quot;&#8211;white&quot;, &quot;&#8211;grey&quot;, or &quot;&#8211;black&quot; options precede the data, <code>greylistd</code> responds &quot;true&quot; or &quot;false&quot;, indicating whether the triplet is currently in the corresponding state.</p>
<h2>Examples</h2>
<h3>Exim 4</h3>
<p>A sample greylistd statement for Exim 4 is provided with this package, and can normally be found in &quot;/usr/share/doc/greylistd/examples/exim4-acl-example.txt&quot;.</p>
<h3>Others</h3>
<p>What others? :-) A prerequisite to greylisting in general is the ability to perform custom filtering throughout the various stages in the SMTP transaction, most notably after the <code>RCPT TO:</code> SMTP command. In particular, <code><a href="/docs/linux/man/8-greylistd/">greylistd</a></code>(8) can be invoked either over a UNIX domain socket or via the supplied <code><a href="/docs/linux/man/1-greylist/">greylist</a></code>(1) utility. Although <code><a href="/docs/linux/man/8-greylistd/">greylistd</a></code>(8) is written mainly with Exim in mind, it should be possible to use it with any MTA that:</p>
<dl>
<dt> &#8211;</p>
<dd>Allows arbitrary strings to be passed on via a UNIX domain socket (<code>/var/run/greylistd/socket</code>) or supplied to external programs (<code><a href="/docs/linux/man/1-greylist/">greylist</a></code>(1)).</p>
<dt> &#8211;</p>
<dd>Can defer the incoming delivery, based on the response.</dl>
<p> Some MTAs either have limited or no support for such external filters in the SMTP transaction (e.g. Sendmail), or define a very custom interface for such filters (e.g. Postifx &quot;Policy Servers&quot;). That said, solutions exist for these other MTAs as well. For Postfix, check into &quot;postgrey&quot;, and for Sendmail there is &quot;relaydelay&quot;. For other MTAs, check the links on Evan Harris&#8217; greylisting project page:<br />
&nbsp;<wbr><a rel="nofollow" href="http://projects.puremagic.com/greylisting/links.html">http://projects.puremagic.com/greylisting/links.html</a> </p>
<h2>Files</h2>
<h3>/etc/greylistd/config</h3>
<p>Configuration settings. Currently, this file consists of three sections:</p>
<dl>
<dt>[timeout]</p>
<dd>Lists various timeouts used to determine how long to keep a new <i>triplet</i> greylisted, and when to expire previosly known <i>triplet</i>s.</p>
<dt>[socket]</p>
<dd>Specifies path and permissions of the UNIX domain socket on which <code>greylistd</code> will listen.</p>
<dt>[data]</p>
<dd>Specifies the paths to the data files, containing the data items and statistics, as well as an <i>update interval</i> specifying how often data will be written to these files.</dl>
<h3>/var/lib/greylistd/states</h3>
<p>(default path, can be modified in the configuration file) </p>
<p> Runtime data. Theare are four sections: <code>[white]</code>, <code>[grey]</code>, <code>[black]</code> and <code>[statistics]</code>. The first three sections consist of lines of the form: </p>
<p>&nbsp;<wbr><i>hash</i>&nbsp;<wbr>=&nbsp;<wbr><i>lastseen firstseen count</i> </p>
<p> where:</p>
<dl>
<dt> &#8211;</p>
<dd><i>hash</i> is a 32-bit value representing a given <i>triplet</i>,</p>
<dt> &#8211;</p>
<dd><i>lastseen</i> is a 32-bit value representing the timestamp of last delivery attempt for this triplet,</p>
<dt> &#8211;</p>
<dd><i>firstseen</i> is a 32-bit value representing the timestamp of first known delivery attempt for this triplet,</p>
<dt> &#8211;</p>
<dd><i>count</i> is a 32-bit value representing the number of delivery attempts that have been made for this triplet in this time period.</dl>
<p> The <code>[statistics]</code> section contains a counter for each of the three lists, indicating how many items that has ever made its way into these lists by way of the <code>update</code> protocol.</p>
<h3>/var/lib/greylistd/triplets</h3>
<p>(default path, can be modified in the configuration file) </p>
<p> Unhashed data &#8211; i.e. the original triplets passed to greylistd. Internally, <code><a href="/docs/linux/man/8-greylistd/">greylistd</a></code>(8) hashes the provided data into a single 32-bit value for efficiency. Prior to version 0.6, the original data was not retained; as of version 0.6, data is optionally saved into this file. </p>
<p> Data items are saved in the form:<br />
&nbsp;<wbr><i>hash</i>&nbsp;<wbr>=&nbsp;<wbr><i>data</i>&nbsp;<wbr>&#8230;</p>
<h3>/var/run/greylistd/socket</h3>
<p>(default path, can be modified in the configuration file) </p>
<p> The UNIX domain socket providing the main interface to &quot;greylistd&quot;. The MTA can either connect to this socket directly, or use the supplied &quot;greylist&quot; utility to do so.</p>
<h2>Bugs</h2>
<p>Because <i>triplet</i>s and timestamps are hashed into simple 32-bit values, there is a very slim chance that deliveries that should have been greylisted are allowed through. More so for very busy sites. </p>
<p> Commands are actually executed in the daemon, not the &quot;greylist&quot; client. If the user who invokes &quot;greylist&quot; interactively has a different time zone than the daemon process, time and date representations in the output will reflect those of the daemon.</p>
<h2>Author</h2>
<p>This python script and manual page is written by Tor Slettnes, originally for Debian GNU/Linux.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004-2005 Tor Slettnes. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> On a Debian GNU/Linux system, the full text of the GPL is available in /usr/share/common-licenses/GPL. It is also available at: </p>
<p>&nbsp;<wbr><a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a></p>
<h2>See Also</h2>
<dl>
<dt><a rel="nofollow" href="http://projects.puremagic.com/greylisting/">http://projects.puremagic.com/greylisting/</a></p>
<dd>Evan Harris&#8217; greylisting whitepaper</p>
<dt><code><a href="/docs/linux/man/1-greylist/">greylist</a></code>(1)</p>
<dd>Command-line interface to the greylist daemon.</p>
<dt><code><a href="/docs/linux/man/8-greylistd-setup-exim4/">greylistd-setup-exim4</a></code>(8)</p>
<dd>Utility to add/remove support for greylistd in Exim 4 configuration files. </p>
