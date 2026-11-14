---
title: "ipa-upgradeconfig(8)"
name: "ipa-upgradeconfig"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipa-upgradeconfig/"
description: "ipa-upgradeconfig – Upgrade the IPA Apache configuration"
---

<p>ipa-upgradeconfig &#8211; Upgrade the IPA Apache configuration</p>
<h2>Synopsis</h2>
<p>ipa-upgradeconfig</p>
<h2>Description</h2>
<p>A tool to update the IPA Apache configuration during an upgrade. </p>
<p> It examines the VERSION value in the head of <i>/etc/httpd/conf.d/ipa.conf</i> and <i>/etc/httpd/conf.d/ipa-rewrite.conf</i> and compares this with the templates. If an update is needed then new files are written. </p>
<p> It also will convert a CA configured to be accessible via ports 9443, 9444, 9445 and 9446 to be proxied by the IPA web server on ports 80 and 443. </p>
<p> This is not intended to be run by an end-user. It is executed when the IPA rpms are upgraded. This must be run as the root user.</p>
<h2>Options</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd>Enable debug logging when more verbose output is needed</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Output only errors</dl>
<h2>Exit Status</h2>
<p>0 if the update was successful or there was nothing to do </p>
<p> 1 if an error occurred</p>
