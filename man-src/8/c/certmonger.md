---
title: "certmonger(8)"
name: "certmonger"
section: "8"
letter: "c"
url: "/docs/linux/man/8-certmonger/"
description: "certmonger"
---

<p>certmonger</p>
<h2>Synopsis</h2>
<p>certmonger [-s|-S] [-L|-l] [-P SOCKET] [-b TIMEOUT|-B] [-n|-f] [-d LEVEL] [-p FILE] [-F] [-c cmd] [-v] </p>
<h2>Description</h2>
<p>The <i>certmonger</i> daemon monitors certificates for impending expiration, and can optionally refresh soon-to-be-expired certificates with the help of a CA. If told to, it can drive the entire enrollment process from key generation through enrollment and refresh. The daemon provides a control interface via the <i>org.fedorahosted.certmonger</i> service, with which client tools such as <code><a href="/docs/linux/man/1-getcert/">getcert</a></code>(1) interact. </p>
<h2>Options</h2>
<dl>
<dt>-s</p>
<dd>Listen on the session bus rather than the system bus.</p>
<dt>-S</p>
<dd>Listen on the system bus rather than the session bus. This is the default.</p>
<dt>-l</p>
<dd>Also listen on a private socket for connections from clients running under the same UID.</p>
<dt>-L</p>
<dd>Listen only on a private socket for connections from clients running under the same UID, and skip connecting to a bus.</p>
<dt>-P</p>
<dd>Specify a location for the private listening socket. If the location beings with a &#8216;/&#8217; character, it will be prefixed with &#8216;unix:path=&#8217;, otherwise it will be prefixed with &#8216;unix:&#8217;. If this option is not specified, the listening socket, if one is created, will be placed in the abstract namespace.</p>
<dt>-b TIMEOUT</p>
<dd>Behave as a bus-activated service: if there are no certificates to be monitored or obtained, and no requests are received within TIMEOUT seconds, exit. Not compatible with the -c option.</p>
<dt>-B</p>
<dd>Don&#8217;t behave as a bus-activated service. This is the default.</p>
<dt>-n</p>
<dd>Don&#8217;t fork, and log messages to stderr rather than syslog.</p>
<dt>-f</p>
<dd>Do fork, and log messages to syslog rather than stderr. This is the default.</p>
<dt>-d LEVEL</p>
<dd>Set debugging level. Higher values produce more debugging output. Implies -n.</p>
<dt>-p FILE</p>
<dd>Store the daemon&#8217;s process ID in the named file.</p>
<dt>-F</p>
<dd>Force NSS to be initialized in FIPS mode. The default behavior is to heed the setting stored in <i>/proc/sys/crypto/fips_enabled</i>.</p>
<dt>-c cmd</p>
<dd>After the service has initialized, run the specified command, then shut down the service after the command exits. If the -l or -L option was also specified, the command will be run with the <i>CERTMONGER_PVT_ADDRESS</i> environment variable set to the listening socket&#8217;s location. Not compatible with the -b option.</p>
<dt>-v</p>
<dd>Print version information and exit. </p>
</dl>
<h2>Files</h2>
<p>The set of certificates being monitored or signed is tracked using files stored under <i>/var/lib/certmonger/requests</i>, or in a directory named by the <i>CERTMONGER_REQUESTS_DIR</i> environment variable. </p>
<p> The set of known CAs is tracked using files stored under <i>/var/lib/certmonger/cas</i>, or in a directory named by the <i>CERTMONGER_CAS_DIR</i> environment variable. </p>
<p> Temporary files will be stored in &quot;<i>/var/run/certmonger</i>&quot;, or in the directory named by the <i>CERTMONGER_TMPDIR</i> environment variable if that value was not given at compile time.</p>
<h2>Bugs</h2>
<p>Please file tickets for any that you find at <a rel="nofollow" href="https://fedorahosted.org/certmonger/">https://fedorahosted.org/certmonger/</a> </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-getcert/">getcert</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-ca/">getcert-add-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-add-scep-ca/">getcert-add-scep-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list-cas/">getcert-list-cas</a></code>(1) <code><a href="/docs/linux/man/1-getcert-list/">getcert-list</a></code>(1) <code><a href="/docs/linux/man/1-getcert-modify-ca/">getcert-modify-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-refresh-ca/">getcert-refresh-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-remove-ca/">getcert-remove-ca</a></code>(1) <code><a href="/docs/linux/man/1-getcert-request/">getcert-request</a></code>(1) <code><a href="/docs/linux/man/1-getcert-resubmit/">getcert-resubmit</a></code>(1) <code><a href="/docs/linux/man/1-getcert-start-tracking/">getcert-start-tracking</a></code>(1) <code><a href="/docs/linux/man/1-getcert-status/">getcert-status</a></code>(1) <code><a href="/docs/linux/man/1-getcert-stop-tracking/">getcert-stop-tracking</a></code>(1) <code><a href="/docs/linux/man/8-certmonger-certmaster-submit/">certmonger-certmaster-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-dogtag-ipa-renew-agent-submit/">certmonger-dogtag-ipa-renew-agent-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-dogtag-submit/">certmonger-dogtag-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-ipa-submit/">certmonger-ipa-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-local-submit/">certmonger-local-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger-scep-submit/">certmonger-scep-submit</a></code>(8) <code><a href="/docs/linux/man/8-certmonger_selinux/">certmonger_selinux</a></code>(8) </p>
