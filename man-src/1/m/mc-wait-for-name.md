---
title: "mc-wait-for-name(1)"
name: "mc-wait-for-name"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mc-wait-for-name/"
description: "mc-wait-for-name – run until a D-Bus name appears on the session bus"
---

<h2>NAME</h2>
<p> mc-wait-for-name &#8211; run until a D-Bus name appears on the session bus</p>
<h2>SYNOPSIS</h2>
<p> <code>mc-wait-for-name</code> <i>WELL-KNOWN-NAME</i> </p>
<pre>
<code>[D-BUS Service]</code>
<code>Name=</code><i>org.freedesktop.Telepathy.Client.Something</i>
<code>Exec=/usr/bin/mc-wait-for-name</code><i> org.freedesktop.Telepathy.Client.Something</i>
</pre>
<h2>DESCRIPTION</h2>
<p> <code>mc-wait-for-name</code> runs until a bus name appears, then exits successfully. This can be used as a service-activation helper for a bus name that is not directly activatable, but will be provided automatically (after a while) by the desktop session.</p>
<h2>EXIT STATUS</h2>
<dl>
<dt>0</p>
<dd> The bus name eventually appeared.</p>
<dt>64 (EX_USAGE)</p>
<dd> Invocation error (too many or too few arguments, or the bus name given was not a syntactically valid well-known bus name).</p>
<dt>69 (EX_UNAVAILABLE)</p>
<dd> mc-wait-for-name was unable to connect to the session bus.</p>
<dt>75 (EX_TEMPFAIL)</p>
<dd> The name did not appear within a reasonable time.</dl>
<h2>OPTIONS</h2>
<p> There are no additional command-line options.</p>
<h2>BUGS</h2>
<p> The &quot;reasonable time&quot; to wait is currently hard-coded. </p>
<h2>Index</h2>
