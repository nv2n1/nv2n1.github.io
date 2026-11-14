---
title: "notify-send(1)"
name: "notify-send"
section: "1"
letter: "n"
url: "/docs/linux/man/1-notify-send/"
description: "notify-send – a program to send desktop notifications"
---

<h2 class="name">NAME</h2>
<p> notify-send &#8211; a program to send desktop notifications </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>notify-send</code> [<i>OPTIONS</i>] {<i>summary</i>} [<i>body</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>With <code>notify-send</code> you can send desktop notifications to the user via a notification daemon from the command line. These notifications can be used to inform the user about an event or display some form of information without getting in the user&#8217;s way.</p>
<h2>OPTIONS</h2>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help and exit.</dl>
<p> <code>-u</code>, <code>&#8211;urgency</code>=<i>LEVEL</i></p>
<dl>
<dt>
<dd> Specifies the urgency level (low, normal, critical).</dl>
<p> <code>-t</code>, <code>&#8211;expire-time</code>=<i>TIME</i></p>
<dl>
<dt>
<dd> The duration, in milliseconds, for the notification to appear on screen. </p>
<p> (Ubuntu&#8217;s Notify OSD and GNOME Shell both ignore this parameter.)</dl>
<p> <code>-i</code>, <code>&#8211;icon</code>=<i>ICON</i>[,<i>ICON</i>&#8230;]</p>
<dl>
<dt>
<dd> Specifies an icon filename or stock icon to display.</dl>
<p> <code>-c</code>, <code>&#8211;category</code>=<i>TYPE</i>[,<i>TYPE</i>&#8230;]</p>
<dl>
<dt>
<dd> Specifies the notification category.</dl>
<p> <code>-h</code>, <code>&#8211;hint</code>=<i>TYPE</i>:<i>NAME</i>:<i>VALUE</i></p>
<dl>
<dt>
<dd> Specifies basic extra data to pass. Valid types are INT, DOUBLE, STRING and BYTE.</dl>
<h2>SEE ALSO</h2>
<p> The Desktop Notification Spec on m[blue]<code><a rel="nofollow" href="http://www.galago-project.org/specs/notification/">http://www.galago-project.org/specs/notification/</a></code>m[].</p>
<h2>AUTHORS</h2>
<p> <code>Andre Filipe de Assuncao e Brito</code> &lt;decko [at] noisemakers.org&gt;</p>
<dl>
<dt>
<dd> Original author</dl>
<p> <code>Paul van Tilburg</code> &lt;paulvt [at] debian.org&gt;</p>
<dl>
<dt>
<dd> Original author</dl>
<p> <code>Riccardo Setti</code> &lt;giskard [at] debian.org&gt;</p>
<dl>
<dt>
<dd> Original author</dl>
<h2>Index</h2>
