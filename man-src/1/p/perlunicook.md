---
title: "perlunicook(1)"
name: "perlunicook"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlunicook/"
description: "perlunicook – cookbookish examples of handling Unicode in Perl"
---

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
 ord(&quot;\x{20_0000}&quot;)
 chr(0x20_0000)
</code></pre>
<h3>℞ 5: Unicode literals by character number</h3>
<p> In an interpolated literal, whether a double-quoted string or a regex, you may specify a character by its number using the <code>&quot;\x{</code>HHHHHH <code>}&quot;</code> escape. </p>
<pre><code> String: &quot;\x{3a3}&quot;
 Regex: /\x{3a3}/
 String: &quot;\x{1d45b}&quot;
 Regex: /\x{1d45b}/
 # even non-BMP ranges in regex work fine
 /[\x{1D434}-\x{1D467}]/
</code></pre>
<h3>℞ 6: Get character name by number</h3>
<pre><code> use charnames ();
 my $name = charnames::viacode(0x03A3);
</code></pre>
<h3>℞ 7: Get character number by name</h3>
<pre><code> use charnames ();
 my $number = charnames::vianame(&quot;GREEK CAPITAL LETTER SIGMA&quot;);
</code></pre>
<h3>℞ 8: Unicode named characters</h3>
<p> Use the <code>&quot;\N{</code>charname <code>}&quot;</code> notation to get the character by that name for use in interpolated literals (double-quoted strings and regexes). In v5.16, there is an implicit </p>
<pre><code> use charnames qw(:full :short);
</code></pre>
<p> But prior to v5.16, you must be explicit about which set of charnames you want. The <code>&quot;:full&quot;</code> names are the official Unicode character name, alias, or sequence, which all share a namespace. </p>
<pre><code> use charnames qw(:full :short latin greek);
 &quot;\N{MATHEMATICAL ITALIC SMALL N}&quot; # :full
 &quot;\N{GREEK CAPITAL LETTER SIGMA}&quot; # :full
</code></pre>
<p> Anything else is a Perl-specific convenience abbreviation. Specify one or more scripts by names if you want short names that are script-specific. </p>
<pre><code> &quot;\N{Greek:Sigma}&quot; # :short
 &quot;\N{ae}&quot; # latin
 &quot;\N{epsilon}&quot; # greek
</code></pre>
<p> The v5.16 release also supports a <code>&quot;:loose&quot;</code> import for loose matching of character names, which works just like loose matching of property names: that is, it disregards case, whitespace, and underscores: </p>
<pre><code> &quot;\N{euro sign}&quot; # :loose (from v5.16)
</code></pre>
<h3>℞ 9: Unicode named sequences</h3>
<p> These look just like character names but return multiple codepoints. Notice the <code>%vx</code> vector-print functionality in <code>&quot;printf&quot;</code>. </p>
<pre><code> use charnames qw(:full);
 my $seq = &quot;\N{LATIN CAPITAL LETTER A WITH MACRON AND GRAVE}&quot;;
 printf &quot;U+%v04X\n&quot;, $seq;
 U+0100.0300
</code></pre>
<h3>℞ 10: Custom named characters</h3>
<p> Use <code>&quot;:alias&quot;</code> to give your own lexically scoped nicknames to existing characters, or even to give unnamed private-use characters useful names. </p>
<pre><code> use charnames &quot;:full&quot;, &quot;:alias&quot; =&gt; {
     ecute =&gt; &quot;LATIN SMALL LETTER E WITH ACUTE&quot;,
     &quot;APPLE LOGO&quot; =&gt; 0xF8FF, # private use character
 };
 &quot;\N{ecute}&quot;
 &quot;\N{APPLE LOGO}&quot;
