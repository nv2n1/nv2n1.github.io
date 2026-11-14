---
title: "epic(1)"
name: "epic"
section: "1"
letter: "e"
url: "/docs/linux/man/1-epic/"
description: "epic – Internet Relay Chat client for UNIX like systems"
---

<h2>NAME</h2>
<p> <code>epic</code> &#8211; Internet Relay Chat client for UNIX like systems</p>
<h2>SYNOPSIS</h2>
<p> <code>epic</code> [<i>-a</i> ] [<i>-b</i> ] [<i>-B</i> ] [<i>-c chan</i> ] [<i>-d </i> ] [<i>-f </i> ] [<i>-F </i> ] [<i>-h </i> ] [<i>-H hostname</i> ] [<i>-l filename</i> ] [<i>-L filename </i> ] [<i>-n nickname</i> ] [<i>-o</i> ] [<i>-O</i> ] [<i>-p port</i> ] [<i>-q </i> ] [<i>-v</i> ] [<i>-x</i> ] [<i>-z username</i> ] [<i>nickname</i> ] [<i>server description list</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>ircII/EPIC</code> program is a unix-based character oriented user agent (&#8216;client&#8217;) to Internet Relay Chat. It is a fully functional ircII client with many useful extensions. This version works with all modern irc server classes as of early 1999. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Append the server description list to the default server list. The default behavior is for the server description list to replace the default server list.</p>
<dt><code>-b</code></p>
<dd> Operate in so called &#8220;bot mode. &#8221; This implies the [<i>-d</i> ] option. EPIC will <a href="/docs/linux/man/2-fork/">fork</a>(2) immediately and the parent process will exit, returning you to your shell. Some system administrators do not look kindly to their users running bots, and they have disabled this option. Even if your administrator has not disabled it, you should not assume this gives you automatic permission to run a bot. If you do run a bot without permission, your administrator may get very angry with you, and possibly revoke your account. In addition, most IRC operators on public irc networks have very little tolerance for people who run bots. So just a word of caution, make sure that your system administrator and your irc administrator have given you permission before you run a bot.</p>
<dt><code>-B</code></p>
<dd> Force the startup file to be loaded immediately rather than waiting until a connection to a server is established.</p>
<dt><code>-c </code><i>chan</i></p>
<dd> Join the specified channel the first time you successfully connect to a server.</p>
<dt><code>-d</code></p>
<dd> Operate in &#8220;dumb mode.&#8221; The client will not put up a full screen display, and will read from standard input and write to standard output. This is useful if the output normally looks awful (because you are using an incorrect <code>TERM </code> setting, or your terminal description is spectacularly broken), or you just don&#8217;t want to use the pretty interface. This option will be turned on automatically if your current <code>TERM</code> setting is not capable of a full screen display.</p>
<dt><code>-f</code></p>
<dd> Force use of hardware flow control. With this option, the control-S and control-Q keys are probably not available to be bound to something else.</p>
<dt><code>-F</code></p>
<dd> Disable use of hardware flow control. With this option, the control-S and control-Q keys are available to be bound to something else. However, you will not have hardware flow control.</p>
<dt><code>-h</code></p>
<dd> Display a moderately concise help message and exit immediately.</p>
<dt><code>-H </code><i>hostname</i></p>
<dd> Use the IP address of the specified hostname as your default IP address. This can be used if you have multiple IP addresses on the same machine and you want to use an address other than the default address. You might need to use this option when <a href="/docs/linux/man/3-gethostname/">gethostname</a>(3) does not return a hostname (in some poorly configured NIS environments). The use of multiple IP addresses on a single machine is commonly referred to as &quot;virtual hosting&quot;, and each IP address is a &quot;virtual host&quot;. Please understand that an irc client may not tell the irc server what your hostname should be: the server alone determines that. Servers typically use the canonical hostname for an IP address as your hostname. Because of this, this option will not permit you to use a CNAME (secondary hostname for an IP address), because the server will use the canonical hostname instead. This option overrides the <code>IRCHOST </code> environment variable.</p>
<dt><code>-l </code><i>filename,[filename]</i></p>
<dd> Use the specified filename(s) as the startup file. The startup file is loaded the first time you successfully connect to a server, unless you specify the [<i>-B</i> ] option. This overrides the <code>IRCRC</code> environment variable. If this option is not specified, and the <code>IRCRC</code> environment variable is not set, then ~/.ircrc is the default startup file.</p>
<dt><code>-n </code><i>nickname</i></p>
<dd> Use the specified nickname as the default nickname whenever you connect to an irc server. This option overrides the <code>IRCNICK</code> environment variable. This option can be overridden if you specify nickname argument in the command line (see below).</p>
<dt><code>-o</code></p>
<dd> Force use of IEXTEN termios characters. POSIX systems are allowed to reserve additional control characters to perform special actions when IEXTEN is turned on. On 4.4BSD, the control-V and control-O keys are used by IEXTEN and thus cannot be used in key bindings within EPIC since the terminal never sends them to EPIC.</p>
<dt><code>-O</code></p>
<dd> Disable use of IEXTEN termios characters. This makes all of the keys reserved by your system&#8217;s IEXTEN termios option available to be used in key bindings. On 4.4BSD, this flag is necessary if you want to use control-V and control-O in your key bindings.</p>
<dt><code>-p </code><i>port</i></p>
<dd> Use the specified port as the default port for new server connections. The default port is usually 6667. Make sure that the servers you want to connect to are listening on this port before you try to connect there.</p>
<dt><code>-q</code></p>
<dd> Suppress the loading of any file when you first establish a connection to an irc server.</p>
<dt><code>-v</code></p>
<dd> Output version identification (VID) information and exit.</p>
<dt><code>-x</code></p>
<dd> This undocumented feature turns on all of the XDEBUG flags. Refer to the help files for XDEBUG if you want to know what happens if you use this.</p>
<dt><code>-z </code><i>username</i></p>
<dd> Use the specified username when negotiating a connection to a new irc server. This overrides the <code>IRCUSER</code> environment variable. If this option is not specified, then the user name specified in /etc/passwd for your user is used. This feature was formerly undocumented, but with the rise and popularity and use of <a href="/docs/linux/man/8-identd/">identd</a>(8) this option is much less useful than it once was. Requests to have this option removed will probably be ignored. If you don&#8217;t want your users to spoof their usernames, install identd, and do everyone on IRC a favor.</p>
<dt><code>nickname</code></p>
<dd> The first bare word found is taken as the default nickname to use. This overrides all other options, including the -n option and the <code>IRCNICK </code> environment variable. If all else fails, then the client uses your login name as the default nickname.</p>
<dt><code>server,[server]</code></p>
<dd> After the nickname, a list of one or more server specifications can be listed. Unless you specify the -a option, this will replace your default server list! The -a option forces any servers listed here to be appended to the default server list. The format for server specifications is: </p>
<blockquote><p><tt>hostname:port:password:nick</tt></p></blockquote>
<p> Any item can be omitted by leaving the field blank, and any trailing colons can also be omitted.</dl>
</dl>
<h2>DETAILED DESCRIPTION</h2>
<h3>The Screen:</h3>
<p> The screen is split into two parts, separated by an inverse-video status line (if supported). The upper (larger) part of the screen displays responses from the <a href="/docs/linux/man/8-ircd/">ircd</a>(8) server. The lower part of the screen (a single line) accepts keyboard input. </p>
<p> Some terminals do not support certain features required by <code>epic</code> , in which case you receive a message stating this. If this occurs, try changing the terminal type or run <code>epic</code> with the -d option.</p>
<h3>Irc Commands:</h3>
<p> Any line beginning with the slash character &#8220;/&#8221; is regarded as an <code>epic</code> command (the command character may be changed). Any line not beginning with this character is treated as a message to be sent to the current channel. The client has a built in help system. Install the help files (they should be available at the same place you got the client) and then type &#8220;/help&#8221; to open up the help system.</p>
<h3>The .ircrc File:</h3>
<p> When <code>epic</code> is executed, it checks the user&#8217;s home directory for a ~/.ircrc file, executing the commands in the file. Commands in this file do not need to have a leading slash character &#8220;/&#8221; This allows predefinition of aliases and other features.</p>
<h2>PRACTICAL EXAMPLES</h2>
<p> Certainly any description of <code>epic </code> in this man page will be sorely inadequate because most of the confusion doesn&#8217;t even start until after you get the client to connect to a server. But if you really have problems getting the client to connect to a server, try some of these:</p>
<dl>
<dt><code>epic</code></p>
<dd> Try this first. This will assume all the defaults. If the person who is maintaining epic at your site has done a halfway decent job, this will put you on a server that is somewhat local to you.</p>
<dt><code>epic nickname irc.domain.com</code></p>
<dd> or something similar will attempt to connect to the irc server running on the host &quot;irc.domain.com&quot; (fill in a real irc server here) with the nickname of well, &quot;nickname&quot;. This is the most common way to specify an alternate server to use.</p>
<dt><code>epic nickname irc.domain.com:6664</code></p>
<dd> Sometimes, some servers are really busy, and it can take them a long time to establish a connection with you on the default port (6667). Most major servers on big public networks accept connections on many different ports, with the most common being most or all of the ports between 6660 and 6675. You can usually connect much faster if you use a port other than 6667, if the server you&#8217;re connecting to supports an alternate port.</p>
<dt><code>epic nickname irc.efnet.net</code></p>
<dd> If you&#8217;re totally stumped and trying to get on efnet, try this.</p>
<dt><code>epic nickname irc.undernet.org</code></p>
<dd> If you&#8217;re totally stumped and trying to get on undernet, try this.</p>
<dt><code>epic nickname irc.dal.net</code></p>
<dd> If you&#8217;re totally stumped and trying to get on dalnet, try this.</dl>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>/usr/local/bin/epic</code></p>
<dd> the default location of the binary</p>
<dt><code>~/.ircrc</code></p>
<dd> default initialization file</p>
<dt><code>~/.irc/</code></p>
<dd> directory you can put your own <code>epic</code> scripts into, that can then be loaded with /load</p>
<dt><code>/usr/local/share/epic</code></p>
<dd> default directory containing message-of-the-day, master initialization, help files and <code>epic</code> scripts</dl>
</dl>
<h2>THE HELP FILES</h2>
<p> Starting up the client is the easy part. Once you get connected, you&#8217;ll probably find you have no idea what you&#8217;re doing. That&#8217;s where the help files come in. If the person who maintains irc at your site didn&#8217;t install the help files, pester them until they do. Once the help files are available, use the &#8220;/help&#8221; command to get started. There are a bazillion commands and a multitude of nuances that will take a few months to get down pat. But once you do, you will be so firmly addicted to irc that your wife will divorce you, your kids will leave you, your dog will run away, and you&#8217;ll flunk all your classes, and be left to sing the blues.</p>
<h2>USEFUL WEB RESOURCES</h2>
<p> Tp </p>
<p> &lt;<a rel="nofollow" href="http://www.epicsol.org/">http://www.epicsol.org/</a>&gt; The EPIC home page Tp </p>
<p> &lt;<a rel="nofollow" href="http://help.epicsol.org/">http://help.epicsol.org/</a>&gt; The Online EPIC Help Pages Tp </p>
<p> &lt;<a rel="nofollow" href="http://www.irchelp.org/">http://www.irchelp.org/</a>&gt; Lots of great help for new irc users.</p>
<h2>SIGNALS</h2>
<p> <code>epic</code> handles the following signals gracefully </p>
<dl>
<dt>
<dl>
<dd>
<dt><code>SIGUSR1</code></p>
<dd> Closes all DCC connections and EXEC&#8217;d processes. </p>
</dl>
</dl>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> It can be helpful to predefine certain variables in in the ~/.cshrc , ~/.profile , or ~/.login file:</p>
<dl>
<dt><code>IRCNICK </code></p>
<dd> The user&#8217;s default IRC nickname</p>
<dt><code>IRCNAME </code></p>
<dd> The user&#8217;s default IRC realname (otherwise retrieved from /etc/passwd )</p>
<dt><code>IRCSERVER </code></p>
<dd> The user&#8217;s default IRC server list (see server option for details)</p>
<dt><code>HOME </code></p>
<dd> Overrides the default home page in /etc/password</p>
<dt><code>TERM </code></p>
<dd> The type of terminal emulation to use</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-ircd/">ircd</a>(8)</p>
<h2>BUGS</h2>
<p> Any non-trivial piece of software has bugs. ircII/EPIC is no exception. You can refer to the KNOWNBUGS file that is distributed with the client source code for a list of problems that are known to exist and may or may not be fixed some day. If you find a bug that is not listed there, you can refer to the BUG_FORM file that is also distributed with the source code. It will give you instructions on how to fill out the report and where to send it.</p>
<h2>ERRATA</h2>
<p> The online documentation probably should be in docbook form rather than in the current help format. The entire help system is a hack. </p>
<p> This manual page only describes the options to epic, but doesn&#8217;t tell you what to do once you get connected.</p>
<h2>AUTHORS</h2>
<p> Program written by Michael Sandrof (ms5n+ [at] andrew.cmu.edu). The copyright holder is Matthew Green (mrg [at] mame.mu.oz.au). This software is maintained by Jeremy Nelson (jnelson [at] acronet.net) on behalf of the EPIC project (list [at] epicsol.org). </p>
<p> At one time or another, this man page has been edited by Darren Reed, R.P.C. Rodgers, the lynX, Matthew Green, and Jeremy Nelson. </p>
<h2>Index</h2>
