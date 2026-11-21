---
title: "dv2dt(1)"
name: "dv2dt"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dv2dt/"
description: "dv2dt – convert a binary TeX DVI file to DTL text representation"
---
<h2 class="name">NAME</h2>
<p> dv2dt - convert a binary TeX DVI file to DTL text representation </p>
<h2>SYNOPSIS</h2>
<p> <code>dv2dt</code> <i>input-DVI-file</i> <i>output-DTL-file</i> </p>
<p> If the filenames are omitted, then <i>stdin</i> and <i>stdout</i> are assumed.  </p>
<h2>DESCRIPTION</h2>
<p> <code>dv2dt</code> converts a binary TeX DVI file to an editable text file in DTL (<i>DVI Text Language</i>) format. The companion <code><a href="/docs/linux/man/1-dt2dv/">dt2dv</a></code>(1) utility can convert the DTL file back to a binary DVI file.  </p>
<h2>DVI COMMAND DESCRIPTION</h2>
<p> TeX DVI files contain a compact binary description of typeset pages, as a stream of operation code bytes, each immediately followed by zero or more parameter bytes. The format of DVI files is fully described in Donald E. Knuth, <i>TeX: The Program</i>, Addison-Wesley (1986), ISBN 0-201-13437-3, as well as in the <code><a href="/docs/linux/man/1-dvitype/">dvitype</a></code>(1) literate program source code. </p>
<p> For convenience, we provide a summary of DVI commands here. In the following list, operation code bytes are given as unsigned decimal values, followed by their symbolic names (not present in the DVI file), and a short description. A designation like <i>b[+n]</i> means that the operation code byte is followed by a parameter <i>b</i> which uses <i>n</i> bytes, and is signed. Without the plus sign, the parameter is unsigned. Signed integer parameter values are always represented in two&#8217;s complement arithmetic, which is the system followed by most computers manufactured today, including all personal computers and workstations. </p>
<dl>
<dd> <p> <i>0 set_char_0</i> Set character 0 from current font. </p>
 </dd>
<dt><i>...</i></dt>
<dd>  </dd>
<dt><i>127 set_char_127</i></dt>
<dd> <p> Set character 127 from current font. </p>
 </dd>
<dt><i>128 set1 c[1]</i></dt>
<dd> <p> Set 1-byte unsigned character (uchar) number <i>c</i>. </p>
 </dd>
<dt><i>129 set2 c[2]</i></dt>
<dd> <p> Set 2-byte uchar number <i>c</i>. </p>
 </dd>
<dt><i>130 set3 c[3]</i></dt>
<dd> <p> Set 3-byte uchar number <i>c</i>. </p>
 </dd>
<dt><i>131 set4 c[+4]</i></dt>
<dd> <p> Set 4-byte signed character (schar) number <i>c</i>. </p>
 </dd>
<dt><i>132 set_rule a[+4] b[+4]</i></dt>
<dd> <p> Set rule, height <i>a</i>, width <i>b</i>. </p>
 </dd>
<dt><i>133 put1 c[1]</i></dt>
<dd> <p> Put 1-byte uchar <i>c</i>. </p>
 </dd>
<dt><i>134 put2 c[2]</i></dt>
<dd> <p> Put 2-byte uchar <i>c</i>. </p>
 </dd>
<dt><i>135 put3 c[3]</i></dt>
<dd> <p> Put 3-byte uchar <i>c</i>. </p>
 </dd>
<dt><i>136 put4 c[+4]</i></dt>
<dd> <p> Put 4-byte schar <i>c</i>. </p>
 </dd>
<dt><i>137 put_rule a[+4] b[+4]</i></dt>
<dd> <p> Put rule, height <i>a</i>, width <i>b</i>. </p>
 </dd>
<dt><i>138 nop</i></dt>
<dd> <p> Do nothing. </p>
 </dd>
<dt><i>139 bop c0[+4] ... c9[+4] p[+4]</i></dt>
<dd> <p> Beginning of page. The parameters <i>c0 ... c9</i> are the TeX page counters, the contents of TeX count registers <i>\count0 ... \count9</i>. The parameter <i>p</i> is the byte offset from the beginning of the DVI file of the previous <i>bop</i> operation code byte. The first such command in the file has <i>p = -1</i>. </p>
 </dd>