</code></pre>
<font SIZE="-1"></font><h3>℞ 11: Names of CJK codepoints</h3>
<p> Sinograms like “東京” come back with character names of <code>&quot;CJK UNIFIED IDEOGRAPH-6771&quot;</code> and <code>&quot;CJK UNIFIED IDEOGRAPH-4EAC&quot;</code>, because their “names” vary. The <font SIZE="-1">CPAN</font> <code>&quot;Unicode::Unihan&quot;</code> module has a large database for decoding these (and a whole lot more), provided you know how to understand its output. </p>
<pre><code> # cpan -i Unicode::Unihan
 use Unicode::Unihan;
 my $str = &quot;東京&quot;;
 my $unhan = Unicode::Unihan-&gt;new;
 for my $lang (qw(Mandarin Cantonese Korean JapaneseOn JapaneseKun)) {
     printf &quot;CJK $str in %-12s is &quot;, $lang;
     say $unhan-&gt;$lang($str);
 }
</code></pre>
<p> prints: </p>
<pre><code> CJK 東京 in Mandarin is DONG1JING1
 CJK 東京 in Cantonese is dung1ging1
 CJK 東京 in Korean is TONGKYENG
 CJK 東京 in JapaneseOn is TOUKYOU KEI KIN
 CJK 東京 in JapaneseKun is HIGASHI AZUMAMIYAKO
</code></pre>
<p> If you have a specific romanization scheme in mind, use the specific module: </p>
<pre><code> # cpan -i Lingua::JA::Romanize::Japanese
 use Lingua::JA::Romanize::Japanese;
 my $k2r = Lingua::JA::Romanize::Japanese-&gt;new;
 my $str = &quot;東京&quot;;
 say &quot;Japanese for $str is &quot;, $k2r-&gt;chars($str);
</code></pre>
<p> prints </p>
<pre><code> Japanese for 東京 is toukyou
</code></pre>
<h3>℞ 12: Explicit encode/decode</h3>
<p> On rare occasion, such as a database read, you may be given encoded text you need to decode. </p>
<pre><code>  use Encode qw(encode decode);
  my $chars = decode(&quot;shiftjis&quot;, $bytes, 1);
 # OR
  my $bytes = encode(&quot;MIME-Header-ISO_2022_JP&quot;, $chars, 1);
</code></pre>
<p> For streams all in the same encoding, don&#8217;t use encode/decode; instead set the file encoding when you open the file or immediately after with <code>&quot;binmode&quot;</code> as described later below.  </p>
<h3>℞ 13: Decode program arguments as utf8</h3>
<pre><code>     $ perl -CA ...
 or
     $ export PERL_UNICODE=A
 or
    use Encode qw(decode);
    @ARGV = map { decode('UTF-8', $_, 1) } @ARGV;
</code></pre>
<h3>℞ 14: Decode program arguments as locale encoding</h3>
<pre><code>    # cpan -i Encode::Locale
    use Encode qw(locale);
    use Encode::Locale;
    # use &quot;locale&quot; as an arg to encode/decode
    @ARGV = map { decode(locale =&gt; $_, 1) } @ARGV;
</code></pre>
<font SIZE="-1"></font><h3>℞ 15: Declare STD{ IN,OUT,ERR } to be utf8</h3>
<p> Use a command-line option, an environment variable, or else call <code>&quot;binmode&quot;</code> explicitly: </p>
<pre><code>     $ perl -CS ...
 or
     $ export PERL_UNICODE=S
 or
     use open qw(:std :encoding(UTF-8));
 or
     binmode(STDIN, &quot;:encoding(UTF-8)&quot;);
     binmode(STDOUT, &quot;:utf8&quot;);
     binmode(STDERR, &quot;:utf8&quot;);
</code></pre>
<font SIZE="-1"></font><h3>℞ 16: Declare STD{ IN,OUT,ERR } to be in locale encoding</h3>
<pre><code>    # cpan -i Encode::Locale
    use Encode;
    use Encode::Locale;
    # or as a stream for binmode or open
    binmode STDIN, &quot;:encoding(console_in)&quot; if -t STDIN;
    binmode STDOUT, &quot;:encoding(console_out)&quot; if -t STDOUT;
    binmode STDERR, &quot;:encoding(console_out)&quot; if -t STDERR;
</code></pre>
<h3>℞ 17: Make file I/O default to utf8</h3>
<p> Files opened without an encoding argument will be in <font SIZE="-1">UTF-8:</font> </p>
<pre><code>     $ perl -CD ...
 or
     $ export PERL_UNICODE=D
 or
     use open qw(:encoding(UTF-8));
