---
title: "fmio(1)"
name: "fmio"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fmio/"
description: "fmio – small utility to manipulate fm radio card"
---

<h2>NAME</h2>
<p> <code>fmio</code> &#8211; small utility to manipulate fm radio card</p>
<h2>SYNOPSIS</h2>
<p> <code>fmio</code> [-<code>d </code><i>driver</i> ] [-<code>f </code><i>freq</i> ] [-<code>i</code> ] [-<code>m</code> ] [-<code>s</code> ] [-<code>v </code><i>vol</i> ] [-<code>x </code><i>vol</i> ] [-<code>X </code><i>vol</i> ]<br />
<code>fmio</code> [-<code>d </code><i>driver</i> ] &#8211;<code>S</code> [-<code>c </code><i>count</i> ] [-<code>l </code><i>begin</i> ] [-<code>h </code><i>end</i> ]<br />
<code>fmio</code> [-<code>d </code><i>driver</i> ] &#8211;<code>W </code><i>frequency</i><br />
<code>fmio</code> &#8211;<code>D</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>fmio</code> is a small program to set and change fm radio card parameters. </p>
<p> It sets frequency, volume of a card, reports signal strength on the working frequency and can set a radio card output to mono provided that the card driver supports it. </p>
<p> The <code>fmio</code> has two additional modes &#8211; scanning and detection. In the scan mode <code>fmio</code> scans frequency range with step 10 kHz and outputs measured signal strength. Frequency range and number of probes for each frequency are configurable. In the detection mode <code>fmio</code> detects any supported radio card. Use this mode if you are not sure which card you have or do not know which port your card uses. </p>
<p> Also, it can control the output volume of a sound card through /dev/mixer </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-d </code><i>driver</i></p>
<dd> Use driver <i>driver</i> See list of currently known drivers in section Sx DRIVERS . If no driver was specified, default one will be used.</p>
<dt><code>-f </code><i>freq</i></p>
<dd> Set fm card frequency (in MHz )</p>
<dt><code>-i</code></p>
<dd> Show all available information about a driver and a card.</p>
<dt><code>-m</code></p>
<dd> Set output of a card to mono. Works only in conjunction with option &#8211;<code>f</code> Note, that not all drivers support this option.</p>
<dt><code>-s</code></p>
<dd> Show current signal status of a radio card.</p>
<dt><code>-v </code><i>volume</i></p>
<dd> Set volume of a card. Option &#8211;<code>v </code><i>0</i> will mute a card. Each driver has its own maximal volume.</p>
<dt><code>-x </code><i>volume</i></p>
<dd> Set volume of an arbitrary mixer line of a sound card thru /dev/mixer The <i>volume</i> has following format: </p>
<blockquote><p><tt>&lt;line name&gt;=[+-]&lt;left channel&gt;,[+-]&lt;right channel&gt;.</tt></p></blockquote>
<p> For the line names see </p>
<blockquote><p><tt>under OpenBSD and NetBSD: /usr/include/sys/audioio.h </tt></p></blockquote>
<blockquote><p><tt>under Linux and FreeBSD: /usr/include/sys/soundcard.h </tt></p></blockquote>
<p> Some examples of the option &#8211;<code>x</code> usage are in the section Sx EXAMPLES below.</p>
<dt><code>-X </code><i>volume</i></p>
<dd> Set volume of the sound card master output through /dev/mixer Format of this option is similar to option &#8211;<code>x</code> except there is no need to specify &lt;line name&gt;.</p>
<dt><code>-D</code></p>
<dd> Detection mode. All known cards will be probed and results will be printed to standard output. Note, this procedure is very slow.</p>
<dt><code>-S</code></p>
<dd> Scan mode. If some of the listed below parameters were not specified the FM maximal and minimal frequencies are used. Measured data is dumped to standard output.</p>
<dt><code>-l </code><i>begin</i></p>
<dd> Lower border of scan range (in MHz ) If it is less than the FM minimal frequency (87.5 MHz , ) it is set to the FM minimal frequency.</p>
<dt><code>-h </code><i>end</i></p>
<dd> Upper border of scan range (in MHz ) If it is greater than the FM maximal frequency (108.0 MHz , ) it is set to the FM maximal frequency.</p>
<dt><code>-c </code><i>count</i></p>
<dd> Number of probes for each frequency. The higher this number is the more precise will be results. Since stereo signal has weight 3, none &#8211; weight 0 and mono is in between, the strongest signal will have value 3 * <i>count</i> If not set, each frequency will be probed only once.</p>
<dt><code>-W </code><i>frequency</i></p>
<dd> Search mode. Nearest to <i>frequency</i> station is searched and, if found, tuned to. The search direction is determined by <i>frequency</i> sign. If <i>frequency</i> has negative value, the station is searched downward. If <i>frequency</i> is positive the search is performed upward.</dl>
<h2>DRIVERS</h2>
<p> <i>Aztech/PackardBell FM Radio Card</i> (ISA) `az&#8217; </p>
<blockquote><p><tt>port 0x350 - az1</tt></p></blockquote>
<blockquote><p><tt>port 0x358 - az2</tt></p></blockquote>
<blockquote><p><tt>Volume - 0 .. 3</tt></p></blockquote>
<blockquote><p><tt>Can set mono - yes</tt></p></blockquote>
<blockquote><p><tt>Software search</tt></p></blockquote>
<p> <i>Brooktree Bt848 Driver</i> `bktr&#8217; </p>
<blockquote><p><tt>Volume - 0 .. 1</tt></p></blockquote>
<blockquote><p><tt>Can set mono - yes</tt></p></blockquote>
<blockquote><p><tt>Software search</tt></p></blockquote>
<blockquote><p><tt>Use with </tt><code>bktrctl</code> </p></blockquote>
<p> <i>BMC FM Radio Card</i> (ISA) `bmc&#8217; </p>
<blockquote><p><tt>port 0x20F - bmc1</tt></p></blockquote>
<blockquote><p><tt>port 0x30F - bmc2</tt></p></blockquote>
<blockquote><p><tt>Volume - 0 .. 15</tt></p></blockquote>
<blockquote><p><tt>Can set mono - yes</tt></p></blockquote>
<blockquote><p><tt>Search not implemented yet</tt></p></blockquote>
<p> <i>BSD Radio Driver</i> `br&#8217; </p>
<blockquote><p><tt>Volume - 0 .. 255</tt></p></blockquote>
<blockquote><p><tt>Can set mono - yes</tt></p></blockquote>
<blockquote><p><tt>Software search</tt></p></blockquote>
<p> <i>EcoRadio Card</i> (ISA) `er&#8217; </p>
<blockquote><p><tt>port 0x316 - er1</tt></p></blockquote>
<blockquote><p><tt>port 0x336 - er2</tt></p></blockquote>
<blockquote><p><tt>Volume - 0 .. 3</tt></p></blockquote>
<blockquote><p><tt>Can set mono - no</tt></p></blockquote>
<blockquote><p><tt>Search not implemented yet</tt></p></blockquote>
<blockquote><p><tt>Detection not implemented yet</tt></p></blockquote>
<p> <i>Gemtek FM Radio Card</i> (ISA) `gti&#8217; </p>
<blockquote><p><tt>port 0x20c - gti1</tt></p></blockquote>
<blockquote><p><tt>port 0x30c - gti2</tt></p></blockquote>
<blockquote><p><tt>port 0x24c - gti3</tt></p></blockquote>
<blockquote><p><tt>port 0x34c - gti4</tt></p></blockquote>
<blockquote><p><tt>port 0x248 - gti5</tt></p></blockquote>
<blockquote><p><tt>Volume - 0 .. 1</tt></p></blockquote>
<blockquote><p><tt>Can set mono - no</tt></p></blockquote>
<blockquote><p><tt>Software search</tt></p></blockquote>
<p> <i>Gemtek FM Radio Card</i> (PCI) `gtp&#8217; </p>
<blockquote><p><tt>Volume - 0 .. 1</tt></p></blockquote>
<blockquote><p><tt>Can set mono - yes</tt></p></blockquote>
<blockquote><p><tt>Hardware search</tt></p></blockquote>
<p> <i>AIMS Lab Highway Xtreme TV card</i> <i>with FM tuner Driver</i> `hx&#8217; </p>
<blockquote><p><tt>Volume - 0 .. 1</tt></p></blockquote>
<blockquote><p><tt>Can set mono - yes</tt></p></blockquote>
<blockquote><p><tt>Software search</tt></p></blockquote>
<blockquote><p><tt>BSD only</tt></p></blockquote>
<blockquote><p><tt>Use with </tt><code>bktrctl</code> </p></blockquote>
<blockquote><p><tt>Needs kernel with `option' </tt></p></blockquote>
<p> BT848_GPIO_ACCESS </p>
<p> <i>Guillemot MaxiRadio FM 2000 Radio Card</i> (PCI) `mr&#8217; </p>
<blockquote><p><tt>Volume - 0 .. 1</tt></p></blockquote>
<blockquote><p><tt>Can set mono - yes</tt></p></blockquote>
<blockquote><p><tt>Hardware search</tt></p></blockquote>
<p> <i>AIMS Lab RadioTrack/RadioReveal RA300 FM Radio Card</i> (ISA) `rt&#8217; </p>
<blockquote><p><tt>port 0x20c - rt1</tt></p></blockquote>
<blockquote><p><tt>port 0x30c - rt2</tt></p></blockquote>
<blockquote><p><tt>Volume - 0 .. 10</tt></p></blockquote>
<blockquote><p><tt>Can set mono - yes</tt></p></blockquote>
<blockquote><p><tt>Software search</tt></p></blockquote>
<p> <i>AIMS Lab RadioTrack II FM Radio Card</i> (ISA) `rtII&#8217; </p>
<blockquote><p><tt>port 0x20c - rtII1</tt></p></blockquote>
<blockquote><p><tt>port 0x30c - rtII2</tt></p></blockquote>
<blockquote><p><tt>Volume - 0 .. 1</tt></p></blockquote>
<blockquote><p><tt>Can set mono - yes</tt></p></blockquote>
<blockquote><p><tt>Hardware search</tt></p></blockquote>
<p> <i>SoundForte Awesome 64R SF64-PCE2 Driver</i> (PCI) `sae&#8217; </p>
<blockquote><p><tt>Volume - 0 .. 1</tt></p></blockquote>
<blockquote><p><tt>Can set mono - yes</tt></p></blockquote>
<blockquote><p><tt>Hardware Search</tt></p></blockquote>
<p> <i>SoundForte Legacy 128 SF16-FMD2 Driver</i> (ISA) `sf2d&#8217; </p>
<blockquote><p><tt>port 0x284 - sf2d1</tt></p></blockquote>
<blockquote><p><tt>port 0x384 - sf2d2</tt></p></blockquote>
<blockquote><p><tt>Volume - 0 .. 1</tt></p></blockquote>
<blockquote><p><tt>Can set mono - yes</tt></p></blockquote>
<blockquote><p><tt>Search not implemented yet</tt></p></blockquote>
<blockquote><p><tt>Detection not implemented yet</tt></p></blockquote>
<p> <i>SoundForte RadioX SF16-FMI Driver</i> (ISAPNP) `sfi&#8217; </p>
<blockquote><p><tt>Also known as Creative ViBRA 16c PnP</tt></p></blockquote>
<blockquote><p><tt>port 0x284 - sfi1</tt></p></blockquote>
<blockquote><p><tt>port 0x384 - sfi2</tt></p></blockquote>
<blockquote><p><tt>Volume - 0 .. 1</tt></p></blockquote>
<blockquote><p><tt>Can set mono - no</tt></p></blockquote>
<blockquote><p><tt>Search not implemented yet</tt></p></blockquote>
<blockquote><p><tt>Detection not implemented yet</tt></p></blockquote>
<p> <i>SoundForte RadioLink SF16-FMR FM Radio Card</i> (ISA) `sfr&#8217; </p>
<blockquote><p><tt>port 0x284 - sfr1</tt></p></blockquote>
<blockquote><p><tt>port 0x384 - sfr2</tt></p></blockquote>
<blockquote><p><tt>Volume - 0 .. 15</tt></p></blockquote>
<blockquote><p><tt>Can set mono - no</tt></p></blockquote>
<blockquote><p><tt>Use with </tt><code>fmrinit</code> </p></blockquote>
<blockquote><p><tt>Search not implemented yet</tt></p></blockquote>
<p> <i>SoundForte RadioLink SF16-FMR2 FM Radio Card</i> (ISA) `sf2r&#8217; </p>
<blockquote><p><tt>Volume - 0 .. 1</tt></p></blockquote>
<blockquote><p><tt>Can set mono - yes</tt></p></blockquote>
<blockquote><p><tt>Hardware search</tt></p></blockquote>
<p> <i>SoundForte RadioLink SF64-PCR FM Radio Card</i> (PCI) `sf4r&#8217; </p>
<blockquote><p><tt>Volume - 0 .. 1</tt></p></blockquote>
<blockquote><p><tt>Can set mono - yes</tt></p></blockquote>
<blockquote><p><tt>Software search</tt></p></blockquote>
<p> <i>Spase PCRadio Card</i> (ISA) `sp&#8217; </p>
<blockquote><p><tt>port 0x1b0 - sp1</tt></p></blockquote>
<blockquote><p><tt>port 0x1f0 - sp2</tt></p></blockquote>
<blockquote><p><tt>port 0x278 - sp3</tt></p></blockquote>
<blockquote><p><tt>port 0x378 - sp4</tt></p></blockquote>
<blockquote><p><tt>port 0x2f8 - sp5</tt></p></blockquote>
<blockquote><p><tt>port 0x3bc - sp6</tt></p></blockquote>
<blockquote><p><tt>Volume - 0 .. 63</tt></p></blockquote>
<blockquote><p><tt>Can set mono - yes </tt></p></blockquote>
<blockquote><p><tt>Search not implemented yet</tt></p></blockquote>
<p> <i>SoundForte Quad X-treme SF256-PCP-R Driver</i> (PCI) `sqx&#8217; </p>
<blockquote><p><tt>Volume - 0 .. 1</tt></p></blockquote>
<blockquote><p><tt>Can set mono - yes</tt></p></blockquote>
<blockquote><p><tt>Hardware search</tt></p></blockquote>
<p> <i>SoundForte Theatre X-treme 5.1 SF256-PCS-R Driver</i> (PCI) `stx&#8217; </p>
<blockquote><p><tt>Volume - 0 .. 1</tt></p></blockquote>
<blockquote><p><tt>Can set mono - yes</tt></p></blockquote>
<blockquote><p><tt>Hardware search</tt></p></blockquote>
<p> <i>Sound Vision 16 Gold Sound Card with FM Radio</i> (ISA) `svg&#8217; </p>
<blockquote><p><tt>Volume - 0 .. 1</tt></p></blockquote>
<blockquote><p><tt>Can set mono - no</tt></p></blockquote>
<blockquote><p><tt>Software search</tt></p></blockquote>
<p> <i>Trust FM Radio Card</i> (ISA) `tr&#8217; </p>
<blockquote><p><tt>Volume - 0 .. 63</tt></p></blockquote>
<blockquote><p><tt>Can set mono - yes</tt></p></blockquote>
<blockquote><p><tt>Software search</tt></p></blockquote>
<p> <i>Terratec FM Radio Card</i> (ISAPNP) `tt&#8217; </p>
<blockquote><p><tt>Volume - 0 .. 7</tt></p></blockquote>
<blockquote><p><tt>Can set mono - yes</tt></p></blockquote>
<blockquote><p><tt>Hardware search</tt></p></blockquote>
<p> <i>Video4Linux Driver</i> `v4l&#8217; </p>
<blockquote><p><tt>Volume - 0 .. 10</tt></p></blockquote>
<blockquote><p><tt>Can set mono - yes</tt></p></blockquote>
<blockquote><p><tt>Software search</tt></p></blockquote>
<p> <i>Zoltrix RadioPlus 108 FM Radio Card</i> (ISA) `zx&#8217; </p>
<blockquote><p><tt>port 0x20c - zx1</tt></p></blockquote>
<blockquote><p><tt>port 0x30c - zx2</tt></p></blockquote>
<blockquote><p><tt>Volume - 0 .. 16</tt></p></blockquote>
<blockquote><p><tt>Can set mono - yes</tt></p></blockquote>
<blockquote><p><tt>Software search</tt></p></blockquote>
<h2>EXAMPLES</h2>
<dl>
<dt><code>Set frequency to 104.5 MHz:</code></p>
<dd>
<blockquote>
<pre>
# fmio -f 104.5
</pre>
</blockquote>
<dt><code>Set frequency to 104.5 MHz and show signal state on this frequency:</code></p>
<dd>
<blockquote>
<pre>
# fmio -f 104.5 -s
</pre>
</blockquote>
<dt><code>Set frequency to 104.5 MHz, hardware volume to 4:</code></p>
<dd>
<blockquote>
<pre>
# fmio -v 4 -f 104.5
</pre>
</blockquote>
<dt><code>Set volume of both channels of line input to 9:</code></p>
<dd>
<blockquote>
<pre>
# fmio -x line=9
</pre>
</blockquote>
<dt><code>For line1, increase volume of left channel by 2, set volume of right channel</code></p>
<dd> to 10: </p>
<blockquote>
<pre>
# fmio -x line1=+2,10
</pre>
</blockquote>
<dt><code>For master output, increase volume of left channel by 2 and decrease volume</code></p>
<dd> of right channel by 1: </p>
<blockquote>
<pre>
# fmio -X +2,-1
</pre>
</blockquote>
<dt><code>Decrease volume of both channels by 2:</code></p>
<dd>
<blockquote>
<pre>
# fmio -X -2
</pre>
</blockquote>
<dt><code>Scan range [100.0&#8230;107.6] using driver</code></p>
<dd> `bktr&#8217; </p>
<blockquote>
<pre>
# fmio -d bktr -S -l 100.0 -h 107.6
</pre>
</blockquote>
<dt><code>Search station below 104.3 MHz using driver</code></p>
<dd> `sf2r&#8217; </p>
<blockquote>
<pre>
# fmio -d sf2r -W -104.3
</pre>
</blockquote>
<dt><code>Detect all available cards:</code></p>
<dd>
<blockquote>
<pre>
# fmio -D
</pre>
</blockquote>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>/dev/mixer </code></p>
<dd> mixer audio device</p>
<dt><code>/dev/tuner </code></p>
<dd> radio tuner device used by the BSD bktr driver.</p>
<dt><code>/dev/radio </code></p>
<dd> radio tuner device used by `v4l&#8217; driver (Linux) and `br&#8217; driver (OpenBSD and NetBSD)</dl>
<h2>ENVIROMENT</h2>
<p> The following environment variables affect the execution of <code>fmio</code></p>
<dl>
<dt><code>FMTUNER</code></p>
<dd> The driver that should be used as default.</p>
<dt><code>RADIODEVICE</code></p>
<dd> The radio tuner device (OpenBSD, NetBSD and Linux)</p>
<dt><code>MIXERDEVICE</code></p>
<dd> The audio mixer device to use.</dl>
<h2>BUGS</h2>
<p> Frequency and hardware volume should be absolute. They cannot be increased or decreased relatively to the current value. </p>
<p> The Gemtek PCI card implementation has some flaw. Namely, when turning a card off, don&#8217;t use option &#8211;<code>f</code> </p>
<p> The SF16-FMR card has 16 volume levels. Thus, <code>fmio -f 104.5</code> can be easily taken in as <code>fmio -v 0</code> Use some volume level when setting up a frequency. Also, this card has to be initialized during bootup. Launch <code>fmrinit</code> from some start script (most likely /etc/rc.local ) </p>
<p> There&#8217;s a flaw in the BSD bktr driver &#8211; after closing /dev/tuner a card is turned off too. Thus, you cannot use <code>fmio</code> alone to manage bktr cards because <code>fmio</code> opens /dev/tuner tunes a card to some frequency and closes /dev/tuner &#8211; and a card is turned off. Since <code>fmio</code> cannot hold /dev/tuner open all the time, use it with <code>bktrctl</code> The same concerns Linux users. Some cards supported by kernel are turned off after closing /dev/radio (e.g. <code>USB tuners</code> ) Use <code>fmio</code> with <code>bktrctl</code> </p>
<p> Due to the above limitation the BSD bktr driver cannot work correctly if frequency was not specified. E.g. <code>fmio -d bktr -i</code> will not work as expected. Correct use is <code>fmio -d bktr -f &lt;some freq&gt; -i</code></p>
<h2>AUTHOR</h2>
<p> Vladimir Popov Aq jumbo [at] narod.ru </p>
<h2>Index</h2>
