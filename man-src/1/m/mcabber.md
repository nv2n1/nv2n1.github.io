---
title: "mcabber(1)"
name: "mcabber"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mcabber/"
---

<h2 class="name">NAME</h2>
 

 mcabber - a simple Jabber console client 

<h2>SYNOPSIS</h2>

 <i>mcabber</i> [ -h | -V | -f configfile ] 

<h2>DESCRIPTION</h2>

 <a HREF="/docs/linux/man/1-mcabber/">mcabber</a>(1) is a small Jabber console client. For now it needs a configuration file to start, so please copy the sample mcabberrc file and adapt your connection settings. 

 You also need to have an existing Jabber account to use this software, as it cannot (un)register accounts yet. 

 Here are some of the features of mcabber: 

 

<dl>
<dt>
<dd> * <i>SSL support</i>.</dl>
 

<dl>
<dt>
<dd> * <i>MUC support</i> (Multi-User Chat).</dl>
 

<dl>
<dt>
<dd> * <i>PGP support</i></dl>
 

<dl>
<dt>
<dd> * <i>Chat States</i> support (typing notifications)</dl>
 

<dl>
<dt>
<dd> * <i>History logging:</i> If enabled (see the CONFIGURATION FILE section), mcabber can save discussions to history log files.</dl>
 

<dl>
<dt>
<dd> * <i>Commands completion:</i> If possible, mcabber will try to complete your command line if you hit the Tab key.</dl>
 

<dl>
<dt>
<dd> * <i>Input line history:</i> Any message or command entered is in the input line history and can be reused easily.</dl>
 

<dl>
<dt>
<dd> * <i>External actions:</i> Some events (like receiving a message) can trigger an external action such as a shell script if you enable it in your configuration file. A sample events script (&quot;eventcmd&quot;) is provided with mcabber source code, in the contrib directory.</dl>

<h2>OPTIONS</h2>

 

 --help, -h
<dl>
<dt>
<dd> Quick help usage message</dl>
 

 -f configfile
<dl>
<dt>
<dd> Use configuration file <i>configfile</i></dl>

<h2>WINDOWS/PANES</h2>

 The <a HREF="/docs/linux/man/1-mcabber/">mcabber</a>(1) screen is divided into 4 regions. The <i>roster</i>, alias <i>buddylist</i>, is on the left. The <i>chat window</i>, or chat buffer, is on the right. The <i>input line</i> lies at the bottom of the screen, under a small <i>log window</i>. 

 Two status lines surround the log window. The bottom status line is the &quot;main status line&quot; and reflects mcabber general status. The other line is the &quot;chat status line&quot; and shows the status of the currently selected buddy. 

 To display buddies chat buffers, you will have to enter <i>chat mode</i>. You can enter chat mode by pressing enter, and leave chat mode with the ESC key. Simply sending a message will also enable chat mode. 

 There are several advantages to the two-mode implementation: first, it allows accurate &quot;unread&quot; message functionality, as described in the next section; without this, merely scrolling to a specific buddy will &quot;read&quot; the new messages of all buddies in-between. Second, it allows quickly hiding the conversation with a single keystroke. Third, it allows jumping between the few buddies with whom you are conversing with the <i>/roster alternate</i> command described in another section, without having to manually scroll back and forth. 

<h2>KEYS</h2>

 Text typing occurs in the <i>input line</i>; basic operations are supported (left arrow, right arrow, home/end keys, insert, delete, backspace...). 

 PageUp and PageDown keys are used to move in the roster. 

 Up and Down arrow keys can be used to move in the input line history; they jump to the previous/next line from the history beginning with the same string (from first column to the cursor column). 

 To send a message, move to the choosen buddy in the buddylist, type your message and hit enter. If the line begins with a slash, this will be interpreted as a command (see the COMMAND section below). Hit escape to leave the chat mode. 

 Here is a quick description of the key bindings: 

 <table> <tr VALIGN=top><td> Esc 

 </td><td> Disable chat mode 

 
</td></tr> <tr VALIGN=top><td> Ctrl-d 

 </td><td> Send/terminate a multi-line message 

 
</td></tr> <tr VALIGN=top><td> Ctrl-p/Ctrl-n 

 </td><td> Scroll up/down half a screen in the buffer window (chat mode) 

 
