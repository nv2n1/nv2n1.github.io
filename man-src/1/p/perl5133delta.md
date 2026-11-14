---
title: "perl5133delta(1)"
name: "perl5133delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5133delta/"
description: "perl5133delta – what is new for perl v5.13.3"
---

<h2 class="name">NAME</h2>
<p> perl5133delta &#8211; what is new for perl v5.13.3 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.13.3 release and the 5.13.2 release. </p>
<p> If you are upgrading from an earlier release such as 5.13.1, first read perl5132delta, which describes differences between 5.13.1 and 5.13.2.</p>
<h2>Core Enhancements</h2>
<h3>\o{&#8230;} for octals</h3>
<p> There is a new escape sequence, <tt>&quot;\o&quot;</tt>, in double-quote-like contexts. It must be followed by braces enclosing an octal number of at least one digit. It interpolates as the character with an ordinal value equal to the octal number. This construct allows large octal ordinals beyond the current max of 0777 to be represented. It also allows you to specify a character in octal which can safely be concatenated with other regex snippets and which won&#8217;t be confused with being a backreference to a regex capture group. See &#8220;Capture groups&#8221; in perlre.</p>
<h3>\N{<i>name</i>} and charnames enhancements</h3>
<p> <tt>&quot;\N{}&quot;</tt> and <tt>&quot;charnames::vianame&quot;</tt> now know about the abbreviated character names listed by Unicode, such as <font SIZE="-1">NBSP</font>, <font SIZE="-1">SHY</font>, <font SIZE="-1">LRO</font>, <font SIZE="-1">ZWJ</font>, etc., as well as all the customary abbreviations for the C0 and C1 control characters (such as <font SIZE="-1">ACK</font>, <font SIZE="-1">BEL</font>, <font SIZE="-1">CAN</font>, etc.), as well as a few new variants in common usage of some C1 full names. </p>
<p> In the past, it was ineffective to override one of Perl&#8217;s abbreviations with your own custom alias. Now it works. </p>
<p> You can also create a custom alias directly to the ordinal of a character, known by <tt>&quot;\N{...}&quot;</tt>, <tt>&quot;charnames::vianame()&quot;</tt>, and <tt>&quot;charnames::viacode()&quot;</tt>. Previously, an alias had to be to an official Unicode character name. This made it impossible to create an alias for a code point that had no name, such as the ones reserved for private use. So this change allows you to make more effective use of private use characters. Only if there is no official name will <tt>&quot;charnames::viacode()&quot;</tt> return your custom one. </p>
<p> See charnames for details on all these changes.</p>
<h3>Uppercase X/B allowed in hexadecimal/binary literals</h3>
<p> Literals may now use either upper case <tt>&quot;0X...&quot;</tt> or <tt>&quot;0B...&quot;</tt> prefixes, in addition to the already supported <tt>&quot;0x...&quot;</tt> and <tt>&quot;0b...&quot;</tt> syntax. (RT#76296) (a674e8d, 333f87f) </p>
<p> C, Ruby, Python and <font SIZE="-1">PHP</font> already supported this syntax, and it makes Perl more internally consistent. A round-trip with <tt>&quot;eval sprintf &quot;%#X&quot;, 0x10&quot;</tt> now returns <tt>16</tt> in addition to <tt>&quot;eval sprintf &quot;%#x&quot;, 0x10&quot;</tt>, which worked before.</p>
<h2>Incompatible Changes</h2>
<h3>\400 &#8211; \777</h3>
<p> Use of <tt>&quot;\400&quot;</tt> &#8211; <tt>&quot;\777&quot;</tt> in regexes in certain circumstances has given different, anomalous behavior than their use in all other double-quote-like contexts. Since 5.10.1, a deprecated warning message has been raised when this happens. Now, all double-quote-like contexts have the same behavior, namely to be equivalent to <tt>&quot;
