---
title: "gmtcolors(5)"
name: "gmtcolors"
section: "5"
letter: "g"
url: "/docs/linux/man/5-gmtcolors/"
description: "gmtcolors – Explanation of color codes in GMT"
---

<p>gmtcolors &#8211; Explanation of color codes in GMT</p>
<h2>Description</h2>
<p>Colors can be specified in GMT as arguments to commands, generally as part of the <code>-G</code> or <code>-W</code> options to select polygon fill or outline pen. Colors are also used in color palette tables (CPT files) that help convert numerical values to colors. </p>
<p> GMT allows several ways to represent a color:</p>
<dl>
<dt><code>Colorname</code></p>
<dd>Specify one of the named colors below. All names are case-insensitive.</p>
<dt><code>R/G/B</code></p>
<dd>Specify <code>R</code>ed, <code>G</code>reen, and <code>B</code>lue levels. Each value is separated by a slash and is in the range from 0 (dark) to 255 (light). This representation is used to color monitors.</p>
<dt><code>#RRGGBB</code></p>
<dd>Specify <code>R</code>ed, <code>G</code>reen, and <code>B</code>lue levels in the way that it is done in HTML. Use two characters for each color channel, ranging from 00 (dark) to FF (light). Upper and lower case are allowed.</p>
<dt><code>Graylevel</code></p>
<dd>For shades of gray, R = G = B, and only one number needs to be used. This representation is popular with black and white printers.</p>
<dt><code>H-S-V</code></p>
<dd>Specify <code>H</code>ue in the range 0 to 360 (degrees), <code>S</code> saturation between 0 (not saturated) and 1 (fully saturated), and value <code>V</code> between 0 (dark) and 1 (light). Number are separated by hyphens. This representation can be helpful when hue varies a lot.</p>
<dt><code>C/M/Y/K</code></p>
<dd>Specify <code>C</code>yan, <code>M</code>agenta, <code>Y</code>ellow, and blacBD(K). Each number is in the range from 0 (no paint) to 1 (maximum paint). This representation is used by most color printers.</dl>
<h2>List Of Colors</h2>
<p>The following list contains the named colors that can be used in GMT and their equivalent color codes. <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>R</i> </td>
<td> <i>G</i> </td>
<td> <i>B</i> </td>
<td> <i>Name</i>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 250 </td>
<td> 250 </td>
<td> snow
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 248 </td>
<td> 248 </td>
<td> 255 </td>
<td> ghostwite
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 250 </td>
<td> 240 </td>
<td> floralwhite
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 245 </td>
<td> 238 </td>
<td> seashell
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 253 </td>
<td> 245 </td>
<td> 230 </td>
<td> oldlace
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 250 </td>
<td> 240 </td>
<td> 230 </td>
<td> linen
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 250 </td>
<td> 235 </td>
<td> 215 </td>
<td> antiquewhite
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 239 </td>
<td> 213 </td>
<td> papayawhip
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 235 </td>
<td> 205 </td>
<td> blanchedalmond
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 228 </td>
<td> 196 </td>
<td> bisque
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 218 </td>
<td> 185 </td>
<td> peachpuff
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 222 </td>
<td> 173 </td>
<td> navajowhite
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 228 </td>
<td> 181 </td>
<td> moccasin
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 250 </td>
<td> 205 </td>
<td> lemonchiffon
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 248 </td>
<td> 220 </td>
<td> cornsilk
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 255 </td>
<td> 240 </td>
<td> ivory
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 240 </td>
<td> 255 </td>
<td> 240 </td>
<td> honeydew
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 245 </td>
<td> 255 </td>
<td> 250 </td>
<td> mintcream
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 240 </td>
<td> 255 </td>
<td> 255 </td>
<td> azure
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 240 </td>
<td> 248 </td>
<td> 255 </td>
<td> aliceblue
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 230 </td>
<td> 230 </td>
<td> 250 </td>
<td> lavender
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 240 </td>
<td> 245 </td>
<td> lavenderblush
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 228 </td>
<td> 225 </td>
<td> mistyrose
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 100 </td>
<td> 149 </td>
<td> 237 </td>
<td> cornflowerblue
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 106 </td>
<td> 90 </td>
<td> 205 </td>
<td> slateblue
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 123 </td>
<td> 104 </td>
<td> 238 </td>
<td> mediumslateblue
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 132 </td>
<td> 112 </td>
<td> 255 </td>
<td> lightslateblue
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 135 </td>
<td> 206 </td>
<td> 235 </td>
<td> skyblue
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 135 </td>
<td> 206 </td>
<td> 250 </td>
<td> lightskyblue
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 119 </td>
<td> 136 </td>
<td> 153 </td>
<td> lightslategray
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 119 </td>
<td> 136 </td>
<td> 153 </td>
<td> lightslategrey
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 112 </td>
<td> 128 </td>
<td> 144 </td>
<td> slategray
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 112 </td>
<td> 128 </td>
<td> 144 </td>
<td> slategrey
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 176 </td>
<td> 196 </td>
<td> 222 </td>
<td> lightsteelblue
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 173 </td>
<td> 216 </td>
<td> 230 </td>
<td> lightblue
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 224 </td>
<td> 255 </td>
<td> 255 </td>
<td> lightcyan
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 176 </td>
<td> 224 </td>
<td> 230 </td>
<td> powderblue
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 175 </td>
<td> 238 </td>
<td> 238 </td>
<td> paleturquoise
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 102 </td>
<td> 205 </td>
<td> 170 </td>
<td> mediumaquamarine
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 127 </td>
<td> 255 </td>
<td> 212 </td>
<td> aquamarine
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 144 </td>
<td> 238 </td>
<td> 144 </td>
<td> lightgreen
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 143 </td>
<td> 188 </td>
<td> 143 </td>
<td> darkseagreen
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 152 </td>
<td> 251 </td>
<td> 152 </td>
<td> palegreen
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 124 </td>
<td> 252 </td>
<td> 0 </td>
<td> lawngreen
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 127 </td>
<td> 255 </td>
<td> 0 </td>
<td> chartreuse
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 173 </td>
<td> 255 </td>
<td> 47 </td>
<td> greenyellow
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 154 </td>
<td> 205 </td>
<td> 50 </td>
<td> yellowgreen
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 107 </td>
<td> 142 </td>
<td> 35 </td>
<td> olivedrab
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 189 </td>
<td> 183 </td>
<td> 107 </td>
<td> darkkhaki
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 240 </td>
<td> 230 </td>
<td> 140 </td>
<td> khaki
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 232 </td>
<td> 170 </td>
<td> palegoldenrod
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 221 </td>
<td> 130 </td>
<td> lightgoldenrod
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 255 </td>
<td> 224 </td>
<td> lightyellow
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 250 </td>
<td> 250 </td>
<td> 210 </td>
<td> lightgoldenrodyellow
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 255 </td>
<td> 0 </td>
<td> yellow
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 128 </td>
<td> 128 </td>
<td> 0 </td>
<td> darkyellow
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 215 </td>
<td> 0 </td>
<td> gold
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 218 </td>
<td> 165 </td>
<td> 32 </td>
<td> goldenrod
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 184 </td>
<td> 134 </td>
<td> 11 </td>
<td> darkgoldenrod
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 188 </td>
<td> 143 </td>
<td> 143 </td>
<td> rosybrown
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 92 </td>
<td> 92 </td>
<td> indianred
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 69 </td>
<td> 19 </td>
<td> saddlebrown
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 160 </td>
<td> 82 </td>
<td> 45 </td>
<td> sienna
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 133 </td>
<td> 63 </td>
<td> peru
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 222 </td>
<td> 184 </td>
<td> 135 </td>
<td> burlywood
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 245 </td>
<td> 245 </td>
<td> 220 </td>
<td> beige
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 245 </td>
<td> 222 </td>
<td> 179 </td>
<td> wheat
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 244 </td>
<td> 164 </td>
<td> 96 </td>
<td> sandybrown
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 210 </td>
<td> 180 </td>
<td> 140 </td>
<td> tan
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 210 </td>
<td> 105 </td>
<td> 30 </td>
<td> chocolate
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 178 </td>
<td> 34 </td>
<td> 34 </td>
<td> firebrick
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 235 </td>
<td> 190 </td>
<td> 85 </td>
<td> lightbrown
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 165 </td>
<td> 42 </td>
<td> 42 </td>
<td> brown
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 120 </td>
<td> 60 </td>
<td> 30 </td>
<td> darkbrown
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 233 </td>
<td> 150 </td>
<td> 122 </td>
<td> darksalmon
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 250 </td>
<td> 128 </td>
<td> 114 </td>
<td> salmon
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 160 </td>
<td> 122 </td>
<td> lightsalmon
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 192 </td>
<td> 128 </td>
<td> lightorange
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 165 </td>
<td> 0 </td>
<td> orange
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 140 </td>
<td> 0 </td>
<td> darkorange
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 127 </td>
<td> 80 </td>
<td> coral
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 240 </td>
<td> 128 </td>
<td> 128 </td>
<td> lightcoral
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 99 </td>
<td> 71 </td>
<td> tomato
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 69 </td>
<td> 0 </td>
<td> orangered
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 0 </td>
<td> 0 </td>
<td> red
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 128 </td>
<td> 128 </td>
<td> lightred
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 0 </td>
<td> 0 </td>
<td> darkred
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 20 </td>
<td> 147 </td>
<td> deeppink
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 105 </td>
<td> 180 </td>
<td> hotpink
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 192 </td>
<td> 203 </td>
<td> pink
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 182 </td>
<td> 193 </td>
<td> lightpink
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 219 </td>
<td> 112 </td>
<td> 147 </td>
<td> palevioletred
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 176 </td>
<td> 48 </td>
<td> 96 </td>
<td> maroon
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 199 </td>
<td> 21 </td>
<td> 133 </td>
<td> mediumvioletred
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 208 </td>
<td> 32 </td>
<td> 144 </td>
<td> violetred
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 0 </td>
<td> 139 </td>
<td> darkmagenta
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 0 </td>
<td> 255 </td>
<td> magenta
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 128 </td>
<td> 255 </td>
<td> lightmagenta
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 130 </td>
<td> 238 </td>
<td> violet
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 218 </td>
<td> 112 </td>
<td> 214 </td>
<td> orchid
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 221 </td>
<td> 160 </td>
<td> 221 </td>
<td> plum
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 186 </td>
<td> 85 </td>
<td> 211 </td>
<td> mediumorchid
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 153 </td>
<td> 50 </td>
<td> 204 </td>
<td> darkorchid
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 148 </td>
<td> 0 </td>
<td> 211 </td>
<td> darkviolet
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 138 </td>
<td> 43 </td>
<td> 226 </td>
<td> blueviolet
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 160 </td>
<td> 32 </td>
<td> 240 </td>
<td> purple
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 147 </td>
<td> 112 </td>
<td> 219 </td>
<td> mediumpurple
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 216 </td>
<td> 191 </td>
<td> 216 </td>
<td> thistle
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 105 </td>
<td> 105 </td>
<td> 105 </td>
<td> dimgray
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 105 </td>
<td> 105 </td>
<td> 105 </td>
<td> dimgrey
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 169 </td>
<td> 169 </td>
<td> 169 </td>
<td> darkgray
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 169 </td>
<td> 169 </td>
<td> 169 </td>
<td> darkgrey
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 190 </td>
<td> 190 </td>
<td> 190 </td>
<td> gray
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 190 </td>
<td> 190 </td>
<td> 190 </td>
<td> grey
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 211 </td>
<td> 211 </td>
<td> 211 </td>
<td> lightgrey
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 211 </td>
<td> 211 </td>
<td> 211 </td>
<td> lightgray
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 220 </td>
<td> 220 </td>
<td> 220 </td>
<td> gainsboro
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 245 </td>
<td> 245 </td>
<td> 245 </td>
<td> whitesmoke
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 255 </td>
<td> 255 </td>
<td> white
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 250 </td>
<td> 250 </td>
<td> snow1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 233 </td>
<td> 233 </td>
<td> snow2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 201 </td>
<td> 201 </td>
<td> snow3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 137 </td>
<td> 137 </td>
<td> snow4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 245 </td>
<td> 238 </td>
<td> seashell1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 229 </td>
<td> 222 </td>
<td> seashell2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 197 </td>
<td> 191 </td>
<td> seashell3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 134 </td>
<td> 130 </td>
<td> seashell4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 239 </td>
<td> 219 </td>
<td> antiquewhite1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 223 </td>
<td> 204 </td>
<td> antiquewhite2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 192 </td>
<td> 176 </td>
<td> antiquewhite3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 131 </td>
<td> 120 </td>
<td> antiquewhite4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 228 </td>
<td> 196 </td>
<td> bisque1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 213 </td>
<td> 183 </td>
<td> bisque2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 183 </td>
<td> 158 </td>
<td> bisque3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 125 </td>
<td> 107 </td>
<td> bisque4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 218 </td>
<td> 185 </td>
<td> peachpuff1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 203 </td>
<td> 173 </td>
<td> peachpuff2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 175 </td>
<td> 149 </td>
<td> peachpuff3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 119 </td>
<td> 101 </td>
<td> peachpuff4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 222 </td>
<td> 173 </td>
<td> navajowhite1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 207 </td>
<td> 161 </td>
<td> navajowhite2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 179 </td>
<td> 139 </td>
<td> navajowhite3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 121 </td>
<td> 94 </td>
<td> navajowhite4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 250 </td>
<td> 205 </td>
<td> lemonchiffon1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 233 </td>
<td> 191 </td>
<td> lemonchiffon2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 201 </td>
<td> 165 </td>
<td> lemonchiffon3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 137 </td>
<td> 112 </td>
<td> lemonchiffon4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 248 </td>
<td> 220 </td>
<td> cornsilk1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 232 </td>
<td> 205 </td>
<td> cornsilk2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 200 </td>
<td> 177 </td>
<td> cornsilk3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 136 </td>
<td> 120 </td>
<td> cornsilk4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 255 </td>
<td> 240 </td>
<td> ivory1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 238 </td>
<td> 224 </td>
<td> ivory2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 205 </td>
<td> 193 </td>
<td> ivory3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 139 </td>
<td> 131 </td>
<td> ivory4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 240 </td>
<td> 255 </td>
<td> 240 </td>
<td> honeydew1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 224 </td>
<td> 238 </td>
<td> 224 </td>
<td> honeydew2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 193 </td>
<td> 205 </td>
<td> 193 </td>
<td> honeydew3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 131 </td>
<td> 139 </td>
<td> 131 </td>
<td> honeydew4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 240 </td>
<td> 245 </td>
<td> lavenderblush1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 224 </td>
<td> 229 </td>
<td> lavenderblush2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 193 </td>
<td> 197 </td>
<td> lavenderblush3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 131 </td>
<td> 134 </td>
<td> lavenderblush4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 228 </td>
<td> 225 </td>
<td> mistyrose1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 213 </td>
<td> 210 </td>
<td> mistyrose2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 183 </td>
<td> 181 </td>
<td> mistyrose3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 125 </td>
<td> 123 </td>
<td> mistyrose4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 240 </td>
<td> 255 </td>
<td> 255 </td>
<td> azure1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 224 </td>
<td> 238 </td>
<td> 238 </td>
<td> azure2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 193 </td>
<td> 205 </td>
<td> 205 </td>
<td> azure3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 131 </td>
<td> 139 </td>
<td> 139 </td>
<td> azure4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 131 </td>
<td> 111 </td>
<td> 255 </td>
<td> slateblue1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 122 </td>
<td> 103 </td>
<td> 238 </td>
<td> slateblue2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 105 </td>
<td> 89 </td>
<td> 205 </td>
<td> slateblue3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 135 </td>
<td> 206 </td>
<td> 255 </td>
<td> skyblue1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 126 </td>
<td> 192 </td>
<td> 238 </td>
<td> skyblue2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 108 </td>
<td> 166 </td>
<td> 205 </td>
<td> skyblue3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 176 </td>
<td> 226 </td>
<td> 255 </td>
<td> lightskyblue1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 164 </td>
<td> 211 </td>
<td> 238 </td>
<td> lightskyblue2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 141 </td>
<td> 182 </td>
<td> 205 </td>
<td> lightskyblue3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 198 </td>
<td> 226 </td>
<td> 255 </td>
<td> slategray1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 185 </td>
<td> 211 </td>
<td> 238 </td>
<td> slategray2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 159 </td>
<td> 182 </td>
<td> 205 </td>
<td> slategray3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 108 </td>
<td> 123 </td>
<td> 139 </td>
<td> slategray4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 202 </td>
<td> 225 </td>
<td> 255 </td>
<td> lightsteelblue1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 188 </td>
<td> 210 </td>
<td> 238 </td>
<td> lightsteelblue2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 162 </td>
<td> 181 </td>
<td> 205 </td>
<td> lightsteelblue3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 110 </td>
<td> 123 </td>
<td> 139 </td>
<td> lightsteelblue4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 191 </td>
<td> 239 </td>
<td> 255 </td>
<td> lightblue1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 178 </td>
<td> 223 </td>
<td> 238 </td>
<td> lightblue2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 154 </td>
<td> 192 </td>
<td> 205 </td>
<td> lightblue3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 104 </td>
<td> 131 </td>
<td> 139 </td>
<td> lightblue4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 224 </td>
<td> 255 </td>
<td> 255 </td>
<td> lightcyan1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 209 </td>
<td> 238 </td>
<td> 238 </td>
<td> lightcyan2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 180 </td>
<td> 205 </td>
<td> 205 </td>
<td> lightcyan3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 122 </td>
<td> 139 </td>
<td> 139 </td>
<td> lightcyan4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 187 </td>
<td> 255 </td>
<td> 255 </td>
<td> paleturquoise1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 174 </td>
<td> 238 </td>
<td> 238 </td>
<td> paleturquoise2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 150 </td>
<td> 205 </td>
<td> 205 </td>
<td> paleturquoise3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 102 </td>
<td> 139 </td>
<td> 139 </td>
<td> paleturquoise4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 152 </td>
<td> 245 </td>
<td> 255 </td>
<td> cadetblue1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 142 </td>
<td> 229 </td>
<td> 238 </td>
<td> cadetblue2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 122 </td>
<td> 197 </td>
<td> 205 </td>
<td> cadetblue3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 151 </td>
<td> 255 </td>
<td> 255 </td>
<td> darkslategray1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 141 </td>
<td> 238 </td>
<td> 238 </td>
<td> darkslategray2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 121 </td>
<td> 205 </td>
<td> 205 </td>
<td> darkslategray3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 127 </td>
<td> 255 </td>
<td> 212 </td>
<td> aquamarine1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 118 </td>
<td> 238 </td>
<td> 198 </td>
<td> aquamarine2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 102 </td>
<td> 205 </td>
<td> 170 </td>
<td> aquamarine3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 193 </td>
<td> 255 </td>
<td> 193 </td>
<td> darkseagreen1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 180 </td>
<td> 238 </td>
<td> 180 </td>
<td> darkseagreen2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 155 </td>
<td> 205 </td>
<td> 155 </td>
<td> darkseagreen3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 105 </td>
<td> 139 </td>
<td> 105 </td>
<td> darkseagreen4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 154 </td>
<td> 255 </td>
<td> 154 </td>
<td> palegreen1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 144 </td>
<td> 238 </td>
<td> 144 </td>
<td> palegreen2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 124 </td>
<td> 205 </td>
<td> 124 </td>
<td> palegreen3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 127 </td>
<td> 255 </td>
<td> 0 </td>
<td> chartreuse1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 118 </td>
<td> 238 </td>
<td> 0 </td>
<td> chartreuse2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 102 </td>
<td> 205 </td>
<td> 0 </td>
<td> chartreuse3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 192 </td>
<td> 255 </td>
<td> 62 </td>
<td> olivedrab1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 179 </td>
<td> 238 </td>
<td> 58 </td>
<td> olivedrab2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 154 </td>
<td> 205 </td>
<td> 50 </td>
<td> olivedrab3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 105 </td>
<td> 139 </td>
<td> 34 </td>
<td> olivedrab4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 202 </td>
<td> 255 </td>
<td> 112 </td>
<td> darkolivegreen1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 188 </td>
<td> 238 </td>
<td> 104 </td>
<td> darkolivegreen2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 162 </td>
<td> 205 </td>
<td> 90 </td>
<td> darkolivegreen3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 110 </td>
<td> 139 </td>
<td> 61 </td>
<td> darkolivegreen4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 246 </td>
<td> 143 </td>
<td> khaki1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 230 </td>
<td> 133 </td>
<td> khaki2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 198 </td>
<td> 115 </td>
<td> khaki3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 134 </td>
<td> 78 </td>
<td> khaki4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 236 </td>
<td> 139 </td>
<td> lightgoldenrod1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 220 </td>
<td> 130 </td>
<td> lightgoldenrod2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 190 </td>
<td> 112 </td>
<td> lightgoldenrod3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 129 </td>
<td> 76 </td>
<td> lightgoldenrod4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 255 </td>
<td> 224 </td>
<td> lightyellow1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 238 </td>
<td> 209 </td>
<td> lightyellow2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 205 </td>
<td> 180 </td>
<td> lightyellow3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 139 </td>
<td> 122 </td>
<td> lightyellow4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 255 </td>
<td> 0 </td>
<td> yellow1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 238 </td>
<td> 0 </td>
<td> yellow2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 205 </td>
<td> 0 </td>
<td> yellow3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 139 </td>
<td> 0 </td>
<td> yellow4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 215 </td>
<td> 0 </td>
<td> gold1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 201 </td>
<td> 0 </td>
<td> gold2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 173 </td>
<td> 0 </td>
<td> gold3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 117 </td>
<td> 0 </td>
<td> gold4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 193 </td>
<td> 37 </td>
<td> goldenrod1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 180 </td>
<td> 34 </td>
<td> goldenrod2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 155 </td>
<td> 29 </td>
<td> goldenrod3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 105 </td>
<td> 20 </td>
<td> goldenrod4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 185 </td>
<td> 15 </td>
<td> darkgoldenrod1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 173 </td>
<td> 14 </td>
<td> darkgoldenrod2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 149 </td>
<td> 12 </td>
<td> darkgoldenrod3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 101 </td>
<td> 8 </td>
<td> darkgoldenrod4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 193 </td>
<td> 193 </td>
<td> rosybrown1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 180 </td>
<td> 180 </td>
<td> rosybrown2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 155 </td>
<td> 155 </td>
<td> rosybrown3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 105 </td>
<td> 105 </td>
<td> rosybrown4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 106 </td>
<td> 106 </td>
<td> indianred1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 99 </td>
<td> 99 </td>
<td> indianred2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 85 </td>
<td> 85 </td>
<td> indianred3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 58 </td>
<td> 58 </td>
<td> indianred4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 130 </td>
<td> 71 </td>
<td> sienna1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 121 </td>
<td> 66 </td>
<td> sienna2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 104 </td>
<td> 57 </td>
<td> sienna3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 71 </td>
<td> 38 </td>
<td> sienna4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 211 </td>
<td> 155 </td>
<td> burlywood1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 197 </td>
<td> 145 </td>
<td> burlywood2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 170 </td>
<td> 125 </td>
<td> burlywood3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 115 </td>
<td> 85 </td>
<td> burlywood4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 231 </td>
<td> 186 </td>
<td> wheat1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 216 </td>
<td> 174 </td>
<td> wheat2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 186 </td>
<td> 150 </td>
<td> wheat3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 126 </td>
<td> 102 </td>
<td> wheat4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 165 </td>
<td> 79 </td>
<td> tan1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 154 </td>
<td> 73 </td>
<td> tan2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 133 </td>
<td> 63 </td>
<td> tan3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 90 </td>
<td> 43 </td>
<td> tan4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 127 </td>
<td> 36 </td>
<td> chocolate1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 118 </td>
<td> 33 </td>
<td> chocolate2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 102 </td>
<td> 29 </td>
<td> chocolate3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 69 </td>
<td> 19 </td>
<td> chocolate4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 48 </td>
<td> 48 </td>
<td> firebrick1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 44 </td>
<td> 44 </td>
<td> firebrick2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 38 </td>
<td> 38 </td>
<td> firebrick3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 26 </td>
<td> 26 </td>
<td> firebrick4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 64 </td>
<td> 64 </td>
<td> brown1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 59 </td>
<td> 59 </td>
<td> brown2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 51 </td>
<td> 51 </td>
<td> brown3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 35 </td>
<td> 35 </td>
<td> brown4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 140 </td>
<td> 105 </td>
<td> salmon1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 130 </td>
<td> 98 </td>
<td> salmon2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 112 </td>
<td> 84 </td>
<td> salmon3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 76 </td>
<td> 57 </td>
<td> salmon4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 160 </td>
<td> 122 </td>
<td> lightsalmon1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 149 </td>
<td> 114 </td>
<td> lightsalmon2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 129 </td>
<td> 98 </td>
<td> lightsalmon3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 87 </td>
<td> 66 </td>
<td> lightsalmon4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 165 </td>
<td> 0 </td>
<td> orange1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 154 </td>
<td> 0 </td>
<td> orange2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 133 </td>
<td> 0 </td>
<td> orange3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 90 </td>
<td> 0 </td>
<td> orange4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 127 </td>
<td> 0 </td>
<td> darkorange1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 118 </td>
<td> 0 </td>
<td> darkorange2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 102 </td>
<td> 0 </td>
<td> darkorange3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 69 </td>
<td> 0 </td>
<td> darkorange4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 114 </td>
<td> 86 </td>
<td> coral1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 106 </td>
<td> 80 </td>
<td> coral2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 91 </td>
<td> 69 </td>
<td> coral3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 62 </td>
<td> 47 </td>
<td> coral4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 99 </td>
<td> 71 </td>
<td> tomato1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 92 </td>
<td> 66 </td>
<td> tomato2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 79 </td>
<td> 57 </td>
<td> tomato3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 54 </td>
<td> 38 </td>
<td> tomato4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 69 </td>
<td> 0 </td>
<td> orangered1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 64 </td>
<td> 0 </td>
<td> orangered2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 55 </td>
<td> 0 </td>
<td> orangered3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 37 </td>
<td> 0 </td>
<td> orangered4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 0 </td>
<td> 0 </td>
<td> red1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 0 </td>
<td> 0 </td>
<td> red2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 0 </td>
<td> 0 </td>
<td> red3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 0 </td>
<td> 0 </td>
<td> red4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 20 </td>
<td> 147 </td>
<td> deeppink1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 18 </td>
<td> 137 </td>
<td> deeppink2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 16 </td>
<td> 118 </td>
<td> deeppink3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 10 </td>
<td> 80 </td>
<td> deeppink4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 110 </td>
<td> 180 </td>
<td> hotpink1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 106 </td>
<td> 167 </td>
<td> hotpink2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 96 </td>
<td> 144 </td>
<td> hotpink3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 58 </td>
<td> 98 </td>
<td> hotpink4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 181 </td>
<td> 197 </td>
<td> pink1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 169 </td>
<td> 184 </td>
<td> pink2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 145 </td>
<td> 158 </td>
<td> pink3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 99 </td>
<td> 108 </td>
<td> pink4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 174 </td>
<td> 185 </td>
<td> lightpink1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 162 </td>
<td> 173 </td>
<td> lightpink2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 140 </td>
<td> 149 </td>
<td> lightpink3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 95 </td>
<td> 101 </td>
<td> lightpink4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 130 </td>
<td> 171 </td>
<td> palevioletred1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 121 </td>
<td> 159 </td>
<td> palevioletred2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 104 </td>
<td> 137 </td>
<td> palevioletred3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 71 </td>
<td> 93 </td>
<td> palevioletred4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 52 </td>
<td> 179 </td>
<td> maroon1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 48 </td>
<td> 167 </td>
<td> maroon2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 41 </td>
<td> 144 </td>
<td> maroon3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 28 </td>
<td> 98 </td>
<td> maroon4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 62 </td>
<td> 150 </td>
<td> violetred1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 58 </td>
<td> 140 </td>
<td> violetred2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 50 </td>
<td> 120 </td>
<td> violetred3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 34 </td>
<td> 82 </td>
<td> violetred4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 0 </td>
<td> 255 </td>
<td> magenta1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 0 </td>
<td> 238 </td>
<td> magenta2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 0 </td>
<td> 205 </td>
<td> magenta3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 0 </td>
<td> 139 </td>
<td> magenta4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 131 </td>
<td> 250 </td>
<td> orchid1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 122 </td>
<td> 233 </td>
<td> orchid2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 105 </td>
<td> 201 </td>
<td> orchid3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 71 </td>
<td> 137 </td>
<td> orchid4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 187 </td>
<td> 255 </td>
<td> plum1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 174 </td>
<td> 238 </td>
<td> plum2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 150 </td>
<td> 205 </td>
<td> plum3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 102 </td>
<td> 139 </td>
<td> plum4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 224 </td>
<td> 102 </td>
<td> 255 </td>
<td> mediumorchid1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 209 </td>
<td> 95 </td>
<td> 238 </td>
<td> mediumorchid2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 180 </td>
<td> 82 </td>
<td> 205 </td>
<td> mediumorchid3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 122 </td>
<td> 55 </td>
<td> 139 </td>
<td> mediumorchid4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 191 </td>
<td> 62 </td>
<td> 255 </td>
<td> darkorchid1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 178 </td>
<td> 58 </td>
<td> 238 </td>
<td> darkorchid2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 154 </td>
<td> 50 </td>
<td> 205 </td>
<td> darkorchid3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 104 </td>
<td> 34 </td>
<td> 139 </td>
<td> darkorchid4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 155 </td>
<td> 48 </td>
<td> 255 </td>
<td> purple1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 145 </td>
<td> 44 </td>
<td> 238 </td>
<td> purple2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 125 </td>
<td> 38 </td>
<td> 205 </td>
<td> purple3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 171 </td>
<td> 130 </td>
<td> 255 </td>
<td> mediumpurple1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 159 </td>
<td> 121 </td>
<td> 238 </td>
<td> mediumpurple2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 137 </td>
<td> 104 </td>
<td> 205 </td>
<td> mediumpurple3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 225 </td>
<td> 255 </td>
<td> thistle1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 238 </td>
<td> 210 </td>
<td> 238 </td>
<td> thistle2
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 205 </td>
<td> 181 </td>
<td> 205 </td>
<td> thistle3
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 139 </td>
<td> 123 </td>
<td> 139 </td>
<td> thistle4
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 102 </td>
<td> 102 </td>
<td> 102 </td>
<td> gray40
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 102 </td>
<td> 102 </td>
<td> 102 </td>
<td> grey40
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 105 </td>
<td> 105 </td>
<td> 105 </td>
<td> gray41
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 105 </td>
<td> 105 </td>
<td> 105 </td>
<td> grey41
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 107 </td>
<td> 107 </td>
<td> 107 </td>
<td> gray42
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 107 </td>
<td> 107 </td>
<td> 107 </td>
<td> grey42
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 110 </td>
<td> 110 </td>
<td> 110 </td>
<td> gray43
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 110 </td>
<td> 110 </td>
<td> 110 </td>
<td> grey43
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 112 </td>
<td> 112 </td>
<td> 112 </td>
<td> gray44
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 112 </td>
<td> 112 </td>
<td> 112 </td>
<td> grey44
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 115 </td>
<td> 115 </td>
<td> 115 </td>
<td> gray45
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 115 </td>
<td> 115 </td>
<td> 115 </td>
<td> grey45
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 117 </td>
<td> 117 </td>
<td> 117 </td>
<td> gray46
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 117 </td>
<td> 117 </td>
<td> 117 </td>
<td> grey46
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 120 </td>
<td> 120 </td>
<td> 120 </td>
<td> gray47
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 120 </td>
<td> 120 </td>
<td> 120 </td>
<td> grey47
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 122 </td>
<td> 122 </td>
<td> 122 </td>
<td> gray48
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 122 </td>
<td> 122 </td>
<td> 122 </td>
<td> grey48
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 125 </td>
<td> 125 </td>
<td> 125 </td>
<td> gray49
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 125 </td>
<td> 125 </td>
<td> 125 </td>
<td> grey49
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 127 </td>
<td> 127 </td>
<td> 127 </td>
<td> gray50
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 127 </td>
<td> 127 </td>
<td> 127 </td>
<td> grey50
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 130 </td>
<td> 130 </td>
<td> 130 </td>
<td> gray51
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 130 </td>
<td> 130 </td>
<td> 130 </td>
<td> grey51
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 133 </td>
<td> 133 </td>
<td> 133 </td>
<td> gray52
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 133 </td>
<td> 133 </td>
<td> 133 </td>
<td> grey52
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 135 </td>
<td> 135 </td>
<td> 135 </td>
<td> gray53
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 135 </td>
<td> 135 </td>
<td> 135 </td>
<td> grey53
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 138 </td>
<td> 138 </td>
<td> 138 </td>
<td> gray54
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 138 </td>
<td> 138 </td>
<td> 138 </td>
<td> grey54
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 140 </td>
<td> 140 </td>
<td> 140 </td>
<td> gray55
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 140 </td>
<td> 140 </td>
<td> 140 </td>
<td> grey55
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 143 </td>
<td> 143 </td>
<td> 143 </td>
<td> gray56
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 143 </td>
<td> 143 </td>
<td> 143 </td>
<td> grey56
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 145 </td>
<td> 145 </td>
<td> 145 </td>
<td> gray57
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 145 </td>
<td> 145 </td>
<td> 145 </td>
<td> grey57
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 148 </td>
<td> 148 </td>
<td> 148 </td>
<td> gray58
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 148 </td>
<td> 148 </td>
<td> 148 </td>
<td> grey58
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 150 </td>
<td> 150 </td>
<td> 150 </td>
<td> gray59
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 150 </td>
<td> 150 </td>
<td> 150 </td>
<td> grey59
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 153 </td>
<td> 153 </td>
<td> 153 </td>
<td> gray60
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 153 </td>
<td> 153 </td>
<td> 153 </td>
<td> grey60
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 156 </td>
<td> 156 </td>
<td> 156 </td>
<td> gray61
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 156 </td>
<td> 156 </td>
<td> 156 </td>
<td> grey61
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 158 </td>
<td> 158 </td>
<td> 158 </td>
<td> gray62
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 158 </td>
<td> 158 </td>
<td> 158 </td>
<td> grey62
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 161 </td>
<td> 161 </td>
<td> 161 </td>
<td> gray63
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 161 </td>
<td> 161 </td>
<td> 161 </td>
<td> grey63
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 163 </td>
<td> 163 </td>
<td> 163 </td>
<td> gray64
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 163 </td>
<td> 163 </td>
<td> 163 </td>
<td> grey64
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 166 </td>
<td> 166 </td>
<td> 166 </td>
<td> gray65
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 166 </td>
<td> 166 </td>
<td> 166 </td>
<td> grey65
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 168 </td>
<td> 168 </td>
<td> 168 </td>
<td> gray66
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 168 </td>
<td> 168 </td>
<td> 168 </td>
<td> grey66
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 171 </td>
<td> 171 </td>
<td> 171 </td>
<td> gray67
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 171 </td>
<td> 171 </td>
<td> 171 </td>
<td> grey67
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 173 </td>
<td> 173 </td>
<td> 173 </td>
<td> gray68
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 173 </td>
<td> 173 </td>
<td> 173 </td>
<td> grey68
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 176 </td>
<td> 176 </td>
<td> 176 </td>
<td> gray69
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 176 </td>
<td> 176 </td>
<td> 176 </td>
<td> grey69
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 179 </td>
<td> 179 </td>
<td> 179 </td>
<td> gray70
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 179 </td>
<td> 179 </td>
<td> 179 </td>
<td> grey70
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 181 </td>
<td> 181 </td>
<td> 181 </td>
<td> gray71
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 181 </td>
<td> 181 </td>
<td> 181 </td>
<td> grey71
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 184 </td>
<td> 184 </td>
<td> 184 </td>
<td> gray72
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 184 </td>
<td> 184 </td>
<td> 184 </td>
<td> grey72
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 186 </td>
<td> 186 </td>
<td> 186 </td>
<td> gray73
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 186 </td>
<td> 186 </td>
<td> 186 </td>
<td> grey73
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 189 </td>
<td> 189 </td>
<td> 189 </td>
<td> gray74
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 189 </td>
<td> 189 </td>
<td> 189 </td>
<td> grey74
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 191 </td>
<td> 191 </td>
<td> 191 </td>
<td> gray75
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 191 </td>
<td> 191 </td>
<td> 191 </td>
<td> grey75
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 194 </td>
<td> 194 </td>
<td> 194 </td>
<td> gray76
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 194 </td>
<td> 194 </td>
<td> 194 </td>
<td> grey76
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 196 </td>
<td> 196 </td>
<td> 196 </td>
<td> gray77
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 196 </td>
<td> 196 </td>
<td> 196 </td>
<td> grey77
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 199 </td>
<td> 199 </td>
<td> 199 </td>
<td> gray78
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 199 </td>
<td> 199 </td>
<td> 199 </td>
<td> grey78
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 201 </td>
<td> 201 </td>
<td> 201 </td>
<td> gray79
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 201 </td>
<td> 201 </td>
<td> 201 </td>
<td> grey79
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 204 </td>
<td> 204 </td>
<td> 204 </td>
<td> gray80
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 204 </td>
<td> 204 </td>
<td> 204 </td>
<td> grey80
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 207 </td>
<td> 207 </td>
<td> 207 </td>
<td> gray81
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 207 </td>
<td> 207 </td>
<td> 207 </td>
<td> grey81
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 209 </td>
<td> 209 </td>
<td> 209 </td>
<td> gray82
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 209 </td>
<td> 209 </td>
<td> 209 </td>
<td> grey82
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 212 </td>
<td> 212 </td>
<td> 212 </td>
<td> gray83
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 212 </td>
<td> 212 </td>
<td> 212 </td>
<td> grey83
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 214 </td>
<td> 214 </td>
<td> 214 </td>
<td> gray84
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 214 </td>
<td> 214 </td>
<td> 214 </td>
<td> grey84
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 217 </td>
<td> 217 </td>
<td> 217 </td>
<td> gray85
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 217 </td>
<td> 217 </td>
<td> 217 </td>
<td> grey85
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 219 </td>
<td> 219 </td>
<td> 219 </td>
<td> gray86
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 219 </td>
<td> 219 </td>
<td> 219 </td>
<td> grey86
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 222 </td>
<td> 222 </td>
<td> 222 </td>
<td> gray87
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 222 </td>
<td> 222 </td>
<td> 222 </td>
<td> grey87
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 224 </td>
<td> 224 </td>
<td> 224 </td>
<td> gray88
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 224 </td>
<td> 224 </td>
<td> 224 </td>
<td> grey88
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 227 </td>
<td> 227 </td>
<td> 227 </td>
<td> gray89
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 227 </td>
<td> 227 </td>
<td> 227 </td>
<td> grey89
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 229 </td>
<td> 229 </td>
<td> 229 </td>
<td> gray90
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 229 </td>
<td> 229 </td>
<td> 229 </td>
<td> grey90
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 232 </td>
<td> 232 </td>
<td> 232 </td>
<td> gray91
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 232 </td>
<td> 232 </td>
<td> 232 </td>
<td> grey91
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 235 </td>
<td> 235 </td>
<td> 235 </td>
<td> gray92
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 235 </td>
<td> 235 </td>
<td> 235 </td>
<td> grey92
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 237 </td>
<td> 237 </td>
<td> 237 </td>
<td> gray93
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 237 </td>
<td> 237 </td>
<td> 237 </td>
<td> grey93
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 240 </td>
<td> 240 </td>
<td> 240 </td>
<td> gray94
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 240 </td>
<td> 240 </td>
<td> 240 </td>
<td> grey94
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 242 </td>
<td> 242 </td>
<td> 242 </td>
<td> gray95
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 242 </td>
<td> 242 </td>
<td> 242 </td>
<td> grey95
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 245 </td>
<td> 245 </td>
<td> 245 </td>
<td> gray96
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 245 </td>
<td> 245 </td>
<td> 245 </td>
<td> grey96
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 247 </td>
<td> 247 </td>
<td> 247 </td>
<td> gray97
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 247 </td>
<td> 247 </td>
<td> 247 </td>
<td> grey97
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 250 </td>
<td> 250 </td>
<td> 250 </td>
<td> gray98
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 250 </td>
<td> 250 </td>
<td> 250 </td>
<td> grey98
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 252 </td>
<td> 252 </td>
<td> 252 </td>
<td> gray99
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 252 </td>
<td> 252 </td>
<td> 252 </td>
<td> grey99
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 255 </td>
<td> 255 </td>
<td> gray100
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 255 </td>
<td> 255 </td>
<td> 255 </td>
<td> grey100
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
</table>
<p></center></p>
<h2>Further Information</h2>
<p>For more information on the use of color, read Appendix I of the <code>GMT TECHNICAL REFERENCE AND COOKBOOK</code>.</p>
<h2>See Also</h2>
<p><code>gmt.conf</code> , <code>gmtlogo</code> , <code>grdcontour</code> , <code>grdvector</code> , <code>grdview</code> <code>psbasemap</code> , <code>pscoast</code> , <code>pscontour</code>, <code>pshistogram</code> , <code>psimage</code> , <code>pslegend</code> , <code>psmask</code> , <code>psrose</code> , <code>pstext</code> , <code>pswiggle</code> , <code>psxy</code> , <code>psxyz</code></p>
<h2>Copyright</h2>
<p>2015, P. Wessel, W. H. F. Smith, R. Scharroo, J. Luis, and F. Wobbe</p>
