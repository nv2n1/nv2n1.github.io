---
title: "asfxload(1)"
name: "asfxload"
section: "1"
letter: "a"
url: "/docs/linux/man/1-asfxload/"
description: "sfxload, asfxload – load a SoundFont file on the Emux WaveTable"
---

<h2 class="name">NAME</h2>
<p> sfxload, asfxload &#8211; load a SoundFont file on the Emux WaveTable</p>
<h2>SYNOPSIS</h2>
<p> <code>sfxload</code> [<i>-options</i>]<i> fontfile</i> </p>
<p> <code>asfxload</code> [<i>-options</i>]<i> fontfile</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>sfxload</code> and <code>asfxload</code> are utility program sto transfer the sound wave and instruments data in a SoundFont file to the AWE32 sound driver, or to the Emux WaveTable of ALSA sbawe and emu10k1 drivers. This program is necessary for playing MIDI samples via sequencer programs supporting AWE driver. There is no big difference between <code>sfxload</code> and <code>asfxload</code> except for that <code>asfxload</code> is for ALSA and <code>sfxload</code> is for OSS, respecitvely. The options to specify devices are different between them (see below). </p>
<p> Basically, sfxload behaves as two ways. % sfxload fontfile<br />
 % sfxload -b1 fontfile </p>
<p> The first usage is to read SF2 (or SBK) file and transfer to the awe driver. In this case, the samples which were loaded on the driver are replaced with the new one. In the second case, sfxload reads the file and appends it to the pre-loaded samples on the driver with specified bank number. The old samples remain in the driver. The additional samples can be cleared via <code>-x</code> option (see below). </p>
<p> The sound files are searched through the path list. The path list is defined as built-in. If the environment variable <code>SFBANKDIR</code> or the command line option <code>-P</code> is given, it replaces the default search list. The file extension <i>.sf2</i>, and <i>.sbk</i> can be abbreviated. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-F, &#8211;device=</code><i>file</i>(sfxload only)</p>
<dd> Specify the device file to be used. Default value is <i>/dev/sequencer</i>.</p>
<dt><code>-D, &#8211;index=</code><i>number</i>(sfxload only)</p>
<dd> Specify the device index of AWE driver. Negative number (e.g. -1) means to probe the first AWE device automatically. For selecting the other AWE cards, a positive index number must be given here. Default value is <code>-1</code>.</p>
<dt><code>-D, &#8211;hwdep=</code><i>name</i>(asfxload only)</p>
<dd> Specify the hwdep name to be used. As default, asfxload seeks until any Emux compatible hwdep device is found.</p>
<dt><code>-i, &#8211;clear</code><i></i>[=bool]</p>
<dd> Remove all samples before loading the fonts. This is an explicit directive (see -b option). If this option is specified alone without soundfont file arguments, sfxload does onlay remove samples. Either of <code>on</code>, <code>off</code>, <code>yes</code>, <code>no</code>, <code>true</code>, or <code>false</code> can be specified as an optional argument.</p>
<dt><code>-x, &#8211;remove</code><i></i>[=bool]</p>
<dd> Remove the optional samples previouly loaded via <code>-b</code> option. Otherwise, all new samples are simply appended.</p>
<dt><code>-N, &#8211;increment</code><i></i>[=bool]</p>
<dd> Do not clear samples even with the absence of <code>-b</code> option. However, this option is not exclusive with <code>-x</code> option. If both options are specified, and the memory full error is encountered during loading fonts, <code>sfxload</code> will try to remove samples and load the fonts again.</p>
<dt><code>-b, &#8211;bank=</code><i>number</i></p>
<dd> Append the sound samples on the specified bank. Without this option, all present samples in the driver are removed before loading the new fonts unless <code>-N</code> option is specified. Usually, this option is necessary to load user bank, typically in bank one. For example, % sfxload synthgm.sbk<br />
 % sfxload -b1 surprise.sf2 </p>
<dt><code>-l, &#8211;lock</code><i></i>[=bool]</p>
<dd> Lock the font. The locked font is no longer removed via remove option (<code>-x</code>) even if it&#8217;s loaded together with <code>-b</code> option.</p>
<dt><code>-C, &#8211;compat</code><i></i>[=bool]</p>
<dd> Use the old (v0.4.2) parameter calculations.</p>
<dt><code>-A, &#8211;sense=</code><i>sensitivity</i></p>
<dd> (Only valid on compatible mode)<br />
 Set sample attenuation sensitivity. This option controls the sensitivity of initial attenuation parameter of each instrument defined in SoundFont file. In the program, each parameter is calculated from the value divided by this number for the original value. The number <i>1.0</i> means that the original initial attenuation parameters would be used. Generally, smaller number makes drum sounds louder. (I think <code>&quot;-A 2&quot;</code> would be similar to Windows sounds.) The default value is <i>10</i>. Note that this option changes also the default attenuation automatically (see below).</p>
