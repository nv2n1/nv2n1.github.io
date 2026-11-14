---
title: "frm_xfrd(8)"
name: "frm_xfrd"
section: "8"
letter: "f"
url: "/docs/linux/man/8-frm_xfrd/"
description: "frm_xfrd – File Residency Manager transfer daemon"
---

<p>frm_xfrd &#8211; File Residency Manager transfer daemon</p>
<h2>Synopsis</h2>
<pre><code>frm_xfrd</code> [<i>options</i>]</pre>
<h2>Description</h2>
<p>The <code>frm_xfrd</code> daemon automatically copies files in and out of the data server. It is part of the File Residency Manager software suite. Usage synopsis can be displayed by typing &quot;<code>frm_xfrd -h</code>&quot;. Complete HTML documentation can be found at </p>
<p> <center> <a rel="nofollow" href="http://xrootd.org/doc/prod/frm_config.htm">http://xrootd.org/doc/prod/frm_config.htm</a><br />
 </center></p>
<h2>Notes</h2>
<p>Documentation for all components associated with <code>frm_xfrd</code> can be found at <a rel="nofollow" href="http://xrootd.org/docs.html">http://xrootd.org/docs.html</a></p>
<h2>Diagnostics</h2>
<p>Configuration errors yield an error message and a non-zero exit status. The program never exits upon success. Use the kill command or &quot;/etc/init.d/frm_xfrd stop&quot; to terminate the program.</p>
<h2>License</h2>
<p>License terms can be displayed by typing &quot;<code>xrootd -H</code>&quot;.</p>
<h2>Support Level</h2>
<p>The <code>frm_xfrd</code> daemon is supported by the xrootd collaboration. Contact information can be found at <center> <a rel="nofollow" href="http://xrootd.org/contact.html">http://xrootd.org/contact.html</a><br />
 </center></p>
