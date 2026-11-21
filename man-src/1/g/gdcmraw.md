---
title: "gdcmraw(1)"
name: "gdcmraw"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdcmraw/"
description: "gdcmraw – .TH \"gdcmraw\" 1 \"Fri Oct 29 2010\" \"Version 2.0.16\" \"GDCM\""
---
<h2 class="name">NAME</h2>
<p> gdcmraw - .TH &quot;gdcmraw&quot; 1 &quot;Fri Oct 29 2010&quot; &quot;Version 2.0.16&quot; &quot;GDCM&quot; </p>
<h2 class="name">NAME</h2>
<p> gdcmraw - .SH &quot;SYNOPSIS&quot; </p>
<pre><code>gdcmraw [options] file-in file-out
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>gdcmraw</code> tool is mostly used for development purpose. It is used to extract a specific binary field from a DICOM DataSet.  </p>
<h2>PARAMETERS</h2>
<pre><code>file-in DICOM input filename
file-out output filename
</code></pre>
<h2>OPTIONS</h2>
<h3>PARAMETERS</h3>
<pre><code>  -i --input Input filename
  -o --output Output filename
  -t --tag Specify tag to extract value from.
</code></pre>
<h3>OPTIONS</h3>
<pre><code>  -S --split-frags Split fragments into multiple files.
  -p --pattern Specify trailing file pattern (see split-frags).
  -P --pixel-data Pixel Data trailing 0.
</code></pre>
<h3>general options</h3>
<pre><code>  -h --help
         print this help text and exit
  -v --version
         print version information and exit
  -V --verbose
         verbose mode (warning+error).
  -W --warning
         warning mode, print warning information
  -E --error
         error mode, print error information
  -D --debug
         debug mode, print debug information
</code></pre>
<h2>Typical usage</h2>
<h3>Copy Attribute Value to file</h3>
<p> This will extract the value at Tag (0025,101b): </p>
<pre><code>$ gdcmraw -i GE_MR_0025xx1bProtocolDataBlock.dcm -t 25,101b -o pdb.raw
</code></pre>
<h3>Extract Pixel Data</h3>
<p> If you do not specify any tag, the Pixel Data element is the default one. So for instance to grab the Pixel Data from an image: </p>
<pre><code>$ gdcmraw -i test.acr -o test.raw
</code></pre>
<p> You can then for example compute the md5sum of this pixel data (very useful): </p>
<pre><code>$ md5sum test.raw
f845c8f283d39a0204c325654493ba53 test.raw
</code></pre>
<h3>Encapsulated Syntax</h3>
<p> When the Pixel Data is encapsulated, multiple fragments can be used to store a single slice image: </p>
<pre><code>$ gdcmdump D_CLUNIE_CT1_J2KR.dcm
</code></pre>
<pre><code>...
(7fe0,0010) OB # u/l,1 Pixel Data
  (fffe,e000) ?? [] # 0,1 Item
  (fffe,e000) ?? ff\4f\ff\51\00\29\00\00\00\00\02\00\00\00\02\00\00\00\00\00\00\00\00\00\00\00\02\00\00\00\02\00 # 65536,1 Item
  (fffe,e000) ?? 2c\b7\ee\68\de\e3\93\2d\b3\b8\ba\90\7b\42\3e\f8\42\16\64\88\46\30\37\d4\50\95\9b\b6\a5\c7\38\9b # 65536,1 Item
  (fffe,e000) ?? 48\3c\03\e8\c4\3f\44\e1\8a\5c\73\3b\02\0a\ad\a5\8f\e4\0c\81\76\a2\d7\1b\7f\b7\cd\bc\30\c6\6a\6a # 43308,1 Item