<dt><i>140 eop</i></dt>
<dd> <p> End of page. </p>
 </dd>
<dt><i>141 push</i></dt>
<dd> <p> Push (<i>h,v,w,x,y,z</i>) onto stack. </p>
 </dd>
<dt><i>142 pop</i></dt>
<dd> <p> Pop (<i>h,v,w,x,y,z</i>) from stack. </p>
 </dd>
<dt><i>143 right1 b[+1]</i></dt>
<dd> <p> Move right <i>b</i> units. </p>
 </dd>
<dt><i>144 right2 b[+2]</i></dt>
<dd> <p> Move right <i>b</i> units. </p>
 </dd>
<dt><i>145 right3 b[+3]</i></dt>
<dd> <p> Move right <i>b</i> units. </p>
 </dd>
<dt><i>146 right4 b[+4]</i></dt>
<dd> <p> Move right <i>b</i> units. </p>
 </dd>
<dt><i>147 w0</i></dt>
<dd> <p> Move right <i>w</i> units. </p>
 </dd>
<dt><i>148 w1 b[+1]</i></dt>
<dd> <p> Move right <i>b</i> units, and set <i>w = b</i>. </p>
 </dd>
<dt><i>149 w2 b[+2]</i></dt>
<dd> <p> Move right <i>b</i> units, and set <i>w = b</i>. </p>
 </dd>
<dt><i>150 w3 b[+3]</i></dt>
<dd> <p> Move right <i>b</i> units, and set <i>w = b</i>. </p>
 </dd>
<dt><i>151 w4 b[+4]</i></dt>
<dd> <p> Move right <i>b</i> units, and set <i>w = b</i>. </p>
 </dd>
<dt><i>152 x0</i></dt>
<dd> <p> Move right <i>x</i> units. </p>
 </dd>
<dt><i>153 x1 b[+1]</i></dt>
<dd> <p> Move right <i>b</i> units, and set <i>x = b</i>. </p>
 </dd>
<dt><i>154 x2 b[+2]</i></dt>
<dd> <p> Move right <i>b</i> units, and set <i>x = b</i>. </p>
 </dd>
<dt><i>155 x3 b[+3]</i></dt>
<dd> <p> Move right <i>b</i> units, and set <i>x = b</i>. </p>
 </dd>
<dt><i>156 x4 b[+4]</i></dt>
<dd> <p> Move right <i>b</i> units, and set <i>x = b</i>. </p>
 </dd>
<dt><i>157 down1 a[+1]</i></dt>
<dd> <p> Move down <i>a</i> units. </p>
 </dd>
<dt><i>158 down2 a[+2]</i></dt>
<dd> <p> Move down <i>a</i> units. </p>
 </dd>
<dt><i>159 down3 a[+3]</i></dt>
<dd> <p> Move down <i>a</i> units. </p>
 </dd>
<dt><i>160 down4 a[+4]</i></dt>
<dd> <p> Move down <i>a</i> units. </p>
 </dd>
<dt><i>161 y0</i></dt>
<dd> <p> Move right <i>y</i> units. </p>
 </dd>
<dt><i>162 y1 a[+1]</i></dt>
<dd> <p> Move right <i>a</i> units, and set <i>y = a</i>. </p>
 </dd>
<dt><i>163 y2 a[+2]</i></dt>
<dd> <p> Move right <i>a</i> units, and set <i>y = a</i>. </p>
 </dd>
<dt><i>164 y3 a[+3]</i></dt>
<dd> <p> Move right <i>a</i> units, and set <i>y = a</i>. </p>
 </dd>
<dt><i>165 y4 a[+4]</i></dt>
<dd> <p> Move right <i>a</i> units, and set <i>y = a</i>. </p>
 </dd>
<dt><i>166 z0</i></dt>
<dd> <p> Move right <i>z</i> units. </p>
 </dd>
<dt><i>167 z1 a[+1]</i></dt>
<dd> <p> Move right <i>a</i> units, and set <i>z = a</i>. </p>
 </dd>
<dt><i>168 z2 a[+2]</i></dt>
<dd> <p> Move right <i>a</i> units, and set <i>z = a</i>. </p>
 </dd>
