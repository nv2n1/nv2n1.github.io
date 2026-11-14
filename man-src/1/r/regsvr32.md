---
title: "regsvr32(1)"
name: "regsvr32"
section: "1"
letter: "r"
url: "/docs/linux/man/1-regsvr32/"
description: "regsvr32 – Wine DLL Registration Server"
---

<h2 class="name">NAME</h2>
<p> regsvr32 &#8211; Wine DLL Registration Server </p>
<h2>SYNOPSIS</h2>
<p> <code>regsvr32</code> [<code>/u</code>] [<code>/s</code>] [<code>/n</code>] [<code>/i</code>[<code>:</code><i>cmdline</i>]] <i>dllname</i></p>
<h2>DESCRIPTION</h2>
<p> <code>regsvr32</code> is the Wine dll registration server, designed to be compatible with its Microsoft Windows counterpart. By default, it will register the given dll.</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>/u</p>
<dd> Unregister the specified dll.</p>
<dt>/s</p>
<dd> Run regsvr32 silently (will not show any GUI dialogs).</p>
<dt>/i</p>
<dd> Call DllInstall passing it an optional </code><i>cmdline</i>. When used with <code>/u</code> calls DllUninstall.</p>
<dt><code>/n</p>
<dd> Do not call DllRegisterServer; this option must be used with /i</code>.</dl>
<h2>BUGS</h2>
<p> Bugs can be reported on the <code>Wine bug tracker</code></p>
<h2>AVAILABILITY</h2>
<p> <code>regsvr32</code> is part of the Wine distribution, which is available through WineHQ, the <code>Wine development headquarters</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wine/">wine</a></code>(1),<br />
 <code>Wine documentation and support</code> </p>
<h2>Index</h2>
