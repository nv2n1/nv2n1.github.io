---
title: "bip(5)"
name: "bip"
section: "5"
letter: "b"
url: "/docs/linux/man/5-bip/"
description: "bip.conf – Configuration file for BIP IRC Proxy"
---

<p>bip.conf &#8211; Configuration file for BIP IRC Proxy</p>
<h2>Description</h2>
<p>A BIP configuration file consists of a list of variable affectations or sections. It contains the global options, networks definitions, users configuration, users connections declarations. Each section is described in this manpage. The bip.conf skeleton should be something like this : </p>
<pre><code>option1 = value;
option2 = value;
...

network {
    net_opt = value;
    ...
    server { ... };
    server { ... };
};
...

user {
    user_opt = value;
    ...
    connection {
        conn_opt = value;
        ...
        channel { ... };
    };
    connection {
        conn_opt = value;
        ...
        channel { ... };
        channel { ... };
        ...
    };
};
</code></pre>
<h2>Syntax Rules</h2>
<p>The syntax is quite simple :<br />
 &#8211; everything after the <code>#</code> character is ignored (comments)<br />
 &#8211; each variable affectation must be finished with a <code>;</code><br />
 &#8211; each section { } must be finished with a <code>;</code> </p>
<p> If you use vim you will probably want to use vim with the provided <code>bip.vim</code> syntax file to avoid common syntax and lexical mistakes. You can also find an example configuration file along with BIP.</p>
<h2>Global Options</h2>
<dl>
<dt><code>client_side_ssl</code> (default: <code>false</code>)</p>
<dd>When true, clients will need to connect to BIP using SSL. You&#8217;ll also need to generate a SSL cert/key pair in &lt;bipdir&gt;/bip.pem (usually ~/.bip/bip.pem or /var/lib/bip/bip.pem) or &lt;client_side_ssl_pem&gt; if defined. </p>
<dt><code>client_side_ssl_pem</code> (default: <code>&lt;bipdir&gt;/bip.pem</code>)</p>
<dd>Set this to the full path of the cert/key pair bip should use to accept clients SSL connections. </p>
<dt><code>ip</code></p>
<dd>Ignored for the time being. </p>
<dt><code>log</code> (default: <code>true</code>)</p>
<dd>When true, the log system is enabled. Else, BIP will not write a single log file. Backlog is then stored into memory. </p>
<dt><code>log_system</code> (default: <code>true</code>)</p>
<dd>When true, system messages such as connection errors are logged. Else, BIP will not write system logs. </p>
<dt><code>log_format</code> (default: <code>%u/%n/%Y-%m/%c.%d.log</code>)</p>
<dd>Determines the log file name depending on :<br />
 &#8211; %u username (name in user { }; section)<br />
 &#8211; %n network name (name in connection { }; section)<br />
 &#8211; %c channel name<br />
 &#8211; %Y 4 digits year<br />
 &#8211; %m 2 digits month<br />
 &#8211; %d 2 digits day </p>
