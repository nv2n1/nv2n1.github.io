---
title: "perlunicook(1)"
name: "perlunicook"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlunicook/"
description: "perlunicook – cookbookish examples of handling Unicode in Perl"
---

<h2 class="name">NAME</h2>
<p> perlunicook &#8211; cookbookish examples of handling Unicode in Perl </p>
<h2>DESCRIPTION</h2>
<p> This manpage contains short recipes demonstrating how to handle common Unicode operations in Perl, plus one complete program at the end. Any undeclared variables in individual recipes are assumed to have a previous appropriate value in them.</p>
<h2>EXAMPLES</h2>
<h3>℞ 0: Standard preamble</h3>
<p> Unless otherwise notes, all examples below require this standard preamble to work correctly, with the <tt>&quot;#!&quot;</tt> adjusted to work on your system: </p>
<pre><code>
#!/ usr / bin / env perl
use utf8;
#so literals and identifiers can be in UTF - 8 use v5 .12;
# or later to get "unicode_strings" feature
         use strict;
#quote strings, declare variables
                    use warnings;
#on by default use warnings qw(FATAL utf8);
#fatalize encoding glitches
    use open qw(
        : std
        : encoding(UTF - 8));
#undeclared streams in UTF - 8 use charnames qw(
                                 : full
                                 : short);
#unneeded in v5 .16
</code></pre>
<p> This <i>does</i> make even Unix programmers <tt>&quot;binmode&quot;</tt> your binary streams, or open them with <tt>&quot;:raw&quot;</tt>, but that&#8217;s the only way to get at them portably anyway. </p>
<p> <font SIZE="-1"><code>WARNING</code></font>: <tt>&quot;use autodie&quot;</tt> (pre 2.26) and <tt>&quot;use open&quot;</tt> do not get along with each other.</p>
<h3>℞ 1: Generic Unicode-savvy filter</h3>
<p> Always decompose on the way in, then recompose on the way out. </p>
<p>use Unicode::Normalize;<br />
while (&lt;&gt;) {<br />
    $_ = NFD($_);<br />
#decompose + reorder canonically&#8230;<br />
}<br />
continue<br />
{<br />
    print NFC($_);<br />
#recompose(where possible) + reorder canonically<br />
}</p>
<h3>℞ 2: Fine-tuning Unicode warnings</h3>
<p> As of v5.14, Perl distinguishes three subclasses of UTF‑8 warnings. </p>
<p>use v5 .14;<br />
#subwarnings unavailable any earlier<br />
    no warnings &#8220;nonchar&#8221;;<br />
#the 66 forbidden non &#8211; characters<br />
                            no warnings &#8220;surrogate&#8221;;<br />
#UTF &#8211; 16 / CESU &#8211; 8 nonsense no warnings &#8220;non_unicode&#8221;;<br />
#for codepoints over 0x10_FFFF</p>
<h3>℞ 3: Declare source in utf8 for identifiers and literals</h3>
<p> Without the all-critical <tt>&quot;use utf8&quot;</tt> declaration, putting UTF‑8 in your literals and identifiers won’t work right. If you used the standard preamble just given above, this already happened. If you did, you can do things like this: </p>
<p>use utf8;<br />
my $measure = &#8220;Ångström&#8221;;<br />
my @μsoft = qw(cp852 cp1251 cp1252);<br />
my @ὑπέρμεγας = qw(ὑπέρ μεγας);<br />
my @鯉 = qw(koi8 &#8211; f koi8 &#8211; u koi8 &#8211; r);<br />
my $motto = &#8221;  &#8220;;<br />
#FAMILY, GROWING HEART, DROMEDARY CAMEL</p>
<p> If you forget <tt>&quot;use utf8&quot;</tt>, high bytes will be misunderstood as separate characters, and nothing will work right.</p>
<h3>℞ 4: Characters and their numbers</h3>
<p> The <tt>&quot;ord&quot;</tt> and <tt>&quot;chr&quot;</tt> functions work transparently on all codepoints, not just on <font SIZE="-1">ASCII</font> alone — nor in fact, not even just on Unicode alone. </p>
<pre>
 # ASCII characters
 ord(&quot;A&quot;)
 chr(65)
 # characters from the Basic Multilingual Plane
 ord(&quot;Σ&quot;)
 chr(0x3A3)
 # beyond the BMP
 ord(&quot;&quot;)               # MATHEMATICAL ITALIC SMALL N
 chr(0x1D45B)
 # beyond Unicode! (up to MAXINT)
 ord(&quot;
