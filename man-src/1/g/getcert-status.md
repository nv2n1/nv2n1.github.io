---
title: "getcert-status(1)"
name: "getcert-status"
section: "1"
letter: "g"
url: "/docs/linux/man/1-getcert-status/"
description: "getcert"
---

<h2 class="name">NAME</h2>
<p> getcert</p>
<h2>SYNOPSIS</h2>
<p> getcert status [options] </p>
<h2>DESCRIPTION</h2>
<p> Queries <i>certmonger</i> for a status of a particular certificate request and sets an exit status to reflect that status. </p>
<h2>SELECTION OPTIONS</h2>
<dl>
<dt><code>-d</code> DIR</dt>
<dd> Check that status of a certificate in the named NSS database. Must be specified with the <code>-n</code> option.</dd>
<dt><code>-n</code> NAME</dt>
<dd> Check that status of a certificate in with the specified nickname. Must be specified with the <code>-d</code> option.</dd>
<dt><code>-f</code> FILE</dt>
<dd> Check that status of a certificate stored in the specified PEM file.</dd>
<dt><code>-i</code> NAME</dt>
<dd> Check that status of a certificate with the specified request nickname. </dd>
</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt>0</dt>
<dd> Certificate is issued and valid.</dd>
<dt>1</dt>
<dd> There was an error communicating with the <code><a href="/docs/linux/man/8-certmonger/">certmonger</a></code>(8) daemon, or there is no such certificate known to it.</dd>
<dt>2.</dt>
<dd> Certificate signing request was rejected by the CA.</dd>
<dt>3.</dt>
<dd> CA could not be reached, but attempts to communicate with it will be retried.</dd>
<dt>4.</dt>
<dd> Configuration error.</dd>
<dt>5.</dt>
<dd> Client is working on the request, or waiting for the server. </dd>
</dl>
<h2>BUGS</h2>
<p> Please file tickets for any that you find at <a rel="nofollow" href="https://fedorahosted.org/certmonger/">https://fedorahosted.org/certmonger/</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-certmonger/">certmonger</a></code>(8) <code><a href="/docs/linux/man/1-getcert/">getcert</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-ca/">getcert-add-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-scep-ca/">getcert-add-scep-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list-cas/">getcert-list-cas</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list/">getcert-list</a></code>(1) <code><a href="/docs/linux/man/1-getcert-modify-ca/">getcert-modify-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-refresh-ca/">getcert-refresh-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-refresh/">getcert-refresh</a></code>(1) <code><a href="/docs/linux/man/1-getcert-remove-ca/">getcert-remove-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-request/">getcert-request</a></code>(1) <code><a href="/docs/linux/man/1-getcert-resubmit/">getcert-resubmit</a></code>(1) <code><a href="/docs/linux/man/1-getcert-start-tracking/">getcert-start-tracking</a></code>(1) <code><a href="/docs/linux/man/1-getcert-status/">getcert-status</a></code>(1) <code><a href="/docs/linux/man/1-getcert-stop-tracking/">getcert-stop-tracking</a></code>(1) <code><a href="/docs/linux/man/8-certmonger-certmaster-submit/">certmonger-certmaster-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-dogtag-ipa-renew-agent-submit/">certmonger-dogtag-ipa-renew-agent-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-dogtag-submit/">certmonger-dogtag-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-ipa-submit/">certmonger-ipa-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-local-submit/">certmonger-local-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-scep-submit/">certmonger-scep-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger_selinux/">certmonger_selinux</a></code>(8) </p>
