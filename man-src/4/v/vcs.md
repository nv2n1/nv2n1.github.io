---
title: "vcs(4)"
name: "vcs"
section: "4"
letter: "v"
url: "/docs/linux/man/4-vcs/"
description: "vcs, vcsa – virtual console memory"
---

<p>vcs, vcsa &#8211; virtual console memory</p>
<h2>Description</h2>
<p><i>/dev/vcs0</i> is a character device with major number 7 and minor number 0, usually with mode 0644 and ownership root:tty. It refers to the memory of the currently displayed virtual console terminal. </p>
<p> <i>/dev/vcs[1-63]</i> are character devices for virtual console terminals, they have major number 7 and minor number 1 to 63, usually mode 0644 and ownership root:tty. <i>/dev/vcsa[0-63]</i> are the same, but using <i>unsigned short</i>s (in host byte order) that include attributes, and prefixed with four bytes giving the screen dimensions and cursor position: <i>lines</i>, <i>columns</i>, <i>x</i>, <i>y</i>. (<i>x</i> = <i>y</i> = 0 at the top left corner of the screen.) </p>
<p> When a 512-character font is loaded, the 9th bit position can be fetched by applying the <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) <code>VT_GETHIFONTMASK</code> operation (available in Linux kernels 2.6.18 and above) on <i>/dev/tty[1-63]</i>; the value is returned in the <i>unsigned short</i> pointed to by the third <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) argument. </p>
<p> These devices replace the screendump <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operations of <code><a href="/docs/linux/man/2-ioctl_console/">ioctl_console</a></code>(2), so the system administrator can control access using filesystem permissions. </p>
<p> The devices for the first eight virtual consoles may be created by: </p>
<p> for x in 0 1 2 3 4 5 6 7 8; do<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mknod -m 644&nbsp;/dev/vcs$x c 7&nbsp;$x;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mknod -m 644&nbsp;/dev/vcsa$x c 7&nbsp;$[$x+128]; done chown root:tty /dev/vcs* </p>
<p> No <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) requests are supported.</p>
<h2>Files</h2>
<p><i>/dev/vcs[0-63]</i><br />
 <i>/dev/vcsa[0-63]</i></p>
<h2>Versions</h2>
<p>Introduced with version 1.1.92 of the Linux kernel.</p>
<h2>Examples</h2>
<p>You may do a screendump on vt3 by switching to vt1 and typing cat /dev/vcs3 &gt;foo Note that the output does not contain newline characters, so some processing may be required, like in fold -w 81 /dev/vcs3 | lpr or (horrors) setterm -dump 3 -file /proc/self/fd/1 The <i>/dev/vcsa0</i> device is used for Braille support. This program displays the character and screen attributes under the cursor of the second virtual console, then changes the background color there: </p>
<pre><code>#include &lt;fcntl.h&gt;
#include &lt;linux/vt.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;sys/ioctl.h&gt;
#include &lt;unistd.h&gt;
int main(void)
{
    int fd;
    char *device = &quot;/dev/vcsa2&quot;;
    char *console = &quot;/dev/tty2&quot;;
    struct {
        unsigned char lines, cols, x, y;
    } scrn;
    unsigned short s;
    unsigned short mask;
    unsigned char attrib;
    int ch;
    fd = open(console, O_RDWR);
    if (fd &lt; 0) {
        perror(console);
        exit(EXIT_FAILURE);
    }
    if (ioctl(fd, VT_GETHIFONTMASK, &amp;mask) &lt; 0) {
        perror(&quot;VT_GETHIFONTMASK&quot;);
        exit(EXIT_FAILURE);
    }
    (void)close(fd);
    fd = open(device, O_RDWR);
    if (fd &lt; 0) {
        perror(device);
        exit(EXIT_FAILURE);
    }
    (void)read(fd, &amp;scrn, 4);
    (void)lseek(fd, 4 + 2 * (scrn.y * scrn.cols + scrn.x), SEEK_SET);
    (void)read(fd, &amp;s, 2);
    ch = s &amp; 0xff;
    if (s &amp; mask)
        ch |= 0x100;
    attrib = ((s &amp; ~mask) &gt;&gt; 8);
    printf(&quot;ch=%#03x attrib=%#02x
&quot;, ch, attrib);
    s ha = 0x1000;
    (void)lseek(fd, -2, SEEK_CUR);
    (void)write(fd, &amp;s, 2);
    exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-ioctl_console/">ioctl_console</a></code>(2), <code><a href="/docs/linux/man/4-tty/">tty</a></code>(4), <code><a href="/docs/linux/man/4-ttys/">ttyS</a></code>(4), <code><a href="/docs/linux/man/8-gpm/">gpm</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
