---
title: "sndrv_compress_ioctl_version(9)"
name: "sndrv_compress_ioctl_version"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sndrv_compress_ioctl_version/"
description: "SNDRV_COMPRESS_IOCTL_VERSION –"
---

<p>SNDRV_COMPRESS_IOCTL_VERSION &#8211;</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>SNDRV_COMPRESS_IOCTL_VERSION(void);</code></dl>
<h2>Arguments</h2>
<dd>None</p>
<h2>Description</h2>
<p>SNDRV_COMPRESS_GET_CAPS: Query capability of DSP SNDRV_COMPRESS_GET_CODEC_CAPS: Query capability of a codec SNDRV_COMPRESS_SET_PARAMS: Set codec and stream parameters</p>
<h2>Note</h2>
<p>only codec params can be changed runtime and stream params cant be SNDRV_COMPRESS_GET_PARAMS: Query codec params SNDRV_COMPRESS_TSTAMP: get the current timestamp value SNDRV_COMPRESS_AVAIL: get the current buffer avail value. This also queries the tstamp properties SNDRV_COMPRESS_PAUSE: Pause the running stream SNDRV_COMPRESS_RESUME: resume a paused stream SNDRV_COMPRESS_START: Start a stream SNDRV_COMPRESS_STOP: stop a running stream, discarding ring buffer content and the buffers currently with DSP SNDRV_COMPRESS_DRAIN: Play till end of buffers and stop after that SNDRV_COMPRESS_IOCTL_VERSION: Query the API version</p>
<h2>Copyright</h2>
