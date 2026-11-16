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
<dt></dt></dl>
<h2>Options</h2>
<dd>
</dd><dl COMPACT>
<dt>-p, &#8211;printOnly</dt>
<dd>Display information only; do not send</dd>
<dt>-a, &#8211;autoSend</dt>
<dd>Don&#8217;t prompt to send; just send</dd>
<dt>-r, &#8211;retry</dt>
<dd>Continue to send until success</dd>
<dt>-c, &#8211;checkin</dt>
<dd>Automated check-in, suitable for cron-jobs</dd>
<dt>-S, &#8211;scanOnly</dt>
<dd>Only scan this machine for known hardware errata; do not send profile</dd>
<dt>&#8211;submitOnly</dt>
<dd>Do not scan this machine for known hardware errata; only submit profile</dd>
<dt>-b, &#8211;bodhi</dt>
<dd>Submit this profile to Bodhi as well, for Fedora Developmnent</dd>
<dt>-n, &#8211;newPublicUUID</dt>
<dd>Request a new public UUID</dd>
<dt>-s <i>SMOON_URL</i>, &#8211;server=<i>SMOON_URL</i></dt>
<dd>Specify the URL of the server</dd>
<dt>-u <i>USERAGENT</i>, &#8211;useragent=<i>USERAGENT</i>, &#8211;user_agent=<i>USERAGENT</i></dt>
<dd>Specify HTTP user agent (default &quot;smolt/0.97&quot;)</dd>
<dt>-t <i>TIMEOUT</i>, &#8211;timeout=<i>TIMEOUT</i></dt>
<dd>Specify HTTP timeout in seconds (default 60.0 seconds)</dd>
<dt>&#8211;uuidFile=<i>UUIDFILE</i></dt>
<dd>Specify which UUID to use; useful for debugging and testing</dd>
<dt>&#8211;username=<i>USERNAME</i></dt>
<dd>Fedora Account System registration username</dd>
<dt>&#8211;password=<i>PASSWORD</i></dt>
<dd>Fedora Account System registration password (will prompt if not specified)</dd>
<dt>-d, &#8211;debug</dt>
<dd>Enable debug information</dd>
<dt>&#8211;version</dt>
<dd>Show program&#8217;s version number and exit</dd>
<dt>-h, &#8211;help</dt>
<dd>Show this help message and exit</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-smoltdeleteprofile/">smoltDeleteProfile</a></code>(1), <code><a href="/docs/linux/man/1-smoltgui/">smoltGui</a></code>(1).</p>
<h2>Author</h2>
<p><code>smoltSendProfile</code> was written by Mike McGrath &lt;mmcgrath [at] redhat.com&gt; and others. </p>
<p> This manual page was written by Chris Lamb &lt;chris [at] chris-lamb.co.uk&gt;, for the Debian project (but may be used by others).</p>
