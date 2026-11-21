---

title: "dc1394_vloopback(1)"
name: "dc1394_vloopback"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dc1394_vloopback/"
description: "dc1394_vloopback – send format0 video to V4L vloopback device"
---

<h2>NAME</h2>
<p> dc1394_vloopback &#8211; send format0 video to V4L vloopback device</p>
<p> <code>dc1394_vloopback [</code><i>&#8211;daemon</i>] [<i>&#8211;pipe</i>] [<i>&#8211;guid=camera-euid</i>] [<i>&#8211;video1394=/dev/video1394/x</i>] [<i>&#8211;vloopback=/dev/video0</i>] [<i>&#8211;palette=yuv422|rgb24</i>] [<i>&#8211;width=n</i>] [<i>&#8211;height=n</i>]</p>
<p> Sends format0 640&#215;480 RGB to the vloopback input device so that it can be consumed by V4L applications on the vloopback output device.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;daemon</code></dt>
<dd> run as a daemon, detached from console (optional).</dd>
<dt><code>&#8211;pipe</code></dt>
<dd> write images to vloopback device instead of using zero-copy mmap mode (optional).</dd>
<dt><code>&#8211;guid</code></dt>
<dd> select camera to use (optional). default is first camera on any port.</dd>
<dt><code>&#8211;video1394</code></dt>
<dd> specifies video1394 device to use (optional). default is /dev/video1394/&lt;port#&gt;.</dd>
<dt><code>&#8211;vloopback</code></dt>
<dd> specifies video4linux device to use (optional). default is to determine this automatically.</dd>
<dt><code>&#8211;palette</code></dt>
<dd> specify the video palette to use (optional). yuv422 (default) or rgb24.</dd>
<dt><code>&#8211;width</code></dt>
<dd> set the initial width (default=640)</dd>
<dt><code>&#8211;height</code></dt>
<dd> set the initial height (default=480)</dd>
<dt><code>&#8211;help</code></dt>
<dd> print help message</dd></dl>
<h2>BUGS</h2>
<p> This program is maintained by the DC1394 Package Mainteners&#8217; team &lt;libdc1394-packaging [at] lists.sourceforge.net&gt;. </p>
<p> The bugs related to libdc1394 and current packaging can be submitted here: </p>
<p> <a rel="nofollow" href="http://bugs.launchpad.net/~libdc1394-dev/">http://bugs.launchpad.net/~libdc1394-dev/</a> </p>
<p> For bugs related to library implementation, please submit to libdc1394 developers: &lt;libdc1394-dev [at] lists.sourceforge.net&gt;.</p>
<h2>AUTHOR</h2>
<p> This manual page was originally written by Peter De Schrijver &lt;p2 [at] debian.org&gt; for the Debian GNU/Linux system (but may be used by others).</p>
<h2>COPYRIGHT</h2>
<p> This manual page is maintained by the DC1394 Package Mainteners&#8217; team. The team members and other information can be found online at: <a rel="nofollow" href="http://launchpad.net/~libdc1394-dev">http://launchpad.net/~libdc1394-dev</a> </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Lesser General Public License, Version 2 or any later version published by the Free Software Foundation. </p>
<p> On Debian systems (like Ubuntu), the complete text of the GNU Lesser General Public License can be found in /usr/share/common-licenses/LGPL-2.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dc1394_reset_bus/">dc1394_reset_bus</a></code>(1) </p>
