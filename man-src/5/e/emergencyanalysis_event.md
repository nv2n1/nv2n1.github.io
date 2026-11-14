---
title: "emergencyanalysis_event(5)"
name: "emergencyanalysis_event"
section: "5"
letter: "e"
url: "/docs/linux/man/5-emergencyanalysis_event/"
---

emergencyanalysis_event.conf - configuration file for libreport.

<h2>Description</h2>

This configuration file defines events for the emergency analysis. These events are supposed to be used when the standard reporting process fails. 

 By default the file contains definition for <i>report_EmergencyAnalysis</i> event applicable for all problem types.

<h3>report_EmergencyAnalysis event configuration file</h3>

The configuration for report_EmergencyAnalysis event is read from /etc/libreport/events/report_EmergencyAnalysis.conf file if exists. 

 The configuration file contains values for options defined in /usr/share/libreport/events/report_EmergencyAnalysis.xml 

 Configuration file lines should have <i>PARAM = VALUE</i> format. The parameters are: 

 <i>Upload_URL</i>
<dl><dd>Configured upload URL</dl>
 

 <i>http_proxy</i>
<dl><dd>the proxy server to use for HTTP</dl>
 

 <i>HTTPS_PROXY</i>
<dl><dd>the proxy server to use for HTTPS</dl>
 

 <i>FTP_PROXY</i>
<dl><dd>the proxy server to use for FTP</dl>

<h2>Example</h2>

The following example shows a possible configuration of <i>report_EmergencyAnalysis</i> event. In this particular case the event execution uploads an archive with all problem data to configured URL. 

 EVENT=report_EmergencyAnalysis reporter-upload

<h2>See Also</h2>

<a HREF="/docs/linux/man/5-report_event-conf/">report_event.conf</a>(5), <a HREF="/docs/linux/man/1-reporter-upload/">reporter-upload</a>(1)

<h2>Author</h2>

<dl><dd>&bull; ABRT team</dl>
