---
title: "rhtsupport_event-conf(5)"
name: "rhtsupport_event-conf"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rhtsupport_event-conf/"
---

rhtsupport_event.conf - configuration file for libreport.

<h2>Description</h2>

This configuration file provides definitions for events which use <i>reporter-rhtsupport</i>. 

 By default the file contains definition for single <i>report_RHTSupport</i> event applicable for all problem types.

<h3>report_RHTSupport event configuration file</h3>

The configuration for report_RHTSupport event is read from /etc/libreport/events/report_RHTSupport.conf file if exists. 

 The configuration file contains values for options defined in /usr/share/libreport/events/report_RHTSupport.xml 

 Configuration file lines should have <i>PARAM = VALUE</i> format. The parameters are: 

 <i>RHTSupport_URL</i>
<dl><dd>Address of the Red Hat support portal</dl>
 

 <i>RHTSupport_Login</i>
<dl><dd>Red Hat customer user name</dl>
 

 <i>RHTSupport_Password</i>
<dl><dd>Red Hat customer user password</dl>
 

 <i>RHTSupport_SSLVerify</i>
<dl><dd>Use yes/true/on/1 to verify server's SSL certificate. (default: yes)</dl>

<h2>See Also</h2>

<a HREF="/docs/linux/man/5-report_event-conf/">report_event.conf</a>(5), <a HREF="/docs/linux/man/1-reporter-rhtsupport/">reporter-rhtsupport</a>(1)

<h2>Author</h2>

<dl><dd>&bull; ABRT team</dl>
