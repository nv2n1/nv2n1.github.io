---
title: "kvirc(1)"
name: "kvirc"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kvirc/"
description: "KVIrc – an Internet Relay Chat client."
---

<h2>NAME</h2>
<p> KVIrc &#8211; an Internet Relay Chat client.</p>
<h2>SYNOPSIS</h2>
<p> <code>kvirc [options] [server [port]] [ircurl [ircurl [&#8230;]]]</code> </p>
<h2>DESCRIPTION</h2>
<p> KVIrc is a Visual Internet Relay Chat client based on the Qt library. </p>
<p> It is intended to be an &quot;user friendly&quot; interface to the IRC protocol (see <i>RFC1459</i>) and its extensions.</p>
<h2>OPTIONS</h2>
<p> <i>KVIrc</i> accepts the following options:</p>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Display a list of all commandline options and exit.</dd>
<dt><code>-v, &#8211;version</code></dt>
<dd> Output the version info.</dd>
<dt><code>-c </code><i>&lt;file&gt;</i></dt>
<dd> Use <i>&lt;file&gt;</i> as configuration file instead of ~/.kvirc.rc . Defaults to $HOME/.kvirc.rc if <i>&lt;file&gt;</i> doesn&#8217;t exists</dd>
<dt><code>-n </code><i>&lt;file&gt;</i></dt>
<dd> Use <i>&lt;file&gt;</i> as configuration file instead of ~/.kvirc.rc . Create <i>&lt;file&gt;</i> if it doesn&#8217;t exist.</dd>
<dt><code>-f</code></dt>
<dd> Force a new KVIrc session, even if there is already a running one.</dd>
<dt><code>-e </code><i>&lt;commands&gt;</i></dt>
<dd> If a KVIrc session is already running, execute the <i>&lt;commands&gt;</i> in that session, otherwise startup normally and execute <i>&lt;commands&gt;</i>. <i>&lt;commands&gt;</i> must be a single shell token. You can eventually use this switch more than once.</dd>
<dt><code>-x </code><i>&lt;commands&gt;</i></dt>
<dd> If a KVIrc session is already running, execute the <i>&lt;commands&gt;</i> in that session, otherwise do nothing and exit. <i>&lt;commands&gt;</i> must be a single shell token. You can eventually use this switch more than once.</dd>
<dt><code>-r </code><i>&lt;commands&gt;</i></dt>
<dd> If a KVIrc session is already running, execute the <i>&lt;commands&gt;</i> in that session, otherwise start up normally (do not execute). <i>&lt;commands&gt;</i> must be a single shell token. You can eventually use this switch more than once.</dd>
<dt><code>-m</code></dt>
<dd> If a KVIrc session is already running, show an informational popup dialog instead of writing to the console. This is useful when starting KVIrc from a graphical taskbar button.</dd>
<dt><code>&#8211;nosplash</code></dt>
<dd> Do not show the splash screen at startup</dd>
<dt><code>[server]</code></dt>
<dd> Connect to this server after startup.</dd>
<dt><code>[port]</code></dt>
<dd> Use this port for connection. This option requires also a server name.</dd>
<dt><code>[ircurl]</code></dt>
<dd> An url in the following form: </dd>
<p>&nbsp;<wbr>&nbsp;<wbr>irc[6]://&lt;server&gt;[:&lt;port&gt;][/&lt;channel&gt;[?&lt;pass&gt;]] </p>
<p> For each url on the commandline create a new irc-context and attempt to connect to &lt;server&gt; on the specified &lt;port&gt;. The optional &lt;channel&gt; is joined just after the connection has been estabilished. </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>KVIRC_LANG</code></dt>
<dd> Language setting. If not set KVIrc will check for $LANG</dd>
<dt><code>LANG</code></dt>
<dd> Language setting. If not set (or set to &#8216;EN&#8217;,&#8217;POSIX&#8217; or &#8216;C&#8217;) KVIrc will use the default language (english).</dd>
</dl>
<h2>FILES</h2>
<p> <code>$PREFIX</code>/share/kvirc/<code>VERSION</code>/* Directory with the global KVIrc settings, modules etc&#8230; </p>
<p> <code>$HOME</code>/.kvirc.rc . This is the first file that KVIrc looks for. If the -c commandline option is specified , the file passed as the option parameter is used instead of this one. If the file is found , KVIrc reads the first non-empty line and treats it as the path to the <i>KVIrc Local directory</i>. If the file can not be found or the <i>KVIrc Local directory</i> is not existing , KVIrc enters the setup mode and allows selecting a new <i>KVIrc Local directory</i>. </p>
<p> <code>KVIrc Local directory</code>/* Directory with the local (per user) KVIrc settings. Similar to the global one. </p>
<h2>SEE ALSO</h2>
<p> <code>X</code>(1) <code><a href="/docs/linux/man/1-talk/">talk</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1999-2009 Szymon Stefanek and The KVIrc Development Team </p>
<p> Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation. </p>
<h2>SUGGESTIONS AND BUG REPORTS</h2>
<p> Any bugs found (and feature requests) should be reported to the tracker at: <i>&lt;<a rel="nofollow" href="https://svn.kvirc.de/">https://svn.kvirc.de/</a>&gt;</i> </p>
<h2>OFFICIAL WWW SITE</h2>
<p> <a rel="nofollow" href="http://www.kvirc.net">http://www.kvirc.net</a> In Russian &#8211; <a rel="nofollow" href="http://www.kvirc.net.ru">http://www.kvirc.net.ru</a> </p>
<h2>AUTHORS</h2>
<p> Szymon &#8216;Pragma&#8217; Stefanek <i>&lt;pragma at kvirc dot net&gt;</i> </p>
<p> Code, fixes, new features, and much more from Alessandro &#8216;Noldor [at] freenode&#8217; Carbone, Elvio &#8216;HelLViS69 [at] freenode&#8217; Basello, Fabio &#8216;CtrlAltCa [at] freenode&#8217; Bas, Alexey &#8216;Alexey [at] freenode&#8217; Uzhva, Voker57 [at] freenode </p>
<p> Old authors </p>
<p> With patches, fixes, extensions, and more from [Anodine]@efnet, Till &#8216;BuTi [at] ircnet&#8217; Busch, Fritz &#8216;KNFritz [at] ircnet&#8217; Elfert, RAD Kade 1 </p>
<p> With bug-hunting, hard-thinking, eyes-consuming, nights spent on IRC, great suggestions and more from lots of people all over the net, including but not limited to Paul &#8216;infected [at] ircnet&#8217; Boehm, Olle &#8216;Crocodile [at] ircnet&#8217; H[:a]lln[:a]s, Diablo [at] ircnet, Andrew &#8216;Drosha [at] ircnet&#8217; Frolov, MalboroLi [at] ircnet, munehiro [at] ircnet </p>
<h2>Index</h2>
