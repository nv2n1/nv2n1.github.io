---
title: "resizecons(8)"
name: "resizecons"
section: "8"
letter: "r"
url: "/docs/linux/man/8-resizecons/"
description: "resizecons – change kernel idea of the console size"
---

<p>resizecons &#8211; change kernel idea of the console size</p>
<h2>Synopsis</h2>
<p><code>resizecons </code><i>COLSxROWS</i><br />
 <code>resizecons -lines </code><i>ROWS</i></p>
<h2>Description</h2>
<p>The <i>resizecons</i> command tries to change the videomode of the console. There are several aspects to this: (a) the kernel must know about it, (b) the hardware must know about it, (c) user programs must know about it, (d) the console font may have to be adapted. (a) The kernel is told about the change using the ioctl VT_RESIZE. This causes the kernel to reallocate console screen memory for all virtual consoles, and might fail if there is not enough memory. (In that case, try to disallocate some virtual consoles first.) If this ioctl succeeds, but a later step fails (e.g., because you do not have root permissions), you may be left with a very messy screen. The most difficult part of this is (b), since it requires detailed knowledge of the video card hardware, and the setting of numerous registers. Only changing the number of rows is slightly easier, and <i>resizecons</i> will try to do that itself, when given the <i>-lines</i> option. (Probably, root permission will be required.) The command <i>resizecons COLSxROWS</i> will execute <i>restoretextmode -r COLSxROWS</i> (and hence requires that you have svgalib installed). Here COLSxROWS is a file that was created earlier by <i>restoretextmode -w COLSxROWS.</i> Again, either root permissions are required, or <i>restoretextmode</i> has to be suid root. In order to deal with (c), <i>resizecons</i> does a `stty rows ROWS cols COLS&#8217; for each active console (in the range tty0..tty15), and sends a SIGWINCH signal to <i>selection</i> if it finds the file /tmp/selection.pid. Finally, (d) is dealt with by executing a <i>setfont</i> command. Most likely, the wrong font is loaded, and you may want to do another <i>setfont</i> yourself afterwards. </p>
<h2>Bugs</h2>
<p><i>resizecons</i> does not work on all hardware. For example, it cannot be used on platforms other than x86 and x86_64. See the <code><a href="/docs/linux/man/1-fbset/">fbset</a></code>(1) program if you are looking for an alternative. This command used to be called <i>resize,</i> but was renamed to avoid conflict with another command with the same name. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-setfont/">setfont</a></code>(8), <code><a href="/docs/linux/man/1-stty/">stty</a></code>(1), <code><a href="/docs/linux/man/1-selection/">selection</a></code>(1), <code><a href="/docs/linux/man/8-restoretextmode/">restoretextmode</a></code>(8), <code><a href="/docs/linux/man/8-disalloc/">disalloc</a></code>(8), <code><a href="/docs/linux/man/1-fbset/">fbset</a></code>(1) </p>
