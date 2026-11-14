---
title: "twconfig(4)"
name: "twconfig"
section: "4"
letter: "t"
url: "/docs/linux/man/4-twconfig/"
description: "twconfig – Tripwire configuration file reference"
---

<p>twconfig &#8211; <i>Tripwire</i> configuration file reference</p>
<h2>Description</h2>
<p>The configuration file stores system-specific information, including the location of <i>Tripwire</i> data files, and the settings used to send email notification. The configuration file settings are generated during the installation process, but can be changed by the system administrator at any time. The configuration file is signed with the site key, and the site passphrase is required to edit the file. </p>
<p> During installation, a signed <i>Tripwire</i> configuration file <i>tw.cfg</i> will be created in the <i>/etc/tripwire</i> directory, and a plain text copy of this configuration file <i>twcfg.txt</i> will be created in the same directory. </p>
<p> The configuration file is modified using the <code>twadmin &#8211;create-cfgfile</code> command. With this command, the user can designate an existing plain text file as the current configuration file. Using the current site key and passphrase, the new configuration file is cryptographically signed and saved with this command.</p>
<h3>Components of the Configuration File</h3>
<p>The <i>Tripwire</i> configuration file is structured as a list of keyword-value pairs, and may also contain comments and variable definitions. Any lines with &quot;#&quot; in the first column are treated as comments. </p>
<p> The general syntax for variable definition is: </p>
<pre><i>keyword</i> = <i>value</i></pre>
<p>For example: <font SIZE="-1"> </font></p>
<pre>ROOT = /usr/tripwire
EDITOR = /usr/local/bin/jove</pre>
<p>Variable substitution on the right hand side is permitted using the syntax: </p>
<pre>$(<i> varname </i>)</pre>
<p>For example: <font SIZE="-1"> </font></p>
<pre>DBFILE = $(ROOT)/db/$(HOSTNAME).twd</pre>
<p>Variable names are case-sensitive, and may contain all alphanumeric characters, underscores, the characters &quot;+-@:&quot;, and the period. Two variables are predefined in the configuration file, and may not be changed. <tt>HOSTNAME</tt> is the unqualified hostname that <i>Tripwire</i> is running on, and <tt>DATE</tt> is a string representation of the date and time.</p>
<h3>Required Variables</h3>
<p>The following variables must be set in order for <i>Tripwire</i> to operate. The values listed below are assigned during installation. </p>
<p> <font SIZE="-1"> </font></p>
<pre>POLFILE Default = /etc/tripwire/tw.pol
DBFILE Default = /var/lib/tripwire/$(HOSTNAME).twd
REPORTFILE Default = /var/lib/tripwire/report/$(HOSTNAME)-$(DATE).twr
SITEKEYFILE Default = /etc/tripwire/site.key
LOCALKEYFILE Default = /etc/tripwire/$(HOSTNAME)-local.key</pre>
<h3>Other Variables</h3>
<p>The following variables are not required to run <i>Tripwire</i>, but some of the program&#8217;s functionality will be lost without them. The values assigned during installation are listed.</p>
<dl>
<dt><tt>EDITOR</tt></p>
<dd>Specifies an editor to be used in interactive modes. If <i>EDITOR</i> is not defined, and no editor is specified on the command line, using interactive modes will cause an error.<br />
 Initial value: <i>/bin/vi</i></p>
<dt><tt>TEMPDIRECTORY</tt></p>
<dd>This variable can be set to the location to which tripwire should write its temporary files. By default it is /tmp, which due to the default permissions can be very insecure. It is recommended that you use this configuration variable to provide tripwire with a secure place to write temporary files. The directory used should have its permissions set such that only the owning process can read/write to it, i.e. &quot;chmod 700&quot;.<br />
 Initial value: <i>/tmp</i></p>
<dt><tt>GLOBALEMAIL</tt></p>
<dd>This variable is set to a list of email addresses separated by either a comma &quot;,&quot;, or semi-colon &quot;;&quot;. If a report would have normally been sent out, it will also be send to this list of recipients.<br />
 Initial value: <i>none</i></p>
