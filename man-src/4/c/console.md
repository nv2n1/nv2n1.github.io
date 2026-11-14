---
title: "console(4)"
name: "console"
section: "4"
letter: "c"
url: "/docs/linux/man/4-console/"
description: "console – console terminal and virtual consoles"
---

<p>console &#8211; console terminal and virtual consoles</p>
<h2>Description</h2>
<p>A Linux system has up to 63 <i>virtual consoles</i> (character devices with major number 4 and minor number 1 to 63), usually called <i>/dev/ttyn</i> with 1 &le; <i>n</i> &le; 63. The current console is also addressed by <i>/dev/console</i> or <i>/dev/tty0</i>, the character device with major number 4 and minor number 0. The device files <i>/dev/*</i> are usually created using the script MAKEDEV, or using <code><a href="/docs/linux/man/1-mknod/">mknod</a></code>(1), usually with mode 0622 and owner <i>root.tty</i>. </p>
<p> Before kernel version 1.1.54 the number of virtual consoles was compiled into the kernel (in <i>tty.h</i>: #define NR_CONSOLES 8) and could be changed by editing and recompiling. Since version 1.1.54 virtual consoles are created on the fly, as soon as they are needed. </p>
<p> Common ways to start a process on a console are: (a) tell <code><a href="/docs/linux/man/8-init/">init</a></code>(8) (in <code><a href="/docs/linux/man/5-inittab/">inittab</a></code>(5)) to start a <code><a href="/docs/linux/man/8-mingetty/">mingetty</a></code>(8) (or <code><a href="/docs/linux/man/8-agetty/">agetty</a></code>(8)) on the console; (b) ask <code><a href="/docs/linux/man/1-openvt/">openvt</a></code>(1) to start a process on the console; (c) start X&#8212;it will find the first unused console, and display its output there. (There is also the ancient <code><a href="/docs/linux/man/8-doshell/">doshell</a></code>(8).) </p>
<p> Common ways to switch consoles are: (a) use Alt+F<i>n</i> or Ctrl+Alt+F<i>n</i> to switch to console <i>n</i>; AltGr+F<i>n</i> might bring you to console <i>n</i>+12 [here Alt and AltGr refer to the left and right Alt keys, respectively]; (b) use Alt+RightArrow or Alt+LeftArrow to cycle through the presently allocated consoles; (c) use the program <code><a href="/docs/linux/man/1-chvt/">chvt</a></code>(1). (The key mapping is user settable, see <code><a href="/docs/linux/man/1-loadkeys/">loadkeys</a></code>(1); the above mentioned key combinations are according to the default settings.) </p>
<p> The command <code><a href="/docs/linux/man/1-deallocvt/">deallocvt</a></code>(1) (formerly <code>disalloc</code>) will free the memory taken by the screen buffers for consoles that no longer have any associated process.</p>
<h3>Properties</h3>
<p>Consoles carry a lot of state. I hope to document that some other time. The most important fact is that the consoles simulate vt100 terminals. In particular, a console is reset to the initial state by printing the two characters ESC c. All escape sequences can be found in <code><a href="/docs/linux/man/4-console_codes/">console_codes</a></code>(4).</p>
<h2>Files</h2>
<p><i>/dev/console</i><br />
 <i>/dev/tty*</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-chvt/">chvt</a></code>(1), <code><a href="/docs/linux/man/1-deallocvt/">deallocvt</a></code>(1), <code><a href="/docs/linux/man/1-loadkeys/">loadkeys</a></code>(1), <code><a href="/docs/linux/man/1-mknod/">mknod</a></code>(1), <code><a href="/docs/linux/man/1-openvt/">openvt</a></code>(1), <code><a href="/docs/linux/man/4-console_codes/">console_codes</a></code>(4), <code><a href="/docs/linux/man/4-console_ioctl/">console_ioctl</a></code>(4), <code><a href="/docs/linux/man/4-tty/">tty</a></code>(4), <code><a href="/docs/linux/man/4-ttys/">ttyS</a></code>(4), <code><a href="/docs/linux/man/7-charsets/">charsets</a></code>(7), <code><a href="/docs/linux/man/8-agetty/">agetty</a></code>(8), <code><a href="/docs/linux/man/8-init/">init</a></code>(8), <code><a href="/docs/linux/man/8-mapscrn/">mapscrn</a></code>(8), <code><a href="/docs/linux/man/8-mingetty/">mingetty</a></code>(8), <code><a href="/docs/linux/man/8-resizecons/">resizecons</a></code>(8), <code><a href="/docs/linux/man/8-setfont/">setfont</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 3.53 of the Linux <i>man-pages</i> project. A description of the project, and information about reporting bugs, can be found at <a rel="nofollow" href="http://www.kernel.org/doc/man-pages/.">http://www.kernel.org/doc/man-pages/.</a> </p>
