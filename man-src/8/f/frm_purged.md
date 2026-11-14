---
title: "frm_purged(8)"
name: "frm_purged"
section: "8"
letter: "f"
url: "/docs/linux/man/8-frm_purged/"
description: "frm_purged – File Residency Manager purge daemon"
---

<p>frm_purged &#8211; File Residency Manager purge daemon</p>
<h2>Synopsis</h2>
<pre><code>frm_purged</code> [<i>options</i>] [<i>parameters</i>]</pre>
<h2>Description</h2>
<p>The <code>frm_purged</code> daemon automatically removes disk resident files based on a set of local rules. It is part of the File Residency Manager software suite. Usage synopsis can be displayed by typing &quot;<code>frm_purged -h</code>&quot;. Complete HTML documentation can be found at </p>
<p> <center> <a rel="nofollow" href="http://xrootd.org/doc/prod/frm_config.htm">http://xrootd.org/doc/prod/frm_config.htm</a><br />
 </center></p>
<h2>Notes</h2>
<p>Documentation for all components associated with <code>frm_purged</code> can be found at <a rel="nofollow" href="http://xrootd.org/docs.html">http://xrootd.org/docs.html</a></p>
<h2>Diagnostics</h2>
<p>Configuration errors yield an error message and a non-zero exit status. The program never exits upon success. Use the kill command or &quot;/etc/init.d/frm_purged stop&quot; to terminate the program.</p>
<h2>License</h2>
<p>License terms can be displayed by typing &quot;<code>xrootd -H</code>&quot;.</p>
<h2>Support Level</h2>
<p>The <code>frm_purged</code> daemon is supported by the xrootd collaboration. Contact information can be found at <center> <a rel="nofollow" href="http://xrootd.org/contact.html">http://xrootd.org/contact.html</a><br />
 </center></p>
