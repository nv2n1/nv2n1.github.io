---
title: "efax(1)"
name: "efax"
section: "1"
letter: "e"
url: "/docs/linux/man/1-efax/"
description: "efax – send/receive faxes with Class 1, 2 or 2.0 fax modem"
---

<h2 class="name">NAME</h2>
<p> efax &#8211; send/receive faxes with Class 1, 2 or 2.0 fax modem </p>
<p> <center> (Please read the <code>fax</code> man page first.)<br />
 </center> </p>
<h2>SYNOPSIS</h2>
<p> <code>efax</code> [ <i>options</i> ] [ <code>-t</code> <i>num</i> [ <i>file</i>&#8230; ] ] </p>
<h2>OPTIONS</h2>
<p> Where <i>options</i> are: </p>
<dl>
<dt><code>-a </code><i>cmd</i></p>
<dd> use the command <code>ATcmd</code> when answering the phone. The default is &quot;A&quot;. </p>
<dt><code>-c </code><i>caps</i></p>
<dd> set the local modem capabilities. See the section on capabilities below for the format and meaning of <i>caps</i>. For Class 1 the default is 1,n,0,2,0,0,0,0 where n is the highest speed supported by the modem. For Class 2 the default is determined by the modem. </p>
<dt><code>-d </code><i>dev</i></p>
<dd> use the fax modem connected to device <i>dev</i>. The default is <code>/dev/modem</code>. </p>
<dt><code>-f </code><i>fnt</i></p>
<dd> use font file <i>fnt</i> for generating the header. The default is a built-in 8&#215;16 font. See the <a href="/docs/linux/man/1-efix/">efix</a>(1) -f option for the font file format. </p>
<dt><code>-g </code><i>cmd</i></p>
<dd> if a <code>CONNECT</code> (or <code>DATA</code>) response indicates a data call, the shell <code>/bin/sh</code> is <a href="/docs/linux/man/2-exec/">exec</a>(2)&#8217;ed with <i>cmd</i> as its command. <i>cmd</i> is a <a href="/docs/linux/man/3-printf/">printf</a>(3) format that may contain up to 6 %d escapes which are replaced by the baud rate following the most recent <code>CONNECT</code> message. <i>cmd</i> typically exec&#8217;s <a href="/docs/linux/man/8-getty/">getty</a>(8). </p>
<dt><code>-h </code><i>hdr</i></p>
<dd> put string `hdr&#8217; at the top of each page. The first %d in `hdr&#8217; is replaced by the page number and the second, if any, is replaced by the number of pages being sent. </p>
<dt><code>-i </code><i>str</i></p>
<dd>
<dt><code>-j </code><i>str</i></p>
<dd>
<dt><code>-k </code><i>str</i></p>
<dd> send the command <code>AT</code><i>str</i> to the modem to initialize it. -i commands are sent before the modem is put into fax mode, -j commands after the modem is in fax mode, and -k commands just before efax exits. The only default is a hang-up (ATH) command that is sent before exiting only if no other -k options are given. Multiple options may be used. </p>
<dt><code>-l </code><i>id</i></p>
<dd> set the local identification string to <i>id</i>. <i>id</i> should be the local telephone number in international format (for example &quot;+1 800 555 1212&quot;). This is passed to the remote fax machine. Some fax machines may not accept characters other than numbers, space, and &#8216;+&#8217;. </p>
<dt><code>-o </code><i>opt</i></p>
<dd> use option <i>opt</i> to accommodate a non-standard fax modem protocol. See the MODEM REQUIREMENTS section below for more details. The <i>opt</i>ions are: </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0</code></p>
<dd> Force use of Class 2.0 fax modem commands. The modem must support Class 2.0. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2</code></p>
<dd> Force use of Class 2 fax modem commands. The modem must support Class 2. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr></code></p>
<dd> Force use of Class 1 fax modem commands. The modem must support Class 1. By default efax queries the modem and uses the first of the three above classes which is supported by the modem. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>a</code></p>
<dd> use software adaptive answer method. If the first attempt to answer the call does not result in a data connection within 8 seconds the phone is hung up temporarily and answered again in fax mode (see &quot;Accepting both fax and data calls&quot; below). </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>e&nbsp;<wbr></code></p>
<dd> ignore errors in modem initialization commands. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>f</code></p>
<dd> use &quot;virtual flow control&quot;. efax tries to estimate the number of bytes in the modem&#8217;s transmit buffer and pauses as necessary to avoid filling it. The modem&#8217;s buffer is assumed to hold at least 96 bytes. This feature does not work properly with Class 2 modems that add redundant padding to scan lines. Use this option only if you have problems configuring flow control. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>h&nbsp;<wbr></code></p>
<dd> use hardware (RTS/CTS) in addition to software (XON/XOFF) flow control. Many modems will stop responding if this option is used. See the section `Resolving Problems&#8217; before using this option. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>l</code></p>
<dd> halve the time between testing lock files when waiting for other programs to complete. By default this is 8 seconds. For example -olll sets the interval to 1 second. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>n</code></p>
<dd> ignore requests for pages to be retransmitted. Use this option if you don&#8217;t care about the quality of the received fax or if the receiving machine is too fussy. Otherwise each page may be retransmitted up to 3 times. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r</code></p>
<dd> do not reverse bit order during data reception for Class 2 modems. Only Multitech modems require this option. Not normally required since efax detects these modems. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>x</code></p>
<dd> send XON (DC1) instead of DC2 to start data reception. Applies to a very few Class 2 modems only. </p>
<dt><code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>z</code></p>
<dd> delay an additional 100 milliseconds before each modem initialization or reset command. The initial delay is 100 ms. For example, -ozzz produces a 400 ms delay. Use with modems that get confused when commands arrive too quickly. </p>
<dt><code>-q </code><i>n</i></p>
<dd> ask for retransmission of pages received with more than <i>n</i> errors. Default is 10. </p>
<dt><code>-r </code><i>pat</i></p>
<dd> each received fax page is stored in a separate file. The file name is created using <i>pat</i> as a <a href="/docs/linux/man/3-strftime/">strftime</a>(3) format string. A page number of the form .001, .002, &#8230; is appended to the file name. If <i>pat</i> is blank (&quot;&quot;) or no -r option is given a default string of &quot;%m%d%H%M%S&quot; is used. </p>
<dt><code>-s</code></p>
<dd> remove lock file(s) after initializing the modem. This allows outgoing calls to proceed when efax is waiting for an incoming call. If efax detects modem activity it will attempt to re-lock the device. If the modem has been locked by the other program efax will exit and return 1 (&#8220;busy&#8221;). Normally a new efax process is then started by <a href="/docs/linux/man/8-init/">init</a>(8). The new efax process will then check periodically until the lock file disappears and then re-initialize the modem. </p>
<dt><code>-t </code><i>num [file</i>&#8230;]</p>
<dd> dial telephone number <i>num</i> and send the fax image files <i>file</i>&#8230;. If used, this must be the last argument on the command line. The telephone number <i>num</i> is a string that may contain any dial modifiers that the modem supports such as a T prefix for tone dialing or commas for delays. If no file names are given the remote fax machine will be polled. If no -t argument is given efax will answer the phone and attempt to receive a fax. </p>
<dt><code>-v </code><i>strng</i></p>
<dd> select types of messages to be printed. Each <i>lower-case</i> letter in <i>strng</i> enables one type of message: </p>
<dl>
<dt>
<dd> <code>e &#8211; </code> errors<br />
 <code>w &#8211; </code> warnings<br />
 <code>i &#8211; </code> session progress information<br />
 <code>n &#8211; </code> capability negotiation information<br />
 <code>c &#8211; </code> modem (AT) commands and responses<br />
 <code>h &#8211; </code> HDLC frame data (Class 1 only)<br />
 <code>m &#8211; </code> modem output<br />
 <code>a &#8211; </code> program arguments<br />
 <code>r &#8211;</code> reception error details<br />
 <code>t &#8211;</code> transmission details<br />
 <code>f &#8211;</code> image file details<br />
 <code>x &#8211;</code> lock file processing </p>
</dl>
<dl>
<dt>
<dd> Up to two -v options may be used. The first is for messages printed to the standard error and the second is for messages to the standard output. The default is &quot;ewin&quot; to the standard error only.</dl>
<dt><code>-w</code></p>
<dd> wait for an OK or CONNECT prompt instead of issuing an answer (<code>ATA</code>) command to receive a fax. Use this option when the modem is set to auto-answer (using S0=<i>n</i>) or if another program has already answered the call. </p>
<dt><code>-x </code><i>lkf</i></p>
<dd> use a UUCP-style lock file <i>lkf</i> to lock the modem device before opening it. If the device is locked, efax checks every 15 seconds until it is free. Up to 16 -x options may be used if there are several names for the same device. A `#&#8217; prefix on the file name creates an binary rather than text (HDB-style) lock file. This is the reverse of what was used by previous efax versions. </p>
</dl>
<h2>FAX FILE FORMATS</h2>
<p> efax can read the same types of files as <code><a href="/docs/linux/man/1-efix/">efix</a>(1)</code> including text, T.4 (Group 3), PBM, single- and multi-page TIFF (G3 and uncompressed). efax automatically determines the type of file from its contents. TIFF files are recommended as they contain information about the image size and resolution. </p>
<p> Each page to be sent should be converted to a separate TIFF format file with Group 3 (G3) compression. Received files are also stored in this format. The EXAMPLES section below shows how efix and other programs can be used to create, view and print these files. </p>
<h2>OPERATING SYSTEM REQUIREMENTS</h2>
<p> The operating system must provide short response times to avoid protocol timeouts. For Class 2 and 2.0 modems the delay should not exceed 1 or 2 seconds. </p>
<p> When using Class 1 modems the program must respond to certain events within 55 milliseconds. Longer delays may cause the fax protocol to fail in certain places (between DCS and TCF or between RTC and MPS). Class 1 modems should therefore not be used on systems that cannot guarantee that the program will respond to incoming data in less than 55 milliseconds. In particular, some intelligent serial cards and terminal servers may introduce enough delay to cause problems with Class 1 operation. </p>
<p> The operating system must also provide sufficient low-level buffering to allow uninterrupted transfer of data between the modem and a disk file at the selected baud rate, typically 9600 bps. Since the fax protocol does not provide end-to-end flow control the effectiveness of flow control while receiving is limited by the size of the modem&#8217;s buffer. This can be less than 100 bytes. Efax does not use flow control during reception. </p>
<h2>MODEM REQUIREMENTS</h2>
<p> The &quot;Group&quot; is the protocol used to send faxes between fax machines. Efax supports the Group 3 protocol used over the public telephone network. </p>
<p> The &quot;Class&quot; is the protocol used by computers to control fax modems. Efax supports Class 1, 2 and 2.0 fax modems. </p>
<p> Most fax modems use XON/XOFF flow control when in fax mode. This type of flow control adds very little overhead for fax use. Many modems have unreliable hardware (RTS/CTS) flow control in fax mode. By default efax enables only XON/XOFF flow control and the -oh option must be used to add hardware flow control. </p>
<p> While some modems have serial buffers of about 1k bytes, many inexpensive modems have buffers of about one hundred bytes and are thus more likely to suffer overruns when sending faxes. </p>
<p> A few older modems may need a delay between commands of more than the default value used by efax (100 milliseconds). If the delay is too short, commands may not echo properly, may time out, or may give inconsistent responses. Use one or more <code>-oz</code> options to increase the delay between modem initialization commands and use the E0 modem initialization command to disable echoing of modem commands. </p>
<p> By default efax sends DC2 to start the data flow from the modem when receiving faxes from Class 2 modems. A few older modems require XON instead. Use of DC2 would cause the modem to give an error message and/or the program to time out. The <code>-ox</code> option should be used in this case. </p>
<p> A few older Class 2 modems (e.g. some Intel models) don&#8217;t send DC2 or XON to start the data flow to the modem when sending faxes. After waiting 2 seconds efax will print a warning and start sending anyways. </p>
<p> A very few Class 2 modems do not reverse the bit order (MSB to LSB) by default on receive. This might cause errors when trying to display or print the received files. The <code>-or</code> option can be used in this case. </p>
<p> Some inexpensive &quot;9600 bps&quot; fax modems only <i>transmit</i> at 9600 bps and reception is limited to 4800 bps. </p>
<p> The following Class 1 modems have been reported to work with efax: AT&amp;T DataPort, Cardinal Digital Fax Modem (14400), Digicom Scout+, Motorola Lifestyle 28.8, Motorola Power 28.8, QuickComm Spirit II, Smartlink 9614AV-Modem, Supra Faxmodem 144LC, USR Courier V.32bis Terbo, USR Sportster (V.32 and V.34), Zoom AFC 2.400, Zoom VFX14.4V. </p>
<p> The following Class 2 modems have been reported to work with efax: 14k4 Amigo Communion fax/modem, Adtech Micro Systems 14.4 Fax/modem, askey modem type 1414VQE, AT&amp;T DataPort, ATT/Paradyne, AT&amp;T Paradyne PCMCIA, Boca modem, BOCA M1440E, Crosslink 9614FH faxmodem, FuryCard DNE 5005, GVC 14.4k internal, Intel 14.4 fax modem, Megahertz 14.4, ,Microcom DeskPorte FAST ES 28.8, Motorola UDS FasTalk II, MultiTech 1432MU, Practical Peripherals PM14400FXMT, Supra V32bis, Telebit Worldblazer, TKR DM-24VF+, Twincom 144/DFi, ViVa 14.4/Fax modem, Vobis Fax-Modem (BZT-approved), Zoom VFX14.4V, ZyXEL U-1496E[+], ZyXEL Elite 2864I. </p>
<h2>MODEM INITIALIZATION OPTIONS</h2>
<p> The required modem initialization commands are generated by efax. Additional commands may be supplied as command-line arguments. The modem must be set up to issue verbose(text) result codes. The following command does this and is sent by efax before trying to initialize the modem. </p>
<dl>
<dt><code>Q0V1</code></p>
<dd> respond to commands with verbose result codes </p>
</dl>
<p> The following commands may be useful for special purposes: </p>
<dl>
<dt><code>X3</code></p>
<dd> don&#8217;t wait for dial tone before dialing. This may be used to send a fax when the call has already been dialed manually. In this case use an empty string (&quot;&quot;) as the first argument to the <code>-t</code> command. Use <code>X4</code> (usual default) to enable all result codes. </p>
<dt><code>M2</code></p>
<dd> leave the monitor speaker turned on for the duration of the call (use <code>M0</code> to leave it off). </p>
<dt><code>L0</code></p>
<dd> turn monitor speaker volume to minimum (use <code>L3</code> for maximum). </p>
<dt><code>E0</code></p>
<dd> disable echoing of modem commands. See the Resolving Problems section below. </p>
<dt><code>&amp;D2</code></p>
<dd> returns the modem to command mode when DTR is dropped. The program drops DTR at the start and end of the call if it can&#8217;t get a response to a modem command. You can use <code>&amp;D3</code> to reset the modem when DTR is dropped. </p>
<dt><code>S7=120</code></p>
<dd> wait up to two minutes (120 seconds) for carrier. This may be useful if the answering fax machine takes a long time to start the handshaking operation (e.g. a combined fax/answering machine with a long announcement). </p>
</dl>
<h2>CAPABILITIES</h2>
<p> The capabilities of the local hardware and software can be set using a string of 8 digits separated by commas: </p>
<p> <i>vr</i>,<i>br</i>,<i>wd</i>,<i>ln</i>,<i>df</i>,<i>ec</i>,<i>bf</i>,<i>st</i> </p>
<p> where: </p>
<dl>
<dt><i>vr </i> (vertical resolution) =</p>
<dd> 0 for 98 lines per inch<br />
 1 for 196 lpi </p>
<dt><i>br </i> (bit rate) =</p>
<dd> 0 for 2400 bps<br />
 1 for 4800<br />
 2 for 7200<br />
 3 for 9600<br />
 4 for 12000 (V.17)<br />
 5 for 14400 (V.17) </p>
<dt><i>wd </i> (width) =</p>
<dd> 0 for 8.5&quot; (21.5 cm) page width<br />
 1 for 10&quot; (25.5 cm)<br />
 2 for 12&quot; (30.3 cm) </p>
<dt><i>ln </i> (length) =</p>
<dd> 0 for 11&quot; (A4: 29.7 cm) page length<br />
 1 for 14&quot; (B4: 36.4 cm)<br />
 2 for unlimited page length </p>
<dt><i>df </i> (data format) =</p>
<dd> 0 for 1-D coding<br />
 1 for 2-D coding (not supported) </p>
<dt><i>ec </i> (error correction) =</p>
<dd> 0 for no error correction </p>
<dt><i>bf </i> (binary file) =</p>
<dd> 0 for no binary file transfer </p>
<dt><i>st </i> (minimum scan time) =</p>
<dd> 0 for zero delay per line<br />
 1 for 5 ms per line<br />
 3 for 10 ms per line<br />
 5 for 20 ms per line<br />
 7 for 40 ms per line </p>
</dl>
<p> When <i>receiving</i> a fax the <i>vr</i>, <i>wd</i>, and <i>ln</i> fields of the capability string should be set to the maximum values that your display software supports. The default is 196 lpi, standard (8.5&quot;/21.5cm) width and unlimited length. </p>
<p> When <i>sending</i> a fax efax will determine <i>vr</i> and <i>ln</i> from the image file and set <i>wd</i> to the default. </p>
<p> If the receiving fax machine does not support high resolution (<i>vr</i>=1) mode, efax will reduce the resolution by combining pairs of scan lines. If the receiving fax machine does not support the image&#8217;s width then efax will truncate or pad as required. Most fax machines can receive <i>ln</i> up to 2. Few machines support values of <i>wd</i> other than 0. </p>
<h2>HEADERS</h2>
<p> efax adds blank scan lines at the top of each image when it is sent. This allows room for the page header but increases the length of the image (by default about 0.1&quot; or 2.5mm of blank space is added). </p>
<p> The header placed in this area typically includes the date and time, identifies the, and shows the page number and total pages. Headers cannot be disabled but the header string can be set to a blank line. </p>
<p> The default font for generating the headers is the built-in 8&#215;16 pixel font scaled to 12&#215;24 pixels (about 9 point size). </p>
<p> Note that both efax and efix have -f options to specify the font. efIx uses the font to generate text when doing text-to-fax conversions (during &quot;fax make&quot;) while efAx uses the font to generate the header (during &quot;fax send&quot;). </p>
<h2>SESSION LOG</h2>
<p> A session log is written to the standard error stream. This log gives status and error messages from the program as selected by the <code>-v</code> option. A time stamp showing the full time or just minutes and seconds is printed before each message. Times printed along with modem responses also show milliseconds. </p>
<h2>RETURN VALUES</h2>
<p> The program returns an error code as follows: </p>
<dl>
<dt>0</p>
<dd> The fax was successfully sent or received. </p>
<dt>1</p>
<dd> The dialed number was busy or the modem device was in use. Try again later. </p>
<dt>2</p>
<dd> Something failed (e.g. file not found or disk full). Don&#8217;t retry. Check the session log for more details. </p>
<dt>3</p>
<dd> Modem protocol error. The program did not receive the expected response from the modem. The modem may not have been properly initialized, the correct <code>-o</code> options were not used, or a bug report may be in order. Check the session log for more details. </p>
<dt>4</p>
<dd> The modem is not responding. Operator attention is required. Check that the modem is turned on and connected to the correct port. </p>
<dt>5</p>
<dd> The program was terminated by a signal. </p>
</dl>
<h2>EXAMPLES</h2>
<p> <code>Creating fax (G3) files</code> </p>
<p> The efix program can be used to convert text files to TIFF-G3 format. For example, the following command will convert the text file <code>letter</code> to the files <code>letter.001</code>, <code>letter.002</code>, etc,: </p>
<dl>
<dt>
<dd>
<pre>
efix -nletter.%03d letter
</pre>
</dl>
<p> Ghostscript&#8217;s <code>tiffg3</code> driver can generate fax files in TIFF-G3 format from postscript files. For example, the command: </p>
<dl>
<dt>
<dd>
<pre>
<tt> gs -q -sDEVICE=tiffg3 -dNOPAUSE \
        -sOutputFile=letter.%03d letter.ps &lt;/dev/null</tt>
</pre>
</dl>
<p> will convert the Postscript file <code>letter.ps</code> into high-resolution (<i>vr</i>=1) G3 fax image files <code>letter.001, letter.002,</code> &#8230; </p>
<p> The images should have margins of at least 1/2 inch (1 cm) since the fax standard only requires that fax machines print a central portion of the image 196.6mm (7.7 inches) wide by 281.5mm (11.1 inches) high. </p>
<p> The efix program can also insert bitmaps in images to create letterhead, signatures, etc. </p>
<p> <code>Printing fax files</code> </p>
<p> You can use the efix program to print faxes on Postscript or HP-PCL (LaserJet) printers. For example, to print the received fax file <code>reply.001</code> on a Postscript printer use the command: </p>
<dl>
<dt>
<dd>
<pre>
efix -ops reply.001 | lpr
</pre>
</dl>
<p> <code>Sending fax files</code> </p>
<p> The following command will dial the number 222-2222 using tone dialing and send a two-page fax from the TIFF-G3 files letter.001 and letter.002 using the fax modem connected to device /dev/cua1. </p>
<dl>
<dt>
<dd>
<pre>
efax -d /dev/cua1 \
     -t T222-2222 letter.001 letter.002
</pre>
</dl>
<p> <code>Manual answer</code> </p>
<p> You can use efax to answer the phone immediately and start fax reception. Use this mode if you need to answer calls manually to see if they are fax or voice. </p>
<p> For example, the following command will make the fax modem on device <code>/dev/ttyS1</code> answer the phone and attempt to receive a fax. The received fax will be stored in the files <code>reply.001</code>, <code>reply.002</code>, and so on. The modem will identify itself as &quot;555 1212&quot; and receive faxes at high or low resolution (<i>vr</i>=1), at up to 14.4 kbps (<i>br</i>=5). </p>
<dl>
<dt>
<dd>
<pre>
efax -d /dev/ttyS1 -l &quot;555 1212&quot; \
   -c 1,5 -r reply
</pre>
</dl>
<p> <code>Automatic answer</code> </p>
<p> The <code>-w</code> option makes efax wait for characters to become available from the modem (indicating an incoming call) before starting fax reception. Use the <code>-w</code> option and a <code>-i</code>S0=<i>n</i> option to answer the phone after <i>n</i> rings. The example below will make the modem answer incoming calls in fax mode on the fourth ring and save the received faxes using files names corresponding to the reception date and time. </p>
<dl>
<dt>
<dd>
<pre>
efax -d /dev/ttyb -w -iS0=4 2&gt;&amp;1 &gt;&gt; fax.log
</pre>
</dl>
<p> <code>Sharing the modem with outgoing calls</code> </p>
<p> The modem device can be shared by programs that use the UUCP device locking protocol. This includes pppd, chat, minicom, kermit, uucico, efax, cu, and many others others. However, locking will only work if all programs use the same lock file. </p>
<p> efax will lock the modem device before opening it if one or more UUCP lock file names are given with <code>-x</code> options. Most programs place their lock files in the <code>/usr/spool/uucp</code> or <code>/var/lock</code> directories and use the name <code>LCK..</code><i>dev</i> where <i>dev</i> is the name of the device file in the /dev directory that is to be locked. </p>
<p> If the <code>-s</code> (share) option is used, the lock file is removed while waiting for incoming calls so other programs can use the same device. </p>
<p> If efax detects another program using the modem while it is waiting to receive a fax, efax exits with a termination code of 1. A subsequent efax process using this device will wait until the other program is finished before re-initializing the modem and starting to wait for incoming calls again. </p>
<p> Programs that try to lock the modem device by using device locking facilities other than UUCP lock files not be able to use this arbitration mechanism because the device will still be open to the efax process. In this case you will need to kill the efax process (e.g. &quot;fax stop&quot;) before starting the other program. </p>
<p> When efax is waiting for a fax it leaves the modem ready to receive in fax mode but removes the lock file. When a slip or PPP program takes over the modem port by setting up its own lock file efax cannot send any more commands to the modem &#8212; not even to reset it. Therefore the other program has to set the modem back to data mode when it starts up. To do this add a modem reset command (send ATZ expect OK) to the beginning of your slip or PPP chat script. </p>
<p> <code>Accepting both fax and data calls</code> </p>
<p> Many modems have an adaptive data/fax answer mode that can be enabled using the <code>-j+FAE=1</code> (for Class 1) or <code>-jFAA=1</code> (for Class 2[.0]) initialization string. The type of call (data or fax) can then be deduced from the modem&#8217;s responses. </p>
<p> Some modems have limited adaptive answer features (e.g. only working properly at certain baud rates or only in Class 2) or none at all. In this case use the initialization string <code>-i+FCLASS=0</code> to answer in data mode first and the <code>-oa</code> option to then hang up and try again in fax mode if the first answer attempt was not successful. This method only works if your telephone system waits a few seconds after you hang up before disconnecting incoming calls. </p>
<p> If the <code>-g</code> option is used then the option&#8217;s argument will be run as a shell command when an incoming data call is detected. Typically this command will exec <code><a href="/docs/linux/man/8-getty/">getty</a></code>(8). This program should expect to find the modem already off-hook and a lock file present so it should not try to hang up the line or create a lock file. Note that the modem should be set up to report the DCE-DTE (modem-computer, e.g. CONNECT 38400) speed, not the DCE-DCE (modem-modem, e.g. CONNECT 14400) speed. For many modems the initialization option -iW0 will set this. </p>
<p> The following command will make efax answer incoming calls on <code>/dev/cua1</code> on the second ring. This device will be locked using two different lock files but these lock files will be removed while waiting for incoming calls (<code>-s</code>). If a data call is detected, the <code>getty</code> program will be run to initialize the terminal driver and start a <code><a href="/docs/linux/man/1-login/">login</a></code>(1) process. Received fax files will be stored using names like <code>Dec02-12.32.33.001</code>, in the <code>/usr/spool/fax/incoming</code> directory and the log file will be appended to <code>/usr/spool/fax/faxlog.cua1</code>. </p>
<dl>
<dt>
<dd>
<pre>
efax -d /dev/cua1  -j '+FAA=1' \
   -x /usr/spool/uucp/LCK..cua1 \
   -x /usr/spool/uucp/LCK..ttyS1 \
   -g &quot;exec /sbin/getty -h /dev/cua1 %d&quot; \
   -iS0=2 -w -s \
   -r &quot;/usr/spool/fax/incoming/%b%d-%H.%I.%S&quot; \
   &gt;&gt; /usr/spool/fax/faxlog.cua1 2&gt;&amp;1
</pre>
</dl>
<p> Note that adaptive answer of either type will not work for all callers. For some data calls the duration of the initial data-mode answer may be too short for data handshaking to complete. In other cases this duration may be so long that incoming fax calls will time out before efax switches to fax mode. In addition, some calling fax modems mistake data-mode answering tones for fax signaling tones and initiate fax negotiation too soon. If you use software adaptive answer you can reduce the value of the initial data-mode answer (set by TO_DATAF in efax.c) to get more reliable fax handshaking or increase it for more reliable data handshaking. However, if you need to provide reliable fax and data service to all callers you should use separate phone numbers for the two types of calls. </p>
<p> When a call is answered the modem goes on-line with the computer-to-modem baud rate fixed at the speed used for the most recent AT command. When efax is waiting for a fax or data call it sets the interface speed to 19200 bps since this is the speed required for fax operation. This prevents full use of 28.8kbps modem capabilities. </p>
<h2>USING INIT TO RUN EFAX</h2>
<p> efax can answer all incoming calls if you place an entry for efax in <code>/etc/inittab</code> (for SysV-like systems) or <code>/etc/ttytab</code> (for BSD-like systems). The <code><a href="/docs/linux/man/8-init/">init</a></code>(8) process will run a new copy of efax when the system boots up and whenever the previous efax process terminates. The inittab or ttytab entry should invoke efax by running the <code>fax</code> script with an <code>answer</code> argument. </p>
<p> For example, placing the following line in <code>/etc/inittab</code> (and running &quot;kill -1 1&quot;) will make init run the <code>fax</code> script with the argument <code>answer</code> every time previous process terminates and <code>init</code> is in runlevel 4 or 5. </p>
<dl>
<dt>
<dd>
<pre>
s1:45:respawn:/bin/sh /usr/bin/fax answer
</pre>
</dl>
<p> For BSD-like systems (e.g. SunOS), a line such as the following in <code>/etc/ttytab</code> will have the same effect: </p>
<dl>
<dt>
<dd>
<pre>
ttya &quot;/usr/local/bin/fax answer&quot; unknown on
</pre>
</dl>
<p> You should protect the fax script and configuration files against tampering since init will execute them as a privileged (root) process. If you will be allowing data calls via getty and login you should ensure that your system is reasonably secure (e.g. that all user id&#8217;s have secure passwords). </p>
<p> If efax exec()&#8217;s getty properly but you get a garbled login prompt then there is probably a baud rate mismatch between the modem and the computer. First, check the efax log file to make sure the modem&#8217;s CONNECT response reported the serial port speed (e.g. 19200), <code>not</code> the modem-modem speed (e.g. 14400). Next, check the getty options and/or configuration files (e.g. /etc/gettydefs) for that particular baud rate. Then run getty manually with the same arguments and verify the port settings using &#8220;stty &lt;/dev/XXX&#8221;. Note that you&#8217;ll probably want to enable hardware flow control for data connections (-h for agetty, CRTSCTS for getty_ps). </p>
<p> A few programs won&#8217;t work properly when efax is set up to answer calls because they don&#8217;t create lock files. You can put the shell script &#8220;wrapper&#8221; below around such programs to make them work properly. Change BIN and LOCKF to suit. </p>
<dl>
<dt>
<dd>
<pre><code>
#!/ bin / sh
BIN = / bin / badprogram LOCKF = / var / spool / uucp / LCK..cua1 if[-f $LOCKF] then echo lock file $LOCKF exists exit 1 else printf "%10d $$ &gt;$LOCKF
                                                        $BIN $ *
                                 rm $LOCKF
                                     fi
</code></pre>
</dl>
<h2>DELIVERING RECEIVED FAXES BY E-MAIL</h2>
<p> The &quot;fax answer&quot; script described above can be configured to e-mail the fax files received by the previous fax answer process to a &quot;fax manager&quot; who can then forward the fax to the correct recipient. The received fax files are send as MIME attachments, one file per page, using the &#8220;base64&#8221; text encoding and the &#8220;image/tiff&#8221; file format. </p>
<p> To view the fax images directly from your e-mail reader you will have to configure it with an application that can display files of type image/tiff. Typically this is specified in a &#8220;mailcap&#8221; file. For example, placing the following line in /etc/mailcap will cause the fax file attachments to be displayed using the &#8220;fax view&#8221; command. </p>
<p> image/tiff; fax view %s </p>
<h2>SENDING FAXES USING THE PRINT SPOOLER</h2>
<p> You can configure a &quot;fax&quot; printer into the lpr print spooler that will fax a document out using efax instead of printing it. This allows a network server running efax to send faxes on behalf of other machines, including non-Unix clients. In the following steps use the directories specified in the fax script if they are different than /usr/bin and /var/spool/fax (FAXDIR). To set up a fax printer do the following as root: </p>
<p> (1) Create a link to the fax script called &#8220;faxlpr&#8221; so the fax script can determine when it is being invoked from the print spooler: </p>
<p> ln -s /usr/bin/fax /usr/bin/faxlpr </p>
<p> (2) Edit /etc/printcap and add an entry such as: </p>
<dl>
<dt>
<dd>
<pre>
fax:lp=/dev/null:sd=/var/spool/fax:if=/usr/bin/faxlpr:
</pre>
</dl>
<p> to define a printer called &quot;fax&quot;. Print files will be spooled to the /var/spool/fax (sd=) directory and then piped to the /usr/bin/faxlpr filter (if=). Error messages will appear on /dev/console. </p>
<p> (3) Create and/or set the permissions to allow anyone to read and write in the fax spool directory. For example: </p>
<dl>
<dt>
<dd>
<pre>
mkdir /var/spool/fax
chmod 777 /var/spool/fax
</pre>
</dl>
<p> (4) Create a printer daemon lock file that is readable by anyone: </p>
<dl>
<dt>
<dd>
<pre>
touch /var/spool/fax/lock
chmod 644 /var/spool/fax/lock
</pre>
</dl>
<p> You should now be able to send a fax using the lpr interface by using a command such as: </p>
<dl>
<dt>
<dd>
<pre>
lpr -P fax -J &quot;555 1212&quot; file.ps
</pre>
</dl>
<p> where the -J option is used to specify the phone number or alias to be dialed. </p>
<p> Note that if more than one file is given on the command line they will be concatenated before being passed to &quot;fax send&quot;. TIFF-G3, Postscript or PBM files must therefore be sent one file at a time although TIFF and Postscript files may contain multiple pages. Only multiple <i>text</i> files can be sent in one command. Page breaks in text files can be marked with form-feed characters. Files will be converted and sent at the default (high) resolution. </p>
<p> You can use <a href="/docs/linux/man/1-lpq/">lpq</a>(1) to check the fax queue, <a href="/docs/linux/man/1-lprm/">lprm</a>(1) to remove fax jobs and <a href="/docs/linux/man/8-lpc/">lpc</a>(8) to control the spooler. In each case use the -Pfax option to specify the fax &#8220;printer.&#8221; A log file will be mailed to the user when the fax is sent. </p>
<p> You should also be able to send a fax from any networked computer that has lpr-compatible remote printing software and that allows you to set the job name (-J option) to an arbitrary string. Such software is available for most computers. </p>
<p> See the <a href="/docs/linux/man/8-lpd/">lpd</a>(8) and <a href="/docs/linux/man/5-printcap/">printcap</a>(5) man pages for information on the print spooler and for restricting access by host name (/etc/host.lpd) or by user group (the `rg&#8217; printcap entry). </p>
<h2>RESOLVING PROBLEMS</h2>
<p> Double check the configuration setup in the first part of the fax script, particularly the modem device name and the lock file names. </p>
<p> If efax hangs when trying to open the modem device (typically /dev/ttyX), the device is either already in use by another process (e.g. pppd) or it requires the carrier detect line to be true before it can be opened. Many systems define an alternate device name for the same physical device (typically cuaX) that can be opened even if carrier is not present or other programs are already using it. </p>
<p> If responses to modem initialization commands are being lost or generated at random, another processes (e.g. getty or an efax auto-answer process) may be trying to use the modem at the same time. Try running efax while this other program is running. If efax does not report &quot;/dev/ttyX locked or busy. waiting.&quot; then the lock files names are not specified correctly. </p>
<p> Attempt to send a fax. Check that the modem starts making the calling signal (CNG, a 0.5 second beep every 3 seconds) as soon as it&#8217;s finished dialing. This shows the modem is in fax mode. You may need to set the SPKR variable to -iM2L3 to monitor the phone line to do this. </p>
<p> Listen for the answering fax machine and check that it sends the answer signal (CED, a 3 second beep) followed by &quot;warbling&quot; sounds (DIS frames) every 3 seconds. If you hear a continuous sound (tones or noise) instead, then you&#8217;ve connected to a data modem instead. </p>
<p> Your modem should send back its own warble (DCS frame) in response to DIS immediately followed by 1.5 seconds of noise (a channel check). If everything is OK, the receiving end will send another warble (CFR frame) and your modem will start to send data. If you have an external modem, check its LEDs. If flow control is working properly the modem&#8217;s send data (SD) LED will turn off periodically while the fax data is sent. </p>
<p> Check the message showing the line count and the average bit rate when the page transmission is done. Low line counts (under 1000 for a letter size image) or the warning &quot;fax output buffer overflow&quot; while sending indicate that the image data format is incorrect. Check the file being sent using the &quot;fax view&quot; command. </p>
<p> If you get the error message &#8220;flow control did not work&#8221; then flow control was not active. This usually results in a garbled transmission and the receiving machine may reject the page, abort the call, print a distorted or blank image and/or hang up. </p>
<p> The warning &quot;characters received while sending&quot; or an &lt;XOFF&gt; character appearing after the transmission means that the operating system ignored the modem&#8217;s XOFF flow control character. Ensure that you are not running other programs such as getty or pppd at the same time as efax since they will turn off xon/xoff flow control. </p>
<p> If you cannot get flow control to work properly then enable &#8220;virtual flow control&#8221; with the <code>-of</code> option or hardware flow control with the <code>-oh</code> option. </p>
<p> Check that the remote machine confirms reception with a +FPTS:1 response (Class 2) or an MCF frame (Class 1). </p>
<p> For Class 2 modems, the error message &quot;abnormal call termination (code <i>nn</i>)&quot; indicates that the modem detected an error and hung up. </p>
<p> Many companies advertise services that will fax back information on their products. These can be useful for testing fax reception. </p>
<p> The message &quot;run length buffer overflow&quot; when receiving indicates an error with the image data format. You may need to use the <code>-or</code> option with certain Class 2 modems. </p>
<p> If efax displays the message &quot;can&#8217;t happen (&lt;details&gt;)&quot; please send a bug report to the author. </p>
<p> Finally, don&#8217;t play &quot;option bingo,&quot; if you can&#8217;t resolve the problem send a verbose log of the failed session (the output from <code>fax -v &#8230;</code>) to the address below. </p>
<h2>WEB PAGE</h2>
<p> A Web Page with pointers to the latest version, known bugs and patches is available at:</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://casas.ee.ubc.ca/efax/">http://casas.ee.ubc.ca/efax/</a></dl>
<h2>RELATED SOFTWARE</h2>
<p> For Linux Systems </p>
<p> Independent packages provide more user-friendly interfaces to efax (xfax, tefax) and provide an e-mail-to-fax (Qfax) gateway using efax. All are available by anonymous FTP from metalab.unc.edu in /pub/Linux/apps/serialcomm/fax/. </p>
<p> For Amiga Systems </p>
<p> A port of an early version of efax for the Amiga is available as a component of a shareware voice mail package, AVM, distributed by Al Villarica (rvillari [at] cat.syr.edu). </p>
<p> Other Ports </p>
<p> efax is relatively easy to port. All system-dependent code is in <code>efaxos.c</code>. An early version of efax was ported to VMS. Version 0.8a was ported to Win32 by Luigi Capriotti. Contact the author if you would like to integrate the Win32 code into the current version. </p>
<h2>AUTHOR</h2>
<p> Efax was written by Ed Casas. Please send comments or bug reports to edc [at] cce.com. </p>
<h2>BUG REPORTS</h2>
<p> Bug reports should include the operating system, the type of the modem and a copy of a verbose session log that demonstrates the problem. It&#8217;s usually impossible to help without a verbose log. Please do <code>not</code> send fax image files. </p>
<h2>COPYRIGHT</h2>
<p> efax is copyright 1993 &#8212; 1999 Ed Casas. It may be used, copied and modified under the terms of the GNU Public License. </p>
<h2>DISCLAIMER</h2>
<p> Although <code>efax</code> has been tested it may have errors that will prevent it from working correctly on your system. Some of these errors may cause serious problems including loss of data and interruptions to telephone service. </p>
<h2>REFERENCES</h2>
<p> CCITT Recommendation T.30, &quot;Procedures for Document Facsimile Transmission in the General Switched Telephone Network&quot;. 1988 </p>
<p> CCITT Recommendation T.4, &quot;Standardization of Group 3 Facsimile Apparatus for Document Transmission&quot;. 1988. </p>
<p> For documentation on Class 1 and Class 2 fax commands as implemented by Connexant (formerly Rockwell) modems see <a rel="nofollow" href="http://www.conexant.com/techinfo.">http://www.conexant.com/techinfo.</a> </p>
<p> For the TIFF specification see <a rel="nofollow" href="http://partners.adobe.com/supportservice/devrelations/PDFS/TN/TIFF6.pdf">http://partners.adobe.com/supportservice/devrelations/PDFS/TN/TIFF6.pdf</a> or RFC 2301 (<a href="ftp://ftp.isi.edu/in-notes/rfc2301.txt">ftp://ftp.isi.edu/in-notes/rfc2301.txt</a>). </p>
<p> For information on Ghostscript see <a rel="nofollow" href="http://www.cs.wisc.edu/~ghost/.">http://www.cs.wisc.edu/~ghost/.</a> </p>
<p> The pbm utilities can be obtained by ftp from wuarchive.wustl.edu in /graphics/graphics/packages/NetPBM/netpbm-1mar1994.tar.gz. </p>
<p> PCX and many other file formats are described in: Gunter Born, The File Formats Handbook, International Thomson Computer Press, 1995. </p>
<p> The &quot;Fax Modem Source Book&quot; by Andrew Margolis, published by John Wiley &amp; Sons in 1994 (ISBN 0471950726), is a book on writing fax applications which includes source code. </p>
<p> Dennis Bodson et. al., &quot;FAX: Digital Facsimile Technology and Applications&quot;, Second Edition. Artech House, Boston. 1992. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fax/">fax</a>(1),</code> <code><a href="/docs/linux/man/1-efix/">efix</a>(1),</code> <code><a href="/docs/linux/man/1-gs/">gs</a>(1),</code> <code><a href="/docs/linux/man/8-init/">init</a>(8),</code> <code><a href="/docs/linux/man/5-inittab/">inittab</a>(5),</code> <code><a href="/docs/linux/man/5-ttytab/">ttytab</a>(5),</code> <code><a href="/docs/linux/man/5-printcap/">printcap</a>(5),</code> <code><a href="/docs/linux/man/8-lpd/">lpd</a>(8),</code> <code><a href="/docs/linux/man/3-printf/">printf</a>(3),</code> <code><a href="/docs/linux/man/3-strftime/">strftime</a>(3).</code> </p>
<h2>BUGS</h2>
<p> Can&#8217;t read TIFF files with more than 1 strip </p>
<p> Class 1 operation may fail if the program can&#8217;t respond to certain data received from the modem within 55 milliseconds. </p>
<p> May fail if multitasking delays cause the received data to overflow the computer&#8217;s serial device buffer or if an under-run of transmit data exceeds 5 seconds. </p>
<p> Polling does not work. </p>
<p> Does not support 2-D coding, ECM, or BFT. </p>
<h2>Index</h2>
