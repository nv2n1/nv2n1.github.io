---
title: "esdsample(1)"
name: "esdsample"
section: "1"
letter: "e"
url: "/docs/linux/man/1-esdsample/"
description: "esdsample – play a sample"
---

<h2>NAME</h2>
<p> esdsample &#8211; play a sample</p>
<h2>SYNOPSIS</h2>
<p> <code>esdsample</code> [-<code>s </code><i>hostname</i>:<i>port</i>] [-<code>b</code>] [-<code>d</code>] [-<code>e</code>] [-<code>h</code>] [-<code>m</code>] [-<code>r </code><i>freq</i>] <i>samplename</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>esdsample</code> utility plays a sample using the Enlighted Sound Daemon (<code>esd</code>).</p>
<h2>OPTIONS</h2>
<p> The following options are supported: </p>
<p> <code>-s </code><i>hostname</i>:<i>port</i> Contact the <code>esd</code> server on <i>hostname</i> at <i>port</i>. </p>
<p> <code>-b</code> Specify that the output should be in 8-bit format. By default, the output is in 16-bit format. </p>
<p> <code>-d</code> Play the sample from file as raw data. The default behavior is to read the data from a sound file (<code>.wav</code>, <code>.au</code>, and so on). If this option is chosen, <i>samplename </i>is the name of a file. </p>
<p> <code>-e</code> Play the sample from the <code>esd </code>cache. If this option is chosen, <i>samplename </i> is the name of the sample in the cache. </p>
<p> <code>-h</code> Display help text, and exit. </p>
<p> <code>-m</code> Specify that the output should be in mono format. By default, the output is in stereo format. </p>
<p> <code>-r </code><i>freq</i> Specify that the output rate should be set to <i>freq</i>. By default, the output rate is set to 44.1 kHz. </p>
<h2>OPERANDS</h2>
<p> The following operands are supported: </p>
<p> <i>samplename</i> The name of the sample to be played. If the &#8211;<code>e</code> option is used, <i>samplename </i>is the <code>esd </code> cache name. Otherwise, <i>samplename </i> is a filename. </p>
<h2>EXAMPLES</h2>
<p> <code>Example 1: Playing a sample from a file </code> </p>
<pre>
example% <code>esdsample generic.wav</code>
</pre>
<p> <code>Example 2: Playing a sample from the esd cache</code> </p>
<pre>
example% <code>esdsample -e</code> esdctl:generic.wav
</pre>
<p> (where <code>esdctl:generic.wav</code> is the cache name)</p>
<h2>EXIT STATUS</h2>
<p> The following exit values are returned: </p>
<p> <code>0</code> Application exited successfully </p>
<p> <code>&gt;0</code> Application exited with failure </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-esd/">esd</a></i>(1), <i><a href="/docs/linux/man/1-esdcat/">esdcat</a></i>(1), <i><a href="/docs/linux/man/1-esddsp/">esddsp</a></i>(1), <i><a href="/docs/linux/man/1-esdloop/">esdloop</a></i>(1), <i><a href="/docs/linux/man/1-esdplay/">esdplay</a></i>(1), <i><a href="/docs/linux/man/1-esd-config/">esd-config</a></i>(1), <i><a href="/docs/linux/man/1-esdctl/">esdctl</a></i>(1), <i><a href="/docs/linux/man/1-esdfilt/">esdfilt</a></i>(1), <i><a href="/docs/linux/man/1-esdmon/">esdmon</a></i>(1), <i><a href="/docs/linux/man/1-esdrec/">esdrec</a></i>(1) </p>
<h2>Index</h2>
