---
title: "report_centosbugtracker-conf(5)"
name: "report_centosbugtracker-conf"
section: "5"
letter: "r"
url: "/docs/linux/man/5-report_centosbugtracker-conf/"
description: "report_CentOSBugTracker.conf – libreport’s configuration file for ‘report_CentOSBugTracker’ events."
---

<p>report_CentOSBugTracker.conf &#8211; libreport&#8217;s configuration file for &#8216;report_CentOSBugTracker&#8217; events.</p>
<h2>Description</h2>
<p>This configuration file contains values for options defined in /usr/share/libreport/events/report_CentOSBugTracker.xml </p>
<p> Configuration file lines should have <i>PARAM = VALUE</i> format. The parameters are: </p>
<p> <i>Mantisbt_Login</i></p>
<dl>
<dd>Login to MantisBT account.</dl>
<p> <i>Mantisbt_Password</i></p>
<dl>
<dd>Password to MantisBT account.</dl>
<p> <i>Mantisbt_MantisbtURL</i></p>
<dl>
<dd>MantisBT HTTP(S) address. (default: m[blue]<code><a rel="nofollow" href="https://bugs.centos.org">https://bugs.centos.org</a></code>m[])</dl>
<p> <i>Mantisbt_SSLVerify</i></p>
<dl>
<dd>Use yes/true/on/1 to verify server&#8217;s SSL certificate. (default: yes)</dl>
<p> <i>Mantisbt_Project</i></p>
<dl>
<dd>Project issue field value. Useful if you needed different project than specified in /etc/os-release</dl>
<p> <i>Mantisbt_ProjectVersion</i></p>
<dl>
<dd>Version issue field value. Useful if you needed different project version than specified in /etc/os-release</dl>
<p> <i>http_proxy</i></p>
<dl>
<dd>the proxy server to use for HTTP</dl>
<p> <i>HTTPS_PROXY</i></p>
<dl>
<dd>the proxy server to use for HTTPS</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-report_event-conf/">report_event.conf</a>(5), <a href="/docs/linux/man/1-reporter-mantisbt/">reporter-mantisbt</a>(1)</p>
<h2>Author</h2>
<dl>
<dd>&bull; ABRT team</dl>
