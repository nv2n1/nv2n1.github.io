---
title: "gammu-smsd-tables(7)"
name: "gammu-smsd-tables"
section: "7"
letter: "g"
url: "/docs/linux/man/7-gammu-smsd-tables/"
description: "gammu-smsd-tables – description of tables for database backends of gammu-smsd(1)"
---

<p>gammu-smsd-tables &#8211; description of tables for database backends of <a href="/docs/linux/man/1-gammu-smsd/">gammu-smsd</a>(1) </p>
<h2>Description</h2>
<p><a href="/docs/linux/man/1-gammu-smsd/">gammu-smsd</a>(1) supports several backends. Actual backend is chosen in a config file <a href="/docs/linux/man/5-gammu-smsdrc/">gammu-smsdrc</a>(5). Separate backends are described in their appropriate man pages. This manual page describes general database structure and required tables. More SMS daemons can share single database. If you do not specify PhoneID in their configuration, all are treated equally and you have no guarantee which one sends outgoing message. If you configure PhoneID and use it when inserting message to the outbox table (<a href="/docs/linux/man/1-gammu-smsd-inject/">gammu-smsd-inject</a>(1) does this), each SMS daemon will have separate outbox queue.</p>
<h3>Receiving of messages</h3>
<p>Received messages are stored in inbox table.</p>
<h3>Transmitting of messages</h3>
<p>Transmitted messages are read from table outbox and possible subsequent parts of the same message from outbox_multipart.</p>
<h3>Description of tables</h3>
<dl>
<dt><code>daemons</code></p>
<dd>Information about running daemons.</p>
<dt><code>gammu</code></p>
<dd>Table holding single value &#8211; version of a database schema. See HISTORY for details what has changed.</p>
<dt><code>inbox</code></p>
<dd>Table where received messages will be stored. Fields description: <code>UpdatedInDB</code> (timestamp)<br />
 when somebody (daemon, user, etc.) updated it <code>ReceivingDateTime</code> (timestamp)<br />
 when SMS was received <code>Text</code> (text)<br />
 encoded SMS text (for all SMS) <code>SenderNumber</code> (varchar(20))<br />
 decoded SMS sender number <code>Coding</code> (enum(&#8216;Default_No_Compression&#8217;, &#8216;Unicode_No_Compression&#8217;, &#8216;8bit&#8217;, &#8216;Default_Compression&#8217;, &#8216;Unicode_Compression&#8217;))<br />
 SMS text coding <code>UDH</code> (text)<br />
 encoded User Data Header text <code>SMSCNumber</code> (varchar(20))<br />
 decoded SMSC number <code>Class</code> (integer)<br />
 SMS class or -1 (0 is normal SMS, 1 is flash one) <code>TextDecoded</code> (varchar(160))<br />
 decoded SMS text (for Default Alphabet/Unicode SMS) <code>ID</code> (integer unsigned)<br />
 SMS identificator (for using with external applications) <code>RecipientID</code> (text)<br />
 which Gammu daemon has added it <code>Processed</code> (enum(&#8216;false&#8217;, &#8216;true&#8217;))<br />
 you can use for marking, whether SMS was processed or not</p>
<dt><code>outbox</code></p>
<dd>Messages enqueued for sending should be placed in this table. If message is multipart, subsequent parts are stored in table outbox_multipart. Fields description: <code>UpdatedInDB</code> (timestamp)<br />
 when somebody (daemon, user, etc.) updated it <code>InsertIntoDB</code> (timestamp)<br />
 when message was inserted into database <code>SendingDateTime</code> (timestamp)<br />
 set it to some value, when want to force sending after some planned time <code>Text</code> (text)<br />
 SMS text encoded using hex values in proper coding. If you want to use TextDecoded field, keep this NULL (or empty). <code>DestinationNumber</code> (varchar(20))<br />
 recipient number <code>Coding</code> (enum(&#8216;Default_No_Compression&#8217;, &#8216;Unicode_No_Compression&#8217;, &#8216;8bit&#8217;, &#8216;Default_Compression&#8217;, &#8216;Unicode_Compression&#8217;))<br />
 SMS text coding <code>UDH</code> (text)<br />
 User Data Header encoded using hex values which will be used for constructing the message. Without this, message will be sent as plain text. <code>Class</code> (integer)<br />
 SMS class or -1 (0 is normal SMS, 1 is flash one) <code>TextDecoded</code> (varchar(160))<br />
 SMS text in &quot;human readable&quot; form <code>ID</code> (integer unsigned)<br />
 SMS/SMS sequence ID Please note that this number has to be unique also for sentitems table, so reusing message IDs might not be a good idea. <code>MultiPart</code> (enum(&#8216;false&#8217;,&#8217;true&#8217;))<br />
 info, whether there are more SMS from this sequence in outbox_multipart <code>RelativeValidity</code> (integer)<br />
 SMS relative validity like encoded using GSM specs <code>SenderID</code> (text)<br />
 which SMSD instance should send this one sequence <code>SendingTimeOut</code> (timestamp)<br />
 used by SMSD instance for own targets <code>DeliveryReport</code> (enum(&#8216;default&#8217;,&#8217;yes&#8217;,&#8217;no&#8217;))<br />
 when default is used, Delivery Report is used or not according to SMSD instance settings; yes forces Delivery Report. <code>CreatorID</code> (text)<br />
 sender identification, it has to match PhoneID in SMSD configuration to make SMSD process this message</p>
<dt><code>outbox_multipart</code></p>
<dd>Data for outgoing multipart messages. Fields description: <code>ID</code> (integer unsigned)<br />
 <code>Text</code> (text)<br />
 <code>Coding</code> (enum(&#8216;Default_No_Compression&#8217;, &#8216;Unicode_No_Compression&#8217;, &#8216;8bit&#8217;, &#8216;Default_Compression&#8217;, &#8216;Unicode_Compression&#8217;))<br />
 <code>UDH</code> (text)<br />
 <code>Class</code> (integer)<br />
 <code>TextDecoded</code> (varchar(160))<br />
 <code>ID</code> (integer unsigned)<br />
 the same meaning as values in outbox table <code>SequencePosition</code> (integer)<br />
 info, what is SMS number in SMS sequence (start at 2, first part is in outbox table).</p>
<dt><code>phones</code></p>
<dd>Information about connected phones. This table is periodically refreshed and you can get information such as battery or signal level from here. Fields description: <code>ID</code> (text)<br />
 PhoneID value <code>UpdatedInDB</code> (timestamp)<br />
 when this record has been updated <code>InsertIntoDB</code> (timestamp)<br />
 when this record has been created (when phone has been connected) <code>TimeOut</code> (timestamp)<br />
 when this record expires <code>Send</code> (boolean)<br />
 currently always true <code>Receive</code> (boolean)<br />
 currently always true <code>IMEI</code> (text)<br />
 IMEI of phone <code>Client</code> (text)<br />
 client name, usually string Gammu with version <code>Battery</code> (integer)<br />
 battery level in percent (or -1 if unknown) <code>Signal</code> (integer)<br />
 signal level in percent (or -1 if unknown) <code>Sent</code> (integer)<br />
 Number of sent SMS messages (SMSD does not reset this counter, so it might overflow). <code>Received</code> (integer)<br />
 Number of received SMS messages (SMSD does not reset this counter, so it might overflow).</p>
<dt><code>sentitems</code></p>
<dd>Log of sent messages (and unsent ones with error code). Also if delivery reports are enabled, message state is updated after receiving delivery report. Fields description: <code>UpdatedInDB</code> (timestamp)<br />
 when somebody (daemon, user, etc.) updated it <code>InsertIntoDB</code> (timestamp)<br />
 when message was inserted into database <code>SendingDateTime</code> (timestamp)<br />
 when message has been sent <code>DeliveryDateTime</code> (timestamp)<br />
 Time of receiving delivery report (if it has been enabled). <code>Status</code> (enum(&#8216;SendingOK&#8217;, &#8216;SendingOKNoReport&#8217;, &#8216;SendingError&#8217;, &#8216;DeliveryOK&#8217;, &#8216;DeliveryFailed&#8217;, &#8216;DeliveryPending&#8217;, &#8216;DeliveryUnknown&#8217;, &#8216;Error&#8217;))<br />
 Status of message sending. SendingError mens that phone failed to send the message, Error indicates some other error while processing message.<br />
&nbsp;<wbr><code>SendingOK</code>&nbsp;<wbr>&#8211; Message has been sent, waiting for delivery report.<br />
&nbsp;<wbr><code>SendingOKNoReport</code>&nbsp;<wbr>&#8211; Message has been sent without asking for delivery report.<br />
&nbsp;<wbr><code>SendingError</code>&nbsp;<wbr>&#8211; Sending has failed.<br />
&nbsp;<wbr><code>DeliveryOK</code>&nbsp;<wbr>&#8211; Delivery report arrived and reported success.<br />
&nbsp;<wbr><code>DeliveryFailed</code>&nbsp;<wbr>&#8211; Delivery report arrived and reports failure.<br />
&nbsp;<wbr><code>DeliveryPending</code>&nbsp;<wbr>&#8211; Delivery report announced pending deliver.<br />
&nbsp;<wbr><code>DeliveryUnknown</code>&nbsp;<wbr>&#8211; Delivery report reported unknown status.<br />
&nbsp;<wbr><code>Error</code>&nbsp;<wbr>&#8211; Some other error happened during sending&nbsp;<wbr>(usually bug in SMSD). <code>StatusError</code> (integer)<br />
 Status of delivery from delivery report message, codes are defined in GSM specification. <code>Text</code> (text)<br />
 SMS text encoded using hex values <code>DestinationNumber</code> (varchar(20))<br />
 decoded destination number for SMS <code>Coding</code> (enum(&#8216;Default_No_Compression&#8217;, &#8216;Unicode_No_Compression&#8217;, &#8216;8bit&#8217;, &#8216;Default_Compression&#8217;, &#8216;Unicode_Compression&#8217;))<br />
 SMS text coding <code>UDH</code> (text)<br />
 User Data Header encoded using hex values <code>SMSCNumber</code> (varchar(20))<br />
 decoded number of SMSC, which sent SMS <code>Class</code> (integer)<br />
 SMS class or -1 (0 is normal SMS, 1 is flash one) <code>TextDecoded</code> (varchar(160))<br />
 SMS text in &quot;human readable&quot; form <code>ID</code> (integer unsigned)<br />
 SMS ID <code>SenderID</code> (text)</dl>
<h3>Injecting a message using SQL</h3>
<p>which SMSD instance sent this one sequence <code>SequencePosition</code> (integer)<br />
 SMS number in SMS sequence <code>TPMR</code> (integer)<br />
 Message Reference like in GSM specs <code>RelativeValidity</code> (integer)<br />
 SMS relative validity like encoded using GSM specs <code>CreatorID</code> (text)<br />
 copied from CreatorID from outbox table, matches PhoneID</p>
<dl>
<dt><code>pbk</code></p>
<dd>Not used by SMSD currently, included only for application usage.</p>
<dt><code>pbk_groups</code></p>
<dd>Not used by SMSD currently, included only for application usage. </p>
<h2>History</h2>
<p>History of schema versions: </p>
<p> 10 &#8211; DeliveryDateTime is now NULL when message is not delivered, added several indexes </p>
<p> 9 &#8211; added sent/received counters to phones table </p>
<p> 8 &#8211; introduced phones table </p>
<p> 7 &#8211; added CreatorID to tables (it holds PhoneID if set)</p>
<h2>Example</h2>
<h3>Creating tables</h3>
<p>SQL scripts to create all needed tables for most databases are included in Gammu documentation (docs/sql). As well as some PHP scripts interacting with the database. For example to create SQLite tables, issue following command:<br />
&nbsp;<wbr><br />
&nbsp;<wbr>sqlite3 smsd.db&nbsp;<wbr>&lt;&nbsp;<wbr>docs/sql/sqlite.sql</p>
<h3>Injecting a message using SQL</h3>
<p>To send a message, you can either use <a href="/docs/linux/man/1-gammu-smsd-inject/">gammu-smsd-inject</a>(1), which does all the magic for you, or you can insert the message manually. The simplest example is short text message: </p>
<pre><code>INSERT INTO outbox (
DestinationNumber,
TextDecoded,
CreatorID,
Coding

) VALUES (
'800123465',
'This is a SQL test message',
'Program',
'Default_No_Compression'

);</code></pre>
<h3>Injecting long message using SQL</h3>
<p>Inserting multipart messages is a bit more tricky, you need to construct also UDH header. For example long text message would look like (please note that each UDH needs to contain number of parts and sequence position as last two bytes, the D3 value in example is message reference number, it can be anything):<br />
&nbsp;<wbr>INSERT INTO outbox&nbsp;<wbr>(<br />
&nbsp;<wbr>&nbsp;<wbr>CreatorID,<br />
&nbsp;<wbr>&nbsp;<wbr>MultiPart,<br />
&nbsp;<wbr>&nbsp;<wbr>DestinationNumber,<br />
&nbsp;<wbr>&nbsp;<wbr>UDH,<br />
&nbsp;<wbr>&nbsp;<wbr>TextDecoded,<br />
&nbsp;<wbr>&nbsp;<wbr>Coding<br />
&nbsp;<wbr>)&nbsp;<wbr>VALUES&nbsp;<wbr>(<br />
&nbsp;<wbr>&nbsp;<wbr>&#8216;Gammu 1.23.91&#8217;,<br />
&nbsp;<wbr>&nbsp;<wbr>&#8216;true&#8217;,<br />
&nbsp;<wbr>&nbsp;<wbr>&#8216;123465&#8217;,<br />
&nbsp;<wbr>&nbsp;<wbr>&#8216;050003D30201&#8217;,<br />
&nbsp;<wbr>&nbsp;<wbr>&#8216;Mqukqirip ya konej eqniu rejropocejor hugiygydewl tfej nrupxujob xuemymiyliralj. Te tvyjuh qaxumur ibewfoiws zuucoz tdygu gelum L ejqigqesykl kya jdytbez&#8217;,<br />
&nbsp;<wbr>&nbsp;<wbr>&#8216;Default_No_Compression&#8217;<br />
&nbsp;<wbr>)<br />
&nbsp;<wbr>INSERT INTO outbox_multipart&nbsp;<wbr>(<br />
&nbsp;<wbr>&nbsp;<wbr>SequencePosition,<br />
&nbsp;<wbr>&nbsp;<wbr>UDH,<br />
&nbsp;<wbr>&nbsp;<wbr>Class,<br />
&nbsp;<wbr>&nbsp;<wbr>TextDecoded,<br />
&nbsp;<wbr>&nbsp;<wbr>ID,<br />
&nbsp;<wbr>&nbsp;<wbr>Coding<br />
&nbsp;<wbr>)&nbsp;<wbr>VALUES&nbsp;<wbr>(<br />
&nbsp;<wbr>&nbsp;<wbr>2,<br />
&nbsp;<wbr>&nbsp;<wbr>&#8216;050003D30202&#8217;,<br />
&nbsp;<wbr>&nbsp;<wbr>&#8216;u xewz qisubevumxyzk ufuylehyzc. Nse xobq dfolizygqysj t bvowsyhyhyemim ovutpapeaempye giuuwbib.&#8217;,&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&lt;ID_OF_INSERTED_RECORD_IN_OUBOX_TABLE&gt;,<br />
&nbsp;<wbr>&nbsp;<wbr>&#8216;Default_No_Compression&#8217;<br />
&nbsp;<wbr>) </p>
<h2>See Also</h2>
<p>Database backends: <a href="/docs/linux/man/7-gammu-smsd-mysql/">gammu-smsd-mysql</a>(7), <a href="/docs/linux/man/7-gammu-smsd-pgsql/">gammu-smsd-pgsql</a>(7), <a href="/docs/linux/man/7-gammu-smsd-dbi/">gammu-smsd-dbi</a>(7) </p>
<p> <a href="/docs/linux/man/1-gammu-smsd/">gammu-smsd</a>(1), <a href="/docs/linux/man/5-gammu-smsdrc/">gammu-smsdrc</a>(5), <a href="/docs/linux/man/1-gammu/">gammu</a>(1), <a href="/docs/linux/man/5-gammurc/">gammurc</a>(5)</p>
<h2>Author</h2>
<p>gammu-smsd and this manual page were written by Michal Cihar &lt;michal [at] cihar.com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009 Michal Cihar and other authors. License GPLv2: GNU GPL version 2 &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">http://www.gnu.org/licenses/old-licenses/gpl-2.0.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>Reporting Bugs</h2>
<p>Please report bugs to &lt;<a rel="nofollow" href="http://bugs.cihar.com">http://bugs.cihar.com</a>&gt;.</p>
