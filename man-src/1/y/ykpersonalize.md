---
title: "ykpersonalize(1)"
name: "ykpersonalize"
section: "1"
letter: "y"
url: "/docs/linux/man/1-ykpersonalize/"
description: "ykpersonalize – personalize YubiKey OTP tokens"
---

<h2>NAME</h2>
<p> ykpersonalize &#8211; personalize YubiKey OTP tokens</p>
<h2>SYNOPSIS</h2>
<p> <code>ykpersonalize</code> [<i>-1</i> | <i>-2</i>] [<i>-sfile</i>] [<i>-ifile</i>] [<i>-fformat</i>] [<i>-axxx</i>] [<i>-cxxx</i>] [<i>-ooption</i>] [<i>-y</i>] [<i>-v</i>] [<i>-d</i>] [<i>-h</i>] [<i>-n</i>] [<i>-t</i>] [<i>-u</i>] [<i>-x</i>] [<i>-z</i>] [<i>-m</i>] [<i>-S</i>] [<i>-V</i>]</p>
<h2>OPTIONS</h2>
<p> Set the AES key, user ID and other settings in a YubiKey. For the complete explanation of the meaning of all parameters, see the reference manual: YubiKey manual &lt;URL: <a rel="nofollow" href="http://yubico.com/files/YubiKey_manual-2.0.pdf">http://yubico.com/files/YubiKey_manual-2.0.pdf</a> &gt;</p>
<dl>
<dt><code>-1</code></p>
<dd> change the first configuration. This is the default and is normally used for true OTP generation. In this configuration, the option flag <code>-oappend-cr</code> is set by default.</p>
<dt><code>-2</code></p>
<dd> change the second configuration. This is for YubiKey II only and is then normally used for static key generation. In this configuration, the option flags <code>-oappend-cr</code>, <code>-ostatic-ticket</code>, <code>-ostrong-pw1</code>, <code>-ostrong-pw2</code> and <code>-oman-update</code> are set by default.</p>
<dt><code>-z</code></p>
<dd> delete configuration in selected slot</p>
<dt><code>-s</code><i>file</i></p>
<dd> save configuration to file instead of key. (if file is -, send to stdout)</p>
<dt><code>-i</code><i>file</i></p>
<dd> read configuration from file. (if file is -, read from stdin) Configuration import is only valid for the ycfg format.</p>
<dt><code>-f</code><i>format</i></p>
<dd> format to be used with <code>-s</code> and <code>-i</code>. Valid options are <code>ycfg</code> and <code>legacy</code>.</p>
<dt><code>-a</code>[<i>xxx</i>]</p>
<dd> the AES secret key as a 32 (or 40 for OATH-HOTP/HMAC CHAL-RESP) char hex value (not modhex) (none to prompt for key on stdin) If <code>-a</code> is not used a random key will be generated.</p>
<dt><code>-c</code><i>xxx</i></p>
<dd> A 12 char hex value (not modhex) to use as access code for programming. NOTE: this does NOT SET the access code, that&#8217;s done with <code>-oaccess</code><i>=</i>.</p>
<dt><code>-o</code><i>option</i></p>
<dd> change configuration option. Possible option arguments are</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>fixed</code>=<i>fffffffffff</i></p>
<dd> The modhex <i>public identity</i> of the YubiKey, 0-32 characters long (encoding up to 16 bytes). It&#8217;s possible to give the identity in hex as well, just prepend the value with `h:&#8217;. The fixed part is emitted before the OTP when the button on the YubiKey is pressed. It can be used as an identifier for the user, for example.</p>
<dt><code>uid</code>=<i>uuuuuu</i></p>
<dd> The uid part of the generated OTP, also called <i>private identity</i>, in hex. Must be 12 characters long. The uid is 6 bytes of static data that is included (encrypted) in every OTP, and is used to validate that an OTP was in fact encrypted with the AES key shared between the YubiKey and the validation service. It cannot be used to identify the YubiKey as it is only readable to those that know the AES key.</p>
<dt><code>access</code>=<i>fffffffffff</i></p>
<dd> New hex access code to set. Must be 12 characters long. If an access code is set, it will be required for subsequent reprogramming of the YubiKey.</p>
<dt><code>oath-imf</code>=<i>xxx</i></p>
<dd> Set OATH Initial Moving Factor. This is the initial counter value for the YubiKey. This should be a value between 0 and 1048560, evenly dividable by 16.</p>
<dt>[-]<i>ticket-flag</i></p>
<dd> Set/clear ticket flag, see the section `Ticket flags&#8217;</p>
<dt>[-]<i>configuration-flag</i></p>
<dd> Set/clear ticket flag, see the section `Configuration flags&#8217;</dl>
</dl>
<dt><code>-y</code></p>
<dd> always commit without prompting</p>
<dt><code>-d</code></p>
<dd> dry-run, run without writing a YubiKey</p>
<dt><code>-v</code></p>
<dd> Be more verbose</p>
<dt><code>-h</code></p>
<dd> Help</p>
<dt><code>-V</code></p>
<dd> Version</p>
<dt><code>YubiKey Neo only</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>-m mode</code></p>
<dd> set device configuration for the YubiKey. It is parsed in the form <i>mode:cr_timeout:autoeject_timeout</i><br />
 where mode is:<br />
 0 OTP device only.<br />
 1 CCID device only.<br />
 2 OTP/CCID composite device.<br />
 3 U2F device only.<br />
 4 OTP/U2F composite device.<br />
 5 U2F/CCID composite device.<br />
 6 OTP/U2F/CCID composite device.<br />
 Add 80 to set MODE_FLAG_EJECT, for example: 81<br />
 cr_timeout is the timeout in seconds for the YubiKey to wait on button press for challenge response (default is 15)<br />
 autoeject_timeout is the timeout in seconds before the card is automatically ejected in mode 81</p>
