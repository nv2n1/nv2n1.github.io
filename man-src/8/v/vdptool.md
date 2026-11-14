---
title: "vdptool(8)"
name: "vdptool"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vdptool/"
description: "vdptool – manage the VSI associations and status of lldpad"
---

<p>vdptool &#8211; manage the VSI associations and status of lldpad</p>
<h2>Synopsis</h2>
<p><code>vdptool &lt;command&gt; [options] [argument]</code></p>
<h2>Description</h2>
<p><code>vdptool</code> is used to query and configure the VSI associations in <code>lldpad.</code> Only the ratified stardard version of the VDP protocol (also refered to as vdp22) is supported. It connects to the client interface of <code>lldpad</code> to perform these operations. <code>vdptool</code> will operate in interactive mode if it is executed without a <i>command</i>. In interactive mode, <code>vdptool</code> will also function as an event listener to print out events as they are received asynchronously from <code>lldpad</code>(still to be done). It will use libreadline for interactive input when available (still to be done).</p>
<h2>Options</h2>
<dl>
<dt><code>-i [ifname]</code></p>
<dd>specifies the network interface to which the command applies. Most <code>vdptool</code> commands require specifying a network interface.</p>
<dt><code>-V [tlvid]</code></p>
<dd>specifies the VDP tlv identifier to be set or queried.<br />
 The tlvid is an integer value used to identify specific VDP TLVs. The tlvid value is the type value for types not equal to 127 (the organizationally specific type). For organizationally specific TLVs, the tlvid is the value represented by the 3 byte OUI and 1 byte subtype &#8211; where the subtype is the lowest order byte of the tlvid.<br />
 The tlvid can be entered as a numerical value (e.g. 10 or 0xa), or for supported TLVs, as a keyword (such as assoc, deassoc, preassoc, preassoc-rr, etc). Review the <code>vdptool</code> help output to see the list of supported TLV keywords. </p>
