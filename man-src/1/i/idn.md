---
title: "idn(1)"
name: "idn"
section: "1"
letter: "i"
url: "/docs/linux/man/1-idn/"
description: "idn – Internationalized Domain Names command line tool"
---

<h2>NAME</h2>
<p> idn &#8211; Internationalized Domain Names command line tool</p>
<h2>SYNOPSIS</h2>
<p> <code>idn</code> [<i>OPTION</i>]&#8230; [<i>STRINGS</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Internationalized Domain Name (IDN) convert STRINGS, or standard input. </p>
<p> Command line interface to the internationalized domain name library. </p>
<p> All strings are expected to be encoded in the preferred charset used by your locale. Use `&#8211;debug&#8217; to find out what this charset is. You can override the charset used by setting environment variable CHARSET. </p>
<p> To process a string that starts with `-&#8216;, for example `-foo&#8217;, use `&#8211;&#8216; to signal the end of parameters, as in `idn <code>&#8211;quiet</code> <code>-a</code> <code>&#8212;</code> <code>-foo</code>&#8216;. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print help and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print version and exit</p>
<dt><code>-s</code>, <code>&#8211;stringprep</code></p>
<dd> Prepare string according to nameprep profile</p>
<dt><code>-d</code>, <code>&#8211;punycode-decode</code></p>
<dd> Decode Punycode</p>
<dt><code>-e</code>, <code>&#8211;punycode-encode</code></p>
<dd> Encode Punycode</p>
<dt><code>-a</code>, <code>&#8211;idna-to-ascii</code></p>
<dd> Convert to ACE according to IDNA (default mode)</p>
<dt><code>-u</code>, <code>&#8211;idna-to-unicode</code></p>
<dd> Convert from ACE according to IDNA</p>
<dt><code>&#8211;allow-unassigned</code></p>
<dd> Toggle IDNA AllowUnassigned flag (default off)</p>
<dt><code>&#8211;usestd3asciirules</code></p>
<dd> Toggle IDNA UseSTD3ASCIIRules flag (default off)</p>
<dt><code>&#8211;no-tld</code></p>
<dd> Don&#8217;t check string for TLD specific rules Only for <code>&#8211;idna-to-ascii</code> and <code>&#8211;idna-to-unicode</code></p>
<dt><code>-n</code>, <code>&#8211;nfkc</code></p>
<dd> Normalize string according to Unicode v3.2 NFKC</p>
<dt><code>-p</code>, <code>&#8211;profile</code>=<i>STRING</i></p>
<dd> Use specified stringprep profile instead Valid stringprep profiles: `Nameprep&#8217;, `iSCSI&#8217;, `Nodeprep&#8217;, `Resourceprep&#8217;, `trace&#8217;, `SASLprep&#8217;</p>
<dt><code>&#8211;debug</code></p>
<dd> Print debugging information</p>
<dt><code>&#8211;quiet</code></p>
<dd> Silent operation</dl>
<h2>AUTHOR</h2>
<p> Written by Simon Josefsson.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to: bug-libidn [at] gnu.org<br />
 GNU Libidn home page: &lt;<a rel="nofollow" href="http://www.gnu.org/software/libidn/">http://www.gnu.org/software/libidn/</a>&gt;<br />
 General help using GNU software: &lt;<a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2013 Simon Josefsson. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>idn</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>idn</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info idn</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