</td></tr> <tr VALIGN=top><td> Ctrl-Left 

 </td><td> Move the cursor back to the start of the current or previous word 

 
</td></tr> <tr VALIGN=top><td> Ctrl-Right 

 </td><td> Move the cursor forward to the end of the current or next word 

 
</td></tr> <tr VALIGN=top><td> Ctrl-u 

 </td><td> Delete from beginning of the line to the cursor 

 
</td></tr> <tr VALIGN=top><td> Ctrl-k 

 </td><td> Delete from the cursor to the end of line 

 
</td></tr> <tr VALIGN=top><td> Ctrl-w 

 </td><td> Backward kill word 

 
</td></tr> <tr VALIGN=top><td> Ctrl-t 

 </td><td> Transpose chars 

 
</td></tr> <tr VALIGN=top><td> Ctrl-o 

 </td><td> Accept line and put the next history line in the input line (accept-line-and-down-history) 

 
</td></tr> <tr VALIGN=top><td> Ctrl-a 

 </td><td> Go to the beginning of the input line 

 
</td></tr> <tr VALIGN=top><td> Ctrl-e 

 </td><td> Go to the end of the input line 

 
</td></tr> <tr VALIGN=top><td> Ctrl-l 

 </td><td> Force a refresh 

 
</td></tr> <tr VALIGN=top><td> Up/Down 

 </td><td> Move in the input line history 

 
</td></tr> <tr VALIGN=top><td> PgUp/PgDown 

 </td><td> Move inside the roster (buddylist) 

 
</td></tr> <tr VALIGN=top><td> Tab 

 </td><td> Complete current word, in the input line 

 
</td></tr> <tr VALIGN=top><td> Ctrl-g 

 </td><td> Cancel completion 

 
</td></tr> <tr VALIGN=top><td> Ctrl-c 

 </td><td> Abort multi-line messages and completions 

 
</td></tr> </table> 

 Additional key bindings may be specified using the <i>/bind</i> command described in the COMMANDS section. 

<h2>MCABBER'S ROSTER</h2>

 The first listed resource on the roster is <i>[status]</i>, which keeps a log of everything that appears in the short log window below the main chat area. While the log window was designed for showing the latest few elements, the dedicated <i>[status]</i> buffer allows more comfortable viewing of the log, as well as scrolling it in a standard manner. 

 Group names are displayed above the resources that are within them, and are indicated by <i>---</i> to the left of the name. 

 For every real Jabber resource, the roster displays four pieces of information: the resource's name or alias, its online status, its authorization status, and whether there are unread messages from the resource waiting for you. 

 The online status is one of the following: 

 <table> <tr VALIGN=top><td> <i>o</i> 

 </td><td> online 

 
</td></tr> <tr VALIGN=top><td> <i>C</i> 

 </td><td> a conference room in which you are participating 

 
</td></tr> <tr VALIGN=top><td> <i>f</i> 

 </td><td> free for chat 

 
</td></tr> <tr VALIGN=top><td> <i>a</i> 

 </td><td> away 

 
</td></tr> <tr VALIGN=top><td> <i>n</i> 

 </td><td> not available (labeled <i>extended away</i> in some clients) 

 
</td></tr> <tr VALIGN=top><td> <i>d</i> 

 </td><td> do not disturb 

 
</td></tr> <tr VALIGN=top><td> <i>i</i> 

 </td><td> invisible (displayed only for your resource) 

 
</td></tr> <tr VALIGN=top><td> <i>_</i> 

 </td><td> offline (or invisible to you) 

 
</td></tr> <tr VALIGN=top><td> <i>?</i> 

 </td><td> unknown, usually meaning you are not authorized to see this resource's status 

 
</td></tr> <tr VALIGN=top><td> <i>x</i> 

 </td><td> a conference room in which you are not participating 

 
