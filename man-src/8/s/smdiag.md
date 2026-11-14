---
title: "smdiag(8)"
name: "smdiag"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smdiag/"
description: "smdiag – Linux soundcard packet radio modem driver diagnostics utility"
---

<p>smdiag &#8211; Linux soundcard packet radio modem driver diagnostics utility</p>
<h2>Synopsis</h2>
<p><code>smdiag</code> <code>[-i device]</code> <code>[-d display]</code> <code>[ -ce ]</code> </p>
<h2>Description</h2>
<p><code>smdiag</code> may help to adjust the audio levels of the soundcard modem driver, as well as to control the quality of the radio link. It may either display an oscilloscope like view of the input signal, or display an eye diagram. The display may be gated with DCD, i.e. only updated if the modem detects a data carrier. </p>
<h2>Options</h2>
<p><code>smdiag</code> accepts the following options: </p>
<dl>
<dt><code>-i</code></p>
<dd>The <i>device</i> argument specifies the soundcard modem device which should be configured or interrogated. It will usually have the following form: <i>sm[0-3].</i></p>
<dt><code>-d</code></p>
<dd>sets the address of the X server to display the window.</p>
<dt><code>-h</code></p>
<dd>display an overview of the available command line parameters and exit.</p>
<dt><code>-c</code></p>
<dd>toggle the carrier gating of the display.</p>
<dt><code>-e</code></p>
<dd>display an eye diagram (overlay of the synchronized demodulator output) instead of an oscilloscope view of the input signal. </p>
</dl>
<h2>Keys</h2>
<dl>
<dt><code>C</code></p>
<dd>clears the window</p>
<dt><code>D</code></p>
<dd>toggles the DCD gating.</p>
<dt><code>E</code></p>
<dd>displays an eye diagram</p>
<dt><code>I</code></p>
<dd>displays the input signal</p>
<dt><code>Q</code></p>
<dd>quits <i>smdiag</i> </p>
</dl>
<h2>Bugs</h2>
<p><code>smdiag</code> Reacts sluggishly to keypresses. The window size is fixed. For speed reasons, two square root operations per sample are not implemented in the AFSK 1200 baud modes. The eye diagram for the AFSK 1200 baud mode is therefore distorted. </p>
<h2>See Also</h2>
<p><code>smmixer</code> (8), <code>sethdlc</code> (8), linux/drivers/net/soundmodem.c </p>
<h2>Author</h2>
<p>smdiag was written by Thomas Sailer (t.sailer [at] alumni.ethz.ch).</p>