<dt><code>-n URI</code></p>
<dd> Program NFC NDEF URI</p>
<dt><code>-t text</code></p>
<dd> Program NFC NDEF text</dl>
</dl>
<dt><code>YubiKey 3.0 and above</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>-S</code><i>0605&#8230;</i></p>
<dd> set the scanmap to be used with the YubiKey NEO. It must be 45 unique bytes as 90 characters. Leave argument empty to reset to the YubiKey&#8217;s default. The scanmap must be sent in the order:<br />
 <i>cbdefghijklnrtuvCBDEFGHIJKLNRTUV0123456789!	</i>.<br />
 the default scanmap in the YubiKey is:<br />
 <i>06050708090a0b0c0d0e0f111517181986858788898a8b8c8d8e8f<br />
 9195979899271e1f202122232425269e2b28</i><br />
 an example for simplified us dvorak would be:<br />
 <i>0c110b071c180d0a0619130f120e09378c918b879c988d8a869993<br />
 8f928e89b7271e1f202122232425269e2b28</i><br />
 or for a french azerty keyboard (digits are shifted):<br />
 <i>06050708090a0b0c0d0e0f111517181986858788898a8b8c8d8e8f<br />
 9195979899a79e9fa0a1a2a3a4a5a6382b28</i><br />
 and a turkish example (has a dotless i instead of usual i):<br />
 <i>06050708090a0b340d0e0f111517181986858788898a8b8c8d8e8f<br />
 9195979899271e1f202122232425269e2b28</i><br />
 Note that you must remove any whitespace present in these examples before using the values.</dl>
