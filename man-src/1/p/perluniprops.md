---
title: "perluniprops(1)"
name: "perluniprops"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perluniprops/"
description: "perluniprops – Index of Unicode Version 12.1.0 character properties in Perl"
---

<h2 class="name">NAME</h2>
<p> perluniprops &#8211; Index of Unicode Version 12.1.0 character properties in Perl </p>
<h2>DESCRIPTION</h2>
<p> This document provides information about the portion of the Unicode database that deals with character properties, that is the portion that is defined on single code points. (&#8220;Other information in the Unicode data base&#8221; below briefly mentions other data that Unicode provides.) </p>
<p> Perl can provide access to all non-provisional Unicode character properties, though not all are enabled by default. The omitted ones are the Unihan properties (accessible via the <font SIZE="-1">CPAN</font> module Unicode::Unihan) and certain deprecated or Unicode-internal properties. (An installation may choose to recompile Perl&#8217;s tables to change this. See &#8220;Unicode character properties that are <font SIZE="-1">NOT</font> accepted by Perl&#8221;.) </p>
<p> For most purposes, access to Unicode properties from the Perl core is through regular expression matches, as described in the next section. For some special purposes, and to access the properties that are not suitable for regular expression matching, all the Unicode character properties that Perl handles are accessible via the standard Unicode::UCD module, as described in the section &#8220;Properties accessible through Unicode::UCD&#8221;. </p>
<p> Perl also provides some additional extensions and short-cut synonyms for Unicode properties. </p>
<p> This document merely lists all available properties and does not attempt to explain what each property really means. There is a brief description of each Perl extension; see &#8220;Other Properties&#8221; in perlunicode for more information on these. There is some detail about Blocks, Scripts, General_Category, and Bidi_Class in perlunicode, but to find out about the intricacies of the official Unicode properties, refer to the Unicode standard. A good starting place is &lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr44/">http://www.unicode.org/reports/tr44/</a>&gt;. </p>
<p> Note that you can define your own properties; see &#8220;User-Defined Character Properties&#8221; in perlunicode.</p>
<h2>Properties accessible through \p{} and \P{}</h2>
<p> The Perl regular expression <tt>&quot;\p{}&quot;</tt> and <tt>&quot;\P{}&quot;</tt> constructs give access to most of the Unicode character properties. The table below shows all these constructs, both single and compound forms. </p>
<p> <code>Compound forms</code> consist of two components, separated by an equals sign or a colon. The first component is the property name, and the second component is the particular value of the property to match against, for example, <tt>&quot;\p{Script_Extensions: Greek}&quot;</tt> and <tt>&quot;\p{Script_Extensions=Greek}&quot;</tt> both mean to match characters whose Script_Extensions property value is Greek. (<tt>&quot;Script_Extensions&quot;</tt> is an improved version of the <tt>&quot;Script&quot;</tt> property.) </p>
<p> <code>Single forms</code>, like <tt>&quot;\p{Greek}&quot;</tt>, are mostly Perl-defined shortcuts for their equivalent compound forms. The table shows these equivalences. (In our example, <tt>&quot;\p{Greek}&quot;</tt> is a just a shortcut for <tt>&quot;\p{Script_Extensions=Greek}&quot;</tt>). There are also a few Perl-defined single forms that are not shortcuts for a compound form. One such is <tt>&quot;\p{Word}&quot;</tt>. These are also listed in the table. </p>
<p> In parsing these constructs, Perl always ignores Upper/lower case differences everywhere within the {braces}. Thus <tt>&quot;\p{Greek}&quot;</tt> means the same thing as <tt>&quot;\p{greek}&quot;</tt>. But note that changing the case of the <tt>&quot;p&quot;</tt> or <tt>&quot;P&quot;</tt> before the left brace completely changes the meaning of the construct, from &#8220;match&#8221; (for <tt>&quot;\p{}&quot;</tt>) to &#8220;doesn&#8217;t match&#8221; (for <tt>&quot;\P{}&quot;</tt>). Casing in this document is for improved legibility. </p>
<p> Also, white space, hyphens, and underscores are normally ignored everywhere between the {braces}, and hence can be freely added or removed even if the <tt>&quot;/x&quot;</tt> modifier hasn&#8217;t been specified on the regular expression. But in the table below a &#8216;<code>T</code>&#8216; at the beginning of an entry means that tighter (stricter) rules are used for that entry:</p>
<dl>
<dt>
<dd>
<dl>
<dt>Single form (&quot;\p{name}&quot;) tighter rules:</p>
<dd> White space, hyphens, and underscores <font SIZE="-1">ARE</font> significant except for:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> white space adjacent to a non-word character</p>
<dt>&bull;</p>
<dd> underscores separating digits in numbers</dl>
</dl>
<dl>
<dt>
<dd>
<p> That means, for example, that you can freely add or remove white space adjacent to (but within) the braces without affecting the meaning.</dl>
<dt>Compound form (&quot;\p{name=value}&quot; or &quot;\p{name:value}&quot;) tighter rules:</p>
<dd> The tighter rules given above for the single form apply to everything to the right of the colon or equals; the looser rules still apply to everything to the left. </p>
<p> That means, for example, that you can freely add or remove white space adjacent to (but within) the braces and the colon or equal sign.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<p> Some properties are considered obsolete by Unicode, but still available. There are several varieties of obsolescence:</p>
<dl>
<dt>
<dd>
<dl>
<dt>Stabilized</p>
<dd> A property may be stabilized. Such a determination does not indicate that the property should or should not be used; instead it is a declaration that the property will not be maintained nor extended for newly encoded characters. Such properties are marked with an &#8216;<code>S</code>&#8216; in the table.</p>
<dt>Deprecated</p>
<dd> A property may be deprecated, perhaps because its original intent has been replaced by another property, or because its specification was somehow defective. This means that its use is strongly discouraged, so much so that a warning will be issued if used, unless the regular expression is in the scope of a <tt>&quot;no warnings 'deprecated'&quot;</tt> statement. A &#8216;<code>D</code>&#8216; flags each such entry in the table, and the entry there for the longest, most descriptive version of the property will give the reason it is deprecated, and perhaps advice. Perl may issue such a warning, even for properties that aren&#8217;t officially deprecated by Unicode, when there used to be characters or code points that were matched by them, but no longer. This is to warn you that your program may not work like it did on earlier Unicode releases. </p>
<p> A deprecated property may be made unavailable in a future Perl version, so it is best to move away from them. </p>
<p> A deprecated property may also be stabilized, but this fact is not shown.</p>
<dt>Obsolete</p>
<dd> Properties marked with an &#8216;<code>O</code>&#8216; in the table are considered (plain) obsolete. Generally this designation is given to properties that Unicode once used for internal purposes (but not any longer).</p>
<dt>Discouraged</p>
<dd> This is not actually a Unicode-specified obsolescence, but applies to certain Perl extensions that are present for backwards compatibility, but are discouraged from being used. These are not obsolete, but their meanings are not stable. Future Unicode versions could force any of these extensions to be removed without warning, replaced by another property with the same name that means something different. An &#8216;<code>X</code>&#8216; flags each such entry in the table. Use the equivalent shown instead. </p>
<p> In particular, matches in the Block property have single forms defined by Perl that begin with <tt>&quot;In_&quot;</tt>, <tt>&quot;&quot;Is_&quot;</tt>, or even with no prefix at all, Like all <font SIZE="-1"><code>DISCOURAGED</code></font> forms, these are not stable. For example, <tt>&quot;\p{Block=Deseret}&quot;</tt> can currently be written as <tt>&quot;\p{In_Deseret}&quot;</tt>, <tt>&quot;\p{Is_Deseret}&quot;</tt>, or <tt>&quot;\p{Deseret}&quot;</tt>. But, a new Unicode version may come along that would force Perl to change the meaning of one or more of these, and your program would no longer be correct. Currently there are no such conflicts with the form that begins <tt>&quot;In_&quot;</tt>, but there are many with the other two shortcuts, and Unicode continues to define new properties that begin with <tt>&quot;In&quot;</tt>, so it&#8217;s quite possible that a conflict will occur in the future. The compound form is guaranteed to not become obsolete, and its meaning is clearer anyway. See &#8220;Blocks&#8221; in perlunicode for more information about this.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<p> The table below has two columns. The left column contains the <tt>&quot;\p{}&quot;</tt> constructs to look up, possibly preceded by the flags mentioned above; and the right column contains information about them, like a description, or synonyms. The table shows both the single and compound forms for each property that has them. If the left column is a short name for a property, the right column will give its longer, more descriptive name; and if the left column is the longest name, the right column will show any equivalent shortest name, in both single and compound forms if applicable. </p>
<p> If braces are not needed to specify a property (e.g., <tt>&quot;\pL&quot;</tt>), the left column contains both forms, with and without braces. </p>
<p> The right column will also caution you if a property means something different than what might normally be expected. </p>
<p> All single forms are Perl extensions; a few compound forms are as well, and are noted as such. </p>
<p> Numbers in (parentheses) indicate the total number of Unicode code points matched by the property. For the entries that give the longest, most descriptive version of the property, the count is followed by a list of some of the code points matched by it. The list includes all the matched characters in the 0-255 range, enclosed in the familiar [brackets] the same as a regular expression bracketed character class. Following that, the next few higher matching ranges are also given. To avoid visual ambiguity, the <font SIZE="-1">SPACE</font> character is represented as <tt>&quot; &quot;</tt>. </p>
<p> For emphasis, those properties that match no code points at all are listed as well in a separate section following the table. </p>
<p> Most properties match the same code points regardless of whether <tt>&quot;/i&quot;</tt> case-insensitive matching is specified or not. But a few properties are affected. These are shown with the notation <tt>&quot;(/i= </tt>other_property<tt>)&quot;</tt> in the second column. Under case-insensitive matching they match the same code pode points as the property <i>other_property</i>. </p>
<p> There is no description given for most non-Perl defined properties (See &lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr44/">http://www.unicode.org/reports/tr44/</a>&gt; for that). </p>
<p> For compactness, &#8216;<code>*</code>&#8216; is used as a wildcard instead of showing all possible combinations. For example, entries like: </p>
<pre><code>
\p
{
Gc:
    *
}
\p
{
General_Category:
    *
}
</code></pre>
<p> mean that &#8216;Gc&#8217; is a synonym for &#8216;General_Category&#8217;, and anything that is valid for the latter is also valid for the former. Similarly, </p>
<p>\p<br />
{<br />
    Is_ *<br />
}<br />
\p<br />
{<br />
    *<br />
}</p>
<p> means that if and only if, for example, <tt>&quot;\p{Foo}&quot;</tt> exists, then <tt>&quot;\p{Is_Foo}&quot;</tt> and <tt>&quot;\p{IsFoo}&quot;</tt> are also valid and all mean the same thing. And similarly, <tt>&quot;\p{Foo=Bar}&quot;</tt> means the same as <tt>&quot;\p{Is_Foo=Bar}&quot;</tt> and <tt>&quot;\p{IsFoo=Bar}&quot;</tt>. &#8220;*&#8221; here is restricted to something not beginning with an underscore. </p>
<p> Also, in binary properties, &#8216;Yes&#8217;, &#8216;T&#8217;, and &#8216;True&#8217; are all synonyms for &#8216;Y&#8217;. And &#8216;No&#8217;, &#8216;F&#8217;, and &#8216;False&#8217; are all synonyms for &#8216;N&#8217;. The table shows &#8216;Y*&#8217; and &#8216;N*&#8217; to indicate this, and doesn&#8217;t have separate entries for the other possibilities. Note that not all properties which have values &#8216;Yes&#8217; and &#8216;No&#8217; are binary, and they have all their values spelled out without using this wild card, and a <tt>&quot;NOT&quot;</tt> clause in their description that highlights their not being binary. These also require the compound form to match them, whereas true binary properties have both single and compound forms available. </p>
<p> Note that all non-essential underscores are removed in the display of the short names below. </p>
<p> <code>Legend summary:</code></p>
<dl>
<dt><code>*</code> is a wild-card</p>
<dd>
<dt><code>(\d+)</code> in the info column gives the number of Unicode code points matched by this property.</p>
<dd>
<dt><code>D</code> means this is deprecated.</p>
<dd>
<dt><code>O</code> means this is obsolete.</p>
<dd>
<dt><code>S</code> means this is stabilized.</p>
<dd>
<dt><code>T</code> means tighter (stricter) name matching applies.</p>
<dd>
<dt><code>X</code> means use of this form is discouraged, and may not be stable.</p>
<dd></dl>
<p>NAME INFO<br />
   \p<br />
{<br />
    Adlam<br />
}<br />
\p{Script_Extensions = Adlam}(Short<br />
                              :<br />
                             \p{Adlm};<br />
                              NOT \p{Block = Adlam})(89)<br />
   \p<br />
{<br />
    Adlm<br />
}<br />
\p{Adlam}(= \p{Script_Extensions = Adlam})(NOT \p{Block = Adlam})(89)<br />
    X \p<br />
{<br />
    Aegean_Numbers<br />
}<br />
\p{Block = Aegean_Numbers}(64)<br />
    T \p<br />
{<br />
Age:<br />
    1.1<br />
}<br />
\p{Age = V1_1}(33_979)<br />
   \p{Age : V1_1} Code point&#8217;s usage introduced in version 1.1(33_979<br />
                                                                : U + 0000..01F5, U + 01FA..0217,<br />
                                                                  U + 0250..02A8, U + 02B0..02DE,<br />
                                                                  U + 02E0..02E9, U + 0300..0345 &#8230;)<br />
    T \p<br />
{<br />
Age:<br />
    2.0<br />
}<br />
\p{Age = V2_0}(144_521)<br />
   \p{Age : V2_0} Code point&#8217;s usage was introduced in version 2.0;<br />
See also Property &#8216;Present_In'(144_521<br />
                               : U + 0591..05A1,<br />
                                 U + 05A3..05AF, U + 05C4, U + 0F00..0F47,<br />
                                 U + 0F49..0F69, U + 0F71..0F8B &#8230;)<br />
    T \p<br />
{<br />
Age:<br />
    2.1<br />
}<br />
\p{Age = V2_1}(2)<br />
   \p{Age : V2_1} Code point&#8217;s usage was introduced in version 2.1;<br />
See also Property &#8216;Present_In'(2<br />
                               : U + 20AC, U + FFFC)<br />
    T \p<br />
{<br />
Age:<br />
    3.0<br />
}<br />
\p{Age = V3_0}(10_307)<br />
   \p{Age : V3_0} Code point&#8217;s usage was introduced in version 3.0;<br />
See also Property &#8216;Present_In'(10_307<br />
                               : U + 01F6..01F9,<br />
                                 U + 0218..021F, U + 0222..0233,<br />
                                 U + 02A9..02AD, U + 02DF, U + 02EA..02EE &#8230;)<br />
    T \p<br />
{<br />
Age:<br />
    3.1<br />
}<br />
\p{Age = V3_1}(44_978)<br />
   \p{Age : V3_1} Code point&#8217;s usage was introduced in version 3.1;<br />
See also Property &#8216;Present_In'(44_978<br />
                               : U + 03F4..03F5,<br />
                                 U + FDD0..FDEF, U + 10300..1031E,<br />
                                 U + 10320..10323, U + 10330..1034A,<br />
                                 U + 10400..10425 &#8230;)<br />
    T \p<br />
{<br />
Age:<br />
    3.2<br />
}<br />
\p{Age = V3_2}(1016)<br />
   \p{Age : V3_2} Code point&#8217;s usage was introduced in version 3.2;<br />
See also Property &#8216;Present_In'(1016<br />
                               : U + 0220, U + 034F,<br />
                                 U + 0363..036F, U + 03D8..03D9, U + 03F6,<br />
                                 U + 048A..048B &#8230;)<br />
    T \p<br />
{<br />
Age:<br />
    4.0<br />
}<br />
\p{Age = V4_0}(1226)<br />
   \p{Age : V4_0} Code point&#8217;s usage was introduced in version 4.0;<br />
See also Property &#8216;Present_In'(1226<br />
                               : U + 0221,<br />
                                 U + 0234..0236, U + 02AE..02AF,<br />
                                 U + 02EF..02FF, U + 0350..0357, U + 035D..035F &#8230;)<br />
    T \p<br />
{<br />
Age:<br />
    4.1<br />
}<br />
\p{Age = V4_1}(1273)<br />
   \p{Age : V4_1} Code point&#8217;s usage was introduced in version 4.1;<br />
See also Property &#8216;Present_In'(1273<br />
                               : U + 0237..0241,<br />
                                 U + 0358..035C, U + 03FC..03FF,<br />
                                 U + 04F6..04F7, U + 05A2, U + 05C5..05C7 &#8230;)<br />
    T \p<br />
{<br />
Age:<br />
    5.0<br />
}<br />
\p{Age = V5_0}(1369)<br />
   \p{Age : V5_0} Code point&#8217;s usage was introduced in version 5.0;<br />
See also Property &#8216;Present_In'(1369<br />
                               : U + 0242..024F,<br />
                                 U + 037B..037D, U + 04CF, U + 04FA..04FF,<br />
                                 U + 0510..0513, U + 05BA &#8230;)<br />
    T \p<br />
{<br />
Age:<br />
    5.1<br />
}<br />
\p{Age = V5_1}(1624)<br />
   \p{Age : V5_1} Code point&#8217;s usage was introduced in version 5.1;<br />
See also Property &#8216;Present_In'(1624<br />
                               : U + 0370..0373,<br />
                                 U + 0376..0377, U + 03CF, U + 0487,<br />
                                 U + 0514..0523, U + 0606..060A &#8230;)<br />
    T \p<br />
{<br />
Age:<br />
    5.2<br />
}<br />
\p{Age = V5_2}(6648)<br />
   \p{Age : V5_2} Code point&#8217;s usage was introduced in version 5.2;<br />
See also Property &#8216;Present_In'(6648<br />
                               : U + 0524..0525,<br />
                                 U + 0800..082D, U + 0830..083E, U + 0900,<br />
                                 U + 094E, U + 0955 &#8230;)<br />
    T \p<br />
{<br />
Age:<br />
    6.0<br />
}<br />
\p{Age = V6_0}(2088)<br />
   \p{Age : V6_0} Code point&#8217;s usage was introduced in version 6.0;<br />
See also Property &#8216;Present_In'(2088<br />
                               : U + 0526..0527,<br />
                                 U + 0620, U + 065F, U + 0840..085B, U + 085E,<br />
                                 U + 093A..093B &#8230;)<br />
    T \p<br />
{<br />
Age:<br />
    6.1<br />
}<br />
\p{Age = V6_1}(732)<br />
   \p{Age : V6_1} Code point&#8217;s usage was introduced in version 6.1;<br />
See also Property &#8216;Present_In'(732<br />
                               : U + 058F, U + 0604,<br />
                                 U + 08A0, U + 08A2..08AC, U + 08E4..08FE,<br />
                                 U + 0AF0 &#8230;)<br />
    T \p<br />
{<br />
Age:<br />
    6.2<br />
}<br />
\p{Age = V6_2}(1)<br />
   \p{Age : V6_2} Code point&#8217;s usage was introduced in version 6.2;<br />
See also Property &#8216;Present_In'(1<br />
                               : U + 20BA)<br />
    T \p<br />
{<br />
Age:<br />
    6.3<br />
}<br />
\p{Age = V6_3}(5)<br />
   \p{Age : V6_3} Code point&#8217;s usage was introduced in version 6.3;<br />
See also Property &#8216;Present_In'(5<br />
                               : U + 061C, U + 2066..2069)<br />
    T \p<br />
{<br />
Age:<br />
    7.0<br />
}<br />
\p{Age = V7_0}(2834)<br />
   \p{Age : V7_0} Code point&#8217;s usage was introduced in version 7.0;<br />
