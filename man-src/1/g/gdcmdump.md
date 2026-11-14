---
title: "gdcmdump(1)"
name: "gdcmdump"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdcmdump/"
description: "gdcmdump – .TH \"gdcmdump\" 1 \"Fri Oct 29 2010\" \"Version 2.0.16\" \"GDCM\""
---

<h2 class="name">NAME</h2>
<p> gdcmdump &#8211; .TH &quot;gdcmdump&quot; 1 &quot;Fri Oct 29 2010&quot; &quot;Version 2.0.16&quot; &quot;GDCM&quot; </p>
<h2 class="name">NAME</h2>
<p> gdcmdump &#8211; .SH &quot;SYNOPSIS&quot; </p>
<pre><code>
gdcmdump[options] dcm_file
    gdcmdump[options] dcm_directory
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>gdcmdump</code> command line program dumps a DICOM file to the console. For those familiary with dcmdump output, gdcmdump has some minor differences. Namely: </p>
<dl>
<dt>*</p>
<dd> For Implicit Transfer Syntax gdcmdump will print ?? instead of the dictionary VR</dl>
<p> gdcmdump has a limited private dictionary that is used to lookup private element whenever possible.</p>
<h2>PARAMETERS</h2>
<pre>
dcm_file        DICOM input filename
dcm_directory   DICOM input directory
</pre>
<h2>OPTIONS</h2>
<h3>OPTIONS</h3>
<p>  -x &#8211;xml-dict  generate the XML dict (only private elements for now).<br />
  -r &#8211;recursive recursive (input is a directory)<br />
  -d &#8211;dump      dump value (limited use).<br />
  -p &#8211;print     print value instead of simply dumping (default).<br />
  -c &#8211;color     print in color.<br />
  -C &#8211;csa       print SIEMENS CSA Header (0029,[12]0,SIEMENS CSA HEADER).<br />
  -P &#8211;pdb       print GEMS Protocol Data Block (0025,1b,GEMS_SERS_01).<br />
  -A &#8211;asn1      print encapsulated ASN1 structure &gt;(0400,0520).</p>
<h3>general options</h3>
<p>&#8211; h&#8211; help<br />
        print this help text and exit &#8211;<br />
    v&#8211; version<br />
        print version information and exit &#8211;<br />
    V&#8211; verbose<br />
        verbose<br />
        mode(warning + error)<br />
            .-<br />
    W&#8211; warning<br />
    warning mode,<br />
    print warning information<br />
        &#8211; E&#8211; error<br />
        error mode,<br />
    print error information<br />
        &#8211; D&#8211; debug<br />
        debug mode,<br />
    print debug information</p>
<h3>special options</h3>
<pre>
  -I --ignore-errors   dumps even if file is corrupted (advanced users only, see disclaimers).
