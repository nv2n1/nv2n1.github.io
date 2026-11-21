---
title: "ascii(7)"
name: "ascii"
section: "7"
letter: "a"
url: "/docs/linux/man/7-ascii/"
description: "ascii – ASCII character set encoded in octal, decimal, and hexadecimal"
---

<p>ascii &#8211; ASCII character set encoded in octal, decimal, and hexadecimal</p>
<h2>Description</h2>
<p>ASCII is the American Standard Code for Information Interchange. It is a 7-bit code. Many 8-bit codes (e.g., ISO 8859-1) contain ASCII as their lower half. The international counterpart of ASCII is known as ISO 646-IRV. </p>
<p> The following table contains the 128 ASCII characters. </p>
<p> C program <tt>'\X'</tt> escapes are noted. </p>
<table>
<tr VALIGN=top>
<td>Oct</td>
<td>Dec</td>
<td>Hex</td>
<td>Char</td>
<td>Oct</td>
<td>Dec</td>
<td>Hex</td>
<td>Char
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=8>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>000</td>
<td>0</td>
<td>00</td>
<td>NUL &#8216;\0&#8217; (null character)</td>
<td>100</td>
<td>64</td>
<td>40</td>
<td>@
</td>
</tr>
<tr VALIGN=top>
<td>001</td>
<td>1</td>
<td>01</td>
<td>SOH (start of heading)</td>
<td>101</td>
<td>65</td>
<td>41</td>
<td>A
</td>
</tr>
<tr VALIGN=top>
<td>002</td>
<td>2</td>
<td>02</td>
<td>STX (start of text)</td>
<td>102</td>
<td>66</td>
<td>42</td>
<td>B
</td>
</tr>
<tr VALIGN=top>
<td>003</td>
<td>3</td>
<td>03</td>
<td>ETX (end of text)</td>
<td>103</td>
<td>67</td>
<td>43</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>004</td>
<td>4</td>
<td>04</td>
<td>EOT (end of transmission)</td>
<td>104</td>
<td>68</td>
<td>44</td>
<td>D
</td>
</tr>
<tr VALIGN=top>
<td>005</td>
<td>5</td>
<td>05</td>
<td>ENQ (enquiry)</td>
<td>105</td>
<td>69</td>
<td>45</td>
<td>E
</td>
</tr>
<tr VALIGN=top>
<td>006</td>
<td>6</td>
<td>06</td>
<td>ACK (acknowledge)</td>
<td>106</td>
<td>70</td>
<td>46</td>
<td>F
</td>
</tr>
<tr VALIGN=top>
<td>007</td>
<td>7</td>
<td>07</td>
<td>BEL &#8216;\a&#8217; (bell)</td>
<td>107</td>
<td>71</td>
<td>47</td>
<td>G
</td>
</tr>
<tr VALIGN=top>
<td>010</td>
<td>8</td>
<td>08</td>
<td>BS &#8216;\b&#8217; (backspace)</td>
<td>110</td>
<td>72</td>
<td>48</td>
<td>H
</td>
</tr>
<tr VALIGN=top>
<td>011</td>
<td>9</td>
<td>09</td>
<td>HT &#8216;\t&#8217; (horizontal tab)</td>
<td>111</td>
<td>73</td>
<td>49</td>
<td>I
</td>
</tr>
<tr VALIGN=top>
<td>012</td>
<td>10</td>
<td>0A</td>
<td>LF &#8216;\n&#8217; (new line)</td>
<td>112</td>
<td>74</td>
<td>4A</td>
<td>J
</td>
</tr>
<tr VALIGN=top>
<td>013</td>
<td>11</td>
<td>0B</td>
<td>VT &#8216;\v&#8217; (vertical tab)</td>
<td>113</td>
<td>75</td>
<td>4B</td>
<td>K
</td>
</tr>
<tr VALIGN=top>
<td>014</td>
<td>12</td>
<td>0C</td>
<td>FF &#8216;\f&#8217; (form feed)</td>
<td>114</td>
<td>76</td>
<td>4C</td>
<td>L
</td>
</tr>
<tr VALIGN=top>
<td>015</td>
<td>13</td>
<td>0D</td>
<td>CR &#8216;\r&#8217; (carriage ret)</td>
<td>115</td>
<td>77</td>
<td>4D</td>
<td>M
</td>
</tr>
<tr VALIGN=top>
<td>016</td>
<td>14</td>
<td>0E</td>
<td>SO (shift out)</td>
<td>116</td>
<td>78</td>
<td>4E</td>
<td>N
</td>
</tr>
<tr VALIGN=top>
<td>017</td>
<td>15</td>
<td>0F</td>
<td>SI (shift in)</td>
<td>117</td>
<td>79</td>
<td>4F</td>
<td>O
</td>
</tr>
<tr VALIGN=top>
<td>020</td>
<td>16</td>
<td>10</td>
<td>DLE (data link escape)</td>
<td>120</td>
<td>80</td>
<td>50</td>
<td>P
</td>
</tr>
<tr VALIGN=top>
<td>021</td>
<td>17</td>
<td>11</td>
<td>DC1 (device control 1)</td>
<td>121</td>
<td>81</td>
<td>51</td>
<td>Q
</td>
</tr>
<tr VALIGN=top>
<td>022</td>
<td>18</td>
<td>12</td>
<td>DC2 (device control 2)</td>
<td>122</td>
<td>82</td>
<td>52</td>
<td>R
</td>
</tr>
<tr VALIGN=top>
<td>023</td>
<td>19</td>
<td>13</td>
<td>DC3 (device control 3)</td>
<td>123</td>
<td>83</td>
<td>53</td>
<td>S
</td>
</tr>
<tr VALIGN=top>
<td>024</td>
<td>20</td>
<td>14</td>
<td>DC4 (device control 4)</td>
<td>124</td>
<td>84</td>
<td>54</td>
<td>T
</td>
</tr>
<tr VALIGN=top>
<td>025</td>
<td>21</td>
<td>15</td>
<td>NAK (negative ack.)</td>
<td>125</td>
<td>85</td>
<td>55</td>
<td>U
</td>
</tr>
<tr VALIGN=top>
<td>026</td>
<td>22</td>
<td>16</td>
<td>SYN (synchronous idle)</td>
<td>126</td>
<td>86</td>
<td>56</td>
<td>V
</td>
</tr>
<tr VALIGN=top>
<td>027</td>
<td>23</td>
<td>17</td>
<td>ETB (end of trans. blk)</td>
<td>127</td>
<td>87</td>
<td>57</td>
<td>W
</td>
</tr>
<tr VALIGN=top>
<td>030</td>
<td>24</td>
<td>18</td>
<td>CAN (cancel)</td>
<td>130</td>
<td>88</td>
<td>58</td>
<td>X
</td>
</tr>
<tr VALIGN=top>
<td>031</td>
<td>25</td>
<td>19</td>
<td>EM (end of medium)</td>
<td>131</td>
<td>89</td>
<td>59</td>
<td>Y
</td>
</tr>
<tr VALIGN=top>
<td>032</td>
<td>26</td>
<td>1A</td>
<td>SUB (substitute)</td>
<td>132</td>
<td>90</td>
<td>5A</td>
<td>Z
</td>
</tr>
<tr VALIGN=top>
<td>033</td>
<td>27</td>
<td>1B</td>
<td>ESC (escape)</td>
<td>133</td>
<td>91</td>
<td>5B</td>
<td>[
</td>
</tr>
<tr VALIGN=top>
<td>034</td>
<td>28</td>
<td>1C</td>
<td>FS (file separator)</td>
<td>134</td>
<td>92</td>
<td>5C</td>
<td>\ &#8216;\\&#8216;
</td>
</tr>
<tr VALIGN=top>
<td>035</td>
<td>29</td>
<td>1D</td>
<td>GS (group separator)</td>
<td>135</td>
<td>93</td>
<td>5D</td>
<td>]
</td>
</tr>
<tr VALIGN=top>
<td>036</td>
<td>30</td>
<td>1E</td>
<td>RS (record separator)</td>
<td>136</td>
<td>94</td>
<td>5E</td>
<td>ha
</td>
</tr>
<tr VALIGN=top>
<td>037</td>
<td>31</td>
<td>1F</td>
<td>US (unit separator)</td>
<td>137</td>
<td>95</td>
<td>5F</td>
<td>_
</td>
</tr>
<tr VALIGN=top>
<td>040</td>
<td>32</td>
<td>20</td>
<td>SPACE</td>
<td>140</td>
<td>96</td>
<td>60</td>
<td>`
</td>
</tr>
<tr VALIGN=top>
<td>041</td>
<td>33</td>
<td>21</td>
<td>!</td>
<td>141</td>
<td>97</td>
<td>61</td>
<td>a
</td>
</tr>
<tr VALIGN=top>
<td>042</td>
<td>34</td>
<td>22</td>
<td>&quot;</td>
<td>142</td>
<td>98</td>
<td>62</td>
<td>b
</td>
</tr>
<tr VALIGN=top>
<td>043</td>
<td>35</td>
<td>23</td>
<td>#</td>
<td>143</td>
<td>99</td>
<td>63</td>
<td>c
</td>
</tr>
<tr VALIGN=top>
<td>044</td>
<td>36</td>
<td>24</td>
<td>$</td>
<td>144</td>
<td>100</td>
<td>64</td>
<td>d
</td>
</tr>
<tr VALIGN=top>
<td>045</td>
<td>37</td>
<td>25</td>
<td>%</td>
<td>145</td>
<td>101</td>
<td>65</td>
<td>e
</td>
</tr>
<tr VALIGN=top>
<td>046</td>
<td>38</td>
<td>26</td>
<td>&amp;</td>
<td>146</td>
<td>102</td>
<td>66</td>
<td>f
</td>
</tr>
<tr VALIGN=top>
<td>047</td>
<td>39</td>
<td>27</td>
<td>&#8216;</td>
<td>147</td>
<td>103</td>
<td>67</td>
<td>g
</td>
</tr>
<tr VALIGN=top>
<td>050</td>
<td>40</td>
<td>28</td>
<td>(</td>
<td>150</td>
<td>104</td>
<td>68</td>
<td>h
</td>
</tr>
<tr VALIGN=top>
<td>051</td>
<td>41</td>
<td>29</td>
<td>)</td>
<td>151</td>
<td>105</td>
<td>69</td>
<td>i
</td>
</tr>
<tr VALIGN=top>
<td>052</td>
<td>42</td>
<td>2A</td>
<td>*</td>
<td>152</td>
<td>106</td>
<td>6A</td>
<td>j
</td>
</tr>
<tr VALIGN=top>
<td>053</td>
<td>43</td>
<td>2B</td>
<td>+</td>
<td>153</td>
<td>107</td>
<td>6B</td>
<td>k
</td>
</tr>
<tr VALIGN=top>
<td>054</td>
<td>44</td>
<td>2C</td>
<td>,</td>
<td>154</td>
<td>108</td>
<td>6C</td>
<td>l
</td>
</tr>
<tr VALIGN=top>
<td>055</td>
<td>45</td>
<td>2D</td>
<td>-</td>
<td>155</td>
<td>109</td>
<td>6D</td>
<td>m
</td>
</tr>
<tr VALIGN=top>
<td>056</td>
<td>46</td>
<td>2E</td>
<td>.</td>
<td>156</td>
<td>110</td>
<td>6E</td>
<td>n
</td>
</tr>
<tr VALIGN=top>
<td>057</td>
<td>47</td>
<td>2F</td>
<td>/</td>
<td>157</td>
<td>111</td>
<td>6F</td>
<td>o
</td>
</tr>
<tr VALIGN=top>
<td>060</td>
<td>48</td>
<td>30</td>
<td>0</td>
<td>160</td>
<td>112</td>
<td>70</td>
<td>p
</td>
</tr>
<tr VALIGN=top>
<td>061</td>
<td>49</td>
<td>31</td>
<td>1</td>
<td>161</td>
<td>113</td>
<td>71</td>
<td>q
</td>
</tr>
<tr VALIGN=top>
<td>062</td>
<td>50</td>
<td>32</td>
<td>2</td>
<td>162</td>
<td>114</td>
<td>72</td>
<td>r
</td>
</tr>
<tr VALIGN=top>
<td>063</td>
<td>51</td>
<td>33</td>
<td>3</td>
<td>163</td>
<td>115</td>
<td>73</td>
<td>s
</td>
</tr>
<tr VALIGN=top>
<td>064</td>
<td>52</td>
<td>34</td>
<td>4</td>
<td>164</td>
<td>116</td>
<td>74</td>
<td>t
</td>
</tr>
<tr VALIGN=top>
<td>065</td>
<td>53</td>
<td>35</td>
<td>5</td>
<td>165</td>
<td>117</td>
<td>75</td>
<td>u
</td>
</tr>
<tr VALIGN=top>
<td>066</td>
<td>54</td>
<td>36</td>
<td>6</td>
<td>166</td>
<td>118</td>
<td>76</td>
<td>v
</td>
</tr>
<tr VALIGN=top>
<td>067</td>
<td>55</td>
<td>37</td>
<td>7</td>
<td>167</td>
<td>119</td>
<td>77</td>
<td>w
</td>
</tr>
<tr VALIGN=top>
<td>070</td>
<td>56</td>
<td>38</td>
<td>8</td>
<td>170</td>
<td>120</td>
<td>78</td>
<td>x
</td>
</tr>
<tr VALIGN=top>
<td>071</td>
<td>57</td>
<td>39</td>
<td>9</td>
<td>171</td>
<td>121</td>
<td>79</td>
<td>y
</td>
</tr>
<tr VALIGN=top>
<td>072</td>
<td>58</td>
<td>3A</td>
<td>:</td>
<td>172</td>
<td>122</td>
<td>7A</td>
<td>z
</td>
</tr>
<tr VALIGN=top>
<td>073</td>
<td>59</td>
<td>3B</td>
<td>;</td>
<td>173</td>
<td>123</td>
<td>7B</td>
<td>{
</td>
</tr>
<tr VALIGN=top>
<td>074</td>
<td>60</td>
<td>3C</td>
<td>&lt;</td>
<td>174</td>
<td>124</td>
<td>7C</td>
<td>|
</td>
</tr>
<tr VALIGN=top>
<td>075</td>
<td>61</td>
<td>3D</td>
<td>= </td>
<td>175</td>
<td>125</td>
<td>7D</td>
<td>}
</td>
</tr>
<tr VALIGN=top>
<td>076</td>
<td>62</td>
<td>3E</td>
<td>&gt;</td>
<td>176</td>
<td>126</td>
<td>7E</td>
<td>~
</td>
</tr>
<tr VALIGN=top>
<td>077</td>
<td>63</td>
<td>3F</td>
<td>?</td>
<td>177</td>
<td>127</td>
<td>7F</td>
<td>DEL
</td>
</tr>
</table>
<h3>Tables</h3>
<p> For convenience, below are more compact tables in hex and decimal. </p>
<pre><code>   2 3 4 5 6 7 30 40 50 60 70 80 90 100 110 120
 ------------- ---------------------------------
0: 0 @ P ` p 0: ( 2 &lt; F P Z d n x
1: ! 1 A Q a q 1: ) 3 = G Q [ e o y
2: &quot; 2 B R b r 2: * 4 &gt; H R \ f p z
3: # 3 C S c s 3: ! + 5 ? I S ] g q {
4: $ 4 D T d t 4: &quot; , 6 @ J T ha h r |
5: % 5 E U e u 5: # - 7 A K U _ i s }
6: &amp; 6 F V f v 6: $ . 8 B L V ` j t ~
7: ' 7 G W g w 7: % / 9 C M W a k u DEL
8: ( 8 H X h x 8: &amp; 0 : D N X b l v
9: ) 9 I Y i y 9: ' 1 ; E O Y c m w
A: * : J Z j z
B: + ; K [ k {
C: , &lt; L \ l |
D: - = M ] m }
E: . &gt; N ha n ~
F: / ? O _ o DEL
</code></pre>
<h2>NOTES</h2>
<h3>History</h3>
<p> An <code>ascii</code> manual page appeared in Version 7 of AT&amp;T UNIX. </p>
<p> On older terminals, the underscore code is displayed as a left arrow, called backarrow, the caret is displayed as an up-arrow and the vertical bar has a hole in the middle. </p>
<p> Uppercase and lowercase characters differ by just one bit and the ASCII character 2 differs from the double quote by just one bit, too. That made it much easier to encode characters mechanically or with a non-microcontroller-based electronic keyboard and that pairing was found on old teletypes. </p>
<p> The ASCII standard was published by the United States of America Standards Institute (USASI) in 1968.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-charsets/">charsets</a></code>(7), <code><a href="/docs/linux/man/7-iso_8859-1/">iso_8859-1</a></code>(7), <code><a href="/docs/linux/man/7-iso_8859-2/">iso_8859-2</a></code>(7), <code><a href="/docs/linux/man/7-iso_8859-3/">iso_8859-3</a></code>(7), <code><a href="/docs/linux/man/7-iso_8859-4/">iso_8859-4</a></code>(7), <code><a href="/docs/linux/man/7-iso_8859-5/">iso_8859-5</a></code>(7), <code><a href="/docs/linux/man/7-iso_8859-6/">iso_8859-6</a></code>(7), <code><a href="/docs/linux/man/7-iso_8859-7/">iso_8859-7</a></code>(7), <code><a href="/docs/linux/man/7-iso_8859-8/">iso_8859-8</a></code>(7), <code><a href="/docs/linux/man/7-iso_8859-9/">iso_8859-9</a></code>(7), <code><a href="/docs/linux/man/7-iso_8859-10/">iso_8859-10</a></code>(7), <code><a href="/docs/linux/man/7-iso_8859-11/">iso_8859-11</a></code>(7), <code><a href="/docs/linux/man/7-iso_8859-13/">iso_8859-13</a></code>(7), <code><a href="/docs/linux/man/7-iso_8859-14/">iso_8859-14</a></code>(7), <code><a href="/docs/linux/man/7-iso_8859-15/">iso_8859-15</a></code>(7), <code><a href="/docs/linux/man/7-iso_8859-16/">iso_8859-16</a></code>(7), <code><a href="/docs/linux/man/7-utf-8/">utf-8</a></code>(7)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
