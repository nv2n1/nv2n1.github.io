---
title: "xrdpfc_print(8)"
name: "xrdpfc_print"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xrdpfc_print/"
description: "xrdpfc_print – print content of ProxyFileCache meta data"
---

<p>xrdpfc_print &#8211; print content of ProxyFileCache meta data</p>
<h2>Synopsis</h2>
<pre><code>xrdpfc_print</code> [<i>options</i>] path
<i>options</i>: [<code>--config</code> <i>args</i>] [<code>--verbose</code>] [<code>--help</code>]</pre>
<h2>Description</h2>
<p>The <code>xrdpfc_print</code> prints status of downloaded file blocks and access statistics of cached files</p>
<h2>Options</h2>
<p><code>-c</code> | <code>&#8211;config</code></p>
<dl>
<dd>xrootd configuration file. Used to load non-default file system (directive ofs.osslib) and prefix for the location of cached files (directive oss.localroot) </p>
</dl>
<p> <code>-v</code> | <code>&#8211;verbose</code></p>
<dl>
<dd>prints additional info for each downloaded file block </p>
</dl>
<p> <code>-h</code> | <code>&#8211;help</code></p>
<dl>
<dd>displays usage information. </p>
</dl>
<h2>Operands</h2>
<p>path</p>
<dl>
<dd>Path to a file or directory for which the information is to be printed. Path can be relative or absoulte. If the path begins with root:/ the path is assumed to be a LFN and gets translated via the standard OSS rules (in the least, it gets prefixed by the oss.localroot). In this case &#8211;config option is mandatory. </p>
</dl>
<h2>Notes</h2>
<p>Documentation for all components associated with <code>xrdpfc_print</code> can be found at <a rel="nofollow" href="http://xrootd.org/docs.html">http://xrootd.org/docs.html</a></p>
<h2>Diagnostics</h2>
<p>Errors yield an error message and a non-zero exit status.</p>
<h2>License</h2>
<p>License terms can be displayed by typing &quot;<code>xrootd -H</code>&quot;.</p>
<h2>Support Level</h2>
<p>The <code>xrdpfc_print</code> command is supported by the xrootd collaboration. Contact information can be found at <center> <a rel="nofollow" href="http://xrootd.org/contact.html">http://xrootd.org/contact.html</a><br />
 </center></p>