</dl>
<dt><code>YubiKey 2.3 and above</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>-u</code></p>
<dd> Update existing configuration, rather than overwriting</p>
<dt><code>-x</code></p>
<dd> Swap configuration slot 1 and 2 inside the YubiKey</dl>
</dl>
</dl>
<h2>Ticket flags</h2>
<dl>
<dt>[-]<code>tab-first</code></p>
<dd> Send a tab character as the first character. This is usually used to move to the next input field.</p>
<dt>[-]<code>append-tab1</code></p>
<dd> Send a tab character between the fixed part and the one-time password part. This is useful if you have the fixed portion equal to the user name and two input fields that you navigate between using tab.</p>
<dt>[-]<code>append-tab2</code></p>
<dd> Send a tab character as the last character.</p>
<dt>[-]<code>append-delay1</code></p>
<dd> Add a half-second delay before sending the one-time password part. This option is only valid for firmware 1.x and 2.x.</p>
<dt>[-]<code>append-delay2</code></p>
<dd> Add a half-second delay after sending the one-time password part. This option is only valid for firmware 1.x and 2.x.</p>
<dt>[-]<code>append-cr</code></p>
<dd> Send a carriage return after sending the one-time password part.</p>
<dt><code>YubiKey 2.0 firmware and above</code></p>
<dd>
<dt>[-]<code>protect-cfg2</code></p>
<dd> When written to configuration 1, block later updates to configuration 2. When written to configuration 2, prevent configuration 1 from having the lock bit set.</p>
<dt><code>YubiKey 2.1 firmware and above</code></p>
<dd>
<dt>[-]<code>oath-hotp</code></p>
<dd> Set OATH-HOTP mode rather than YubiKey mode. In this mode, the token functions according to the OATH-HOTP standard.</p>
<dt><code>YubiKey 2.2 firmware and above</code></p>
<dd>
<dt>[-]<code>chal-resp</code></p>
<dd> Set challenge-response mode.</dl>
<h2>Configuration flags</h2>
<p> [-]<code>send-ref</code> Send a reference string of all 16 modhex characters before the fixed part. This can not be combined with the <code>-ostrong-pw2</code> flag.</p>
<dl>
<dt>[-]<code>pacing-10ms</code></p>
<dd> Add a 10ms delay between key presses.</p>
<dt>[-]<code>pacing-20ms</code></p>
<dd> Add a 20ms delay between key presses.</p>
<dt>[-]<code>static-ticket</code></p>
<dd> Output a fixed string rather than a one-time password. The password is still based on the AES key and should be hard to guess and impossible to remember.</p>
<dt><code>YubiKey 1.x firmware only</code></p>
<dd>
<dt>[-]<code>ticket-first</code></p>
<dd> Send the one-time password rather than the fixed part first.</p>
<dt>[-]<code>allow-hidtrig</code></p>
<dd> Allow trigger through HID/keyboard by pressing caps-, num or scroll-lock twice. Not recommended for security reasons.</p>
<dt><code>YubiKey 2.0 firmware and above</code></p>
<dd>
<dt>[-]<code>short-ticket</code></p>
<dd> Limit the length of the static string to max 16 digits. This flag only makes sense with the <code>-ostatic-ticket</code> option. When <code>-oshort-ticket</code> is used without <code>-ostatic-ticket</code> it will program the YubiKey in &quot;scan-code mode&quot;, in this mode the key sends the contents of fixed, uid and key as raw keyboard scancodes. For example, by using the fixed string <i>h:8b080f0f122c9a12150f079e</i> in this mode it will send <i>Hello World!</i> on a qwerty keyboard. This mode sends raw scan codes, so output will differ between keyboard layouts.</p>
<dt>[-]<code>strong-pw1</code></p>
<dd> Upper-case the two first letters of the output string. This is for compatibility with legacy systems that enforce both uppercase and lowercase characters in a password and does not add any security.</p>
<dt>[-]<code>strong-pw2</code></p>
<dd> Replace the first eight characters of the modhex alphabet with the numbers 0 to 7. Like <code>-ostrong-pw1</code>, this is intended to support legacy systems.</p>
<dt>[-]<code>man-update</code></p>
<dd> Enable user-initiated update of the static password. Only makes sense with the <code>-ostatic-ticket</code> option. This is only valid for firmware 2.x.</p>
<dt><code>YubiKey 2.1 firmware and above</code></p>
<dd>
<dt>[-]<code>oath-hotp8</code></p>
<dd> When set, generate an 8-digit HOTP rather than a 6-digit one.</p>
<dt>[-]<code>oath-fixed-modhex1</code></p>
<dd> When set, the first byte of the fixed part is sent as modhex.</p>
<dt>[-]<code>oath-fixed-modhex2</code></p>
<dd> When set, the first two bytes of the fixed part is sent as modhex.</p>
<dt>[-]<code>oath-fixed-modhex</code></p>
<dd> When set, the fixed part is sent as modhex.</p>
<dt><code>oath-id=m:OOTTUUUUUUUU</code></p>
<dd> Configure OATH token id with a provided value. See description of this option under the 2.2 section for details, but note that a YubiKey 2.1 key can&#8217;t report its serial number and thus a token identifier value must be specified.</p>
<dt><code>YubiKey 2.2 firmware and above</code></p>
<dd>
<dt>[-]<code>chal-yubico</code></p>
<dd> Yubico OTP challenge-response mode.</p>
<dt>[-]<code>chal-hmac</code></p>
<dd> Generate HMAC-SHA1 challenge responses.</p>
<dt>[-]<code>hmac-lt64</code></p>
<dd> Calculate HMAC on less than 64 bytes input. Whatever is in the last byte of the challenge is used as end of input marker (backtracking from end of payload).</p>
<dt>[-]<code>chal-btn-trig</code></p>
<dd> The YubiKey will wait for the user to press the key (within 15 seconds) before answering the challenge.</p>
<dt>[-]<code>serial-btn-visible</code></p>
<dd> The YubiKey will emit its serial number if the button is pressed during power-up. This option is only valid for the 2.x firmware line.</p>
<dt>[-]<code>serial-usb-visible</code></p>
<dd> The YubiKey will indicate its serial number in the USB iSerial field. This option is not available in the 3.0 and 3.1 firmwares.</p>
<dt>[-]<code>serial-api-visible</code></p>
<dd> The YubiKey will allow its serial number to be read using an API call.</p>
<dt><code>oath-id[=m:OOTTUUUUUUUU]</code></p>
<dd> Configure OATH token id with a provided value, or if used without a value use the standard YubiKey token identifier. </p>
<p> The standard OATH token id for a Yubico YubiKey is (modhex) OO=ub, TT=he, (decimal) UUUUUUUU=serial number. </p>
<p> The reason for the decimal serial number is to make it easy for humans to correlate the serial number on the back of the YubiKey to an entry in a list of associated tokens for example. Other encodings can be accomplished using the appropriate oath-fixed-modhex options. </p>
<p> Note that the YubiKey must be programmed to allow reading its serial number, otherwise automatic token id creation is not possible. </p>
<p> See section &quot;5.3.4 &#8211; OATH-HOTP Token Identifier&quot; of the YubiKey manual &lt;URL: <a rel="nofollow" href="http://yubico.com/files/YubiKey_manual-2.0.pdf">http://yubico.com/files/YubiKey_manual-2.0.pdf</a> &gt; for further details.</p>
<dt><code>YubiKey 2.3 firmware and above</code></p>
<dd>
<dt>[-]<code>use-numeric-keypad</code></p>
<dd> Send scancodes for numeric keypad keypresses when sending digits &#8211; helps with some keyboard layouts. This option is only valid for the 2.x firmware line.</p>
<dt>[-]<code>fast-trig</code></p>
<dd> Faster triggering when only configuration 1 is available. This option is always in effect on firmware versions 3.0 and above.</p>
<dt>[-]<code>allow-update</code></p>
<dd> Allow updating of certain parameters in a configuration at a later time.</p>
<dt>[-]<code>dormant</code></p>
<dd> Hides/unhides a configuration stored in a YubiKey.</p>
<dt><code>YubiKey 2.4/3.1 firmware and above</code></p>
<dd>
<dt>[-]<code>led-inv</code></p>
<dd> Inverts the behaviour of the led on the YubiKey. </p>
</dl>
<h2>OATH-HOTP Mode</h2>
<p> When using OATH-HOTP mode, a HMAC key of 160 bits (20 bytes, 40 chars of hex) can be supplied with <code>-a</code>. </p>
<h2>Challenge-response Mode</h2>
<p> In <code>CHAL-RESP</code> mode, the token will NOT generate any keypresses when the button is pressed (although it is perfectly possible to have one slot with a keypress-generating configuration, and the other in challenge-response mode). Instead, a program capable of sending USB HID feature reports to the token must be used to send it a challenge, and read the response. </p>
<h2>Modhex</h2>
<p> Modhex is a way of writing hex digits where the &#8220;digits&#8221; are chosen for being in the same place on most keyboard layouts.</p>
<dl>
<dt>To convert from hex to modhex, you can use</p>
<dd>
<dl>
<dt>
<dd> tr &quot;[0123456789abcdef]&quot; &quot;[cbdefghijklnrtuv]&quot;</dl>
<dt>To convert the other way, use</p>
<dd>
<dl>
<dt>
<dd> tr &quot;[cbdefghijklnrtuv]&quot; &quot;[0123456789abcdef]&quot;</dl>
</dl>
<h2>BUGS</h2>
<p> Report ykpersonalize bugs in the issue tracker &lt;URL: <a rel="nofollow" href="https://github.com/Yubico/yubikey-personalization/issues">https://github.com/Yubico/yubikey-personalization/issues</a> &gt;</p>
<h2>SEE ALSO</h2>
<p> The ykpersonalize home page &lt;URL: <a rel="nofollow" href="https://developers.yubico.com/yubikey-personalization/">https://developers.yubico.com/yubikey-personalization/</a> &gt; </p>
<p> YubiKeys can be obtained from Yubico &lt;URL: <a rel="nofollow" href="http://www.yubico.com/">http://www.yubico.com/</a> &gt;. </p>
<h2>Index</h2>
