---
title: "getcert-refresh(1)"
name: "getcert-refresh"
section: "1"
letter: "g"
url: "/docs/linux/man/1-getcert-refresh/"
description: "getcert"
---

<h2 class="name">NAME</h2>
<p> getcert</p>
<h2>SYNOPSIS</h2>
<p> getcert refresh [options] </p>
<h2>DESCRIPTION</h2>
<p> Forces <i>certmonger</i> to immediately check on the status of an enrollment request for which it was either unable to contact a CA or for which it is waiting for the CA. </p>
<h2>SPECIFYING REQUESTS BY NICKNAME</h2>
<dl>
<dt><code>-i</code> NAME</p>
<dd> Check on the status of the signing request which has this nickname. If this option is not specified, and a tracking entry which matches the certificate storage options which are specified already exists, that entry will be used. If not specified, the location of the certificate should be specified with either a combination of the <code>-d</code> and <code>-n</code> options, or with the <code>-f</code> option. </p>
</dl>
<h2>SPECIFYING REQUESTS BY CERTIFICATE LOCATION</h2>
<dl>
<dt><code>-d</code> DIR</p>
<dd> The certificate is in the NSS database in the specified directory.</p>
<dt><code>-n</code> NAME</p>
<dd> The certificate in the NSS database named with <code>-d</code> has the specified nickname. Only valid with <code>-d</code>.</p>
<dt><code>-t</code> TOKEN</p>
<dd> If the NSS database has more than one token available, the certificate is stored in this token. This argument only rarely needs to be specified. Only valid with <code>-d</code>.</p>
<dt><code>-f</code> FILE</p>
<dd> The certificate is stored in the named file. </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Refresh information about all requests for which the service will need to attempt to contact the CA again. </p>
</dl>
<h2>BUGS</h2>
<p> Please file tickets for any that you find at <a rel="nofollow" href="https://fedorahosted.org/certmonger/">https://fedorahosted.org/certmonger/</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-certmonger/">certmonger</a></code>(8) <code><a href="/docs/linux/man/1-getcert/">getcert</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-ca/">getcert-add-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-scep-ca/">getcert-add-scep-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list-cas/">getcert-list-cas</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list/">getcert-list</a></code>(1) <code><a href="/docs/linux/man/1-getcert-modify-ca/">getcert-modify-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-refresh-ca/">getcert-refresh-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-remove-ca/">getcert-remove-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-request/">getcert-request</a></code>(1) <code><a href="/docs/linux/man/1-getcert-resubmit/">getcert-resubmit</a></code>(1) <code><a href="/docs/linux/man/1-getcert-start-tracking/">getcert-start-tracking</a></code>(1) <code><a href="/docs/linux/man/1-getcert-status/">getcert-status</a></code>(1) <code><a href="/docs/linux/man/1-getcert-stop-tracking/">getcert-stop-tracking</a></code>(1) <code><a href="/docs/linux/man/8-certmonger-certmaster-submit/">certmonger-certmaster-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-dogtag-ipa-renew-agent-submit/">certmonger-dogtag-ipa-renew-agent-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-dogtag-submit/">certmonger-dogtag-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-ipa-submit/">certmonger-ipa-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-local-submit/">certmonger-local-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-scep-submit/">certmonger-scep-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger_selinux/">certmonger_selinux</a></code>(8) </p>
<h2>Index</h2>
