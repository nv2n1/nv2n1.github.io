---
title: "lircmd(8)"
name: "lircmd"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lircmd/"
description: "lircmd – LIRC mouse daemon translates infrared signals into mouse events"
---

<p>lircmd &#8211; LIRC mouse daemon translates infrared signals into mouse events</p>
<h2>Synopsis</h2>
<p><code>lircmd [</code><i>options</i>] [<i>config-file</i>]</p>
<h2>Description</h2>
<p>This daemon can simulate a MouseSystems, IntelliMouse or IMPS/2 type mouse. It gets the received buttons from lircd and converts them to mouse events. To make this possible, lircmd needs a config file located in /etc/lircmd.conf. In this file you have to determine which button from which remote causes a mouse move or a mouse button click. You can also specify a special button which activates or deactivates the mouse mode.</p>
<dl>
<dt><code>-h</code> <code>&#8211;help</code></p>
<dd>display this message</p>
<dt><code>-v</code> <code>&#8211;version</code></p>
<dd>display version</p>
<dt><code>-n</code> <code>&#8211;nodaemon</code></p>
<dd>don&#8217;t fork to background</p>
<dt> <code>-O</code> <code>&#8211;options-file</code>=<i>file</i> alternative default options file</p>
<dt><code>-u</code> <code>&#8211;uinput</code></p>
<dd>
<dd>generate Linux input events</dl>
<h2>Options</h2>
<p>If you provide the &#8211;nodaemon option lircmd won&#8217;t fork to background. </p>
<p> On Linux systems the &#8211;uinput option will enable automatic generation of Linux input events. lircmd will open /dev/input/uinput and inject the simulated mouse events into the Linux kernel rather than creating the /dev/lircm device.</p>
<h2>Files</h2>
<p>lircmd will use syslogd to output error messages. It depends on your system configuration where they will show up. </p>
<p> The options file is by default /etc/lirc/lirc_options.conf; lircmd handles the values under the [lircd] section in this file. The location can be changed using the -O/&#8211;options-file command-line option or using the environment variable LIRC_OPTIONS_PATH. The values here are used as defaults for any option not present on command line.</p>
<h2>Daemons</h2>
<p>lircmd is a daemon. You should start it in some init script depending on your system. Besides the preferred systemd setup which is installed by default there are also example scripts for other distros and init systems in the contrib directory. lircmd has to be started after lircd as it connects to the socket lircd provides. </p>
<p> If you start lircd or lircmd from your shell prompt you will usually get back immediately to the prompt. This is not an error, daemons always run in background.</p>
<h2>See Also</h2>
<p>The documentation for <code>lirc</code> is maintained as html pages. They are located under html/ in the documentation directory. </p>
