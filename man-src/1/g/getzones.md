---
title: "getzones(1)"
name: "getzones"
section: "1"
letter: "g"
url: "/docs/linux/man/1-getzones/"
description: "getzones – list AppleTalk zone names"
---

<h2 class="name">NAME</h2>
<p> getzones &#8211; list AppleTalk zone names </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>getzones</code> [-m | -l] [<i>address</i>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>Getzones</code></p>
<dd>is used to obtain a list of AppleTalk zone names using the Zone Information Protocol (ZIP). It sends a GetZoneList request to an AppleTalk router. By default, it sends the request to the locally running <code><a href="/docs/linux/man/8-atalkd/">atalkd</a></code>(8).</p>
<h2>OPTIONS</h2>
<p> <code>-m</code></p>
<dl>
<dt>
<dd> List the name of the local zone only; this is accomplished by sending a ZIP GetMyZone request.</dl>
<p> <code>-l</code></p>
<dl>
<dt>
<dd> List the local zones; this is accomplished by sending a GetLocalZones request.</dl>
<p> <i>address</i></p>
<dl>
<dt>
<dd> Contact the AppleTalk router at <i>address.</i> <i>address</i> is parsed by <code><a href="/docs/linux/man/3-atalk_aton/">atalk_aton</a></code>(3).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-atalk_aton/">atalk_aton</a></code>(3), <code><a href="/docs/linux/man/8-atalkd/">atalkd</a></code>(8). </p>
<h2>Index</h2>
