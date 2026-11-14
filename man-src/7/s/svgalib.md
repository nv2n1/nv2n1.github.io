---
title: "svgalib(7)"
name: "svgalib"
section: "7"
letter: "s"
url: "/docs/linux/man/7-svgalib/"
description: "svgalib.mach32 – Information on the Mach32 chipset driver"
---

<p>svgalib.mach32 &#8211; Information on the Mach32 chipset driver</p>
<h2>Table Of Contents</h2>
<p><code> 0. </code>Introduction<br />
 <code> 1. </code>Specifying pixel clocks<br />
 <code> 2. </code>Copyrights<br />
 <code> 3. </code>The mach32info utility<br />
 <code> 4. </code>Third party cards<br />
 <code> 5. </code>Logical line width<br />
 <code> 6. </code>Noisy video signals<br />
 <code> 7. </code>The configuration EEPROM<br />
 <code> 8. </code>EEPROM woes<br />
 <code> 9. </code>The Mach32Eeprom command<br />
 <code>10. </code>Setup of the memory aperture (linear framebuffer)<br />
 <code>11. </code>Accelerator support and other weird features<br />
 <code>12. </code>Ramdacs<br />
 <code>13. </code>Meaning of the detection message from svgalib<br />
 <code>14. </code>Conclusions</p>
<h2>0. Introduction</h2>
<p>The driver should allow you to use any of the graph-modes your Mach32 card supports. Note that there is no support for &lt;8bpp modes and that I won&#8217;t ever implement that because I don&#8217;t see any reason for doing so. All standard VGA-modes are supported, of course (by using the standard VGA driver routines). </p>
<p> If you configured your Mach32 for a memory aperture and it is at least as big as the memory of your card (that is, not a 1MB memory aperture for a 2MB card) support for linear frame buffer access of svgalib is given. </p>
<p> Auto detection of the Mach32 seems not to work on all cards. That&#8217;s really strange since I got the code from the X people. It should be OK regardless of my docs. Well, I fixed that (hopefully). Actually the bug was found by Daniel Lee Jackson (djackson [at] ichips.intel.com). (Thanks again.. It was so silly&#8230; I would have never found it) If you still have problems just put a chipset Mach32 in your config file.</p>
<h2>1. Specifying Pixel Clocks</h2>
<p><code>WARNING!</code> The Mach32 driver needs to know correct clock frequencies for graceful DAC configuration. Wrong clocks may damage your card! However, this version contains code for automatic clock detection. Since clock detection is time critical, please do it on a completely idle system. Then put the printed out <code>clocks</code> line in your <code><a href="/docs/linux/man/5-libvga-config/">libvga.config</a></code>(5) file. </p>
<p> The driver tries to do this for you. After that, you can restart whatever svgalib program you used and you are set. If you already put a <code>clocks</code> line in your config by hand, comment it out to have the driver check your clocks. </p>
<p> Since clock probing is time critical, values differ from time to time, you may try it multiple times and see which values seem to be most exact. You can also compare them with the standard clock chips for Mach32 cards in <code><a href="/docs/linux/man/5-libvga-config/">libvga.config</a></code>(5)). </p>
<p> The clock probing relies on the 7th clock being 44.9MHz as this is what Xfree does. If this is not true (and it is not always), probing is hosed. See <code><a href="/docs/linux/man/5-libvga-config/">libvga.config</a></code>(5) for a list of the <code>clocks</code> used by common svgalib cards.</p>
<h2>2. Copyrights</h2>
<p>Some tiny routines are copied from Xfree86. The clock detection code is almost just copied. So I repeat the copyright statements for these parts here: </p>
<p> Copyright 1992 by Orest Zborowski &lt;obz [at] Kodak.com&gt;<br />
 Copyright 1993 by David Wexelblat &lt;dwex [at] goblin.org&gt; </p>
