---
title: "logwatch-conf(5)"
name: "logwatch-conf"
section: "5"
letter: "l"
url: "/docs/linux/man/5-logwatch-conf/"
description: "logwatch.conf, ignore.conf, override.conf – logwatch configuration files"
---

<p>logwatch.conf, ignore.conf, override.conf &#8211; logwatch configuration files</p>
<h2>Description</h2>
<p><code>logwatch.conf</code> &#8211; ( <code>/etc/logwatch/conf/logwatch.conf</code> ) &#8211; can contain the local configuration options. The list of valid settings and their default values are in <code>/usr/share/logwatch/default.conf/logwatch.conf.</code> <code>ignore.conf</code> &#8211; ( <code>/etc/logwatch/conf/ignore.conf</code> ) is the list of regular expressions. The set of logs decribed by this set is ignored by logwatch. <code>override.conf</code> &#8211; ( <code>/etc/logwatch/conf/override.conf</code> ) contains the settings which overrides the standard configuration of specific log files or services. The syntax is the same as in log/service files. </p>
<h2>Files</h2>
<p><i>/etc/logwatch/conf/logwatch.conf</i> <i>/etc/logwatch/conf/logwatch.conf</i> <i>/etc/logwatch/conf/logwatch.conf</i> <i>/usr/share/logwatch/default.conf/logwatch.conf</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-logwatch/">logwatch</a></code>(8) </p>
