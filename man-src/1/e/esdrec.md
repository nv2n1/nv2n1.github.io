---
title: "esdrec(1)"
name: "esdrec"
section: "1"
letter: "e"
url: "/docs/linux/man/1-esdrec/"
description: "esdrec – record a sound file"
---

<h2>NAME</h2>
<p> esdrec &#8211; record a sound file</p>
<h2>SYNOPSIS</h2>
<p> <code>esdrec</code> [-<code>s </code><i>hostname</i>:<i>port</i>] [-<code>b</code>] [-<code>h</code>] [-<code>m</code>] [-<code>r </code><i>freq</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>esdrec</code> application pipes data from the sound device to <code>stdout</code> using the Enlightened Sound Daemon (<code>esd</code>).</p>
<h2>OPTIONS</h2>
<p> The following options are supported: </p>
<p> <code>-s </code><i>hostname</i>:<i>port</i> Contact the <code>esd</code> server on <i>hostname</i> at <i>port</i>. </p>
<p> <code>-b</code> Specify that the output should be in 8-bit format. By default, the output is in 16-bit format. </p>
<p> <code>-h</code> Display help text, and exit. </p>
<p> <code>-m</code> Specify that the output should be in mono format. By default, the output is in stereo format. </p>
<p> <code>-r </code><i>freq</i> Specify that the output rate should be set to <i>freq</i>. By default, the output rate is set to 44.1 kHz. </p>
<h2>EXAMPLES</h2>
<p> <code>Example 1: Record sound from sound device to file &quot;sample&quot;</code> </p>
<pre>
example% <code>esdrec &gt; sample</code>
</pre>
<h2>EXIT STATUS</h2>
<p> The following exit values are returned: </p>
<p> <code>0</code> Application exited successfully </p>
<p> <code>&gt;0</code> Application exited with failure </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-esd/">esd</a></i>(1), <i><a href="/docs/linux/man/1-esdcat/">esdcat</a></i>(1), <i><a href="/docs/linux/man/1-esddsp/">esddsp</a></i>(1), <i><a href="/docs/linux/man/1-esdloop/">esdloop</a></i>(1), <i><a href="/docs/linux/man/1-esdplay/">esdplay</a></i>(1), <i><a href="/docs/linux/man/1-esdsample/">esdsample</a></i>(1), <i><a href="/docs/linux/man/1-esd-config/">esd-config</a></i>(1), <i><a href="/docs/linux/man/1-esdctl/">esdctl</a></i>(1), <i><a href="/docs/linux/man/1-esdfilt/">esdfilt</a></i>(1), <i><a href="/docs/linux/man/1-esdmon/">esdmon</a></i>(1) </p>
<h2>Index</h2>
