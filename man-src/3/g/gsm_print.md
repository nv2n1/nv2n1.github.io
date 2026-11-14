---
title: "gsm_print(3)"
name: "gsm_print"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gsm_print/"
---

<h2>NAME</h2>

 gsm_print --- GSM 06.10 supplementary function for debugging

<h2>SYNOPSIS</h2>

 #include &quot;gsm.h&quot; #include &lt;stdio.h&gt; 

 int gsm_print(f, g, frame); 
 FILE * f; 
 gsm g; 
 gsm_frame frame;

<h2>DESCRIPTION</h2>

 Gsm is an implementation of the final draft GSM 06.10 standard for full-rate speech transcoding, a lossy speech compression algorithm. The compressed form involves 76 variables with different numbers of significant bits packed into 33 bytes. 

 If you are interested in investigating the details of this coding scheme, gsm_print() can be used to dump the contents of individual gsm_frames to a file pointer provided by the application. 

<h2>RETURN VALUE</h2>

 gsm_print() returns -1 if the frame is invalid, else 0.

<h2>EXAMPLE</h2>

 A single frame looks like this: 
 <pre>
LARc:   29  32  20  11  08  05  06  07
#1:     Nc 0040    bc 0    Mc 1    xmaxc 60
        06 04 00 03 03 06 04 02 02 04 05 04 01
#2:     Nc 0045    bc 1    Mc 1    xmaxc 48
        03 07 01 03 04 04 07 01 03 02 04 05 03
#3:     Nc 0091    bc 1    Mc 1    xmaxc 46
        00 03 03 07 01 06 02 04 05 03 03 02 04
#4:     Nc 0120    bc 0    Mc 1    xmaxc 47
        07 03 06 00 03 03 06 05 00 03 02 07 04
</pre>

<h2>BUGS</h2>

 Please direct bug reports to jutta [at] cs.tu-berlin.de and cabo [at] cs.tu-berlin.de.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/3-gsm/">gsm</a>(3), <a HREF="/docs/linux/man/3-gsm_explode/">gsm_explode</a>(3) 

<h2>Index</h2>


