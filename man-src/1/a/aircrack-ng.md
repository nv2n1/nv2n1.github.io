---
title: "aircrack-ng(1)"
name: "aircrack-ng"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aircrack-ng/"
description: "aircrack-ng – a 802.11 WEP / WPA-PSK key cracker"
---

<h2 class="name">NAME</h2>
<p> aircrack-ng &#8211; a 802.11 WEP / WPA-PSK key cracker </p>
<h2>SYNOPSIS</h2>
<p> <code>aircrack-ng</code> [options] &lt;.cap / .ivs file(s)&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>aircrack-ng</code> is an 802.11 WEP and WPA/WPA2-PSK key cracking program.<br />
 It can recover the WEP key once enough encrypted packets have been captured with airodump-ng. This part of the aircrack-ng suite determines the WEP key using two fundamental methods. The first method is via the PTW approach (Pyshkin, Tews, Weinmann). The main advantage of the PTW approach is that very few data packets are required to crack the WEP key. The second method is the FMS/KoreK method. The FMS/KoreK method incorporates various statistical attacks to discover the WEP key and uses these in combination with brute forcing.<br />
 Additionally, the program offers a dictionary method for determining the WEP key. For cracking WPA/WPA2 pre-shared keys, a wordlist (file or stdin) or an airolib-ng has to be used.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>Common options:</code></p>
