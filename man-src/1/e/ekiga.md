---
title: "ekiga(1)"
name: "ekiga"
section: "1"
letter: "e"
url: "/docs/linux/man/1-ekiga/"
description: "Ekiga – SIP and H.323 Voice over IP and Videoconferencing for UN*X"
---

<h2>NAME</h2>
<p> Ekiga &#8211; SIP and H.323 Voice over IP and Videoconferencing for UN*X</p>
<h2>SYNOPSIS</h2>
<p> <code>ekiga [-d level] [-c URL]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>Ekiga</code> is a SIP and H.323 VoIP, IP Telephony and Video Conferencing application which complies to the SIP and H.323 protocols. It can connect to a variety of other SIP and H323 applications including specific hardware. Ekiga can work with or without a webcam, and is able to create pure audio communications or traditional audio+video communications. Ekiga was formerly known as GnomeMeeting. Ekiga has been designed for the GNOME desktop and therefore uses <code><a href="/docs/linux/man/1-gconfd-2/">gconfd-2</a></code>(1) for storing its userdata. It offers to configure almost every option from within the GUI. Command-line options include <code>-d</code> to turn on debugging during calls. <code>-c </code> to call another URL.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-d level</p>
<dd> turn on debugging (on the console), level should be between 1 and 4.</p>
<dt>-c URL</p>
<dd> Calls the given URL. Ekiga can be running or not when invoking that option. SIP, H.323 and CALLTO URLs are supported. </p>
</dl>
<h2>FILES</h2>
<p> <i>/etc/gconf/gconf.xml.defaults/apps/ekiga/</i></p>
<dl>
<dt>
<dd> The system wide configuration file. See <code><a href="/docs/linux/man/1-gconf-config/">gconf-config</a></code>(1) for further details on gconf. (The actual place can differ depending on your system&#8217;s configuration)</dl>
<p> <i>~/.gconf/apps/ekiga</i></p>
<dl>
<dt>
<dd> Per user configuration file. See <code><a href="/docs/linux/man/1-gconf-config/">gconf-config</a></code>(1) for further details.</dl>
<h2>ENVIRONMENT</h2>
<p> On startup Ekiga reads the system-wide gconf schemas (like every other GNOME2 app should do) from <i>/etc/gconf/gconf.xml.defaults/apps</i>. Every modification of the gconf keys using the GUI, gconftool or gconf-editor is reflected in real-time by Ekiga. </p>
<h2>DOCUMENTATION</h2>
<p> More documentation is available in the manual available through Ekiga&#8217;s Help menu. There is also a FAQ at: <a rel="nofollow" href="http://www.ekiga.org">http://www.ekiga.org</a> </p>
<h2>GETTING HELP</h2>
<p> Feel free to join #ekiga on irc.gnome.org (GIMPnet) or the ML at: </p>
<p> <a rel="nofollow" href="http://mail.gnome.org/mailman/listinfo/ekiga-list">http://mail.gnome.org/mailman/listinfo/ekiga-list</a> </p>
<p> <code>after</code> having read the FAQ at </p>
<p> <a rel="nofollow" href="http://www.ekiga.org/">http://www.ekiga.org/</a> . </p>
<h2>AUTHOR</h2>
<p> Damien Sandras &lt;dsandras at seconix dot com&gt; </p>
<h2>OTHER INFO</h2>
<p> The webpage for Ekiga is at <a rel="nofollow" href="http://www.ekiga.org.">http://www.ekiga.org.</a> You can find info about Ekiga there and download the latest version. Either as packages for all major distributions or as sourcecode. Patched version of the libs are available, if necessary.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2000-2008 Damien Sandras<br />
 This is free software licensed under the GPLv2; see the LICENSE file in the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gconf-config/">gconf-config</a></code>(1), <code><a href="/docs/linux/man/1-gconfd-1/">gconfd-1</a></code>(1), <code><a href="/docs/linux/man/1-gconfd-2/">gconfd-2</a></code>(1), <code><a href="/docs/linux/man/1-gconftool-1/">gconftool-1</a></code>(1), <code><a href="/docs/linux/man/1-gconftool-2/">gconftool-2</a></code>(1), <code><a href="/docs/linux/man/1-gconfigger/">gconfigger</a></code>(1) </p>
<h2>Index</h2>
