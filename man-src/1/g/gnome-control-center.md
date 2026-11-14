---
title: "gnome-control-center(1)"
name: "gnome-control-center"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnome-control-center/"
description: "gnome-control-center – Configure GNOME settings"
---

<h2 class="name">NAME</h2>
<p> gnome-control-center &#8211; Configure GNOME settings </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gnome-control-center </code><code>[OPTION&#8230;]</code><code>[PANEL]</code><code>[ARG&#8230;]</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>gnome-control-center</code></p>
<dd>is a graphical user interface to configure various aspects of GNOME. </p>
<p> When run without arguments, the shell displays the overview, which shows all available configuration panels. The overview allows to open individual panels by clicking on them. It also has a search entry to find panels by searching keywords. </p>
<p> It is also possible to specify a panel name as commandline argument to go directly to that panel. Individual panels may accept further arguments to specify which tab to open (for multi-tabbed panels) or which item to display (for panels with lists). </p>
<p> Note that <code>gnome-control-center</code> is not meant to expose each and every setting that is available. The settings that can be found here represent what is considered useful and commonly needed options. For more exotic or uncommon options, you can look at <code>gnome-tweak-tool</code> or the <code>gsettings</code> commandline utility.</p>
<h2>PANELS</h2>
<p> The following panel names can be specified: </p>
<p> <code>background</code></p>
<dl>
<dt>
<dd> The background panel lets you set your desktop background.</dl>
<p> <code>bluetooth</code></p>
<dl>
<dt>
<dd> The bluetooth panel lets you configure your computer&#8217;s Bluetooth adapter, and pair the computer with Bluetooth keyboards, phones, etc.</dl>
<p> <code>color</code></p>
<dl>
<dt>
<dd> The color panel can calibrate monitors, web cams and printers for accurate color reproduction.</dl>
<p> <code>datetime</code></p>
<dl>
<dt>
<dd> The datetime panel lets you set the timezone and time format. </p>
<p> Some operations in this panel affect all user accounts on the computer and require privieges.</dl>
<p> <code>display</code></p>
<dl>
<dt>
<dd> The display panel configures the resolution and arrangement of monitors and laptop panels. Note that monitors can be rearranged by drag-and-drop, and you can change which monitor is your main display by dragging the black bar.</dl>
<p> <code>info-overview</code></p>
<dl>
<dt>
<dd> The info-overview panel shows a general overview of the system configuration. It also lets you change the default applications for various tasks and the handling of removable media.</dl>
<p> <code>keyboard</code></p>
<dl>
<dt>
<dd> The keyboard panel can change how the keyboard reacts to key presses and lets you change keyboard shortcuts or create custom shortcuts. </p>
<p> You can open this panel on a specific tab by passing <code>typing</code> or <code>shortcuts</code> as extra argument.</dl>
<p> <code>mouse</code></p>
<dl>
<dt>
<dd> The mouse panel can change how mice and touchpads react to user input.</dl>
<p> <code>network</code></p>
<dl>
<dt>
<dd> The network panel provides a view of available network devices (wired, wireless or mobile) and their current configuration. It also provides a way to create new VPN connections and configure proxy settings. </p>
<p> You can open this panel on a specific dialog by passing <code>create-wifi</code>, <code>connect-hidden-wifi</code>, <code>connect-3g</code>, <code>connect-8021x-wifi</code> or <code>show-device</code> as extra argument. The last three parameters require an additional extra argument for the network object in the form <i>/org/freedesktop/NetworkManager/Devices/0</i>.</dl>
<p> <code>notifications</code></p>
<dl>
<dt>
<dd> The notifications panel provides a way to control the display of notifications.</dl>
<p> <code>online-accounts</code></p>
<dl>
<dt>
<dd> The online-accounts panel shows your configured online accounts and lets you add or remove accounts.</dl>
<p> <code>power</code></p>
<dl>
<dt>
<dd> The power panel shows the fill level of batteries and can configure what happens when the computer is idle or runs out of battery.</dl>
<p> <code>printers</code></p>
<dl>
<dt>
<dd> The printers panel shows all known printers and their status. It is possible to inspect queued print jobs and add new printers. </p>
<p> Some operations in this panel require privileges.</dl>
<p> <code>privacy</code></p>
<dl>
<dt>
<dd> The privacy panel allows to control visible file usage history, temporary files, and name.</dl>
<p> <code>region</code></p>
<dl>
<dt>
<dd> The region panel contains regional settings such as the display language, formatting for times, dates, numbers, and input sources.</dl>
<p> <code>search</code></p>
<dl>
<dt>
<dd> The search panel controls the results visible in the overview, and the files and folders to be indexed.</dl>
<p> <code>screen</code></p>
<dl>
<dt>
<dd> The screen panel contains settings that control the screen brightness and screen lock behavior.</dl>
<p> <code>sharing</code></p>
<dl>
<dt>
<dd> The sharing panel contains settings that control what is shared over the network.</dl>
<p> <code>sound</code></p>
<dl>
<dt>
<dd> The sound panel shows all known sound devices and their configuration, including volume and balance settings. </p>
<p> You can open this panel on a specific tab by passing <code>output</code>, <code>input</code>, <code>hardware</code>, <code>effects</code> or <code>applications</code> as extra argument.</dl>
<p> <code>universal-access</code></p>
<dl>
<dt>
<dd> The universal-access panel contains settings for accessible technologies such as the screen reader, magnifier, screen keyboard and AccessX options.</dl>
<p> <code>user-accounts</code></p>
<dl>
<dt>
<dd> The user-accounts panel shows all user accounts that exist on the computer and allows to change them in some ways, such as changing the user name, password or permissions. It also allows to create or remove accounts. </p>
<p> Some operations in this panel require privileges.</dl>
<p> <code>wacom</code></p>
<dl>
<dt>
<dd> the wacom panel shows connected Wacom graphics tablets and lets you calibrate and configure such devices.</dl>
<h2>OPTIONS</h2>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Prints a short help text and exits.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Prints the program version and exits.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Enables verbose mode.</dl>
<p> <code>-l</code>, <code>&#8211;list</code></p>
<dl>
<dt>
<dd> Lists the available panels and exits.</dl>
<p> <code>-o</code>, <code>&#8211;overview</code></p>
<dl>
<dt>
<dd> Opens the overview.</dl>
<p> <code>-s</code> <i>term</i>, <code>&#8211;search</code> <i>term</i></p>
<dl>
<dt>
<dd> Sets the following search term.</dl>
<h2>EXIT STATUS</h2>
<p> On success 0 is returned, a non-zero failure code otherwise.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gsettings/">gsettings</a></code>(1) </p>
<h2>Index</h2>
