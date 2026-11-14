---
title: "cspctl(1)"
name: "cspctl"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cspctl/"
description: "cspctl – Sound Blaster 16 ASP/CSP control program"
---

<h2 class="name">NAME</h2>
<p> cspctl &#8211; Sound Blaster 16 ASP/CSP control program</p>
<h2>SYNOPSIS</h2>
<p> <code>cspctl</code> command [-options] &lt;filename&gt; </p>
<h2>DESCRIPTION</h2>
<p> <code>cspctl</code> is a simple CSP microcode loader for Crative Sound Blaster 16ASP and some Sound Blaster AWE32 sound cards with Creative Signal Processor (CSP) chip (CT1748A) installed. <code>cspctl</code> can also be used as a post-install function to <i>snd-sb16-csp</i> module to load default codec at module installation. If CSP chip is succesfully detected and initialized, it will be installed as a hardware dependant device <i>hwC0D2</i> into /dev/snd directory. Currently, following codecs can be loaded to CSP device:</p>
<dl>
<dt>
<dd>
<pre>
<code>wfm0001a.csp</code>    QSound decoder
<code>wfm0006a.csp</code>    A-law codec
<code>wfm0007a.csp</code>    u-law codec
<code>wfm0011a.csp</code>    IMA ADPCM codec (distorted output for IMA test files)
<code>wfm0200a.csp</code>    Creative ADPCM codec (sounds like Intel/DVI IMA ADPCM compatible)
<code>wfm0202a.csp</code>    Fast Speech 8 codec
<code>wfm0203a.csp</code>    Fast Speech 10 codec
</pre>
</dl>
<p> These codecs are not yet supported by ALSA:</p>
<dl>
<dt>
<dd> <code>wfm0201a.csp</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Text2Speech decoder
</dl>
<p> Qsound microcode file has <code>four functions,</code> each function is a decoder for different sample rate. Rates for QSound functions #1, #2, #3 and #4 are 44100, 22050, 11025 and 8000Hz respectively. IMA ADPCM and FastSpeech codecs are formed of <code>two functions,</code> the first one is for capture and the second one is for playback. A-law and u-law codecs have only <code>one function.</code> To load for example function #2 from QSound microcode file (decoder for 22050Hz), run as follows:</p>
<dl>
<dt>
<dd> % cspctl load -f 2 -d QSound wfm0001a.csp</dl>
<p> After successful loading, /proc/asound/SB16/cspD2 will show:</p>
<dl>
<dt>
<dd>
<pre><code>
Creative Signal Processor[v1 .0] State : -x-- L
                                             Codec : QSound[func #2] Sample rates : 22050Hz QSound decoder disabled
</code></pre>
</dl>
<p> With QSound decoder microcode loaded, all simple PCM file formats can be played with QSound 180 degree positioning applied. QSound element is dynamically added into mixer structure as <i>3DEffect1-space</i> element. It will only show if support for CSP has been compiled into ALSA drivers, CSP chip has been found, and QSound codec is loaded into CSP. When enabled, QSound position can be dynamically changed by mixer slider, and proc interface should follow the state of CSP chip and its current QSound position:</p>
<dl>
<dt>
<dd>
Creative Signal Processor[v1 .0] State : Qx &#8211; RL<br />
                                                  Codec : QSound[func #2] Sample rates : 22050Hz QSound decoder enabled<br />
                                                              Processing 16bit mono PCM samples<br />
                                                                  Qsound position : left = 0x9,<br />
                                                                                    right = 0x9
</dl>
<p> Driver supports autoloading of u-Law, A-Law and Ima-ADPCM hardware codecs. Autoloading is active only when there is no microcode loaded to CSP, and there is no need to preload appropriate *.csp files. To unload manually loaded microcode, you should run</p>
<dl>
<dt>
<dd> % cspctl unload</dl>
<p> If hardware codec microcode has been manually loaded, then CSP will support only loaded PCM format and autoloading will be disabled. In such case, proc interface will show loaded codec properties:</p>
<dl>
<dt>
<dd>
<pre><code>
Creative Signal Processor[v1 .0] State : -x-- L
                                             Codec : IMA -
                                                     ADPCM[func #2] Sample rates : All
                                                                                       PCM format ID : 0x400000(16bit / -)[mono / stereo][playback / -]
</code></pre>
</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>load</code></p>
<dd> Load microcode from filename to CSP.</p>
<dt><code>unload</code></p>
<dd> Unload microcode from CSP.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Display a short help.</p>
<dt><code>-c card</code></p>
<dd> Select a card number. Option defaults to 0.</p>
<dt><code>-f function</code></p>
<dd> Select a function from microcode file. Option defaults to 1.</p>
<dt><code>-d description</code></p>
<dd> Optional microcode description string. </p>
</dl>
<h2>AUTHOR</h2>
<p> Uros Bizjak &lt;uros [at] kss-loka.si&gt;. </p>
<h2>Index</h2>
