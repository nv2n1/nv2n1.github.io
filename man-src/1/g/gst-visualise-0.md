---
title: "gst-visualise-0(1)"
name: "gst-visualise-0"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gst-visualise-0/"
description: "gst-visualise – Run a GStreamer pipeline to display an audio visualisation"
---

<h2 class="name">NAME</h2>
<p> gst-visualise &#8211; Run a GStreamer pipeline to display an audio visualisation </p>
<h2>SYNOPSIS</h2>
<p> <code>gst-visualise</code> <i>[visualiser]</i></p>
<h2>DESCRIPTION</h2>
<p> <i>gst-visualise</i> is a tool that is used to run a basic <i>GStreamer</i> pipeline, to display a graphical visualisation of an audio stream. </p>
<p> By default, the audio stream is read from ESD (the Enlightened Sound Daemon), but this can be changed by setting the AUDIOSRC parameter in ~/.gst. For example, you might set &quot;AUDIOSRC=osssrc&quot; to display a visualisation of the sound input to your soundcard. </p>
<p> You can select a visualiser by providing a parameter naming the visualiser. For example: </p>
<p>&nbsp;<wbr>gst-visualise synaesthesia </p>
<p> will use the synaesthesia plugin. If no visualiser is named, the VISUALIZER property in ~/.gst will be used. If this is not specified either, the goom visualiser will be used. </p>
<p> The videosink to use to display the visualisation will be read from the VIDEOSINK parameter in ~/.gst, defaulting to sdlvideosink. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gst-launch-ext/">gst-launch-ext</a></code>(1), <code><a href="/docs/linux/man/1-gst-inspect/">gst-inspect</a></code>(1), <code><a href="/docs/linux/man/1-gst-launch/">gst-launch</a></code>(1),</p>
<h2>AUTHOR</h2>
<p> The GStreamer team at <a rel="nofollow" href="http://gstreamer.net/">http://gstreamer.net/</a> </p>
<h2>Index</h2>