<p> Permission to use, copy, modify, distribute, and sell this software and its documentation for any purpose is hereby granted without fee, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation, and that the names of Orest Zborowski and David Wexelblat not be used in advertising or publicity pertaining to distribution of the software without specific, written prior permission. Orest Zborowski and David Wexelblat make no representations about the suitability of this software for any purpose. It is provided &quot;as is&quot; without express or implied warranty. </p>
<p> <code>Orest Zborowski and David Wexelblat disclaim all warranties with regard </code> <code>to this software, including all implied warranties of merchantability and </code> <code>fitness, in no event shall Orest Zborowski or David Wexelblat be liable </code> <code>for any special, indirect or consequential damages or any damages </code> <code>whatsoever resulting from loss of use, data or profits, whether in an </code> <code>action of contract, negligence or other tortious action, arising out of </code> <code>or in connection with the use or performance of this software.</code> </p>
<p> Copyright 1990,91 by Thomas Roell, Dinkelscherben, Germany.<br />
 Copyright 1993 by Kevin E. Martin, Chapel Hill, North Carolina. </p>
<p> Permission to use, copy, modify, distribute, and sell this software and its documentation for any purpose is hereby granted without fee, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation, and that the name of Thomas Roell not be used in advertising or publicity pertaining to distribution of the software without specific, written prior permission. Thomas Roell makes no representations about the suitability of this software for any purpose. It is provided &quot;as is&quot; without express or implied warranty. </p>
<p> <code>Thomas Roell, Kevin E. Martin, and Rickard E. Faith disclaim all</code> <code>warranties with regard to this software, including all implied</code> <code>warranties of merchantability and fitness, in no event shall the authors</code> <code>be liable for any special, indirect or consequential damages or any</code> <code>damages whatsoever resulting from loss of use, data or profits, whether</code> <code>in an action of contract, negligence or other tortious action, arising</code> <code>out of or in connection with the use or performance of this software.</code> </p>
<p> Author: Thomas Roell, roell [at] informatik.tu-muenchen.de </p>
<p> Rewritten for the 8514/A by Kevin E. Martin (martin [at] cs.unc.edu)<br />
 Modified for the Mach-8 by Rickard E. Faith (faith [at] cs.unc.edu)<br />
 Rewritten for the Mach32 by Kevin E. Martin (martin [at] cs.unc.edu) </p>