</pre>
<h2>Typical usage</h2>
<h3>Printing Implicit Transfer Syntax</h3>
<p> The VR are not found in the file, thus are presented with a &#8216;(??)&#8217;, and right next to it (if found) the correct VR. </p>
<p> Eg.: </p>
<pre>
$ gdcmdump GE_DLX-8-MONO2-PrivateSyntax.dcm
</pre>
<p>#Dicom &#8211; File &#8211; Format<br />
&#8230;(0008, 0000) ? ? (UL)434 #4, 1 Generic Group Length(0008, 0005) ? ? (CS)[ISO_IR 100] #10, 1 &#8211; n Specific Character Set(0008, 0008) ? ? (CS)[ORIGINAL\PRIMARY\SINGLE PLANE] #30, 2 &#8211; n Image Type(0008, 0016) ? ? (UI)[1.2.840.10008.5.1.4.1.1.12.1] #28, 1 SOP Class UID(0008, 0018) ? ? (UI)[1.2.840.113619.2.16.1.0.906539207.1.24207] #42, 1 SOP Instance UID(0008, 0020) ? ? (DA)[19980923] #8, 1 Study Date(0008, 0021) ? ? (DA)[19980923] #8, 1 Series Date(0008, 0022) ? ? (DA)[19980923] #8, 1 Acquisition Date(0008, 0023) ? ? (DA)[19980923] #8, 1 Content Date(0008, 0030) ? ? (TM)[101229.000] #10, 1 Study Time(0008, 0031) ? ? (TM)[101229.000] #10, 1 Series Time(0008, 0032) ? ? (TM)[102653.000] #10, 1 Acquisition Time(0008, 0033) ? ? (TM)[102653.000] #10, 1 Content Time&#8230;</p>
<h3>Print Private Attributes</h3>
<p> GDCM has a limited private dictionary. Whenever possible, it will try to lookup the private data element. </p>
<pre>
$ gdcmdump 012345.002.050.dcm
</pre>
<p>&#8230;(0009, 0010) LO[GEMS_IDEN_01] #12, 1 Private Creator(0009, 1001) LO[GE_GENESIS_FF] #14, 1 Full fidelity(0009, 1002) SH[MRCV] #4, 1 Suite id(0009, 1004) SH[SIGNA] #6, 1 Product id(0009, 1027) SL 985968524 #4, 1 Image actual date(0009, 1030) SH[19356UMR2] #10, 1 Service id(0009, 1031) SH[999] #4, 1 Mobile location number(0009, 10e3) UI[1.2.840.113619.1.1.4.1762386977] #32, 1 Equipment UID(0009, 10e6) SH[08] #2, 1 Genesis Version &#8211; now(0009, 10e7) UL 2757786872 #4, 1 Exam Record checksum(0009, 10e9) SL 985968523 #4, 1 Actual series data time stamp&#8230;(0019, 0000) UL 1208 #4, 1 Generic Group Length(0019, 0010) LO[GEMS_ACQU_01] #12, 1 Private Creator(0019, 100f) DS[424.399994] #10, 1 Horiz.Frame of ref.(0019, 1011)SS 0 #2, 1 Series contrast&#8230;(0019, 10e0) DS[0.000000] #8, 1 User data 24 {#DTI Diffusion Dir., release 10.0 &amp; above}(0019, 10e2)DS[0.000000] #8, 1 Velocity Encode Scale(0019, 10f2) SS 0 #2, 1 Fast phases(0019, 10f9) DS[98] #2, 1 Transmit gain&#8230;(0021, 0000) UL 372 #4, 1 Generic Group Length(0021, 0010) LO[GEMS_RELA_01] #12, 1 Private Creator(0021, 1003) SS 0 #2, 1 Series from which Prescribed&#8230;</p>
<h3>SIEMENS CSA Header</h3>
<p> Using this option it is possible to dump as a readable text what is contained in the private attribute as found in typical SIEMENS MR DICOM file. </p>
<p> Eg.: </p>
<pre>
$ gdcmdump --csa MR_SIEMENS_forceLoad29-1010_29-1020.dcm
</pre>
<pre>
(0029,0010)siemens csa header
Image shadow data (0029,xx10)
0 - 'EchoLinePosition' VM 1, VR IS, SyngoDT 6, NoOfItems 6, Data '64      '
1 - 'EchoColumnPosition' VM 1, VR IS, SyngoDT 6, NoOfItems 6, Data '64      '
2 - 'EchoPartitionPosition' VM 1, VR IS, SyngoDT 6, NoOfItems 6, Data '32      '
3 - 'UsedChannelMask' VM 1, VR UL, SyngoDT 9, NoOfItems 6, Data '255     '
4 - 'Actual3DImaPartNumber' VM 1, VR IS, SyngoDT 6, NoOfItems 0, Data 
5 - 'ICE_Dims' VM 1, VR LO, SyngoDT 19, NoOfItems 6, Data 'X_1_1_1_1_1_1_31_1_1_1_1_19'
6 - 'B_value' VM 1, VR IS, SyngoDT 6, NoOfItems 6, Data '0       '
7 - 'Filter1' VM 1, VR IS, SyngoDT 6, NoOfItems 0, Data 
8 - 'Filter2' VM 1, VR IS, SyngoDT 6, NoOfItems 0, Data 
...
</pre>
<h3>GEMS Protocol Data Block</h3>
<p> Using this option it is possible to dump as a readable text what is contained in the private attribute as found in typical GEMS MR DICOM file. </p>
<p> Protocol Data Block : 0025,xx1b,GEMS_SERS_01 </p>
<pre>
$ gdcmdump --pdb GE_MR_0025xx1bProtocolDataBlock.dcm
</pre>
<pre>
ENTRY &quot;Head First&quot;
POSITION &quot;Supine&quot;
ANREF &quot;NA&quot;
COIL &quot;HEAD&quot;
PLANE &quot;OBLIQUE&quot;
SEDESCFLAG &quot;1&quot;
SEDESC &quot;AX FSE T2&quot;
IMODE &quot;2D&quot;
PSEQ &quot;FSE-XL&quot;
IOPT &quot;FC, EDR, TRF, Fast&quot;
PLUG &quot;22&quot;
FILTCHOICE &quot;None&quot;
BWRT &quot;-1&quot;
TRICKSIMG &quot;1&quot;
TAG_SPACE &quot;7&quot;
TAG_TYPE &quot;None&quot;
...
</pre>
<h3>Encapsulated ASN1 Structure</h3>
<p> This option is mainly used for dumping the ASN1 structure of the encrypted Attribute (0040,0520) </p>
<pre>
$ gdcmdump encrypted.dcm
</pre>
<pre>
...
(0400,0500) SQ                                                    # u/l,1 Encrypted Attributes Sequence
  (fffe,e000) na (Item with undefined length)
    (0400,0510) UI [1.2.840.10008.1.2]                            # 18,1 Encrypted Content Transfer Syntax UID
    (0400,0520) OB 30\82a
