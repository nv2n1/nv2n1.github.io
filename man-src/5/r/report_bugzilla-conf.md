---
title: "report_bugzilla-conf(5)"
name: "report_bugzilla-conf"
section: "5"
letter: "r"
url: "/docs/linux/man/5-report_bugzilla-conf/"
description: "report_Bugzilla.conf – libreport’s configuration file for ‘report_Bugzilla’ events."
---

<p>report_Bugzilla.conf &#8211; libreport&#8217;s configuration file for &#8216;report_Bugzilla&#8217; events.</p>
<h2>Description</h2>
<p>This configuration file contains values for options defined in /usr/share/libreport/events/report_Bugzilla.xml </p>
<p> Configuration file lines should have <i>PARAM = VALUE</i> format. The parameters are: </p>
<p> <i>Bugzilla_Login</i></p>
<dl>
<dd>Login to Bugzilla account.</dl>
<p> <i>Bugzilla_Password</i></p>
<dl>
<dd>Password to Bugzilla account.</dl>
<p> <i>Bugzilla_BugzillaURL</i></p>
<dl>
<dd>Bugzilla HTTP(S) address. (default: m[blue]<code><a rel="nofollow" href="https://bugzilla.redhat.com">https://bugzilla.redhat.com</a></code>m[])</dl>
<p> <i>Bugzilla_SSLVerify</i></p>
<dl>
<dd>Use yes/true/on/1 to verify server&#8217;s SSL certificate. (default: yes)</dl>
<p> <i>Bugzilla_Product</i></p>
<dl>
<dd>Product bug field value. Useful if you needed different product than specified in /etc/os-release</dl>
<p> <i>Bugzilla_ProductVersion</i></p>
<dl>
<dd>Version bug field value. Useful if you needed different product version than specified in /etc/os-release</dl>
<p> <i>http_proxy</i></p>
<dl>
<dd>the proxy server to use for HTTP</dl>
<p> <i>HTTPS_PROXY</i></p>
<dl>
<dd>the proxy server to use for HTTPS</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-report_event-conf/">report_event.conf</a>(5), <a href="/docs/linux/man/1-reporter-bugzilla/">reporter-bugzilla</a>(1), <a href="/docs/linux/man/5-bugzilla_event-conf/">bugzilla_event.conf</a>(5)</p>
<h2>Author</h2>
<dl>
<dd>&bull; ABRT team</dl>