<dd>
<dt><i>-a &lt;amode&gt;</i></p>
<dd> Force the attack mode, 1 or wep for WEP and 2 or wpa for WPA-PSK.</p>
<dt><i>-e &lt;essid&gt;</i></p>
<dd> Select the target network based on the ESSID. This option is also required for WPA cracking if the SSID is cloacked. For SSID containing special characters, see <a rel="nofollow" href="http://www.aircrack-ng.org/doku.php?id=faq#how_to_use_spaces_double_quote_and_single_quote_etc._in_ap_names">http://www.aircrack-ng.org/doku.php?id=faq#how_to_use_spaces_double_quote_and_single_quote_etc._in_ap_names</a></p>
<dt><i>-b &lt;bssid&gt; or &#8211;bssid &lt;bssid&gt;</i></p>
<dd> Select the target network based on the access point MAC address.</p>
<dt><i>-p &lt;nbcpu&gt;</i></p>
<dd> Set this option to the number of CPUs to use (only available on SMP systems). By default, it uses all available CPUs</p>
<dt><i>-q</i></p>
<dd> If set, no status information is displayed.</p>
<dt><i>-C &lt;macs&gt; or &#8211;combine &lt;macs&gt;</i></p>
<dd> Merges all those APs MAC (separated by a comma) into a virtual one.</p>
<dt><i>-l &lt;file&gt;</i></p>
<dd> Write the key into a file.</p>
<dt><i>-E &lt;file&gt;</i></p>
<dd> Create Elcomsoft Wireless Security Auditor (EWSA) Project file v3.02.</dl>
<dl>
<dt><code>Static WEP cracking options:</code></p>
<dd>
<dt><i>-c</i></p>
<dd> Search alpha-numeric characters only.</p>
<dt><i>-t</i></p>
<dd> Search binary coded decimal characters only.</p>
<dt><i>-h </i></p>
<dd> Search the numeric key for Fritz!BOX</p>
<dt><i>-d &lt;mask&gt; or &#8211;debug &lt;mask&gt;</i></p>
<dd> Specify mask of the key. For example: A1:XX:CF</p>
<dt><i>-m &lt;maddr&gt;</i></p>
<dd> Only keep the IVs coming from packets that match this MAC address. Alternatively, use -m ff:ff:ff:ff:ff:ff to use all and every IVs, regardless of the network (this disables ESSID and BSSID filtering).</p>
<dt><i>-n &lt;nbits&gt;</i></p>
<dd> Specify the length of the key: 64 for 40-bit WEP, 128 for 104-bit WEP, etc., until 512 bits of length. The default value is 128.</p>
<dt><i>-i &lt;index&gt;</i></p>
<dd> Only keep the IVs that have this key index (1 to 4). The default behaviour is to ignore the key index in the packet, and use the IV regardless.</p>
<dt><i>-f &lt;fudge&gt;</i></p>
<dd> By default, this parameter is set to 2. Use a higher value to increase the bruteforce level: cracking will take more time, but with a higher likelihood of success.</p>
<dt><i>-k &lt;korek&gt;</i></p>
<dd> There are 17 KoreK attacks. Sometimes one attack creates a huge false positive that prevents the key from being found, even with lots of IVs. Try -k 1, -k 2, &#8230; -k 17 to disable each attack selectively.</p>
<dt><i>-x or -x0</i></p>
<dd> Disable last keybytes bruteforce (not advised).</p>
<dt><i>-x1</i></p>
<dd> Enable last keybyte bruteforcing (default)</p>
<dt><i>-x2</i></p>
<dd> Enable last two keybytes bruteforcing.</p>
<dt><i>-X</i></p>
<dd> Disable bruteforce multithreading (SMP only).</p>
<dt><i>-s</i></p>
<dd> Shows ASCII version of the key at the right of the screen.</p>
<dt><i>-y </i></p>
<dd> This is an experimental single brute-force attack which should only be used when the standard attack mode fails with more than one million IVs.</p>
<dt><i>-z </i></p>
<dd> Uses PTW (Andrei Pyshkin, Erik Tews and Ralf-Philipp Weinmann) attack (default attack).</p>
<dt><i>-P &lt;num&gt; or &#8211;ptw-debug &lt;num&gt;</i></p>
<dd> PTW debug: 1 Disable klein, 2 PTW.</p>
<dt><i>-K</i></p>
<dd> Use KoreK attacks instead of PTW.</p>
<dt><i>-D or &#8211;wep-decloak</i></p>
<dd> WEP decloak mode.</p>
<dt><i>-1 or &#8211;oneshot</i></p>
<dd> Run only 1 try to crack key with PTW.</p>
<dt><i>-M &lt;num&gt;</i></p>
<dd> Specify maximum number of IVs to use.</dl>
<dl>
<dt><code>WEP and WPA-PSK cracking options</code></p>
<dd>
<dt><i>-w &lt;words&gt;</i></p>
<dd> Path to a dictionary file for wpa cracking. Specify &quot;-&quot; to use stdin. Here is a list of wordlists: <a rel="nofollow" href="http://www.aircrack-ng.org/doku.php?id=faq#where_can_i_find_good_wordlists">http://www.aircrack-ng.org/doku.php?id=faq#where_can_i_find_good_wordlists</a></dl>
<dl>
<dt><code>WPA-PSK cracking options:</code></p>
<dd>
<dt><i>-S</i></p>
<dd> WPA cracking speed test.</p>
<dt><i>-r &lt;database&gt;</i></p>
<dd> Path to the airolib-ng database. Cannot be used with &#8216;-w&#8217;.</dl>
<dl>
<dt><code>Other options:</code></p>
<dd>
<dt><i>-H or &#8211;help</i></p>
<dd> Show help screen</p>
<dt><i>-u or &#8211;cpu-detect</i></p>
<dd> Provide information on the number of CPUs and MMX/SSE support</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Adam Cecile &lt;gandalf [at] le-vert.net&gt; for the Debian system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-airbase-ng/">airbase-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-aireplay-ng/">aireplay-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airmon-ng/">airmon-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airodump-ng/">airodump-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airodump-ng-oui-update/">airodump-ng-oui-update</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airserv-ng/">airserv-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airtun-ng/">airtun-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-besside-ng/">besside-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-easside-ng/">easside-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-tkiptun-ng/">tkiptun-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-wesside-ng/">wesside-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/1-airdecap-ng/">airdecap-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airdecloak-ng/">airdecloak-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airolib-ng/">airolib-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-besside-ng-crawler/">besside-ng-crawler</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-buddy-ng/">buddy-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-ivstools/">ivstools</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-kstats/">kstats</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-makeivs-ng/">makeivs-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-packetforge-ng/">packetforge-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-wpaclean/">wpaclean</a>(1)</code> </p>
<h2>Index</h2>
