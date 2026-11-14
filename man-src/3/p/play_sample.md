---
title: "play_sample(3)"
name: "play_sample"
section: "3"
letter: "p"
url: "/docs/linux/man/3-play_sample/"
description: "play_sample – Plays a sample. Allegro game programming library."
---

<p>play_sample &#8211; Plays a sample. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int play_sample(const SAMPLE *spl, int vol, int pan, int freq, int loop);</code></pre>
<h2>Description</h2>
<p>Triggers a sample at the specified volume, pan position, and frequency. The parameters `vol&#8217; and `pan&#8217; range from 0 (min/left) to 255 (max/right). Frequency is relative rather than absolute: 1000 represents the frequency that the sample was recorded at, 2000 is twice this, etc. If `loop&#8217; is not zero, the sample will repeat until you call stop_sample(), and can be manipulated while it is playing by calling adjust_sample(). Example: </p>
<pre><code>/* Scream from the left speaker, twice the freq. */
int sound = play_sample(scream, 255, 0, 2000, 0);</code></pre>
<h2>Return Value</h2>
<p>Returns the voice number that was allocated for the sample or negative if no voices were available. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-install_sound/">install_sound</a></code>(3), <code><a href="/docs/linux/man/3-load_sample/">load_sample</a></code>(3), <code><a href="/docs/linux/man/3-adjust_sample/">adjust_sample</a></code>(3), <code><a href="/docs/linux/man/3-stop_sample/">stop_sample</a></code>(3), <code><a href="/docs/linux/man/3-exsample/">exsample</a></code>(3), <code><a href="/docs/linux/man/3-exsprite/">exsprite</a></code>(3) </p>
