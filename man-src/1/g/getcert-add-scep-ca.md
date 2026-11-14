---
title: "getcert-add-scep-ca(1)"
name: "getcert-add-scep-ca"
section: "1"
letter: "g"
url: "/docs/linux/man/1-getcert-add-scep-ca/"
description: "getcert"
---

<h2 class="name">NAME</h2>
<p> getcert</p>
<h2>SYNOPSIS</h2>
<p> getcert add-scep-ca [options] </p>
<h2>DESCRIPTION</h2>
<p> Adds a CA configuration to <i>certmonger</i>, which can subsequently be used to enroll certificates. The configuration will use the bundled <i>scep-submit</i> helper. The <i>add-scep-ca</i> command is more or less a wrapper for the <i>add-ca</i> command. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> NAME</p>
<dd> The nickname to give to this CA configuration. This same value can later be passed in to <i>getcert</i>&#8216;s <i>request</i>, <i>resubmit</i>, and <i>start-tracking</i> commands using the <code>-c</code> flag.</p>
<dt><code>-u</code> URL</p>
<dd> The location of the SCEP server&#8217;s enrollment interface. This option must be specified.</p>
<dt><code>-R</code> ca-certificate-file</p>
<dd> The location of a PEM-formatted copy of the SCEP server&#8217;s CA&#8217;s certificate. A discovered value is supplied by the certmonger daemon for use in verifying the signature on data returned by the SCEP server, but it is not used for verifying HTTPS server certificates. This option must be specified if the URL is an <i>https</i> location.</p>
<dt><code>-r</code> ra-certificate-file</p>
<dd> The location of a PEM-formatted copy of the SCEP server&#8217;s RA&#8217;s certificate. A discovered value is normally supplied by the certmonger daemon, but one can be specified for troubleshooting purposes.</p>
<dt><code>-I</code> other-certificates-file</p>
<dd> The location of a file containing other PEM-formatted certificates which may be needed in order to properly verify signed responses sent by the SCEP server back to the client. A discovered set is normally supplied by the certmonger daemon, but can be specified for troubleshooting purposes.</p>
<dt><code>-i</code> identifier</p>
<dd> A CA identifier value which will passed to the server when the <i>scep-submit</i> helper is used to retrieve copies of the server&#8217;s certificates.</p>
<dt><code>-v</code></p>
<dd> Be verbose about errors. Normally, the details of an error received from the daemon will be suppressed if the client can make a diagnostic suggestion. </p>
</dl>
<h2>BUGS</h2>
<p> Please file tickets for any that you find at <a rel="nofollow" href="https://fedorahosted.org/certmonger/">https://fedorahosted.org/certmonger/</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-certmonger/">certmonger</a></code>(8) <code><a href="/docs/linux/man/1-getcert/">getcert</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-ca/">getcert-add-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list-cas/">getcert-list-cas</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list/">getcert-list</a></code>(1) <code><a href="/docs/linux/man/1-getcert-modify-ca/">getcert-modify-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-refresh-ca/">getcert-refresh-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-refresh/">getcert-refresh</a></code>(1) <code><a href="/docs/linux/man/1-getcert-remove-ca/">getcert-remove-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-request/">getcert-request</a></code>(1) <code><a href="/docs/linux/man/1-getcert-resubmit/">getcert-resubmit</a></code>(1) <code><a href="/docs/linux/man/1-getcert-status/">getcert-status</a></code>(1) <code><a href="/docs/linux/man/1-getcert-stop-tracking/">getcert-stop-tracking</a></code>(1) <code><a href="/docs/linux/man/8-certmonger-certmaster-submit/">certmonger-certmaster-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-dogtag-ipa-renew-agent-submit/">certmonger-dogtag-ipa-renew-agent-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-dogtag-submit/">certmonger-dogtag-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-ipa-submit/">certmonger-ipa-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-local-submit/">certmonger-local-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-scep-submit/">certmonger-scep-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger_selinux/">certmonger_selinux</a></code>(8) </p>
<h2>Index</h2>