</td></tr> </table> 

 The authorization status indicates whether a resource is authorized to receive your online status updates, and is displayed by the brackets surrounding the resource's online status. Square brackets, like <i>[o]</i>, indicate that this resource is authorized to receive your status. Curly braces, like <i>{o}</i>, indicate that they are not authorized to receive your status. 

 When there are unread messages from the resource which you have not looked at, a hash mark (<i>#</i>) appears in the leftmost section of the roster for that resource. The hash mark disappears once you view that resource's message log. 

 Examples: 

 <table> <tr VALIGN=top><td> <i> --- Buds</i> 

 </td><td> This is a group named <i>Buds</i> 

 
</td></tr> <tr VALIGN=top><td> <i>#[o] John</i> 

 </td><td> John is online, can see your status, and sent you a message that you did not read yet 

 
</td></tr> <tr VALIGN=top><td> <i> {?} Sally</i> 

 </td><td> Neither you nor Sally have authorized each other to see your online status 

 
</td></tr> <tr VALIGN=top><td> <i> {a} Jane</i> 

 </td><td> Jane is away, but she cannot see your online status 

 
</td></tr> <tr VALIGN=top><td> <i>#[C] x@y.c</i> 

 </td><td> You are participating in x@y.c conference room, and there are unread messages 

 
</td></tr> </table> 

<h2>COMMANDS</h2>

 Please refer to the online help (command /help), it is probably more up-to-date than this manpage. Furthermore, help files have been translated into several languages. You will find an overview of the mcabber commands in this manual. 

<h2>COMMANDS RELATED TO MCABBER</h2>

 

 /alias [name [= command line]]
<dl>
<dt>
<dd> Add &quot;name&quot; as an alias for &quot;command line&quot;. Aliases are expanded only once, thus they can not be chained. &quot;/alias name&quot; displays the value associated with the &quot;name&quot; alias; &quot;/alias name =&quot; unsets the &quot;name&quot; alias. &quot;/alias&quot; displays a list of the existing aliases. Example: &quot;/alias away = status away&quot;.</dl>
 

 /bind [keycode [= command line]]
<dl>
<dt>
<dd> Bind a command line to the key with the &quot;keycode&quot; code number. Keycodes of unused keys are displayed by mcabber in the log window when pressing the key, for example &quot;Unknown key=265&quot;. &quot;/bind keycode&quot; displays the command line bound to the given keycode; &quot;/bind keycode =&quot; unbinds the given keycode. &quot;/bind&quot; displays a list of the bound keycodes. Note: aliases can be used in key bindings. Example: &quot;/bind 265 = status online&quot; (265 is F1 for me, but it may depend on your ncurses installation).</dl>
 

 /buffer clear|close|close_all|purge, /buffer top|bottom|date|%|search_backward|search_forward, /buffer scroll_lock|scroll_unlock|scroll_toggle
<dl>
<dt>
<dd> The <i>buffer</i> command manipulates the current buddy's buffer (chat window). <table> <tr VALIGN=top><td> <i>clear</i> </td><td> clear the current buddy chat window 
</td></tr> <tr VALIGN=top><td> <i>close</i> </td><td> empty all contents of the buffer and close the current buddy chat window 
</td></tr> <tr VALIGN=top><td> <i>close_all</i> </td><td> empty all contents of the chat buffers and close the chat windows 
</td></tr> <tr VALIGN=top><td> <i>purge</i> </td><td> clear the current buddy chat window and empty all contents of the chat buffer 
</td></tr> <tr VALIGN=top><td> <i>top</i> </td><td> jump to the top of the current buddy chat buffer 
</td></tr> <tr VALIGN=top><td> <i>bottom</i> </td><td> jump to the bottom of the current buddy chat buffer 
</td></tr> <tr VALIGN=top><td> <i>up</i> [n] </td><td> scroll the buffer up n lines (default: half a screen) 
</td></tr> <tr VALIGN=top><td> <i>down</i> [n] </td><td> scroll the buffer down n lines (default: half a screen) 
</td></tr> <tr VALIGN=top><td> <i>date</i> date </td><td> jump to the first line after the specified date in the chat buffer (date format: &quot;YYYY-mm-dd[THH:MM:SS]&quot;, &quot;-&quot; and &quot;:&quot; are optional) 
</td></tr> <tr VALIGN=top><td> <i>%</i> n </td><td> jump to position %n of the buddy chat buffer 
</td></tr> <tr VALIGN=top><td> <i>search_backward</i> text </td><td> search for &quot;text&quot; in the current buddy chat buffer 
</td></tr> <tr VALIGN=top><td> <i>search_forward</i> text </td><td> search for &quot;text&quot; in the current buddy chat buffer 
</td></tr> <tr VALIGN=top><td> <i>scroll_lock</i> </td><td> lock buffer scrolling 
</td></tr> <tr VALIGN=top><td> <i>scroll_unlock</i> </td><td> unlock buffer scrolling 
</td></tr> <tr VALIGN=top><td> <i>scroll_toggle</i> </td><td> toggle buffer scrolling (lock/unlock) 
</td></tr> </table> 

</dl>
 

 /clear
<dl>
<dt>
<dd> The <i>clear</i> command is actually an alias for &quot;/buffer clear&quot;.</dl>
 

 /help [command]
<dl>
<dt>
<dd> Display generic help or help about a specific mcabber command.</dl>
 

 /quit
<dl>
<dt>
<dd> Disconnect and leave <a HREF="/docs/linux/man/1-mcabber/">mcabber</a>(1).</dl>
 

 /set option[=value]
<dl>
<dt>
<dd> Display or set an option value.</dl>
 

 /source [file]
<dl>
<dt>
<dd> Read a configuration file.</dl>
 

 /version
<dl>
<dt>
<dd> Display mcabber version</dl>

<h2>COMMANDS RELATED TO THE SERVER AND CONNECTION</h2>

 

 /connect
<dl>
<dt>
<dd> Establish connection to the Jabber server.</dl>
 

 /disconnect
<dl>
<dt>
<dd> Terminate connection to the Jabber server. Note: the roster is only available when the connection to the server is active, so the buddylist is empty when disconnected.</dl>
 

 /event #n|* accept|ignore|reject, /event list
<dl>
<dt>
<dd> Tell mcabber what to do about a pending event. If the first parameter is &quot;*&quot;, the command will apply to all queued events. <table> <tr VALIGN=top><td> <i>accept</i> </td><td> accept the event #n 
</td></tr> <tr VALIGN=top><td> <i>ignore</i> </td><td> remove the event #n from the list 
</td></tr> <tr VALIGN=top><td> <i>reject</i> </td><td> reject the event #n 
</td></tr> <tr VALIGN=top><td> <i>list</i> </td><td> list all pending events 
</td></tr> </table> 

</dl>
 

 /rawxml send string
<dl>
<dt>
<dd> 

 <i>send</i> string: send string (raw XML format) to the Jabber server. No check is done on the string provided. BEWARE! Use this only if you know what you are doing, or you could terminate the connection.</dl>

<h2>COMMANDS RELATED TO THE ROSTER AND JABBER RESOURCES</h2>

 

 /add [jid [nickname]]
<dl>
<dt>
<dd> Add the &quot;jid&quot; Jabber user to our roster (default group), and send a notification request to this buddy. If no nickname is specified, the jid is used. If no jid (or an empty string &quot;&quot;) is provided or if jid is &quot;.&quot;, the current buddy is used.</dl>
 

 /authorization allow|cancel|request|request_unsubscribe [jid]
<dl>
<dt>
<dd> Manage the presence subscriptions. If no jid is provided, the current buddy is used. <table> <tr VALIGN=top><td> <i>allow</i> </td><td> allow the buddy to receive your presence updates 
</td></tr> <tr VALIGN=top><td> <i>cancel</i> </td><td> cancel the buddy' subscription to your presence updates 
</td></tr> <tr VALIGN=top><td> <i>request</i> </td><td> request a subscription to the buddy's presence updates 
</td></tr> <tr VALIGN=top><td> <i>request_unsubscribe</i> </td><td> request unsubscription from the buddy's presence updates 
</td></tr> </table> 

</dl>
 

 /del
<dl>
<dt>
<dd> Delete the current buddy from our roster, unsubscribe from its presence notification and unsubscribe it from ours.</dl>
 

 /group fold|unfold|toggle
<dl>
<dt>
<dd> The <i>group</i> command changes the current group display. <table> <tr VALIGN=top><td> <i>fold</i> </td><td> fold (shrink) the current group tree in the roster 
</td></tr> <tr VALIGN=top><td> <i>unfold</i> </td><td> unfold (expand) the current group tree in the roster 
</td></tr> <tr VALIGN=top><td> <i>toggle</i> </td><td> toggle the state (fold/unfold) of the current tree 
</td></tr> </table> 

</dl>
 

 /info
<dl>
<dt>
<dd> Display info on the selected entry (user, agent, group...). For users, resources are displayed with the status, priority and status message (if available) of each resource.</dl>
 

 /move [groupname]
<dl>
<dt>
<dd> Move the current buddy to the requested group. If no group is specified, then the buddy is moved to the default group. If the group groupname doesn't exist, it is created. Tip: if the chatmode is enabled, you can use &quot;/roster alternate&quot; to jump to the moved buddy.</dl>
 

 /msay begin|verbatim|send|send_to|toggle|toggle_verbatim|abort
<dl>
<dt>
<dd> Send a multi-line message. To write a single message with several lines, the <i>multi-line mode</i> should be used. In multi-line mode, each line (except command lines) typed in the input line will be added to the multi-line message. Once the message is finished, it can be sent to the current selected buddy with the &quot;/msay send&quot; command (or Ctrl-d). The <i>begin</i> subcommand enables multi-line mode. Note that it allows a message subject to be specified. The <i>verbatim</i> multi-line mode disables commands, so that it is possible to enter lines starting with a slash. Only the &quot;/msay&quot; command (with send or abort parameters) can be used to exit verbatim mode. The <i>toggle</i> and <i>toggle_verbatim</i> subcommands can be bound to a key to use the multi-line mode quickly (for example, &quot;bind M109 = msay toggle&quot; to switch using the Meta-m combination). <table> <tr VALIGN=top><td> <i>begin</i> [subject] </td><td> enter multi-line mode 
</td></tr> <tr VALIGN=top><td> <i>verbatim</i> </td><td> enter verbatim multi-line mode 
</td></tr> <tr VALIGN=top><td> <i>send</i> </td><td> send the current multi-line message to the currently selected buddy 
</td></tr> <tr VALIGN=top><td> <i>send_to</i> jid </td><td> send the current multi-line message to &quot;jid&quot; 
</td></tr> <tr VALIGN=top><td> <i>toggle</i> </td><td> switch to/from multi-line mode (begin/send) 
</td></tr> <tr VALIGN=top><td> <i>toggle_verbatim</i> </td><td> same with verbatim multi-line mode 
</td></tr> <tr VALIGN=top><td> <i>abort</i> </td><td> leave multi-line mode without sending the message 
</td></tr> </table> 

</dl>
 

 /pgp disable|enable|force|info [jid], /pgp setkey [jid [key]]
<dl>
<dt>
<dd> Manipulate PGP settings for the specified jid (by default the currently selected contact). Please note that PGP encryption won't be used if no remote PGP support is detected, even if PGP is enabled with this command. <table> <tr VALIGN=top><td> <i>disable</i> [jid] </td><td> disable PGP encryption for jid (or the currently selected contact) 
</td></tr> <tr VALIGN=top><td> <i>enable</i> [jid] </td><td> enable PGP encryption for jid (or the currently selected contact) 
</td></tr> <tr VALIGN=top><td> <i>force</i> [jid] </td><td> enforce PGP encryption, even for offline messages, and always assume the recipient has PGP support 
</td></tr> <tr VALIGN=top><td> <i>info</i> [jid] </td><td> show current PGP settings for the contact 
</td></tr> <tr VALIGN=top><td> <i>setkey</i> [jid [key]] </td><td> set the PGP key to be used to encrypt message for this contact. If no key is provided, the current key is erased. You can use the shortcut-jid &quot;.&quot; for the currently selected contact. 
</td></tr> </table> 

</dl>
 

 /rename name
<dl>
<dt>
<dd> Rename current buddy or group to the given name. Please note that a group name change is only done when the server's acknowledgment is received, so a slight delay can be noticed.</dl>
 

 /request last|time|vcard|version [jid]
<dl>
<dt>
<dd> Send a &quot;IQ&quot; query to the current buddy, or to the specified Jabber user. If the resource is not provided with the jid, mcabber will send the query to all known resources for this user.</dl>
 

 /room join|leave|names|nick|privmsg|remove|topic|unlock|destroy, /room invite|kick|ban|role|affil, /room bookmark [add|del] [-autojoin|+autojoin]
<dl>
<dt>
<dd> The <i>room</i> command handles Multi-User Chat room actions. <table> <tr VALIGN=top><td> <i>join</i> [room [nick [pass]]] </td><td> join &quot;room&quot;, using &quot;nick&quot; as nickname. If no nickname is provided (or if it is an empty string), the &quot;nickname&quot; option value is used (see sample configuration file). If the currently selected entry is correctly recognized as a room by mcabber, the shortcut &quot;.&quot; can be used instead of the full room id. A password can be provided to enter protected rooms. If your nickname contains space characters, use quotes. 
</td></tr> <tr VALIGN=top><td> <i>whois</i> nick </td><td> display MUC information about &quot;nick&quot; 
</td></tr> <tr VALIGN=top><td> <i>ban</i> jid [reason] </td><td> ban jid from the current room 
</td></tr> <tr VALIGN=top><td> <i>invite</i> jid [reason] </td><td> invite jid to the current room 
</td></tr> <tr VALIGN=top><td> <i>kick</i> nick [reason] </td><td> kick &quot;nick&quot; from the current room 
</td></tr> <tr VALIGN=top><td> <i>role</i> jid role [reason] </td><td> change jid's role (role can be &quot;none&quot;, &quot;visitor&quot;, &quot;participant&quot;, &quot;moderator&quot;) 
</td></tr> <tr VALIGN=top><td> <i>affil</i> jid affil [reason] </td><td> change jid's affiliation (affil can be &quot;none&quot;, &quot;member&quot;, &quot;admin&quot;, &quot;owner&quot;) <i>bookmark</i> add/update/remove a room bookmark, set/unset autojoin 
</td></tr> <tr VALIGN=top><td> <i>leave</i> [message] </td><td> leave the current room 
</td></tr> <tr VALIGN=top><td> <i>names</i> [--detail|--short|--quiet] </td><td> display the members of the current room 
</td></tr> <tr VALIGN=top><td> <i>nick</i> nick </td><td> change your nickname in the current room 
</td></tr> <tr VALIGN=top><td> <i>privmsg</i> nick msg </td><td> send private message &quot;msg&quot; to &quot;nick&quot; 
</td></tr> <tr VALIGN=top><td> <i>remove</i> </td><td> remove the current room from the roster (you must have left this room before) 
</td></tr> <tr VALIGN=top><td> <i>topic</i> </td><td> set topic for current room 
</td></tr> <tr VALIGN=top><td> <i>unlock</i> </td><td> unlock current room (if you are the owner) 
</td></tr> <tr VALIGN=top><td> <i>destroy</i> [reason] </td><td> destroy the current room (use with care!) 
</td></tr> </table> 

</dl>
 

 /roster bottom|top|up|down|group_prev|group_next, /roster alternate|unread_first|unread_next, /roster search bud, /roster hide_offline|show_offline|toggle_offline, /roster item_lock|item_unlock, /roster hide|show|toggle, /roster note [-|text]
<dl>
<dt>
<dd> The <i>roster</i> command manipulates the roster/buddylist. Here are the available parameters: <table> <tr VALIGN=top><td> <i>bottom</i> </td><td> jump to the bottom of the roster 
</td></tr> <tr VALIGN=top><td> <i>search</i> bud </td><td> search for a buddy with a name or jid containing &quot;bud&quot; (only in the displayed buddylist) 
</td></tr> <tr VALIGN=top><td> <i>hide_offline</i> </td><td> hide offline buddies 
</td></tr> <tr VALIGN=top><td> <i>show_offline</i> </td><td> show offline buddies 
</td></tr> <tr VALIGN=top><td> <i>toggle_offline</i> </td><td> toggle display of offline buddies 
</td></tr> <tr VALIGN=top><td> <i>item_lock</i> jid </td><td> lock the roster item so it remains visible regardless of its status 
</td></tr> <tr VALIGN=top><td> <i>item_unlock</i> jid </td><td> undo the effects of item_lock 
</td></tr> <tr VALIGN=top><td> <i>hide</i> </td><td> hide roster (full-width chat window) 
</td></tr> <tr VALIGN=top><td> <i>show</i> </td><td> show roster 
</td></tr> <tr VALIGN=top><td> <i>toggle</i> </td><td> toggle roster visibility 
</td></tr> <tr VALIGN=top><td> <i>note</i> [text] </td><td> display or set an annotation (if text is &quot;-&quot;, the annotation is deleted). In the &quot;status&quot; buffer, it will display all annotations. 
</td></tr> <tr VALIGN=top><td> <i>top</i> </td><td> jump to the top of the roster 
</td></tr> <tr VALIGN=top><td> <i>up</i> </td><td> move up in the roster 
</td></tr> <tr VALIGN=top><td> <i>down</i> </td><td> move down in the roster 
</td></tr> <tr VALIGN=top><td> <i>group_prev</i> </td><td> jump to the previous group in the roster 
</td></tr> <tr VALIGN=top><td> <i>group_next</i> </td><td> jump to the next group in the roster 
</td></tr> <tr VALIGN=top><td> <i>alternate</i> </td><td> jump to alternate buddy. The &quot;alternate&quot; buddy is the last buddy left while being in chat mode (this command is thus especially useful after commands like &quot;/roster unread_first&quot;) 
</td></tr> <tr VALIGN=top><td> <i>unread_first</i> </td><td> jump to the first unread message 
</td></tr> <tr VALIGN=top><td> <i>unread_next</i> </td><td> jump to the next unread message 
</td></tr> </table> 

</dl>
 

 /say text
<dl>
<dt>
<dd> Send the &quot;text&quot; message to the currently selected buddy. Can be useful if you want to send a message beginning with a slash, for example.</dl>
 

 /say_to jid text
<dl>
<dt>
<dd> Send the &quot;text&quot; message to the specified jid. Please note that this command doesn't set the default resource for a contact, so if you want to send several messages to a specific resource you will have to use &quot;/say_to&quot; for each message.</dl>
 

 /status [online|avail|invisible|free|dnd|notavail|away [-|StatusMessage]]
<dl>
<dt>
<dd> Show or set the current status. If no status is specified, display the current status. If a status message is specified, it will overrride the message* variables (these variables can be set in the configuration file). If no relevant message* variable is set and no status message provided, the current status message is kept. If StatusMessage is &quot;-&quot;, the current status message is cleared.</dl>
 

 /status_to jid online|avail|invisible|free|dnd|notavail|away [StatusMessage]
<dl>
<dt>
<dd> Send the requested status to the specified Jabber user. If the specified jid is &quot;.&quot;, the current buddy is used. Note: this status will be overridden by subsequent &quot;/status&quot; commands. If you are using the auto-away feature, the status will overridden too. Note: The jid can include a resource (i.e. user [at] server/resource).</dl>

<h2>CONFIGURATION FILE</h2>

 See the provided sample configuration file, which should be self-documenting. 

<h2>FILES</h2>

 The following files can be used by <a HREF="/docs/linux/man/1-mcabber/">mcabber</a>(1): 

 

<dl>
<dt>
<dd> <pre>
$HOME/.mcabber/mcabberrc    Default configuration file
$HOME/.mcabberrc            Configuration file used if no other has been found
$HOME/.mcabber/histo/       Default directory for storing chat history files, if enabled
</pre></dl>

<h2>BUGS</h2>

 Certainly. Please tell me if you find one! :-) 

