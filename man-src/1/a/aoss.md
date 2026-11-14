---
title: "aoss(1)"
name: "aoss"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aoss/"
description: "aoss – Wrapper script to facilitate use of the ALSA OSS compatibility library."
---

<h2>NAME</h2>
<p> aoss &#8211; Wrapper script to facilitate use of the ALSA OSS compatibility library.</p>
<h2>SYNOPSIS</h2>
<p> <code>aoss</code> [-32] <i>osscommand</i> [arguments] </p>
<h2>DESCRIPTION</h2>
<p> <code>aoss</code> is a simple wrapper script which facilitates the use of the ALSA OSS compatibility library. It just sets the appropriate LD_PRELOAD path and then runs the command. </p>
<p> This is useful in cases where routing settings (which can be made in your .asoundrc file) need to be applied to commands that use the OSS API. </p>
<p> Examples of asoundrc configuration: </p>
<p> pcm.dsp0 { <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>type plug<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>slave.pcm &quot;hw:0,0&quot;<br />
 } </p>
<p> or </p>
<p> pcm.dsp0 { <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>type plug<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>slave.pcm &quot;dmix&quot;<br />
 } </p>
<p> In the above configuration examples, the pcm.dsp0 definition is used to wrap calls do /dev/dsp0. You can also wrap usage of /dev/dsp1, /dev/dsp2, etc. by defining pcm.dsp1, pcm.dsp2, etc.. </p>
<p> The PCM name to open can be given explicitly via <code>ALSA_OSS_PCM_DEVICE</code> environment variable, too. This overrides the default <code>dsp0</code>, etc. </p>
<p> Note on mmap: aoss mmap support might be buggy. Your results may vary when trying to use an application that uses mmap&#8217;ing to access the OSS device files. </p>
<h3>Arguments</h3>
<dl>
<dt>32</p>
<dd> Use 32-bit alsa-oss library (on 64-bit systems) <i>osscommand</i> A command that uses the OSS API</p>
<dt><i>arguments</i></p>
<dd> The appropriate arguments and options for the OSS command.</p>
<dt>
<dd></dl>
<h2>AUTHORS</h2>
<p> The OSS compatibility library is by Abramo Bagnara &lt;abramo [at] alsa-project.org&gt;. The aoss script and this document are by James Tappin &lt;james [at] xena.uklinux.net&gt;. </p>
<h2>Index</h2>
