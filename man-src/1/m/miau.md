---
title: "miau(1)"
name: "miau"
section: "1"
letter: "m"
url: "/docs/linux/man/1-miau/"
description: "miau.info – miau.info"
---

<h2>NAME</h2>
<p> miau.info &#8211; miau.info</p>
<h2>miau Manual</h2>
<p> This is edition 0.6.1 of the `<code>miau Manual</code>&#8216;, last updated 7 January 2006. </p>
<p> * Menu: </p>
<p> Why you need an irc-bouncer and how it is used: see &#8220;Introduction&#8221; </p>
<p> How to install miau: see &#8220;Installation&#8221; </p>
<p> Invocation of miau: see &#8220;Command Line Options&#8221; </p>
<p> Commands while miau is running: see &#8220;miau Commands&#8221; </p>
<p> Statements in your miaurc: see &#8220;miaurc Commands&#8221;</p>
<h2>1 What is an irc-bouncer?</h2>
<p> A bouncer doesn&#8217;t do anything else than diverting a network-connection. </p>
<p> In case of an irc-bouncer, connections from your irc-program (client) are diverted by the bouncer to a irc-server. </p>
<p> &#8220;What is this good for?&#8221;, you might ask. </p>
<p> Well, let&#8217;s assume you&#8217;ve got a dialup-connection. If somebody performs a `<code>/WHOIS</code>&#8216; on you it shows something like &#8220;yournick is yournick!yourident [at] dialup66-r-v.isp.at&#8221;. </p>
<p> If you are vain you don&#8217;t want people to see this stupid hostname. So you get a account on a machine with a cool hostname (from now on refered as middleman), get miau running there and a /whois on you will show middleman&#8217;s hostname, since the connection to the irc-server is actually originating from middleman. </p>
<p> Another advantage is that network-attacks aren&#8217;t really destinating to <font SIZE="-1">YOUR</font> computer but to middleman, which is in theory a machine that can&#8217;t be brought down. </p>
<p> 2 What makes miau special over other bouncers? ********************************************** </p>
<p> miau is very straight and simple to set up and the probably most important and interesting feature is that miau keeps the middleman -&gt; irc-server connection up even after you disconnect with your client. </p>
<p> This means miau prevents people from using your nick (this is especially handy on nets like IRCNet, since there are no services like on dalnet etc) and tells people who message you that you&#8217;re not here and logs what these people said. </p>
<p> Upon your next connect to miau, it will let the channels you&#8217;ve been in in your last session pop up, which means that you&#8217;ll keep your status in these channels. </p>
<p> Besides that miau&#8217;s got a sophisticated flood-protection making it (almost) impossible to disconnect miau. </p>
<p> 3 Copyright *********** </p>
<p> miau has been written by Tommi Saviranta &lt;wnd [at] iki.fi&gt;. miau branched from muh, see <a rel="nofollow" href="http://mind.riot.org/muh/.">http://mind.riot.org/muh/.</a> miau is licensed under the <font SIZE="-1">GPL</font>. See <font SIZE="-1">COPYING</font> for details.</p>
<h2>4 Command Line Options</h2>
<p> `<code>-f</code>&#8216; Stay in foreground (don&#8217;t fork) </p>
<p> `<code>-d directory</code>&#8216; Specifies a different directory than the default for miaurc, messages and log </p>
<p> `<code>-c</code>&#8216; You will be prompted for a word to crypt. The output can be used as `<code>password</code>&#8216; in miaurc if you don&#8217;t wanna have the password stored in clear text. Note that you&#8217;ll still have to authorize with the unencrypted password. </p>
<p> This option might not be compiled in.</p>
<h2>5 miau Commands</h2>
<p> miau accepts following commands to be issued by the client via `/MIAU &lt;command&gt;&#8217;. </p>
<p> Note that some IRC-clients might require a prefix such as `<code>/QUOTE</code>&#8216; or `<code>/RAW</code>&#8216; to send commands they don&#8217;t know about. </p>
<p> `<font SIZE="-1"><code>HELP</code></font>&#8216; Display supported commands </p>
<p> `<font SIZE="-1"><code>READ</code></font>&#8216; Read received messages </p>
<p> `<font SIZE="-1"><code>DEL</code></font>&#8216; Delete all messages </p>
<p> `<font SIZE="-1"><code>PRINT</code></font>&#8216; Prints miau&#8217;s server-list. Servers prefixed with &#8216;+&#8217; work, those with &#8216;-&#8216; don&#8217;t. </p>
<p> `<font SIZE="-1"><code>JUMP</code></font><code> [servernumber]</code>&#8216; Jump to next server in serverlist. If `<code>servernumber</code>&#8216; (see `<font SIZE="-1"><code>PRINT</code></font>&#8216;) is specified, miau will jump to this server (even if marked as not working). </p>
<p> `<font SIZE="-1"><code>REHASH</code></font>&#8216; Reread config-file. Note that this can also be performed by sending a `<font SIZE="-1"><code>SIGHUP</code></font>&#8216; to miau (see `<a href="/docs/linux/man/1-kill/">kill</a><code>(1)</code>&#8216;). If `<code>realname</code>&#8216; or `<code>username</code>&#8216; have been changed miau will reconnect to it&#8217;s current server. </p>
<p> `<font SIZE="-1"><code>DIE</code></font><code> [reason]</code>&#8216; Terminate miau. A quit reason can be given after command. </p>
<p> `<font SIZE="-1"><code>UPTIME</code></font>&#8216; Prints uptime of miau. </p>
<p> This command might not be compiled in. </p>
<p> `<font SIZE="-1"><code>PINGSTAT</code></font>&#8216; Prints ping statistics. </p>
<p> This command might not be compiled in. </p>
<p> `<font SIZE="-1"><code>DUMP</code></font>&#8216; Prints some of miau&#8217;s internal variables. Used for debugging. </p>
<p> This command might not be compiled in.</p>
<h2>6 Installation</h2>
<p> Create a `<code>.miau/</code>&#8216;-directory in your homedir and copy `<code>miaurc</code>&#8216; there (it will probably reside in `<code>/usr/share/miau</code>&#8216;, depending on your os/distribution). </p>
<p> Edit `<code>miaurc</code>&#8216;, _make sure noone except you has read-access_ and launch miau. </p>
<p> To make sure miau&#8217;s running all day there is a script called `<code>miau-check</code>&#8216; that came with miau. Edit it as well and make `<a href="/docs/linux/man/5-crontab/">crontab</a><code>(5)</code>&#8216; call it periodically.</p>
<h2>7 miaurc Commands</h2>
<p> There are numerous commands with which you can extensively customize miau&#8217;s behaviour. The must be placed in the `<code>miaurc</code>&#8216; that miau reads on startup, it is usually `<code>$HOME/.miau/miaurc</code>&#8216;. </p>
<p> 8 Required settings ******************* </p>
<p> `<code>nicknames = { &#8220;nick&#8221; }</code>&#8216; Your nickname (and secondary nicknames) on <font SIZE="-1">IRC</font>. If the primary nick (first nick on the list) is already on use, miau will try the others on the list. </p>
<p> `<code>realname = &#8220;realname&#8221;</code>&#8216; Your &#8220;real&#8221; name (which will be shown by `<code>/WHOIS</code>&#8216;-command) on <font SIZE="-1">IRC</font>. </p>
<p> `<code>username = &#8220;username&#8221;</code>&#8216; Your ident (matters only if you don&#8217;t have `<code>identd</code>&#8216; running). </p>
<p> `<code>password = &#8220;password&#8221;</code>&#8216; The password miau will expect to receive from client when it&#8217;s registering with nick. If this is 13 characters long, miau assumed it&#8217;s crypted. miau can generate password-hashes with `<code>-c</code>&#8216; -switch, if it is compiled with that feature. </p>
<p> `<code>listenport = &#8220;port&#8221;</code>&#8216; The port miau will wait for incoming connections. This is the port you connect your IRC-client to. </p>
<p> `<code>servers = { &#8220;server&#8221;:&#8220;port&#8221;:&#8220;password&#8221;:&#8220;timeout&#8221; }</code>&#8216; miau&#8217;s IRC-server-list. Each line represents one server, where timeout is delay in seconds before connectiong attempt times out. Only `<code>server</code>&#8216; parameter is required. </p>
<p> `<code>connhosts = { &#8220;host&#8221;:&#8220;permitted&#8221; }</code>&#8216; List of hosts that are allowed (or denied) to connect to miau. When `<code>permitted</code>&#8216; is left unset, it is assumed to be `<code>true</code>&#8216;. This list will be processed as a chain which means latter rules can override previous ones. </p>
<p> Note: You can define &#8220;your&#8221; hostname with `<code>@@</code>&#8216;. Only the _last_ occurance of `<code>@@</code>&#8216; will be translated. </p>
<p> 9 Optional settings ******************* </p>
<p> `<code>statelog = &#8220;state&#8221;</code>&#8216; Should miau write state log to `<code>$MIAUDIR/log</code>&#8216;? When true, log will be written in this file. If set to false, the same stuff is printed on `<code>stdout</code>&#8216; (on terminal). </p>
<p> `<code>listenhost = &#8220;host&#8221;</code>&#8216; Host miau uses to listen on. If you are compiled with <font SIZE="-1">IPV6</font> and need this to listen on an <font SIZE="-1">IPV4</font> port, you must use an <font SIZE="-1">IP</font> in the form `<code>::FFFF:127.0.0.1</code>&#8216;. </p>
<p> `<code>floodtimer = &#8220;number&#8221;</code>&#8216; Time it takes to send one message. When configuring flood-protection, this variable defined how fast you can send messages; how many seconds sending one message takes. See also `<code>burstsize</code>&#8216;. </p>
<p> `<code>burstsize = &#8220;number&#8221;</code>&#8216; How many messages can be sent at once. When configuring flood-protection, this variable defined how many messages can be sent at once (in a burst). See also `<code>floodtimer</code>&#8216;. </p>
<p> `<code>jointries = &#8220;number&#8221;</code>&#8216; Number of tries to join channel after dropping from server etc. miau tries to join channels once a minute. </p>
<p> `<code>bind = &#8220;host&#8221;</code>&#8216; Host/IP miau uses for outgoing connections. </p>
<p> `<code>maxclients = &#8220;number&#8221;</code>&#8216; Maximum number of clients connected to miau concurrently. Set to zero for unlimited clients. </p>
<p> `<code>stonedtimeout = &#8220;seconds&#8221;</code>&#8216; Time (in seconds) with no data from the server before it is declared stoned and being disconnected. Although minimum value is 30, this value has no upper limit. Watch out, though, if this value is set too high, death of servers may stay undetected for a very long time if you are idle. </p>
<p> `<code>connecttimeout = &#8220;seconds&#8221;</code>&#8216; Time (in seconds) before connection attampt will time out. Note that while connecting to the server miau will not respond to clients. Minimum value is 5, and many systems define maximum value. </p>
<p> `<code>channels = { &#8220;channel&#8221;:&#8220;keyword&#8221; }</code>&#8216; List of channels to join. </p>
<p> `<code>rejoin = &#8220;state&#8221;</code>&#8216; Rejoin channels after disconnecting from the server. If `<code>rejoin</code>&#8216; is set to `<code>true</code>&#8216;, channels defined in `<code>channels</code>&#8216;&quot; are also joined when client first time connects to miau. </p>
<p> `<code>leave = &#8220;state&#8221;</code>&#8216; Leave channels when all clients have detached from miau. If `<code>leave</code>&#8216; is set to `<code>false</code>&#8216; and `<code>rejoin</code>&#8216; is set to `<code>true</code>&#8216;, channels defined at `<code>channels</code>&#8216; will be joined at miau startup. If both `<code>leave</code>&#8216; and `<code>rejoin</code>&#8216; is set to `<code>true</code>&#8216;, channels that are left at client detach, are rejoined when client attached back to miau. </p>
<p> `<code>leavemsg = &#8220;message&#8221;</code>&#8216; Message miau will either use as PART-message or as <font SIZE="-1">ACTION</font> when all clients have detached from miau. If unset or set to empty, no message will be shown. Note that many people dislike event-based messages (which happens when `<code>leave</code>&#8216; is set to `<code>false</code>&#8216; and `<code>leavemsg</code>&#8216; is set). Note that commenting this option out and rehashing after `<code>leavemsg</code>&#8216; was set, this option is _not_ reverted. To disable `<code>leavemsg</code>&#8216; afterwards you need to write an empty string here and rehash. Also see `<code>usequitmsg</code>&#8216;. </p>
<p> `<code>awaymsg = &#8220;message&#8221;</code>&#8216; Text that will be set to miau&#8217;s away-reason when all clients have detached from miau. If unset or set to empty, AWAY-status will be left untouched. When any client attaches back to miau, AWAY-status will be reset. Note that is user sets him/herself away, miau will _not_ touch away-status nor message neither when connecting to or disconnected from miau. Also note that commenting this option out and rehashing after `<code>awaymsg</code>&#8216; was set, this option is _not_ reverted. To disable `<code>awaymsg</code>&#8216; afterwards you need to write an empty string here and rehash. Also see `<code>usequitmsg</code>&#8216;. </p>
<p> `<code>usequitmsg = &#8220;state&#8221;</code>&#8216; Use last quit-reason as away-reason and/or leave-message (if respective options are enabled) when all clients have disconnected from miau. If quit-reason was empty, default values of awaymsg and leavemsg will be used, otherwise most recent quit-message overrides values in miaurc. </p>
<p> `<code>autoaway = &#8220;mode&#8221;</code>&#8216; miau can set user away automatically. This option allows to define when to do that: `<code>never</code>&#8216; Never set user away automatically </p>
<p> `<code>detach</code>&#8216; Set user away when any of the clients disconnects </p>
<p> `<code>noclients</code>&#8216; Set user away when the last client disconnects If `<code>usequitmsg</code>&#8216; is set, quit message will be used as a reason. If not, `<code>awaymsg</code>&#8216; will be used. </p>
<p> `<code>chandiscon = &#8220;mode&#8221;</code>&#8216; When miau is disconnected from the server e.g. because of network problem, miau can notify user about this in a couple of ways. `<code>nothing</code>&#8216; Only print server notice </p>
<p> `<code>notice</code>&#8216; Send notice to each channel </p>
<p> `<code>part</code>&#8216; Part each channel. mIRC users probably don&#8217;t want to use this. </p>
<p> `<code>privmsg</code>&#8216; Only send a private message to the user </p>
<p> `<code>getnick = &#8220;selection&#8221;</code>&#8216; miau can try to reclaim your primary nick when it is lost. This option may be one of the following: `<code>never</code>&#8216; miau will not try to get your nick back </p>
<p> `<code>detached</code>&#8216; miau will try to get your nick when no clients are attached </p>
<p> `<code>attached</code>&#8216; miau will try to get your nick when there are one or more clients attached </p>
<p> `<code>always</code>&#8216; miau will try to get your nick Note: do _not_ use options `<code>attached</code>&#8216; and `<code>always</code>&#8216; with clients (like irc-II <font SIZE="-1">EPIC</font>) that automatically change your nick when they receive `<font SIZE="-1"><code>ERR_NICKINUSE</code></font>&#8216; from the server &#8211; you might end up chaning your nick until server drops your connection due excess (nick) flood. </p>
<p> `<code>getnickinterval = &#8220;seconds&#8221;</code>&#8216; Time between tries (in seconds) to obtain currently (possibly) lost primary nick. Don&#8217;t set it too low or you might get kicked out the server due to excess flood. </p>
<p> `<code>antiidle = &#8220;minutes&#8221;</code>&#8216; Time between idle-timer resets in minutes. Set to 0 to disable. </p>
<p> `<code>qloglength = &#8220;minutes&#8221;</code>&#8216; Age of oldest entry in quicklog in minutes. Set to zero to disable quicklog. </p>
<p> Note: private messages get also logged into quicklog, but if `<code>inbox</code>&#8216; is enabled, they are moved to messagelog instead of simply dropping of from quicklog. </p>
<p> This option might not be compiled in. </p>
<p> `<code>timestamp = &#8220;mode&#8221;</code>&#8216; Location of timestamp in quicklog. </p>
<p> Available modes: `<code>none</code>&#8216; No timestamp </p>
<p> `<code>beginning</code>&#8216; Timestamp in beginning of line </p>
<p> `<code>end</code>&#8216; Timestamp at end of line </p>
<p> This options might not be compiled in. </p>
<p> `<code>flushqlog = &#8220;state&#8221;</code>&#8216; If set to `<code>true</code>&#8216;, quicklog will be written only when no clients are connected and quicklog will be erased when client connects to miau. If you are running a single client, you probably want to leave this to `<code>false</code>&#8216;. </p>
<p> This option might not be compiled in. </p>
<p> `<code>inbox = &#8220;state&#8221;</code>&#8216; Enables logging private messages when no clients are connected to miau. </p>
<p> Note: if quicklog is enabled (see `<code>qloglength</code>&#8216;), private messages are first stored in quicklog and moved to messagelog when they become too old to be stored in quicklog. </p>
<p> This option might not be compiled in. </p>
<p> `<code>nevergiveup = &#8220;state&#8221;</code>&#8216; If set to `<code>true</code>&#8216;, miau will reset &#8220;working&#8221;-status of servers to working when all are set to dysfunctional. Respectively, if set to `<code>false</code>&#8216;, miau will quit when all servers on the list have been set to dysfunctional. </p>
<p> `<code>norestricted = &#8220;state&#8221;</code>&#8216; If set to `<code>true</code>&#8216;, miau will not stay on server that forces user to have restricted-status (+r). </p>
<p> `<code>reconnectdelay = &#8220;seconds&#8221;</code>&#8216; Time (in seconds) between connection attempts. Minumun value is set to 1. </p>
<p> `<code>nickfillchar = &#8220;fill character&#8221;</code>&#8216; Character used to modify your primary nick when all defined nicks are already occupied. Note character is a single octet (byte) and if longer string is fed, only the first character is used. </p>
<p> `<code>maxnicklen = &#8220;length&#8221;</code>&#8216; Maximum nick length, used with `<code>nickfillchar</code>&#8216;. </p>
<p> `<code>usermode = &#8220;usermode(s)&#8221;</code>&#8216; Usermode that miau will request (if no clients are attached at the moment) from the server when connection to the server is established. Leave unset or set to empty to disable this feature. </p>
<p> `<code>forwardmsg = &#8220;command&#8221;</code>&#8216; miau can collect the (private) messages within specified time (see `<code>forwardtime</code>&#8216;) and pipe them into the program specified. Leave this unset or set to empty to disable this feature. </p>
<p> `<code>forwardtime = &#8220;seconds&#8221;</code>&#8216; Time in seconds after first inserted line into forwardmsg queue before piping the stuff out. Default is 180 seconds (or three mintues). </p>
<p> `<code>ignore = { &#8220;mask&#8221;:&#8220;ignored&#8221; }</code>&#8216; List of users whose private messages (<font SIZE="-1">PRIVMSG</font>) and noticies (<font SIZE="-1">NOTICE</font>) are ignored when no clients are attached to miau. When `<code>ignored</code>&#8216; is left undefined, it is assumed to be `<code>true</code>&#8216;. Setting `<code>ignored</code>&#8216; to `<code>false</code>&#8216; means that this user will _not_ be ignored. This list is processed as a chain. </p>
<p> Note: You can define &#8220;your&#8221; hostname with @@. Only the _last_ occurance of @@ will be translated. </p>
<p> `<code>privlog = &#8220;mode&#8221;</code>&#8216; Whatever private messages should be logged in nick-specific files. Can be one of following: `<code>never</code>&#8216; never write private message logs </p>
<p> `<code>detached</code>&#8216; write private message logs only when there are no clients connected </p>
<p> `<code>attached</code>&#8216; write private logs only when there are clients connected </p>
<p> `<code>always</code>&#8216; always write private message logs </p>
<p> All logfiles are written into miau&#8217;s log directory (`<code>logs</code>&#8216;). </p>
<p> This option might not be compiled in. </p>
<p> `<code>chanlog = { &#8220;channel(s)&#8221;:&#8220;options&#8221;:&#8220;logfile&#8221; }</code>&#8216; List of channel logfiles. </p>
<p> When channel is set to `<code>*</code>&#8216;, line represents global log. When logging, if channel doesn&#8217;t have entry of it&#8217;s own in this list, it will use settings of global log and write log to it&#8217;s own file. When defining global log, `<code>logfile</code>&#8216; is ignored. Each line can have multiple channels (like `<code>#foobar,#miau</code>&#8216;). </p>
<p> If logfile is left undefined, logfile will be named after the channel with possible suffix (see `<code>logsuffix</code>&#8216;). All filenames are relative and are, by default, written in miau&#8217;s log directory (`<code>logs</code>&#8216;). </p>
<p> Options consist of abritary set of following possibilities: `<code>j</code>&#8216; log joins </p>
<p> `<code>e</code>&#8216; log parts (exits) </p>
<p> `<code>q</code>&#8216; log quits </p>
<p> `<code>m</code>&#8216; log messages (privmsg/notice) </p>
<p> `<code>c</code>&#8216; log mode changes </p>
<p> `<code>n</code>&#8216; log nick changes </p>
<p> `<code>o</code>&#8216; log misc events (other) </p>
<p> `<code>b</code>&#8216; log messages from miau (bouncer) </p>
<p> `<code>a</code>&#8216; log all of above </p>
<p> `<code>A</code>&#8216; log when a client is attached </p>
<p> `<code>D</code>&#8216; log when a client is detached </p>
<p> `<code>C</code>&#8216; log continuously (status of clients doesn&#8217;t matter) </p>
<p> Note that all channelless messages (such as <font SIZE="-1">QUIT</font>) are logged on every active channel. This is a feature, not a bug. </p>
<p> This option might not be compiled in. </p>
<p> `<code>logsuffix = &#8220;suffix&#8221;</code>&#8216; When writing log to undefined logfile, each logfile consists of channel name followed by suffix. Suffix can be defined here. </p>
<p> `<code>onconnect = { &#8220;mode&#8221;:&#8220;target/data&#8221;(:&#8220;data&#8221;) }</code>&#8216; When miau connects and registers user to server, miau can send pre-defined messages. User can define miau to send normal messages (`<font SIZE="-1"><code>PRIVMSG</code></font>&#8216;), notices (`<font SIZE="-1"><code>NOTICE</code></font>&#8216;) or arbitrary messages. </p>
<p> Mode can be one of the following: `<code>p</code>&#8216; private message (`<font SIZE="-1"><code>PRIVMSG</code></font>&#8216;). </p>
<p> `<code>n</code>&#8216; notice (`<font SIZE="-1"><code>NOTICE</code></font>&#8216;). Should be used with services and automatons, but unfortunately some network services can&#8217;t cope with notices. </p>
<p> `<code>r</code>&#8216; &#8220;raw&#8221; message. This means user must provide complete message to send to the server. Using raw message user has complete control over what is being sent. If you don&#8217;t know what this is, you don&#8217;t need this. When using modes &quot;`<code>p</code>&#8216;&#8220; or &#8221;`<code>n</code>&#8216;&quot;, user must provide both message and target where as with raw messages only one parameter in addition to type should be given. </p>
<p> This option might not be compiled in. </p>
<p> `<code>automodes = { &#8220;mask&#8221;:&#8220;privilegded&#8221; }</code>&#8216; List of people who are automatically given certain privilege on channel. Mask is given in form of `<code>mode:nick!username [at] host/#channel</code>&#8216; (where `<code>mode</code>&#8216; is a single character) and list is processed as a chain. </p>
<p> Note: You can define &#8220;your&#8221; hostname with @@. Only the _last_ occurance of @@ will be translated. </p>
<p> This option might not be compiled in. </p>
<p> `<code>automodedelay = &#8220;seconds&#8221;</code>&#8216; Time (in seconds) after first queued mode change would take effect. During this period of time miau can collect more than one mode change and commit up to three at a time. Other situation reasonaly big value (like 30) here could prove useful is channel where there are stupid &#8220;auto-oping&#8221; bots. (Stupid bots do mode changes even if someone else did that already.) </p>
<p> This option might not be compiled in. </p>
<p> `<code>cmdpasswd = &#8220;password&#8221;</code>&#8216; Password for remote commands. If this is 13 characters long, miau assumes it&#8217;s crypted. Comment this out or leave it empty to disable remote commands. When sending miau a remote command, password _always_ begins with column (&#8216;:&#8217;) (if `<code>cmdpasswd</code>&#8216; is set to &#8220;foobar&#8221; (or hash of it), you need to send miau a message beginning with `<code>:foobar</code>&#8216; to issue a remote command). miau can generate password-hashes with `<code>-c</code>&#8216; -switch, if it is compiled with that feature. </p>
<p> This feature might not be compiled in. </p>
<p> `<code>dccbounce = &#8220;state&#8221;</code>&#8216; miau can bounce DCCs. Set to true to enable bouncing. You probably don&#8217;t need this. </p>
<p> This option might not be compiled in. </p>
<p> `<code>dccbindhost = &#8220;host&#8221;</code>&#8216; If miau has separate IPs for IRC-network and clients, you should enter <font SIZE="-1">IP</font> for clients here. </p>
<p> This option might not be compiled in. </p>
<h2>Index</h2>