<h2>AUTHOR</h2>

 Written by <i>Mikael BERTHE</i>[1]. Originally based on <i>Cabber</i>[2], please consult the AUTHORS file for details. 

<h2>RESOURCES</h2>

 <i>Main web site</i>[3] 

<h2>COPYING</h2>

 Copyright (C) 2005, 2006, 2007, 2008 Mikael Berthe. Some portions are Copyright (C) 2002-2004 <i>cabber [at] ajmacias.com</i>[4]. 

 Free use of this software is granted under the terms of the GNU General Public License (GPL). 

<h2>REFERENCES</h2>

<dl>
<dt> 1.
<dd> Mikael BERTHE
<dl>
<dt>
<dd> mailto:mcabber [at] lilotux.net</dl>

<dt> 2.
<dd> Cabber
<dl>
<dt>
<dd> <a rel="nofollow" HREF="http://cabber.sourceforge.net">http://cabber.sourceforge.net</a></dl>

<dt> 3.
<dd> Main web site
<dl>
<dt>
<dd> <a rel="nofollow" HREF="http://www.lilotux.net/~mikael/mcabber/">http://www.lilotux.net/~mikael/mcabber/</a></dl>

<dt> 4.
<dd> cabber [at] ajmacias.com
<dl>
<dt>
<dd> mailto:cabber [at] ajmacias.com</dl>
 

</dl>

<h2>Index</h2>


