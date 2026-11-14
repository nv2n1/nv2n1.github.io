---
title: "mailx_event-conf(5)"
name: "mailx_event-conf"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mailx_event-conf/"
---

mailx_event.conf - configuration file for libreport.

<h2>Description</h2>

This configuration file provides definitions for events which uses <i>reporter-mailx</i>. 

 By default the file contains definition for <i>report_Mailx</i>, <i>notify</i> and <i>notify-dup</i> events for all problem types.

<h3>report_Mailx event configuration file</h3>

The configuration for report_Mailx event is read from /etc/libreport/events/report_Mailx.conf file if exists. 

 The configuration file contains values for options defined in /usr/share/libreport/events/report_Mailx.xml 

 Configuration file lines should have <i>PARAM = VALUE</i> format. The parameters are: 

 <i>Mailx_Subject</i>
<dl><dd>Message subject</dl>
 

 <i>Mailx_EmailFrom</i>
<dl><dd>Sender's email</dl>
 

 <i>Mailx_EmailTo</i>
<dl><dd>Recipient's email</dl>
 

 <i>Mailx_SendBinaryData</i>
<dl><dd>Send binary files like coredump</dl>

<h2>See Also</h2>

<a HREF="/docs/linux/man/5-report_event-conf/">report_event.conf</a>(5), <a HREF="/docs/linux/man/1-reporter-mailx/">reporter-mailx</a>(1)

<h2>Author</h2>

<dl><dd>&bull; ABRT team</dl>
