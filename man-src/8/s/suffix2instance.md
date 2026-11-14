---
title: "suffix2instance(8)"
name: "suffix2instance"
section: "8"
letter: "s"
url: "/docs/linux/man/8-suffix2instance/"
description: "suffix2instance – Directory Server script for finding a backend name"
---

<p>suffix2instance &#8211; Directory Server script for finding a backend name</p>
<h2>Synopsis</h2>
<p>suffix2instance [-Z serverID] -s suffix [-h]</p>
<h2>Description</h2>
<p>Maps a suffix to a backend name. This script can be run while the server is running, or stopped.</p>
<h2>Options</h2>
<p>A summary of options is included below:</p>
<dl>
<dt><code>-Z</code> <i>Server Identifier</i></p>
<dd>The server ID of the Directory Server instance. If there is only one instance on the system, this option can be skipped.</p>
<dt><code>-s</code> <i>Suffix DN</i></p>
<dd>The suffix DN to be mapped to a backend name. Example: &quot;dc=example,dc=com&quot;</p>
<dt><code>-h</code></p>
<dd>Display the usage.</dl>
<h2>Example</h2>
<dl>
<dt>suffix2instance -s &#8216;dc=example,dc=com&#8217;</p>
<dd>
<dt>suffix2instance -Z instance3 -s &#8216;dc=example,dc=com&#8217;</p>
<dd></dl>
<h2>Diagnostics</h2>
<p>Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>Author</h2>
<p>suffix2instance was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Red Hat, Inc.</p>
