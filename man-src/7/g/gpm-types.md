---
title: "gpm-types(7)"
name: "gpm-types"
section: "7"
letter: "g"
url: "/docs/linux/man/7-gpm-types/"
description: "gpm-types – pointer types (mice, tablets, etc.) managed by gpm. The information below is extracted from the texinfo file, which is the preferred source of information."
---

<p>gpm-types &#8211; pointer types (mice, tablets, etc.) managed by gpm.<br />
 The information below is extracted from the texinfo file, which is the preferred source of information.</p>
<h2>Description</h2>
<p>This manpage describes the various pointer types currently available in gpm. If you look at the source code, you&#8217;ll find that pointer-specific code is confined to mice.c (while it used to only include mouse decoders, gpm now supports tablets and touchscreens as well). The mouse type is specified on command line with the -t option. The option takes an argument, which represents the name of a mouse type. Each type can be associated to different names. For old mouse types, one name is the old selection-compatible name, and another is the XFree name. After version 1.18.1 of gpm, the number of synonyms was made arbitrary and the actual name being used is made available to the function responsible for mouse initialization. Therefore it is possible for a mouse decoder to behave slightly differently according to the name being used for the device (if this feature was already present, we wouldn&#8217;t have for example ms+ and ms+lr as different mouse types). The initialization procedure of each mouse type can also receive extra option, by means of the -o command line option. Since interpretation of the option string is decoder-specific, the allowed options are described in association to each mouse type. When no description of option strings is provided, that means the option string is unused for that mouse type and specifying one generates an error. When the document refer to &#8220;standard serial options&#8221; it means that one of -o dtr, -o rts, -o both can be specified to toggle the control lines of the serial port. The following mouse type are currently recognized:</p>
<dl>
<dt>bare Microsoft</p>
<dd>The Microsoft protocol, without any extension. It only reports two buttons. If your device has three, you should either try running the mman decoder or msc. In the latter case, you need to tell the mouse to talk msc protocol by toggling the DTR and RTS lines (with one of -o drt, -o rts or -o both) or invoking gpm -t msc while keeping the middle button pressed. Very annoying, indeed. This mouse decoder accepts standard serial options, although they should not be needed.</p>
<dt>ms</p>
<dd>This is the original Microsoft protocol, with a middle-button extension. Some old two-button devices send some spurious packets which can be misunderstood as middle-button events. If this is your case, use the bare mouse type. Some new two-button devices are &#8220;plug and play&#8221;, and they don&#8217;t play fair at all; in this case try -t pnp. Many (most) three-button devices that use the Microsoft protocol fail to report some middle-button events during mouse motion. Since the protocol does not distinguish between the middle button going up and the middle button going down it would be liable to get out of step, so this decoder declares the middle button to be up whenever the mouse moves. This prevents dragging with the middle button, so you should probably use -t ms+lr instead of this decoder, especially if you want to use X. This mouse decoder accepts standard serial options, although they should not be needed.</p>
<dt>ms+</p>
<dd>This is the same as -t ms except that the middle button is not reset during mouse motion. So you can drag with the middle button. However, if your mouse exhibits the usual buggy behaviour the decoder is likely to get out of step with reality, thinking the middle button is up when it&#8217;s down and vice versa. You should probably use -t ms+lr instead of this decoder. This mouse decoder accepts standard serial options, although they should not be needed.</p>
<dt>ms+lr</p>
<dd>This is the same as -t ms+ except that there is an additional facility to reset the state of the middle button by pressing the other two buttons together. Do this when the decoder gets into a confused state where it thinks the middle button is up when it&#8217;s down and vice versa. (If you get sick of having to do this, please don&#8217;t blame gpm; blame your buggy mouse! Note that most three-button mice that do the Microsoft protocol can be made to do the MouseSystems protocol instead. The &#8220;3 Button Serial Mouse mini-HOWTO&#8221; has information about this.) This mouse decoder accepts standard serial options, although they should not be needed.</p>
<dt>msc MouseSystems</p>
<dd>This is the standard protocol for three-button serial devices. Some of such devices only enter MouseSystem mode if the RTS, DTR or both lines are pushed low. Thus, you may try -t msc associated with -o rts, -o dtr or -o both.</p>
<dt>mman Mouseman</p>
<dd>The protocol used by the new Logitech devices with three buttons. It is backward compatible with the Microsoft protocol, so if your mouse has three buttons and works with -t ms or similar decoders you may try -t mman instead to use the middle button. This mouse decoder accepts standard serial options, although they should not be needed.</p>
<dt>sun</p>
<dd>The protocol used on Sparc computers and a few others. This mouse decoder accepts standard serial options, although they should not be needed.</p>
<dt>mm MMSeries</p>
<dd>Title says it all. This mouse decoder accepts standard serial options, although they should not be needed.</p>
<dt>logi Logitech</p>
<dd>This is the protocol used by old serial Logitech mice.</p>
<dt>bm BusMouse</p>
<dd>Some bus devices use this protocol, including those produced by Logitech.</p>
<dt>ps2 PS/2</p>
<dd>The protocol used by most busmice.</p>
<dt>ncr</p>
<dd>This `type&#8217; is able to decode the pointing pen found on some laptops (the NCR 3125 pen)</p>
<dt>wacom</p>
<dd>The protocol used by the Wacom tablet. Since version 1.18.1 we have a new Wacom decoder, as the old one was not working with new tablets. This decoder was tested with Ultrapad, PenPartner, and Graphire tablets. Options: -o relative (default) for relative mode, -o absolute for absolute mode.</p>
<dt>genitizer</p>
<dd>The This mouse decoder accepts standard serial options, although they should not be needed.</p>
<dt>logim</p>
<dd>Used to turn Logitech mice into Mouse-Systems-Compatible. Obviously, it only works with some of the Logitech mice.</p>
<dt>pnp</p>
<dd>This decoder works with the new mice produces by our friend Bill, and maybe with the old ones as well. The Pnp protocol is hardwired at 1200 baud and is upset by normal initialization, so this is a -t bare decoder with no initialization at all. This mouse decoder accepts standard serial options, although they should not be needed.</p>
<dt>ms3</p>
<dd>A decoder for the new serial IntelliMouse devices, the ones with three buttons and a protocol incompatible with older ones. The wheel is currently unused.</p>
<dt>imps2</p>
<dd>&#8220;IntelliMouse&#8221; on the ps/2 port. This type can also be used for a generic 2-button ps/2 mouse too, since it will auto-detect the type.</p>
<dt>netmouse</p>
<dd>Decodes the &#8220;Genius NetMouse&#8221; type of devices on the ps/2 port. For serial &#8220;Netmouse&#8221; devices, use the &#8220;ms3&#8221; decoder.</p>
<dt>cal</p>
<dd>A decoder of the &#8220;Calcomp UltraSlate device.</p>
<dt>calr</p>
<dd>Same as above, but in relative mode.</p>
<dt>twid</p>
<dd>Support for the twiddler keyboard. As of gpm-1.14 this decoder includes a char generator for the text console, but doesn&#8217;t yet support X keycodes. If used with -R, gpm will anyway repeat mouse events to the X server. More information about twiddler support can be found in README.twiddler, in the gpm distribution.</p>
<dt>syn synaptics</p>
<dd>A decoder for the Synaptics TouchPad connected to the serial port. This mouse decoder accepts standard serial options, although they should not be needed.</p>
<dt>synps2 synaptics_ps2</p>
<dd>Same as above, but for the devices attached to the ps2 port.</p>
<dt>brw</p>
<dd>A decoder for the Fellowes Browser, a device with 4 buttons and a wheel. This mouse decoder accepts standard serial options, although they should not be needed.</p>
<dt>js Joystick</p>
<dd>This mouse type uses the joystick device to generate mouse events. It is only available if the header linux/joystick.h is found at compile time. The header (and the device as well) has been introduced only during 2.1 development, and is not present in version 2.0 of the kernel.</p>
<dt>summa</p>
<dd>This is a decode for the Symmagraphics of Genius tablet, run in absolute mode. A repeater is associated to this decoder, so it can -R summa can be used to generate X events even for other absolute-pointing devices, like touchscreens. To use the repeated data from X, you need a modified xf86Summa.o module.</p>
<dt>mtouch</p>
<dd>A decoder for the MicroTouch touch screen. Please refer to the file README.microtouch in the source tree of gpm for further information. In the near future, anyways, I plan to fold back to this documentation the content of that file.</p>
<dt>gunze</p>
<dd>A decoder for the gunze touch screen. Please refer to the file README.gunze in the source tree of gpm for further information. In the near future, anyways, I plan to fold back to this documentation the content of that file. The decoder accepts the following options: smooth=, debounce=. An higher smoothness results in slower motion as well; a smaller smoothness gives faster motion but, obviously, less smooth. The default smoothness is 9. The debounce time is express in milliseconds and is the minimum duration of an up-down event to be taken as a tap. Smaller bounces are ignored.</p>
<dt>acecad</p>
<dd>The Acecad tablet in absolute mode.</p>
<dt>wp wizardpad</p>
<dd>Genius WizardPad tablet </p>
<h2>Files</h2>
<pre>src/mice.c The source file for pointer decoders</pre>
<h2>See Also</h2>
<pre><code> <a href="//www.systutorials.com/docs/linux/man/8-gpm/">gpm</a>(8) </code> The General Purpose Mouse server</pre>
<p>The info file about `gpm&#8217;, which gives more complete information and explains how to write a gpm client. </p>
