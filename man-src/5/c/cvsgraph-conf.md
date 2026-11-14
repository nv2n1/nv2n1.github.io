---
title: "cvsgraph-conf(5)"
name: "cvsgraph-conf"
section: "5"
letter: "c"
url: "/docs/linux/man/5-cvsgraph-conf/"
description: "cvsgraph.conf – CVS/RCS repository grapher configuration"
---

<p>cvsgraph.conf &#8211; CVS/RCS repository grapher configuration</p>
<h2>Overview</h2>
<p>The configuration file is a context free grammar where empty lines and whitespace are ignored. Comments start with &#8216;#&#8217; and everything until end of line is ignored.<br />
 A configuration parameter is written as:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;keyword&gt; = &lt;argument&gt; ;</p>
<p> Keywords are defined in <code>PARAMETERS</code>. The argument can be either numerical or string typed. </p>
<p> Numbers may be entered as octal, decimal or hex as in 0117, 79 and 0x4f respectively. Floating point numbers contain a single &#8216;.&#8217;, but must start with a digit. Integer numbers are automagically converted to floats if required. </p>
<p> Strings are C-style strings, enclosed in double quotes in which characters may be escaped with &#8216;\&#8217; and written in octal and hex escapes. Note that &#8216;\&#8217; must be escaped if it is to be entered as a character. Escapes recognized are &#8216;\[abfnrtv]&#8217;, &#8216;\[xX][0-9a-fA-F]{2}&#8217; and &#8216;\[012][0-7]{0,2}&#8217;.<br />
 Some strings are expanded with printf like conversions which start with &#8216;%&#8217;. Not all are applicable at all times, in which case they will expand to nothing.<br />
 Note that expansions of paths are available with and without trailing &#8216;/&#8217;. The distinction is required for path construction to ensure that empty expansions will not redirect the path to root and no double &#8216;/&#8217; in a path is generated.</p>
