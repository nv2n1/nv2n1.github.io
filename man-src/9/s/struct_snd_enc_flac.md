---
title: "struct_snd_enc_flac(9)"
name: "struct_snd_enc_flac"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_snd_enc_flac/"
---

struct_snd_enc_flac -

<h2>Synopsis</h2>

<pre><code>struct snd_enc_flac {
    __u32 num;
    __u32 gain;
};</code></pre>

<h2>Members</h2>

num
<dl><dd>serial number, valid only for OGG formats needs to be set by application</dl>
 

 gain
<dl><dd>Add replay gain tags</dl>

<h2>Description</h2>

These options were extracted from the FLAC online documentation at <a rel="nofollow" HREF="http://flac.sourceforge.net/documentation_tools_flac.html">http://flac.sourceforge.net/documentation_tools_flac.html</a> 

 To make the API simpler, it is assumed that the user will select quality profiles. Additional options that affect encoding quality and speed can be added at a later stage if needed. 

 By default the Subset format is used by encoders. 

 TAGS such as pictures, etc, cannot be handled by an offloaded encoder and are not supported in this API.

<h2>Copyright</h2>


