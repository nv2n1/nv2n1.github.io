---
title: "xrdcnsd(8)"
name: "xrdcnsd"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xrdcnsd/"
description: "XrdCnsd – Cluster Name Space daemon"
---

<p>XrdCnsd &#8211; Cluster Name Space daemon</p>
<h2>Synopsis</h2>
<pre><code>XrdCnsd</code> [<i>options</i>]</pre>
<h2>Description</h2>
<p>The <code>XrdCnsd</code> daemon creates and maintains a file inventory for a data server. This is known as a server-side inventory (<code>ssi</code>) service. The daemon can also be run as a one-time command to repair inventory problems. Complete HTML documentation can be found at </p>
<p> <center> <a rel="nofollow" href="http://xrootd.org/doc/prod/cms_config.htm">http://xrootd.org/doc/prod/cms_config.htm</a><br />
 </center></p>
<h2>Notes</h2>
<p>The <code>cns_ssi</code> utility is used to display a server&#8217;s inventory of files. Documentation for all components associated with <code>XrdCnsd</code> can be found at <a rel="nofollow" href="http://xrootd.org/docs.html">http://xrootd.org/docs.html</a></p>
<h2>Diagnostics</h2>
<p>Configuration errors yield an error message and a non-zero exit status. The daemon is normally started as piped command via an xrootd daemon configuration directive.</p>
<h2>License</h2>
<p>License terms can be displayed by typing &quot;<code>xrootd -H</code>&quot;.</p>
<h2>Support Level</h2>
<p>The <code>XrdCnsd</code> daemon is supported by the xrootd collaboration. Contact information can be found at <center> <a rel="nofollow" href="http://xrootd.org/contact.html">http://xrootd.org/contact.html</a><br />
 </center></p>