<dt><code>log_level</code> (default: <code>1</code>)</p>
<dd>Specify the verbosity of BIP from 0 (fatal errors) to 6 (huge debug output) </p>
<dt><code>log_root</code> (default: <code>HOME/.bip/logs</code>)</p>
<dd>Main log directory. Sub-directories and files will be created from there depending on <code>log_format</code>. </p>
<dt><code>log_sync_interval</code> (default: <code>5</code>)</p>
<dd>Defines the delay between each logfiles sync to the disk. Must be a non null positive integer. </p>
<dt><code>pid_file</code> (default: <code>HOME/.bip/bip.pid</code>)</p>
<dd>Defines the file where BIP&#8217;s pid will be stored. BIP checks if this file exists and if the pid is still alive upon startup. If true, BIP refuses to start. </p>
<dt><code>port</code> (default: <code>7778</code>)</p>
<dd>The port on which BIP should listen for clients. </p>
</dl>
<h2>Network Section</h2>
<p>This section allows you to declare a network for use in the connection sections. It may appear more than once in the configuration file. </p>
<dl>
<dt><code>ssl</code> (default: <code>false</code>)</p>
<dd>If true, BIP will connect to this network using SSL only. You cannot mix SSL servers and non-SSL servers in the same network section. This is by choice, we believe it&#8217;s a bad idea. </p>
<dt><code>name</code></p>
<dd>It&#8217;s the network name used in the <code>connection section</code>. Please note that this value is not used in <code>log_format</code>, since it uses the variable <code>name</code> from the <code>connection section</code>. </p>
</dl>
<h2>Server Sub-Section</h2>
<p>BIP will cycle through the server sections list when reconnecting to a network. It may appear more than once in a network section. </p>
<dl>
<dt><code>host</code></p>
<dd>The server&#8217;s hostname or IP address. </p>
<dt><code>port</code> (default: <code>6667</code>)</p>
<dd>The server port to connect to. </p>
</dl>
<h2>User Section</h2>
<p>This section allows you to define the users allowed to connect to BIP and their options. It may appear more than once in the configuration file. </p>
<dl>
<dt><code>admin</code> (default: <code>false</code>)</p>
<dd>If a user has admin set to true, he&#8217;ll become a bip administrator, which allows him for example to RELOAD bip from IRC or to see the user configuration. </p>
<dt><code>backlog</code> (default: <code>true</code>)</p>
<dd>Enable or disable the whole backlog system, which allows clients to see a log replay upon connection. </p>
<dt><code>backlog_always</code> (default: <code>false</code>)</p>
<dd>If true, clients will always receive <code>backlog_lines</code> log lines, even if they were already sent before. That means : If <code>backlog_always</code> is false, backlog will be reset whenever there is no more client connected to a network. Else backlog will not be reset. This option should of course not be enabled if <code>backlog_lines</code> is 0 ! If you still want to do so, don&#8217;t forget to /BIP BLRESET sometimes. </p>
<dt><code>backlog_lines</code> (default: <code>10</code>)</p>
<dd>If set to 0, BIP will replay all the logs since last client disconnect. Else, it&#8217;ll replay exactly <code>backlog_lines</code> lines on each channel and privates. Be aware that BIP will replay <code>backlog_lines</code> lines of all privates, even if there are more. For example if Coyote told you 12 lines and then RoadRunner 6, you&#8217;ll only have a replay of the 6 RoadRunner&#8217;s lines and the last 4 of Coyote&#8217;s. </p>
<p> <code>backlog_no_timestamp</code> (default: <code>false</code>) If true, backlogged line won&#8217;t include the timestamp. </p>
<dt><code>backlog_reset_on_talk</code> (default: <code>false</code>)</p>
<dd>When true, backlog will be reset upon client talk (channel/private message or action). It means that next time you log to your bip session, the backlogging will start at the time right after your last words on that specific channel or query. </p>
<dt><code>backlog_reset_connection</code> (default: <code>false</code>)</p>
<dd>When true, backlog_reset_on_talk option above is changed in that the whole network backlog is resetted when you talk in the network. </p>
<dt><code>backlog_msg_only</code> (default: <code>false</code>)</p>
<dd>When true, bip will backlog only channel/private messages/notices. No topic change, nick change, user quit/part/join will be backlogged upon connection. </p>
<dt><code>bip_use_notice</code> (default: <code>false</code>)</p>
<dd>If <code>bip_use_notice</code> is true, bip&#8217;s notifications to the clients will be send as notices instead of private messages. For example, this setting applies to disconnection notifications or /BIP command replies. </p>
<dt><code>default_nick</code></p>
<dd>The default nick option for each <code>connection section</code> where no <code>nick</code> is defined. See <code>CONNECTION SECTION</code> for more details. </p>
<dt><code>default_realname</code></p>
<dd>The default realname option for each <code>connection section</code> where no <code>realname</code> is defined. See <code>CONNECTION SECTION</code> for more details. </p>
<dt><code>default_user</code></p>
<dd>The default user option for each <code>connection section</code> where no <code>user</code> is defined. See <code>CONNECTION SECTION</code> for more details. </p>
<dt><code>name</code></p>
<dd>The user name. It&#8217;ll be used to authenticate to bip and in <code>log_format</code>. </p>
<dt><code>password</code></p>
<dd>The password. It <code>MUST</code> be generated with <code>bipmkpw</code> or it&#8217;ll not work. </p>
<dt><code>ssl_check_mode</code> (default: <code>none</code>)</p>
<dd>Tells whether BIP should check the server SSL certificate and against what. Can be <code>none</code> for no check at all, <code>ca</code> to check if the cert is signed by a Certificate Authority in repository, or <code>basic</code> to check if cert exists in repository. The repository is defined by <code>ssl_check_store</code>. This allows a &quot;ssh-like&quot; private key generation scheme. Note that in basic mode: </p>
<p>&nbsp;<wbr>&#8211; expired certificates that are in the store are considered valid. </p>
<p>&nbsp;<wbr>&#8211; CA-signed certificates are considered valid even if not in store. </p>
<dt><code>ssl_check_store</code> (default: <code>not set</code>)</p>
<dd>This repository is browsed by BIP when a SSL certificate or CA check is needed. </p>
<dt><code>ssl_client_certfile</code> (default: <code>not set</code>)</p>
<dd>Some networks (OFTC at least) allow you to authenticate to nickserv services using a client side certificate. Make this variable point to the .pem file to use this feature. </p>
</dl>
<h2>Connection Sub-Section</h2>
<p>Each connection section associates a user to the networks he wants to connect to. Thus, it must be declared in the user sections, and can be used more than once. </p>
<dl>
<dt><code>away_nick</code> (default: <code>not set</code>)</p>
<dd>If set, and if there are no more client attached, BIP will change nickname to this <code>away_nick</code>. Your nickname will be restored upon client connect. </p>
<dt><code>no_client_away_msg</code> (default: <code>not set</code>)</p>
<dd>This options allows you to set an away message. This away message will be set when the last client disconnects, and removed when a client connects. </p>
<dt><code>follow_nick</code> (default: <code>false</code>)</p>
<dd>If set to true, when you change nick, BIP stores the new nickname as the new default nickname value. Thus, if you are disconnected from the server, BIP will restore the correct nickname. </p>
<dt><code>autojoin_on_kick</code> (default: <code>true</code>)</p>
<dd>If set to false bip will not attempt to re-join a channel from which you were kicked. </p>
<dt><code>ignore_first_nick</code> (default: <code>false</code>)</p>
<dd>If set to true, BIP will ignore the nickname sent by the client upon connect. Further nickname changes will be processed as usual. </p>
<dt><code>ignore_server_capab</code> (default: <code>true</code>)</p>
<dd>By default bip ignores when a server advertises the CAPAB feature. Servers that support this can prefix each line with a &quot;+&quot; or a &quot;-&quot; depending if a user is registered or not. xchat checks if a server has the CAPAB feature and enables it. If you have two clients connected to a bip connection, one that supports this mode and one that does not, you see the plus and the minuses on each line in the client that does not support CAPAB. To avoid that, when a server advertises CAPAB bip simply removes it. You can set this option to false to keep using CAPAB (if you only use clients that support it for instance). </p>
<dt><code>network</code></p>
<dd>The network name. See the <code>NETWORK SECTION</code>. </p>
<dt><code>nick</code></p>
<dd>BIP will send that string as your nickname upon connect. If not specified and if <code>default_nickname</code> is specified in the <code>user section</code>, BIP will use that default nickname string. </p>
<dt><code>on_connect_send</code></p>
<dd>You can specify this field more than once. BIP will send the text as is to the server. It&#8217;d be useful for a greet on connect or to send your NickServ password. </p>
<dt><code>password</code></p>
<dd>This is the irc server password, which is sent upon connection to the irc server only. </p>
<dt><code>realname</code></p>
<dd>BIP will send that string as the realname part (description in whois result) upon connect. If not specified and if <code>default_realname</code> is specified in the <code>user section</code>, BIP will use that default realname string. </p>
<dt><code>source_port</code></p>
<dd>If specified, tells BIP to connect from this port to the IRC server. </p>
<dt><code>ssl_check_mode</code> (default: <code>the user&#8217;s option</code>)</p>
<dd>See <code>ssl_check_mode</code> option in User options. </p>
<dt><code>user</code></p>
<dd>BIP will send that string as the user part (usually between ! and @ in a whois result) upon connect. It&#8217;s also used by the oidentd support (if enabled). If not specified and if <code>default_user</code> is specified in the <code>user section</code>, BIP will use that default user string. </p>
<dt><code>vhost</code></p>
<dd>If specified, BIP will use <code>vhost</code> as the IP address to bind to when connecting to the IRC server. It&#8217;ll allow you to use a specific IP address for this network when you have more than one. This options is totally useless to people who only have one IP address. </p>
</dl>
<h2>Channel Sub-Sub-Section</h2>
<p>This section defines the list of channels to join for a user on a particular network. It is to be found in the connection sections and appear more than once in a connection section. </p>
<dl>
<dt><code>name</code></p>
<dd>The channel name (#bip, &amp;bip, &#8230;). </p>
<dt><code>key</code></p>
<dd>The channel key if needed. </p>
<dt><code>backlog</code> (default: <code>true</code>)</p>
<dd>Enable or disable backlogging of this particular channel. Setting this to true will NOT enable the backlog system, see the User section. </p>
</dl>
<h2>See Also</h2>
<p>bip, bipmkpw </p>
<h2>Author</h2>
<p>bip authors:<br />
 Arnaud &#8216;nohar&#8217; Cornet<br />
 Loïc &#8216;Kyoshiro&#8217; Gomez </p>
<p> Thanks to jj, YS and lafouine, for hanging around while we were coding.<br />
 Crypto shamelessly taken from Christophe &#8216;sexy&#8217; Devine.<br />
 This man page is written by Loïc &#8216;Kyoshiro&#8217; Gomez.</p>
