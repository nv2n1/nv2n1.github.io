---
title: "xfce4-power-manager(1)"
name: "xfce4-power-manager"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xfce4-power-manager/"
description: "xfce4-power-manager – The Xfce 4 Power manager"
---

<h2 class="name">NAME</h2>
<p> xfce4-power-manager &#8211; The Xfce 4 Power manager</p>
<h2>SYNOPSIS</h2>
<p> <code>xfce4-power-manager</code> <i>[options]</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>xfce4-power-manager</code> manages the power sources on the computer and the devices that can be controlled to reduce their power consumption (such as LCD brightness level, monitor sleep). In addition, <code>xfce4-power-manager</code> provides a set of freedesktop-compliant DBus interfaces to inform other applications about current power level so that they can adjust their power consumption, and it provides the inhibit interface which allows applications to prevent automatic sleep actions via the power manager; as an example, the operating system&#8217;s package manager should make use of this interface while it is performing update operations. </p>
<p> You can run <code>xfce4-power-manager</code> from the command line without specifying any extra arguments. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;no-daemon</code></p>
<dd> Starts the power manager in non-daemon mode: useful for debugging.</p>
<dt><code>&#8211;debug</code></p>
<dd> Have the power manager print debug messages to the console; useful if you have to send in a bug report.</p>
<dt><code>&#8211;dump</code></p>
<dd> Have the power manager print the configuration information to the console.</p>
<dt><code>&#8211;restart</code></p>
<dd> Causes the running power manager to restart.</p>
<dt><code>&#8211;customize</code></p>
<dd> Shows the configuration dialog.</p>
<dt><code>&#8211;quit</code></p>
<dd> Causes any running instance of <code>xfce4-power-manager</code> to exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the version information. </p>
</dl>
<h2>BUGS</h2>
<p> Please report any bugs to <i><a rel="nofollow" href="http://bugzilla.xfce.org/">http://bugzilla.xfce.org/</a></i>. Development discussion should be conducted on the <i>xfce4-dev [at] xfce.org</i> mailing list. Usage related questions should be directed to the <i>xfce [at] xfce.org</i> mailing list. See: <i><a rel="nofollow" href="https://mail.xfce.org/mailman/listinfo/">https://mail.xfce.org/mailman/listinfo/</a></i> </p>
<h2>HOMEPAGE</h2>
<p> <i><a rel="nofollow" href="http://goodies.xfce.org/">http://goodies.xfce.org/</a></i> </p>
<h2>AUTHOR</h2>
<p> Ali Abdallah &lt;aliov [at] xfce.org&gt;, Eric Koegel &lt;eric [at] xfce.org&gt;, Simon Steinbeiss &lt;simon [at] xfce.org&gt;, Harald Judt &lt;h.judt [at] gmx.at&gt; </p>
<h2>MANPAGE AUTHORS</h2>
<p> Ali Abdallah &lt;aliov [at] xfce.org&gt;, Robby Workman &lt;rworkman [at] slackware.com&gt;, Eric Koegel &lt;eric [at] xfce.org&gt;. </p>
<h2>Index</h2>
