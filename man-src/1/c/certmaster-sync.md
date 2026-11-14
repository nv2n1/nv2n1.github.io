---
title: "certmaster-sync(1)"
name: "certmaster-sync"
section: "1"
letter: "c"
url: "/docs/linux/man/1-certmaster-sync/"
description: "certmaster-sync — synchronize client certificates with Func."
---

<h2 class="name">NAME</h2>
<p> certmaster-sync &#8212; synchronize client certificates with Func. </p>
<h2>SYNOPSIS</h2>
<p> certmaster-sync [-f|&#8211;force]</p>
<h2>DESCRIPTION</h2>
<p> certmaster-sync synchronizes client certificates amongst certmaster clients via Func. It is assumed that the hosts who have requested certificates are reachable via Func for synchronization operations. </p>
<p> certmaster-sync by default is called as a post-sign and post-clean trigger. In order to enable synchronization you must set <code>sync_certs</code> to <code>True</code>, see <font SIZE="-1"><code>CONFIGURATION</code></font><font SIZE="-1"><code>VALUES</code></font> below. </p>
<p> The synchronization occurs by querying remote Func methods in <code>certmastermod</code> on the minion hosts. This will gather information, copy any new certificates, and remove any certificates that have been cleaned.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-f, &#8211;force</p>
<dd> Override the configuration value for <code>sync_certs</code> in <i>/etc/certmaster/certmaster.conf</i></dl>
<h2>CONFIGURATION VALUES</h2>
<dl>
<dt>sync_certs</p>
<dd> <code>sync_certs</code> determines whether or not the script will actually synchronize or if it will exit with no operation. You can use -f|&#8211;force to override this configuration value. (Default: False)</dl>
<h2>ADDITONAL RESOURCES</h2>
<p> See <a rel="nofollow" href="https://fedorahosted.org/certmaster.">https://fedorahosted.org/certmaster.</a> It&#8217;s a Wiki. See also <a rel="nofollow" href="https://fedorahosted.org/func">https://fedorahosted.org/func</a></p>
<h2>AUTHOR</h2>
<p> John Eckersberg &lt;jeckersb [at] redhat.com&gt; </p>
<h2>Index</h2>
