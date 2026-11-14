---
title: "aggregate(1)"
name: "aggregate"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aggregate/"
description: "aggregate – optimise a list of route prefixes to help make nice short filters"
---

<h2>NAME</h2>
<p> <code>aggregate</code> &#8211; optimise a list of route prefixes to help make nice short filters </p>
<h2>SYNOPSIS</h2>
<p> <code>aggregate</code> [-m max-length] [-o max-opt-length] [-p default-length] [-q] [-t] [-v] </p>
<h2>DESCRIPTION</h2>
<p> Takes a list of prefixes in conventional format on stdin, and performs two optimisations to attempt to reduce the length of the prefix list. </p>
<p> The first optimisation is to remove any supplied prefixes which are superfluous because they are already included in another supplied prefix. For example, 203.97.2.0/24 would be removed if 203.97.0.0/17 was also supplied. </p>
<p> The second optimisation identifies adjacent prefixes that can be combined under a single, shorter-length prefix. For example, 203.97.2.0/24 and 203.97.3.0/24 can be combined into the single prefix 203.97.2.0/23. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-m max-length</code></p>
<dd> Sets the maximum prefix length for entries read from stdin <i>max_length</i> bits. The default is 32. Prefixes with longer lengths will be discarded prior to processing. </p>
<dt><code>-o max-opt-length</code></p>
<dd> Sets the maximum prefix length for optimisation to <i>max-opt-length</i> bits. The default is 32. Prefixes with longer lengths will not be subject to optimisation. </p>
<dt><code>-p default-length</code></p>
<dd> Sets the default prefix length. There is no default; without this option a prefix without a mask length is treated as invalid. Use <code>-p 32 -m 32 -o 32</code> to aggregate a list of host routes specified as bare addresses, for example. </p>
<dt><code>-q</code></p>
<dd> Sets quiet mode &#8212; instructs <code>aggregate</code> never to generate warning messages or other output on stderr. </p>
<dt><code>-t</code></p>
<dd> Silently truncate prefixes that seem to have an inconsistent prefix: e.g. an input prefix 203.97.2.226/24 would be truncated to 203.97.2.0/24. Without this option an input prefix 203.97.2.226/24 would not be accepted, and a warning about the inconsistent mask would be generated. </p>
<dt><code>-v</code></p>
<dd> Sets verbose mode. This changes the output format to display the source line number that the prefix was obtained from, together with a preceding &quot;-&quot; to indicate a route that can be suppressed, or a &quot;+&quot; to indicate a shorter-prefix aggregate that was added by <code>aggregate</code> as an adjacency optimisation. Note that verbose output continues even if -q is selected.</dl>
<h2>DIAGNOSTICS</h2>
<p> <code>Aggregate</code> exits 0 on success, and &gt;0 if an error occurs. </p>
<h2>EXAMPLES</h2>
<p> The following list of prefixes: </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>193.58.204.0/22<br />
&nbsp;<wbr>&nbsp;<wbr>193.58.208.0/22<br />
&nbsp;<wbr>&nbsp;<wbr>193.193.160.0/22<br />
&nbsp;<wbr>&nbsp;<wbr>193.193.168.0/22<br />
&nbsp;<wbr>&nbsp;<wbr>193.243.164.0/22<br />
&nbsp;<wbr>&nbsp;<wbr>194.126.128.0/22<br />
&nbsp;<wbr>&nbsp;<wbr>194.126.132.0/22<br />
&nbsp;<wbr>&nbsp;<wbr>194.126.134.0/23<br />
&nbsp;<wbr>&nbsp;<wbr>194.151.128.0/19<br />
&nbsp;<wbr>&nbsp;<wbr>195.42.240.0/21<br />
&nbsp;<wbr>&nbsp;<wbr>195.240.0.0/16<br />
&nbsp;<wbr>&nbsp;<wbr>195.241.0.0/16 </code> </p>
<p> is optimised as followed by <code>aggregate</code> (output shown using the <i>-v</i> flag): </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>aggregate: maximum prefix length permitted will be 24<br />
&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0]&nbsp;<wbr>+&nbsp;<wbr>193.58.204.0/21<br />
&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1]&nbsp;<wbr>&#8211; 193.58.204.0/22<br />
&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2]&nbsp;<wbr>&#8211; 193.58.208.0/22<br />
&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>193.193.160.0/22<br />
&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>4]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>193.193.168.0/22<br />
&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>5]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>193.243.164.0/22<br />
&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0]&nbsp;<wbr>+&nbsp;<wbr>194.126.128.0/21<br />
&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>6]&nbsp;<wbr>&#8211; 194.126.128.0/22<br />
&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>7]&nbsp;<wbr>&#8211; 194.126.132.0/22<br />
&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>8]&nbsp;<wbr>&#8211; 194.126.134.0/23<br />
&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>9]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>194.151.128.0/19<br />
&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>195.42.240.0/21<br />
&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0]&nbsp;<wbr>+&nbsp;<wbr>195.240.0.0/15<br />
&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>11]&nbsp;<wbr>&#8211; 195.240.0.0/16<br />
&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>12]&nbsp;<wbr>&#8211; 195.241.0.0/16 </code> </p>
<p> Note that 193.58.204.0/22 and 193.58.208.0/22 were combined under the single prefix 193.58.204.0/21, and 194.126.134.0/23 was suppressed because it was included in 194.126.132.0/22. The number in square brackets at the beginning of each line indicates the original line number, or zero for new prefixes that were introduced by <code>aggregate.</code> </p>
<p> The output without the <i>-v</i> flag is as follows: </p>
<p> <code><br />
&nbsp;<wbr>&nbsp;<wbr>193.58.204.0/21<br />
&nbsp;<wbr>&nbsp;<wbr>193.193.160.0/22<br />
&nbsp;<wbr>&nbsp;<wbr>193.193.168.0/22<br />
&nbsp;<wbr>&nbsp;<wbr>193.243.164.0/22<br />
&nbsp;<wbr>&nbsp;<wbr>194.126.128.0/21<br />
&nbsp;<wbr>&nbsp;<wbr>194.151.128.0/19<br />
&nbsp;<wbr>&nbsp;<wbr>195.42.240.0/21<br />
&nbsp;<wbr>&nbsp;<wbr>195.240.0.0/15 </code> </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-aggregate-ios/">aggregate-ios</a>(1) </p>
<h2>HISTORY</h2>
<p> <code>Aggregate</code> was written by Joe Abley &lt;jabley [at] mfnx.net&gt;, and has been reasonably well tested. It is suitable for reducing customer prefix filters for production use without extensive hand-proving of results. </p>
<p> Autoconf bits were donated by Michael Shields &lt;michael.shields [at] mfn.com&gt;. The <code>-t</code> option was suggested by Robin Johnson &lt;robbat2 [at] fermi.orbis-terrarum.net&gt;, and the treatment of leading zeros on octet parsing was changed following comments from Arnold Nipper &lt;arnold [at] nipper.de&gt;. </p>
<p> An early version of <code>aggregate</code> would attempt to combine adjacent prefixes regardless of whether the first prefix lay on an appropriate bit boundary or not (pointed out with great restraint by Robert Noland &lt;rnoland [at] 2hip.net&gt;). </p>
<h2>BUGS</h2>
<p> Common unix parsing of IPv4 addresses understands the representation of individual octets in octal or hexadecimal, following a &quot;0&quot; or &quot;0x&quot; prefix, respectively. That convention has been deliberately disabled here, since resources such as the IRR do not follow the convention, and confusion can result. </p>
<p> For extremely sensitive applications, judicious use of the <i>-v</i> option together with a pencil and paper is probably advisable. </p>
<h2>Index</h2>