<dt><i>169 z3 a[+3]</i></dt>
<dd> <p> Move right <i>a</i> units, and set <i>z = a</i>. </p>
 </dd>
<dt><i>170 z4 a[+4]</i></dt>
<dd> <p> Move right <i>a</i> units, and set <i>z = a</i>. </p>
 </dd>
<dt><i>171 fnt_num_0</i></dt>
<dd> <p> Set current font number <i>(f) = 0</i>. </p>
 </dd>
<dt><i>...</i></dt>
<dd>  </dd>
<dt><i>234 fnt_num_63</i></dt>
<dd> <p> Set <i>f = 63</i>. </p>
 </dd>
<dt><i>235 fnt1 k[1]</i></dt>
<dd> <p> Set <i>f = k</i>. </p>
 </dd>
<dt><i>236 fnt2 k[2]</i></dt>
<dd> <p> Set <i>f = k</i>. </p>
 </dd>
<dt><i>237 fnt3 k[3]</i></dt>
<dd> <p> Set <i>f = k</i>. </p>
 </dd>
<dt><i>238 fnt4 k[+4]</i></dt>
<dd> <p> Set <i>f = k</i>. </p>
 </dd>
<dt><i>239 xxx1 k[1] x[k]</i></dt>
<dd> <p> Special string <i>x</i> with <i>k</i> bytes. </p>
 </dd>
<dt><i>240 xxx2 k[2] x[k]</i></dt>
<dd> <p> Special string <i>x</i> with <i>k</i> bytes. </p>
 </dd>
<dt><i>241 xxx3 k[3] x[k]</i></dt>
<dd> <p> Special string <i>x</i> with <i>k</i> bytes. </p>
 </dd>
<dt><i>242 xxx4 k[4] x[k]</i></dt>
<dd> <p> Special string <i>x</i> with (unsigned) <i>k</i> bytes. </p>
 </dd>
<dt><i>243 fnt_def1 k[1] c[4] s[4] d[4] a[1] l[1] n[a+l]</i></dt>
<dd> <p> Define font <i>k</i>. The parameters are: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><i>c</i></dt>
<dd> <p> Checksum for TFM file. </p>
 </dd>
<dt><i>s</i></dt>
<dd> <p> Scale factor, in DVI units. </p>
 </dd>
<dt><i>d</i></dt>
<dd> <p> Design size, in DVI units. </p>
 </dd>
<dt><i>a</i></dt>
<dd> <p> Length of the ``area&#8217;&#8216; or directory. </p>
 </dd>
<dt><i>l</i></dt>
<dd> <p> Length of the font name. </p>
 </dd>
<dt><i>n</i></dt>
<dd> <p> Area and font name string(s). </p>
 </dd></dl>
</dl>
<dt><i>244 fnt_def2 k[2] c[4] s[4] d[4] a[1] l[1] n[a+l]</i></dt>
<dd> <p> Define font <i>k</i>. </p>
 </dd>
<dt><i>245 fnt_def3 k[3] c[4] s[4] d[4] a[1] l[1] n[a+l]</i></dt>
<dd> <p> Define font <i>k</i>. </p>
 </dd>
<dt><i>246 fnt_def4 k[+4] c[4] s[4] d[4] a[1] l[1] n[a+l]</i></dt>
<dd> <p> Define font <i>k</i>. </p>
 </dd>
<dt><i>247 pre i[1] num[4] den[4] mag[4] k[1] x[k]</i></dt>
<dd> <p> Begin preamble. The parameters are: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><i>i</i></dt>
<dd> <p> DVI format. Standard TeX has <i>ID = 2</i>, and TeX-XeT has <i>ID = 3</i>. </p>
 </dd>
<dt><i>num</i></dt>
<dd> <p> Numerator of 100 nm / DVI unit. </p>
 </dd>
<dt><i>den</i></dt>
<dd> <p> Denominator of 100 nm / DVI unit. </p>
 </dd>
<dt><i>mag</i></dt>
<dd> <p> 1000 * magnification. </p>
 </dd>
<dt><i>k</i></dt>
<dd> <p> Comment length. </p>
 </dd>
<dt><i>x</i></dt>
<dd> <p> Comment string. </p>
 </dd></dl>
