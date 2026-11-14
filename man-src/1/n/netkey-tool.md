---
title: "netkey-tool(1)"
name: "netkey-tool"
section: "1"
letter: "n"
url: "/docs/linux/man/1-netkey-tool/"
description: "netkey-tool – administrative utility for Netkey E4 cards"
---

<h2 class="name">NAME</h2>
<p> netkey-tool &#8211; administrative utility for Netkey E4 cards </p>
<h2>SYNOPSIS</h2>
<p> <code>netkey-tool</code> [OPTIONS] [COMMAND]</p>
<h2>DESCRIPTION</h2>
<p> The <code>netkey-tool</code> utility can be used from the command line to perform some smart card operations with NetKey E4 cards that cannot be done easily with other OpenSC-tools, such as changing local PINs, storing certificates into empty NetKey E4 cert-files or displaying the initial PUK-value.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code>, <code>-h</code></p>
<dl>
<dt>
<dd> Displays a short help message.</dl>
<p> <code>&#8211;reader</code> number, <code>-r</code> number</p>
<dl>
<dt>
<dd> Use smart card in specified reader. Default is reader 0.</dl>
<p> <code>-v</code></p>
<dl>
<dt>
<dd> Causes <code>netkey-tool</code> to be more verbose. This options may be specified multiple times to increase verbosity.</dl>
<p> <code>&#8211;pin</code> pin-value, <code>-p</code> pin-value</p>
<dl>
<dt>
<dd> Specifies the current value of the global PIN.</dl>
<p> <code>&#8211;puk</code> pin-value, <code>-u</code> pin-value</p>
<dl>
<dt>
<dd> Specifies the current value of the global PUK.</dl>
<p> <code>&#8211;pin0</code> pin-value, <code>-0</code> pin-value</p>
<dl>
<dt>
<dd> Specifies the current value of the local PIN0 (aka local PIN).</dl>
<p> <code>&#8211;pin1</code> pin-value, <code>-1</code> pin-value</p>
<dl>
<dt>
<dd> Specifies the current value of the local PIN1 (aka local PUK).</dl>
<h2>PIN FORMAT</h2>
<p> With the <code>-p</code>, <code>-u</code>, <code>-0</code> or the <code>-1</code> one of the cards pins may be specified. You may use plain ascii-strings (i.e. 123456) or a hex-string (i.e. 31:32:33:34:35:36). A hex-string must consists of exacly n 2-digit hexnumbers separated by n-1 colons. Otherwise it will be interpreted as an ascii string. For example :12:34: and 1:2:3:4 are both pins of length 7, while 12:34 and 01:02:03:04 are pins of length 2 and 4.</p>
<h2>COMMANDS</h2>
<p> When used without any options or commands, <code>netkey-tool</code> will display information about the smart cards pins and certificates. This will not change your card in any aspect (assumed there are no bugs in <code>netkey-tool</code>). In particular the tries-left counters of the pins are investigated without doing actual pin-verifications. </p>
<p> If you specify the global PIN via the <code>&#8211;pin</code> option, <code>netkey-tool</code> will also display the initial value of the cards global PUK. If your global PUK was changed <code>netkey-tool</code> will still diplay its initial value. There&#8217;s no way to recover a lost global PUK once it was changed. There&#8217;s also no way to display the initial value of your global PUK without knowing the current value of your global PIN. </p>
<p> For most of the commands that <code>netkey-tool</code> can execute, you have to specify one pin. One notable exeption is the <code>nullpin</code> command, but this command can only be executed once in the lifetime of a NetKey E4 card. </p>
<p> <code>unblock</code> { <code>pin</code> | <code>pin0</code> | <code>pin1</code> }</p>
<dl>
<dt>
<dd> This unblocks the specified pin. You must specify another pin to be able to do this and if you don&#8217;t specify a correct one, <code>netkey-tool</code> will tell you which one is needed.</dl>
<p> <code>change</code> { <code>pin</code> | <code>puk</code> | <code>pin0</code> | <code>pin1</code> } new-pin</p>
<dl>
<dt>
<dd> This changes the value of the specified pin to the given new value. You must specify either the current value of the pin or another pin to be able to do this and if you don&#8217;t specify a correct one, <code>netkey-tool</code> will tell you which one is needed.</dl>
<p> <code>nullpin</code> initial-pin</p>
<dl>
<dt>
<dd> This command can be executed only if the global PIN of your card is in nullpin-state. There&#8217;s no way to return back to nullpin-state once you have changed your global PIN. You don&#8217;t need a pin to execute the nullpin-command. After a succesfull nullpin-command <code>netkey-tool</code> will display your cards initial PUK-value.</dl>
<p> <code>cert</code> number filename</p>
<dl>
<dt>
<dd> This command will read one of your cards certificates (as specified by <code>number</code>) and save this certificate into file <code>filename</code> in PEM-format. Certificates on a NetKey E4 card are readable without a pin, so you don&#8217;t have to specify one.</dl>
<p> <code>cert</code> filename number</p>
<dl>
<dt>
<dd> This command will read the first PEM-encoded certificate from file <code>filename</code> and store this into your smart cards certificate file <code>number</code>. Some of your smart cards certificate files might be readonly, so this will not work with all values of <code>number</code>. If a certificate file is writable you must specify a pin in order to change it. If you try to use this command without specifying a pin, <code>netkey-tool</code> will tell you which one is needed.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-opensc/">opensc</a>(7), <a href="/docs/linux/man/1-opensc-explorer/">opensc-explorer</a>(1)</p>
<h2>AUTHORS</h2>
<p> <code>netkey-tool</code> was written by Peter Koch &lt;pk_opensc [at] web.de&gt;. </p>
<h2>Index</h2>