See also Property &#8216;Present_In'(2834<br />
                               : U + 037F,<br />
                                 U + 0528..052F, U + 058D..058E, U + 0605,<br />
                                 U + 08A1, U + 08AD..08B2 &#8230;)<br />
    T \p<br />
{<br />
Age:<br />
    8.0<br />
}<br />
\p{Age = V8_0}(7716)<br />
   \p{Age : V8_0} Code point&#8217;s usage was introduced in version 8.0;<br />
See also Property &#8216;Present_In'(7716<br />
                               : U + 08B3..08B4,<br />
                                 U + 08E3, U + 0AF9, U + 0C5A, U + 0D5F, U + 13F5 &#8230;)<br />
    T \p<br />
{<br />
Age:<br />
    9.0<br />
}<br />
\p{Age = V9_0}(7500)<br />
   \p{Age : V9_0} Code point&#8217;s usage was introduced in version 9.0;<br />
See also Property &#8216;Present_In'(7500<br />
                               : U + 08B6..08BD,<br />
                                 U + 08D4..08E2, U + 0C80, U + 0D4F,<br />
                                 U + 0D54..0D56, U + 0D58..0D5E &#8230;)<br />
    T \p<br />
{<br />
Age:<br />
    10.0<br />
}<br />
\p{Age = V10_0}(8518)<br />
   \p{Age : V10_0} Code point&#8217;s usage was introduced in version 10.0;<br />
