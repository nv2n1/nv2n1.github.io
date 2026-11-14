---
title: "stinit(8)"
name: "stinit"
section: "8"
letter: "s"
url: "/docs/linux/man/8-stinit/"
description: "stinit – initialize SCSI magnetic tape drives"
---

<p>stinit &#8211; initialize SCSI magnetic tape drives</p>
<h2>Synopsis</h2>
<p><code>stinit</code> [-f conf-file] [-h] [-p] [-r] [-v] [devices&#8230;]</p>
<h2>Description</h2>
<p>This manual page documents the tape control program <code>stinit</code> can used to initialize SCSI tape drive modes at system startup, after loading the tape driver as module, or after introduction of new device to the SCSI subsystem at run-time. The initialization is performed by sending ioctl commands to the drive. The commands are defined in a text file that is indexed using the inquiry data the drive returns (manufacturer, device, revision). Values for all of the general and mode-specific SCSI tape parameters up to Linux version 2.6.0 can be initialized. </p>
<h2>Options</h2>
<dl>
<dt><i>-f conf-file</i></p>
<dd>Specifies the name of the text file containing the definitions for different tape drive types. By default <code>stinit</code> tries to find the definition file <i>stinit.def</i> or <i>/etc/stinit.def</i> (in this order).</p>
<dt><i>-h</i></p>
<dd>Print the usage information.</p>
<dt><i>-p</i></p>
<dd>The definition file is parsed but no tape drive initialization is attempted. This option can be used for testing the integrity of a definition file after changes have been made.</p>
<dt><i>-r</i></p>
<dd>Rewind every device being initialized.</p>
<dt><i>-v</i></p>
<dd>The more -v options (currently up to two), the more verbose output.</p>
<dt><i>&#8211;version</i></p>
<dd>Print the program version.</dl>
<h2>The Devices Being Initialized</h2>
<p>If the program is started without arguments, it tries to find all accessible SCSI tape devices and the device files for the different modes of the devices. The tape drives are searched in the scanning order of the kernel and searching is stopped at the first non-existing tape. All of the found devices are initialized if a matching description is found from the parameter file. Note that a mode for a device is not initialized if the corresponding device file is not found even if a matching description for the mode exists. The non-rewind device is preferred over the auto-rewind device for each mode. If the directory <i>/dev/tapes</i> is found, the devfs filesystem is assumed to be mounted on /dev. Otherwise, the directories <i>/dev/scsi</i> and <i>/dev</i> are scanned for device files. </p>
<p> SCSI tape drives can be initialized selectively using program arguments. A numeric argument specifies the number of the tape drive in the scanning order of the kernel. A file name specifies that the device corresponding to this name is to be initialized. If the file name is given without the directory specification, the program searches for the name in the device directories <i>/dev/scsi</i> and <i>/dev.</i> Only full path names are supported with devfs.</p>
<h2>The Configuration File</h2>
<p>The configuration file is a simple text file that contains descriptions of tape drives and the corresponding initialization parameters. The parameter definition blocks are delimited by <i>{}.</i> Specification of the drive description is restarted after each parameter definition block. </p>
<p> The drive descriptions and the parameter definitions consist of pairs <i>name = value.</i> The value is either a numeric parameter, a string not containing blanks, or a quoted string. In case of a numeric parameter, the postfix <i>k</i> or <i>M</i> can be used to give the value in units of 1024 or 1024 * 1024, respectively. If the <i>=value</i> -part is omitted, the value <i>&quot;1&quot;</i> is used. If the character <i>#</i> is found from an input line, the rest of the line is discarded. This allows use of comments in the definition file. The following example contains definitions for one type of tape drives: </p>
<dl>
<dd>
<pre># The XY dat
manufacturer=XY-COMPANY model = &quot;UVW DRIVE&quot; {
scsi2logical=1 # Common definitions for all modes
can-bsr can-partitions auto-lock
# Definition of modes
mode1 blocksize=0 compression=1
mode2 blocksize=1024 compression=1
mode3 blocksize=0 compression=0
mode4 blocksize = 1k compression=0 }</pre>
</dl>
<p> The devices are identified using zero or more of the following keywords corresponding to the data returned by the tape device as response to the SCSI INQUIRY command. The matches are case-sensitive and performed up to the length defined in the configuration file (permitting use of partial matches).</p>
<dl>
<dt>manufacturer=</p>
<dd>This keyword specifies the string that must match the vendor identification returned by the device.</p>
<dt>model=</p>
<dd>This keyword defines the string that must match the <code>product identification</code> returned by the device.</p>
<dt>revision=</p>
<dd>This keyword matched the string that must match the <code>product revision level</code> returned by the device.</dl>
<p> All of the matching initializations are collected in the order they are defined in the file. This means that common parameters can be defined for all devices using zero keywords for a definition block. Another consequence is that, for instance, some parameters can be easily given different values for a specific firmware revision without repeating the parameters common to all revisions. </p>
<p> The tape parameters are defined using the following keywords. More thorough description of the parameters can be found from the <i><a href="/docs/linux/man/4-st/">st</a>(4)</i> man page (not up to date when this is written) or from the file <i>drivers/scsi/README.st</i> in the Linux kernel source tree. The keywords are matched using only the first characters. The part of the keywords not used in matching is enclosed by []. The numeric values may be specified either in decimal notation or hexadecimal notation (using the prefix 0x).</p>
<dl>
<dt>drive-[buffering]=value</p>
<dd>The drive&#8217;s buffering parameter is set to <i>value.</i> This parameter if common for all modes.</p>
<dt>cleaning</p>
<dd>The cleaning request notifying parameter is set to <i>value</i></p>
<dt>no-w[ait]</p>
<dd>The immediate mode is used with commands like rewind if <i>value</i> is non-zero (i.e., the driver does not wait for the command to finish).</p>
<dt>mode=value</p>
<dd>This keyword starts definition of tape mode <i>value.</i> The number of the mode must be between 1 and 4.</p>
<dt>disab[led]=value</p>
<dd>This mode is disabled for this device if <i>value</i> is non-zero. Can be used if some mode defined in a more general definition should be disabled by a more specific definition for some device (for example, for a device with buggy firmware level).</p>
<dt>block[size]=value</p>
<dd>The default tape block size is set to <i>value.</i> bytes. The block size zero means variable block mode.</p>
<dt>dens[ity]=value</p>
<dd>The tape density code is set to <i>value.</i></p>
<dt>buff[ering]=value</p>
<dd>The buffered writes by the driver in fixed block mode are enabled if <i>value</i> is non-zero.</p>
<dt>async[-writes]=value</p>
<dd>Asynchronous writes by the driver are enabled if <i>value</i> is non-zero.</p>
<dt>read[-ahead]=value</p>
<dd>Read-ahead by the driver in fixed block mode is allowed if <i>value</i> is non-zero.</p>
<dt>two[-fms]=value</p>
<dd>Two filemarks are written when a file being written to is closed if <i>value</i> is non-zero. By default, one filemark is written.</p>
<dt>comp[ression]=value</p>
<dd>Compression of the data by the drive is enabled if <i>value</i> is non-zero. Note that the tape driver can&#8217;t enable compression for all drives that can compress data. Note also that some drives define compression using density codes.</p>
<dt>auto[-lock]=value</p>
<dd>The tape drive door is locked automatically when the device file is opened if <i>value</i> is non-zero.</p>
<dt>fast[-eom]=value</p>
<dd>The MTEOM command is performed using the SCSI command that spaces directly to the end of medium if <i>value</i> is non-zero. The drawback is that the file number in the status becomes invalid. By default, spacing to end of medium is performed by spacing over filemarks until end of medium is detected and the file number remains valid.</p>
<dt>can-b[sr]=value</p>
<dd>Backspacing over records is used by the driver when repositioning the tape when read-ahead is enabled if <i>value</i> is non-zero.</p>
<dt>noblk[limits]=value</p>
<dd>The tape driver does not use the READ BLOCK LIMITS SCSI command when the device is being opened if <i>value</i> is non-zero. This is for the drives that do not support this SCSI command.</p>
<dt>can-p[artitions]=value</p>
<dd>The support for tape partitions is enabled if <i>value</i> is non-zero.</p>
<dt>scsi2[logical]=value</p>
<dd>Logical block addresses are used in the MTSEEK and MTIOCPOS commands if <i>value</i> is non-zero. The default is to use the device-specific addresses.</p>
<dt>sili=value</p>
<dd>If <i>value</i> is non-zero, the SILI bit is set when reading in variable block mode. This may speed up reading blocks shorter than the read byte count. Set this only if you know that the drive supports SILI and the HBA reliably returns transfer residual byte counts. Requires kernel version &gt;= 2.6.26.</p>
<dt>defs-for-w[rites]=value</p>
<dd>The parameters defining the tape format (density, block size, etc.) are forced when writing starts at the beginning of a tape if <i>value</i> is non-zero. The default is to change there parameters each time the device is opened at the beginning of a tape (or the mode is changed in the middle of a tape).</p>
<dt>sysv=value</p>
<dd>The System V tape semantics are used if <i>value</i> is non-zero. Otherwise the BSD semantics are used.</p>
<dt>timeout=value</p>
<dd>The normal timeout for the device is set to <i>value</i> seconds.</p>
<dt>long-time[out]=value</p>
<dd>The long timeout for the device is set to <i>value</i> seconds.</dl>
<h2>Return Value</h2>
<p>The program exits with value one if the command line is incorrect, the definition file is not found, or option -p is given and parsing the definition file fails. In all other cases the return value is zero (i.e., failing of initialization is not currently signaled by the return value).</p>
<h2>Restrictions</h2>
<p>With the exception of the -p option, the program can be used only by the superuser. This is because the program uses ioctls allowed only for the superuser.</p>
<h2>Author</h2>
<p>The program is written by Kai Makisara &lt;Kai.Makisara [at] kolumbus.fi&gt;.</p>
<h2>Copyright</h2>
<p>The program and the manual page are copyrighted by Kai Makisara, 1998-2008. They can be distributed according to the GNU Copyleft.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/4-st/">st</a>(4) <a href="/docs/linux/man/1-mt/">mt</a>(1) </p>
