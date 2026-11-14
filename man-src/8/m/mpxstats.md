---
title: "mpxstats(8)"
name: "mpxstats"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mpxstats/"
description: "mpxstats – Multiplexing Monitor Statistics daemon"
---

<p>mpxstats &#8211; Multiplexing Monitor Statistics daemon</p>
<h2>Synopsis</h2>
<pre><code>mpxstats</code> [<i>options</i>] <code>-p</code> <i>port</i></pre>
<h2>Description</h2>
<p>The <code>mpxstats</code> daemon multiplexes xrootd and cmsd monitoring data streams into a single sequential format suitable for ingestion by a monitoring agent (e.g. ganglia, MonaLisa, nagios, etc.). Usage synopsis can be displayed by typing &quot;<code>mpxstats</code>&quot;. Complete HTML documentation can be found at </p>
<p> <center> <a rel="nofollow" href="http://xrootd.org/doc/prod/xrd_monitoring.htm">http://xrootd.org/doc/prod/xrd_monitoring.htm</a><br />
 </center></p>
<h2>Notes</h2>
<p>Documentation for all components associated with <code>mpxstats</code> can be found at <a rel="nofollow" href="http://xrootd.org/docs.html">http://xrootd.org/docs.html</a></p>
<h2>Diagnostics</h2>
<p>Errors yield an error message and a non-zero exit status. The program never exits upon success. Use the kill command to terminate the program.</p>
<h2>License</h2>
<p>License terms can be displayed by typing &quot;<code>xrootd -H</code>&quot;.</p>
<h2>Support Level</h2>
<p>The <code>mpxstats</code> daemon is supported by the xrootd collaboration. Contact information can be found at <center> <a rel="nofollow" href="http://xrootd.org/contact.html">http://xrootd.org/contact.html</a><br />
 </center></p>
