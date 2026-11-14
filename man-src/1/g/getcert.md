---
title: "getcert(1)"
name: "getcert"
section: "1"
letter: "g"
url: "/docs/linux/man/1-getcert/"
description: "getcert"
---

<h2 class="name">NAME</h2>
<p> getcert</p>
<h2>SYNOPSIS</h2>
<p>&nbsp;<wbr>getcert request&nbsp;<wbr>[options]<br />
&nbsp;<wbr>getcert resubmit&nbsp;<wbr>[options]<br />
&nbsp;<wbr>getcert start-tracking&nbsp;<wbr>[options]<br />
&nbsp;<wbr>getcert status&nbsp;<wbr>[options]<br />
&nbsp;<wbr>getcert stop-tracking&nbsp;<wbr>[options]<br />
&nbsp;<wbr>getcert list&nbsp;<wbr>[options]<br />
&nbsp;<wbr>getcert list-cas&nbsp;<wbr>[options]<br />
&nbsp;<wbr>getcert refresh-cas&nbsp;<wbr>[options] </p>
<h2>DESCRIPTION</h2>
<p> The <i>getcert</i> tool issues requests to a org.fedorahosted.certmonger service on behalf of the invoking user. It can ask the service to begin enrollment, optionally generating a key pair to use, it can ask the service to begin monitoring a certificate in a specified location for expiration, and optionally to refresh it when expiration nears, it can list the set of certificates that the service is already monitoring, or it can list the set of CAs that the service is capable of using. </p>
<p> If no command is given as the first command-line argument, <i>getcert</i> will print short usage information for each of its functions. </p>
<p> If <i>getcert</i> is invoked by a user with UID 0, and there is no system bus available, <i>getcert</i> will attempt to launch a temporary copy of the <i>certmonger</i> daemon to handle its requests. </p>
<h2>COMMON ARGUMENTS</h2>
<p> If <i>CERTMONGER_PVT_ADDRESS</i> is set in the environment, <i>getcert</i> contacts the service directly at the specified location. All commands can take either the <code>-s</code> or <code>-S</code> arguments, which instruct <i>getcert</i> to contact the org.fedorahosted.certmonger service on the session or system bus, if no value is set. By default, <i>getcert</i> consults the org.fedorahosted.certmonger service attached to the system bus. </p>
<h2>BUGS</h2>
<p> Please file tickets for any that you find at <a rel="nofollow" href="https://fedorahosted.org/certmonger/">https://fedorahosted.org/certmonger/</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-certmonger/">certmonger</a></code>(8) <code><a href="/docs/linux/man/1-getcert-add-ca/">getcert-add-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-scep-ca/">getcert-add-scep-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list-cas/">getcert-list-cas</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list/">getcert-list</a></code>(1) <code><a href="/docs/linux/man/1-getcert-modify-ca/">getcert-modify-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-refresh-ca/">getcert-refresh-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-refresh/">getcert-refresh</a></code>(1) <code><a href="/docs/linux/man/1-getcert-remove-ca/">getcert-remove-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-request/">getcert-request</a></code>(1) <code><a href="/docs/linux/man/1-getcert-resubmit/">getcert-resubmit</a></code>(1) <code><a href="/docs/linux/man/1-getcert-start-tracking/">getcert-start-tracking</a></code>(1) <code><a href="/docs/linux/man/1-getcert-status/">getcert-status</a></code>(1) <code><a href="/docs/linux/man/1-getcert-stop-tracking/">getcert-stop-tracking</a></code>(1) <code><a href="/docs/linux/man/8-certmonger-certmaster-submit/">certmonger-certmaster-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-dogtag-ipa-renew-agent-submit/">certmonger-dogtag-ipa-renew-agent-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-dogtag-submit/">certmonger-dogtag-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-ipa-submit/">certmonger-ipa-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-local-submit/">certmonger-local-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-scep-submit/">certmonger-scep-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger_selinux/">certmonger_selinux</a></code>(8) </p>
<h2>Index</h2>