<dt><tt>LATEPROMPTING</tt></p>
<dd>Prompt for passphrase as late as possible to minimize the amount of time that the passphrase is stored in memory. If the value is <i>true</i> (case-sensitive), then late prompting is turned on. With any other value, or if the variable is removed from the configuration file, late prompting is turned off.<br />
 Initial value: <i>false</i></p>
<dt><tt>LOOSEDIRECTORYCHECKING</tt></p>
<dd>When a file is added or removed from a directory, <i>Tripwire</i> reports both the changes to the file itself, and the modification to the directory (size, num links, etc.). This can create redundant entries in <i>Tripwire</i> reports. With loose directory checking, Tripwire will not check directories for any properties that would change when a file was added or deleted. This includes: size, number of links, access time, change time, modification time, number of blocks, growing file, and all hashes.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></p>
<dd>If the value for this variable is <i>true</i> (case-sensitive), then loose directory checking is turned on, and these properties will be ignored for all directories. With any other value, or if the variable is removed from the configuration file, loose directory checking is turned off. Turning loose directory checking on is equivalent to appending the following propertymask to the rules for all directory inodes: <font SIZE="-1"> -snacmblCMSH </font><br />
 Initial value: <i>false</i></p>
<dt><tt>SYSLOGREPORTING</tt></p>
<dd>If this variable is set to <i>true</i>, messages are sent to the syslog for four events: database initialization, integrity check completions, database updates, and policy updates. The syslog messages are sent from the &quot;user&quot; facility at the &quot;notice&quot; level. For more information, see the <code><a href="/docs/linux/man/1-syslogd/">syslogd</a></code>(1) man page and the <i>syslog.conf</i> file. The following illustrates the information logged in the syslog for each of the four events: <font SIZE="-1"> </font></p>
<pre>Jun 18 14:09:42 lighthouse tripwire[9444]: Database initialized:
/var/lib/tripwire/test.twd
Jun 18 14:10:57 lighthouse tripwire[9671]: Integrity Check Complete:
TWReport lighthouse 20000618141057 V:2 S:90 A:1 R:0 C:1
 
Jun 18 14:11:19 lighthouse tripwire[9672]: Database Update Complete:
/var/lib/tripwire/test.twd 
Jun 18 14:18:26 lighthouse tripwire[9683]: Policy Update Complete:
/var/lib/tripwire/test.twd </pre>
<p>The letters in the Integrity Checking log correspond to # of violations, maximum severity level, and # of files added, deleted, and changed, respectively. With any value other than <i>true</i>, or if this variable is removed from the configuration file, syslog reporting will be turned off.<br />
 Initial value: <i>true</i></p>
<dt><tt>REPORTLEVEL</tt></p>
<dd>Specifies the default level of report produced by the <code>twprint &#8211;print-report</code> mode. Valid values for this option are 0 to 4. The report level specified by this option can be overridden with the (<code>-t</code>&nbsp;<wbr>or&nbsp;<wbr><code>&#8211;report-level</code>) option on the command line. If this variable is not included in the configuration file, the default report level is 3. Note that only reports printed using the <code>twprint &#8211;print-report</code> mode are affected by this parameter; reports displayed by other modes and other commands are not affected.<br />
 Initial value: <i>3</i></p>
<dt><tt>HASH_DIRECT_IO</tt></p>
<dd>Use direct i/o when hashing files. (Linux-only as of OST 2.4.3.2)<br />
 Initial value: <i>false</i></p>
<dt><tt>RESOLVE_IDS_TO_NAMES</tt></p>
<dd>Specifies whether to resolve uid/gid values to user &amp; group names. Static binaries may segfault while calling getpwuid/getgrgid in certain nsswitch.conf configurations, and setting this to false will bypass the name resolution step and prevent the segfault.<br />
 Initial value: <i>true</i></dl>
<h3>Email Notification Variables</h3>
<dl>
<dt><tt>MAILMETHOD</p>
<dd>Specifies the protocol to be used by </tt><i>Tripwire</i> for email notification. The only acceptable values for this field are <tt>SMTP</tt> or <tt>SENDMAIL</tt>. Any other value will produce an error message.<br />
 Initial value: <i>SENDMAIL</i></p>
