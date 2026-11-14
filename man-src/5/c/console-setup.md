---
title: "console-setup(5)"
name: "console-setup"
section: "5"
letter: "c"
url: "/docs/linux/man/5-console-setup/"
description: "console-setup – configuration file for setupcon"
---

<p>console-setup &#8211; configuration file for setupcon</p>
<h2>Description</h2>
<p>The file <code>console-setup</code> specifies the encoding and the font to be used by <code><a href="/docs/linux/man/1-setupcon/">setupcon</a></code>(1) in order to setup the console. It can be used also to specify the keyboard layout but it is not recommended to do so, use <code><a href="/docs/linux/man/5-keyboard/">keyboard</a></code>(5) instead. The font specification consists of three parameters &#8211; codeset, font face and font size. The codeset specifies what characters will be supported by the font. There isn&#8217;t one-to-one correspondence between codeset and encoding, for example the codeset <code>Lat15</code> is suitable for ISO 8859-1, ISO 8859-9 and ISO 8859-15. The codesets are two kinds &#8211; small and big. Only small codesets are supported on FreeBSD. The font face determines the general look of the font. Each font face is available in certain possible sizes. On FreeBSD only <code>8&#215;16</code>, <code>8&#215;14</code> and <code>8&#215;8</code> are valid sizes. On Linux if framebuffer is not used or <code><a href="/docs/linux/man/1-consolechars/">consolechars</a></code>(1) is installed instead of <code><a href="/docs/linux/man/1-setfont/">setfont</a></code>(1), then the permitted sizes have the form 8x<i>NUMBER</i>. The console driver of FreeBSD permits fonts in different sizes to be simultaneously loaded. Which one of them will be actually used depends on the current video mode. Therefore, on this platform the font size specification will be ignored and <code><a href="/docs/linux/man/1-setupcon/">setupcon</a></code>(1) will load the selected font face in all available sizes. The file <code>console-setup</code> consists of variable settings in <font SIZE="-1">POSIX</font> format:</p>
<dl>
<dd><i>VARIABLE</i>=&#8217;<i>VALUE</i>&#8216;</dl>
<p> Only one assignment is allowed per line. Comments (starting with &#8216;#&#8217;) are also allowed. </p>
<h2>Options</h2>
<p>The following variables can be set. </p>
<dl>
<dt><code>ACTIVE_CONSOLES</code></p>
<dd>Specifies the device files in <i>/dev</i> of the virtual terminals to be configured. File name wild-cards (<code>*</code>,&nbsp;<code>?</code>) are allowed. On Linux usually you can set this to <code>/dev/tty[1-6]</code> and on FreeBSD a sensible value is <code>/dev/ttyv[0-8]</code>. You can assign to this variable also the special value <code>guess</code>. It will cause <code><a href="/docs/linux/man/1-setupcon/">setupcon</a></code>(1) to attempt to guess the active virtual consoles by looking in configuration files such as <i>/etc/inittab</i> and <i>/etc/ttys</i>. This guessing is not always reliable. </p>
<dt><code>CHARMAP</code></p>
<dd>Specifies the desired encoding on the console. Valid values are: <code>UTF-8</code>, <code>ARMSCII-8</code>, <code>CP1251</code>, <code>CP1255</code>, <code>CP1256</code>, <code>GEORGIAN-ACADEMY</code>, <code>GEORGIAN-PS</code>, <code>IBM1133</code>, <code>ISIRI-3342</code>, <code>ISO-8859-1</code>, <code>ISO-8859-2</code>, <code>ISO-8859-3</code>, <code>ISO-8859-4</code>, <code>ISO-8859-5</code>, <code>ISO-8859-6</code>, <code>ISO-8859-7</code>, <code>ISO-8859-8</code>, <code>ISO-8859-9</code>, <code>ISO-8859-10</code>, <code>ISO-8859-11</code>, <code>ISO-8859-13</code>, <code>ISO-8859-14</code>, <code>ISO-8859-15</code>, <code>ISO-8859-16</code>, <code>KOI8-R</code>, <code>KOI8-U</code>, <code>TIS-620</code> and <code>VISCII</code>. The special value <code>guess</code> is also recognized in which case the system command <code><a href="/docs/linux/man/1-locale/">locale</a></code>(1) will be used to guess the desired encoding (currently this works reliably only with <font SIZE="-1">GNU</font> libc). </p>
<dt><code>CODESET</code></p>
<dd>In most cases the special value <code>guess</code> can be used here in which case a suitable codeset will be guessed. The codeset determines which symbols are supported by the font. Valid small codesets are: <code>Armenian</code>, <code>CyrAsia</code>, <code>CyrKoi</code>, <code>CyrSlav</code>, <code>Georgian</code>, <code>Greek</code>, <code>Hebrew</code>, <code>Lao</code>, <code>Lat15</code>, <code>Lat2</code>, <code>Lat38</code>, <code>Lat7</code> and <code>Thai</code>. Valid big codesets are: <code>Arabic</code>, <code>Ethiopian</code>, <code>Uni1</code>, <code>Uni2</code>, <code>Uni3</code> and <code>Vietnamese</code>. Only small codesets can be used on FreeBSD. See below the section entitled &#8220;CODESETS&#8221; for detailed description of each of these codesets. </p>
<dt><code>FONTFACE</code> and <code>FONTSIZE</code></p>
<dd>Valid font faces are: <code>VGA</code> (sizes <code>8&#215;8</code>, <code>8&#215;14</code>, <code>8&#215;16</code>, <code>16&#215;28</code> and <code>16&#215;32</code>), <code>Terminus</code> (sizes <code>6&#215;12</code>, <code>8&#215;14</code>, <code>8&#215;16</code>, <code>10&#215;20</code>, <code>12&#215;24</code>, <code>14&#215;28</code> and <code>16&#215;32</code>), <code>TerminusBold</code> (sizes <code>8&#215;14</code>, <code>8&#215;16</code>, <code>10&#215;20</code>, <code>12&#215;24</code>, <code>14&#215;28</code> and <code>16&#215;32</code>), <code>TerminusBoldVGA</code> (sizes <code>8&#215;14</code> and <code>8&#215;16</code>), and <code>Fixed</code> (sizes <code>8&#215;13</code>, <code>8&#215;14</code>, <code>8&#215;15</code>, <code>8&#215;16</code> and <code>8&#215;18</code>). If however <code>CODESET</code>=<code>Ethiopian</code>, then the available font faces are <code>Goha</code> and <code>GohaClassic</code>, each in sizes <code>8&#215;12</code>, <code>8&#215;14</code> and <code>8&#215;16</code>. </p>
<p> Set <code>FONTFACE</code> and <code>FONTSIZE</code> to empty strings if you want to configure only the keyboard and to leave the console font unchanged. </p>
<dt><code>VIDEOMODE</code></p>
<dd>Set <code>VIDEOMODE</code> to an empty string to avoid setting up the video mode. On FreeBSD you can run </p>
<pre>vidcontrol -i mode</pre>
<p>in order to see all possible video modes. On Linux <code><a href="/docs/linux/man/1-fbset/">fbset</a></code>(1) is used to configure the video mode but very often this doesn&#8217;t work because the default framebuffer driver (VesaFB) is rather limited and doesn&#8217;t allow changes of the video mode. </p>
<dt><code>FONT</code>, <code>FONT_MAP</code> and <code>CONSOLE_MAP</code></p>
<dd>If set, specify that a non standard font is to be used. The value of the variable <code>FONT</code> consists of one or more space separated font file names. On Linux, when the font doesn&#8217;t contain embedded Unicode map, an external map can be specified with the variable <code>FONT_MAP</code>. The value of <code>CONSOLE_MAP</code> is a file that specifies a translation map from the user&#8217;s 8-bit encoding to Unicode (Linux only) or directly to font positions. </p>
<dt><code>SCREEN_WIDTH</code> and <code>SCREEN_HEIGHT</code></p>
<dd>If set, these variables specify a screen size that <code><a href="/docs/linux/man/1-setupcon/">setupcon</a></code>(1) will enforce with <code><a href="/docs/linux/man/1-stty/">stty</a></code>(1). This can be useful with some braille devices that are only 40 cells wide. The screen size can not exceed what the current screen resolution can display according to the size of the loaded font. </p>
<dt><code>BEEP</code></p>
<dd>This variable controls the style of the system beep on the console. When unset or when <code>BEEP=default</code> no changes to the system beep will be made. Other possible values of <code>BEEP</code> are: <code>standard &#8211;</code> set a standard beep; <code>short &#8211;</code> like the standard beep but somewhat shorter; <code>shortest &#8211;</code> even more short, suitable when your work generates lots of beeps; <code>polite &#8211;</code> a very short beep with low frequency, suitable when there are other people in the room; <code>attention &#8211;</code> a very long beep, suitable when you want to warn yourself about an occurring event; <code>annoying &#8211;</code> also a long beep, suitable when you want to warn somebody else about an occurring event; and <code>off &#8211;</code> disable the system beep on the console. </p>
</dl>
<h2>Codesets</h2>
<p>There are two kinds of codesets &#8211; small (up to 256 symbols) and big (up to 512 symbols). Only small codesets can be used on FreeBSD. When the screen is in text mode (i.e. framebuffer is not used) then fonts covering big codesets will reduce the number of available foreground colors.</p>
<h3>Arabic (a big codeset)</h3>
<p>Supported languages: Arabic, Kurdish in Iran, Pashto, Persian and Urdu. </p>
<p> Completely covered by the following font faces: <code>Fixed</code> (size <code>8&#215;16</code>) and <code>VGA</code> (sizes <code>8&#215;16</code> and <code>16&#215;32</code>).</p>
<h3>Armenian</h3>
<p>Supported language: Armenian. </p>
<p> Completely covered by the following font faces: <code>Fixed</code> (all sizes).</p>
<h3>CyrAsia</h3>
<p>This codeset supports some of the non-Slavic Cyrillic languages &#8211; Abkhazia, Avaric, Azerbaijani, Bashkir, Buryat, Chechen, Chuvash, Inupiaq (Eskimo), Kara-Kalpak, Kazakh, Kirgiz, Komi, Kumyk, Kurdish, Lezghian, Mari (Cheremis), Mongolian, Ossetic, Selkup (Ostyak-Samoyed), Tajik, Tatar, Turkmen, Tuvinian, Uzbek and Yakut. </p>
<p> Completely supported by the following font faces: <code>Fixed</code> (all sizes).</p>
<h3>CyrKoi</h3>
<p>Supports entirely the 8-bit encodings KOI8-R and KOI8-U. Suitable for Russian and Ukrainian when one of these two encodings is used. </p>
<p> Completely covered by the following font faces (in all sizes): <code>Fixed</code>, <code>Terminus</code>, <code>TerminusBold</code>, <code>TerminusBoldVGA</code> and <code>VGA</code>.</p>
<h3>CyrSlav</h3>
<p>Supports entirely the 8-bit encodings ISO-8859-5 and CP1251. Suitable the Slavic Cyrillic languages &#8211; Belarusian, Bulgarian, Macedonian, Russian, Serbian and Ukrainian. For Serbian both the Cyrillic and the Latin alphabets are supported. </p>
<p> Completely covered by the following font faces: <code>Fixed</code> (all sizes), <code>Terminus</code> (all sizes), <code>TerminusBold</code> (all sizes), <code>TerminusBoldVGA</code> (all sizes), <code>VGA</code> (sizes <code>8&#215;16</code> and <code>16&#215;32</code>).</p>
<h3>Ethiopian (a big codeset)</h3>
<p>Supports Amharic, Ethiopic (Geez), Tigre and Tigrinya. </p>
<p> This codeset is partially covered by the following font faces: <code>Fixed</code> (sizes <code>8&#215;15</code> and <code>8&#215;18</code>), <code>Goha</code> (all sizes) and <code>GohaClassic</code> (all sizes).</p>
<h3>Georgian</h3>
<p>Supported language: Georgian. </p>
<p> Completely covered by the following font faces: <code>Fixed</code> (all sizes).</p>
<h3>Greek</h3>
<p>Supported language: Greek. </p>
<p> Completely covered by the following font faces: <code>Fixed</code> (all sizes) and <code>VGA</code> (sizes <code>8&#215;16</code> and <code>16&#215;32</code>).</p>
<h3>Hebrew</h3>
<p>Supported languages: Hebrew and Yiddish. </p>
<p> Completely covered by the following font faces: <code>Fixed</code> (sizes <code>8&#215;13</code>, <code>8&#215;15</code>, <code>8&#215;16</code> and <code>8&#215;18</code>) and <code>VGA</code> (sizes <code>8&#215;16</code> and <code>16&#215;32</code>).</p>
<h3>Lao</h3>
<p>Supported languages: Lao. </p>
<p> Completely covered by the following font faces: <code>Fixed</code> (sizes <code>8&#215;15</code> and <code>8&#215;16</code>).</p>
<h3>Lat15</h3>
<p>Covers entirely ISO-8859-1, ISO-8859-9 and ISO-8859-15. Suitable for the so called Latin1 and Latin5 languages &#8211; Afar, Afrikaans, Albanian, Aragonese, Asturian, Aymara, Basque, Bislama, Breton, Catalan, Chamorro, Danish, Dutch, English, Estonian, Faroese, Fijian, Finnish, French, Frisian, Friulian, Galician, German, Hiri Motu, Icelandic, Ido, Indonesian, Interlingua, Interlingue, Italian, Low Saxon, Lule Sami, Luxembourgish, Malagasy, Manx Gaelic, Norwegian Bokmal, Norwegian Nynorsk, Occitan, Oromo or Galla, Portuguese, Rhaeto-Romance (Romansch), Scots Gaelic, Somali, South Sami, Spanish, Swahili, Swedish, Tswana, Turkish, Volapuk, Votic, Walloon, Xhosa, Yapese and Zulu. </p>
<p> Completely covered by the following font faces: <code>Fixed</code> (all sizes), <code>Terminus</code> (all sizes), <code>TerminusBold</code> (all sizes), <code>TerminusBoldVGA</code> (all sizes), <code>VGA</code> (sizes <code>8&#215;16</code> and <code>16&#215;32</code>).</p>
<h3>Lat2</h3>
<p>Covers entirely ISO-8859-2. The Euro sign and the Romanian letters with comma below are also supported. Suitable for the so called Latin2 languages &#8211; Bosnian, Croatian, Czech, Hungarian, Polish, Romanian, Slovak, Slovenian and Sorbian (lower and upper). </p>
<p> Completely covered by the following font faces: <code>Fixed</code> (all sizes), <code>Terminus</code> (all sizes), <code>TerminusBold</code> (all sizes), <code>TerminusBoldVGA</code> (all sizes), <code>VGA</code> (sizes <code>8&#215;16</code> and <code>16&#215;32</code>).</p>
<h3>Lat38</h3>
<p>Covers entirely ISO-8859-3 and ISO-8859-14. Suitable for Chichewa Esperanto, Irish, Maltese and Welsh. </p>
<p> Completely covered by the following font faces: <code>Fixed</code> (all sizes) and <code>VGA</code> (sizes <code>8&#215;16</code> and <code>16&#215;32</code>).</p>
<h3>Lat7</h3>
<p>Covers entirely ISO-8859-13. Suitable for Lithuanian, Latvian, Maori and Marshallese. </p>
<p> Completely covered by the following font faces: <code>Fixed</code> (all sizes), <code>Terminus</code> (all sizes), <code>TerminusBold</code> (all sizes), <code>TerminusBoldVGA</code> (all sizes), <code>VGA</code> (sizes <code>8&#215;16</code> and <code>16&#215;32</code>).</p>
<h3>Thai</h3>
<p>Supported language: Thai. </p>
<p> Completely covered by the following font faces: <code>Fixed</code> (all sizes).</p>
<h3>Uni1 (a big codeset)</h3>
<p>Supports most of the Latin languages, the Slavic Cyrillic languages, Hebrew and barely Arabic. </p>
<p> Completely covered by the following font faces: <code>Fixed</code> (sizes <code>8&#215;15</code> and <code>8&#215;16</code>) and <code>VGA</code> (all sizes).</p>
<h3>Uni2 (a big codeset)</h3>
<p>Supports most of the Latin languages, the Slavic Cyrillic languages and Greek. </p>
<p> Completely covered by the following font faces: <code>Fixed</code> (all sizes) and <code>VGA</code> (sizes <code>8&#215;16</code> and <code>16&#215;32</code>).</p>
<h3>Uni3 (a big codeset)</h3>
<p>Supports most of the Latin and Cyrillic languages. </p>
<p> Completely covered by the following font faces: <code>Fixed</code> (all sizes).</p>
<h3>Vietnamese (a big codeset)</h3>
<p>Supported language: Vietnamese. </p>
<p> Completely covered by the following font faces: <code>Fixed</code> (sizes <code>8&#215;13</code>, <code>8&#215;15</code>, <code>8&#215;16</code> and <code>8&#215;18</code>).</p>
<h2>Files</h2>
<p>The standard location of the <code>console-setup</code> configuration file is <i>/etc/default/console-setup</i>. The keyboard configuration is in <i>/etc/default/keyboard</i>. Fonts that can be used with the variable <code>FONT</code> are usually installed in <i>/usr/share/consolefonts/</i> or <i>/usr/share/syscons/fonts/</i>. Translation maps that can be used with the variable CONSOLE_MAP are usually installed in <i>/usr/share/consoletrans/</i> or <i>/usr/share/syscons/scrnmaps/</i>.</p>
<h2>Notes</h2>
<p>The aim of the Terminus font is to reduce the eyes-fatigue when one has to read a lot. Currently this font supports only the Latin, the Cyrillic and the Greek scripts (the <code>Lat15</code>, <code>Lat2</code>, <code>Lat7</code>, <code>CyrAsia</code>, <code>CyrKoi</code>, <code>CyrSlav</code>, <code>Greek</code>, <code>Uni2</code> and <code>Uni3</code> codesets). The fonts with font face <code>TerminusBoldVGA</code> are optimized for use with regular text video modes. They should not be used with framebuffer video modes. The fonts with font face <code>TerminusBold</code> are optimized for use with the framebuffer video modes. The fonts with font face <code>Terminus</code> can be used in all video modes. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-setupcon/">setupcon</a></code>(1), <code><a href="/docs/linux/man/5-keyboard/">keyboard</a></code>(5), <code><a href="/docs/linux/man/8-setfont/">setfont</a></code>(8), <code><a href="/docs/linux/man/1-vidcontrol/">vidcontrol</a></code>(1) </p>
