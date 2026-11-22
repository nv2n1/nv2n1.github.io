---

title: "dviasm(1)"
name: "dviasm"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dviasm/"
description: "DVIasm – a TeX utility program for editing DVI files directly"
---

<p> DVIasm &#8211; a TeX utility program for editing DVI files directly </p>
<h2>SYNOPSIS</h2>
<p> <code>dviasm</code> [&lt;<i>options</i>&gt;] &lt;<i>dvi_file</i>&gt;|&lt;<i>dvi_dump_file</i>&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>DVIasm</code> is a TeX utility program which is designed for editing DeVice-Independent (DVI) files directly. It consists of a single Python script, dviasm.py, in a human readable text format. It runs on any platform in which Python 3 is installed.</p>
<dl>
<dt>Features of <code>DVIasm</code> includes:</dt>
<dd>
</dd><dt>
</dt><dd> 1) Disassemble a DVI file (or XeTeX XDV file) into a human-readable text file, the contents of which are easy to modify.</dd>
<dt>
</dt><dd> 2) Assembles the output text file back to the binary format.</dd>
<dt>There are several alternatives for dumping and editing DVI files:</dt>
<dd>
</dd><dt>
</dt><dd> 1) <code>DVItype</code> developed by Donald E. Knuth supports one-way conversion from DVI to a text format. There are also some derivatives: <code>pDVItype</code> for pTeX, <code>upDVItype</code> for upTeX, <code>ODVItype</code> for Omega.</dd>
<dt>
</dt><dd> 2) The programs <code>dv2dt</code> and <code>dt2dv</code> can be used in pairs to allow two-way conversion between DVI and the DVI Text Language (DTL).</dd>
<dt>
</dt><dd> 3) The program <code>dvispc</code> (part of DVIOUT previewer) also has an ability to convert between DVI and text.</dd></dl>
<p> Among those, <code>DVIasm</code> is designed to allow users to edit DVI files easily, for example by unifying &#8220;right1&#8221;-&#8220;right4&#8221; to a single command &#8220;right&#8221; which can be used regardless of the amount of move.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> Show program&#8217;s version number and exit.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Show this help message and exit.</dd>
<dt><code>-u</code> &lt;<i>STR</i>&gt;, <code>&#8211;unit=</code>&lt;<i>STR</i>&gt;</dt>
<dd> Set unit [default: `pt&#8217;]. Allowed values are: `sp&#8217;, `pt&#8217;, `bp&#8217;, `mm&#8217;, `cm&#8217; and `in&#8217;.</dd>
<dt><code>-o</code> &lt;<i>FILE</i>&gt;, <code>&#8211;output=</code>&lt;<i>FILE</i>&gt;</dt>
<dd> Set filename for output instead of stdout.</dd>
<dt><code>-e</code> &lt;<i>STR</i>&gt;, <code>&#8211;encoding=</code>&lt;<i>STR</i>&gt;</dt>
<dd> Set encoding for input/output of dumped text [default: `utf8&#8242;]. Allowed values are: `ascii&#8217;, `latin1&#8242;, `utf8&#8242;, `sjis&#8217; and `eucjp&#8217;. When used with the option <code>-p</code> (or <code>&#8211;ptex</code>), allowed values are only `utf8&#8242;, `sjis&#8217; and `eucjp&#8217;.</dd>
<dl>
<dt>
</dt><dd> # NOTE: This feature does not support dumping through stdout.</dd></dl>
<dt><code>-x</code> &lt;<i>STR</i>&gt;, <code>&#8211;xxx-encoding=</code>&lt;<i>STR</i>&gt;</dt>
<dd> Set encoding for interpreting `xxx:&#8217; strings [default: `none&#8217;]. Allowed values are: `none&#8217;, `utf8&#8242;, `sjis&#8217; and `eucjp&#8217;.</dd>
<dl>
<dt>
</dt><dd> This option allows users to specify the correct encoding for dumping/compiling the contents of \special.</dd>
<dl>
<dt>Typical usages are as follows:</dt>
<dd>
</dd><dt>
</dt><dd> 1) By default, the contents of \special are dumped/compiled as byte-to-byte escape sequences in `\x..&#8216; format. This would suffice when you don&#8217;t need to read/edit the contents of \special.  </dd>
<dd>  3) For XeTeX and upTeX users, `<code>-x utf8</code>&#8216; would be useful since these engines use UTF-8 to encode strings inside \special commands.  </dd>
<dd>  2) For pTeX users with ISO-2022-JP-encoded DVI, it would be helpful to select the appropriate option `<code>-x eucjp</code>&#8216; (for Unix) or `<code>-x sjis</code>&#8216; (for Windows) to be consistent with the internal Kanji encoding used by pTeX engine.  </dd></dl>
 </dl>
 <dt><code>-t</code> &lt;<i>INT</i>&gt;, <code>--tabsize=</code>&lt;<i>INT</i>&gt;</dt>
<dd>  Set tab size for push/pop [default: 2].  </dd>
<dt><code>-p</code>, <code>--ptex</code></dt>
<dd>  Dump and compile ISO-2022-JP-encoded DVI for Japanese pTeX. This option is required to decode or encode Japanese characters being typeset (using `set2&#8217; or `put2&#8217;) properly.  </dd>
<dt><code>-s</code> &lt;<i>STR</i>&gt;, <code>--subfont=</code>&lt;<i>STR</i>&gt;</dt>
<dd>  Specify the list of fonts with UCS2 subfont scheme in the comma-separated format. If &lt;<i>STR</i>&gt; is empty, the pre-defined internal subfont list is disabled.  </dd>
<dl>
<dd>  This option would be useful for example when using CJK package.  </dd></dl>
 </dl>
  <h2>EXAMPLE</h2>
 Documentation of <code>DVIasm</code> by the original author Jin-Hwan Cho is published as: <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<a rel="nofollow" href="http://tug.org/TUGboat/Articles/tb28-2/tb89cho.pdf">http://tug.org/TUGboat/Articles/tb28-2/tb89cho.pdf</a>&nbsp;(TUGboat) <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<a rel="nofollow" href="http://ajt.ktug.kr/assets/2008/5/1/0201cho.pdf">http://ajt.ktug.kr/assets/2008/5/1/0201cho.pdf</a>&nbsp;(Asian Journal of TeX)  <h2>AUTHORS</h2>
 The first version was written in Python 2 by Jin-Hwan Cho in 2007. Khaled Hosny started to support dumping/compiling XeTeX XDV format in 2014. Arthur Reutenauer ported the script to Python 3 in 2019. Current maintainer of <code>DVIasm</code> is Hironobu Yamashita, since 2020.  <h2>BUG REPORT</h2>
 Please visit the GitHub repository &lt;<a rel="nofollow" href="https://github.com/aminophen/dviasm">https://github.com/aminophen/dviasm</a>&gt;.  <h2>SEE ALSO</h2>
 <code><a href="/docs/linux/man/1-dvitype/">dvitype</a></code>(1), <code><a href="/docs/linux/man/1-dv2dt/">dv2dt</a></code>(1), <code><a href="/docs/linux/man/1-dt2dv/">dt2dv</a></code>(1), <code><a href="/docs/linux/man/1-dvispc/">dvispc</a></code>(1). 