See also Property &#8216;Present_In'(8518<br />
                               : U + 0860..086A,<br />
                                 U + 09FC..09FD, U + 0AFA..0AFF, U + 0D00,<br />
                                 U + 0D3B..0D3C, U + 1CF7 &#8230;)<br />
    T \p<br />
{<br />
Age:<br />
    11.0<br />
}<br />
\p{Age = V11_0}(684)<br />
   \p{Age : V11_0} Code point&#8217;s usage was introduced in version 11.0;<br />
See also Property &#8216;Present_In'(684<br />
                               : U + 0560, U + 0588,<br />
                                 U + 05EF, U + 07FD..07FF, U + 08D3, U + 09FE &#8230;)<br />
    T \p<br />
{<br />
Age:<br />
    12.0<br />
}<br />
\p{Age = V12_0}(554)<br />
   \p{Age : V12_0} Code point&#8217;s usage was introduced in version 12.0;<br />
See also Property &#8216;Present_In'(554<br />
                               : U + 0C77, U + 0E86,<br />
                                 U + 0E89, U + 0E8C, U + 0E8E..0E93, U + 0E98 &#8230;)<br />
    T \p<br />
{<br />
Age:<br />
    12.1<br />
}<br />
\p{Age = V12_1}(1)<br />
   \p{Age : V12_1} Code point&#8217;s usage was introduced in version 12.1;<br />
