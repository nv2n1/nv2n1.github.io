---
title: "snd_card_free_when_closed(9)"
name: "snd_card_free_when_closed"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_card_free_when_closed/"
description: "snd_card_free_when_closed – Disconnect the card, free it later eventually"
---

<p>snd_card_free_when_closed &#8211; Disconnect the card, free it later eventually</p>
<h2>Synopsis</h2>
<pre><code>int snd_card_free_when_closed(struct snd_card *card);</code></pre>
<h2>Arguments</h2>
<p><i>card</i></p>
<dl>
<dd>
<dd>soundcard structure</dl>
<h2>Description</h2>
<p>Unlike <code>snd_card_free</code>, this function doesn&#8217;t try to release the card resource immediately, but tries to disconnect at first. When the card is still in use, the function returns before freeing the resources. The card resources will be freed when the refcount gets to zero.</p>
<h2>Copyright</h2>