</dl>
<dt><i>248 post p[4] num[4] den[4] mag[4] l[4] u[4] s[2] t[2]</i></dt>
<dd> <p> Begin postamble. The parameters are: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><i>p</i></dt>
<dd> <p> Pointer to final bop. </p>
 </dd>
<dt><i>num, den, mag</i></dt>
<dd> <p> Duplicates of values in preamble. </p>
 </dd>
<dt><i>l</i></dt>
<dd> <p> Height-plus-depth of tallest page, in DVI units. </p>
 </dd>
<dt><i>u</i></dt>
<dd> <p> Width of widest page, in DVI units. </p>
 </dd>
<dt><i>s</i></dt>
<dd> <p> Maximum stack depth needed to process this DVI file. </p>
 </dd>
<dt><i>t</i></dt>
<dd> <p> Total number of pages (<i>bop</i> commands) present. </p>
 </dd></dl>
</dl>
<dt><i>249 post_post q[4] i[1] 223 ... 223</i></dt>
<dd> <p> End postamble. The parameters are: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><i>q</i></dt>
<dd> <p> Byte offset from the beginning of the DVI file to the <i>post</i> command that started the postamble. </p>
 </dd>
<dt><i>i</i></dt>
<dd> <p> DVI format ID, as in the preamble. </p>
 </dd>
<dt><i>223</i></dt>
<dd> <p> At least four <i>223</i> bytes. </p>
 </dd></dl>
</dl>
<dt><i>250</i></dt>
<dd> <p> Undefined. </p>
 </dd>
<dt><i>...</i></dt>
<dd>  </dd>
<dt><i>255</i></dt>
<dd> <p> Undefined. </p>
 </dd></dl>
<h2>DTL COMMAND DESCRIPTION</h2>
<p> A DTL file contains one line per command, with a limit of 1024 characters per line. Each command contains a symbolic operation name, followed by zero or more parameter values. The parameter value descriptions are not repeated here; they can be found in the previous section. </p>
<dl>
<dt>variety &lt;variety-name&gt;</dt>
<dd> <p> This command specifies the name of the DTL file type; it has no DVI file equivalent. </p>
 </dd>
<dt><i>(text)</i></dt>
<dd> <p> Series of set_char commands, for printable ASCII text. </p>
 </dd>
<dt><i>\(</i></dt>
<dd> <p> Literal ASCII left parenthesis in (text). </p>
 </dd>
<dt><i>\)</i></dt>
<dd> <p> Literal ASCII right parenthesis in (text). </p>
 </dd>
<dt><i>\\</i></dt>
<dd> <p> Literal ASCII backslash in (text). </p>
 </dd>
<dt><i>\</i></dt>
<dd> <p> Literal ASCII double quote in (text). </p>
 </dd>
<dt><i>\XY</i></dt>
<dd> <p> Set_char for character with hexadecimal code XY, not in parentheses, but by itself for readability. </p>
 </dd>
<dt><i>s1, s2, s2, s3</i></dt>
<dd> <p> Set, with (1,2,3,4)-byte charcodes. </p>
 </dd>
<dt><i>sr</i></dt>
<dd> <p> <i>set_rule</i>. </p>
 </dd>
<dt><i>p1, p2, p2, p3</i></dt>
<dd> <p> Put, with (1,2,3,4)-byte charcodes. </p>
 </dd>
<dt><i>pr</i></dt>
<dd> <p> <i>put_rule</i>. </p>
 </dd>
<dt><i>nop</i></dt>
<dd> <p> <i>nop</i> (do nothing). </p>
 </dd>
<dt><i>bop</i></dt>
<dd> <p> <i>bop</i> (beginning of page). </p>
 </dd>
<dt><i>eop</i></dt>
<dd> <p> <i>eop</i> (end of page). </p>
 </dd>
<dt><i>[</i></dt>
<dd> <p> Push. </p>
 </dd>
<dt><i>]</i></dt>
<dd> <p> Pop. </p>
 </dd>
<dt><i>r1, r2, r3, r4</i></dt>
<dd> <p> Right, with (1,2,3,4)-byte argument. </p>
 </dd>
<dt><i>w0, w1, w2, w3, w4</i></dt>
<dd> <p> As in DVI. </p>
 </dd>
<dt><i>x0, x1, x2, x3, x4</i></dt>
<dd> <p> As in DVI. </p>
 </dd>
