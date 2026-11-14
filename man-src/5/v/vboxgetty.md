---
title: "vboxgetty(5)"
name: "vboxgetty"
section: "5"
letter: "v"
url: "/docs/linux/man/5-vboxgetty/"
description: "vboxgetty.conf – config file for vboxgetty"
---

<p>vboxgetty.conf &#8211; config file for vboxgetty</p>
<h2>Description</h2>
<p>The file <code>/etc/isdn/vboxgetty.conf</code> is used to configure vboxgetty. Please read the man page <a href="/docs/linux/man/8-vboxgetty/">vboxgetty</a>(8) for a description of how vboxgetty works. Everything after &quot;#&quot; is ignored, as are empty lines. All arguments must be separated by whitespace (spaces, tabs). Arguments may not contain whitespace. All settings before the first <code>port </code> command are global settings, after a port command they only affect the current port.</p>
<dl>
<dt><code>port &lt;string&gt;</code></p>
<dd>ISDN device to configure.</p>
<dt><code>modeminit &lt;string&gt;</code></p>
<dd>Command to initialize the modem. You should set the MSN/EAZ on which vboxgetty should listen for incoming calls. Default is &quot;ATZ&quot;.</p>
<dt><code>user &lt;string&gt;</code></p>
<dd>Name of the user that vboxgetty will use. This user must exist in /etc/passwd and you must use this parameter.</p>
<dt><code>group &lt;string&gt;</code></p>
<dd>Name of the group that vboxgetty will use. This group must exist in /etc/group and you must use this parameter.</p>
<dt><code>umask &lt;number&gt;</code></p>
<dd>Vboxgetty will use this umask when creating new files. You must give the umask as an octal number. Default is 077.</p>
<dt><code>dropdtrtime &lt;seconds&gt;</code></p>
<dd>Number of milliseconds to hold the DTR-Line low to reset the modem. Default value is 800.</p>
<dt><code>initpause &lt;number&gt;</code></p>
<dd>Number of milliseconds to wait after initializing the modem. This is used to compensate the delay of the &quot;NO CARRIER&quot; response. Default value is 1500.</p>
<dt><code>badinitsexit &lt;number&gt;</code></p>
<dd>Maximum failures with modeminit. If this number is reached, vboxgetty exits. Default is 0.</p>
<dt><code>ringtimeout &lt;number&gt;</code></p>
<dd>Time in seconds to wait for a RING. If no RING is received within this time, no call is taken. Default is 5.</p>
<dt><code>echotimeout &lt;number&gt;</code></p>
<dd>Time in seconds to wait for the echo from the modem. Default is 4.</p>
<dt><code>commandtimeout &lt;number&gt;</code></p>
<dd>Time in seconds to wait for a response to a modem command. Default is 4.</p>
<dt><code>alivetimeout &lt;number&gt;</code></p>
<dd>After this time in seconds vboxgetty will check if the modem is still responding to modem commands. Default is 1800.</p>
<dt><code>compression &lt;string&gt;</code></p>
<dd>Audio compression to use to record new messages. Possible values are ADPCM-2, ADPCM-3, ADPCM-4 and ULAW. The ALAW compression mode is no longer supported. Default is ULAW.</p>
<dt><code>spooldir &lt;string&gt;</code></p>
<dd>Spool directory to use. This directory must exist. It&#8217;s used for control files of several programs. Default is /var/spool/vbox/&lt;user&gt;.</p>
<dt><code>vboxconfig &lt;string&gt;</code></p>
<dd>Full path of the vbox config file. Default value is &lt;spooldir&gt;/vbox.conf.</p>
<dt><code>freespace &lt;number&gt;</code></p>
<dd>Number of bytes that must be available on the partition with the spool directory, so that a call may be taken. Default is 0.</p>
<dt><code>debuglevel &lt;string&gt;</code></p>
<dd>What messages are be written to /var/log/vbox/vboxgetty-&lt;device&gt;.log. The string consists of letters representing the severities of the messages to log (F=FATAL, E=ERROR, W=WARNING, I=INFO, D=DEBUG, J=JUNK). Default is FEWI. </p>
<h2>Files</h2>
<dl>
<dt><code>/etc/isdn/vboxgetty.conf</code></p>
<dd>this configuration file </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-vboxgetty/">vboxgetty</a>(8), <a href="/docs/linux/man/5-vbox/">vbox</a>(5), <a href="/docs/linux/man/5-vboxtcl/">vboxtcl</a>(5)</code> </p>
<h2>Author</h2>
<p>This manual page was written by Andreas Jellinghaus &lt;aj [at] dungeon.inka.de&gt;, for Debian GNU/Linux and isdn4linux.</p>
