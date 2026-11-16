---
title: "mbim-network(1)"
name: "mbim-network"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mbim-network/"
description: "mbim-network – Simple network management of MBIM devices"
---

<h2>NAME</h2>
<p> mbim-network &#8211; Simple network management of MBIM devices</p>
<h2>SYNOPSIS</h2>
<p> <code>mbim-network</code> [<i>,OPTIONS/</i>] [<i>,DEVICE/</i>] [<i>,COMMAND/</i>]</p>
<h2>DESCRIPTION</h2>
<p> Simple network management of MBIM devices</p>
<h3>Commands:</h3>
<dl>
<dt>start</dt>
<dd> Start network connection</dd>
<dt>stop</dt>
<dd> Stop network connection</dd>
<dt>status</dt>
<dd> Query network connection status</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;profile</code>=<i>,[PATH]/</i></dt>
<dd> Use the profile in the specified path</dd>
<dt><code>&#8211;help</code></dt>
<dd> Show help options</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show version</dd></dl>
<p> Notes:</p>
<dl>
<dt>
</dt><dd> 1) [DEVICE] is given as the full path to the cdc-wdm character device, e.g.:</dd>
<dt>
</dt><dd> <i>,/dev/cdc-wdm0/</i></dd>
<dt>
</dt><dd> 2) The mbim-network script requires a profile to work. Unless explicitly specified with `&#8211;profile&#8217;, the file is assumed to be available in the following path:</dd>
<dt>
</dt><dd> <i>,/etc/mbim-network.conf/</i></dd>
<dt>
</dt><dd> 3) The APN to use should be configured in the profile, in the following way (e.g. assuming APN is called &#8216;internet&#8217;):</dd>
<dt>
</dt><dd> APN=internet</dd>
<dt>
</dt><dd> 4) Optional APN user/password strings may be given in the following way:</dd>
<dt>
</dt><dd> APN_USER=user APN_PASS=password</dd>
<dt>
</dt><dd> 5) If APN user/password is specified, the authentication protocol to use (one of PAP, CHAP or MSCHAPV2) must also be specified in the following way:</dd>
<dt>
</dt><dd> APN_AUTH=protocol</dd>
<dt>
</dt><dd> 6) If you want to instruct the mbim-network script to use the mbim-proxy setup, you can do so by configuring the following line in the profile:</dd>
<dt>
</dt><dd> PROXY=yes</dd>
<dt>
</dt><dd> 7) Once the mbim-network script reports a successful connection you still need to run a DHCP client on the associated WWAN network interface.</dd></dl>
<h2>COPYRIGHT</h2>
<p> Copyright (2013-2015) Aleksander Morgado License GPLv2+: GNU GPL version 2 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl-2.0.html">http://gnu.org/licenses/gpl-2.0.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>mbim-network</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>mbim-network</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info mbim-network</code></dd></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
