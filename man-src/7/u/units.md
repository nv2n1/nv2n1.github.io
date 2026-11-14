---
title: "units(7)"
name: "units"
section: "7"
letter: "u"
url: "/docs/linux/man/7-units/"
---

units - decimal and binary prefixes

<h2>Description</h2>

<h3>Decimal prefixes</h3>

The SI system of units uses prefixes that indicate powers of ten. A kilometer is 1000 meter, and a megawatt is 1000000 watt. Below the standard prefixes.
<dl><dd><table> <tr VALIGN=top><td>Prefix</td><td>Name</td><td>Value
</td></tr><tr VALIGN=top><td>y</td><td>yocto</td><td>10^-24 = 0.000000000000000000000001
</td></tr><tr VALIGN=top><td>z</td><td>zepto</td><td>10^-21 = 0.000000000000000000001
</td></tr><tr VALIGN=top><td>a</td><td>atto</td><td>10^-18 = 0.000000000000000001
</td></tr><tr VALIGN=top><td>f</td><td>femto</td><td>10^-15 = 0.000000000000001
</td></tr><tr VALIGN=top><td>p</td><td>pico</td><td>10^-12 = 0.000000000001
</td></tr><tr VALIGN=top><td>n</td><td>nano</td><td>10^-9 = 0.000000001
</td></tr><tr VALIGN=top><td>&micro;</td><td>micro</td><td>10^-6 = 0.000001
</td></tr><tr VALIGN=top><td>m</td><td>milli</td><td>10^-3 = 0.001
</td></tr><tr VALIGN=top><td>c</td><td>centi</td><td>10^-2 = 0.01
</td></tr><tr VALIGN=top><td>d</td><td>deci</td><td>10^-1 = 0.1
</td></tr><tr VALIGN=top><td>da</td><td>deka</td><td>10^ 1 = 10
</td></tr><tr VALIGN=top><td>h</td><td>hecto</td><td>10^ 2 = 100
</td></tr><tr VALIGN=top><td>k</td><td>kilo</td><td>10^ 3 = 1000
</td></tr><tr VALIGN=top><td>M</td><td>mega</td><td>10^ 6 = 1000000
</td></tr><tr VALIGN=top><td>G</td><td>giga</td><td>10^ 9 = 1000000000
</td></tr><tr VALIGN=top><td>T</td><td>tera</td><td>10^12 = 1000000000000
</td></tr><tr VALIGN=top><td>P</td><td>peta</td><td>10^15 = 1000000000000000
</td></tr><tr VALIGN=top><td>E</td><td>exa</td><td>10^18 = 1000000000000000000
</td></tr><tr VALIGN=top><td>Z</td><td>zetta</td><td>10^21 = 1000000000000000000000
</td></tr><tr VALIGN=top><td>Y</td><td>yotta</td><td>10^24 = 1000000000000000000000000
</td></tr> </table></dl>
 

 The symbol for micro is the Greek letter mu, often written u in an ASCII context where this Greek letter is not available. See also 

<dl><dd></dl>

<h3>Binary prefixes</h3>

The binary prefixes resemble the decimal ones, but have an additional 'i' (and &quot;Ki&quot; starts with a capital 'K'). The names are formed by taking the first syllable of the names of the decimal prefix with roughly the same size, followed by &quot;bi&quot; for &quot;binary&quot;.
<dl><dd><table> <tr VALIGN=top><td>Prefix</td><td>Name</td><td>Value
</td></tr><tr VALIGN=top><td>Ki</td><td>kibi</td><td>2^10 = 1024
</td></tr><tr VALIGN=top><td>Mi</td><td>mebi</td><td>2^20 = 1048576
</td></tr><tr VALIGN=top><td>Gi</td><td>gibi</td><td>2^30 = 1073741824
</td></tr><tr VALIGN=top><td>Ti</td><td>tebi</td><td>2^40 = 1099511627776
</td></tr><tr VALIGN=top><td>Pi</td><td>pebi</td><td>2^50 = 1125899906842624
</td></tr><tr VALIGN=top><td>Ei</td><td>exbi</td><td>2^60 = 1152921504606846976
</td></tr> </table></dl>
 

 See also

<h3>Discussion</h3>

Before these binary prefixes were introduced, it was fairly common to use k=1000 and K=1024, just like b=bit, B=byte. Unfortunately, the M is capital already, and cannot be capitalized to indicate binary-ness. 

 At first that didn't matter too much, since memory modules and disks came in sizes that were powers of two, so everyone knew that in such contexts &quot;kilobyte&quot; and &quot;megabyte&quot; meant 1024 and 1048576 bytes, respectively. What originally was a sloppy use of the prefixes &quot;kilo&quot; and &quot;mega&quot; started to become regarded as the &quot;real true meaning&quot; when computers were involved. But then disk technology changed, and disk sizes became arbitrary numbers. After a period of uncertainty all disk manufacturers settled on the standard, namely k=1000, M=1000 k, G=1000 M. 

 The situation was messy: in the 14k4 modems, k=1000; in the 1.44 MB diskettes, M=1024000; and so on. In 1998 the IEC approved the standard that defines the binary prefixes given above, enabling people to be precise and unambiguous. 

 Thus, today, MB = 1000000 B and MiB = 1048576 B. 

 In the free software world programs are slowly being changed to conform. When the Linux kernel boots and says 

 hda: 120064896 sectors (61473 MB) w/2048KiB Cache 

 the MB are megabytes and the KiB are kibibytes.

<h2>Colophon</h2>

This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" HREF="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> 
