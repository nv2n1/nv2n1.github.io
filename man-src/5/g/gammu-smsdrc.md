---
title: "gammu-smsdrc(5)"
name: "gammu-smsdrc"
section: "5"
letter: "g"
url: "/docs/linux/man/5-gammu-smsdrc/"
description: "gammu-smsdrc – gammu-smsd(1) configuration file"
---

<p>gammu-smsdrc &#8211; <a href="/docs/linux/man/1-gammu-smsd/">gammu-smsd</a>(1) configuration file </p>
<h2>Synopsis</h2>
<p><i>/etc/gammu-smsdrc</i></p>
<h2>Description</h2>
<p><a href="/docs/linux/man/1-gammu-smsd/">gammu-smsd</a>(1) reads configuration from a config file. It&#8217;s location can be specified on command line, otherwise default path /etc/gammu-smsdrc is used. This file use ini file syntax, with comments being marked with both ; and #. Sections of config file are identified in square brackets line [this]. All key values are case insensitive. Configuration file of gammu-smsd consists of at least two sections &#8211; [gammu] and [smsd]. The [gammu] section is configuration of a phone connection and is same as described in <a href="/docs/linux/man/5-gammurc/">gammurc</a>(5) with the only exception that logfile is ignored and common logging for gammu library and SMS daemon is used. However the logformat directive still configures how much messages gammu emits. The [smsd] section configures SMS daemon itself, which are described in following subsections. First general parameters of SMS daemon are listed and then specific parameters for storage backends. Then there are optional sections [include_numbers] and [exclude_numbers], which control message filtering (see bellow).</p>
<h3>General parameters of SMS daemon</h3>
<dl>
<dt><code>Service</code></p>
<dd>SMSD service to use, one of FILES, MYSQL, PGSQL, DBI (depends on compiled in support for backends). <code>FILES</code> &#8211; stores messages in files, see <a href="/docs/linux/man/7-gammu-smsd-files/">gammu-smsd-files</a>(7) for details<br />
 <code>MYSQL</code> &#8211; stores messages in MySQL database, see <a href="/docs/linux/man/7-gammu-smsd-mysql/">gammu-smsd-mysql</a>(7) for details<br />
 <code>PGSQL</code> &#8211; stores messages in PostgreSQL database, see <a href="/docs/linux/man/7-gammu-smsd-pgsql/">gammu-smsd-pgsql</a>(7) for details<br />
 <code>DBI</code> &#8211; stores messages in any database supported by libdbi, this includes MSSQL, MySQL, PostgreSQL or SQLite databases, see <a href="/docs/linux/man/7-gammu-smsd-dbi/">gammu-smsd-dbi</a>(7) for details</p>
<dt><code>PIN</code></p>
<dd>PIN for SIM card. This is optional, but you should set it if your phone after power on requires PIN.</p>
<dt><code>NetworkCode</code></p>
<dd>Network personalisation password. This is optional, but some phones require it after power on.</p>
<dt><code>PhoneCode</code></p>
<dd>Phone lock password. This is optional, but some phones require it after power on.</p>
<dt><code>LogFile</code></p>
<dd>File where SMSD actions are being logged. You can also use special value &quot;syslog&quot; which will send all messages to syslog daemon. On Windows another special value &quot;eventlog&quot; exists, which will send logs to Windows Event Log. Default is to provide no logging.</p>
<dt><code>DebugLevel</code></p>
<dd>Debug level for SMSD. The integer value should be sum of all flags you want to enable. <code>1</code> &#8211; enables basic debugging information<br />
 <code>2</code> &#8211; enables logging of SQL queries of service backends<br />
 <code>4</code> &#8211; enables logging of gammu debug information (has to be enabled also in gammu section) Generally to get as much debug information as possible, use 255. Default is 0, what should mean no extra information.</p>
