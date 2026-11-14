---
title: "iwpriv(8)"
name: "iwpriv"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iwpriv/"
description: "iwpriv – configure optionals (private) parameters of a wireless network interface"
---

<p>iwpriv &#8211; configure optionals (private) parameters of a wireless network interface</p>
<h2>Synopsis</h2>
<p><code>iwpriv [</code><i>interface</i><code>]</code><br />
 <code>iwpriv </code><i>interface private-command </i><code>[</code><i>private-parameters</i><code>]</code><br />
 <code>iwpriv </code><i>interface private-command </i><code>[</code><i>I</i><code>] [</code><i>private-parameters</i><code>]</code><br />
 <code>iwpriv </code><i>interface</i><code> &#8211;all</code></p>
<h2>Description</h2>
<p><code>Iwpriv</code> is the companion tool to <i><a href="/docs/linux/man/8-iwconfig/">iwconfig</a></i>(8). <code>Iwpriv</code> deals with parameters and setting specific to each driver (as opposed to <i>iwconfig</i> which deals with generic ones). </p>
<p> Without any argument, <code>iwpriv</code> list the available private commands available on each interface, and the parameters that they require. Using this information, the user may apply those interface specific commands on the specified interface. </p>
<p> In theory, the documentation of each device driver should indicate how to use those interface specific commands and their effect.</p>
<h2>Parameters</h2>
<dl>
<dt><i>private-command</i> [<i>private-parameters</i>]</p>
<dd>Execute the specified <i>private-command</i> on the interface.<br />
 The command may optionally take or require arguments, and may display information. Therefore, the command line parameters may or may not be needed and should match the command expectations. The list of commands that <code>iwpriv</code> displays (when called without argument) should give you some hints about those parameters.<br />
 However you should refer to the device driver documentation for information on how to properly use the command and the effect.</p>
<dt><i>private-command </i>[<i>I</i>] [<i>private-parameters</i>]</p>
<dd>Idem, except that <i>I</i> (an integer) is passed to the command as a <i>Token Index</i>. Only some command will use the Token Index (most will ignore it), and the driver documentation should tell you when it&#8217;s needed.</p>
<dt><code>-a</code>/<code>&#8211;all</code></p>
<dd>Execute and display all the private commands that don&#8217;t take any arguments (i.e. read only).</dl>
<h2>Display</h2>
<p>For each device which support private commands, <i>iwpriv</i> will display the list of private commands available. </p>
<p> This include the name of the private command, the number or arguments that may be set and their type, and the number or arguments that may be display and their type. </p>
<p> For example, you may have the following display :<br />
 <code>eth0 Available private ioctl :</code><br />
 <code> setqualthr (89F0) : set 1 byte &amp; get 0</code><br />
 <code> gethisto (89F7) : set 0 &amp; get 16 int</code> </p>
<p> This indicate that you may set the quality threshold and display an histogram of up to 16 values with the following commands :<br />
 <i> iwpriv eth0 setqualthr 20</i><br />
 <i> iwpriv eth0 gethisto</i></p>
<h2>Author</h2>
<p>Jean Tourrilhes &#8211; jt [at] hpl.hp.com</p>
<h2>Files</h2>
<p><i>/proc/net/wireless</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-iwconfig/">iwconfig</a></code>(8), <code><a href="/docs/linux/man/8-iwlist/">iwlist</a></code>(8), <code><a href="/docs/linux/man/8-iwevent/">iwevent</a></code>(8), <code><a href="/docs/linux/man/8-iwspy/">iwspy</a></code>(8), <code><a href="/docs/linux/man/7-wireless/">wireless</a></code>(7). </p>
