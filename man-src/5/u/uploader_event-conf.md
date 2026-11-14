---
title: "uploader_event-conf(5)"
name: "uploader_event-conf"
section: "5"
letter: "u"
url: "/docs/linux/man/5-uploader_event-conf/"
---

uploader_event.conf - configuration file for libreport.

<h2>Description</h2>

This configuration file provides definitions for events which use <i>reporter-uploader</i>. 

 By default the file contains definition for single <i>report_Uploader</i> event applicable for all problem types.

<h3>report_Uploader event configuration file</h3>

The configuration for report_Uploader event is read from /etc/libreport/events/report_Uploader.conf file if exists. 

 The configuration file contains values for options defined in /usr/share/libreport/events/report_Uploader.xml 

 Configuration file lines should have <i>PARAM = VALUE</i> format. The parameters are: 

 <i>Upload_URL</i>
<dl><dd>Configured upload URL</dl>
 

 <i>http_proxy</i>
<dl><dd>the proxy server to use for HTTP</dl>
 

 <i>HTTPS_PROXY</i>
<dl><dd>the proxy server to use for HTTPS</dl>
 

 <i>FTP_PROXY</i>
<dl><dd>the proxy server to use for FTP</dl>

<h2>See Also</h2>

<a HREF="/docs/linux/man/5-report_event-conf/">report_event.conf</a>(5), <a HREF="/docs/linux/man/1-reporter-uploader/">reporter-uploader</a>(1)

<h2>Author</h2>

<dl><dd>&bull; ABRT team</dl>
