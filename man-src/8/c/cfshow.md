---
title: "cfshow(8)"
name: "cfshow"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cfshow/"
description: "cfshow – Dump cfengine databases"
---

<p>cfshow &#8211; Dump cfengine databases</p>
<h2>Synopsis</h2>
<p>/usr/local/sbin/cfshow [options] </p>
<h2>Description</h2>
<p><code>cfengine</code> is a language based system specifically designed for testing and configuring unix-like systems attached to a TCP/IP network. cfshow is a tool for showing the contents of the internal databases used by cfengine in its operation. Many users will not care about these internal details, while cfengine manages the system transparently. More advanced users might desire a simple way to dump the contents of these databases to text, for reporting purposes. HTML and XML versions of the output are provided for easy integration with reporting. </p>
<h2>Examples</h2>
<p>cfshow &#8211;locks cfshow &#8211;last-seen cfshow &#8211;checksum cfshow &#8211;active cfshow &#8211;audit cfshow &#8211;classes cfshow &#8211;regex These show the named databases. </p>
<h2>Options</h2>
<p>Here are all of the options supported: </p>
<p> &#8211;help (-h) &#8211;debug (-d) &#8211;verbose (-v) &#8211;locks (-l) &#8211;last-seen (-s) &#8211;performance (-p) &#8211;checksum (-c) &#8211;classes (-C) &#8211;filename (-f) &#8211;regex (-r) &#8211;active (-a) &#8211;version (-V) &#8211;html (-H) &#8211;xml (-X) &#8211;purge (-P) &#8211;audit (-A)</p>
<h2>Files</h2>
<p>cfshow reads cfengine internal information that is normally stored in the Work Directory /var/cfengine.</p>
<h2>Author</h2>
<p>Mark Burgess, Oslo University College</p>
<h2>Information</h2>
<p><a rel="nofollow" href="http://www.cfengine.org">http://www.cfengine.org</a></p>
