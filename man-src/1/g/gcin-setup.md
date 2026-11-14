---
title: "gcin-setup(1)"
name: "gcin-setup"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gcin-setup/"
description: "gcin-setup – configuration tools of gcin"
---

<h2>NAME</h2>
<p> gcin-setup &#8211; configuration tools of gcin</p>
<h2>SYNOPSIS</h2>
<p> <code>gcin-setup</code></p>
<h2>DESCRIPTION</h2>
<p> <code>gcin-setup</code> is the default configuration tool of gcin. Another configuring method is writing conffiles in $HOME/.gcin/config. See CONFFILES section for further information.</p>
<h2>CONFFILES</h2>
<p> Those conffiles below will be created automatically by gcin-setup, except gcin-bell-volume and gcin-sound-play-overlap. </p>
<p> If you want to write conffiles by yourself, please make sure you have the config directory: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>mkdir -p&nbsp;<wbr>$HOME/.gcin/config </p>
<p> After that, you may try: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>echo zo&nbsp;<wbr>&gt;&nbsp;<wbr>$HOME/.gcin/config/phonetic-keyboard </p>
<p> Thus you make a <code>phonetic-keyboard</code> file with its content <code>zo</code>, which means you select the standard style with 1234 selection method. </p>
<p> All available conffiles are listed, and default options are showed <code>bold</code>.</p>
<dl>
<dt><code>$HOME/.gcin/config/default-input-method</code> <i>number</i></p>
<dd> Default input method when gcin is called.</dl>
<p> OPTIONS MEANINGS<br />
 1 Chanjei input method, version 3<br />
 2 Chanjei input method, version 5<br />
 3 Bopomofo input method<br />
 4 Symbols virtual keyboard<br />
 5 Pinyin input method<br />
 <code>6 Tsin intelligent Bopomofo input method</code><br />
 7 Dayi input method<br />
 8 Array input method, 30 keys version<br />
 9 Boshiamy input method, aka Liu&#8217;s input method<br />
 10 Direct input for UTF-32 (U+) or Big-5 characters<br />
 11 Simple Chanjei input method<br />
 12 Japanese anthy input method<br />
 13 Greek letters input method<br />
 14 Latin letters input method<br />
 15 Jyutping input method<br />
 16 NewCJ3 input method</p>
<dl>
<dt><code>$HOME/.gcin/config/gcb-position</code> <i>number</i></p>
<dd> Disable or enable gcb clipboard manager.</dl>
<p> OPTIONS MEANINGS<br />
 0 Disable<br />
 1 Enable, at lower left corner<br />
 2 Enable, at upper left corner<br />
 3 Enable, at lower right corner<br />
 <code>4 Enable, at upper right corner</code></p>
<dl>
<dt><code>$HOME/.gcin/config/gcb-position-x</code> <i>number</i></p>
<dd> The X-axis padding of gcb clipboard manager. Default is <code>0</code>.</p>
<dt><code>$HOME/.gcin/config/gcb-position-y</code> <i>number</i></p>
<dd> The Y-axis padding of gcb clipboard manager. Default is <code>0</code>.</p>
<dt><code>$HOME/.gcin/config/gcin-bell-volume</code> <i>number</i></p>
<dd> Volume of bell ring, between -100 to 100. Default is <code>-97</code>.</p>
<dt><code>$HOME/.gcin/config/gcin-capslock-lower</code> <i>boolean</i></p>
<dd> Input lower-case letters when Caps Lock key is ON.</dl>
<p> OPTIONS MEANINGS<br />
 <code>1 ON</code><br />
 0 OFF</p>
<dl>
<dt><code>$HOME/.gcin/config/gcin-eng-phrase-enabled</code> <i>boolean</i></p>
<dd> Enable Alt-Shift phrases in alphabet-numeric mode.</dl>
<p> OPTIONS MEANINGS<br />
 <code>1 ON</code><br />
 0 OFF</p>
