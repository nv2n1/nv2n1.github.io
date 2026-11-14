---
title: "gammu-smsd-files(7)"
name: "gammu-smsd-files"
section: "7"
letter: "g"
url: "/docs/linux/man/7-gammu-smsd-files/"
description: "gammu-smsd-files – gammu-smsd(1) backend using filesystem as a message storage"
---

<p>gammu-smsd-files &#8211; <a href="/docs/linux/man/1-gammu-smsd/">gammu-smsd</a>(1) backend using filesystem as a message storage </p>
<h2>Description</h2>
<p><a href="/docs/linux/man/1-gammu-smsd/">gammu-smsd</a>(1) supports several backends. Actual backend is chosen in a config file <a href="/docs/linux/man/5-gammu-smsdrc/">gammu-smsdrc</a>(5). FILES backend stores all data on a filesystem in folders defined by configuration (see <a href="/docs/linux/man/5-gammu-smsdrc/">gammu-smsdrc</a>(5) for description of configuration options).</p>
<h3>Limitation</h3>
<p>FILES backend does not support <a href="/docs/linux/man/1-gammu-smsd-inject/">gammu-smsd-inject</a>(1) program. This support might be eventually added in future versions.</p>
<h3>Receiving of messages</h3>
<p>Received messages are stored in a folder defined by configuration. The filename will be IN&lt;date&gt;_&lt;time&gt;_&lt;serialno&gt;_&lt;phone_number&gt;_&lt;sequence&gt;.&lt;ext&gt;, for example NN20021130_021531_00_+45409000931640979_00.txt. Explanation of fields: <code>&lt;date&gt;</code> &#8211; date in format YYYYMMDD<br />
 <code>&lt;time&gt;</code> &#8211; time in format HHMMSS<br />
 <code>&lt;serialno&gt;</code> &#8211; order of a message (in case more messages were received at same time), in format NN<br />
 <code>&lt;sequence&gt;</code> &#8211; part of the message for multipart messages, in format NN<br />
 <code>&lt;ext&gt;</code> &#8211; txt for text message, 8-bit messages are stored with bin extension</p>
<h3>Transmitting of messages</h3>
<p>Transmitted messages are read from a folder defined by configuration. The filename should be one of the following formats: &#8211; OUT&lt;phone_number&gt;.&lt;ext&gt;&lt;options&gt;<br />
 &#8211; OUT&lt;priority&gt;_&lt;phone_number&gt;_&lt;serialno&gt;.&lt;ext&gt;&lt;options&gt;<br />
 &#8211; OUT&lt;priority&gt;&lt;date&gt;_&lt;time&gt;_&lt;serialno&gt;_&lt;phone_number&gt;_&lt;anything&gt;.&lt;ext&gt;&lt;options&gt; Explanation of fields: <code>&lt;priority&gt;</code> &#8211; an alphabetic character (A-Z) A = highest priority<br />
 <code>&lt;ext&gt;</code> &#8211; txt for normal text SMS<br />
 <code>&lt;options&gt;</code> &#8211; Options appended to the extension applying to text SMS:<br />
&nbsp;<wbr><code>d</code>&nbsp;<wbr>&#8211; delivery report requested<br />
&nbsp;<wbr><code>f</code>&nbsp;<wbr>&#8211; flash SMS<br />
&nbsp;<wbr><code>b</code>&nbsp;<wbr>&#8211; WAP bookmark as name,URL For example OUTG20040620_193810_123_+4512345678_xpq.txtdf is a flash text SMS requesting delivery reports. Other fields are same as for received messages. SMSes will be transmitted sequentially based on the file name. The contents of the file is the SMS to be transmitted (in Unicode or standard character set). The contents of the file is the SMS to be transmitted (in Unicode or standard character set), for WAP bookmarks it is split on as Name,URL, for text messages whole file content is used. Please note that if file is not in Unicode, encoding is detected based on locales, which do not have to be configured if SMSD is running from init script. If this is your case, please add locales definition to init script. </p>
<h2>Example</h2>
<p>Example of the &#8216;detail&#8217; inbox format:  </p>
<pre>[SMSBackup000]
#ABCDEFGHIJKLMNOPQRSTUVWXYZ
#
SMSC = &quot;+4540590000&quot;
SMSCUnicode = 002B0034003500340030003500390030003000300030
Sent = 20021201T025023
State = UnRead
Number = &quot;+4522706947&quot;
NumberUnicode = 002B0034003500320032003700300036003900340037
Name = &quot;&quot;
NameUnicode =
Text00 = 004100420043004400450046004700480049004A004B004C004D004E004F0050005100520053005400550056005700580059005A000A
Coding = Default
Folder = 1
Length = 27
Class = -1
ReplySMSC = False
RejectDuplicates = True
ReplaceMessage = 0
MessageReference = 0</pre>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-gammu-smsd/">gammu-smsd</a>(1), <a href="/docs/linux/man/5-gammu-smsdrc/">gammu-smsdrc</a>(5), <a href="/docs/linux/man/1-gammu/">gammu</a>(1), <a href="/docs/linux/man/5-gammurc/">gammurc</a>(5)</p>
<h2>Author</h2>
<p>gammu-smsd and this manual page were written by Michal Cihar &lt;michal [at] cihar.com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009 Michal Cihar and other authors. License GPLv2: GNU GPL version 2 &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">http://www.gnu.org/licenses/old-licenses/gpl-2.0.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>Reporting Bugs</h2>
<p>Please report bugs to &lt;<a rel="nofollow" href="http://bugs.cihar.com">http://bugs.cihar.com</a>&gt;.</p>
