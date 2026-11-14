---
title: "gamma4scanimage(1)"
name: "gamma4scanimage"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gamma4scanimage/"
description: "gamma4scanimage – create a gamma table for scanimage"
---

<h2 class="name">NAME</h2>
<p> gamma4scanimage &#8211; create a gamma table for scanimage </p>
<h2>SYNOPSIS</h2>
<p> <code>gamma4scanimage</code> <i>gamma</i> [<i>shadow</i> [<i>highlight</i> [<i>maxin</i> [<i>maxout</i>]]]] </p>
<h2>DESCRIPTION</h2>
<p> The tool <code>gamma4scanimage</code> creates a gamma table in the format expected by scanimage. You can define a <code>gamma,</code> a <code>shadow</code> and a <code>highlight</code> value. You also can specify the size (<code>maxin</code>) and maximum output value (<code>maxout</code>) of the gamma table. </p>
<p> <code>gamma</code> is a floating point value, neutral value being 1.0. If the value is larger than 1.0 then the image is brighter. </p>
<p> <code>shadow</code> defines the minimum input value that is necessary to create an output value larger than zero. shadow has to be in the range [0..<code>maxin</code>]. Its default value is 0. </p>
<p> <code>highlight</code> defines the maximum input value that produces an output value smaller than maxout. highlight must be in the range [0..<code>maxin</code>] and larger than shadow. Its default value is the same as <code>maxin</code> (16383 if not set). </p>
<p> <code>maxin</code> defines the size of the gamma table. The size depends on the scanner/backend. If the scanner uses 8 bit gamma input then <code>maxin</code> must be set to 255, 1023 for 10 bits, 4095 for 12 bits, and 16383 for 14 bits. The default is 16383. To find out what value <code>maxin</code> has to be, call <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1) with a very large gamma table [0]0-[99999]255 and <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1) will print an error message with the needed gamma table size. </p>
<p> <code>maxout</code> defines the maximum output value. Take a look at the output of <i>scanimage -h</i> to find out what <code>maxout</code> must be. The default value is 255. </p>
<h2>EXAMPLE</h2>
<p> scanimage &#8211;custom-gamma=yes &#8211;gamma-table `gamma4scanimage 1.8 0 11500 16383 255` &gt;image.pnm </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Oliver Rauch </p>
<h2>EMAIL-CONTACT</h2>
<p> <i>Oliver.Rauch [at] Rauch-Domain.DE</i> </p>
<h2>Index</h2>
