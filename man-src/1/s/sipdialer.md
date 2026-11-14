---
title: "sipdialer(1)"
name: "sipdialer"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sipdialer/"
description: "sipdialer – initiate phone call (click-to-call)"
---

<h2>NAME</h2>
<p> sipdialer &#8211; initiate phone call (click-to-call)</p>
<h2>SYNOPSIS</h2>
<p> <code>sipdialer URI</code></p>
<h2>DESCRIPTION</h2>
<p> sipdialer attempts to contact the phone described in ~/.sipdial/sipdial.cfg, sending a SIP REFER message to the phone, instructing it to dial the remote party specified by the URI parameter on the command line. sipdialer is typically registered in the gconf database or in the web browser configuration so that it will be invoked when the user clicks a sip:, sips: or tel: URI.</p>
<h2>AUTHOR</h2>
<p> Daniel Pocock &lt;daniel [at] pocock.com.au&gt;</p>
<h2>REPORTING BUGS</h2>
<p> See <a rel="nofollow" href="http://www.resiprocate.org">http://www.resiprocate.org</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2007 Daniel Pocock &#8211; licenced under BSD terms </p>
<h2>Index</h2>
