---
title: "wnstats(7)"
name: "wnstats"
section: "7"
letter: "w"
url: "/docs/linux/man/7-wnstats/"
description: "wnstats – WordNet 3.0 database statistics"
---

<p>wnstats &#8211; WordNet 3.0 database statistics</p>
<h2>Description</h2>
<h3>Number of words, synsets, and senses</h3>
<p><center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>POS</code></td>
<td ALIGN=center><code>Unique</code></td>
<td ALIGN=center><code>Synsets</code></td>
<td ALIGN=center><code>Total</code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center></td>
<td ALIGN=center><code>Strings</code></td>
<td ALIGN=center></td>
<td ALIGN=center><code>Word-Sense Pairs</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Noun</td>
<td ALIGN=right>117798</td>
<td ALIGN=right>82115</td>
<td ALIGN=right>146312
</td>
</tr>
<tr VALIGN=top>
<td>Verb</td>
<td ALIGN=right>11529</td>
<td ALIGN=right>13767</td>
<td ALIGN=right>25047
</td>
</tr>
<tr VALIGN=top>
<td>Adjective</td>
<td ALIGN=right>21479</td>
<td ALIGN=right>18156</td>
<td ALIGN=right>30002
</td>
</tr>
<tr VALIGN=top>
<td>Adverb</td>
<td ALIGN=right>4481</td>
<td ALIGN=right>3621</td>
<td ALIGN=right>5580
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Totals</td>
<td ALIGN=right>155287</td>
<td ALIGN=right>117659</td>
<td ALIGN=right>206941
</td>
</tr>
</table>
</table>
<p></center></p>
<h3>Polysemy information</h3>
<p><center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>POS</code></td>
<td ALIGN=center><code>Monosemous</code></td>
<td ALIGN=center><code>Polysemous</code></td>
<td ALIGN=center><code>Polysemous</code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center></td>
<td ALIGN=center><code>Words and Senses</code></td>
<td ALIGN=center><code>Words</code></td>
<td ALIGN=center><code>Senses</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Noun</td>
<td ALIGN=right>101863</td>
<td ALIGN=right>15935</td>
<td ALIGN=right>44449
</td>
</tr>
<tr VALIGN=top>
<td>Verb</td>
<td ALIGN=right>6277</td>
<td ALIGN=right>5252</td>
<td ALIGN=right>18770
</td>
</tr>
<tr VALIGN=top>
<td>Adjective</td>
<td ALIGN=right>16503</td>
<td ALIGN=right>4976</td>
<td ALIGN=right>14399
</td>
</tr>
<tr VALIGN=top>
<td>Adverb</td>
<td ALIGN=right>3748</td>
<td ALIGN=right>733</td>
<td ALIGN=right>1832
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Totals</td>
<td ALIGN=right>128391</td>
<td ALIGN=right>26896</td>
<td ALIGN=right>79450
</td>
</tr>
</table>
</table>
<p></center> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>POS</code></td>
<td ALIGN=center><code>Average Polysemy</code></td>
<td ALIGN=center><code>Average Polysemy</code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center></td>
<td ALIGN=center><code>Including Monosemous Words</code></td>
<td ALIGN=center><code>Excluding Monosemous Words</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Noun</td>
<td ALIGN=right>1.24</td>
<td ALIGN=right>2.79
</td>
</tr>
<tr VALIGN=top>
<td>Verb</td>
<td ALIGN=right>2.17</td>
<td ALIGN=right>3.57
</td>
</tr>
<tr VALIGN=top>
<td>Adjective</td>
<td ALIGN=right>1.40</td>
<td ALIGN=right>2.71
</td>
</tr>
<tr VALIGN=top>
<td>Adverb</td>
<td ALIGN=right>1.25</td>
<td ALIGN=right>2.50
</td>
</tr>
</table>
</table>
<p></center> </p>
<h2>Notes</h2>
<p>Statistics for all types of adjectives and adjective satellites are combined. The total of all unique noun, verb, adjective, and adverb strings is actually 147278. However, many strings are unique within a syntactic category, but are in more than one syntactic category. The figures in the table represent the unique strings in each syntactic category. </p>