</code></pre>
<h3>℞ 18: Make all I/O and args default to utf8</h3>
<pre><code>     $ perl -CSDA ...
 or
     $ export PERL_UNICODE=SDA
 or
     use open qw(:std :encoding(UTF-8));
     use Encode qw(decode);
     @ARGV = map { decode('UTF-8', $_, 1) } @ARGV;
</code></pre>
<h3>℞ 19: Open file with specific encoding</h3>
<p> Specify stream encoding. This is the normal way to deal with encoded text, not by calling low-level functions. </p>
<pre><code> # input file
     open(my $in_file, &quot;&lt; :encoding(UTF-16)&quot;, &quot;wintext&quot;);
 OR
     open(my $in_file, &quot;&lt;&quot;, &quot;wintext&quot;);
     binmode($in_file, &quot;:encoding(UTF-16)&quot;);
 THEN
     my $line = &lt;$in_file&gt;;
 # output file
     open($out_file, &quot;&gt; :encoding(cp1252)&quot;, &quot;wintext&quot;);
 OR
     open(my $out_file, &quot;&gt;&quot;, &quot;wintext&quot;);
     binmode($out_file, &quot;:encoding(cp1252)&quot;);
 THEN
     print $out_file &quot;some text\n&quot;;
</code></pre>
<p> More layers than just the encoding can be specified here. For example, the incantation <code>&quot;:raw :encoding(UTF-16LE) :crlf&quot;</code> includes implicit <font SIZE="-1">CRLF</font> handling.  </p>
<h3>℞ 20: Unicode casing</h3>
<p> Unicode casing is very different from <font SIZE="-1">ASCII</font> casing. </p>
<pre><code> uc(&quot;henry ⅷ&quot;) # &quot;HENRY Ⅷ&quot;
 uc(&quot;tschüß&quot;) # &quot;TSCHÜSS&quot; notice ß =&gt; SS
 # both are true:
 &quot;tschüß&quot; =~ /TSCHÜSS/i # notice ß =&gt; SS
 &quot;Σίσυφος&quot; =~ /ΣΊΣΥΦΟΣ/i # notice Σ,σ,ς sameness
</code></pre>
<h3>℞ 21: Unicode case-insensitive comparisons</h3>
<p> Also available in the <font SIZE="-1">CPAN</font> Unicode::CaseFold module, the new <code>&quot;fc&quot;</code> “foldcase” function from v5.16 grants access to the same Unicode casefolding as the <code>&quot;/i&quot;</code> pattern modifier has always used: </p>
<pre><code> use feature &quot;fc&quot;; # fc() function is from v5.16
 # sort case-insensitively
 my @sorted = sort { fc($a) cmp fc($b) } @list;
 # both are true:
 fc(&quot;tschüß&quot;) eq fc(&quot;TSCHÜSS&quot;)
 fc(&quot;Σίσυφος&quot;) eq fc(&quot;ΣΊΣΥΦΟΣ&quot;)
</code></pre>
<h3>℞ 22: Match Unicode linebreak sequence in regex</h3>
<p> A Unicode linebreak matches the two-character <font SIZE="-1">CRLF</font> grapheme or any of seven vertical whitespace characters. Good for dealing with textfiles coming from different operating systems. </p>
<pre><code> \R
 s/\R/\n/g; # normalize all linebreaks to \n
</code></pre>
<h3>℞ 23: Get character category</h3>
<p> Find the general category of a numeric codepoint. </p>
<pre><code> use Unicode::UCD qw(charinfo);
 my $cat = charinfo(0x3A3)-&gt;{category}; # &quot;Lu&quot;
</code></pre>
<h3>℞ 24: Disabling Unicode-awareness in builtin charclasses</h3>
<p> Disable <code>&quot;\w&quot;</code>, <code>&quot;\b&quot;</code>, <code>&quot;\s&quot;</code>, <code>&quot;\d&quot;</code>, and the <font SIZE="-1">POSIX</font> classes from working correctly on Unicode either in this scope, or in just one regex. </p>
<pre><code> use v5.14;
 use re &quot;/a&quot;;
 # OR
 my($num) = $str =~ /(\d+)/a;
