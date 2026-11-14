---
title: "amlabel(8)"
name: "amlabel"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amlabel/"
description: "amlabel – label an Amanda tape"
---

<p>amlabel &#8211; label an Amanda tape</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amlabel</code> [<code>&#8211;barcode&nbsp;<wbr></code><i>barcode</i>] [<code>&#8211;meta&nbsp;<wbr></code><i>meta-label</i>] [<code>&#8211;assign</code>] [<code>-f</code>] [<code>&#8211;version</code>] [<code>-o</code>&nbsp;<wbr><i>configoption</i>&#8230;] <i>config</i> [<i>label</i>] [slot&nbsp;<wbr><i>slot</i>]</dl>
<h2>Description</h2>
<dd>This command applies a label to an Amanda volume, erasing the volume in the process. </p>
<p> Amanda uses labels to identify volumes: <code><a href="/docs/linux/man/8-amdump/">amdump</a></code>(8) and <code><a href="/docs/linux/man/8-amflush/">amflush</a></code>(8) verify the label before writing to make sure the proper volume is loaded, and the recovery programs use the label to ensure they are reading the data they expect. </p>
<p> If no [<i>slot</i>] and no [<i>barcode</i>] is given, then <code>amlabel</code> labels the tape in the current slot of the default changer. If a slot is given, it labels the volume in that slot. If a barcode is given, it labels the volume with that barcode. <i>Label</i> may be any string that does not contain whitespace and that matches the <code>labelstr</code> (see <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5)). </p>
<p> If [<i>label</i>] is not given, an autolabel is generated, see <code>autolabel</code> in <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5). </p>
<p> If [<code>&#8211;assign</code>] is given, the barcode and meta-label are assigned to the label without labeling the volume. The label must already be in the tapelist file. </p>
<p> This command also appends the new volume to the <code><a href="/docs/linux/man/5-tapelist/">tapelist</a></code>(5) file, so that they will be used in the order they are labeled (depending on the taperscan in use &#8212; see <code><a href="/docs/linux/man/7-amanda-taperscan/">amanda-taperscan</a></code>(7)). </p>
<p> As a precaution, <code>amlabel</code> will not write a label if the volume already contains an active label or if the label specified is on an active tape. The [-f] (force) flag bypasses these verifications.</p>
<h2>Options</h2>
<p><code>&#8211;barcode </code><i>barcode</i></p>
<dl>
<dd>With [&#8211;assign], assign the barcode to the label. Without [&#8211;assign], label the volume with that barcode.</dl>
<p> <code>&#8211;meta </code><i>meta-label</i></p>
<dl>
<dd>Assign the meta label to the label after labeling the volume.</dl>
<p> <code>&#8211;assign</code></p>
<dl>
<dd>Assign the barcode or meta-label to the label without labeling the volume. The label must already be in the tapelist file.</dl>
<p> <code>-f</code></p>
<dl>
<dd>Force the label operation; see above</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Output version information</dl>
<p> <code>-o </code><i>configoption</i></p>
<dl>
<dd>See the &quot;CONFIGURATION OVERRIDE&quot; section in <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8).</dl>
<h2>Example</h2>
<p>Write an Amanda label with the string &quot;DMP000&quot; on the current volume: </p>
<pre>% amlabel daily DMP000 </pre>
<p>Label the tape in slot 3 of the changer with the label &quot;DMP003&quot;: </p>
<pre>% amlabel daily DMP003 slot 3 </pre>
<h2>Messages</h2>
<p>Label &#8216;<i>label</i>&#8216; doesn&#8217;t match labelstr &#8216;<i>labelstr</i>&#8216;</p>
<dl>
<dd>The given label does not match the configured labelstr. Even with <code>-f</code>, this is an error.</dl>
<p> Label &#8216;<i>label</i>&#8216; already on a volume</p>
<dl>
<dd>The given label is already on another volume in the tapelist, and Amanda will not write it to this volume unless forced.</dl>
<p> Found label &#8216;<i>label</i>&#8216;, but it is not from configuration <i>config</i>.</p>
<dl>
<dd>The label <code>amlabel</code> found on the volume does not match this configuration&#8217;s <code>labelstr</code>, so it is probably part of a different Amanda configuration. Amanda will not overwrite the label unless it is forced.</dl>
<p> Volume with label &#8216;<i>label</i>&#8216; contains data from this configuration.</p>
<dl>
<dd>The label <code>amlabel</code> found on the volume still has valid data on it and Amanda will not overwrite it unless forced. Note that this does not distinguish between active and inactive volumes.</dl>
<dl>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), <code><a href="/docs/linux/man/5-tapelist/">tapelist</a></code>(5), <code><a href="/docs/linux/man/7-amanda-taperscan/">amanda-taperscan</a></code>(7), <code><a href="/docs/linux/man/8-amdump/">amdump</a></code>(8), <code><a href="/docs/linux/man/8-amflush/">amflush</a></code>(8) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Authors</h2>
<p><code>James da Silva</code> &lt;jds [at] amanda.org&gt; </p>
<p> <code>Stefan G. Weichinger</code> &lt;sgw [at] amanda.org&gt; </p>
<p> <code>Dustin J. Mitchell</code> &lt;dustin [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