<dt><code>CommTimeout</code></p>
<dd>How many seconds should SMSD wait after each read/write loop. Default is 30.</p>
<dt><code>SendTimeout</code></p>
<dd>Shows how many seconds SMSD should wait for network answer during sending sms. If nothing happen during this time, sms will be resent. Default is 30.</p>
<dt><code>MaxRetries</code></p>
<dd>How many times will SMSD try to resend message if sending fails. Default is 1.</p>
<dt><code>ReceiveFrequency</code></p>
<dd>The number of seconds between testing for received SMSes, when the phone is busy sending SMSes. Normally a test for received SMSes is done every CommTimeout seconds and after each sent SMS. Default is 0 (not used).</p>
<dt><code>CheckSecurity</code></p>
<dd>Whether to check if phone wants to enter PIN. Default is 1 (enabled).</p>
<dt><code>ResetFrequency</code></p>
<dd>The number of seconds between performing a preventive soft reset in order to minimize the cases of hanging phones e.g. Nokia 5110 will sometimes freeze to a state when only after unmounting the battery the phone will be functional again. Default is 0 (not used).</p>
<dt><code>DeliveryReport</code></p>
<dd>Whether delivery reports should be used, one of &#8216;no&#8217;, &#8216;log&#8217;, &#8216;sms&#8217;. <code>log</code> &#8211; one line log entry,<br />
 <code>sms</code> &#8211; store in inbox as a received SMS<br />
 <code>no</code> &#8211; no delivery reports Default is &#8216;no&#8217;.</p>
<dt><code>DeliveryReportDelay</code></p>
<dd>Delay in seconds how long is still delivery report considered valid. This depends on brokeness of your network (delivery report should have same timestamp as sent message). Increase this if delivery reports are not paired with sent messages.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> Default is 600 (10 minutes).</p>
<dt><code>PhoneID</code></p>
<dd>String with info about phone used for sending/receiving. This can be useful if you want to run several SMS daemons. When you set PhoneID, all messages (including injected ones) will be marked by this string and it allow more SMS daemons to share single database. This option has actually no effect of FILES backend service.</p>
<dt><code>RunOnReceive</code></p>
<dd>Executes a program after receiving message. This parameter is executed through shell, so you might need to escape some special characters and you can include any number of parameters. Additionally parameters with identifiers of received messages are appended to the command line. The identifiers depend on used service backend, typically it is ID of inserted row for database backends or file name for file based backends.</dl>
<h3>Database backends options</h3>
<p>All DBI, MYSQL and PGSQL backends (see <a href="/docs/linux/man/7-gammu-smsd-mysql/">gammu-smsd-mysql</a>(7), <a href="/docs/linux/man/7-gammu-smsd-pgsql/">gammu-smsd-pgsql</a>(7), <a href="/docs/linux/man/7-gammu-smsd-dbi/">gammu-smsd-dbi</a>(7)) for their documentation) supports same options for configuring connection to a database:</p>
<dl>
<dt><code>User</code></p>
<dd>User name used for connection to a database.</p>
<dt><code>Password</code></p>
<dd>Password used for connection to a database.</p>
<dt><code>PC</code></p>
<dd>Database server address. It can also contain port or socket path after semicolon, for example localhost:/path/to/socket.</p>
<dt><code>Database</code></p>
<dd>Name of database to use. Please note that you should create tables in this database before using gammu-smsd. SQL files for creating needed tables are included in documentation.</p>
<dt><code>SkipSMSCNumber</code></p>
<dd>When you send sms from some SMS centere you can have delivery reports from other SMSC number. You can set here number of this SMSC used by you and Gammu will not check it&#8217;s number during assigning reports to sent SMS.</p>
<dt><code>Driver</code></p>
<dd>DBI driver to use. Depends on what DBI drivers you have installed, DBI supports: mysql, freetds (provides access to MS SQL Server and Sybase), pgsql, sqlite, sqlite3, firebird and ingres, msql and oracle drivers are under development.</p>
<dt><code>DriversPath</code></p>
<dd>Path, where DBI drivers are stored, this usually does not have to be set if you have properly installed drivers.</p>
<dt><code>DBDir</code></p>
<dd>Database directory for some (currently only sqlite) DBI drivers. Set here path where sqlite database files are stored.</dl>
<h3>Files backend options</h3>
<p>The FILES backend accepts following configuration options. See <a href="/docs/linux/man/7-gammu-smsd-files/">gammu-smsd-files</a>(7) for more detailed service backend description. Please note that all path should contain trailing path separator (/ on Unix systems):</p>
<dl>
<dt><code>InboxPath</code></p>
<dd>Where the received SMSes are stored. Default is current directory.</p>
<dt><code>OutboxPath</code></p>
<dd>Where SMSes to be sent should be placed. Default is current directory.</p>
<dt><code>SentSMSPath</code></p>
<dd>Where the transmitted SMSes are placed, if same as OutBoxPath transmitted messages are deleted. Default is to delete transmitted messages.</p>
<dt><code>ErrorSMSPath</code></p>
<dd>Where SMSes with error in transmission is placed. Default is same as SentSMSPath.</p>
<dt><code>InboxFormat</code></p>
<dd>The format in which the SMS will be stored: &#8216;detail&#8217;, &#8216;unicode&#8217;, &#8216;standard&#8217;. <code>detail</code> &#8211; format used for message backup by <a href="/docs/linux/man/1-gammu/">gammu</a>(1)<br />
 <code>unicode</code> &#8211; message text stored in unicode (UTF-16)<br />
 <code>standard</code> &#8211; message text stored in system charset Default is &#8216;unicode&#8217;.</p>
