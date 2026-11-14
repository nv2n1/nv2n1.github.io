---
title: "groff_char(7)"
name: "groff_char"
section: "7"
letter: "g"
url: "/docs/linux/man/7-groff_char/"
description: "groff_char – groff glyph names"
---

<p>groff_char &#8211; groff glyph names</p>
<h2>Description</h2>
<p>This manual page lists the standard <code>groff</code> glyph names and the default input mapping, latin1. The glyphs in this document look different depending on which output device was chosen (with option <code>-T</code> for the <code><a href="/docs/linux/man/1-man/">man</a></code>(1) program or the roff formatter). Glyphs not available for the device that is being used to print or view this manual page are marked with &#8216;(N/A)&#8217;. </p>
<p> In the actual version, <code>groff</code> provides only 8-bit characters for direct input and named entities for further glyphs. On ASCII platforms, input character codes in the range 0 to 127 (decimal) represent the usual 7-bit ASCII characters, while codes between 127 and 255 are interpreted as the corresponding characters in the <i>latin1</i> (<i>ISO-8859-1</i>) code set by default. This mapping is contained in the file <tt>latin1.tmac</tt> and can be changed by loading a different input encoding. Note that some of the input characters are reserved by <code>groff</code>, either for internal use or for special input purposes. On EBCDIC platforms, only code page <i>cp1047</i> is supported (which contains the same characters as latin1; the input encoding file is called <tt>cp1047.tmac</tt>). Again, some input characters are reserved for internal and special purposes. </p>
<p> All roff systems provide the concept of named glyphs. In traditional roff systems, only names of length 2 were used, while groff also provides support for longer names. It is strongly suggested that only named glyphs are used for all character representations outside of the printable 7-bit ASCII range. </p>
<p> Some of the predefined groff escape sequences (with names of length 1) also produce single glyphs; these exist for historical reasons or are printable versions of syntactical characters. They include &#8216;<tt>\</tt>&#8216;, &#8216;<tt>\'</tt>&#8216;, &#8216;<tt>\`</tt>&#8216;, &#8216;<tt>\-</tt>&#8216;, &#8216;<tt>\.</tt>&#8216;, and &#8216;<tt></tt>&#8216;; see <code><a href="/docs/linux/man/7-groff/">groff</a></code>(7). </p>
<p> In groff, all of these different types of characters and glyphs can be tested positively with the &#8216;<tt>.if c</tt>&#8216; conditional.</p>
<h2>Reference</h2>
<p>In this section, the glyphs in groff are specified in tabular form. The meaning of the columns is as follows.</p>
<dl>
<dt><i>Output</i></p>
<dd>shows how the glyph is printed for the current device; although this can have quite a different shape on other devices, it always represents the same glyph.</p>
<dt><i>Input</i></p>
<dd>specifies how the glyph is input either directly by a key on the keyboard, or by a groff escape sequence.</p>
<dt><i>Code</i></p>
<dd>applies to glyphs which can be input with a single character, and gives the ISO latin1 decimal code of that input character. Note that this code is equivalent to the lowest 256 Unicode characters, including 7-bit ASCII in the range 0 to 127.</p>
<dt><i>PostScript</i></p>
<dd>gives the usual PostScript name of the glyph.</p>
<dt><i>Unicode</i></p>
<dd>is the glyph name used in composite glyph names. The names in the Unicode column look like <code>u0021</code> or <code>u0041_0300</code>. In groff, the corresponding Unicode characters can be constructed by adding a backslash and a pair of square brackets, for example <code>\[u0021]</code> or <code>\[u0041_0300]</code>.</dl>
<h3>7-bit Character Codes 32-126</h3>
<p>These are the basic glyphs having 7-bit ASCII code values assigned. They are identical to the printable characters of the character standards ISO-8859-1 (latin1) and Unicode (range <i>Basic Latin</i>). The glyph names used in composite glyph names are &#8216;u0020&#8217; up to &#8216;u007E&#8217;. </p>
<p> Note that input characters in the range 0-31 and character 127 are <i>not</i> printable characters. Most of them are invalid input characters for <code>groff</code> anyway, and the valid ones have special meaning. For EBCDIC, the printable characters are in the range 66-255.</p>
<dl>
<dt>48-57</p>
<dd>Decimal digits 0 to 9 (print as themselves).</p>
<dt>65-90</p>
<dd>Upper case letters A-Z (print as themselves).</p>
<dt>97-122</p>
<dd>Lower case letters a-z (print as themselves).</dl>
<p> Most of the remaining characters not in the just described ranges print as themselves; the only exceptions are the following characters:</p>
<dl>
<dt><code>`</code></p>
<dd>the ISO latin1 &#8216;Grave Accent&#8217; (code 96) prints as &#8216;, a left single quotation mark (Unicode u2018). The same output glyph can be requested explicitly with &#8216;<tt>\(oq</tt>&#8216;. The original character can be obtained with &#8216;<tt>\`</tt>&#8216; (Unicode u0060).</p>
<dt><code>&#8216;</code></p>
<dd>the ISO latin1 &#8216;Apostrophe&#8217; (code 39) prints as &#8216;, a right single quotation mark (Unicode u2019). The same output glyph is commonly used in typography to represent a punctation apostrophe, for example in contractions. It can be requested explicitly with &#8216;<tt>\(cq</tt>&#8216;. The original character can be obtained with &#8216;<tt>\(aq</tt>&#8216; (Unicode u0027).</p>
<dt><code>&#8211;</code></p>
<dd>the ISO latin1 &#8216;Hyphen, Minus Sign&#8217; (code 45) prints as a hyphen (Unicode u2010). The same output glyph can be requested explicitly with &#8216;<tt>\(hy</tt>&#8216;. A minus sign can be obtained with &#8216;<tt>\-</tt>&#8216; (Unicode u2212).</p>
<dt><code>~</code></p>
<dd>the ISO latin1 &#8216;Tilde&#8217; (code 126) is reduced in size to be usable as a diacritic (Unicode u02DC). A larger glyph can be obtained with &#8216;<tt>\(ti</tt>&#8216; (Unicode u007E).</p>
<dt><code>^</code></p>
<dd>the ISO latin1 &#8216;Circumflex Accent&#8217; (code 94) is reduced in size to be usable as a diacritic (Unicode u02C6); a larger glyph can be obtained with &#8216;<tt>\(ha</tt>&#8216; (Unicode u005E).</dl>
<table>
<tr VALIGN=top>
<td>Output</td>
<td>Input</td>
<td>Code</td>
<td>PostScript</td>
<td>Unicode</td>
<td>Notes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=6>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>33</td>
<td>33</td>
<td>33</td>
<td>exclam</td>
<td>u0021</td>
<td>exclamation mark (bang)
</td>
</tr>
<tr VALIGN=top>
<td>34</td>
<td>34</td>
<td>34</td>
<td>quotedbl</td>
<td>u0022</td>
<td>double quote
</td>
</tr>
<tr VALIGN=top>
<td>35</td>
<td>35</td>
<td>35</td>
<td>numbersign</td>
<td>u0023</td>
<td>number sign
</td>
</tr>
<tr VALIGN=top>
<td>36</td>
<td>36</td>
<td>36</td>
<td>dollar</td>
<td>u0024</td>
<td>currency dollar sign
</td>
</tr>
<tr VALIGN=top>
<td>37</td>
<td>37</td>
<td>37</td>
<td>percent</td>
<td>u0025</td>
<td>percent
</td>
</tr>
<tr VALIGN=top>
<td>38</td>
<td>38</td>
<td>38</td>
<td>ampersand</td>
<td>u0026</td>
<td>ampersand
</td>
</tr>
<tr VALIGN=top>
<td>&#8216;</td>
<td>&#8216;</td>
<td>39</td>
<td>quoteright</td>
<td>u2019</td>
<td>right quote
</td>
</tr>
<tr VALIGN=top>
<td>&#8216;</td>
<td>\(aq</td>
<td></td>
<td>quotesingle</td>
<td>u0027</td>
<td>apostrophe quote
</td>
</tr>
<tr VALIGN=top>
<td>40</td>
<td>40</td>
<td>40</td>
<td>parenleft</td>
<td>u0028</td>
<td>parentheses left
</td>
</tr>
<tr VALIGN=top>
<td>41</td>
<td>41</td>
<td>41</td>
<td>parenright</td>
<td>u0029</td>
<td>parentheses right
</td>
</tr>
<tr VALIGN=top>
<td>42</td>
<td>42</td>
<td>42</td>
<td>asterisk</td>
<td>u002A</td>
<td>asterisk
</td>
</tr>
<tr VALIGN=top>
<td>43</td>
<td>43</td>
<td>43</td>
<td>plus</td>
<td>u002B</td>
<td>plus
</td>
</tr>
<tr VALIGN=top>
<td>44</td>
<td>44</td>
<td>44</td>
<td>comma</td>
<td>u002C</td>
<td>comma
</td>
</tr>
<tr VALIGN=top>
<td>&#8211;</td>
<td>45</td>
<td>45</td>
<td>hyphen</td>
<td>u2010</td>
<td>hyphen
</td>
</tr>
<tr VALIGN=top>
<td>&#8211;</td>
<td>\-</td>
<td></td>
<td>minus</td>
<td>u2212</td>
<td>minus sign
</td>
</tr>
<tr VALIGN=top>
<td>46</td>
<td>46</td>
<td>46</td>
<td>period</td>
<td>u002E</td>
<td>period, dot
</td>
</tr>
<tr VALIGN=top>
<td>47</td>
<td>47</td>
<td>47</td>
<td>slash</td>
<td>u002F</td>
<td>slash
</td>
</tr>
<tr VALIGN=top>
<td>58</td>
<td>58</td>
<td>58</td>
<td>colon</td>
<td>u003A</td>
<td>colon
</td>
</tr>
<tr VALIGN=top>
<td>59</td>
<td>59</td>
<td>59</td>
<td>semicolon</td>
<td>u003B</td>
<td>semicolon
</td>
</tr>
<tr VALIGN=top>
<td>60</td>
<td>60</td>
<td>60</td>
<td>less</td>
<td>u003C</td>
<td>less than
</td>
</tr>
<tr VALIGN=top>
<td>61</td>
<td>61</td>
<td>61</td>
<td>equal</td>
<td>u003D</td>
<td>equal
</td>
</tr>
<tr VALIGN=top>
<td>62</td>
<td>62</td>
<td>62</td>
<td>greater</td>
<td>u003E</td>
<td>greater than
</td>
</tr>
<tr VALIGN=top>
<td>63</td>
<td>63</td>
<td>63</td>
<td>question</td>
<td>u003F</td>
<td>question mark
</td>
</tr>
<tr VALIGN=top>
<td>64</td>
<td>64</td>
<td>64</td>
<td>at</td>
<td>u0040</td>
<td>at
</td>
</tr>
<tr VALIGN=top>
<td>91</td>
<td>91</td>
<td>91</td>
<td>bracketleft</td>
<td>u005B</td>
<td>square bracket left
</td>
</tr>
<tr VALIGN=top>
<td>92</td>
<td>92</td>
<td>92</td>
<td>backslash</td>
<td>u005C</td>
<td>backslash
</td>
</tr>
<tr VALIGN=top>
<td>93</td>
<td>93</td>
<td>93</td>
<td>bracketright</td>
<td>u005D</td>
<td>square bracket right
</td>
</tr>
<tr VALIGN=top>
<td>a^</td>
<td>ha</td>
<td>94</td>
<td>circumflex</td>
<td>u02C6</td>
<td>modifier circumflex
</td>
</tr>
<tr VALIGN=top>
<td>ha</td>
<td>\(ha</td>
<td></td>
<td>asciicircum</td>
<td>u005E</td>
<td>circumflex accent
</td>
</tr>
<tr VALIGN=top>
<td>95</td>
<td>95</td>
<td>95</td>
<td>underscore</td>
<td>u005F</td>
<td>underscore
</td>
</tr>
<tr VALIGN=top>
<td>&#8216;</td>
<td>`</td>
<td>96</td>
<td>quoteleft</td>
<td>u2018</td>
<td>left quote
</td>
</tr>
<tr VALIGN=top>
<td>`</td>
<td>\(ga</td>
<td></td>
<td>grave</td>
<td>u0060</td>
<td>grave accent
</td>
</tr>
<tr VALIGN=top>
<td>23</td>
<td>23</td>
<td>123</td>
<td>braceleft</td>
<td>u007B</td>
<td>curly brace left
</td>
</tr>
<tr VALIGN=top>
<td>24</td>
<td>24</td>
<td>124</td>
<td>bar</td>
<td>u007C</td>
<td>bar
</td>
</tr>
<tr VALIGN=top>
<td>25</td>
<td>25</td>
<td>125</td>
<td>braceright</td>
<td>u007D</td>
<td>curly brace right
</td>
</tr>
<tr VALIGN=top>
<td>DC</td>
<td>~</td>
<td>126</td>
<td>tilde</td>
<td>u02DC</td>
<td>small tilde
</td>
</tr>
<tr VALIGN=top>
<td>~</td>
<td>\(ti</td>
<td></td>
<td>asciitilde</td>
<td>u007E</td>
<td>tilde
</td>
</tr>
</table>
<h3>8-bit Character Codes 160 to 255</h3>
<p>They are interpreted as printable characters according to the <i>latin1</i> (<i>ISO-8859-1</i>) code set, being identical to the Unicode range <i>Latin-1 Supplement</i>. </p>
<p> Input characters in range 128-159 (on non-EBCDIC hosts) are not printable characters.</p>
<dl>
<dt>160</p>
<dd>the ISO latin1 <i>no-break space</i> is mapped to &#8216;<tt>\~</tt>&#8216;, the stretchable space character.</p>
<dt>173</p>
<dd>the soft hyphen control character. <code>groff</code> never uses this character for output (thus it is omitted in the table below); the input character 173 is mapped onto &#8216;<tt>\%</tt>&#8216;.</dl>
<p> The remaining ranges (161-172, 174-255) are printable characters that print as themselves. Although they can be specified directly with the keyboard on systems with a latin1 code page, it is better to use their glyph names; see the next section. </p>
<table>
<tr VALIGN=top>
<td>Output</td>
<td>Input</td>
<td>Code</td>
<td>PostScript</td>
<td>Unicode</td>
<td>Notes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=6>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>61</td>
<td>61</td>
<td>161</td>
<td>exclamdown</td>
<td>u00A1</td>
<td>inverted exclamation mark
</td>
</tr>
<tr VALIGN=top>
<td>62</td>
<td>62</td>
<td>162</td>
<td>cent</td>
<td>u00A2</td>
<td>currency unit
</td>
</tr>
<tr VALIGN=top>
<td>63</td>
<td>63</td>
<td>163</td>
<td>sterling</td>
<td>u00A3</td>
<td>pound sterling
</td>
</tr>
<tr VALIGN=top>
<td>64</td>
<td>64</td>
<td>164</td>
<td>currency</td>
<td>u00A4</td>
<td>generic currency symbol
</td>
</tr>
<tr VALIGN=top>
<td>65</td>
<td>65</td>
<td>165</td>
<td>yen</td>
<td>u00A5</td>
<td>Japanese currency symbol
</td>
</tr>
<tr VALIGN=top>
<td>66</td>
<td>66</td>
<td>166</td>
<td>brokenbar</td>
<td>u00A6</td>
<td>broken bar
</td>
</tr>
<tr VALIGN=top>
<td>67</td>
<td>67</td>
<td>167</td>
<td>section</td>
<td>u00A7</td>
<td>section sign
</td>
</tr>
<tr VALIGN=top>
<td>68</td>
<td>68</td>
<td>168</td>
<td>dieresis</td>
<td>u00A8</td>
<td>dieresis (umlaut)
</td>
</tr>
<tr VALIGN=top>
<td>69</td>
<td>69</td>
<td>169</td>
<td>copyright</td>
<td>u00A9</td>
<td>copyright symbol
</td>
</tr>
<tr VALIGN=top>
<td>70</td>
<td>70</td>
<td>170</td>
<td>ordfeminine</td>
<td>u00AA</td>
<td>feminine ordinal (Spanish)
</td>
</tr>
<tr VALIGN=top>
<td>71</td>
<td>71</td>
<td>171</td>
<td>guillemotleft</td>
<td>u00AB</td>
<td>left guillemet [sic]
</td>
</tr>
<tr VALIGN=top>
<td>72</td>
<td>72</td>
<td>172</td>
<td>logicalnot</td>
<td>u00AC</td>
<td>logical not
</td>
</tr>
<tr VALIGN=top>
<td>74</td>
<td>74</td>
<td>174</td>
<td>registered</td>
<td>u00AE</td>
<td>registered mark symbol
</td>
</tr>
<tr VALIGN=top>
<td>75</td>
<td>75</td>
<td>175</td>
<td>macron</td>
<td>u00AF</td>
<td>overbar accent
</td>
</tr>
<tr VALIGN=top>
<td>76</td>
<td>76</td>
<td>176</td>
<td>degree</td>
<td>u00B0</td>
<td>degree sign
</td>
</tr>
<tr VALIGN=top>
<td>77</td>
<td>77</td>
<td>177</td>
<td>plusminus</td>
<td>u00B1</td>
<td>plus-minus sign
</td>
</tr>
<tr VALIGN=top>
<td>78</td>
<td>78</td>
<td>178</td>
<td>twosuperior</td>
<td>u00B2</td>
<td>superscript 2
</td>
</tr>
<tr VALIGN=top>
<td>79</td>
<td>79</td>
<td>179</td>
<td>threesuperior</td>
<td>u00B3</td>
<td>superscript 3
</td>
</tr>
<tr VALIGN=top>
<td>80</td>
<td>80</td>
<td>180</td>
<td>acute</td>
<td>u00B4</td>
<td>acute accent
</td>
</tr>
<tr VALIGN=top>
<td>81</td>
<td>81</td>
<td>181</td>
<td>mu</td>
<td>u00B5</td>
<td>micro sign
</td>
</tr>
<tr VALIGN=top>
<td>82</td>
<td>82</td>
<td>182</td>
<td>paragraph</td>
<td>u00B6</td>
<td>end of paragraphs marker
</td>
</tr>
<tr VALIGN=top>
<td>83</td>
<td>83</td>
<td>183</td>
<td>periodcentered</td>
<td>u00B7</td>
<td>centered period
</td>
</tr>
<tr VALIGN=top>
<td>84</td>
<td>84</td>
<td>184</td>
<td>cedilla</td>
<td>u00B8</td>
<td>cedilla accent
</td>
</tr>
<tr VALIGN=top>
<td>85</td>
<td>85</td>
<td>185</td>
<td>onesuperior</td>
<td>u00B9</td>
<td>superscript 1
</td>
</tr>
<tr VALIGN=top>
<td>86</td>
<td>86</td>
<td>186</td>
<td>ordmasculine</td>
<td>u00BA</td>
<td>masculine ordinal (Spanish)
</td>
</tr>
<tr VALIGN=top>
<td>87</td>
<td>87</td>
<td>187</td>
<td>guillemotright</td>
<td>u00BB</td>
<td>right guillemet [sic]
</td>
</tr>
<tr VALIGN=top>
<td>88</td>
<td>88</td>
<td>188</td>
<td>onequarter</td>
<td>u00BC</td>
<td>1/4 symbol
</td>
</tr>
<tr VALIGN=top>
<td>89</td>
<td>89</td>
<td>189</td>
<td>onehalf</td>
<td>u00BD</td>
<td>1/2 symbol
</td>
</tr>
<tr VALIGN=top>
<td>90</td>
<td>90</td>
<td>190</td>
<td>threequarters</td>
<td>u00BE</td>
<td>3/4 symbol
</td>
</tr>
<tr VALIGN=top>
<td>91</td>
<td>91</td>
<td>191</td>
<td>questiondown</td>
<td>u00BF</td>
<td>inverted question mark
</td>
</tr>
<tr VALIGN=top>
<td>92</td>
<td>92</td>
<td>192</td>
<td>Agrave</td>
<td>u0041_0300</td>
<td>A grave
</td>
</tr>
<tr VALIGN=top>
<td>93</td>
<td>93</td>
<td>193</td>
<td>Aacute</td>
<td>u0041_0301</td>
<td>A acute
</td>
</tr>
<tr VALIGN=top>
<td>94</td>
<td>94</td>
<td>194</td>
<td>Acircumflex</td>
<td>u0041_0302</td>
<td>A circumflex
</td>
</tr>
<tr VALIGN=top>
<td>95</td>
<td>95</td>
<td>195</td>
<td>Atilde</td>
<td>u0041_0303</td>
<td>A tilde
</td>
</tr>
<tr VALIGN=top>
<td>96</td>
<td>96</td>
<td>196</td>
<td>Adieresis</td>
<td>u0041_0308</td>
<td>A dieresis (umlaut)
</td>
</tr>
<tr VALIGN=top>
<td>97</td>
<td>97</td>
<td>197</td>
<td>Aring</td>
<td>u0041_030A</td>
<td>A ring
</td>
</tr>
<tr VALIGN=top>
<td>98</td>
<td>98</td>
<td>198</td>
<td>AE</td>
<td>u00C6</td>
<td>A+E combined
</td>
</tr>
<tr VALIGN=top>
<td>99</td>
<td>99</td>
<td>199</td>
<td>Ccedilla</td>
<td>u0043_0327</td>
<td>C cedilla
</td>
</tr>
<tr VALIGN=top>
<td>00</td>
<td>00</td>
<td>200</td>
<td>Egrave</td>
<td>u0045_0300</td>
<td>E grave
</td>
</tr>
<tr VALIGN=top>
<td>01</td>
<td>01</td>
<td>201</td>
<td>Eacute</td>
<td>u0045_0301</td>
<td>E acute
</td>
</tr>
<tr VALIGN=top>
<td>02</td>
<td>02</td>
<td>202</td>
<td>Ecircumflex</td>
<td>u0045_0302</td>
<td>E circumflex
</td>
</tr>
<tr VALIGN=top>
<td>03</td>
<td>03</td>
<td>203</td>
<td>Edieresis</td>
<td>u0045_0308</td>
<td>E dieresis (umlaut)
</td>
</tr>
<tr VALIGN=top>
<td>04</td>
<td>04</td>
<td>204</td>
<td>Igrave</td>
<td>u0049_0300</td>
<td>I grave
</td>
</tr>
<tr VALIGN=top>
<td>05</td>
<td>05</td>
<td>205</td>
<td>Iacute</td>
<td>u0049_0301</td>
<td>I acute
</td>
</tr>
<tr VALIGN=top>
<td>06</td>
<td>06</td>
<td>206</td>
<td>Icircumflex</td>
<td>u0049_0302</td>
<td>I circumflex
</td>
</tr>
<tr VALIGN=top>
<td>07</td>
<td>07</td>
<td>207</td>
<td>Idieresis</td>
<td>u0049_0308</td>
<td>I dieresis
</td>
</tr>
<tr VALIGN=top>
<td>08</td>
<td>08</td>
<td>208</td>
<td>Eth</td>
<td>u00D0</td>
<td>E th
</td>
</tr>
<tr VALIGN=top>
<td>09</td>
<td>09</td>
<td>209</td>
<td>Ntilde</td>
<td>u004E_0303</td>
<td>N tilde
</td>
</tr>
<tr VALIGN=top>
<td>10</td>
<td>10</td>
<td>210</td>
<td>Ograve</td>
<td>u004F_0300</td>
<td>O grave
</td>
</tr>
<tr VALIGN=top>
<td>11</td>
<td>11</td>
<td>211</td>
<td>Oacute</td>
<td>u004F_0301</td>
<td>O acute
</td>
</tr>
<tr VALIGN=top>
<td>12</td>
<td>12</td>
<td>212</td>
<td>Ocircumflex</td>
<td>u004F_0302</td>
<td>O circumflex
</td>
</tr>
<tr VALIGN=top>
<td>13</td>
<td>13</td>
<td>213</td>
<td>Otilde</td>
<td>u004F_0303</td>
<td>O tilde
</td>
</tr>
<tr VALIGN=top>
<td>14</td>
<td>14</td>
<td>214</td>
<td>Odieresis</td>
<td>u004F_0308</td>
<td>O dieresis (umlaut)
</td>
</tr>
<tr VALIGN=top>
<td>15</td>
<td>15</td>
<td>215</td>
<td>multiply</td>
<td>u00D7</td>
<td>multiply
</td>
</tr>
<tr VALIGN=top>
<td>16</td>
<td>16</td>
<td>216</td>
<td>Oslash</td>
<td>u00D8</td>
<td>O slash
</td>
</tr>
<tr VALIGN=top>
<td>17</td>
<td>17</td>
<td>217</td>
<td>Ugrave</td>
<td>u0055_0300</td>
<td>U grave
</td>
</tr>
<tr VALIGN=top>
<td>18</td>
<td>18</td>
<td>218</td>
<td>Uacute</td>
<td>u0055_0301</td>
<td>U acute
</td>
</tr>
<tr VALIGN=top>
<td>19</td>
<td>19</td>
<td>219</td>
<td>Ucircumflex</td>
<td>u0055_0302</td>
<td>U circumflex
</td>
</tr>
<tr VALIGN=top>
<td>20</td>
<td>20</td>
<td>220</td>
<td>Udieresis</td>
<td>u0055_0308</td>
<td>U dieresis (umlaut)
</td>
</tr>
<tr VALIGN=top>
<td>21</td>
<td>21</td>
<td>221</td>
<td>Yacute</td>
<td>u0059_0301</td>
<td>Y acute
</td>
</tr>
<tr VALIGN=top>
<td>22</td>
<td>22</td>
<td>222</td>
<td>Thorn</td>
<td>u00DE</td>
<td>Thorn
</td>
</tr>
<tr VALIGN=top>
<td>23</td>
<td>23</td>
<td>223</td>
<td>germandbls</td>
<td>u00DF</td>
<td>German double s (sharp s)
</td>
</tr>
<tr VALIGN=top>
<td>24</td>
<td>24</td>
<td>224</td>
<td>agrave</td>
<td>u0061_0300</td>
<td>a grave
</td>
</tr>
<tr VALIGN=top>
<td>25</td>
<td>25</td>
<td>225</td>
<td>aacute</td>
<td>u0061_0301</td>
<td>a acute
</td>
</tr>
<tr VALIGN=top>
<td>26</td>
<td>26</td>
<td>226</td>
<td>acircumflex</td>
<td>u0061_0302</td>
<td>a circumflex
</td>
</tr>
<tr VALIGN=top>
<td>27</td>
<td>27</td>
<td>227</td>
<td>atilde</td>
<td>u0061_0303</td>
<td>a tilde
</td>
</tr>
<tr VALIGN=top>
<td>28</td>
<td>28</td>
<td>228</td>
<td>adieresis</td>
<td>u0061_0308</td>
<td>a dieresis (umlaut)
</td>
</tr>
<tr VALIGN=top>
<td>29</td>
<td>29</td>
<td>229</td>
<td>aring</td>
<td>u0061_030A</td>
<td>a ring
</td>
</tr>
<tr VALIGN=top>
<td>30</td>
<td>30</td>
<td>230</td>
<td>ae</td>
<td>u00E6</td>
<td>a+e combined
</td>
</tr>
<tr VALIGN=top>
<td>31</td>
<td>31</td>
<td>231</td>
<td>ccedilla</td>
<td>u0063_0327</td>
<td>c cedilla
</td>
</tr>
<tr VALIGN=top>
<td>32</td>
<td>32</td>
<td>232</td>
<td>egrave</td>
<td>u0065_0300</td>
<td>e grave
</td>
</tr>
<tr VALIGN=top>
<td>33</td>
<td>33</td>
<td>233</td>
<td>eacute</td>
<td>u0065_0301</td>
<td>e acute
</td>
</tr>
<tr VALIGN=top>
<td>34</td>
<td>34</td>
<td>234</td>
<td>ecircumflex</td>
<td>u0065_0302</td>
<td>e circumflex
</td>
</tr>
<tr VALIGN=top>
<td>35</td>
<td>35</td>
<td>235</td>
<td>edieresis</td>
<td>u0065_0308</td>
<td>e dieresis (umlaut)
</td>
</tr>
<tr VALIGN=top>
<td>36</td>
<td>36</td>
<td>236</td>
<td>igrave</td>
<td>u0069_0300</td>
<td>i grave
</td>
</tr>
<tr VALIGN=top>
<td>37</td>
<td>37</td>
<td>237</td>
<td>iacute</td>
<td>u0069_0301</td>
<td>i acute
</td>
</tr>
<tr VALIGN=top>
<td>38</td>
<td>38</td>
<td>238</td>
<td>icircumflex</td>
<td>u0069_0302</td>
<td>i circumflex
</td>
</tr>
<tr VALIGN=top>
<td>39</td>
<td>39</td>
<td>239</td>
<td>idieresis</td>
<td>u0069_0308</td>
<td>i dieresis (umlaut)
</td>
</tr>
<tr VALIGN=top>
<td>40</td>
<td>40</td>
<td>240</td>
<td>eth</td>
<td>u00F0</td>
<td>e th
</td>
</tr>
<tr VALIGN=top>
<td>41</td>
<td>41</td>
<td>241</td>
<td>ntilde</td>
<td>u006E_0303</td>
<td>n tilde
</td>
</tr>
<tr VALIGN=top>
<td>42</td>
<td>42</td>
<td>242</td>
<td>ograve</td>
<td>u006F_0300</td>
<td>o grave
</td>
</tr>
<tr VALIGN=top>
<td>43</td>
<td>43</td>
<td>243</td>
<td>oacute</td>
<td>u006F_0301</td>
<td>o acute
</td>
</tr>
<tr VALIGN=top>
<td>44</td>
<td>44</td>
<td>244</td>
<td>ocircumflex</td>
<td>u006F_0302</td>
<td>o circumflex
</td>
</tr>
<tr VALIGN=top>
<td>45</td>
<td>45</td>
<td>245</td>
<td>otilde</td>
<td>u006F_0303</td>
<td>o tilde
</td>
</tr>
<tr VALIGN=top>
<td>46</td>
<td>46</td>
<td>246</td>
<td>odieresis</td>
<td>u006F_0308</td>
<td>o dieresis (umlaut)
</td>
</tr>
<tr VALIGN=top>
<td>47</td>
<td>47</td>
<td>247</td>
<td>divide</td>
<td>u00F7</td>
<td>divide
</td>
</tr>
<tr VALIGN=top>
<td>48</td>
<td>48</td>
<td>248</td>
<td>oslash</td>
<td>u00F8</td>
<td>o slash
</td>
</tr>
<tr VALIGN=top>
<td>49</td>
<td>49</td>
<td>249</td>
<td>ugrave</td>
<td>u0075_0300</td>
<td>u grave
</td>
</tr>
<tr VALIGN=top>
<td>50</td>
<td>50</td>
<td>250</td>
<td>uacute</td>
<td>u0075_0301</td>
<td>u acute
</td>
</tr>
<tr VALIGN=top>
<td>51</td>
<td>51</td>
<td>251</td>
<td>ucircumflex</td>
<td>u0075_0302</td>
<td>u circumflex
</td>
</tr>
<tr VALIGN=top>
<td>52</td>
<td>52</td>
<td>252</td>
<td>udieresis</td>
<td>u0075_0308</td>
<td>u dieresis (umlaut)
</td>
</tr>
<tr VALIGN=top>
<td>53</td>
<td>53</td>
<td>253</td>
<td>yacute</td>
<td>u0079_0301</td>
<td>y acute
</td>
</tr>
<tr VALIGN=top>
<td>54</td>
<td>54</td>
<td>254</td>
<td>thorn</td>
<td>u00FE</td>
<td>thorn
</td>
</tr>
<tr VALIGN=top>
<td>55</td>
<td>55</td>
<td>255</td>
<td>ydieresis</td>
<td>u0079_0308</td>
<td>y dieresis (umlaut)
</td>
</tr>
</table>
<h3>Named Glyphs</h3>
<p>Glyph names can be embedded into the document text by using escape sequences. <code><a href="/docs/linux/man/7-groff/">groff</a></code>(7) describes how these escape sequences look. Glyph names can consist of quite arbitrary characters from the ASCII or latin1 code set, not only alphanumeric characters. Here some examples:</p>
<dl>
<dt><tt>\(</tt><i>ch</i></p>
<dd>A glyph having the 2-character name <i>ch</i>.</p>
<dt><tt>\[</tt>,<i>char_name/</i><tt>]</tt></p>
<dd>A glyph having the name <i>char_name</i> (having length 1, 2, 3, &#8230;). Note that &#8216;<i>c</i>&#8216; is not the same as &#8216;<tt>\[</tt>,<i>c/</i><tt>]</tt>&#8216; (,<i>c</i>&nbsp;a single character): The latter is internally mapped to glyph name &#8216;\<i>c</i>&#8216;. By default, groff defines a single glyph name starting with a backslash, namely &#8216;\-&#8216;, which can be either accessed as &#8216;<tt>\-</tt>&#8216; or &#8216;<tt>\[-]</tt>&#8216;.</p>
<dt><tt>\[</tt>,<i>base_glyph composite_1 composite_2 &#8230;/</i><tt>]</tt></p>
<dd>A composite glyph; see below for a more detailed description.</dl>
<p> In groff, each 8-bit input character can also referred to by the construct &#8216;<tt>\[char</tt>,<i>n/</i><tt>]</tt>&#8216; where <i>n</i> is the decimal code of the character, a number between 0 and 255 without leading zeros (those entities are <i>not</i> glyph names). They are normally mapped onto glyphs using the <tt>.trin</tt> request. </p>
<p> Another special convention is the handling of glyphs with names directly derived from a Unicode code point; this is shown in the &#8216;Unicode&#8217; column of the table below. In general, all glyphs not having a name as listed in this manual page can be accessed with the &#8216;<tt>\[u</tt>,<i>XXXX/</i><tt>]</tt>&#8216; construct. Refer to section &#8220;Using Symbols&#8221; in <i>Groff: The GNU Implementation of troff</i>, the <i>groff</i> Texinfo manual, which describes how <i>groff</i> glyph names are constructed. </p>
<p> Moreover, new glyph names can be created by the <tt>.char</tt> request; see <code><a href="/docs/linux/man/7-groff/">groff</a></code>(7). </p>
<p> In the following, a plus sign &#8216;+&#8217; in the &#8216;Notes&#8217; column indicates that this particular glyph name appears in the PS version of the original troff documentation, CSTR 54. </p>
<p> Entries marked with &#8216;***&#8217; denote glyphs for mathematical purposes (mainly used for DVI output). Normally, such glyphs have metrics which make them unusable in normal text. </p>
<table>
<tr VALIGN=top>
<td>Output</td>
<td>Input</td>
<td>PostScript</td>
<td>Unicode</td>
<td>Notes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>&ETH;</td>
<td>\[-D]</td>
<td>Eth</td>
<td>u00D0</td>
<td>uppercase eth
</td>
</tr>
<tr VALIGN=top>
<td>&eth;</td>
<td>\[Sd]</td>
<td>eth</td>
<td>u00F0</td>
<td>lowercase eth
</td>
</tr>
<tr VALIGN=top>
<td>&THORN;</td>
<td>\[TP]</td>
<td>Thorn</td>
<td>u00DE</td>
<td>uppercase thorn
</td>
</tr>
<tr VALIGN=top>
<td>&thorn;</td>
<td>\[Tp]</td>
<td>thorn</td>
<td>u00FE</td>
<td>lowercase thorn
</td>
</tr>
<tr VALIGN=top>
<td>&szlig;</td>
<td>\[ss]</td>
<td>germandbls</td>
<td>u00DF</td>
<td>German double s (sharp s)
</td>
</tr>
</table>
<p> <i>Ligatures and Other Latin Glyphs</i> </p>
<table>
<tr VALIGN=top>
<td>Output</td>
<td>Input</td>
<td>PostScript</td>
<td>Unicode</td>
<td>Notes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>ff</td>
<td>\[ff]</td>
<td>ff</td>
<td>u0066_0066</td>
<td>ff ligature +
</td>
</tr>
<tr VALIGN=top>
<td>fi</td>
<td>\[fi]</td>
<td>fi</td>
<td>u0066_0069</td>
<td>fi ligature +
</td>
</tr>
<tr VALIGN=top>
<td>fl</td>
<td>\[fl]</td>
<td>fl</td>
<td>u0066_006C</td>
<td>fl ligature +
</td>
</tr>
<tr VALIGN=top>
<td>ffi</td>
<td>\[Fi]</td>
<td>ffi</td>
<td>u0066_0066_0069</td>
<td>ffi ligature +
</td>
</tr>
<tr VALIGN=top>
<td>ffl</td>
<td>\[Fl]</td>
<td>ffl</td>
<td>u0066_0066_006C</td>
<td>ffl ligature +
</td>
</tr>
<tr VALIGN=top>
<td>&#x141;</td>
<td>\[/L]</td>
<td>Lslash</td>
<td>u0141</td>
<td>L slash (Polish)
</td>
</tr>
<tr VALIGN=top>
<td>&#x142;</td>
<td>\[/l]</td>
<td>lslash</td>
<td>u0142</td>
<td>l slash (Polish)
</td>
</tr>
<tr VALIGN=top>
<td>&Oslash;</td>
<td>\[/O]</td>
<td>Oslash</td>
<td>u00D8</td>
<td>O slash (Scandinavian)
</td>
</tr>
<tr VALIGN=top>
<td>&oslash;</td>
<td>\[/o]</td>
<td>oslash</td>
<td>u00F8</td>
<td>o slash (Scandinavian)
</td>
</tr>
<tr VALIGN=top>
<td>&AElig;</td>
<td>\[AE]</td>
<td>AE</td>
<td>u00C6</td>
<td>A+E combined
</td>
</tr>
<tr VALIGN=top>
<td>&aelig;</td>
<td>\[ae]</td>
<td>ae</td>
<td>u00E6</td>
<td>a+e combined
</td>
</tr>
<tr VALIGN=top>
<td>&OElig;</td>
<td>\[OE]</td>
<td>OE</td>
<td>u0152</td>
<td>O+E combined
</td>
</tr>
<tr VALIGN=top>
<td>&oelig;</td>
<td>\[oe]</td>
<td>oe</td>
<td>u0153</td>
<td>o+e combined
</td>
</tr>
<tr VALIGN=top>
<td>IJ</td>
<td>\[IJ]</td>
<td>IJ</td>
<td>u0132</td>
<td>I+J combined (Dutch)
</td>
</tr>
<tr VALIGN=top>
<td>ij</td>
<td>\[ij]</td>
<td>ij</td>
<td>u0133</td>
<td>i+j combined(Dutch)
</td>
</tr>
<tr VALIGN=top>
<td>&#x131;</td>
<td>\[.i]</td>
<td>dotlessi</td>
<td>u0131</td>
<td>i without a dot (Turkish)
</td>
</tr>
<tr VALIGN=top>
<td>.j</td>
<td>\[.j]</td>
<td>dotlessj</td>
<td>u0237</td>
<td>j without a dot
</td>
</tr>
</table>
<p> <i>Accented Characters</i> </p>
<table>
<tr VALIGN=top>
<td>Output</td>
<td>Input</td>
<td>PostScript</td>
<td>Unicode</td>
<td>Notes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>&Aacute;</td>
<td>\[&#8216;A]</td>
<td>Aacute</td>
<td>u0041_0301</td>
<td>A acute
</td>
</tr>
<tr VALIGN=top>
<td>&#8216;C</td>
<td>\[&#8216;C]</td>
<td>Cacute</td>
<td>u0043_0301</td>
<td>C acute
</td>
</tr>
<tr VALIGN=top>
<td>&Eacute;</td>
<td>\[&#8216;E]</td>
<td>Eacute</td>
<td>u0045_0301</td>
<td>E acute
</td>
</tr>
<tr VALIGN=top>
<td>&Iacute;</td>
<td>\[&#8216;I]</td>
<td>Iacute</td>
<td>u0049_0301</td>
<td>I acute
</td>
</tr>
<tr VALIGN=top>
<td>&Oacute;</td>
<td>\[&#8216;O]</td>
<td>Oacute</td>
<td>u004F_0301</td>
<td>O acute
</td>
</tr>
<tr VALIGN=top>
<td>&Uacute;</td>
<td>\[&#8216;U]</td>
<td>Uacute</td>
<td>u0055_0301</td>
<td>U acute
</td>
</tr>
<tr VALIGN=top>
<td>&Yacute;</td>
<td>\[&#8216;Y]</td>
<td>Yacute</td>
<td>u0059_0301</td>
<td>Y acute
</td>
</tr>
<tr VALIGN=top>
<td>&aacute;</td>
<td>\[&#8216;a]</td>
<td>aacute</td>
<td>u0061_0301</td>
<td>a acute
</td>
</tr>
<tr VALIGN=top>
<td>&#8216;c</td>
<td>\[&#8216;c]</td>
<td>cacute</td>
<td>u0063_0301</td>
<td>c acute
</td>
</tr>
<tr VALIGN=top>
<td>&eacute;</td>
<td>\[&#8216;e]</td>
<td>eacute</td>
<td>u0065_0301</td>
<td>e acute
</td>
</tr>
<tr VALIGN=top>
<td>&iacute;</td>
<td>\[&#8216;i]</td>
<td>iacute</td>
<td>u0069_0301</td>
<td>i acute
</td>
</tr>
<tr VALIGN=top>
<td>&oacute;</td>
<td>\[&#8216;o]</td>
<td>oacute</td>
<td>u006F_0301</td>
<td>o acute
</td>
</tr>
<tr VALIGN=top>
<td>&uacute;</td>
<td>\[&#8216;u]</td>
<td>uacute</td>
<td>u0075_0301</td>
<td>u acute
</td>
</tr>
<tr VALIGN=top>
<td>&yacute;</td>
<td>\[&#8216;y]</td>
<td>yacute</td>
<td>u0079_0301</td>
<td>y acute
</td>
</tr>
<tr VALIGN=top>
<td>&Auml;</td>
<td>\[:A]</td>
<td>Adieresis</td>
<td>u0041_0308</td>
<td>A dieresis (umlaut)
</td>
</tr>
<tr VALIGN=top>
<td>&Euml;</td>
<td>\[:E]</td>
<td>Edieresis</td>
<td>u0045_0308</td>
<td>E dieresis (umlaut)
</td>
</tr>
<tr VALIGN=top>
<td>&Iuml;</td>
<td>\[:I]</td>
<td>Idieresis</td>
<td>u0049_0308</td>
<td>I dieresis (umlaut)
</td>
</tr>
<tr VALIGN=top>
<td>&Ouml;</td>
<td>\[:O]</td>
<td>Odieresis</td>
<td>u004F_0308</td>
<td>O dieresis (umlaut)
</td>
</tr>
<tr VALIGN=top>
<td>&Uuml;</td>
<td>\[:U]</td>
<td>Udieresis</td>
<td>u0055_0308</td>
<td>U dieresis (umlaut)
</td>
</tr>
<tr VALIGN=top>
<td>:Y</td>
<td>\[:Y]</td>
<td>Ydieresis</td>
<td>u0059_0308</td>
<td>Y dieresis (umlaut)
</td>
</tr>
<tr VALIGN=top>
<td>&auml;</td>
<td>\[:a]</td>
<td>adieresis</td>
<td>u0061_0308</td>
<td>a dieresis (umlaut)
</td>
</tr>
<tr VALIGN=top>
<td>&euml;</td>
<td>\[:e]</td>
<td>edieresis</td>
<td>u0065_0308</td>
<td>e dieresis (umlaut)
</td>
</tr>
<tr VALIGN=top>
<td>&iuml;</td>
<td>\[:i]</td>
<td>idieresis</td>
<td>u0069_0308</td>
<td>i dieresis (umlaut)
</td>
</tr>
<tr VALIGN=top>
<td>&ouml;</td>
<td>\[:o]</td>
<td>odieresis</td>
<td>u006F_0308</td>
<td>o dieresis (umlaut)
</td>
</tr>
<tr VALIGN=top>
<td>&uuml;</td>
<td>\[:u]</td>
<td>udieresis</td>
<td>u0075_0308</td>
<td>u dieresis (umlaut)
</td>
</tr>
<tr VALIGN=top>
<td>&yuml;</td>
<td>\[:y]</td>
<td>ydieresis</td>
<td>u0079_0308</td>
<td>y dieresis (umlaut)
</td>
</tr>
<tr VALIGN=top>
<td>&Acirc;</td>
<td>\[^A]</td>
<td>Acircumflex</td>
<td>u0041_0302</td>
<td>A circumflex
</td>
</tr>
<tr VALIGN=top>
<td>&Ecirc;</td>
<td>\[^E]</td>
<td>Ecircumflex</td>
<td>u0045_0302</td>
<td>E circumflex
</td>
</tr>
<tr VALIGN=top>
<td>&Icirc;</td>
<td>\[^I]</td>
<td>Icircumflex</td>
<td>u0049_0302</td>
<td>I circumflex
</td>
</tr>
<tr VALIGN=top>
<td>&Ocirc;</td>
<td>\[^O]</td>
<td>Ocircumflex</td>
<td>u004F_0302</td>
<td>O circumflex
</td>
</tr>
<tr VALIGN=top>
<td>&Ucirc;</td>
<td>\[^U]</td>
<td>Ucircumflex</td>
<td>u0055_0302</td>
<td>U circumflex
</td>
</tr>
<tr VALIGN=top>
<td>&acirc;</td>
<td>\[^a]</td>
<td>acircumflex</td>
<td>u0061_0302</td>
<td>a circumflex
</td>
</tr>
<tr VALIGN=top>
<td>&ecirc;</td>
<td>\[^e]</td>
<td>ecircumflex</td>
<td>u0065_0302</td>
<td>e circumflex
</td>
</tr>
<tr VALIGN=top>
<td>&icirc;</td>
<td>\[^i]</td>
<td>icircumflex</td>
<td>u0069_0302</td>
<td>i circumflex
</td>
</tr>
<tr VALIGN=top>
<td>&ocirc;</td>
<td>\[^o]</td>
<td>ocircumflex</td>
<td>u006F_0302</td>
<td>o circumflex
</td>
</tr>
<tr VALIGN=top>
<td>&ucirc;</td>
<td>\[^u]</td>
<td>ucircumflex</td>
<td>u0075_0302</td>
<td>u circumflex
</td>
</tr>
<tr VALIGN=top>
<td>&Agrave;</td>
<td>\[`A]</td>
<td>Agrave</td>
<td>u0041_0300</td>
<td>A grave
</td>
</tr>
<tr VALIGN=top>
<td>&Egrave;</td>
<td>\[`E]</td>
<td>Egrave</td>
<td>u0045_0300</td>
<td>E grave
</td>
</tr>
<tr VALIGN=top>
<td>&Igrave;</td>
<td>\[`I]</td>
<td>Igrave</td>
<td>u0049_0300</td>
<td>I grave
</td>
</tr>
<tr VALIGN=top>
<td>&Ograve;</td>
<td>\[`O]</td>
<td>Ograve</td>
<td>u004F_0300</td>
<td>O grave
</td>
</tr>
<tr VALIGN=top>
<td>&Ugrave;</td>
<td>\[`U]</td>
<td>Ugrave</td>
<td>u0055_0300</td>
<td>U grave
</td>
</tr>
<tr VALIGN=top>
<td>&agrave;</td>
<td>\[`a]</td>
<td>agrave</td>
<td>u0061_0300</td>
<td>a grave
</td>
</tr>
<tr VALIGN=top>
<td>&egrave;</td>
<td>\[`e]</td>
<td>egrave</td>
<td>u0065_0300</td>
<td>e grave
</td>
</tr>
<tr VALIGN=top>
<td>&igrave;</td>
<td>\[`i]</td>
<td>igrave</td>
<td>u0069_0300</td>
<td>i grave
</td>
</tr>
<tr VALIGN=top>
<td>&ograve;</td>
<td>\[`o]</td>
<td>ograve</td>
<td>u006F_0300</td>
<td>o grave
</td>
</tr>
<tr VALIGN=top>
<td>&ugrave;</td>
<td>\[`u]</td>
<td>ugrave</td>
<td>u0075_0300</td>
<td>u grave
</td>
</tr>
<tr VALIGN=top>
<td>&Atilde;</td>
<td>\[~A]</td>
<td>Atilde</td>
<td>u0041_0303</td>
<td>A tilde
</td>
</tr>
<tr VALIGN=top>
<td>&Ntilde;</td>
<td>\[~N]</td>
<td>Ntilde</td>
<td>u004E_0303</td>
<td>N tilde
</td>
</tr>
<tr VALIGN=top>
<td>&Otilde;</td>
<td>\[~O]</td>
<td>Otilde</td>
<td>u004F_0303</td>
<td>O tilde
</td>
</tr>
<tr VALIGN=top>
<td>&atilde;</td>
<td>\[~a]</td>
<td>atilde</td>
<td>u0061_0303</td>
<td>a tilde
</td>
</tr>
<tr VALIGN=top>
<td>&ntilde;</td>
<td>\[~n]</td>
<td>ntilde</td>
<td>u006E_0303</td>
<td>n tilde
</td>
</tr>
<tr VALIGN=top>
<td>&otilde;</td>
<td>\[~o]</td>
<td>otilde</td>
<td>u006F_0303</td>
<td>o tilde
</td>
</tr>
<tr VALIGN=top>
<td>vS</td>
<td>\[vS]</td>
<td>Scaron</td>
<td>u0053_030C</td>
<td>S caron
</td>
</tr>
<tr VALIGN=top>
<td>vs</td>
<td>\[vs]</td>
<td>scaron</td>
<td>u0073_030C</td>
<td>s caron
</td>
</tr>
<tr VALIGN=top>
<td>vZ</td>
<td>\[vZ]</td>
<td>Zcaron</td>
<td>u005A_030C</td>
<td>Z caron
</td>
</tr>
<tr VALIGN=top>
<td>vz</td>
<td>\[vz]</td>
<td>zcaron</td>
<td>u007A_030C</td>
<td>z caron
</td>
</tr>
<tr VALIGN=top>
<td>&Ccedil;</td>
<td>\[,C]</td>
<td>Ccedilla</td>
<td>u0043_0327</td>
<td>C cedilla
</td>
</tr>
<tr VALIGN=top>
<td>&ccedil;</td>
<td>\[,c]</td>
<td>ccedilla</td>
<td>u0063_0327</td>
<td>c cedilla
</td>
</tr>
<tr VALIGN=top>
<td>&Aring;</td>
<td>\[oA]</td>
<td>Aring</td>
<td>u0041_030A</td>
<td>A ring
</td>
</tr>
<tr VALIGN=top>
<td>&aring;</td>
<td>\[oa]</td>
<td>aring</td>
<td>u0061_030A</td>
<td>a ring
</td>
</tr>
</table>
<p> <i>Accents</i> </p>
<p> The <code>composite</code> request is used to map most of the accents to non-spacing glyph names; the values given in parentheses are the original (spacing) ones. </p>
<table>
<tr VALIGN=top>
<td>Output</td>
<td>Input</td>
<td>PostScript</td>
<td>Unicode</td>
<td>Notes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>a&#8221;</td>
<td>\[a&quot;]</td>
<td>hungarumlaut</td>
<td>u030B (u02DD)</td>
<td>Hungarian umlaut
</td>
</tr>
<tr VALIGN=top>
<td>a-</td>
<td>\[a-]</td>
<td>macron</td>
<td>u0304 (u00AF)</td>
<td>overbar accent
</td>
</tr>
<tr VALIGN=top>
<td>a.</td>
<td>\[a.]</td>
<td>dotaccent</td>
<td>u0307 (u02D9)</td>
<td>dot accent
</td>
</tr>
<tr VALIGN=top>
<td>a^</td>
<td>\[a^]</td>
<td>circumflex</td>
<td>u0302 (u005E)</td>
<td>circumflex accent
</td>
</tr>
<tr VALIGN=top>
<td>&acute;</td>
<td>\[aa]</td>
<td>acute</td>
<td>u0301 (u00B4)</td>
<td>acute accent +
</td>
</tr>
<tr VALIGN=top>
<td>`</td>
<td>\[ga]</td>
<td>grave</td>
<td>u0300 (u0060)</td>
<td>grave accent +
</td>
</tr>
<tr VALIGN=top>
<td>ab</td>
<td>\[ab]</td>
<td>breve</td>
<td>u0306 (u02D8)</td>
<td>breve accent
</td>
</tr>
<tr VALIGN=top>
<td>ac</td>
<td>\[ac]</td>
<td>cedilla</td>
<td>u0327 (u00B8)</td>
<td>cedilla accent
</td>
</tr>
<tr VALIGN=top>
<td>ad</td>
<td>\[ad]</td>
<td>dieresis</td>
<td>u0308 (u00A8)</td>
<td>umlaut accent
</td>
</tr>
<tr VALIGN=top>
<td>ah</td>
<td>\[ah]</td>
<td>caron</td>
<td>u030C (u02C7)</td>
<td>caron accent
</td>
</tr>
<tr VALIGN=top>
<td>ao</td>
<td>\[ao]</td>
<td>ring</td>
<td>u030A (u02DA)</td>
<td>small circle, ring accent
</td>
</tr>
<tr VALIGN=top>
<td>~</td>
<td>\[a~]</td>
<td>tilde</td>
<td>u0303 (u007E)</td>
<td>tilde accent
</td>
</tr>
<tr VALIGN=top>
<td>ho</td>
<td>\[ho]</td>
<td>ogonek</td>
<td>u0328 (u02DB)</td>
<td>hook accent
</td>
</tr>
<tr VALIGN=top>
<td>ha</td>
<td>\[ha]</td>
<td>asciicircum</td>
<td>u005E</td>
<td> high circumflex, ASCII character, in mathematics the power sign
</td>
</tr>
<tr VALIGN=top>
<td>~</td>
<td>\[ti]</td>
<td>asciitilde</td>
<td>u007E</td>
<td> tilde in vertical middle, ASCII, in Unix-like the home directory
</td>
</tr>
</table>
<p> <i>Quotes</i> </p>
<table>
<tr VALIGN=top>
<td>Output</td>
<td>Input</td>
<td>PostScript</td>
<td>Unicode</td>
<td>Notes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Bq</td>
<td>\[Bq]</td>
<td>quotedblbase</td>
<td>u201E</td>
<td>low double comma quote
</td>
</tr>
<tr VALIGN=top>
<td>bq</td>
<td>\[bq]</td>
<td>quotesinglbase</td>
<td>u201A</td>
<td>low single comma quote
</td>
</tr>
<tr VALIGN=top>
<td>&#8220;</td>
<td>\[lq]</td>
<td>quotedblleft</td>
<td>u201C</td>
<td>left double quote
</td>
</tr>
<tr VALIGN=top>
<td>&#8220;</td>
<td>\[rq]</td>
<td>quotedblright</td>
<td>u201D</td>
<td>right double quote
</td>
</tr>
<tr VALIGN=top>
<td>&#8216;</td>
<td>\[oq]</td>
<td>quoteleft</td>
<td>u2018</td>
<td>single open (left) quote
</td>
</tr>
<tr VALIGN=top>
<td>&#8216;</td>
<td>\[cq]</td>
<td>quoteright</td>
<td>u2019</td>
<td>single closing (right) quote
</td>
</tr>
<tr VALIGN=top>
<td>&#8216;</td>
<td>\[aq]</td>
<td>quotesingle</td>
<td>u0027</td>
<td>apostrophe quote (ASCII 39)
</td>
</tr>
<tr VALIGN=top>
<td>&quot;</td>
<td>\[dq]</td>
<td>quotedbl</td>
<td>u0022</td>
<td>double quote (ASCII 34)
</td>
</tr>
<tr VALIGN=top>
<td>&laquo;</td>
<td>\[Fo]</td>
<td>guillemotleft</td>
<td>u00AB</td>
<td>left guillemet [sic]
</td>
</tr>
<tr VALIGN=top>
<td>&raquo;</td>
<td>\[Fc]</td>
<td>guillemotright</td>
<td>u00BB</td>
<td>right guillemet [sic]
</td>
</tr>
<tr VALIGN=top>
<td>&lsaquo;</td>
<td>\[fo]</td>
<td>guilsinglleft</td>
<td>u2039</td>
<td> single left-pointing angle quotation mark
</td>
</tr>
<tr VALIGN=top>
<td>&rsaquo;</td>
<td>\[fc]</td>
<td>guilsinglright</td>
<td>u203A</td>
<td> single right-pointing angle quotation mark
</td>
</tr>
</table>
<p> <i>Punctuation</i> </p>
<table>
<tr VALIGN=top>
<td>Output</td>
<td>Input</td>
<td>PostScript</td>
<td>Unicode</td>
<td>Notes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>&iexcl;</td>
<td>\[r!]</td>
<td>exclamdown</td>
<td>u00A1</td>
<td>inverted exclamation mark
</td>
</tr>
<tr VALIGN=top>
<td>&iquest;</td>
<td>\[r?]</td>
<td>questiondown</td>
<td>u00BF</td>
<td>inverted question mark
</td>
</tr>
<tr VALIGN=top>
<td>&#8212;</td>
<td>\[em]</td>
<td>emdash</td>
<td>u2014</td>
<td>em-dash symbol +
</td>
</tr>
<tr VALIGN=top>
<td>&#8211;</td>
<td>\[en]</td>
<td>endash</td>
<td>u2013</td>
<td>en-dash symbol
</td>
</tr>
<tr VALIGN=top>
<td>&#8211;</td>
<td>\[hy]</td>
<td>hyphen</td>
<td>u2010</td>
<td>hyphen symbol +
</td>
</tr>
</table>
<p> <i>Brackets</i> </p>
<p> The extensible bracket pieces are font-invariant glyphs. In classical troff only one glyph was available to vertically extend brackets, braces, and parentheses: &#8216;bv&#8217;. We map it rather arbitrarily to u23AA. </p>
<p> Note that not all devices contain extensible bracket pieces which can be piled up with &#8216;<tt></tt>&#8216; due to the restrictions of the escape&#8217;s piling algorithm. A general solution to build brackets out of pieces is the following macro: </p>
<pre><dl><dt><dd>.\&quot; Make a pile centered vertically 0.5em
.\&quot; above the baseline.
.\&quot; The first argument is placed at the top.
.\&quot; The pile is returned in string 'pile'
.eo
.de pile-make
. nr pile-wd 0
. nr pile-ht 0
. ds pile-args
.
. nr pile-# 
[.$]
. while 
[pile-#] \{\
. nr pile-wd (
[pile-wd] &gt;? \w'\$[
[pile-#]]')
. nr pile-ht +(
[rst] - 
[rsb])
. as pile-args '
[rsb]u'\&quot;
. as pile-args \Z'\$[
[pile-#]]'\&quot;
. as pile-args '-
[rst]u'\&quot;
. nr pile-# -1
. \}
.
. ds pile '(-0.5m + (
[pile-ht]u / 2u))'\&quot;
. as pile \*[pile-args]\&quot;
. as pile '((
[pile-ht]u / 2u) + 0.5m)'\&quot;
. as pile \h'
[pile-wd]u'\&quot;
..
.ec
</dl></pre>
<p>Another complication is the fact that some glyphs which represent bracket pieces in original troff can be used for other mathematical symbols also, for example &#8216;lf&#8217; and &#8216;rf&#8217; which provide the &#8216;floor&#8217; operator. Other devices (most notably for DVI output) don&#8217;t unify such glyphs. For this reason, the four glyphs &#8216;lf&#8217;, &#8216;rf&#8217;, &#8216;lc&#8217;, and &#8216;rc&#8217; are not unified with similarly looking bracket pieces. In <code>groff</code>, only glyphs with long names are guaranteed to pile up correctly for all devices (provided those glyphs exist). </p>
<table>
<tr VALIGN=top>
<td>Output</td>
<td>Input</td>
<td>PostScript</td>
<td>Unicode</td>
<td>Notes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>[</td>
<td>\[lB]</td>
<td>bracketleft</td>
<td>u005B</td>
<td> left square bracket
</td>
</tr>
<tr VALIGN=top>
<td>]</td>
<td>\[rB]</td>
<td>bracketright</td>
<td>u005D</td>
<td> right square bracket
</td>
</tr>
<tr VALIGN=top>
<td>{</td>
<td>\[lC]</td>
<td>braceleft</td>
<td>u007B</td>
<td> left curly brace
</td>
</tr>
<tr VALIGN=top>
<td>}</td>
<td>\[rC]</td>
<td>braceright</td>
<td>u007D</td>
<td> right curly brace
</td>
</tr>
<tr VALIGN=top>
<td>&lt;</td>
<td>\[la]</td>
<td>angleleft</td>
<td>u27E8</td>
<td> left angle bracket
</td>
</tr>
<tr VALIGN=top>
<td>&gt;</td>
<td>\[ra]</td>
<td>angleright</td>
<td>u27E9</td>
<td> right angle bracket
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>|</td>
<td>\[bv]</td>
<td>braceex</td>
<td>u23AA</td>
<td> curly brace vertical extension *** +
</td>
</tr>
<tr VALIGN=top>
<td>ex</td>
<td>\[braceex]</td>
<td>braceex</td>
<td>u23AA</td>
<td> curly brace vertical extension
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>tp</td>
<td>\[bracketlefttp]</td>
<td>bracketlefttp</td>
<td>u23A1</td>
<td> left square bracket top
</td>
</tr>
<tr VALIGN=top>
<td>bt</td>
<td>\[bracketleftbt]</td>
<td>bracketleftbt</td>
<td>u23A3</td>
<td> left square bracket bottom
</td>
</tr>
<tr VALIGN=top>
<td>ex</td>
<td>\[bracketleftex]</td>
<td>bracketleftex</td>
<td>u23A2</td>
<td> left square bracket extension
</td>
</tr>
<tr VALIGN=top>
<td>tp</td>
<td>\[bracketrighttp]</td>
<td>bracketrighttp</td>
<td>u23A4</td>
<td> right square bracket top
</td>
</tr>
<tr VALIGN=top>
<td>bt</td>
<td>\[bracketrightbt]</td>
<td>bracketrightbt</td>
<td>u23A6</td>
<td> right square bracket bottom
</td>
</tr>
<tr VALIGN=top>
<td>ex</td>
<td>\[bracketrightex]</td>
<td>bracketrightex</td>
<td>u23A5</td>
<td> right square bracket extension
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>lt</td>
<td>\[lt]</td>
<td>bracelefttp</td>
<td>u23A7</td>
<td> left curly brace top +
</td>
</tr>
<tr VALIGN=top>
<td>tp</td>
<td>\[bracelefttp]</td>
<td>bracelefttp</td>
<td>u23A7</td>
<td> left curly brace top
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="+2">{</font></td>
<td>\[lk]</td>
<td>braceleftmid</td>
<td>u23A8</td>
<td> left curly brace middle +
</td>
</tr>
<tr VALIGN=top>
<td>id</td>
<td>\[braceleftmid]</td>
<td>braceleftmid</td>
<td>u23A8</td>
<td> left curly brace middle
</td>
</tr>
<tr VALIGN=top>
<td>[</td>
<td>\[lb]</td>
<td>braceleftbt</td>
<td>u23A9</td>
<td> left curly brace bottom +
</td>
</tr>
<tr VALIGN=top>
<td>bt</td>
<td>\[braceleftbt]</td>
<td>braceleftbt</td>
<td>u23A9</td>
<td> left curly brace bottom
</td>
</tr>
<tr VALIGN=top>
<td>ex</td>
<td>\[braceleftex]</td>
<td>braceleftex</td>
<td>u23AA</td>
<td> left curly brace extension
</td>
</tr>
<tr VALIGN=top>
<td>rt</td>
<td>\[rt]</td>
<td>bracerighttp</td>
<td>u23AB</td>
<td> right curly brace top +
</td>
</tr>
<tr VALIGN=top>
<td>tp</td>
<td>\[bracerighttp]</td>
<td>bracerighttp</td>
<td>u23AB</td>
<td> right curly brace top
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="+2">}</font></td>
<td>\[rk]</td>
<td>bracerightmid</td>
<td>u23AC</td>
<td> right curly brace middle +
</td>
</tr>
<tr VALIGN=top>
<td>id</td>
<td>\[bracerightmid]</td>
<td>bracerightmid</td>
<td>u23AC</td>
<td> right curly brace middle
</td>
</tr>
<tr VALIGN=top>
<td>rb</td>
<td>\[rb]</td>
<td>bracerightbt</td>
<td>u23AD</td>
<td> right curly brace bottom +
</td>
</tr>
<tr VALIGN=top>
<td>bt</td>
<td>\[bracerightbt]</td>
<td>bracerightbt</td>
<td>u23AD</td>
<td> right curly brace bottom
</td>
</tr>
<tr VALIGN=top>
<td>ex</td>
<td>\[bracerightex]</td>
<td>bracerightex</td>
<td>u23AA</td>
<td> right curly brace extension
</td>
</tr>
<tr VALIGN=top>
<td>tp</td>
<td>\[parenlefttp]</td>
<td>parenlefttp</td>
<td>u239B</td>
<td> left parenthesis top
</td>
</tr>
<tr VALIGN=top>
<td>bt</td>
<td>\[parenleftbt]</td>
<td>parenleftbt</td>
<td>u239D</td>
<td> left parenthesis bottom
</td>
</tr>
<tr VALIGN=top>
<td>ex</td>
<td>\[parenleftex]</td>
<td>parenleftex</td>
<td>u239C</td>
<td> left parenthesis extension
</td>
</tr>
<tr VALIGN=top>
<td>tp</td>
<td>\[parenrighttp]</td>
<td>parenrighttp</td>
<td>u239E</td>
<td> right parenthesis top
</td>
</tr>
<tr VALIGN=top>
<td>bt</td>
<td>\[parenrightbt]</td>
<td>parenrightbt</td>
<td>u23A0</td>
<td> right parenthesis bottoom
</td>
</tr>
<tr VALIGN=top>
<td>ex</td>
<td>\[parenrightex]</td>
<td>parenrightex</td>
<td>u239F</td>
<td> right parenthesis extension
</td>
</tr>
</table>
<p> <i>Arrows</i> </p>
<table>
<tr VALIGN=top>
<td>Output</td>
<td>Input</td>
<td>PostScript</td>
<td>Unicode</td>
<td>Notes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>&larr;</td>
<td>\[&lt;-]</td>
<td>arrowleft</td>
<td>u2190</td>
<td>horizontal arrow left +
</td>
</tr>
<tr VALIGN=top>
<td>&rarr;</td>
<td>\[-&gt;]</td>
<td>arrowright</td>
<td>u2192</td>
<td>horizontal arrow right +
</td>
</tr>
<tr VALIGN=top>
<td>&harr;</td>
<td>\[&lt;&gt;]</td>
<td>arrowboth</td>
<td>u2194</td>
<td> horizontal arrow in both directions
</td>
</tr>
<tr VALIGN=top>
<td>&darr;</td>
<td>\[da]</td>
<td>arrowdown</td>
<td>u2193</td>
<td>vertical arrow down +
</td>
</tr>
<tr VALIGN=top>
<td>&uarr;</td>
<td>\[ua]</td>
<td>arrowup</td>
<td>u2191</td>
<td>vertical arrow up +
</td>
</tr>
<tr VALIGN=top>
<td>va</td>
<td>\[va]</td>
<td>arrowupdn</td>
<td>u2195</td>
<td> vertical arrow in both directions
</td>
</tr>
<tr VALIGN=top>
<td>&lArr;</td>
<td>\[lA]</td>
<td>arrowdblleft</td>
<td>u21D0</td>
<td>horizontal double arrow left
</td>
</tr>
<tr VALIGN=top>
<td>&rArr;</td>
<td>\[rA]</td>
<td>arrowdblright</td>
<td>u21D2</td>
<td>horizontal double arrow right
</td>
</tr>
<tr VALIGN=top>
<td>&hArr;</td>
<td>\[hA]</td>
<td>arrowdblboth</td>
<td>u21D4</td>
<td> horizontal double arrow in both directions
</td>
</tr>
<tr VALIGN=top>
<td>&dArr;</td>
<td>\[dA]</td>
<td>arrowdbldown</td>
<td>u21D3</td>
<td>vertical double arrow down
</td>
</tr>
<tr VALIGN=top>
<td>&uArr;</td>
<td>\[uA]</td>
<td>arrowdblup</td>
<td>u21D1</td>
<td>vertical double arrow up
</td>
</tr>
<tr VALIGN=top>
<td>vA</td>
<td>\[vA]</td>
<td>uni21D5</td>
<td>u21D5</td>
<td> vertical double arrow in both directions
</td>
</tr>
<tr VALIGN=top>
<td>an</td>
<td>\[an]</td>
<td>arrowhorizex</td>
<td>u23AF</td>
<td>horizontal arrow extension
</td>
</tr>
</table>
<p> <i>Lines</i> </p>
<p> The font-invariant glyphs &#8216;br&#8217;, &#8216;ul&#8217;, and &#8216;rn&#8217; form corners; they can be used to build boxes. Note that both the PostScript and the Unicode-derived names of these three glyphs are just rough approximations. </p>
<p> &#8216;rn&#8217; also serves in classical troff as the horizontal extension of the square root sign. </p>
<p> &#8216;ru&#8217; is a font-invariant glyph, namely a rule of length 0.5m. </p>
<table>
<tr VALIGN=top>
<td>Output</td>
<td>Input</td>
<td>PostScript</td>
<td>Unicode</td>
<td>Notes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>|</td>
<td>\[ba]</td>
<td>bar</td>
<td>u007C</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>|</td>
<td>\[br]</td>
<td>SF110000</td>
<td>u2502</td>
<td>box rule +
</td>
</tr>
<tr VALIGN=top>
<td>_</td>
<td>\[ul]</td>
<td>underscore</td>
<td>u005F</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&#175;</td>
<td>\[rn]</td>
<td>overline</td>
<td>u203E</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>_</td>
<td>\[ru]</td>
<td>&#8212;</td>
<td>&#8212;</td>
<td>baseline rule +
</td>
</tr>
<tr VALIGN=top>
<td>|</td>
<td>\[bb]</td>
<td>brokenbar</td>
<td>u00A6</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>/</td>
<td>\[sl]</td>
<td>slash</td>
<td>u002F</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>\</td>
<td>\[rs]</td>
<td>backslash</td>
<td>u005C</td>
<td>reverse solidus
</td>
</tr>
</table>
<p> Use &#8216;<tt>\[radicalex]</tt>&#8216;, not &#8216;<tt>\[overline]</tt>&#8216;, for continuation of square root. </p>
<p> <i>Text markers</i> </p>
<table>
<tr VALIGN=top>
<td>Output</td>
<td>Input</td>
<td>PostScript</td>
<td>Unicode</td>
<td>Notes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>&#x25cb;</td>
<td>\[ci]</td>
<td>circle</td>
<td>u25CB</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&bull;</td>
<td>\[bu]</td>
<td>bullet</td>
<td>u2022</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>=</td>
<td>\[dd]</td>
<td>daggerdbl</td>
<td>u2021</td>
<td>double dagger sign +
</td>
</tr>
<tr VALIGN=top>
<td>&#8211;</td>
<td>\[dg]</td>
<td>dagger</td>
<td>u2020</td>
<td>dagger +
</td>
</tr>
<tr VALIGN=top>
<td>&loz;</td>
<td>\[lz]</td>
<td>lozenge</td>
<td>u25CA</td>
<td>lozenge, diamond, pound key
</td>
</tr>
<tr VALIGN=top>
<td>&#x25a1;</td>
<td>\[sq]</td>
<td>uni25A1</td>
<td>u25A1</td>
<td>white square +
</td>
</tr>
<tr VALIGN=top>
<td>&para;</td>
<td>\[ps]</td>
<td>paragraph</td>
<td>u00B6</td>
<td>end of paragraph marker
</td>
</tr>
<tr VALIGN=top>
<td>&#167;</td>
<td>\[sc]</td>
<td>section</td>
<td>u00A7</td>
<td>section sign +
</td>
</tr>
<tr VALIGN=top>
<td>&#x261a;</td>
<td>\[lh]</td>
<td>uni261C</td>
<td>u261C</td>
<td>hand pointing left +
</td>
</tr>
<tr VALIGN=top>
<td>&#x261b;</td>
<td>\[rh]</td>
<td>a14</td>
<td>u261E</td>
<td>hand pointing right +
</td>
</tr>
<tr VALIGN=top>
<td>@</td>
<td>\[at]</td>
<td>at</td>
<td>u0040</td>
<td>at
</td>
</tr>
<tr VALIGN=top>
<td>#</td>
<td>\[sh]</td>
<td>numbersign</td>
<td>u0023</td>
<td>number sign
</td>
</tr>
<tr VALIGN=top>
<td>&#x240d;</td>
<td>\[CR]</td>
<td>carriagereturn</td>
<td>u21B5</td>
<td>carriage return
</td>
</tr>
<tr VALIGN=top>
<td>OK</td>
<td>\[OK]</td>
<td>a19</td>
<td>u2713</td>
<td>check mark, tick
</td>
</tr>
</table>
<p> <i>Legal Symbols</i> </p>
<table>
<tr VALIGN=top>
<td>Output</td>
<td>Input</td>
<td>PostScript</td>
<td>Unicode</td>
<td>Notes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>&#169;</td>
<td>\[co]</td>
<td>copyright</td>
<td>u00A9</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&#174;</td>
<td>\[rg]</td>
<td>registered</td>
<td>u00AE</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&trade;</td>
<td>\[tm]</td>
<td>trademark</td>
<td>u2122</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>bs</td>
<td>\[bs]</td>
<td>&#8212;</td>
<td>&#8212;</td>
<td>AT&amp;T Bell Labs logo +
</td>
</tr>
</table>
<p> The Bell Labs logo is not supported in groff. </p>
<p> <i>Currency symbols</i> </p>
<table>
<tr VALIGN=top>
<td>Output</td>
<td>Input</td>
<td>PostScript</td>
<td>Unicode</td>
<td>Notes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>$</td>
<td>\[Do]</td>
<td>dollar</td>
<td>u0024</td>
<td>dollar
</td>
</tr>
<tr VALIGN=top>
<td>&#162;</td>
<td>\[ct]</td>
<td>cent</td>
<td>u00A2</td>
<td>cent +
</td>
</tr>
<tr VALIGN=top>
<td>&euro;</td>
<td>\[eu]</td>
<td>&#8212;</td>
<td>u20AC</td>
<td>official Euro symbol
</td>
</tr>
<tr VALIGN=top>
<td>&euro;</td>
<td>\[Eu]</td>
<td>Euro</td>
<td>u20AC</td>
<td>font-specific Euro glyph variant
</td>
</tr>
<tr VALIGN=top>
<td>&yen;</td>
<td>\[Ye]</td>
<td>yen</td>
<td>u00A5</td>
<td>Japanese Yen
</td>
</tr>
<tr VALIGN=top>
<td>&pound;</td>
<td>\[Po]</td>
<td>sterling</td>
<td>u00A3</td>
<td>pound sterling (British)
</td>
</tr>
<tr VALIGN=top>
<td>&curren;</td>
<td>\[Cs]</td>
<td>currency</td>
<td>u00A4</td>
<td>Scandinavian currency sign
</td>
</tr>
<tr VALIGN=top>
<td>Fn</td>
<td>\[Fn]</td>
<td>florin</td>
<td>u0192</td>
<td>Dutch currency sign
</td>
</tr>
</table>
<p> <i>Units</i> </p>
<table>
<tr VALIGN=top>
<td>Output</td>
<td>Input</td>
<td>PostScript</td>
<td>Unicode</td>
<td>Notes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>&#176;</td>
<td>\[de]</td>
<td>degree</td>
<td>u00B0</td>
<td>degree +
</td>
</tr>
<tr VALIGN=top>
<td>&permil;</td>
<td>\[%0]</td>
<td>perthousand</td>
<td>u2030</td>
<td>per thousand, per mille sign
</td>
</tr>
<tr VALIGN=top>
<td>&#180;</td>
<td>\[fm]</td>
<td>minute</td>
<td>u2032</td>
<td>arc minute sign +
</td>
</tr>
<tr VALIGN=top>
<td>sd</td>
<td>\[sd]</td>
<td>second</td>
<td>u2033</td>
<td>acr second sign
</td>
</tr>
<tr VALIGN=top>
<td>&micro;</td>
<td>\[mc]</td>
<td>mu</td>
<td>u00B5</td>
<td>mu, micro sign
</td>
</tr>
<tr VALIGN=top>
<td>Of</td>
<td>\[Of]</td>
<td>ordfeminine</td>
<td>u00AA</td>
<td>feminine ordinal (Spanish)
</td>
</tr>
<tr VALIGN=top>
<td>Om</td>
<td>\[Om]</td>
<td>ordmasculine</td>
<td>u00BA</td>
<td>masculine ordinal (Spanish)
</td>
</tr>
</table>
<p> <i>Logical Symbols</i> </p>
<table>
<tr VALIGN=top>
<td>Output</td>
<td>Input</td>
<td>PostScript</td>
<td>Unicode</td>
<td>Notes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>AN</td>
<td>\[AN]</td>
<td>logicaland</td>
<td>u2227</td>
<td>logical and
</td>
</tr>
<tr VALIGN=top>
<td>OR</td>
<td>\[OR]</td>
<td>logicalor</td>
<td>u2228</td>
<td>logical or
</td>
</tr>
<tr VALIGN=top>
<td>&#172;</td>
<td>\[no]</td>
<td>logicalnot</td>
<td>u00AC</td>
<td>logical not + ***
</td>
</tr>
<tr VALIGN=top>
<td>no</td>
<td>\[tno]</td>
<td>logicalnot</td>
<td>u00AC</td>
<td>text variant of &#8216;no&#8217;
</td>
</tr>
<tr VALIGN=top>
<td>te</td>
<td>\[te]</td>
<td>existential</td>
<td>u2203</td>
<td>there exists
</td>
</tr>
<tr VALIGN=top>
<td>fa</td>
<td>\[fa]</td>
<td>universal</td>
<td>u2200</td>
<td>for all
</td>
</tr>
<tr VALIGN=top>
<td>st</td>
<td>\[st]</td>
<td>suchthat</td>
<td>u220B</td>
<td>sucht that
</td>
</tr>
<tr VALIGN=top>
<td>3d</td>
<td>\[3d]</td>
<td>therefore</td>
<td>u2234</td>
<td>therefore
</td>
</tr>
<tr VALIGN=top>
<td>&there4;</td>
<td>\[tf]</td>
<td>therefore</td>
<td>u2234</td>
<td>therefore
</td>
</tr>
<tr VALIGN=top>
<td>|</td>
<td>\[or]</td>
<td>bar</td>
<td>u007C</td>
<td> bitwise OR operator (as used in C) +
</td>
</tr>
</table>
<p> <i>Mathematical Symbols</i> </p>
<table>
<tr VALIGN=top>
<td>Output</td>
<td>Input</td>
<td>PostScript</td>
<td>Unicode</td>
<td>Notes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>&#189;</td>
<td>\[12]</td>
<td>onehalf</td>
<td>u00BD</td>
<td>1/2 symbol +
</td>
</tr>
<tr VALIGN=top>
<td>&#188;</td>
<td>\[14]</td>
<td>onequarter</td>
<td>u00BC</td>
<td>1/4 symbol +
</td>
</tr>
<tr VALIGN=top>
<td>&#190;</td>
<td>\[34]</td>
<td>threequarters</td>
<td>u00BE</td>
<td>3/4 symbol +
</td>
</tr>
<tr VALIGN=top>
<td>18</td>
<td>\[18]</td>
<td>oneeighth</td>
<td>u215B</td>
<td>1/8 symbol
</td>
</tr>
<tr VALIGN=top>
<td>38</td>
<td>\[38]</td>
<td>threeeighths</td>
<td>u215C</td>
<td>3/8 symbol
</td>
</tr>
<tr VALIGN=top>
<td>58</td>
<td>\[58]</td>
<td>fiveeighths</td>
<td>u215D</td>
<td>5/8 symbol
</td>
</tr>
<tr VALIGN=top>
<td>78</td>
<td>\[78]</td>
<td>seveneighths</td>
<td>u215E</td>
<td>7/8 symbol
</td>
</tr>
<tr VALIGN=top>
<td>&sup1;</td>
<td>\[S1]</td>
<td>onesuperior</td>
<td>u00B9</td>
<td>superscript 1
</td>
</tr>
<tr VALIGN=top>
<td>&sup2;</td>
<td>\[S2]</td>
<td>twosuperior</td>
<td>u00B2</td>
<td>superscript 2
</td>
</tr>
<tr VALIGN=top>
<td>&sup3;</td>
<td>\[S3]</td>
<td>threesuperior</td>
<td>u00B3</td>
<td>superscript 3
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>+</td>
<td>\[pl]</td>
<td>plus</td>
<td>u002B</td>
<td>plus in special font +
</td>
</tr>
<tr VALIGN=top>
<td>&#8211;</td>
<td>\[mi]</td>
<td>minus</td>
<td>u2212</td>
<td>minus in special font +
</td>
</tr>
<tr VALIGN=top>
<td>-+</td>
<td>\[-+]</td>
<td>uni2213</td>
<td>u2213</td>
<td>minus-plus
</td>
</tr>
<tr VALIGN=top>
<td>&plusmn;</td>
<td>\[+-]</td>
<td>plusminus</td>
<td>u00B1</td>
<td>plus-minus + ***
</td>
</tr>
<tr VALIGN=top>
<td>+-</td>
<td>\[t+-]</td>
<td>plusminus</td>
<td>u00B1</td>
<td>text variant of \[+-]
</td>
</tr>
<tr VALIGN=top>
<td>pc</td>
<td>\[pc]</td>
<td>periodcentered</td>
<td>u00B7</td>
<td>period centered
</td>
</tr>
<tr VALIGN=top>
<td>md</td>
<td>\[md]</td>
<td>dotmath</td>
<td>u22C5</td>
<td>multiplication dot
</td>
</tr>
<tr VALIGN=top>
<td>&#215;</td>
<td>\[mu]</td>
<td>multiply</td>
<td>u00D7</td>
<td>multiply sign + ***
</td>
</tr>
<tr VALIGN=top>
<td>mu</td>
<td>\[tmu]</td>
<td>multiply</td>
<td>u00D7</td>
<td>text variant of \[mu]
</td>
</tr>
<tr VALIGN=top>
<td>&otimes;</td>
<td>\[c*]</td>
<td>circlemultiply</td>
<td>u2297</td>
<td>multiply sign in circle
</td>
</tr>
<tr VALIGN=top>
<td>&oplus;</td>
<td>\[c+]</td>
<td>circleplus</td>
<td>u2295</td>
<td>plus sign in circle
</td>
</tr>
<tr VALIGN=top>
<td>&#247;</td>
<td>\[di]</td>
<td>divide</td>
<td>u00F7</td>
<td>division sign + ***
</td>
</tr>
<tr VALIGN=top>
<td>di</td>
<td>\[tdi]</td>
<td>divide</td>
<td>u00F7</td>
<td>text variant of \[di]
</td>
</tr>
<tr VALIGN=top>
<td>&frasl;</td>
<td>\[f/]</td>
<td>fraction</td>
<td>u2044</td>
<td>bar for fractions
</td>
</tr>
<tr VALIGN=top>
<td>*</td>
<td>\[**]</td>
<td>asteriskmath</td>
<td>u2217</td>
<td>mathematical asterisk +
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>&le;</td>
<td>\[&lt;=]</td>
<td>lessequal</td>
<td>u2264</td>
<td>less or equal +
</td>
</tr>
<tr VALIGN=top>
<td>&ge;</td>
<td>\[&gt;=]</td>
<td>greaterequal</td>
<td>u2265</td>
<td>greater or equal +
</td>
</tr>
<tr VALIGN=top>
<td><<</td>
<td>\[&lt;&lt;]</td>
<td>uni226A</td>
<td>u226A</td>
<td>much less
</td>
</tr>
<tr VALIGN=top>
<td>>></td>
<td>\[&gt;&gt;]</td>
<td>uni226B</td>
<td>u226B</td>
<td>much greater
</td>
</tr>
<tr VALIGN=top>
<td>=</td>
<td>\[eq]</td>
<td>equal</td>
<td>u003D</td>
<td>equals in special font +
</td>
</tr>
<tr VALIGN=top>
<td>&ne;</td>
<td>\[!=]</td>
<td>notequal</td>
<td>u003D_0338</td>
<td>not equal +
</td>
</tr>
<tr VALIGN=top>
<td>&equiv;</td>
<td>\[==]</td>
<td>equivalence</td>
<td>u2261</td>
<td>equivalent +
</td>
</tr>
<tr VALIGN=top>
<td>ne</td>
<td>\[ne]</td>
<td>uni2262</td>
<td>u2261_0338</td>
<td>not equivalent
</td>
</tr>
<tr VALIGN=top>
<td>&cong;</td>
<td>\[=~]</td>
<td>congruent</td>
<td>u2245</td>
<td> congruent, approx. equal
</td>
</tr>
<tr VALIGN=top>
<td>|=</td>
<td>\[|=]</td>
<td>uni2243</td>
<td>u2243</td>
<td>asymptot. equal to +
</td>
</tr>
<tr VALIGN=top>
<td>&asymp;</td>
<td>\[ap]</td>
<td>similar</td>
<td>u223C</td>
<td>similar +
</td>
</tr>
<tr VALIGN=top>
<td>~~</td>
<td>\[~~]</td>
<td>approxequal</td>
<td>u2248</td>
<td>almost equal to
</td>
</tr>
<tr VALIGN=top>
<td>~=</td>
<td>\[~=]</td>
<td>approxequal</td>
<td>u2248</td>
<td>almost equal to
</td>
</tr>
<tr VALIGN=top>
<td>pt</td>
<td>\[pt]</td>
<td>proportional</td>
<td>u221D</td>
<td>proportional +
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>&#216;</td>
<td>\[es]</td>
<td>emptyset</td>
<td>u2205</td>
<td>empty set +
</td>
</tr>
<tr VALIGN=top>
<td>mo</td>
<td>\[mo]</td>
<td>element</td>
<td>u2208</td>
<td>element of a set +
</td>
</tr>
<tr VALIGN=top>
<td>nm</td>
<td>\[nm]</td>
<td>notelement</td>
<td>u2208_0338</td>
<td>not element of set
</td>
</tr>
<tr VALIGN=top>
<td>sb</td>
<td>\[sb]</td>
<td>propersubset</td>
<td>u2282</td>
<td>proper subset +
</td>
</tr>
<tr VALIGN=top>
<td>nb</td>
<td>\[nb]</td>
<td>notsubset</td>
<td>u2282_0338</td>
<td>not supset
</td>
</tr>
<tr VALIGN=top>
<td>sp</td>
<td>\[sp]</td>
<td>propersuperset</td>
<td>u2283</td>
<td>proper superset +
</td>
</tr>
<tr VALIGN=top>
<td>nc</td>
<td>\[nc]</td>
<td>uni2285</td>
<td>u2283_0338</td>
<td>not superset
</td>
</tr>
<tr VALIGN=top>
<td>ib</td>
<td>\[ib]</td>
<td>reflexsubset</td>
<td>u2286</td>
<td>subset or equal +
</td>
</tr>
<tr VALIGN=top>
<td>ip</td>
<td>\[ip]</td>
<td>reflexsuperset</td>
<td>u2287</td>
<td>superset or equal +
</td>
</tr>
<tr VALIGN=top>
<td>ca</td>
<td>\[ca]</td>
<td>intersection</td>
<td>u2229</td>
<td>intersection, cap +
</td>
</tr>
<tr VALIGN=top>
<td>cu</td>
<td>\[cu]</td>
<td>union</td>
<td>u222A</td>
<td>union, cup +
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>/_</td>
<td>\[/_]</td>
<td>angle</td>
<td>u2220</td>
<td>angle
</td>
</tr>
<tr VALIGN=top>
<td>pp</td>
<td>\[pp]</td>
<td>perpendicular</td>
<td>u22A5</td>
<td>perpendicular
</td>
</tr>
<tr VALIGN=top>
<td>Integral</td>
<td>\[is]</td>
<td>integral</td>
<td>u222B</td>
<td>integral +
</td>
</tr>
<tr VALIGN=top>
<td>al</td>
<td>\[integral]</td>
<td>integral</td>
<td>u222B</td>
<td>integral ***
</td>
</tr>
<tr VALIGN=top>
<td>um</td>
<td>\[sum]</td>
<td>summation</td>
<td>u2211</td>
<td>summation ***
</td>
</tr>
<tr VALIGN=top>
<td>ct</td>
<td>\[product]</td>
<td>product</td>
<td>u220F</td>
<td>product ***
</td>
</tr>
<tr VALIGN=top>
<td>ct</td>
<td>\[coproduct]</td>
<td>uni2210</td>
<td>u2210</td>
<td>coproduct ***
</td>
</tr>
<tr VALIGN=top>
<td>gr</td>
<td>\[gr]</td>
<td>gradient</td>
<td>u2207</td>
<td>gradient +
</td>
</tr>
<tr VALIGN=top>
<td>sr</td>
<td>\[sr]</td>
<td>radical</td>
<td>u221A</td>
<td>square root +
</td>
</tr>
<tr VALIGN=top>
<td>rt</td>
<td>\[sqrt]</td>
<td>radical</td>
<td>u221A</td>
<td>square root
</td>
</tr>
<tr VALIGN=top>
<td>ex</td>
<td>\[radicalex]</td>
<td>radicalex</td>
<td>&#8212;</td>
<td> square root continuation ***
</td>
</tr>
<tr VALIGN=top>
<td>ex</td>
<td>\[sqrtex]</td>
<td>radicalex</td>
<td>&#8212;</td>
<td> square root continuation ***
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>|&#175;</td>
<td>\[lc]</td>
<td>uni2308</td>
<td>u2308</td>
<td>left ceiling +
</td>
</tr>
<tr VALIGN=top>
<td>&#175;|</td>
<td>\[rc]</td>
<td>uni2309</td>
<td>u2309</td>
<td>right ceiling +
</td>
</tr>
<tr VALIGN=top>
<td>|_</td>
<td>\[lf]</td>
<td>uni230A</td>
<td>u230A</td>
<td>left floor +
</td>
</tr>
<tr VALIGN=top>
<td>_|</td>
<td>\[rf]</td>
<td>uni230B</td>
<td>u230B</td>
<td>right floor +
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>&infin;</td>
<td>\[if]</td>
<td>infinity</td>
<td>u221E</td>
<td>infinity +
</td>
</tr>
<tr VALIGN=top>
<td>&alepfsym;</td>
<td>\[Ah]</td>
<td>aleph</td>
<td>u2135</td>
<td>aleph
</td>
</tr>
<tr VALIGN=top>
<td>Im</td>
<td>\[Im]</td>
<td>Ifraktur</td>
<td>u2111</td>
<td>Gothic I, imaginary
</td>
</tr>
<tr VALIGN=top>
<td>Re</td>
<td>\[Re]</td>
<td>Rfraktur</td>
<td>u211C</td>
<td>Gothic R, real
</td>
</tr>
<tr VALIGN=top>
<td>wp</td>
<td>\[wp]</td>
<td>weierstrass</td>
<td>u2118</td>
<td>Weierstrass~p
</td>
</tr>
<tr VALIGN=top>
<td>d</td>
<td>\[pd]</td>
<td>partialdiff</td>
<td>u2202</td>
<td> partial differentiation +
</td>
</tr>
<tr VALIGN=top>
<td>-h</td>
<td>\[-h]</td>
<td>uni210F</td>
<td>u210F</td>
<td> Planck constant&nbsp;/&nbsp;2pi (h-bar)
</td>
</tr>
<tr VALIGN=top>
<td>ar</td>
<td>\[hbar]</td>
<td>uni210F</td>
<td>u210F</td>
<td> Planck constant&nbsp;/&nbsp;2pi (h-bar)
</td>
</tr>
</table>
<p> <i>Greek glyphs</i> </p>
<p> These glyphs are intended for technical use, not for real Greek; normally, the uppercase letters have upright shape, and the lowercase ones are slanted. There is a problem with the mapping of letter phi to Unicode. Prior to Unicode version 3.0, the difference between U+03C6, GREEK SMALL LETTER PHI, and U+03D5, GREEK PHI SYMBOL, was not clearly described; only the glyph shapes in the Unicode book could be used as a reference. Starting with Unicode 3.0, the reference glyphs have been exchanged and described verbally also: In mathematical context, U+03D5 is the stroked variant and U+03C6 the curly glyph. Unfortunately, most font vendors didn&#8217;t update their fonts to this (incompatible) change in Unicode. At the time of this writing (January 2006), it is not clear yet whether the Adobe Glyph Names &#8216;phi&#8217; and &#8216;phi1&#8217; also change its meaning if used for mathematics, thus compatibility problems are likely to happen &#8211; being conservative, groff currently assumes that &#8216;phi&#8217; in a PostScript symbol font is the stroked version. </p>
<p> In groff, symbol &#8216;<tt>\[*f]</tt>&#8216; always denotes the stroked version of phi, and &#8216;<tt>\[+f]</tt>&#8216; the curly variant. </p>
<table>
<tr VALIGN=top>
<td>Output</td>
<td>Input</td>
<td>PostScript</td>
<td>Unicode</td>
<td>Notes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>&Alpha;</td>
<td>\[*A]</td>
<td>Alpha</td>
<td>u0391</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&Beta;</td>
<td>\[*B]</td>
<td>Beta</td>
<td>u0392</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&Gamma;</td>
<td>\[*G]</td>
<td>Gamma</td>
<td>u0393</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&Delta;</td>
<td>\[*D]</td>
<td>Delta</td>
<td>u0394</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&Epsilon;</td>
<td>\[*E]</td>
<td>Epsilon</td>
<td>u0395</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&Zeta;</td>
<td>\[*Z]</td>
<td>Zeta</td>
<td>u0396</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&Eta;</td>
<td>\[*Y]</td>
<td>Eta</td>
<td>u0397</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&Theta;</td>
<td>\[*H]</td>
<td>Theta</td>
<td>u0398</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&Iota;</td>
<td>\[*I]</td>
<td>Iota</td>
<td>u0399</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&Kappa;</td>
<td>\[*K]</td>
<td>Kappa</td>
<td>u039A</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&Lambda;</td>
<td>\[*L]</td>
<td>Lambda</td>
<td>u039B</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&Mu;</td>
<td>\[*M]</td>
<td>Mu</td>
<td>u039C</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&Nu;</td>
<td>\[*N]</td>
<td>Nu</td>
<td>u039D</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&Xi;</td>
<td>\[*C]</td>
<td>Xi</td>
<td>u039E</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&Omicron;</td>
<td>\[*O]</td>
<td>Omicron</td>
<td>u039F</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&Pi;</td>
<td>\[*P]</td>
<td>Pi</td>
<td>u03A0</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&Rho;</td>
<td>\[*R]</td>
<td>Rho</td>
<td>u03A1</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&Sigma;</td>
<td>\[*S]</td>
<td>Sigma</td>
<td>u03A3</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&Tau;</td>
<td>\[*T]</td>
<td>Tau</td>
<td>u03A4</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&Upsilon;</td>
<td>\[*U]</td>
<td>Upsilon</td>
<td>u03A5</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&Phi;</td>
<td>\[*F]</td>
<td>Phi</td>
<td>u03A6</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&Chi;</td>
<td>\[*X]</td>
<td>Chi</td>
<td>u03A7</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&Psi;</td>
<td>\[*Q]</td>
<td>Psi</td>
<td>u03A8</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&Omega;</td>
<td>\[*W]</td>
<td>Omega</td>
<td>u03A9</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&alpha;</td>
<td>\[*a]</td>
<td>alpha</td>
<td>u03B1</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&beta;</td>
<td>\[*b]</td>
<td>beta</td>
<td>u03B2</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&gamma;</td>
<td>\[*g]</td>
<td>gamma</td>
<td>u03B3</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&delta;</td>
<td>\[*d]</td>
<td>delta</td>
<td>u03B4</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&epsilon;</td>
<td>\[*e]</td>
<td>epsilon</td>
<td>u03B5</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&zeta;</td>
<td>\[*z]</td>
<td>zeta</td>
<td>u03B6</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&eta;</td>
<td>\[*y]</td>
<td>eta</td>
<td>u03B7</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&theta;</td>
<td>\[*h]</td>
<td>theta</td>
<td>u03B8</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&iota;</td>
<td>\[*i]</td>
<td>iota</td>
<td>u03B9</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&kappa;</td>
<td>\[*k]</td>
<td>kappa</td>
<td>u03BA</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&lambda;</td>
<td>\[*l]</td>
<td>lambda</td>
<td>u03BB</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&mu;</td>
<td>\[*m]</td>
<td>mu</td>
<td>u03BC</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&nu;</td>
<td>\[*n]</td>
<td>nu</td>
<td>u03BD</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&xi;</td>
<td>\[*c]</td>
<td>xi</td>
<td>u03BE</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&omicron;</td>
<td>\[*o]</td>
<td>omicron</td>
<td>u03BF</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&pi;</td>
<td>\[*p]</td>
<td>pi</td>
<td>u03C0</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&rho;</td>
<td>\[*r]</td>
<td>rho</td>
<td>u03C1</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>s</td>
<td>\[ts]</td>
<td>sigma1</td>
<td>u03C2</td>
<td>terminal sigma +
</td>
</tr>
<tr VALIGN=top>
<td>&sigma;</td>
<td>\[*s]</td>
<td>sigma</td>
<td>u03C3</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&tau;</td>
<td>\[*t]</td>
<td>tau</td>
<td>u03C4</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&upsilon;</td>
<td>\[*u]</td>
<td>upsilon</td>
<td>u03C5</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&phi;</td>
<td>\[*f]</td>
<td>phi</td>
<td>u03D5</td>
<td>(stroked glyph) +
</td>
</tr>
<tr VALIGN=top>
<td>&chi;</td>
<td>\[*x]</td>
<td>chi</td>
<td>u03C7</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&psi;</td>
<td>\[*q]</td>
<td>psi</td>
<td>u03C8</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>&omega;</td>
<td>\[*w]</td>
<td>omega</td>
<td>u03C9</td>
<td>+
</td>
</tr>
<tr VALIGN=top>
<td>+h</td>
<td>\[+h]</td>
<td>theta1</td>
<td>u03D1</td>
<td>variant theta
</td>
</tr>
<tr VALIGN=top>
<td>+f</td>
<td>\[+f]</td>
<td>phi1</td>
<td>u03C6</td>
<td>variant phi (curly shape)
</td>
</tr>
<tr VALIGN=top>
<td>+p</td>
<td>\[+p]</td>
<td>omega1</td>
<td>u03D6</td>
<td>variant pi, looking like omega
</td>
</tr>
<tr VALIGN=top>
<td>+e</td>
<td>\[+e]</td>
<td>uni03F5</td>
<td>u03F5</td>
<td>variant epsilon
</td>
</tr>
</table>
<p> <i>Card symbols</i> </p>
<table>
<tr VALIGN=top>
<td>Output</td>
<td>Input</td>
<td>PostScript</td>
<td>Unicode</td>
<td>Notes
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>CL</td>
<td>\[CL]</td>
<td>club</td>
<td>u2663</td>
<td>black club suit
</td>
</tr>
<tr VALIGN=top>
<td>SP</td>
<td>\[SP]</td>
<td>spade</td>
<td>u2660</td>
<td>black spade suit
</td>
</tr>
<tr VALIGN=top>
<td>HE</td>
<td>\[HE]</td>
<td>heart</td>
<td>u2665</td>
<td>black heart suit
</td>
</tr>
<tr VALIGN=top>
<td>61</td>
<td>\[u2661]</td>
<td>uni2661</td>
<td>u2661</td>
<td>white heart suit
</td>
</tr>
<tr VALIGN=top>
<td>DI</td>
<td>\[DI]</td>
<td>diamond</td>
<td>u2666</td>
<td>black diamond suit
</td>
</tr>
<tr VALIGN=top>
<td>62</td>
<td>\[u2662]</td>
<td>uni2662</td>
<td>u2662</td>
<td>white diamond suit
</td>
</tr>
</table>
<h2>Authors</h2>
<p>This document was written by James Clark with additions by Werner Lemberg and Bernd Warken and revised to use real tables by Eric S. Raymond</p>
<h2>See Also</h2>
<p><i>Groff: The GNU Implementation of troff</i>, by Trent A. Fisher and Werner Lemberg, is the primary <i>groff</i> manual. Section &#8220;Using Symbols&#8221; may be of particular note. You can browse it interactively with &#8220;info &#8216;(groff)Using Symbols'&#8221;.</p>
<dl>
<dt><code><a href="/docs/linux/man/1-groff/">groff</a></code>(1)</p>
<dd>the GNU roff formatter</p>
<dt><code><a href="/docs/linux/man/7-groff/">groff</a></code>(7)</p>
<dd>a short reference of the groff formatting language</dl>
<p> <i>An extension to the troff character set for Europe</i>, E.G. Keizer, K.J. Simonsen, J. Akkerhuis; EUUG Newsletter, Volume 9, No. 2, Summer 1989 The Unicode Standard </p>
