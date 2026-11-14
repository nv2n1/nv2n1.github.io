---
title: "lsdahdi(8)"
name: "lsdahdi"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lsdahdi/"
---

lsdahdi - List all dahdi channels with their types and spans.

<h2>Synopsis</h2>

lsdahdi

<h2>Description</h2>

Example output: 

 <pre> ### Span 1: WCTDM/0 &quot;Wildcard TDM400P REV E/F Board 1&quot;
 1 FXO FXOLS (In use)
 2 FXS FXSKS
 3 FXS FXSKS
 4 FXS FXSKS
 ### Span 2: XBUS-00/XPD-00 &quot;Xorcom XPD #00/00: FXO&quot;
 5 FXO FXSKS (In use)
 6 FXO FXSKS (In use) (no pcm)
 7 FXO FXSKS (In use) (no pcm)
 8 FXO FXSKS (In use) (no pcm)
 9 FXO FXSKS (In use) (no pcm)
 10 FXO FXSKS (In use) (no pcm)
 11 FXO FXSKS (In use) (no pcm)
 12 FXO FXSKS (In use) (no pcm)
 ### Span 3: XBUS-00/XPD-10 &quot;Xorcom XPD #00/10: FXO&quot;
 13 FXO FXSKS (In use) (no pcm)
 14 FXO FXSKS (In use) (no pcm)
 15 FXO FXSKS (In use) (no pcm)
 16 FXO FXSKS (In use) (no pcm)
 17 FXO FXSKS (In use) (no pcm)
 18 FXO FXSKS (In use) (no pcm)
 19 FXO FXSKS (In use) (no pcm)
 20 FXO FXSKS (In use) (no pcm)
 ...
 ### Span 6: XBUS-01/XPD-00 &quot;Xorcom XPD #01/00: FXS&quot;
 37 FXS FXOLS (In use)
 38 FXS FXOLS (In use) (no pcm)
 39 FXS FXOLS (In use) (no pcm)
 40 FXS FXOLS (In use) (no pcm)
 41 FXS FXOLS (In use) (no pcm)
 42 FXS FXOLS (In use) (no pcm)
 43 FXS FXOLS (In use) (no pcm)
 44 FXS FXOLS (In use) (no pcm)
 45 Output FXOLS (In use) (no pcm)
 46 Output FXOLS (In use) (no pcm)
 47 Input FXOLS (In use) (no pcm)
 48 Input FXOLS (In use) (no pcm)
 49 Input FXOLS (In use) (no pcm)
 50 Input FXOLS (In use) (no pcm)</pre>The first column is the type of the channel (port, for an analog device) and the second one is the signalling (if set).

<h2>Files</h2>

lsdahdi is a somewhat glorified 'cat /proc/dahdi/*' . Unlike that command, it sorts the spans with the proper order. It also formats the output slightly differently.
