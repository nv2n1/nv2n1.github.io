---
title: "host_aliases(5)"
name: "host_aliases"
section: "5"
letter: "h"
url: "/docs/linux/man/5-host_aliases/"
description: "host_aliases – xxQS_NAMExx host aliases file format"
---

<p>host_aliases &#8211; xxQS_NAMExx host aliases file format</p>
<h2>Description</h2>
<p>All xxQS_NAMExx components use a hostname resolving service provided by the communication library to identify hosts via a unique hostname. The communication library itself references standard UNIX directory services such as DNS, NIS and /etc/hosts to resolve hostnames (through the Name Service Switch on systems which support it). In some cases, typically clusters with hosts on multiple networks, these standard services cannot be setup cleanly, and xxQS_NAMExx daemons running on different hosts are unable to determine automatically a unique hostname for one or all hosts which can be used on all hosts. In such situations a xxQS_NAMExx host aliases file can be used to provide the daemons with a private and consistent hostname resolution database. </p>
<p> The location for the host aliases file is <i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common/host_aliases</i>.</p>
<h2>Format</h2>
<p>For each host a single line must be provided with a blank-, comma-, or semicolon-separated list of hostname aliases. The first alias is defined to be the <code>unique</code> hostname which will be used by all xxQS_NAMExx components using the hostname aliasing service of the communication library.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-nsswitch-conf/">nsswitch.conf</a></i>(5).</p>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
