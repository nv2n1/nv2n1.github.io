---
title: "cups-files(5)"
name: "cups-files"
section: "5"
letter: "c"
url: "/docs/linux/man/5-cups-files/"
---

cups-files.conf - file and directory configuration file for cups

<h2>Description</h2>

The <i>cups-files.conf</i> file configures the files and directories used by the CUPS scheduler, <i><a HREF="/docs/linux/man/8-cupsd/">cupsd</a>(8)</i>. It is normally located in the <i>/etc/cups</i> directory. 

 Each line in the file can be a configuration directive, a blank line, or a comment. Comment lines start with the # character.

<h2>Directives</h2>

The following directives are understood by <i><a HREF="/docs/linux/man/8-cupsd/">cupsd</a>(8)</i>. Consult the on-line help for detailed descriptions:
<dl><dt>AccessLog filename
<dd><dt>AccessLog syslog
<dd><dt>AccessLog journal
<dd>Defines the access log filename.
<dt>ConfigFilePerm mode
<dd>Specifies the permissions for all configuration files that the scheduler writes.
<dt>DataDir path
<dd>Specified the directory where data files can be found.
<dt>DocumentRoot directory
<dd>Specifies the root directory for the internal web server documents.
<dt>ErrorLog filename
<dd><dt>ErrorLog syslog
<dd><dt>ErrorLog journal
<dd>Specifies the error log filename.
<dt>FatalErrors none
<dd><dt>FatalErrors all -kind [... -kind]
<dd><dt>FatalErrors kind [... kind]
<dd>Specifies which errors are fatal, causing the scheduler to exit. &quot;Kind&quot; is &quot;browse&quot;, &quot;config&quot;, &quot;listen&quot;, &quot;log&quot;, or &quot;permissions&quot;.
<dt>FileDevice Yes
<dd><dt>FileDevice No
<dd>Specifies whether the file pseudo-device can be used for new printer queues.
<dt>FontPath directory[:directory:...]
<dd>Specifies the search path for fonts.
<dt>Group group-name-or-number
<dd>Specifies the group name or ID that will be used when executing external programs.
<dt>LogFilePerm mode
<dd>Specifies the permissions for all log files that the scheduler writes.
<dt>PageLog filename
<dd><dt>PageLog syslog
<dd><dt>PageLog journal
<dd>Specifies the page log filename.
<dt>Printcap
<dd><dt>Printcap filename
<dd>Specifies the filename for a printcap file that is updated automatically with a list of available printers (needed for legacy applications); specifying Printcap with no filename disables printcap generation.
<dt>RemoteRoot user-name
<dd>Specifies the username that is associated with unauthenticated root accesses.
<dt>RequestRoot directory
<dd>Specifies the directory to store print jobs and other HTTP request data.
<dt>ServerBin directory
<dd>Specifies the directory where backends, CGIs, daemons, and filters may be found.
<dt>ServerCertificate filename
<dd>Specifies the encryption certificate to use.
<dt>ServerKey filename
<dd>Specifies the encryption key to use.
<dt>ServerRoot directory
<dd>Specifies the directory where the server configuration files can be found.
<dt>SyncOnClose Yes
<dd><dt>SyncOnClose No
<dd>Specifies whether the scheduler calls <i><a HREF="/docs/linux/man/2-fsync/">fsync</a>(2)</i> after writing configuration or state files. The default is Yes.
<dt>SystemGroup group-name [group-name ...]
<dd>Specifies the group(s) to use for System class authentication.
<dt>TempDir directory
<dd>Specifies the directory where temporary files are stored.
<dt>User user-name
<dd>Specifies the user name or ID that is used when running external programs.</dl>

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/5-classes-conf/">classes.conf</a>(5)</i>, <i><a HREF="/docs/linux/man/8-cupsd/">cupsd</a>(8)</i>, <i><a HREF="/docs/linux/man/5-cupsd-conf/">cupsd.conf</a>(5)</i>, <i><a HREF="/docs/linux/man/5-mime-convs/">mime.convs</a>(5)</i>, <i><a HREF="/docs/linux/man/5-mime-types/">mime.types</a>(5)</i>, <i><a HREF="/docs/linux/man/5-printers-conf/">printers.conf</a>(5)</i>, <i><a HREF="/docs/linux/man/5-subscriptions-conf/">subscriptions.conf</a>(5)</i>, 
 <a rel="nofollow" HREF="http://localhost:631/help">http://localhost:631/help</a>

<h2>Copyright</h2>

Copyright 2007-2013 by Apple Inc.
