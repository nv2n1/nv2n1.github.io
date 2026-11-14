---
title: "xkblatchmodifiers(3)"
name: "xkblatchmodifiers"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkblatchmodifiers/"
---

XkbLatchModifiers - Latches and unlatches any of the eight real keyboard modifiers 

<h2>Synopsis</h2><dl COMPACT><dt> <b>Bool XkbLatchModifiers</b> <b>(Display *</b><i>display</i><b>,</b> <b>unsigned int </b><i>device_spec</i><b>,</b> <b>unsigned int </b><i>affect</i><b>,</b> <b>unsigned int </b><i>values</i><b>);</b> 
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl><h2>Arguments</h2><dl COMPACT><dt><i>display</i>
<dd><dd>connection to the X server
<dt><i>device_spec</i>
<dd>device ID, or XkbUseCoreKbd
<dt><i>affect</i>
<dd>mask of real modifiers whose lock state is to change
<dt><i>values</i>
<dd>1 =&gt; lock, 0 =&gt; unlock; only for modifiers selected by affect</dl><h2>Description</h2><i>XkbLatchModifiers </i> sends a request to the server to latch the real modifiers selected by both <i>affect </i> and <i>values </i> and to unlatch the real modifiers selected by <i>affect</i> , but not selected by <i>values. </i> 

 <i>XkbLatchModifiers </i> does not wait for a reply from the server. It returns True if the request was sent, and False otherwise. 

 The functions in this section that change the use of modifiers use a mask in the parameter affect. It is a bitwise inclusive OR of the legal modifier masks: 

 <table> <tr VALIGN=top><td ALIGN=center>Table 1 Real Modifier Masks
</td></tr><tr VALIGN=top><td><hr></td></tr><tr VALIGN=top><td>Mask
</td></tr><tr VALIGN=top><td><hr></td></tr><tr VALIGN=top><td>ShiftMask
</td></tr><tr VALIGN=top><td>LockMask
</td></tr><tr VALIGN=top><td>ControlMask
</td></tr><tr VALIGN=top><td>Mod1Mask
</td></tr><tr VALIGN=top><td>Mod2Mask
</td></tr><tr VALIGN=top><td>Mod3Mask
</td></tr><tr VALIGN=top><td>Mod4Mask
</td></tr><tr VALIGN=top><td>Mod5Mask
</td></tr> </table><h2>Return Values</h2><dl COMPACT><dt>True
<dd>The <i>XkbLatchModifiers </i> function returns True if a request was sent to the server to latch the real modifiers selected by both <i>affect </i> and <i>values </i> and to unlatch the real modifiers selected by <i>affect</i> , but not selected by <i>values. </i>
<dt>False
<dd>The <i>XkbLatchModifiers </i> function returns False if the request was not sent. 

 

</dl>