<dl>
<dt>%c</p>
<dd>CVS root including a trailing &#8216;/&#8217; if non-empty</p>
<dt>%C</p>
<dd>CVS root without trailing &#8216;/&#8217;, regardless of how it was entered on the command line</p>
<dt>%m</p>
<dd>CVS module including trailing &#8216;/&#8217; if non-empty</p>
<dt>%M</p>
<dd>CVS module without trailing &#8216;/&#8217;, regardless of how it was entered on the command line</p>
<dt>%f</p>
<dd>filename without path (<i>basename &lt;name&gt;</i> functionality)</p>
<dt>%F</p>
<dd>filename without path and with &quot;,v&quot; stripped (<i>basename &lt;name&gt; ,v</i> functionality)</p>
<dt>%p</p>
<dd>path part of filename. This includes a trailing &#8216;/&#8217; if the path is non-empty</p>
<dt>%r</p>
<dd>number of revisions</p>
<dt>%b</p>
<dd>number of branches</p>
<dt>%%</p>
<dd>literal &#8216;%&#8217;</p>
<dt>%R</p>
<dd>the revision number (e.g. &#8216;1.2.4.4&#8217;)</p>
<dt>%P</p>
<dd>previous revision number</p>
<dt>%B</p>
<dd>the branch number (e.g. &#8216;1.2.4&#8217;)</p>
<dt>%d</p>
<dd>date of revision</p>
<dt>%a</p>
<dd>author of revision</p>
<dt>%s</p>
<dd>state of revision</p>
<dt>%l</p>
<dd>The log entry of the revision. You need to enable <code>parse_logs</code> for this to work. You may append an optional truncate length by writing &#8216;[num]&#8217; (with num the maximum length) directly after %l. If no truncation is specified, then all will be expanded. Specifying a negative truncation length means that newlines should be replaced by spaces. If truncation occurs, then &quot;&#8230;&quot; will be appended. The expansion is scanned for possible HTML entities and are replaced by &amp;#&#8230;; equivalents.<br />
 For example: &quot;%l[25]&quot; will expand up to 25 characters of the log.<br />
 Note: This expansion is obsolete. Please use &quot;%(%L%)&quot;; see comment below.</p>
<dt>%L</p>
<dd>Same as %l, but no HTML entity translations are performed.</p>
<dt>%t</p>
<dd>current tag of branch or revision</p>
<dt>%0..%9</p>
<dd>command-line argument -0 .. -9</p>
<dt>%(&#8230;%)</p>
<dd>HTMLize the string withing the parenthesis. This is useful to prevent a possible cross site scripting bug when expanding tags into the map generation. For an exploit, you need to have an attack on your CVS server, or you need to be a complete idiot to enter a tag with &#8216;&lt;&#8216;, &#8216;&gt;&#8217; or &#8216;&quot;&#8217; characters.<br />
 Example: a string &quot;%(%t%)&quot;, with tag <code>&gt;&lt;script xxx=&quot;&#8230;&quot;&gt;&lt;</code> will expand to <code>&amp;gt;&amp;lt;script xxx=&amp;#34;&#8230;&amp;#34;&amp;gt;&amp;lt;</code> and not into the execution of a script.<br />
 Note: This method is preferred to the %l expansion, because it is more generic solution (i.e. use &quot;%(%L%)&quot; for log expansions). </p>
</dl>
<p> Fonts are numbered 0..4 (as defined in libgd) where 0 = tiny, 1 = small, 2 = medium (bold), 3 = large and 4 = giant. </p>
<p> Colors are strings, similar to HTML type colors in the form &quot;#rrggbb&quot; with parts written in hex, where rr = red (00-ff), gg = green (00-ff) and bb = blue (00-ff). </p>
<p> Colors and some strings can also be defined as conditional expressions so that revision/branch conditions can be repesented visually: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>color/string&nbsp;<wbr>=&nbsp;<wbr>[&nbsp;<wbr>&quot;key&quot;&nbsp;<wbr>op&nbsp;<wbr>&quot;content&quot;&nbsp;<wbr>truecase falsecase&nbsp;<wbr>];<br />
 Operator &#8216;op&#8217; can be one of:</p>
<dl>
<dt>=~</p>
<dd>contained in regex</p>
<dt>=*</p>
<dd>contained in regex, case insensitive</p>
<dt>!~</p>
<dd>not contained in regex</p>
<dt>!*</p>
<dd>not contained in regex, case insensitive</p>
<dt>&lt;</p>
<dd>less than string, timestamp or rev/branch number</p>
<dt>&lt;=</p>
<dd>less or equal than string, timestamp or rev/branch number</p>
<dt>&gt;</p>
<dd>greater than string, timestamp or rev/branch number</p>
<dt>&gt;=</p>
<dd>greater or equal than string, timestamp or rev/branch number</p>
<dt>==</p>
<dd>equal than string, timestamp or rev/branch number</p>
<dt>!=</p>
<dd>not equal than string, timestamp or rev/branch number</dl>
<p> The &#8216;content&#8217; is one of:<br />
&nbsp;<wbr>*&nbsp;<wbr>POSIX 1003.2 extended regular expression<br />
&nbsp;<wbr>*&nbsp;<wbr>timestamp in UTC format: YYYY[.MM[.DD[.hh[.mm[.ss]]]]]<br />
&nbsp;<wbr>*&nbsp;<wbr>revision or branch number </p>
<p> The &#8216;key&#8217; can be one of:</p>
<dl>
<dt>state</p>
<dd>State of the revision</p>
<dt>author</p>
<dd>The auther of a revision</p>
<dt>tag</p>
<dd>both revision- and branch-tags</p>
<dt>date</p>
<dd>date of the revision</p>
<dt>rev</p>
<dd>numeric revision- or branch-number</dl>
<p> Both &#8216;truecase&#8217; and &#8216;falsecase&#8217; can be either a (color-)string, as described above, or a new conditional expression. Examples: </p>
<p>&nbsp;<wbr>rev_bgcolor&nbsp;<wbr>=&nbsp;<wbr>[&nbsp;<wbr>&quot;state&quot;&nbsp;<wbr>=~&nbsp;<wbr>&quot;dead&quot;&nbsp;<wbr>&quot;#e08080&quot;&nbsp;<wbr>&quot;#f0f0f0&quot;&nbsp;<wbr>]; </p>
<p>&nbsp;<wbr>branch_color=&nbsp;<wbr>[&nbsp;<wbr>&quot;rev&quot;&nbsp;<wbr>&lt;&nbsp;<wbr>&quot;2.1.2&quot;&nbsp;<wbr>&quot;#000000&quot;&nbsp;<wbr>[&nbsp;<wbr>&quot;tag&quot;&nbsp;<wbr>=~&nbsp;<wbr>&quot;XyZ.*&quot;&nbsp;<wbr>&quot;#123456&quot;&nbsp;<wbr>&quot;#654321&quot;&nbsp;<wbr>]&nbsp;<wbr>]; </p>
<p>&nbsp;<wbr>rev_idtext&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>[&nbsp;<wbr>&quot;state&quot;&nbsp;<wbr>==&nbsp;<wbr>&quot;dead&quot;&nbsp;<wbr>&quot;Dead&nbsp;<wbr>%R&quot;&nbsp;<wbr>&quot;%R&quot;&nbsp;<wbr>]<br />
 Note that not all colors can be changed on the fly. For example, branch_color cannot be be changed based on revision identification (i.e. author, date or state). The color_bg is always unique and fixed (all expressions will evaluate to the false case). Also, only string rev_text and rev_idtext can be conditional expressions as other do not make much sense to be dynamic. </p>
<p> Booleans have three possible arguments: true, false and not. `Not&#8217; means inverse of what it was (logical negation) and is represented by the value -1. For the configuration file that means that the default value is negated. However, the not possibility is a very handy tool for command line overrides generated from (CGI) scripts. </p>
<p> There are several reserved words besides of the keywords. These additional reserved words expand to numerical values:<br />
 Booleans:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>false = 0</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>true = 1</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>not = -1</p>
<p> Alignment specifiers:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>left = 0</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>center = 1</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>right = 2</p>
<p> Image specifiers:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>gif = 0</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>png = 1</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>jpeg = 2</p>
<p> Font specifiers:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>tiny = 0</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>small = 1</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>medium = 2</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>large = 3</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>giant = 4</p>
<p> HTML level specifiers:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>HTML3 = 1</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>HTML4 = 2</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>XHTML = 3</p>
<h2>Parameters</h2>
<dl>
<dt><code>cvsroot</code> <i>string</i></p>
<dd>The absolute base directory where the CVS/RCS repository can be found. A &#8216;/&#8217; will be appended to the string if it is not empty and does not contain a trailing &#8216;/&#8217;.<br />
 Default is an empty string. </p>
<dt><code>cvsmodule</code> <i>string</i></p>
<dd>The module name in the CVS/RCS repository. This is converted into a subdirectory name with a trailing &#8216;/&#8217;.<br />
 Default is an empty string. </p>
<dt><code>color_bg</code> <i>color</i></p>
<dd>The background color of the image.<br />
 Default is white (&quot;#ffffff&quot;). </p>
<dt><code>transparent_bg</code> <i>boolean</i></p>
<dd>The background color of the image is to be the transparent color. This is only useful for PNG images. Be sure to set <code>color_bg</code> to something reasonable to make sure that the image is viewable with programs that do not support transparency.<br />
 Default is false. </p>
<dt><code>date_format</code> <i>string</i></p>
<dd>The <code><a href="/docs/linux/man/3-strftime/">strftime</a>(3)</code> format string for date and time representation in the &#8216;%d&#8217; expansion.<br />
 Default is &quot;%d-%b-%Y %H:%M:%S&quot;. </p>
<dt><code>box_shadow</code> <i>boolean</i></p>
<dd>A boolean whether or not to draw a shadow for the boxes of revisions and branches.<br />
 Default is false. </p>
<dt><code>upside_down</code> <i>boolean</i></p>
<dd>Draw the entire tree upside down if set. I.e. highest revisions are at the top of the image. See also <code><a href="/docs/linux/man/1-cvsgraph/">cvsgraph</a>(1)</code> option &#8216;<code>-u</code>&#8216;.<br />
 Default is false. </p>
<dt><code>left_right</code> <i>boolean</i></p>
<dd>Draw the entire tree from left to right instead of top down if set. I.e. highest revisions are at the right of the image. You can also draw the tree right to left when <code>upside_down</code> is set too.<br />
 Default is false. </p>
<dt><code>strip_untagged</code> <i>boolean</i></p>
<dd>Omit all revisions that do not have tags and are not a branch point. This reduces the image-size, but can be confusing when looking for a specific revision. See also <code><a href="/docs/linux/man/1-cvsgraph/">cvsgraph</a>(1)</code> option &#8216;<code>-s</code>&#8216;.<br />
 Default is false. </p>
<dt><code>strip_first_rev</code> <i>boolean</i></p>
<dd>Also omit the first revision in a branch if it does not have tags and is not a branch point. This has only effect if <code>strip_untagged</code> is set. See also <code><a href="/docs/linux/man/1-cvsgraph/">cvsgraph</a>(1)</code> option &#8216;<code>-S</code>&#8216;.<br />
 Default is false. </p>
<dt><code>auto_stretch</code> <i>boolean</i></p>
<dd>Try to stretch the inter-revision spacing to move the trunks more to the left, effectively reducing the image&#8217;s size. See also <code><a href="/docs/linux/man/1-cvsgraph/">cvsgraph</a>(1)</code> option &#8216;<code>-k</code>&#8216;.<br />
 Default is false. </p>
<dt><code>use_ttf</code> <i>boolean</i></p>
<dd>Enable TrueType rendering of strings using the FreeType interface of libgd. Note that ttf rendering is significantly slower than libgd&#8217;s bitmap fonts.<br />
 Default is false. </p>
<dt><code>anti_alias</code> <i>boolean</i></p>
<dd>Enable antialias rendering of TrueType fonts. This has only effect if <code>use_ttf</code> is set. Enabling anti_alias gives very nice results. However, that is at the expense of 8-bit vs. 4-bit colormap images, which can be a major drawback because the size of 8-bit images is 3..4 times that of 4-bit images (with compressed PNG as output).<br />
 Default is true. </p>
<dt><code>thick_lines</code> <i>number</i></p>
<dd>Set the thickness of connector lines between boxes. Normally, lines are drawn one pixel wide, but can look somewhat thin. Setting the thickness to anything over 5 would be plain ugly (but hey, who is to debate taste :-). Values less than 1 and over 11 are clipped.<br />
 Default is 1. </p>
<dt><code>parse_logs</code> <i>boolean</i></p>
<dd>Enable the parsing of the <i>entire</i> ,v file to read the log-entries between revisions. This is necessary for the %l expansion to work, but slows down parsing by a very large factor. You&#8217;ve been warned.<br />
 Default is false. </p>
<dt><code>html_level</code> <i>number</i></p>
<dd>Set the compliance to different types of HTML. The generated image map is slightly different for version 3.x, 4.x and XHTML. You can use the predefined identifiers (HTML3, HTML4 and XHTML) to set this value. Command line option &#8216;<code>-x</code>&#8216; overrides the setting.<br />
 Default is HTML3 (3.x compatibility). </p>
<dt><code>branch_ttfont</code> <i>string</i></p>
<dd>
<dt><code>branch_tag_ttfont</code> <i>string</i></p>
<dd>
<dt><code>rev_ttfont</code> <i>string</i></p>
<dd>
<dt><code>rev_text_ttfont</code> <i>string</i></p>
<dd>
<dt><code>tag_ttfont</code> <i>string</i></p>
<dd>
<dt><code>title_ttfont</code> <i>string</i></p>
<dd>
<dt><code>msg_ttfont</code> <i>string</i></p>
<dd>Set the TrueType font face or filename for the individual elements. Gd&#8217;s bitmap fonts are used as a fallback if the font cannot be found or contains errors.<br />
 Default none. </p>
<dt><code>branch_ttsize</code> <i>float</i></p>
<dd>
<dt><code>branch_tag_ttsize</code> <i>float</i></p>
<dd>
<dt><code>rev_ttsize</code> <i>float</i></p>
<dd>
<dt><code>rev_text_ttsize</code> <i>float</i></p>
<dd>
<dt><code>tag_ttsize</code> <i>float</i></p>
<dd>
<dt><code>title_ttsize</code> <i>float</i></p>
<dd>
<dt><code>msg_ttsize</code> <i>float</i></p>
<dd>Set the TrueType font size for the individual elements. See also *_ttfont.<br />
 Default 0.0. </p>
<dt><code>tag_font</code> <i>number</i></p>
<dd>The font used to draw tags in the revision boxes.<br />
 Default is tiny. </p>
<dt><code>tag_color</code> <i>color</i></p>
<dd>The color used to draw tags in the revision boxes.<br />
 Default is black (&quot;#000000&quot;). </p>
<dt><code>tag_ignore</code> <i>string</i></p>
<dd>An extended regular expression as described in <code><a href="/docs/linux/man/7-regex/">regex</a>(7)</code> to match all tags that should not be displayed in the graph. Note that a tag will always be displayed if it matches the <code>merge_from</code>/<code>merge_to</code> expressions regardless to it being set to ignore here.<br />
 Example: tag_ignore = &quot;(test|alpha)_release.*&quot;;<br />
 Default is empty (no matching occurs). </p>
<dt><code>tag_nocase</code> <i>boolean</i></p>
<dd>Ignore the case in regex matching in <code>tag_ignore</code>.<br />
 Default is false. </p>
<dt><code>tag_negate</code> <i>boolean</i></p>
<dd>Negate the matching criteria of the <code>tag_ignore</code> setting. If set, tags that match the <code>tag_ignore</code> will be shown, instead of matches being ignored. In any case, tags that match <code>merge_from</code>/<code>merge_to</code> expressions will never be suppressed.<br />
 Default is false. </p>
<dt><code>tag_ignore_merge</code> <i>boolean</i></p>
<dd>If set, then tags matched with <code>tag_ignore</code> will no longer be considered for matching by <code>merge_from</code> and <code>merge_to</code>.<br />
 Default is false. </p>
<dt><code>rev_font</code> <i>number</i></p>
<dd>Default is tiny. </p>
<dt><code>rev_color</code> <i>color</i></p>
<dd>The color of revision boxes, including the revision number.<br />
 Default is black (&quot;#000000&quot;). </p>
<dt><code>rev_bgcolor</code> <i>color</i></p>
<dd>Revision box background color. This is the interior fill of the box.<br />
 Default is white (&quot;#ffffff&quot;). </p>
<dt><code>rev_separator</code> <i>number</i></p>
<dd>Space between tags in revision boxes.<br />
 Default is 0. </p>
<dt><code>rev_minline</code> <i>number</i></p>
<dd>The minimum vertical distance between revision boxes.<br />
 Default is 0. </p>
<dt><code>rev_maxline</code> <i>number</i></p>
<dd>The maximum vertical distance between revision boxes. This has only effect if <code>auto_stretch</code> is set to true (or option &#8216;<code>-k</code>&#8216; is specified).<br />
 Default is 5 times <code>rev_minline</code>. </p>
<dt><code>rev_lspace</code> <i>number</i></p>
<dd>
<dt><code>rev_rspace</code> <i>number</i></p>
<dd>
<dt><code>rev_tspace</code> <i>number</i></p>
<dd>
<dt><code>rev_bspace</code> <i>number</i></p>
<dd>Interior spacing in revision boxes of left, right, top and bottom respectively. Note that the left right spacing is not used separately because text is center aligned.<br />
 Default is 0. </p>
<dt><code>rev_idtext</code> <i>conditional string</i></p>
<dd>The revision ID or revision number in a revision box.<br />
 Default is &quot;%R&quot;. </p>
<dt><code>rev_text</code> <i>conditional string</i></p>
<dd>The additional text in a revision box under the revision number.<br />
 Default is &quot;%d&quot;. </p>
<dt><code>rev_text_font</code> <i>number</i></p>
<dd>The font of the additional text in a revision box under the revision number.<br />
 Default is tiny. </p>
<dt><code>rev_text_color</code> <i>color</i></p>
<dd>The font color of the additional text in a revision box under the revision number.<br />
 Default is black (&quot;#000000&quot;). </p>
<dt><code>rev_maxtags</code> <i>number</i></p>
<dd>Limit the number of tags in a revision box. Old trees tend to have some revisions with extremely many tags attached, which would generate a huge revision box when drawn. Limiting the number is a fair solution. Note that tag sorting is not specified in the <code><a href="/docs/linux/man/7-rcsfile/">rcsfile</a>(7)</code>, but <code><a href="/docs/linux/man/1-cvs/">cvs</a>(1)</code> will normally have the newest tags located before older ones. Therefore, limiting the number of tags would most likely only affect older tags to be stripped. However, no guarantees are given that a specific tag is present when the limit is imposed. An ellipsis (&#8230;) is shown in the revision box when the number of tags got truncated.<br />
 Default is 0, meaning all tags shown. </p>
<dt><code>rev_hidenumber</code> <i>boolean</i></p>
<dd>If set, then no revision number is displayed in the revisionboxes. This reduces size for those graphs where the actual revision-number is irrelevant.<br />
 Default is false. </p>
<dt><code>msg_font</code> <i>number</i></p>
<dd>The font used to draw error and warning messages at the bottom of the graph.<br />
 Default is tiny. </p>
<dt><code>msg_color</code> <i>color</i></p>
<dd>The color used to draw error and warning messages.<br />
 Default is black (&quot;#000000&quot;). </p>
<dt><code>merge_color</code> <i>color</i></p>
<dd>The color of the lines to show merges.<br />
 Default is black (&quot;#000000&quot;). </p>
<dt><code>merge_front</code> <i>boolean</i></p>
<dd>The merge lines are drawn on top of the image if true. Otherwise, merge lines are drawn underneath.<br />
 Default is false. </p>
<dt><code>merge_nocase</code> <i>boolean</i></p>
<dd>Ignore the case in regex matching in <code>merge_from</code> and <code>merge_to</code>.<br />
 Default is false. </p>
<dt><code>merge_from</code> <i>string</i></p>
<dd>The <code>merge_from</code> is an extended regular expression as described in <code><a href="/docs/linux/man/7-regex/">regex</a>(7)</code> and POSIX 1003.2 (see also Single Unix Specification at <a rel="nofollow" href="http://www.opengroup.com">http://www.opengroup.com</a> ). The matching tags describe source revisions of merges. Each match is subsequently used in a search for the destination tag as described by the <code>merge_to</code> parameter.<br />
 Note: normal string rules apply. Therefore, all backslashes &#8216;\&#8217; must be escaped, e.g. &quot;\.&quot; must be written as &quot;\.&quot;.<br />
 Example: merge_from = &quot;^from_(.*)&quot;;<br />
 Default is empty (no matching occurs). </p>
<dt><code>merge_to</code> <i>string</i></p>
<dd>The <code>merge_to</code> is an extended regular expression with a twist. All subexpressions from the <code>merge_from</code> are expanded into <code>merge_to</code> using %[1-9] (in contrast to \[1-9] for backreferences). Care is taken to escape the constructed expression. A &#8216;$&#8217; at the end of the <code>merge_to</code> expression can be important to prevent &#8216;near match&#8217; references. Normally, you want the destination to be a good representation of the source. However, this depends on how well you defined the tags in the first place.<br />
 Example: merge_to = &quot;^merge_%1$&quot;;<br />
 Above example, combined with the merge_from example would match a tag &quot;from_BugFix_2002&quot; to the merge-destination with tag &quot;merge_BugFix_2002&quot;.<br />
 Default is empty (no matching occurs). </p>
<dt><code>merge_findall</code> <i>boolean</i></p>
<dd>Normally, <code>merge_from</code>/m<code>erge_to</code> will only find the first matching tag-combination and draw a line between them, If <code>merge_findall</code> is set, then all matching <code>merge_to</code>s will result in lines from the from-tag to the to-tag.<br />
 Default is false. </p>
<dt><code>merge_arrows</code> <i>boolean</i></p>
<dd>Enable the use of arrows pointing to the merge destination.<br />
 Default is true. </p>
<dt><code>merge_cvsnt</code> <i>boolean</i></p>
<dd>Enable drawing of mergepoints as used by CVSNT.<br />
 Default is true. </p>
<dt><code>merge_cvsnt_color</code> <i>color</i></p>
<dd>The color of the lines to show merges from mergepoints.<br />
 Default is black (&quot;#000000&quot;). </p>
<dt><code>arrow_width</code> <i>number</i></p>
<dd>
<dt><code>arrow_length</code> <i>number</i></p>
<dd>Specifies the size of the arrow pointing to the merge destination.<br />
 Default is arrow_width=3, arrow_length=12. </p>
<dt><code>branch_font</code> <i>number</i></p>
<dd>The font of the number in a branch box.<br />
 Default is tiny. </p>
<dt><code>branch_tag_font</code> <i>number</i></p>
<dd>The font of the tags in a branch box.<br />
 Default is tiny. </p>
<dt><code>branch_color</code> <i>color</i></p>
<dd>All branch element&#8217;s color excluding tags.<br />
 Default is black (&quot;#000000&quot;). </p>
<dt><code>branch_bgcolor</code> <i>color</i></p>
<dd>Branch box background color. This is the interior fill of the box.<br />
 Default is white (&quot;#ffffff&quot;). </p>
<dt><code>branch_tag_color</code> <i>color</i></p>
<dd>All branch tags&#8217; color.<br />
 Default is black (&quot;#000000&quot;). </p>
<dt><code>branch_lspace</code> <i>number</i></p>
<dd>
<dt><code>branch_rspace</code> <i>number</i></p>
<dd>
<dt><code>branch_tspace</code> <i>number</i></p>
<dd>
<dt><code>branch_bspace</code> <i>number</i></p>
<dd>Interior spacing of branch boxes.<br />
 Default is 0. </p>
<dt><code>branch_margin</code> <i>number</i></p>
<dd>Exterior spacing of branches. Each branch will be spaced with a minimum of this value.<br />
 Default is 0. </p>
<dt><code>branch_connect</code> <i>number</i></p>
<dd>Length of the vertical connector from a revision to the branch box.<br />
 Default is 0. </p>
<dt><code>branch_dupbox</code> <i>boolean</i></p>
<dd>Add an extra branch box at the end of the trunk. Useful for upside down drawn trees. If there are no commits on a branch, then no extra box is added, regardless of the setting of this option.<br />
 Default is false. </p>
<dt><code>branch_fold</code> <i>boolean</i></p>
<dd>Fold branches that have no commits into one branch-box. This helps to reduce the size of the overall image by a huge factor (5..10 in most cases). Many applications of CVS use many branches, but not all files in the repository change for each branch. Especially stable files line .cvsignore or older code tend to accumulate many empty branches at one and the same revision. Folding these branches into one box reduces the width of these images considerably.<br />
 Default is true. </p>
<dt><code>branch_foldall</code> <i>boolean</i></p>
<dd>Fold all empty branches that sprout from the save revision in one box. If this option is not set, then multiple boxes will be created if the empty branches are interspaced with ones that have revisions attached. When this option is set, then all empty branches will be collected and put into the box of the first occurring empty branch on the revision&#8217;s branch point. Setting this option will reduce image size with interspaced commits to the a maximum.<br />
 Default is false. </p>
<dt><code>branch_resort</code> <i>boolean</i></p>
<dd>Resort the branches according to the number of revisions they have, where less revisions will stick closer to the sprouting trunk. This will reduce image size under circumstances where many branches have significant different number of revisions.<br />
 Default is false. </p>
<dt><code>branch_subtree</code> <i>string</i></p>
<dd>Reduce the tree only to include the subtree from the branch-number given in the argument. If the argument is a revision which is the root of branches, then all those branches will be shown. The argument can also be a symbolic tag (either a branch- or revision-tag). You normally would set this option from the command line with the -O option for interactive flexibility.<br />
 Example: branch_subtree = &quot;1.2.4&quot;;<br />
 Default is empty (all branches shown). </p>
<dt><code>title</code> <i>string</i></p>
<dd>The title of the image.<br />
 Default is empty string. </p>
<dt><code>title_x</code> <i>number</i></p>
<dd>
<dt><code>title_y</code> <i>number</i></p>
<dd>Position of title.<br />
 Default is 0. </p>
<dt><code>title_font</code> <i>number</i></p>
<dd>The font of the title.<br />
 Default is tiny. </p>
<dt><code>title_align</code> <i>number</i></p>
<dd>Horizontal alignment of the title.<br />
 Default is left. </p>
<dt><code>title_color</code> <i>color</i></p>
<dd>The color of the title.<br />
 Default is black (&quot;#000000&quot;). </p>
<dt><code>margin_top</code> <i>number</i></p>
<dd>
<dt><code>margin_bottom</code> <i>number</i></p>
<dd>
<dt><code>margin_left</code> <i>number</i></p>
<dd>
<dt><code>margin_right</code> <i>number</i></p>
<dd>Margins of the image. Note: the title position is not affected by the margin.<br />
 Default is 0. </p>
<dt><code>image_type</code> <i>number</i></p>
<dd>Image types are available if they can be found in the gd library. Some versions of gd do not have gif, although newer version have it implemented again. CvsGraph will automatically generate png images if gif is not available.<br />
 Default is dependent on availability and is prioritized in the order png, gif and jpeg. </p>
<dt><code>image_quality</code> <i>number</i></p>
<dd>The quality of a jpeg image (1..100)<br />
 Default is 100. </p>
<dt><code>image_compress</code> <i>number</i></p>
<dd>Set the compression level of png images (-1..9). Zero means no compression. A higher number means higher compression. Minus one selects the default library setting.<br />
 Default is -1. </p>
<dt><code>image_interlace</code> <i>boolean</i></p>
<dd>Write png and jpeg images in interlaced format. This enables progressive loading in your browser (if supported).<br />
 Default is false. </p>
<dt><code>map_name</code> <i>string</i></p>
<dd>The name= attribute in &lt;map name=&quot;mapname&quot;&gt;&#8230;&lt;/map&gt; in the generated HTML map.<br />
 Default is &quot;CvsGraphImageMap&quot;. </p>
<dt><code>map_branch_href</code> <i>string</i></p>
<dd>
<dt><code>map_rev_href</code> <i>string</i></p>
<dd>
<dt><code>map_diff_href</code> <i>string</i></p>
<dd>
<dt><code>map_merge_href</code> <i>string</i></p>
<dd>These are the href= attributes in the &lt;area&gt; tags of HTML.<br />
 Default are:<br />
 branch: &quot;href=\&quot;unset: conf.map_branch_href\&quot;&quot;<br />
 revision: &quot;href=\&quot;unset: conf.map_rev_href\&quot;&quot;<br />
 diff: &quot;href=\&quot;unset: conf.map_diff_href\&quot;&quot;<br />
 merge: &quot;href=\&quot;unset: conf.map_merge_href\&quot;&quot; </p>
<dt><code>map_branch_alt</code> <i>string</i></p>
<dd>
<dt><code>map_rev_alt</code> <i>string</i></p>
<dd>
<dt><code>map_diff_alt</code> <i>string</i></p>
<dd>
<dt><code>map_merge_alt</code> <i>string</i></p>
<dd>These are the alt= attributes in the &lt;area&gt; tags of HTML.<br />
 Default are &quot;alt=\&quot;%B\&quot;&quot;, &quot;alt=\&quot;%R\&quot;&quot;, &quot;alt=\&quot;%P &amp;lt;-&amp;gt; %R\&quot;&quot; and &quot;alt=\&quot;%P &amp;lt;-&amp;gt; %R\&quot;&quot; respectively. </p>
</dl>
<h2>Author</h2>
<p><code>CvsGraph</code> is written and maintained by B. Stultiens.<br />
 Send comments and bug reports to <i>cvsgraph [at] akhphd.au.dk</i> (read the mailnote in the README file first) and visit the homepage at:<br />
 <i><a rel="nofollow" href="http://www.akhphd.au.dk/~bertho/cvsgraph/">http://www.akhphd.au.dk/~bertho/cvsgraph/</a></i>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-cvsgraph/">cvsgraph</a>(1)</code> </p>
