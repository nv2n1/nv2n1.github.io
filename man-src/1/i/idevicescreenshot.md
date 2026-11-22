---

title: "idevicescreenshot(1)"
name: "idevicescreenshot"
section: "1"
letter: "i"
url: "/docs/linux/man/1-idevicescreenshot/"
description: "idevicescreenshot – Gets a screenshot from the connected device."
---

<p> idevicescreenshot &#8211; Gets a screenshot from the connected device.</p>
<h2>SYNOPSIS</h2>
<p> <code>idevicescreenshot</code> [OPTIONS] </p>
<h2>DESCRIPTION</h2>
<p> Gets a screenshot from the connected device. </p>
<p> NOTE: A mounted developer disk image is required on the device, otherwise<br/>
&nbsp;<wbr>the screenshotr service is not available. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d, &#8211;debug</code></dt>
<dd> enable communication debugging.</dd>
<dt><code>-u, &#8211;udid UDID</code></dt>
<dd> target specific device by its 40-digit device UDID.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> prints usage information </dd>
</dl>
<h2>AUTHOR</h2>
<p> Nikias Bassen </p>
<p> Man page written to conform with Debian by Julien Lavergne. </p>
