---
title: "mbexamine(8)"
name: "mbexamine"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mbexamine/"
description: "mbexamine – examine a cyrus-format mailbox"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>mbexamine &#8211; examine a cyrus-format mailbox</p>
<h2>Synopsis</h2>
<p><code>mbexamine</code> [ <code>-C</code> <i>config-file</i> ] [ <code>-u uid</code> ] <i>mailbox</i>&#8230;<br />
 <code>mbexamine</code> [ <code>-C</code> <i>config-file</i> ] [ <code>-s seqnum</code> ] <i>mailbox</i>&#8230;<br />
 <code>mbexamine</code> [ <code>-C</code> <i>config-file</i> ] <code>-q</code> <i>mailbox</i>&#8230;</p>
<h2>Description</h2>
<p><i>Mbexamine</i> will examine the header, index, and cache files of a cyrus format mailbox and dump the information contained therein. It can also limit its output to a specific uid or sequence number, through use of the -s and -u switches. <i>Mbexamine</i> reads its configuration options out of the <i><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a></i>(5) file unless specified otherwise by <code>-C</code>. It uses the mboxlist database to locate the mailbox on disk.</p>
<h2>Options</h2>
<dl>
<dt><code>-C</code><i> config-file</i></p>
<dd>Read configuration options from <i>config-file</i>.</p>
<dt><code>-s</code></p>
<dd>Dump information for the given sequence number only.</p>
<dt><code>-u</code></p>
<dd>Dump information for the given uid only.</p>
<dt><code>-q</code></p>
<dd>Compare the quota usage in cyrus.index to the actual message file sizes and report any differences. If there are differences, the mailbox SHOULD be reconstructed.</dl>
<h2>Files</h2>
<p><code>/etc/imapd.conf</code></p>
