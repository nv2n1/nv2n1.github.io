---
title: "gnokii-smsd(8)"
name: "gnokii-smsd"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gnokii-smsd/"
description: "gnokii-gnokii-smsd.- daemon for handling incoming and outgoing SMSes using libgnokii"
---

<p>gnokii-gnokii-smsd.- daemon for handling incoming and outgoing SMSes using libgnokii</p>
<h2>Synopsis</h2>
<p><code>gnokii-gnokii-smsd.</code><i>[OPTIONS]</i> </p>
<h2>Description</h2>
<p>The <code>SMSD</code> (SMS daemon) program is intended for receiving and sending SMSes. The program is designed to use modules (plugins) to work with different backends. Currently are supported PostgreSQL, MySQL and a special module &#8216;file&#8217; which is designed to work without an SQL database (see below for special instructions in the file module section). When <code>SMSD</code> uses an SQL server as a repository for SMSes you must create a database (default name is &#8216;sms&#8217;) with tables defined in sms.tables.{module}.sql files. Table &#8216;inbox&#8217; is for received SMSes. <code>SMSD</code> periodically checks a given phone memory to move messages to this table. Only received SMSes and status reports are deleted from the phone, other kinds of messages are not removed. Table &#8216;inbox&#8217; has the following fields:</p>
<dl>
<dd>
<dl>
<dt><code>number</code></p>
<dd>phone number from which is sms received</p>
<dt><code>gnokii-smsd.te</code></p>
<dd>date set by SMS center</p>
<dt><code>insertdate</code></p>
<dd>date SMS was inserted into table</p>
<dt><code>text</code></p>
<dd>SMS text</p>
<dt><code>phone</code></p>
<dd>number of phone to use. If you use gnokii-gnokii-smsd.without -t option you can ignore this column. See -t option below.</p>
<dt><code>processed</code></p>
<dd>gnokii-gnokii-smsd.sets this always to FALSE. You can use it for another program which will parse SMSes.</dl>
</dl>
<p> Table &#8216;outbox&#8217; is for outgoing SMSes. <code>SMSD</code> periodically looks into this table and searches for lines with attribute &#8216;processed&#8217; set to FALSE. If it finds such SMS, it will send SMS to &#8216;number&#8217;. Table &#8216;outbox&#8217; has the following fields:</p>
<dl>
<dd>
<dl>
<dt><code>number</code></p>
<dd>recipient&#8217;s phone number</p>
<dt><code>processed_date</code></p>
<dd>date of processing SMS.</p>
<dt><code>insertdate</code></p>
<dd>date of inserting SMS in table</p>
<dt><code>text</code></p>
<dd>SMS text</p>
<dt><code>phone</code></p>
<dd>number of phone to use. If you use gnokii-gnokii-smsd.without -t option you must not fill this column. See -t option below.</p>
<dt><code>processed</code></p>
<dd>new SMS must have this attribute set to FALSE. <code>SMSD</code> will send this SMS and will update &#8216;processed&#8217; to TRUE.</p>
<dt><code>error</code></p>
<dd>This attribute contains return value of gn_sms_send() function. For explanation of numeric values see &lt;gnokii/error.h&gt; in gnokii source.</p>
<dt><code>dreport</code></p>
<dd>request for delivery report per message. Possible values are 0 for no delivery report, 1 for delivery report.</p>
<dt><code>not_before</code></p>
<dd>sms will not be sent before this time (default 00:00:00).</p>
<dt><code>not_after</code></p>
<dd>sms will not be sent after this time (default 23:59:59).</dl>
</dl>
<p> <code>SMSD</code> is multi threaded program. If you list processes you will see more than one instance of gnokii-smsd.</p>
<h3>The File Module</h3>
<p>This module doesn&#8217;t need an SQL server to work. For incoming messages it works in a way that it calls a program giving phone number, date as parameter and the message text on stdin. In the gnokii-gnokii-smsd.directory there is an example file action. It shows sms data to stdout. If you want something useful you must write your own action. For outgoing messages you can set spool directory where gnokii-gnokii-smsd.looks regularly. Incoming sms are passed in format</p>
<dl>
<dd>
<dl>
<dt><code>action number date&nbsp;<wbr>&lt;&nbsp;<wbr>sms</code></p>
<dd></dl>
</dl>
<p> Outgoing sms must be in format:</p>
<dl>
<dd>
<dl>
<dt><code>number</code></p>
<dd>
<dt><code>text</code></p>
<dd></dl>
</dl>
<p> The name of file is unimportant but gnokii-gnokii-smsd.ignores all files with prefix &quot;ERR.&quot;. If gnokii-gnokii-smsd.succesfully sends sms, it removes file from spool directory. If gnokii-gnokii-smsd.cannot send sms prepends file with &quot;ERR.&quot; prefix and ignores it. If you use <i>-m file</i>, <i>-u</i> (<i>&#8211;user</i>) and <i>-c</i> (<i>&#8211;host</i>) will have other meaning. <i>-u</i> is for action (action must be executable) <i>-c</i> is for spool directory where gnokii-gnokii-smsd.looks for smses. Smsd must have read and write permissions to this directory. <i>-p</i>, <i>-d</i> parameters have no meaning when <i>-m file</i> is used. If you don&#8217;t specify <i>-u</i>, default action is to print sms to stdout. If you don&#8217;t specify <i>-c</i>, sms sending will be disabled.</p>
<h3>Options</h3>
<p>Available options:</p>
<dl>
<dt><code>-u, &#8211;user db_username</code></p>
<dd>Specify user name.</p>
<dt><code>-p, &#8211;password db_password</code></p>
<dd>Specify user password.</p>
<dt><code>-d, &#8211;db db_name</code></p>
<dd>Specify database name for &#8216;pq&#8217; and &#8216;mysql&#8217; modules or full path to database file for &#8216;sqlite&#8217; module (defaults to &#8216;sms&#8217;).</p>
<dt><code>-c, &#8211;host db_hostname</code></p>
<dd>Specify database server host name.</p>
<dt><code>-s, &#8211;schema db_hostname</code></p>
<dd>Specify database schema used by the PostgreSQL module (defaults to &#8216;public&#8217;).</p>
<dt><code>-e, &#8211;encoding client_encoding</code></p>
<dd>Specify client encoding for database connection.</p>
<dt><code>-m, &#8211;module db_module</code></p>
<dd>Specify which module to use for connection to DB server. Currently supported values are &#8216;pq&#8217; for PostgreSQL, &#8216;mysql&#8217; for MySQL, &#8216;sqlite&#8217; for SQLite3 and &#8216;file&#8217;. File module is not supported in Windows.</p>
<dt><code>-l, &#8211;libdir path_to_db_module</code></p>
<dd>Specify path to DB modules. If you specify pq module, gnokii-gnokii-smsd.searches in libdir for file libsmsd_pq.so (for mysql &#8211; libsmsd_mysql.so). Do not interchange these plugins with default SQL libraries from database distribution!</p>
<dt><code>-f, &#8211;logfile file</code></p>
<dd>If used, gnokii-gnokii-smsd.will monitor sms traffic to file &quot;file&quot;. File is reopened and closed for every message so you can simply rename or delete it if you want to rotate logs. If you use &#8216;-&#8216; as filename smsd will use standard output.</p>
<dt><code>-t, &#8211;phone phone_number</code></p>
<dd>You can run more instances of gnokii-smsd. One instance per phone. In this setup you must configure phone section in the config file. For example:</p>
<dl>
<dd>[global] port = /dev/ttyS0 model = 6110 initlength = default connection = serial bindir = /usr/local/sbin/ use_locking = no serial_baudrate = 38400 smsc_timeout = 10 [phone_1] port = /dev/ttyS0 model = 6110 initlength = default connection = serial bindir = /usr/local/sbin/ use_locking = no serial_baudrate = 38400 [phone_2] port = /dev/ttyS1 model = AT initlength = default connection = serial bindir = /usr/local/sbin/ use_locking = no serial_baudrate = 38400 smsc_timeout = 10 In this setup if you run gnokii-gnokii-smsd.without -t option it will use config from global section. If you run gnokii-gnokii-smsd.with -t 1 it will use config from phone_1 and likewise with -t 2 uses phone_2. In case of use -t option gnokii-gnokii-smsd.fills phone number for incoming sms&#8217;s and in outbox it looks only for sms&#8217;s with the specified phone number in column &#8216;phone&#8217;. This behaviour gives you possibility to run one instance of gnokii-gnokii-smsd.for every phone you have at the same time.</dl>
<dt><code>-i, &#8211;interval interval</code></p>
<dd>Polling interval for incoming sms&#8217;s in seconds. Default is 1 second.</p>
<dt><code>-S, &#8211;maxsms number</code></p>
<dd>When phone driver doesn&#8217;t support sms status it is possible to specify number of sms&#8217;s supported by phone. Default is 10. If driver support sms status this option is ignored.</p>
<dt><code>-b, &#8211;inbox memory_type</code></p>
<dd>Where to look for new messages (defaults to IN for most Nokia phones and to SM for all other phones). For debugging or for unusual setups you can use another memory type supported by your phone (eg. IN for the Inbox, OU for the Outbox, AR for the Archive, TE for the Templates and F1,&#8230;,F20 for your own folders). Use gnokii &#8211;showsmsfolderstatus for a list of such memory types.</p>
<dt><code>-0, &#8211;firstpos0</code></p>
<dd>SMSD starts messages reading from position 1. If your phone stores sms&#8217;s from postion 0, use this option.</p>
<dt><code>-v, &#8211;version</code></p>
<dd>Shows gnokii-gnokii-smsd.version.</p>
<dt><code>-h, &#8211;help</code></p>
<dd>Shows short help. </p>
<h2>Diagnostics</h2>
<p>Various error messages are printed to STDERR. </p>
<p> Debug output can be enabled setting xdebug=on (for messages specific to <code>SMSD</code>) and debug=on (for messages specific to <code>libgnokii</code>) in the configuration file.</p>
<h2>Bugs</h2>
<p>None reported. </p>
<h2>Author</h2>
<p><code>SMSD</code> was written by Jan Derfinak and contributed by other people. See also Docs/CREDITS from the Gnokii sources.</p>
<h2>Copying</h2>
<p>This program is distributed under the GNU Public License.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-gnokii/">gnokii</a>(1) </p>
