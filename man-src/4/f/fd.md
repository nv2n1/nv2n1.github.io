---
title: "fd(4)"
name: "fd"
section: "4"
letter: "f"
url: "/docs/linux/man/4-fd/"
description: "fd – floppy disk device"
---

<p>fd &#8211; floppy disk device</p>
<h2>Configuration</h2>
<p>Floppy drives are block devices with major number 2. Typically they are owned by <i>root.floppy</i> (i.e., user root, group floppy) and have either mode 0660 (access checking via group membership) or mode 0666 (everybody has access). The minor numbers encode the device type, drive number, and controller number. For each device type (that is, combination of density and track count) there is a base minor number. To this base number, add the drive&#8217;s number on its controller and 128 if the drive is on the secondary controller. In the following device tables, <i>n</i> represents the drive number. </p>
<p> <code>Warning: If you use formats with more tracks than supported by your drive, you may cause it mechanical damage.</code> Trying once if more tracks than the usual 40/80 are supported should not damage it, but no warranty is given for that. If you are not sure, don&#8217;t create device entries for those formats, so as to prevent their usage. </p>
<p> Drive-independent device files which automatically detect the media format and capacity: </p>
<table>
<tr VALIGN=top>
<td>Name</td>
<td>Base minor #
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i></td>
<td>0
</td>
</tr>
</table>
<p> 5.25 inch double density device files: </p>
<table>
<tr VALIGN=top>
<td>Name</td>
<td>Capac.</td>
<td>Cyl.</td>
<td>Sect.</td>
<td>Heads</td>
<td>Base minor #
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=6>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>d360</code></td>
<td>360K</td>
<td>40</td>
<td>9</td>
<td>2</td>
<td>4
</td>
</tr>
</table>
<p> 5.25 inch high density device files: </p>
<table>
<tr VALIGN=top>
<td>Name</td>
<td>Capac.</td>
<td>Cyl.</td>
<td>Sect.</td>
<td>Heads</td>
<td>Base minor #
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=6>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>h360</code></td>
<td>360K</td>
<td>40</td>
<td>9</td>
<td>2</td>
<td>20
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>h410</code></td>
<td>410K</td>
<td>41</td>
<td>10</td>
<td>2</td>
<td>48
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>h420</code></td>
<td>420K</td>
<td>42</td>
<td>10</td>
<td>2</td>
<td>64
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>h720</code></td>
<td>720K</td>
<td>80</td>
<td>9</td>
<td>2</td>
<td>24
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>h880</code></td>
<td>880K</td>
<td>80</td>
<td>11</td>
<td>2</td>
<td>80
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>h1200</code></td>
<td>1200K</td>
<td>80</td>
<td>15</td>
<td>2</td>
<td>8
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>h1440</code></td>
<td>1440K</td>
<td>80</td>
<td>18</td>
<td>2</td>
<td>40
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>h1476</code></td>
<td>1476K</td>
<td>82</td>
<td>18</td>
<td>2</td>
<td>56
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>h1494</code></td>
<td>1494K</td>
<td>83</td>
<td>18</td>
<td>2</td>
<td>72
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>h1600</code></td>
<td>1600K</td>
<td>80</td>
<td>20</td>
<td>2</td>
<td>92
</td>
</tr>
</table>
<p> 3.5 inch double density device files: </p>
<table>
<tr VALIGN=top>
<td>Name</td>
<td>Capac.</td>
<td>Cyl.</td>
<td>Sect.</td>
<td>Heads</td>
<td>Base minor #
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=6>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>D360</code></td>
<td>360K</td>
<td>80</td>
<td>9</td>
<td>1</td>
<td>12
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>D720</code></td>
<td>720K</td>
<td>80</td>
<td>9</td>
<td>2</td>
<td>16
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>D800</code></td>
<td>800K</td>
<td>80</td>
<td>10</td>
<td>2</td>
<td>120
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>D1040</code></td>
<td>1040K</td>
<td>80</td>
<td>13</td>
<td>2</td>
<td>84
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>D1120</code></td>
<td>1120K</td>
<td>80</td>
<td>14</td>
<td>2</td>
<td>88
</td>
</tr>
</table>
<p> 3.5 inch high density device files: </p>
<table>
<tr VALIGN=top>
<td>Name</td>
<td>Capac.</td>
<td>Cyl.</td>
<td>Sect.</td>
<td>Heads</td>
<td>Base minor #
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=6>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>H360</code></td>
<td>360K</td>
<td>40</td>
<td>9</td>
<td>2</td>
<td>12
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>H720</code></td>
<td>720K</td>
<td>80</td>
<td>9</td>
<td>2</td>
<td>16
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>H820</code></td>
<td>820K</td>
<td>82</td>
<td>10</td>
<td>2</td>
<td>52
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>H830</code></td>
<td>830K</td>
<td>83</td>
<td>10</td>
<td>2</td>
<td>68
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>H1440</code></td>
<td>1440K</td>
<td>80</td>
<td>18</td>
<td>2</td>
<td>28
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>H1600</code></td>
<td>1600K</td>
<td>80</td>
<td>20</td>
<td>2</td>
<td>124
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>H1680</code></td>
<td>1680K</td>
<td>80</td>
<td>21</td>
<td>2</td>
<td>44
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>H1722</code></td>
<td>1722K</td>
<td>82</td>
<td>21</td>
<td>2</td>
<td>60
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>H1743</code></td>
<td>1743K</td>
<td>83</td>
<td>21</td>
<td>2</td>
<td>76
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>H1760</code></td>
<td>1760K</td>
<td>80</td>
<td>22</td>
<td>2</td>
<td>96
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>H1840</code></td>
<td>1840K</td>
<td>80</td>
<td>23</td>
<td>2</td>
<td>116
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>H1920</code></td>
<td>1920K</td>
<td>80</td>
<td>24</td>
<td>2</td>
<td>100
</td>
</tr>
</table>
<p> 3.5 inch extra density device files: </p>
<table>
<tr VALIGN=top>
<td>Name</td>
<td>Capac.</td>
<td>Cyl.</td>
<td>Sect.</td>
<td>Heads</td>
<td>Base minor #
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=6>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>E2880</code></td>
<td>2880K</td>
<td>80</td>
<td>36</td>
<td>2</td>
<td>32
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>CompaQ</code></td>
<td>2880K</td>
<td>80</td>
<td>36</td>
<td>2</td>
<td>36
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>E3200</code></td>
<td>3200K</td>
<td>80</td>
<td>40</td>
<td>2</td>
<td>104
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>E3520</code></td>
<td>3520K</td>
<td>80</td>
<td>44</td>
<td>2</td>
<td>108
</td>
</tr>
<tr VALIGN=top>
<td><code>fd</code><i>n</i><code>E3840</code></td>
<td>3840K</td>
<td>80</td>
<td>48</td>
<td>2</td>
<td>112
</td>
</tr>
</table>
<h2>Description</h2>
<p><code>fd</code> special files access the floppy disk drives in raw mode. The following <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) calls are supported by <code>fd</code> devices:</p>
<dl>
<dt><code>FDCLRPRM</code></p>
<dd>clears the media information of a drive (geometry of disk in drive).</p>
<dt><code>FDSETPRM</code></p>
<dd>sets the media information of a drive. The media information will be lost when the media is changed.</p>
<dt><code>FDDEFPRM</code></p>
<dd>sets the media information of a drive (geometry of disk in drive). The media information will not be lost when the media is changed. This will disable autodetection. In order to reenable autodetection, you have to issue an <code>FDCLRPRM</code>.</p>
<dt><code>FDGETDRVTYP</code></p>
<dd>returns the type of a drive (name parameter). For formats which work in several drive types, <code>FDGETDRVTYP</code> returns a name which is appropriate for the oldest drive type which supports this format.</p>
<dt><code>FDFLUSH</code></p>
<dd>invalidates the buffer cache for the given drive.</p>
<dt><code>FDSETMAXERRS</code></p>
<dd>sets the error thresholds for reporting errors, aborting the operation, recalibrating, resetting, and reading sector by sector.</p>
<dt><code>FDSETMAXERRS</code></p>
<dd>gets the current error thresholds.</p>
<dt><code>FDGETDRVTYP</code></p>
<dd>gets the internal name of the drive.</p>
<dt><code>FDWERRORCLR</code></p>
<dd>clears the write error statistics.</p>
<dt><code>FDWERRORGET</code></p>
<dd>reads the write error statistics. These include the total number of write errors, the location and disk of the first write error, and the location and disk of the last write error. Disks are identified by a generation number which is incremented at (almost) each disk change.</p>
<dt><code>FDTWADDLE</code></p>
<dd>Switch the drive motor off for a few microseconds. This might be needed in order to access a disk whose sectors are too close together.</p>
<dt><code>FDSETDRVPRM</code></p>
<dd>sets various drive parameters.</p>
<dt><code>FDGETDRVPRM</code></p>
<dd>reads these parameters back.</p>
<dt><code>FDGETDRVSTAT</code></p>
<dd>gets the cached drive state (disk changed, write protected et al.)</p>
<dt><code>FDPOLLDRVSTAT</code></p>
<dd>polls the drive and return its state.</p>
<dt><code>FDGETFDCSTAT</code></p>
<dd>gets the floppy controller state.</p>
<dt><code>FDRESET</code></p>
<dd>resets the floppy controller under certain conditions.</p>
<dt><code>FDRAWCMD</code></p>
<dd>sends a raw command to the floppy controller.</dl>
<p> For more precise information, consult also the <i>&lt;linux/fd.h&gt;</i> and <i>&lt;linux/fdreg.h&gt;</i> include files, as well as the <code><a href="/docs/linux/man/1-floppycontrol/">floppycontrol</a></code>(1) manual page.</p>
<h2>Files</h2>
<p>/dev/fd*</p>
<h2>Notes</h2>
<p>The various formats permit reading and writing many types of disks. However, if a floppy is formatted with an inter-sector gap that is too small, performance may drop, to the point of needing a few seconds to access an entire track. To prevent this, use interleaved formats. </p>
<p> It is not possible to read floppies which are formatted using GCR (group code recording), which is used by Apple II and Macintosh computers (800k disks). </p>
<p> Reading floppies which are hard sectored (one hole per sector, with the index hole being a little skewed) is not supported. This used to be common with older 8-inch floppies.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-chown/">chown</a></code>(1), <code><a href="/docs/linux/man/1-floppycontrol/">floppycontrol</a></code>(1), <code><a href="/docs/linux/man/1-getfdprm/">getfdprm</a></code>(1), <code><a href="/docs/linux/man/1-mknod/">mknod</a></code>(1), <code><a href="/docs/linux/man/1-superformat/">superformat</a></code>(1), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-setfdprm/">setfdprm</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 3.53 of the Linux <i>man-pages</i> project. A description of the project, and information about reporting bugs, can be found at <a rel="nofollow" href="http://www.kernel.org/doc/man-pages/.">http://www.kernel.org/doc/man-pages/.</a> </p>
