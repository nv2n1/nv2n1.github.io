---
title: "dosfslabel(8)"
name: "dosfslabel"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dosfslabel/"
description: "fatlabel – set or get MS-DOS filesystem label or volume ID"
---

<p>fatlabel &#8211; set or get MS-DOS filesystem label or volume ID</p>
<h2>Synopsis</h2>
<p><code>fatlabel</code> [<i>OPTIONS</i>] <i>DEVICE</i> [<i>NEW</i>]</p>
<h2>Description</h2>
<p><code>fatlabel</code> will display or change the volume label or volume ID on the MS-DOS filesystem located on <i>DEVICE</i>. By default it works in label mode. It can be switched to volume ID mode with the option <code>-i</code> or <code>&#8211;volume-id</code>. </p>
<p> If <i>NEW</i> is omitted, then the existing label or volume ID is written to the standard output. A label can&#8217;t be longer than 11 bytes and should be in all upper case for best compatibility. An empty string or a label consisting only of white space is not allowed. A volume ID must be given as a hexadecimal number (no leading &quot;0x&quot; or similar) and must fit into 32 bits.</p>
<h2>Options</h2>
<dl>
<dt><code>-i</code>, <code>&#8211;volume-id</code></p>
<dd>Switch to volume ID mode.</p>
<dt><code>-r</code>, <code>&#8211;reset</code></p>
<dd>Remove label in label mode or generate new ID in volume ID mode.</p>
<dt><code>-c</code> <i>PAGE</i>, <code>&#8211;codepage</code>=<i>PAGE</i></p>
<dd>Use DOS codepage <i>PAGE</i> to encode/decode label. By default codepage 850 is used.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Display a help message and terminate.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Show version number and terminate.</dl>
<h2>COMPATIBILITY and BUGS</h2>
<p>For historic reasons FAT label is stored in two different locations: in the boot sector and as a special volume label entry in the root directory. MS-DOS 5.00, MS-DOS 6.22, MS-DOS 7.10, Windows 98, Windows XP and also Windows 10 read FAT label only from the root directory. Absence of the volume label in the root directory is interpreted as empty or none label, even if boot sector contains some valid label. </p>
<p> When Windows XP or Windows 10 system changes a FAT label it stores it only in the root directory &#8212; letting boot sector unchanged. Which leads to problems when a label is removed on Windows. Old label is still stored in the boot sector but is removed from the root directory. </p>
<p> <code>dosfslabel</code> prior to the version 3.0.7 operated only with FAT labels stored in the boot sector, completely ignoring a volume label in the root directory. </p>
<p> <code>dosfslabel</code> in versions 3.0.7-3.0.15 reads FAT labels from the root directory and in case of absence, it fallbacks to a label stored in the boot sector. Change operation resulted in updating a label in the boot sector and <i>sometimes</i> also in the root directory due to the bug. That bug was fixed in <code>dosfslabel</code> version 3.0.16 and since this version <code>dosfslabel</code> updates label in both location. </p>
<p> Since version 4.2, <code>fatlabel</code> reads a FAT label only from the root directory (like MS-DOS and Windows systems), but changes a FAT label in both locations. In version 4.2 was fixed handling of empty labels and labels which starts with a byte 0xE5. Also in this version was added support for non-ASCII labels according to the specified DOS codepage and were added checks if a new label is valid. </p>
<p> It is strongly suggested to not use <code>dosfslabel</code> prior to version 3.0.16.</p>
<h2>Dos Codepages</h2>
<p>MS-DOS and Windows systems use DOS (OEM) codepage for encoding and decoding FAT label. In Windows systems DOS codepage is global for all running applications and cannot be configured explicitly. It is set implicitly by option <i>Language for non-Unicode programs</i> available in <i>Regional and Language Options</i> via <i>Control Panel</i>. Default DOS codepage for fatlabel is 850. See following mapping table between DOS codepage and Language for non-Unicode programs: </p>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>Codepage</code></td>
<td><code>Language</code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>437</td>
<td> English (India), English (Malaysia), English (Republic of the Philippines), English (Singapore), English (South Africa), English (United States), English (Zimbabwe), Filipino, Hausa, Igbo, Inuktitut, Kinyarwanda, Kiswahili, Yoruba
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>720</td>
<td>Arabic, Dari, Persian, Urdu, Uyghur
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>737</td>
<td>Greek
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>775</td>
<td>Estonian, Latvian, Lithuanian
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>850</td>
<td> Afrikaans, Alsatian, Basque, Breton, Catalan, Corsican, Danish, Dutch, English (Australia), English (Belize), English (Canada), English (Caribbean), English (Ireland), English (Jamaica), English (New Zealand), English (Trinidad and Tobago), English (United Kingdom), Faroese, Finnish, French, Frisian, Galician, German, Greenlandic, Icelandic, Indonesian, Irish, isiXhosa, isiZulu, Italian, K&#8217;iche, Lower Sorbian, Luxembourgish, Malay, Mapudungun, Mohawk, Norwegian, Occitan, Portuguese, Quechua, Romansh, Sami, Scottish Gaelic, Sesotho sa Leboa, Setswana, Spanish, Swedish, Tamazight, Upper Sorbian, Welsh, Wolof
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>852</td>
<td> Albanian, Bosnian (Latin), Croatian, Czech, Hungarian, Polish, Romanian, Serbian (Latin), Slovak, Slovenian, Turkmen
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>855</td>
<td>Bosnian (Cyrillic), Serbian (Cyrillic)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>857</td>
<td>Azeri (Latin), Turkish, Uzbek (Latin)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>862</td>
<td>Hebrew
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>866</td>
<td> Azeri (Cyrillic), Bashkir, Belarusian, Bulgarian, Kyrgyz, Macedonian, Mongolian, Russian, Tajik, Tatar, Ukrainian, Uzbek (Cyrillic), Yakut
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>874</td>
<td>Thai
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>932</td>
<td>Japanese
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>936</td>
<td>Chinese (Simplified)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>949</td>
<td>Korean
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>950</td>
<td>Chinese (Traditional)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>1258</td>
<td>Vietnamese
</td>
</tr>
</table>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fsck-fat/">fsck.fat</a></code>(8), <code><a href="/docs/linux/man/8-mkfs-fat/">mkfs.fat</a></code>(8)</p>
<h2>Homepage</h2>
<p>The home for the <code>dosfstools</code> project is its GitHub project page</p>
<h2>Authors</h2>
<p><code>dosfstools</code> were written by Werner Almesberger Roman Hodek and others. Current maintainers are Andreas Bombe and Pali Rohár</p>
