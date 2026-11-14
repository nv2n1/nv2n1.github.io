---
title: "timidity(5)"
name: "timidity"
section: "5"
letter: "t"
url: "/docs/linux/man/5-timidity/"
description: "timidity.cfg – configure file of TiMidity++"
---

<p>timidity.cfg &#8211; configure file of TiMidity++</p>
<h2>Description</h2>
<p>The file <code>timidity.cfg</code> describes the runtime environments of <a href="/docs/linux/man/1-timidity/">timidity</a>(1): that are the path of sound font, instruments configurations, etc.<br />
 <code>TiMidity++</code> looks for the configuration file <code>timidity.cfg</code> at startup, before processing any options. If it can&#8217;t be accessed, and the library path is changed with a <code>-L</code> option on the command line, then the default file will be sought again along the new library path after processing all options, unless another configuration file was specified with the <code>-c</code> option.<br />
 Configuration files define the mapping of MIDI programs to instrument files. Multiple files may be specified, and statements in later ones will override earlier ones.</p>
<h2>Variable</h2>
<p>When alphanumeric and/or underscore `_&#8217; characters continue after dollar sign `$&#8217;, it is considered that the string is a variable and the configuration file is processed, it is transposed to another string. The variable name can also be written with an inside parenthesis, in order to separate from a following character. </p>
<p> For example:<br />
 $variable<br />
 ${variable} # same as $variable </p>
<p> For the moment, the command which newly defines variables is not prepared. The undefined variable is transposed to null string.<br />
 The variable defined as a regular variable is the next only one.</p>
<dl>
<dt><code>$basedir</code></p>
<dd>Expresses the directory where the configuration file exists. By the command which mainly specifies a path, it uses in order to specify the relative path from a setting file.<br />
 When a blank may be included in $basedir, it is necessary to bundle with &quot;&quot;. </p>
<p> For example:<br />
 In /usr/local/share/timidity/timidity.cfg<br />
 dir $basedir/inst # source /usr/local/share/timidity/inst</dl>