</code></pre>
<p> Or use specific un-Unicode properties, like <code>&quot;\p{ahex}&quot;</code> and <code>&quot;\p{POSIX_Digit&quot;</code>}. Properties still work normally no matter what charset modifiers (<code>&quot;/d /u /l /a /aa&quot;</code>) should be effect.  </p>
<h3>℞ 25: Match Unicode properties in regex with \p, \P</h3>
<p> These all match a single codepoint with the given property. Use <code>&quot;\P&quot;</code> in place of <code>&quot;\p&quot;</code> to match one codepoint lacking that property. </p>
<pre><code> \pL, \pN, \pS, \pP, \pM, \pZ, \pC
 \p{Sk}, \p{Ps}, \p{Lt}
 \p{alpha}, \p{upper}, \p{lower}
 \p{Latin}, \p{Greek}
 \p{script_extensions=Latin}, \p{scx=Greek}
 \p{East_Asian_Width=Wide}, \p{EA=W}
 \p{Line_Break=Hyphen}, \p{LB=HY}
 \p{Numeric_Value=4}, \p{NV=4}
</code></pre>
<h3>℞ 26: Custom character properties</h3>
<p> Define at compile-time your own custom character properties for use in regexes. </p>
<pre><code> # using private-use characters
 sub In_Tengwar { &quot;E000\tE07F\n&quot; }
 if (/\p{In_Tengwar}/) { ... }
 # blending existing properties
 sub Is_GraecoRoman_Title {&lt;&lt;'END_OF_SET'}
 +utf8::IsLatin
 +utf8::IsGreek
 &amp;utf8::IsTitle
 END_OF_SET
 if (/\p{Is_GraecoRoman_Title}/ { ... }
</code></pre>
<h3>℞ 27: Unicode normalization</h3>
<p> Typically render into <font SIZE="-1">NFD</font> on input and <font SIZE="-1">NFC</font> on output. Using <font SIZE="-1">NFKC</font> or <font SIZE="-1">NFKD</font> functions improves recall on searches, assuming you&#8217;ve already done to the same text to be searched. Note that this is about much more than just pre- combined compatibility glyphs; it also reorders marks according to their canonical combining classes and weeds out singletons. </p>
<pre><code> use Unicode::Normalize;
 my $nfd = NFD($orig);
 my $nfc = NFC($orig);
 my $nfkd = NFKD($orig);
 my $nfkc = NFKC($orig);
</code></pre>
<h3>℞ 28: Convert non-ASCII Unicode numerics</h3>
<p> Unless you’ve used <code>&quot;/a&quot;</code> or <code>&quot;/aa&quot;</code>, <code>&quot;\d&quot;</code> matches more than <font SIZE="-1">ASCII</font> digits only, but Perl’s implicit string-to-number conversion does not current recognize these. Here’s how to convert such strings manually. </p>
<pre><code> use v5.14; # needed for num() function
 use Unicode::UCD qw(num);
 my $str = &quot;got Ⅻ and ४५६७ and ⅞ and here&quot;;
 my @nums = ();
 while ($str =~ /(\d+|\N)/g) { # not just ASCII!
    push @nums, num($1);
 }
 say &quot;@nums&quot;; # 12 4567 0.875
 use charnames qw(:full);
 my $nv = num(&quot;\N{RUMI DIGIT ONE}\N{RUMI DIGIT TWO}&quot;);
</code></pre>
<h3>℞ 29: Match Unicode grapheme cluster in regex</h3>
<p> Programmer-visible “characters” are codepoints matched by <code>&quot;/./s&quot;</code>, but user-visible “characters” are graphemes matched by <code>&quot;/\X/&quot;</code>. </p>
<pre><code> # Find vowel *plus* any combining diacritics,underlining,etc.
 my $nfd = NFD($orig);
 $nfd =~ / (?=[aeiou]) \X /xi
</code></pre>
<h3>℞ 30: Extract by grapheme instead of by codepoint (regex)</h3>
<pre><code> # match and grab five first graphemes
 my($first_five) = $str =~ /^ ( \X{5} ) /x;
</code></pre>
<h3>℞ 31: Extract by grapheme instead of by codepoint (substr)</h3>
<pre><code> # cpan -i Unicode::GCString
 use Unicode::GCString;
 my $gcs = Unicode::GCString-&gt;new($str);
 my $first_five = $gcs-&gt;substr(0, 5);
</code></pre>
<h3>℞ 32: Reverse string by grapheme</h3>
<p> Reversing by codepoint messes up diacritics, mistakenly converting <code>&quot;crème brûlée&quot;</code> into <code>&quot;éel̂urb em̀erc&quot;</code> instead of into <code>&quot;eélûrb emèrc&quot;</code>; so reverse by grapheme instead. Both these approaches work right no matter what normalization the string is in: </p>
<pre><code> $str = join(&quot;&quot;, reverse $str =~ /\X/g);
 # OR: cpan -i Unicode::GCString
 use Unicode::GCString;
 $str = reverse Unicode::GCString-&gt;new($str);
</code></pre>
<h3>℞ 33: String length in graphemes</h3>
<p> The string <code>&quot;brûlée&quot;</code> has six graphemes but up to eight codepoints. This counts by grapheme, not by codepoint: </p>
<pre><code> my $str = &quot;brûlée&quot;;
 my $count = 0;
 while ($str =~ /\X/g) { $count++ }
  # OR: cpan -i Unicode::GCString
 use Unicode::GCString;
 my $gcs = Unicode::GCString-&gt;new($str);
 my $count = $gcs-&gt;length;
</code></pre>
<h3>℞ 34: Unicode column-width for printing</h3>
<p> Perl’s <code>&quot;printf&quot;</code>, <code>&quot;sprintf&quot;</code>, and <code>&quot;format&quot;</code> think all codepoints take up 1 print column, but many take 0 or 2. Here to show that normalization makes no difference, we print out both forms: </p>
<pre><code> use Unicode::GCString;
 use Unicode::Normalize;
 my @words = qw/crème brûlée/;
 @words = map { NFC($_), NFD($_) } @words;
 for my $str (@words) {
     my $gcs = Unicode::GCString-&gt;new($str);
     my $cols = $gcs-&gt;columns;
     my $pad = &quot; &quot; x (10 - $cols);
     say str, $pad, &quot; |&quot;;
 }
</code></pre>
<p> generates this to show that it pads correctly no matter the normalization: </p>
<pre><code> crème |
 crème |
 brûlée |
 brûlée |
</code></pre>
<h3>℞ 35: Unicode collation</h3>
<p> Text sorted by numeric codepoint follows no reasonable alphabetic order; use the <font SIZE="-1">UCA</font> for sorting text. </p>
<pre><code> use Unicode::Collate;
 my $col = Unicode::Collate-&gt;new();
 my @list = $col-&gt;sort(@old_list);
</code></pre>
<p> See the <i>ucsort</i> program from the Unicode::Tussle <font SIZE="-1">CPAN</font> module for a convenient command-line interface to this module.  </p>
<i></i><h3>℞ 36: Case- and accent-insensitive Unicode sort</h3>
<p> Specify a collation strength of level 1 to ignore case and diacritics, only looking at the basic character. </p>
<pre><code> use Unicode::Collate;
 my $col = Unicode::Collate-&gt;new(level =&gt; 1);
 my @list = $col-&gt;sort(@old_list);
</code></pre>
<h3>℞ 37: Unicode locale collation</h3>
<p> Some locales have special sorting rules. </p>
<pre><code> # either use v5.12, OR: cpan -i Unicode::Collate::Locale
 use Unicode::Collate::Locale;
 my $col = Unicode::Collate::Locale-&gt;new(locale =&gt; &quot;de__phonebook&quot;);
 my @list = $col-&gt;sort(@old_list);
</code></pre>
<p> The <i>ucsort</i> program mentioned above accepts a <code>&quot;--locale&quot;</code> parameter.  </p>
<h3>℞ 38: Making cmp work on text instead of codepoints</h3>
<p> Instead of this: </p>
<pre><code> @srecs = sort {
     $b-&gt;{AGE} &lt;=&gt; $a-&gt;{AGE}
                 ||
     $a-&gt;{NAME} cmp $b-&gt;{NAME}
 } @recs;
</code></pre>
<p> Use this: </p>
<pre><code> my $coll = Unicode::Collate-&gt;new();
 for my $rec (@recs) {
     $rec-&gt;{NAME_key} = $coll-&gt;getSortKey( $rec-&gt;{NAME} );
 }
 @srecs = sort {
     $b-&gt;{AGE} &lt;=&gt; $a-&gt;{AGE}
                     ||
     $a-&gt;{NAME_key} cmp $b-&gt;{NAME_key}
 } @recs;
</code></pre>
<i></i><h3>℞ 39: Case- and accent-insensitive comparisons</h3>
<p> Use a collator object to compare Unicode text by character instead of by codepoint. </p>
<pre><code> use Unicode::Collate;
 my $es = Unicode::Collate-&gt;new(
     level =&gt; 1,
     normalization =&gt; undef
 );
  # now both are true:
 $es-&gt;eq(&quot;García&quot;, &quot;GARCIA&quot; );
 $es-&gt;eq(&quot;Márquez&quot;, &quot;MARQUEZ&quot;);
</code></pre>
<i></i><h3>℞ 40: Case- and accent-insensitive locale comparisons</h3>
<p> Same, but in a specific locale. </p>
<pre><code> my $de = Unicode::Collate::Locale-&gt;new(
            locale =&gt; &quot;de__phonebook&quot;,
          );
 # now this is true:
 $de-&gt;eq(&quot;tschüß&quot;, &quot;TSCHUESS&quot;); # notice ü =&gt; UE, ß =&gt; SS
</code></pre>
<h3>℞ 41: Unicode linebreaking</h3>
<p> Break up text into lines according to Unicode rules. </p>
<pre><code> # cpan -i Unicode::LineBreak
 use Unicode::LineBreak;
 use charnames qw(:full);
 my $para = &quot;This is a super\N{HYPHEN}long string. &quot; x 20;
 my $fmt = Unicode::LineBreak-&gt;new;
 print $fmt-&gt;break($para), &quot;\n&quot;;
</code></pre>
<font SIZE="-1"></font><h3>℞ 42: Unicode text in DBM hashes, the tedious way</h3>
<p> Using a regular Perl string as a key or value for a <font SIZE="-1">DBM</font> hash will trigger a wide character exception if any codepoints won’t fit into a byte. Here’s how to manually manage the translation: </p>
<pre><code>    use DB_File;
    use Encode qw(encode decode);
    tie %dbhash, &quot;DB_File&quot;, &quot;pathname&quot;;
 # STORE
    # assume $uni_key and $uni_value are abstract Unicode strings
    my $enc_key = encode(&quot;UTF-8&quot;, $uni_key, 1);
    my $enc_value = encode(&quot;UTF-8&quot;, $uni_value, 1);
    $dbhash{$enc_key} = $enc_value;
 # FETCH
    # assume $uni_key holds a normal Perl string (abstract Unicode)
    my $enc_key = encode(&quot;UTF-8&quot;, $uni_key, 1);
    my $enc_value = $dbhash{$enc_key};
    my $uni_value = decode(&quot;UTF-8&quot;, $enc_value, 1);
</code></pre>
<font SIZE="-1"></font><h3>℞ 43: Unicode text in DBM hashes, the easy way</h3>
<p> Here’s how to implicitly manage the translation; all encoding and decoding is done automatically, just as with streams that have a particular encoding attached to them: </p>
<pre><code>    use DB_File;
    use DBM_Filter;
    my $dbobj = tie %dbhash, &quot;DB_File&quot;, &quot;pathname&quot;;
    $dbobj-&gt;Filter_Value(&quot;utf8&quot;); # this is the magic bit
 # STORE
    # assume $uni_key and $uni_value are abstract Unicode strings
    $dbhash{$uni_key} = $uni_value;
  # FETCH
    # $uni_key holds a normal Perl string (abstract Unicode)
    my $uni_value = $dbhash{$uni_key};
</code></pre>
<font SIZE="-1"></font><h3>℞ 44: PROGRAM: Demo of Unicode collation and printing</h3>
<p> Here’s a full program showing how to make use of locale-sensitive sorting, Unicode casing, and managing print widths when some of the characters take up zero or two columns, not just one column each time. When run, the following program produces this nicely aligned output: </p>
<pre><code>    Crème Brûlée....... €2.00
    Éclair............. €1.60
    Fideuà............. €4.20
    Hamburger.......... €6.00
    Jamón Serrano...... €4.45
    Linguiça........... €7.00
    Pâté............... €4.15
    Pears.............. €2.00
    Pêches............. €2.25
    Smørbrød........... €5.75
    Spätzle............ €5.50
    Xoriço............. €3.00
    Γύρος.............. €6.50
    막걸리............. €4.00
    おもち............. €2.65
    お好み焼き......... €8.00
    シュークリーム..... €1.85
    寿司............... €9.99
    包子............... €7.50
</code></pre>
<p> Here&#8217;s that program; tested on v5.14. </p>
<pre><code> #!/usr/bin/env perl
 # umenu - demo sorting and printing of Unicode food
 #
 # (obligatory and increasingly long preamble)
 #
 use utf8;
 use v5.14; # for locale sorting
 use strict;
 use warnings;
 use warnings qw(FATAL utf8); # fatalize encoding faults
 use open qw(:std :encoding(UTF-8)); # undeclared streams in UTF-8
 use charnames qw(:full :short); # unneeded in v5.16
 # std modules
 use Unicode::Normalize; # std perl distro as of v5.8
 use List::Util qw(max); # std perl distro as of v5.10
 use Unicode::Collate::Locale; # std perl distro as of v5.14
 # cpan modules
 use Unicode::GCString; # from CPAN
 # forward defs
 sub pad($$$);
 sub colwidth(_);
 sub entitle(_);
 my %price = (
     &quot;γύρος&quot; =&gt; 6.50, # gyros
     &quot;pears&quot; =&gt; 2.00, # like um, pears
     &quot;linguiça&quot; =&gt; 7.00, # spicy sausage, Portuguese
     &quot;xoriço&quot; =&gt; 3.00, # chorizo sausage, Catalan
     &quot;hamburger&quot; =&gt; 6.00, # burgermeister meisterburger
     &quot;éclair&quot; =&gt; 1.60, # dessert, French
     &quot;smørbrød&quot; =&gt; 5.75, # sandwiches, Norwegian
     &quot;spätzle&quot; =&gt; 5.50, # Bayerisch noodles, little sparrows
     &quot;包子&quot; =&gt; 7.50, # bao1 zi5, steamed pork buns, Mandarin
     &quot;jamón serrano&quot; =&gt; 4.45, # country ham, Spanish
     &quot;pêches&quot; =&gt; 2.25, # peaches, French
     &quot;シュークリーム&quot; =&gt; 1.85, # cream-filled pastry like eclair
     &quot;막걸리&quot; =&gt; 4.00, # makgeolli, Korean rice wine
     &quot;寿司&quot; =&gt; 9.99, # sushi, Japanese
     &quot;おもち&quot; =&gt; 2.65, # omochi, rice cakes, Japanese
     &quot;crème brûlée&quot; =&gt; 2.00, # crema catalana
     &quot;fideuà&quot; =&gt; 4.20, # more noodles, Valencian
                                  # (Catalan=fideuada)
     &quot;pâté&quot; =&gt; 4.15, # gooseliver paste, French
     &quot;お好み焼き&quot; =&gt; 8.00, # okonomiyaki, Japanese
 );
 my $width = 5 + max map { colwidth } keys %price;
 # So the Asian stuff comes out in an order that someone
 # who reads those scripts won't freak out over; the
 # CJK stuff will be in JIS X 0208 order that way.
 my $coll = Unicode::Collate::Locale-&gt;new(locale =&gt; &quot;ja&quot;);
 for my $item ($coll-&gt;sort(keys %price)) {
     print pad(entitle($item), $width, &quot;.&quot;);
     printf &quot; €%.2f\n&quot;, $price{$item};
 }
 sub pad($$$) {
     my($str, $width, $padchar) = @_;
     return $str . ($padchar x ($width - colwidth($str)));
 }
 sub colwidth(_) {
     my($str) = @_;
     return Unicode::GCString-&gt;new($str)-&gt;columns;
 }
 sub entitle(_) {
     my($str) = @_;
     $str =~ s{ (?=\pL)(\S) (\S*) }
              { ucfirst($1) . lc($2) }xge;
     return $str;
 }
</code></pre>
<h2>SEE ALSO</h2>
<p> See these manpages, some of which are <font SIZE="-1">CPAN</font> modules: perlunicode, perluniprops, perlre, perlrecharclass, perluniintro, perlunitut, perlunifaq, PerlIO, DB_File, DBM_Filter, DBM_Filter::utf8, Encode, Encode::Locale, Unicode::UCD, Unicode::Normalize, Unicode::GCString, Unicode::LineBreak, Unicode::Collate, Unicode::Collate::Locale, Unicode::Unihan, Unicode::CaseFold, Unicode::Tussle, Lingua::JA::Romanize::Japanese, Lingua::ZH::Romanize::Pinyin, Lingua::KO::Romanize::Hangul. </p>
<p> The Unicode::Tussle <font SIZE="-1">CPAN</font> module includes many programs to help with working with Unicode, including these programs to fully or partly replace standard utilities: <i>tcgrep</i> instead of <i>egrep</i>, <i>uniquote</i> instead of <i>cat -v</i> or <i>hexdump</i>, <i>uniwc</i> instead of <i>wc</i>, <i>unilook</i> instead of <i>look</i>, <i>unifmt</i> instead of <i>fmt</i>, and <i>ucsort</i> instead of <i>sort</i>. For exploring Unicode character names and character properties, see its <i>uniprops</i>, <i>unichars</i>, and <i>uninames</i> programs. It also supplies these programs, all of which are general filters that do Unicode-y things: <i>unititle</i> and <i>unicaps</i>; <i>uniwide</i> and <i>uninarrow</i>; <i>unisupers</i> and <i>unisubs</i>; <i>nfd</i>, <i>nfc</i>, <i>nfkd</i>, and <i>nfkc</i>; and <i>uc</i>, <i>lc</i>, and <i>tc</i>. </p>
<p> Finally, see the published Unicode Standard (page numbers are from version 6.0.0), including these specific annexes and technical reports: </p>
<dl>
<dt>§3.13 Default Case Algorithms, page 113; §4.2 Case, pages 120–122; Case Mappings, page 166–172, especially Caseless Matching starting on page 170.</dt>
<dd>  </dd>
<dt><font SIZE="-1">UAX</font> #44: Unicode Character Database</dt>
<dd>  </dd>
<dt><font SIZE="-1">UTS</font> #18: Unicode Regular Expressions</dt>
<dd>  </dd>
<dt><font SIZE="-1">UAX</font> #15: Unicode Normalization Forms</dt>
<dd>  </dd>
<dt><font SIZE="-1">UTS</font> #10: Unicode Collation Algorithm</dt>
<dd>  </dd>
<dt><font SIZE="-1">UAX</font> #29: Unicode Text Segmentation</dt>
<dd>  </dd>
<dt><font SIZE="-1">UAX</font> #14: Unicode Line Breaking Algorithm</dt>
<dd>  </dd>
<dt><font SIZE="-1">UAX</font> #11: East Asian Width</dt>
<dd>  </dd></dl>
<h2>AUTHOR</h2>
<p> Tom Christiansen &lt;tchrist [at] perl.com&gt; wrote this, with occasional kibbitzing from Larry Wall and Jeffrey Friedl in the background.  </p>
<h2>COPYRIGHT AND LICENCE</h2>
<p> Copyright © 2012 Tom Christiansen. </p>
<p> This program is free software; you may redistribute it and/or modify it under the same terms as Perl itself. </p>
<p> Most of these examples taken from the current edition of the “Camel Book”; that is, from the 4ᵗʰ Edition of <i>Programming Perl</i>, Copyright © 2012 Tom Christiansen &lt;et al.&gt;, 2012-02-13 by O’Reilly Media. The code itself is freely redistributable, and you are encouraged to transplant, fold, spindle, and mutilate any of the examples in this manpage however you please for inclusion into your own programs without any encumbrance whatsoever. Acknowledgement via code comment is polite but not required.  </p>
<h2>REVISION HISTORY</h2>
<p> v1.0.0 – first public release, 2012-02-27 </p>
