---
title: "getcert-stop-tracking(1)"
name: "getcert-stop-tracking"
section: "1"
letter: "g"
url: "/docs/linux/man/1-getcert-stop-tracking/"
description: "getcert"
---

<h2 class="name">NAME</h2>
<p> getcert</p>
<h2>SYNOPSIS</h2>
<p> getcert stop-tracking [options] </p>
<h2>DESCRIPTION</h2>
<p> Tells <i>certmonger</i> to stop monitoring or attempting to obtain or refresh a certificate. </p>
<h2>TRACKING OPTIONS</h2>
<dl>
<dt><code>-i</code> NAME</p>
<dd> The certificate was tracked using the request with the specified nickname. If this option is not specified, some combination of <code>-d</code> and <code>-n</code> or <code>-f</code> can be used to specify which certificate should henceforth be forgotten. </p>
</dl>
<h2>KEY AND CERTIFICATE STORAGE OPTIONS</h2>
<dl>
<dt><code>-d</code> DIR</p>
<dd> The certificate is the one stored in the specified NSS database.</p>
<dt><code>-n</code> NAME</p>
<dd> The certificate is the one which has this nickname. Only valid with <code>-d</code>.</p>
<dt><code>-t</code> TOKEN</p>
<dd> If the NSS database has more than one token available, the certificate is stored in this token. This argument only rarely needs to be specified. Only valid with <code>-d</code>.</p>
<dt><code>-f</code> FILE</p>
<dd> The certificate is or was to be stored in this file.</p>
<dt><code>-k</code> FILE</p>
<dd> The private key is or was to be stored in this file. Only valid with <code>-f</code>. </p>
</dl>
<h2>OTHER OPTIONS</h2>
<dl>
<dt><code>-v</code></p>
<dd> Be verbose about errors. Normally, the details of an error received from the daemon will be suppressed if the client can make a diagnostic suggestion. </p>
</dl>
<h2>BUGS</h2>
<p> Please file tickets for any that you find at <a rel="nofollow" href="https://fedorahosted.org/certmonger/">https://fedorahosted.org/certmonger/</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-certmonger/">certmonger</a></code>(8) <code><a href="/docs/linux/man/1-getcert/">getcert</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-ca/">getcert-add-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-scep-ca/">getcert-add-scep-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list-cas/">getcert-list-cas</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list/">getcert-list</a></code>(1) <code><a href="/docs/linux/man/1-getcert-modify-ca/">getcert-modify-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-refresh-ca/">getcert-refresh-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-refresh/">getcert-refresh</a></code>(1) <code><a href="/docs/linux/man/1-getcert-remove-ca/">getcert-remove-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-request/">getcert-request</a></code>(1) <code><a href="/docs/linux/man/1-getcert-resubmit/">getcert-resubmit</a></code>(1) <code><a href="/docs/linux/man/1-getcert-start-tracking/">getcert-start-tracking</a></code>(1) <code><a href="/docs/linux/man/1-getcert-status/">getcert-status</a></code>(1) <code><a href="/docs/linux/man/8-certmonger-certmaster-submit/">certmonger-certmaster-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-dogtag-ipa-renew-agent-submit/">certmonger-dogtag-ipa-renew-agent-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-dogtag-submit/">certmonger-dogtag-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-ipa-submit/">certmonger-ipa-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-local-submit/">certmonger-local-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-scep-submit/">certmonger-scep-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger_selinux/">certmonger_selinux</a></code>(8) </p>
<h2>Index</h2>
