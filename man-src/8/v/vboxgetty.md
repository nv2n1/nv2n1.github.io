---
title: "vboxgetty(8)"
name: "vboxgetty"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vboxgetty/"
description: "vboxgetty – isdn voice box (getty)"
---

<p>vboxgetty &#8211; isdn voice box (getty)</p>
<h2>Synopsis</h2>
<p><code>vboxgetty</code> <i>[OPTION] [OPTION] [&#8230;]</i> </p>
<h2>Description</h2>
<p>Vboxgetty is the heart of vbox: it watches the isdn system and waits for incoming voice calls, </p>
<h2>Options</h2>
<dl>
<dt><code>-f, &#8211;file FILE</code></p>
<dd>Config file to use. Default is the file &#8216;/etc/isdn/vboxgetty.conf&#8217;. </p>
<dt><code>-d, &#8211;device TTY</code></p>
<dd>ISDNdevice to use. You must use this option! </p>
<dt><code>-h, &#8211;help</code></p>
<dd>Show summary of options. </p>
<dt><code>-v, &#8211;version</code></p>
<dd>Show version of program. </p>
</dl>
<h2>Configuring Vbox</h2>
<p>vboxgetty should be started from the init process. To do this you need one line per vboxgetty in /etc/inittab like this one: </p>
<p> I5:2345:respawn:/usr/sbin/vboxgetty -d /dev/ttyI5 </p>
<p> The next step is to set up a working configuration for all ports in /etc/isdn/vboxgetty.conf: read <a href="/docs/linux/man/5-vboxgetty-conf/">vboxgetty.conf</a>(5) how to do this and look at the example config file in /usr/doc/isdnutils/examples. </p>
<p> You should then create the spool directories for each user: /var/spool/vbox/&lt;user&gt;, /var/spool/vbox/&lt;user&gt;/incoming and /var/spool/vbox/&lt;user&gt;/messages. Copy the example config files vbox.conf and standard.tcl from /usr/doc/isdnutils/examples to /var/spool/vbox/&lt;user&gt;, read the man pages <a href="/docs/linux/man/5-vbox-conf/">vbox.conf</a>(5) and <a href="/docs/linux/man/5-vboxtcl/">vboxtcl</a>(5) and edit these config files. </p>
<p> Change the owner of all files in /var/spool/vbox/&lt;user&gt; with &quot;chown &lt;user&gt;.&lt;group&gt; /var/spool/vbox/&lt;user&gt; -Rv&quot; and correct the permissions with &quot;chmod o-rwx,g-rwx /var/spool/vbox/&lt;user&gt; -Rv&quot;. </p>
<p> The last step: run &quot;init q&quot; to force init to reread /etc/inittab</p>
<h2>How It Works</h2>
<p>For each line in /etc/inittab one vboxgetty is started by init. Make sure the first field (ID) and the device file are different. Each vboxgetty does this: </p>
<p> First /etc/isdn/vbox.conf is read, the global settings are loaded and then the port specific settings. Then vboxgetty waits for an incoming call. </p>
<p> On an incoming call vboxgetty reads /var/spool/vbox/&lt;user&gt;/vbox.conf (unless you change that name), and vboxgetty determines if it should take that call or how many RINGs it should wait. It also gets the name of the standard message, beep message, timeout message, if these should be played and an alias for the current caller, if there is one. </p>
<p> If vbox has waited enough RINGs and the caller is still ringing, it takes the call and starts the tcl script /var/spool/vbox/&lt;user&gt;/standard.tcl (unless you change that name), and this script will do the rest (normally: play standard and beep message, record and then play timeout message).</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/isdn/vboxgetty.conf</code></p>
<dd>default config file </p>
<dt><code>/etc/inittab</code></p>
<dd>init starts vboxgetty via this file. </p>
<dt><code>/etc/isdn/vboxgetty.conf</code></p>
<dd>the global vbox config file </p>
<dt><code>/var/spool/vbox/&lt;user&gt;/vbox.conf</code></p>
<dd>the per user configuration file for this port </p>
<dt><code>/var/spool/vbox/&lt;user&gt;/standard.tcl</code></p>
<dd>the tcl script used to communicate with the caller </p>
<dt><code>/var/run/vboxgetty-&lt;device&gt;.pid</code></p>
<dd>process id of the vboxgetty </p>
<dt><code>/var/log/vbox/vboxgetty-&lt;device&gt;.log</code></p>
<dd>logfile of the vboxgetty </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-vboxgetty-conf/">vboxgetty.conf</a>(5), <a href="/docs/linux/man/5-vbox-conf/">vbox.conf</a>(5), <a href="/docs/linux/man/5-vboxtcl/">vboxtcl</a>(5), <a href="/docs/linux/man/5-isdntime/">isdntime</a>(5)</code> </p>
<h2>Author</h2>
<p>This manual page was written by Andreas Jellinghaus &lt;aj [at] dungeon.inka.de&gt;, for Debian GNU/Linux and isdn4linux.</p>
