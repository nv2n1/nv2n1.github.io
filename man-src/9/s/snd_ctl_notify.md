---
title: "snd_ctl_notify(9)"
name: "snd_ctl_notify"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ctl_notify/"
---

snd_ctl_notify - Send notification to user-space for a control change

<h2>Synopsis</h2>

<pre><code>void snd_ctl_notify(struct snd_card *card, unsigned int mask, struct snd_ctl_elem_id *id);</code></pre>

<h2>Arguments</h2>

<i>card</i>
<dl><dd><dd>the card to send notification</dl>
 

 <i>mask</i>
<dl><dd>the event mask, SNDRV_CTL_EVENT_*</dl>
 

 <i>id</i>
<dl><dd>the ctl element id to send notification</dl>

<h2>Description</h2>

This function adds an event record with the given id and mask, appends to the list and wakes up the user-space for notification. This can be called in the atomic context.

<h2>Copyright</h2>