<p> Use option -c to specify the parameters and its values to be set or queried.</p>
<dt><code>-n</code></p>
<dd>&quot;neighbor&quot; option for commands which can use it (e.g. get-tlv). Use this flag to retrieve the last VDP22 data returned from the bridge. (not yet supported).</p>
<dt><code>-c &lt;argument list&gt;</code></p>
<dd>Specifies additional parameters for TLV queries and associations commands. The argument list varies, depending on the command option <code>(-T)</code> or <code>(-t)</code>. To establish a VSI association use the command option <code>(-T)</code> and specify additional information as arguments in the form of key=value. See the <i>VSI Parameter</i> subsection and <i>Example</i> section below. To query a VSI specific association use the command option <code>(-t)</code> and specify the value of the VSI Instance Identifier (keywork uuid followed be the VSI UUID value) of the VSI association as configuration parameter.</p>
<dt><code>-r</code></p>
<dd>show raw client interface messages</p>
<dt><code>-R</code></p>
<dd>show only raw Client interface messages</p>
<dt><code>-W</code></p>
<dd>Wait for the bridge response message</dl>
<h3>VSI Parameter</h3>
<p>Each VDP22 TLVs contains a command mode, manager identifier, type identifier, type identifier version, VSI instance identifier, migration hints and filter information. The fields are explained next:</p>
<dl>
<dt><code>mode (Command Mode):</code></p>
<dd>The command mode determines the type of the VSI association to be established. It is an ascii string can be one of:</p>
<dl>
<dd>
<dl>
<dt>assoc:</p>
<dd>Create an VSI association.</p>
<dt>preassoc:</p>
<dd>Create an VSI preassociation. The association is only announced to the switch.</p>
<dt>preassoc-rr:</p>
<dd>Create an VSI preassociation. The association is only announced to the switch and the switch should reserve the resources.</p>
<dt>deassoc:</p>
<dd>Delete an VSI association.</dl>
</dl>
<p> Other strings are not recognized and return an error.</p>
<dt><code>mgrid2 (Manager identifier):</code></p>
<dd>The manager identifier is a string of up to 16 alphanumeric characters. It can also be an UUID according to RFC 4122 with optional dashes in between.</p>
<dt><code>typeid (Type Identifier):</code></p>
<dd>The type identifier is a number in the range of 0 to 2^24 &#8211; 1.</p>
<dt><code>typeidver (Type Identifier Version):</code></p>
<dd>The type identifer version is a number in the range of 0 to 255.</p>
<dt><code>uuid (VSI Instance Identifier):</code></p>
<dd>The VSI instance identifier is an UUID according to RFC 4122 with optional dashes in between.</p>
<dt><code>hints (Migration Hints):</code></p>
<dd>The migration hints is a string aiding in migration of virtual machines:</p>
<dl>
<dd>
<dl>
<dt>none:</p>
<dd>No hints available.</p>
<dt>from:</p>
<dd>The virtual machine is migrating away.</p>
<dt>to:</p>
<dd>The virtual machine is migrating to.</dl>
</dl>
<dt><code>fid (Filter Information Data):</code></p>
<dd>The filter information data can be supplied in four different formats identified by numbers in parathesis. Multiple filter information fields can be supplied, but all have to be of the same format.</p>
<dl>
<dd>
<dl>
<dt>vlan (1)</p>
<dd>A vlan number only, also known as filter information format 1. The vlan identifier is a number in the range of 1 to 2^16 &#8211; 1. The high order 4 bits are used as quality of service bits. The vlan identifier can be zero, a vlan identifier is then selected by the switch. Refer to IEEE 802.1 Qbg ratified standard for details.</p>
<dt>vlan-mac (2)</p>
<dd>A vlan number and MAC address delimited by a slash (&#8216;-&#8216;), also known as filter information format 2. The MAC address is specified in the format xx:xx:xx:xx:xx:xx. The colons are mandatory. For vlan details see (1).</p>
<dt>vlan-mac-group (4)</p>
<dd>A vlan number, MAC address and group identifier, each delimited by a slash (&#8216;-&#8216;), also known as filter information format 4. The group identifier is a 32 bit number. For vlan and MAC address details see (1) and (2).</p>
<dt>vlan&#8211;group (3)</p>
<dd>A vlan number and group identifier, delimited by two slashes (&#8216;&#8211;&#8216;), also known as filter information format 3. For vlan and group details see (1) and (4).</dl>
</dl>
<dt><code>oui (Organizationally Unique Identifier):</code></p>
<dd>This defines the optional Organizationally defined information field. This contains the specific sets of values for this entry. There can be multiple organizational specific fields, in which case there will be multiple keywords <i>oui=</i> followed by the values. The value is of the following format: oui=OUI,[Organization specific values ] The OUI specifies the name of the Organization that is responsible for defining this content. A comma is mandatory after the OUI field. The fields following this<br />
&nbsp;<wbr>is specified by the organization and hence will be decoded based on the value of this OUI field. Currently, the following values for OUI are supported.</p>
<dl>
<dd>
<dl>
<dt>cisco</p>
<dd>Specifies Cisco defined OUI.</p>
<dt></dl>
</dl>
</dl>
<h2>Commands</h2>
<dd>
<dl>
<dt><code>license</code></p>
<dd>show license information</p>
<dt><code>-h, help</code></p>
<dd>show usage information</p>
<dt><code>-v, version</code></p>
<dd>show version information</p>
<dt><code>-t, get-vsi</code></p>
<dd>get VSI information for the specified interface</p>
<dt><code>-T, set-vsi</code></p>
<dd>set VSI information for the specified interface</p>
<dt><code>-p, ping</code></p>
<dd>display the process identifier of the running lldpad process</p>
<dt><code>-q, quit</code></p>
<dd>exit from interactive mode</dl>
<h2>Notes</h2>
<p>This tool is in its early design and development phase. It it buggy, incomplete and most of the ideas have not even been thought of&#8230;. It reflects the current state of development when I had been given another work assignment. I append it so some else can continue to work on this.</p>
<h2>Examples</h2>
<dl>
<dt>Display process identifier of lldpad</p>
<dd>vdptool -p</p>
<dt>Create a VSI association on interface eth2</p>
<dd>
<pre>vdptool -i eth2 -T -V assoc -c mode=assoc -c mgrid2=blabla \
 -c typeid=5 -c uuid=1122 -c typeidver=4 -c hints=none \
 -c filter=2-52:00:00:11:22:33-200</pre>
<dt>Create a VSI association on interface eth2 and wait for the</p>
<dd>response from the bridge </p>
<pre>vdptool -i eth2 -T -W -V assoc -c mode=assoc -c mgrid2=blabla \
 -c typeid=5 -c uuid=1122 -c typeidver=4 -c hints=none \
 -c filter=0-52:00:00:11:22:33-200</pre>
<dt>Create a VSI association on interface eth2 wth OUI parameters</p>
<dd>and wait for the response from the bridge </p>
<pre>vdptool -i eth2 -T -W -V assoc -c mode=assoc -c mgrid2=blabla \
 -c typeid=5 -c uuid=1122 -c typeidver=4 -c hints=none \
 -c filter=0-52:00:00:11:22:33-200 -c oui=CompanyA,data</pre>
<dt>Create a VSI association on interface eth2 wth multiple OUI parameters</p>
<dd>and wait for the response from the bridge </p>
<pre>vdptool -i eth2 -T -W -V assoc -c mode=assoc -c mgrid2=blabla \
 -c typeid=5 -c uuid=1122 -c typeidver=4 -c hints=none \
 -c filter=0-52:00:00:11:22:33-200 -c oui=CompanyA,data \
 -c oui=CompanyB,data</pre>
<dt>Query all VSI association on interface eth2</p>
<dd>vdptool -i eth2 -t -V assoc </p>
<dt>Query VSI association on interface eth2 that matches specific</p>
<dd>VSI parameters. Any of the VSI parameters below can be omitted.<br />
 vdptool -i eth2 -t -V assoc -t -V assoc -c mode=assoc \<br />
&nbsp;<wbr>&nbsp;<wbr>-c mgrid2=blabla -c typeid=5 -c uuid=1122&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>-c typeidver=4 -c hints=none</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lldptool-dcbx/">lldptool-dcbx</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-ets/">lldptool-ets</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-pfc/">lldptool-pfc</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-app/">lldptool-app</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-med/">lldptool-med</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-vdp/">lldptool-vdp</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-evb/">lldptool-evb</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-evb22/">lldptool-evb22</a></code>(8), <code><a href="/docs/linux/man/8-dcbtool/">dcbtool</a></code>(8), <code><a href="/docs/linux/man/8-lldpad/">lldpad</a></code>(8)</p>
<h2>Copyright</h2>
<p>vdptool &#8211; VSI configuration utility </p>
<dl>
<dt>Copyright(c)</p>
<dd>(c) 2014 IBM Corporation. Portions of vdptool are based on:</p>
<dt>open-lldp-0.96</p>
<dd>
<dt>lldptool &#8211; LLDP agent configuration utility</p>
<dd>
<dt>Copyright(c)</p>
<dd>2007-2012 Intel Corporation. Portions of lldptool are based on:</p>
<dt>hostapd-0.5.7</p>
<dd>
<dt>Copyright</p>
<dd>(c) 2004-2008, Jouni Malinen &lt;j@w1.fi&gt; </p>
</dl>
<h2>License</h2>
<p>This program is free software; you can redistribute it and/or modify it under the terms and conditions of the GNU General Public License, version 2, as published by the Free Software Foundation. </p>
<p> This program is distributed in the hope it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin St &#8211; Fifth Floor, Boston, MA 02110-1301 USA. </p>
<p> The full GNU General Public License is included in this distribution in the file called &quot;COPYING&quot;.</p>
<h2>Support</h2>
<p>Contact Information: open-lldp Mailing List &lt;lldp-devel [at] open-lldp.org&gt;</p>
