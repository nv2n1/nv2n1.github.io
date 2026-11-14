---
title: "mbpath(8)"
name: "mbpath"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mbpath/"
description: "mbpath – translate mailbox names to filesystem paths"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p>mbpath &#8211; translate mailbox names to filesystem paths</p>
<h2>Synopsis</h2>
<p><code>mbpath</code> [ <code>-C</code> <i>config-file</i> ] [ <code>-q</code> ] [ <code>-s</code> ] [ <code>-m</code> ] [ <i>mailbox-names</i>&#8230; ]</p>
<h2>Description</h2>
<p>Given a mailbox name or a space separated list of mailbox names, <i>mbpath</i> outputs the filesystem path to the mailbox. </p>
<p> <i>Mbpath</i> reads its configuration options out of the <i><a href="/docs/linux/man/5-imapd-conf/">imapd.conf</a></i>(5) file unless specified otherwise by <code>-C</code>.</p>
<h2>Options</h2>
<dl>
<dt><code>-C</code><i> config-file</i></p>
<dd>Read configuration options from <i>config-file</i>.</dl>
<p> <i>-q</i> suppress any error output. </p>
<p> <i>-s</i> if any error occurs, stop processing the list of mailboxes and exit. </p>
<p> <i>-m</i> output the path to the metadata files (if different from the message files).</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/imapd.conf</code></p>
<dd></dl>
