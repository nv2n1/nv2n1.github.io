---
title: "lpinfo(8)"
name: "lpinfo"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lpinfo/"
description: "lpinfo – show available devices or drivers (deprecated)"
---

<p>lpinfo &#8211; show available devices or drivers (deprecated)</p>
<h2>Synopsis</h2>
<p><code>lpinfo</code> [ <code>-E</code> ] [ <code>-h </code><i>server</i>[<code>:</code><i>port</i>] ] [ <code>-l</code> ] [ <code>&#8211;device-id</code> <i>device-id-string</i> ] [ <code>&#8211;exclude-schemes</code> <i>scheme-list</i> ] [ <code>&#8211;include-schemes</code> <i>scheme-list</i> ] [ <code>&#8211;language</code> <i>locale</i> ] [ <code>&#8211;make-and-model</code> <i>name</i> ] [ <code>&#8211;product</code> <i>name</i> ] <code>-m</code><br />
 <code>lpinfo</code> [ <code>-E</code> ] [ <code>-h </code><i>server</i>[<code>:</code><i>port</i>] ] [ <code>-l</code> ] [ <code>&#8211;exclude-schemes</code> <i>scheme-list</i> ] [ <code>&#8211;include-schemes</code> <i>scheme-list</i> ] [ <code>&#8211;timeout</code> <i>seconds</i> ] <code>-v</code></p>
<h2>Description</h2>
<p><code>lpinfo</code> lists the available devices or drivers known to the CUPS server. The first form (<i>-m</i>) lists the available drivers, while the second form (<i>-v</i>) lists the available devices.</p>
<h2>Options</h2>
<p><code>lpinfo</code> accepts the following options:</p>
<dl>
<dt><code>-E</code></p>
<dd>Forces encryption when connecting to the server.</p>
<dt><code>-h </code><i>server</i>[<code>:</code><i>port</i>]</p>
<dd>Selects an alternate server.</p>
<dt><code>-l</code></p>
<dd>Shows a &quot;long&quot; listing of devices or drivers.</p>
<dt><code>&#8211;device-id </code><i>device-id-string</i></p>
<dd>Specifies the IEEE-1284 device ID to match when listing drivers with the <i>-m</i> option.</p>
<dt><code>&#8211;exclude-schemes </code><i>scheme-list</i></p>
<dd>Specifies a comma-delimited list of device or PPD schemes that should be excluded from the results. Static PPD files use the &quot;file&quot; scheme.</p>
<dt><code>&#8211;include-schemes </code><i>scheme-list</i></p>
<dd>Specifies a comma-delimited list of device or PPD schemes that should be included in the results. Static PPD files use the &quot;file&quot; scheme.</p>
<dt><code>&#8211;language </code><i>locale</i></p>
<dd>Specifies the language to match when listing drivers with the <i>-m</i> option.</p>
<dt><code>&#8211;make-and-model </code><i>name</i></p>
<dd>Specifies the make and model to match when listing drivers with the <i>-m</i> option.</p>
<dt><code>&#8211;product </code><i>name</i></p>
<dd>Specifies the product to match when listing drivers with the <i>-m</i> option.</p>
<dt><code>&#8211;timeout </code><i>seconds</i></p>
<dd>Specifies the timeout when listing devices with the <i>-v</i> option.</dl>
<h2>Conforming To</h2>
<p>The <i>lpinfo</i> command is unique to CUPS.</p>
<h2>Examples</h2>
<p>List all devices: </p>
<pre> lpinfo -v</pre>
<p>List all drivers: </p>
<pre> lpinfo -m</pre>
<p>List drivers matching &quot;HP LaserJet&quot;: </p>
<pre> lpinfo --make-and-model &quot;HP LaserJet&quot; -m</pre>
<h2>Notes</h2>
<p>CUPS printer drivers and backends are deprecated and will no longer be supported in a future feature release of CUPS. Printers that do not support IPP can be supported using applications such as <code><a href="/docs/linux/man/1-ippeveprinter/">ippeveprinter</a></code>(1).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lpadmin/">lpadmin</a></code>(8), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2021-2022 by OpenPrinting.</p>
