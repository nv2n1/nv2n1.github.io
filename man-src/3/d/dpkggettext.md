---
title: "dpkggettext(3)"
name: "dpkggettext"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkggettext/"
---

Dpkg::Gettext - convenience wrapper around Locale::gettext 

<h2>Description</h2>The Dpkg::Gettext module is a convenience wrapper over the Locale::gettext module, to guarantee we always have working gettext functions, and to add some commonly used aliases.
<h2>Functions</h2><dl COMPACT><dt>my $trans = _g($msgid)
<dd>Calls <i>gettext()</i> on the <tt>$msgid</tt> and returns its translation for the current locale. If <i>gettext()</i> is not available, simply returns <tt>$msgid</tt>.
<dt>my $trans = P_($msgid, $msgid_plural, $n)
<dd>Calls <i>ngettext()</i>, returning the correct translation for the plural form dependent on <tt>$n</tt>. If <i>gettext()</i> is not available, returns <tt>$msgid</tt> if <tt>$n</tt> is 1 or <tt>$msgid_plural</tt> otherwise.</dl><h2>Changes</h2><h3>Version 1.00</h3>Mark the module as public.
