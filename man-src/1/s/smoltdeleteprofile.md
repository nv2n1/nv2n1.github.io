---
title: "smoltdeleteprofile(1)"
name: "smoltdeleteprofile"
section: "1"
letter: "s"
url: "/docs/linux/man/1-smoltdeleteprofile/"
description: "smoltDeleteProfie – Delete Smolt hardware profile from server"
---

<p>smoltDeleteProfie &#8211; Delete Smolt hardware profile from server</p>
<h2>Synopsis</h2>
<p><code>smoltDeleteProfile</code> [options]</p>
<h2>Description</h2>
<p><code>smoltDeleteProfile</code> deletes the machine&#8217;s profile from a remote Smoon server. Smolt is a cross-desktop hardware reporting tool for GNU/Linux based systems.</p>
<dl COMPACT>
<dt></dl>
<h2>Options</h2>
<dd>
<dl COMPACT>
<dt>-s <i>SMOON_URL</i>, &#8211;server=<i>SMOON_URL</i></p>
<dd>Specify the URL of the server</p>
<dt>-u <i>USERAGENT</i>, &#8211;useragent=<i>USERAGENT</i>, &#8211;user_agent=<i>USERAGENT</i></p>
<dd>Specify HTTP user agent (default &quot;smolt/0.97&quot;)</p>
<dt>-t <i>TIMEOUT</i>, &#8211;timeout=<i>TIMEOUT</i></p>
<dd>Specify HTTP timeout in seconds (default 60.0 seconds)</p>
<dt>&#8211;uuidFile=<i>UUIDFILE</i></p>
<dd>Specify which UUID to use; useful for debugging and testing</p>
<dt>-d, &#8211;debug</p>
<dd>Enable debug information</p>
<dt>&#8211;version</p>
<dd>Show program&#8217;s version number and exit</p>
<dt>-h, &#8211;help</p>
<dd>Show this help message and exit</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-smoltsendprofile/">smoltSendProfile</a></code>(1), <code><a href="/docs/linux/man/1-smoltgui/">smoltGui</a></code>(1).</p>
<h2>Author</h2>
<p><code>smoltSendProfile</code> was written by Mike McGrath &lt;mmcgrath [at] redhat.com&gt; and others. </p>
<p> This manual page was written by Chris Lamb &lt;chris [at] chris-lamb.co.uk&gt;, for the Debian project (but may be used by others).</p>
