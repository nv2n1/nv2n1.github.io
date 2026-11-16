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
<dt><code>start</code></dt>
<dd>Initialize <code>tlp</code> and apply settings according to the actual power source. </dd>
<dt><code>bat</code></dt>
<dd>Apply settings for battery power source. </dd>
<dt><code>true</code></dt>
<dd>Same as <code>bat</code> (this command is called when power source changes to battery). </dd>
<dt><code>ac</code></dt>
<dd>Apply settings for ac power source. </dd>
<dt><code>false</code></dt>
<dd>Same as <code>ac</code> (this command is called when power source changes to ac). </dd>
<dt><code>usb</code></dt>
<dd>Enable autosuspend for all usb devices, except blacklisted ones. </dd>
<dt><code>bayoff </code></dt>
<dd>Turn off optical drive in UltraBay/MediaBay. The drive may be re-enabled by pulling the eject lever or pushing the media eject button on newer models. </dd>
<dt><code>setcharge [START_CHARGE STOP_CHARGE] [BAT0|BAT1] </code>(ThinkPads only)</dt>
<dd>Set charge thresholds of main (BAT0) or Ultrabay (BAT1) battery temporarily. Values must be between 1 and 100, Stop &gt; Start + 3. Configured thresholds are restored upon next system start. When called without arguments, configured thresholds are set. </dd>
<dt><code>fullcharge [BAT0|BAT1] </code>(ThinkPads only)</dt>
<dd>Set charge thresholds of main (BAT0) or Ultrabay (BAT1) battery to factory preset (96/100) temporarily (causing a full charge). Configured thresholds are restored upon next system start. </dd>
<dt><code>chargeonce [BAT0|BAT1] </code>(ThinkPads only)</dt>
<dd>Charge main (BAT0) or Ultrabay (BAT1) battery to upper charge threshold once (bypassing lower threshold). Configured thresholds are restored upon next system start. </dd>
<dt><code>discharge [BAT0|BAT1] </code>(ThinkPads only)</dt>
<dd>Force complete discharge of main (BAT0) or Ultrabay (BAT1) battery. </dd>
<dt><code>recalibrate [BAT0|BAT1] </code>(ThinkPads only)</dt>
<dd>Battery recalibration: completely discharge main (BAT0) or Ultrabay (BAT1) battery and recharge to 100%. </dd>
<dt><code>stat</code></dt>
<dd>Same as tlp-stat. </dd>
<dt><code>diskid</code></dt>
<dd>Show disk ids for configuration. </dd>
</dl>
<h2>Files</h2>
<p><i>/etc/default/tlp</i></p>
<dl>
<dd>System configuration file containing all power management settings. </dd>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tlp-stat/">tlp-stat</a></code>(8), <code><a href="/docs/linux/man/1-bluetooth/">bluetooth</a></code>(1), <code><a href="/docs/linux/man/1-wifi/">wifi</a></code>(1), <code><a href="/docs/linux/man/1-wwan/">wwan</a></code>(1). </p>
<h2>Author</h2>
<p>Thomas Koch &lt;linrunner at gmx.net&gt;</p>