<dt><i>d1, d2, d3, d4</i></dt>
<dd> <p> Down, with (1,2,3,4)-byte argument. </p>
 </dd>
<dt><i>y0, y1, y2, y3, y4</i></dt>
<dd> <p> As in DVI. </p>
 </dd>
<dt><i>z0, z1, z2, z3, z4</i></dt>
<dd> <p> As in DVI. </p>
 </dd>
<dt><i>fn</i></dt>
<dd> <p> <i>fnt_num</i> (set current font to font number in 0 to 63). </p>
 </dd>
<dt><i>f1, f2, f3, f4</i></dt>
<dd> <p> <i>fnt</i> (set current font to (1,2,3,4)-byte font number). </p>
 </dd>
<dt><i>special</i></dt>
<dd> <p> <i>xxx</i> (special commands with (1,2,3,4)-byte string length). </p>
 </dd>
<dt><i>fd</i></dt>
<dd> <p> <i>fnt_def</i> (assign a number to a named font). </p>
 </dd>
<dt><i>pre</i></dt>
<dd> <p> Preamble. </p>
 </dd>
<dt><i>post</i></dt>
<dd> <p> <i>post</i> (begin postamble). </p>
 </dd>
<dt><i>post_post</i></dt>
<dd> <p> <i>post_post</i> (end postamble). </p>
 </dd>
<dt><i>opcode</i></dt>
<dd> <p> Undefined DVI command (250 to 255). </p>
 </dd></dl>
<h2>SAMPLE DTL FILE</h2>
<p> The following 2-line TeX file </p>
<dl>
<dd> <pre><code>Hello.
\bye
</code></pre>
 </dd></dl>
<p> when processed with the commands </p>
<dl>
<dd> <pre><code>tex hello.tex
dv2dt hello.dvi hello.dtl
</code></pre>
 </dd></dl>
<p> produces this DTL file: </p>
<dl>
<dd> <pre><code>variety sequences-6
pre 2 25400000 473628672 1000 27 ' TeX output 1995.03.02:2334'
bop 1 0 0 0 0 0 0 0 0 0 -1
[
d3 -917504
]
d4 42152922
[
d4 -41497562
[
r3 1310720
fd1 0 11374260171 655360 655360 0 5 '' 'cmr10'
fn0
(Hello.)
]
]
d3 1572864
[
r4 15229091
(1)
]
eop
post 42 25400000 473628672 1000 43725786 30785863 2 1
fd1 0 11374260171 655360 655360 0 5 'cmr10'
post_post 152 2 223 223 223 223
</code></pre>
 </dd></dl>
<p> The command </p>
<dl>
<dd> <pre><code>dt2dv hello.dtl hello.dvi
</code></pre>
 </dd></dl>
<p> will reconstruct the original DVI file.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dt2dv/">dt2dv</a></code>(1), <code><a href="/docs/linux/man/1-dvitype/">dvitype</a></code>(1), <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1).  </p>
<h2>FILES</h2>
<dl>
<dt><i>*.dvi</i></dt>
<dd> <p> binary TeX DVI file. </p>
 </dd>
<dt><i>*.dtl</i></dt>
<dd> <p> text representation of a TeX DVI file in <i>DVI Text Language</i> format. </p>
 </dd></dl>
<h2>AUTHOR</h2>
<p> <code>dv2dt</code> and <code><a href="/docs/linux/man/1-dt2dv/">dt2dv</a></code>(1) were written by </p>
<dl>
<dd> <pre><code>Geoffrey Tobin
Department of Electronic Engineering
La Trobe University
Bundoora, Victoria 3083
Australia
Tel: +61 3 479 3736
FAX: +61 3 479 3025
Email: &lt;G.Tobin [at] ee.latrobe.edu.au&gt;
</code></pre>
 </dd></dl>
<p> These manual pages were primarily written by </p>
<dl>
<dd> <pre><code>Nelson H. F. Beebe, Ph.D.
Center for Scientific Computing
Department of Mathematics
University of Utah
Salt Lake City, UT 84112
Tel: +1 801 581 5254
FAX: +1 801 581 4148
Email: &lt;beebe [at] math.utah.edu&gt;
</code></pre>
 </dd></dl>
