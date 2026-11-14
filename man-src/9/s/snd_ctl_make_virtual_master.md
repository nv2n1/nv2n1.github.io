---
title: "snd_ctl_make_virtual_master(9)"
name: "snd_ctl_make_virtual_master"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ctl_make_virtual_master/"
description: "snd_ctl_make_virtual_master – Create a virtual master control"
---

<p>snd_ctl_make_virtual_master &#8211; Create a virtual master control</p>
<h2>Synopsis</h2>
<pre><code>struct snd_kcontrol *snd_ctl_make_virtual_master(char *name, const unsigned int *tlv);</code></pre>
<h2>Arguments</h2>
<p><i>name</i></p>
<dl>
<dd>
<dd>name string of the control element to create</dl>
<p> <i>tlv</i></p>
<dl>
<dd>optional TLV int array for dB information</dl>
<h2>Description</h2>
<p>Creates a virtual master control with the given name string. </p>
<p> After creating a vmaster element, you can add the slave controls via <code>snd_ctl_add_slave</code> or <code>snd_ctl_add_slave_uncached</code>. </p>
<p> The optional argument <i>tlv</i> can be used to specify the TLV information for dB scale of the master control. It should be a single element with #SNDRV_CTL_TLVT_DB_SCALE, #SNDRV_CTL_TLV_DB_MINMAX or #SNDRV_CTL_TLVT_DB_MINMAX_MUTE type, and should be the max 0dB.</p>
<h2>Return</h2>
<p>The created control element, or <code>NULL</code> for errors (ENOMEM).</p>
<h2>Copyright</h2>
