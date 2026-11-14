---
title: "perldeprecation(1)"
name: "perldeprecation"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perldeprecation/"
description: "perldeprecation – list Perl deprecations"
---

<h2 class="name">NAME</h2>
<p> perldeprecation &#8211; list Perl deprecations </p>
<h2>DESCRIPTION</h2>
<p> The purpose of this document is to document what has been deprecated in Perl, and by which version the deprecated feature will disappear, or, for already removed features, when it was removed. </p>
<p> This document will try to discuss what alternatives for the deprecated features are available. </p>
<p> The deprecated features will be grouped by the version of Perl in which they will be removed.</p>
<h3>Perl 5.32</h3>
<p> <i>Constants from lexical variables potentially modified elsewhere</i> </p>
<p> You wrote something like </p>
<pre>
    my $var;
    $sub = sub () { $var };
</pre>
<p> but <tt>$var</tt> is referenced elsewhere and could be modified after the <tt>&quot;sub&quot;</tt> expression is evaluated. Either it is explicitly modified elsewhere (<tt>&quot;$var = 3&quot;</tt>) or it is passed to a subroutine or to an operator like <tt>&quot;printf&quot;</tt> or <tt>&quot;map&quot;</tt>, which may or may not modify the variable. </p>
<p> Traditionally, Perl has captured the value of the variable at that point and turned the subroutine into a constant eligible for inlining. In those cases where the variable can be modified elsewhere, this breaks the behavior of closures, in which the subroutine captures the variable itself, rather than its value, so future changes to the variable are reflected in the subroutine&#8217;s return value. </p>
<p> If you intended for the subroutine to be eligible for inlining, then make sure the variable is not referenced elsewhere, possibly by copying it: </p>
<pre>
    my $var2 = $var;
    $sub = sub () { $var2 };
</pre>
<p> If you do want this subroutine to be a closure that reflects future changes to the variable that it closes over, add an explicit <tt>&quot;return&quot;</tt>: </p>
<pre><code>
my $var;
$sub = sub(){return $var};
</code></pre>
<p> This usage has been deprecated, and will no longer be allowed in Perl 5.32. </p>
<p> <i>Use of strings with code points over 0xFF as arguments to </i>&quot;vec&quot;<i></i> </p>
<p> <tt>&quot;vec&quot;</tt> views its string argument as a sequence of bits. A string containing a code point over 0xFF is nonsensical. This usage is deprecated in Perl 5.28, and will be removed in Perl 5.32. </p>
<p> <i>Use of code points over 0xFF in string bitwise operators</i> </p>
<p> The string bitwise operators, <tt>&quot;&amp;&quot;</tt>, <tt>&quot;|&quot;</tt>, <tt>&quot;^&quot;</tt>, and <tt>&quot;~&quot;</tt>, treat their operands as strings of bytes. As such, values above 0xFF are nonsensical. Some instances of these have been deprecated since Perl 5.24, and were made fatal in 5.28, but it turns out that in cases where the wide characters did not affect the end result, no deprecation notice was raised, and so remain legal. Now, all occurrences either are fatal or raise a deprecation warning, so that the remaining legal occurrences will be fatal in 5.32. </p>
<p> An example of this is </p>
<pre>
 &quot;&quot; &amp; &quot;
