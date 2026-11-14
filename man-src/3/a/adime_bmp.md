---
title: "adime_bmp(3)"
name: "adime_bmp"
section: "3"
letter: "a"
url: "/docs/linux/man/3-adime_bmp/"
description: "adime_bmp"
---

<h2>NAME</h2>
<p> adime_bmp</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/adime.h">adime.h</a>&gt;</code> </p>
<p> <code>BITMAP *adime_bmp;</code></p>
<h2>DESCRIPTION</h2>
<p> If you want the dialog to be displayed on a certain video bitmap other than `screen&#8217;, set this to point to that bitmap. This is particulary useful if you for some reason have scrolled away from the top left area of the video memory and want the dialog to be displayed on currently visible video memory rather than on the default location. If this is NULL (it is by default), `adime_dialogf()&#8217; &amp; co will scroll to the top left corner of screen and use that part to display the dialog on. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-adime_dialogf/">adime_dialogf</a></code>(3), <code><a href="/docs/linux/man/3-adime_font/">adime_font</a></code>(3) </p>
<h2>Index</h2>
