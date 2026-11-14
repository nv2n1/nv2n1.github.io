---
title: "amtapetype(8)"
name: "amtapetype"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amtapetype/"
description: "amtapetype – generate a tapetype definition by testing the device directly"
---

<p>amtapetype &#8211; generate a tapetype definition by testing the device directly</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amtapetype</code> [-h] [-c] [-f] [-p] [-b&nbsp;<wbr><i>blocksize</i>] [-t&nbsp;<wbr><i>typename</i>] [-l&nbsp;<wbr><i>label</i>] [<code>-o</code>&nbsp;<wbr><i>configoption</i>&#8230;] [<i>config</i>] [<i>device</i>]</dl>
<h2>Description</h2>
<p><code>amtapetype</code></p>
<dd>generates a tapetype entry for Amanda by testing the device directly.</p>
<h2>Options</h2>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> The options for <code>amtapetype</code> have changed in version 2.6.1 </p>
</dl>
<p> <code>-h</code></p>
<dl>
<dd>Display the help message.</dl>
<p> <code>-c</code></p>
<dl>
<dd>Run only the hardware compression detection heuristic test and stop. This takes a few minutes only.</dl>
<p> <code>-f</code></p>
<dl>
<dd>Run amtapetype even if the loaded volume is already labeled.</dl>
<p> <code>-p</code></p>
<dl>
<dd>Run only the device property discovery.</dl>
<p> <code>-b</code><i> blocksize</i></p>
<dl>
<dd>block size to use with the device (default: 32k)</dl>
<p> <code>-t</code> <i>typename</i></p>
<dl>
<dd>Name to give to the new tapetype definition.</dl>
<p> <code>-l</code><i> label</i></p>
<dl>
<dd>Label to write on the tape (default is randomly generated).</dl>
<p> <code>-o </code><i>configoption</i></p>
<dl>
<dd>See the &quot;CONFIGURATION OVERRIDE&quot; section in <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8).</dl>
<p> If a configuration is specified, it is loaded and used to configure the device. Note that global configuration parameters are not applied to the device, so if you need to apply properties to a device to run amtapetype, you should supply those properties in a named <i>device</i> section.</p>
<h2>Example</h2>
<p>Generate a tapetype definition for your tape device: </p>
<dl>
<dd>
<pre>% amtapetype -f /dev/nst0</pre>
</dl>
<h2>Notes</h2>
<p>If the device cannot reliably report its comprssion status (and as of this writing, no devices can do so), hardware compression is detected by measuring the writing speed difference of the tape drive when writing an amount of compressable and uncompresseable data. If your tape drive has very large buffers or is very fast, the program could fail to detect hardware compression status reliably. </p>
<p> Volume capacity is determined by writing one large file until an error, interpereted as end-of-tape, is encountered. In the next phase, about 100 files are written to fill the tape. This second phase will write less data, because each filemark consumes some tape. With a little arithmetic, <code>amtapetype</code> calculates the size of these filemarks. </p>
<p> All sorts of things might happen to cause the amount of data written to vary enough to generate a strange file mark size guess. A little more &quot;shoe shining&quot; because of the additional file marks (and flushes), dirt left on the heads from the first pass of a brand new tape, the temperature/humidity changed during the multi-hour run, a different amount of data was written after the last file mark before EOT was reported, etc. </p>
<p> Note that the file mark size might really be zero for whatever device this is, and it was just the measured capacity variation that caused <code>amtapetype</code> to think those extra file marks in pass 2 actually took up space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Authors</h2>
<p><code>Dustin J. Mitchell</code> &lt;dustin [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
<p> <code>Jean-Louis Martineau</code> &lt;martineau [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
