---
title: "museekcontrol(1)"
name: "museekcontrol"
section: "1"
letter: "m"
url: "/docs/linux/man/1-museekcontrol/"
description: "MuseekControl – Command-Line control Python Script for Museekd"
---

<h2>NAME</h2>
<p> <code>MuseekControl</code> &#8211; Command-Line control Python Script for Museekd</p>
<h2>DESCRIPTION</h2>
<p> MuseekControl is command-line Python script that connects to <i><a href="/docs/linux/man/1-museekd/">museekd</a></i>(1) and initiates many different commands. Chat Room watching, one-time chat messages, browsing shares, searching, viewing User info and setting tickers are just some of the many commands available. </p>
<p> Only one museek option will work at a time. If two are set, the last one will be used. </p>
<p> Setting the interface and password on the command-line is a security risk. Since interface and password settings are saved to the config file when set, you should set them, exit museekcontrol, and rerun museekcontrol without the password options on the commandline..LP </p>
<p> Before running, you will need a working <i><a href="/docs/linux/man/1-museekd/">museekd</a></i>(1) and need to know your museekd interface and interface password. Configure those with <i><a href="/docs/linux/man/1-musetup/">musetup</a></i>(1).</p>
<h2>SYNOPSIS</h2>
<p> <code>museekcontrol</code> [-c |&#8211;config &lt;<i>config-filename</i>&gt;] [&#8211;gs | &#8211;gsearch &lt;<i>query</i>&gt;] [&#8211;rs | &#8211;rsearch &lt;<i>query</i>&gt;] [&#8211;bs | &#8211;bsearch &lt;<i>query</i>&gt;] [-r | &#8211;rooms] [&#8211;roomlist] [&#8211;joined] [&#8211;roominfo &lt;<i>room</i>&gt;] [&#8211;roomsinfo] [&#8211;sroom &lt;<i>room</i>&gt;] [&#8211;srooms] [&#8211;sprivate &lt;<i>user</i>&gt;] [&#8211;sprivates] [&#8211;tickers &lt;<i>room</i>&gt;] [&#8211;alltickers] [-j | &#8211;join &lt;<i>room</i>&gt;] [-l | &#8211;leave &lt;<i>room</i>&gt;] [-m | &#8211;message &lt;<i>message</i>&gt;] [&#8211;chat &lt;<i>room</i>&gt;] [&#8211;pm | &#8211;private &lt;<i>user</i>&gt;] [&#8211;setticker &lt;<i>room</i>&gt;] [&#8211;settempticker &lt;<i>room</i>&gt;] [&#8211;setdefaultticker] [&#8211;buddy | &#8211;unbuddy &lt;<i>user</i>&gt;] [&#8211;ignore | &#8211;unignore &lt;<i>user</i>&gt;] [&#8211;ban | &#8211;unban &lt;<i>user</i>&gt;] [&#8211;trust | &#8211;distrust &lt;<i>user</i>&gt;] [&#8211;comment &lt;<i>string</i>&gt;] [&#8211;info &lt;<i>user</i>&gt;] [&#8211;minfo] [&#8211;ip &lt;<i>user</i>&gt;] [-b | &#8211;browse &lt;<i>user</i>&gt;] [&#8211;mb | &#8211;mbrowse] [-t | &#8211;transfers] [&#8211;mt | &#8211;mtransfers] [&#8211;download <i><a href="slsk://user/path">slsk://user/path</a></i>] [&#8211;upload <i><a href="slsk://user/path">slsk://user/path</a></i>] [&#8211;abortup <i><a href="slsk://user/path">slsk://user/path</a></i>] [&#8211;abortdown <i><a href="slsk://user/path">slsk://user/path</a></i>] [&#8211;removeup <i><a href="slsk://user/path">slsk://user/path</a></i>] [&#8211;removedown <i><a href="slsk://user/path">slsk://user/path</a></i>] [&#8211;retryup <i><a href="slsk://user/path">slsk://user/path</a></i>] [&#8211;retrydown <i><a href="slsk://user/path">slsk://user/path</a></i>] [-i | &#8211;interface &lt;<i>host:port | /socket.path</i>&gt; [-p | &#8211;password &lt;<i>inteface-password</i>&gt;] [-v | &#8211;version] [-h | &#8211;help]</p>
<h2>OPTIONS</h2>
<p> Museekcontrol accepts the following options:</p>
<dl>
<dt><code>-c &lt;</code><i>filename</i>&gt;, &#8211;config &lt;<i>filename</i>&gt;</p>
<dd> Use a different config file. v SEARCHING:</p>
<dt><code>&#8211;gs, &#8211;gsearch &lt;</code><i>query</i>&gt;</p>
<dd> Globally search for query &amp; show results</p>
<dt><code>&#8211;rs, &#8211;rsearch &lt;</code><i>query</i>&gt;</p>
<dd> Room search for query &amp; show results</p>
<dt><code>&#8211;bs, &#8211;bsearch &lt;</code><i>query</i>&gt;</p>
<dd> Buddy search for query &amp; show results</p>
<dt>CHAT ROOMS:</p>
<dd>
<dt><code>-r, &#8211;rooms</code></p>
<dd> Show list of rooms</p>
<dt><code>&#8211;roomlist</code></p>
<dd> Refresh list of rooms</p>
<dt><code>&#8211;joined</code></p>
<dd> Show list of Joined rooms</p>
<dt><code>&#8211;roominfo &lt;</code><i>room</i>&gt;</p>
<dd> Show users in a Joined room</p>
<dt><code>&#8211;roomsinfo</code></p>
<dd> Show users for all Joined rooms</p>
<dt><code>&#8211;sroom &lt;</code><i>room</i>&gt;</p>
<dd> Show chat log for room</p>
<dt><code>&#8211;srooms</code></p>
<dd> Show chat log for all rooms</p>
<dt><code>-j, &#8211;join &lt;</code><i>room</i>&gt;</p>
<dd> Join a room</p>
<dt><code>-l, &#8211;leave &lt;</code><i>room</i>&gt;</p>
<dd> Leave a room</p>
<dt><code>&#8211;chat &lt;</code><i>room</i>&gt;</p>
<dd> Use with &#8211;message</p>
<dt><code>-m, &#8211;message &lt;</code><i>message</i>&gt;</p>
<dd> Say message in room (Use with &#8211;chat)</p>
<dt>TICKERS:</p>
<dd>
<dt><code>&#8211;tickers &lt;</code><i>room</i>&gt;</p>
<dd> Show tickers in room</p>
<dt><code>&#8211;alltickers</code></p>
<dd> Show tickers in all rooms</p>
<dt><code>&#8211;setticker &lt;</code><i>room</i>&gt;</p>
<dd> Pick a room to set the ticker in. (Use with &#8211;message)</p>
<dt><code>&#8211;settempticker &lt;</code><i>room</i>&gt;</p>
<dd> Pick a room for a temporary ticker (Use with &#8211;message)</p>
<dt><code>&#8211;setdefaultticker</code></p>
<dd> Set the default ticker for all room (Use with &#8211;message)</p>
<dt><code>-m, &#8211;message &lt;</code><i>message</i>&gt;</p>
<dd> Set the ticker to this.</p>
<dt>PRIVATE CHAT:</p>
<dd>
<dt><code>&#8211;sprivate &lt;</code><i>user</i>&gt;</p>
<dd> Show Private Chat log for a user</p>
<dt><code>&#8211;sprivates</code></p>
<dd> Show Private Chat logs for all users</p>
<dt><code>&#8211;pm, &#8211;private &lt;</code><i>user</i>&gt;</p>
<dd> Say message in PM (Use with &#8211;message)</p>
<dt><code>-m, &#8211;message &lt;</code><i>message</i>&gt;</p>
<dd> Say message in PM (Use with &#8211;pm)</p>
<dt>USERS:</p>
<dd>
<dt><code>&#8211;buddy &#8211;unbuddy &lt;</code><i>user</i>&gt;</p>
<dd> Add/Remove user from Buddies list</p>
<dt><code>&#8211;ignore &#8211;unignore &lt;</code><i>user</i>&gt;</p>
<dd> Add/Remove user from Ignore list</p>
<dt><code>&#8211;ban &#8211;unban &lt;</code><i>user</i>&gt;</p>
<dd> Add/Remove user from Banned list</p>
<dt><code>&#8211;trust &#8211;distrust &lt;</code><i>user</i>&gt;</p>
<dd> Add/Remove user from Trusted list</p>
<dt><code>&#8211;comment &lt;</code><i>string</i>&gt;</p>
<dd> Comment for the user in list</p>
<dt>USERINFO:</p>
<dd>
<dt><code>&#8211;info &lt;</code><i>user</i>&gt;</p>
<dd> Show a user&#8217;s info (Saves image to &lt;user&gt;.img if available)</p>
<dt><code>&#8211;minfo</code></p>
<dd> Monitor all User Info</p>
<dt><code>&#8211;ip &lt;</code><i>user</i>&gt;</p>
<dd> Get a user&#8217;s IP and Port<br />
&nbsp;<wbr>&nbsp;<wbr>BROWSING:</p>
<dt><code>-b. &#8211;browse &lt;</code><i>user</i>&gt;</p>
<dd> Get a user&#8217;s shares and show them</p>
<dt><code>&#8211;mb, &#8211;mbrowse</code></p>
<dd> Monitor browsing </p>
<p>&nbsp;<wbr>&nbsp;<wbr>TRANSFERS:</p>
<dt><code>-t, &#8211;transfers</code></p>
<dd> Display all current uploads and downloads and exit.</p>
<dt><code>&#8211;mt, &#8211;mtransfers</code></p>
<dd> Monitor transfers</p>
<dt><code>&#8211;download </code><i><a href="slsk://user/path">slsk://user/path</a></i></p>
<dd> Add file or dir to the download queue</p>
<dt><code>&#8211;upload </code><i><a href="slsk://user/path">slsk://user/path</a></i></p>
<dd> Attempt to upload file to user</p>
<dt><code>&#8211;abortup </code><i><a href="slsk://user/path">slsk://user/path</a></i></p>
<dd> Abort Upload</p>
<dt><code>&#8211;abortdown </code><i><a href="slsk://user/path">slsk://user/path</a></i></p>
<dd> Abort Download</p>
<dt><code>&#8211;removeup </code><i><a href="slsk://user/path">slsk://user/path</a></i></p>
<dd> Remove Upload from queue</p>
<dt><code>&#8211;removedown </code><i><a href="slsk://user/path">slsk://user/path</a></i></p>
<dd> Remove Download from queue</p>
<dt><code>&#8211;retryup </code><i><a href="slsk://user/path">slsk://user/path</a></i></p>
<dd> Retry Upload (for remote uploads)</p>
<dt><code>&#8211;retrydown </code><i><a href="slsk://user/path">slsk://user/path</a></i></p>
<dd> Retry Download </p>
<dt><code>-i, &#8211;interface &lt;</code><i>host:port | /socket.path</i>&gt;</p>
<dd> Choose a different interface (saved to config file)</p>
<dt><code>-p, &#8211;password &lt;</code><i>interface-password</i>&gt;</p>
<dd> Choose a different password (saved to config file)</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Display Version and exit.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display Help and exit. </p>
</dl>
<h2>EXAMPLE</h2>
<p> To run this program the standard way type: </p>
<p> museekcontrol </p>
<p> Alternativly you use a different config file with: </p>
<p> museekcontrol &#8211;config museekcontrol.config </p>
<p> To set the interface password: </p>
<p> museekcontrol &#8211;password 1234567890 </p>
<p> To listen to all joined Chat Rooms: </p>
<p> museekcontrol &#8211;srooms </p>
<p> To Search Globally for &quot;crazy pumpkin rabbits&quot;: </p>
<p> museekcontrol &#8211;gsearch &quot;crazy pumpkin rabbits&quot;</p>
<h2>FILES</h2>
<dl>
<dt>
&nbsp;<wbr><i>~/.museekd/museekcontrol.config</i></p>
<dd> The default location for the <code>museekcontrol</code> config file.</dl>
<h2>AUTHORS</h2>
<p> daelstorm &lt;daelstorm [at] gmail.com&gt; </p>
<p> Hyriand &lt;hyriand [at] thegraveyard.org&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-mucous/">mucous</a></i>(1) <i><a href="/docs/linux/man/1-mulog/">mulog</a></i>(1) <i><a href="/docs/linux/man/1-murmur/">murmur</a></i>(1) <i><a href="/docs/linux/man/1-muscan/">muscan</a></i>(1) <i><a href="/docs/linux/man/1-muscand/">muscand</a></i>(1) <i><a href="/docs/linux/man/1-museekd/">museekd</a></i>(1) <i><a href="/docs/linux/man/1-museeq/">museeq</a></i>(1) <i><a href="/docs/linux/man/1-musetup/">musetup</a></i>(1) <i><a href="/docs/linux/man/1-musetup-gtk/">musetup-gtk</a></i>(1) </p>
<h2>Index</h2>
