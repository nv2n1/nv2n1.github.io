---
title: "system-config-printer-applet(1)"
name: "system-config-printer-applet"
section: "1"
letter: "s"
url: "/docs/linux/man/1-system-config-printer-applet/"
description: "system-config-printer-applet – print job manager"
---

<h2 class="name">NAME</h2>
<p> system-config-printer-applet &#8211; print job manager </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>system-config-printer-applet</code> [&#8211;help] [&#8211;version] [&#8211;debug]</dl>
<h2>DESCRIPTION</h2>
<p> <code>system-config-printer-applet</code></p>
<dd>is a print job manager for CUPS. Normally it will display a printer icon in the notification area, greyed out when there are no print jobs for the current user. Clicking on the icon displays a simple print job manager for cancelling or reprinting jobs. </p>
<p> To save memory, the applet waits first of all until the user has printed a job before putting the icon in the notification area. To invoke the print job manager before a job has been printed, run the applet with the <code>&#8211;no-tray-icon</code> option: a desktop file is provided for this, so that it should appear in the system menu. </p>
<p> As well as displaying a printer icon in the notification area, the applet also provides a D-BUS server for the com.redhat.PrintDriverSelection interface, to help configure a new printer when it is plugged in.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display a short usage message.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display the version of the applet.</dl>
<p> <code>&#8211;debug</code></p>
<dl>
<dt>
<dd> Show debugging information.</dl>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>Index</h2>