(fffe,e0dd) 0
</code></pre>
<p> In order to create a J2K image out of it, we need to extract each fragments and concatenate them: </p>
<pre><code>$ gdcmraw -i D_CLUNIE_CT1_J2KR.dcm -o D_CLUNIE_CT1_J2KR.j2k
</code></pre>
<p> This is a valid J2K file, using the Kakadu software package: </p>
<pre><code>$ kdu_expand -i D_CLUNIE_CT1_J2KR.j2k -o D_CLUNIE_CT1_J2KR.tiff -record D_CLUNIE_CT1_J2KR.txt
</code></pre>
<pre><code>$ cat D_CLUNIE_CT1_J2KR.txt
</code></pre>
<pre><code>Sprofile=PROFILE2
Scap=no
Sextensions=0
Ssize={512,512}
Sorigin={0,0}
Stiles={512,512}
Stile_origin={0,0}
Scomponents=1
Ssigned=yes
Sprecision=16
Ssampling={1,1}
Sdims={512,512}
Cycc=no
Cmct=0
Clayers=1
Cuse_sop=no
Cuse_eph=no
Corder=LRCP
Calign_blk_last={no,no}
Clevels=5
Cads=0
Cdfs=0
Cdecomp=B(-:-:-)
Creversible=yes
Ckernels=W5X3
Catk=0
Cuse_precincts=no
Cblk={64,64}
Cmodes=0
Qguard=1
Qabs_ranges=18,19,19,20,19,19,20,19,19,20,19,19,20,19,19,20
&gt;&gt; New attributes for tile 0:
</code></pre>
<h3>Extract fragments as single file</h3>
<p> Sometimes each fragments is in fact a single slice, so we would not need to concatenate them: </p>
<pre><code>$ gdcmdump 00191113.dcm
</code></pre>
<pre><code>...
(7fe0,0010) OB # u/l,1 Pixel Data
  (fffe,e000) ?? 00\00\00\00\6b\38\01\00\10\77\02\00\37\b6\03\00\a7\f4\04\00 # 20,1 Item
  (fffe,e000) ?? ff\d8\ff\c3\00\0b\08\02\00\02\00\01\00\11\00\ff\c4\00\1b\00\01\01\01\01\01\01\01\01\00\00\00\00 # 79970,1 Item
  (fffe,e000) ?? ff\d8\ff\c3\00\0b\08\02\00\02\00\01\00\11\00\ff\c4\00\1b\00\01\01\01\01\01\01\01\01\00\00\00\00 # 81564,1 Item
  (fffe,e000) ?? ff\d8\ff\c3\00\0b\08\02\00\02\00\01\00\11\00\ff\c4\00\1b\00\01\01\01\01\01\01\01\01\00\00\00\00 # 81694,1 Item
  (fffe,e000) ?? ff\d8\ff\c3\00\0b\08\02\00\02\00\01\00\11\00\ff\c4\00\1b\00\01\01\01\01\01\01\01\01\00\00\00\00 # 81511 (81512),1 Item
(fffe,e0dd) 0
</code></pre>
<p> Let&#8217;s try to extract those 4 individual Lossless jpeg individually: </p>
<pre><code>$ gdcmraw --split-frags -i 00191113.dcm -o jpeg --pattern %02d.ljpeg
</code></pre>
<p> This will output 4 files: </p>
<pre><code>-rw-r--r-- 1 mathieu mathieu 81512 2008-08-08 22:10 jpeg03.ljpeg
-rw-r--r-- 1 mathieu mathieu 81694 2008-08-08 22:10 jpeg02.ljpeg
-rw-r--r-- 1 mathieu mathieu 81564 2008-08-08 22:10 jpeg01.ljpeg
-rw-r--r-- 1 mathieu mathieu 79970 2008-08-08 22:10 jpeg00.ljpeg
</code></pre>
<h2>Footnote about JPEG files</h2>
<p> It is a common misunderstanding to interchange &#8216;JPEG 8bits lossy&#8217; with simply JPEG file. The JPEG specification is much broader than simply the common lossy 8bits file (as found on internet). </p>
<p> You can have </p>
<dl>
<dt>*</dt>
<dd> <p> JPEG Lossy 8bits </p>
 </dd>
<dt>*</dt>
<dd> <p> JPEG Lossy 12bits </p>
 </dd>
<dt>*</dt>
<dd> <p> JPEG Lossless 2-16bits </p>
 </dd></dl>
<p> Those are what is defined in ITU-T T.81, ISO/IEC IS 10918-1.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gdcmdump/">gdcmdump</a></code>(1), <code><a href="/docs/linux/man/1-gdcmraw/">gdcmraw</a></code>(1)  </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2006-2010 Mathieu Malaterre </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">PARAMETERS</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">OPTIONS</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAG">PARAMETERS</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">OPTIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAI">general options</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAJ">Typical usage</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAK">Copy Attribute Value to file</a></dt>
<dd>  </dd>
<dt><a href="#lbAL">Extract Pixel Data</a></dt>
<dd>  </dd>
<dt><a href="#lbAM">Encapsulated Syntax</a></dt>
<dd>  </dd>
<dt><a href="#lbAN">Extract fragments as single file</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAO">Footnote about JPEG files</a></dt>
<dd>  </dd>
<dt><a href="#lbAP">SEE ALSO</a></dt>
<dd>  </dd>
<dt><a href="#lbAQ">COPYRIGHT</a></dt>
<dd>  </dd></dl>