<dl>
<dt><code>$HOME/.gcin/config/gcin-flags-im-enabled</code> <i>number</i></p>
<dd> Available input methods to be cyclic selected by Control-Shift.</dl>
<p> OPTIONS MEANINGS<br />
 <code>2147483647 All input methods are enabled.</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>Ctrl-Alt-1 Chanjei input method, version 3 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>4&nbsp;<wbr>&nbsp;<wbr>Ctrl-Alt-2 Chanjei input method, version 5 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>8&nbsp;<wbr>&nbsp;<wbr>Ctrl-Alt-3 Bopomofo input method </p>
<p>&nbsp;<wbr>&nbsp;<wbr>16&nbsp;<wbr>&nbsp;<wbr>Ctrl-Alt-4 Symbols virtual keyboard </p>
<p>&nbsp;<wbr>&nbsp;<wbr>32&nbsp;<wbr>&nbsp;<wbr>Ctrl-Alt-5 Pinyin input method </p>
<p>&nbsp;<wbr>&nbsp;<wbr>64&nbsp;<wbr>&nbsp;<wbr>Ctrl-Alt-6 Tsin intelligent Bopomofo input method </p>
<p>&nbsp;<wbr>128&nbsp;<wbr>&nbsp;<wbr>Ctrl-Alt-7 Dayi input method </p>
<p>&nbsp;<wbr>256&nbsp;<wbr>&nbsp;<wbr>Ctrl-Alt-8 Array input method, 30 keys version </p>
<p>&nbsp;<wbr>512&nbsp;<wbr>&nbsp;<wbr>Ctrl-Alt-9 Boshiamy input method, aka Liu&#8217;s input method </p>
<p>1024&nbsp;<wbr>&nbsp;<wbr>Ctrl-Alt-0 Direct input for UTF-32&nbsp;<wbr>(U+)&nbsp;<wbr>or Big-5 characters </p>
<p>2048&nbsp;<wbr>&nbsp;<wbr>Ctrl-Alt&#8211; Simple Chanjei input method </p>
<p>4096&nbsp;<wbr>&nbsp;<wbr>Ctrl-Alt-=&nbsp;<wbr>Japanese anthy input method </p>
<p>8192&nbsp;<wbr>&nbsp;<wbr>Ctrl-Alt-`&nbsp;<wbr>Greek letters input method </p>
<p>&nbsp;<wbr>&nbsp;<wbr>16384&nbsp;<wbr>&nbsp;<wbr>Ctrl-Alt-[&nbsp;<wbr>Latin letters input method </p>
<p>&nbsp;<wbr>&nbsp;<wbr>32768&nbsp;<wbr>&nbsp;<wbr>Ctrl-Alt-]&nbsp;<wbr>Jyutping input method </p>
<p>&nbsp;<wbr>&nbsp;<wbr>65536&nbsp;<wbr>&nbsp;<wbr>Ctrl-Alt-\&nbsp;<wbr>NewCJ3 input method </p>
<p> 2147483647 minus numbers of input methods, then you get the configuration number. For example, to disable Greek and Latin letters, calculate 2147483647 &#8211; 8192 &#8211; 16384 = 2147459071. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>echo 2147459071&nbsp;<wbr>&gt;&nbsp;<wbr>$HOME/.gcin/config/gcin-flags-im-enabled </p>
<p> Then you get it.</p>
<dl>
<dt><code>$HOME/.gcin/config/gcin-font-name</code> <i>string</i></p>
<dd> Default font.</dl>
<p> OPTIONS MEANINGS<br />
 <code>sans Sans-serif</code><br />
 serif Serif</p>
<dl>
<dt><code>$HOME/.gcin/config/gcin-font-size</code> <i>number</i></p>
<dd> Font size of character-selection area. Default is <code>16</code>.</p>
<dt><code>$HOME/.gcin/config/gcin-font-size-gtab-in</code> <i>number</i></p>
<dd> Font size of key codes input area in gtab input methods (Chanjei IM, Array IM, etc.). Default is <code>10</code>.</p>
<dt><code>$HOME/.gcin/config/gcin-font-size-pho-near</code> <i>number</i></p>
<dd> Font size of similar-phonetic character selection in Tsin IM. Default is <code>14</code>.</p>
<dt><code>$HOME/.gcin/config/gcin-font-size-symbol</code> <i>number</i></p>
<dd> Font size of symbol-selection window. Default is <code>12</code>.</p>
<dt><code>$HOME/.gcin/config/gcin-font-size-tsin-pho-in</code> <i>number</i></p>
<dd> Font size of phonetic input area in Bopomofo and Tsin IM. Default is <code>10</code>.</p>
<dt><code>$HOME/.gcin/config/gcin-font-size-tsin-presel</code> <i>number</i></p>
<dd> Font size of phrase pre-selection window in Tsin IM. Default is <code>16</code>.</p>
<dt><code>$HOME/.gcin/config/gcin-im-toggle-keys</code> <i>number</i></p>
<dd> Toggle Key for IM window ON/OFF.</dl>
<p> OPTIONS MEANINGS<br />
 <code>0 Control-Space</code><br />
 1 Shift-Space<br />
 2 Alt-Space<br />
 3 Windows-Space</p>
<dl>
<dt><code>$HOME/.gcin/config/gcin-init-im-enabled</code> <i>boolean</i></p>
<dd> Enable input method mode without pressing toggle keys. This option is not available in XIM mode.</dl>
<p> OPTIONS MEANINGS<br />
 1 ON<br />
 <code>0 OFF</code></p>
<dl>
<dt><code>$HOME/.gcin/config/gcin-inner-frame</code> <i>boolean</i></p>
<dd> Show frame border in gcin window.</dl>
<p> OPTIONS MEANINGS<br />
 1 ON<br />
 <code>0 OFF</code></p>
<dl>
<dt><code>$HOME/.gcin/config/gcin-input-style</code> <i>number</i></p>
<dd> Window style of gcin.</dl>
<p> OPTIONS MEANINGS<br />
 <code>1 OverTheSpot (Follow the cursor)</code><br />
 2 Root (Fixed index window)</p>
<dl>
<dt><code>$HOME/.gcin/config/gcin-pop-up-win</code> <i>boolean</i></p>
<dd> Dynamic pop up window.</dl>
<p> OPTIONS MEANINGS<br />
 <code>1 ON</code><br />
 0 OFF</p>
<dl>
<dt><code>$HOME/.gcin/config/gcin-remote-client</code> <i>boolean</i></p>
<dd> Use gcin in remote applications.</dl>
<p> OPTIONS MEANINGS<br />
 1 ON<br />
 <code>0 OFF</code></p>
<dl>
<dt><code>$HOME/.gcin/config/gcin-root-x</code> <i>number</i></p>
<dd> Window position in X-axis when window style is Root (Fixed index window). Default is <code>1600</code>.</p>
<dt><code>$HOME/.gcin/config/gcin-root-y</code> <i>number</i></p>
<dd> Window position in Y-axis when window style is Root (Fixed index window). Default is <code>1200</code>.</p>
<dt><code>$HOME/.gcin/config/gcin-sel-key-color</code> <i>hex</i></p>
<dd> Color of selection Key.</dl>
<p> OPTIONS MEANINGS<br />
 #FF0000 Red<br />
 #00FF00 Green<br />
 <code>#0000FF Blue</code><br />
 #FFFF00 Yellow<br />
 #FF00FF Magenta<br />
 #00FFFF Cyan</p>
<dl>
<dt><code>$HOME/.gcin/config/gcin-shift-space-eng-full</code> <i>boolean</i></p>
<dd> Toggle to double-wide English character mode with Shift-Space.</dl>
<p> OPTIONS MEANINGS<br />
 <code>1 ON</code><br />
 0 OFF</p>
<dl>
<dt><code>$HOME/.gcin/config/gcin-sound-play-overlap</code> <i>boolean</i></p>
<dd> Play all sound when text-to-speech is enabled.</dl>
<p> OPTIONS MEANINGS<br />
 1 ON<br />
 <code>0 OFF</code></p>
<dl>
<dt><code>$HOME/.gcin/config/gcin-status-tray</code> <i>boolean</i></p>
<dd> Show gcin status in system tray.</dl>
<p> OPTIONS MEANINGS<br />
 <code>1 ON</code><br />
 0 OFF</p>
<dl>
<dt><code>$HOME/.gcin/config/gcin-win-color-bg</code> <i>hex</i></p>
<dd> Background color of gcin window. Default is <code>#005BFF</code>.</p>
<dt><code>$HOME/.gcin/config/gcin-win-color-fg</code> <i>hex</i></p>
<dd> Foreground color of gcin window.</dl>
<p> OPTIONS MEANINGS<br />
 #FF0000 Red<br />
 #00FF00 Green<br />
 #0000FF Blue<br />
 #FFFF00 Yellow<br />
 #FF00FF Magenta<br />
 <code>#FFFFFF White</code></p>
<dl>
<dt><code>$HOME/.gcin/config/gcin-win-color-use</code> <i>boolean</i></p>
<dd> Customized colors in gcin window.</dl>
<p> OPTIONS MEANINGS<br />
 1 ON<br />
 <code>0 OFF</code></p>
<dl>
<dt><code>$HOME/.gcin/config/gcin-win-sym-click-close</code> <i>boolean</i></p>
<dd> Close symbol-selection window after choosing a symbol.</dl>
<p> OPTIONS MEANINGS<br />
 <code>1 ON</code><br />
 0 OFF</p>
<dl>
<dt><code>$HOME/.gcin/config/gtab-auto-select-by_phrase</code> <i>boolean</i></p>
<dd> Auto-select according to Tsin phrase database in gtab input methods.</dl>
<p> OPTIONS MEANINGS<br />
 1 ON<br />
 <code>0 OFF</code></p>
<dl>
<dt><code>$HOME/.gcin/config/gtab-capslock-in-eng</code> <i>boolean</i></p>
<dd> Toggle Chinese/English mode with Caps Lock key in gtab input methods.</dl>
<p> OPTIONS MEANINGS<br />
 <code>1 ON</code><br />
 0 OFF</p>
<dl>
<dt><code>$HOME/.gcin/config/gtab-disp-im-name</code> <i>boolean</i></p>
<dd> Display input method name in gtab input methods.</dl>
<p> OPTIONS MEANINGS<br />
 <code>1 ON</code><br />
 0 OFF</p>
<dl>
<dt><code>$HOME/.gcin/config/gtab-disp-key-codes</code> <i>boolean</i></p>
<dd> Show all possible key codes of character in gtab input methods.</dl>
<p> OPTIONS MEANINGS<br />
 <code>1 ON</code><br />
 0 OFF</p>
<dl>
<dt><code>$HOME/.gcin/config/gtab-disp-partial-match</code> <i>boolean</i></p>
<dd> Display partial matched characters in gtab input methods.</dl>
<p> OPTIONS MEANINGS<br />
 <code>1 ON</code><br />
 0 OFF</p>
<dl>
<dt><code>$HOME/.gcin/config/gtab-dup-select-bell</code> <i>boolean</i></p>
<dd> Bell ring when multiple selections are available in gtab input methods.</dl>
<p> OPTIONS MEANINGS<br />
 1 ON<br />
 <code>0 OFF</code></p>
<dl>
<dt><code>$HOME/.gcin/config/gtab-hide-row2</code> <i>boolean</i></p>
<dd> Hide second row of window in gtab input methods.</dl>
<p> OPTIONS MEANINGS<br />
 1 ON<br />
 <code>0 OFF</code></p>
<dl>
<dt><code>$HOME/.gcin/config/gtab-in-row1</code> <i>boolean</i></p>
<dd> Show key codes in first row of window in gtab input methods.</dl>
<p> OPTIONS MEANINGS<br />
 1 ON<br />
 <code>0 OFF</code></p>
<dl>
<dt><code>$HOME/.gcin/config/gtab-invalid-key-in</code> <i>boolean</i></p>
<dd> Clear key codes input area when invalid key and Space key are pressed.</dl>
<p> OPTIONS MEANINGS<br />
 <code>1 ON</code><br />
 0 OFF</p>
<dl>
<dt><code>$HOME/.gcin/config/gtab-pre-select</code> <i>boolean</i></p>
<dd> Show candidate characters before pressing endkey (Space key). For gtab input methods.</dl>
<p> OPTIONS MEANINGS<br />
 <code>1 ON</code><br />
 0 OFF</p>
<dl>
<dt><code>$HOME/.gcin/config/gtab-press-full-auto-send</code> <i>boolean</i></p>
<dd> Auto-send character when key codes input area is filled in gtab input methods.</dl>
<p> OPTIONS MEANINGS<br />
 <code>1 ON</code><br />
 0 OFF</p>
<dl>
<dt><code>$HOME/.gcin/config/gtab-que-wild-card</code> <i>boolean</i></p>
<dd> Use ? as wildcard.</dl>
<p> OPTIONS MEANINGS<br />
 1 ON<br />
 <code>0 OFF</code></p>
<dl>
<dt><code>$HOME/.gcin/config/gtab-shift-phrase-key</code> <i>boolean</i></p>
<dd> Use single Shift key to input Alt-Shift phrases in gtab input methods.</dl>
<p> OPTIONS MEANINGS<br />
 1 ON<br />
 <code>0 OFF</code></p>
<dl>
<dt><code>$HOME/.gcin/config/gtab-space-auto-first</code> <i>number</i></p>
<dd> Function of Space Key in gtab input methods.</dl>
<p> OPTIONS MEANINGS<br />
 <code>0 Auto-selected by definition in .gtab file.</code><br />
 1 Send first character in Boshiamy input method.<br />
 2 Send first character in character-selection area.<br />
 4 Does not send first character. (For Array input method.)</p>
<dl>
<dt><code>$HOME/.gcin/config/gtab-unique-auto-send</code> <i>boolean</i></p>
<dd> Auto send characters when there is only one choice in gtab input methods.</dl>
<p> OPTIONS MEANINGS<br />
 1 ON<br />
 <code>0 OFF</code></p>
<dl>
<dt><code>$HOME/.gcin/config/gtab-vertical-select</code> <i>boolean</i></p>
<dd> Vertical selection window in gtab input methods.</dl>
<p> OPTIONS MEANINGS<br />
 1 ON<br />
 <code>0 OFF</code></p>
<dl>
<dt><code>$HOME/.gcin/config/left-right-button-tips</code> <i>boolean</i></p>
<dd> Show button tips when mouse cursor stays on gcin window. Default is ON, but it will be turned OFF after <code>gcin-setup</code> is executed.</dl>
<p> OPTIONS MEANINGS<br />
 <code>1 ON</code><br />
 0 OFF</p>
<dl>
<dt><code>$HOME/.gcin/config/pho-hide-row2</code> <i>boolean</i></p>
<dd> Hide second row of window in Bopomofo and Tsin IM.</dl>
<p> OPTIONS MEANINGS<br />
 1 ON<br />
 <code>0 OFF</code></p>
<dl>
<dt><code>$HOME/.gcin/config/pho-in-row1</code> <i>boolean</i></p>
<dd> Show key codes in first row of window in Bopomofo IM.</dl>
<p> OPTIONS MEANINGS<br />
 <code>1 ON</code><br />
 0 OFF</p>
<dl>
<dt><code>$HOME/.gcin/config/phonetic-char-dynamic-sequence</code> <i>boolean</i></p>
<dd> Dynamic character sequence adjustment in Bopomofo and Tsin IM.</dl>
<p> OPTIONS MEANINGS<br />
 <code>1 ON</code><br />
 0 OFF</p>
<dl>
<dt><code>$HOME/.gcin/config/phonetic-huge-tab</code> <i>boolean</i></p>
<dd> Input all Traditional Chinese, Simplified Chinese, and Japanese characters provided by pho-huge.tab in Bopomofo and Tsin IM.</dl>
<p> OPTIONS MEANINGS<br />
 1 ON<br />
 <code>0 OFF</code></p>
<dl>
<dt><code>$HOME/.gcin/config/phonetic-keyboard</code> <i>string</i></p>
<dd> Key codes arrangement style in Bopomofo, Tsin, and Japanese anthy IM.</dl>
<p> OPTIONS MEANINGS<br />
 zo Standard style with 1234 selection method<br />
 <code>zo-asdf Standard style with asdf selection method</code><br />
 et Eten style with 1234 selection method<br />
 et-asdf Eten style with asdf selection method<br />
 et26 Eten 26 keys style with 1234 selection method<br />
 et26-asdf Eten 26 keys style with asdf selection method<br />
 hsu Mr. Hsu&#8217;s style (Kuo-Yin IM, Natural Bopomofo IM)<br />
 pinyin Phonetic Pinyin style with 1234 selection method<br />
 pinyin-asdf Phonetic Pinyin style with asdf selection method<br />
 dvorak Dvorak style<br />
 ibm IBM style<br />
 mitac Mitac style</p>
<dl>
<dt><code>$HOME/.gcin/config/phonetic-speak</code> <i>boolean</i></p>
<dd> Enable text-to-speech. You have to install speech data for this feature.</dl>
<p> OPTIONS MEANINGS<br />
 1 ON<br />
 <code>0 OFF</code></p>
<dl>
<dt><code>$HOME/.gcin/config/phonetic-speak-sel</code> <i>string</i></p>
<dd> Speech data filename for text-to-speech.</p>
<dt><code>$HOME/.gcin/config/tsin-buffer-editing-mode</code> <i>boolean</i></p>
<dd> VI-like editing mode in Tsin IM.</dl>
<p> OPTIONS MEANINGS<br />
 1 ON<br />
 <code>0 OFF</code></p>
<dl>
<dt><code>$HOME/.gcin/config/tsin-buffer-size</code> <i>number</i></p>
<dd> Size of buffer (editing area) in Tsin IM. Default is <code>40</code>.</p>
<dt><code>$HOME/.gcin/config/tsin-chinese-english-toggle_key</code> <i>number</i></p>
<dd> Toggle key for Chinese/English mode in Tsin IM.</dl>
<p> OPTIONS MEANINGS<br />
 <code>1 Caps Lock key</code><br />
 2 Tab key<br />
 4 Shift key (Not available in XIM mode).<br />
 8 Left Shift key (Not available in XIM mode).<br />
 16 Right Shift key (Not available in XIM mode).</p>
<dl>
<dt><code>$HOME/.gcin/config/tsin-cursor-color</code> <i>hex</i></p>
<dd> Color of cursor in Tsin IM.</dl>
<p> OPTIONS MEANINGS<br />
 #FF0000 Red<br />
 #00FF00 Green<br />
 <code>#0000FF Blue</code><br />
 #FFFF00 Yellow<br />
 #FF00FF Magenta<br />
 #00FFFF Cyan</p>
<dl>
<dt><code>$HOME/.gcin/config/tsin-phrase-line-color</code> <i>hex</i></p>
<dd> Color of phrase-underline in Tsin IM. Default is <code>#0000FF</code>.</p>
<dt><code>$HOME/.gcin/config/tsin-phrase-pre-select</code> <i>boolean</i></p>
<dd> Show phrase pre-selection window in Tsin IM.</dl>
<p> OPTIONS MEANINGS<br />
 <code>1 ON</code><br />
 0 OFF</p>
<dl>
<dt><code>$HOME/.gcin/config/tsin-space-opt</code> <i>number</i></p>
<dd> Function of Space key in Tsin IM.</dl>
<p> OPTIONS MEANINGS<br />
 <code>1 Select other same phonetic characters.</code><br />
 2 Send space to buffer of Tsin IM.</p>
<dl>
<dt><code>$HOME/.gcin/config/tsin-tab-phrase-end</code> <i>boolean</i></p>
<dd> Use Escape key or Tab key to stop phrase-auto-selection in Tsin IM.</dl>
<p> OPTIONS MEANINGS<br />
 1 ON<br />
 <code>0 OFF</code></p>
<dl>
<dt><code>$HOME/.gcin/config/tsin-tail-select-key</code> <i>boolean</i></p>
<dd> Show selection keys follows choices in Tsin IM.</dl>
<p> OPTIONS MEANINGS<br />
 1 ON<br />
 <code>0 OFF</code></p>
<dl>
<dt><code>$HOME/.gcin/config/tsin-tone-char-input</code> <i>boolean</i></p>
<dd> Input tone sympols of Bopomofo in Tsin IM.</dl>
<p> OPTIONS MEANINGS<br />
 1 ON<br />
 <code>0 OFF</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gcin/">gcin</a></code>(1) </p>
<h2>Index</h2>
