---
title: "mousedrv(4)"
name: "mousedrv"
section: "4"
letter: "m"
url: "/docs/linux/man/4-mousedrv/"
description: "mouse – Xorg mouse input driver"
---

<p>mouse &#8211; Xorg mouse input driver</p>
<h2>Synopsis</h2>
<pre><code>Section &#34;InputDevice&#34;</code>
<code> Identifier &#34;</code><i>idevname</i><code>&#34;</code>
<code> Driver &#34;mouse&#34;</code>
<code> Option &#34;Protocol&#34; &#34;</code><i>protoname</i><code>&#34;</code>
<code> Option &#34;Device&#34; &#34;</code><i>devpath</i><code>&#34;</code>
&nbsp;<wbr>&nbsp;<wbr>...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>mouse</code> is an Xorg input driver for mice. The driver supports most available mouse types and interfaces, though the level of support for types of mice depends on the OS. </p>
<p> The <code>mouse</code> driver functions as a pointer input device. Multiple mice are supported by multiple instances of this driver.</p>
<h2>Supported Hardware</h2>
<dl>
<dt>USB mouse</p>
<dd>USB (Universal Serial Bus) ports are present on most modern computers. Several devices can be plugged into this bus, including mice and keyboards. Support for USB mice is platform specific.</p>
<dt>PS/2 mouse</p>
<dd>The PS/2 mouse is an intelligent device and may have more than three buttons and a wheel or a roller. The PS/2 mouse is usually compatible with the original PS/2 mouse from IBM immediately after power up. The PS/2 mouse with additional features requires a specialized initialization procedure to enable these features. Without proper initialization, it behaves as though it were an ordinary two or three button mouse.</p>
<dt>Serial mouse</p>
<dd>There have been numerous serial mouse models from a number of manufacturers. Despite the wide range of variations, there have been relatively few protocols (data format) with which the serial mouse talks to the host computer. </p>
<p> The modern serial mouse conforms to the PnP COM device specification so that the host computer can automatically detect the mouse and load an appropriate driver. This driver supports this specification and can detect popular PnP serial mouse models on most platforms.</p>
<dt>Bus mouse</p>
<dd>The bus mouse connects to a dedicated interface card in an expansion slot. Some older video cards, notably those from ATI, and integrated I/O cards may also have a bus mouse connector.</dl>
<p> The interface type of the mouse can be determined by looking at the connector of the mouse. USB mice have a thin rectangular connector. PS/2 mice are equipped with a small, round DIN 6-pin connector. Serial mouse have a D-Sub female 9- or 25-pin connector. Bus mice have either a D-Sub male 9-pin connector or a round DIN 9-pin connector. Some mice come with adapters with which the connector can be converted to another. If you are to use such an adapter, remember that the connector at the very end of the mouse/adapter pair is what matters.</p>
<h2>Configuration Details</h2>
<p>Depending on the X server version in use, input device options may be set in either a xorg.conf file, an xorg.conf.d snippet or in the configuration files read by the Hardware Abstraction Layer (HAL) daemon, <a href="/docs/linux/man/1-hald/">hald</a>(1). </p>
<p> Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details and for options that can be used with all input drivers. This section only covers configuration details specific to this driver. </p>
<p> The driver can auto-detect the mouse type on some platforms. On some platforms this is limited to plug and play serial mice, and on some the auto-detection works for any mouse that the OS&#8217;s kernel driver supports. On others, it is always necessary to specify the mouse protocol in the config file. The <i>README</i> document provided with this driver contains some detailed information about this. </p>
<p> The following driver <code>Options</code> are supported:</p>
<dl>
<dt><code>Option &#34;Protocol&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Specify the mouse protocol. Valid protocol types include:</dl>
<dl>
<dd>Auto, Microsoft, MouseSystems, MMSeries, Logitech, MouseMan, MMHitTab, GlidePoint, IntelliMouse, ThinkingMouse, ValuMouseScroll, AceCad, PS/2, ImPS/2, ExplorerPS/2, ThinkingMousePS/2, MouseManPlusPS/2, GlidePointPS/2, NetMousePS/2, NetScrollPS/2, BusMouse, SysMouse, WSMouse, USB, VUID, Xqueue.</dl>
<dl>
<dd>Not all protocols are supported on all platforms. The &quot;Auto&quot; protocol specifies that protocol auto-detection should be attempted. The default protocol setting is platform-specific.</dl>
<dl>
<dt><code>Option &#34;Device&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Specifies the device through which the mouse can be accessed. A common setting is &quot;/dev/mouse&quot;, which is often a symbolic link to the real device. This option is mandatory, and there is no default setting. The driver may however attempt to probe some default devices if this option is missing. Property: &quot;Device Node&quot; (read-only).</p>
<dt><code>Option &#34;Buttons&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Specifies the number of mouse buttons. In cases where the number of buttons cannot be auto-detected, the default value is 3. The maximum number is 24.</p>
<dt><code>Option &#34;Emulate3Buttons&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable/disable the emulation of the third (middle) mouse button for mice which only have two physical buttons. The third button is emulated by pressing both buttons simultaneously. Default: on, until a press of a physical button 3 is detected. Property: &quot;Mouse Middle Button Emulation&quot;</p>
<dt><code>Option &#34;Emulate3Timeout&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Sets the timeout (in milliseconds) that the driver waits before deciding if two buttons where pressed &quot;simultaneously&quot; when 3 button emulation is enabled. Default: 50. Property: &quot;Mouse Middle Button Timeout&quot;</p>
<dt><code>Option &#34;ChordMiddle&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable/disable handling of mice that send left+right events when the middle button is used. Default: off.</p>
<dt><code>Option &#34;EmulateWheel&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable/disable &quot;wheel&quot; emulation. Wheel emulation means emulating button press/release events when the mouse is moved while a specific real button is pressed. Wheel button events (typically buttons 4 and 5) are usually used for scrolling. Wheel emulation is useful for getting wheel-like behaviour with trackballs. It can also be useful for mice with 4 or more buttons but no wheel. See the description of the <code>EmulateWheelButton</code>, <code>EmulateWheelInertia</code>, <code>XAxisMapping</code>, and <code>YAxisMapping</code> options below. Default: off.</p>
<dt><code>Option &#34;EmulateWheelButton&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Specifies which button must be held down to enable wheel emulation mode. While this button is down, X and/or Y pointer movement will generate button press/release events as specified for the <code>XAxisMapping</code> and <code>YAxisMapping</code> settings. If set to 0, no button is required and any motion of the device is converted into wheel events. Default: 4.</p>
<dt><code>Option &#34;EmulateWheelInertia&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Specifies how far (in pixels) the pointer must move to generate button press/release events in wheel emulation mode. Default: 10.</p>
<dt><code>Option &#34;EmulateWheelTimeout&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Specifies the time in milliseconds the <code>EmulateWheelButton</code> must be pressed before wheel emulation is started. If the <code>EmulateWheelButton</code> is released before this timeout, the original button press/release event is sent. Default: 200.</p>
<dt><code>Option &#34;XAxisMapping&#34; &#34;</code><i>N1 N2</i><code>&#34;</code></p>
<dd>Specifies which buttons are mapped to motion in the X direction in wheel emulation mode. Button number <i>N1</i> is mapped to the negative X axis motion and button number <i>N2</i> is mapped to the positive X axis motion. Default: no mapping.</p>
<dt><code>Option &#34;YAxisMapping&#34; &#34;</code><i>N1 N2</i><code>&#34;</code></p>
<dd>Specifies which buttons are mapped to motion in the Y direction in wheel emulation mode. Button number <i>N1</i> is mapped to the negative Y axis motion and button number <i>N2</i> is mapped to the positive Y axis motion. Default: no mapping.</p>
<dt><code>Option &#34;ZAxisMapping&#34; &#34;X&#34;</code></p>
<dd>
<dt><code>Option &#34;ZAxisMapping&#34; &#34;Y&#34;</code></p>
<dd>
<dt><code>Option &#34;ZAxisMapping&#34; &#34;</code><i>N1 N2</i><code>&#34;</code></p>
<dd>
<dt><code>Option &#34;ZAxisMapping&#34; &#34;</code><i>N1 N2 N3 N4</i><code>&#34;</code></p>
<dd>Set the mapping for the Z axis (wheel) motion to buttons or another axis (<code>X</code> or <code>Y</code>). Button number <i>N1</i> is mapped to the negative Z axis motion and button number <i>N2</i> is mapped to the positive Z axis motion. For mice with two wheels, four button numbers can be specified, with the negative and positive motion of the second wheel mapped respectively to buttons number <i>N3</i> and <i>N4</i>. Note that the protocols for mice with one and two wheels can be different and the driver may not be able to autodetect it. Default: &quot;4 5&quot;.</p>
<dt><code>Option &#34;ButtonMapping&#34; &#34;</code><i>N1 N2 [&#8230;]</i><code>&#34;</code></p>
<dd>Specifies how physical mouse buttons are mapped to logical buttons. Physical button 1 is mapped to logical button <i>N1</i>, physical button 2 to <i>N2</i>, and so forth. This enables the use of physical buttons that are obscured by <i>ZAxisMapping</i>. Default:&nbsp;<wbr>&quot;1 2 3 8 9 10 &#8230;&quot;.</p>
<dt><code>Option &#34;FlipXY&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable/disable swapping the X and Y axes. This transformation is applied after the <code>InvX</code>, <code>InvY</code> and <code>AngleOffset</code> transformations. Default: off.</p>
<dt><code>Option &#34;InvX&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Invert the X axis. Default: off.</p>
<dt><code>Option &#34;InvY&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Invert the Y axis. Default: off.</p>
<dt><code>Option &#34;AngleOffset&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Specify a clockwise angular offset (in degrees) to apply to the pointer motion. This transformation is applied before the <code>FlipXY</code>, <code>InvX</code> and <code>InvY</code> transformations. Default: 0.</p>
<dt><code>Option &#34;SampleRate&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Sets the number of motion/button events the mouse sends per second. Setting this is only supported for some mice, including some Logitech mice and some PS/2 mice on some platforms. Default: whatever the mouse is already set to.</p>
<dt><code>Option &#34;Resolution&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Sets the resolution of the device in counts per inch. Setting this is only supported for some mice, including some PS/2 mice on some platforms. Default: whatever the mouse is already set to.</p>
<dt><code>Option &#34;Sensitivity&#34; &#34;</code><i>float</i><code>&#34;</code></p>
<dd>Mouse movements are multiplied by this float before being processed. Use this mechanism to slow down high resolution mice. Because values bigger than 1.0 will result in not all pixels on the screen being accessible, you should better use mouse acceleration (see <code>man xset</code>) for speeding up low resolution mice. Default: 1.0</p>
<dt><code>Option &#34;DragLockButtons&#34; &#34;</code><i>L1 B2 L3 B4</i><code>&#34;</code></p>
<dd>Sets &#34;drag lock buttons&#34; that simulate holding a button down, so that low dexterity people do not have to hold a button down at the same time they move a mouse cursor. Button numbers occur in pairs, with the lock button number occurring first, followed by the button number that is the target of the lock button.</p>
<dt><code>Option &#34;DragLockButtons&#34; &#34;</code><i>M1</i><code>&#34;</code></p>
<dd>Sets a &#34;master drag lock button&#34; that acts as a &#34;Meta Key&#34; indicating that the next button pressed is to be &#34;drag locked&#34;.</p>
<dt><code>Option &#34;ClearDTR&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable/disable clearing the DTR line on the serial port used by the mouse. Some dual-protocol mice require the DTR line to be cleared to operate in the non-default protocol. This option is for serial mice only and is handled by the X server. Default: off.</p>
<dt><code>Option &#34;ClearRTS&#34; &#34;</code><i>boolean</i><code>&#34;</code></p>
<dd>Enable/disable clearing the RTS line on the serial port used by the mouse. Some dual-protocol mice require the RTS line to be cleared to operate in the non-default protocol. This option is for serial mice only and is handled by the X server. Default: off.</p>
<dt><code>Option &#34;BaudRate&#34; &#34;</code><i>integer</i><code>&#34;</code></p>
<dd>Set the baud rate to use for communicating with a serial mouse. This option should rarely be required because the default is correct for almost all situations. Valid values include: 300, 1200, 2400, 4800, 9600, 19200. Default: 1200.</dl>
<p> There are some other options that may be used to control various parameters for serial port communication, but they are not documented here because the driver sets them correctly for each mouse protocol type.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7), README.mouse. <a href="/docs/linux/man/7-hal/">hal</a>(7), <a href="/docs/linux/man/8-hald/">hald</a>(8), <a href="/docs/linux/man/5-fdi/">fdi</a>(5). </p>
