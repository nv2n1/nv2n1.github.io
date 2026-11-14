---
title: "gnokii(1)"
name: "gnokii"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnokii/"
description: "gnokii – tool suite for mobile phones"
---

<h2>NAME</h2>
<p> gnokii &#8211; tool suite for mobile phones</p>
<h2>SYNOPSIS</h2>
<p> <code>gnokii</code> <i>[CONFIG OPTIONS]</i> [<i>OPTIONS</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>gnokii</code> is a multiple systems tool suite and driver for mobile phones. </p>
<p> <code>gnokii</code> supports the AT protocol defined by the GSM standard (with workarounds for some vendor&#8217;s quirks), some proprietary protocols of Nokia phones (the so called FBUS and FBUS2) and SIM cards in PC/SC compatible Smart Card readers. Limited support for the older and slow Nokia MBUS protocol is also available. </p>
<p> You can assume that your phone will work with <code>gnokii</code> when using the AT protocol, however some phones implement only a subset of the protocol and in those cases you will get very limited functionality. The recommended model setting for your config file are:<br />
&nbsp;<wbr>&#8211; model&nbsp;<wbr>=&nbsp;<wbr>series40, if you have a fairly recent Nokia phone except Symbian phones prior to Series60 3rd Edition<br />
&nbsp;<wbr>&#8211; model&nbsp;<wbr>=&nbsp;<wbr>gnapplet, if you have a Nokia Symbian Series60 prior to 3rd Edition phone<br />
&nbsp;<wbr>&#8211; model&nbsp;<wbr>=&nbsp;<wbr>AT, for all other phones of any brand<br />
&nbsp;<wbr>&#8211; if you have some older Nokia phone that doesn&#8217;t work with model&nbsp;<wbr>=&nbsp;<wbr>series40 you may try using its brand name, eg. for Nokia 6210 use <i>model = 6210</i>. </p>
<p> The recommended connection and port settings for your config file are:<br />
&nbsp;<wbr>&#8211; connection&nbsp;<wbr>=&nbsp;<wbr>bluetooth and port&nbsp;<wbr>=&nbsp;<wbr>phone address, for Bluetooth connections<br />
&nbsp;<wbr>&#8211; connection&nbsp;<wbr>=&nbsp;<wbr>dku2libusb and port&nbsp;<wbr>=&nbsp;<wbr>1, for most Nokia USB cables<br />
&nbsp;<wbr>&#8211; connection&nbsp;<wbr>=&nbsp;<wbr>serial and port&nbsp;<wbr>=&nbsp;<wbr>/dev/&#8230;, for all other cables </p>
<p> See also the sample gnokiirc for a description of all configuration parameters and our &lt;<a rel="nofollow" href="http://wiki.gnokii.org/index.php/Config">http://wiki.gnokii.org/index.php/Config</a>&gt; for configurations known to work. </p>
<p> Symbian series60 3rd edition and later (most Nokia N and E series) are not supported by the gnapplet driver due to changes in Symbian API. For now you can get some functionality using the AT driver (with all connection types supported by the phone) or using the series40 driver (only with connection = dku2libusb). </p>
<p> Please note that currently there are Nokia models with almost the same names as the old ones, like 6110c vs 6110 or 3110c vs 3110. They are completly incompatible. DO NOT use <i>model = 6110</i> or <i>model = 3110</i> setting for them, use <i>model = series40</i> instead. </p>
<h2>CONFIG OPTIONS</h2>
<dl>
<dt><code>&#8211;config </code><i>filename</i></p>
<dd> reads configuration from <i>filename</i> instead of trying default locations. Normally gnokii looks for config file in <i>$XDG_CONFIG_HOME/gnokii/config</i> (which is usually <i>$HOME/.config/gnokii/config</i>), <i>$HOME/.gnokiirc</i> (legacy), <i>$XDG_CONFIG_DIRS/gnokii/config</i> (which is usually <i>/etc/xdg/gnokii/config</i>) and <i>/etc/gnokiirc</i> (legacy).</p>
<dt><code>&#8211;phone </code><i>name</i></p>
<dd> usees parameters from the given phone section of your config file. A phone section named &#8216;foo&#8217; starts with [phone_foo] and is used as &#8211;phone foo </p>
</dl>
<h2>OPTIONS</h2>
<p> The options that are recognized by <code>gnokii</code> can be divided into several different groups. </p>
<h3>GENERAL</h3>
<dl>
<dt><code>&#8211;help</code></p>
<dd> displays usage information.</p>
<dt><code>&#8211;version</code></p>
<dd> displays version and copyright information.</p>
<dt><code>&#8211;monitor [</code><i>delay</i>|<i>once</i>]</p>
<dd> continually updates phone status to stderr. Optional <i>delay</i> parameter sets the refresh interval to <i>delay</i> seconds. Default is 1. <i>once</i> means the output will be printed only once.</p>
<dt><code>&#8211;shell</code></p>
<dd> runs interactive session that will allow to run sequent gnokii commands without a need to reconnect for the sequent commands. </p>
</dl>
<h3>DIALING</h3>
<dl>
<dt><code>&#8211;getspeeddial </code><i>location</i></p>
<dd> reads speed dial from the specified location.</p>
<dt><code>&#8211;setspeeddial </code><i>number</i> <i>memory_type</i> <i>location</i></p>
<dd> specify speed dial. <i>location</i> number 1 is usually reserved for voice mailbox number and it is unavailable as speed dial.</p>
<dt><code>&#8211;dialvoice </code><i>number</i></p>
<dd> initiate voice call. On success print the <i>callid</i> identifier to be used with the &#8211;hangup command. The &#8211;monitor command can be used to show the <i>callid</i>. </p>
<p> With <i>model = AT</i> direct dialing from phonebooks is supported with careful use of shell quoting, for example:<br />
&nbsp;<wbr>gnokii &#8211;dialvoice&nbsp;<wbr>&quot;&gt;SM42&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>dial the number in location 42 of SM memory<br />
&nbsp;<wbr>gnokii &#8211;dialvoice&nbsp;<wbr>&#8216;&gt;&quot;Home&quot;&#8217;&nbsp;<wbr>#&nbsp;<wbr>dial the number if string matches exactly a contact name&nbsp;<wbr>(note the use of single and double quotes)</p>
<dt><code>&#8211;senddtmf </code><i>string</i></p>
<dd> send DTMF sequence.</p>
<dt><code>&#8211;answercall</code> <i>callid</i></p>
<dd> answer an incoming call. <i>callid</i> is a small integer number used to identify one of the incoming calls. The &#8211;monitor command can be used to show the <i>callid</i>.</p>
<dt><code>&#8211;hangup</code> <i>callid</i></p>
<dd> hangup an incoming call or an already established call. <i>callid</i> is a small integer number used to identify one of the incoming calls. If you initiated the call with &#8211;dialvoice this is the number printed by that command. The &#8211;monitor command can be used to show the <i>callid</i>.</p>
<dt><code>&#8211;divert {&#8211;op|-o} {register|enable|query|disable|erasure} {&#8211;type|-t} {all|busy|noans|outofreach|notavail} {&#8211;call|-c} {all|voice|fax|data} [{&#8211;timeout|-m} </code><i>time_in_seconds</i>] [{&#8211;number|-n} <i>number</i>]</p>
<dd> Manage call diverting/forwarding. </p>
<p> <code>&#8211;op</code> specifies one of the operations: <code>register enable query disable erasure </code> </p>
<p> <code>&#8211;type</code> specifies one of the event types: <code>busy noans outofreach notavail unconditional all</code> </p>
<p> <code>&#8211;call</code> specifies one of the call types: <code>voice fax data all</code> </p>
<p> <code>&#8211;timeout</code> is the number of seconds an incoming call will ring before being forwarded to the registered number (use with &#8211;type noans) </p>
<p> <code>&#8211;number</code> is the phone number to which calls are to be forwarded </p>
</dl>
<h3>PHONE SETTINGS</h3>
<dl>
<dt><code>&#8211;getdisplaystatus</code></p>
<dd> shows what icons are displayed.</p>
<dt><code>&#8211;displayoutput</code></p>
<dd> show texts displayed in phone&#8217;s screen.</p>
<dt><code>&#8211;getprofile [</code><i>number</i>]</p>
<dd> show settings for selected(all) profile(s).</p>
<dt><code>&#8211;setprofile</code></p>
<dd> sets settings for selected(all) profile(s).</p>
<dt><code>&#8211;getactiveprofile</code></p>
<dd> reads the active profile.</p>
<dt><code>&#8211;setactiveprofile </code><i>profile_no</i></p>
<dd> sets active profile to the profile number <i>profile_no</i>.</p>
<dt><code>&#8211;netmonitor {</code><i>reset</i>|<i>off</i>|<i>field</i>|<i>devel</i>|<i>next</i>|<i>nr</i>}</p>
<dd> setting/querying netmonitor mode.</p>
<dt><code>&#8211;reset [</code><i>soft</i>|<i>hard</i>]</p>
<dd> resets the phone. By default a <i>soft</i> reset is performed. Depending on phone, the <i>hard</i> option also deletes everything in the internal memory and restores the factory settings. </p>
</dl>
<h3>TODO</h3>
<dl>
<dt><code>&#8211;gettodo </code><i>start_number</i> [<i>end_number</i>|<i>end</i>] [-v|&#8211;vCal]</p>
<dd> get the notes with numbers from <i>start_number</i> to <i>end_number</i> from ToDo list. <i>end</i> is a keyword that denotes &#8216;everything till the end&#8217;. </p>
<p> -v | &#8211;vCal &#8211; output in vCalendar 1.0 format</p>
<dt><code>&#8211;writetodo </code><i>vcalfile</i> <i>start_number</i> [<i>end_number</i>|<i>end</i>]</p>
<dd> write the notes with numbers from <i>start_number</i> to <i>end_number</i> from vCalendar file <i>vcalfile</i> to ToDo list. More than one note a time can be saved. <i>end</i> is a keyword that denotes &#8216;everything till the end&#8217;. </p>
<p> number &#8211; location of the note in the vCalendar file</p>
<dt><code>&#8211;deletealltodos</code></p>
<dd> delete all notes from the ToDo list. </p>
</dl>
<h3>CALENDAR</h3>
<dl>
<dt><code>&#8211;getcalendarnote </code><i>start_number</i> [<i>end_number</i>|<i>end</i>] [-v|&#8211;vCal]</p>
<dd> get the notes with numbers from <i>start_number</i> to <i>end_number</i> from calendar. <i>end</i> is a keyword that denotes &#8216;everything till the end&#8217;. </p>
<p> -v | &#8211;vCal &#8211; output in vCalendar 1.0 format</p>
<dt><code>&#8211;writecalendarnote </code><i>vcalfile</i> <i>start_number</i> [<i>end_number</i>|<i>end</i>]</p>
<dd> write the notes with numbers from <i>start_number</i> to <i>end_number</i> from vCalendar file <i>vcalfile</i> to a phone calendar. More than one note a time can be saved. <i>end</i> is a keyword that denotes &#8216;everything till the end&#8217;. </p>
<p> number &#8211; location of the note in the vCalendar file</p>
<dt><code>&#8211;deletecalendarnote </code><i>start_number</i> [<i>end_number</i>|<i>end</i>]</p>
<dd> delete the notes with numbers from <i>start_number</i> to <i>end_number</i> from calendar. <i>end</i> is a keyword that denotes &#8216;everything till the end&#8217;. </p>
</dl>
<h3>SMS</h3>
<dl>
<dt><code>&#8211;getsms </code><i>memory_type</i> <i>start</i> [<i>end</i>] [-f|&#8211;file <i>file</i>] [-F|&#8211;force-file <i>file</i>] [-a|&#8211;append-file <i>file</i>] [-d|&#8211;delete]</p>
<dd> gets SMS messages from specified <i>memory type</i> starting at entry <i>start</i> and ending at <i>end</i> and print them to stdout by default. <i>end</i> can be a number or the string &#8216;end&#8217;. If <i>end</i> is not specified only one location &#8211; <i>start</i> is read.</p>
<dt>
<dd> For the <i>memory types</i> you usually use <i>IN</i> (Inbox) and <i>OU</i> (Outbox) for Nokias and <i>SM</i> (SIM card) and <i>ME</i> (phone memory) for other brands, except for modern Motorolas that prefer <i>MT</i> (combined SIM and phone memory); in any case the <code>&#8211;showsmsfolderstatus</code> command shows the list of <i>memory types</i> available in your phone with their descriptions and message counts (each part of multipart messages is counted separately).</p>
<dt>
<dd> -f | &#8211;file <i>file</i> &#8211; save messages to <i>file</i> in mbox format. If <i>file</i> already exists, user is prompted whether to overwrite it</p>
<dt>
<dd> -F | &#8211;force-file <i>file</i> &#8211; save messages to <i>file</i> in mbox format. If <i>file</i> already exists, it is overwritten without asking</p>
<dt>
<dd> -a | &#8211;append-file <i>file</i> &#8211; save messages to <i>file</i> in mbox format. If <i>file</i> already exists, messages are added to the end</p>
<dt>
<dd> -d | &#8211;delete &#8211; delete message after reading.</p>
<dt><code>&#8211;deletesms </code><i>memory_type</i> <i>start</i> [<i>end</i>]</p>
<dd> deletes SMS messages from specified <i>memory type</i> starting at entry <i>start</i> and ending at <i>end</i>. If <i>end is not specified only one location &#8211; start</i> is deleted.</p>
<dt><code>&#8211;sendsms </code><i>destination</i> [&#8211;smsc <i>message_center_number</i> | &#8211;smscno <i>message_center_index</i>] [-r|&#8211;report] [-8|&#8211;8bit] [-C|&#8211;class <i>n</i>] [-v|&#8211;validity <i>n</i>] [-i|&#8211;imelody] [-a|&#8211;animation <i>file;file;file;file</i>] [-o|&#8211;concat <i>this;total;serial</i>] [-w|&#8211;wappush <i>url</i>]</p>
<dd> sends an SMS message to <i>destination</i> via <i>message_center_number</i> or SMSC number taken from phone memory from address <i>message_center_index</i>. If this argument is omitted SMSC number is taken from phone memory from location 1. Message text is taken from STDIN. Meaning of other optional parameters: </p>
<p> -r | &#8211;report &#8211; request for delivery report </p>
<p> -8 | &#8211;8bit &#8211; set 8bit coding </p>
<p> -C | &#8211;class <i>n</i> &#8211; Class Message <i>n</i>, where <i>n</i> can be 0..3 </p>
<p> -v | &#8211;validity <i>n</i> &#8211; validity in minutes </p>
<p> -i | &#8211;imelody &#8211; send iMelody within SMS </p>
<p> -a | &#8211;animation <i>file;file;file;file</i> &#8211; send animation message </p>
<p> -o | &#8211;concat <i>this;total;serial</i> &#8211; send <i>this</i> part of all <i>total</i> parts identified by <i>serial</i> </p>
<p> -w | &#8211;wappush <i>url</i> &#8211; send wappush to the given <i>url</i></p>
<dt>Sample usage:</p>
<dd> echo &quot;This is a test message&quot; | gnokii &#8211;sendsms +48501123456 -r </p>
<dt><code>&#8211;savesms [&#8211;sender </code><i>from</i>] [&#8211;smsc <i>message_center_number</i> | &#8211;smscno <i>message_center_index</i>] [&#8211;folder <i>folder_id</i>] [&#8211;location <i>number</i>] [&#8211;sent | &#8211;read] [&#8211;deliver] [&#8211;datetime <i>YYMMDDHHMMSS</i>]</p>
<dd> saves SMS messages to phone. Messages are read from STDIN. You can specify the following optional arguments: </p>
<p> &#8211;sender &#8211; set the sender number (only <i>&#8211;deliver</i>) </p>
<p> &#8211;smsc <i>message_center_number</i> &#8211; set the SMSC number (only <i>&#8211;deliver</i>) </p>
<p> &#8211;smscno <i>message_center_index</i> &#8211; SMSC number taken from phone memory from address <i>message_center_index</i> (only <i>&#8211;deliver</i>) </p>
<p> &#8211;folder <i>folder_id</i> &#8211; folder ID where to save the SMS to (only valid for newer phones, i.e. 6210/6510 series). For legal values see <i>&#8211;getsms</i>. </p>
<p> &#8211;location <i>number</i> &#8211; save the message to location <i>number</i> </p>
<p> &#8211;sent | &#8211;read &#8211; mark the message saved/read depending on <i>&#8211;deliver</i> </p>
<p> &#8211;deliver &#8211; set the message type to SMS_Deliver </p>
<p> &#8211;datetime <i>YYMMDDHHMMSS</i> &#8211; sets datetime of delivery, i.e. 031123185713 would set message delivery time to 23rd November 2003, 6:57:13 PM </p>
<dt><code>&#8211;getsmsc [</code><i>start_number</i> [<i>end_number</i>]] [-r|&#8211;raw]</p>
<dd> show the SMSC parameters from specified location(s) or for all locations. </p>
<p> -r | &#8211;raw &#8211; output in a format suitable for &#8211;setsmsc </p>
<dt><code>&#8211;setsmsc</code></p>
<dd> set SMSC parameters read from STDIN. See <i>&#8211;raw</i> output of <i>&#8211;getsmsc</i> for syntax. </p>
<dt><code>&#8211;createsmsfolder </code><i>name</i></p>
<dd> create SMS folder with name <i>name</i>. </p>
<dt><code>&#8211;deletesmsfolder </code><i>number</i></p>
<dd> delete folder # <i>number</i> of &#8216;My Folders&#8217;. </p>
<dt><code>&#8211;showsmsfolderstatus</code></p>
<dd> list SMS folder names with <i>memory types</i> and total number of messages available. </p>
<dt><code>&#8211;smsreader</code></p>
<dd> keeps reading incoming SMS and saves them into the mailbox. </p>
</dl>
<h3>MMS</h3>
<dl>
<dt><code>&#8211;getmms </code><i>memory_type</i> <i>start</i> [<i>end</i>] [{&#8211;pdu|&#8211;raw} <i>file</i>] [-o|&#8211;overwrite]</p>
<dd> gets MMS messages from specified <i>memory type</i> starting at entry <i>start</i> and ending at <i>end</i>. Default output format is human readable, alternative output formats are &#8211;pdu which is the binary format of MMS as received by the phone from the network and &#8211;raw which saves the data as read from the phone. </p>
<p> When the -o or &#8211;overwrite option is used, existing files are overwritten without asking. </p>
<dt><code>&#8211;deletemms </code><i>memory_type</i> <i>start</i> [<i>end</i>]</p>
<dd> deletes MMS messages from specified <i>memory type</i> starting at entry <i>start</i> and ending at <i>end</i>. If <i>end is not specified only one location &#8211; start</i> is deleted. </p>
</dl>
<h3>LOGOS</h3>
<dl>
<dt><code>&#8211;sendlogo {caller|op|picture} </code><i>destination</i> <i>logofile</i> [<i>network_code</i>]</p>
<dd> send the <i>logofile</i> to <i>destination</i> as operator or CLI logo.</p>
<dt><code>&#8211;setlogo op [</code><i>logofile</i> [<i>network_code</i>]]</p>
<dd>
<dt><code>&#8211;setlogo startup [</code><i>logofile</i>]</p>
<dd>
<dt><code>&#8211;setlogo caller [</code><i>logofile</i> [<i>caller_group_number</i> [<i>group_name</i>]]]</p>
<dd> set or clear operator, startup or caller logo.</p>
<dt><code>&#8211;setlogo {dealer|text} [</code><i>text</i>]</p>
<dd> set or clear welcome note.</p>
<dt><code>&#8211;getlogo op [</code><i>logofile</i> [<i>network_code</i>]]</p>
<dd>
<dt><code>&#8211;getlogo startup [</code><i>logofile</i> [<i>network_code</i>]]</p>
<dd>
<dt><code>&#8211;getlogo caller [</code><i>caller_group_number</i> [<i>logofile</i> [<i>network_code</i>]]]</p>
<dd> get operator, startup or caller logo.</p>
<dt><code>&#8211;getlogo {dealer|text}</code></p>
<dd> get welcome note.</p>
<dt><code>&#8211;viewlogo </code><i>logofile</i></p>
<dd> print the <i>logofile</i> as ASCII art. Formats that are automatically detected are: NOL, NGG, NSM, NLM, BMP, I61, GGP, XPM. The OTA format can be used only if the filename ends with the .otb extension.</dl>
<p> Format of <i>network_code</i> parameter is 3 digits MCC, a space, 2 digits MNC surrounded by single or double quotes, eg. &quot;123 45&quot;. </p>
<h3>RINGTONES</h3>
<dl>
<dt><code>&#8211;sendringtone </code><i>destination rtttlfile</i></p>
<dd> send the <i>rtttlfile</i> to <i>destination</i> as ringtone.</p>
<dt><code>&#8211;setringtone </code><i>rtttlfile</i></p>
<dd> set the <i>rtttlfile</i> as ringtone (on 6110). </p>
</dl>
<h3>PHONEBOOK</h3>
<dl>
<dt><code>&#8211;getphonebook </code><i>memory_type</i> <i>start_number</i> [<i>end_number|end</i>] [<i>[-r|&#8211;raw]|[-v|&#8211;vcard]|[-l|&#8211;ldif]</i>]</p>
<dd> reads specified memory location from phone. If <i>end_number</i> is not specified only one location &#8211; <i>start</i> is read. If instead of <i>end_number</i> the text <i>end</i> is specified then gnokii will read from <i>start_number</i> until it encounters a non-existant location. Valid <i>memory types</i> are ME, SM, FD, ON, EN, DC, RC, MC, LD:</p>
<dt>
<dd> <code>ME</code> Internal memory of the mobile equipment</p>
<dt>
<dd> <code>SM</code> SIM card memory</p>
<dt>
<dd> <code>FD</code> Fixed dial numbers</p>
<dt>
<dd> <code>ON</code> Own numbers</p>
<dt>
<dd> <code>EN</code> Emergency numbers</p>
<dt>
<dd> <code>DC</code> Dialled numbers</p>
<dt>
<dd> <code>RC</code> Received calls</p>
<dt>
<dd> <code>MC</code> Missed calls</p>
<dt>
<dd> <code>LD</code> Last dialed numbers</dl>
<p> Normally you get human readable output. Please note, that it is not compatible with expected input by <i>&#8211;writephonebook</i>. You can use <i>-v</i> or <i>&#8211;vcard</i> switch to get output in vCard format or <i>-l</i> or <i>&#8211;ldif</i> switch to get output in ldif format or <i>-r</i> or <i>&#8211;raw</i> switch to get the raw output which is explained below. You can use it then with <i>&#8211;writephonebook</i>.</p>
<dl>
<dt><code>&#8211;writephonebook [</code><i>-o|&#8211;overwrite] [-f|&#8211;find-free] [-m|&#8211;memory-type|&#8211;memory memory_type] [-n|&#8211;memory-location|&#8211;location number] [[-v|&#8211;vcard]|[-l|&#8211;ldif]</i>]</p>
<dd> reads data from stdin and writes to phonebook. Uses the format as provided by the output of the getphonebook command using <i>&#8211;raw</i> or <i>&#8211;vcard</i> or <i>&#8211;ldif</i>. Default is raw format (see below for details) and alternate formats are vCard and ldif. Default <i>&#8211;getphonebook</i> output format is not compatible with <i>&#8211;writephonebook</i>.</dl>
<p> With <i>&#8211;memory-type memory_type</i> and <i>&#8211;memory-location number</i> you can set a memory type and a location if the input data doesn&#8217;t specify them. </p>
<p> When the -o or &#8211;overwrite option is used, existing entries at a given location are overwritten. </p>
<p> When the -f or &#8211;find-free option is given, <code>gnokii</code> tries to find a free location. In this case, you can omit the location field in the input data. </p>
<p> The raw phonebook format is very simple. Each line represents one entry. Fields are separated by semicolons. Semicolons aren&#8217;t allowed inside a field. The fields have to be in this order (the subentries are optional, ie. you can repeat all subentry field multiple times, but they have to be alltogether in the given order):</p>
<dl>
<dt>
<dd> name</p>
<dt>
<dd> number</p>
<dt>
<dd> memory_type</p>
<dt>
<dd> entry_location</p>
<dt>
<dd> caller_group_number</p>
<dt>
<dd> subentry_type</p>
<dt>
<dd> subentry_number_type</p>
<dt>
<dd> subentry_id</p>
<dt>
<dd> subentry_text</dl>
<p> Possible values of <code>caller_group_number</code> and the corresponding caller groups are (these are defaults, you are able to change these manually in your phone):</p>
<dl>
<dt>
<dd> <code>0</code> Family</p>
<dt>
<dd> <code>1</code> VIP</p>
<dt>
<dd> <code>2</code> Friends</p>
<dt>
<dd> <code>3</code> Colleagues</p>
<dt>
<dd> <code>4</code> Other</p>
<dt>
<dd> <code>5</code> No group</p>
<dt>
<dd></dl>
<p> Possible subentry types are described in the <i>gnokii/common.h</i> file:</p>
<dl>
<dt>
<dd> <code>7</code> subentry is the name</p>
<dt>
<dd> <code>8</code> subentry is the email address</p>
<dt>
<dd> <code>9</code> subentry is the postal address (snail mail)</p>
<dt>
<dd> <code>10</code> subentry is the note (text field)</p>
<dt>
<dd> <code>11</code> subentry is the number</p>
<dt>
<dd> <code>12</code> subentry is the ringtone</p>
<dt>
<dd> <code>19</code> subentry is the date (used for DC, RD, LD)</p>
<dt>
<dd> <code>26</code> subentry is the pointer (pointer to the other memory)</p>
<dt>
<dd> <code>27</code> subentry is the logo (bitmap)</p>
<dt>
<dd> <code>28</code> subentry is the logo switch</p>
<dt>
<dd> <code>30</code> subentry is the group (octect)</p>
<dt>
<dd> <code>44</code> subentry is the URL</p>
<dt>
<dd> <code>47</code> subentry is the location (octect)</p>
<dt>
<dd> <code>51</code> subentry is the image (file id)</p>
<dt>
<dd> <code>55</code> subentry is the ringtoneadv (file id or ringtone)</p>
<dt>
<dd> <code>56</code> subentry is the userid</p>
<dt>
<dd> <code>63</code> subentry is the pttaddress</p>
<dt>
<dd> <code>67</code> subentry is the extgroup</p>
<dt>
<dd> <code>69</code> subentry is the video (file id)</p>
<dt>
<dd> <code>70</code> subentry is the firstname</p>
<dt>
<dd> <code>71</code> subentry is the lastname</p>
<dt>
<dd> <code>74</code> subentry is the postaladdress</p>
<dt>
<dd> <code>75</code> subentry is the extendedaddress</p>
<dt>
<dd> <code>76</code> subentry is the street</p>
<dt>
<dd> <code>77</code> subentry is the city</p>
<dt>
<dd> <code>78</code> subentry is the stateprovince</p>
<dt>
<dd> <code>79</code> subentry is the zipcode</p>
<dt>
<dd> <code>50</code> subentry is the country</p>
<dt>
<dd> <code>82</code> subentry is the formalname</p>
<dt>
<dd> <code>84</code> subentry is the jobtitle</p>
<dt>
<dd> <code>85</code> subentry is the company</p>
<dt>
<dd> <code>86</code> subentry is the nickname</p>
<dt>
<dd> <code>87</code> subentry is the birthday</dl>
<p> Possible subentry number types are described in the <i>gnokii/common.h</i> file:</p>
<dl>
<dt>
<dd> <code>2</code> number is the home phone number</p>
<dt>
<dd> <code>3</code> number is the mobile phone number</p>
<dt>
<dd> <code>4</code> number is the fax number</p>
<dt>
<dd> <code>6</code> number is the work phone number</p>
<dt>
<dd> <code>10</code> number is the general number</dl>
<p> For the subentry types that don&#8217;t care about number type (as text files) this should be set to 0.</p>
<dl>
<dt><code>&#8211;deletephonebook </code><i>memory_type</i> <i>start_number</i> [<i>end_number|end</i>]</p>
<dd> delete entries with <i>start_number</i> to <i>end_number</i> from the phone book in <i>memory_type</i>. <i>end</i> is a keyword that denotes &#8216;everything till the end&#8217;. </p>
</dl>
<h3>WAP</h3>
<dl>
<dt><code>&#8211;getwapbookmark </code><i>number</i></p>
<dd> reads the specified WAP bookmark from phone</p>
<dt><code>&#8211;writewapbookmark </code><i>name</i> <i>URL</i></p>
<dd> write WAP bookmark to phone</p>
<dt><code>&#8211;deletewapbookmark </code><i>number</i></p>
<dd> delete WAP bookmark from phone</p>
<dt><code>&#8211;getwapsetting </code><i>number</i> [<i>-r|&#8211;raw</i>]</p>
<dd> read WAP setting from phone</p>
<dt><code>&#8211;writewapsetting</code></p>
<dd> reads data from stdin and writes it to phone. Hint: see syntax from <i>&#8211;getwapsetting</i> <i>-r</i> option</p>
<dt><code>&#8211;activatewapsetting </code><i>number</i></p>
<dd> activate WAP setting <i>number</i> </p>
</dl>
<h3>DATE, TIME AND ALARM</h3>
<dl>
<dt><code>&#8211;setdatetime [</code><i>YYYY</i> [<i>MM</i> [<i>DD</i> [<i>HH</i> [<i>MM</i>]]]]]</p>
<dd> set the date and the time of the phone.</p>
<dt><code>&#8211;getdatetime</code></p>
<dd> shows current date and time in the phone.</p>
<dt><code>&#8211;setalarm </code><i>HH</i> <i>MM</i></p>
<dd> set the alarm of the phone.</p>
<dt><code>&#8211;getalarm</code></p>
<dd> shows current alarm. </p>
</dl>
<h3>SECURITY</h3>
<dl>
<dt><code>&#8211;identify</code></p>
<dd> get IMEI, manufacturer, model, product name and revision.</p>
<dt><code>&#8211;entersecuritycode {</code><i>PIN</i>|<i>PIN2</i>|<i>PUK</i>|<i>PUK2</i>|<i>SEC</i>}</p>
<dd> asks for the code and sends it to the phone. Code is read from terminal or from stdin.</p>
<dt><code>&#8211;getsecuritycode</code></p>
<dd> shows the currently set security code.</p>
<dt><code>&#8211;getsecuritycodestatus</code></p>
<dd> show if a security code is needed.</p>
<dt><code>&#8211;getlocksinfo</code></p>
<dd> show information about the (sim)locks of the phone: the lock data, whether a lock is open or closed, whether it is a user or factory lock and the number of unlock attempts. </p>
</dl>
<h3>FILE</h3>
<p> Note that some phones (like Nokia 6610i) support only id based operations (gnokii options with &quot;byid&quot; suffix). Use gnokiifs for the transparent support.</p>
<dl>
<dt><code>&#8211;getfilelist </code><i>remote_path</i></p>
<dd> lists files from the given directory. Use A:\* or B:\* to get the root directory from either phone memory or card memory.</p>
<dt><code>&#8211;getfiledetailsbyid [</code><i>id</i>]</p>
<dd> lists file details or directory contents from the entry identified by <i>id</i>. If no identifier is given, list the root directory contents.</p>
<dt><code>&#8211;getfileid </code><i>remote_filename</i></p>
<dd> gets id of the file.</p>
<dt><code>&#8211;getfile </code><i>remote_filename</i> [<i>local_filename</i>]</p>
<dd> gets file identified by name and path from the phone and stores it at the local computer.</p>
<dt><code>&#8211;getfilebyid </code><i>id</i> [<i>local_filename</i>]</p>
<dd> gets file identified by id from the phone and stores it at the local computer.</p>
<dt><code>&#8211;getallfiles </code><i>remote_path</i></p>
<dd> gets all files from the remote path.</p>
<dt><code>&#8211;putfile </code><i>local_filename</i> <i>remote_filename</i></p>
<dd> stores the file in the phone memory or on the memory card.</p>
<dt><code>&#8211;deletefile </code><i>remote_filename</i></p>
<dd> removes the file from the phone.</p>
<dt><code>&#8211;deletefilebyid </code><i>id</i></p>
<dd> removes the file from the phone. </p>
</dl>
<h3>MISC</h3>
<dl>
<dt><code>&#8211;keysequence</code></p>
<dd> emulates pressing keys on phone keyboard. Input is read from stdin.</p>
<dt>
<dd> Supported keys (any other char is ignored):</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>M</code> menu</p>
<dt>
<dd> <code>N</code> names</p>
<dt>
<dd> <code>P</code> power</p>
<dt>
<dd> <code>G</code> green phone</p>
<dt>
<dd> <code>R</code> red phone</p>
<dt>
<dd> <code>U</code> up</p>
<dt>
<dd> <code>D</code> down</p>
<dt>
<dd> <code>+</code> increase volume</p>
<dt>
<dd> <code>&#8211;</code> decrease volume</p>
<dt>
<dd> <code>0123456789#*</code> as is</dl>
</dl>
<dt>
<dd> Example: to increase volume</p>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>echo&nbsp;<wbr>&quot;+&quot;&nbsp;<wbr>| gnokii &#8211;keysequence</p>
<dt>
<dd> Note: this command isn&#8217;t supported by all phones/drivers. </p>
<dt><code>&#8211;enterchar</code></p>
<dd> emulates typing a character on phone keyboard. By emulating multiple pressions of keys, it can input all characters supported by the phone in use, but to input an SMS predictive text should be disabled. Input is read from stdin, with newline interpreted as the &quot;Menu&quot; key and escape interpreted as the &quot;Names&quot; key.</p>
<dt>
<dd> Note: this command isn&#8217;t supported by all phones/drivers. </p>
<dt><code>&#8211;listnetworks</code></p>
<dd> prints a list of cellular network operators with their 3-digits MCC (Mobile country code) and 2-digits MNC (Mobile Network Code).</p>
<dt>
<dd> Note: this command doesn&#8217;t need a valid config or a phone to work. </p>
<dt><code>&#8211;getnetworkinfo</code></p>
<dd> prints information about the network currently in use. </p>
</dl>
<h2>DIAGNOSTICS</h2>
<p> Various error messages are printed to standard error. The exit code is 0 for correct functioning. Errors which appear to be caused by invalid or abused command line parameters cause an exit code of 2, and other errors cause an exit code of 1. </p>
<h2>BUGS</h2>
<p> We write quality software here ;) but see KNOWN_BUGS just in case. If you&#8217;d like to send us the bugreport please read the README and Bugs files. </p>
<h2>AUTHOR</h2>
<p> Hugh Blemings &lt;hugh at blemings dot org&gt;, Pavel Janik ml. &lt;Pavel.Janik at suse dot cz&gt; and Pawel Kot &lt;gnokii at gmail dot com&gt;. </p>
<p> Manual page written by Dag Wieers &lt;dag at mind dot be&gt;, Pawel Kot &lt;gnokii at gmail dot com&gt; and Daniele Forsi &lt;daniele at forsi dot it&gt;. </p>
<p> See also Docs/CREDITS from gnokii sources. </p>
<h2>COPYING</h2>
<p> This program is distributed under the GNU Public License Version 2, or (at your option) any later version. </p>
<h2>SEE ALSO</h2>
<p> gnokiid, xgnokii, mgnokiidev, ppm2nokia, sendsms, todologo </p>
<h2>Index</h2>
