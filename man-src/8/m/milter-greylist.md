---
title: "milter-greylist(8)"
name: "milter-greylist"
section: "8"
letter: "m"
url: "/docs/linux/man/8-milter-greylist/"
description: "milter-greylist – grey listing filter for sendmail"
---

<p><code>milter-greylist </code> &#8211; grey listing filter for sendmail</p>
<h2>Synopsis</h2>
<p><code>milter-greylist </code> [<code>-A</code>] [<code>-a </code><i>autowhite_delay</i>] [<code>-c</code>] [<code>-D</code>] [<code>-d </code><i>dumpfile</i>] [<code>-f </code><i>configfile</i>] [<code>-h</code>] [<code>-l</code>] [<code>-q</code>] [<code>-r</code>] [<code>-S</code>] [<code>-T</code>] [<code>-u </code><i>username</i>[:<i>groupname</i>]] [<code>-v</code>] [<code>-w </code><i>greylist_delay</i>] [<code>-L </code><i>cidrmask</i>] [<code>-M </code><i>prefixlen</i>] [<code>-P </code><i>pidfile</i>] <code>-p</code> <i>socket</i></p>
<h2>Description</h2>
<p><code>milter-greylist</code> is a mail filter for sendmail that implements grey listing, a spam filtering technique proposed by Evan Harris. </p>
<p> Grey listing works by assuming that contrarily to legitimate MTA, spam engines will not retry sending their junk mail on a temporary error. The filter will always temporarily reject mail on a first attempt, and accept it after some time has elapsed. </p>
<p> If spammers ever try to resend rejected messages, we can assume they will not stay idle between the two sends. Odds are good that the spammer will send a mail to an honey pot address and get blacklisted in a distributed black list before the second attempt. </p>
<p> Of course, the filter can be configured to not apply grey listing to some hosts or networks. You can whitelist friendly SMTP servers, and you should whitelist your own network, otherwise your SMTP clients will have real trouble to send e-mail. Whitelisting localhost is also a must. </p>
<p> <code>milter-greylist</code> works with two files. <i>greylist.conf</i> is the configuration file. It holds the whitelist of addresses that will not suffer grey list filtering. It is read once upon <code>milter-greylist</code> startup, then it will be automatically reloaded whenever a new message gets in and if it had been modified. You should not send <code>milter-greylist</code> a kill -1 as it will just terminate it (libmilter works that way). </p>
<p> See <code><a href="/docs/linux/man/5-greylist-conf/">greylist.conf</a>(5)</code> for documentation on the file&#8217;s format. </p>
<p> The second file is <i>greylist.db</i>. <code>milter-greylist</code> will regularly dump its grey list database into this file, which is used on startup to restore the previous grey list state. If the file does not exist or is unreadable, <code>milter-greylist</code> will start with an empty grey list. </p>
<p> The default location for the grey list database and the socket for communicating with sendmail is <code>/var/milter-greylist/</code>. That directory must be owned and writeable by the user id under which <code>milter-greylist</code> runs. </p>
<p> The following options are available; if present, they override their equivalents specified in the configuration file:</p>
<dl>
<dt><code>-A</code></p>
<dd>Normally, <code>milter-greylist</code> does not greylist senders that succeeded SMTP AUTH. This option disables that feature and causes authentication to be ignored. Equivalent to the <i>noauth</i> option in the configuration file.</p>
<dt><code>-a </code><i>autowhite_delay</i></p>
<dd>Configure auto-whitelisting. After a tuple (sender IP, sender e-mail, recipient e-mail) has been accepted, other identical tuples will get accepted for <i>autowhite_delay</i>. The default is one day. Use zero to disable auto-whitelisting. A suffix can be added to specify seconds (s), minutes (m), hours (h), days (d) or weeks (w). Without any suffix, values are treated as seconds. Equivalent to the <i>autowhite</i> option in the configuration file.</p>
<dt><code>-c</code></p>
<dd>Only check the configuration file and exit. Return value is 0 if the configuration is valid, or an error code from <i>&lt;sysexit.h&gt;</i> otherwise.</p>
<dt><code>-D</code></p>
<dd>Do not fork; run in the foreground instead. Without this flag, <code>milter-greylist</code> will become a daemon. Equivalent to the <i>nodetach</i> option in the configuration file.</p>
<dt><code>-d </code><i>dumpfile</i></p>
<dd>Location of the dump file. Default is <i>/var/lib/milter-greylist/db/greylist.db</i>. Equivalent to the <i>dumpfile</i> option in the configuration file.</p>
<dt><code>-f </code><i>configfile</i></p>
<dd>Location of the config file. Default is <i>/etc/mail/greylist.conf</i>.</p>
<dt><code>-h</code></p>
<dd>Show usage information.</p>
<dt><code>-L </code><i>cidrmask</i></p>
<dd>Use <i>cidrmask</i> as a matching mask when checking IPv4 addresses entries in the greylist. This is aimed as a workaround to mail farms that re-emit messages from different IP addresses. With <code>-L 24</code>, the matching mask is 255.255.255.0, and all addresses within the same class C network are considered the same. Default is <code>-L 32</code>, which corresponds to all addresses considered different.</p>
<dt><code>-M </code><i>prefixlen</i></p>
<dd>Use <i>prefixlen</i> as a matching mask when checking IPv6 addresses entries in the greylist. This is aimed as a workaround to mail farms that re-emit messages from different IP addresses. With <code>-M 64</code>, the matching mask is ffff:ffff:ffff:ffff::, and all addresses within the same subnet are considered the same. Default is <code>-M 128</code>, which corresponds to all IPv6 addresses considered different.</p>
<dt><code>-l</code></p>
<dd>Enable debug output in the access-list management code.</p>
<dt><code>-P </code><i>pidfile</i></p>
<dd>write the daemon&#8217;s PID to <i>pidfile</i>. Equivalent to the <i>pidfile</i> option in the configuration file.</p>
<dt><code>-p </code><i>socket</i></p>
<dd>Use <i>socket</i> as the socket used by <code><a href="/docs/linux/man/8-sendmail/">sendmail</a>(8)</code> to communicate with <code>milter-greylist</code>.</p>
<dt><code>-q</code></p>
<dd>Quiet mode. <code>milter-greylist</code> will not tell SMTP clients how much time they have to wait before the message will be accepted. Equivalent to the <i>quiet</i> option in the configuration file.</p>
<dt><code>-r</code></p>
<dd>Display <code>milter-greylist</code> version and build environment, then exit.</p>
<dt><code>-S</code></p>
<dd>If <code>milter-greylist</code> was built with SPF support, then SPF-compliant senders bypass greylisting. This flag causes messages to be greylisted regardless of whether they are SPF-compliant or not. Equivalent to the <i>nospf</i> option in the configuration file.</p>
<dt><code>-T</code></p>
<dd>Enable test mode. This alters the meaning of <i>rcpt</i> lines in <i>greylist.conf</i>, so that only messages sent to recipient addresses listed there are selected for greylisting. This option and the <i>rcpt</i> lines have been deprecated in favor of ACL, so do not use it.</p>
<dt><code>-u </code><i>username</i>[:<i>groupname</i>]</p>
<dd>Drop root privileges and switch to <i>username</i> (and optionally <i>groupname</i>) credentials. Make sure this user (and group) has write access to <i>greylist.db</i>. Equivalent to the <i>user</i> option in the configuration file.</p>
<dt><code>-v</code></p>
<dd>Enable debug output. <code>milter-greylist </code> will send messages (and debug output if it is given the <code>-v</code> flag) to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a>(8)</code> with facility LOG_MAIL. Equivalent to the <i>verbose</i> option in the configuration file.</p>
<dt><code>-w </code><i>greylist_delay</i></p>
<dd>sets the minimum delay between the first attempt and the time the message can be accepted. Default is 30 minutes. A suffix can be added to specify seconds (s), minutes (m), hours (h), days (d) or weeks (w). Without any suffix, values are treated as seconds. Equivalent to the <i>greylist</i> option in the configuration file.</dl>
<h2>Greylist Mx Sync</h2>
<p><code>milter-greylist</code> is now able to sync the greylist between multiple MX. In order to enable this feature, you need to list the peer MXs in <code><a href="/docs/linux/man/5-greylist-conf/">greylist.conf</a>(5)</code> like this: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>peer 192.0.2.17<br />
&nbsp;<wbr>&nbsp;<wbr>peer 192.0.2.18 </p>
<p> When peers are configured, <code>milter-greylist</code> will listen on the port defined for the mxglsync service in <i>/etc/services </i> (defaults to 5252), and it will connect to peers at this port. Each time an entry is added or deleted on one MX, it will be propagated to the others. </p>
<p> The protocol is quite simple, just telnet to your MX at port 5252, and type <i>help</i> to see how it works. Note that connections will only be accepted from peer MXs, even localhost will be rejected (and don&#8217;t ever add localhost as a peer for MX sync, as you will cause each entry in the greylist to be added twice). </p>
<p> If an MX is down, changes to the greylist will be queued until it gets back up again. The queue length is limited (default is 1024 entries), and if it overflows, newer entries will be discarded.</p>
<h2>Authors</h2>
<p>Emmanuel Dreyfus &lt;manu [at] netbsd.org&gt; </p>
<p> <code>milter-greylist</code> received many contributions from (in alphabetical order): Adrian Dabrowski, Aida Shinra, Adam Katz, Alexander Lobodzinski, Alexandre Cherif, Alexey Popov, Andrew McGill, Attila Bruncsak, Benoit Branciard, Bernhard Schneider, Bob Smith, Constantine A. Murenin, Chris Bennett, Christian Pelissier, Cyril Guibourg, Dan Hollis, David Binderman, Denis Solovyov, Elrond, Enrico Scholz, Eugene Crosser, Fabien Tassin, Fredrik Pettai, Gary Aitken, Georg Horn, Gert Doering, Greg Troxel, Guido Kerkewitz, Hajimu Umemoto, Hideki ONO, Ivan F. Martinez, Jacques Beigbeder, Jean Benoit, Jean-Jacques Puig, Jeff Rife, Jim Klimov, Jobst Schmalenbach, Joe Pruett, Joel Bertrand, Johann E. Klasek, Johann Klasek, John Thiltges, John Wood, Jorgen Lundman, Klas Heggemann, Kouhei Sutou, Laurence Moindrot, Lev Walkin, Manuel Badzong, Mart Pirita, Martin Paul, Matt Kettler, Mattheu Herrb, Matthias Scheler, Matthieu Herrb, Michael Fromme, Moritz Both, Nerijus Baliunas, Ole Hansen, Pavel Cahyna, Pascal Lalonde, Per Holm, Petar Bogdanovic, Petr Kristof, Piotr Wadas, R P Herrold, Ralf S. Engelschall, Ranko Zivojnovic, Remy Card, Rick Adams, Rogier Maas, Romain Kang, Rudy Eschauzier, Stephane Lentz, Steven Hiscocks, Thomas Scheunemann, Tim Mooney, Vincent Dufresne, Wolfgang Solfrank, and Yaroslav Boychuk. </p>
<p> Thanks to Helmut Messerer and Thomas Pfau for their feedback on the first releases of this software.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-greylist-conf/">greylist.conf</a>(5), <a href="/docs/linux/man/8-sendmail/">sendmail</a>(8), <a href="/docs/linux/man/8-syslogd/">syslogd</a>(8).</p>
<dl>
<dt>Evan Harris&#8217;s paper:</p>
<dd><i><a rel="nofollow" href="http://projects.puremagic.com/greylisting/">http://projects.puremagic.com/greylisting/</a></i></p>
<dt>milter-greylist&#8217;s web site:</p>
<dd><i><a rel="nofollow" href="http://hcpnet.free.fr/milter-greylist/">http://hcpnet.free.fr/milter-greylist/</a></i> </p>
