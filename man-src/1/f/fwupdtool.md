---
title: "fwupdtool(1)"
name: "fwupdtool"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fwupdtool/"
description: "fwupdtool – standalone firmware update utility"
---

<h2 class="name">NAME</h2>
<p> fwupdtool &#8211; standalone firmware update utility </p>
<h2>SYNOPSIS</h2>
<p> fwupdtool [CMD]</p>
<h2>DESCRIPTION</h2>
<p> This tool allows an administrator to use the fwupd plugins without being installed on the host system. </p>
<p> Additionally <code>dfu-tool</code> can be used to convert firmware from various different formats, or to modify the images contained inside the container firmware file. For example, you can convert DFU or Intel HEX firmware into the vendor-specific format.</p>
<h2>OPTIONS</h2>
<p> The fwupdtool command takes various options depending on the action. Run <code>fwupdtool &#8211;help</code> for the full list.</p>
<h2>EXIT STATUS</h2>
<p> Commands that successfully execute will return &quot;0&quot;, but commands that have no actions but successfully execute will return &quot;2&quot;.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-fwupdagent/">fwupdagent</a>(1), <a href="/docs/linux/man/1-fwupdmgr/">fwupdmgr</a>(1)</p>
<h2>BUGS</h2>
<p> No known bugs.</p>
<h2>AUTHOR</h2>
<p> Richard Hughes (richard [at] hughsie.com) </p>
<h2>Index</h2>
