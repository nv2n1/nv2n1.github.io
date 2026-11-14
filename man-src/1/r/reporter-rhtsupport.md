---
title: "reporter-rhtsupport(1)"
name: "reporter-rhtsupport"
section: "1"
letter: "r"
url: "/docs/linux/man/1-reporter-rhtsupport/"
description: "reporter-rhtsupport – Reports problem to RHTSupport."
---

<h2 class="name">NAME</h2>
<p> reporter-rhtsupport &#8211; Reports problem to RHTSupport. </p>
<h2>SYNOPSIS</h2>
<p> <i>reporter-rhtsupport</i> [-v] [-c CONFFILE] [-F FMTFILE] [-u -C UR_CONFFILE] -d DIR </p>
<p> Or: </p>
<p> <i>reporter-rhtsupport</i> [-v] [-c CONFFILE] [-d DIR] -t[ID] FILE&#8230;</p>
<h2>DESCRIPTION</h2>
<p> The tool reads problem directory DIR. Then it logs in to RHTSupport and creates a new case. </p>
<p> The tool can be configured to submit an uReport to RHTSupport together with creating a new case. </p>
<p> The URL to new case is printed to stdout and recorded in <i>reported_to</i> element in DIR. </p>
<p> If not specified, CONFFILE defaults to /etc/libreport/plugins/rhtsupport.conf. </p>
<p> Option -t uploads FILEs to the already created case on RHTSupport site. The case ID is retrieved from directory specified by -d DIR. If problem data in DIR was never reported to RHTSupport, upload will fail. </p>
<p> Option -tCASE uploads FILEs to the case CASE on RHTSupport site. -d DIR is ignored. </p>
<p> Option -u uploads uReport along with creating a new case. uReport configuration is loaded from UR_CONFFILE which defaults to /etc/libreport/plugins/ureport.conf.</p>
<h3>Configuration file</h3>
<p> Configuration file lines should have <i>PARAM = VALUE</i> format. The parameters are: </p>
<p> <i>Login</i></p>
<dl>
<dt>
<dd> Login to RHTSupport account.</dl>
<p> <i>Password</i></p>
<dl>
<dt>
<dd> Password to RHTSupport account.</dl>
<p> <i>URL</i></p>
<dl>
<dt>
<dd> HTTP(S) address. (default: m[blue]<code><a rel="nofollow" href="https://api.access.redhat.com/rs">https://api.access.redhat.com/rs</a></code>m[])</dl>
<p> <i>SSLVerify</i></p>
<dl>
<dt>
<dd> Use yes/true/on/1 to verify server&#8217;s SSL certificate. (default: yes)</dl>
<p> <i>SubmitUReport</i></p>
<dl>
<dt>
<dd> Use yes/true/on/1 to enable submitting uReport together wit creating a new case. (default: no)</dl>
<p> Parameters can be overridden via $RHTSupport_PARAM environment variables.</p>
<h3>Integration with ABRT events</h3>
<p> <i>reporter-rhtsupport</i> can be used as an ABRT reporter. Example fragment for /etc/libreport/report_event.conf: </p>
<dl>
<dt>
<dd>
<pre>
# Report Python crashes
EVENT=report_RHTSupport analyzer=Python
      reporter-rhtsupport -d . -c /etc/libreport/plugins/rhtsupport.conf
</pre>
</dl>
<h2>OPTIONS</h2>
<p> -d DIR</p>
<dl>
<dt>
<dd> Path to problem directory.</dl>
<p> -c CONFFILE</p>
<dl>
<dt>
<dd> Path to configuration file.</dl>
<p> -t[ID]</p>
<dl>
<dt>
<dd> Upload FILEs to the already created case on RHTSupport site.</dl>
<p> -u</p>
<dl>
<dt>
<dd> Submit uReport together with creating a new case.</dl>
<p> -C UR_CONFFILE</p>
<dl>
<dt>
<dd> Configuration file for submitting uReports.</dl>
<p> -F CONF_FORMAT_FILE</p>
<dl>
<dt>
<dd> Formatting file for a new case.</dl>
<h2>FILES</h2>
<p> /usr/share/libreport/conf.d/plugins/rhtsupport.conf</p>
<dl>
<dt>
<dd> Readonly default configuration files.</dl>
<p> /etc/libreport/plugins/rhtsupport.conf</p>
<dl>
<dt>
<dd> Configuration file.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-abrt_event-conf/">abrt_event.conf</a>(5), <a href="/docs/linux/man/5-rhtsupport-conf/">rhtsupport.conf</a>(5), <a href="/docs/linux/man/5-rhtsupport_event-conf/">rhtsupport_event.conf</a>(5) </p>
<h2>Index</h2>
