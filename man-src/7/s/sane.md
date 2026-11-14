---
title: "sane(7)"
name: "sane"
section: "7"
letter: "s"
url: "/docs/linux/man/7-sane/"
description: "sane – Scanner Access Now Easy: API for accessing scanners"
---

<p>sane &#8211; Scanner Access Now Easy: API for accessing scanners</p>
<h2>Description</h2>
<p><code>SANE</code> is an application programming interface (API) that provides standardized access to any raster image scanner hardware. The standardized interface makes it possible to write just one driver for each scanner device instead of one driver for each scanner and application. While <code>SANE</code> is primarily targeted at a UNIX environment, the standard has been carefully designed to make it possible to implement the API on virtually any hardware or operating system. This manual page provides a summary of the information available about <code>SANE</code>. If you have trouble getting your scanner detected, read the PROBLEMS section. </p>
<h2>Terminology</h2>
<p>An application that uses the <code>SANE</code> interface is called a <code>SANE frontend.</code> A driver that implements the <code>SANE</code> interface is called a <code>SANE backend.</code> A <code>meta backend</code> provides some means to manage one or more other backends.</p>
<h2>Software Packages</h2>
<p>The package <code>sane-backends</code> contains backends, documentation, networking support, and the command line frontend <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1). The frontends <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1), <code><a href="/docs/linux/man/1-xcam/">xcam</a></code>(1), and <code><a href="/docs/linux/man/1-scanadf/">scanadf</a></code>(1) are included in the package <code>sane-frontends</code>. Both packages can be downloaded from the <code>SANE</code> homepage (<i><a rel="nofollow" href="http://www.sane-project.org/">http://www.sane-project.org/</a></i>). Information about other frontends and backends can also be found on the <code>SANE</code> homepage.</p>
<h2>General Information</h2>
<p>The following sections provide short descriptions and links to more information about several aspects of <code>SANE.</code> A name with a number in parenthesis (e.g. <code><a href="/docs/linux/man/5-sane-dll/">sane-dll</a></code>(5)) points to a manual page. In this case <i>man 5 sane-dll</i> will display the page. Entries like <i>/usr/share/doc/libsane/README</i> are references to text files that were copied to the <code>SANE</code> documentation directory (<i>/usr/share/doc/libsane/</i>) during installation. Everything else is a URL to a resource on the web. </p>
<dl>
<dt><code>SANE homepage</code></p>
<dd>Information on all aspects of SANE including a tutorial and a link to the SANE FAQ can be found on the SANE homepage: <i><a rel="nofollow" href="http://www.sane-project.org/">http://www.sane-project.org/</a></i>.</p>
<dt><code>SANE device lists</code></p>
<dd>The <code>SANE</code> device lists contain information about the status of <code>SANE</code> support for a specific device. If your scanner is not listed there (either supported or unsupported), please contact us. See section HOW CAN YOU HELP SANE for details. There are lists for specific releases of SANE, for the current development version and a search engine: <i><a rel="nofollow" href="http://www.sane-project.org/sane-supported-devices.html">http://www.sane-project.org/sane-supported-devices.html</a></i>. The lists are also installed on your system at <i>/usr/share/doc/libsane/</i>.</p>
<dt><code>SANE mailing list</code></p>
<dd>There is a mailing list for the purpose of discussing the SANE standard and its implementations: sane-devel. Despite its name, the list is not only intended for developers, but also for users. There are also some more lists for special topics. However, for users, sane-devel is the right list. How to subscribe and unsubscribe: <i><a rel="nofollow" href="http://www.sane-project.org/mailing-lists.html">http://www.sane-project.org/mailing-lists.html</a></i>.</p>
<dt><code>SANE IRC channel</code></p>
<dd>The IRC (Internet Relay Chat) channel #sane can be found on the Freenode network (irc.libera.chat). It&#8217;s for discussing <code>SANE</code> problems, talking about development and general <code>SANE</code> related chatting. Before asking for help, please read the other documentation mentioned in this manual page. The channel&#8217;s topic is also used for announcements of problems with SANE infrastructure (mailing lists, web server, etc.).</p>
<dt><code>Compiling and installing SANE</code></p>
<dd>Look at <i>/usr/share/doc/libsane/README</i> and the os-dependent README files for information about compiling and installing <code>SANE.</code></p>
<dt><code>SCSI configuration</code></p>
<dd>For information about various systems and SCSI controllers see <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5).</p>
<dt><code>USB configuration</code></p>
<dd>For information about USB configuration see <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5). </p>
</dl>
<h2>Frontends And Miscellaneous Programs</h2>
<dl>
<dt><code>scanimage</code></p>
<dd>Command-line frontend. See <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1).</p>
<dt><code>saned</code></p>
<dd><code>SANE</code> network daemon that allows remote clients to access image acquisition devices available on the local host. See <code><a href="/docs/linux/man/8-saned/">saned</a></code>(8).</p>
<dt><code>sane-find-scanner</code></p>
<dd>Command-line tool to find SCSI and USB scanners and determine their UNIX device files. See <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1).</dl>
<p> Also, have a look at the <code>sane-frontends</code> package (which includes <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1), <code><a href="/docs/linux/man/1-xcam/">xcam</a></code>(1), and <code><a href="/docs/linux/man/1-scanadf/">scanadf</a></code>(1)) and the frontend information page at <i><a rel="nofollow" href="http://www.sane-project.org/sane-frontends.html">http://www.sane-project.org/sane-frontends.html</a></i>.</p>
<h2>Backends For Scanners</h2>
<dl>
<dt><code>abaton</code></p>
<dd>Supports Abaton flatbed scanners such as the Scan 300/GS (8bit, 256 levels of gray) and the Scan 300/S (black and white, untested). See <code><a href="/docs/linux/man/5-sane-abaton/">sane-abaton</a></code>(5) for details.</p>
<dt><code>agfafocus</code></p>
<dd>Supports AGFA Focus scanners and the Siemens S9036 (untested). See <code><a href="/docs/linux/man/5-sane-agfafocus/">sane-agfafocus</a></code>(5) for details.</p>
<dt><code>apple</code></p>
<dd>Supports Apple flatbed scanners including the following scanners: AppleScanner, OneScanner and ColorOneScanner. See <code><a href="/docs/linux/man/5-sane-apple/">sane-apple</a></code>(5) for details.</p>
<dt><code>artec</code></p>
<dd>Supports several Artec/Ultima SCSI flatbed scanners as well as the BlackWidow BW4800SP and the Plustek 19200S. See <code><a href="/docs/linux/man/5-sane-artec/">sane-artec</a></code>(5) for details.</p>
<dt><code>artec_eplus48u</code></p>
<dd>Supports the Artec E+ 48U scanner and re-badged models like Tevion MD 9693, Medion MD 9693, Medion MD 9705 and Trust Easy Webscan 19200. See <code><a href="/docs/linux/man/5-sane-artec_eplus48u/">sane-artec_eplus48u</a></code>(5) for details.</p>
<dt><code>as6e</code></p>
<dd>Supports the Artec AS6E parallel port interface scanner. See <code><a href="/docs/linux/man/5-sane-as6e/">sane-as6e</a></code>(5) for details.</p>
<dt><code>avision</code></p>
<dd>Supports several Avision based scanners including the original Avision scanners (like AV 630, AV 620, &#8230;) as well as the HP ScanJet 53xx and 74xx series, Fujitsu ScanPartner, some Mitsubishi and Minolta film-scanners. See <code><a href="/docs/linux/man/5-sane-avision/">sane-avision</a></code>(5) for details.</p>
<dt><code>bh</code></p>
<dd>Supports Bell+Howell Copiscan II series document scanners. See <code><a href="/docs/linux/man/5-sane-bh/">sane-bh</a></code>(5) for details.</p>
<dt><code>canon</code></p>
<dd>Supports the CanoScan 300, CanoScan 600, and CanoScan 2700F SCSI flatbed scanners. See <code><a href="/docs/linux/man/5-sane-canon/">sane-canon</a></code>(5) for details.</p>
<dt><code>canon630u</code></p>
<dd>Supports the CanoScan 630u and 636u USB scanners. See <code><a href="/docs/linux/man/5-sane-canon630u/">sane-canon630u</a></code>(5) for details.</p>
<dt><code>canon_dr</code></p>
<dd>Supports the Canon DR-Series ADF SCSI and USB scanners. See <code><a href="/docs/linux/man/5-sane-canon_dr/">sane-canon_dr</a></code>(5) for details.</p>
<dt><code>canon_lide70</code></p>
<dd>Supports the CanoScan LiDE 70 and 600 USB scanners. See <code><a href="/docs/linux/man/5-sane-canon_lide70/">sane-canon_lide70</a></code>(5) for details.</p>
<dt><code>canon_pp</code></p>
<dd>Supports the CanoScan FB330P, FB630P, N340P and N640P parallel port scanners. See <code><a href="/docs/linux/man/5-sane-canon_pp/">sane-canon_pp</a></code>(5) for details.</p>
<dt><code>cardscan</code></p>
<dd>Support for Corex Cardscan USB scanners. See <code><a href="/docs/linux/man/5-sane-cardscan/">sane-cardscan</a></code>(5) for details.</p>
<dt><code>coolscan coolscan2 coolscan3</code></p>
<dd>Supports Nikon Coolscan film-scanners. See <code><a href="/docs/linux/man/5-sane-coolscan/">sane-coolscan</a></code>(5), <code><a href="/docs/linux/man/5-sane-coolscan2/">sane-coolscan2</a></code>(5) and <code><a href="/docs/linux/man/5-sane-coolscan3/">sane-coolscan3</a></code>(5) for details.</p>
<dt><code>epjitsu</code></p>
<dd>Supports Epson-based Fujitsu USB scanners. See <code><a href="/docs/linux/man/5-sane-epjitsu/">sane-epjitsu</a></code>(5) for details.</p>
<dt><code>epson</code></p>
<dd>Old driver for Epson SCSI, parallel port and USB flatbed scanners. See <code><a href="/docs/linux/man/5-sane-epson/">sane-epson</a></code>(5) for details but try <code>epson2</code> first.</p>
<dt><code>epson2</code></p>
<dd>Newer driver for Epson SCSI, parallel port, network and USB flatbed scanners (try this before <code>epson</code> which is outdated). See <code><a href="/docs/linux/man/5-sane-epson2/">sane-epson2</a></code>(5) for details.</p>
<dt><code>escl</code></p>
<dd>Supports scanners through the eSCL protocol. See <code><a href="/docs/linux/man/5-sane-escl/">sane-escl</a></code>(5) for details.</p>
<dt><code>fujitsu</code></p>
<dd>Supports most Fujitsu SCSI and USB, flatbed and adf scanners. See <code><a href="/docs/linux/man/5-sane-fujitsu/">sane-fujitsu</a></code>(5) for details.</p>
<dt><code>genesys</code></p>
<dd>Supports several scanners based on the Genesys Logic GL646, GL841, GL843, GL847 and GL124 chips like the Medion 6471 and Hewlett-Packard 2300c. See <code><a href="/docs/linux/man/5-sane-genesys/">sane-genesys</a></code>(5) for details.</p>
<dt><code>gt68xx</code></p>
<dd>Supports scanners based on the Grandtech GT-6801 and GT-6816 chips like the Artec Ultima 2000 and several Mustek BearPaw CU and TA models.<br />
 Some Genius, Lexmark, Medion, Packard Bell, Plustek, and Trust scanners are also supported. See <code><a href="/docs/linux/man/5-sane-gt68xx/">sane-gt68xx</a></code>(5) for details.</p>
<dt><code>hp</code></p>
<dd>Supports Hewlett-Packard ScanJet scanners which utilize SCL (Scanner Control Language by HP). See <code><a href="/docs/linux/man/5-sane-hp/">sane-hp</a></code>(5) for details.</p>
<dt><code>hpsj5s</code></p>
<dd>Supports the Hewlett-Packard ScanJet 5S scanner. See <code><a href="/docs/linux/man/5-sane-hpsj5s/">sane-hpsj5s</a></code>(5) for details.</p>
<dt><code>hp3500</code></p>
<dd>Supports the Hewlett-Packard ScanJet 3500 series. See <code><a href="/docs/linux/man/5-sane-hp3500/">sane-hp3500</a></code>(5) for details.</p>
<dt><code>hp3900</code></p>
<dd>Supports the Hewlett-Packard ScanJet 3900 series. See <code><a href="/docs/linux/man/5-sane-hp3900/">sane-hp3900</a></code>(5) for details.</p>
<dt><code>hp4200</code></p>
<dd>Supports the Hewlett-Packard ScanJet 4200 series. See <code><a href="/docs/linux/man/5-sane-hp4200/">sane-hp4200</a></code>(5) for details.</p>
<dt><code>hp5400</code></p>
<dd>Supports the Hewlett-Packard ScanJet 54XXC series. See <code><a href="/docs/linux/man/5-sane-hp5400/">sane-hp5400</a></code>(5) for details.</p>
<dt><code>hpljm1005</code></p>
<dd>Supports the Hewlett-Packard LaserJet M1005 scanner. See <code><a href="/docs/linux/man/5-sane-hpljm1005/">sane-hpljm1005</a></code>(5) for details.</p>
<dt><code>hs2p</code></p>
<dd>Supports the Ricoh IS450 family of SCSI scanners. See <code><a href="/docs/linux/man/5-sane-hs2p/">sane-hs2p</a></code>(5) for details.</p>
<dt><code>ibm</code></p>
<dd>Supports some IBM and Ricoh SCSI scanners. See <code><a href="/docs/linux/man/5-sane-ibm/">sane-ibm</a></code>(5) for details.</p>
<dt><code>kodak</code></p>
<dd>Supports some large Kodak scanners. See <code><a href="/docs/linux/man/5-sane-kodak/">sane-kodak</a></code>(5) for details.</p>
<dt><code>kodakaio</code></p>
<dd>Supports Kodak AiO printer/scanners. See <code><a href="/docs/linux/man/5-sane-kodakaio/">sane-kodakaio</a></code>(5) for details.</p>
<dt><code>kvs1025</code></p>
<dd>Supports Panasonic KV-S102xC scanners. See <code><a href="/docs/linux/man/5-sane-kvs1025/">sane-kvs1025</a></code>(5) for details.</p>
<dt><code>leo</code></p>
<dd>Supports the LEO S3 and the Across FS-1130, which is a re-badged LEO FS-1130 scanner. See <code><a href="/docs/linux/man/5-sane-leo/">sane-leo</a></code>(5) for details.</p>
<dt><code>lexmark</code></p>
<dd>Supports the Lexmark X1100 series of USB scanners. See <code><a href="/docs/linux/man/5-sane-lexmark/">sane-lexmark</a></code>(5) for details.</p>
<dt><code>ma1509</code></p>
<dd>Supports the Mustek BearPaw 1200F USB flatbed scanner. See <code><a href="/docs/linux/man/5-sane-ma1509/">sane-ma1509</a></code>(5) for details.</p>
<dt><code>magicolor</code></p>
<dd>Supports the KONICA MINOLTA magicolor 1690MF multi-function printer/scanner/fax. See <code><a href="/docs/linux/man/5-sane-magicolor/">sane-magicolor</a></code>(5) for details.</p>
<dt><code>matsushita</code></p>
<dd>Supports some Panasonic KVSS high speed scanners. See <code><a href="/docs/linux/man/5-sane-matsushita/">sane-matsushita</a></code>(5) for details.</p>
<dt><code>microtek</code></p>
<dd>Supports &quot;second generation&quot; Microtek scanners with SCSI-1 command set. See <code><a href="/docs/linux/man/5-sane-microtek/">sane-microtek</a></code>(5) for details.</p>
<dt><code>microtek2</code></p>
<dd>Supports some Microtek scanners with a SCSI-2 command set. See <code><a href="/docs/linux/man/5-sane-microtek2/">sane-microtek2</a></code>(5) for details.</p>
<dt><code>mustek</code></p>
<dd>Supports most Mustek SCSI flatbed scanners including the Paragon and ScanExpress series and the 600 II N and 600 II EP (non-SCSI). Some Trust scanners are also supported. See <code><a href="/docs/linux/man/5-sane-mustek/">sane-mustek</a></code>(5) for details.</p>
<dt><code>mustek_pp</code></p>
<dd>Supports Mustek parallel port flatbed scanners. See <code><a href="/docs/linux/man/5-sane-mustek_pp/">sane-mustek_pp</a></code>(5) for details.</p>
<dt><code>mustek_usb</code></p>
<dd>Supports some Mustek ScanExpress USB flatbed scanners. See <code><a href="/docs/linux/man/5-sane-mustek_usb/">sane-mustek_usb</a></code>(5) for details.</p>
<dt><code>mustek_usb2</code></p>
<dd>Supports scanners using the SQ113 chipset like the Mustek BearPaw 2448 TA Pro USB flatbed scanner. See <code><a href="/docs/linux/man/5-sane-mustek_usb2/">sane-mustek_usb2</a></code>(5) for details.</p>
<dt><code>nec</code></p>
<dd>Supports the NEC PC-IN500/4C SCSI scanner. See <code><a href="/docs/linux/man/5-sane-nec/">sane-nec</a></code>(5) for details.</p>
<dt><code>niash</code></p>
<dd>Supports the Agfa Snapscan Touch and the HP ScanJet 3300c, 3400c, and 4300c USB flatbed scanners. See <code><a href="/docs/linux/man/5-sane-niash/">sane-niash</a></code>(5) for details.</p>
<dt><code>p5</code></p>
<dd>Supports the Primax PagePartner. See <code><a href="/docs/linux/man/5-sane-p5/">sane-p5</a></code>(5) for details.</p>
<dt><code>pie</code></p>
<dd>Supports Pacific Image Electronics (PIE) and Devcom SCSI flatbed scanners. See <code><a href="/docs/linux/man/5-sane-pie/">sane-pie</a></code>(5) for details.</p>
<dt><code>pixma</code></p>
<dd>Supports Canon PIXMA MP series (multi-function devices), Canon imageCLASS series (laser devices), Canon MAXIFY series and some Canon CanoScan series. See <code><a href="/docs/linux/man/5-sane-pixma/">sane-pixma</a></code>(5) for details.</p>
<dt><code>plustek</code></p>
<dd>Supports USB flatbed scanners that use the National Semiconductor LM983[1/2/3] chipset aka Merlin. Scanners using this LM983x chips include some models from Plustek, KYE/Genius, Hewlett-Packard, Mustek, Umax, Epson, and Canon. See <code><a href="/docs/linux/man/5-sane-plustek/">sane-plustek</a></code>(5) for details.</p>
<dt><code>plustek_pp</code></p>
<dd>Supports Plustek parallel port flatbed scanners using the Plustek ASIC P96001, P96003, P98001 and P98003, which includes some models from Plustek, KYE/Genius, Primax. See <code><a href="/docs/linux/man/5-sane-plustek_pp/">sane-plustek_pp</a></code>(5) for details.</p>
<dt><code>ricoh</code></p>
<dd>Supports the Ricoh flatbed scanners IS50 and IS60. See <code><a href="/docs/linux/man/5-sane-ricoh/">sane-ricoh</a></code>(5) for details.</p>
<dt><code>ricoh2</code></p>
<dd>Supports the Ricoh flatbed scanners: SG-3100SNw, SP-100SU, and SP-111SU. See <code><a href="/docs/linux/man/5-sane-ricoh2/">sane-ricoh2</a></code>(5) for details.</p>
<dt><code>s9036</code></p>
<dd>Supports Siemens 9036 flatbed scanners. See <code><a href="/docs/linux/man/5-sane-s9036/">sane-s9036</a></code>(5) for details.</p>
<dt><code>sceptre</code></p>
<dd>Supports the Sceptre S1200 flatbed scanner. See <code><a href="/docs/linux/man/5-sane-sceptre/">sane-sceptre</a></code>(5) for details.</p>
<dt><code>sharp</code></p>
<dd>Supports Sharp SCSI scanners. See <code><a href="/docs/linux/man/5-sane-sharp/">sane-sharp</a></code>(5) for details.</p>
<dt><code>sm3600</code></p>
<dd>Supports the Microtek ScanMaker 3600 USB scanner. See <code><a href="/docs/linux/man/5-sane-sm3600/">sane-sm3600</a></code>(5) for details.</p>
<dt><code>sm3840</code></p>
<dd>Supports the Microtek ScanMaker 3840 USB scanner. See <code><a href="/docs/linux/man/5-sane-sm3840/">sane-sm3840</a></code>(5) for details.</p>
<dt><code>snapscan</code></p>
<dd>Supports AGFA SnapScan flatbed scanners including some which are rebadged to other brands. See <code><a href="/docs/linux/man/5-sane-snapscan/">sane-snapscan</a></code>(5) for details.</p>
<dt><code>sp15c</code></p>
<dd>Supports the Fujitsu FCPA ScanPartner 15C flatbed scanner. See <code><a href="/docs/linux/man/5-sane-sp15c/">sane-sp15c</a></code>(5) for details.</p>
<dt><code>st400</code></p>
<dd>Supports the Siemens ST400 and ST800. See <code><a href="/docs/linux/man/5-sane-st400/">sane-st400</a></code>(5) for details.</p>
<dt><code>tamarack</code></p>
<dd>Supports Tamarack Artiscan flatbed scanners. See <code><a href="/docs/linux/man/5-sane-tamarack/">sane-tamarack</a></code>(5) for details.</p>
<dt><code>teco1 teco2 teco3</code></p>
<dd>Supports some TECO scanners, usually sold under the Relisys, Trust, Primax, Piotech, Dextra names. See <code><a href="/docs/linux/man/5-sane-teco1/">sane-teco1</a></code>(5), <code><a href="/docs/linux/man/5-sane-teco2/">sane-teco2</a></code>(5) and <code><a href="/docs/linux/man/5-sane-teco3/">sane-teco3</a></code>(5) for details.</p>
<dt><code>u12</code></p>
<dd>Supports USB flatbed scanners based on Plustek&#8217;s ASIC 98003 (parallel-port ASIC) and a GeneSys Logics&#8217; USB-parport bridge chip like the Plustek OpticPro U(T)12. See <code><a href="/docs/linux/man/5-sane-u12/">sane-u12</a></code>(5) for details.</p>
<dt><code>umax</code></p>
<dd>Supports UMAX-SCSI-scanners and some Linotype Hell SCSI-scanners. See <code><a href="/docs/linux/man/5-sane-umax/">sane-umax</a></code>(5) for details.</p>
<dt><code>umax_pp</code></p>
<dd>Supports Umax parallel port flatbed scanners and the HP 3200C. See <code><a href="/docs/linux/man/5-sane-umax_pp/">sane-umax_pp</a></code>(5) for details.</p>
<dt><code>umax1200u</code></p>
<dd>Supports the UMAX Astra 1220U (USB) flatbed scanner (and also the UMAX Astra 2000U, sort of). See <code><a href="/docs/linux/man/5-sane-umax1220u/">sane-umax1220u</a></code>(5) for details.</p>
<dt><code>xerox_mfp</code></p>
<dd>Supports multiple Samsung-based Samsung, Xerox, and Dell scanners. See <code><a href="/docs/linux/man/5-sane-xerox_mfp/">sane-xerox_mfp</a></code>(5) for details.</dl>
<p> Also, have a look at the backend information page at <i><a rel="nofollow" href="http://www.sane-project.org/sane-supported-devices.html">http://www.sane-project.org/sane-supported-devices.html</a></i> and the list of projects in <i>/usr/share/doc/libsane/PROJECTS</i>.</p>
<h2>Backends For Digital Cameras</h2>
<dl>
<dt><code>dc210</code></p>
<dd>Supports the Kodak DC210 Digital Camera. See <code><a href="/docs/linux/man/5-sane-dc210/">sane-dc210</a></code>(5).</p>
<dt><code>dc240</code></p>
<dd>Supports the Kodak DC240 Digital Camera. See <code><a href="/docs/linux/man/5-dc240/">dc240</a></code>(5).</p>
<dt><code>dc25</code></p>
<dd>Supports Kodak DC20/DC25 Digital Cameras. See <code><a href="/docs/linux/man/5-dc25/">dc25</a></code>(5).</p>
<dt><code>dmc</code></p>
<dd>Supports the Polaroid Digital Microscope Camera. See <code><a href="/docs/linux/man/5-dmc/">dmc</a></code>(5).</p>
<dt><code>gphoto2</code></p>
<dd>Supports digital cameras supported by the gphoto2 library package. (See <i><a rel="nofollow" href="http://www.gphoto.org">http://www.gphoto.org</a></i> for more information and a list of supported cameras.) Gphoto2 supports over 140 different camera models. However, please note that more development and testing is needed before all of these cameras will be supported by <code>SANE</code> backend. See <code><a href="/docs/linux/man/5-gphoto2/">gphoto2</a></code>(5).</p>
<dt><code>qcam</code></p>
<dd>Supports Connectix QuickCam cameras. See <code><a href="/docs/linux/man/5-qcam/">qcam</a></code>(5).</p>
<dt><code>stv680</code></p>
<dd>Supports webcams with a stv680 chip. See <code><a href="/docs/linux/man/5-stv680/">stv680</a></code>(5) for details.</dl>
<p> Also, have a look at the backend information page at <i><a rel="nofollow" href="http://www.sane-project.org/sane-supported-devices.html">http://www.sane-project.org/sane-supported-devices.html</a></i> and the list of projects in <i>/usr/share/doc/libsane/PROJECTS</i>.</p>
<h2>Miscellaneous Backends</h2>
<dl>
<dt><code>dll</code></p>
<dd>Implements a <code>SANE</code> backend that provides access to an arbitrary number of other <code>SANE</code> backends by dynamic loading. See <code><a href="/docs/linux/man/5-sane-dll/">sane-dll</a></code>(5).</p>
<dt><code>net</code></p>
<dd>The <code>SANE</code> network daemon <code><a href="/docs/linux/man/8-saned/">saned</a></code>(8) provides access to scanners located on different computers in connection with the <code><a href="/docs/linux/man/5-sane-net/">sane-net</a></code>(5) backend. See <code><a href="/docs/linux/man/8-saned/">saned</a></code>(8).</p>
<dt><code>pnm</code></p>
<dd>PNM image reader pseudo-backend. The purpose of this backend is primarily to aid in debugging of <code>SANE</code> frontends. See <code><a href="/docs/linux/man/5-sane-pnm/">sane-pnm</a></code>(5).</p>
<dt><code>pint</code></p>
<dd>Supports scanners that use the <code>PINT</code> (Pint Is Not Twain) device driver. The <code>PINT</code> driver is being actively developed on the OpenBSD platform, and has been ported to a few other *NIX-like operating systems. See <code><a href="/docs/linux/man/5-sane-pint/">sane-pint</a></code>(5).</p>
<dt><code>test</code></p>
<dd>Tests frontends and the <code>SANE</code> installation. It provides test pictures and various test options. See <code><a href="/docs/linux/man/5-sane-test/">sane-test</a></code>(5).</p>
<dt><code>v4l</code></p>
<dd>Provides generic access to video cameras and similar equipment using the <code>V4L</code> (Video for Linux) API. See <code><a href="/docs/linux/man/5-sane-v4l/">sane-v4l</a></code>(5)<code>.</code></dl>
<p> Also, have a look at the backend information page at <i><a rel="nofollow" href="http://www.sane-project.org/sane-supported-devices.html">http://www.sane-project.org/sane-supported-devices.html</a></i> and the list of projects in <i>/usr/share/doc/libsane/PROJECTS</i>.</p>
<h2>Changing The Top-Level Backend</h2>
<p>By default, all <code>SANE</code> backends (drivers) are loaded dynamically by the <code>sane-dll</code> meta backend. If you have any questions about the dynamic loading, read <code><a href="/docs/linux/man/5-sane-dll/">sane-dll</a></code>(5). <code>SANE</code> frontends can also be linked to other backends directly by copying or linking a backend to <code>libsane.so</code> in <i>/usr/lib/x86_64-linux-gnu/sane</i>.</p>
<h2>Developer&#8217;S Documentation</h2>
<p>It&#8217;s not hard to write a <code>SANE</code> backend. It can take some time, however. You should have basic knowledge of C and enough patience to work through the documentation and find out how your scanner works. Appended is a list of some documents that help to write backends and frontends. </p>
<p> The <code>SANE</code> standard defines the application programming interface (API) that is used to communicate between frontends and backends. It can be found at <i><a rel="nofollow" href="http://sane-project.gitlab.io/standard/">http://sane-project.gitlab.io/standard/</a> .</i> </p>
<p> There is some more information for programmers in <i>/usr/share/doc/libsane/backend-writing.txt</i>. Most of the internal <code>SANE</code> routines (<code>sanei</code>) are documented using doxygen: <i><a rel="nofollow" href="http://www.sane-project.org/sanei/">http://www.sane-project.org/sanei/</a></i>. Before a new backend or frontend project is started, have a look at <i>/usr/share/doc/libsane/PROJECTS</i> for projects that are planned or not yet included into the <code>SANE</code> distribution and at our bug-tracking system: <i><a rel="nofollow" href="http://www.http://www.sane-project.org/bugs.html">http://www.http://www.sane-project.org/bugs.html</a></i>. </p>
<p> There are some links on how to find out about the protocol of a scanner: <i><a rel="nofollow" href="http://www.meier-geinitz.de/sane/misc/develop.html">http://www.meier-geinitz.de/sane/misc/develop.html</a></i>. </p>
<p> If you start writing a backend or frontend or any other part of <code>SANE,</code> please contact the sane-devel mailing list for coordination so that work is not duplicated.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/*.conf</i></p>
<dd>The backend configuration files.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-*.a</i></p>
<dd>The static libraries implementing the backends.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-*.so</i></p>
<dd>The shared libraries implementing the backends (present on systems that support dynamic loading).</p>
<dt><i>/usr/share/doc/libsane/*</i></p>
<dd><code>SANE</code> documentation: The READMEs, text files for backends etc. </p>
</dl>
<h2>Problems</h2>
<p>If your device isn&#8217;t found but you know that it is supported, make sure that it is detected by your operating system. For SCSI and USB scanners, use the <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1) utility. It prints one line for each scanner it has detected and some comments (#). If <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1) finds your scanner only as root but not as normal user, the permissions for the device files are not adjusted correctly. If the scanner isn&#8217;t found at all, the operating system hasn&#8217;t detected it and may need some help. Depending on the type of your scanner, read <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5) or <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5). If your scanner (or other device) is not connected over the SCSI bus or USB, read the backend&#8217;s manual page for details on how to set it up. </p>
<p> Is your scanner detected by the operating system but not by <code>SANE</code>? Try <i>scanimage -L</i>. If the scanner is not found, check that the backend&#8217;s name is mentioned in <i>/etc/sane.d/dll.conf</i>. Some backends are commented out by default. Remove the comment sign for your backend in this case. Also some backends aren&#8217;t compiled at all if one of their prerequisites are missing. Examples include dc210, dc240, canon_pp, hpsj5s, gphoto2, pint, qcam, v4l, net, sm3600, snapscan, pnm. If you need one of these backends and it isn&#8217;t available, read the build instructions in the <code>README</code> file and the individual manual pages of the backends. </p>
<p> Another reason for not being detected by <i>scanimage -L</i> may be a missing or incorrect configuration in the backend&#8217;s configuration file. While <code>SANE</code> tries to automatically find most scanners, some can&#8217;t be setup correctly without the intervention of the administrator. Also on some operating systems auto-detection may not work. Check the backend&#8217;s manual page for details. </p>
<p> If your scanner is still not found, try setting the various environment variables that are available to assist in debugging. The environment variables are documented in the relevant manual pages. For example, to get the maximum amount of debug information when testing a Mustek SCSI scanner, set environment variables <code>SANE_DEBUG_DLL</code>, <code>SANE_DEBUG_MUSTEK</code>, and <code>SANE_DEBUG_SANEI_SCSI</code> to 128 and then invoke <i>scanimage -L</i>. The <code>SANE_DEBUG_DLL</code> messages tell if the <code><a href="/docs/linux/man/5-sane-mustek/">sane-mustek</a></code>(5) backend was found and loaded at all. The <code>SANE_DEBUG_MUSTEK</code> messages explain what the backend is doing while the <code>SANE_DEBUG_SCSI</code> debugging shows the low level handling. If you can&#8217;t find out what&#8217;s going on by checking the messages carefully, contact the sane-devel mailing list for help (see REPORTING BUGS below). </p>
<p> Now that your scanner is found by <i>scanimage -L</i>, try to do a scan: <i>scanimage&nbsp;&gt;image.pnm</i>. This command starts a scan for the default scanner with default settings. All the available options are listed by running <i>scanimage &#8211;help</i>. If scanning aborts with an error message, turn on debugging as mentioned above. Maybe the configuration file needs some tuning, e.g. to setup the path to a firmware that is needed by some scanners. See the backend&#8217;s manual page for details. If you can&#8217;t find out what&#8217;s wrong, contact sane-devel. </p>
<p> To check that the <code>SANE</code> libraries are installed correctly you can use the test backend, even if you don&#8217;t have a scanner or other <code>SANE</code> device:</p>
<dl>
<dd>scanimage -d test -T</dl>
<p> You should get a list of PASSed tests. You can do the same with your backend by changing &quot;test&quot; to your backend&#8217;s name. </p>
<p> So now scanning with <code>scanimage (1)</code> works and you want to use one of the graphical frontends like <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1)<code>,</code> <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1)<code>, or</code> <code>quiteinsane (1)</code> but those frontends don&#8217;t detect your scanner? One reason may be that you installed two versions of <code>SANE</code>. E.g. the version that was installed by your distribution in <i>/usr</i> and one you installed from source in <i>/usr/local/</i>. Make sure that only one version is installed. Another possible reason is, that your system&#8217;s dynamic loader can&#8217;t find the <code>SANE</code> libraries. For Linux, make sure that <i>/etc/ld.so.conf</i> contains <i>/usr/local/lib</i> and does <code>not</code> contain <i>/usr/local/lib/sane</i>. See also the documentation of the frontends.</p>
<h2>How Can You Help Sane</h2>
<p>We appreciate any help we can get. Please have a look at our web page about contributing to <code>SANE</code>: <i><a rel="nofollow" href="http://www.sane-project.org/contrib.html">http://www.sane-project.org/contrib.html</a></i></p>
<h2>Contact</h2>
<p>For reporting bugs or requesting new features, please use our bug-tracking system: <i><a rel="nofollow" href="http://www.sane-project.org/bugs.html">http://www.sane-project.org/bugs.html</a></i>. You can also contact the author of your backend directly. Usually the email address can be found in the <i>/usr/share/doc/libsane/AUTHORS</i> file or the backend&#8217;s manpage. For general discussion about SANE, please use the <code>SANE</code> mailing list sane-devel (see <i><a rel="nofollow" href="http://www.sane-project.org/mailing-lists.html">http://www.sane-project.org/mailing-lists.html</a></i> for details).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-saned/">saned</a></code>(8), <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1), <code><a href="/docs/linux/man/5-sane-abaton/">sane-abaton</a></code>(5), <code><a href="/docs/linux/man/5-sane-agfafocus/">sane-agfafocus</a></code>(5), <code><a href="/docs/linux/man/5-sane-apple/">sane-apple</a></code>(5), <code><a href="/docs/linux/man/5-sane-artec/">sane-artec</a></code>(5), <code><a href="/docs/linux/man/5-sane-artec_eplus48u/">sane-artec_eplus48u</a></code>(5), <code><a href="/docs/linux/man/5-sane-as6e/">sane-as6e</a></code>(5), <code><a href="/docs/linux/man/5-sane-avision/">sane-avision</a></code>(5), <code><a href="/docs/linux/man/5-sane-bh/">sane-bh</a></code>(5), <code><a href="/docs/linux/man/5-sane-canon/">sane-canon</a></code>(5), <code><a href="/docs/linux/man/5-sane-canon630u/">sane-canon630u</a></code>(5), <code><a href="/docs/linux/man/5-sane-canon_dr/">sane-canon_dr</a></code>(5), <code><a href="/docs/linux/man/5-sane-canon_pp/">sane-canon_pp</a></code>(5), <code><a href="/docs/linux/man/5-sane-cardscan/">sane-cardscan</a></code>(5), <code><a href="/docs/linux/man/5-sane-coolscan/">sane-coolscan</a></code>(5), <code><a href="/docs/linux/man/5-sane-coolscan2/">sane-coolscan2</a></code>(5), <code><a href="/docs/linux/man/5-sane-coolscan3/">sane-coolscan3</a></code>(5), <code><a href="/docs/linux/man/5-sane-dc210/">sane-dc210</a></code>(5), <code><a href="/docs/linux/man/5-sane-dc240/">sane-dc240</a></code>(5), <code><a href="/docs/linux/man/5-sane-dc25/">sane-dc25</a></code>(5), <code><a href="/docs/linux/man/5-sane-dll/">sane-dll</a></code>(5), <code><a href="/docs/linux/man/5-sane-dmc/">sane-dmc</a></code>(5), <code><a href="/docs/linux/man/5-sane-epson/">sane-epson</a></code>(5), <code><a href="/docs/linux/man/5-sane-epson2/">sane-epson2</a></code>(5), <code><a href="/docs/linux/man/5-sane-escl/">sane-escl</a></code>(5), <code><a href="/docs/linux/man/5-sane-fujitsu/">sane-fujitsu</a></code>(5), <code><a href="/docs/linux/man/5-sane-genesys/">sane-genesys</a></code>(5), <code><a href="/docs/linux/man/5-sane-gphoto2/">sane-gphoto2</a></code>(5), <code><a href="/docs/linux/man/5-sane-gt68xx/">sane-gt68xx</a></code>(5), <code><a href="/docs/linux/man/5-sane-hp/">sane-hp</a></code>(5), <code><a href="/docs/linux/man/5-sane-hpsj5s/">sane-hpsj5s</a></code>(5), <code><a href="/docs/linux/man/5-sane-hp3500/">sane-hp3500</a></code>(5), <code><a href="/docs/linux/man/5-sane-hp3900/">sane-hp3900</a></code>(5), <code><a href="/docs/linux/man/5-sane-hp4200/">sane-hp4200</a></code>(5), <code><a href="/docs/linux/man/5-sane-hp5400/">sane-hp5400</a></code>(5), <code><a href="/docs/linux/man/5-sane-hpljm1005/">sane-hpljm1005</a></code>(5), <code><a href="/docs/linux/man/5-sane-ibm/">sane-ibm</a></code>(5), <code><a href="/docs/linux/man/5-sane-kodak/">sane-kodak</a></code>(5), <code><a href="/docs/linux/man/5-sane-leo/">sane-leo</a></code>(5), <code><a href="/docs/linux/man/5-sane-lexmark/">sane-lexmark</a></code>(5), <code><a href="/docs/linux/man/5-sane-ma1509/">sane-ma1509</a></code>(5), <code><a href="/docs/linux/man/5-sane-matsushita/">sane-matsushita</a></code>(5), <code><a href="/docs/linux/man/5-sane-microtek2/">sane-microtek2</a></code>(5), <code><a href="/docs/linux/man/5-sane-microtek/">sane-microtek</a></code>(5), <code><a href="/docs/linux/man/5-sane-mustek/">sane-mustek</a></code>(5), <code><a href="/docs/linux/man/5-sane-mustek_pp/">sane-mustek_pp</a></code>(5), <code><a href="/docs/linux/man/5-sane-mustek_usb/">sane-mustek_usb</a></code>(5), <code><a href="/docs/linux/man/5-sane-mustek_usb2/">sane-mustek_usb2</a></code>(5), <code><a href="/docs/linux/man/5-sane-nec/">sane-nec</a></code>(5), <code><a href="/docs/linux/man/5-sane-net/">sane-net</a></code>(5), <code><a href="/docs/linux/man/5-sane-niash/">sane-niash</a></code>(5), <code><a href="/docs/linux/man/5-sane-pie/">sane-pie</a></code>(5), <code><a href="/docs/linux/man/5-sane-pint/">sane-pint</a></code>(5), <code><a href="/docs/linux/man/5-sane-plustek/">sane-plustek</a></code>(5), <code><a href="/docs/linux/man/5-sane-plustek_pp/">sane-plustek_pp</a></code>(5), <code><a href="/docs/linux/man/5-sane-pnm/">sane-pnm</a></code>(5), <code><a href="/docs/linux/man/5-sane-qcam/">sane-qcam</a></code>(5), <code><a href="/docs/linux/man/5-sane-ricoh/">sane-ricoh</a></code>(5), <code><a href="/docs/linux/man/5-sane-ricoh2/">sane-ricoh2</a></code>(5), <code><a href="/docs/linux/man/5-sane-s9036/">sane-s9036</a></code>(5), <code><a href="/docs/linux/man/5-sane-sceptre/">sane-sceptre</a></code>(5), <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5), <code><a href="/docs/linux/man/5-sane-sharp/">sane-sharp</a></code>(5), <code><a href="/docs/linux/man/5-sane-sm3600/">sane-sm3600</a></code>(5), <code><a href="/docs/linux/man/5-sane-sm3840/">sane-sm3840</a></code>(5), <code><a href="/docs/linux/man/5-sane-snapscan/">sane-snapscan</a></code>(5), <code><a href="/docs/linux/man/5-sane-sp15c/">sane-sp15c</a></code>(5), <code><a href="/docs/linux/man/5-sane-st400/">sane-st400</a></code>(5), <code><a href="/docs/linux/man/5-sane-stv680/">sane-stv680</a></code>(5), <code><a href="/docs/linux/man/5-sane-tamarack/">sane-tamarack</a></code>(5), <code><a href="/docs/linux/man/5-sane-teco1/">sane-teco1</a></code>(5), <code><a href="/docs/linux/man/5-sane-teco2/">sane-teco2</a></code>(5), <code><a href="/docs/linux/man/5-sane-teco3/">sane-teco3</a></code>(5), <code><a href="/docs/linux/man/5-sane-test/">sane-test</a></code>(5), <code><a href="/docs/linux/man/5-sane-u12/">sane-u12</a></code>(5), <code><a href="/docs/linux/man/5-sane-umax1220u/">sane-umax1220u</a></code>(5), <code><a href="/docs/linux/man/5-sane-umax/">sane-umax</a></code>(5), <code><a href="/docs/linux/man/5-sane-umax_pp/">sane-umax_pp</a></code>(5), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5), <code><a href="/docs/linux/man/5-sane-v4l/">sane-v4l</a></code>(5), <code><a href="/docs/linux/man/5-sane-xerox_mfp/">sane-xerox_mfp</a></code>(5) </p>
<h2>Author</h2>
<p>David Mosberger-Tang and many many more (see <i>/usr/share/doc/libsane/AUTHORS</i> for details). This man page was written by Henning Meier-Geinitz. Quite a lot of text was taken from the <code>SANE</code> standard, several man pages, and README files.</p>
