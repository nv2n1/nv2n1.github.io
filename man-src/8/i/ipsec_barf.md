---
title: "ipsec_barf(8)"
name: "ipsec_barf"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipsec_barf/"
description: "ipsec_barf – spew out collected IPsec debugging information"
---

<p>ipsec_barf &#8211; spew out collected IPsec debugging information</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ipsec</code> <i>barf</i> [&#8211;short &#8211;maxlines&nbsp;<wbr><i>&lt;100&gt;</i>]</dl>
<h2>Description</h2>
<p><i>Barf</i></p>
<dd>outputs (on standard output) a collection of debugging information (contents of files, selections from logs, etc.) related to the IPsec encryption/authentication system. It is primarily a convenience for remote debugging, a single command which packages up (and labels) all information that might be relevant to diagnosing a problem in IPsec. </p>
<p> The <code>&#8211;short</code> option limits the length of the log portion of <i>barf</i>&#8216;s output, which can otherwise be extremely voluminous if debug logging is turned on. </p>
<p> <code>&#8211;maxlines &lt;100&gt;</code> option sets the length of some bits of information, currently netstat -rn. Useful on boxes where the routing table is thousands of lines long. Default is 100. </p>
<p> On systems with systemd, ipsec barf will look for logs using the journalctl command. If the logfile= option is used, logs will also not be found by the ipsec barf command. </p>
<p> <i>Barf</i> censors its output, replacing keys and secrets with brief checksums to avoid revealing sensitive information. </p>
<p> Beware that the output of both commands is aimed at humans, not programs, and the output format is subject to change without warning. </p>
<p> <i>Barf</i> has to figure out which files in /var/log contain the IPsec log messages. It looks for KLIPS and general log messages first in <i>messages</i> and <i>syslog</i>, and for Pluto messages first in <i>secure</i>, <i>auth.log</i>, and <i>debug</i>. In both cases, if it does not find what it is looking for in one of those &#8220;likely&#8221; places, it will resort to a brute-force search of most (non-compressed) files in /var/log.</p>
<h2>Files</h2>
<dl>
<dd>
<pre>/proc/net/*
/var/log/*
/etc/ipsec.conf
/etc/ipsec.secrets</pre>
</dl>
<h2>History</h2>
<p>Written for the Linux FreeS/WAN project &lt;m[blue]<code><a rel="nofollow" href="http://www.freeswan.org">http://www.freeswan.org</a></code>m[]&gt; by Henry Spencer.</p>
<h2>Bugs</h2>
<p><i>Barf</i> uses heuristics to try to pick relevant material out of the logs, and relevant messages which are not labelled with any of the tags that <i>barf</i> looks for will be lost. We think we&#8217;ve eliminated the last such case, but one never knows&#8230; </p>
<p> Finding <i>updown</i> scripts (so they can be included in output) is, in general, difficult. <i>Barf</i> uses a very simple heuristic that is easily fooled. </p>
<p> The brute-force search for the right log files can get expensive on systems with a lot of clutter in /var/log.</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