<dt><code>TransmitFormat</code></p>
<dd>The format for transmitting the SMS: &#8216;auto&#8217;, &#8216;unicode&#8217;, &#8216;7bit&#8217;. Default is &#8216;auto&#8217;.</dl>
<h3>Message filtering</h3>
<p>SMSD allows to process only limited subset of incoming messages. You can define filters in [include_numbers] and [exclude_numbers] sections. If [include_numbers] section exists, all values (keys are ignored) from it are used as allowed phone numbers and no other message is processed. On the other side, in [exclude_numbers] you can specify numbers which you want to skip. </p>
<h2>Example</h2>
<p>There is more complete example available in Gammu documentation. Please note that for simplicity following examples do not include [gammu] section, you can look into <a href="/docs/linux/man/5-gammurc/">gammurc</a>(5) for some examples how it can look like. SMSD configuration file for FILES backend could look like:  </p>
<pre>[smsd]
Service = files
PIN = 1234
LogFile = syslog
InboxPath = /var/spool/sms/inbox/
OutboPpath = /var/spool/sms/outbox/
SentSMSPath = /var/spool/sms/sent/
ErrorSMSPath = /var/spool/sms/error/</pre>
<p> If you want to use MYSQL backend, you will need something like this:  </p>
<pre>[smsd]
Service = mysql
PIN = 1234
LogFile = syslog
User = smsd
Password = smsd
PC = localhost
Database = smsd</pre>
<p> Process only messages from 123456 number:  </p>
<pre>[include_numbers]
number1 = 123456</pre>
<p> Do not process messages from evil number 666:  </p>
<pre>[exclude_numbers]
number1 = 666</pre>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-gammu-smsd/">gammu-smsd</a>(1), <a href="/docs/linux/man/1-gammu/">gammu</a>(1), <a href="/docs/linux/man/5-gammurc/">gammurc</a>(5) </p>
<p> <a href="/docs/linux/man/7-gammu-smsd-files/">gammu-smsd-files</a>(7), <a href="/docs/linux/man/7-gammu-smsd-mysql/">gammu-smsd-mysql</a>(7), <a href="/docs/linux/man/7-gammu-smsd-pgsql/">gammu-smsd-pgsql</a>(7), <a href="/docs/linux/man/7-gammu-smsd-dbi/">gammu-smsd-dbi</a>(7), <a href="/docs/linux/man/7-gammu-smsd-tables/">gammu-smsd-tables</a>(7)</p>
<h2>Author</h2>
<p>gammu-smsd and this manual page were written by Michal Cihar &lt;michal [at] cihar.com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009 Michal Cihar and other authors. License GPLv2: GNU GPL version 2 &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">http://www.gnu.org/licenses/old-licenses/gpl-2.0.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>Reporting Bugs</h2>
<p>Please report bugs to &lt;<a rel="nofollow" href="http://bugs.cihar.com">http://bugs.cihar.com</a>&gt;. </p>
<p> Before reporting a bug, please enable verbose logging in SMSD configuration: </p>
<p>&nbsp;<wbr>[gammu]<br />
&nbsp;<wbr>logformat&nbsp;<wbr>=&nbsp;<wbr>textall </p>
<p>&nbsp;<wbr>[smsd]<br />
&nbsp;<wbr>debuglevel&nbsp;<wbr>=&nbsp;<wbr>255<br />
&nbsp;<wbr>logfile&nbsp;<wbr>=&nbsp;<wbr>smsd.log </p>
<p> and include this verbose log within bug report.</p>
