---
title: "pinentry-kwallet(1)"
name: "pinentry-kwallet"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pinentry-kwallet/"
description: "pinentry-kwallet – kwallet-based pass-phrase dialog for use with GnuPG"
---

<h2>NAME</h2>
<p> <code>pinentry-kwallet</code> &#8211; kwallet-based pass-phrase dialog for use with GnuPG</p>
<h2>SYNOPSIS</h2>
<p> [-<code>q</code> ] [<i>options</i> ]</p>
<h2>DESCRIPTION</h2>
<p> is a kwallet- and pinentry-based pass-phrase dialog for use with GnuPG. It is intended to be called from the gpg-agent1 daemon and not invoked directly. </p>
<p> replaces the regular <code>pinentry-program</code> stanza set in ~/.gnupg/gpg-agent.conf and looks up the passphrases requested in the KWallet first, falling back to <code>pinentry</code> only if not found. The user is given the option to store it in the KWallet afterwards. Negative answers to this are also stored in the KWallet to avoid asking each time. </p>
<p> (like other pinentry variants) talks a simplified subset of the regular Assuan protocol on stdio; all commands, even unknown ones, are passed through to a <code>pinentry</code> co-process during run-time, even if the latter is never used. It accepts the same options as <code>pinentry</code> even unknown ones, because it is designed to plug in. As an exception, &#8211;<code>q</code> makes more quiet (suppress warnings on stderr), and &#8211;<code>V</code> displays the version on stderr (unless &#8211;<code>q )</code> </p>
<p> attempts sophisticated error handling: if an error dialogue is displayed, an internal counter is increased. If the counter reaches 2, the value stored in the KWallet is ignored, and the user is asked anew. The counter is stored in the KWallet, which is suboptimal but necessary, because <a href="/docs/linux/man/1-gpg2/">gpg2</a>(1) does not re-use the Assuan sessions, instead spawning a new each time a passphrase is required (rather stupid). Error counters are valid for 15 seconds since their last increasement.</p>
<h2>RETURN VALUES</h2>
<p> exits 1 if it is called recursively, 0 if help or version information are requested, and return codes do not matter in any other cases because errors are signalled in-band. It will exit 0 after the Assuan session is terminated.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> The X11 display to use for child processes. If not set, will immediately replace itself with the slave <code>PINENTRY</code> programme to use.</p>
<dt><code>GPG_TERM</code></p>
<dd> Terminal type of the current tty.</p>
<dt><code>GPG_TTY</code></p>
<dd> The current terminal.</p>
<dt><code>PINENTRY</code></p>
<dd> The <code>pinentry</code> programme to use. Default: &#8220;pinentry&#8221;</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-date/">date</a>(1), gpg-agent1, <a href="/docs/linux/man/1-gpg2/">gpg2</a>(1), <a href="/docs/linux/man/1-kwalletcli/">kwalletcli</a>(1), kwalletcli_getpin1, <a href="/docs/linux/man/1-mksh/">mksh</a>(1), pinentry-curses1, pinentry-gtk-21, pinentry-qt1, pinentry-x111</p>
<h2>AUTHORS</h2>
<p> was written by An mirabilos Aq m@mirbsd.org mostly for tarent solutions GmbH.</p>
<h2>CAVEATS</h2>
<p> Some newer pinentry features, such as three-button operation, are not supported yet. </p>
<p> Some commands, such as version inquiry, as passed through to the pinentry coprocess indiscriminately, which may lead to strange results, should the protocol change or extend. </p>
<h2>Index</h2>
