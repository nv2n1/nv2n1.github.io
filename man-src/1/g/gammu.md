---
title: "gammu(1)"
name: "gammu"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gammu/"
description: "Gammu – Does some neat things with your cellular phone or modem."
---

<h2 class="name">NAME</h2>
<p> Gammu &#8211; Does some neat things with your cellular phone or modem.</p>
<h2>SYNOPSIS</h2>
<p> Usage: gammu [<i>parameters</i>] &lt;command&gt; [<i>options</i>] </p>
<h2>DESCRIPTION</h2>
<p> This program is a tool for mobile phones. Many vendors and phones are supported, for actual listing see &lt;<a rel="nofollow" href="http://cihar.com/gammu/phonedb/">http://cihar.com/gammu/phonedb/</a>&gt;. </p>
<h2>OPTIONS</h2>
<p> Parameters before command configure gammu behaviour:<br />
 -c / &#8211;config &lt;filename&gt; &#8230; name of configuration file<br />
 -s / &#8211;section &lt;confign&gt; &#8230; section of config file to use, eg. 42<br />
 -d / &#8211;debug &lt;level&gt; &#8230; debug level (see <a href="/docs/linux/man/5-gammurc/">gammurc</a>(5) for possible values)<br />
 -f / &#8211;debug-file &lt;filename&gt; &#8230; file for logging debug messages </p>
