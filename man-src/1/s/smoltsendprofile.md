---
title: "smoltsendprofile(1)"
name: "smoltsendprofile"
section: "1"
letter: "s"
url: "/docs/linux/man/1-smoltsendprofile/"
description: "smoltSendProfie – Submit Smolt hardware profile to server"
---

<p>smoltSendProfie &#8211; Submit Smolt hardware profile to server</p>
<h2>Synopsis</h2>
<p><code>smoltSendProfile</code> [options]</p>
<h2>Description</h2>
<p><code>smoltSendProfile</code> program submits the hardware profile of the current machine to the Smoon server. Smolt is a cross-desktop hardware reporting tool for GNU/Linux based systems.</p>
<dl COMPACT>
<dt></dl>
<h2>Options</h2>
<dd>
<dl COMPACT>
<dt>-p, &#8211;printOnly</p>
<dd>Display information only; do not send</p>
<dt>-a, &#8211;autoSend</p>
<dd>Don&#8217;t prompt to send; just send</p>
<dt>-r, &#8211;retry</p>
<dd>Continue to send until success</p>
<dt>-c, &#8211;checkin</p>
<dd>Automated check-in, suitable for cron-jobs</p>
<dt>-S, &#8211;scanOnly</p>
<dd>Only scan this machine for known hardware errata; do not send profile</p>
<dt>&#8211;submitOnly</p>
<dd>Do not scan this machine for known hardware errata; only submit profile</p>
<dt>-b, &#8211;bodhi</p>
<dd>Submit this profile to Bodhi as well, for Fedora Developmnent</p>
<dt>-n, &#8211;newPublicUUID</p>
<dd>Request a new public UUID</p>
<dt>-s <i>SMOON_URL</i>, &#8211;server=<i>SMOON_URL</i></p>
<dd>Specify the URL of the server</p>
<dt>-u <i>USERAGENT</i>, &#8211;useragent=<i>USERAGENT</i>, &#8211;user_agent=<i>USERAGENT</i></p>
<dd>Specify HTTP user agent (default &quot;smolt/0.97&quot;)</p>
<dt>-t <i>TIMEOUT</i>, &#8211;timeout=<i>TIMEOUT</i></p>
<dd>Specify HTTP timeout in seconds (default 60.0 seconds)</p>
<dt>&#8211;uuidFile=<i>UUIDFILE</i></p>
<dd>Specify which UUID to use; useful for debugging and testing</p>
<dt>&#8211;username=<i>USERNAME</i></p>
<dd>Fedora Account System registration username</p>
<dt>&#8211;password=<i>PASSWORD</i></p>
<dd>Fedora Account System registration password (will prompt if not specified)</p>
<dt>-d, &#8211;debug</p>
<dd>Enable debug information</p>
<dt>&#8211;version</p>
<dd>Show program&#8217;s version number and exit</p>
<dt>-h, &#8211;help</p>
<dd>Show this help message and exit</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-smoltdeleteprofile/">smoltDeleteProfile</a></code>(1), <code><a href="/docs/linux/man/1-smoltgui/">smoltGui</a></code>(1).</p>
<h2>Author</h2>
<p><code>smoltSendProfile</code> was written by Mike McGrath &lt;mmcgrath [at] redhat.com&gt; and others. </p>
<p> This manual page was written by Chris Lamb &lt;chris [at] chris-lamb.co.uk&gt;, for the Debian project (but may be used by others).</p>