<h2>Syntax</h2>
<p>The following statements can be used in a configuration file:</p>
<dl>
<dt><code>dir </code><i>directory [&#8230;]</i></p>
<dd>Adds <i>directory</i> to the search path in the same manner as the <code>-L</code> command line option.<br />
 Archive file are also allowed. </p>
<p> For example:<br />
 dir /usr/local/share/timidity/inst/foo.zip#<br />
 bank 0<br />
 0 bar.pat<br />
 1 baz.pat<br />
 2 zoo.pat </p>
<p> At first, <code>dir</code> specifies the archive name (followed by `#&#8217;) for the path of patch files same as directory name (in this case, /usr/local/share/timidity/inst/foo.zip). <code>TiMidity++</code> recognize the path is an archive file if the expression has the last character `#&#8217;, and also read the files contained in this archive file. In previous example the patch files bar.pat, baz.pat and zoo.pat contained in the foo.zip are also installed.</p>
<dt><code>source </code><i>file [&#8230;]</i></p>
<dd>Reads another configuration file, then continues processing the current one.</p>
<dt><code>progbase </code><i>number</i></p>
<dd>Sets and displays the tone number from <i>number</i> to <i>number</i>+128. If <code>progbase 1</code> are specified, tone numbers that follow are set and displayed as the numbers from <code>1</code> to <code>128</code>.</p>
<dt><code>bank </code><i>[MapID1] number</i></p>
<dd>Selects the tone bank to modify. Patch mappings that follow will affect this tone bank. You can indicate specific map as a target, by specifying any of the following to <i>MapID1</i>: <code>gm2</code>, <code>sc55</code>, <code>sc88</code>, <code>sc88pro</code>, <code>sc8850</code>, <code>xg</code> and <code>xgsfx64</code>.</p>
<dt><code>drumset </code><i>[MapID2] number</i></p>
<dd>Selects the drum set to modify. Patch mappings that follow will affect this drum set. You can indicate specific map as a target, by specifying any ofthe following to <i>MapID2</i>: <code>gm2drum</code>, <code>sc55drum</code>, <code>sc88drum</code>, <code>sc88prodrum</code>, <code>sc8850drum</code>, <code>xgdrum</code> and <code>xgsfx126</code>.</p>
<dt><code>number </code><i>file [options]</i></p>
<dd>
<dt><code>number %font </code><i>file bank prog [key] [options]</i></p>
<dd>
<dt><code>number %sample </code><i>file [options]</i></p>
<dd>Specifies that the MIDI program number in the current tone bank or drum set should be played using the patch file. If <i>file</i> is SoundFont, the specific instrument with <i>bank</i>, <i>prog</i>, and <i>key</i> is taken out by the format of <code>number %font</code>. If <i>file</i> is linear AIFF or WAV sample data, the MIDI program number is specified by the format of <code>number %sample</code>. Options may be any of the following:</p>
<dl>
<dd>
<dl>
<dt><code>amp=</code><i>amplification</i></p>
<dd>Amplifies the instrument&#8217;s volume by <i>amplification</i> percent. If no value is specified, one will be automatically determined whenever the instrument is loaded.</p>
<dt><code>note=</code><i>note</i></p>
<dd>Specifies a fixed MIDI note to use when playing the instrument. If <i>note</i> is <code>0</code>, the instrument will be played at whatever note the Note On event triggering it has. For percussion instruments, if no value is specified in the configuration file, the default in the patch file will be used.</p>
<dt><code>pan=</code><i>panning</i></p>
<dd>Sets the instrument&#8217;s default panning. <i>panning</i> may be <code>left</code>, <code>right</code>, <code>center</code>, or an integer between <code>-100</code> and <code>100</code>, designating full left and full right respectively. If no value is specified, the default in the patch file will be used. Note that panning controls in MIDI files will override this value.</p>
<dt><code>tune=</code><i>tuning[,&#8230;]</i></p>
<dd>Adjust the instrument&#8217;s root frequency. <code>tune=1</code> causes <code>1</code> half tone higher. Since a fraction is available for <i>tuning</i>, it is possible to do fine tuning such as <code>tune=-0.2</code>. When two or more sample data is contained, the arguments after the second can specify different value respectively.</p>
<dt><code>rate=</code><i>attack:decay:sustain:release1:release2:release3[,&#8230;]</i></p>
<dd>Sets the instrument&#8217;s ADSR rate. Each value may be an integer between <code>0</code> and <code>255</code>. When you set only sustain rate, </p>
<p> 6 GUS/hrpschrd.pat rate=::60 </p>
<p> is available. When you set only attack time fasten, </p>
<p> 6 GUS/hrpschrd.pat rate=255 </p>
<p> is available. When two or more sample data is contained, the arguments after the second can specify different value respectively.</p>
<dt><code>offset=</code><i>attack:decay:sustain:release1:release2:release3[,&#8230;]</i></p>
<dd>Sets the instrument&#8217;s ADSR offset. Each value may be an integer between <code>0</code> and <code>255</code>. The format is same as <code>rate=</code>.</p>
<dt><code>keep={loop|env}</code></p>
<dd>By default, percussion instruments have their loop and envelope information stripped. Strangely shaped envelopes are removed automatically from melodic instruments as well. <code>keep=</code> can be used to prevent stripping loop or envelope data. For example, the Short and Long Whistle percussion instruments (General Midi numbers 71 and 72) need to have `<code>keep=loop keep=env</code>&#8216; specified in the configuration file.</p>
<dt><code>strip={loop|env|tail}</code></p>
<dd>Force removal of loop or envelope information from all patches in the instrument, or strip the tail, i.e. all data after the loop. Some third-party instruments have garbage after the loop, as evidenced by a clicking noise whenever the instrument is played, so adding the <code>strip=tail</code> option will markedly improve sound quality.</p>
<dt><code>tremolo=</code><i>sweep_increment:control_ratio:depth[,&#8230;]</i></p>
<dd>Sets the instrument&#8217;s tremolo. Each value may be an integer between <code>0</code> and <code>255</code>. The format is similar to <code>rate=</code>. <i>sweep_increment</i> is the time until tremolo is started. <i>control_ratio</i> is the rate changing amplification. <i>depth</i> is the depth changing amplification.</p>
<dt><code>vibrato=</code><i>sweep_increment:phase_increment:depth[,&#8230;]</i></p>
<dd>Sets the instrument&#8217;s vibrato. Each value may be an integer between <code>0</code> and <code>255</code>. The format is similar to <code>rate=</code>. <i>sweep_increment</i> is the time until vibrato is started. <i>phase_increment</i> is the rate changing frequency. <i>depth</i> is the depth changing frequency.</p>
<dt><code>sclnote=</code><i>note[,&#8230;]</i></p>
<dd>Sets the instrument&#8217;s standard note for scale tuning. For example, <code>sclnote=60</code> causes the center note C to be standard note for scale tuning. When two or more sample data is contained, the arguments after the second can specify different value respectively.</p>
<dt><code>scltune=</code><i>tune[,&#8230;]</i></p>
<dd>Sets the instrument&#8217;s scale tuning factor in cents. For example, <code>scltune=50</code> causes the half tone steps as <code>50</code> cents. When two or more sample data is contained, the arguments after the second can specify different value respectively.</p>
<dt><code>comm=</code><i>comment</i></p>
<dd>Specifies the comment <i>comment</i>.</p>
<dt><code>modrate=</code><i>attack:decay:sustain:release1:release2:release3[,&#8230;]</i></p>
<dd>
<dt><code>modoffset=</code><i>attack:decay:sustain:release1:release2:release3[,&#8230;]</i></p>
<dd>Sets the instrument&#8217;s behavior of change of modulation envelope. The format and values are fundamentally same as volume envelope. Except for some SoundFonts, even if it specifies only the option, nothing happens.</p>
<dt><code>envkeyf=</code><i>attack:decay:sustain:release1:release2:release3[,&#8230;]</i></p>
<dd>Sets the instrument&#8217;s volume envelope key follow. Based on <code>note=60</code>, it changes envelope time according to note. The unit is +-cent/key. For example, <code>envkeyf=100</code> means that the attack time will double when it goes up by 1 octave. The format is similar to <code>rate=</code>. The parameter of <i>decay</i> and <i>sustain</i> may be preset in some SoundFont.</p>
<dt><code>envvelf=</code><i>attack:decay:sustain:release1:release2:release3[,&#8230;]</i></p>
<dd>Sets the instrument&#8217;s volume envelope velocity follow. Based on <code>velocity=64</code>, it changes envelope time according to velocity. The unit is +-cent/velocity. For example, <code>envvelf=100</code> means that the attack time will 38 times at <code>velocity=127</code>. The format is similar to <code>rate=</code>. In the future, the specification of this option may be changed.</p>
<dt><code>modkeyf=</code><i>attack:decay:sustain:release1:release2:release3[,&#8230;]</i></p>
<dd>Sets the instrument&#8217;s modulation envelope key follow. Based on <code>note=60</code>, it changes envelope time according to note. The unit is +-cent/key. For example, <code>modkeyf=100</code> means that the attack time will double when it goes up by 1 octave. The format is similar to <code>rate=</code>. The parameter of <i>decay</i> and <i>sustain</i> may be preset in some SoundFont.</p>
<dt><code>modvelf=</code><i>attack:decay:sustain:release1:release2:release3[,&#8230;]</i></p>
<dd>Sets the instrument&#8217;s modulation envelope velocity follow. Based on <code>velocity=64</code>, it changes envelope time according to velocity. The unit is +-cent/velocity. For example, <code>modvelf=100</code> means that the attack time will 38 times at <code>velocity=127</code>. The format is similar to <code>rate=</code>. In the future, the specification of this option may be changed.</p>
<dt><code>trempitch=</code><i>num[,&#8230;]</i></p>
<dd>Sets the instrument&#8217;s depth of changing pitch according to tremolo. The effect itself is same as vibrato, it uses to operate in another system. The unit is +-cent. The format is similar to <code>rate=</code>.</p>
<dt><code>tremfc=</code><i>num[,&#8230;]</i></p>
<dd>Sets the instrument&#8217;s depth of changing cutoff frequency according to tremolo. It can express the so-called glowl effect. The unit, etc. are same as <code>trempitch=</code>.</p>
<dt><code>modpitch=</code><i>num[,&#8230;]</i></p>
<dd>Sets the instrument&#8217;s depth of changing pitch according to modulation envelope. It can temporarily express raising pitch only for the attack stage. The unit, etc. are same as <code>trempitch=</code>.</p>
<dt><code>modfc=</code><i>num[,&#8230;]</i></p>
<dd>Sets the instrument&#8217;s depth of changing cutoff frequency according to modulation envelope. The unit, etc. are same as <code>trempitch=</code>.</p>
<dt><code>fc=</code><i>num[,&#8230;]</i></p>
<dd>Sets the instrument&#8217;s standard of cutoff frequency. The unit is Hz. The format is similar to <code>rate=</code>.</p>
<dt><code>q=</code><i>num[,&#8230;]</i></p>
<dd>Sets the instrument&#8217;s Q (resonance). The unit is cB. The format is similar to <code>rate=</code>.</p>
<dt><code>fckeyf=</code><i>num</i></p>
<dd>Sets the instrument&#8217;s filter key follow. Based on <code>note=60</code>, it change cutoff frequency according to note. The unit is +-cent/key. For example, <code>fckeyf=100</code> means that it changes same as pitch.</p>
<dt><code>fcvelf=</code><i>num</i></p>
<dd>Sets the instrument&#8217;s filter velocity follow. Based on <code>velocity=127</code>, it changes cutoff frequency according to velocity. The unit is +-cent. In SoundFont, <code>-2400</code> is set up as a characteristic value.</p>
<dt><code>qvelf=</code><i>num</i></p>
<dd>Sets the instrument&#8217;s resonance velocity follow. Based on <code>velocity=0</code>, it changes resonance according to velocity. The unit is +-cB.</dl>
</dl>
<dt><code>default </code><i>file</i></p>
<dd>When MIDI program appears, which is not mapped to instrument file, this file is pronounced as a substitute.</p>
<dt><code>map </code><i>MapID1 from-bank from-prog to-bank to-prog</i></p>
<dd>The existing tone is assigned as a tone of GS/XG each map. <code>gm2</code>, <code>sc55</code>, <code>sc88</code>, <code>sc88pro</code>, <code>sc8850, </code><code>xg</code> and <code>xgsfx64</code> can be specified to be <i>MapID1</i>.</p>
<dt><code>map </code><i>MapID2 from-drumset from-keynote to-drumset to-keynote</i></p>
<dd>The existing drum is assigned as a drum of GS/XG each map. <code>gm2drum</code>, <code>sc55drum</code>, <code>sc88drum</code>, <code>sc88prodrum</code>, <code>sc8850drum</code>, <code>xgdrum</code> and <code>xgsfx126</code> can be specified to be <i>MapID2</i>.</p>
<dt><code>soundfont </code><i>file [options]</i></p>
<dd>Read the whole SoundFont. <i>options</i> may be any of the following:</p>
<dl>
<dd>
<dl>
<dt><code>order=</code><i>number</i></p>
<dd>Sets the order of searching for instrument. When <code>order=0</code>, first read SoundFont, and then search for insufficient samples in GUS/patch. When <code>order=1</code>, after reading GUS/patch, search for SoundFont.</p>
<dt><code>amp=</code><i>amplification</i></p>
<dd>Sets the amplification of the whole SoundFont as <i>amplification</i>%. If the value is not specified, it is set by <code>100</code>%.</p>
<dt><code>cutoff=</code><i>number</i></p>
<dd>Specifies whether LPF in SoundFont is enable (<code>1</code>) or disable (<code>0</code>). If the value is not specified, it is considered to be enable.</p>
<dt><code>reso=</code><i>number</i></p>
<dd>Specifies whether resonance in SoundFont is enable (<code>1</code>) or disable (<code>0</code>). If the value is not specified, it is considered to be enable.</p>
<dt><code>remove</code></p>
<dd>Cancels the target SoundFont from the memory.</dl>
</dl>
<dt><code>font exclude </code><i>bank [prog [key]]</i></p>
<dd>Suppresses searching for SoundFont of <i>bank</i>, <i>prog</i>. If the sample is drumset, bank is <code>128</code>, drumset is <i>prog</i>, keynum is <i>key</i>.</p>
<dt><code>font order </code><i>number bank [prog [key]]</i></p>
<dd>Sets the order of searching for instrument individually. The format is same as <code>font exclude</code>.</dl>
<p> The following statements are available only latest <code>TiMidity++</code>.</p>
<dl>
<dt><code>#extension altassign </code><i>program1 program2 &#8230;</i></p>
<dd>Sets the alternate assign for drum set. For example, if you want to pronounce Hi-Hat cymbals (note number <code>42</code>, <code>44</code> and <code>46</code>) in the <code>drumset 0</code> exclusively to each others, specify: </p>
<p> drumset 0<br />
 altassign 42 44 46 </p>
<p> Note that alternate assign of <code>drumset 0</code> is used by default.</p>
<dt><code>#extension comm </code><i>program comment</i></p>
<dd>Specifies the comment <i>comment</i> for the tone number <i>program</i>. These comments are displayed in the indicator line when <code>TiMidity++</code> is booted with option <code>-int</code>, <code>-iTt</code>.</p>
<dt><code>#extension timeout </code><i>program second</i></p>
<dd>Specifies the time-out value of the <i>program</i>. If any notes played with the tone number <i>program</i> are suspended for more than <i>second</i> seconds, <code>TiMidity++</code> kills the notes.</p>
<dt><code>#extension copydrumset </code><i>drumset</i></p>
<dd>Copies all settings of the <i>drumset</i> to the current drumset.</p>
<dt><code>#extension copybank </code><i>bank</i></p>
<dd>Copies all settings of the <i>bank</i> to the current bank.</p>
<dt><code>#extension copymap </code><i>to-MapID from-MapID</i></p>
<dd>Copies all settings of the banks defined for the map <i>from-MapID</i> to the map <i>to-MapID</i>.</p>
<dt><code>#extension HTTPproxy </code><i>hostname:port</i></p>
<dd>Specifies the proxy of the HTTP protocol. <i>hostname</i> and <i>port</i><code> are of the proxy host&#8217;s.</p>
<dt>#extension FTPproxy </code><i>hostname:port</i></p>
<dd>Specifies the proxy of the FTP protocol. Same as HTTP.</p>
<dt><code>#extension mailaddr </code><i>your-mail-address</i></p>
<dd>Specifies user&#8217;s mail address. This address is sent to the FTP server if <code>TiMidity++</code> access any file via FTP.</p>
<dt><code>#extension opt </code><i>option</i></p>
<dd>Sets the value of boot-time options.</p>
<dt><code>#extension undef </code><i>progno</i></p>
<dd>Undefines the tone <i>progno</i> of current tone bank.</p>
<dt><code>#extension legato </code><i>progno </i><code>{0|1}</code></p>
<dd>Specifies whether legato is enable (<code>1</code>) or disable (<code>0</code>) on <i>progno</i>.</p>
<dt><code>#extension level </code><i>progno tva_level</i></p>
<dd>Sets the standard value of changing amplification when processing Drum Instrument TVA Level of NRPN. Unless Drum Instrument TVA Level is specified at playing, the amplification is not influenced. <i>progno</i> can carry out package specification by `,&#8217; and/or [<i>start</i>]-[<i>end</i>]. If start and end are omitted, they are assumed to be <code>0</code> and <code>127</code> respectively.</p>
<dt><code>#extension damper </code><i>progno </i><code>{0|1}</code></p>
<dd>Specifies whether redamper and half-damper are enable (<code>1</code>) or disable (<code>0</code>) on <i>progno</i>.</p>
<dt><code>#extension playnote </code><i>progno note</i></p>
<dd>Sets the frequency of pronounce to <code>note</code>. If the frequency of pronounce is specified by GS SysEx Play Note, the pitch is changed appropriately according to the value. <i>progno</i> can carry out package specification by `,&#8217; and/or [<i>start</i>]-[<i>end</i>]. If start and end are omitted, they are assumed to be <code>0</code> and <code>127</code> respectively. </p>
<p> For example:<br />
 drumset 0<br />
 #extension playnote -37,39,44-46,55-60</p>
<dt><code>#extension delaysend </code><i>progno level</i></p>
<dd>
<dt><code>#extension chorussend </code><i>progno level</i></p>
<dd>
<dt><code>#extension reverbsend </code><i>progno level</i></p>
<dd>Sets the send level when drum part effect is enable. All initial value are <code>127</code>. If one of delay, chorus and reverb is at least set up, the effect which is not set as the tone will become the initial value <code>0</code>. <i>progno</i> can carry out package specification by `,&#8217; and/or [<i>start</i>]-[<i>end</i>]. If start and end are omitted, they are assumed to be <code>0</code> and <code>127</code> respectively.</p>
<dt><code>#extension rnddelay </code><i>progno msec</i></p>
<dd>For every pronunciation, it is random and less than a maximum of <i>msec</i> delay. The distribution of random value is pink noise (1/f fluctuation) rather than a white noise.</dl>
<p> These <code>#extension</code> statements are beginning with character `#&#8217; that is the comment flag of old TiMidity (version 0.2i or earlier). So these statements are treated as comment line.<br />
 The latest <code>TiMidity++</code> treats <code>#extension</code> as white-space. So you can omit it. </p>
<p> If any file-name expression ended with character `|&#8217; (Ascii 0x7c), the file-name is treated as command and outputs of the command are also examined as arguments of statements.<br />
 <code>source</code> <i>command</i>| causes the output of <i>command</i> becomes the argument of <code>source</code>. It is convenient to choose settings of <code>TiMidity++</code> according to environment. In addition, if a space enters on the way like <i>command</i> |, it will be divided at the time of setting file reading, and will no longer be regarded as a command. This function is applicable to all the places that can specify a file name. </p>
<dl>
<dd>timidity &#8216;cat fild.mid|&#8217;</dl>
<p> will read from the output of cat fild.mid.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/timidity/timidity.cfg</code></p>
<dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-timidity/">timidity</a>(1), <a href="/docs/linux/man/1-lsmidiprog/">lsmidiprog</a>(1), <a href="/docs/linux/man/1-mididump/">mididump</a>(1), <a href="/docs/linux/man/1-patinfo/">patinfo</a>(1), <a href="/docs/linux/man/1-sf2text/">sf2text</a>(1), <a href="/docs/linux/man/1-wav2pat/">wav2pat</a>(1)</p>
<h2>Copyright</h2>
<p>Copyright (C) 1999-2004 Masanao Izumo &lt;iz [at] onicos.co.jp&gt;<br />
 Copyright (C) 1995 Tuukka Toivonen &lt;tt [at] cgs.fi&gt; </p>
<p> The original version was developed by Tuukka Toivonen &lt;tt [at] cgs.fi&gt; until the release of TiMidity-0.2i. His development was discontinued because of his being busy with work. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <i>GNU General Public License</i> as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the <i>GNU General Public License</i> for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA</p>
<h2>Availability</h2>
<p>The latest release is available on the <code>TiMidity++</code> Page, </p>
<p> URL <a rel="nofollow" href="http://www.timidity.jp/">http://www.timidity.jp/</a></p>
