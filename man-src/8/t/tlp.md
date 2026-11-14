---
title: "tlp(8)"
name: "tlp"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tlp/"
description: "tlp – apply laptop power management settings"
---

<p>tlp &#8211; apply laptop power management settings</p>
<h2>Synopsis</h2>
<p><code>tlp </code><i>command</i> [<i>param</i>] </p>
<h2>Description</h2>
<p>This command allows one to invoke TLP&#8217;s functions manually and provides extended battery functions for ThinkPads. </p>
<h2>Commands</h2>
<dl>
<dt><code>start</code></p>
<dd>Initialize <code>tlp</code> and apply settings according to the actual power source. </p>
<dt><code>bat</code></p>
<dd>Apply settings for battery power source. </p>
<dt><code>true</code></p>
<dd>Same as <code>bat</code> (this command is called when power source changes to battery). </p>
<dt><code>ac</code></p>
<dd>Apply settings for ac power source. </p>
<dt><code>false</code></p>
<dd>Same as <code>ac</code> (this command is called when power source changes to ac). </p>
<dt><code>usb</code></p>
<dd>Enable autosuspend for all usb devices, except blacklisted ones. </p>
<dt><code>bayoff </code></p>
<dd>Turn off optical drive in UltraBay/MediaBay. The drive may be re-enabled by pulling the eject lever or pushing the media eject button on newer models. </p>
<dt><code>setcharge [START_CHARGE STOP_CHARGE] [BAT0|BAT1] </code>(ThinkPads only)</p>
<dd>Set charge thresholds of main (BAT0) or Ultrabay (BAT1) battery temporarily. Values must be between 1 and 100, Stop &gt; Start + 3. Configured thresholds are restored upon next system start. When called without arguments, configured thresholds are set. </p>
<dt><code>fullcharge [BAT0|BAT1] </code>(ThinkPads only)</p>
<dd>Set charge thresholds of main (BAT0) or Ultrabay (BAT1) battery to factory preset (96/100) temporarily (causing a full charge). Configured thresholds are restored upon next system start. </p>
<dt><code>chargeonce [BAT0|BAT1] </code>(ThinkPads only)</p>
<dd>Charge main (BAT0) or Ultrabay (BAT1) battery to upper charge threshold once (bypassing lower threshold). Configured thresholds are restored upon next system start. </p>
<dt><code>discharge [BAT0|BAT1] </code>(ThinkPads only)</p>
<dd>Force complete discharge of main (BAT0) or Ultrabay (BAT1) battery. </p>
<dt><code>recalibrate [BAT0|BAT1] </code>(ThinkPads only)</p>
<dd>Battery recalibration: completely discharge main (BAT0) or Ultrabay (BAT1) battery and recharge to 100%. </p>
<dt><code>stat</code></p>
<dd>Same as tlp-stat. </p>
<dt><code>diskid</code></p>
<dd>Show disk ids for configuration. </p>
</dl>
<h2>Files</h2>
<p><i>/etc/default/tlp</i></p>
<dl>
<dd>System configuration file containing all power management settings. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tlp-stat/">tlp-stat</a></code>(8), <code><a href="/docs/linux/man/1-bluetooth/">bluetooth</a></code>(1), <code><a href="/docs/linux/man/1-wifi/">wifi</a></code>(1), <code><a href="/docs/linux/man/1-wwan/">wwan</a></code>(1). </p>
<h2>Author</h2>
<p>Thomas Koch &lt;linrunner at gmx.net&gt;</p>
