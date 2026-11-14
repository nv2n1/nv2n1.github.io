---
title: "abrt-reportuploader(7)"
name: "abrt-reportuploader"
section: "7"
letter: "a"
url: "/docs/linux/man/7-abrt-reportuploader/"
---

ReportUploader plugin for <a HREF="/docs/linux/man/8-abrt/">abrt</a>(8)

<h2>Description</h2>

<i>abrt</i> is a daemon which watches for application crashes. When a crash occurs, it collects the crash data and performs some actions according to the configuration. This manual page describes the <i>ReportUploader</i> plugin for <i>abrt</i>. This plugin will send a report to an anonymous FTP site. It's intended for use in cases where a ticketing system is associated with the FTP site, but the ticketing system has no way to automatically create new tickets, or add to existing tickets. Customer Name is put in config file. Ticket name (or number) is also put in config file. If no ticket name is configured, assume ticketing system should create a new ticket. This information is added to the report, the report is copied into a compressed, optionally encrypted, tarball. Then the tarball is FTP'd to the upload site. Then a status string is displayed to the user showing the name of the file on the FTP site, it's MD5SUM, and it's encryption key. This information can be pasted into a ticket in the ticketing system.

<h2>Invocation</h2>

The plugin is invoked in the <i>abrt.conf</i> configuration file. No parameters are necessary.

<h2>Configuration</h2>

The <i>ReportUploader.conf</i> configuration file contains entries in a format &quot;Option = Value&quot;. The options are:

<h3>Customer</h3>

This is the customer's name or other customer identifier.

<h3>Ticket</h3>

This is the ticket name or number.

<h3>Encrypt</h3>

&quot;yes&quot; for encrypt upload, anything else for not.

<h3>Upload</h3>

&quot;yes&quot; for for upload to FTP site, anything else for copy to local /tmp.

<h3>Url</h3>

URL of upload site (ie. <a HREF="ftp://support.com/upload">ftp://support.com/upload</a>).

<h2>Examples</h2>

This is a snippet from the <i>abrt.conf</i> configuration file. Log all the C/C++ application crashes: [AnalyzerActionsAndReporters] 
 CCpp = RHUpload

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/8-abrt/">abrt</a></i>(8), <i><a HREF="/docs/linux/man/5-abrt-conf/">abrt.conf</a></i>(5), <i><a HREF="/docs/linux/man/7-abrt-plugins/">abrt-plugins</a></i>(7)

<h2>Author</h2>

Plugin and man page by Gavin Romig-Koch &lt;gavin [at] redhat.com&gt;.