<dt><tt>SMTPHOST</p>
<dd>Specifies the domain name or IP address of the SMTP server used for email notification. Ignored unless MAILMETHOD</tt> is set to <tt>SMTP</tt>.<br />
 Initial value: <i>mail.domain.com</i></p>
<dt><tt>SMTPPORT</p>
<dd>Specifies the port number used with SMTP. Ignored unless MAILMETHOD</tt> is set to <tt>SMTP</tt>.<br />
 Initial value: <i>25</i></p>
<dt><tt>MAILPROGRAM</tt></p>
<dd>Specifies the program used for email reporting of rule violations if <tt>MAILMETHOD</tt> is set to <tt>SENDMAIL</tt>. The program must take an RFC822 style mail header, and recipients will be listed in the &quot;To:&quot; field of the mail header. Some mail programs interpret a line consisting of only a single period character to mean end-of-input, and all text after that is ignored. Since there is a small possibility that a <i>Tripwire</i> report would contain such a line, the mail program specified must be able to ignore lines that consist of a single period (the <code>-oi</code> option to sendmail produces this behavior).<br />
 Initial value: <i>/usr/lib/sendmail -oi -t</i></p>
<dt><tt>EMAILREPORTLEVEL</tt></p>
<dd>Specifies the default level of report produced by the <code>tripwire &#8211;check</code> mode email report. Valid values for this option are 0 to 4. The report level specified by this option can be overridden with the (<code>-t</code>&nbsp;<wbr>or&nbsp;<wbr><code>&#8211;email-report-level</code>) option on the command-line. If this variable is not included in the configuration file, the default report level is 3.<br />
 Initial value: <i>3</i></p>
<dt><tt>MAILNOVIOLATIONS</tt></p>
<dd>This option controls the way that <i>Tripwire</i> sends email notification if no rule violations are found during an integrity check. If <tt>MAILNOVIOLATIONS</tt> is set to <i>false</i> and no violations are found, <i>Tripwire</i> will not send a report. With any other value, or if the variable is removed from the configuration file, <i>Tripwire</i> will send an email message stating that no violations were found.</p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></p>
<dd>Mailing reports of no violations allows an administrator to distinguish between unattended integrity checks that are failing to run and integrity checks that are running but are not finding any violations. However, mailing no violations reports will increase the amount of data that must be processed.<br />
 Initial value: <i>true</i></p>
<dt><tt>MAILFROMADDRESS</tt></p>
<dd>Specifies the value of the &quot;From:&quot; field in email reports.<br />
 Initial value: <i>tripwire [at] hostname</i>, where &#8216;hostname&#8217; is the local machine name.</dl>
<h2>Version Information</h2>
<p>This man page describes <i>Tripwire 2.4</i>.</p>
<h2>Authors</h2>
<p>Tripwire, Inc.</p>
<h2>Copying Permissions</h2>
<p>Permission is granted to make and distribute verbatim copies of this man page provided the copyright notice and this permission notice are preserved on all copies. </p>
<p> Permission is granted to copy and distribute modified versions of this man page under the conditions for verbatim copying, provided that the entire resulting derived work is distributed under the terms of a permission notice identical to this one. </p>
<p> Permission is granted to copy and distribute translations of this man page into another language, under the above conditions for modified versions, except that this permission notice may be stated in a translation approved by Tripwire, Inc. </p>
<p> Copyright 2000-2017 Tripwire, Inc. Tripwire is a registered trademark of Tripwire, Inc. in the United States and other countries. All rights reserved.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-twintro/">twintro</a></code>(8), <code><a href="/docs/linux/man/8-tripwire/">tripwire</a></code>(8), <code><a href="/docs/linux/man/8-twadmin/">twadmin</a></code>(8), <code><a href="/docs/linux/man/8-twprint/">twprint</a></code>(8), <code><a href="/docs/linux/man/8-siggen/">siggen</a></code>(8), <code><a href="/docs/linux/man/4-twpolicy/">twpolicy</a></code>(4), <code><a href="/docs/linux/man/5-twfiles/">twfiles</a></code>(5), <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1), <code><a href="/docs/linux/man/1-vi/">vi</a></code>(1), <code><a href="/docs/linux/man/1-syslogd/">syslogd</a></code>(1) </p>
