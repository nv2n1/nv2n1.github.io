---
title: "sap(7)"
name: "sap"
section: "7"
letter: "s"
url: "/docs/linux/man/7-sap/"
description: "sap – Service Access Point specification"
---

<p>sap &#8211; Service Access Point specification</p>
<h2>Description</h2>
<p>The <code>text2sap</code> and <code>sap2text</code> functions use the format described in this man page. Because all standard ATM tools on Linux use those functions to convert to or from the textual representation of SAP specifications, they expect them in the same format too. The SAP is divided into two parts: the <i>broadband high layer information</i> (BHLI) and the <i>broadband low layer information</i> (BLLI). A SAP can contain one, both, or none of them. In the latter case, the SAP is usually considered as a wildcard SAP, i.e. a SAP that is compatible with any other SAP. Each part begins with its name (<code>bhli</code> or <code>blli</code>), followed by a colon and a (non-empty) list of attributes, which are of the form <i>attribute</i><code>=</code><i>value</i>. Some attributes have sub-attributes, which follow them. Everything that isn&#8217;t separated by a colon or an equal sign is separated by a comma. Values which are a number of bytes are specified as the corresponding sequence of pairs of hex digits. The sequence can be optionally prefixed with <code>0x</code>. Values with are integers in a given range can be specified in decimal (no prefix), octal (<code>0</code> prefix), and hexadecimal (<code>0x</code> prefix). The following, mutually exclusive attributes are allowed in the <code>bhli</code> part (see the corresponding ATM Forum and ITU documents for the semantics):</p>
<dl>
<dt><code>iso=</code><i>1-8 bytes</i></p>
<dd>ISO</p>
<dt><code>user=</code><i>1-8 bytes</i></p>
<dd>User-specific</p>
<dt><code>hlp=</code><i>4 bytes</i></p>
<dd>High layer profile. Note that this attribute only exists on UNI 3.0. <code>text2sap</code> only recognizes it if your system is configured to accept UNI 3.0 message formats.</p>
<dt><code>oui=</code><i>3 bytes</i><code>,id=</code><i>4 bytes</i></p>
<dd>Vendor-specific application identifier</dl>
<p> The structure of the <code>bhli</code> part is more complex. It distinguishes three layers, <code>l1</code>, <code>l2</code>, and <code>l3</code>, of which the first one is presently unsupported. For layer two, the following (mutually exclusive) possibilities exist:</p>
<dl>
<dt><code>l2=iso1745</code></p>
<dd>Basic mode ISO 1745</p>
<dt><code>l2=q291</code></p>
<dd>ITU-T Q.291 (Rec. I.441)</p>
<dt><code>l2=lapb</code></p>
<dd>Extended LAPB, half-duplex (Rec. T.71)</p>
<dt><code>l2=iso8802</code></p>
<dd>LAN LLC (ISO/IEC 8802/2)</p>
<dt><code>l2=x75</code></p>
<dd>ITU-T X.75, SLP</p>
<dt><code>l2=x25_ll</code>&nbsp;<wbr>&#8230;</p>
<dd>ITU-T X.25, link layer. This attribute and the following attributes through <code>l2=iso7776</code> can optionally be followed by one or more of the following sub-attributes: <code>mode=</code><i>mode</i> (mode of operation, either <code>norm</code> or <code>ext</code>), and <code>window=</code><i>window size</i> (window size in k, 1-127).</p>
<dt><code>l2=x25_ml</code>&nbsp;<wbr>&#8230;</p>
<dd>ITU-T X.25, multilink</p>
<dt><code>l2=hdlc_arm</code>&nbsp;<wbr>&#8230;</p>
<dd>HDLC ARM (ISO/IEC 4335)</p>
<dt><code>l2=hdlc_nrm</code>&nbsp;<wbr>&#8230;</p>
<dd>HDLC NRM (ISO/IEC 4335)</p>
<dt><code>l2=hdlc_abm</code>&nbsp;<wbr>&#8230;</p>
<dd>HDLC ABM (ISO/IEC 4335)</p>
<dt><code>l2=q992</code>&nbsp;<wbr>&#8230;</p>
<dd>ITU-T Q.922</p>
<dt><code>l2=iso7776</code>&nbsp;<wbr>&#8230;</p>
<dd>ISO 7776 DTE-DTE</p>
<dt><code>l2=user,info=</code><i>information</i></p>
<dd>User-specified. <i>information</i> is an integer in the range 0 to 255.</dl>
<p> For layer three, the following (again, mutually exclusive) possibilities exist:</p>
<dl>
<dt><code>l3=iso8473</code></p>
<dd>ITU-T X.233 | ISO/IEC 8473</p>
<dt><code>l3=t70</code></p>
<dd>ITU-T T.70 minimum network layer</p>
<dt><code>l3=h321</code></p>
<dd>ITU-T Recommendation H.321</p>
<dt><code>l3=x25</code>&nbsp;<wbr>&#8230;</p>
<dd>ITU-T X.25, packet layer. This attribute and the following attributes through <code>l3=x223</code> can optionally be followed by one or more of the following sub-attributes: <code>mode=</code><i>mode</i> (see above), <code>size=</code><i>default packet size</i> (4-12, corresponding to 16-4096), <code>window=</code><i>window size</i> (see above).</p>
<dt><code>l3=iso8208</code>&nbsp;<wbr>&#8230;</p>
<dd>ISO/IEC 8208</p>
<dt><code>l3=x223</code>&nbsp;<wbr>&#8230;</p>
<dd>ITU-T X.223 | ISO/IEC 8878</p>
<dt><code>l3=tr9577,ipi=</code><i>identifier</i>&nbsp;<wbr>&#8230;</p>
<dd>ISO/IEC TR 9577. <i>identifier</i> is the initial protocol identifier in the range 0-255. For SNAP (0x80), the keyword <code>snap</code> can be used, and the following sub-attributes have to be specified: <code>oui=</code><i>3 bytes</i>, and <code>pid=</code><i>2 bytes</i>.</p>
<dt><code>l2=user,info=</code><i>information</i></p>
<dd>User-specified, see above.</p>
<dt><code>l3=h310</code>&nbsp;<wbr>&#8230;</p>
<dd>ITU-T Recommendation H.310. The sub-attribute <code>term=</code><i>type</i> (terminal type, <code>rx</code>, <code>tx</code>, or <code>rxtx</code>) is recognized. If present, it enables the two additional sub-attributes <code>fw_mpx=</code><i>capability</i> (forward multiplexing capability, <code>ts</code>, <code>ts_fec</code>, <code>ps</code>, <code>ps_fec</code>, or <code>h221</code>) and <code>bw_mpx=</code><i>capability</i>. Both are optional.</dl>
<p> Note that commas must never follow colons or other commas. Also, whitespace is not allowed inside a SAP specification. SAP specifications are case-insensitive. On input, items must be written in exactly the order used in this document. </p>
<h2>Examples</h2>
<dl>
<dt><code>blli:l2=iso8802</code></p>
<dd>Classical IP over ATM (RFC1577)</p>
<dt><code>bhli:oui=0x0060D7,id=0x01000001,blli:l2=iso8802</code></p>
<dd>Arequipa (RFC2170)</p>
<dt><code>blli:l3=tr9577,ipi=snap,oui=0x00A03E,pid=0x0002</code></p>
<dd>LAN Emulation</dl>
<h2>Author</h2>
<p>Werner Almesberger, EPFL LRC &lt;werner.almesberger [at] lrc.di.epfl.ch&gt;</p>
