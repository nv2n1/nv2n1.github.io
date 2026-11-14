---
title: "smmixer(8)"
name: "smmixer"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smmixer/"
description: "smmixer – get/set Linux soundcard packet radio modem driver mixer"
---

<p>smmixer &#8211; get/set Linux soundcard packet radio modem driver mixer</p>
<h2>Synopsis</h2>
<p><code>smmixer</code> <code>[-i device]</code> <code>[ </code>params<code> ]</code> </p>
<h2>Description</h2>
<p><code>smmixer</code> displays and/or sets the input source and input and output levels of a soundcard modem port. </p>
<h2>Options</h2>
<p><code>smmixer</code> accepts the following option: </p>
<dl>
<dt><code>-i</code></p>
<dd>The <i>device</i> argument specifies the soundcard modem device which should be configured or interrogated. It will usually have the following form: <i>sm[0-3].</i> </p>
</dl>
<h2>Parameters</h2>
<p>The <code>AD1848 (WSS)</code> mixer accepts the following parameters:</p>
<dl>
<dt><code>ol=val</code></p>
<dd>sets the level of the left output to the specified value. Legal values are from -100..0dB.</p>
<dt><code>or=val</code></p>
<dd>sets the level of the right output to the specified value. Legal values are from -100..0dB.</p>
<dt><code>o=val</code></p>
<dd>sets the level of both outputs to the specified value. Legal values are from -100..0dB.</p>
<dt><code>il=val</code></p>
<dd>sets the level of the left input to the specified value. Legal values are from 0..43dB.</p>
<dt><code>ir=val</code></p>
<dd>sets the level of the right input to the specified value. Legal values are from 0..43dB.</p>
<dt><code>i=val</code></p>
<dd>sets the level of both inputs to the specified value. Legal values are from 0..43dB.</p>
<dt><code>sl=val</code></p>
<dd>sets the source of the left input to the specified value. Legal values are <i>line, aux1, mic</i> or <i>dac.</i></p>
<dt><code>sr=val</code></p>
<dd>sets the source of the right input to the specified value. Legal values are <i>line, aux1, mic</i> or <i>dac.</i></p>
<dt><code>s=val</code></p>
<dd>sets the source of both inputs to the specified value. Legal values are <i>line, aux1, mic</i> or <i>dac.</i> </p>
<p> The <code>CT1335 (SB2.x)</code> mixer accepts the following parameter:</p>
<dt><code>o=val</code></p>
<dd>sets the output level to the specified value. Legal values are from -46..0dB. </p>
<p> The <code>CT1345 (SBPro)</code> mixer accepts the following parameters:</p>
<dt><code>ol=val</code></p>
<dd>sets the level of the left output to the specified value. Legal values are from -46..0dB.</p>
<dt><code>or=val</code></p>
<dd>sets the level of the right output to the specified value. Legal values are from -46..0dB.</p>
<dt><code>o=val</code></p>
<dd>sets the level of both outputs to the specified value. Legal values are from -46..0dB.</p>
<dt><code>s=val</code></p>
<dd>sets the input source to the specified value. Legal values are <i>mic, cd</i> or <i>line.</i> </p>
<p> The <code>CT1745 (SB16, SB32 AWE)</code> mixer accepts the following parameters:</p>
<dt><code>ol=val</code></p>
<dd>sets the level of the left output to the specified value. Legal values are from -62..18dB.</p>
<dt><code>or=val</code></p>
<dd>sets the level of the right output to the specified value. Legal values are from -62..18dB.</p>
<dt><code>o=val</code></p>
<dd>sets the level of both outputs to the specified value. Legal values are from -62..18dB.</p>
<dt><code>il=val</code></p>
<dd>sets the level of the left input to the specified value. Legal values are from -62..18dB.</p>
<dt><code>ir=val</code></p>
<dd>sets the level of the right input to the specified value. Legal values are from -62..18dB.</p>
<dt><code>i=val</code></p>
<dd>sets the level of both inputs to the specified value. Legal values are from -62..18dB.</p>
<dt><code>s=val</code></p>
<dd>enables the specified value as a source. Legal values are <i>line, line.l, line.r, midi, midi.l, midi.r, cd, cd.l, cd.r</i> or <i>mic.</i> </p>
</dl>
<h2>Considerations</h2>
<p>It is important that the audio levels of your radio match those of the soundcard. To help achieve this, use the <i>smdiag</i> utility. </p>
<p> This utility can only be used after the interface is started up, i.e. after ifconfig sm? up. </p>
<p> The sound driver and the soundcard modem driver are mutually exclusive, i.e. they cannot both access the same soundcard at the same time. Even worse, the sound driver reserves the soundcard as soon as it gets loaded. The souncard modem driver however reserves the card only when the interface is started, i.e. during ifconfig if up. </p>
<p> 9600 baud may not currently work on SoundBlaster cards with DSP revision 4.x, i.e. SB16 and SB32 AWE. This is because they seem to not be fully backwards compatible.</p>
<h2>See Also</h2>
<p><code>smdiag</code> (8), <code>sethdlc</code> (8), linux/drivers/net/soundmodem.c </p>
<h2>Author</h2>
<p>smmixer was written by Thomas Sailer (t.sailer [at] alumni.ethz.ch).</p>
