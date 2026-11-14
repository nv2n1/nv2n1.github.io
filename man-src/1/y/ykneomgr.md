---
title: "ykneomgr(1)"
name: "ykneomgr"
section: "1"
letter: "y"
url: "/docs/linux/man/1-ykneomgr/"
description: "ykneomgr – YubiKey NEO management tool"
---

<h2>NAME</h2>
<p> ykneomgr &#8211; YubiKey NEO management tool</p>
<h2>SYNOPSIS</h2>
<p> <code>ykneomgr</code> [<i>OPTIONS</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> ykneomgr 0.1.8 </p>
<p> YubiKey NEO management tool.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print help and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print version and exit</p>
<dt><code>-m</code>, <code>&#8211;get-mode</code></p>
<dd> Output mode of YubiKey NEO (default=off)</p>
<dt><code>-w</code>, <code>&#8211;get-version</code></p>
<dd> Output firmware version for YubiKey NEO (default=off)</p>
<dt><code>-s</code>, <code>&#8211;get-serialno</code></p>
<dd> Output serial number (default=off)</p>
<dt><code>-l</code>, <code>&#8211;list-readers</code></p>
<dd> List all connected PCSC devices (default=off)</p>
<dt><code>-a</code>, <code>&#8211;applet-list</code></p>
<dd> List applets on device (default=off)</p>
<dt><code>-D</code>, <code>&#8211;applet-delete</code>=<i>STRING</i></p>
<dd> Delete given applet AID from device</p>
<dt><code>-i</code>, <code>&#8211;applet-install</code>=<i>FILE</i></p>
<dd> Install applets on device from CAP file</p>
<dt><code>-M</code>, <code>&#8211;set-mode</code>=<i>STRING</i></p>
<dd> Set the USB operation mode of the YubiKey NEO. The possible MODE arguments are: 0 for HID device only, 1 for CCID device only, 81 for CCID device with touch eject, 2 for HID/CCID composite device, 3 for U2F device only, 4 for OTP/U2F composite device, 5 for U2F/CCID composite device, 6 for OTP/U2F/CCID composite device.</p>
<dt><code>-S</code>, <code>&#8211;send-apdu</code>=<i>STRING</i></p>
<dd> Send an arbitrary APDU to the device</p>
<dt><code>-r</code>, <code>&#8211;reader</code>=<i>STRING</i></p>
<dd> Use only a matching card reader</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> Print debug information to standard error (default=off)</dl>
<h2>EXAMPLES</h2>
<p> To display the firmware version of a connected YubiKey NEO you use the &#8211;get-version or -w parameter. Typical output would be the string &quot;3.0.4&quot;. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>ykneomgr &#8211;get-version </p>
<p> To display the serial number you would use the &#8211;get-serialno or -s parameter. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>ykneomgr &#8211;get-serialno </p>
<p> To display the device mode you use the &#8211;get-mode or -m parameter. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>ykneomgr &#8211;get-mode </p>
<p> The possible modes are 0 for HID device only, 1 for CCID device only, 2 for HID/CCID composite device. For the CCID modes (i.e., 1 and 2), you can add 80 to enable MODE_FLAG_EJECT which means that touching the YubiKey button will trigger eject/insert of the smartcard. That is, 81 means CCID device only with touch eject/insert, and 82 means HID/CCID composite device with touch eject/insert. </p>
<p> To mode switch the NEO into OTP-only mode, you use the &#8211;set-mode or -M parameter with mode 0. Note that you have to eject the YubiKey NEO and re-insert it before it changes mode. </p>
<p>ykneomgr &#8211;set-mode 0 </p>
<p> To mode switch the NEO into CCID-only mode, you use the &#8211;set-mode or -M parameter with mode 1. Note that you have to eject the YubiKey NEO and re-insert it before it changes mode. </p>
<p>ykneomgr &#8211;set-mode 1 </p>
<p> To mode switch the NEO into hybrid OTP/CCID composite mode, you use the &#8211;set-mode or -M parameter with mode 2. Note that you have to eject the YubiKey NEO and re-insert it before it changes mode. </p>
<p>ykneomgr &#8211;set-mode 2 </p>
<p> To mode switch the NEO into CCID-only mode, with the touch button acting as eject/insert of the card, you use the &#8211;set-mode or -M parameter with mode 81. Note that you have to eject the YubiKey NEO and re-insert it before it changes mode. </p>
<p>ykneomgr &#8211;set-mode 81 </p>
<p> To mode switch the NEO into hybrid OTP/CCID composite mode, with the touch button acting as eject/insert of the card, you use the &#8211;set-mode or -M parameter with mode 82. Note that you have to eject the YubiKey NEO and re-insert it before it changes mode. </p>
<p>ykneomgr &#8211;set-mode 82 </p>
<p> To list the connected readers you use the &#8211;list-readers or -l parameter. </p>
<p>ykneomgr &#8211;list-readers </p>
<p> To list the available applets on the device you use the &#8211;applet-list or -a parameter. The output is a list of AIDs identifying applets. For example, d27600012401 means the OpenPGP applet. </p>
<p>ykneomgr &#8211;applet-list </p>
<p> To delete an applet you use the &#8211;applet-delete or -D parameter, giving it the applet AID as an parameter. Note that deleting an applet may take a second or two to complete. Warning! Deleting an applet will destroy all storage associated with that applet, including any private keys or other credentials. </p>
<p>ykneomgr &#8211;applet-delete d27600012401 </p>
<p> To install a CAP file as an applet you use the &#8211;applet-install or -i parameter, giving it the filename of the CAP file applet as a parameter. Note that loading can take several seconds, for typical CAP file sizes it takes around 5 seconds. </p>
<p>ykneomgr &#8211;applet-install path/to/applet.cap </p>
<p> To work with multiple card readers use the &#8211;reader or -r parameter, giving it a substring of the card reader name to use. Consider a system which has three card readers, one YubiKey NEO in CCID mode, one YubiKey NEO in OTP+CCID mode, and one Gemalto GemPC Express reader. Running ykneomgr -l results in the following output: </p>
<p>0: Gemalto GemPC Express 00 00<br />
1: Yubico Yubikey NEO CCID 01 00<br />
2: Yubico Yubikey NEO OTP+CCID 02 00 </p>
<p> To use the second NEO, you could use -r OTP+CCID as follows: </p>
<p>ykneomgr &#8211;reader OTP+CCID &#8211;applet-list </p>
<p> To use the first NEO, you could match on the trailing digits which is the device number. For example: </p>
<p>ykneomgr &#8211;reader 01 &#8211;applet-list</p>
<h2>TROBLESHOOTING</h2>
<p> Debug messages are printed if you pass the &#8211;debug parameter, which can be useful for debugging or deeper analysis. </p>
<p> The error &quot;No device found&quot; can be because a number of reasons. The simplest, of course, is that the device really is not connected to the machine (USB or NFC). Another reason may be that it is in a mode where &quot;ykneomgr&quot; cannot talk to it. This can happen if the device is in OTP-only mode (mode 0), where you must use the &quot;ykpersonalize&quot; tool to mode switch it from the OTP-only mode. It can also happen if the device is in a MODE_FLAG_EJECT mode (i.e., 81 or 82). If that is the case, you must touch the button in order to &quot;insert&quot; the virtual smartcard before you can invoke &quot;ykneomgr&quot;.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs at &lt;yubico-devel [at] googlegroups.com&gt;. </p>
<h2>Index</h2>
