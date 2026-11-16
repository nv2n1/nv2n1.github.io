---
title: "strongimcv_pki-acert(1)"
name: "strongimcv_pki-acert"
section: "1"
letter: "s"
url: "/docs/linux/man/1-strongimcv_pki-acert/"
description: "pki –acert – Issue an attribute certificate"
---

<p>pki &#8211;acert &#8211; Issue an attribute certificate</p>
<h2>Synopsis</h2>
<p>[ <code>&#8211;in </code><i>file</i> ] [ <code>&#8211;group </code><i>membership</i> ] <code>&#8211;issuerkey~</code><i>file</i><code>|&#8211;issuerkeyid~</code><i>hex</i> <code>&#8211;issuercert~</code><i>file</i> [ <code>&#8211;lifetime </code><i>hours</i> ] [ <code>&#8211;not-before </code><i>datetime</i> ] [ <code>&#8211;not-after </code><i>datetime</i> ] [ <code>&#8211;serial </code><i>hex</i> ] [ <code>&#8211;digest </code><i>digest</i> ] [ <code>&#8211;outform </code><i>encoding</i> ] [ <code>&#8211;debug </code><i>level</i> ] <code>&#8211;options~</code><i>file</i> <code>-h</code> | <code>&#8211;help</code></p>
<h2>Description</h2>
<p>This sub-command of <code><a href="/docs/linux/man/1-pki/">pki</a></code>(1) is used to issue an attribute certificate using an issuer certificate with its private key and the holder certificate.</p>
<h2>Options</h2>
<dl COMPACT>
<dt><code>-h, &#8211;help</code></dt>
<dd>Print usage information with a summary of the available options.</dd>
<dt><code>-v, &#8211;debug </code><i>level</i></dt>
<dd>Set debug level, default: 1.</dd>
<dt><code>-+, &#8211;options </code><i>file</i></dt>
<dd>Read command line options from <i>file</i>.</dd>
<dt><code>-i, &#8211;in </code><i>file</i></dt>
<dd>Holder certificate to issue an attribute certificate for. If not given the certificate is read from <i>STDIN</i>.</dd>
<dt><code>-m, &#8211;group </code><i>membership</i></dt>
<dd>Group membership the attribute certificate shall certify. The specified group is included as a string. To include multiple groups, the option can be repeated.</dd>
<dt><code>-k, &#8211;issuerkey </code><i>file</i></dt>
<dd>Issuer private key file. Either this or <code>&#8211;issuerkeyid</code> is required.</dd>
<dt><code>-x, &#8211;issuerkeyid </code><i>hex</i></dt>
<dd>Key ID of a issuer private key on a smartcard. Either this or <code>&#8211;issuerkey</code> is required.</dd>
<dt><code>-c, &#8211;issuercert </code><i>file</i></dt>
<dd>Issuer certificate file. Required.</dd>
<dt><code>-l, &#8211;lifetime </code><i>hours</i></dt>
<dd>Hours the attribute certificate is valid, default: 24. Ignored if both an absolute start and end time are given.</dd>
<dt><code>-F, &#8211;not-before </code><i>datetime</i></dt>
<dd>Absolute time when the validity of the AC begins. The datetime format is defined by the <code>&#8211;dateform</code> option.</dd>
<dt><code>-T, &#8211;not-after </code><i>datetime</i></dt>
<dd>Absolute time when the validity of the AC ends. The datetime format is defined by the <code>&#8211;dateform</code> option.</dd>
<dt><code>-D, &#8211;dateform </code><i>form</i></dt>
<dd><a href="/docs/linux/man/3-strptime/">strptime</a>(3) format for the <code>&#8211;not-before</code> and <code>&#8211;not-after</code> options, default: <code>%d.%m.%y %T</code></dd>
<dt><code>-s, &#8211;serial </code><i>hex</i></dt>
<dd>Serial number in hex. It is randomly allocated by default.</dd>
<dt><code>-g, &#8211;digest </code><i>digest</i></dt>
<dd>Digest to use for signature creation. One of <i>md5</i>, <i>sha1</i>, <i>sha224</i>, <i>sha256</i>, <i>sha384</i>, or <i>sha512</i>. Defaults to <i>sha1</i>.</dd>
<dt><code>-f, &#8211;outform </code><i>encoding</i></dt>
<dd>Encoding of the created certificate file. Either <i>der</i> (ASN.1 DER) or <i>pem</i> (Base64 PEM), defaults to <i>der</i>.</dd></dl>
<h2>Examples</h2>
<p>To save repetitive typing, command line options can be stored in files. Lets assume <i>acert.opt</i> contains the following contents: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;issuercert aacert.der &#8211;issuerkey aakey.der &#8211;digest sha256 &#8211;lifetime 4 </p>
<p> Then the following command can be used to issue an attribute certificate based on a holder certificate and the options above: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>pki &#8211;acert &#8211;options acert.opt &#8211;in holder.der &#8211;group sales &#8211;group finance -f pem </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pki/">pki</a></code>(1)</p>
