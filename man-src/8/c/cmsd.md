---
title: "cmsd(8)"
name: "cmsd"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cmsd/"
description: "cmsd – Cluster Management Services daemon"
---

<p>cmsd &#8211; Cluster Management Services daemon</p>
<h2>Synopsis</h2>
<pre><code>cmsd</code> [<i>options</i>] <code>-c</code> <i>configfile</i></pre>
<h2>Description</h2>
<p>The <code>cmsd</code> daemon provides cluster services to xrootd data servers. Usage synopsis can be displayed by typing &quot;<code>cmsd -h</code>&quot;. Complete HTML documentation can be found at </p>
<p> <center> <a rel="nofollow" href="http://xrootd.org/doc/prod/cms_config.htm">http://xrootd.org/doc/prod/cms_config.htm</a><br />
 </center></p>
<h2>Notes</h2>
<p>Documentation for all components associated with <code>cmsd</code> can be found at <a rel="nofollow" href="http://xrootd.org/docs.html">http://xrootd.org/docs.html</a></p>
<h2>Diagnostics</h2>
<p>Configuration errors yield an error message and a non-zero exit status. The program never exits upon success. Use the kill command or &quot;/etc/init.d/cmsd stop&quot; to terminate the program.</p>
<h2>License</h2>
<p>License terms can be displayed by typing &quot;<code>cmsd -H</code>&quot;.</p>
<h2>Support Level</h2>
<p>The <code>cmsd</code> daemon is supported by the xrootd collaboration. Contact information can be found at <center> <a rel="nofollow" href="http://xrootd.org/contact.html">http://xrootd.org/contact.html</a><br />
 </center></p>
