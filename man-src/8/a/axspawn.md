---
title: "axspawn(8)"
name: "axspawn"
section: "8"
letter: "a"
url: "/docs/linux/man/8-axspawn/"
description: "axspawn – Allow automatic login to a Linux system."
---

<p>axspawn &#8211; Allow automatic login to a Linux system.</p>
<h2>Synopsis</h2>
<p><code>axspawn [&#8211;pwprompt PR0MPT, -p PR0MPT] [&#8211;changeuser, -c] [&#8211;rootlogin, -r] [&#8211;only-md5] [&#8211;wait, -w]</code></p>
<h2>Description</h2>
<p><code>Axspawn</code> will check if the peer is an AX.25 connect, the callsign a valid Amateur Radio callsign, strip the SSID, check if UID/GID are valid, allow a password-less login if the password-entry in /etc/passwd is lq+rq or empty; in every other case login will prompt for a password. </p>
<p> <code>Axspawn</code> can create user accounts automatically. You may specify the user shell, first and maximum user id, group ID in the config file and (unlike WAMPES) create a file lq/etc/ax25/ax25.profilerq which will be copied to ~/.profile.</p>
<h2>Security</h2>
<p>Auto accounting is a security problem by definition. Unlike WAMPES, which creates an empty password field, Axspawn adds an lqimpossiblerq (&#8216;+&#8217;) password to /etc/passwd. Login gets called with the lq-frq option, thus new users have the chance to login without a password. (I guess this won&#8217;t work with the shadow password system). </p>
<p> Of course <code>axspawn</code> does callsign checking: Only letters and numbers are allowed, the callsign must be longer than 4 characters and shorter than 6 characters (without SSID). There must be at least one digit, and max. two digits within the call. The SSID must be within the range of 0 and 15. Please drop me a note if you know a valid Amateur Radio callsign that does not fit this pattern _and_ can be represented correctly in AX.25. </p>
<p> axspawn also has the well known authentication mechanisms of the AX.25 bbs <code>baycom (sys)</code> and <code>md5</code> standards. axspawn searches in /etc/ax25/bcpasswd (first) and ~user/.bcpasswd (second) for a match of the required authentication mechanism and password. md5 and baycom passwords may differ. md5 passwords gain over baycom passwords. </p>
<p> Note: you could &quot;lock&quot; special &quot;friends&quot; out by specifying an empty password in /etc/ax25/bcpasswd (line &quot;n0call:md5:&quot;). -&gt; md5 Passwords are enforced. But the length is shorter than the minimum (len 8 for md5, len 20 for baycom); user&#8217;s password file is not searched because in /etc/ax25/bcpasswd its already found.. </p>
<p> Syntax and caveeats for /etc/ax25/bcpasswd:<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Has to be a regular file&nbsp;<wbr>(no symlink). Not world-readable/writable.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Example lines:<br />
&nbsp;<wbr>#&nbsp;<wbr>Thomas<br />
&nbsp;<wbr>dl9sau:md5:abcdefgh<br />
&nbsp;<wbr>#&nbsp;<wbr>Test<br />
&nbsp;<wbr>te1st:sys:12345678901234567890<br />
&nbsp;<wbr>#&nbsp;<wbr>root<br />
&nbsp;<wbr>root:md5:ziz7AoxuAt6jeuthTheexet0uDa9iefuAeph3eelAetahmi0<br />
&nbsp;<wbr>#&nbsp;<wbr>misconfiguration:<br />
&nbsp;<wbr>thisbadlineisignored<br />
&nbsp;<wbr>#&nbsp;<wbr>With this line<br />
&nbsp;<wbr>systempasswordonly<br />
&nbsp;<wbr>#&nbsp;<wbr>.. axspan will not look in user&#8217;s homedir for his .bcpasswd </p>
<p> Syntax and caveeats for user&#8217;s .bcpasswd in his $HOME:<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Has to be a regular file&nbsp;<wbr>(no symlink). Neither group- nor world-<br />
read-/writable. Has to be owned by the user or uid 0&nbsp;<wbr>(root).<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Example lines:<br />
&nbsp;<wbr>#&nbsp;<wbr>could be shorter<br />
&nbsp;<wbr>md5:abcdefgh<br />
&nbsp;<wbr>#&nbsp;<wbr>should be longer<br />
&nbsp;<wbr>sys:12345678901234567890</p>
<h2>Options</h2>
<dl>
<dt><code>-p DB0FHN or &#8211;pwprompt DB0FHN</code></p>
<dd>While baycom or md5 password authentication (see above), the password prompt is set to the first argument (DB0FHN in this example). This may be needed for some packet-radio terminal programs for detecting the password prompt properly.</p>
<dt><code>-c, &#8211;changeuser</code></p>
<dd>Allow connecting ax25 users to change their username for login. They&#8217;ll be asked for their real login name.</p>
<dt><code>-e, &#8211;embedded</code></p>
<dd>Special treatment for axspawn on non-standard conform embedded devices. I.e. openwrt has no true /bin/login: if you use it as a real login program, it raises a security hole.</p>
<dt><code>-r, &#8211;rootlogin</code></p>
<dd>Permit login as user root. Cave: only md5 or baycom style is allowed; no plaintext password.</p>
<dt><code>&#8211;only-md5</code></p>
<dd>Insist in md5 authentication during login. If no password for the user is found, or it is not md5, then no other login mechanism is granted. This option, in combination with -c and -r, may be a useful configuration for systems where no ax25 user accounts are available, but you as sysop would like to have a login access for your administrative tasks.</p>
<dt><code>-w, &#8211;wait</code></p>
<dd>Eats the first line the user sends. This feature is useful if you have TCP VC connects to the same Call+SSID. It is now obsolete, because ax25d is the right place for this and implements this functionality better.</p>
<dt>Theses are options and not part of the preferences because you _may_ like to have on every interface definition in ax25d.conf (where axspawn is started from) a different behaviour.</p>
<dd></dl>
<h2>Files</h2>
<pre>/etc/passwd
<br>
/etc/ax25/ax25.profile
<br>
/etc/ax25/axspawn.conf</pre>
<p>/etc/ax25/bcpasswd ~/.bcpasswd</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-axspawn-conf/">axspawn.conf</a></code>(5), <code><a href="/docs/linux/man/8-ax25d/">ax25d</a></code>(8).</p>
<h2>Author</h2>
<p>Joerg Reuter DL1BKE &lt;jreuter [at] poboxes.com&gt;</p>
