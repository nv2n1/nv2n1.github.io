---
title: "certmaster-getcert(1)"
name: "certmaster-getcert"
section: "1"
letter: "c"
url: "/docs/linux/man/1-certmaster-getcert/"
description: "certmaster-getcert"
---

<h2 class="name">NAME</h2>
<p> certmaster-getcert</p>
<h2>SYNOPSIS</h2>
<p>&nbsp;<wbr>certmaster-getcert request&nbsp;<wbr>[options]<br />
&nbsp;<wbr>certmaster-getcert resubmit&nbsp;<wbr>[options]<br />
&nbsp;<wbr>certmaster-getcert start-tracking&nbsp;<wbr>[options]<br />
&nbsp;<wbr>certmaster-getcert status&nbsp;<wbr>[options]<br />
&nbsp;<wbr>certmaster-getcert stop-tracking&nbsp;<wbr>[options]<br />
&nbsp;<wbr>certmaster-getcert list&nbsp;<wbr>[options]<br />
&nbsp;<wbr>certmaster-getcert list-cas&nbsp;<wbr>[options]<br />
&nbsp;<wbr>certmaster-getcert refresh-cas&nbsp;<wbr>[options] </p>
<h2>DESCRIPTION</h2>
<p> The <i>certmaster-getcert</i> tool issues requests to a org.fedorahosted.certmonger service on behalf of the invoking user. It can ask the service to begin enrollment, optionally generating a key pair to use, it can ask the service to begin monitoring a certificate in a specified location for expiration, and optionally to refresh it when expiration nears, it can list the set of certificates that the service is already monitoring, or it can list the set of CAs that the service is capable of using. </p>
<p> If no command is given as the first command-line argument, <i>certmaster-getcert</i> will print short usage information for each of its functions. </p>
<p> The <i>certmaster-getcert</i> tool behaves identically to the generic <i>getcert</i> tool when it is used with the <code>-c </code><i>certmaster</i> option. </p>
<p> There is no standard authenticated method for obtaining the root certificate from certmaster CAs, so <code>certmonger</code> does not support retrieving trust information from them. While the <code>-F</code> and <code>-a</code> options will still be recognized, they will effectively be ignored. </p>
<h2>BUGS</h2>
<p> Please file tickets for any that you find at <a rel="nofollow" href="https://fedorahosted.org/certmonger/">https://fedorahosted.org/certmonger/</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-certmonger/">certmonger</a></code>(8) <code><a href="/docs/linux/man/1-getcert/">getcert</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-ca/">getcert-add-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-scep-ca/">getcert-add-scep-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list-cas/">getcert-list-cas</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list/">getcert-list</a></code>(1) <code><a href="/docs/linux/man/1-getcert-modify-ca/">getcert-modify-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-refresh-ca/">getcert-refresh-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-refresh/">getcert-refresh</a></code>(1) <code><a href="/docs/linux/man/1-getcert-remove-ca/">getcert-remove-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-request/">getcert-request</a></code>(1) <code><a href="/docs/linux/man/1-getcert-resubmit/">getcert-resubmit</a></code>(1) <code><a href="/docs/linux/man/1-getcert-start-tracking/">getcert-start-tracking</a></code>(1) <code><a href="/docs/linux/man/1-getcert-status/">getcert-status</a></code>(1) <code><a href="/docs/linux/man/1-getcert-stop-tracking/">getcert-stop-tracking</a></code>(1) <code><a href="/docs/linux/man/8-certmonger-certmaster-submit/">certmonger-certmaster-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-dogtag-ipa-renew-agent-submit/">certmonger-dogtag-ipa-renew-agent-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-dogtag-submit/">certmonger-dogtag-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-ipa-submit/">certmonger-ipa-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-local-submit/">certmonger-local-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-scep-submit/">certmonger-scep-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger_selinux/">certmonger_selinux</a></code>(8) </p>
<h2>Index</h2>
