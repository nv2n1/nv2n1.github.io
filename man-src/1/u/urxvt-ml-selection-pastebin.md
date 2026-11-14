---
title: "urxvt-ml-selection-pastebin(1)"
name: "urxvt-ml-selection-pastebin"
section: "1"
letter: "u"
url: "/docs/linux/man/1-urxvt-ml-selection-pastebin/"
---

<h2 class="name">NAME</h2>
 

 selection-pastebin - automatic pastebin upload 

<h2>EXAMPLES</h2>

 <pre>
  URxvt.keysym.C-M-e: selection-pastebin:remote-pastebin
</pre>

<h2>DESCRIPTION</h2>

 This is a little rarely useful extension that uploads the selection as textfile to a remote site (or does other things). (The implementation is not currently secure for use in a multiuser environment as it writes to <i>/tmp</i> directly.). 

 It listens to the <tt>&quot;selection-pastebin:remote-pastebin&quot;</tt> action, which, when activated, runs a command with <tt>&quot;%&quot;</tt> replaced by the name of the textfile. This command can be set via a resource: 

 <pre>
   URxvt.selection-pastebin.cmd: rsync -apP % ruth:/var/www/<a rel="nofollow" HREF="http://www.ta-sa.org">www.ta-sa.org</a>/files/txt/.
</pre> 

 And the default is likely not useful to anybody but the few people around here :) 

 The name of the textfile is the hex encoded md5 sum of the selection, so the same content should lead to the same filename. 

 After a successful upload the selection will be replaced by the text given in the <tt>&quot;selection-pastebin-url&quot;</tt> resource (again, the % is the placeholder for the filename): 

 <pre>
   URxvt.selection-pastebin.url: <a rel="nofollow" HREF="http://www.ta-sa.org/files/txt/%">http://www.ta-sa.org/files/txt/%</a>
</pre> 

 <i>Note to xrdb users:</i> xrdb uses the C preprocessor, which might interpret the double <tt>&quot;/&quot;</tt> characters as comment start. Use <tt>&quot;\057\057&quot;</tt> instead, which works regardless of whether xrdb is used to parse the resource file or not. 

<h2>Index</h2>


