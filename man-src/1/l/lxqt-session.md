---
title: "lxqt-session(1)"
name: "lxqt-session"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lxqt-session/"
description: "lxqt-session – Session manager of LXQt: The Lightweight Qt Desktop Environment"
---

<h2>NAME</h2>
<p> <code>lxqt-session</code> &#8211; Session manager of <code>LXQt</code>: The Lightweight Qt Desktop Environment</p>
<h2>SYNOPSIS</h2>
<p> <code>lxqt-session</code> </p>
<h2>DESCRIPTION</h2>
<p> This module handles session autostart application over <code>LXQt</code> desktop environment startup. </p>
<p> The <code>LXQt modules</code> are desktop independent tools, and operate as daemons for the local user on desktop specific operations. </p>
<p> <code>LXQt</code> is an advanced, easy-to-use, and fast desktop environment based on the Qt framework. It has been tailored for users who value simplicity, speed, and an intuitive interface, with minimal resource requirements. It comprises several optional desktop components: </p>
<p>&nbsp;<wbr>*&nbsp;<wbr>Session module&nbsp;<wbr>(<i>this</i>, normally invoked with&nbsp;<wbr><code>startlxqt</code>)<br />
&nbsp;<wbr>*&nbsp;<wbr>Settings configuration center<br />
&nbsp;<wbr>*&nbsp;<wbr>Application launcher<br />
&nbsp;<wbr>*&nbsp;<wbr>Desktop<br />
&nbsp;<wbr>*&nbsp;<wbr>Panel with optional plugins<br />
&nbsp;<wbr>*&nbsp;<wbr>Polkit authorization agent<br />
&nbsp;<wbr>*&nbsp;<wbr>SSH password access<br />
&nbsp;<wbr>*&nbsp;<wbr>Display manager module<br />
&nbsp;<wbr>*&nbsp;<wbr>Power management module<br />
&nbsp;<wbr>*&nbsp;<wbr>Sudo/su module&nbsp;<wbr>(privilege elevation) </p>
<p> These components perform similar actions to those available in other desktop environments, and their name is self-descriptive. They are usually launched automatically, when choosing a <code>LXQt</code> session in the Display Manager.</p>
<h2>BEHAVIOR</h2>
<p> This application manages the <code>LXQt</code> session desktop behavior, module loading, and related startup programs prior loading the user workspace. By default this module loads the panel, desktop, and power management modules, thus it is important for a working <code>LXQt</code> session.</p>
<h2>AUTOSTART</h2>
<p> The modules are only shown by default in the <code>LXQt</code> desktop environment, but an autostart action can be created for other preferred desktop environments.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="https://github.com/LXDE/LXQt/issues">https://github.com/LXDE/LXQt/issues</a></p>
<h2>SEE ALSO</h2>
<p> <code>startlxqt.1</code> LXQt session initialization and launch script (e.g. in <code>.xinitrc</code>) </p>
<p> <code>lxqt-config-session.1</code> LXQt default and autostart applications settings, plus environment settings </p>
<p> <code>lxqt-config.1</code> LXQt settings Configuration Center interface </p>
<p> <code>lxqt-leave.1</code> LXQt session logout, reboot, shutdown, suspend, hibernate and lock screen </p>
<p> <code>lxqt-openssh-askpass.1</code> LXQt password access over ssh cryptography toolkit </p>
<p> <code>lxqt-panel.1</code> LXQt desktop panel with optional plugins </p>
<p> <code>lxqt-policykit-agent.1</code> LXQt polkit authorization agent </p>
<p> <code>lxqt-runner.1</code> LXQt application launcher by keyboard shortcut </p>
<p> <code>lxqt-sudo.1</code> LXQt sudo/su GUI for application privilege elevation </p>
<h2>Index</h2>