<h3>Commands</h3>
<p> Commands can be specified with or without leading &#8211;. </p>
<h3>Calls</h3>
<dl>
<dt><code>answercall</code><i> [ID]</i></p>
<dd> Answer incoming call. </p>
<dt><code>cancelcall</code><i> [ID]</i></p>
<dd> Cancel incoming call </p>
<dt><code>canceldiverts</code></p>
<dd>
<dt><code>conferencecall</code><i> ID</i></p>
<dd>
<dt><code>dialvoice</code><i> number [show|hide]</i></p>
<dd> Make voice call from SIM card line set in phone. </p>
<dt><code>divert</code><i> get|set all|busy|noans|outofreach all|voice|fax|data [number timeout]</i></p>
<dd>
<dt><code>getspeeddial</code><i> start [stop]</i></p>
<dd>
<dt><code>getussd</code><i> code</i></p>
<dd>
<dt><code>holdcall</code><i> ID</i></p>
<dd>
<dt><code>maketerminatedcall</code><i> number length [show|hide]</i></p>
<dd> Make voice call from SIM card line set in phone which will be terminated after <code>length</code> seconds. </p>
<dt><code>monitor</code><i> [times]</i></p>
<dd> Get phone status and writes continuously to standard output. Press Ctrl+C to break this state. </p>
<dt><code>senddtmf</code><i> sequence</i></p>
<dd> Plays DTMF sequence. In some phones available only during calls </p>
<dt><code>splitcall</code><i> ID</i></p>
<dd>
<dt><code>switchcall</code><i> [ID]</i></p>
<dd>
<dt><code>transfercall</code><i> [ID]</i></p>
<dd>
<dt><code>unholdcall</code><i> ID</i></p>
<dd>
</dl>
<h3>SMS and EMS</h3>
<p> Sending messages might look a bit complicated on first attempt to use. But be patient, the command line has been written in order to allow almost every usage. See EXAMPLE section for some hints on usage. </p>
<dl>
<dt><code>addsms</code><i> folder file [-yes]</i></p>
<dd> Adds SMSes from file (format like backupsms uses) to selected folder in phone.</p>
<dt><code>addsmsfolder</code><i> name</i></p>
<dd>
<dt><code>backupsms</code><i> file [-yes|-all]</i></p>
<dd> Stores all SMSes from phone to file. </p>
<p> Use -yes for answering yes to all questions (backup all messages and delete them from phone), or -all to just backup all folders while keeping messages in phone. </p>
<dt><code>deleteallsms</code><i> folder</i></p>
<dd> Delete all SMS from specified SMS folder. </p>
<dt><code>deletesms</code><i> folder start [stop]</i></p>
<dd> Delete SMS from phone. See description for <code>getsms</code> for info about sms folders naming convention. </p>
<p> Locations are numerated from 1. </p>
<dt><code>displaysms</code><i> &#8230; (options like in sendsms)</i></p>
<dd>
<p> Displays PDU data of encoded SMS messages. It accepts same parameters and behaves same like sendsms. </p>
<dt><code>getallsms</code><i> -pbk</i></p>
<dd> Get all SMS from phone. In some phones you will have also SMS templates and info about locations used to save Picture Images. With each sms you will see location. If you want to get such sms from phone alone, use <code>gammu getsms 0 location</code> </p>
<dt><code>geteachsms</code><i> -pbk</i></p>
<dd> Similiary to <code>getallsms</code>. Difference is, that links all contacenated sms </p>
<dt><code>getsms</code><i> folder start [stop]</i></p>
<dd> Get SMS. </p>
<p> Locations are numerated from 1. </p>
<p> When give folder 0, sms is given from &quot;flat&quot; memory (all sms from all folders have unique numbers). It&#8217;s sometimes emulated by Gammu. You can use it with all phones. </p>
<p> When give folder 1, 2, etc. sms are taken from Inbox, Outbox, etc. and each sms has unique number in his folder. Name of folders can depend on your phone (the most often 1=&quot;Inbox&quot;, 2=&quot;Outbox&quot;, etc.). This method is not supported by all phones (for example, not supported by Nokia 3310, 5110, 6110). If work with your phone, use <code>getsmsfolders</code> to get folders list. </p>
<dt><code>getsmsc</code><i> [start [stop]]</i></p>
<dd> Get SMSC settings from SIM card. </p>
<p> Locations are numerated from 1. </p>
<dt><code>getsmsfolders</code></p>
<dd> Get names for SMS folders in phone </p>
<dt><code>nokiagett9</code></p>
<dd>
<dt><code>restoresms</code><i> file [-yes]</i></p>
<dd> Restores SMSes from file (format like backupsms uses) to selected folder in phone. Please note that this overwrites existing messages in phone (if it supports it).</p>
<dt><code>savesms</code><i> VCARD10|VCARD21 file SM|ME location [-nokia] [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd> Read phonebook entry from file created by <code>backup</code> option and saves in VCARD 1.0 (only name and default number) or VCARD 2.1 (all entry details with all numbers, text and name) format as SMS </p>
<dt><code>savesms ANIMATION</code><i> frames file1 file2&#8230; [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
<dt><code>savesms BOOKMARK</code><i> file location [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd> Read WAP bookmark from file created by <code>backup</code> option and saves in Nokia format as SMS </p>
<dt><code>savesms CALENDAR</code><i> file location [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd> Read calendar note from file created by <code>backup</code> option and saves in VCALENDAR 1.0 format as SMS </p>
<dt><code>savesms CALLER</code><i> file [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd> Save caller logo as sms (Nokia format &#8211; size 72&#215;14). </p>
<dt><code>savesms EMS</code><i> [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num] [-unicode] [-16bit] [-format lcrasbiut] [-text text] [-unicodefiletext file] [-defsound ID] [-defanimation ID] [-tone10 file] [-tone10long file] [-tone12 file] [-tone12long file] [-toneSE file] [-toneSElong file] [-fixedbitmap file] [-variablebitmap file] [-variablebitmaplong file] [-animation frames file1 &#8230;] [-protected number]</i></p>
<dd>
<p> Saves EMS sequence. All parameters after <code>-unread</code> (like <code>-defsound</code>) can be used few times. </p>
<p> <code>-text</code> &#8211; adds text </p>
<p> <code>-unicodefiletext</code> &#8211; adds text from Unicode file </p>
<p> <code>-defanimation</code> &#8211; adds default animation with ID specified by user.ID for different phones are different. </p>
<p> <code>-animation</code> &#8211; adds &quot;frames&quot; frames read from file1, file2, etc. </p>
<p> <code>-defsound</code> &#8211; adds default sound with ID specified by user. ID for different phones are different. </p>
<p> <code>-tone10</code> &#8211; adds IMelody version 1.0 read from RTTL or other compatible file </p>
<p> <code>-tone10long</code> &#8211; IMelody version 1.0 saved in one of few SMS with UPI. Phones compatible with UPI (like SonyEricsson phones) will read such ringtone as one </p>
<p> <code>-tone12</code> &#8211; adds IMelody version 1.2 read from RTTL or other compatible file </p>
<p> <code>-tone12long</code> &#8211; IMelody version 1.0 saved in one of few SMS with UPI. Phones compatible with UPI (like SonyEricsson phones) will read such ringtone as one </p>
<p> <code>-toneSE</code> &#8211; adds IMelody in &quot;short&quot; form supported by SonyEricsson phones </p>
<p> <code>-tone10long</code> &#8211; SonyEricsson IMelody saved in one or few SMS with UPI </p>
<p> <code>-variablebitmap</code> &#8211; bitmap in any size saved in one SMS </p>
<p> <code>-variablebitmaplong</code> &#8211; bitmap with maximal size 96&#215;128 saved in one or few sms </p>
<p> <code>-fixedbitmap </code> &#8211; bitmap 16&#215;16 or 32&#215;32 </p>
<p> <code>-protected</code> &#8211; all ringtones and bitmaps after this parameter (excluding default ringtones and logos) will be &quot;protected&quot; (in phones compatible with ODI like SonyEricsson products it won&#8217;t be possible to forward them from phone menu) </p>
<p> <i>Example:</i> gammu savesms EMS -text &quot;Greetings&quot; -defsound 1 -text &quot;from Gammu&quot; -tone10 axelf.txt -animation 2 file1.bmp file2.bmp </p>
<p> will create EMS sequence with text &quot;Greetings&quot; and default sound 1 and text &quot;from Gammu&quot; and ringtone axelf.txt and 2 frame animation read from (1&#8217;st frame) file1.bmp and (2&#8217;nd frame) file2.bmp </p>
<p> <i>Example:</i> gammu savesms EMS -protected 2 -variablebitmaplong ala.bmp -toneSElong axelf.txt -toneSE ring.txt </p>
<p> ala.bmp and axelf.txt will be &quot;protected&quot; </p>
<dt><code>savesms MMSINDICATOR</code><i> URL Title Sender [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
<dt><code>savesms MMSSETTINGS</code><i> file location [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
<dt><code>savesms OPERATOR</code><i> file [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num] [-netcode netcode] [-biglogo]</i></p>
<dd> Save operator logo as sms (Nokia format &#8211; size 72&#215;14 or 78&#215;21 after using <code>-biglogo</code>). </p>
<dt><code>savesms PICTURE</code><i> file [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num] [-text text] [-unicode] [-alcatelbmmi]</i></p>
<dd> Save Picture Image as sms (Nokia format &#8211; size 72&#215;28). </p>
<dt><code>savesms PROFILE</code><i> [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num] [-name name] [-bitmap bitmap] [-ringtone ringtone]</i></p>
<dd> Read ringtone (RTTL) format and bitmap (Picture Image size) and name and save as Nokia profile. </p>
<dt><code>savesms RINGTONE</code><i> file [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num] [-long] [-scale]</i></p>
<dd> Read RTTL ringtone from file and save as SMS into SIM/phone memory. Ringtone is saved in Nokia format. </p>
<p> <code>-folder number</code> &#8211; save to specified folder. </p>
<p> Folders are numerated from 1. </p>
<p> The most often folder 1 = &quot;Inbox&quot;, 2 = &quot;Outbox&quot;, etc. </p>
<p> <code>-unread</code> &#8211; makes message unread. In some phones (like 6210) you won&#8217;t see unread sms envelope after saving such sms. In some phones with internal SMS memory (like 6210) after using it with folder 1 SIM SMS memory will be used </p>
<p> <code>-read</code> &#8211; makes message read. In some phones with internal SMS memory (like 6210) after using it with folder 1 SIM SMS memory will be used <code>-unsent</code> &#8211; makes message unsent </p>
<p> <code>-reply</code> &#8211; reply SMSC is set </p>
<p> <code>-sender number</code> &#8211; set sender number </p>
<p> <code>-flash</code> &#8211; Class 0 SMS </p>
<p> <code>-smscset number</code> &#8211; SMSC will be taken from set <code>number</code>. Default set: 1 </p>
<p> <code>-smscnumber number</code> &#8211; SMSC number </p>
<p> <code>-long</code> &#8211; ringtone is saved using Profile style. It can be longer (and saved in 2 SMS), but decoded only by newer phones (like 33xx) </p>
<p> <code>-scale</code> &#8211; ringtone will have Scale info for each note. It will allow to edit it correctly later in phone composer (for example, in 33xx) </p>
<dt><code>savesms SMSTEMPLATE</code><i> [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num] [-unicode] [-text text] [-unicodefiletext file] [-defsound ID] [-defanimation ID] [-tone10 file] [-tone10long file] [-tone12 file] [-tone12long file] [-toneSE file] [-toneSElong file] [-variablebitmap file] [-variablebitmaplong file] [-animation frames file1 &#8230;]</i></p>
<dd>
<dt><code>savesms TEXT</code><i> [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num] [-inputunicode] [-16bit] [-flash] [-len len] [-autolen len] [-unicode] [-enablevoice] [-disablevoice] [-enablefax] [-disablefax] [-enableemail] [-disableemail] [-voidsms] [-replacemessages ID] [-replacefile file] [-text msgtext] [-textutf8 msgtext]</i></p>
<dd> Take text from stdin (or commandline if -text specified) and save as text SMS into SIM/phone memory. </p>
<p> <code>-folder number</code> &#8211; save to specified folder. </p>
<p> Folders are numerated from 1. </p>
<p> The most often folder 1 = &quot;Inbox&quot;, 2 = &quot;Outbox&quot;,etc. Use <code>getsmsfolders</code> to get folder list. </p>
<p> <code>-unread</code> &#8211; makes message unread. In some phones (like 6210) you won&#8217;t see unread sms envelope after saving such sms. In some phones with internal SMS memory (like 6210) after using it with folder 1 SIM SMS memory will be used </p>
<p> <code>-read</code> &#8211; makes message read. In some phones with internal SMS memory (like 6210) after using it with folder 1 SIM SMS memory will be used </p>
<p> <code>-unsent</code> &#8211; makes message unsent </p>
<p> <code>-reply</code> &#8211; reply SMSC is set </p>
<p> <code>-sender number</code> &#8211; set sender number (default: &quot;Gammu&quot;) </p>
<p> <code>-flash</code> &#8211; Class 0 SMS </p>
<p> <code>-smscset number</code> &#8211; SMSC will be taken from set <code>number</code>. Default set: 1 </p>
<p> <code>-smscnumber number</code> &#8211; SMSC number </p>
<p> <code>-len len</code> &#8211; specify, how many chars will be read. When use this option and text will be longer than 1 SMS, will be splitted into more linked SMS </p>
<p> <code>-autolen len</code> &#8211; specify, how many chars will be read. When use this option and text will be longer than 1 SMS, will be splitted into more linked SMS.Coding type (SMS default alphabet/Unicode) is set according to input text </p>
<p> <code>-enablevoice</code> | <code>-disablevoice</code> | <code>-enablefax </code> | <code>-disablefax </code> | <code>-enableemail </code> | <code>-disableemail </code> &#8211; sms will set such indicators. Text will be cut to 1 sms. </p>
<p> <code>-voidsms</code> &#8211; many phones after receiving it won&#8217;t display anything, only beep, vibrate or turn on light. Text will be cut to 1 sms. </p>
<p> <code>-unicode</code> &#8211; SMS will be saved in Unicode format </p>
<p> <code>-inputunicode</code> &#8211; input text is in Unicode. </p>
<p> <code>-text</code> &#8211; get text from command line instead of stdin. </p>
<p> <code>-textutf8</code> &#8211; get text in UTF-8 from command line instead of stdin. </p>
<p> <i>TIP:</i> You can create Unicode file using WordPad in Win32 (during saving select &quot;Unicode Text Document&quot; format). In Unix can use for example YUdit. </p>
<p> <code>-replacemessages ID</code> &#8211; <code>ID</code> can be 1..7. When you will use option and send more single SMS to one recipient with the same ID, each another SMS will replace each previous with the same ID </p>
<p> <code>-replacefile file</code> &#8211; when you want, you can make file in such format: <code>src_unicode_char1, dest_unicode_char1, src_unicode_char2, dest_unicode_char2</code> (everything in one line). After reading text for SMS from stdin there will be made translation and each src char will be converted to dest char. In docs there is example file (<i>replace.txt</i>), which will change all &quot;a&quot; chars to &quot;1&quot; </p>
<p> <i>TIP:</i> when use ~ char in sms text and <code>-unicode</code> option (Unicode coding required), text of sms after ~ char will blink in some phones (like N33xx) </p>
<p> <i>Example:</i> echo some_text | gammu savesms TEXT </p>
<dt><code>savesms TODO</code><i> file location [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
<dt><code>savesms WAPINDICATOR</code><i> URL Title [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
<dt><code>savesms WAPSETTINGS</code><i> file location DATA|GPRS [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd> Read WAP settings from file created by <code>backup</code> option and saves in Nokia format as SMS </p>
<dt><code>sendsms</code><i> VCARD10|VCARD21 destination file SM|ME location [-nokia] [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
<dt><code>sendsms ANIMATION</code><i> destination frames file1 file2&#8230; [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
<dt><code>sendsms BOOKMARK</code><i> destination file location [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
<dt><code>sendsms CALENDAR</code><i> destination file location [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
<dt><code>sendsms CALLER</code><i> destination file [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
<dt><code>sendsms EMS</code><i> destination [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num] [-unicode] [-16bit] [-format lcrasbiut] [-text text] [-unicodefiletext file] [-defsound ID] [-defanimation ID] [-tone10 file] [-tone10long file] [-tone12 file] [-tone12long file] [-toneSE file] [-toneSElong file] [-fixedbitmap file] [-variablebitmap file] [-variablebitmaplong file] [-animation frames file1 &#8230;] [-protected number]</i></p>
<dd>
<dt><code>sendsms MMSINDICATOR</code><i> destination URL Title Sender [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
<p> Sends a message with MMS indication. The recipient phone will then download MMS from given URL and display it. </p>
<p> Please note that you should provide valid smil data on that URL. </p>
<dt><code>sendsms MMSSETTINGS</code><i> destination file location [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
<dt><code>sendsms OPERATOR</code><i> destination file [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num] [-netcode netcode] [-biglogo]</i></p>
<dd>
<dt><code>sendsms PICTURE</code><i> destination file [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num] [-text text] [-unicode] [-alcatelbmmi]</i></p>
<dd>
<dt><code>sendsms PROFILE</code><i> destination [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num] [-name name] [-bitmap bitmap] [-ringtone ringtone]</i></p>
<dd>
<dt><code>sendsms RINGTONE</code><i> destination file [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num] [-long] [-scale]</i></p>
<dd>
<dt><code>sendsms SMSTEMPLATE</code><i> destination [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num] [-unicode] [-text text] [-unicodefiletext file] [-defsound ID] [-defanimation ID] [-tone10 file] [-tone10long file] [-tone12 file] [-tone12long file] [-toneSE file] [-toneSElong file] [-variablebitmap file] [-variablebitmaplong file] [-animation frames file1 &#8230;]</i></p>
<dd>
<dt><code>sendsms TEXT</code><i> destination [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num] [-inputunicode] [-16bit] [-flash] [-len len] [-autolen len] [-unicode] [-enablevoice] [-disablevoice] [-enablefax] [-disablefax] [-enableemail] [-disableemail] [-voidsms] [-replacemessages ID] [-replacefile file] [-text msgtext] [-textutf8 msgtext]</i></p>
<dd>
<dt><code>sendsms TODO</code><i> destination file location [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
<dt><code>sendsms WAPINDICATOR</code><i> destination URL Title [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
<dt><code>sendsms WAPSETTINGS</code><i> destination file location DATA|GPRS [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
</dl>
<h3>Memory (phonebooks and calls)</h3>
<dl>
<dt><code>addcategory</code><i> TODO|PHONEBOOK text</i></p>
<dd>
<dt><code>addnew</code><i> file [-yes]</i></p>
<dd> Adds data written in file created using <code>backup option</code>. All things backup&#8217;ed by <code>backup</code> can be restored (when made backup to Gammu text file). </p>
<p> Please note that this adds all content of backup file to phone and does not care about current data in the phone (no duplicates are detected). </p>
<dt><code>backup</code><i> file [-yes]</i></p>
<dd> Backup your phone to file. It&#8217;s possible to backup (depends on phone and backup format): </p>
<p> * phonebook from SIM and phone memory<br />
 * calendar notes<br />
 * SMSC settings<br />
 * operator logo<br />
 * startup (static) logo or startup text<br />
 * WAP bookmarks<br />
 * WAP settings<br />
 * caller logos and groups<br />
 * user ringtones </p>
<p> There are various backup formats supported and the backup format is guessed based on file extension: </p>
<p> * .lmb &#8211; Nokia backup, supports contacts, caller logos and startup logo.<br />
 * .vcs &#8211; vCalendar, supports calendar and todo.<br />
 * .vcf &#8211; vCard, supports contacts.<br />
 * .ldif &#8211; LDAP import, supports contacts.<br />
 * .ics &#8211; iCalendar, supports calendar and todo.<br />
 * Any other extension is Gammu backup file and it supports all data mentioned above. </p>
<p> <i>TIP:</i> if you will backup settings to Gammu text file, it will be possible to edit it. It&#8217;s easy: many things in this file will be written double &#8211; once in Unicode, once in ASCII. When you will remove Unicode version Gammu will use ASCII on <code>restore</code> (and you can easy edit ASCII text) and will convert it according to your OS locale. When will be available Unicode version of text, it will be used instead of ASCII (usefull with Unicode phones &#8211; it isn&#8217;t important, what locale is set in computer and no conversion Unicode -&gt; ASCII and ASCII -&gt; Unicode is done). </p>
<p> <i>TIP:</i> you can use any editor with regular expressions function to edit backup text file. Example: TextPad 4.2.2 from <a rel="nofollow" href="http://www.textpad.com/">http://www.textpad.com/</a> with regular expressions based on POSIX standard P1003.2 is OK for it. Few examples for it: </p>
<p> * to remove info about voice tags:<br />
 FROM: ^Entry\([0-9][0-9]\)VoiceTag = \(.*\)
<br />
 TO: </p>
<p> * to change all numbers starting from +3620, +3630, +3660, +3670 to +3620<br />
 Find: Type = NumberGeneral
Entry\([0-9][0-9]\)Text = &quot;\+36\(20\|30\|60\|70\)<br />
 Repl: Type = NumberMobile
Entry\1Text = &quot;\+3620 </p>
<p> * to change phone numbers type to mobile for numbers starting from +3620, +3630,&#8230; and removing the corresponding TextUnicode line<br />
 F: Type = NumberGeneral
Entry\([0-9][0-9]\)Text = &quot;\+36\([2367]0\)\([^\&quot;]*\)&quot;
Entry\([0-9][0-9]\)TextUnicode = \([^
]*\)
<br />
 R: Type = NumberMobile
Entry\1Text = &quot;\+36\2\3&quot;
 </p>
<dt><code>clearall</code></p>
<dd>
<dt><code>deleteallmemory</code><i> DC|MC|RC|ON|VM|SM|ME|MT|FD|SL</i></p>
<dd> Deletes all entries from specified memory type.</p>
<dt><code>deletememory</code><i> DC|MC|RC|ON|VM|SM|ME|MT|FD|SL start [stop]</i></p>
<dd> Deletes entries in specified range from specified memory type.</p>
<dt><code>getallcategory</code><i> TODO|PHONEBOOK</i></p>
<dd>
<dt><code>getallmemory</code><i> DC|MC|RC|ON|VM|SM|ME|MT|FD|SL</i></p>
<dd>
<dt><code>getcategory</code><i> TODO|PHONEBOOK start [stop]</i></p>
<dd>
<dt><code>getmemory</code><i> DC|MC|RC|ON|VM|SM|ME|MT|FD|SL start [stop [-nonempty]]</i></p>
<dd> Get memory location from phone. </p>
<p> Locations are numerated from 1. </p>
<p> <code>DC</code> = Dialled calls<br />
 <code>MC</code> = Missed calls<br />
 <code>RC</code> = Received calls<br />
 <code>ON</code> = Own numbers<br />
 <code>VM</code> = voice mailbox<br />
 <code>SM</code> = SIM phonebook<br />
 <code>ME</code> = phone internal phonebook<br />
 <code>FD</code> = fixed dialling<br />
 <code>SL</code> = sent SMS log </p>
<dt><code>getspeeddial</code><i> start [stop]</i></p>
<dd>
<dt><code>listmemorycategory</code><i> text|number</i></p>
<dd>
<dt><code>nokiagetpbkfeatures</code><i> memorytype</i></p>
<dd>
<dt><code>restore</code><i> file [-yes]</i></p>
<dd> Restore settings written in file created using <code>backup</code> option. </p>
<p> Please note that restoring deletes all current content in phone. If you want only to add entries to phone, use addnew. </p>
<p> In some phones restoring calendar notes will not show error, but won&#8217;t be done, when phone doesn&#8217;t have set clock inside. </p>
<dt><code>savefile</code><i> VCARD10|VCARD21 target.vcf file SM|ME location</i></p>
<dd>
<dt><code>savesms</code><i> VCARD10|VCARD21 file SM|ME location [-nokia] [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd> Read phonebook entry from file created by <code>backup</code> option and saves in VCARD 1.0 (only name and default number) or VCARD 2.1 (all entry details with all numbers, text and name) format as SMS </p>
<dt><code>searchmemory</code><i> text</i></p>
<dd>
<dt><code>sendsms</code><i> VCARD10|VCARD21 destination file SM|ME location [-nokia] [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
</dl>
<h3>Filesystem</h3>
<dl>
<dt><code>addfile</code><i> folderID name [-type JAR|BMP|PNG|GIF|JPG|MIDI|WBMP|AMR|3GP|NRT] [-readonly] [-protected] [-system] [-hidden] [-newtime]</i></p>
<dd> Add file with specified name to folder with specified folder ID. </p>
<p> <code>-type </code> &#8211; file type was required for filesystem 1 in Nokia phones (current filesystem 2 doesn&#8217;t need this) </p>
<p> <code>-readonly, -protected, -system, -hidden</code> &#8211; you can set readonly, protected (file can&#8217;t be for example forwarded from phone menu), system and hidden (file is hidden from phone menu) file attributes </p>
<p> <code>-newtime </code> &#8211; after using it date/time of file modification will be set to moment of uploading </p>
<dt><code>addfolder</code><i> parentfolderID name</i></p>
<dd>
<dt><code>deletefiles</code><i> fileID</i></p>
<dd>
<dt><code>deletefolder</code><i> name</i></p>
<dd>
<dt><code>getfilefolder</code><i> ID1, ID2, &#8230;</i></p>
<dd>
<dt><code>getfiles</code><i> ID1, ID2, &#8230;</i></p>
<dd>
<dt><code>getfilesystem</code><i> [-flatall|-flat]</i></p>
<dd> Display info about all folders and files in phone memory/memory card. By default there is tree displayed, you can change it: </p>
<p> <code>-flatall</code> there are displayed full file/folder details like ID (first parameter in line) </p>
<p> <code>-flat</code> </p>
<p> Please note, that in some phones (like N6230) content of some folders (with more files) can be cut (only part of files will be displayed) for example on infrared connection. This is not Gammu issue, but phone firmware problem. </p>
<dt><code>getfilesystemstatus</code></p>
<dd>
<dt><code>getfolderlisting</code><i> folderID</i></p>
<dd>
<p> Display files and folders available in folder with given folder ID. You can get ID&#8217;s using getfilesystem -flatall. </p>
<p> Please note, that in some phones (like N6230) content of some folders (with more files) can be cut (only part of files will be displayed) for example on infrared connection. This is not Gammu issue, but phone firmware problem. </p>
<dt><code>getrootfolders</code></p>
<dd>
<p> Display info about drives available in phone/memory card. </p>
<dt><code>nokiaaddfile</code><i> Gallery|Gallery2|Camera|Tones|Tones2|Records|Video|Playlist|MemoryCard file [-name name] [-protected] [-readonly] [-system] [-hidden] [-newtime]</i></p>
<dd> Install the *.jar/*.jad file pair of a midlet in the application or game menu of the phone. You have to give the name without the jar/jad suffix, otherwise you will get the slightly confusing error message Can&#8217;t open specified file. Read only ? </p>
<p> The option <i>-overwrite</i> deletes the application&#8217;s .jad and .jar files bevor installing, but doesn&#8217;t delete the application data. Option <i>-overwriteall</i> will also delete all data. Both these options work only for Application or Game upload. </p>
<p> <i>Example:</i> gammu nokiaaddfile Application Alien will read Alien.JAD and Alien.JAR and add to Applications </p>
<p> <i>Example:</i> gammu nokiaaddfile Tones file.mid will read file.mid and add to Tones folder </p>
<p> You can use <a href="/docs/linux/man/1-jadmaker/">jadmaker</a>(1) to generate a .jad file from a .jar file. </p>
<dt><code>nokiaaddplaylists</code></p>
<dd>
<dt><code>sendfile</code><i> name</i></p>
<dd>
<dt><code>setfileattrib</code><i> folderID [-system] [-readonly] [-hidden] [-protected]</i></p>
<dd>
</dl>
<h3>Logo and pictures</h3>
<dl>
<dt><code>copybitmap</code><i> inputfile [outputfile [OPERATOR|PICTURE|STARTUP|CALLER]]</i></p>
<dd> Allow to convert logos files to another. When give ONLY inputfile, output will be written to stdout using ASCII art. When give output file and format, in some file formats (like NLM) will be set indicator informing about logo type to given. </p>
<dt><code>getbitmap</code><i> DEALER</i></p>
<dd> In some models it&#8217;s possible to save dealer welcome note &#8211; text displayed during enabling phone, which can&#8217;t be edited from phone menu. Here you can get it. </p>
<dt><code>getbitmap CALLER</code><i> location [file]</i></p>
<dd> Get caller group logo from phone. Locations 1-5. </p>
<dt><code>getbitmap OPERATOR</code><i> [file]</i></p>
<dd> Get operator logo (picture displayed instead of operator name) from phone. </p>
<dt><code>getbitmap PICTURE</code><i> location [file]</i></p>
<dd> Get Picture Image from phone. </p>
<dt><code>getbitmap STARTUP</code><i> [file]</i></p>
<dd> Get static startup logo from phone. Allow to save it in file. </p>
<dt><code>savesms ANIMATION</code><i> frames file1 file2&#8230; [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
<dt><code>savesms CALLER</code><i> file [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd> Save caller logo as sms (Nokia format &#8211; size 72&#215;14). </p>
<dt><code>savesms OPERATOR</code><i> file [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num] [-netcode netcode] [-biglogo]</i></p>
<dd> Save operator logo as sms (Nokia format &#8211; size 72&#215;14 or 78&#215;21 after using <code>-biglogo</code>). </p>
<dt><code>savesms PICTURE</code><i> file [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num] [-text text] [-unicode] [-alcatelbmmi]</i></p>
<dd> Save Picture Image as sms (Nokia format &#8211; size 72&#215;28). </p>
<dt><code>sendsms ANIMATION</code><i> destination frames file1 file2&#8230; [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
<dt><code>sendsms CALLER</code><i> destination file [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
<dt><code>sendsms OPERATOR</code><i> destination file [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num] [-netcode netcode] [-biglogo]</i></p>
<dd>
<dt><code>sendsms PICTURE</code><i> destination file [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num] [-text text] [-unicode] [-alcatelbmmi]</i></p>
<dd>
<dt><code>setbitmap CALLER</code><i> location [file]</i></p>
<dd> Set caller logo. </p>
<dt><code>setbitmap COLOUROPERATOR</code><i> [fileID [netcode]]</i></p>
<dd>
<dt><code>setbitmap COLOURSTARTUP</code><i> [fileID]</i></p>
<dd>
<dt><code>setbitmap DEALER</code><i> text</i></p>
<dd>
<dt><code>setbitmap OPERATOR</code><i> [file [netcode]]</i></p>
<dd> Set operator logo in phone. When won&#8217;t give file and netcode, operator logo will be removed from phone. When will give only filename, operator logo will be displayed for your current GSM operator. When give additionaly network code, it will be displayed for this operator: <code>gammu setbitmap OPERATOR file &quot;260 02&quot;</code> </p>
<dt><code>setbitmap PICTURE</code><i> file location [text]</i></p>
<dd>
<dt><code>setbitmap STARTUP</code><i> file|1|2|3</i></p>
<dd> Set startup logo in phone. It can be static (then you will have to give file name) or one of predefined animated (only some phones like Nokia 3310 or 3330 supports it) </p>
<dt><code>setbitmap TEXT</code><i> text</i></p>
<dd>
<dt><code>setbitmap WALLPAPER</code><i> fileID</i></p>
<dd>
</dl>
<h3>Ringtones</h3>
<dl>
<dt><code>addnew</code><i> file [-yes]</i></p>
<dd> Adds data written in file created using <code>backup option</code>. All things backup&#8217;ed by <code>backup</code> can be restored (when made backup to Gammu text file). </p>
<p> Please note that this adds all content of backup file to phone and does not care about current data in the phone (no duplicates are detected). </p>
<dt><code>backup</code><i> file [-yes]</i></p>
<dd> Backup your phone to file. It&#8217;s possible to backup (depends on phone and backup format): </p>
<p> * phonebook from SIM and phone memory<br />
 * calendar notes<br />
 * SMSC settings<br />
 * operator logo<br />
 * startup (static) logo or startup text<br />
 * WAP bookmarks<br />
 * WAP settings<br />
 * caller logos and groups<br />
 * user ringtones </p>
<p> There are various backup formats supported and the backup format is guessed based on file extension: </p>
<p> * .lmb &#8211; Nokia backup, supports contacts, caller logos and startup logo.<br />
 * .vcs &#8211; vCalendar, supports calendar and todo.<br />
 * .vcf &#8211; vCard, supports contacts.<br />
 * .ldif &#8211; LDAP import, supports contacts.<br />
 * .ics &#8211; iCalendar, supports calendar and todo.<br />
 * Any other extension is Gammu backup file and it supports all data mentioned above. </p>
<p> <i>TIP:</i> if you will backup settings to Gammu text file, it will be possible to edit it. It&#8217;s easy: many things in this file will be written double &#8211; once in Unicode, once in ASCII. When you will remove Unicode version Gammu will use ASCII on <code>restore</code> (and you can easy edit ASCII text) and will convert it according to your OS locale. When will be available Unicode version of text, it will be used instead of ASCII (usefull with Unicode phones &#8211; it isn&#8217;t important, what locale is set in computer and no conversion Unicode -&gt; ASCII and ASCII -&gt; Unicode is done). </p>
<p> <i>TIP:</i> you can use any editor with regular expressions function to edit backup text file. Example: TextPad 4.2.2 from <a rel="nofollow" href="http://www.textpad.com/">http://www.textpad.com/</a> with regular expressions based on POSIX standard P1003.2 is OK for it. Few examples for it: </p>
<p> * to remove info about voice tags:<br />
 FROM: ^Entry\([0-9][0-9]\)VoiceTag = \(.*\)
<br />
 TO: </p>
<p> * to change all numbers starting from +3620, +3630, +3660, +3670 to +3620<br />
 Find: Type = NumberGeneral
Entry\([0-9][0-9]\)Text = &quot;\+36\(20\|30\|60\|70\)<br />
 Repl: Type = NumberMobile
Entry\1Text = &quot;\+3620 </p>
<p> * to change phone numbers type to mobile for numbers starting from +3620, +3630,&#8230; and removing the corresponding TextUnicode line<br />
 F: Type = NumberGeneral
Entry\([0-9][0-9]\)Text = &quot;\+36\([2367]0\)\([^\&quot;]*\)&quot;
Entry\([0-9][0-9]\)TextUnicode = \([^
]*\)
<br />
 R: Type = NumberMobile
Entry\1Text = &quot;\+36\2\3&quot;
 </p>
<dt><code>clearall</code></p>
<dd>
<dt><code>copyringtone</code><i> source destination [RTTL|BINARY]</i></p>
<dd> Copy source ringtone to destination. </p>
<dt><code>getphoneringtone</code><i> location [file]</i></p>
<dd>
<p> Get one of &quot;default&quot; ringtones and saves into file </p>
<dt><code>getringtone</code><i> location [file]</i></p>
<dd> Get ringtone from phone in RTTL or BINARY format. </p>
<p> Locations are numerated from 1. </p>
<dt><code>getringtoneslist</code></p>
<dd>
<dt><code>nokiacomposer</code><i> file</i></p>
<dd> Show, how to enter RTTL ringtone in composer existing in many Nokia phones (and how should it look like). </p>
<dt><code>playringtone</code><i> file</i></p>
<dd> Play aproximation of ringtone over phone buzzer. File can be in RTTL or BINARY (Nokia DCT3) format. </p>
<dt><code>playsavedringtone</code><i> number</i></p>
<dd>
<p> Play one of &quot;built&quot; ringtones. This option is available for DCT4 phones. For getting ringtones list use getringtoneslist. </p>
<dt><code>restore</code><i> file [-yes]</i></p>
<dd> Restore settings written in file created using <code>backup</code> option. </p>
<p> Please note that restoring deletes all current content in phone. If you want only to add entries to phone, use addnew. </p>
<p> In some phones restoring calendar notes will not show error, but won&#8217;t be done, when phone doesn&#8217;t have set clock inside. </p>
<dt><code>savesms RINGTONE</code><i> file [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num] [-long] [-scale]</i></p>
<dd> Read RTTL ringtone from file and save as SMS into SIM/phone memory. Ringtone is saved in Nokia format. </p>
<p> <code>-folder number</code> &#8211; save to specified folder. </p>
<p> Folders are numerated from 1. </p>
<p> The most often folder 1 = &quot;Inbox&quot;, 2 = &quot;Outbox&quot;, etc. </p>
<p> <code>-unread</code> &#8211; makes message unread. In some phones (like 6210) you won&#8217;t see unread sms envelope after saving such sms. In some phones with internal SMS memory (like 6210) after using it with folder 1 SIM SMS memory will be used </p>
<p> <code>-read</code> &#8211; makes message read. In some phones with internal SMS memory (like 6210) after using it with folder 1 SIM SMS memory will be used <code>-unsent</code> &#8211; makes message unsent </p>
<p> <code>-reply</code> &#8211; reply SMSC is set </p>
<p> <code>-sender number</code> &#8211; set sender number </p>
<p> <code>-flash</code> &#8211; Class 0 SMS </p>
<p> <code>-smscset number</code> &#8211; SMSC will be taken from set <code>number</code>. Default set: 1 </p>
<p> <code>-smscnumber number</code> &#8211; SMSC number </p>
<p> <code>-long</code> &#8211; ringtone is saved using Profile style. It can be longer (and saved in 2 SMS), but decoded only by newer phones (like 33xx) </p>
<p> <code>-scale</code> &#8211; ringtone will have Scale info for each note. It will allow to edit it correctly later in phone composer (for example, in 33xx) </p>
<dt><code>sendsms RINGTONE</code><i> destination file [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num] [-long] [-scale]</i></p>
<dd>
<dt><code>setringtone</code><i> file [-location location] [-scale] [-name name]</i></p>
<dd> Set ringtone in phone. When don&#8217;t give location, it will be written &quot;with preview&quot; (in phones supporting this feature like 61xx or 6210). When use RTTL ringtones, give location and use <code>-scale</code>, there will be written scale info with each note. It will avoid scale problems available during editing ringtone in composer from phone menu (for example, in N33xx). </p>
<p> <i>TIP:</i> when use ~ char in ringtone name, in some phones (like 33xx) name will blink later in phone menus </p>
</dl>
<h3>Calendar notes</h3>
<dl>
<dt><code>addnew</code><i> file [-yes]</i></p>
<dd> Adds data written in file created using <code>backup option</code>. All things backup&#8217;ed by <code>backup</code> can be restored (when made backup to Gammu text file). </p>
<p> Please note that this adds all content of backup file to phone and does not care about current data in the phone (no duplicates are detected). </p>
<dt><code>backup</code><i> file [-yes]</i></p>
<dd> Backup your phone to file. It&#8217;s possible to backup (depends on phone and backup format): </p>
<p> * phonebook from SIM and phone memory<br />
 * calendar notes<br />
 * SMSC settings<br />
 * operator logo<br />
 * startup (static) logo or startup text<br />
 * WAP bookmarks<br />
 * WAP settings<br />
 * caller logos and groups<br />
 * user ringtones </p>
<p> There are various backup formats supported and the backup format is guessed based on file extension: </p>
<p> * .lmb &#8211; Nokia backup, supports contacts, caller logos and startup logo.<br />
 * .vcs &#8211; vCalendar, supports calendar and todo.<br />
 * .vcf &#8211; vCard, supports contacts.<br />
 * .ldif &#8211; LDAP import, supports contacts.<br />
 * .ics &#8211; iCalendar, supports calendar and todo.<br />
 * Any other extension is Gammu backup file and it supports all data mentioned above. </p>
<p> <i>TIP:</i> if you will backup settings to Gammu text file, it will be possible to edit it. It&#8217;s easy: many things in this file will be written double &#8211; once in Unicode, once in ASCII. When you will remove Unicode version Gammu will use ASCII on <code>restore</code> (and you can easy edit ASCII text) and will convert it according to your OS locale. When will be available Unicode version of text, it will be used instead of ASCII (usefull with Unicode phones &#8211; it isn&#8217;t important, what locale is set in computer and no conversion Unicode -&gt; ASCII and ASCII -&gt; Unicode is done). </p>
<p> <i>TIP:</i> you can use any editor with regular expressions function to edit backup text file. Example: TextPad 4.2.2 from <a rel="nofollow" href="http://www.textpad.com/">http://www.textpad.com/</a> with regular expressions based on POSIX standard P1003.2 is OK for it. Few examples for it: </p>
<p> * to remove info about voice tags:<br />
 FROM: ^Entry\([0-9][0-9]\)VoiceTag = \(.*\)
<br />
 TO: </p>
<p> * to change all numbers starting from +3620, +3630, +3660, +3670 to +3620<br />
 Find: Type = NumberGeneral
Entry\([0-9][0-9]\)Text = &quot;\+36\(20\|30\|60\|70\)<br />
 Repl: Type = NumberMobile
Entry\1Text = &quot;\+3620 </p>
<p> * to change phone numbers type to mobile for numbers starting from +3620, +3630,&#8230; and removing the corresponding TextUnicode line<br />
 F: Type = NumberGeneral
Entry\([0-9][0-9]\)Text = &quot;\+36\([2367]0\)\([^\&quot;]*\)&quot;
Entry\([0-9][0-9]\)TextUnicode = \([^
]*\)
<br />
 R: Type = NumberMobile
Entry\1Text = &quot;\+36\2\3&quot;
 </p>
<dt><code>clearall</code></p>
<dd>
<dt><code>deletecalendar</code><i> start [stop]</i></p>
<dd>
<dt><code>getallcalendar</code></p>
<dd>
<dt><code>getcalendar</code><i> start [stop]</i></p>
<dd>
<dt><code>getcalendarsettings</code></p>
<dd>
<dt><code>restore</code><i> file [-yes]</i></p>
<dd> Restore settings written in file created using <code>backup</code> option. </p>
<p> Please note that restoring deletes all current content in phone. If you want only to add entries to phone, use addnew. </p>
<p> In some phones restoring calendar notes will not show error, but won&#8217;t be done, when phone doesn&#8217;t have set clock inside. </p>
<dt><code>savefile CALENDAR</code><i> target.vcs file location</i></p>
<dd> Allows to convert between various backup formats which gammu supports for calendar events. The file type is guessed (for input file guess is based on extension and file content, for output solely on extension). </p>
<p> For example if you want to convert single entry from gammu native backup to vCalendar, you need following command: </p>
<p>&nbsp;<wbr>gammu savefile CALENDAR output.vcs myCalendar.backup 260 </p>
<dt><code>savesms CALENDAR</code><i> file location [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd> Read calendar note from file created by <code>backup</code> option and saves in VCALENDAR 1.0 format as SMS </p>
<dt><code>sendsms CALENDAR</code><i> destination file location [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
</dl>
<h3>To do lists</h3>
<dl>
<dt><code>addcategory</code><i> TODO|PHONEBOOK text</i></p>
<dd>
<dt><code>addnew</code><i> file [-yes]</i></p>
<dd> Adds data written in file created using <code>backup option</code>. All things backup&#8217;ed by <code>backup</code> can be restored (when made backup to Gammu text file). </p>
<p> Please note that this adds all content of backup file to phone and does not care about current data in the phone (no duplicates are detected). </p>
<dt><code>backup</code><i> file [-yes]</i></p>
<dd> Backup your phone to file. It&#8217;s possible to backup (depends on phone and backup format): </p>
<p> * phonebook from SIM and phone memory<br />
 * calendar notes<br />
 * SMSC settings<br />
 * operator logo<br />
 * startup (static) logo or startup text<br />
 * WAP bookmarks<br />
 * WAP settings<br />
 * caller logos and groups<br />
 * user ringtones </p>
<p> There are various backup formats supported and the backup format is guessed based on file extension: </p>
<p> * .lmb &#8211; Nokia backup, supports contacts, caller logos and startup logo.<br />
 * .vcs &#8211; vCalendar, supports calendar and todo.<br />
 * .vcf &#8211; vCard, supports contacts.<br />
 * .ldif &#8211; LDAP import, supports contacts.<br />
 * .ics &#8211; iCalendar, supports calendar and todo.<br />
 * Any other extension is Gammu backup file and it supports all data mentioned above. </p>
<p> <i>TIP:</i> if you will backup settings to Gammu text file, it will be possible to edit it. It&#8217;s easy: many things in this file will be written double &#8211; once in Unicode, once in ASCII. When you will remove Unicode version Gammu will use ASCII on <code>restore</code> (and you can easy edit ASCII text) and will convert it according to your OS locale. When will be available Unicode version of text, it will be used instead of ASCII (usefull with Unicode phones &#8211; it isn&#8217;t important, what locale is set in computer and no conversion Unicode -&gt; ASCII and ASCII -&gt; Unicode is done). </p>
<p> <i>TIP:</i> you can use any editor with regular expressions function to edit backup text file. Example: TextPad 4.2.2 from <a rel="nofollow" href="http://www.textpad.com/">http://www.textpad.com/</a> with regular expressions based on POSIX standard P1003.2 is OK for it. Few examples for it: </p>
<p> * to remove info about voice tags:<br />
 FROM: ^Entry\([0-9][0-9]\)VoiceTag = \(.*\)
<br />
 TO: </p>
<p> * to change all numbers starting from +3620, +3630, +3660, +3670 to +3620<br />
 Find: Type = NumberGeneral
Entry\([0-9][0-9]\)Text = &quot;\+36\(20\|30\|60\|70\)<br />
 Repl: Type = NumberMobile
Entry\1Text = &quot;\+3620 </p>
<p> * to change phone numbers type to mobile for numbers starting from +3620, +3630,&#8230; and removing the corresponding TextUnicode line<br />
 F: Type = NumberGeneral
Entry\([0-9][0-9]\)Text = &quot;\+36\([2367]0\)\([^\&quot;]*\)&quot;
Entry\([0-9][0-9]\)TextUnicode = \([^
]*\)
<br />
 R: Type = NumberMobile
Entry\1Text = &quot;\+36\2\3&quot;
 </p>
<dt><code>clearall</code></p>
<dd>
<dt><code>deletetodo</code><i> start [stop]</i></p>
<dd>
<dt><code>getallcategory</code><i> TODO|PHONEBOOK</i></p>
<dd>
<dt><code>getalltodo</code></p>
<dd>
<dt><code>getcategory</code><i> TODO|PHONEBOOK start [stop]</i></p>
<dd>
<dt><code>gettodo</code><i> start [stop]</i></p>
<dd>
<dt><code>listtodocategory</code><i> text|number</i></p>
<dd>
<dt><code>restore</code><i> file [-yes]</i></p>
<dd> Restore settings written in file created using <code>backup</code> option. </p>
<p> Please note that restoring deletes all current content in phone. If you want only to add entries to phone, use addnew. </p>
<p> In some phones restoring calendar notes will not show error, but won&#8217;t be done, when phone doesn&#8217;t have set clock inside. </p>
<dt><code>savefile TODO</code><i> target.vcs file location</i></p>
<dd> Allows to convert between various backup formats which gammu supports for todo events. The file type is guessed (for input file guess is based on extension and file content, for output solely on extension). </p>
<p> For example if you want to convert single entry from gammu native backup to vCalendar, you need following command: </p>
<p>&nbsp;<wbr>gammu savefile CALENDAR output.vcs myCalendar.backup 260 </p>
<dt><code>savesms TODO</code><i> file location [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
<dt><code>sendsms TODO</code><i> destination file location [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
</dl>
<h3>Notes</h3>
<dl>
<dt><code>getallnotes</code></p>
<dd>
</dl>
<h3>Date, time and alarms</h3>
<dl>
<dt><code>getalarm</code><i> [start]</i></p>
<dd> Get alarm from phone, if no location is specified, 1 is used. </p>
<dt><code>getdatetime</code></p>
<dd> Get date and time from phone </p>
<dt><code>setalarm</code><i> hour minute</i></p>
<dd> Sets repeating alarm in phone on selected time.</p>
<dt><code>setdatetime</code><i> [HH:MM[:SS]] [YYYY/MM/DD]</i></p>
<dd> Set date and time in phone to date and time set in computer. Please note, that this option doesn&#8217;t show clock on phone screen. It only set date and time. </p>
<p> <i>TIP:</i> you can make such synchronization each time, when will connect your phone and use Gammu. See <a href="/docs/linux/man/5-gammurc/">gammurc</a>(5) for details. </p>
</dl>
<h3>Categories</h3>
<dl>
<dt><code>addcategory</code><i> TODO|PHONEBOOK text</i></p>
<dd>
<dt><code>addnew</code><i> file [-yes]</i></p>
<dd> Adds data written in file created using <code>backup option</code>. All things backup&#8217;ed by <code>backup</code> can be restored (when made backup to Gammu text file). </p>
<p> Please note that this adds all content of backup file to phone and does not care about current data in the phone (no duplicates are detected). </p>
<dt><code>backup</code><i> file [-yes]</i></p>
<dd> Backup your phone to file. It&#8217;s possible to backup (depends on phone and backup format): </p>
<p> * phonebook from SIM and phone memory<br />
 * calendar notes<br />
 * SMSC settings<br />
 * operator logo<br />
 * startup (static) logo or startup text<br />
 * WAP bookmarks<br />
 * WAP settings<br />
 * caller logos and groups<br />
 * user ringtones </p>
<p> There are various backup formats supported and the backup format is guessed based on file extension: </p>
<p> * .lmb &#8211; Nokia backup, supports contacts, caller logos and startup logo.<br />
 * .vcs &#8211; vCalendar, supports calendar and todo.<br />
 * .vcf &#8211; vCard, supports contacts.<br />
 * .ldif &#8211; LDAP import, supports contacts.<br />
 * .ics &#8211; iCalendar, supports calendar and todo.<br />
 * Any other extension is Gammu backup file and it supports all data mentioned above. </p>
<p> <i>TIP:</i> if you will backup settings to Gammu text file, it will be possible to edit it. It&#8217;s easy: many things in this file will be written double &#8211; once in Unicode, once in ASCII. When you will remove Unicode version Gammu will use ASCII on <code>restore</code> (and you can easy edit ASCII text) and will convert it according to your OS locale. When will be available Unicode version of text, it will be used instead of ASCII (usefull with Unicode phones &#8211; it isn&#8217;t important, what locale is set in computer and no conversion Unicode -&gt; ASCII and ASCII -&gt; Unicode is done). </p>
<p> <i>TIP:</i> you can use any editor with regular expressions function to edit backup text file. Example: TextPad 4.2.2 from <a rel="nofollow" href="http://www.textpad.com/">http://www.textpad.com/</a> with regular expressions based on POSIX standard P1003.2 is OK for it. Few examples for it: </p>
<p> * to remove info about voice tags:<br />
 FROM: ^Entry\([0-9][0-9]\)VoiceTag = \(.*\)
<br />
 TO: </p>
<p> * to change all numbers starting from +3620, +3630, +3660, +3670 to +3620<br />
 Find: Type = NumberGeneral
Entry\([0-9][0-9]\)Text = &quot;\+36\(20\|30\|60\|70\)<br />
 Repl: Type = NumberMobile
Entry\1Text = &quot;\+3620 </p>
<p> * to change phone numbers type to mobile for numbers starting from +3620, +3630,&#8230; and removing the corresponding TextUnicode line<br />
 F: Type = NumberGeneral
Entry\([0-9][0-9]\)Text = &quot;\+36\([2367]0\)\([^\&quot;]*\)&quot;
Entry\([0-9][0-9]\)TextUnicode = \([^
]*\)
<br />
 R: Type = NumberMobile
Entry\1Text = &quot;\+36\2\3&quot;
 </p>
<dt><code>clearall</code></p>
<dd>
<dt><code>getallcategory</code><i> TODO|PHONEBOOK</i></p>
<dd>
<dt><code>getcategory</code><i> TODO|PHONEBOOK start [stop]</i></p>
<dd>
<dt><code>listmemorycategory</code><i> text|number</i></p>
<dd>
<dt><code>listtodocategory</code><i> text|number</i></p>
<dd>
<dt><code>restore</code><i> file [-yes]</i></p>
<dd> Restore settings written in file created using <code>backup</code> option. </p>
<p> Please note that restoring deletes all current content in phone. If you want only to add entries to phone, use addnew. </p>
<p> In some phones restoring calendar notes will not show error, but won&#8217;t be done, when phone doesn&#8217;t have set clock inside. </p>
</dl>
<h3>Backing up and restoring</h3>
<dl>
<dt><code>addnew</code><i> file [-yes]</i></p>
<dd> Adds data written in file created using <code>backup option</code>. All things backup&#8217;ed by <code>backup</code> can be restored (when made backup to Gammu text file). </p>
<p> Please note that this adds all content of backup file to phone and does not care about current data in the phone (no duplicates are detected). </p>
<dt><code>addsms</code><i> folder file [-yes]</i></p>
<dd> Adds SMSes from file (format like backupsms uses) to selected folder in phone.</p>
<dt><code>backup</code><i> file [-yes]</i></p>
<dd> Backup your phone to file. It&#8217;s possible to backup (depends on phone and backup format): </p>
<p> * phonebook from SIM and phone memory<br />
 * calendar notes<br />
 * SMSC settings<br />
 * operator logo<br />
 * startup (static) logo or startup text<br />
 * WAP bookmarks<br />
 * WAP settings<br />
 * caller logos and groups<br />
 * user ringtones </p>
<p> There are various backup formats supported and the backup format is guessed based on file extension: </p>
<p> * .lmb &#8211; Nokia backup, supports contacts, caller logos and startup logo.<br />
 * .vcs &#8211; vCalendar, supports calendar and todo.<br />
 * .vcf &#8211; vCard, supports contacts.<br />
 * .ldif &#8211; LDAP import, supports contacts.<br />
 * .ics &#8211; iCalendar, supports calendar and todo.<br />
 * Any other extension is Gammu backup file and it supports all data mentioned above. </p>
<p> <i>TIP:</i> if you will backup settings to Gammu text file, it will be possible to edit it. It&#8217;s easy: many things in this file will be written double &#8211; once in Unicode, once in ASCII. When you will remove Unicode version Gammu will use ASCII on <code>restore</code> (and you can easy edit ASCII text) and will convert it according to your OS locale. When will be available Unicode version of text, it will be used instead of ASCII (usefull with Unicode phones &#8211; it isn&#8217;t important, what locale is set in computer and no conversion Unicode -&gt; ASCII and ASCII -&gt; Unicode is done). </p>
<p> <i>TIP:</i> you can use any editor with regular expressions function to edit backup text file. Example: TextPad 4.2.2 from <a rel="nofollow" href="http://www.textpad.com/">http://www.textpad.com/</a> with regular expressions based on POSIX standard P1003.2 is OK for it. Few examples for it: </p>
<p> * to remove info about voice tags:<br />
 FROM: ^Entry\([0-9][0-9]\)VoiceTag = \(.*\)
<br />
 TO: </p>
<p> * to change all numbers starting from +3620, +3630, +3660, +3670 to +3620<br />
 Find: Type = NumberGeneral
Entry\([0-9][0-9]\)Text = &quot;\+36\(20\|30\|60\|70\)<br />
 Repl: Type = NumberMobile
Entry\1Text = &quot;\+3620 </p>
<p> * to change phone numbers type to mobile for numbers starting from +3620, +3630,&#8230; and removing the corresponding TextUnicode line<br />
 F: Type = NumberGeneral
Entry\([0-9][0-9]\)Text = &quot;\+36\([2367]0\)\([^\&quot;]*\)&quot;
Entry\([0-9][0-9]\)TextUnicode = \([^
]*\)
<br />
 R: Type = NumberMobile
Entry\1Text = &quot;\+36\2\3&quot;
 </p>
<dt><code>backupsms</code><i> file [-yes|-all]</i></p>
<dd> Stores all SMSes from phone to file. </p>
<p> Use -yes for answering yes to all questions (backup all messages and delete them from phone), or -all to just backup all folders while keeping messages in phone. </p>
<dt><code>restore</code><i> file [-yes]</i></p>
<dd> Restore settings written in file created using <code>backup</code> option. </p>
<p> Please note that restoring deletes all current content in phone. If you want only to add entries to phone, use addnew. </p>
<p> In some phones restoring calendar notes will not show error, but won&#8217;t be done, when phone doesn&#8217;t have set clock inside. </p>
<dt><code>restoresms</code><i> file [-yes]</i></p>
<dd> Restores SMSes from file (format like backupsms uses) to selected folder in phone. Please note that this overwrites existing messages in phone (if it supports it).</p>
<dt><code>savefile</code><i> VCARD10|VCARD21 target.vcf file SM|ME location</i></p>
<dd>
<dt><code>savefile BOOKMARK</code><i> target.url file location</i></p>
<dd>
<dt><code>savefile CALENDAR</code><i> target.vcs file location</i></p>
<dd> Allows to convert between various backup formats which gammu supports for calendar events. The file type is guessed (for input file guess is based on extension and file content, for output solely on extension). </p>
<p> For example if you want to convert single entry from gammu native backup to vCalendar, you need following command: </p>
<p>&nbsp;<wbr>gammu savefile CALENDAR output.vcs myCalendar.backup 260 </p>
<dt><code>savefile TODO</code><i> target.vcs file location</i></p>
<dd> Allows to convert between various backup formats which gammu supports for todo events. The file type is guessed (for input file guess is based on extension and file content, for output solely on extension). </p>
<p> For example if you want to convert single entry from gammu native backup to vCalendar, you need following command: </p>
<p>&nbsp;<wbr>gammu savefile CALENDAR output.vcs myCalendar.backup 260 </p>
</dl>
<h3>Nokia specific</h3>
<dl>
<dt><code>nokiaaddfile</code><i> Gallery|Gallery2|Camera|Tones|Tones2|Records|Video|Playlist|MemoryCard file [-name name] [-protected] [-readonly] [-system] [-hidden] [-newtime]</i></p>
<dd> Install the *.jar/*.jad file pair of a midlet in the application or game menu of the phone. You have to give the name without the jar/jad suffix, otherwise you will get the slightly confusing error message Can&#8217;t open specified file. Read only ? </p>
<p> The option <i>-overwrite</i> deletes the application&#8217;s .jad and .jar files bevor installing, but doesn&#8217;t delete the application data. Option <i>-overwriteall</i> will also delete all data. Both these options work only for Application or Game upload. </p>
<p> <i>Example:</i> gammu nokiaaddfile Application Alien will read Alien.JAD and Alien.JAR and add to Applications </p>
<p> <i>Example:</i> gammu nokiaaddfile Tones file.mid will read file.mid and add to Tones folder </p>
<p> You can use <a href="/docs/linux/man/1-jadmaker/">jadmaker</a>(1) to generate a .jad file from a .jar file. </p>
<dt><code>nokiaaddplaylists</code></p>
<dd>
<dt><code>nokiacomposer</code><i> file</i></p>
<dd> Show, how to enter RTTL ringtone in composer existing in many Nokia phones (and how should it look like). </p>
<dt><code>nokiadebug</code><i> filename [[v11-22] [,v33-44]&#8230;]</i></p>
<dd>
<dt><code>nokiadisplayoutput</code></p>
<dd>
<dt><code>nokiadisplaytest</code><i> number</i></p>
<dd>
<dt><code>nokiagetadc</code></p>
<dd>
<dt><code>nokiagetoperatorname</code></p>
<dd> 6110.c phones have place for name for one GSM network (of course, with flashing it&#8217;s possible to change all names, but Gammu is not flasher ;-)). You can get this name using this option. </p>
<dt><code>nokiagetpbkfeatures</code><i> memorytype</i></p>
<dd>
<dt><code>nokiagetscreendump</code></p>
<dd>
<dt><code>nokiagett9</code></p>
<dd>
<dt><code>nokiagetvoicerecord</code><i> location</i></p>
<dd>
<p> Get voice record from location and save to WAV file. File is coded using GSM 6.10 codec (available for example in win32). Name of file is like name of voice record in phone. </p>
<dt><code>nokiamakecamerashoot</code></p>
<dd>
<dt><code>nokianetmonitor</code><i> test</i></p>
<dd> Takes output or set netmonitor for Nokia DCT3 phones. </p>
<p> <i>TIP:</i> For more info about this option, please visit <i><a rel="nofollow" href="http://www.mwiacek.com">http://www.mwiacek.com</a></i> and read netmonitor manual. </p>
<p> <i>TIP:</i> test <code>243</code> enables all tests (after using command <code>gammu nokianetmonitor 243</code> in some phones like 6210 or 9210 have to reboot them to see netmonitor menu) </p>
<dt><code>nokianetmonitor36</code></p>
<dd> Reset counters from netmonitor test 36 in Nokia DCT3 phones. </p>
<p> <i>TIP:</i> For more info about this option, please visit <i><a rel="nofollow" href="http://www.mwiacek.com">www.mwiacek.com</a></i> and read netmonitor manual. </p>
<dt><code>nokiasecuritycode</code></p>
<dd> Get/reset to &quot;12345&quot; security code </p>
<dt><code>nokiaselftests</code></p>
<dd>
<dt><code>nokiasetlights</code><i> keypad|display|torch on|off</i></p>
<dd>
<dt><code>nokiasetoperatorname</code><i> [networkcode name]</i></p>
<dd>
<dt><code>nokiasetphonemenus</code></p>
<dd> Enable all (?) possible menus for DCT3 Nokia phones: </p>
<p> 1. ALS (Alternative Line Service) option menu<br />
 2. vibra menu for 3210<br />
 3. 3315 features in 3310 5.45 and higher<br />
 4. two additional games (React and Logic) for 3210 5.31 and higher<br />
 5. WellMate menu for 6150<br />
 6. NetMonitor </p>
<p> and for DCT4: </p>
<p> 1. ALS (Alternative Line Service) option menu<br />
 2. Bluetooth, WAP bookmarks and settings menu, &#8230; (6310i)<br />
 3. GPRS Always Online </p>
<p>&nbsp;<wbr>&#8230; </p>
<dt><code>nokiasetvibralevel</code><i> level</i></p>
<dd> Set vibra power to &quot;level&quot; (given in percent) </p>
<dt><code>nokiatuneradio</code></p>
<dd>
<dt><code>nokiavibratest</code></p>
<dd>
</dl>
<h3>Siemens specific</h3>
<dl>
<dt><code>siemensnetmonact</code><i> netmon_type (1-full, 2-simple)</i></p>
<dd>
<dt><code>siemensnetmonitor</code><i> test</i></p>
<dd>
<dt><code>siemenssatnetmon</code></p>
<dd>
</dl>
<h3>Network</h3>
<dl>
<dt><code>getgprspoint</code><i> start [stop]</i></p>
<dd>
<dt><code>listnetworks</code><i> [country]</i></p>
<dd> Show names/codes of GSM networks known for Gammu </p>
<dt><code>monitor</code><i> [times]</i></p>
<dd> Get phone status and writes continuously to standard output. Press Ctrl+C to break this state. </p>
<dt><code>networkinfo</code></p>
<dd>
<dt><code>nokiadebug</code><i> filename [[v11-22] [,v33-44]&#8230;]</i></p>
<dd>
<dt><code>nokiagetoperatorname</code></p>
<dd> 6110.c phones have place for name for one GSM network (of course, with flashing it&#8217;s possible to change all names, but Gammu is not flasher ;-)). You can get this name using this option. </p>
<dt><code>nokianetmonitor</code><i> test</i></p>
<dd> Takes output or set netmonitor for Nokia DCT3 phones. </p>
<p> <i>TIP:</i> For more info about this option, please visit <i><a rel="nofollow" href="http://www.mwiacek.com">http://www.mwiacek.com</a></i> and read netmonitor manual. </p>
<p> <i>TIP:</i> test <code>243</code> enables all tests (after using command <code>gammu nokianetmonitor 243</code> in some phones like 6210 or 9210 have to reboot them to see netmonitor menu) </p>
<dt><code>nokiasetoperatorname</code><i> [networkcode name]</i></p>
<dd>
<dt><code>setautonetworklogin</code></p>
<dd>
<dt><code>siemensnetmonact</code><i> netmon_type (1-full, 2-simple)</i></p>
<dd>
<dt><code>siemensnetmonitor</code><i> test</i></p>
<dd>
<dt><code>siemenssatnetmon</code></p>
<dd>
</dl>
<h3>WAP settings and bookmarks</h3>
<dl>
<dt><code>addnew</code><i> file [-yes]</i></p>
<dd> Adds data written in file created using <code>backup option</code>. All things backup&#8217;ed by <code>backup</code> can be restored (when made backup to Gammu text file). </p>
<p> Please note that this adds all content of backup file to phone and does not care about current data in the phone (no duplicates are detected). </p>
<dt><code>backup</code><i> file [-yes]</i></p>
<dd> Backup your phone to file. It&#8217;s possible to backup (depends on phone and backup format): </p>
<p> * phonebook from SIM and phone memory<br />
 * calendar notes<br />
 * SMSC settings<br />
 * operator logo<br />
 * startup (static) logo or startup text<br />
 * WAP bookmarks<br />
 * WAP settings<br />
 * caller logos and groups<br />
 * user ringtones </p>
<p> There are various backup formats supported and the backup format is guessed based on file extension: </p>
<p> * .lmb &#8211; Nokia backup, supports contacts, caller logos and startup logo.<br />
 * .vcs &#8211; vCalendar, supports calendar and todo.<br />
 * .vcf &#8211; vCard, supports contacts.<br />
 * .ldif &#8211; LDAP import, supports contacts.<br />
 * .ics &#8211; iCalendar, supports calendar and todo.<br />
 * Any other extension is Gammu backup file and it supports all data mentioned above. </p>
<p> <i>TIP:</i> if you will backup settings to Gammu text file, it will be possible to edit it. It&#8217;s easy: many things in this file will be written double &#8211; once in Unicode, once in ASCII. When you will remove Unicode version Gammu will use ASCII on <code>restore</code> (and you can easy edit ASCII text) and will convert it according to your OS locale. When will be available Unicode version of text, it will be used instead of ASCII (usefull with Unicode phones &#8211; it isn&#8217;t important, what locale is set in computer and no conversion Unicode -&gt; ASCII and ASCII -&gt; Unicode is done). </p>
<p> <i>TIP:</i> you can use any editor with regular expressions function to edit backup text file. Example: TextPad 4.2.2 from <a rel="nofollow" href="http://www.textpad.com/">http://www.textpad.com/</a> with regular expressions based on POSIX standard P1003.2 is OK for it. Few examples for it: </p>
<p> * to remove info about voice tags:<br />
 FROM: ^Entry\([0-9][0-9]\)VoiceTag = \(.*\)
<br />
 TO: </p>
<p> * to change all numbers starting from +3620, +3630, +3660, +3670 to +3620<br />
 Find: Type = NumberGeneral
Entry\([0-9][0-9]\)Text = &quot;\+36\(20\|30\|60\|70\)<br />
 Repl: Type = NumberMobile
Entry\1Text = &quot;\+3620 </p>
<p> * to change phone numbers type to mobile for numbers starting from +3620, +3630,&#8230; and removing the corresponding TextUnicode line<br />
 F: Type = NumberGeneral
Entry\([0-9][0-9]\)Text = &quot;\+36\([2367]0\)\([^\&quot;]*\)&quot;
Entry\([0-9][0-9]\)TextUnicode = \([^
]*\)
<br />
 R: Type = NumberMobile
Entry\1Text = &quot;\+36\2\3&quot;
 </p>
<dt><code>clearall</code></p>
<dd>
<dt><code>deletewapbookmark</code><i> start [stop]</i></p>
<dd> Delete WAP bookmarks from phone. </p>
<p> Locations are numerated from 1. </p>
<dt><code>getchatsettings</code><i> start [stop]</i></p>
<dd>
<dt><code>getsyncmlsettings</code><i> start [stop]</i></p>
<dd>
<dt><code>getwapbookmark</code><i> start [stop]</i></p>
<dd> Get WAP bookmarks from phone. </p>
<p> Locations are numerated from 1. </p>
<dt><code>getwapsettings</code><i> start [stop]</i></p>
<dd> Get WAP settings from phone. </p>
<p> Locations are numerated from 1. </p>
<dt><code>restore</code><i> file [-yes]</i></p>
<dd> Restore settings written in file created using <code>backup</code> option. </p>
<p> Please note that restoring deletes all current content in phone. If you want only to add entries to phone, use addnew. </p>
<p> In some phones restoring calendar notes will not show error, but won&#8217;t be done, when phone doesn&#8217;t have set clock inside. </p>
<dt><code>savefile BOOKMARK</code><i> target.url file location</i></p>
<dd>
<dt><code>savesms BOOKMARK</code><i> file location [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd> Read WAP bookmark from file created by <code>backup</code> option and saves in Nokia format as SMS </p>
<dt><code>savesms WAPINDICATOR</code><i> URL Title [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
<dt><code>savesms WAPSETTINGS</code><i> file location DATA|GPRS [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd> Read WAP settings from file created by <code>backup</code> option and saves in Nokia format as SMS </p>
<dt><code>sendsms BOOKMARK</code><i> destination file location [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
<dt><code>sendsms WAPINDICATOR</code><i> destination URL Title [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
<dt><code>sendsms WAPSETTINGS</code><i> destination file location DATA|GPRS [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
</dl>
<h3>MMS and MMS settings</h3>
<dl>
<dt><code>getallmms</code><i> [-save]</i></p>
<dd>
<dt><code>geteachmms</code><i> [-save]</i></p>
<dd>
<dt><code>getmmsfolders</code></p>
<dd>
<dt><code>getmmssettings</code><i> start [stop]</i></p>
<dd>
<dt><code>readmmsfile</code><i> file [-save]</i></p>
<dd>
<dt><code>savesms MMSINDICATOR</code><i> URL Title Sender [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
<dt><code>savesms MMSSETTINGS</code><i> file location [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
<dt><code>sendsms MMSINDICATOR</code><i> destination URL Title Sender [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
<p> Sends a message with MMS indication. The recipient phone will then download MMS from given URL and display it. </p>
<p> Please note that you should provide valid smil data on that URL. </p>
<dt><code>sendsms MMSSETTINGS</code><i> destination file location [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num]</i></p>
<dd>
</dl>
<h3>Phone tests</h3>
<dl>
<dt><code>nokiadisplaytest</code><i> number</i></p>
<dd>
<dt><code>nokiagetadc</code></p>
<dd>
<dt><code>nokiaselftests</code></p>
<dd>
<dt><code>nokiasetlights</code><i> keypad|display|torch on|off</i></p>
<dd>
<dt><code>nokiavibratest</code></p>
<dd>
</dl>
<h3>FM radio</h3>
<dl>
<dt><code>addnew</code><i> file [-yes]</i></p>
<dd> Adds data written in file created using <code>backup option</code>. All things backup&#8217;ed by <code>backup</code> can be restored (when made backup to Gammu text file). </p>
<p> Please note that this adds all content of backup file to phone and does not care about current data in the phone (no duplicates are detected). </p>
<dt><code>backup</code><i> file [-yes]</i></p>
<dd> Backup your phone to file. It&#8217;s possible to backup (depends on phone and backup format): </p>
<p> * phonebook from SIM and phone memory<br />
 * calendar notes<br />
 * SMSC settings<br />
 * operator logo<br />
 * startup (static) logo or startup text<br />
 * WAP bookmarks<br />
 * WAP settings<br />
 * caller logos and groups<br />
 * user ringtones </p>
<p> There are various backup formats supported and the backup format is guessed based on file extension: </p>
<p> * .lmb &#8211; Nokia backup, supports contacts, caller logos and startup logo.<br />
 * .vcs &#8211; vCalendar, supports calendar and todo.<br />
 * .vcf &#8211; vCard, supports contacts.<br />
 * .ldif &#8211; LDAP import, supports contacts.<br />
 * .ics &#8211; iCalendar, supports calendar and todo.<br />
 * Any other extension is Gammu backup file and it supports all data mentioned above. </p>
<p> <i>TIP:</i> if you will backup settings to Gammu text file, it will be possible to edit it. It&#8217;s easy: many things in this file will be written double &#8211; once in Unicode, once in ASCII. When you will remove Unicode version Gammu will use ASCII on <code>restore</code> (and you can easy edit ASCII text) and will convert it according to your OS locale. When will be available Unicode version of text, it will be used instead of ASCII (usefull with Unicode phones &#8211; it isn&#8217;t important, what locale is set in computer and no conversion Unicode -&gt; ASCII and ASCII -&gt; Unicode is done). </p>
<p> <i>TIP:</i> you can use any editor with regular expressions function to edit backup text file. Example: TextPad 4.2.2 from <a rel="nofollow" href="http://www.textpad.com/">http://www.textpad.com/</a> with regular expressions based on POSIX standard P1003.2 is OK for it. Few examples for it: </p>
<p> * to remove info about voice tags:<br />
 FROM: ^Entry\([0-9][0-9]\)VoiceTag = \(.*\)
<br />
 TO: </p>
<p> * to change all numbers starting from +3620, +3630, +3660, +3670 to +3620<br />
 Find: Type = NumberGeneral
Entry\([0-9][0-9]\)Text = &quot;\+36\(20\|30\|60\|70\)<br />
 Repl: Type = NumberMobile
Entry\1Text = &quot;\+3620 </p>
<p> * to change phone numbers type to mobile for numbers starting from +3620, +3630,&#8230; and removing the corresponding TextUnicode line<br />
 F: Type = NumberGeneral
Entry\([0-9][0-9]\)Text = &quot;\+36\([2367]0\)\([^\&quot;]*\)&quot;
Entry\([0-9][0-9]\)TextUnicode = \([^
]*\)
<br />
 R: Type = NumberMobile
Entry\1Text = &quot;\+36\2\3&quot;
 </p>
<dt><code>clearall</code></p>
<dd>
<dt><code>getfmstation</code><i> start [stop]</i></p>
<dd> Show info about FM stations in phone </p>
<dt><code>nokiatuneradio</code></p>
<dd>
<dt><code>restore</code><i> file [-yes]</i></p>
<dd> Restore settings written in file created using <code>backup</code> option. </p>
<p> Please note that restoring deletes all current content in phone. If you want only to add entries to phone, use addnew. </p>
<p> In some phones restoring calendar notes will not show error, but won&#8217;t be done, when phone doesn&#8217;t have set clock inside. </p>
</dl>
<h3>Phone information</h3>
<dl>
<dt><code>checkfirmware</code></p>
<dd>
<p> Gammu connects to <a rel="nofollow" href="http://www.gammu.org">www.gammu.org</a> and checks for latest firmware versions available for the device. The file &lt;<a rel="nofollow" href="http://www.gammu.org/support/phones/phonedbxml.php?model=x">http://www.gammu.org/support/phones/phonedbxml.php?model=x</a>&gt; will be downloaded, all phone details will be read from it and (if any higher firmware exist) displayed info to user on each application startup. No private data are sent to server. Internet connection to <a rel="nofollow" href="http://www.gammu.org">www.gammu.org</a> on port 80 required. </p>
<dt><code>getdisplaystatus</code></p>
<dd>
<dt><code>getsecuritystatus</code></p>
<dd> Show, if phone wait for security code (like PIN, PUK, etc.) or not </p>
<dt><code>identify</code></p>
<dd> Show the most important phone data. </p>
<dt><code>monitor</code><i> [times]</i></p>
<dd> Get phone status and writes continuously to standard output. Press Ctrl+C to break this state. </p>
<dt><code>nokiasecuritycode</code></p>
<dd> Get/reset to &quot;12345&quot; security code </p>
</dl>
<h3>Phone settings</h3>
<dl>
<dt><code>getcalendarsettings</code></p>
<dd>
<dt><code>getprofile</code><i> start [stop]</i></p>
<dd>
<dt><code>resetphonesettings</code><i> PHONE|DEV|UIF|ALL|FACTORY</i></p>
<dd> Reset phone settings. <i>BE CAREFULL !!!!</i> </p>
<p> <code>PHONE:</code> </p>
<p> <code>DEV:</code> </p>
<p> <code>ALL:</code> </p>
<p> Clear user settings<br />
 * removes or set logos to default<br />
 * set default phonebook and other menu settings<br />
 * clear T9 words,<br />
 * clear call register info<br />
 * set default profiles settings<br />
 * clear user ringtones </p>
<p> <code>UIF:</code><br />
 * changes like after <code>ALL</code><br />
 * disables netmon and PPS (all &quot;hidden&quot; menus) </p>
<p> <code>FACTORY:</code><br />
 * changes like after <code>UIF</code><br />
 * clear date/time </p>
<dt><code>savesms PROFILE</code><i> [-folder id] [-unread] [-read] [-unsent] [-sent] [-sender number] [-smsname name] [-smscset number] [-smscnumber number] [-reply] [-maxsms num] [-name name] [-bitmap bitmap] [-ringtone ringtone]</i></p>
<dd> Read ringtone (RTTL) format and bitmap (Picture Image size) and name and save as Nokia profile. </p>
<dt><code>sendsms PROFILE</code><i> destination [-report] [-validity HOUR|6HOURS|DAY|3DAYS|WEEK|MAX] [-save [-folder number]] [-smscset number] [-smscnumber number] [-reply] [-maxsms num] [-name name] [-bitmap bitmap] [-ringtone ringtone]</i></p>
<dd>
</dl>
<h3>Dumps decoding</h3>
<dl>
<dt><code>decodebinarydump</code><i> file [phonemodel]</i></p>
<dd> After using option <code>logfile</code> with name <code>binary</code> (see <i>/readme.txt</i> for info about this method of reporting bugs) created file can be decoded using this option. It&#8217;s available only, if Gammu was compiled with debug. </p>
<dt><code>decodesniff</code><i> MBUS2|IRDA file [phonemodel]</i></p>
<dd> Option available only, if Gammu was compiled with debug. Allows to decode sniffs. See <i>/docs/develop/develop.txt</i> for more details. </p>
<dt><code>makeconverttable</code><i> file</i></p>
<dd>
</dl>
<h3>Functions that don&#8217;t fit elsewhere</h3>
<dl>
<dt><code>batch</code><i> [file]</i></p>
<dd>
<dt><code>entersecuritycode</code><i> PIN|PUK|PIN2|PUK2|PHONE|NETWORK code|-</i></p>
<dd> Allow to enter security code from PC. When code is -, it is read from stdin. </p>
<dt><code>nokiagetscreendump</code></p>
<dd>
<dt><code>nokiagetvoicerecord</code><i> location</i></p>
<dd>
<p> Get voice record from location and save to WAV file. File is coded using GSM 6.10 codec (available for example in win32). Name of file is like name of voice record in phone. </p>
<dt><code>nokiamakecamerashoot</code></p>
<dd>
<dt><code>nokiasetphonemenus</code></p>
<dd> Enable all (?) possible menus for DCT3 Nokia phones: </p>
<p> 1. ALS (Alternative Line Service) option menu<br />
 2. vibra menu for 3210<br />
 3. 3315 features in 3310 5.45 and higher<br />
 4. two additional games (React and Logic) for 3210 5.31 and higher<br />
 5. WellMate menu for 6150<br />
 6. NetMonitor </p>
<p> and for DCT4: </p>
<p> 1. ALS (Alternative Line Service) option menu<br />
 2. Bluetooth, WAP bookmarks and settings menu, &#8230; (6310i)<br />
 3. GPRS Always Online </p>
<p>&nbsp;<wbr>&#8230; </p>
<dt><code>nokiasetvibralevel</code><i> level</i></p>
<dd> Set vibra power to &quot;level&quot; (given in percent) </p>
<dt><code>presskeysequence</code><i> mMnNpPuUdD+-123456789*0#gGrR&lt;&gt;[]hHcCjJfFoOmMdD@</i></p>
<dd> Press specified key sequence on phone keyboard </p>
<p> <code>mM</code> &#8211; Menu<br />
 <code>nN</code> &#8211; Names key<br />
 <code>pP</code> &#8211; Power<br />
 <code>uU</code> &#8211; Up<br />
 <code>dD</code> &#8211; Down<br />
 <code>+-</code> &#8211; +-<br />
 <code>gG</code> &#8211; Green<br />
 <code>rR</code> &#8211; Red<br />
 <code>123456789*0#</code> is numeric keyboard </p>
<dt><code>reset</code><i> SOFT|HARD</i></p>
<dd> Make phone reset: soft (without asking for PIN) or hard (with PIN). </p>
<p> <i>Note:</i> some phones will make hard reset even with <code>SOFT</code> option. </p>
<dt><code>searchphone</code><i> [-debug]</i></p>
<dd>
</dl>
<h3>Gammu information</h3>
<dl>
<dt><code>checkversion</code><i> [stable]</i></p>
<dd> Checks whether there is newer Gammu version available online (if Gammu has been compiled with CURL). If you pass additional parameter stable, only stable versions will be checked. </p>
<dt><code>features</code></p>
<dd>
<dt><code>help</code></p>
<dd> Output help information and exit. </p>
<dt><code>version</code></p>
<dd> Output version information and exit. </p>
</dl>
<h2>FILES</h2>
<p> <i>~/.gammurc</i><br />
 <i>/usr/share/doc/gammu/*</i><br />
 <i>/dev/ircomm?</i><br />
 <i>/dev/ttyS?</i><br />
 <i>/dev/ttyACM?</i> </p>
<h2>EXAMPLE</h2>
<p> To check it out, you need to have configuration file for gammu, see <a href="/docs/linux/man/5-gammurc/">gammurc</a>(5) for more details about it. </p>
<dl>
<dt>Save text message up to standard 160 chars:</p>
<dd>
<p> echo &quot;All your base are belong to us&quot; | gammu savesms TEXT </p>
<p> or </p>
<p> gammu savesms TEXT -text &quot;All your base are belong to us&quot; </p>
<dt>Save long text message:</p>
<dd>
<p> echo &quot;All your base are belong to us&quot; | gammu savesms TEXT -len 400 </p>
<p> or </p>
<p> gammu savesms TEXT -len 400 -text &quot;All your base are belong to us&quot; </p>
<p> or </p>
<p> gammu savesms EMS -text &quot;All your base are belong to us&quot; </p>
<dt>Save some funky message with predefined sound and animation from 2 bitmaps:</p>
<dd>
<p> gammu savesms EMS -text &quot;Greetings&quot; -defsound 1 -text &quot;from Gammu&quot; -tone10 axelf.txt -animation 2 file1.bmp file2.bmp </p>
<dt>Save protected message with ringtone:</p>
<dd>
<p> gammu savesms EMS -protected 2 -variablebitmaplong ala.bmp -toneSElong axelf.txt -toneSE ring.txt </p>
</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2003-2009 Marcin Wiacek, Michal Cihar and other authors. License GPLv2: GNU GPL version 2 &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">http://www.gnu.org/licenses/old-licenses/gpl-2.0.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law. </p>
<h2>REPORTING BUGS</h2>
<p> There are definitely many bugs, reporting to author is welcome. Please include some useful information when sending bug reports (especially debug logs, operating system, it&#8217;s version and phone information are needed). </p>
<p> To generate debug log, enable it in gammurc (alternatively you can do it on command line using -d textall -f /tmp/gammu.log): </p>
<p>&nbsp;<wbr>[gammu]<br />
&nbsp;<wbr>&#8230;your connection settings&#8230;<br />
&nbsp;<wbr>logfile&nbsp;<wbr>=&nbsp;<wbr>/tmp/gammu.log<br />
&nbsp;<wbr>logformat&nbsp;<wbr>=&nbsp;<wbr>textall </p>
<p> With this settings, Gammu generates /tmp/gammu.log on each connection to phone and stores dump of communication there. You can also find some hints for improving support for your phone in this log. </p>
<p> Please report bugs to &lt;<a rel="nofollow" href="http://bugs.cihar.com">http://bugs.cihar.com</a>&gt;. </p>
<h2>AUTHOR</h2>
<p> You can contact authors on &lt;gammu-users [at] lists.sourceforge.net&gt;. </p>
<p> <i>Michal Cihar</i> &lt;michal [at] cihar.com&gt; is current project maintainer and contributor of most of AT and OBEX code. </p>
<p> <i>Marcin Wiacek</i> &lt;marcin [at] mwiacek.com&gt; is project iniciator and contributor of most Nokia code. </p>
<p> As this project grew from Gnokii, we would like to thanks all Gnokii developers, especially <i>Pavel Janik</i>, <i>Pawel Kot</i> and <i>Manfred Jonsson</i> (see CREDITS from Gnokii for all their contributor). </p>
<p> Many other people have helped with various features, check ChangeLog for more details. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gammu-smsd/">gammu-smsd</a>(1), <a href="/docs/linux/man/1-gammu-smsd-inject/">gammu-smsd-inject</a>(1), <a href="/docs/linux/man/5-gammurc/">gammurc</a>(5), <a href="/docs/linux/man/1-jadmaker/">jadmaker</a>(1) </p>
<p> Some more hints can be found in README file or on wiki &lt;<a rel="nofollow" href="http://www.gammu.org/">http://www.gammu.org/</a>&gt;. </p>
<p> Related programs which can be used with GSM modem: </p>
<p> <a href="/docs/linux/man/1-cu/">cu</a>(1), <a href="/docs/linux/man/1-gnokii/">gnokii</a>(1), <a href="/docs/linux/man/1-minicom/">minicom</a>(1) </p>
<p> Graphical interfaces for Gammu: </p>
<p> <a href="/docs/linux/man/1-wammu/">wammu</a>(1), <a href="/docs/linux/man/1-gmobilemedia/">gmobilemedia</a>(1) </p>
<h2>Index</h2>
