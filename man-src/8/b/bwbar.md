---
title: "bwbar(8)"
name: "bwbar"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bwbar/"
description: "bwbar – create a textual and graphical readout of current bandwidth usage"
---

<p>bwbar &#8211; create a textual and graphical readout of current bandwidth usage</p>
<h2>Synopsis</h2>
<p><code>bwbar</code> [ <code>&#8211;input|-i</code> ] [ <code>&#8211;output|-o</code> ] [ <code>&#8211;directory|-d</code> <i>directory</i> ] [ <code>&#8211;text-file|-t</code> <i>file</i> ] [ <code>&#8211;png-file|-p</code> <i>file</i> ] [ <code>&#8211;interval|-t</code> <i>seconds</i> ] [ <code>&#8211;width|-x</code> <i>pixels</i> ] [ <code>&#8211;height|-y</code> <i>pixels</i> ] [ <code>&#8211;border|-b</code> <i>pixels</i> ] [ <code>&#8211;kbps|-k</code> ] [ <code>&#8211;Mbps|-M</code> ] [ <code>&#8211;Gbps|-G</code> ] [ <code>&#8211;help|-h</code> ] <i>interface</i> <i>max-Mbps</i> </p>
<h2>Description</h2>
<p>This manual page briefly documents the <code>bwbar</code> program. <code>bwbar</code> is a simple daemon which creatse a readout of current bandwidth usage, generally for inclusion on a webpage. The output appear in both a text file and a PNG format bargraph in the specified output directory, and is based on data gathered from the specified device and the specified maximum bandwidth. </p>
<h2>Options</h2>
<p><code></p>
<dl>
<dt>&#8211;input|-i</dt>
<dd></code> Measure the input bandwidth <code></dd>
<dt>&#8211;output|-o</dt>
<dd></code> Measure output bandwidth (default) <code></dd>
<dt>&#8211;directory|-d</dt>
<dd></code> Specify the output directory <code></dd>
<dt>&#8211;text-file|-f</dt>
<dd></code> Specify the name of the text-format ouput file (defaults to &quot;ubar.txt&quot;) <code></dd>
<dt>&#8211;png-file|-p</dt>
<dd></code> Specify the name of the PNG-format output file (defaults to &quot;ubar.png&quot;) <code></dd>
<dt>&#8211;interval|-t</dt>
<dd></code> Set the poll interval in seconds (defaults to 15 seconds) <code></dd>
<dt>&#8211;width|-x</dt>
<dd></code> Set the width of the graphical bar (defaults to 600 pixels) <code></dd>
<dt>&#8211;height|-y</dt>
<dd></code> Set the height of the graphical bar (defaults to 4 pixels) <code></dd>
<dt>&#8211;border|-b</dt>
<dd></code> Set the border width of the graphical bar (defaults to 1 pixel) <code></dd>
<dt>&#8211;kbps|-k</dt>
<dd></code> Set the units of bandwidth measure to kilobits/second <code></dd>
<dt>&#8211;Mbps|-M</dt>
<dd></code> Set the units of bandwidth measure to megabits/second (default) <code></dd>
<dt>&#8211;Gbps|-G</dt>
<dd></code> Set the units of bandwidth measure to gigabits/second <code></dd>
<dt>&#8211;Daemon|-D</dt>
<dd></code> Run as daemon <code></dd>
<dt>&#8211;help|-h</dt>
<dd></code> Online help </dd>
</dl>
<h2>Author</h2>
<p><code>bwbar</code> was written by Peter Anvin &lt;hpa [at] zytor.com&gt;. </p>
<p> This manual page was prepared by Nick Rusnov &lt;nickrusnov [at] debian.org&gt; for the Debian Project.</p>
