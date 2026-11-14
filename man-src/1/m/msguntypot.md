---
title: "msguntypot(1)"
name: "msguntypot"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msguntypot/"
---

<h2 class="name">NAME</h2>
 

 msguntypot - update po files when a typo is fixed in pot file 

<h2>SYNOPSIS</h2>

 msguntypot -o &lt;old_pot&gt; -n &lt;new_pot&gt; pofiles...

<h2>DESCRIPTION</h2>

 When you fix a trivial error which surely doesn't affect translations (e.g. a typo) in a .pot file, you should unfuzzy the corresponding msgstr in the translated .po files to avoid so extra work to the translators. 

 This task is difficult and error prone when done manually, and this tool is there to help doing so correctly. You just need to provide the two versions of the pot file: before the edition and after as marked in the above synopsis, and it all becomes automatic.

<h2>HOW TO USE IT</h2>

 In short, when you discover a typo in one of your [english] message, do the following:
<dl>
<dt>- Regenerate your pot and po files.
<dd> <pre>
  make -C po/ update-po # for message program translations
  debconf-updatepo      # for debconf translations
  po4a po4a.conf        # for po4a based documentation translations
</pre> 

 or something else, depending on your project's building settings. You know how to make sure your pot an po files are uptodate, don't you??
<dt>- Make a copy of your pot file.
<dd> <pre>
  cp myfile.pot myfile.pot.orig
</pre>
<dt>- Make a copy of all your files.
<dd> <pre>
  mkdir po_fridge; cp *.po po_fridge
</pre>
<dt>- Fix your typo
<dd> <tt>$EDITOR</tt> the_file_in_which_there_is_a_typo
<dt>- Regenerate your pot and po files.
<dd> See above.</dl>
 

 At this point, the typo fix fuzzied all the translations, and this unfortunate change is the only one between the po files of your main directory and the one from the fridge. Here is how to solve this.
<dl>
<dt>- Discard fuzzy translation, restore the ones from the fridge.
<dd> <pre>
  cp po_fridge/*.po .
</pre>
<dt>- Manually merge the po files with the new pot file, but taking the useless fuzzy into account
<dd> <pre>
  msguntypot -o myfile.pot.orig -n myfile.pot *.po
</pre>
<dt>- Cleanups.
<dd> <pre>
  rm -rf myfile.pot.orig po_fridge
</pre></dl>
 

 You're done. The typo was eradicated from msgstr of both your pot and po files, and the po files were not fuzzyied in the process. Your translators love you already.

<h2>SEE ALSO</h2>

 Despite its name, this tool is not part of the gettext tool suite. It is instead part of po4a. More precisely, it's a random perl script using the fine po4a modules. For more information about po4a, please see: 

 <i><a HREF="/docs/linux/man/7-po4a/">po4a</a></i>(7).

<h2>AUTHORS</h2>

 <pre>
 Martin Quinson (mquinson#debian,org)
</pre>

<h2>COPYRIGHT AND LICENSE</h2>

 Copyright 2005 by <font SIZE="-1">SPI</font>, inc. 

 This program is free software; you may redistribute it and/or modify it under the terms of <font SIZE="-1">GPL</font> (see the <font SIZE="-1">COPYING</font> file). 

<h2>Index</h2>