See also Property &#8216;Present_In'(1<br />
                               : U + 32FF)<br />
   \p<br />
{<br />
Age:<br />
    NA<br />
}<br />
\p{Age = Unassigned}(836_536 plus all<br />
                         above &#8211;<br />
                     Unicode code points)<br />
   \p{Age : Unassigned} Code point&#8217;s usage has not been assigned in any Unicode release thus far.(Short<br />
                                                                                                   :<br />
                             \p{Age = NA})(836_536 plus all above &#8211;<br />
                                                Unicode code points<br />
                                            : U + 0378..0379,<br />
                                              U + 0380..0383, U + 038B, U + 038D, U + 03A2,<br />
                                              U + 0530 &#8230;)<br />
   \p<br />
{<br />
    Aghb<br />
}<br />
\p{Caucasian_Albanian}(=<br />
                             \p{Script_Extensions =<br />
                                     Caucasian_Albanian})(NOT \p{Block =<br />
                                                                     Caucasian_Albanian})(53)<br />
   \p<br />
{<br />
    AHex<br />
}<br />
\p{PosixXDigit}(= \p{ASCII_Hex_Digit = Y})(22)<br />
   \p<br />
{<br />
AHex:<br />
    *<br />
}<br />
\p<br />
{<br />
ASCII_Hex_Digit:<br />
    *<br />
}<br />
\p<br />
{<br />
    Ahom<br />
}<br />
\p{Script_Extensions = Ahom}(NOT \p{Block =<br />
                                        Ahom})(58)<br />
    X \p<br />
{<br />
    Alchemical<br />
}<br />
\p{Alchemical_Symbols}(= \p{Block =<br />
                                Alchemical_Symbols})(128)<br />
    X \p<br />
{<br />
    Alchemical_Symbols<br />
}<br />
\p{Block = Alchemical_Symbols}(Short<br />
                               :<br />
                             \p{InAlchemical})(128)<br />
   \p{All} All code points,<br />
    including those above<br />
        Unicode.Same as qr<br />
        /./ s(1_114_112 plus all above &#8211; Unicode code points<br />
              : U + 0000..infinity)<br />
   \p<br />
{<br />
    Alnum<br />
}<br />
\p{XPosixAlnum}(127_886)<br />
   \p<br />
{<br />
    Alpha<br />
}<br />
\p{XPosixAlpha}(= \p{Alphabetic = Y})(127_256)<br />
   \p<br />
{<br />
Alpha:<br />
    *<br />
}<br />
\p<br />
{<br />
Alphabetic:<br />
    *<br />
}<br />
\p<br />
{<br />
    Alphabetic<br />
}          \p{XPosixAlpha} (= \p{Alphabetic=Y})<br />
                             (127_256)<br />
   \p{Alphabetic: N*}      (Short: \p{Alpha=N}, \P{Alpha}) (986_856<br />
                             plus all above-Unicode code points:<br />
                             [
