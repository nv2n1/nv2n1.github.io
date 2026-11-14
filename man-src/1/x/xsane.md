---
title: "xsane(1)"
name: "xsane"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xsane/"
description: "xsane – scanner frontend for SANE"
---

<h2 class="name">NAME</h2>
<p> xsane &#8211; scanner frontend for SANE </p>
<h2>SYNOPSIS</h2>
<p> <code>xsane</code> [<code>&#8211;version</code>|<code>-v</code>] [<code>&#8211;license</code>|<code>-l</code>] [<code>&#8211;device-settings</code> <i>file</i> |<code>-d</code> <i>file</i>] [<code>&#8211;viewer</code>|<code>-V</code>] [<code>&#8211;save</code>|<code>-s</code>] [<code>&#8211;copy</code>|<code>-c</code>] [<code>&#8211;fax</code>|<code>-f</code>] [<code>&#8211;mail</code>|<code>-m</code>] [<code>&#8211;no-mode-selection</code>|<code>-n</code>] [<code>&#8211;Fixed</code>|<code>-F</code>] [<code>&#8211;Resizable</code>|<code>-R</code>] [<code>&#8211;print-filenames</code>|<code>-p</code>] [<code>&#8211;force-filename</code> <i>name</i> |<code>-N</code> <i>name</i>] [<code>&#8211;display</code> <i>d</i>] [<code>&#8211;sync</code>] [<i>devicename</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>xsane</code> provides a graphical user-interface to control an image acquisition device such as a flatbed scanner. It allows previewing and scanning individual images and can be invoked either directly from the command-line or through The GIMP image manipulation program. In the former case, <code>xsane</code> acts as a stand-alone program that saves acquired images in a suitable PNM format (PBM for black-and-white images, PGM for grayscale images, and PPM for color images) or converts the image to JPEG, PNG, PS or TIFF. In the latter case, the images are directly passed to The GIMP for further processing. </p>
<p> <code>xsane</code> accesses image acquisition devices through the SANE (Scanner Access Now Easy) interface. The list of available devices depends on installed hardware and configuration. When invoked without an explicit devicename argument, <code>xsane</code> presents a dialog listing all known and available devices. To access an available device that is not known to the system, the devicename must be specified explicitly. The format of devicename is backendname:devicefile (eg: umax:/dev/sga).</p>
<h2>RUNNING UNDER THE GIMP</h2>
<p> To run <code>xsane</code> under the <code><a href="/docs/linux/man/1-gimp/">gimp</a></code>(1), you should at first make sure that xsane is compiled with gimp support by entering &quot;xsane -v&quot; on a shell. If xsane is compiled with gimp support then simply set a symbolic link from the xsane-binary to one of the <code><a href="/docs/linux/man/1-gimp/">gimp</a></code>(1) plug-ins directories. For example, for gimp-1.0.x the command </p>
<dl>
<dt>
<dd> ln -s /usr/bin/xsane ~/.gimp/plug-ins/</dl>
<p> for gimp 1.2.x the command: </p>
<dl>
<dt>
<dd> ln -s /usr/bin/xsane ~/.gimp-1.2/plug-ins/</dl>
<p> and for gimp 2.0.x the command: </p>
<dl>
<dt>
<dd> ln -s /usr/bin/xsane ~/.gimp-2.0/plug-ins/</dl>
<p> adds a symlink for the <code>xsane</code> binary to the user&#8217;s plug-ins directory. After creating this symlink, <code>xsane</code> will be queried by <code><a href="/docs/linux/man/1-gimp/">gimp</a></code>(1) the next time it&#8217;s invoked. From then on, <code>xsane</code> can be invoked through &quot;Xtns-&gt;XSane-&gt;Device dialog&#8230;&quot; (gimp-1.0.x) or through &quot;File-&gt;Acquire-&gt;XSane-&gt;Device dialog&#8230;&quot; (gimp-1.2.x and 2.0.x) menu entry. </p>
<p> You&#8217;ll also find that the &quot;Xtns-&gt;XSane&quot; or &quot;File-&gt;Acquire-&gt;XSane&quot; menu contains short-cuts to the SANE devices that were available at the time the <code>xsane</code> was queried. Note that <code><a href="/docs/linux/man/1-gimp/">gimp</a></code>(1) caches these short-cuts in ~/.gimp/pluginrc. Thus, when the list of available devices changes (e.g., a new scanner is installed or the device of the scanner has changed), then it is typically desirable to rebuild this cache. To do this, you can either <code><a href="/docs/linux/man/1-touch/">touch</a></code>(1) the <code>xsane</code> binary (e.g., &quot;touch /usr/bin/xsane&quot;) or delete the plugin cache (e.g., &quot;rm ~/.gimp/pluginrc&quot;). Either way, invoking <code><a href="/docs/linux/man/1-gimp/">gimp</a></code>(1) afterwards will cause the pluginrc to be rebuilt. </p>
<p> When <code>xsane</code> is started from the <code>gimp</code> then it is not possible to add a devicename explicitly. You have to make the devices known to the system by configuring <code>sane-dll, sane-net</code> and <code>saned.</code> </p>
<h2>OPTIONS</h2>
<p> If the <code>&#8211;version</code> or <code>-v</code> flag is given xsane prints a version information, some information about gtk+ and gimp version it is compiled against and lists the supported file formats, then it exits. </p>
<p> when the <code>&#8211;license</code> or <code>-l</code> flag is given xsane prints license information and exits. </p>
<p> The <code>&#8211;device-settings</code> or <code>-d</code> flag reads the next option as default filename for device settings. The extension &quot;.drc&quot; must not be included. </p>
<p> The <code>&#8211;viewer</code> or <code>-V</code> flag forces xsane to start in viewer mode. </p>
<p> The <code>&#8211;save</code> or <code>-s</code> flag forces xsane to start in save mode. </p>
<p> The <code>&#8211;copy</code> or <code>-c</code> flag forces xsane to start in copy mode. </p>
<p> The <code>&#8211;fax</code> or <code>-f</code> flag forces xsane to start in fax mode. </p>
<p> The <code>&#8211;mail</code> or <code>-m</code> flag forces xsane to start in mail mode. </p>
<p> The <code>&#8211;no-mode-selection</code> or <code>-n</code> flag disables the menu for xsane mode selection (viewer, save, copy, fax, mail). </p>
<p> If the <code>&#8211;Fixed</code> or <code>-F</code> flag is given then xsane uses a fixed, non resizable main window. The flag overwrites the preferences value. </p>
<p> If the <code>&#8211;Resizable</code> or <code>-R</code> flag is given then xsane uses a scrolled and resizable main window. The flag overwrites the preferences value. </p>
<p> If <code>&#8211;print-filenames</code> or <code>-p</code> flag is given then xsane prints the names of created files to the standard output. </p>
<p> When the flag <code>&#8211;force-filename</code> or <code>-N</code> is given then xsane reads the next option as default image filename. The name should be of the format &quot;name-001.ext&quot;. (or any other number instead of 001) that 001 part will be used as a filename counter if xsane is so configured. Beware that the number of digits must correspond to the configuration of xsane. The selection box for filenames is disabled. This option normally should be used with the option <code>&#8211;no-mode-selection</code> and <code>&#8211;save.</code> </p>
<p> The <code>&#8211;display</code> flag selects the X11 display used to present the graphical user-interface (see <code><a href="/docs/linux/man/1-x/">X</a></code>(1) for details). </p>
<p> The <code>&#8211;sync</code> flag requests a synchronous connection with the X11 server. This is for debugging purposes only.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><i>SANE_DEFAULT_DEVICE</i></p>
<dd> is used to preselect the device in the device dialog. This way you only have to accept the device (&lt;ENTER&gt; or OK-Button). </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><i>$HOME/.sane/xsane/xsane.rc</i></p>
<dd> This files holds the user preferences. Normally, this file should not be manipulated directly. Instead, the user should customize the program through the &quot;Preferences&quot; menu.</p>
<dt><i>$HOME/.sane/xsane/devicename.rc</i></p>
<dd> For each device, there is one rc-file that holds the saved settings for that particular device. Normally, this file should not be manipulated directly. Instead, the user should use the <code>xsane</code> interface to select appropriate values and then save the device settings using the &quot;Preferences-&gt;Save Device Settings&quot; menubar entry.</p>
<dt><i>/usr/share/sane/xsane/xsane-style.rc</i></p>
<dd> This system-wide file controls the aspects of the user-interface such as colors and fonts. It is a GTK style file and provides fine control over the visual aspects of the user-interface.</p>
<dt><i>$HOME/.sane/xsane/xsane-style.rc</i></p>
<dd> This file serves the same purpose as the system-wide style file. If present, it takes precedence over the system wide style file.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gimp/">gimp</a>(1), <a href="/docs/linux/man/1-xscanimage/">xscanimage</a>(1), <a href="/docs/linux/man/1-scanimage/">scanimage</a>(1), <a href="/docs/linux/man/5-sane-dll/">sane-dll</a>(5), <a href="/docs/linux/man/5-sane-net/">sane-net</a>(5), <a href="/docs/linux/man/1-saned/">saned</a>(1), <a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a>(5), <a href="/docs/linux/man/5-sane-usb/">sane-usb</a>(5), sane-&quot;backendname&quot;(5)</p>
<h2>AUTHOR</h2>
<p> Oliver Rauch &lt;Oliver.Rauch [at] rauch-domain.de&gt; </p>
<h2>Index</h2>
