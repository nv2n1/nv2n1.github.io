---
title: "abrt-conf(5)"
name: "abrt-conf"
section: "5"
letter: "a"
url: "/docs/linux/man/5-abrt-conf/"
---

abrt.conf - Configuration file for abrt.

<h2>Description</h2>

<i>abrt</i> is a daemon that watches for application crashes. When a crash occurs, it collects the problem data and takes action according to its configuration. This document describes abrt's configuration file. 

 The configuration file consists of items in the format &quot;Option = Value&quot;. A description of each item follows: 

 DumpLocation = <i>directory</i>
<dl><dd>The directory where should <i>abrt</i> store coredumps and all files which are needed for reporting. The default is /var/tmp/abrt.</dl>
 

 MaxCrashReportsSize = <i>number</i>
<dl><dd>The maximum disk space (specified in megabytes) that <i>abrt</i> will use for all the crash dumps. Specify a value here to ensure that the crash dumps will not fill all available storage space. The default is 1000.</dl>
 

 WatchCrashdumpArchiveDir = <i>directory</i>
<dl><dd>The daemon will watch this directory and call <i>abrt-handle-upload</i> on files which appear there. This is used to auto-unpack crashdump tarballs uploaded via ftp, scp, etc. The directory must exist and be writable for <i>abrt</i>. There is no default.</dl>
 

 DeleteUploaded = <i>yes/no</i>
<dl><dd>The daemon will delete an uploaded crashdump archive after an atempt to unpack it. An archive will be delete whether unpacking finishes successfully or not. The default value is <i>no</i>.</dl>
 

 DebugLevel = <i>0-100</i>: Allows ABRT tools to detect problems in ABRT itself. By increasing the value you can force ABRT to detect, process and report problems in ABRT. You have to bare in mind that ABRT might fall into an infinite loop when handling problems caused by itself. The default is 0 (non debug mode).

<h2>See Also</h2>

<a HREF="/docs/linux/man/8-abrtd/">abrtd</a>(8) <a HREF="/docs/linux/man/5-abrt-action-save-package-data-conf/">abrt-action-save-package-data.conf</a>(5) <a HREF="/docs/linux/man/1-abrt-handle-upload/">abrt-handle-upload</a>(1)

<h2>Authors</h2>

<dl><dd>&bull; ABRT team</dl>
