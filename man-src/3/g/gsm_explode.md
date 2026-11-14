---
title: "gsm_explode(3)"
name: "gsm_explode"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gsm_explode/"
---

<h2>NAME</h2>

 gsm_explode, gsm_implode --- GSM 06.10 supplementary functions for testing

<h2>SYNOPSIS</h2>

 #include &quot;gsm.h&quot; 

 void gsm_explode(g, frame, xframe) 
 gsm g; 
 gsm_frame frame; 
 gsm_signal xframe[ 76 ]; 

 void gsm_implode(g, xframe, frame) 
 gsm g; 
 gsm_signal xframe[ 76 ]; 
 gsm_frame frame;

<h2>DESCRIPTION</h2>

 Gsm is an implementation of the final draft GSM 06.10 standard for full-rate speech transcoding. Test data for implementations of this particular document can be bought and used to verify an implementation. 

 The encoded test data uses a format different from what one would use to transmit frames with the least number of bits. Gsm_explode() and gsm_implode() convert between the internal, small, 33-byte format and the 76-word format used by the test data. 

<h2>RETURN VALUE</h2>

 gsm_explode() returns -1 if the passed frame is invalid, else 0.

<h2>BUGS</h2>

 Please direct bug reports to jutta [at] cs.tu-berlin.de and cabo [at] cs.tu-berlin.de.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/3-gsm/">gsm</a>(3) 

<h2>Index</h2>


