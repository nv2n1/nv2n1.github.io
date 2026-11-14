---
title: "xferlog(5)"
name: "xferlog"
section: "5"
letter: "x"
url: "/docs/linux/man/5-xferlog/"
description: "xferlog – ProFTPD server logfile"
---

<p>xferlog &#8211; ProFTPD server logfile</p>
<h2>Description</h2>
<p>The <code>xferlog</code> file contains logging information from the FTP server daemon, <code><a href="/docs/linux/man/8-proftpd/">proftpd</a></code>(8). This file usually is found in <code>/var/log</code> but can be located anywhere by using a <code><a href="/docs/linux/man/8-proftpd/">proftpd</a></code>(8) configuration directive. Each server entry is composed of a single line of the following form, with all fields being separated by spaces.</p>
<dl>
<dd><i>current-time&nbsp;<wbr>&nbsp;<wbr> transfer-time&nbsp;<wbr>&nbsp;<wbr> remote-host&nbsp;<wbr>&nbsp;<wbr> file-size&nbsp;<wbr>&nbsp;<wbr> filename&nbsp;<wbr>&nbsp;<wbr> transfer-type&nbsp;<wbr>&nbsp;<wbr> special-action-flag&nbsp;<wbr>&nbsp;<wbr> direction&nbsp;<wbr>&nbsp;<wbr> access-mode&nbsp;<wbr>&nbsp;<wbr> username&nbsp;<wbr>&nbsp;<wbr> service-name&nbsp;<wbr>&nbsp;<wbr> authentication-method&nbsp;<wbr>&nbsp;<wbr> authenticated-user-id&nbsp;<wbr>&nbsp;<wbr>completion-status</i></dl>
<dl>
<dt><i>current-time</i></p>
<dd>is the current local time in the form &quot;DDD MMM dd hh:mm:ss YYYY&quot;. Where DDD is the day of the week, MMM is the month, dd is the day of the month, hh is the hour, mm is the minutes, ss is the seconds, and YYYY is the year.</p>
<dt><i>transfer-time</i></p>
<dd>is the total time in seconds for the transfer.</p>
<dt><i>remote-host</i></p>
<dd>is the remote host name.</p>
<dt><i>file-size</i></p>
<dd>is the size of the transferred file in bytes.</p>
<dt><i>filename</i></p>
<dd>is the name of the transferred file. If the filename contains any spaces or control characters, each such character is replaced by an underscore (&#8216;_&#8217;) character.</p>
<dt><i>transfer-type</i></p>
<dd>is a single character indicating the type of transfer. Can be one of:</p>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt><code>a</code></p>
<dd>for an ascii transfer</p>
<dt><code>b</code></p>
<dd>for a binary transfer</dl>
</dl>
</dl>
<dt><i>special-action-flag</i></p>
<dd>is one or more single character flags indicating any special action taken. Can be one or more of:</p>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt><code>C</code></p>
<dd>file was compressed</p>
<dt><code>U</code></p>
<dd>file was uncompressed</p>
<dt><code>T</code></p>
<dd>file was tar&#8217;ed</p>
<dt><code>_</code></p>
<dd>no action was taken</dl>
</dl>
</dl>
<dt><i>direction</i></p>
<dd>is the direction of the transfer. Can be one of:</p>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt><code>o</code></p>
<dd>outgoing</p>
<dt><code>i</code></p>
<dd>incoming</p>
<dt><code>d</code></p>
<dd>deleted</dl>
</dl>
</dl>
<dt><i>access-mode</i></p>
<dd>is the method by which the user is logged in. Can be one of:</p>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt><code>a</code></p>
<dd>(anonymous) is for an anonymous guest user.</p>
<dt><code>r</code></p>
<dd>(real) is for a local authenticated user.</dl>
</dl>
</dl>
<dt><i>username</i></p>
<dd>is the local username, or if guest, the ID string given.</p>
<dt><i>service-name</i></p>
<dd>is the name of the service being invoked, usually FTP.</p>
<dt><i>authentication-method</i></p>
<dd>is the method of authentication used. Can be one of:</p>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt><code>0</code></p>
<dd>none</p>
<dt><code>1</code></p>
<dd>RFC931 Authentication</dl>
</dl>
</dl>
<dt><i>authenticated-user-id</i></p>
<dd>is the user id returned by the authentication method. A * is used if an authenticated user id is not available.</p>
<dt><i>completion-status</i></p>
<dd>is a single character indicating the status of the transfer. Can be one of:</p>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt><code>c</code></p>
<dd>complete transfer</p>
<dt><code>i</code></p>
<dd>incomplete transfer</dl>
</dl>
</dl>
</dl>
<h2>Files</h2>
<dl>
<dt><code>/var/log/xferlog</code></p>
<dd></dl>
<h2>Authors</h2>
<p>ProFTPD is written and maintained by a number of people, full credits can be found on <code><a rel="nofollow" href="http://www.proftpd.org/credits.html">http://www.proftpd.org/credits.html</a></code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-proftpd/">proftpd</a>(8)</code> Full documentation on ProFTPD, including configuration and FAQs, is available at <code><a rel="nofollow" href="http://www.proftpd.org/">http://www.proftpd.org/</a></code> For help/support, try the ProFTPD mailing lists, detailed on <code><a rel="nofollow" href="http://www.proftpd.org/lists.html">http://www.proftpd.org/lists.html</a></code> Report bugs at <code><a rel="nofollow" href="http://bugs.proftpd.org/">http://bugs.proftpd.org/</a></code> </p>
