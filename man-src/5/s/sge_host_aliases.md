---
title: "sge_host_aliases(5)"
name: "sge_host_aliases"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sge_host_aliases/"
description: "host_aliases – Grid Engine host aliases file format"
---

<p>host_aliases &#8211; Grid Engine host aliases file format</p>
<h2>Description</h2>
<p>All Grid Engine components use a hostname resolving service provided by the communication library to identify hosts via a unique hostname. The communication library itself references standard UNIX directory services such as DNS, NIS and /etc/hosts to resolve hostnames. In rare cases these standard services cannot be setup cleanly and Grid Engine communication daemons running on different hosts are unable to automatically determine a unique hostname for one or all hosts which can be used on all hosts. In such situations a Grid Engine host aliases file can be used to provide the communication daemons with a private and consistent hostname resolution database. </p>
<p> The location for the host aliases file is <i>&lt;ge_root&gt;/&lt;cell&gt;/common/host_aliases.</i></p>
<h2>Format</h2>
<p>For each host a single line must be provided with a blank, comma or semicolon separated list of hostname aliases. The first alias is defined to be the <code>unique</code> hostname which will be used by all Grid Engine components using the hostname aliasing service of the communication library.</p>
<h2>See Also</h2>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
