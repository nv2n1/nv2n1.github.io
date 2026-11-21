---

title: "sendsms(1)"
name: "sendsms"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sendsms/"
description: "sendsms – command line tool to send SMSes using gnokii"
---

<h2>NAME</h2>
<p> sendsms &#8211; command line tool to send SMSes using gnokii</p>
<p> <code>sendsms </code><i>[OPTIONS]</i> </p>
<p> <code>sendsms</code> allows you to send a SMS using gnokii not knowing the syntax of gnokii command. It is written using dialog and allows to send a text SMS choosing recipients from the phone address book or entering it manually. </p>
<h3>OPTIONS</h3>
<p> Available options:</p>
<dl>
<dt><code>[&#8211;debug|-D]</code></dt>
<dd> May bother with more debugging messages. For debugging purpose.</dd>
<dt><code>&#8211;simul[ate], -S</code></dt>
<dd> Simulation mode. Doesn&#8217;t really send SMS by phone. Only simulates. For debugging purpose.</dd>
<dt><code>&#8211;forceSMread, -s</code></dt>
<dd> Forces <code>sendsms</code> to read phonebook from SIM card, and to parse the generated file in order to update the numbers&#8217; list (useful only if required to pickup number from the phone&#8217;s memory). See NOTE.</dd>
<dt><code>&#8211;forceMEread, -m</code></dt>
<dd> Forces <code>sendsms</code> to read phonebook from phone memory, and to parse the generated file in order to update the numbers&#8217; list (useful only if required to pickup number from the phone&#8217;s memory). See NOTE.</dd>
<dt><code>&#8211;skipgnokiicheck, -K</code></dt>
<dd> Skip the test of the presence of binary &#8216;gnokii&#8217;. (It must be somewhere in your $PATH). It allows you to try this script program, even if you don&#8217;t have &#8216;gnokii&#8217; already. ;)</dd>
<dt><code>&#8211;smsset, &#8211;setsms</code></dt>
<dd> Allows you to preset a SMS message from STDIN. (pipe or input redirection). This message will be proposed on the &#8216;SMS message&#8217; field during the program input cycle.</dd>
<dt><code>&#8211;help, -h,&nbsp;<wbr>/h</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version, -V</code></dt>
<dd> output version information and exit&quot;</dd>
<dt>NOTE:</dt>
<dd> If you require to pickup number from phone&#8217;s memory (or from SIM card), for the first time, it anyway reads phonebook from your mobile phone. (It may take a while&#8230; please, be patient ;-) </dd>
</dl>
<h2>BUGS</h2>
<p> None reported. </p>
<h2>AUTHOR</h2>
<p> Sendsms was written by Gabriele Zappi &#8211; Rimini &lt;gzappi [at] inwind.it&gt;. </p>
<p> This manual page was written by Pawel Kot. </p>
<h2>COPYING</h2>
<p> This program is distributed under the GNU Public License. </p>
<h2>SEE ALSO</h2>
<p> gnokii </p>