<p> And here is my own copyright: </p>
<p> This driver is free software; you can redistribute it and/or modify it without any restrictions. This library is distributed in the hope that it will be useful, but without any warranty. </p>
<p> Copyright 1994 by Michael Weller </p>
<p> Email addresses as of this writing: </p>
<p> eowmob [at] exp-math.uni-essen.de mat42b [at] spi.power.uni-essen.de </p>
<p> <code>Michael Weller disclaims all warranties with regard</code> <code>to this software, including all implied warranties of merchantability and</code> <code>fitness, in no event shall Michael Weller be liable</code> <code>for any special, indirect or consequential damages or any damages</code> <code>whatsoever resulting from loss of use, data or profits, whether in an</code> <code>action of contract, negligence or other tortious action, arising out of</code> <code>or in connection with the use or performance of this software.</code></p>
<h2>3. The Mach32Info Utility</h2>
<p>The <code><a href="/docs/linux/man/6-mach32info/">mach32info</a></code>(6) utility or demo reads out all configuration registers and the configuration EEPROM of your Mach32 card. If there is a problem with the particular card you have, compile and run the utility in the <i>mach32/</i> directory of the svgalib distribution and send it&#8217;s stdout to me This might also be useful if you need a lot of options (e.g. clocks on new models?) to get it to work so that this can be done automatically in future versions.</p>
<h2>4. Third Party Cards</h2>
<p>I got a few reports about AST systems with onboard Mach32. They do feature an incompatible EEPROM setup, but I think I got around that. Nevertheless the Mach32 chipset driver doesn&#8217;t work out of the box on any AST system I heard of. </p>
<p> Since original ATI Mach32 demos and tools don&#8217;t work as well, I&#8217;ve to claim that the Mach32 on these AST systems does not conform to ATI&#8217;s Mach32 docs. Fortunately, Vernon C. Hoxie &lt;vern [at] zebra.alphacdc.com&gt; found a work around after years (really!) of investigating. AST Mach32 seems to work now. The work around was also submitted to Xfree and will be incorporated to allow running it on the AST hardware too in recent versions. Please read on the <code>misc_ctl</code> command below. </p>
<p> Dell users should have a look at the <code>vendor</code>, <code>ramdac</code>, and <code>svgaclocks</code> commands below (if they have problems with the default settings).</p>
<h3>Commands to support third party cards</h3>
<p>I had to learn that those cards seem to use not only non standard clocks for the Mach32, but also for the included SVGA. However, since people often like to use proprietary, non standard VGA (read 80&#215;25) text modes, the Mach32 driver has to set the included SVGA to a VGA compatible clock frequency. Otherwise svgalib has problems using plain VGA modes. This screws VGA modes up if these clocks have different values on third party Mach32 cards. </p>
<dl>
<dt><code>svgaclocks </code><i>n</i></p>
<dd>with <i>n</i> a number between <code>0</code> and <code>31</code> to select the svga clocks to be used in vga modes. The bits of <i>n</i> refer to specific ATI register bits to complicated to explain here. Even if I would, I can&#8217;t tell which clocks they would select on your third party card (which is the actual problem) </p>
<p> <code>svgaclocks 9</code> is the default setting and correct for original ATI cards. </p>
<p> Often <code>svgaclocks 0</code> (Dell cards) works.</p>
<dt><code>svgaclocks keep</code></p>
<dd>is special in that the driver will not touch any SVGA timings. This requires the Mach32 SVGA part to be in a VGA compatible mode when the svgalib application is started, that is, you must use 80&#215;25 (maybe 80&#215;50) console text modes.</dl>
<p> As I mentioned already, Vernon C. Hoxie &lt;vern [at] zebra.alphacdc.com&gt; really seems to have located the reason for the Mach32 AST problems. Any access to <code>MISC_CTL</code> locks up the card &amp; system. Fortunately <code>MISC_CTL</code> is only used for some DAC fine tuning (actually the setting you can fine tune with the <code>blank</code> command) which is only of barely noticeable effect to the screen. </p>
<p> The following configuration commands exist to support AST cards: </p>
<dl>
<dt><code>misc_ctl keep-off</code></p>
<dd>Do not dare to touch MISC_CTL.</p>
<dt><code>misc_ctl use</code></p>
<dd>Use it for fine tuning of the Ramdac setup (default).</dl>
<p> Finally, for your convenience there exist: </p>
<dl>
<dt><code>vendor ati</code></p>
<dd>
<dt><code>vendor dell</code></p>
<dd>
<dt><code>vendor ast</code></p>
<dd>These are macros that expand to settings for <code>svgaclocks</code>, <code>ramdac</code>, <code>misc_ctl</code>, and <code>mach32eeprom</code> that are usually correct for ATI, Dell, AST cards. Be aware that they really work like macros. That is, they override any setting of <code>svgaclocks</code>, <code>ramdac</code>, <code>misc_ctl</code>, and <code>mach32eeprom</code> made before them and individual aspects will be changed by a following <code>svgaclocks</code>, <code>ramdac</code>, <code>misc_ctl</code>, and <code>mach32eeprom</code> command. </p>
<p> Note that the <code>mach32eeprom ignore</code> required for some Dell cards requires you to include explicit timings for Mach32 modes other than 640x480x256. The <i>mach32/mach32.std-modes</i> file in the svgalib distribution contains recommendations for modes from ATI. </p>
<p> I heard about a bug in some ATI chipsets returning wrong memory amounts configs. (But cannot confirm that) </p>
<p> You can enforce correct chipset identification from the configuration file: </p>
<dt><code>chipset Mach32 </code><i>chiptype memory</i></p>
<dd>where <i>chiptype</i> is the sum of at exactly one value from each of the following two groups </p>
<dl>
<dd>
<dl>
<dt><code>128</code></p>
<dd>use no memory aperture.</p>
<dt><code>160</code></p>
<dd>use a 1MB memory aperture.</p>
<dt><code>192</code></p>
<dd>use a 4MB memory aperture.</p>
<dt><code>0</code></p>
<dd>choose size for the memory aperture automatically.</dl>
<p> and </p>
<dl>
<dt><code>16</code></p>
<dd>Ramdac is of type 0 (ATI68830)</p>
<dt><code>17</code></p>
<dd>Ramdac is of type 1 (IMS-G173, SC11486)</p>
<dt><code>18</code></p>
<dd>Ramdac is of type 2 (ATI68875, TLC34075)</p>
<dt><code>19</code></p>
<dd>Ramdac is of type 3 (INMOS176, INMOS178)</p>
<dt><code>20</code></p>
<dd>Ramdac is of type 4 (Bt481, Bt482)</p>
<dt><code>21</code></p>
<dd>Ramdac is of type 5 (ATI68860)</p>
<dt><code>0</code></p>
<dd>Ramdac type is queried from Mach32 chip.</dl>
</dl>
<dd><i>memory</i> is the amount of video memory in KB.</dl>
<p> Note that the type of the ramdac can be set more conveniently with the <code>ramdac</code> command.</p>
<h2>5. Logical Linewidth</h2>
<p>At least my VRAM card seems to be very peculiar about logical line widths. From my experience a multiple of 64 pels is needed. Your mileage may vary. Use the config file options to adjust it and tell me if your card needs a different value. Include the name and model number of the card and what the correct numbers should be. This is so that I can correct the auto configuration of the driver. </p>
<p> If some svgalib application has problems, note that you can force the logical line width to the default value from the config file. Probably this will lead to glitches in some 800&#215;600 resolutions. You can <code>inhibit</code> these resolutions from the config file as well. Apropos glitches, I found no guidelines as to what clock rates to use due to memory restrictions. I adjusted the driver, such that I get a stable pic in all resolutions. However sometimes the screen is disturbed by heavy video memory accesses. If you don&#8217;t like that, reduce the clocks used with the maxclock16 or maxclock24 command, resp. This may of course lead to none of the predefined modes being used. Then you can try to define your own mode via the define command.</p>
<h2>6. Noisy Video Signals</h2>
<p>If you get some flicker or heavy noise on your screen, some fine tuning may be needed. My docs didn&#8217;t give me hints as to what each card can stand. Especially DRAM cards may give problems (I&#8217;ve VRAM). In that case, use the fine tuning config commands and send me your results along with the output of <code><a href="/docs/linux/man/6-mach32info/">mach32info</a></code>(6). Then I can include them in my next release.</p>
<h3>Fine-tuning configuration commands</h3>
<p>First you should think about the <code>maxclock*</code> configuration commands to reduce pixel clocks used for each color depth. </p>
<p> Especially important for DRAM cards is the video FIFO depth used to queue memory values for writing to the screen. Here is a command to set this value for the 8bpp modes: </p>
<dl>
<dt><code>vfifo8 </code><i>number</i></p>
<dd>where <i>number is in range</i> <code>0</code> &#8211; <code>15</code>. The default is now 6. </p>
<p> Since vfifo is of some impact to the speed of the card, tell me the lowest setting that satisfies your card. </p>
<p> For 16/24/32 modes, there are non-zero values preset from internal tables and the EEPROM, however you can enforce minimal vfifo values with:</dl>
<p> <code>vfifo16 </code><i>number</i><br />
 <code>vfifo24 </code><i>number</i><br />
 <code>vfifo32 </code><i>number</i> </p>
<dl>
<dt><code>blank </code><i>number</i></p>
<dd>where <i>number</i> is <code>4 * </code><i>pixel_delay</i><code> + </code><i>blank_adjust</i> where <i>pixel_delay</i> and <i>blank_adjust</i> are in range <code>0</code> .. <code>3</code>. <i>pixel_delay</i> delays pixels before they are sent to the DAC and <i>blank_adjust</i> adjusts the blank pulse for type 2 DAC&#8217;s. <code>blank</code> should be set correctly for each DAC type automatically. So use it only as a last resort. </p>
<dt><code>latch </code><i>number</i></p>
<dd>where <i>number</i> is the sum of zero or more of the following numbers:</p>
<dl>
<dd>
<dl>
<dt><code>128</code></p>
<dd>VRAM serial delay latch enable, DRAM latch bits 63 &#8211; 0 enable.</p>
<dt><code>4096</code></p>
<dd>Latch video memory data.</p>
<dt><code>8192</code></p>
<dd>Memory data delay latch enable for data bits 63 &#8211; 0.</p>
<dt><code>16384</code></p>
<dd>Memory full clock pulse enable.</dl>
</dl>
<dd>Default is to switch all settings on (they are on on my card by default anyway).</dl>
<p> Note that these commands may vanish again once they are no longer needed for debugging purposes. </p>
<p> There is no 320&#215;200 mode in the EEPROM of the Mach32 at all, however I defined one in the default configuration file for you. This is the best thing I could get up on my card/screen. Note that it will probably have big borders on your screen, and black lines in between the pixel lines. This is because of the lack of low clocks &lt; 16MHz on the Mach32 and the lack of a line doubling mode as VGA has. The Mach32 is not intended for such low resolutions. If you find a better mode or have an idea, please let me know. You can also just remove my timings from the default configuration file.</p>
<h2>7. The Configuration Eeprom</h2>
<p>Ah yes, about the EEPROM, I figured out how to read out the Mach32 EEPROM. I did it by disassembling the BIOS routine mentioned in the docs. I then redid it in C. The driver will use everything it finds there. </p>
<p> Use the Mach32 install tools (they should have reached you together with your Mach32 VGA card) to setup your card/monitor combo correctly. The <code>monitors</code> setting from the config file (or default of 35kHz or something) will be obeyed by the driver nevertheless (for safety!). </p>
<p> As you probably know already, accessing the EEPROM causes some screen flickering. If this annoys you (or even worse your monitor) have a look at the <code>mach32eeprom</code> command described below. This allows you to put the data from the EEPROM into a file and which can be read whenever it is required. </p>
<p> Don&#8217;t even think about changing the contents of the file. (There is an easily faked checksum in it.). Anyway the driver ensures (hopefully) that no damage can be caused. </p>
<p> Also, if some mode is not well aligned on your screen or you don&#8217;t like it&#8217;s sync frequency, consider using the Mach32 install utility (setup for custom monitor) and set one up interactively. If there is no valid faster (higher VSYNC) standard mode given in the EEPROM the driver will use that mode. You will find that this is fun compared with calculating video timings for <i>/etc/XF86Config</i> or <i>/etc/vga/libvga.config</i>. </p>
<p> However the install utility does restrict the maximum pixel depth for custom modes sometimes unneeded hard and the driver obeys that. (Hmm.. actually it should be smart enough to decide itself which pixel depth it can use in that mode.) Since the standard modes are usually only slightly shifted to one side a file with the configuration commands representing the standard modes is given in <i>mach32/mach32.std-modes</i> in the svgalib distribution. You can use these as a starting point. </p>
<p> But here are some real problems:</p>
<h2>8. Eeprom Woes</h2>
<p>I got 2 reports of people having problems with incorrect EEPROM checksums. Both had motherboards with onboard Mach32 VGA&#8217;s from AST. I guessed a checksum algorithm from those reports and put this in the code in addition to the standard ATI style. Still I got a report of someone whose EEPROM was completely empty. If you have problems with checksums send me the output of <code><a href="/docs/linux/man/6-mach32info/">mach32info</a></code>(6) and I&#8217;ll see what I can do. </p>
<p> By default svgalib writes a complaining message and ignores the contents. You can have svgalib ignore the checksum and contents with the configuration command </p>
<p> <code>mach32eeprom ignore</code> </p>
<p> Then you can decide to use the partial info that is still in it. Use </p>
<p> <code>mach32eeprom ignore usetimings</code> </p>
<p> to use the video modes that are defined in the EEPROM (if no better modes are known by the driver). This is usually safe, because the driver knows which modes are safe for your hardware (if <code>clocks</code>, <code>monitor</code> and <code>ramdac</code> are configured correctly). You can also allow the driver to use the configuration for the linear frame buffer in the EEPROM: </p>
<p> <code>mach32eeprom ignore useaperture</code> </p>
<p> or </p>
<p> <code>mach32eeprom ignore usetimings useaperture</code> </p>
<p> However I discourage this because the driver will just enable what the EEPROM says about the aperture. Use <code><a href="/docs/linux/man/6-mach32info/">mach32info</a></code>(6) to check the address it will choose is safe. It might be better to use <code>setuplinear</code> to set up a 4MB aperture at a free address range.</p>
<h2>9. The Mach32Eeprom Command</h2>
<p>The <code>mach32eeprom</code> allows to work around these problems. Here is the complete description for this configuration command. </p>
<dl>
<dt><code>mach32eeprom </code><i>filename</i></p>
<dd>The <i>filename</i> has to begin with a &quot;/&quot;. </p>
<p> Unfortunately reading the EEPROM causes annoying screen flickering and is slow. To avoid this, specify a <i>filename</i> from which to read the contents of the EEPROM. </p>
<p> If the file cannot be read, the EEPROM is read out and the file is created. There is a very simple checksum put into this file. Although it can easily be fooled, don&#8217;t change the file except you know <code>very, very</code> well what you are doing. </p>
<p> Also, as long as the file exists, changes in the Mach32&#8217;s EEPROM are ignored. Delete the file to recreate an updated version on next use of svgalib. You should ensure that the permissions of the file don&#8217;t allow normal users to change it. (This may happen if umask has a bad value when svgalib creates the file). </p>
<p> Example: </p>
<p> <code>mach32eeprom /etc/vga/mach32.eeprom</code> </p>
</dl>
<p> Due to problems with some boards this command got heavily expanded: </p>
<dl>
<dt><code>mach32eeprom </code><i>subcommand1</i><code> [</code><i>subcommand2</i><code>&#8230;]</code></p>
<dd>At least one <i>subcommand</i> is needed. Valid <i>subcommands</i> are: </p>
<dl>
<dd>
<dl>
<dt><code>ignore</code></p>
<dd>Don&#8217;t complain about checksum and don&#8217;t use any EEPROM contents.</p>
<dt><code>useaperture</code></p>
<dd>Use the configuration for the memory aperture given in the EEPROM.</p>
<dt><code>usetimings</code></p>
<dd>Use video modes found in the EEPROM of the board.</p>
<dt><code>nofile</code></p>
<dd>Forget about any filename that maybe was already configured. Don&#8217;t read a file, don&#8217;t create one.</p>
<dt><code>file </code><i>filename</i></p>
<dd>New style form to specify the <i>filename</i>; On contrary to the <code>mach32eeprom </code><i>filename</i> form it can be mixed with any other mach32eeprom subcommand.</p>
<dt><code>updatefile</code></p>
<dd>Don&#8217;t read the file, always read the EEPROM (except when <code>ignore</code> is given) and create an uptodate image of the EEPROM.</p>
<dt><code>keepfile</code></p>
<dd>Disable all previous updatefile commands.</p>
<dt><code>compatible</code></p>
<dd>Fall back to default behavior: If checksum on the EEPROM data is not ok, use nothing of the configuration data. If it is ok, configure everything as specified in the EEPROM.</dl>
</dl>
<dd>The subcommands are intended to be used together and are performed in the order specified. For example: </p>
<p> <code>mach32eeprom ignore useaperture usetimings</code> </p>
<p> will ignore the checksum of your EEPROM, but use its contents. Order is vital! So: </p>
<p> <code>mach32eeprom useaperture usetimings ignore</code> </p>
<p> won&#8217;t use any configuration from your EEPROM. Be careful with the <code>useaperture</code> subcommand. Please see the <code>EEPROM WOES</code> section. Note that any non understood <i>subcommand</i> will terminate the <code>mach32eeprom</code> command silently! Use only one <i>subcommand</i> per <code>mach32eeprom</code> command to avoid this. </p>
<p> The <code>mach32eeprom</code> command is usually not allowed in the environment variable <code>SVGALIB_CONFIG</code>. </p>
</dl>
<h2>10. Setup Of The Memory Aperture (Linear Framebuffer)</h2>
<p>Due to poor design, Xfree86 insists on setting up the aperture itself. It doesn&#8217;t reset the original settings at a VC switch once it runs. You should not start X for the first time after a boot as long as an svgalib application is running. This will result in pre X values being restored at a VC switch by svgalib. If you use svgalib and XF86_Mach32 together, run X first or at least do not start it while any svgalib appl. is still running. After X was started once you can use svgalib and X in all combinations w/o any problems. Xfree uses whatever address is given in the <code>MEM_CFG</code> Mach32 register for a 4MB aperture, even if the aperture is not already enabled and the value in this register is pointless garbage. This is IMHO a dangerous bug as some systems may work only with a 1MB aperture. </p>
<p> However, usage of a correct EEPROM circumvents any such problems. If you cannot use that, use <code>mach32info (6)</code> to find the address in <code>MEM_CFG.</code> Then, <code>if it is a sensible setting for your system</code>, enable a 4MB aperture at that address with <code>setuplinear</code>. Ensure that no other card or memory uses the address range you choose.</p>
<h2>11. Accelerator Support And Other Weird Features</h2>
<p>This version now has support for all accelerator functions of svgalib. However they were intended for use with the cirrus chips. It may happen that at runtime they find they cannot emulate the function actually requested. Then you should disable the corresponding blit function (at least for that application) with the blit config command. </p>
<p> Data transfer between the host and the Mach32 is normally via I/O. This proved to be pretty slow. If a big enough aperture is available, a simple memory copy is used instead. This is usually much faster. You can change which method is used with the blit command. This I/O option affects only <code><a href="/docs/linux/man/3-vga_imageblt/">vga_imageblt</a></code>(3). The other functions are incredible fast. </p>
<p> For type 2 DACS, there is support for 8 bit per color (instead of the normal 6) in the RGB triple in the color lookup table of the 256 color modes. This can be enabled by an application, if it supports it. The <code><a href="/docs/linux/man/6-testaccel/">testaccel</a></code>(6) demo uses it if supported by your hardware. You can use <code><a href="/docs/linux/man/3-vga_ext_set/">vga_ext_set</a></code>(3) to use it from your programs.</p>
<h2>12. Ramdacs</h2>
<p>Mach32 Ramdacs are specified by a type in range 1 .. 5. This type can be queried from the Mach32 and then specifies how to set up the ramdac. A list of actual hardware chips used for each type exists, but is not of much use. The Mach32 will return a type and the ramdac will be completely hardware compatible to one of the given type. </p>
<p> Type 1 and 4 Dacs need different clock frequencies for high colormodes. For 32K/64K colormodes the frequencies have to be doubled and for 16M colors (type 4 only) they have to be tripled. I followed the ATI scheme and did this internally. However this means that for 32K/64K you can use only clocks for which the doubled frequencies can be generated as well. </p>
<p> This is no hard restriction as the 16 clocks of the Mach32 can be divided by 2. Thus if you setup some mode yourself try to use one of the divided clocks in your timings and I can use the undivided clocks internally. </p>
<p> It is a real restriction for 16M colors. ATI itself only supports 25MHz (640&#215;480) here by use of a 75MHz clock. Depending on your clock chip other values may be usable as well. Even the doubled/tripled clocks have to be less than the magic 80 MHz. However the driver does all this itself. It may just happen that some of the predefined or one of your handmade mode-timings can&#8217;t be used because the clock that is used cannot be doubled/tripled. Even though there is already some tolerance in the driver you may fix that by slightly changing the clock values that you set with the <code>clocks</code> command. But note that this will as well affect the ability of the driver to calculate video timings and thus it ability to check the monitor and DAC safety restrictions. </p>
<p> In addition (in complete contrast to my original ATI docs) RAMDAC 4 does not support RGB with blue byte first but only with red first. This required special handling and me adding a bunch of functions to all modules of svgalib and vgagl. The added functions are of lower performance than the usual functions. However most data has to be completely mangled, so I doubt that it can be done much faster. Sorry. </p>
<p> Of course, I might have forgotten to port some parts or even confused things. About bugs in the gl and drawing libs, please ask Harm. But then, I&#8217;m able to emulate a BGR ramdac on my card, so I should even be able to reproduce your problems. </p>
<p> Recently I hear often about type 6 ramdacs in non ATI Mach32 cards. There exists no info about these dacs, thus I cannot support them. The driver assumes unknown DACs can stand up to 80MHz in 256 color clut modes and does not touch the ramdac (that is, assumes it is in the 256 color mode already) </p>
<p> To get rid of the warning message you can use the </p>
<dl>
<dt><code>ramdac </code><i>n</i></p>
<dd>configuration command. It allows to explicitly set the type of the dac to <i>n</i> (in range <code>0</code> to <code>5).</code> <code>Ramdac 3</code> is the most dumbest ramdac possible, s.t. you can use it without any fear for your hardware.</p>
<dt><code>ramdac dumb</code></p>
<dd>is equivalent to <code>ramdac 3</code>.</p>
<dt><code>ramdac auto</code></p>
<dd>switches back to the default autodetection.</dl>
<h2>13. Meaning Of The Detection Message From Svgalib</h2>
<p>Some programs (which do not switch it off) will show a </p>
<p> <code>Using Mach32 </code><i>version</i><code> (</code><i>size</i><code>M at </code><i>adr</i><code>M (</code><i>how</i><code>), </code><i>mem</i><code>K mem, DAC </code><i>dactype</i><code>)</code> </p>
<p> line. This will show up in <code><a href="/docs/linux/man/6-testlinear/">testlinear</a></code>(6) etc but will probably scroll away when you use <code><a href="/docs/linux/man/6-vgatest/">vgatest</a></code>(6). In this line: </p>
<dl>
<dt><i>version</i></p>
<dd>is the version of the driver (as of my counting, not the svgalib version).</p>
<dt><i>size</i></p>
<dd>is the size of the memory aperture. It can be <code>1</code> or <code>4</code> (<code>1</code> will lead to not using the linear aperture if your card has more than 1MB memory, however applications can still use the 1MB aperture and page the video memory through it in 1MB steps). <i>size</i> can also be <code>no</code> if no aperture is setup at all.</p>
<dt><i>adr</i></p>
<dd>is the base address of the aperture in MB.</p>
<dt><i>how</i></p>
<dd>is <code>autodetect</code> if the aperture was setup this way already when the program started. It is <code>setup</code> when the the setting was enforced with a <code>setuplinear</code> configuration command. It is <code>EEPROM</code> when no aperture was detected, but parameters to set it up were found in the EEPROM.</p>
<dt><i>mem</i></p>
<dd>is the amount of memory the card reported to have.</p>
<dt><i>dactype</i></p>
<dd>is the type of the DAC that was detected. </p>
<p> If a special ramdac type was set with the <code>ramdac</code> command a <code>(set)</code> will be displayed after <i>dactype</i>.</dl>
<p> If <i>mem</i>, <i>dactype</i> and/or the chipset were enforced with <code>chipset from the configuration file</code> or <code><a href="/docs/linux/man/3-vga_setchipsetandfeatures/">vga_setchipsetandfeatures</a></code>(3) a <code>forced</code> will be appended to the line.</p>
<h2>14. Conclusions</h2>
<p>A final word: I have an ATI ULTRA PRO/2MB/EISA with a Type 2 DAC. My monitor is an EIZO F550i-M. Everything I tried works on it like a charm. However, I couldn&#8217;t try it with other machines myself and esp. other DAC&#8217;s. Fortunately the Type 2 DAC is the worst to code. So I will probably have gotten the other DAC&#8217;s right. But please be warned! </p>
<p> I did my very best to code the driver to support the other DAC&#8217;s by just reading the docs. <code>But i can&#8217;t give any definitive guarantee for</code> <code>it to work or even not damaging your hardware. So please be careful!</code> </p>
<p> Note that you will have to set the environment variable <code>SVGALIB_MACH32</code> to <code>ILLTRYIT</code> if your DAC is not type 0, 2, 3 or 4. This will of course change if no one with a DAC equal to 1 or 5 has serious problems. If you have a different DAC, making patches to support your card will be much more helpful instead of just complaining. If you have a different DAC that works well tell me as well such that I can remove the need for SVGALIB_MACH32 in the next release. Still, even now, after years, I got no reports of a Mach32 card with a type 1 or 5 ramdac. Go figure. </p>
<p> Thank you for your audience and wishes you will enjoy this driver,<br />
 Michael.</p>
<h2>Files</h2>
<p><i>/etc/vga/libvga.config</i><br />
 <i>/etc/vga/mach32.eeprom</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-svgalib/">svgalib</a></code>(7), <code><a href="/docs/linux/man/5-libvga-config/">libvga.config</a></code>(5), <code><a href="/docs/linux/man/6-mach32info/">mach32info</a></code>(6). </p>
<h2>Author</h2>
<p>The Mach32 driver and this documentation was written by Michael Weller &lt;eowmob [at] exp-math.uni-essen.de&gt;.</p>
