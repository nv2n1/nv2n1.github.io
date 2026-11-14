---
title: "kwalletaskpass(1)"
name: "kwalletaskpass"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kwalletaskpass/"
description: "kwalletaskpass – kwallet-based pass-phrase dialog for use with OpenSSH"
---

<h2>NAME</h2>
<p> <code>kwalletaskpass</code> &#8211; kwallet-based pass-phrase dialog for use with OpenSSH</p>
<h2>SYNOPSIS</h2>
<p> [<i>options</i> ] <i>label</i></p>
<h2>DESCRIPTION</h2>
<p> is a kwallet- and pinentry-based pass-phrase dialog for use with OpenSSH. It is intended to be called from the ssh-add1 programme and not invoked directly. </p>
<p> If a passphrase is requested, works by first looking up the passphrase in the KWallet by means of <a href="/docs/linux/man/1-kwalletcli/">kwalletcli</a>(1); using it if found, then calling kwalletcli_getpin1 to interactively retrieve an answer from the user via <code>pinentry</code> otherwise. If the user specifies a passphrase, kwalletcli_getpin1 is run again to ask if the passphrase should be stored in the KWallet. Negative answers will be stored in the KWallet to avoid being asked each time. uses the KWallet folders <code>kwalletaskpass</code> and <code>kwalletaskpass-blacklist</code> with matching entry names. </p>
<p> If anything other than a key passphrase is requested, it is merely relayed to kwalletcli_getpin1. Some requests are known to require a boolean answer and are relayed using the boolean query flag; all others are relayed using a PIN query. <a href="/docs/linux/man/1-ssh/">ssh</a>(1) accepts either the literal word &#8220;yes&#8221; (case-insensitively matched) or an empty answer (both only when using the OK button) as confirmation. </p>
<p> There are currently no options.</p>
<h2>RETURN VALUES</h2>
<p> exits 0 on success, 1 if the user cancelled the dialogue, or &gt;1 if an error occurred.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> The X11 display to use for child processes. If this is unset or empty, <code>kwalletcli</code> will not be called.</p>
<dt><code>PINENTRY</code></p>
<dd> The <code>pinentry</code> programme to use. The default is inherited from kwalletcli_getpin1.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-kwalletcli/">kwalletcli</a>(1), kwalletcli_getpin1, ssh-add1, ssh-askpass1</p>
<h2>AUTHORS</h2>
<p> was written by An mirabilos Aq m@mirbsd.org mostly for tarent solutions GmbH. The idea came from an askpass.C file found somewhere on the &#8216;net, with no author information. Since it was licenced less freely, this is a rewrite from scratch; modular and with more functionality, too. </p>
<h2>Index</h2>
