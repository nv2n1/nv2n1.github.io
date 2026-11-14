---
title: "psf(8)"
name: "psf"
section: "8"
letter: "p"
url: "/docs/linux/man/8-psf/"
description: "psf – PostScript filter"
---

<p>psf &#8211; PostScript filter</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>psf</code> [-n&nbsp;<wbr><i>name</i>] [-h&nbsp;<wbr><i>host</i>] [-w&nbsp;<wbr><i>width</i>] [-l&nbsp;<wbr><i>length</i>] [-i&nbsp;<wbr><i>indent</i>] [-c]</dl>
<h2>Description</h2>
<p><code>psf</code></p>
<dd>is an <code>lpd</code> filter for PostScript printing. <code>psf</code> interprets the name it was called with to determine what filters to invoke. First, if the string &#8220;pap&#8221; appears anywhere in the name, <code>psf</code> invokes <code>pap</code> to talk to a printer via AppleTalk. Next, if the string &#8220;rev&#8221; appears, <code>psf</code> invokes <code>psorder</code> to reverse the pages of the job. Finally, if <code>psf</code> was called with a filter&#8217;s name as the leading string, it invokes that filter. If there is no filter to run, <code>psf</code> examines the magic number of the input, and if the input is not PostScript, converts it to PostScript.</p>
<h2>Kludge</h2>
<p>In the default configuration, <code>psf</code> supports two kludges. The first causes <code>psf</code> to check its name for the letter `m&#8217;. If this letter is found and accounting is turned on, <code>psf</code> calls <code>pap</code> twice, once to get an initial page count and to print the job, and another time to get a final page count. This is a work-around for bugs in a variety of PAP implementions that cause printers to never properly close the PAP output file. A notable example is any printer by Hewlett-Packard. </p>
<p> The second kludge causes <code>psf</code> to examine its name for the letter `w&#8217;. If this letter is found and accounting is turned on, <code>psf</code> calls <code>pap</code> with the <code>-w</code> flag. This flag causes <code>pap</code> to wait until the printer&#8217;s status contains the string `idle&#8217;. Once this string is found, the job is printed as normal. This kludge is a work-around for printers, notably Hewlett-Packard&#8217;s LaserJet IV, which will report a page count while a previous jobs is still printing.</p>
<h2>Example</h2>
<p>The sample <code>printcap</code> entry below invokes <code>psf</code> to print text files, PostScript files, <code>troff</code>&#8216;s C/A/T output, and <code>TeX</code>&#8216;s DVI output, to an AppleTalk connected LaserWriter Plus. Since the LaserWriter Plus stacks pages in descending order, we reverse the pages and print the burst page last. </p>
<dl>
<dd>
<pre>laser|lp|LaserWriter Plus on AppleTalk:\
 :sd=/usr/spool/lpd/laser:\
 :lp=/usr/spool/lpd/laser/null:\
 :lf=/var/adm/lpd-errs:pw#80:hl:\
 :of=/usr/libexec/ofpap:\
 :if=/usr/libexec/ifpaprev:\
 :tf=/usr/libexec/tfpaprev:\
 :df=/usr/libexec/dfpaprev:</pre>
</dl>
<p> Note that if the host in question spools to more than one AppleTalk printer, /dev/null should not be used for the <code>lp</code> capability. Instead, a null device should be created with <code>mknod</code> for each printer, as has been done above. </p>
<p> Finally, there is a file in the spool directory, /var/spool/lpd/laser, called <code>.paprc</code>, which <code>pap</code> reads for the AppleTalk name of the printer.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-psorder/">psorder</a></code>(1), <code><a href="/docs/linux/man/5-printcap/">printcap</a></code>(5), <code><a href="/docs/linux/man/1-lpd/">lpd</a></code>(1), <code><a href="/docs/linux/man/1-mknod/">mknod</a></code>(1), <code><a href="/docs/linux/man/1-pap/">pap</a></code>(1). </p>