<dt><code>-a, &#8211;atten=</code><i>attenuation</i></p>
<dd> (Only valid on compatible mode)<br />
 Set the default attenuation level. This option controls the minimum attenuation of the sample. The parameter is given in raw digit number for AWE driver, that is, in 8/3 dB unit. Since <code>&#8211;sense</code> option changes the default attenuation automatically, specify this option later from <code>&#8211;sense</code> option. The default value is <i>32</i>.</p>
<dt><code>-d, &#8211;decay=</code><i>scale</i></p>
<dd> (Only valid on compatible mode)<br />
 Set the scale of envelope decay time. Default value is <i>50.0</i>. Sounds decay fast when larger number is set. The ver.0.3 sfxload uses <i>54.8</i>. If you want to keep the same sound, use this number instead.</p>
<dt><code>-M, &#8211;memory</code><i></i>[=bool]</p>
<dd> Display the left memory size in DRAM on the AWE32 card.</p>
<dt><code>-c, &#8211;chorus=</code><i>percent</i></p>
<dd> Specify the effects of chorus. The value is in percent, from 0 to 100. The default is unspecified. This value may be overwritten by MIDI control messages.</p>
<dt><code>-r, &#8211;reverb=</code><i>percent</i></p>
<dd> Specify the effects of reverb. The value is in percent, from 0 to 100. The default is unspecified. This value may be overwritten by MIDI control messages.</p>
<dt><code>-B, &#8211;addblank</code><i></i>[=bool]</p>
<dd> Add 48 size of blank loop on each sample data. Usually, this option is not necessary. Most of soundfont files are designed well for enough blank loops for each sample.</p>
<dt><code>-L, &#8211;extract=</code><i>source</i>[:<i>map</i>]</p>
<dd> Extract and load only the specified preset(s). This option is usually employed by drvmidi. The preset is given as same as in virtual bank file.</p>
<dt><code>-v, &#8211;verbose</code><i></i>[=level]</p>
<dd> Increase or set the verbosity level.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Don&#8217;t show error messages, equivalen with &#8211;verbose=0.</p>
<dt><code>-V, &#8211;volume=</code><i>percent</i></p>
<dd> Specify the total volume of sounds, provided in percent. The default volume is <i>70%</i>.</p>
<dt><code>-P, &#8211;path=</code><i>path1</i><code>:</code><i>path2</i><code>:</code><i>pathN</i></p>
<dd> Specify the search path list. The sound files are searched from <i>path1</i>, <i>path2</i>, and so on. This overrides both the system path and environment variable <code>SFBANKDIR</code>. </p>
</dl>
<h2>VIRTUAL BANK FILE</h2>
<p> The virtual bank file is a list of presets treated as one soundfont file. The syntax of virtual bank is as follows: <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt># comments</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>source:map[:soundfont [preset-name]</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>source:map[:soundfont [preset-name]</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8230;</p>
<p> The first and second items are the source and mapped presets, respectively. The former is the existing preset in the soundfont, and the latter is the actual preset loaded on the sound driver. The preset is described by the following three values, <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>preset/bank/keynote<br />
 If bank and keynote are omitted, bank 0 and keynote -1 (meaning to search all keys) are applied. </p>
<p> The third item is the name of soundfont file. The file is searched from the prescribed search-path. The remaining arguments are ignored in <code>sfxload</code>. </p>
<p> If the soundfont name is omitted, sfxload loads it as preset mapping. It just behaves like a symbolic link of file opposing to copying of the file. Any sample data is not referred at this time, but searched first when the note is played. </p>
<p> A couple of special commands can be used together with the virtual presets above. <code>default</code> command is used to specify the default soundfont file. Any other presets which are not defined in the virtual preset lists are loaded from this default font. For example, in the following virtual bank, <i>2mbgmgs.sf2</i> is used except for standard drumsets which employs <i>drum.sf2</i>: <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0/128:0/128:drum.sf2</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>default 2mbgmgs.sf2</p>
<p> Another special command is <code>include</code> command. This simply includes another virtual bank file under the current position. For example, <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>default standard.sf2</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0/128:0/128:drum.sf2</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>include xgsfx.bnk</p>
<h2>SYSTEM RESROUCE FILE</h2>
<p> The default option arguments can be stored in the system resource file. There are two files loaded as default. <i>$HOME/.sfxloadrc</i><br />
 <i>/etc/sfxloadrc</i> </p>
<p> The syntax is as follows: fontname -options.. The first argument is soundfont file name for each option. The remaining arguments are identical with command line options. The font name <i>default</i> is used for default options for all sound fonts. The default options are overridden by specific options or command line options. </p>
<p> For example, to set default chorus level 20 except for synthgm font, you can write a resource file <i>~/.sfxloadrc</i> like that: default<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8211;chorus=20</p>
<p> synthgm &#8211;chorus=0 </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>SFBANKDIR</code></p>
<dd> Search path for sound files. The current directory is always searched at first. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-drvmidi/">drvmidi</a></code>(1) </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1996-2003 Takashi Iwai. The AWE32 driver and utilties are free software; you can redistribute them and/or modify them under the terms of the <i>GNU General Public License</i> as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<h2>Index</h2>
